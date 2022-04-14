# Arbeitsagentur Ausbildungssuche API 
Die Bundesagentur für Arbeit verfügt über eine der größten Datenbanken für Ausbildungsangebote in Deutschland. Obwohl sie vollständig staatlich ist und es sich dabei um einen sehr spannenden Basisdatensatz handelt, mit dem viele Analysen möglich wären, bietet die Bundesagentur für Arbeit dafür bis heute keine offizielle API an.


## Authentifizierung
Die Authentifizierung funktioniert per OAuth 2 Client Credentials mit JWTs.
Client Credentials sind, wie beispielsweise einem GET-request an https://web.arbeitsagentur.de/ausbildungssuche/berufsausbildung-suche zu entnehmen ist, folgende:

**ClientID:** 1c852184-1944-4a9e-a093-5cc078981294

**ClientSecret:** 777f9915-9f0d-4982-9c33-07b5810a3e79

```bash
curl \
-H 'Host: rest.arbeitsagentur.de' \
-H 'Accept: */*' \
-H 'Content-Type: application/x-www-form-urlencoded; charset=utf-8' \
-H 'Accept-Language: de,en-US;q=0.7,en;q=0.3' \
-H 'User-Agent:  Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:88.0) Gecko/20100101 Firefox/88.0' \
--data-binary "client_id=1c852184-1944-4a9e-a093-5cc078981294&client_secret=777f9915-9f0d-4982-9c33-07b5810a3e79&grant_type=client_credentials" \
--compressed 'https://rest.arbeitsagentur.de/oauth/gettoken_cc'
```

Der generierte Token muss bei folgenden GET-requests an https://rest.arbeitsagentur.de/infosysbub/absuche/pc/v1/ausbildungsangebot im header als 'OAuthAccessToken' inkludiert werden.


## Ausbildungssuche

**URL:** https://rest.arbeitsagentur.de/infosysbub/absuche/pc/v1/ausbildungsangebot
	

Die Ausbildungssuche ermöglicht verfügbare Angebote mit dem Ziel einer Berufsausbildung, Schulabschluss, Ausbildungsvorbereitung oder -begleitung mit verschiedenen GET-Parametern zu filtern:


### Filter


**Parameter:** *sty*  (Optional)
- 0
- 1
- 2
- 3

sty: 0=Berufsausbildung; 1=Schulabschluss; 2=Vorbereitung auf Aus- und Weiterbildung oder berufliche Tätigkeit; 3=Begleitende Hilfen.


**Parameter:** *ids*  (Optional)

Berufs-ID einer Berufsbezeichnung (z.B. 2927 für IT-System-Elektroniker/innen). Mehrere Komma-getrennte Angaben möglich.


**Parameter:** *orte*  (Optional)

ID für Orte (z.B. 38450 für den Ort Feucht). Mehrere Komma-getrennte Angaben möglich.


**Parameter:** *page* (Optional)

Seite (beginnend mit 0).


**Parameter:** *uk* (Optional)
- Bundesweit
- 25
- 50
- 100
- 150
- 200

Umkreis:  Bundesweit=Bundesweit, 25=25 km, 50=50 km, 100=100 km, 150=150 km, 200=200 km.

**Parameter:** *re*  (Optional)
- BW
- BY
- BE
- BB
- HB
- HH
- HE
- MV
- NI
- NW
- RP
- SL
- SN
- ST
- SH
- TH

Region/Bundesland: BW=Bade-Württemberg, BY=Bayern, BE=Berlin, BB=Brandenburg, HB=Bremen, HH=Hamburg, HE=Hessen, MV=Mecklenburg-Vorpommern, NI=Niedersachsen, NW=Nordrhei-Westfalen, RP=Rheinland-Pfalz, SL=Saarland, SN=Sachsen, ST=Sachsen-Anhalt, SH=Schleswig-Holstein, TH=Thüringen. Mehrere Komma-getrennte Angaben möglich (z.B. re=TH,BW).

**Parameter:** *bt* (Optional)
- 2
- 101
- 102
- 103
- 104
- 105
- 106
- 107
- 108
- 109
- 110
- 111
- 112

Beginntermin: 2=frühere Termine, 101=Januar des Folgejahres, 102=Februar des Folgejahres, 103=März des Folgejahres, 104=April des Folgejahres, 105=Mai des Folgejahres, 106=Juni des Folgejahres, 107=Juli des Folgejahres, 108=August des Folgejahres, 109=September des Folgejahres, 110=Oktober des Folgejahres, 111=November des Folgejahres, 112=Dezember des Folgejahres. Mehrere Komma-getrennte Angaben möglich.


**Parameter:** *bart* (Optional)
- 101
- 102
- 105
- 109

Ausbildungstyp: 101=Teilqualifizierung, 102=Berufsausbildung, 105=Abschluss nachholen, 109=Umschulung


**Parameter:** *ityp* (Optional)
- 1
- 2

Integrationstyp: 0=Ausbildung Reha, 1=weiterbildung Reha. Mehrere Komma-getrennte Angaben möglich (z.B. ityp=0,1).


**Parameter:** *ban* (Optional)
Bildungsanbieter-ID (z.B. 465). 


**Parameter:** *bg* (Optional)
- true
- false

Bildungsgutschein: true=nur Angebote mit Zulassung zur Förderung mit Bildungsgutschein anzeigen, false=nicht nur Angebote mit Zulassung zur Förderung mit Bildungsgutschein anzeigen.


### Beispiel:

```bash
wb=$(curl -m 60 -H "Host: rest.arbeitsagentur.de" \
-H "User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:88.0) Gecko/20100101 Firefox/88.0" \
-H "Accept: application/json, text/plain, */*" \
-H "Accept-Language: de,en-US;q=0.7,en;q=0.3" \
-H "Accept-Encoding: gzip, deflate, br" \
-H "Origin: https://web.arbeitsagentur.de" \
-H "DNT: 1" \
-H "Connection: keep-alive" \
-H "Pragma: no-cache" \
-H "Cache-Control: no-cache" \
-H "OAuthAccessToken: $token" \
'https://rest.arbeitsagentur.de/infosysbub/absuche/pc/v1/ausbildungsangebot?ids=2927&bg=false&page=0')
```
