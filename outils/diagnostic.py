"""Diagnostic d'une exploitation : rapport en Markdown à partir d'un profil.

Usage :
  python outils/diagnostic.py exemples/ferme-laitiere.yaml              # rapport à l'écran
  python outils/diagnostic.py mon-profil.json --sortie rapport.md        # rapport dans un fichier

Le profil est un fichier YAML ou JSON {question_ou_consommation: valeur}. Celui que la page
« Diagnostic de sa ferme » du site permet de télécharger convient tel quel. Les consommations
absentes sont estimées à partir de la structure de la ferme ; les renseigner depuis les
factures rend le diagnostic plus juste.

Les profils de vraies exploitations ne doivent pas être ajoutés au dépôt : les garder hors du
dossier, ou dans profils/ (ignoré par git).
"""
import argparse
import datetime as dt
import json
import sys
from pathlib import Path

import yaml

RACINE = Path(__file__).resolve().parent.parent
DONNEES = RACINE / "docs" / "assets" / "diagnostic" / "donnees.json"
SITE = "https://sapidesrl.github.io/Agrifutur/"
sys.path.insert(0, str(RACINE / "outils"))
from moteur_diagnostic import diagnostiquer  # noqa: E402

PISTES_NON_CHIFFREES = [
    ("Plastiques (enrubannage, bâches, paillages)", "fiches/materiaux/plastiques-agricoles/"),
    ("Haies, auxiliaires et biocontrôle", "fiches/protection/fongicides-insecticides/"),
    ("Séchage du foin en grange", "fiches/elevage/fourrages-recoltes/"),
    ("Transformation à la ferme et vente directe", "fiches/transformation/transformation-industrielle/"),
    ("Circuits courts", "fiches/distribution/circuits-longs/"),
]


def fr(x, d=0) -> str:
    if x is None:
        return "—"
    return f"{x:,.{d}f}".replace(",", " ").replace(".", ",")


def charger_donnees() -> dict:
    return json.loads(DONNEES.read_text(encoding="utf-8"))


def charger_profil(chemin: Path) -> dict:
    texte = chemin.read_text(encoding="utf-8")
    profil = json.loads(texte) if chemin.suffix == ".json" else yaml.safe_load(texte)
    return profil.get("profil", profil) if isinstance(profil, dict) else {}


def trier(recos: list[dict], modele: dict) -> list[dict]:
    infos = {r["id"]: r for r in modele["recommandations"]}

    def cle(r):
        retour = r["retour"].get("actuel") if r["retour"] else None
        return (infos[r["id"]]["vague"], retour if retour is not None else 0, -(r["economie"]["actuel"] or 0))

    return sorted(recos, key=cle)


def rapport(donnees: dict, profil: dict, nom: str) -> str:
    modele, valeurs = donnees["modele"], donnees["valeurs"]
    res = diagnostiquer(modele, valeurs, profil)
    infos = {r["id"]: r for r in modele["recommandations"]}
    lignes = [f"# Diagnostic : {nom}", "",
              f"Établi le {dt.date.today().strftime('%d/%m/%Y')} avec les prix de référence du projet "
              f"« L'agriculture après le pétrole » ({SITE}). Les chiffres valent pour une ferme moyenne "
              "de cette structure ; une consommation saisie depuis les factures remplace l'estimation.", ""]

    lignes += ["## Consommations retenues", "", "| Poste | Retenu | Estimation | Unité |", "|---|---|---|---|"]
    for c in modele["consommations"]:
        saisi = profil.get(c["id"]) not in (None, "")
        retenu = fr(res["consommations"][c["id"]])
        lignes.append(f"| {c['libelle']} | {retenu}{' (saisi)' if saisi else ''} | "
                      f"{fr(res['estimations'][c['id']])} | {c['unite']} |")

    lignes += ["", "## Dépenses liées au pétrole et au gaz", "",
               "| Poste | Prix actuel | Avant la crise | Prix haut |", "|---|---|---|---|"]
    tot = {"actuel": 0.0, "bas": 0.0, "haut": 0.0}
    postes = {p["id"]: p for p in modele["postes"]}
    for p in res["postes"]:
        d = p["depense"]
        if not d["actuel"]:
            continue
        for s in tot:
            tot[s] += d[s] or 0
        lignes.append(f"| {postes[p['id']]['libelle']} | {fr(d['actuel'])} € | {fr(d['bas'])} € | {fr(d['haut'])} € |")
    lignes.append(f"| **Total** | **{fr(tot['actuel'])} €** | **{fr(tot['bas'])} €** | **{fr(tot['haut'])} €** |")
    lignes += ["", f"La crise de l'énergie coûte environ {fr(tot['actuel'] - tot['bas'])} € par an à cette "
               "ferme par rapport aux prix de février 2026 (calculé).", ""]

    lignes += ["## Changements proposés", "",
               "Classés par vague (1 = rentable aujourd'hui, 2 = sous conditions), puis par temps de retour.", "",
               "| Changement | Vague | Économie par an | Avant la crise | Investissement | Retour |",
               "|---|---|---|---|---|---|"]
    recos = trier(res["recommandations"], modele)
    for r in recos:
        i = infos[r["id"]]
        e = r["economie"]
        inv = f"{fr(r['investissement'])} €" if r["investissement"] is not None else "—"
        if r["aide"]:
            inv += f" (aide {fr(r['aide'])} €)"
        ret = f"{fr(r['retour'].get('actuel'), 1)} ans" if r["retour"].get("actuel") is not None else "—"
        lignes.append(f"| [{i['titre']}]({SITE}{i['lien']}) | {i['vague']} | {fr(e['actuel'])} € | "
                      f"{fr(e['bas'])} € | {inv} | {ret} |")
    if not recos:
        lignes.append("| Aucun changement chiffré pour ce profil | | | | | |")
    lignes += [""]
    for r in recos:
        i = infos[r["id"]]
        lignes += [f"- **{i['titre']}** ({i['titre_fiche']}) : {i['texte']}"]

    lignes += ["", "## Pistes non chiffrées ici", ""]
    lignes += [f"- [{t}]({SITE}{u})" for t, u in PISTES_NON_CHIFFREES]
    lignes += ["", "Ce diagnostic est une première orientation : chaque changement demande une étude "
               "propre à la ferme (devis, contraintes, aides réellement accessibles).", ""]
    return "\n".join(lignes)


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    p.add_argument("profil", type=Path, help="fichier YAML ou JSON décrivant la ferme")
    p.add_argument("--sortie", type=Path, help="écrire le rapport dans ce fichier (Markdown)")
    p.add_argument("--nom", default=None, help="nom affiché dans le titre du rapport")
    args = p.parse_args()
    texte = rapport(charger_donnees(), charger_profil(args.profil), args.nom or args.profil.stem)
    if args.sortie:
        args.sortie.write_text(texte, encoding="utf-8")
        print(f"Rapport écrit dans {args.sortie}")
    else:
        print(texte)
    return 0


if __name__ == "__main__":
    sys.exit(main())
