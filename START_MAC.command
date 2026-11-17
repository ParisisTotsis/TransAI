#!/bin/bash
set -euo pipefail
cd "$(dirname "$0")"
if [[ ! -x .venv/bin/python ]]; then
  echo "Installation fehlt: zuerst SETUP_MAC.command ausführen."
  read -r -p "Enter zum Schließen ..." _
  exit 1
fi
./.venv/bin/python -m streamlit run app.py --server.address 127.0.0.1
