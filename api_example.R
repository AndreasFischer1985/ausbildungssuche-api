##################
# Simple Example
##################

install.packages(c("devtools","jsonlite","httr"))
devtools::install_github("AndreasFischer1985/qqBaseX")
clientId="infosysbub-absuche"
url="https://rest.arbeitsagentur.de/infosysbub/absuche/pc/v1/ausbildungsangebot?uk=Bundesweit&bart=101&sty=0"
data_request=httr::GET(url=url, httr::add_headers(.headers=c("X-API-Key"=clientId)),
        config=httr::config(connecttimeout=60))
data=jsonlite::fromJSON(rawToChar(httr::content(data_request)))

writeLines(jsonlite::toJSON(data$aggregations,pretty=TRUE,auto_unbox=TRUE),paste0(Sys.Date(),"_absuche_bart101_aggregations.json"))

data$aggregations$ANZAHL_GESAMT
data$aggregations$REGIONEN

