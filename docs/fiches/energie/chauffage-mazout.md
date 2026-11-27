---
id: chauffage-mazout
titre: Chauffage et eau chaude au mazout
domaine: énergie
dependance_fossile: mazout
alternatives: [Chaudière à plaquettes, récupération de chaleur, pompe à chaleur]
vague_meilleure_alternative: 1
statut: relu
maj: 2026-11-27
---

# Chauffage et eau chaude au mazout

!!! warning "Sources à relire"
    Les sources ont été relues sur la page d'origine le 26 novembre 2026, sauf deux pages restées inaccessibles (protection anti-robots) : le relevé de prix Valbiom repris par Callmepower (prix des plaquettes) et l'article Trustup sur les pompes à chaleur. Leurs chiffres ne sont connus que par des extraits de moteur de recherche. Les aides publiques ont été relues le 27 novembre 2026 (voir [les aides publiques](../../aides.md)).

## En bref

Beaucoup de fermes wallonnes chauffent au mazout l'habitation, les bureaux, l'eau chaude de la laiterie et parfois des gîtes. Au prix actuel, un kWh de mazout coûte {{ v('mazout_kwh') }} TVAC, contre {{ v('plaquettes_kwh') }} TVAC pour les plaquettes de bois, soit {{ v('ratio_mazout_plaquettes', 1) }} plus cher ({{ v('ratio_mazout_plaquettes', 1, scenario='bas') }} au prix d'avant-crise). La chaudière à plaquettes est rentable aujourd'hui pour une ferme qui consomme plusieurs milliers de litres par an, surtout si ses haies fournissent une partie du bois (vague 1). Pour 8 000 L de mazout par an, elle se rembourse en {{ v('chaudiere_retour_ans', 0) }} sans aide ; au prix d'avant-crise, en {{ v('chaudiere_retour_ans', 0, scenario='bas') }} sans aide et {{ v('chaudiere_retour_green_ans', 1, scenario='bas') }} avec l'aide régionale GREEN de {{ v('green_taux_chaudiere_biomasse', 0) }} (calculé). La récupération de chaleur sur le tank à lait réduit le besoin d'eau chaude, et la pompe à chaleur convient aux petits besoins bien isolés.

## Comment ça marche aujourd'hui

Une chaudière brûle le mazout pour chauffer l'eau d'un circuit de radiateurs ou d'un ballon. Le mazout est stocké en citerne et livré quelques fois par an.

Ordres de grandeur :

- une habitation belge moyenne consomme environ 2 500 L par an (2 478 L selon un vendeur de mazout, chiffre publié en 2020)[^mol] ;
- une ferme laitière de la province de Luxembourg, qui chauffe la laiterie et trois habitations, consommait environ 8 000 L par an avant de passer aux plaquettes[^febhel] ;
- une ferme de Meux (Namur), avec des salles de réception et des gîtes, consommait 28 000 L par an dans six anciennes chaudières[^febhel].

Le SPF Économie fixe un prix maximum du mazout. En moyenne du 1er au 26 novembre 2026, ce prix maximum valait {{ v('gasoil_chauffage_2000l_tvac') }} TVAC pour au moins 2 000 L, contre {{ v('gasoil_chauffage_2000l_tvac', scenario='bas') }} en février 2026 (prix officiels, voir [les hypothèses](../../hypotheses.md)).

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

Le prix du mazout est TVA comprise : c'est ce que paie l'habitation. C'est aussi le coût réel d'un agriculteur au régime forfaitaire, qui ne récupère pas la TVA. Le relevé Valbiom des plaquettes est lui aussi un prix de détail TVA comprise[^callmepower], au taux de 6 % du bois de chauffage[^ar20] : la comparaison se fait donc TVA comprise des deux côtés. Une exploitation qui récupère la TVA sur le chauffage de la laiterie paie le mazout {{ v('mazout_kwh_htva') }} HTVA ({{ fourchette('mazout_kwh_htva') }}), et les plaquettes environ 6 % de moins que le prix relevé : l'avantage des plaquettes se réduit alors, sans disparaître.

Les plaquettes coûtaient {{ v('plaquettes_prix', 2) }} TVAC en octobre 2026 en Wallonie (relevé Valbiom), à peine plus qu'un an plus tôt[^callmepower]. Leur prix a peu bougé pendant la crise, contrairement au mazout. Le calcul suppose qu'un MAP (mètre cube apparent) de plaquettes contient {{ v('plaquettes_energie_map') }}. C'est l'équivalence de Valbiom : il faut en moyenne 10 MAP de plaquettes forestières séchées (20 % d'humidité) ou 1 000 L de mazout pour produire 10 000 kWh. Dans son exemple de coût annuel, Valbiom compte toutefois environ 115 MAP pour remplacer 10 000 L de mazout, soit environ 15 % de plaquettes en plus[^valbiom-guide].

Valbiom a publié pour septembre 2026 un kWh de mazout 2,4 fois plus cher que celui des plaquettes[^callmepower], moins que le calcul ci-dessus. Sa méthode (énergie du MAP, prix du mazout retenu, rendements) n'a pas pu être lue : le calcul de cette fiche reste à comparer avec le sien.

Pour la ferme de 8 000 L par an citée plus haut, il faut environ {{ v('chauffage_map_an', 0) }} de plaquettes. L'économie de combustible atteint {{ v('chauffage_economie_an') }} au prix actuel, et encore {{ v('chauffage_economie_an', scenario='bas') }} au prix d'avant-crise (calculé, à rendement de chaudière égal, hors entretien).

Investissement et entretien :

- une chaufferie complète de 50 kW coûte en moyenne 30 000 à 45 000 €, selon le silo et le réseau de chaleur ; l'entretien et la maintenance reviennent à environ 950 € par an[^valbiom-guide] ;
- pour la FEBHEL, une chaudière de 50 à 100 kW coûte autour de 30 000 à 45 000 €[^febhel] ;
- dans un exemple wallon de Valbiom, un réseau de chaleur à plaquettes de 75 kW relie un gîte, une habitation et une piscine. Il a coûté 50 500 € (dont 35 000 € pour la chaudière et les sous-stations, 8 500 € pour le silo et le désilage, 7 000 € pour 60 m de réseau), avec 20 200 € de subside. Il consomme 120 MAP par an[^valbiom-guide] ;
- il faut une chaufferie d'au moins 20 m² et un silo de 25 à 100 m³ selon le besoin. Pour 10 000 L de mazout remplacés, soit environ 100 MAP par an, un silo de 35 m³ rempli trois fois par an suffit[^febhel] [^valbiom-guide].

Rentabilité pour la ferme de 8 000 L par an (calculé, chaufferie de {{ v('chaudiere_plaquettes_kw', 0) }} à {{ v('chaudiere_plaquettes_prix', 0) }}, milieu de la fourchette de Valbiom, entretien de {{ v('chaudiere_entretien_supp_an', 0) }} de plus qu'une chaudière au mazout, sans frais financiers) :

| Calculé | Prix actuel | Prix d'avant-crise |
|---|---|---|
| Gain annuel, entretien déduit | {{ v('chaudiere_gain_net_an', 0) }} | {{ v('chaudiere_gain_net_an', 0, scenario='bas') }} |
| Temps de retour sans aide | {{ v('chaudiere_retour_ans', 1) }} | {{ v('chaudiere_retour_ans', 1, scenario='bas') }} |
| Temps de retour avec l'aide GREEN ({{ v('chaudiere_aide_green', 0) }}) | {{ v('chaudiere_retour_green_ans', 1) }} | {{ v('chaudiere_retour_green_ans', 1, scenario='bas') }} |

Sans aide, la conclusion dépend donc du scénario : au prix d'avant-crise, la chaudière à plaquettes ne se rembourse vite que pour les gros consommateurs, comme la ferme de Meux et ses 28 000 L par an. Les deux fermes citées par la FEBHEL annoncent 6 et 8 ans, et la fédération donne 5 à 12 ans en général[^febhel]. L'exemple du gîte se rembourse en 10 ans avec les primes et en 17 ans sans, mais avec un mazout compté à 0,72 € par litre[^valbiom-guide]. La rentabilité dépend surtout du volume de mazout remplacé et de son prix : plus la consommation est forte, plus vite la chaudière est payée.

**Aides.** L'aide wallonne aux investissements agricoles (AII) ne finance ni chaudière biomasse, ni pompe à chaleur, ni récupérateur de chaleur : ils sont absents de sa liste de 2026, qui contient en revanche un broyeur à plaquettes forestières[^am-adisa] [^aii-liste]. L'aide utile est **GREEN**, la prime régionale aux entreprises pour l'énergie renouvelable (voir [les aides publiques](../../aides.md#green)). L'agriculture n'est pas exclue, et Valbiom écrit qu'« une entreprise ou un agriculteur » peut l'obtenir[^valbiom-guide] [^decret-2004] :

- {{ v('green_taux_chaudiere_biomasse', 0) }} pour une PME, pour une chaudière biomasse jusqu'à 300 kW, sur un coût éligible plafonné à {{ v('green_plafond_chaudiere_kw') }} jusqu'à 100 kW[^green-spw]. Pour la chaufferie type de {{ v('chaudiere_plaquettes_kw', 0) }}, ce plafond dépasse le prix : l'aide porte sur tout le prix, soit {{ v('chaudiere_aide_green', 0) }} (calculé) ;
- un investissement d'au moins {{ v('green_seuil_pme', 0) }}, une demande avant le début des travaux, et un **audit ou une étude de faisabilité AMUREBA** préalable par un auditeur agréé, exigé depuis 2026[^green-agw] [^amureba-memo]. La Région subventionne cet audit à {{ v('amureba_taux_pme', 0) }} pour une PME[^amureba] ; l'accès d'une exploitation agricole à cette subvention reste à vérifier. Le coût de l'audit n'est pas compté dans le tableau ;
- pas de cumul avec une autre aide régionale pour le même programme d'investissements[^decret-2004].

Valbiom donne un exemple proche : une chaudière à pellets de 50 kW à 35 000 €, avec 14 000 € de subside, se rembourse en 8 ans au lieu de 14[^valbiom-guide]. Avec l'aide, la chaudière à plaquettes reste rentable même au prix d'avant-crise pour la ferme de 8 000 L : la vague 1 est confirmée, et elle ne dépend pas de l'aide au prix actuel.

Conditions :

- une consommation de plusieurs milliers de litres de mazout par an ;
- de la place pour la chaufferie et un silo accessible au tracteur ou au camion ;
- des plaquettes sèches (l'équivalence de Valbiom suppose environ 20 % d'humidité)[^valbiom-guide] ;
- du temps pour l'entretien et le décendrage.

### 2. Récupération de chaleur (vague 1)

Avant d'acheter une nouvelle chaudière, on réduit le besoin. Sur une exploitation laitière, un récupérateur branché sur le groupe froid du tank à lait préchauffe l'eau du chauffe-eau vers 55 °C et économise 60 à 90 % de l'énergie du chauffe-eau, électrique dans l'exemple de la source (chiffres français)[^reussir-tank]. Le chauffe-eau ou la chaudière reste nécessaire en appoint pour le lavage à chaud (voir la fiche [refroidissement du lait](../elevage/tank-a-lait.md)). L'isolation des ballons et des tuyaux, et la régulation de la chaudière, vont dans le même sens. Aucune aide n'est accessible en pratique : le récupérateur est absent de la liste de l'AII[^aii-liste], et son prix reste loin du seuil de {{ v('green_seuil_pme', 0) }} de GREEN[^green-agw]. Il est rentable sans aide.

### 3. Pompe à chaleur (vague 2)

La pompe à chaleur air-eau prend la chaleur de l'air extérieur avec un compresseur électrique. Elle fournit 3 à 4,5 kWh de chaleur par kWh d'électricité, et une installation pour une habitation coûte de 8 000 à 18 000 € selon la surface[^trustup-pac]. Elle convient à une habitation bien isolée avec des émetteurs basse température, et devient intéressante derrière ses propres panneaux. Elle est moins adaptée aux grands bâtiments mal isolés et à l'eau très chaude de lavage (80 à 90 °C).

**Aides.** GREEN paie {{ v('green_taux_pac', 0) }} d'une pompe à chaleur air-eau ou eau-eau jusqu'à 45 kW thermiques, sur un coût éligible de 1 320 à 1 760 €/kW selon la puissance, et 20 % au-delà[^green-spw], avec les mêmes conditions que pour la chaudière (audit AMUREBA, demande avant travaux)[^green-agw]. Mais GREEN exige un investissement d'au moins {{ v('green_seuil_pme', 0) }}[^green-agw] : une pompe à chaleur de la taille d'une habitation reste en dessous, et n'y a donc pas droit. GREEN ne vise que les investissements d'une entreprise ; le chauffage du logement de l'exploitant relève plutôt des aides au logement. L'AII ne finance pas la pompe à chaleur[^aii-liste]. L'aide ne change rien pour les petits besoins ; elle aide une installation professionnelle plus grande (laiterie, gîtes), qui reste à chiffrer. La vague 2 est maintenue.

Pour le logement, depuis le 1er octobre 2026, les aides wallonnes à la rénovation des logements prennent la forme de prêts à taux zéro ou réduit (Rénopack, Rénoprêt), après un audit logement, et visent les logements classés PEB E, F ou G[^renovation-2026].

## Ce qui ferme la boucle

- Les haies de la ferme produisent du bois. Selon Valbiom, 12 MAP de plaquettes pour 100 m de haie tous les dix ans est une moyenne raisonnable, soit environ 12 MAP par kilomètre et par an. Une haie récoltée tous les dix ans par la méthode Harbonnier donne 12 à 25 MAP pour 100 m, et un recépage complet peut atteindre 40 MAP[^valbiom-haies]. Pour 80 MAP par an, il faut donc de l'ordre de 3 à 7 km de haies (calculé).
- Sur un chantier standard, Valbiom observe un coût de production de 12 à 20 € par MAP de plaquettes de haie[^valbiom-haies] : moins que le prix d'achat ({{ v('plaquettes_prix', 2) }}).
- Les cendres de bois retournent au champ ou au jardin (voir la fiche [engrais phosphatés et potassiques](../fertilisation/engrais-p-k.md)).
- La chaleur du tank à lait chauffe l'eau de lavage.

## À vérifier

- Lire sur valbiom.be le relevé repris par Callmepower (prix des plaquettes d'octobre 2026 et d'octobre 2025, ratio de 2,4 ; site injoignable le 27 novembre 2026) et l'article Trustup (rendement et prix des pompes à chaleur, page inaccessible le 26 novembre 2026). Prix des plaquettes de février 2026 : non trouvé (le scénario bas utilise octobre 2025).
- L'exemption du décret PEB pour les unités agricoles non résidentielles faibles consommatrices d'énergie s'applique-t-elle à l'interdiction des chaudières au mazout de 2031 (article 71/1) ? À demander au SPW Énergie.
- Méthode du ratio mazout/plaquettes de Valbiom (2,4 en septembre 2026) : énergie du MAP, prix du mazout retenu, rendements. Avec 10 kWh par litre et 1 000 kWh par MAP, ce ratio supposerait un mazout bien moins cher que le prix maximum de septembre 2026 rapporté par la presse (calculé).
- Prix des plaquettes livrées en vrac à une exploitation, sur devis : le relevé Valbiom est un prix de détail TVAC.
- Rendement d'une chaudière au mazout (celui des chaudières biomasse dépasse 90 % selon Valbiom).
- Éligibilité à GREEN du chauffage d'habitations situées sur l'exploitation (dans l'exemple, la chaudière chauffe la laiterie et trois habitations) : GREEN vise les investissements d'une entreprise.
- Accès d'une exploitation agricole à la subvention AMUREBA de l'audit (règle *de minimis*), passage annoncé à 50 %, et coût réel d'une étude de faisabilité pour une chaufferie de ferme.
- Cumul de GREEN et de la déduction fédérale pour investissement (« pas encore finalisé » en février 2026)[^amureba-memo].
- Les taux de GREEN viennent du tableau du SPW Économie : l'annexe officielle de l'arrêté n'a pas pu être lue.
- Consommation réelle de mazout de l'exploitation, qui remplace l'exemple de 8 000 L.

## Sources

[^mol]: « Les chiffres clés du mazout de chauffage en Belgique », Mazout-on-line (site commercial), 26 février 2020. https://www.mazout-on-line.be/fr/actualites/astuces-et-conseils/les-chiffres-cles-du-mazout-de-chauffage-en-belgique/
[^febhel]: « Bois-énergie et agriculture belge, est-ce compatible ? », FEBHEL (Fédération interprofessionnelle belge du bois-énergie), article prévu pour Pleinchamp, avril 2024. https://www.febhel.be/sites/default/files/2024-05/version-finale---article-pleinchamps---chaudieres-biomasse-dans-l'agriculture-belge-2-pages.pdf
[^wallonie-2031]: « Chaudières au mazout et au charbon : la Wallonie reporte l'interdiction à 2031 », Wallonie.be, 3 juillet 2026. https://wallonie.be/fr/actualites/chaudieres-au-mazout-et-au-charbon-la-wallonie-reporte-linterdiction-2031
[^decret-peb]: Décret wallon du 28 novembre 2013 relatif à la performance énergétique des bâtiments, version consolidée sur Wallex : article 71/1 (inséré par le décret du 2 juillet 2026, art. 24) et article 10, 3° et 6°. Consulté le 26 novembre 2026. https://wallex.wallonie.be/eli/loi-decret/2013/11/28/2013207272
[^am-adisa]: Arrêté ministériel du 23 février 2023 exécutant l'arrêté du Gouvernement wallon du 23 février 2023 relatif aux aides à l'installation et aux investissements (secteurs agricole et horticole), version consolidée en vigueur depuis le 1er janvier 2026 (modifiée en dernier lieu le 11 mai 2026) : article 4 et annexe 3 « Investissements productifs admissibles ». Wallex, consulté le 26 novembre 2026. https://wallex.wallonie.be/eli/arrete/2023/02/23/2023042748
[^callmepower]: « Le sac de pellets passe à 7,02 euros en octobre », Callmepower, 29 octobre 2026 (relevé Valbiom d'octobre 2026, prix de détail TVAC selon la méthode de l'Observatoire des prix APERe / Énergie commune), lu le 27 novembre 2026. https://callmepower.be/fr/energie/actualites/prix-pellets-sac-7-euros-wallonie
[^valbiom-guide]: « Installer une chaudière biomasse pour me chauffer ? J'y pense ! », Les Carnets de Valbiom n° 5, mise à jour juin 2025, hébergé par le SPW Énergie. https://energie.wallonie.be/files/%c3%89nergies%20vertes/Bio%c3%a9nergie/Poele%20chaudiere/installer-une-chaudiere-biomasse-pour-se-chauffer-2025.pdf
[^reussir-tank]: « Économies d'énergie : prérefroidisseurs et récupérateurs de chaleur sont de plus en plus rentables », Réussir (France), 4 octobre 2023. https://www.reussir.fr/lait/economies-denergie-prerefroidisseurs-et-recuperateurs-de-chaleur-sont-de-plus-en-plus-rentables
[^ar20]: Arrêté royal n° 20 du 20 juillet 1970 fixant les taux de la taxe sur la valeur ajoutée et déterminant la répartition des biens et des services selon ces taux, tableau A, rubrique VII, 12° (bois de chauffage, déchets de bois : 6 %), version en vigueur en novembre 2026.
[^trustup-pac]: « Pompe à chaleur air-eau : prix et rendement », Trustup (site commercial), juillet 2026 (page inaccessible le 26 novembre 2026, lue par extrait seulement). https://blog.trustup.be/fr/pompe-a-chaleur-air-eau-prix-rendement/
[^renovation-2026]: « Nouveau le 1er octobre : un nouveau régime pour le soutien à la rénovation en Wallonie », DH (dépêche Belga), 27 septembre 2026. https://www.dhnet.be/dernieres-depeches/2026/09/27/nouveau-le-1er-octobre-un-nouveau-regime-pour-le-soutien-a-la-renovation-en-wallonie-KVHUKGCC2RBH7MJSBO4AYPH7LA
[^valbiom-haies]: « Entretenir et valoriser mes haies et bandes boisées en plaquettes bocagères ? J'y pense ! », Les Carnets de Valbiom n° 1, mars 2021, hébergé par le SPW Énergie. https://energie.wallonie.be/files/%c3%89nergies%20vertes/Bio%c3%a9nergie/Plaquettes/carnet-entretenir-et-valoriser-mes-haies-mars-2021.pdf
[^aii-liste]: « Liste des investissements admissibles », SPW Agriculture, janvier 2026, consultée le 27 novembre 2026. https://agriculture.wallonie.be/files/accueil/Aides/AII/outils/Liste%20des%20investissements%20admissibles.pdf
[^green-agw]: Arrêté du Gouvernement wallon du 23 mai 2024 relatif aux primes à l'investissement (aides GREEN), en vigueur le 1er janvier 2025 : articles 4 à 16 et 26. Wallex, consulté le 27 novembre 2026. https://wallex.wallonie.be/sites/wallex/contents/acts/108/108350/1.html
[^green-spw]: « Réforme des aides spécifiques à la protection de l'environnement et à l'utilisation de l'énergie », SPW Économie, Emploi, Recherche, publié le 28 novembre 2024, mis à jour le 23 janvier 2025, consulté le 27 novembre 2026. https://economie.wallonie.be/fr/home/actualites/actualites/reforme-des-aides-specifiques-a-la-protection-de-l-environnement-et-a-l-utilisation-de-l-energie.html
[^decret-2004]: Décret du 11 mars 2004 relatif aux incitants régionaux en faveur des petites ou moyennes entreprises, version en vigueur depuis le 1er janvier 2025, articles 3 à 5. Wallex, consulté le 27 novembre 2026. https://wallex.wallonie.be/eli/loi-decret/2004/03/11/2004200990
[^amureba]: Arrêté du Gouvernement wallon du 1er février 2024 relatif à l'octroi de subventions à l'audit ou à l'étude dans le secteur non résidentiel (AMUREBA), annexe 5. Wallex, consulté le 27 novembre 2026. https://wallex.wallonie.be/eli/arrete/2024/02/01/2024004275
[^amureba-memo]: « Mémo Table ronde des auditeurs du 6 février 2026 », SPW Énergie, consulté le 27 novembre 2026. https://energie.wallonie.be/files/Actualit%c3%a9s/20260206_m%c3%a9mo%20Table%20ronde%20auditeurs.pdf
