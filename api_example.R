#----------------
# Simple Example
#----------------
install.packages(c("devtools","jsonlite","httr"))
devtools::install_github("AndreasFischer1985/qqBaseX")
clientId="1c852184-1944-4a9e-a093-5cc078981294"
clientSecret="777f9915-9f0d-4982-9c33-07b5810a3e79"
postData=list( "grant_type"="client_credentials","client_id"=clientId,"client_secret"=clientSecret) 
token_request=httr::POST(
        url="https://rest.arbeitsagentur.de/oauth/gettoken_cc",
        body=postData,encode="form",
        config=httr::config(connecttimeout=60))
token=(httr::content(token_request, as='parsed')$access_token)
url="https://rest.arbeitsagentur.de/infosysbub/absuche/pc/v1/ausbildungsangebot?uk=Bundesweit&bart=101&sty=0"
data_request=httr::GET(url=url, httr::add_headers(.headers=c("OAuthAccessToken"=token)),
        config=httr::config(connecttimeout=60))
data=jsonlite::fromJSON(rawToChar(httr::content(data_request)))

writeLines(jsonlite::toJSON(data$aggregations,pretty=TRUE,auto_unbox=TRUE),paste0(Sys.Date(),"_absuche_bart101_aggregations.json"))

data$aggregations$ANZAHL_GESAMT
data$aggregations$REGIONEN

#--------------------
# Get data by region
#--------------------

t1=print(Sys.time())
url="https://rest.arbeitsagentur.de/infosysbub/absuche/pc/v1/ausbildungsangebot?bart=101&sty=0"
completeData=lapply(sort(gsub("TH.*","TH%C3%9C",names(data$aggregations$REGIONEN)),decreasing=T),function(bl){
        print(paste0("start with ",bl));
	dataL=jsonlite::fromJSON(rawToChar(httr::content(httr::GET(url=paste0(url,"&re=",bl), 
			httr::add_headers(.headers=c("OAuthAccessToken"=token)),
        		config=httr::config(connecttimeout=60)))))
	maxPage=ceiling(dataL$"aggregations"$"ANZAHL_GESAMT"$COUNT/20)
	lapply(0:maxPage,function(i){
       	 	print(paste0("BL=",bl,"; ",i,"/",maxPage));
		jsonlite::fromJSON(rawToChar(httr::content(httr::GET(url=paste0(url,"&page=",i,"&re=",bl), 
			httr::add_headers(.headers=c("OAuthAccessToken"=token)),
        		config=httr::config(connecttimeout=60)))))
	})
})
t2=print(Sys.time())
print(t2-t1)

save.image(paste0(Sys.Date(),"_absuche_bart101_workspace.RData"))


#---------------------
# Plot data by region
#---------------------

koordinaten=sapply(1:length(completeData),function(bl)
	sapply(1:length(completeData[[bl]]),function(page)completeData[[bl]][[page]][["_embedded"]][["termine"]][["adresse"]][["ortStrasse"]][["koordinaten"]]))
x=do.call(rbind,lapply(koordinaten,function(x)do.call(rbind,x)))

library(ggplot2)
library(raster)
if(!exists("germany"))
	germany <- raster::getData(country = "Germany", level = 1) 
dat=data.frame(x)
colnames(dat)=c("LAT","LON") 
spatial_dat=dat
coordinates(spatial_dat) <- ~LON+LAT
proj4string(spatial_dat) <- proj4string(germany)
spatial_dat=sp:::over(spatial_dat, germany , fn = NULL) 
dat=dat[!is.na(spatial_dat[,"GID_0"]),] # select data of TQs in Germany
dim(dat) #  26254 in Germany
length(table(paste(dat$LAT,dat$LON))) # 585 different coordinates
table(spatial_dat[,"GID_0"],useNA="always")
sort(table(spatial_dat[,"NAME_1"],useNA="always"))
labels=NULL 
if(T){ # generate a data.frame for labels and aggregated data
	labels=data.frame(coordinates(germany),germany,(table(spatial_dat[,"NAME_1"],useNA="always"))[germany$NAME_1])
	labels$Freq[is.na(labels$Freq)]=0
	set.seed(0)
	#dat$LAT=jitter(dat$LAT)
	#dat$LON=jitter(dat$LON)
	colnames(labels)[1:2]=c("long","lat")
	labels[,"HASC_1"]=gsub("DE.","",labels[,"HASC_1"])
	w=which(labels[,"HASC_1"]=="BR")
	labels[w,"lat"]=labels[w,"lat"]-0.4
	w=which(labels[,"HASC_1"]=="HH"|labels[,"HASC_1"]=="HB"|labels[,"HASC_1"]=="BE")
	labels[w,"lat"]=labels[w,"lat"]+0.2
}
if(T){ add feature to Polygon-element
	library(dplyr)
	germany$Freq=labels$Freq
	gertab <- fortify(germany) 
	gislayerdata <- mutate(as.data.frame(germany), id = rownames(data.frame(germany)) ) 
	gertab <- inner_join(gertab, gislayerdata, "id")
}
dev.new();
ggplot() +
  geom_polygon(data=gertab,
               aes(x=long, y=lat, group=group, fill=Freq),
	       colour='black'
               ) +
  geom_point(data=dat,
             aes(x=LON, y=LAT),  
	     colour="darkblue",
             alpha=.5,
             size=1.5) +
  geom_text(data=labels, 
	     aes(x=long, y=lat, label=HASC_1),
             alpha=.5, 
	     size=3, 
             fontface="bold",col="white")+
  coord_map() +
  theme_void() +
  xlab("Longitude") + ylab("Latitude") +
  labs(
	fill="Angebote\nje Bundesland") +
  scale_fill_gradient(low= "white", high= rgb(0/255, 50/255, 100/255))+
  ggtitle('Teilqualifikationen in Deutschland',
	subtitle =paste(dim(dat)[1],"Angebote an",length(table(paste(dat$LAT,dat$LON))),"Orten (Stand: 06.11.2022)"))

		 
