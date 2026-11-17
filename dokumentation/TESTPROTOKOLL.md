# Testprotokoll – Phase 2

**Testumgebung:** Erstellungsumgebung Python 3.13.5, pytest 9.0.2; `streamlit` und `transformers` dort nicht installiert. Modellgewichte nicht geladen.

Die folgenden Tests betreffen ausschließlich Programmeingaben und die **simulierte** Übersetzungslogik. Sie sind **kein Nachweis** der realen Übersetzungsleistung.

| ID | Prüfung | Erwartung | Ist-Ergebnis |
|---|---|---|---|
| UT01 | Leere Eingabe | Eingabe abweisen | Siehe pytest-Ergebnis |
| UT02 | Ungültige Sprache | Eingabe abweisen | Siehe pytest-Ergebnis |
| UT03 | 3001 Zeichen | Eingabe abweisen | Siehe pytest-Ergebnis |
| UT04 | Rand-Leerzeichen | Leerzeichen entfernen | Siehe pytest-Ergebnis |
| UT05 | Modellzuordnung | de-en/de-fr korrekt | Siehe pytest-Ergebnis |
| UT06 | Übersetzen mit Mock | Simulierter Text wird zurückgegeben | Siehe pytest-Ergebnis |
| IT01 | Streamlit startet | Oberfläche erreichbar | **Nicht getestet** |
| IT02 | Echtes Modell DE → EN | Plausible Übersetzung | **Nicht getestet** |
| IT03 | Echtes Modell DE → FR | Plausible Übersetzung | **Nicht getestet** |
| IT04 | Offline nach Download | Keine Internetverbindung nötig | **Nicht getestet** |

**Ausstehend auf dem Rechner des Studierenden:** Installationsversuch mit Python 3.11/3.12; `pip freeze`; Bildschirmnachweis; reale Modelltests und qualitative Bewertung anhand fiktiver Kundenanfragen; Zeit- und RAM-Messung.
