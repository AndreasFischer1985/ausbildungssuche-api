# ausbildungssuche.DefaultApi

All URIs are relative to *https://rest.arbeitsagentur.de/infosysbub/absuche*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ausbildungssuche**](DefaultApi.md#ausbildungssuche) | **GET** /pc/v1/ausbildungsangebot | Ausbildungssuche


# **ausbildungssuche**
> Response ausbildungssuche()

Ausbildungssuche

Die Ausbildungssuche ermöglicht verfügbare Angebote mit dem Ziel einer Berufsausbildung, Schulabschluss, Ausbildungsvorbereitung oder -begleitung mit verschiedenen GET-Parametern zu filtern.

### Example

* OAuth Authentication (clientCredAuth):

```python
import time
from deutschland import ausbildungssuche
from deutschland.ausbildungssuche.api import default_api
from deutschland.ausbildungssuche.model.response import Response
from pprint import pprint
# Defining the host is optional and defaults to https://rest.arbeitsagentur.de/infosysbub/absuche
# See configuration.py for a list of all supported configuration parameters.
configuration = ausbildungssuche.Configuration(
    host = "https://rest.arbeitsagentur.de/infosysbub/absuche"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: clientCredAuth
configuration = ausbildungssuche.Configuration(
    host = "https://rest.arbeitsagentur.de/infosysbub/absuche"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with ausbildungssuche.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    sty = 0 # int | sty - 0=Berufsausbildung; 1=Schulabschluss; 2=Vorbereitung auf Aus- und Weiterbildung oder berufliche Tätigkeit; 3=Begleitende Hilfen. (optional)
    ids = 2927 # int | Berufs-ID einer Berufsbezeichnung. Mehrere Komma-getrennte Angaben möglich. (optional)
    orte = 38450 # int | ID eines Ortes. Mehrere Komma-getrennte Angaben möglich. (optional)
    page = 0 # int | Ergebnissseite (optional)
    uk = "Bundesweit" # str | Umkreis - Bundesweit=Bundesweit, 25=25 km, 50=50 km, 100=100 km, 150=150 km, 200=200 km. (optional)
    re = "BY" # str | Region/Bundesland - BW=Baden-Württemberg, BY=Bayern, BE=Berlin, BB=Brandenburg, HB=Bremen, HH=Hamburg, HE=Hessen, MV=Mecklenburg-Vorpommern, NI=Niedersachsen, NW=Nordrhei-Westfalen, RP=Rheinland-Pfalz, SL=Saarland, SN=Sachsen, ST=Sachsen-Anhalt, SH=Schleswig-Holstein, TH=Thüringen. Mehrere Komma-getrennte Angaben möglich. (optional)
    bart = 102 # int | Ausbildungstyp - 101=Teilqualifizierung, 102=Berufsausbildung, 105=Abschluss nachholen, 109=Umschulung (optional)
    ityp = 0 # int | Integrationstyp - 0=Ausbildung Reha, 1=weiterbildung Reha. Mehrere Komma-getrennte Angaben möglich. (optional)
    bt = 2 # int | Beginntermin - 2=frühere Termine, 101=Januar des Folgejahres, 102=Februar des Folgejahres, 103=März des Folgejahres, 104=April des Folgejahres, 105=Mai des Folgejahres, 106=Juni des Folgejahres, 107=Juli des Folgejahres, 108=August des Folgejahres, 109=September des Folgejahres, 110=Oktober des Folgejahres, 111=November des Folgejahres, 112=Dezember des Folgejahres. Mehrere Komma-getrennte Angaben möglich. (optional)
    ban = 465 # int | Bildungsanbieter-ID. Mehrere Komma-getrennte Angaben möglich. (optional)
    bg = True # bool | Bildungsgutschein - true=nur Angebote mit Zulassung zur Förderung mit Bildungsgutschein anzeigen, false=nicht nur Angebote mit Zulassung zur Förderung mit Bildungsgutschein anzeigen. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Ausbildungssuche
        api_response = api_instance.ausbildungssuche(sty=sty, ids=ids, orte=orte, page=page, uk=uk, re=re, bart=bart, ityp=ityp, bt=bt, ban=ban, bg=bg)
        pprint(api_response)
    except ausbildungssuche.ApiException as e:
        print("Exception when calling DefaultApi->ausbildungssuche: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sty** | **int**| sty - 0&#x3D;Berufsausbildung; 1&#x3D;Schulabschluss; 2&#x3D;Vorbereitung auf Aus- und Weiterbildung oder berufliche Tätigkeit; 3&#x3D;Begleitende Hilfen. | [optional]
 **ids** | **int**| Berufs-ID einer Berufsbezeichnung. Mehrere Komma-getrennte Angaben möglich. | [optional]
 **orte** | **int**| ID eines Ortes. Mehrere Komma-getrennte Angaben möglich. | [optional]
 **page** | **int**| Ergebnissseite | [optional]
 **uk** | **str**| Umkreis - Bundesweit&#x3D;Bundesweit, 25&#x3D;25 km, 50&#x3D;50 km, 100&#x3D;100 km, 150&#x3D;150 km, 200&#x3D;200 km. | [optional]
 **re** | **str**| Region/Bundesland - BW&#x3D;Baden-Württemberg, BY&#x3D;Bayern, BE&#x3D;Berlin, BB&#x3D;Brandenburg, HB&#x3D;Bremen, HH&#x3D;Hamburg, HE&#x3D;Hessen, MV&#x3D;Mecklenburg-Vorpommern, NI&#x3D;Niedersachsen, NW&#x3D;Nordrhei-Westfalen, RP&#x3D;Rheinland-Pfalz, SL&#x3D;Saarland, SN&#x3D;Sachsen, ST&#x3D;Sachsen-Anhalt, SH&#x3D;Schleswig-Holstein, TH&#x3D;Thüringen. Mehrere Komma-getrennte Angaben möglich. | [optional]
 **bart** | **int**| Ausbildungstyp - 101&#x3D;Teilqualifizierung, 102&#x3D;Berufsausbildung, 105&#x3D;Abschluss nachholen, 109&#x3D;Umschulung | [optional]
 **ityp** | **int**| Integrationstyp - 0&#x3D;Ausbildung Reha, 1&#x3D;weiterbildung Reha. Mehrere Komma-getrennte Angaben möglich. | [optional]
 **bt** | **int**| Beginntermin - 2&#x3D;frühere Termine, 101&#x3D;Januar des Folgejahres, 102&#x3D;Februar des Folgejahres, 103&#x3D;März des Folgejahres, 104&#x3D;April des Folgejahres, 105&#x3D;Mai des Folgejahres, 106&#x3D;Juni des Folgejahres, 107&#x3D;Juli des Folgejahres, 108&#x3D;August des Folgejahres, 109&#x3D;September des Folgejahres, 110&#x3D;Oktober des Folgejahres, 111&#x3D;November des Folgejahres, 112&#x3D;Dezember des Folgejahres. Mehrere Komma-getrennte Angaben möglich. | [optional]
 **ban** | **int**| Bildungsanbieter-ID. Mehrere Komma-getrennte Angaben möglich. | [optional]
 **bg** | **bool**| Bildungsgutschein - true&#x3D;nur Angebote mit Zulassung zur Förderung mit Bildungsgutschein anzeigen, false&#x3D;nicht nur Angebote mit Zulassung zur Förderung mit Bildungsgutschein anzeigen. | [optional]

### Return type

[**Response**](Response.md)

### Authorization

[clientCredAuth](../README.md#clientCredAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

