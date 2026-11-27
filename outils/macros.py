"""Macros MkDocs (plugin mkdocs-macros).

Dans une page :
  {{ v('gasoil_agricole_htva') }}          -> 1,22 €/L
  {{ v('ratio_gasoil_pv', 1) }}           -> 5,3 fois
  {{ v('prix_kg_n', unite=False) }}       -> 1,64
  {{ v('prix_kg_n', scenario='bas') }}    -> valeur du scénario de prix bas
  {{ fourchette('prix_kg_n') }}           -> 1,15 à 2,13 €/kg N (scénarios bas et haut)
  {{ tableau_hypotheses() }}, {{ tableau_calculs() }}, {{ index_fiches() }}
  {{ tableau_synthese(1) }}, {{ synthese_par_ferme('lait') }}   (page docs/synthese.md)
"""
import csv
import re
from pathlib import Path

import yaml


def _charger_liste(chemin: Path) -> list:
    if not chemin.exists():
        return []
    with chemin.open(encoding="utf-8") as f:
        return yaml.safe_load(f) or []


def _charger(chemin: Path) -> dict:
    if not chemin.exists():
        return {}
    with chemin.open(encoding="utf-8") as f:
        return yaml.safe_load(f) or {}


def _fmt(nombre: float, decimales: int) -> str:
    texte = f"{nombre:,.{decimales}f}"
    return texte.replace(",", " ").replace(".", ",")


def _decimales_auto(nombre: float) -> int:
    a = abs(nombre)
    if a >= 100:
        return 0
    if a >= 10:
        return 1
    if a >= 1:
        return 2
    return 3


def lire_alternatives(chemin: Path) -> list[dict]:
    """Alternatives d'une fiche : numéro, titre, vague et ancre de chaque « ### n. Titre (vague X) »."""
    from markdown.extensions.toc import slugify

    out = []
    for ligne in chemin.read_text(encoding="utf-8").splitlines():
        m = re.match(r"^### (\d+)\. (.+?) \(vague (\d)\)\s*$", ligne)
        if m:
            entete = ligne[4:].strip()
            out.append({"num": int(m.group(1)), "titre": m.group(2), "vague": int(m.group(3)),
                        "ancre": slugify(entete, "-")})
    return out


def trouver_alternative(alternatives: list[dict], debut: str) -> dict | None:
    debut = debut.strip().lower()
    trouvees = [a for a in alternatives if a["titre"].lower().startswith(debut)]
    return trouvees[0] if len(trouvees) == 1 else None


def define_env(env):
    racine = Path(env.project_dir)
    hypotheses = _charger(racine / "data" / "hypotheses.yaml")
    calculs = _charger(racine / "data" / "calculs.yaml")

    def entree(cle: str) -> dict:
        if cle in calculs:
            return calculs[cle]
        if cle in hypotheses:
            return hypotheses[cle]
        raise KeyError(f"Clé inconnue dans hypotheses.yaml et calculs.yaml : {cle}")

    def valeur_scenario(cle: str, scenario: str):
        e = entree(cle)
        valeur = e.get("valeur")
        if scenario == "actuel" or valeur is None:
            return valeur
        if scenario not in ("bas", "haut"):
            raise ValueError(f"Scénario inconnu : {scenario} (actuel, bas ou haut)")
        if cle in calculs:
            return e.get(scenario, valeur)
        if not e.get("scenario"):
            return valeur
        if e.get(scenario) is not None:
            return e[scenario]
        return valeur * hypotheses[f"scenario_{scenario}_facteur"]["valeur"]

    def formater(cle: str, valeur, decimales: int | None, unite: bool) -> str:
        if valeur is None:
            return "*(à saisir)*"
        u = entree(cle).get("unite", "") or ""
        if u == "%":
            valeur = valeur * 100
        d = _decimales_auto(valeur) if decimales is None else decimales
        texte = _fmt(valeur, d)
        if unite and u:
            texte += " " + u
        return texte

    @env.macro
    def v(cle: str, decimales: int | None = None, unite: bool = True, scenario: str = "actuel") -> str:
        return formater(cle, valeur_scenario(cle, scenario), decimales, unite)

    @env.macro
    def fourchette(cle: str, decimales: int | None = None, unite: bool = True) -> str:
        bas, haut = valeur_scenario(cle, "bas"), valeur_scenario(cle, "haut")
        if bas is None or haut is None:
            return "*(à saisir)*"
        if bas > haut:
            bas, haut = haut, bas
        if decimales is None:
            k = 100 if entree(cle).get("unite") == "%" else 1
            decimales = _decimales_auto(min(abs(bas), abs(haut)) * k)
        return f"{formater(cle, bas, decimales, False)} à {formater(cle, haut, decimales, unite)}"

    @env.macro
    def tableau_hypotheses() -> str:
        lignes = ["| Paramètre | Valeur | Bas | Haut | Statut | Date | Source |", "|---|---|---|---|---|---|---|"]
        for cle, e in hypotheses.items():
            source = e.get("source") or ""
            lien = f"[lien]({source})" if source else ""
            notes = [e[n] for n in ("note", "bas_note", "haut_note") if e.get(n)]
            note = "".join(f"<br><small>{n}</small>" for n in notes)
            bas, haut = (v(cle, scenario="bas"), v(cle, scenario="haut")) if e.get("scenario") else ("", "")
            lignes.append(
                f"| {e.get('libelle', cle)}{note}<br><code>{cle}</code> | {v(cle)} | {bas} | {haut} "
                f"| {e.get('statut', '')} | {e.get('date', '') or ''} | {lien} |"
            )
        return "\n".join(lignes)

    @env.macro
    def tableau_calculs() -> str:
        lignes = ["| Indicateur | Actuel | Bas | Haut | Calcul |", "|---|---|---|---|---|"]
        for cle, e in calculs.items():
            bas, haut = (v(cle, scenario="bas"), v(cle, scenario="haut")) if "bas" in e else ("=", "=")
            lignes.append(f"| {e['libelle']}<br><code>{cle}</code> | {v(cle)} | {bas} | {haut} | {e['formule']} |")
        return "\n".join(lignes)

    @env.macro
    def index_fiches() -> str:
        chemin = racine / "data" / "technologies.csv"
        with chemin.open(encoding="utf-8") as f:
            lignes_csv = list(csv.DictReader(f))
        lignes = [
            "| Technologie actuelle | Domaine | Dépend de | Meilleure alternative | Statut |",
            "|---|---|---|---|---|",
        ]
        for r in lignes_csv:
            vague = f"vague {r['vague_meilleure_alternative']}" if r["vague_meilleure_alternative"] else "à évaluer"
            if r["vague_meilleure_alternative"] and r["statut"] == "à rédiger":
                vague += " (provisoire)"
            lignes.append(
                f"| [{r['technologie_actuelle']}]({r['fiche']}) | {r['domaine']} | {r['dependance_fossile']} "
                f"| {vague} | {r['statut']} |"
            )
        return "\n".join(lignes)

    synthese = _charger_liste(racine / "data" / "synthese.yaml")
    fiches_dir = racine / "docs" / "fiches"

    def _titre_fiche(fiche: str) -> str:
        texte = (fiches_dir / fiche).read_text(encoding="utf-8")
        m = re.match(r"^---\n(.*?)\n---\n", texte, re.S)
        return (yaml.safe_load(m.group(1)) or {}).get("titre", fiche) if m else fiche

    def _lignes(vague: int | None = None, ferme: str | None = None) -> list[dict]:
        out = []
        for r in synthese:
            alt = trouver_alternative(lire_alternatives(fiches_dir / r["fiche"]), r["alternative"])
            if alt is None:
                raise KeyError(f"synthese.yaml : alternative introuvable « {r['alternative']} » dans {r['fiche']}")
            if vague is not None and alt["vague"] != vague:
                continue
            fermes = r.get("fermes", [])
            if ferme is not None and ferme not in fermes and "toutes" not in fermes:
                continue
            out.append({**r, **alt, "lien": f"fiches/{r['fiche']}#{alt['ancre']}"})
        return out

    def _a_un_scenario(cle: str) -> bool:
        e = entree(cle)
        return ("bas" in e) if cle in calculs else bool(e.get("scenario"))

    def _avec_bas(cle: str, decimales: int | None = None) -> str:
        texte = v(cle, decimales)
        if _a_un_scenario(cle) and valeur_scenario(cle, "bas") != entree(cle).get("valeur"):
            texte += f" ({v(cle, decimales, scenario='bas')} avant la crise)"
        return texte

    def _repere(r: dict) -> str:
        rep = r.get("repere")
        if not rep:
            return "—"
        texte = f"**{_avec_bas(rep['cle'])}** {rep['libelle']}"
        if rep.get("compare"):
            texte += f", contre {_avec_bas(rep['compare'])} {rep['compare_libelle']}"
        return texte

    @env.macro
    def tableau_synthese(vague: int) -> str:
        lignes = [
            "| Alternative | Pour quelles fermes | Repère chiffré (prix actuel) | Temps de retour | Avec les aides |",
            "|---|---|---|---|---|",
        ]
        for r in _lignes(vague=vague):
            alt = f"[{r['titre']}]({r['lien']})<br><small>{_titre_fiche(r['fiche'])}. {r.get('note', '')}</small>"
            retour = _avec_bas(r["retour"], 1) if r.get("retour") else "—"
            aide = _avec_bas(r["retour_aide"], 1) if r.get("retour_aide") else "—"
            lignes.append(f"| {alt} | {', '.join(r.get('fermes', []))} | {_repere(r)} | {retour} | {aide} |")
        return "\n".join(lignes)

    @env.macro
    def synthese_par_ferme(ferme: str) -> str:
        lignes = []
        for vague in (1, 2):
            for r in _lignes(vague=vague, ferme=ferme):
                rep = r.get("repere")
                chiffre = f" : {v(rep['cle'])} {rep['libelle']}" if rep else ""
                lignes.append(f"- vague {vague} : [{r['titre']}]({r['lien']}) ({_titre_fiche(r['fiche']).lower()}){chiffre}")
        return "\n".join(lignes) if lignes else "- Aucune alternative listée."

    @env.macro
    def liste_vague(vague: int) -> str:
        """Toutes les alternatives d'une vague, lues dans les fiches, avec un lien."""
        lignes = []
        for chemin in sorted(fiches_dir.rglob("*.md")):
            if chemin.name == "index.md":
                continue
            rel = chemin.relative_to(fiches_dir).as_posix()
            for a in lire_alternatives(chemin):
                if a["vague"] == vague:
                    lignes.append(f"- [{a['titre']}](fiches/{rel}#{a['ancre']}) ({_titre_fiche(rel)})")
        return "\n".join(lignes)
