---
id: tank-a-lait
titre: Refroidissement du lait
domaine: élevage
dependance_fossile: électricité
alternatives: [Pré-refroidisseur, récupérateur de chaleur]
vague_meilleure_alternative: 1
statut: brouillon
maj: 2026-11-26
---

# Refroidissement du lait

!!! warning "Sources à relire"
    Les sources de cette fiche n'ont été consultées que par les extraits d'un moteur de recherche (novembre 2026). Chaque chiffre sourcé doit être confirmé sur la page avant le passage au statut « relu ».

## En bref

Le lait sort de la vache à environ 35 °C et doit être refroidi à 4 °C dans le tank. C'est le premier poste électrique d'une exploitation laitière avec la traite. Le fossile entre par l'électricité du réseau, en partie produite au gaz. Deux équipements simples et éprouvés réduisent la facture : le pré-refroidisseur, qui refroidit le lait avec l'eau d'abreuvement, et le récupérateur de chaleur, qui chauffe l'eau de lavage avec la chaleur du tank. Les deux sont rentables aujourd'hui (vague 1).

## Comment ça marche aujourd'hui

Le tank est une cuve isolée avec un groupe frigorifique : un compresseur électrique extrait la chaleur du lait et la rejette dans l'air par un condenseur. Sans pré-refroidissement, il faut environ 14 kWh d'électricité pour refroidir 1 000 L de lait[^inagro][^rundveeloket], 15 kWh selon une autre brochure flamande[^ilvo]. Pour une exploitation qui livre {{ v('lait_livre_an') }} (hypothèse), cela fait environ 7 000 kWh par an (calculé à partir de ces deux chiffres).

L'eau chaude de lavage de la machine à traire et du tank est souvent produite par un chauffe-eau électrique, parfois par la chaudière au mazout.

## Où entrent le pétrole et le gaz

- **Électricité** : en 2025, le gaz fournissait environ 19 % de la production d'électricité en Belgique[^mix-2025]. Le prix de l'électricité suit en partie celui du gaz.
- **Eau chaude** : au mazout ou au gaz sur certaines exploitations.
- **Fluide frigorigène** : gaz fluoré de synthèse, issu de la chimie.
- **Collecte du lait** : camion-citerne au gasoil (hors exploitation).

## Les alternatives

### 1. Pré-refroidisseur (vague 1)

Un échangeur à plaques fait passer le lait d'un côté et l'eau froide du puits ou du réseau de l'autre. Le lait arrive dans le tank vers 15 à 20 °C au lieu de 33 °C[^inagro]. L'eau, réchauffée de quelques degrés, part à l'abreuvement : les vaches boivent volontiers après la traite.

Le pré-refroidisseur économise environ {{ v('prerefroidisseur_gain', 0) }} de l'électricité du tank selon Rundveeloket, et jusqu'à 50 % selon Inagro[^rundveeloket][^inagro]. Pour l'exploitation type (calculé) :

- électricité économisée : {{ v('prerefroidisseur_kwh_an') }} ;
- économie : {{ v('prerefroidisseur_eur_an') }} au prix du réseau ({{ fourchette('prerefroidisseur_eur_an') }} selon les scénarios).

Le prix d'un pré-refroidisseur va de 4 000 à 10 000 € selon l'installation (prix français)[^reussir-eco]. Rundveeloket estime l'investissement amorti en 3 à 4 ans sur la plupart des exploitations[^rundveeloket] ; des sources françaises donnent 2 à 7 ans[^reussir-mc]. Avec le calcul ci-dessus, un appareil à 4 000 € se rembourse en 5 à 6 ans (ordre de grandeur) : le retour est plus rapide sur les grandes exploitations et quand le tank est petit pour le volume livré.

Conditions :

- de l'eau en quantité : au moins 1 L d'eau par litre de lait, de préférence 1,5 à 2 L[^rundveeloket] ;
- un usage de cette eau, sinon on la gaspille : abreuvement, lavage des aires. Au pâturage, quand les vaches boivent loin de l'étable, l'intérêt baisse ;
- de l'eau froide : le gain est plus faible en été, quand l'eau est plus chaude. L'eau de puits, plus fraîche l'été, est un avantage.

### 2. Récupérateur de chaleur (vague 1)

Un échangeur placé sur le circuit frigorifique du tank récupère la chaleur extraite du lait pour préchauffer l'eau d'un ballon vers 55 °C. Il économise 60 à 90 % de l'énergie du chauffe-eau[^reussir-eco]. Le chauffe-eau reste nécessaire pour monter l'eau de lavage à 80-90 °C. Il produit 0,3 à 0,8 L d'eau à 55 °C par litre de lait, et l'efficacité du groupe froid baisse un peu au-delà d'environ 50 °C[^handboek].

Coût : un exemple français à 7 100 € posé (échangeurs, ballon, circuit et pose)[^reussir-recup], avec un retour de 2 à 5 ans selon l'Institut de l'élevage[^reussir-recup]. D'autres références françaises donnent des retours bien plus longs, jusqu'à une quinzaine d'années sans aide : le résultat dépend du volume d'eau chaude réellement utilisé.

Conditions :

- poser par un frigoriste, car on intervient sur le circuit du tank ;
- si la laiterie est propriétaire du tank, son accord est nécessaire (pratique française, à vérifier en Belgique)[^reussir-traite] ;
- un besoin d'eau chaude régulier.

### 3. Les deux ensemble

Les deux équipements se combinent. Le refroidissement passe alors d'environ 13-15 kWh à 10-11 kWh par 1 000 L, tout en fournissant l'eau chaude préchauffée[^handboek].

## Ce qui ferme la boucle

- L'eau du puits refroidit le lait, puis abreuve les vaches.
- La chaleur du lait chauffe l'eau de lavage, au lieu d'être rejetée dans l'air.
- La traite a lieu tôt le matin et le soir, hors des heures de production solaire : une batterie ou un stockage de froid (eau glacée produite à midi) permettrait de refroidir le lait avec ses propres panneaux. Cette piste reste à documenter.

## À vérifier

- Relire toutes les sources sur la page d'origine (consultées par extraits seulement).
- Prix belges d'un pré-refroidisseur et d'un récupérateur, posés.
- En Belgique, le tank appartient-il en général à l'éleveur ou à la laiterie ?
- Éligibilité de ces équipements à l'aide wallonne aux investissements agricoles (AII).
- Part du gaz dans la production d'électricité belge en 2025, dans le bilan officiel d'Elia.
- Consommation réelle du tank sur l'exploitation (relevé du compteur ou sous-compteur).
- Refroidissement sur photovoltaïque avec stockage de froid : coût et retours d'expérience.

## Sources

[^inagro]: « Voorkoeler voor melkveebedrijf », Inagro, date à vérifier. https://inagro.be/themas/energie/energie-besparen/aanpassingen/melkveebedrijf-voorkoeler
[^rundveeloket]: « Efficiëntie voorkoeler », Rundveeloket, date à vérifier. https://rundveeloket.be/vraag_antwoord/voorkoelen
[^ilvo]: « Energieke landbouw – Watt brengt het op?! », ILVO et Inagro, date à vérifier. https://rundveeloket.be/sites/default/files/inline-files/Energieke_landbouw_%20Watt_brengt_het_op.pdf
[^handboek]: Handboek Melkveehouderij 2023-2024, chapitre 9, Wageningen University & Research, 2023. https://rundveeloket.be/sites/default/files/inline-files/Handboek_Melkveehouderij-H9-NL-2023.pdf
[^mix-2025]: « Une année électrique en Belgique : que faut-il retenir de 2025 ? », Connaissance des énergies, 2026. https://www.connaissancedesenergies.org/une-annee-electrique-en-belgique-que-faut-il-retenir-de-2025
[^reussir-eco]: « Économies d'énergie : prérefroidisseurs et récupérateurs de chaleur sont de plus en plus rentables », Réussir (France), date à vérifier. https://www.reussir.fr/lait/economies-denergie-prerefroidisseurs-et-recuperateurs-de-chaleur-sont-de-plus-en-plus-rentables
[^reussir-mc]: « Traite des vaches laitières : comment optimiser sa consommation électrique », Réussir Agriculture Massif central (France), date à vérifier. https://www.reussir.fr/agriculture-massif-central/traite-des-vaches-laitieres-comment-optimiser-sa-consommation-electrique
[^reussir-recup]: « Avec le récupérateur de chaleur sur le tank, nous profitons d'une énergie gratuite », Réussir (France), date à vérifier. https://www.reussir.fr/avec-le-recuperateur-de-chaleur-sur-le-tank-nous-profitons-dune-energie-gratuite
[^reussir-traite]: « Traite : comment réaliser des économies d'énergie », Réussir (France), date à vérifier. https://www.reussir.fr/lait%2F/traite-comment-realiser-des-economies-denergie
