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
    Les sources ont été relues sur la page d'origine le 26 novembre 2026, sauf deux pages restées inaccessibles (protection anti-robots) : le relevé de prix Valbiom repris par Callmepower (prix des plaquettes) et l'article Trustup sur les pompes à chaleur. Leurs chiffres ne sont connus que par des extraits de moteur de recherche.

## En bref

Beaucoup de fermes wallonnes chauffent au mazout l'habitation, les bureaux, l'eau chaude de la laiterie et parfois des gîtes. Au prix actuel, un kWh de mazout coûte {{ v('mazout_kwh') }}, contre {{ v('plaquettes_kwh') }} pour les plaquettes de bois, soit {{ v('ratio_mazout_plaquettes', 1) }} plus cher. La chaudière à plaquettes est rentable aujourd'hui pour une ferme qui consomme plusieurs milliers de litres par an, surtout si ses haies fournissent une partie du bois (vague 1). La récupération de chaleur sur le tank à lait réduit le besoin d'eau chaude. La pompe à chaleur convient aux petits besoins bien isolés.

## Comment ça marche aujourd'hui

Une chaudière brûle le mazout pour chauffer l'eau d'un circuit de radiateurs ou d'un ballon. Le mazout est stocké en citerne et livré quelques fois par an.

Ordres de grandeur :

- une habitation belge moyenne consomme environ 2 500 L par an (2 478 L selon un vendeur de mazout, chiffre publié en 2020)[^mol] ;
- une ferme laitière de la province de Luxembourg, qui chauffe la laiterie et trois habitations, consommait environ 8 000 L par an avant de passer aux plaquettes[^febhel] ;
- une ferme de Meux (Namur), avec des salles de réception et des gîtes, consommait 28 000 L par an dans six anciennes chaudières[^febhel].

Le SPF Économie fixe un prix maximum du mazout. En moyenne du 1er au 26 novembre 2026, ce prix maximum valait {{ v('gasoil_chauffage_2000l_tvac') }} TVAC pour au moins 2 000 L, contre {{ v('gasoil_chauffage_2000l_tvac', scenario='bas') }} en février 2026, soit près de 80 % de hausse (prix officiels, voir [les hypothèses](../../hypotheses.md)).

La réglementation pousse aussi au changement. En Wallonie, une chaudière au mazout ne peut plus être installée dans un bâtiment neuf depuis le 1er janvier 2026[^wallonie-2031]. Dans les bâtiments existants, résidentiels ou non, il sera interdit à partir du 1er janvier 2031 d'installer une chaudière au mazout ou de remplacer un appareil de chauffage par une chaudière au mazout. Le brûleur d'une chaudière au mazout peut encore être remplacé jusqu'au 31 décembre 2034, et des dérogations sont possibles quand aucune alternative n'est réalisable techniquement, économiquement ou fonctionnellement. Le texte n'interdit pas d'utiliser une chaudière déjà en place[^decret-peb].

L'habitation de la ferme est donc visée. Pour les bâtiments agricoles non résidentiels, le texte ne prévoit pas d'exception propre, mais le décret PEB exempte déjà de ses exigences les unités agricoles non résidentielles faibles consommatrices d'énergie, et celles des entreprises liées par une convention environnementale sectorielle[^decret-peb]. On ne sait pas encore si cette exemption s'applique aussi à l'interdiction de 2031 (voir « À vérifier »).

## Où entrent le pétrole et le gaz

- **Combustible** : le mazout est un gasoil de chauffage, raffiné à partir du pétrole.
- **Livraison** : camion-citerne au gasoil.
- **Électricité de la chaudière** (brûleur, circulateur) : une petite part vient de centrales au gaz.

## Les alternatives

### 1. Chaudière à plaquettes de bois (vague 1)

Une chaudière automatique brûle des plaquettes (du bois broyé) amenées par une vis depuis un silo. Elle fonctionne comme une chaudière au mazout, avec un décendrage et un entretien plus réguliers. Selon Valbiom, les chaudières biomasse actuelles ont un rendement supérieur à 90 %[^valbiom-guide].

Coût du combustible (calculé) :

| Combustible | Prix du kWh actuel | Fourchette des scénarios |
|---|---|---|
| Mazout | {{ v('mazout_kwh') }} | {{ fourchette('mazout_kwh') }} |
| Plaquettes sèches | {{ v('plaquettes_kwh') }} | {{ fourchette('plaquettes_kwh') }} |

Les plaquettes coûtaient {{ v('plaquettes_prix', 2) }} en octobre 2026 en Wallonie (relevé Valbiom), à peine plus qu'un an plus tôt[^callmepower]. Leur prix a peu bougé pendant la crise, contrairement au mazout. Le calcul suppose qu'un MAP (mètre cube apparent) de plaquettes contient {{ v('plaquettes_energie_map') }}. C'est l'équivalence de Valbiom : il faut en moyenne 10 MAP de plaquettes forestières séchées (20 % d'humidité) ou 1 000 L de mazout pour produire 10 000 kWh. Dans son exemple de coût annuel, Valbiom compte toutefois environ 115 MAP pour remplacer 10 000 L de mazout, soit environ 15 % de plaquettes en plus[^valbiom-guide].

Valbiom a publié pour septembre 2026 un kWh de mazout 2,4 fois plus cher que celui des plaquettes[^callmepower], moins que le calcul ci-dessus. Sa méthode (énergie du MAP, prix du mazout retenu, rendements) n'a pas pu être lue : le calcul de cette fiche reste à comparer avec le sien.

Pour la ferme de 8 000 L par an citée plus haut, il faut environ {{ v('chauffage_map_an', 0) }} de plaquettes. L'économie de combustible atteint {{ v('chauffage_economie_an') }} au prix actuel, et encore {{ v('chauffage_economie_an', scenario='bas') }} au prix d'avant-crise (calculé, à rendement de chaudière égal, hors entretien).

Investissement et entretien :

- une chaufferie complète de 50 kW coûte en moyenne 30 000 à 45 000 €, selon le silo et le réseau de chaleur ; l'entretien et la maintenance reviennent à environ 950 € par an[^valbiom-guide] ;
- pour la FEBHEL, une chaudière de 50 à 100 kW coûte autour de 30 000 à 45 000 €[^febhel] ;
- dans un exemple wallon de Valbiom, un réseau de chaleur à plaquettes de 75 kW relie un gîte, une habitation et une piscine. Il a coûté 50 500 € (dont 35 000 € pour la chaudière et les sous-stations, 8 500 € pour le silo et le désilage, 7 000 € pour 60 m de réseau), avec 20 200 € de subside. Il consomme 120 MAP par an[^valbiom-guide] ;
- il faut une chaufferie d'au moins 20 m² et un silo de 25 à 100 m³ selon le besoin. Pour 10 000 L de mazout remplacés, soit environ 100 MAP par an, un silo de 35 m³ rempli trois fois par an suffit[^febhel] [^valbiom-guide].

Avec ces chiffres, l'investissement se rembourse en 4 à 6 ans au prix actuel et en plus de 10 ans au prix d'avant-crise, hors aides (ordre de grandeur, à partir des montants ci-dessus, de l'entretien et du calcul d'économie). Les deux fermes citées par la FEBHEL annoncent 6 et 8 ans, et la fédération donne 5 à 12 ans en général[^febhel]. L'exemple du gîte se rembourse en 10 ans avec les primes et en 17 ans sans, mais avec un mazout compté à 0,72 € par litre[^valbiom-guide]. La rentabilité dépend donc surtout du volume de mazout remplacé et de son prix : plus la consommation est forte, plus vite la chaudière est payée.

Aides : Valbiom indique qu'une entreprise ou un agriculteur peut obtenir une prime allant jusqu'à 40 % de l'investissement, et que les aides régionales aux entreprises (« GREEN ») demandent depuis 2025 un audit énergétique préalable (AMUREBA)[^valbiom-guide]. En revanche, l'aide wallonne aux investissements agricoles ne finance que les investissements repris dans sa liste : dans sa version de 2026, cette liste contient des panneaux photovoltaïques, des éoliennes et la petite biométhanisation, mais ni chaudière biomasse, ni pompe à chaleur, ni récupérateur de chaleur. Elle contient en revanche un broyeur à plaquettes forestières[^am-adisa].

Conditions :

- une consommation de plusieurs milliers de litres de mazout par an ;
- de la place pour la chaufferie et un silo accessible au tracteur ou au camion ;
- des plaquettes sèches (l'équivalence de Valbiom suppose environ 20 % d'humidité)[^valbiom-guide] ;
- du temps pour l'entretien et le décendrage.

### 2. Récupération de chaleur (vague 1)

Avant d'acheter une nouvelle chaudière, on réduit le besoin. Sur une exploitation laitière, un récupérateur branché sur le groupe froid du tank à lait préchauffe l'eau du chauffe-eau vers 55 °C et économise 60 à 90 % de sa consommation d'électricité (chiffres français)[^reussir-tank] (voir la fiche [refroidissement du lait](../elevage/tank-a-lait.md)). L'isolation des ballons et des tuyaux, et la régulation de la chaudière, vont dans le même sens.

### 3. Pompe à chaleur (vague 2)

La pompe à chaleur air-eau prend la chaleur de l'air extérieur avec un compresseur électrique. Elle fournit 3 à 4,5 kWh de chaleur par kWh d'électricité, et une installation pour une habitation coûte de 8 000 à 18 000 € selon la surface[^trustup-pac]. Elle convient à une habitation bien isolée avec des émetteurs basse température, et devient intéressante derrière ses propres panneaux. Elle est moins adaptée aux grands bâtiments mal isolés et à l'eau très chaude de lavage (80 à 90 °C).

Attention aux aides : depuis le 1er octobre 2026, les aides wallonnes à la rénovation des logements prennent la forme de prêts à taux zéro ou réduit (Rénopack, Rénoprêt), après un audit logement, et visent les logements classés PEB E, F ou G[^renovation-2026].

## Ce qui ferme la boucle

- Les haies de la ferme produisent du bois. Selon Valbiom, 12 MAP de plaquettes pour 100 m de haie tous les dix ans est une moyenne raisonnable, soit environ 12 MAP par kilomètre et par an. Une haie récoltée tous les dix ans par la méthode Harbonnier donne 12 à 25 MAP pour 100 m, et un recépage complet peut atteindre 40 MAP[^valbiom-haies]. Pour 80 MAP par an, il faut donc de l'ordre de 3 à 7 km de haies (calculé).
- Sur un chantier standard, Valbiom observe un coût de production de 12 à 20 € par MAP de plaquettes de haie[^valbiom-haies] : moins que le prix d'achat.
- Les cendres de bois retournent au champ ou au jardin (voir la fiche [engrais phosphatés et potassiques](../fertilisation/engrais-p-k.md)).
- La chaleur du tank à lait chauffe l'eau de lavage.

## À vérifier

- Lire sur la page d'origine le relevé Valbiom repris par Callmepower (prix des plaquettes d'octobre 2026 et d'octobre 2025, ratio de 2,4) et l'article Trustup (rendement et prix des pompes à chaleur) : pages inaccessibles le 26 novembre 2026.
- L'exemption du décret PEB pour les unités agricoles non résidentielles faibles consommatrices d'énergie s'applique-t-elle à l'interdiction des chaudières au mazout de 2031 (article 71/1) ? À demander au SPW Énergie.
- Méthode du ratio mazout/plaquettes de Valbiom (2,4 en septembre 2026) : énergie du MAP, prix du mazout retenu, rendements. Avec 10 kWh par litre et 1 000 kWh par MAP, ce ratio supposerait un mazout bien moins cher que le prix maximum de septembre 2026 rapporté par la presse (calculé).
- Rendement d'une chaudière au mazout (celui des chaudières biomasse dépasse 90 % selon Valbiom).
- Taux et conditions des aides régionales aux entreprises (GREEN, audit AMUREBA) pour une chaudière biomasse ou une pompe à chaleur agricole.
- Consommation réelle de mazout de l'exploitation, qui remplace l'exemple de 8 000 L.

## Sources

[^mol]: « Les chiffres clés du mazout de chauffage en Belgique », Mazout-on-line (site commercial), 26 février 2020. https://www.mazout-on-line.be/fr/actualites/astuces-et-conseils/les-chiffres-cles-du-mazout-de-chauffage-en-belgique/
[^febhel]: « Bois-énergie et agriculture belge, est-ce compatible ? », FEBHEL (Fédération interprofessionnelle belge du bois-énergie), article prévu pour Pleinchamp, avril 2024. https://www.febhel.be/sites/default/files/2024-05/version-finale---article-pleinchamps---chaudieres-biomasse-dans-l'agriculture-belge-2-pages.pdf
[^wallonie-2031]: « Chaudières au mazout et au charbon : la Wallonie reporte l'interdiction à 2031 », Wallonie.be, 3 juillet 2026. https://wallonie.be/fr/actualites/chaudieres-au-mazout-et-au-charbon-la-wallonie-reporte-linterdiction-2031
[^decret-peb]: Décret wallon du 28 novembre 2013 relatif à la performance énergétique des bâtiments, version consolidée sur Wallex : article 71/1 (inséré par le décret du 2 juillet 2026, art. 24) et article 10, 3° et 6°. Consulté le 26 novembre 2026. https://wallex.wallonie.be/eli/loi-decret/2013/11/28/2013207272
[^am-adisa]: Arrêté ministériel du 23 février 2023 exécutant l'arrêté du Gouvernement wallon du 23 février 2023 relatif aux aides à l'installation et aux investissements (secteurs agricole et horticole), version consolidée en vigueur depuis le 1er janvier 2026 (modifiée en dernier lieu le 11 mai 2026) : article 4 et annexe 3 « Investissements productifs admissibles ». Wallex, consulté le 26 novembre 2026. https://wallex.wallonie.be/eli/arrete/2023/02/23/2023042748
[^callmepower]: « Le sac de pellets passe à 7,02 euros en octobre », Callmepower, novembre 2026 (relevé Valbiom ; page inaccessible le 26 novembre 2026, lue par extrait seulement). https://callmepower.be/fr/energie/actualites/prix-pellets-sac-7-euros-wallonie
[^valbiom-guide]: « Installer une chaudière biomasse pour me chauffer ? J'y pense ! », Les Carnets de Valbiom n° 5, mise à jour juin 2025, hébergé par le SPW Énergie. https://energie.wallonie.be/files/%c3%89nergies%20vertes/Bio%c3%a9nergie/Poele%20chaudiere/installer-une-chaudiere-biomasse-pour-se-chauffer-2025.pdf
[^reussir-tank]: « Économies d'énergie : prérefroidisseurs et récupérateurs de chaleur sont de plus en plus rentables », Réussir (France), 4 octobre 2023. https://www.reussir.fr/lait/economies-denergie-prerefroidisseurs-et-recuperateurs-de-chaleur-sont-de-plus-en-plus-rentables
[^trustup-pac]: « Pompe à chaleur air-eau : prix et rendement », Trustup (site commercial), juillet 2026 (page inaccessible le 26 novembre 2026, lue par extrait seulement). https://blog.trustup.be/fr/pompe-a-chaleur-air-eau-prix-rendement/
[^renovation-2026]: « Nouveau le 1er octobre : un nouveau régime pour le soutien à la rénovation en Wallonie », DH (dépêche Belga), 27 septembre 2026. https://www.dhnet.be/dernieres-depeches/2026/09/27/nouveau-le-1er-octobre-un-nouveau-regime-pour-le-soutien-a-la-renovation-en-wallonie-KVHUKGCC2RBH7MJSBO4AYPH7LA
[^valbiom-haies]: « Entretenir et valoriser mes haies et bandes boisées en plaquettes bocagères ? J'y pense ! », Les Carnets de Valbiom n° 1, mars 2021, hébergé par le SPW Énergie. https://energie.wallonie.be/files/%c3%89nergies%20vertes/Bio%c3%a9nergie/Plaquettes/carnet-entretenir-et-valoriser-mes-haies-mars-2021.pdf
