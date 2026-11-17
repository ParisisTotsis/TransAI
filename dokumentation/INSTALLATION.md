# Installation unter macOS / VS Code

Siehe `README.md` für die Schritt-für-Schritt-Anleitung. Entwicklungsumgebung: Python 3.11 oder 3.12, separate virtuelle Umgebung `.venv`. Alle Befehle im Projektordner ausführen:

```bash
bash SETUP_MAC.command
./.venv/bin/python -m pytest -q
./.venv/bin/python -m streamlit run app.py --server.address 127.0.0.1
```

**Modellquellen:** `Helsinki-NLP/opus-mt-de-en` und `Helsinki-NLP/opus-mt-de-fr`. Bei Erstverwendung Online-Download der Gewichte; danach Cache. Die ZIP enthält aus Platzgründen keine Modellgewichte. Versionsnachweis über `./.venv/bin/python skripte/versionen_sichern.py`. Echtes Modellverhalten ist auf dem Zielrechner zu überprüfen und zu protokollieren.
