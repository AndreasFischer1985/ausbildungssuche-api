##################
# Simple Example
##################

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

######################
# Get data by region
######################

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


#######################
# Plot data by region
#######################

koordinaten=sapply(1:length(completeData),function(bl)
	sapply(1:length(completeData[[bl]]),function(page)completeData[[bl]][[page]][["_embedded"]][["termine"]][["adresse"]][["ortStrasse"]][["koordinaten"]]))
koordinaten=do.call(rbind,lapply(koordinaten,function(x)do.call(rbind,x)))


library(ggplot2)
library(raster)

cc=geodata::country_codes()
if(!exists("rasterDat"))
  rasterDat=geodata::elevation_30s("DEU",getwd())
terra::values(rasterDat)[terra::values(rasterDat)<0]=0
g0=ggplot2::ggplot() +
    tidyterra::geom_spatraster(data = rasterDat)+
    tidyterra::scale_fill_hypso_tint_c(
      limits = c(0,3000),
      palette = "wiki-2.0_hypso" 
    ) +
    #ggplot2::labs(fill="Elevation")+
    #ggplot2::ggtitle("Map of Germany") +
    ggplot2::theme_minimal()

dev.new();g0;


# Data Topping 
#-------------

if(!exists("germany"))
	germany <- raster::getData(country = "Germany", level = 1) 
dat=data.frame(koordinaten)
colnames(dat)=c("LAT","LON") 
udat=apply(dat,1,function(x)paste(x,collapse=";"))
udat=sort(table(udat))
udat=data.frame(
	LAT=as.numeric(gsub(";.*","",names(udat))),
	LON=as.numeric(gsub(".*;","",names(udat))),
        NUM=as.numeric(udat))
udat=udat[udat[,"LAT"]!=0&udat[,"LON"]!=0,]
sp::coordinates(udat) <- ~LON+LAT
sp::proj4string(udat) <- sp::proj4string(germany)
udat=data.frame(udat,sp:::over(udat, germany , fn = NULL)) # locate udat-coordinates in Germany
udat=udat[!is.na(udat[,"GID_0"]),] # remove udat-entries outside of Germany
table(udat[,"GID_0"],useNA="always")

germany$Freq=(table(udat[,"NAME_1"],useNA="always"))[germany$NAME_1]#
germany$Freq[is.na(labels$Freq)]=0
germany$Label=gsub("DE.","",labels[,"HASC_1"])
germany$LON=sp::coordinates(germany)[,1]
germany$LAT=sp::coordinates(germany)[,2]
w=which(germany$Label=="BR");germany$LAT[w]=germany$LAT[w]-0.4
w=which(germany$Label=="HH"|germany$Label=="BE");germany$LAT[w]=germany$LAT[w]+0.2

#invisible(lapply(1:16,function(i){germany@polygons[[i]]@"labpt"=c(germany$LON,germany$LON)}))

g1=g0+
  ggplot2::geom_polygon(data=germany, # borders of 16 countries
               ggplot2::aes(x=long, y=lat, group=group),
               fill=NA,
	       colour=rgb(1,1,1,1))+
  ggplot2::geom_point(data=udat, # white underground for udat-entries
             ggplot2::aes(x=LON, y=LAT,size=NUM),  
	     colour="white",
             alpha=1)+
  ggplot2::geom_point(data=udat, # darkblue udat-entries
             ggplot2::aes(x=LON, y=LAT,size=NUM),  
	     colour="darkblue",
             alpha=.5)+
  ggplot2::geom_text(data=(germany@data), # country-Labels 
	     ggplot2::aes(x=LON, y=LAT, label=Label),
             alpha=.8, 
	     size=3, 
             fontface="bold",col="black")+
  ggplot2::xlab("") + ggplot2::ylab("") +
  ggplot2::guides(fill="none")+
  ggplot2::labs(size="TQ-Angebote")+ 
  ggplot2::ggtitle('Teilqualifikationen in Deutschland',
	subtitle =paste(sum(udat[,"NUM"]),"Angebote an",dim(udat),"Orten"))

dev.new();g1

ggplot2::ggsave("TQMapOfGermany.png")

