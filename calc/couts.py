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
     "Consommation (côté batterie) × coût du kWh utile PV, pertes de charge comprises",
     lambda h, c: h["tracteur_compact_conso_elec"] * c["pv_kwh_utile"]),
    ("tracteur_reseau_eur_h", "Tracteur compact : énergie par heure en électrique sur réseau", "€/h",
     "Consommation (côté batterie) × coût du kWh utile réseau, pertes de charge comprises",
     lambda h, c: h["tracteur_compact_conso_elec"] * c["reseau_kwh_utile"]),
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
    ("chauffage_economie_an", "Ferme type : économie annuelle de combustible, plaquettes au lieu de mazout", "€/an",
     "Litres de mazout × énergie du litre × (kWh mazout − kWh plaquettes), même rendement de chaudière, hors entretien",
     lambda h, c: h["chauffage_mazout_ferme"] * h["energie_litre_gasoil"] * (c["mazout_kwh"] - c["plaquettes_kwh"])),
    ("chauffage_map_an", "Ferme type : plaquettes nécessaires par an", "MAP/an",
     "Litres de mazout × énergie du litre ÷ énergie du MAP",
     lambda h, c: h["chauffage_mazout_ferme"] * h["energie_litre_gasoil"] / h["plaquettes_energie_map"]),
    # Lait
    ("prerefroidisseur_kwh_an", "Pré-refroidisseur : électricité économisée par an", "kWh/an",
     "kWh par 1 000 L × gain × lait livré ÷ 1 000",
     lambda h, c: h["tank_kwh_1000l"] * h["prerefroidisseur_gain"] * h["lait_livre_an"] / 1000),
    ("prerefroidisseur_eur_an", "Pré-refroidisseur : économie par an (électricité du réseau)", "€/an",
     "kWh économisés × prix du réseau (la traite a lieu matin et soir, hors production PV)",
     lambda h, c: c["prerefroidisseur_kwh_an"] * h["electricite_reseau_htva"]),
    # Électricité : photovoltaïque de la ferme type
    ("ratio_reseau_pv", "Le kWh du réseau coûte … fois le kWh photovoltaïque produit", "fois",
     "Prix du réseau ÷ coût de production PV",
     lambda h, c: h["electricite_reseau_htva"] / c["pv_kwh_production"]),
    ("pv_autoconso_mini", "Taux d'autoconsommation à partir duquel le PV est rentable", "%",
     "(Coût du kWh PV − prix d'injection) ÷ (prix du réseau − prix d'injection), 0 si le PV coûte moins que l'injection",
     lambda h, c: max(0.0, (c["pv_kwh_production"] - h["pv_injection_prix"])
                      / (h["electricite_reseau_htva"] - h["pv_injection_prix"]))),
    ("pv_ferme_production_an", "Ferme type : production photovoltaïque annuelle", "kWh/an",
     "Puissance × production par kWc",
     lambda h, c: h["pv_ferme_kwc"] * h["pv_production"]),
    ("pv_ferme_autoconso_kwh", "Ferme type : électricité PV consommée sur place", "kWh/an",
     "Production × taux d'autoconsommation",
     lambda h, c: c["pv_ferme_production_an"] * h["pv_autoconsommation"]),
    ("pv_ferme_injection_kwh", "Ferme type : électricité PV injectée", "kWh/an",
     "Production − autoconsommation",
     lambda h, c: c["pv_ferme_production_an"] - c["pv_ferme_autoconso_kwh"]),
    ("pv_ferme_couverture", "Ferme type : part de la consommation couverte par le PV", "%",
     "Électricité PV autoconsommée ÷ consommation de la ferme",
     lambda h, c: c["pv_ferme_autoconso_kwh"] / h["ferme_conso_elec"]),
    ("pv_ferme_investissement", "Ferme type : investissement photovoltaïque", "€",
     "Puissance × prix installé",
     lambda h, c: h["pv_ferme_kwc"] * h["pv_prix_installe"]),
    ("pv_ferme_aide_aii", "Ferme type : aide AII au photovoltaïque (taux de base + architecture verte)", "€",
     "Puissance × coût simplifié AII × taux, limité à l'investissement",
     lambda h, c: min(h["pv_ferme_kwc"] * h["aii_pv_forfait"] * h["aii_taux_pv"], c["pv_ferme_investissement"])),
    ("pv_ferme_valeur_an", "Ferme type : valeur annuelle de l'électricité PV", "€/an",
     "kWh autoconsommés × prix du réseau + kWh injectés × prix d'injection",
     lambda h, c: c["pv_ferme_autoconso_kwh"] * h["electricite_reseau_htva"]
     + c["pv_ferme_injection_kwh"] * h["pv_injection_prix"]),
    ("pv_ferme_cout_an", "Ferme type : coût annuel du photovoltaïque (investissement et entretien étalés)", "€/an",
     "Production annuelle × coût de production du kWh PV, sans aide ni frais financiers",
     lambda h, c: c["pv_ferme_production_an"] * c["pv_kwh_production"]),
    ("pv_ferme_gain_net_an", "Ferme type : gain net annuel du photovoltaïque", "€/an",
     "Valeur annuelle − coût annuel, sans aide ni frais financiers",
     lambda h, c: c["pv_ferme_valeur_an"] - c["pv_ferme_cout_an"]),
    ("pv_ferme_retour_ans", "Ferme type : temps de retour simple du photovoltaïque, aide AII déduite", "ans",
     "(Investissement − aide) ÷ (valeur annuelle − entretien annuel)",
     lambda h, c: (c["pv_ferme_investissement"] - c["pv_ferme_aide_aii"])
     / (c["pv_ferme_valeur_an"] - c["pv_ferme_investissement"] * h["pv_entretien_part"] / h["pv_duree_vie"])),
    ("pv_ferme_valeur_an_sans_autoconso", "Ferme type : valeur annuelle si tout était injecté", "€/an",
     "Production × prix d'injection",
     lambda h, c: c["pv_ferme_production_an"] * h["pv_injection_prix"]),
    # Batterie
    ("batterie_gain_kwh_an", "Batterie : gain annuel par kWh de capacité", "€/kWh/an",
     "Cycles par an × (rendement × prix du réseau − prix d'injection)",
     lambda h, c: h["batterie_cycles_an"] * (h["batterie_rendement"] * h["electricite_reseau_htva"]
                                             - h["pv_injection_prix"])),
    ("batterie_retour_ans", "Batterie : temps de retour simple", "ans",
     "Prix par kWh ÷ gain annuel par kWh, hors remplacement et entretien",
     lambda h, c: h["batterie_prix_kwh"] / c["batterie_gain_kwh_an"]),
    # Micro-biométhanisation
    ("microbiometh_production_an", "Micro-biométhanisation : électricité produite par an", "kWh/an",
     "Puissance × heures de fonctionnement",
     lambda h, c: h["microbiometh_kw"] * h["microbiometh_heures"]),
    ("microbiometh_autoconso_kwh", "Micro-biométhanisation : électricité consommée par la ferme", "kWh/an",
     "Plus petite valeur entre la production et la consommation de la ferme",
     lambda h, c: min(c["microbiometh_production_an"], h["ferme_conso_elec"])),
    ("microbiometh_valeur_an", "Micro-biométhanisation : valeur annuelle de l'électricité, hors certificats verts", "€/an",
     "kWh autoconsommés × prix du réseau + surplus × prix d'injection",
     lambda h, c: c["microbiometh_autoconso_kwh"] * h["electricite_reseau_htva"]
     + (c["microbiometh_production_an"] - c["microbiometh_autoconso_kwh"]) * h["pv_injection_prix"]),
    ("microbiometh_investissement", "Micro-biométhanisation : investissement", "€",
     "Puissance × coût par kW",
     lambda h, c: h["microbiometh_kw"] * h["microbiometh_cout_kw"]),
    ("microbiometh_retour_ans", "Micro-biométhanisation : temps de retour simple, électricité seule", "ans",
     "Investissement ÷ valeur annuelle, sans aide, certificats verts, chaleur ni entretien",
     lambda h, c: c["microbiometh_investissement"] / c["microbiometh_valeur_an"]),
    # Engins de cour
    ("valet_gasoil_eur_h", "Chargeur de cour : énergie par heure au gasoil", "€/h",
     "Consommation × prix du gasoil",
     lambda h, c: h["valet_conso_gasoil"] * c["gasoil_agricole_htva"]),
    ("valet_pv_eur_h", "Chargeur de cour : énergie par heure en électrique sur PV", "€/h",
     "Consommation à la borne × coût du kWh PV (pertes de charge déjà dans la mesure)",
     lambda h, c: h["valet_conso_elec"] * c["pv_kwh_production"]),
    ("valet_reseau_eur_h", "Chargeur de cour : énergie par heure en électrique sur réseau", "€/h",
     "Consommation à la borne × prix du réseau (pertes de charge déjà dans la mesure)",
     lambda h, c: h["valet_conso_elec"] * h["electricite_reseau_htva"]),
    ("valet_economie_an_pv", "Chargeur de cour : économie d'énergie par an (électrique sur PV)", "€/an",
     "(Gasoil − PV) × heures par an, hors surcoût d'achat et entretien",
     lambda h, c: (c["valet_gasoil_eur_h"] - c["valet_pv_eur_h"]) * h["heures_valet_an"]),
    ("valet_economie_an_reseau", "Chargeur de cour : économie d'énergie par an (électrique sur réseau)", "€/an",
     "(Gasoil − réseau) × heures par an, hors surcoût d'achat et entretien",
     lambda h, c: (c["valet_gasoil_eur_h"] - c["valet_reseau_eur_h"]) * h["heures_valet_an"]),
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
    # Fourrages récoltés
    ("gasoil_eur_foin_ha", "Foin récolté au champ : gasoil par hectare", "€/ha",
     "Litres par hectare × prix du gasoil",
     lambda h, c: h["gasoil_foin_ha"] * c["gasoil_agricole_htva"]),
    ("gasoil_eur_enrubannage_ha", "Enrubannage : gasoil par hectare", "€/ha",
     "Litres par hectare × prix du gasoil",
     lambda h, c: h["gasoil_enrubannage_ha"] * c["gasoil_agricole_htva"]),
    ("gasoil_eur_ensilage_herbe_ha", "Ensilage d'herbe : gasoil par hectare", "€/ha",
     "Litres par hectare × prix du gasoil",
     lambda h, c: h["gasoil_ensilage_herbe_ha"] * c["gasoil_agricole_htva"]),
    ("gasoil_eur_mais_ensilage_ha", "Maïs ensilage : gasoil par hectare", "€/ha",
     "Litres par hectare × prix du gasoil",
     lambda h, c: h["gasoil_mais_ensilage_ha"] * c["gasoil_agricole_htva"]),
    ("sechage_grange_reseau_tms", "Séchoir en grange : électricité du réseau par tonne de MS", "€/t MS",
     "kWh par tonne × prix du kWh réseau",
     lambda h, c: h["sechage_grange_kwh_tms"] * h["electricite_reseau_htva"]),
    ("sechage_grange_pv_tms", "Séchoir en grange : électricité photovoltaïque par tonne de MS", "€/t MS",
     "kWh par tonne × coût de production du kWh PV",
     lambda h, c: h["sechage_grange_kwh_tms"] * c["pv_kwh_production"]),
    # Désherbage (fiche protection/herbicides)
    ("mais_chimique_eur_ha", "Maïs : désherbage chimique (herbicides + passages de pulvérisateur)", "€/ha",
     "Herbicides maïs + passages × coût d'un passage de pulvérisateur",
     lambda h, c: h["herbicides_mais_eur_ha"] + h["passages_pulverisateur_mais"] * h["cout_passage_pulverisateur"]),
    ("mais_mecanique_eur_ha", "Maïs : désherbage mécanique (1 herse étrille + binages)", "€/ha",
     "Passage de herse étrille + passages de bineuse × coût d'un binage",
     lambda h, c: h["cout_passage_herse_etrille"] + h["passages_bineuse_mais"] * h["cout_passage_bineuse"]),
    ("mais_meca_gasoil_supp_l_ha", "Maïs : gasoil en plus pour le désherbage mécanique", "L/ha",
     "(Herse + binages) − passages de pulvérisateur",
     lambda h, c: h["gasoil_passage_herse_etrille"] + h["passages_bineuse_mais"] * h["gasoil_passage_bineuse"]
     - h["passages_pulverisateur_mais"] * h["gasoil_passage_pulverisateur"]),
    ("mais_meca_gasoil_supp_eur_ha", "Maïs : coût du gasoil en plus pour le désherbage mécanique", "€/ha",
     "Gasoil en plus × prix du gasoil agricole",
     lambda h, c: c["mais_meca_gasoil_supp_l_ha"] * c["gasoil_agricole_htva"]),
    ("glyphosate_energie_kwh_ha", "Énergie de fabrication du glyphosate d'un traitement", "kWh/ha",
     "Énergie par kg × dose ÷ 3,6",
     lambda h, c: h["glyphosate_energie_mj_kg"] * h["glyphosate_dose_kg_ha"] / 3.6),
    ("glyphosate_eq_gasoil_l_ha", "Énergie de fabrication du glyphosate d'un traitement, en litres de gasoil", "L/ha",
     "Énergie du traitement ÷ énergie d'un litre de gasoil",
     lambda h, c: c["glyphosate_energie_kwh_ha"] / h["energie_litre_gasoil"]),
    ("sd_sans_glyphosate_gasoil_eur_ha", "Semis direct sans glyphosate (labour fréquent) : coût du gasoil en plus", "€/ha/an",
     "Gasoil en plus × prix du gasoil agricole",
     lambda h, c: h["gasoil_supp_sd_sans_glyphosate"] * c["gasoil_agricole_htva"]),
    ("farmdroid_amort_eur_ha", "Robot FarmDroid : amortissement par hectare et par an", "€/ha/an",
     "Prix ÷ (durée × surface par an), sans frais financiers ni entretien",
     lambda h, c: h["farmdroid_prix"] / (h["farmdroid_duree"] * h["farmdroid_surface"])),
    ("farmdroid_eq_heures_ha", "Robot FarmDroid : amortissement exprimé en heures de main-d'œuvre", "h/ha/an",
     "Amortissement par hectare ÷ coût horaire de la main-d'œuvre",
     lambda h, c: c["farmdroid_amort_eur_ha"] / h["main_oeuvre_eur_h"]),
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
