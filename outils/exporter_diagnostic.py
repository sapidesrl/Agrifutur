"""Prépare les données du diagnostic d'exploitation pour la page web et le script.

Écrit docs/assets/diagnostic/donnees.json : le modèle (data/diagnostic.yaml), enrichi de la
vague et du lien de chaque recommandation lus dans les fiches, et les valeurs de toutes les
hypothèses et de tous les calculs dans les trois scénarios de prix.
Appelé par calc/couts.py ; ne pas éditer le fichier JSON à la main.
"""
import json
import re
import sys
from pathlib import Path

import yaml

RACINE = Path(__file__).resolve().parent.parent
MODELE = RACINE / "data" / "diagnostic.yaml"
SORTIE = RACINE / "docs" / "assets" / "diagnostic" / "donnees.json"
FICHES = RACINE / "docs" / "fiches"

sys.path.insert(0, str(RACINE / "outils"))
from macros import lire_alternatives, trouver_alternative  # noqa: E402


def _titre_fiche(fiche: str) -> str:
    texte = (FICHES / fiche).read_text(encoding="utf-8")
    m = re.match(r"^---\n(.*?)\n---\n", texte, re.S)
    return (yaml.safe_load(m.group(1)) or {}).get("titre", fiche) if m else fiche


def _url_fiche(fiche: str) -> str:
    return "fiches/" + fiche[:-3] + "/"


def charger_modele() -> dict:
    modele = yaml.safe_load(MODELE.read_text(encoding="utf-8"))
    for p in modele.get("postes", []):
        if p.get("fiche"):
            p["lien"] = _url_fiche(p["fiche"])
    for r in modele.get("recommandations", []):
        alt = trouver_alternative(lire_alternatives(FICHES / r["fiche"]), r["alternative"])
        if alt is None:
            raise KeyError(f"diagnostic.yaml : alternative introuvable « {r['alternative']} » dans {r['fiche']}")
        r["vague"] = alt["vague"]
        r["lien"] = _url_fiche(r["fiche"]) + "#" + alt["ancre"]
        r["titre_fiche"] = _titre_fiche(r["fiche"])
    return modele


def valeurs_par_scenario(hypotheses: dict[str, dict], calculs: dict[str, dict]) -> dict:
    """hypotheses et calculs : {scenario: {cle: valeur}}."""
    out = {}
    for s in ("actuel", "bas", "haut"):
        v = {k: (None if x is None else round(float(x), 6)) for k, x in hypotheses[s].items()
             if isinstance(x, (int, float)) or x is None}
        v.update({k: round(float(x), 6) for k, x in calculs[s].items()})
        out[s] = dict(sorted(v.items()))
    return out


def exporter(hypotheses: dict, calculs: dict) -> Path:
    donnees = {"modele": charger_modele(), "valeurs": valeurs_par_scenario(hypotheses, calculs)}
    SORTIE.parent.mkdir(parents=True, exist_ok=True)
    SORTIE.write_text(json.dumps(donnees, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    return SORTIE
