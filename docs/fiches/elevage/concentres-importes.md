---
id: concentres-importes
titre: Concentrés et soja importés
domaine: élevage
dependance_fossile: gasoil (culture, transport); gaz et vapeur (trituration); hexane
alternatives: [Pâturage, légumineuses fourragères, tourteau de colza du commerce, tourteau de colza fermier, féverole et pois]
vague_meilleure_alternative: 1
statut: relu
maj: 2026-11-27
---

# Concentrés et soja importés

## En bref

Le tourteau de soja, correcteur azoté de référence des rations belges, vient surtout d'Amérique du Sud[^craw-autonomie]. Le fossile entre par la culture, l'extraction de l'huile à l'hexane (un solvant pétrolier) et le transport : rendu en Europe, une tonne de tourteau de soja a demandé environ {{ v('soja_gasoil_eq_t', 0, unite=False) }} L d'équivalent gasoil en énergie non renouvelable, contre {{ v('colza_gasoil_eq_t', 0, unite=False) }} L pour le tourteau de colza européen (calculé d'après les tables INRAE-CIRAD-AFZ[^ft-energie]). La meilleure alternative est de produire la protéine sur la ferme avec l'herbe pâturée, dont le kg de matière azotée totale (MAT) revient à environ {{ v('mat_cout_herbe_paturee') }} contre {{ v('mat_cout_soja') }} pour le soja (calculé, coût français de l'herbe en 2025), et avec des prairies riches en trèfle ou en luzerne (vague 1). Le tourteau de colza du commerce remplace le soja pour un coût inférieur à protéines égales, environ {{ v('ecart_colza_soja_t', 0, unite=False) }} € par tonne de soja remplacée au prix actuel (vague 1). Le tourteau de colza pressé à la ferme et les protéagineux (féverole, pois) demandent des conditions précises (vague 2).

## Comment ça marche aujourd'hui

**Le tourteau.** La graine de soja est aplatie, puis l'huile est extraite par un solvant, l'hexane. Une tonne de graines donne environ 780 kg de tourteau et 180 kg d'huile brute[^inrae-trituration]. Le tourteau sert à nourrir le bétail, l'huile part vers l'alimentation humaine et les carburants. En pratique, la culture du soja est surtout motivée par le tourteau[^craw-autonomie].

**La dépendance wallonne.** L'herbe fournit l'essentiel des protéines produites en Wallonie pour l'élevage (62,6 %), devant les céréales (14,1 %) et le maïs ensilage (10,3 %)[^craw-autonomie]. Mais une partie des besoins doit venir de matières riches en protéines (MRP, plus de 15 % de MAT) : 21,1 % des besoins en protéines selon une estimation du CRA-W, dont la région ne produit qu'environ un cinquième[^craw-autonomie]. Les bovins utilisent 77,4 % de ces MRP, dont 49,8 % pour les troupeaux laitiers[^craw-autonomie]. Dans les fermes laitières herbagères des provinces de Liège et de Luxembourg suivies par le projet AUTOPROT, l'autonomie protéique des fourrages atteint 97 %, celle des concentrés environ 3 %[^craw-autonomie].

**Les volumes belges.** Les membres de la fédération belge des fabricants d'aliments (BFA) transforment environ 800 000 t de soja et de tourteau de soja par an (page non datée, consultée le 26/11/2026)[^bfa-soja]. Le secteur a produit 6,75 millions de tonnes d'aliments en 2025[^boerenbond]. Selon une étude du WWF Belgique, le soja utilisé pour nourrir les animaux élevés en Belgique est passé de 683 000 t en 2013 à 1,02 million de tonnes en 2018 ; les vaches laitières en consomment 19 % et les bovins viandeux 2 %, le reste allant aux porcs et aux volailles[^wwf]. La part de soja dans les concentrés pour bovins va de 5 % (bovins viandeux) à 22 % (vaches laitières)[^wwf].

**Dans la ration.** Les éleveurs laitiers wallons du projet PROTECOW distribuaient 222 g de concentrés par litre de lait en 2018-2019, avec une ration de base d'ensilage de maïs et d'herbe[^craw-autonomie]. Plus une ration contient de maïs ensilage, pauvre en protéines (7 à 9 % de la MS), plus le concentré doit être riche en protéines[^craw-autonomie].

**Teneurs en protéines** (tables INRAE-CIRAD-AFZ, sur produit brut)[^ft-mat] :

| Aliment | MAT sur brut | Prix de novembre 2026 | Coût du kg de MAT (calculé) |
|---|---|---|---|
| Tourteau de soja (49 %, Belgique) | {{ v('tourteau_soja_mat') }} | {{ v('tourteau_soja_prix') }} | {{ v('mat_cout_soja') }} |
| Tourteau de colza déshuilé | {{ v('tourteau_colza_mat') }} | {{ v('tourteau_prix') }} | {{ v('mat_cout_colza') }} |
| Tourteau de colza gras (pressé à froid) | {{ v('tourteau_colza_gras_mat') }} | même prix (hypothèse) | {{ v('mat_cout_colza_fermier') }} |
| Pois fourrager | {{ v('pois_mat') }} | {{ v('pois_prix') }} | {{ v('mat_cout_pois') }} |

Le prix du soja est une cotation belge : tourteau d'extraction 49 %, en vrac départ négoce, le 23 novembre 2026[^sillon-soja]. La teneur en MAT est celle du soja 48 des tables, un peu moins riche. Les prix du colza et du pois sont français : colza départ Rouen[^pleinchamp-colza], pois départ Marne[^depeche-semaine] ; le colza belge était coté 345 €/t en septembre 2026, au même niveau[^sillon-soja]. En France, le tourteau de soja est monté de 430 €/t le 5 novembre à 484 €/t le 25 novembre 2026[^depeche-5nov][^depeche-25nov] ; en février 2026, il se situait entre 338 et 344 €/t[^depeche-fev20][^depeche-fev25]. Le prix belge de février n'est pas public : le scénario bas applique au prix belge la baisse française, mesurée entre février et le 24 novembre (estimé)[^depeche-24nov].

## Où entrent le pétrole et le gaz

- **La culture.** Gasoil des tracteurs et des moissonneuses, produits phytosanitaires, engrais phosphatés et potassiques, séchage des graines. Le soja étant une légumineuse, il fixe lui-même l'azote de l'air : les engrais azotés pèsent peu.
- **La trituration.** Les graines sont chauffées à la vapeur avant extraction. L'hexane, solvant tiré du pétrole, extrait l'huile ; il est ensuite chassé du tourteau par la chaleur ou par de la vapeur directe, puis recyclé[^inrae-trituration]. Il ne reste qu'environ 1 % d'huile dans le tourteau[^inrae-trituration].
- **Le transport.** Camions jusqu'aux ports d'Amérique du Sud ou des États-Unis, navire jusqu'en Europe, puis camion jusqu'à l'usine d'aliments et la ferme.
- **Ordre de grandeur.** Les tables INRAE-CIRAD-AFZ (données Ecoalim) comptent 7,08 MJ d'énergie non renouvelable (fossile et nucléaire) par kg de tourteau de soja brésilien sortie d'usine au Brésil, et 8,63 MJ rendu au port de Brest. Le tourteau de colza français sortie d'usine en demande 2,77 MJ[^ft-energie]. Par kg de MAT, le soja demande donc {{ v('ratio_energie_mat_soja_colza', 1) }} plus d'énergie non renouvelable que le colza (calculé).
- **La déforestation.** Ce n'est pas du fossile, mais c'est le même produit : le soja est lié à la conversion de forêts et de savanes au Brésil et en Argentine, et le règlement européen sur la déforestation (voir plus bas) va peser sur son prix[^wwf].

**Le règlement européen sur la déforestation (RDUE).** Le règlement (UE) 2023/1115 interdit de mettre sur le marché européen du soja (et des bovins, du cacao, du café, de l'huile de palme, du caoutchouc et du bois) lié à une déforestation[^ec-rdue]. Le règlement (UE) 2025/2650 a reporté son application au 30 décembre 2026 pour les grands opérateurs, et au 30 juin 2027 pour les micro et petites entreprises[^ec-report]. Fin novembre 2026, le marché attend encore la confirmation de cette date. Jusque-là, les fabricants d'aliments paient une prime « mass balance » (FEFAC) ; si le RDUE s'applique, le soja conforme deviendrait l'offre standard des importateurs[^depeche-semaine]. Selon La Dépêche, les coûts administratifs liés au règlement se répercutent probablement déjà sur le prix du tourteau de soja[^depeche-5nov]. La BFA vise 85 % de soja conforme aux lignes directrices de la FEFAC en 2027 et 100 % en 2030[^bfa-soja].

## Les alternatives

### 1. Pâturage (vague 1)

L'herbe jeune pâturée est riche en protéines : de 12 à 22 % de MAT dans la MS selon le stade[^craw-autonomie]. La vache la récolte elle-même, sans gasoil, sans plastique et sans tourteau. Avec une herbe à {{ v('herbe_mat') }} de MAT (valeur retenue par le CRA-W dans son exemple de première coupe)[^craw-autonomie] et un coût de {{ v('herbe_paturee_cout', 0) }} pour l'herbe sur pied d'une prairie permanente (prix français 2025, hors clôtures et abreuvement)[^ca-na-fourrages], le kg de MAT revient à environ {{ v('mat_cout_herbe_paturee') }}, contre {{ v('mat_cout_ensilage_herbe') }} pour l'ensilage d'herbe et {{ v('mat_cout_soja') }} pour le tourteau de soja (calculé). L'herbe pâturée fournit donc la protéine environ trois fois moins cher que le soja au prix actuel, et reste nettement moins chère qu'au prix de février 2026 ({{ v('mat_cout_soja', scenario='bas') }}). L'ancienne référence wallonne (0,05 €/kg MS, prix de 2021)[^craw-ptd] donnait le même ordre de grandeur.

Le pâturage tournant dynamique en tire le meilleur parti. Sur 12 fermes laitières wallonnes passées à cette technique, 9 relient ce changement à la recherche d'autonomie alimentaire et 8 mettent en avant un gain économique[^craw-ptd]. La mise en place (paddocks, chemins, points d'eau) est détaillée dans la fiche [Ensilage et enrubannage](fourrages-recoltes.md).

**Aides.** Les prairies pâturées reçoivent l'éco-régime « prairies permanentes » ({{ v('er_pp_base_eur_ha', 0) }} prévus, plus {{ v('er_pp_supp_eur_ha', 0) }} entre 0,6 et 2 UGB/ha de surface fourragère)[^er-pp] et, pour un troupeau peu chargé, la MAEC « autonomie fourragère » MB13A ({{ v('maec_mb13a_eur_ha', 0, unite=False) }} € par hectare de prairie et par an sous 1,4 UGB/ha, effluents de la ferme seulement)[^mb13]. Les deux se cumulent[^mb13]. Détails dans la fiche [Ensilage et enrubannage](fourrages-recoltes.md) et sur la page [les aides publiques](../../aides.md#pac-2e-pilier-maec-bio-natura-2000-installation). Le pâturage est rentable sans elles (vague 1).

Limites : le pâturage ne couvre que la saison de pousse. L'hiver, et pour les vaches à très haut niveau de production, il faut encore des fourrages conservés et un correcteur. Il demande assez de prairies accessibles autour des bâtiments.

### 2. Légumineuses fourragères : trèfle et luzerne (vague 1)

Des prairies temporaires avec trèfle violet, trèfle blanc ou luzerne produisent un fourrage riche en protéines sans engrais azoté. Elles fixent l'azote de l'air, améliorent la structure du sol et en laissent à la culture suivante[^craw-luzerne] (voir la fiche [Azote de synthèse](../fertilisation/azote-synthese.md)).

**Protéines par hectare.** Le CRA-W cite une référence allemande : 920 kg de MAT par hectare et par an pour le soja (2,3 t MS à 40 %), contre 2 160 kg pour la luzerne entière (12 t MS à 18 %)[^craw-luzerne]. La luzerne produit donc deux à trois fois plus de protéines par hectare que le soja[^craw-luzerne].

**Résistance à la sécheresse.** Dans des essais de l'UCLouvain financés par le SPW à Corroy-le-Grand (2013-2018), luzerne et trèfle violet ont mieux résisté au manque d'eau que les graminées, sans aucun apport d'azote. En 2015, année sèche, la deuxième coupe a donné environ 2 t MS/ha pour le ray-grass anglais, 5,5 t pour le trèfle violet et 8 à 9 t pour la luzerne. En 2017-2018, la luzerne pure et l'association dactyle et luzerne ont donné les meilleurs rendements[^spw-secheresse].

**Coût.** Un ensilage d'herbe revient à environ {{ v('ensilage_herbe_cout', 0) }} (estimé d'après des repères français de 2025 : herbe sur pied et récolte, travail payé, hors pertes de conservation et bâche)[^ca-na-fourrages]. À {{ v('herbe_mat') }} de MAT, son kg de MAT coûte environ {{ v('mat_cout_ensilage_herbe') }} (calculé) : moins que le tourteau de soja au prix actuel ({{ v('mat_cout_soja') }}), mais plus qu'au prix de février 2026 ({{ v('mat_cout_soja', scenario='bas') }}). Voir la fiche [Ensilage et enrubannage](fourrages-recoltes.md). L'ensilage de légumineuses ne bat donc le soja sur le seul prix de la protéine que pendant la crise ; avant la crise, il ne le battait que pâturé, ou plus riche en protéines que l'herbe de référence. Sa rentabilité tient surtout à l'engrais azoté évité, à la résistance à la sécheresse et, quand on les fait pâturer, au faible coût de l'herbe pâturée.

**Aides.** La luzerne, la lupuline, le sainfoin, le lotier et la vesce cultivés sur terre arable ouvrent l'éco-régime « cultures favorables » V1_A : {{ v('er_cfe_v1a_eur_ha', 0) }} prévus (220 à 420 €/ha selon la demande), à condition de n'utiliser aucun insecticide, même en enrobage des semences, et de laisser 10 % de zone refuge[^cfe]. Le **trèfle n'est pas dans cette liste** : une prairie temporaire au trèfle violet ou blanc ne touche pas cet éco-régime[^cfe]. En bio, l'aide au maintien ajoute {{ v('bio_prairie_eur_ha', 0) }} pour les légumineuses fourragères (60 premiers hectares), cumulable avec l'éco-régime[^bio] [^cumuls].

Cet éco-régime améliore la marge de la luzerne par rapport au tourteau acheté, sans changer la vague (déjà 1). Il avantage la luzerne sur le trèfle, qui n'y a pas droit. Comme tout éco-régime, c'est un engagement d'un an dont le montant payé n'est connu qu'après la campagne.

Conditions :

- récolter jeune, au stade début bourgeonnement pour la luzerne, et soigner la conservation. Les pertes en matière sèche d'un ensilage d'herbe vont de 13 à 47 % selon les pratiques[^craw-autonomie] ;
- ajouter un conservateur pour légumineuses, car la luzerne s'ensile mal[^craw-luzerne] ;
- un sol sain et une année favorable : les pluies abondantes et les basses températures de 2016 ont pénalisé la luzerne et le trèfle violet dans les essais de l'UCLouvain[^spw-secheresse].

Limites : la protéine de l'herbe et de la luzerne est très dégradable dans le rumen, contrairement à celle du tourteau de soja[^craw-luzerne]. Dans un essai du CRA-W en 2023 sur deux lots de cinq vaches, remplacer le correcteur à base de soja par un ensilage de feuilles de luzerne a fait baisser l'ingestion (19,5 contre 21,2 kg MS par jour) et le lait (21,9 contre 25,7 L par jour), probablement par manque d'énergie[^craw-luzerne]. La luzerne réduit le besoin de tourteau ; elle ne le supprime pas toujours chez les fortes productrices.

### 3. Tourteau de colza du commerce (vague 1)

Le tourteau de colza vient d'huileries européennes. Il est moins riche que le soja (39 à 43 % de MAT dans la MS, contre 48 à 53 %)[^craw-autonomie]. À protéines égales, il faut {{ v('colza_pour_1kg_soja') }} de tourteau de colza pour remplacer 1 kg de tourteau de soja 48 (calculé sur la MAT[^ft-mat]).

**Coût.** Au prix de novembre 2026, remplacer une tonne de soja par la quantité de colza qui apporte la même MAT donne un écart de {{ v('ecart_colza_soja_t', 0, unite=False) }} € par tonne de soja remplacée (calculé ; un chiffre négatif veut dire que le colza revient moins cher). Dans le scénario bas, l'écart est de {{ v('ecart_colza_soja_t', 0, unite=False, scenario='bas') }} €. Attention : le prix de février 2026 du tourteau de colza n'a pas été trouvé ; le scénario bas compare donc deux prix estimés : celui du soja (baisse française appliquée au prix belge) et celui du colza (−30 %, hypothèse).

**Énergie fossile.** Le kg de MAT de colza européen demande environ {{ v('ratio_energie_mat_soja_colza', 1) }} moins d'énergie non renouvelable que celui du soja brésilien rendu en Europe (calculé[^ft-energie]).

Limites : à poids égal, le tourteau de colza apporte moins d'énergie et de protéines protégées du rumen que le soja ; il faut donc recalculer la ration. Le colza est trituré lui aussi à l'hexane dans les grandes huileries : le tourteau du commerce réduit le transport et la déforestation, pas la dépendance au solvant[^inrae-trituration]. Le colza cultivé reçoit de l'engrais azoté de synthèse.

### 4. Tourteau de colza fermier (vague 2)

Une petite presse à froid sépare à la ferme l'huile et le tourteau. Il n'y a ni hexane ni vapeur, mais le tourteau reste gras : 12 à 18 % de matière grasse, contre 2 à 2,5 % pour un tourteau déshuilé du commerce (Institut de l'élevage, référence française ancienne)[^idele-presse]. Une presse fermière laisse environ 15 % d'huile dans le tourteau, contre environ 1 % en huilerie[^inrae-trituration]. Ce tourteau gras contient {{ v('tourteau_colza_gras_mat') }} de MAT sur brut[^ft-mat].

**Le lien avec le carburant.** L'huile peut alimenter un tracteur adapté (voir la fiche [Tracteur diesel](../traction/tracteur-diesel.md)). Une tonne de graines donne environ {{ v('tourteau_par_tonne', 2, unite=False) }} t de tourteau et {{ v('huile_par_tonne', unite=False) }} L d'huile (valeurs centrales d'une fiche du CRA-W et de l'Idele)[^autoprot]. Le calcul du coût de l'huile y déduit la valeur du tourteau au prix du commerce. Même ainsi, pressage payé, l'huile carburant reste plus chère que le gasoil dans les trois scénarios de prix (voir la fiche tracteur) : le débouché qui paie la presse est plutôt l'huile alimentaire vendue en direct (voir la fiche [Transformation industrielle](../transformation/transformation-industrielle.md)). Valorisé à ce prix, le kg de MAT du tourteau fermier coûte {{ v('mat_cout_colza_fermier') }} (calculé), un peu plus que le tourteau déshuilé, mais il apporte en plus de l'énergie sous forme de matière grasse.

Conditions :

- limiter la quantité : une ration de vache laitière ne doit pas dépasser 4,5 à 5 % de matière grasse. Avec une ration à base d'ensilage de maïs, on ne distribue pas plus de 1,5 à 2 kg de tourteau gras par vache et par jour, ce qui ne suffit pas à remplacer 4 kg de tourteau de soja chez une forte productrice[^idele-presse] ;
- un débouché pour l'huile : carburant de la ferme (avec l'autorisation « utilisateur final » des accises, voir la fiche tracteur), vente ou alimentation ;
- une presse, un stockage propre de l'huile et du tourteau, et du temps de travail. Un pressage collectif (CUMA, coopérative) réduit le coût.

Pourquoi vague 2 : la rentabilité dépend du débouché de l'huile (vente alimentaire en direct surtout, car comme carburant elle coûte plus que le gasoil) et de l'organisation (presse en commun). Le tourteau gras ne couvre qu'une partie du besoin en correcteur.

### 5. Féverole et pois, crus ou toastés (vague 2)

Les protéagineux se cultivent en Wallonie. La féverole contient 30 à 31 % de MAT dans la MS, le pois environ 23 %, le lupin 35 à 41 %[^craw-autonomie]. Ils fixent l'azote de l'air et diversifient la rotation. Le toastage (chauffage des graines) rend une partie de leurs protéines moins dégradable dans le rumen ; la féverole toastée fait partie des leviers étudiés par PROTECOW[^craw-autonomie].

**Où en est la Wallonie.** La Belgique est passée de 4 637 ha de légumineuses à graines en 2019 à 10 594 ha en 2025, dont plus de 77 % en Wallonie ; une partie de la hausse vient de l'inclusion des méteils dans les statistiques[^walprot]. Ces cultures restent sous 2 % des terres arables wallonnes (2024)[^walprot]. Le plan du Collège des Producteurs vise 15 000 ha de protéines végétales en Wallonie en 2030, avec six cultures prioritaires : pois, féverole, colza, lupin, luzerne et soja[^walprot].

**Coût.** Au prix de novembre 2026, le kg de MAT du pois fourrager coûte {{ v('mat_cout_pois') }}, plus cher que celui du soja ({{ v('mat_cout_soja') }}) (calculé). C'est encore vrai au prix de février 2026 ({{ v('mat_cout_pois', scenario='bas') }} contre {{ v('mat_cout_soja', scenario='bas') }}). Le pois apporte aussi de l'amidon, qui remplace une partie des céréales : son prix ne paie pas seulement la protéine. Aucune cotation de la féverole n'était disponible en novembre 2026[^depeche-semaine].

Limites : rendements irréguliers, graines aussi consommables par l'homme, place à trouver dans l'assolement[^craw-autonomie]. Parmi les freins relevés par le rapport WalProt du CRA-W (2026) figurent l'instabilité des rendements, le manque d'outils de collecte et de transformation, la concurrence des produits importés à bas prix et le manque de coordination de la filière[^walprot]. Le toastage demande une installation et de la chaleur : pour que le gain soit complet, cette chaleur doit venir d'une source renouvelable (unité collective au bois, au biogaz ou à l'électricité solaire).

**Aides.** Deux voies existent, qui **ne se cumulent pas** sur une même parcelle[^cumuls] (voir [les aides publiques](../../aides.md#les-regles-de-cumul)) :

- **pois ou féverole purs** (ou dominants dans un mélange), récoltés après le 15 juin : soutien couplé aux protéines végétales ({{ v('soutien_proteines_eur_ha', 0) }} prévus, 270 à 400 €/ha)[^couple-prot], cumulable avec l'éco-régime « réduction d'intrants » ({{ v('ri_eur_ha', 0) }} prévus) si la parcelle n'utilise aucune des 36 molécules « à substituer » ou reçoit deux désherbages mécaniques[^ri]. Ensemble : {{ v('proteagineux_aides_ha', 0) }} (calculé). Pas de réduction d'intrants en bio[^ri] ;
- **mélange céréales-légumineuses** (au moins 50 % de céréales et 20 % de légumineuses) récolté après le 15 juin : éco-régime « cultures favorables » V3_B, {{ v('er_cfe_v3b_eur_ha', 0) }} prévus, sans insecticide[^cfe]. Il ne se cumule pas avec la réduction d'intrants[^cumuls].

La voie du soutien couplé rapporte {{ v('proteagineux_ecart_v3b_ha', 0) }} de plus (calculé), mais seulement si la parcelle remplit aussi les conditions de la réduction d'intrants ; sinon le mélange en V3_B paie davantage. En bio, l'aide au maintien ({{ v('bio_autres_cultures_eur_ha', 0) }} pour les protéagineux) s'ajoute aux deux voies[^bio] [^cumuls].

Ces aides sont payées à l'hectare, quel que soit le prix de la récolte : elles améliorent la marge de la culture, alors que la comparaison au kg de MAT sans aide la donne perdante face au soja. Le coût du kg de protéine aide comprise n'est pas calculé ici, faute de rendement de référence wallon pour le pois et la féverole (voir « À vérifier »).

Pourquoi vague 2 : sans aide, au prix du marché, le kg de MAT du pois coûte plus cher que celui du soja, avant comme pendant la crise. La culture ne devient intéressante que sous conditions : aides PAC aux protéagineux (dont le montant payé varie chaque année), bénéfice de rotation reconnu (précédent pour le blé, économie d'azote) et outil de toastage partagé. Une alternative qui ne tient que par une aide annuelle reste en vague 2.

## Ce qui ferme la boucle

- La vache récolte l'herbe et rend ses bouses à la prairie : la protéine est produite sur place, sans transport ni solvant.
- Trèfle, luzerne, féverole et pois fixent l'azote de l'air : ils remplacent à la fois le tourteau acheté et l'engrais azoté.
- Le colza pressé à la ferme donne l'huile pour le tracteur et le tourteau pour les animaux ; le fumier fertilise les cultures suivantes.
- Une ration moins poussée réduit le besoin de correcteur. Les éleveurs wallons de PROTECOW ont réduit de 14 % leurs concentrés par litre de lait (de 235 à 202 g) entre 2016-2017 et 2019-2020, en valorisant mieux leurs fourrages et en ajustant la complémentation[^craw-autonomie].
- Ce qui reste à acheter peut venir de coproduits locaux (solubles de blé, drèches, pulpes) plutôt que de soja d'outre-mer[^craw-autonomie].

## À vérifier

- Prix belge de février 2026 du tourteau de soja (historique réservé aux abonnés du Sillon belge) et prix belge récent du tourteau de colza (dernière cotation publiée : septembre 2026).
- Prix du tourteau de colza en février 2026 : non trouvé ; le scénario bas utilise −30 % (hypothèse). Les bulletins de La Dépêche de février ne donnent que des variations.
- Prix de la féverole en novembre 2026 (non cotée en France) et prix belge du pois.
- Coûts wallons actualisés de l'herbe pâturée et de l'ensilage d'herbe par tonne de MS : les valeurs utilisées ({{ v('herbe_paturee_cout', 0) }} et {{ v('ensilage_herbe_cout', 0) }}) sont des repères français de 2025 ; la dernière référence wallonne lue (CRA-W d'après Fourrages Mieux) date de 2021. Le coût de l'ensilage ne compte ni les pertes de conservation (13 à 47 % de la MS) ni la bâche : il est sous-estimé quand la conservation est mal maîtrisée.
- Règle pratique de remplacement du soja par le colza (souvent citée : 1 kg de soja pour 1,5 kg de colza) et valeurs PDIE/DVE des deux tourteaux : non lues dans une source fiable. Le calcul de la fiche ne compare que la MAT.
- Volume de tourteau de soja importé en Belgique en 2025 et part consommée par les bovins (statistiques BFA ou Statbel) : le dernier chiffre lu date de 2018 (WWF).
- Décomposition de l'énergie fossile du tourteau de soja (culture, trituration, transport maritime) et données propres à un tourteau livré en Belgique (port d'Anvers ou de Gand).
- Résultat de la revue de simplification du RDUE prévue en 2026 et confirmation de l'application au 30 décembre 2026.
- Coût d'un toastage à façon de féverole ou de pois en Wallonie et énergie utilisée par les unités existantes.
- Coût d'une presse à huile fermière en 2026 et tarifs de pressage collectif en Wallonie : le projet utilise le tarif d'une CUMA française à presse amortie ({{ v('pressage_cout', 2) }}).
- Montants **payés** en 2025 et 2026 du soutien couplé aux protéagineux, de la réduction d'intrants et des cultures favorables : seuls les montants prévus sont connus (400 €/ha de soutien couplé payés en 2024)[^couple-prot].
- Rendement de référence wallon du pois et de la féverole, pour chiffrer le coût du kg de MAT aide comprise.
- Un mélange où le pois ou la féverole dominent en grains/m² peut toucher le soutien couplé : à quelle limite le choix entre soutien couplé et V3_B se fait-il en pratique ?

## Sources

[^craw-autonomie]: Boulet L., Battheu-Noirfalise C., « Autonomie et efficience protéique des élevages laitiers », CRA-W (synthèse des projets Interreg AUTOPROT et PROTECOW), 2022. https://www.cra.wallonie.be/uploads/2022/09/2022-brochureautonomieproteique-a4-web.pdf
[^inrae-trituration]: Fine F., Lucas J.-L., Chardigny J.-M., Redlingshöfer B., Renard M., « Pertes alimentaires dans la filière oléagineuse », Innovations Agronomiques, 48, p. 97-114, 2015 (CETIOM, INRA). https://hal.inrae.fr/hal-02629820v1/document
[^ft-mat]: « Crude protein » (teneurs en matière azotée totale), Tables de composition et de valeur nutritive des matières premières, INRAE-CIRAD-AFZ, consultées le 26 novembre 2026. https://www.feedtables.com/content/crude-protein
[^ft-energie]: « Cumulative energy demand, non renewable (fossil+nuclear) », Tables INRAE-CIRAD-AFZ (données Ecoalim), consultées le 26 novembre 2026. https://www.feedtables.com/content/cumulative-energy-demand-non-renewable-fossilnuclear
[^bfa-soja]: « Duurzame soja », Belgian Feed Association (BFA), page non datée, consultée le 26 novembre 2026. https://bfa.be/DuurzameSoja
[^boerenbond]: « Veevoedersector houdt stand maar vreest Iran-inflatie », Boerenbond, 2026 (accès partiel, chapeau lu le 26 novembre 2026). https://www.boerenbond.be/node/22048
[^wwf]: « Soja » (fiche d'information), WWF Belgique, avril 2021 (date tirée de l'adresse du document), d'après UN Comtrade et FAO Stat, 2013-2018. https://support.wwf.be/sites/default/files/2021-04/Factsheet-SOY-final-FR.pdf
[^depeche-24nov]: « Marché des oléagineux du 24 novembre 2026 : le prix du soja engrange une troisième séance de hausse », La Dépêche - Le Petit Meunier (Réussir), 24 novembre 2026, tableau des cotations. https://www.reussir.fr/articles/marche-des-oleagineux-du-24-novembre-2026-le-prix-du-soja-engrange-une-troisieme-seance-de
[^depeche-25nov]: « Marché des oléagineux du 25 novembre 2026 : le soja poursuit sa progression sur le CBOT », La Dépêche (Réussir), 25 novembre 2026. https://www.reussir.fr/articles/marche-des-oleagineux-du-25-novembre-2026-le-soja-poursuit-sa-progression-sur-le-cbot
[^depeche-5nov]: « Marché des oléagineux du 5 novembre 2026 : repli généralisé des cours », La Dépêche (Réussir), 5 novembre 2026. https://www.reussir.fr/articles/marche-des-oleagineux-du-5-novembre-2026-repli-generalise-des-cours-malgre-des
[^depeche-semaine]: K. Floquet, « Marché des oléagineux et coproduits du 11 au 18 novembre 2026 », La Dépêche (Réussir), 19 novembre 2026. https://www.reussir.fr/articles/marche-des-oleagineux-et-coproduits-du-11-au-18-novembre-2026-les-prix-du-colza-ont-vire
[^depeche-fev20]: « Marché des oléagineux du 20 février 2026 : le prix du colza retombe sous la barre des 490 €/t sur Euronext », La Dépêche (Réussir), 20 février 2026. https://www.reussir.fr/marche-des-oleagineux-du-20-fevrier-2026-le-prix-du-colza-retombe-sous-la-barre-des-490-eut-sur
[^depeche-fev25]: « Marché des oléagineux du 25 février 2026 : le prix européen du colza repasse sous la barre des 490 €/t », La Dépêche (Réussir), 25 février 2026. https://www.reussir.fr/ladepeche/marche-des-oleagineux-du-25-fevrier-2026-le-prix-europeen-du-colza-repasse-sous-la-barre-des-490
[^pleinchamp-colza]: « Tourteaux de colza », cotation Argus Media publiée par Pleinchamp, relevé du 24 novembre 2026, lu le 26 novembre 2026. https://www.pleinchamp.com/les-cours/aliments-du-betail/43-tourteaux-de-colza
[^ec-rdue]: « Implementing the EU Deforestation Regulation (EUDR) », Commission européenne, Green Forum, consulté le 26 novembre 2026. https://green-forum.ec.europa.eu/deforestation-regulation-implementation_en
[^ec-report]: « Retard jusqu'en décembre 2026 et autres évolutions dans la mise en œuvre du règlement EUDR », Commission européenne, Access2Markets, 28 janvier 2026. https://trade.ec.europa.eu/access-to-markets/fr/news/retard-jusquen-decembre-2026-et-autres-evolutions-dans-la-mise-en-oeuvre-du-reglement-eudr
[^ca-na-fourrages]: « Fourrages 2025 : des repères de prix », Chambres d'agriculture de Nouvelle-Aquitaine, 2025 (prix français, engrais de l'automne 2024, tarifs d'entraide 2025), lu le 27 novembre 2026. https://cmds.chambres-agriculture.fr/fileadmin/user_upload/Nouvelle-Aquitaine/Medias_Externes/Synthese_prix_fourrages_2025.pdf
[^autoprot]: « Production de tourteau de colza gras à la ferme », fiche Autoprot C1, CRA-W et Idele, juin 2021 (240 à 350 L d'huile et 0,68 à 0,78 t de tourteau par tonne de graines selon la presse), lue le 27 novembre 2026. https://www.autoprot.eu/wp-content/uploads/2021/10/Fiche-C1-Production-de-tourteau-de-colza-gras-a-la-ferme.pdf
[^craw-ptd]: Lefèvre A., « Motivations, freins et leviers face à des changements de pratiques visant à optimiser la valorisation des fourrages. Retour d'expérience d'éleveurs laitiers wallons », CRA-W, mai 2022 (coût de l'herbe d'après Glesner N., Lefèvre A., *Lettre paysanne* FUGEA, 2021). https://www.cra.wallonie.be/uploads/2022/06/delivrable-3-4-retour-dexperience-deleveurs-laitiers-wallons-motivations-freins-leviers-face-a-des-changements-de-pratiques-visant-a-ameliorer-lerf.pdf
[^craw-luzerne]: « Récolter des feuilles de luzerne, un moyen de concentrer les protéines ! », CRA-W pour les Contrats captage, 2024 (essais 2022-2023 ; tableau de production d'après Junker, 2016). https://www.cra.wallonie.be/uploads/2024/03/recolter-des-feuilles-de-luzerne-un-moyen-de-concentrer-les-proteines.pdf
[^spw-secheresse]: Nihoul Ph. (SPW-ARNE), Lambert R. (UCLouvain), « Production fourragère des prairies : quelles espèces traditionnelles pérennes les plus adaptées à la sécheresse ? », synthèse d'essais 2013-2018, SPW Agriculture, document non daté, consulté le 26 novembre 2026. https://agriculture.wallonie.be/files/accueil/Recherche%20et%20d%c3%a9veloppement/Secheresse/r%c3%a9silience%20fourrag%c3%a8re/Quelles%20esp%c3%a8ces%20traditionnelles%20p%c3%a9rennes%20les%20plus%20adapt%c3%a9es%20%c3%a0%20la%20s%c3%a9cheresse%20%20.pdf
[^idele-presse]: F. Mechekour, « Les tourteaux pressés à la ferme ont un fort taux de matière grasse, note l'Institut de l'élevage » (entretien avec Ph. Brunschwig), Réussir Lait (France), 17 septembre 2003. https://www.reussir.fr/lait/les-tourteaux-presses-la-ferme-ont-un-fort-taux-de-matiere-grasse-note-linstitut-de-lelevage
[^er-pp]: « Eco-régime prairies permanentes conditionné à la charge en bétail », Portail de l'agriculture wallonne, page modifiée le 17 avril 2026, consultée le 27 novembre 2026. https://agriculture.wallonie.be/home/aides/pac-2023-2027-description-des-interventions/eco-regimes/eco-regime-prairies-permanentes-conditionnee-a-la-charge-en-betail.html
[^mb13]: « MAEC Autonomie fourragère – MB13 », Portail de l'agriculture wallonne, page modifiée le 17 avril 2026, consultée le 27 novembre 2026. https://agriculture.wallonie.be/home/aides/pac-2023-2027-description-des-interventions/mesures-agro-environnementales-et-climatiques/maec-autonomie-fourragere---mb13.html
[^cfe]: « Eco-régime cultures favorables à l'environnement », Portail de l'agriculture wallonne, page modifiée le 17 avril 2026, consultée le 27 novembre 2026. https://agriculture.wallonie.be/home/aides/pac-2023-2027-description-des-interventions/eco-regimes/eco-regime-culture-favorable-a-l-environnement.html
[^ri]: « Eco-régime réduction d'intrants », Portail de l'agriculture wallonne, page modifiée le 3 juillet 2026, consultée le 27 novembre 2026. https://agriculture.wallonie.be/home/aides/pac-2023-2027-description-des-interventions/eco-regimes/eco-regime-reduction-d-intrants.html
[^couple-prot]: « Soutien couplé aux cultures de protéines végétales », Portail de l'agriculture wallonne, page modifiée le 21 novembre 2025, consultée le 27 novembre 2026. https://agriculture.wallonie.be/home/aides/pac-2023-2027-description-des-interventions/soutien-couple/soutien-couple-aux-cultures-de-proteines-vegetales.html
[^bio]: « Soutien à l'agriculture biologique », Portail de l'agriculture wallonne, page modifiée le 17 avril 2026, consultée le 27 novembre 2026. https://agriculture.wallonie.be/home/aides/pac-2023-2027-description-des-interventions/soutien-a-l-agriculture-biologique.html
[^cumuls]: « Cumuls entre les aides », Portail de l'agriculture wallonne, page modifiée le 18 septembre 2025 (tableaux « prairie » et « culture »), consultée le 27 novembre 2026. https://agriculture.wallonie.be/home/aides/pac-2023-2027-description-des-interventions/cumuls-entre-les-aides.html
[^walprot]: Verhoeven C., Cassart P., Froidmont É., Van Stappen F., « Portrait de la filière des protéines végétales et alternatives en Wallonie. Analyse qualitative des barrières et leviers », CRA-W, projet Wal'Prot (IIS Protewin), juin 2026. https://www.cra.wallonie.be/uploads/2026/07/rapport-walprot-portrait-filiere-proteines-vegetales-alternatives-wallonie-2026-pdf.pdf
[^sillon-soja]: « Tourteau extraction soja, 49 %, Belgique » (vrac, départ négoce, 531 €/t le 23 novembre 2026) et « Tourteau extraction colza, 34 %, Belgique » (345 €/t le 15 septembre 2026), marchés de l'alimentation animale, Le Sillon belge, lus le 27 novembre 2026. https://www.sillonbelge.be/marches/matieres-premieres
