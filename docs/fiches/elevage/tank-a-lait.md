---
id: tank-a-lait
titre: Refroidissement du lait
domaine: élevage
dependance_fossile: électricité
alternatives: [Pré-refroidisseur, récupérateur de chaleur]
vague_meilleure_alternative: 1
statut: relu
maj: 2026-11-27
---

# Refroidissement du lait

## En bref

Le lait sort de la vache à environ 37 °C et doit être refroidi sous 4 °C dans le tank[^rundveeloket]. Le tank est le premier poste électrique du bloc traite[^reussir-mc]. Le fossile entre par l'électricité du réseau, en partie produite au gaz. Deux équipements simples et éprouvés réduisent la facture : le pré-refroidisseur, qui refroidit le lait avec l'eau d'abreuvement, et le récupérateur de chaleur, qui chauffe l'eau de lavage avec la chaleur du tank. Les deux sont rentables aujourd'hui (vague 1) : un pré-refroidisseur simple se rembourse en 3 à 5 ans, le récupérateur surtout au-delà d'environ 500 000 L de lait par an.

## Comment ça marche aujourd'hui

Le tank est une cuve isolée avec un groupe frigorifique : un compresseur électrique extrait la chaleur du lait et la rejette dans l'air par un condenseur. Sans pré-refroidissement, il faut environ 14 kWh d'électricité pour refroidir 1 000 L de lait selon Inagro[^inagro], 15 kWh selon Rundveeloket et une brochure du Département flamand de l'agriculture[^rundveeloket][^ilvo], 13 à 15 kWh selon un manuel néerlandais[^handboek]. Pour une exploitation qui livre {{ v('lait_livre_an') }} (hypothèse), cela fait environ {{ v('tank_kwh_an', 0) }} (calculé).

L'eau chaude de lavage de la machine à traire et du tank est souvent produite par un chauffe-eau électrique, parfois par la chaudière au mazout.

## Où entrent le pétrole et le gaz

- **Électricité** : en 2025, les centrales au gaz ont produit 12,6 TWh, soit 19 % de la production d'électricité en Belgique, selon le bilan annuel provisoire d'Elia, le gestionnaire du réseau de transport[^elia-2025]. Le prix de l'électricité suit en partie celui du gaz (voir la fiche [Électricité du réseau](../energie/electricite-reseau.md)).
- **Eau chaude** : au mazout ou au gaz sur certaines exploitations.
- **Fluide frigorigène** : gaz fluoré de synthèse, issu de la chimie.
- **Collecte du lait** : camion-citerne au gasoil (hors exploitation).

## Les alternatives

### 1. Pré-refroidisseur (vague 1)

Un échangeur à plaques fait passer le lait d'un côté et l'eau froide du puits ou du réseau de l'autre. Le lait arrive dans le tank vers 15 à 20 °C au lieu de 33 °C[^inagro]. L'eau, réchauffée de quelques degrés, part à l'abreuvement : les vaches boivent volontiers après la traite.

Le pré-refroidisseur économise environ {{ v('prerefroidisseur_gain', 0) }} de l'électricité du tank selon Rundveeloket et le manuel néerlandais, et jusqu'à 50 % selon Inagro, suivant la taille de l'échangeur et la température de l'eau[^rundveeloket][^handboek][^inagro]. Pour l'exploitation type (calculé) :

- électricité économisée : {{ v('prerefroidisseur_kwh_an') }} ;
- économie : {{ v('prerefroidisseur_eur_an') }} au prix du réseau ({{ fourchette('prerefroidisseur_eur_an') }} selon les scénarios).

Le prix d'un pré-refroidisseur va de 4 000 à 10 000 € selon l'installation (prix français)[^reussir-eco]. Rundveeloket estime l'investissement amorti en 3 à 4 ans sur la plupart des exploitations[^rundveeloket] ; des sources françaises donnent 2 à 7 ans[^reussir-mc]. Avec le calcul ci-dessus, un appareil à {{ v('prerefroidisseur_prix_bas', 0) }} se rembourse en {{ v('prerefroidisseur_retour_bas_ans', 1) }} au prix actuel de l'électricité ({{ fourchette('prerefroidisseur_retour_bas_ans', 1) }} selon les scénarios, calculé, hors entretien) : il reste rentable au prix d'avant-crise. Un appareil à {{ v('prerefroidisseur_prix_haut', 0) }} demande en revanche {{ fourchette('prerefroidisseur_retour_haut_ans', 0) }} selon les scénarios (calculé). Le retour est plus rapide sur les grandes exploitations et quand le tank est petit pour le volume livré.

Conditions :

- de l'eau en quantité : au moins 1 L d'eau par litre de lait, de préférence 1,5 à 2 L selon Inagro[^inagro] ; Rundveeloket conseille 2 à 2,5 L pour un fonctionnement optimal[^rundveeloket] ;
- un usage de cette eau, sinon on la gaspille : abreuvement, lavage des aires. Au pâturage, l'eau tiède s'accumule sans emploi et certains éleveurs arrêtent alors le pré-refroidisseur, ce qui annule le gain[^reussir-eco] ;
- de l'eau froide : plus l'eau est froide, mieux le lait est refroidi. L'eau de forage (10 à 12 °C) refroidit mieux que l'eau de pluie (14 à 15 °C, jusqu'à 20 °C si elle circule)[^rundveeloket].

### 2. Récupérateur de chaleur (vague 1)

Un échangeur placé sur le circuit frigorifique du tank récupère la chaleur extraite du lait pour préchauffer l'eau d'un ballon vers 55 °C. Il économise 60 à 90 % de l'électricité du chauffe-eau selon des conseillers français[^reussir-eco] ; le manuel néerlandais parle de jusqu'à 50 % de l'énergie de chauffe de l'eau[^handboek]. Le chauffe-eau reste nécessaire en appoint pour le lavage à chaud. Le récupérateur produit 0,3 à 0,8 L d'eau à 55 °C par litre de lait. En contrepartie, le groupe froid consomme un peu plus : 15 à 17 kWh par 1 000 L au lieu de 13 à 15[^handboek].

Coût : 5 000 à 6 000 € pose comprise selon l'Institut de l'élevage (prix français)[^reussir-eco] ; un exemple français à 7 100 € posé sur un tank de 30 000 L (échangeurs, ballon, circuit et pose)[^reussir-recup]. Le retour est de 2 à 5 ans selon l'Institut de l'élevage[^reussir-recup], mais dépasse 5 ans en dessous d'environ 500 000 L de lait par an[^reussir-eco] : le résultat dépend du volume d'eau chaude réellement utilisé.

Conditions :

- poser par un frigoriste, car on intervient sur le circuit du tank ;
- si la laiterie est propriétaire du tank, son accord est nécessaire (pratique française, à vérifier en Belgique)[^reussir-traite] ;
- un besoin d'eau chaude régulier.

### Aides : presque aucune

Le pré-refroidisseur et le récupérateur de chaleur n'ont presque pas d'aide accessible pour une exploitation (voir [les aides publiques](../../aides.md#ce-que-laii-ne-finance-pas)) :

- **AII** : la liste des investissements admissibles de 2026 ne contient ni pré-refroidisseur ni récupérateur de chaleur[^aii-liste]. Seul le tank lui-même a une ligne, sans case « architecture verte » ni « résilience économique ». Avec le seuil de sélection de {{ v('aii_seuil_points', 0, unite=False) }} points, un éleveur herbager de moins de 60 ha, ni jeune ni bio, hors zone à contraintes, n'a que 7,5 points (calculé à partir des points de l'arrêté) et n'atteint pas le seuil pour cette ligne[^am-aii].
- **GREEN** (économie d'énergie) : l'investissement doit atteindre au moins {{ v('green_seuil_pme', 0) }} pour une PME, un audit AMUREBA est exigé depuis 2026, et un investissement dont le temps de retour actualisé est de 3 ans ou moins est exclu[^green-agw]. Un pré-refroidisseur ou un récupérateur coûte nettement moins que ce seuil et se rembourse souvent en 3 à 5 ans : il n'entre pas dans GREEN, sauf peut-être au sein d'un programme d'économie d'énergie plus large (à vérifier). GREEN cite pourtant la récupération de chaleur sur un processus de production comme investissement admissible[^green-brochure]. L'audit AMUREBA n'est pas subventionné pour l'activité agricole : la subvention relève du règlement *de minimis* général, qui exclut la production agricole primaire[^amureba] [^de-minimis].
- **GREEN** (groupes de froid) : GREEN aide aussi un groupe de froid neuf de moins de 40 kW au CO2, à l'ammoniac ou au propane, sur un surcoût forfaitaire face à un groupe au R449, au taux de 30 % pour une PME. Pour ce volet, ni audit AMUREBA ni compteurs ne sont exigés[^green-brochure]. C'est une piste pour le remplacement du groupe froid du tank, mais son application au tank à lait n'est écrite nulle part, et le seuil de {{ v('green_seuil_pme', 0) }} s'applique a priori aussi[^green-agw].

La vague 1 tient donc **sans aide** : les aides n'y changent presque rien.

### 3. Les deux ensemble (vague 2)

Les deux équipements se combinent. Le refroidissement passe alors d'environ 13-15 kWh à 10-11 kWh par 1 000 L, tout en fournissant l'eau chaude préchauffée[^handboek]. Ils se pénalisent un peu : avec un pré-refroidisseur, il reste moins de chaleur à récupérer. Un conseiller français juge le couple pertinent à partir d'environ 700 000 L par an[^reussir-traite] : c'est une solution pour les grands troupeaux (vague 2).

## Ce qui ferme la boucle

- L'eau du puits refroidit le lait, puis abreuve les vaches.
- La chaleur du lait chauffe l'eau de lavage, au lieu d'être rejetée dans l'air.
- La traite a lieu tôt le matin et le soir, hors des heures de production solaire : une batterie ou un stockage de froid (eau glacée produite à midi) permettrait de refroidir le lait avec ses propres panneaux. Cette piste reste à documenter.

## À vérifier

- Prix belges d'un pré-refroidisseur et d'un récupérateur, posés.
- En Belgique, le tank appartient-il en général à l'éleveur ou à la laiterie ?
- Un programme GREEN plus large (pré-refroidisseur, récupérateur et autres économies d'énergie de l'étable, au-delà du seuil de {{ v('green_seuil_pme', 0) }}) serait-il recevable ?
- Admissibilité du groupe froid d'un tank à lait (propane ou CO2) au volet « groupes de froid » de GREEN, et seuil de {{ v('green_seuil_pme', 0) }} pour ce volet. Surcoût réel d'un groupe au propane ou au CO2 pour un tank.
- Aide wallonne aux investissements agricoles (AII) : la liste des investissements admissibles (annexe 3 de l'arrêté ministériel du 23 février 2023, version au 1er janvier 2026) ne cite ni pré-refroidisseur ni récupérateur de chaleur ; elle prévoit un forfait « tank-refroidisseur » de 3 465 € par 1 000 L[^am-aii]. Reste à demander à l'administration si ces équipements peuvent entrer dans le forfait du tank lors d'un achat neuf.
- Consommation réelle du tank sur l'exploitation (relevé du compteur ou sous-compteur).
- Refroidissement sur photovoltaïque avec stockage de froid : coût et retours d'expérience.

## Sources

[^inagro]: « Voorkoeler voor melkveebedrijf », Inagro, publié le 4 janvier 2022, mis à jour le 28 août 2026. https://inagro.be/themas/energie/energie-besparen/aanpassingen/melkveebedrijf-voorkoeler
[^rundveeloket]: « Efficiëntie voorkoeler », Rundveeloket (avec Boerenbond), 12 juin 2024. https://rundveeloket.be/vraag_antwoord/voorkoelen
[^ilvo]: « Energieke landbouw: Watt brengt dat op?! », Département Landbouw en Visserij (Vlaamse overheid), avec ILVO et Inagro, 2014, chapitre 11 « Voorkoeler ». https://rundveeloket.be/sites/default/files/inline-files/Energieke_landbouw_%20Watt_brengt_het_op.pdf
[^handboek]: Handboek Melkveehouderij 2023-2024, chapitre 9 « Melkwinning », § 9.10, Wageningen University & Research, édition 2023-2024 (PDF de mars 2024). https://rundveeloket.be/sites/default/files/inline-files/Handboek_Melkveehouderij-H9-NL-2023.pdf
[^elia-2025]: « Elektriciteitsmix 2025: zonneproductie stijgt met 21%… », communiqué d'Elia, 26 décembre 2025 (chiffres provisoires), version néerlandaise publiée par la VFB. https://www.vfb.be/Media/Default/pdf/20251226_Elektriciteitsmix%202025_NL.pdf
[^reussir-eco]: « Économies d'énergie : prérefroidisseurs et récupérateurs de chaleur sont de plus en plus rentables », Réussir Lait (France), 4 octobre 2023. https://www.reussir.fr/lait/economies-denergie-prerefroidisseurs-et-recuperateurs-de-chaleur-sont-de-plus-en-plus-rentables
[^reussir-mc]: « Traite des vaches laitières : comment optimiser sa consommation électrique », Réussir Agriculture Massif central (France), 13 avril 2026. https://www.reussir.fr/agriculture-massif-central/traite-des-vaches-laitieres-comment-optimiser-sa-consommation-electrique
[^reussir-recup]: « Avec le récupérateur de chaleur sur notre tank à lait, nous profitons d'une énergie gratuite », Réussir Machinisme (France), 30 juillet 2026. https://www.reussir.fr/machinisme/avec-le-recuperateur-de-chaleur-sur-le-tank-nous-profitons-dune-energie-gratuite
[^reussir-traite]: « Traite : comment réaliser des économies d'énergie ? », Réussir Lait (France), 30 mars 2023. https://www.reussir.fr/lait/traite-comment-realiser-des-economies-denergie
[^aii-liste]: « Liste des investissements admissibles », SPW Agriculture, janvier 2026, consultée le 27 novembre 2026. https://agriculture.wallonie.be/files/accueil/Aides/AII/outils/Liste%20des%20investissements%20admissibles.pdf
[^green-agw]: Arrêté du Gouvernement wallon du 23 mai 2024 relatif aux primes à l'investissement (aides GREEN), en vigueur le 1er janvier 2025 : articles 7, 10, 11 et 26, Wallex, consulté le 27 novembre 2026. https://wallex.wallonie.be/sites/wallex/contents/acts/108/108350/1.html
[^am-aii]: Arrêté ministériel du 23 février 2023 exécutant l'arrêté du Gouvernement wallon du 23 février 2023 relatif aux aides à l'installation et aux investissements (secteurs agricole et horticole…), article 6 et annexes 2 et 3, version consolidée en vigueur au 1er janvier 2026 (seuil de sélection : AM du 15 janvier 2026), Wallex. https://wallex.wallonie.be/sites/wallex/contents/acts/87/87905/4.html
[^green-brochure]: « Aides GREEN – Brochure explicative », SPW Économie, Emploi, Recherche, octobre 2026 : points 1.1, 3, 4 et 7.4, annexes 2 et 3, consulté le 27 novembre 2026. https://iodda.be/public/annexes/8063/document/fr
[^amureba]: Arrêté du Gouvernement wallon du 1er février 2024 relatif à l'octroi de subventions à l'audit ou à l'étude dans le secteur non résidentiel (AMUREBA), articles 43 et 44, annexe 5, Wallex, consulté le 27 novembre 2026. https://wallex.wallonie.be/eli/arrete/2024/02/01/2024004275
[^de-minimis]: Règlement (UE) 2023/2831 de la Commission du 13 décembre 2023 relatif aux aides de minimis, article 1er, § 1er, c) et § 2, Journal officiel de l'Union européenne du 15 décembre 2023, consulté le 27 novembre 2026. http://data.europa.eu/eli/reg/2023/2831/oj
