# Les aides publiques

!!! warning "Montants de 2026, à confirmer avant toute décision"
    Les montants ont été lus sur les sources le 27 novembre 2026. Ceux du 1er pilier de la PAC sont des montants **prévus** : le montant payé est fixé après la campagne, selon la demande, entre un minimum et un maximum. Les pages du Portail de l'agriculture wallonne précisent qu'elles n'ont aucune portée légale : seuls les arrêtés publiés font foi. Plusieurs règles restent à confirmer (voir « À vérifier »).

## À quoi servent les aides dans ce projet

Les fiches comparent d'abord les alternatives **sans aide**. Elles ajoutent ensuite les aides accessibles quand elles changent la rentabilité (voir [la méthode](methode.md#les-aides)). Cette page rassemble les aides utiles aux alternatives du projet, leurs montants 2026 et leurs règles de cumul.

Trois familles d'aides comptent :

- **la PAC** paie des pratiques chaque année (éco-régimes, aides couplées) ou pendant cinq ans (MAEC, bio) ;
- **les aides à l'investissement** (AII agricole, GREEN pour l'énergie) paient une part du matériel ;
- **les certificats verts** paient chaque MWh d'électricité renouvelable produit.

Une aide ne rend pas une alternative solide à elle seule. Une alternative qui ne tient que par une aide annuelle dont le montant varie reste en vague 2 (rentable sous conditions).

## PAC, 1er pilier : éco-régimes et aides couplées

### Ce que paient les éco-régimes

Les éco-régimes sont des engagements d'un an. Le montant prévu pour 2026 est donné ci-dessous ; le montant payé peut aller du minimum au maximum publié[^ri] [^cfe] [^maillage].

| Éco-régime | Ce qui est exigé | Montant prévu 2026 |
|---|---|---|
| Réduction d'intrants | Par parcelle d'au moins 1 ha : aucune des 36 molécules « à substituer », **ou** au moins deux désherbages mécaniques pendant la culture[^ri] | {{ v('ri_eur_ha', 0) }} (16 à 150 €/ha ; 100 €/ha payés en 2024)[^ri] |
| Cultures favorables, légumineuses fourragères (V1_A) | Luzerne, lupuline, sainfoin, lotier, vesce ; aucun insecticide, même en enrobage ; 10 % de zone refuge[^cfe] | {{ v('er_cfe_v1a_eur_ha', 0) }} |
| Cultures favorables, avec bande bordure (V1_B, nouveau) | Même culture, bande bordure adjacente de 10 %[^cfe] [^am-er-2026] | {{ v('er_cfe_v1b_eur_ha', 0) }} |
| Cultures favorables, céréales de printemps, chanvre, sarrasin, tournesol, caméline… (V2) | Aucun insecticide[^cfe] | {{ v('er_cfe_v2_eur_ha', 0) }} |
| Cultures favorables, mélange céréales-légumineuses (V3_A / V3_B) | Au moins 50 % de céréales et 20 % de légumineuses ; récolte après le 31 mai (V3_A) ou le 15 juin (V3_B)[^cfe] | {{ v('er_cfe_v3a_eur_ha', 0) }} / {{ v('er_cfe_v3b_eur_ha', 0) }} |
| Maillage écologique | Haies, arbres, mares, bandes bordures, jachères mellifères convertis en hectares environnementaux ; pas de phyto à moins d'un mètre du pied des haies[^maillage] | {{ v('eco_regime_maillage_eur_he', 0) }}, soit {{ v('haie_eco_regime_eur_km', 0) }} de haie (calculé) |
| Couverture longue du sol | Sol couvert du 1er janvier au 15 février sur 70, 80 ou 90 % de la surface ; payé sur toute la SAU[^cls] | {{ v('er_cls_entree_eur_ha', 0) }}, {{ v('er_cls_intermediaire_eur_ha', 0) }} ou {{ v('er_cls_superieur_eur_ha', 0) }} |
| Prairies permanentes | Garder au moins 80 % des prairies ; aide supplémentaire selon la charge en bétail[^pp] | {{ v('er_pp_base_eur_ha', 0) }} + {{ v('er_pp_supp_eur_ha', 0) }} (0,6 à 2 UGB/ha)[^pp] |

Quelques points pratiques :

- le maillage écologique est plafonné à {{ v('er_maillage_plafond_sau', 0) }} de la SAU. Une bande bordure vaut {{ v('er_maillage_bande_he_ha', 1) }} et une jachère mellifère {{ v('er_maillage_jachere_mellifere_he_ha', 0) }}[^maillage] ;
- la destruction chimique du couvert de l'éco-régime couverture longue sera interdite à partir de 2027[^cls]. Le semis direct qui détruit son couvert au glyphosate perd donc cette aide : c'est un cas où l'aide pousse à supprimer une dépendance, pas à la déplacer ;
- l'obligation de garder 4 % d'éléments non productifs a été supprimée en 2025 : ce volet est devenu volontaire et payé par le maillage écologique[^bcae8].

### Aides couplées

Le **soutien couplé aux protéines végétales** paie {{ v('soutien_proteines_eur_ha', 0) }} prévus (270 à 400 €/ha ; 400 €/ha payés en 2024) pour le soja, le pois, la féverole, le lupin, la lentille ou le pois chiche, purs ou dominants dans un mélange, récoltés après le 15 juin[^couple-prot]. Les aides couplées à l'élevage paient {{ v('couple_viandeux_eur_tete', 0, unite=False) }} € par femelle viandeuse et {{ v('couple_laitiere_eur_tete', 0, unite=False) }} € par vache laitière (montants prévus)[^couple-viande] [^couple-lait].

Le paiement redistributif ({{ v('pac_redistributif_eur_ha', 0) }} prévus sur les 30 premiers hectares)[^redistributif] et l'aide aux jeunes agriculteurs ({{ v('pac_jeune_eur_ha', 0) }} prévus jusqu'à 50 ha)[^jeune] soutiennent le revenu sans lien avec les pratiques.

## PAC, 2e pilier : MAEC, bio, Natura 2000, installation

Ces aides ont un **montant fixe** et un engagement de cinq ans.

| Aide | Ce qui est exigé | Montant 2026 |
|---|---|---|
| MAEC Prairie naturelle (MB2) | Rien du 1er novembre au 15 juin ; ni engrais minéral, ni phyto, ni concentré ; engrais de ferme autorisés[^mb2] | {{ v('maec_mb2_eur_ha', 0) }} |
| MAEC Prairie de haute valeur biologique (MC4) | Avis d'expert, aucun intrant[^mc4] | {{ v('maec_mc4_eur_ha', 0) }} |
| MAEC Tournière enherbée (MB5) | Bande de 10 à 20 m, graminées et au moins trois légumineuses, aucun intrant[^mb5] | {{ v('maec_mb5_eur_ha', 0) }} |
| MAEC Parcelle aménagée (MC7) | Avis d'expert, parcelles de 0,02 à 1,5 ha, ni engrais ni phyto[^mc7] | {{ v('maec_parcelle_amenagee_eur_ha', 0) }} |
| MAEC Autonomie fourragère (MB13) | Moins de 1,4 UGB/ha de surface fourragère ; seuls les effluents de la ferme sont épandus[^mb13] | {{ v('maec_mb13a_eur_ha', 0) }} (30 €/ha sous 1,8 UGB/ha)[^mb13] |
| MAEC Sol (MR14), au résultat | 90 % de la surface engagée ; mesure du carbone organique au début et à la fin[^mr14] | jusqu'à {{ v('maec_mr14_favorable_eur_ha', 0) }} en état « favorable » |
| MAEC Plan d'action (MC10) | Avis d'expert, plan sur cinq ans[^mc10] | 20 €/ha (50 ha au plus) et {{ v('maec_mc10_majoration', 0) }} de toutes les aides environnementales[^mc10] |
| Bio, maintien | Certification bio[^bio] | {{ v('bio_prairie_eur_ha', 0) }} en prairie et fourrages, {{ v('bio_autres_cultures_eur_ha', 0) }} en autres cultures, {{ v('bio_maraichage_eur_ha', 0) }} en maraîchage (premiers hectares) |
| Bio, conversion | Deux premières années[^bio] | + {{ v('bio_conversion_majoration_eur_ha', 0) }} |
| Natura 2000, prairies à contraintes fortes | Cahier des charges de l'unité de gestion[^natura] | {{ v('natura2000_prairie_eur_ha', 0) }} |
| Zone à contraintes naturelles (ICNS) | Ferme en zone défavorisée[^icns] | {{ v('icns_eur_ha', 0) }} sur les 20 premiers hectares |
| Installation d'un jeune agriculteur | 40 ans au plus, plan d'entreprise sur cinq ans[^installation] | {{ v('installation_ja_eur', 0) }} en capital |
| Investissements non productifs | Fascines, noues, mares tampons contre l'érosion[^inp] | 100 % des forfaits, {{ v('inp_plafond_eur', 0) }} au plus sur 2023-2027 |

La MAEC « haies » (MB1) n'existe plus depuis 2023 : les haies, arbres et mares passent par l'éco-régime maillage écologique[^faq-2026]. Le petit maraîchage diversifié bio reçoit un forfait de 4 000 €/ha[^bio].

## Les aides à l'investissement agricole (AII)

### Comment l'aide est calculée

L'AII ne paie pas un pourcentage du prix réel. Elle paie un pourcentage d'un **coût simplifié** fixé pour chaque type d'investissement dans une liste (annexe 3 de l'arrêté), hors TVA, sans dépasser le montant réellement investi[^am-aii].

- Taux de base d'un agriculteur actif : {{ v('aii_taux_base', 0) }}[^am-aii].
- Majorations : + {{ v('aii_maj_av_re', 0) }} si la ligne de la liste coche « architecture verte » ou « résilience économique » (les deux ne se cumulent pas), + {{ v('aii_maj_jeune', 0) }} pour un jeune agriculteur, + {{ v('aii_maj_bio_total', 0) }} pour une ferme totalement bio, + {{ v('aii_maj_herbager', 0) }} pour un système herbager ou en zone à contraintes, et quelques autres (polyculture, moins de 60 ha par membre, filière de qualité)[^am-aii].
- Un agriculteur sans autre majoration touche donc {{ v('aii_taux_pv', 0) }} sur une ligne « architecture verte » (calculé), {{ v('aii_taux_base', 0) }} sur les autres.
- Plafonds : {{ v('aii_plafond_taux', 0) }} du coût simplifié, toutes majorations comprises ; {{ v('aii_plafond_beneficiaire', 0) }} d'aide par bénéficiaire sur 2023-2027 ; bâtiments limités aux 1 000 premiers m²[^am-aii].
- En CUMA, le taux de base est de {{ v('aii_cuma_taux_base', 0) }}, + {{ v('aii_cuma_maj_av_re', 0) }} pour une ligne « architecture verte », + {{ v('aii_cuma_maj_6_membres', 0) }} avec six membres ou plus : {{ v('aii_taux_cuma_av', 0) }} en tout (calculé), avec un seuil de sélection de 5 points[^am-aii].
- Transformation et diversification à la ferme (moulin, atelier, utilitaire réfrigéré) : {{ v('aii_diversif_taux_base', 0) }} de base, + 10 % pour un jeune, + 10 % en bio ou en qualité différenciée[^am-aii].

### Les règles de 2026

- **Seuil de {{ v('aii_seuil_points', 0, unite=False) }} points** pour la demande d'un agriculteur (AM du 15 janvier 2026)[^am-aii]. Points : jeune agriculteur 10, zone à contraintes 5, polyculture 5, bio 4 ou 5, prairie permanente majoritaire 5, moins de 60 ha par membre 2,5, investissement « architecture verte » 5, « résilience économique » 5[^am-aii].
- Un éleveur herbager de moins de 60 ha, ni jeune ni bio, hors zone à contraintes, a 7,5 points (calculé). Il n'atteint pas le seuil pour un tank à lait, dont la ligne ne coche aucun critère. Il l'atteint pour du photovoltaïque seulement si les points « architecture verte » et « résilience » s'additionnent, ce que le texte ne dit pas clairement (voir « À vérifier »).
- **Une seule demande par trimestre**, par appels à projets trimestriels[^agw-aii].
- Ne pas commencer l'investissement avant l'avis de recevabilité. Le réaliser dans les 18 mois, demander le paiement dans les 36 mois[^agw-aii].
- Pendant cinq ans : comptabilité de gestion, maintien de l'investissement, pas de location à des tiers[^agw-aii].

### Quelques coûts simplifiés utiles au projet

| Investissement | Coût simplifié | Cases cochées |
|---|---|---|
| Panneaux photovoltaïques | {{ v('aii_pv_forfait') }} | architecture verte, résilience |
| Biométhanisation de 10 kW au plus | {{ v('aii_biometh_forfait') }} | architecture verte, résilience |
| Herse étrille | {{ v('aii_herse_etrille_forfait') }} | architecture verte |
| Bineuse à guidage par caméra | {{ v('aii_bineuse_camera_forfait') }} | architecture verte |
| Robot de binage autoguidé (jusqu'à 2,5 ha par jour) | {{ v('aii_robot_petit_forfait') }} | architecture verte, résilience |
| Tracteur électrique ou au biogaz de plus de 150 ch | {{ v('aii_tracteur_elec_forfait') }} | architecture verte, résilience |
| Chargeur ou télescopique de moins de 50 ch (toute motorisation) | {{ v('aii_chargeur_50ch_forfait') }} | aucune |
| Hall de séchage pour vrac | {{ v('aii_hall_sechage_forfait') }} | architecture verte, résilience |
| Utilitaire réfrigéré (diversification, toute motorisation) | {{ v('aii_utilitaire_frigo_forfait') }} | résilience |
| Moulin à meules de 50 à 100 cm (diversification) | {{ v('aii_moulin_petit_forfait') }} | résilience |

Source : annexe 3 de l'arrêté ministériel, version en vigueur en 2026[^am-aii] [^aii-liste].

### Ce que l'AII ne finance pas

La liste de 2026 ne contient ni **batterie**, ni **pompe à chaleur**, ni **chaudière biomasse**, ni **récupérateur de chaleur**, ni **pré-refroidisseur** du lait, ni **pompe solaire** ou réseau d'abreuvement, ni **clôture de pâturage**, ni **haie** (hors vergers), ni **toile de paillage**, ni **presse à huile**, ni **vélo-cargo**[^aii-liste]. Elle ne distingue pas l'utilitaire, le télescopique ou le chargeur électrique de leur version diesel. Le tracteur électrique n'a une ligne propre qu'au-delà de 150 ch. La biométhanisation n'y figure que jusqu'à 10 kW[^aii-liste]. Le matériel d'occasion est exclu[^am-aii].

## L'énergie : GREEN, AMUREBA, certificats verts

### GREEN

Les aides GREEN de la Région wallonne paient une part des investissements d'une entreprise dans l'énergie renouvelable ou les économies d'énergie[^green-agw]. L'agriculture ne figure pas parmi les secteurs exclus[^decret-2004], et Valbiom écrit qu'« une entreprise ou un agriculteur » peut obtenir jusqu'à 40 % pour une chaudière biomasse[^valbiom].

| Investissement (PME) | Taux | Coût éligible maximal |
|---|---|---|
| Chaudière biomasse jusqu'à 300 kW | {{ v('green_taux_chaudiere_biomasse', 0) }} | {{ v('green_plafond_chaudiere_kw') }} jusqu'à 100 kW, 880 €/kW de 100 à 300 kW[^green-spw] |
| Pompe à chaleur air-eau ou eau-eau jusqu'à 45 kW thermiques | {{ v('green_taux_pac', 0) }} | 1 320 à 1 760 €/kW selon la puissance[^green-spw] |
| Solaire thermique | {{ v('green_taux_solaire_thermique', 0) }} | 1 320 €/m² jusqu'à 20 m²[^green-spw] |
| Biométhanisation de 10 à 200 kW, consommation sur place | {{ v('green_taux_biometh', 0) }} | {{ v('green_plafond_biometh_kw') }}[^green-spw] |
| Économie d'énergie d'une petite entreprise | {{ v('green_taux_efficacite_petite', 0) }} | exclu si le temps de retour actualisé est de 3 ans ou moins (règle propre aux économies d'énergie)[^green-agw] |

Les conditions pèsent lourd pour une ferme :

- investissement d'au moins {{ v('green_seuil_pme', 0) }} pour une PME[^green-agw] ;
- **audit ou étude de faisabilité AMUREBA** par un auditeur agréé, exigé pour tous les programmes depuis 2026, avec compteurs d'énergie[^green-agw] [^amureba-memo] ;
- demande avant le début des travaux ; passeport entreprise[^green-agw] ;
- **exclus** : photovoltaïque, biométhanisation de moins de 10 kW, batteries, tout équipement qui brûle un combustible fossile[^green-agw].

### AMUREBA

La Région subventionne l'audit ou l'étude exigés par GREEN : {{ v('amureba_taux_pme', 0) }} du coût hors TVA pour une PME, avec un plafond de 20 000 € pour une étude de faisabilité sur la chaleur[^amureba]. Un passage à 50 % pour tous était annoncé pour « mi-2026 au mieux »[^amureba-memo] ; il n'était pas publié au 27 novembre 2026. L'accès d'une exploitation agricole à cette subvention, soumise à la règle *de minimis*, reste à vérifier.

### Certificats verts

Une installation d'électricité renouvelable de plus de 10 kW reçoit des certificats verts, sur réservation préalable[^cv-cpma]. Pour les demandes introduites en 2025 :

- biométhanisation jusqu'à 200 kW avec plus de 50 % d'effluents d'élevage : {{ v('cv_biogaz_taux', 1) }}, le maximum légal[^cv-tableau] ;
- photovoltaïque de 10 à 1 000 kW : {{ v('cv_pv_taux', 3) }}[^cv-tableau].

Elia rachète chaque certificat au prix garanti de {{ v('cv_prix_garanti', 0) }}[^cv-rapport]. Le photovoltaïque gagne donc {{ v('pv_cv_eur_mwh', 1) }} produit (calculé) ; pour les {{ v('pv_ferme_kwc', 0) }} de la ferme type, environ {{ v('pv_ferme_cv_an', 0) }} (calculé). Les taux 2026 et la durée d'octroi n'étaient pas publiés au 27 novembre 2026.

## Les autres aides

- **Plantation de haies.** La Région paie {{ v('haie_subv_1rang', 0) }} de haie d'un rang, {{ v('haie_subv_2rangs', 0) }} de deux rangs, 9 €/m de trois rangs ; ces montants sont multipliés par {{ v('haie_subv_majoration_entreprise', 1, unite=False) }} si une entreprise plante, sans dépasser 80 % des factures[^haies]. Un kilomètre de haie double reçoit {{ v('haie_plantation_subv_km', 0) }} à la plantation (calculé), puis {{ v('haie_eco_regime_eur_km', 0) }} d'éco-régime (calculé). Conditions : au moins 100 m, trois espèces, paillage biodégradable[^haies].
- **Halls relais agricoles.** Un promoteur (commune, ou structure qui valorise des produits agricoles) peut recevoir {{ v('hra_taux_base', 0) }} des investissements, plus deux bonus de 15 % au maximum, jusqu'à 200 000 €, pour un atelier partagé par des agriculteurs[^hra]. Il n'y a pas d'aide directe à un agriculteur seul, et aucun appel n'a été trouvé pour 2026.
- **Déduction fédérale pour investissement.** Un indépendant ou une petite société déduit de ses bénéfices imposables {{ v('dpi_thematique_pp', 0) }} du prix d'un investissement « thématique » : énergie (stockage compris), transport sans émission, environnement[^dpi-barreau]. Les camionnettes et vélos-cargo électriques neufs, à usage exclusivement professionnel, y ont droit avec une attestation du SPF Mobilité depuis avril 2026, pour les achats faits depuis 2025[^dpi-tm] [^dpi-itaa]. Exemple du ministre : pour une camionnette de 40 000 €, environ 4 000 € d'impôt en moins pour une société et plus de 8 000 € pour un indépendant[^dpi-tm]. Cette aide **ne joue que pour un exploitant imposé sur ses bénéfices réels** : elle n'aide pas un agriculteur imposé au forfait (point non vérifié sur le texte du SPF Finances).

## Les règles de cumul

- **AII et autres aides wallonnes.** Le bénéficiaire de l'AII ne demande aucune autre aide wallonne pour ses investissements pendant cinq ans. Exception depuis janvier 2026 : les soutiens régionaux à la production d'énergie renouvelable[^agw-aii]. Lecture de ce projet, à confirmer : les certificats verts restent compatibles avec l'AII, une aide GREEN « économie d'énergie » ne l'est pas.
- **GREEN.** Pas de cumul avec une autre aide régionale pour le même programme d'investissements[^decret-2004]. Le cumul avec la déduction fédérale n'était « pas encore finalisé » en février 2026[^amureba-memo].
- **AII et installation.** L'aide à l'installation et l'AII se cumulent[^agw-aii].
- **Cultures favorables et protéagineux.** L'éco-régime cultures favorables et le soutien couplé aux protéagineux ne se cumulent pas sur une même parcelle[^cumuls].
- **Réduction d'intrants.** Pas sur une parcelle bio ; pas avec les variantes V2_A et V3 des cultures favorables ; cumulable avec le soutien couplé aux protéagineux[^ri] [^cumuls].
- **Maillage écologique.** Pas sur les surfaces en MAEC MB5, MC7 ou MB12, sauf les arbres et haies qui s'y trouvent[^maillage]. MB5, MC7 et MB12 ensemble : 25 % des terres arables au plus[^mb5].
- **Bio.** Pas d'aide bio sur les jachères, bandes bordures, tournières et parcelles aménagées ; cumulable avec les cultures favorables, la couverture longue, les prairies permanentes, MB13 et le soutien couplé aux protéagineux[^bio] [^cumuls].
- **Haies.** Le cumul de la subvention à la plantation et de l'éco-régime n'est pas traité par l'arrêté (à vérifier).

## Quelle aide pour quelle alternative

Les chiffres « avec aide » sont calculés avec les montants prévus et les hypothèses du projet ; ils sont détaillés dans [les calculs](calculs.md).

| Alternative | Aide | Effet sur la rentabilité (calculé) |
|---|---|---|
| [Micro-biométhanisation](fiches/energie/electricite-reseau.md) (20 kW) | Certificats verts ; GREEN de 10 à 200 kW (AII jusqu'à 10 kW) | Retour de {{ v('microbiometh_retour_ans', 0) }} sans soutien, {{ v('microbiometh_retour_cv_ans', 1) }} avec les certificats verts ({{ v('microbiometh_cv_an', 0) }}), {{ v('microbiometh_retour_aides_ans', 1) }} avec GREEN en plus ({{ v('microbiometh_aide_invest', 0) }}) ; {{ fourchette('microbiometh_retour_aides_ans', 1) }} selon le prix de l'électricité. Reste en vague 2 : dépend d'aides dont le taux 2026 n'est pas publié. |
| [Photovoltaïque](fiches/energie/electricite-reseau.md) | AII ; certificats verts au-delà de 10 kW ; déduction fédérale au régime réel | AII déjà comptée ({{ v('pv_ferme_aide_aii', 0) }} pour la ferme type) ; certificats verts : {{ v('pv_ferme_cv_an', 0) }}. Vague 1 inchangée. |
| [Batterie](fiches/energie/electricite-reseau.md) | Ni AII ni GREEN ; déduction fédérale seulement | Pas de changement. |
| [Chaudière à plaquettes](fiches/energie/chauffage-mazout.md) (50 kW, 8 000 L de mazout) | GREEN {{ v('green_taux_chaudiere_biomasse', 0) }} (audit AMUREBA) | Aide de {{ v('chaudiere_aide_green', 0) }}. Retour de {{ v('chaudiere_retour_ans', 1) }} sans aide, {{ v('chaudiere_retour_green_ans', 1) }} avec. Au prix d'avant-crise : {{ v('chaudiere_retour_ans', 0, scenario='bas') }} sans aide, {{ v('chaudiere_retour_green_ans', 1, scenario='bas') }} avec. Vague 1 confirmée, plus solide avec l'aide. |
| [Pompe à chaleur](fiches/energie/chauffage-mazout.md) | GREEN {{ v('green_taux_pac', 0) }} jusqu'à 45 kW thermiques | Améliore le chauffage ; à chiffrer dans la fiche. |
| [Chaudière biomasse pour le séchage](fiches/energie/sechage-grains.md) (500 t de maïs) | GREEN {{ v('green_taux_chaudiere_biomasse', 0) }} jusqu'à 300 kW | Installation remboursée en {{ v('duree_retour_visee', 0) }} (hypothèse) : {{ v('sechage_chaudiere_invest_max', 0) }} au plus sans aide, {{ v('sechage_chaudiere_invest_max_green', 0) }} avec GREEN. Reste en vague 2 tant que le prix d'une installation de cette taille n'est pas connu. |
| [Pré-refroidisseur, récupérateur de chaleur](fiches/elevage/tank-a-lait.md) | En pratique aucune (absents de l'AII ; GREEN exige 20 000 € et un retour de plus de 3 ans) | Vague 1 sans aide. |
| [Séchoir en grange](fiches/elevage/fourrages-recoltes.md) | AII : hall de séchage {{ v('aii_hall_sechage_forfait') }} (architecture verte) | Effet modeste ; vague 2 inchangée. |
| [Pâturage, prairies](fiches/elevage/fourrages-recoltes.md) | Éco-régime prairies permanentes ; MB13 ; MB2 ; bio | {{ v('er_pp_base_eur_ha', 0) }} + {{ v('er_pp_supp_eur_ha', 0) }}, plus {{ v('maec_mb13a_eur_ha', 0) }} en MB13A. |
| [Désherbage mécanique du maïs](fiches/protection/herbicides.md) | Éco-régime réduction d'intrants (pas en bio) ; AII herse et bineuse | Surcoût de {{ v('mais_meca_surcout_ha', 0) }} sans aide ; avec l'éco-régime, le bilan passe à {{ v('mais_meca_bilan_ri_ha', 0) }} (négatif : le mécanique revient moins cher que le chimique). Même au montant minimum de l'éco-régime (16 €/ha)[^ri], le mécanique reste moins cher. Vague 1 confirmée, sauf en bio (pas d'éco-régime). |
| [Robot de binage](fiches/protection/herbicides.md) | AII ({{ v('aii_taux_pv', 0) }} seul, {{ v('aii_taux_cuma_av', 0) }} en CUMA) | Aide de {{ v('farmdroid_aide_aii', 0) }} seul, {{ v('farmdroid_aide_cuma', 0) }} en CUMA ; amortissement de {{ v('farmdroid_amort_eur_ha') }} à {{ v('farmdroid_amort_eur_ha_aii') }}. Vague 2 inchangée ; la voie CUMA aide plus. |
| [Pois, féverole](fiches/elevage/concentres-importes.md) | Soutien couplé + réduction d'intrants, **ou** cultures favorables V3 en mélange (non cumulables) | Pois ou féverole purs : {{ v('proteagineux_aides_ha', 0) }} ; mélange céréales-légumineuses récolté après le 15 juin : {{ v('er_cfe_v3b_eur_ha', 0) }}. La voie du soutien couplé paie {{ v('proteagineux_ecart_v3b_ha', 0) }} de plus (calculé), si la parcelle remplit les conditions de la réduction d'intrants. |
| [Légumineuses fourragères](fiches/fertilisation/azote-synthese.md) (luzerne, lupuline, sainfoin…) | Cultures favorables V1 ; bio | {{ v('er_cfe_v1a_eur_ha', 0) }} prévus, en plus de l'azote fixé ({{ v('valeur_n_fixe', 0) }}). |
| [Couverts et semis direct](fiches/traction/tracteur-diesel.md) | Couverture longue du sol ; MAEC Sol | Destruction chimique interdite à partir de 2027 pour l'éco-régime. |
| [Haies et auxiliaires](fiches/protection/fongicides-insecticides.md) | Subvention à la plantation ; maillage écologique ; MC7, MB5 | {{ v('haie_plantation_subv_km', 0) }} à la plantation, puis {{ v('haie_eco_regime_eur_km', 0) }}. |
| [Tracteur électrique](fiches/traction/tracteur-diesel.md) | AII seulement au-delà de 150 ch | Environ {{ v('aii_taux_pv', 0) }} de {{ v('aii_tracteur_elec_forfait', 0) }} ; pas de ligne pour le tracteur compact. Pas de changement de vague. |
| [Télescopique, chargeur électrique](fiches/traction/engins-de-cour.md) | AII au même forfait que le diesel | Pas de changement. |
| [Utilitaire électrique](fiches/transport/vehicules-livraison.md) | Déduction fédérale de {{ v('dpi_thematique_pp', 0) }}, **au régime réel seulement** | Pour un indépendant imposé à {{ v('ipp_taux_marginal', 0) }} (hypothèse), l'impôt économisé vaut {{ v('utilitaire_dpi_part_prix', 0) }} du prix (calculé). L'électrique neuf se rembourse par l'énergie jusqu'à un diesel équivalent de {{ v('utilitaire_prix_max_neuf_dpi', 0) }}, contre {{ v('utilitaire_prix_max_neuf', 0) }} sans la déduction. Vague 1 renforcée au régime réel ; rien pour un agriculteur au forfait. |
| [Moulin, atelier, légumerie](fiches/transformation/transformation-industrielle.md) | AII diversification ({{ v('aii_diversif_taux_base', 0) }} de base) ; halls relais en collectif | Renforce la voie collective ; pas de changement de vague. |
| [Presse à huile](fiches/transformation/transformation-industrielle.md) | Aucune ligne AII ; halls relais seulement | Pas de changement. |
| [Pompe solaire, clôtures](fiches/eau/irrigation-pompes.md) | Aucune aide trouvée | Pas de changement. |

## À vérifier

- Montants **payés** pour 2025 et 2026 des éco-régimes et aides couplées : seuls ceux de 2024 sont publiés.
- Taux d'octroi des certificats verts pour les demandes de 2026, et durée d'octroi.
- Effet d'une aide GREEN sur le taux d'octroi des certificats verts d'une biométhanisation : les paramètres de référence du régime Cpma comptent un « taux de subsidiation » de l'investissement[^am-cpma]. À demander au SPW Énergie.
- Cumul des certificats verts et de GREEN pour un même méthaniseur (règle de non-cumul des aides régionales du décret de 2004).
- Les points « architecture verte » et « résilience économique » s'additionnent-ils dans la sélection AII ? À demander à l'Organisme payeur de Wallonie.
- Plafond de 40 % pour l'AII à la transformation et à la diversification (écrit pour l'investissement productif, pas retrouvé à l'article 15).
- Accès d'une exploitation agricole à la subvention AMUREBA de 75 % (règle *de minimis*) et passage annoncé à 50 %.
- Déduction fédérale pour investissement : texte du SPF Finances (site inaccessible), cas de l'agriculteur au forfait, éligibilité d'un tracteur ou d'un télescopique électrique, cumul avec GREEN.
- Cumul de la subvention à la plantation de haies et de l'éco-régime maillage écologique.
- Appel 2026 aux halls relais agricoles.
- Montant 2026 de l'ICNS (page de 2024).
- Les montants de GREEN viennent du tableau du SPW Économie : l'annexe officielle de l'arrêté n'a pas pu être lue (texte illisible à l'extraction).

## Sources

Toutes les sources ont été consultées le 27 novembre 2026.

[^ri]: « Eco-régime réduction d'intrants », Portail de l'agriculture wallonne, page modifiée le 3 juillet 2026. https://agriculture.wallonie.be/home/aides/pac-2023-2027-description-des-interventions/eco-regimes/eco-regime-reduction-d-intrants.html
[^cfe]: « Eco-régime cultures favorables à l'environnement », Portail de l'agriculture wallonne, page modifiée le 17 avril 2026. https://agriculture.wallonie.be/home/aides/pac-2023-2027-description-des-interventions/eco-regimes/eco-regime-culture-favorable-a-l-environnement.html
[^am-er-2026]: Arrêté ministériel du 15 janvier 2026 modifiant l'arrêté ministériel du 23 février 2023 relatif aux éco-régimes, Wallex. https://wallex.wallonie.be/eli/arrete/2026/01/15/2026200467/2026/01/01
[^maillage]: « Eco-régime maillage écologique », Portail de l'agriculture wallonne, page modifiée le 17 avril 2026. https://agriculture.wallonie.be/home/aides/pac-2023-2027-description-des-interventions/eco-regimes/eco-regime-maillage-ecologique.html
[^cls]: « Eco-régime couverture longue du sol », Portail de l'agriculture wallonne, page modifiée le 17 avril 2026. https://agriculture.wallonie.be/home/aides/pac-2023-2027-description-des-interventions/eco-regimes/eco-regime-couverture-longue-du-sol.html
[^pp]: « Eco-régime prairies permanentes conditionné à la charge en bétail », Portail de l'agriculture wallonne, page modifiée le 17 avril 2026. https://agriculture.wallonie.be/home/aides/pac-2023-2027-description-des-interventions/eco-regimes/eco-regime-prairies-permanentes-conditionnee-a-la-charge-en-betail.html
[^bcae8]: « BCAE 8 Maintien des particularités topographiques et interdiction de tailler les haies », Portail de l'agriculture wallonne, page modifiée le 9 avril 2026. https://agriculture.wallonie.be/home/aides/pac-2023-2027-description-des-interventions/conditionnalite-renforcee/bcae-8-maintien-des-particularites-topographiques-et-interdiction-de-tailler-les-haies.html
[^couple-prot]: « Soutien couplé aux cultures de protéines végétales », Portail de l'agriculture wallonne, page modifiée le 21 novembre 2025. https://agriculture.wallonie.be/home/aides/pac-2023-2027-description-des-interventions/soutien-couple/soutien-couple-aux-cultures-de-proteines-vegetales.html
[^couple-viande]: « Soutien couplé aux bovins femelles viandeux », Portail de l'agriculture wallonne, page modifiée le 21 novembre 2025. https://agriculture.wallonie.be/home/aides/pac-2023-2027-description-des-interventions/soutien-couple/soutien-couple-aux-bovins-femelles-viandeux.html
[^couple-lait]: « Soutien couplé aux vaches laitières », Portail de l'agriculture wallonne, page modifiée le 21 novembre 2025. https://agriculture.wallonie.be/home/aides/pac-2023-2027-description-des-interventions/soutien-couple/soutien-couple-aux-vaches-laitieres.html
[^redistributif]: « Paiement redistributif », Portail de l'agriculture wallonne, page modifiée le 3 avril 2025. https://agriculture.wallonie.be/home/aides/pac-2023-2027-description-des-interventions/paiement-de-base-paiement-redistributif-et-paiement-jeune/paiement-redistributif1.html
[^jeune]: « Aide complémentaire au revenu pour les jeunes agriculteurs », Portail de l'agriculture wallonne, page modifiée le 3 avril 2025. https://agriculture.wallonie.be/home/aides/pac-2023-2027-description-des-interventions/paiement-de-base-paiement-redistributif-et-paiement-jeune/aide-complementaire-au-revenu-pour-les-jeunes-agriculteurs.html
[^mb2]: « MAEC Prairie naturelle – MB2 », Portail de l'agriculture wallonne, page modifiée le 17 avril 2026. https://agriculture.wallonie.be/home/aides/pac-2023-2027-description-des-interventions/mesures-agro-environnementales-et-climatiques/maec-prairie-naturelle---mb2.html
[^mc4]: « MAEC Prairie à haute valeur biologique – MC4 », Portail de l'agriculture wallonne, page modifiée le 17 avril 2026. https://agriculture.wallonie.be/home/aides/pac-2023-2027-description-des-interventions/mesures-agro-environnementales-et-climatiques/maec-prairie-a-haute-valeur-biologique---mc4.html
[^mb5]: « MAEC Tournières enherbées – MB5 », Portail de l'agriculture wallonne, page modifiée le 17 avril 2026. https://agriculture.wallonie.be/home/aides/pac-2023-2027-description-des-interventions/mesures-agro-environnementales-et-climatiques/maec-tournieres-enherbees---mb5.html
[^mc7]: « MAEC Parcelles aménagées – MC7 », Portail de l'agriculture wallonne, page modifiée le 17 avril 2026. https://agriculture.wallonie.be/home/aides/pac-2023-2027-description-des-interventions/mesures-agro-environnementales-et-climatiques/maec-parcelles-amenagees---mc7.html
[^mb13]: « MAEC Autonomie fourragère – MB13 », Portail de l'agriculture wallonne, page modifiée le 17 avril 2026. https://agriculture.wallonie.be/home/aides/pac-2023-2027-description-des-interventions/mesures-agro-environnementales-et-climatiques/maec-autonomie-fourragere---mb13.html
[^mr14]: « MAEC Sol – MR14 », Portail de l'agriculture wallonne, page modifiée le 4 juin 2026. https://agriculture.wallonie.be/home/aides/pac-2023-2027-description-des-interventions/mesures-agro-environnementales-et-climatiques/maec-sol---mr14.html
[^mc10]: « MAEC Plan d'action agro-environnemental », Portail de l'agriculture wallonne, page modifiée le 17 avril 2026. https://agriculture.wallonie.be/home/aides/pac-2023-2027-description-des-interventions/mesures-agro-environnementales-et-climatiques/maec-plan-d-action-agro-environnemental.html
[^bio]: « Soutien à l'agriculture biologique », Portail de l'agriculture wallonne, page modifiée le 17 avril 2026. https://agriculture.wallonie.be/home/aides/pac-2023-2027-description-des-interventions/soutien-a-l-agriculture-biologique.html
[^natura]: « Paiement Natura 2000 en zone agricole », Portail de l'agriculture wallonne, page modifiée le 16 décembre 2024. https://agriculture.wallonie.be/home/aides/pac-2023-2027-description-des-interventions/paiements-natura-2000-nouveaute-2025/paiement-natura-2000-en-zone-agricole.html
[^icns]: « Paiements en faveur des zones soumises à des contraintes naturelles ou spécifiques », Portail de l'agriculture wallonne, page modifiée le 20 août 2024. https://agriculture.wallonie.be/home/aides/pac-2023-2027-description-des-interventions/paiements-en-faveur-des-zones-soumises-a-des-contraintes-naturelles-ou-specifiques.html
[^installation]: « Aides à l'installation des jeunes agriculteurs », Portail de l'agriculture wallonne, page modifiée le 6 février 2026. https://agriculture.wallonie.be/home/aides/pac-2023-2027-description-des-interventions/installation-des-jeunes-agriculteurs/aides-a-l-installation-des-jeunes-agriculteurs.html
[^inp]: « Aides aux investissements non-productifs dans les exploitations agricoles », Portail de l'agriculture wallonne, page modifiée le 17 avril 2026. https://agriculture.wallonie.be/home/aides/pac-2023-2027-description-des-interventions/aides-aux-investissements/aides-aux-investissements-non-productifs-dans-les-exploitations-agricoles.html
[^faq-2026]: « FAQ 2ième Pilier – Mesures surfaciques – Campagne 2026 », SPW ARNE, version « 150425 ». https://agriculture.wallonie.be/files/accueil/Aides/FAQ/FAQ%202i%c3%a8me%20Pilier%20Mesures%20surfaciques%20-%20Campagne%202026.pdf
[^cumuls]: « Cumuls entre les aides », Portail de l'agriculture wallonne, page modifiée le 18 septembre 2025 (tableaux « prairie » et « culture »). https://agriculture.wallonie.be/home/aides/pac-2023-2027-description-des-interventions/cumuls-entre-les-aides.html
[^am-aii]: Arrêté ministériel du 23 février 2023 exécutant l'arrêté du Gouvernement wallon du 23 février 2023 relatif aux aides à l'installation et aux investissements, version consolidée (modifications des 15 janvier et 11 mai 2026) : articles 3 à 6, 15 et 18, annexes 2 et 3. Wallex. https://wallex.wallonie.be/eli/arrete/2023/02/23/2023042748
[^agw-aii]: Arrêté du Gouvernement wallon du 23 février 2023 relatif aux aides à l'installation et aux investissements, version en vigueur depuis le 1er janvier 2026 : articles 5 à 12 et 36. Wallex. https://wallex.wallonie.be/eli/arrete/2023/02/23/2023042313/2026/01/01
[^aii-liste]: « Liste des investissements admissibles », SPW Agriculture, janvier 2026. https://agriculture.wallonie.be/files/accueil/Aides/AII/outils/Liste%20des%20investissements%20admissibles.pdf
[^green-agw]: Arrêté du Gouvernement wallon du 23 mai 2024 relatif aux primes à l'investissement (aides GREEN), en vigueur le 1er janvier 2025 : articles 4 à 16 et 26. Wallex. https://wallex.wallonie.be/sites/wallex/contents/acts/108/108350/1.html
[^green-spw]: « Réforme des aides spécifiques à la protection de l'environnement et à l'utilisation de l'énergie », SPW Économie, Emploi, Recherche, publié le 28 novembre 2024, mis à jour le 23 janvier 2025. https://economie.wallonie.be/fr/home/actualites/actualites/reforme-des-aides-specifiques-a-la-protection-de-l-environnement-et-a-l-utilisation-de-l-energie.html
[^decret-2004]: Décret du 11 mars 2004 relatif aux incitants régionaux en faveur des petites ou moyennes entreprises, version en vigueur depuis le 1er janvier 2025, article 3. Wallex. https://wallex.wallonie.be/eli/loi-decret/2004/03/11/2004200990
[^valbiom]: « Installer une chaudière biomasse pour me chauffer ? J'y pense ! », Les Carnets de Valbiom n° 5, juin 2025, hébergé par le SPW Énergie. https://energie.wallonie.be/files/%c3%89nergies%20vertes/Bio%c3%a9nergie/Poele%20chaudiere/installer-une-chaudiere-biomasse-pour-se-chauffer-2025.pdf
[^amureba]: Arrêté du Gouvernement wallon du 1er février 2024 relatif à l'octroi de subventions à l'audit ou à l'étude dans le secteur non résidentiel (AMUREBA), annexe 5. Wallex. https://wallex.wallonie.be/eli/arrete/2024/02/01/2024004275
[^amureba-memo]: « Mémo Table ronde des auditeurs du 6 février 2026 », SPW Énergie. https://energie.wallonie.be/files/Actualit%c3%a9s/20260206_m%c3%a9mo%20Table%20ronde%20auditeurs.pdf
[^cv-cpma]: « Régime Cpma », SPW Énergie (plafond de 2,5 certificats verts par MWh, exclusion du photovoltaïque de moins de 10 kW). https://energie.wallonie.be/home/soutiens-financiers/soutien-a-la-production-d-electricite-verte/mecanismes-de-soutien/regime-cpma.html
[^cv-tableau]: « Tableau récapitulatif des taux d'octroi forfaitaires applicables aux nouvelles installations pour les demandes introduites en 2025 », SPW Énergie. https://energie.wallonie.be/files/Soutiens%20financiers/%c3%a9lectricit%c3%a9%20verte/M%c3%a9canismes%20de%20soutiens/R%c3%a9gime%20CPMA/Tableau%20nouvelles%20installations%20-%20Taux%20octrois%20et%20CPMA%20des%20cat%c3%a9gories%20-%202025.pdf
[^cv-rapport]: « Rapport marché CV 2025 T3-T4 », SPW Énergie, 12 juin 2026. https://energie.wallonie.be/files/Les%20march%c3%a9s/Les%20CV/Rapports%20trimestriels/rapport-marche-cv-2025-t3_t4.pdf
[^am-cpma]: Arrêté ministériel du 1er octobre 2025 fixant les valeurs de référence et les taux d'octroi de certificats verts (méthodologies Cpma), version consolidée au 19 juin 2026, copie non officielle de la base Justel (refli.be). https://refli.be/en/lex/2025008208
[^haies]: Arrêté du Gouvernement wallon du 8 septembre 2016 relatif à l'octroi de subventions pour la plantation d'une haie vive, d'un taillis linéaire, d'un verger et d'alignements d'arbres, version en vigueur depuis le 15 avril 2024, annexe. Wallex. https://wallex.wallonie.be/sites/wallex/contents/acts/3/3890/3.html
[^hra]: Arrêté du Gouvernement wallon du 30 août 2018 fixant les conditions d'octroi des subventions relatives aux halls relais agricoles, version en vigueur depuis le 9 novembre 2023. Wallex. https://wallex.wallonie.be/sites/wallex/contents/acts/3/3926/2.html
[^dpi-barreau]: « Nouvelle déduction pour investissement à partir de 2025 : cap sur la durabilité et le numérique », Barreau de Liège-Huy, 12 juin 2025. https://barreaudeliege-huy.be/fr/actualites/nouvelle-deduction-pour-investissement-partir-de-2025-cap-sur-la-durabilite-et-le
[^dpi-tm]: « Véhicules à zéro émissions : la déduction pour investissement est opérationnelle », Transportmedia, 1er avril 2026. https://transportmedia.be/fr/2026/04/vehicules-a-zero-emissions-la-deduction-pour-investissement-est-operationnelle/
[^dpi-itaa]: « Déduction pour investissement : nouvelle procédure d'attestation pour les véhicules zéro émission », blog de l'ITAA, 15 avril 2026. https://www.blogitaa.be/fr/2026/04/15/deduction-pour-investissement-nouvelle-procedure-dattestation-pour-les-vehicules-zero-emission/
