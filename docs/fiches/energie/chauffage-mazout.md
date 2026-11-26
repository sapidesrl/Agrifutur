---
id: chauffage-mazout
titre: Chauffage et eau chaude au mazout
domaine: énergie
dependance_fossile: mazout
alternatives: [Chaudière à plaquettes, récupération de chaleur, pompe à chaleur]
vague_meilleure_alternative: 1
statut: brouillon
maj: 2026-11-26
---

# Chauffage et eau chaude au mazout

!!! warning "Sources à relire"
    Les sources de cette fiche n'ont été consultées que par les extraits d'un moteur de recherche (novembre 2026). Chaque chiffre sourcé doit être confirmé sur la page avant le passage au statut « relu ».

## En bref

Beaucoup de fermes wallonnes chauffent au mazout l'habitation, les bureaux, l'eau chaude de la laiterie et parfois des gîtes. Au prix actuel, un kWh de mazout coûte {{ v('mazout_kwh') }}, contre {{ v('plaquettes_kwh') }} pour les plaquettes de bois, soit {{ v('ratio_mazout_plaquettes', 1) }} plus cher. La chaudière à plaquettes est rentable aujourd'hui pour une ferme qui consomme plusieurs milliers de litres par an, surtout si ses haies fournissent une partie du bois (vague 1). La récupération de chaleur sur le tank à lait réduit le besoin d'eau chaude. La pompe à chaleur convient aux petits besoins bien isolés.

## Comment ça marche aujourd'hui

Une chaudière brûle le mazout pour chauffer l'eau d'un circuit de radiateurs ou d'un ballon. Le mazout est stocké en citerne et livré quelques fois par an.

Ordres de grandeur :

- une habitation belge moyenne consomme environ 2 500 L par an[^mol] ;
- une ferme avec laiterie et trois habitations consommait environ 8 000 L par an avant de passer aux plaquettes[^febhel] ;
- une exploitation de Meux (Namur), avec des salles et des gîtes, consommait 28 000 L par an dans six vieilles chaudières[^febhel].

Le prix du mazout est fixé chaque jour par le SPF Économie. Au prix maximum du 4 novembre 2026 ({{ v('gasoil_chauffage_2000l_tvac') }} TVAC pour au moins 2 000 L), il a environ doublé depuis février 2026.

La réglementation pousse aussi au changement : en Wallonie, une chaudière au mazout ne peut plus être installée dans un bâtiment neuf depuis le 1er janvier 2026. Pour les bâtiments existants, l'interdiction d'installer ou de remplacer une chaudière est reportée au 1er janvier 2031. Une chaudière existante peut continuer à fonctionner[^wallonie-2031].

## Où entrent le pétrole et le gaz

- **Combustible** : le mazout est un gasoil de chauffage, raffiné à partir du pétrole.
- **Livraison** : camion-citerne au gasoil.
- **Électricité de la chaudière** (brûleur, circulateur) : une petite part vient de centrales au gaz.

## Les alternatives

### 1. Chaudière à plaquettes de bois (vague 1)

Une chaudière automatique brûle des plaquettes (du bois broyé) amenées par une vis depuis un silo. Elle fonctionne comme une chaudière au mazout, avec un décendrage et un entretien plus réguliers.

Coût du combustible (calculé) :

| Combustible | Prix du kWh actuel | Fourchette des scénarios |
|---|---|---|
| Mazout | {{ v('mazout_kwh') }} | {{ fourchette('mazout_kwh') }} |
| Plaquettes sèches | {{ v('plaquettes_kwh') }} | {{ fourchette('plaquettes_kwh') }} |

Les plaquettes coûtaient {{ v('plaquettes_prix', 2) }} en octobre 2026 en Wallonie (relevé Valbiom), à peine plus qu'un an plus tôt[^callmepower]. Leur prix a peu bougé pendant la crise, contrairement au mazout. Le calcul suppose qu'un MAP (mètre cube apparent) de plaquettes contient {{ v('plaquettes_energie_map') }}, l'équivalence de Valbiom : 10 MAP remplacent environ 1 000 L de mazout[^valbiom-guide].

Pour la ferme de 8 000 L par an citée plus haut, il faut environ {{ v('chauffage_map_an', 0) }} de plaquettes. L'économie de combustible atteint {{ v('chauffage_economie_an') }} au prix actuel, et encore {{ v('chauffage_economie_an', scenario='bas') }} au prix d'avant-crise (calculé, à rendement de chaudière égal, hors entretien).

Investissement et entretien :

- une chaufferie de 50 kW coûte en moyenne 30 000 à 45 000 €, selon la puissance, le silo et le réseau de chaleur ; l'entretien revient à environ 950 € par an[^spw-12] ;
- dans un gîte de Durbuy, une chaudière de 75 kW avec un silo enterré de 25 m³ a coûté 32 000 €, dont 5 000 € pour le silo et les travaux[^spw-gite] ;
- il faut une chaufferie d'environ 20 m² et un silo de 25 à 100 m³[^febhel].

Avec ces chiffres, l'investissement se rembourse en 4 à 6 ans au prix actuel et en plus de 10 ans au prix d'avant-crise (ordre de grandeur, à partir des montants ci-dessus et du calcul d'économie). Les exemples belges publiés donnent 6 à 8 ans[^febhel]. La rentabilité dépend donc surtout du volume de mazout remplacé : plus la consommation est forte, plus vite la chaudière est payée.

Conditions :

- une consommation de plusieurs milliers de litres de mazout par an ;
- de la place pour la chaufferie et un silo accessible au tracteur ou au camion ;
- des plaquettes sèches (moins de 25 à 30 % d'humidité) ;
- du temps pour l'entretien et le décendrage.

### 2. Récupération de chaleur (vague 1)

Avant d'acheter une nouvelle chaudière, on réduit le besoin. Sur une exploitation laitière, un récupérateur branché sur le groupe froid du tank à lait produit de l'eau chaude vers 55 °C et économise 60 à 90 % de l'énergie du chauffe-eau[^reussir-tank] (voir la fiche [refroidissement du lait](../elevage/tank-a-lait.md)). L'isolation des ballons et des tuyaux, et la régulation de la chaudière, vont dans le même sens.

### 3. Pompe à chaleur (vague 2)

La pompe à chaleur air-eau prend la chaleur de l'air extérieur avec un compresseur électrique. Elle fournit 3 à 4,5 kWh de chaleur par kWh d'électricité, et une installation pour une habitation coûte de 8 000 à 18 000 € selon la surface[^trustup-pac]. Elle convient à une habitation bien isolée avec des émetteurs basse température, et devient intéressante derrière ses propres panneaux. Elle est moins adaptée aux grands bâtiments mal isolés et à l'eau très chaude de lavage (80 à 90 °C).

Attention aux aides : les primes Habitation wallonnes ont pris fin le 30 septembre 2026. Depuis le 1er octobre 2026, le soutien à la rénovation passe surtout par des prêts, après un audit[^renovation-2026].

## Ce qui ferme la boucle

- Les haies de la ferme produisent du bois. Selon Valbiom, une haie entretenue donne en moyenne environ 12 MAP de plaquettes pour 100 m tous les dix ans, soit environ 12 MAP par kilomètre et par an (de 12 à 25 selon la méthode d'exploitation)[^valbiom-haies]. Pour 80 MAP par an, il faut donc de l'ordre de 4 à 7 km de haies.
- Le coût de production des plaquettes de haie est estimé de 12 à 22 € par MAP selon le chantier, en France[^reussir-haies] : moins que le prix d'achat.
- Les cendres de bois retournent au champ ou au jardin (voir la fiche [engrais phosphatés et potassiques](../fertilisation/engrais-p-k.md)).
- La chaleur du tank à lait chauffe l'eau de lavage.

## À vérifier

- Relire toutes les sources sur la page d'origine (consultées par extraits seulement).
- L'interdiction des chaudières au mazout de 2031 vise-t-elle aussi les bâtiments agricoles, ou seulement les bâtiments soumis à la PEB ?
- Le ratio mazout/plaquettes publié par Valbiom (2,4 en septembre 2026) est plus faible que le calcul de ce projet : vérifier les hypothèses de Valbiom (rendement des chaudières, prix TVAC, énergie du MAP).
- Les chaudières à plaquettes et les pompes à chaleur sont-elles éligibles à l'aide wallonne aux investissements agricoles (AII), et à quel taux ?
- Différence de rendement entre une chaudière au mazout et une chaudière à plaquettes.
- Consommation réelle de mazout de l'exploitation, qui remplace l'exemple de 8 000 L.
- Coût de production belge des plaquettes de haie.

## Sources

[^mol]: « Les chiffres clés du mazout de chauffage en Belgique », Mazout-on-line (site commercial), date à vérifier. https://www.mazout-on-line.be/fr/actualites/astuces-et-conseils/les-chiffres-cles-du-mazout-de-chauffage-en-belgique/
[^febhel]: « Chaudières biomasse dans l'agriculture belge », FEBHEL, article paru dans Pleinchamp, mai 2024. https://www.febhel.be/sites/default/files/2024-05/version-finale---article-pleinchamps---chaudieres-biomasse-dans-l'agriculture-belge-2-pages.pdf
[^wallonie-2031]: « Chaudières au mazout et au charbon : la Wallonie reporte l'interdiction à 2031 », Wallonie.be, 2026. https://wallonie.be/fr/actualites/chaudieres-au-mazout-et-au-charbon-la-wallonie-reporte-linterdiction-2031
[^callmepower]: « Le sac de pellets passe à 7,02 euros en octobre », Callmepower, novembre 2026 (relevé Valbiom). https://callmepower.be/fr/energie/actualites/prix-pellets-sac-7-euros-wallonie
[^valbiom-guide]: « Installer une chaudière biomasse pour se chauffer », Valbiom et SPW Énergie, juin 2025. https://energie.wallonie.be/files/%c3%89nergies%20vertes/Bio%c3%a9nergie/Poele%20chaudiere/installer-une-chaudiere-biomasse-pour-se-chauffer-2025.pdf
[^spw-12]: « 12. Placer un système de chauffage biomasse », SPW Énergie, date à vérifier. https://energie.wallonie.be/servlet/Repository/12-placer-un-systeme-de-chauffage-biomasse.pdf?ID=87282
[^spw-gite]: « Une chaudière à plaquettes de bois et un silo potager installés au sein d'un gîte », SPW Énergie, date à vérifier. https://energie.wallonie.be/servlet/Repository/une-chaudiere-a-plaquettes-de-bois-et-un-silo-potager-installes-au-sein-d-un-gite.pdf?ID=53339&saveFile=true
[^reussir-tank]: « Économies d'énergie : prérefroidisseurs et récupérateurs de chaleur sont de plus en plus rentables », Réussir (France), date à vérifier. https://www.reussir.fr/lait/economies-denergie-prerefroidisseurs-et-recuperateurs-de-chaleur-sont-de-plus-en-plus-rentables
[^trustup-pac]: « Pompe à chaleur air-eau : prix et rendement », Trustup (site commercial), juillet 2026. https://blog.trustup.be/fr/pompe-a-chaleur-air-eau-prix-rendement/
[^renovation-2026]: « Nouveau le 1er octobre : un nouveau régime pour le soutien à la rénovation en Wallonie », DH, 27 septembre 2026. https://www.dhnet.be/dernieres-depeches/2026/09/27/nouveau-le-1er-octobre-un-nouveau-regime-pour-le-soutien-a-la-renovation-en-wallonie-KVHUKGCC2RBH7MJSBO4AYPH7LA
[^valbiom-haies]: « Entretenir et valoriser mes haies », Valbiom et SPW, mars 2021. https://energie.wallonie.be/servlet/Repository/carnet-entretenir-et-valoriser-mes-haies-mars-2021.pdf?IDR=51458
[^reussir-haies]: « Les haies, des atouts agronomiques et une source de revenu », Réussir (France), date à vérifier. https://www.reussir.fr/les-haies-des-atouts-agronomiques-et-une-source-de-revenu
