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

t1=print(Sys.time())
url="https://rest.arbeitsagentur.de/infosysbub/absuche/pc/v1/ausbildungsangebot?bart=101&sty=0"
completeData=lapply(sort(gsub("THÜ","TH%C3%9C",names(data$aggregations$REGIONEN)),decreasing=T),function(bl){
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

