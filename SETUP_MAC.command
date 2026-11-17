#!/bin/bash
set -euo pipefail
cd "$(dirname "$0")"
if command -v python3.11 >/dev/null 2>&1; then PY=python3.11
elif command -v python3.12 >/dev/null 2>&1; then PY=python3.12
else
  echo "Python 3.11 oder 3.12 nicht gefunden. Bitte zuerst installieren (python.org oder Homebrew)."
  read -r -p "Enter zum Beenden ..." _
  exit 1
fi
"$PY" -m venv .venv
./.venv/bin/python -m pip install --upgrade pip
./.venv/bin/python -m pip install -r requirements-dev.txt
./.venv/bin/python -m pytest -q
printf '\nInstallation abgeschlossen. Mit START_MAC.command starten oder VS Code Task nutzen.\n'
read -r -p "Enter zum Schließen ..." _
