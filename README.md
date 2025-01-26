# Arbeitsagentur Ausbildungssuche API 
Die Bundesagentur für Arbeit verfügt über eine der größten Datenbanken für Ausbildungsangebote in Deutschland. Obwohl sie vollständig staatlich ist und es sich dabei um einen sehr spannenden Basisdatensatz handelt, mit dem viele Analysen möglich wären, bietet die Bundesagentur für Arbeit dafür bis heute keine offizielle API an.


## Authentifizierung

Die Authentifizierung funktioniert über die clientId der Ausbildungssuche, die einem GET-request an https://web.arbeitsagentur.de/weiterbildungssuche/suche entnommen werden kann:

**clientId:** infosysbub-absuche

Bei folgenden GET-requests ist die clientId als Header-Parameter 'X-API-Key' zu übergeben.


## Ausbildungssuche

**URL:** https://rest.arbeitsagentur.de/infosysbub/absuche/pc/v1/ausbildungsangebot
	

Die Ausbildungssuche ermöglicht verfügbare Angebote mit dem Ziel einer Berufsausbildung, Schulabschluss, Ausbildungsvorbereitung oder -begleitung mit verschiedenen GET-Parametern zu filtern:


### Filter


**Parameter:** *sty*  (Optional)
- 0
- 1
- 2
- 3
- 4

sty: 0=Berufsausbildung; 1=Schulabschluss; 2=Vorbereitung auf Aus- und Weiterbildung oder berufliche Tätigkeit; 3=Begleitende Hilfen; 4=Alle.


**Parameter:** *ids*  (Optional)

Berufs-ID einer Berufsbezeichnung (z.B. 2927 für IT-System-Elektroniker/innen). Mehrere Komma-getrennte Angaben möglich.


**Parameter:** *orte*  (Optional)

ID für Orte (z.B. 38450 für den Ort Feucht). Mehrere Komma-getrennte Angaben möglich.


**Parameter:** *page* (Optional)

Seite (beginnend mit 0).


**Parameter:** *size* (Optional)

Anzahl der Ergebnisse pro Seite (maximal 2000). Insgesamt werden über alle Seiten hinweg maximal 10000 Ergebnisse angezeigt.


**Parameter:** *uk* (Optional)
- Bundesweit
- 25
- 50
- 100
- 150
- 200

Umkreis:  Bundesweit=Bundesweit, 25=25 km, 50=50 km, 100=100 km, 150=150 km, 200=200 km.

**Parameter:** *re*  (Optional)

- BAW
- BAY
- BER
- BRA
- BRE
- HAM
- HES
- MBV
- NDS
- NRW
- RPF
- SAA
- SAC
- SAN
- SLH
- TH%C3%9C
- "-"

Region/Bundesland: BAW=Bade-Württemberg, BAY=Bayern, BER=Berlin, BRA=Brandenburg, BRE=Bremen, HAM=Hamburg, HES=Hessen, MBV=Mecklenburg-Vorpommern, NDS=Niedersachsen, NRW=Nordrhein-Westfalen, RPF=Rheinland-Pfalz, SAA=Saarland, SAC=Sachsen, SAN=Sachsen-Anhalt, SLH=Schleswig-Holstein, TH%C3%9C=Thüringen, -=überregional. Mehrere Komma-getrennte Angaben möglich (z.B. re=TH%C3%9C,BAW).

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
- 0 
- 100 
- 101
- 102
- 103 
- 104 
- 105
- 106 
- 107108
- 109

Ausbildungstyp: 0=Keine Zuordnung möglich, 100=Allgemeinbildung, 101=Teilqualifizierung, 102=Berufsausbildung, 103=Gesetzlich/gesetzesähnlich geregelte Fortbildung/Qualifizierung, 104=Fortbildung/Qualifizierung, 105=Abschluss nachholen, 106=Rehabilitation,  107108=Studienangebot - grundständig, 109=Umschulung


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
wb=$(curl -m 60 \
-H "X-API-Key: infosysbub-absuche" \
'https://rest.arbeitsagentur.de/infosysbub/absuche/pc/v1/ausbildungsangebot?bart=101&sty=0')
```
