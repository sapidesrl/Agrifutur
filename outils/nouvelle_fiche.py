"""Crée une fiche vide à partir du gabarit et de sa ligne dans data/technologies.csv.

Usage :
  python outils/nouvelle_fiche.py <id>      une fiche
  python outils/nouvelle_fiche.py --toutes  toutes les fiches manquantes
Une fiche qui existe déjà n'est jamais écrasée.
"""
import csv
import sys
from datetime import date
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent
INDEX = RACINE / "data" / "technologies.csv"
GABARIT = RACINE / "templates" / "fiche.md"
FICHES = RACINE / "docs" / "fiches"


def lire_index() -> list[dict]:
    with INDEX.open(encoding="utf-8") as f:
        return list(csv.DictReader(f))


def creer(ligne: dict) -> bool:
    cible = FICHES / ligne["fiche"]
    if cible.exists():
        print(f"existe déjà : {cible.relative_to(RACINE)}")
        return False
    alternatives = [a.strip() for a in ligne["alternatives"].split(";") if a.strip()]
    sections = "\n\n".join(
        f"### {i}. {a[0].upper() + a[1:]}\n\n*À rédiger : principe, maturité, coût, conditions, vague.*"
        for i, a in enumerate(alternatives, start=1)
    )
    texte = GABARIT.read_text(encoding="utf-8").format(
        id=ligne["id"],
        titre=ligne["technologie_actuelle"],
        domaine=ligne["domaine"],
        dependance=ligne["dependance_fossile"],
        alternatives_liste=", ".join(alternatives),
        vague=ligne["vague_meilleure_alternative"] or "null",
        date=date.today().isoformat(),
        sections_alternatives=sections,
    )
    cible.parent.mkdir(parents=True, exist_ok=True)
    cible.write_text(texte, encoding="utf-8")
    print(f"créée : {cible.relative_to(RACINE)}")
    return True


def main() -> None:
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    lignes = lire_index()
    if sys.argv[1] == "--toutes":
        n = sum(creer(l) for l in lignes)
        print(f"{n} fiche(s) créée(s)")
        return
    for l in lignes:
        if l["id"] == sys.argv[1]:
            creer(l)
            return
    sys.exit(f"id inconnu dans {INDEX.relative_to(RACINE)} : {sys.argv[1]}")


if __name__ == "__main__":
    main()
