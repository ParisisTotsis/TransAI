# TransAI – VS Code für macOS (Phase 2, Arbeitsstand)

**Ziel:** Kostenloser lokaler Übersetzungs-Demonstrator für fiktive Online-Shop-Anfragen (Deutsch → Englisch/Französisch). Python, Streamlit und lokal geladene OPUS-MT-Modelle. Keine kostenpflichtige API.

## Anleitung für Mac und VS Code

1. ZIP-Datei entpacken (Finder). In **Visual Studio Code > File > Open Folder** den Ordner `TransAI_Phase2_Mac_VSCode` öffnen.
2. Python **3.11 oder 3.12** installieren; in VS Code die Erweiterung **Python** (Microsoft) installieren. Auf Apple Silicon oder Intel installiert Python/PyTorch die jeweils passende Plattformversion, sofern verfügbar.
3. In VS Code **Terminal > New Terminal** öffnen, dann im Projektordner ausführen:

   ```bash
   chmod +x SETUP_MAC.command START_MAC.command
   ./SETUP_MAC.command
   ```

   Alternativ `SETUP_MAC.command` im Finder öffnen; macOS kann bei nicht signierten Dateien eine Sicherheitswarnung anzeigen. Ein Aufruf über das VS-Code-Terminal ist transparenter. Das Setup benötigt Internet und lädt Pakete herunter.
4. **Command + Shift + P** → `Python: Select Interpreter` → `.venv/bin/python` wählen.
5. Aus VS Code **Terminal > Run Task > TransAI: Starten (macOS)**; oder im Terminal:

   ```bash
   ./.venv/bin/python -m streamlit run app.py --server.address 127.0.0.1
   ```

6. Im Browser **http://127.0.0.1:8501** öffnen. Beim ersten Übersetzen werden die Modellgewichte heruntergeladen. Für echte lokale Offline-Nutzung sind die Modelle zunächst einmal online zu laden.

## Diagnose und Tests

```bash
./.venv/bin/python -m pytest -q
./.venv/bin/python skripte/versionen_sichern.py
```

In VS Code kann mit **F5** debuggt werden; dabei muss vorher der `.venv`-Interpreter gewählt sein. Die sechs Unit-Tests prüfen nur die modellunabhängige Logik und Mock-Übersetzungen. **Ob die echten Modelle auf deinem Mac funktionieren, ist noch nicht bestätigt.** Bitte eine echte DE→EN- und DE→FR-Übersetzung ausführen und die Ergebnisse mit Geräteangaben und installierten Versionen dokumentieren.

## Häufige Probleme

- `command not found: python3.11`: Python 3.11/3.12 installieren, danach VS Code neu starten.
- `permission denied`: `chmod +x SETUP_MAC.command START_MAC.command` ausführen.
- `ModuleNotFoundError`: sicherstellen, dass `.venv/bin/python` statt einer globalen Python-Version gewählt ist.
- Modell-Download scheitert: Internet prüfen; gegebenenfalls Download erneut versuchen. Das Modell ist nicht in der ZIP enthalten.
- Speicher / Laufzeit: erster Modellstart und CPU-Übersetzungen können auf älteren Macs langsamer sein; diese Beobachtungen später protokollieren.

## Ordnerübersicht

- `app.py` – Benutzeroberfläche
- `transai/translator.py` – Modellanbindung und Validierung
- `.vscode/` – Mac-kompatible Task-/Debug-Konfiguration
- `requirements.txt`, `requirements-dev.txt` – Bibliotheken
- `tests/` – automatisierte Unit-Tests
- `dokumentation/` – Vergleich, Installationshinweise, Testprotokoll
- `skripte/versionen_sichern.py` – Versionsnachweis

Für die spätere IU-Abgabe alle relevanten Dateien und beobachteten Ergebnisse sichern. Keine echten Kundendaten verwenden. Der Server wird nur an `127.0.0.1` gebunden. Der Code ist ein **Arbeitsstand**, keine bereits vollständig validierte Prüfungsabgabe.
