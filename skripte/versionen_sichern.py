"""Schreibt die tatsaechlich installierten Paketversionen in eine Datei."""
import subprocess
import sys
from pathlib import Path

result = subprocess.run([sys.executable, "-m", "pip", "freeze"], capture_output=True, text=True, check=True)
out = Path(__file__).resolve().parents[1] / "installierte_versionen.txt"
out.write_text(f"Python: {sys.version.split()[0]}\n\n" + result.stdout, encoding="utf-8")
print(f"Gespeichert: {out}")
