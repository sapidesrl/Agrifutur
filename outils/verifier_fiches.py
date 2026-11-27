"""Contrôles avant commit.

Erreurs (code de sortie 1) :
  - fiche de l'index absente, ou fiche absente de l'index ;
  - frontmatter incomplet ;
  - section obligatoire manquante ou dans le désordre ;
  - macro {{ v('cle') }} qui appelle une clé inconnue ;
  - note de bas de page appelée mais jamais définie.
Avertissements :
  - ligne avec un montant (€, £, $) sans note de bas de page ni macro.
Usage : python outils/verifier_fiches.py
"""
import csv
import re
import sys
from pathlib import Path

import yaml

RACINE = Path(__file__).resolve().parent.parent
FICHES = RACINE / "docs" / "fiches"
SECTIONS = [
    "## En bref",
    "## Comment ça marche aujourd'hui",
    "## Où entrent le pétrole et le gaz",
    "## Les alternatives",
    "## Ce qui ferme la boucle",
    "## À vérifier",
    "## Sources",
]
CHAMPS = ["id", "titre", "domaine", "dependance_fossile", "alternatives", "vague_meilleure_alternative", "statut", "maj"]
MACRO = re.compile(r"\{\{\s*(?:v|fourchette)\(\s*'([^']+)'")
APPEL_NOTE = re.compile(r"\[\^([^\]]+)\](?!:)")
DEF_NOTE = re.compile(r"^\[\^([^\]]+)\]:", re.M)
MONTANT = re.compile(r"\d[\d\s .,]*\s?(?:k€|c€|€|£|\$)")


def charger_yaml(nom: str) -> dict:
    chemin = RACINE / "data" / nom
    if not chemin.exists():
        return {}
    return yaml.safe_load(chemin.read_text(encoding="utf-8")) or {}


def main() -> int:
    erreurs: list[str] = []
    avertissements: list[str] = []
    cles = set(charger_yaml("hypotheses.yaml")) | set(charger_yaml("calculs.yaml"))
    if not (RACINE / "data" / "calculs.yaml").exists():
        erreurs.append("data/calculs.yaml absent : lance python calc/couts.py")

    with (RACINE / "data" / "technologies.csv").open(encoding="utf-8") as f:
        index = {r["fiche"]: r for r in csv.DictReader(f)}

    for fiche in index:
        if not (FICHES / fiche).exists():
            erreurs.append(f"{fiche} : dans l'index mais fichier absent (python outils/nouvelle_fiche.py --toutes)")

    for chemin in sorted(FICHES.rglob("*.md")):
        rel = chemin.relative_to(FICHES).as_posix()
        if rel == "index.md":
            continue
        if rel not in index:
            erreurs.append(f"{rel} : fichier absent de data/technologies.csv")
        texte = chemin.read_text(encoding="utf-8")

        m = re.match(r"^---\n(.*?)\n---\n", texte, re.S)
        if not m:
            erreurs.append(f"{rel} : frontmatter manquant")
            corps = texte
        else:
            meta = yaml.safe_load(m.group(1)) or {}
            for champ in CHAMPS:
                if champ not in meta:
                    erreurs.append(f"{rel} : champ « {champ} » absent du frontmatter")
            corps = texte[m.end():]

        positions = [corps.find(s + "\n") for s in SECTIONS]
        for section, pos in zip(SECTIONS, positions):
            if pos < 0:
                erreurs.append(f"{rel} : section manquante « {section} »")
        trouvees = [p for p in positions if p >= 0]
        if trouvees != sorted(trouvees):
            erreurs.append(f"{rel} : sections dans le désordre")

        for cle in MACRO.findall(corps):
            if cle not in cles:
                erreurs.append(f"{rel} : clé inconnue dans une macro « {cle} »")

        definies = set(DEF_NOTE.findall(corps))
        for note in set(APPEL_NOTE.findall(corps)):
            if note not in definies:
                erreurs.append(f"{rel} : note [^{note}] appelée mais non définie")

        for n, ligne in enumerate(corps.splitlines(), start=1):
            if ligne.startswith("[^"):
                continue
            if MONTANT.search(ligne) and "[^" not in ligne and "{{" not in ligne:
                avertissements.append(f"{rel}:{n} : montant sans source ni macro → {ligne.strip()[:90]}")

    # Synthèse : chaque ligne doit pointer vers une alternative existante et des clés connues.
    sys.path.insert(0, str(RACINE / "outils"))
    from macros import lire_alternatives, trouver_alternative
    synthese = yaml.safe_load((RACINE / "data" / "synthese.yaml").read_text(encoding="utf-8")) or []
    for n, r in enumerate(synthese, start=1):
        chemin = FICHES / r.get("fiche", "")
        if not chemin.exists():
            erreurs.append(f"synthese.yaml, ligne {n} : fiche absente {r.get('fiche')}")
            continue
        if trouver_alternative(lire_alternatives(chemin), r.get("alternative", "")) is None:
            erreurs.append(f"synthese.yaml, ligne {n} : alternative introuvable ou ambiguë « {r.get('alternative')} » dans {r['fiche']}")
        rep = r.get("repere") or {}
        for cle in [rep.get("cle"), rep.get("compare"), r.get("retour"), r.get("retour_aide")]:
            if cle and cle not in cles:
                erreurs.append(f"synthese.yaml, ligne {n} : clé inconnue « {cle} »")

    # Diagnostic d'exploitation : chaque formule n'utilise que des noms connus,
    # et chaque recommandation retrouve son alternative dans sa fiche.
    from moteur_diagnostic import ErreurFormule, noms
    diag = yaml.safe_load((RACINE / "data" / "diagnostic.yaml").read_text(encoding="utf-8")) or {}
    connus = set(cles) | {q["id"] for q in diag.get("questions", [])} | {c["id"] for c in diag.get("consommations", [])}
    for section, champs in (("consommations", ["estimation"]), ("postes", ["depense"]),
                            ("recommandations", ["condition", "economie", "investissement", "aide"])):
        for x in diag.get(section, []):
            for champ in champs:
                if not x.get(champ):
                    continue
                try:
                    inconnus = noms(x[champ]) - connus
                except ErreurFormule as e:
                    erreurs.append(f"diagnostic.yaml, {section} « {x.get('id')} », {champ} : {e}")
                    continue
                for n in sorted(inconnus):
                    erreurs.append(f"diagnostic.yaml, {section} « {x.get('id')} », {champ} : nom inconnu « {n} »")
    for r in diag.get("recommandations", []):
        chemin = FICHES / r.get("fiche", "")
        if not chemin.exists() or trouver_alternative(lire_alternatives(chemin), r.get("alternative", "")) is None:
            erreurs.append(f"diagnostic.yaml, recommandation « {r.get('id')} » : alternative introuvable dans {r.get('fiche')}")

    for a in avertissements:
        print(f"AVERTISSEMENT  {a}")
    for e in erreurs:
        print(f"ERREUR         {e}")
    print(f"\n{len(index)} fiches dans l'index, {len(erreurs)} erreur(s), {len(avertissements)} avertissement(s)")
    return 1 if erreurs else 0


if __name__ == "__main__":
    sys.exit(main())
