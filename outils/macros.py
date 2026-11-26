"""Macros MkDocs (plugin mkdocs-macros).

Dans une page :
  {{ v('gasoil_agricole_htva') }}          -> 1,22 €/L
  {{ v('ratio_gasoil_pv', 1) }}           -> 5,3 fois
  {{ v('prix_kg_n', unite=False) }}       -> 1,64
  {{ v('prix_kg_n', scenario='bas') }}    -> valeur du scénario de prix bas
  {{ fourchette('prix_kg_n') }}           -> 1,15 à 2,13 €/kg N (scénarios bas et haut)
  {{ tableau_hypotheses() }}, {{ tableau_calculs() }}, {{ index_fiches() }}
"""
import csv
from pathlib import Path

import yaml


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
