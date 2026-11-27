"""Vérifie que les moteurs Python et JavaScript du diagnostic donnent les mêmes résultats.

Usage : python outils/tester_diagnostic.py   (demande Node.js ; lancé par la CI)
Compare, pour chaque profil de exemples/, le résultat de outils/moteur_diagnostic.py et celui
de docs/javascripts/diagnostic-moteur.js, à un centime près.
"""
import json
import subprocess
import sys
from pathlib import Path

import yaml

RACINE = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RACINE / "outils"))
from moteur_diagnostic import diagnostiquer  # noqa: E402

DONNEES = RACINE / "docs" / "assets" / "diagnostic" / "donnees.json"
MOTEUR_JS = RACINE / "docs" / "javascripts" / "diagnostic-moteur.js"
NODE = """
const m = require(process.argv[1]); const fs = require('fs');
const d = JSON.parse(fs.readFileSync(process.argv[2], 'utf8'));
const p = JSON.parse(process.argv[3]);
process.stdout.write(JSON.stringify(m.diagnostiquer(d.modele, d.valeurs, p)));
"""


def comparer(a, b, chemin="") -> list[str]:
    ecarts = []
    if isinstance(a, dict) and isinstance(b, dict):
        for k in set(a) | set(b):
            ecarts += comparer(a.get(k), b.get(k), f"{chemin}.{k}")
    elif isinstance(a, list) and isinstance(b, list):
        if len(a) != len(b):
            return [f"{chemin} : {len(a)} éléments contre {len(b)}"]
        for i, (x, y) in enumerate(zip(a, b)):
            ecarts += comparer(x, y, f"{chemin}[{i}]")
    elif isinstance(a, (int, float)) and isinstance(b, (int, float)):
        if abs(a - b) > 0.011:
            ecarts.append(f"{chemin} : {a} contre {b}")
    elif a != b:
        ecarts.append(f"{chemin} : {a!r} contre {b!r}")
    return ecarts


def main() -> int:
    donnees = json.loads(DONNEES.read_text(encoding="utf-8"))
    profils = sorted((RACINE / "exemples").glob("*.yaml"))
    erreurs = 0
    for chemin in profils:
        profil = yaml.safe_load(chemin.read_text(encoding="utf-8")) or {}
        py = diagnostiquer(donnees["modele"], donnees["valeurs"], profil)
        js = json.loads(subprocess.run(["node", "-e", NODE, str(MOTEUR_JS), str(DONNEES), json.dumps(profil)],
                                       check=True, capture_output=True, text=True).stdout)
        ecarts = comparer(json.loads(json.dumps(py)), js)
        erreurs += len(ecarts)
        print(f"{chemin.name} : {'identiques' if not ecarts else str(len(ecarts)) + ' écart(s)'}")
        for e in ecarts[:10]:
            print("   ", e)
    print(f"\n{len(profils)} profil(s), {erreurs} écart(s)")
    return 1 if erreurs else 0


if __name__ == "__main__":
    sys.exit(main())
