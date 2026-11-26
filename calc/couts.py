"""Recalcule les comparaisons de coûts à partir de data/hypotheses.yaml.

Écrit data/calculs.yaml, lu par les fiches via la macro {{ v('cle') }}.
Chaque calcul est fait pour trois scénarios de prix (actuel, bas, haut) : voir
l'en-tête de data/hypotheses.yaml.
Usage : python calc/couts.py
"""
from pathlib import Path

import yaml

RACINE = Path(__file__).resolve().parent.parent
HYPOTHESES = RACINE / "data" / "hypotheses.yaml"
SORTIE = RACINE / "data" / "calculs.yaml"


SCENARIOS = ("actuel", "bas", "haut")


def charger_brut() -> dict:
    with HYPOTHESES.open(encoding="utf-8") as f:
        return yaml.safe_load(f)


def valeurs_scenario(brut: dict, scenario: str) -> dict:
    """Valeurs des hypothèses dans un scénario. Seules les entrées `scenario: true` varient."""
    h = {cle: e.get("valeur") for cle, e in brut.items()}
    if scenario == "actuel":
        return h
    facteur = h[f"scenario_{scenario}_facteur"]
    for cle, e in brut.items():
        if e.get("scenario") and e.get("valeur") is not None:
            h[cle] = e[scenario] if e.get(scenario) is not None else e["valeur"] * facteur
    return h


def charger_hypotheses() -> dict:
    return valeurs_scenario(charger_brut(), "actuel")


def gasoil_agricole(h: dict) -> float:
    saisi = h.get("gasoil_agricole_htva_saisi")
    if saisi is not None:
        return saisi
    return (h["gasoil_chauffage_2000l_tvac"] - h["ecart_gasoil_agricole_chauffage"]) / (1 + h["tva"])


# (clé, libellé, unité, formule lisible, fonction(h, c) -> valeur)
# Les calculs sont faits dans l'ordre : un calcul peut lire ceux d'avant dans c.
CALCULS = [
    # Énergie
    ("gasoil_agricole_htva", "Gasoil agricole HTVA utilisé dans les calculs", "€/L",
     "Prix saisi, sinon (gasoil chauffage TVAC − écart) ÷ (1 + TVA)",
     lambda h, c: gasoil_agricole(h)),
    ("gasoil_kwh_utile", "Gasoil : coût du kWh utile (à l'arbre)", "€/kWh",
     "Prix du litre ÷ (énergie du litre × rendement du moteur)",
     lambda h, c: c["gasoil_agricole_htva"] / (h["energie_litre_gasoil"] * h["rendement_moteur_diesel"])),
    ("gasoil_kwh_utile_fev2026", "Gasoil en février 2026 : coût du kWh utile", "€/kWh",
     "Même calcul au prix d'avant la guerre",
     lambda h, c: h["gasoil_agricole_fev2026_htva"] / (h["energie_litre_gasoil"] * h["rendement_moteur_diesel"])),
    ("pv_kwh_production", "Coût de production d'un kWh photovoltaïque", "€/kWh",
     "Prix installé × (1 + entretien) ÷ (production annuelle × durée de vie), sans frais financiers",
     lambda h, c: h["pv_prix_installe"] * (1 + h["pv_entretien_part"]) / (h["pv_production"] * h["pv_duree_vie"])),
    ("pv_kwh_utile", "PV : coût du kWh utile", "€/kWh",
     "kWh PV ÷ rendement de la chaîne électrique",
     lambda h, c: c["pv_kwh_production"] / h["rendement_chaine_electrique"]),
    ("reseau_kwh_utile", "Réseau : coût du kWh utile", "€/kWh",
     "kWh réseau ÷ rendement de la chaîne électrique",
     lambda h, c: h["electricite_reseau_htva"] / h["rendement_chaine_electrique"]),
    ("ratio_gasoil_pv", "Le kWh utile au gasoil coûte … fois celui du PV", "fois",
     "Gasoil ÷ PV",
     lambda h, c: c["gasoil_kwh_utile"] / c["pv_kwh_utile"]),
    ("ratio_gasoil_reseau", "Le kWh utile au gasoil coûte … fois celui du réseau", "fois",
     "Gasoil ÷ réseau",
     lambda h, c: c["gasoil_kwh_utile"] / c["reseau_kwh_utile"]),
    # Tracteur compact
    ("tracteur_gasoil_eur_h", "Tracteur compact : énergie par heure au gasoil", "€/h",
     "Consommation × prix du gasoil",
     lambda h, c: h["tracteur_compact_conso_gasoil"] * c["gasoil_agricole_htva"]),
    ("tracteur_pv_eur_h", "Tracteur compact : énergie par heure en électrique sur PV", "€/h",
     "Consommation × coût du kWh PV",
     lambda h, c: h["tracteur_compact_conso_elec"] * c["pv_kwh_production"]),
    ("tracteur_reseau_eur_h", "Tracteur compact : énergie par heure en électrique sur réseau", "€/h",
     "Consommation × prix du réseau",
     lambda h, c: h["tracteur_compact_conso_elec"] * h["electricite_reseau_htva"]),
    ("tracteur_economie_an", "Tracteur compact : économie d'énergie par an (électrique sur PV)", "€/an",
     "(Gasoil − PV) × heures par an, hors surcoût d'achat et entretien",
     lambda h, c: (c["tracteur_gasoil_eur_h"] - c["tracteur_pv_eur_h"]) * h["heures_tracteur_an"]),
    # Tracteur lourd
    ("batterie_journee_lourde", "Batterie nécessaire pour une journée de travail lourd", "kWh",
     "Consommation × heures × énergie du litre × rendement moteur ÷ rendement électrique",
     lambda h, c: h["tracteur_lourd_conso_gasoil"] * h["heures_journee_lourde"] * h["energie_litre_gasoil"]
     * h["rendement_moteur_diesel"] / h["rendement_chaine_electrique"]),
    ("batterie_masse_journee_lourde", "Masse de cette batterie", "t",
     "Énergie ÷ énergie massique du pack",
     lambda h, c: c["batterie_journee_lourde"] / h["batterie_densite_pack"] / 1000),
    # Azote
    ("prix_kg_n", "Prix du kg d'azote (ammonitrate)", "€/kg N",
     "Prix de la tonne ÷ kg d'azote par tonne",
     lambda h, c: h["ammonitrate_prix"] / (1000 * h["ammonitrate_teneur_n"])),
    ("valeur_n_fixe", "Valeur de l'azote fixé par les légumineuses", "€/ha/an",
     "kg N fixés × prix du kg N",
     lambda h, c: h["azote_fixe_legumineuses"] * c["prix_kg_n"]),
    # Chaleur
    ("mazout_kwh", "Mazout : prix du kWh", "€/kWh",
     "Prix TVAC ÷ énergie du litre",
     lambda h, c: h["gasoil_chauffage_2000l_tvac"] / h["energie_litre_gasoil"]),
    ("plaquettes_kwh", "Plaquettes sèches : prix du kWh", "€/kWh",
     "Prix du MAP ÷ énergie du MAP",
     lambda h, c: h["plaquettes_prix"] / h["plaquettes_energie_map"]),
    ("ratio_mazout_plaquettes", "Le kWh de mazout coûte … fois celui des plaquettes", "fois",
     "Mazout ÷ plaquettes",
     lambda h, c: c["mazout_kwh"] / c["plaquettes_kwh"]),
    # Huile de colza
    ("huile_cout_litre", "Huile de colza : coût d'un litre, tourteau déduit", "€/L",
     "(Prix de la graine − valeur du tourteau) ÷ litres d'huile + pressage, hors accises",
     lambda h, c: (h["colza_prix"] - h["tourteau_par_tonne"] * h["tourteau_prix"]) / h["huile_par_tonne"]
     + h["pressage_cout"]),
    ("huile_cout_eq_gasoil", "Huile de colza : coût ramené à l'énergie d'un litre de gasoil", "€/L",
     "Coût du litre × énergie du gasoil ÷ énergie de l'huile",
     lambda h, c: c["huile_cout_litre"] * h["energie_litre_gasoil"] / h["energie_litre_huile"]),
    ("huile_ecart_gasoil", "Huile de colza : écart avec le gasoil agricole HTVA", "€/L",
     "Négatif : l'huile revient moins cher (hors accises)",
     lambda h, c: c["huile_cout_eq_gasoil"] - c["gasoil_agricole_htva"]),
    ("part_surface_colza", "Part de la surface en colza pour l'autonomie en carburant", "%",
     "Litres d'huile nécessaires par ha ÷ litres d'huile produits par ha de colza",
     lambda h, c: h["gasoil_labour"] * h["energie_litre_gasoil"] / h["energie_litre_huile"]
     / (h["colza_rendement"] * h["huile_par_tonne"])),
    # Travail du sol
    ("gasoil_economise_semis_direct", "Gasoil économisé en semis direct", "L/ha/an",
     "Labour − semis direct",
     lambda h, c: h["gasoil_labour"] - h["gasoil_semis_direct"]),
    ("valeur_gasoil_economise", "Valeur de ce gasoil", "€/ha/an",
     "Litres économisés × prix du gasoil",
     lambda h, c: c["gasoil_economise_semis_direct"] * c["gasoil_agricole_htva"]),
]


def calculer(h: dict) -> dict:
    c: dict = {}
    for cle, _libelle, _unite, _formule, fonction in CALCULS:
        c[cle] = fonction(h, c)
    return c


def main() -> None:
    brut = charger_brut()
    resultats = {s: calculer(valeurs_scenario(brut, s)) for s in SCENARIOS}
    sortie: dict = {}
    for cle, libelle, unite, formule, _fonction in CALCULS:
        e = {"libelle": libelle, "valeur": round(resultats["actuel"][cle], 6)}
        bas, haut = round(resultats["bas"][cle], 6), round(resultats["haut"][cle], 6)
        if bas != e["valeur"] or haut != e["valeur"]:
            e["bas"], e["haut"] = bas, haut
        e.update({"unite": unite, "formule": formule})
        sortie[cle] = e
    entete = "# Généré par calc/couts.py : ne pas éditer à la main.\n"
    SORTIE.write_text(entete + yaml.safe_dump(sortie, allow_unicode=True, sort_keys=False), encoding="utf-8")
    largeur = max(len(e["libelle"]) for e in sortie.values())
    print(f"{'':<{largeur}}  {'actuel':>12}  {'bas':>12}  {'haut':>12}")
    for e in sortie.values():
        k = 100 if e["unite"] == "%" else 1
        cols = [e["valeur"]] + ([e["bas"], e["haut"]] if "bas" in e else [])
        texte = "  ".join(f"{x * k:>12.4f}" for x in cols)
        if "bas" not in e:
            texte += f"  {'=':>12}  {'=':>12}"
        print(f"{e['libelle']:<{largeur}}  {texte}  {e['unite']}")
    print(f"\n{len(sortie)} calculs écrits dans {SORTIE.relative_to(RACINE)}")


if __name__ == "__main__":
    main()
