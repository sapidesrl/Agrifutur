---
id: engrais-p-k
titre: Engrais phosphatés et potassiques
domaine: fertilisation
dependance_fossile: gasoil (mines et transport)
alternatives: [Effluents, compost, cendres de bois, recyclage urbain]
vague_meilleure_alternative: 1
statut: brouillon
maj: 2026-11-26
---

# Engrais phosphatés et potassiques

## En bref

Le phosphore (P) et le potassium (K) des engrais minéraux viennent de mines lointaines : phosphate du Maroc surtout, potasse du Canada, de Russie, de Biélorussie ou de Chine[^eew-engrais]. Le phosphate est attaqué à l'acide sulfurique, fait avec du soufre du Moyen-Orient, puis tout voyage par bateau et camion. Au prix de l'automne 2026, le kg de P2O5 du superphosphate coûte {{ v('prix_kg_p2o5') }} et le kg de K2O du chlorure de potassium {{ v('prix_kg_k2o') }} (prix français, calculés).

En Wallonie, 80 % du phosphore apporté aux sols vient déjà des effluents d'élevage[^eew-sols-p]. Bien gérés, ils restent la meilleure alternative : le P et le K d'une tonne de fumier de bovins valent {{ v('valeur_pk_fumier', 1) }}, et encore {{ v('valeur_pk_fumier', 1, scenario='bas') }} au prix d'avant-crise (calculé). C'est rentable aujourd'hui, crise ou pas (vague 1). Le compost et les cendres de bois complètent dans certaines fermes (vague 2). Le recyclage du phosphore des eaux usées (struvite, cendres de boues) reste à préparer (vague 3).

## Comment ça marche aujourd'hui

Le phosphore et le potassium sont des éléments majeurs de la nutrition des plantes, avec l'azote. On les apporte en « fumure de fond », avant ou pendant l'implantation de la culture. Les formes courantes sont :

- le **superphosphate triple** (TSP, 45 % de P2O5) ;
- le **chlorure de potassium** (KCl, 60 % de K2O), aussi appelé potasse ;
- les **binaires** PK (par exemple 0-25-25) et les **ternaires** NPK.

Prix de gros relevés en France (stade distributeur)[^depeche-nov] [^depeche-mars] :

| Engrais | Février 2026 (avant-crise) | Septembre-octobre 2026 |
|---|---|---|
| Superphosphate triple | {{ v('tsp_prix', scenario='bas') }} | {{ v('tsp_prix') }} |
| Chlorure de potassium | {{ v('kcl_prix', scenario='bas') }} | {{ v('kcl_prix') }} |

Au départ de Gand, un négociant en ligne affichait fin novembre 2026 des prix du même ordre : TSP à 675 €/t et chlorure de potassium à 360 €/t[^agryco]. Le prix payé à la ferme peut être plus élevé : un essai wallon comptait le chlorure de potassium à 420 €/t en juillet 2025[^fm-bache].

Le phosphore a suivi la crise, pas la potasse. Le prix du TSP a monté d'environ 26 % depuis février (calculé), alors que celui de la potasse est resté stable, voire a un peu baissé. Le kg de P2O5 coûte {{ fourchette('prix_kg_p2o5') }} selon les scénarios de prix, le kg de K2O {{ fourchette('prix_kg_k2o') }} (calculé).

Les agriculteurs réagissent en réduisant la fumure de fond. En France, les livraisons d'engrais phosphatés ont reculé d'environ 30 % et celles de potassiques de 17 % au début de la campagne 2026-2027. Les distributeurs s'attendent à une baisse de 50 à 60 % de la demande en phosphore sur l'ensemble de la campagne[^depeche-nov].

En Wallonie, l'usage d'engrais minéraux P et K a déjà fortement baissé. En 2023, on épandait en moyenne 23,6 kg de K2O et 9,7 kg de P2O5 minéraux par hectare de surface agricole. Ces quantités avaient baissé de 70 % (K) et 76 % (P) entre 1995 et 2009, puis encore de 28 % et 36 % en 2022, avec la crise énergétique[^eew-engrais].

### L'état des sols wallons

Pendant des décennies, jusqu'aux environs de l'an 2000, les apports de phosphore ont dépassé les besoins des cultures. Le phosphore s'est accumulé dans les sols. Depuis, le bilan est négatif : les cultures puisent dans ce stock, sans baisse de leurs exportations[^eew-sols-p].

- Sous cultures (prairies temporaires comprises), la teneur moyenne en phosphore disponible était de 7,3 mg/100 g sur 2021-2025, entre 3,9 et 8,5 mg/100 g selon les régions agricoles. Pour un sol de texture moyenne, l'état est considéré comme bon entre 4,6 et 7,5 mg/100 g ; au-delà, il y a un risque de déséquilibre et de pertes vers les eaux, à apprécier à la parcelle[^eew-sols-p].
- Ces teneurs baissent : − 11 % en moyenne entre 2006-2010 et 2021-2025, − 14 % en Région limoneuse, − 18 % en Région sablo-limoneuse, − 13 % en Condroz[^eew-sols-p].
- Selon Requasud, les teneurs en P diminuent presque partout, sauf dans les sols déjà pauvres. Le potassium baisse en Région limoneuse et en Ardenne et reste stable ailleurs[^requasud-2023].
- En prairie, le potassium manque souvent : selon le Centre de Michamps, 40 % des fourrages analysés présentent une carence en potassium[^fm-bache].

Conséquence pratique : dans une terre riche en phosphore, l'analyse de sol peut justifier de réduire ou de suspendre l'engrais phosphaté quelques années. C'est ce qui se passe déjà à l'échelle de la Wallonie : depuis 2000, les cultures puisent dans le stock sans baisse de leurs exportations[^eew-sols-p]. Ce n'est pas une alternative durable : le stock s'épuise, et il faudra le relayer par des apports recyclés.

## Où entrent le pétrole et le gaz

- **Extraction** : mines de phosphate et de potasse, avec des engins et des installations qui fonctionnent au fioul, au gaz et à l'électricité.
- **Procédé** : la roche phosphatée est attaquée par l'acide sulfurique. Cet acide est fait avec du soufre, venu surtout du Moyen-Orient[^depeche-nov]. La moitié des exportations mondiales de soufre passaient par le détroit d'Ormuz avant la crise, et son prix est passé d'environ 500 $/t fin février 2026 à plus de 1 000 $/t début septembre[^escp]. Le DAP et le MAP demandent en plus de l'ammoniac, fabriqué au gaz naturel (voir la fiche [engrais azoté de synthèse](azote-synthese.md))[^escp].
- **Transport** : par bateau depuis le Maroc, l'Amérique du Nord ou l'Europe de l'Est, puis camion. L'exploitation de la potasse d'Alsace s'est arrêtée en 2002[^eew-engrais].
- **Émissions** : pour le chlorure de potassium, environ 0,70 kg d'équivalent CO2 par kg de K2O ; 1,42 kg pour le sulfate de potassium, utilisé en agriculture biologique (facteurs cités par Fourrages Mieux)[^fm-bache].
- **Épandage** : passages de tracteur au gasoil.

La dépendance est aussi géopolitique. Le Maroc détient environ 68 % des réserves mondiales de roche phosphatée, et son groupe public OCP environ 30 % du commerce mondial de produits phosphatés[^escp]. Les sanctions européennes contre la Russie et la Biélorussie, depuis 2021, ont relancé l'intérêt pour les gisements de potasse en Allemagne[^eew-engrais]. Enfin, les phosphates d'Afrique du Nord contiennent plus de cadmium (38 à 200 mg par kg de P2O5) que ceux de Russie (moins de 1 mg). Le règlement européen sur les fertilisants plafonne le cadmium à 60 mg par kg de P2O5[^eew-engrais].

## Les alternatives

### 1. Effluents d'élevage (vague 1)

Fumiers et lisiers sont des engrais complets. Selon Protect'eau, tout le phosphore et tout le potassium qu'ils contiennent sont disponibles pour la culture suivante (coefficient d'équivalence de 1). Seule exception : sur un sol pauvre en phosphore, on ne compte que 85 % du phosphore d'un lisier[^protecteau].

Teneurs moyennes en Wallonie (sources PGDA et Requasud)[^protecteau] :

| Effluent | P2O5 | K2O |
|---|---|---|
| Fumier de bovins | {{ v('fumier_bovin_p2o5', 1) }} | {{ v('fumier_bovin_k2o', 1) }} |
| Lisier de bovins | {{ v('lisier_bovin_p2o5', 1) }} | {{ v('lisier_bovin_k2o', 1) }} |
| Lisier de porcs | 3,5 kg/t | 4,7 kg/t |
| Fumier de volailles | 14,9 kg/t | 15,1 kg/t |

Ce que valent ces éléments aux prix des engrais (calculé, coefficient d'équivalence de 1) :

| Effluent | Valeur du P et du K, prix actuel | Fourchette des scénarios |
|---|---|---|
| Fumier de bovins, par tonne | {{ v('valeur_pk_fumier') }} | {{ fourchette('valeur_pk_fumier') }} |
| Lisier de bovins, par m³ | {{ v('valeur_pk_lisier') }} | {{ fourchette('valeur_pk_lisier') }} |

Dans une tonne de fumier, le phosphore vaut {{ v('valeur_p_fumier') }} et le potassium {{ v('valeur_k_fumier') }} (calculé). Le lisier est compté à une tonne par m³ (hypothèse). Un apport de {{ v('fumier_dose_ha', 0) }} de fumier au printemps avant un maïs fournit 133 kg de P2O5 et 311 kg de K2O[^protecteau], soit {{ v('valeur_pk_fumier_ha', 0) }} d'engrais P et K évités (calculé). Ces valeurs ne comptent ni l'azote, ni la matière organique.

La valeur reste du même ordre dans les trois scénarios : la potasse n'a presque pas bougé avec la crise, et seule la part du phosphore varie. Recycler ses effluents est donc rentable même si les prix redescendent.

Les teneurs varient beaucoup d'une ferme à l'autre. Dans sept tas de fumier frais de bovins suivis dans des fermes wallonnes du réseau Terraé, le fumier contenait en moyenne 10,8 kg de K2O par tonne (7,6 à 14,8) et 2,6 kg de P2O5 (1,8 à 3,5) : plus de potasse et moins de phosphore que les valeurs moyennes[^fm-bache]. Une analyse d'effluent périodique vaut donc la peine.

**Ne pas perdre la potasse au stockage.** La pluie lessive les tas de fumier laissés au champ, ce que le PGDA autorise en Wallonie jusqu'à 9 mois. Dans l'essai de Fourrages Mieux, une bâche respirante en polypropylène a réduit les pertes de potassium de 23 % à 6 % en moyenne. Le bâchage coûte environ 1,21 € par tonne de fumier, main-d'œuvre comprise. Avec un chlorure de potassium à 420 €/t (juillet 2025), il devient rentable au-delà de 145 jours de stockage au champ, et dès 70 jours si la potasse perdue est remplacée par du sulfate de potassium (agriculture biologique)[^fm-bache]. Le premier conseil reste d'épandre tôt ou de stocker sous fumière couverte[^fm-bache]. La bâche est elle-même en plastique fossile (voir la fiche [plastiques agricoles](../materiaux/plastiques-agricoles.md)) ; selon l'essai, ses émissions restent 6 à 25 fois plus faibles que celles évitées sur la potasse[^fm-bache].

**Les limites.**

- Les effluents ne créent pas de phosphore : ils recyclent celui des aliments. Quand le troupeau mange des concentrés importés, une partie du phosphore épandu est elle aussi importée (voir la fiche [concentrés importés](../elevage/concentres-importes.md)). Le recyclage est vraiment circulaire quand l'alimentation vient de la ferme ou du territoire.
- Le PGDA plafonne l'azote organique épandu : 230 kg d'azote par hectare dans la norme utilisée par Protect'eau, soit au plus 39 t/ha de fumier ou 52 t/ha de lisier de bovins[^protecteau]. Avec les fientes de volailles, très riches en P et en K, on risque de surdoser ces éléments[^protecteau].
- Une ferme sans élevage dépend d'échanges avec les voisins (paille contre fumier) et du coût du transport, qui n'est pas compté ici.
- Sur les sols déjà riches, ajouter du phosphore organique n'apporte rien et augmente les pertes vers les eaux de surface : les flux de phosphore des sols agricoles wallons vers les eaux atteignaient 2 100 t par an sur 2021-2025[^eew-sols-p].

### 2. Compost et digestat (vague 2)

Le **compostage** du fumier réduit sa masse et concentre les éléments. Selon Protect'eau, un fumier composté contient en moyenne {{ v('fumier_composte_p2o5', 1) }} de P2O5 et {{ v('fumier_composte_k2o', 1) }} de K2O[^protecteau], soit {{ v('valeur_pk_compost') }} de P et de K (calculé). On transporte et on épand moins de tonnes pour la même quantité d'éléments. Le compostage coûte du temps et du gasoil (retournements) : ce coût n'a pas été chiffré ici. L'essai de Fourrages Mieux suggère qu'un tas bâché composte mieux, ce qui pourrait remplacer une partie des retournements (piste à confirmer)[^fm-bache].

Le **digestat** de biométhanisation garde le phosphore et le potassium des matières entrées dans le digesteur. Moyennes wallonnes de Requasud pour un digestat complet : {{ v('digestat_p2o5', 2) }} de P2O5 et {{ v('digestat_k2o', 1) }} de K2O, avec 6,8 % de matière sèche. La phase solide est plus riche (2,0 kg de P2O5 et 4,8 kg de K2O par tonne)[^fiwap]. Le P et le K d'une tonne de digestat complet valent {{ v('valeur_pk_digestat') }} (calculé). Plus de 50 unités wallonnes produisaient environ 600 000 t de digestat par an (chiffre Valbiom de 2020)[^fiwap].

Conditions :

- du matériel d'épandage et de compostage, en propre ou en CUMA ;
- pour le digestat, une unité de biométhanisation proche ;
- des analyses du produit, car les teneurs varient selon les intrants.

Comme pour le fumier, ces produits recyclent un phosphore déjà présent dans le territoire : ils ne suppriment pas l'import s'il entre par les aliments ou par les déchets de l'industrie agroalimentaire.

### 3. Cendres de bois (vague 2)

Les cendres d'une chaudière à bois contiennent du calcium, du potassium, du magnésium et du phosphore. Leur pH très élevé (12 à 13) en fait aussi un amendement basique, qui remonte le pH du sol[^solagro]. Une étude française a mesuré, pour des cendres de plaquettes forestières, environ {{ v('cendres_bois_k2o', 1) }} de potassium et {{ v('cendres_bois_p2o5', 1) }} de phosphore, et un tiers de calcium (moyenne de 9 analyses)[^ademe-cendres]. Une tonne de cendres remplacerait ainsi environ {{ v('kcl_evite_t_cendres', 0) }} de chlorure de potassium (calculé). Son P et son K valent {{ v('valeur_pk_cendres', 0) }} (calculé, valeurs françaises de 2005 à confirmer).

C'est intéressant pour une ferme qui a déjà sa chaudière à plaquettes (voir la fiche [chauffage au mazout](../energie/chauffage-mazout.md)), surtout si le bois vient de ses haies : le potassium que les arbres ont puisé retourne au champ.

Limites :

- les quantités sont faibles, à la mesure de la chaudière : un appoint de potasse et de chaux, pas un remplacement de l'engrais à l'échelle de la ferme ;
- la composition varie avec l'essence, le sol où l'arbre a poussé et le combustible. Des cendres de bois traité, de palettes ou de déchets de bois contiennent beaucoup plus de métaux lourds (plomb, chrome, zinc, cuivre) que celles de plaquettes forestières[^ademe-cendres] ;
- la valorisation agricole se décide au cas par cas, après analyse[^solagro] ;
- le cadre légal wallon (déchet ou produit, autorisation d'épandage) reste à vérifier (voir « À vérifier »).

### 4. Recyclage urbain : boues, struvite, cendres de boues (vague 3)

Le phosphore que nous mangeons finit dans les eaux usées. En Flandre, Aquafin reçoit dans ses stations environ 4 000 t de phosphore par an, dont 85 % se retrouvent dans les boues d'épuration. Ces boues y sont incinérées (en cimenterie, avec des déchets ménagers ou seules)[^aquafin].

Trois voies existent pour rendre ce phosphore à l'agriculture :

- **Épandre les boues** : la Wallonie l'encadre par un arrêté de 1995. Il impose notamment un délai de 6 semaines avant pâturage ou récolte d'un fourrage, et l'interdit sur les cultures maraîchères et fruitières consommées crues pendant les dix mois qui précèdent la récolte[^agw-boues]. Les boues apportent aussi des contaminants : la Belgique fixe des teneurs maximales en métaux lourds pour les boues valorisées en agriculture[^eew-engrais].
- **Précipiter de la struvite** (phosphate de magnésium et d'ammonium) dans les stations qui digèrent leurs boues. À Louvain, Aquafin produit environ 500 kg de struvite par semaine. Cette struvite respecte les normes flamandes de sortie du statut de déchet, et a donné en pot le même rendement que le superphosphate triple. Mais elle ne récupère que 5 à 15 % du phosphore des boues, et sa valeur de marché était estimée à 250 €/t en 2019[^aquafin].
- **Extraire le phosphore des boues ou de leurs cendres** : à partir des cendres de boues incinérées, les démonstrateurs du projet européen Phos4You ont récupéré plus de 80 % du phosphore. L'Université de Liège y a testé un procédé d'extraction directement à partir des boues (PULSE, 60 à 70 % du phosphore récupéré, à l'échelle de 500 équivalents-habitants)[^phos4you].

Le règlement européen sur les fertilisants (UE) 2019/1009, appliqué depuis 2022, encourage les engrais issus de matières recyclées et permet de les vendre librement dans l'Union s'ils portent le marquage « fertilisant UE ». En Wallonie, cette libre circulation fait craindre une concurrence avec les effluents locaux, dans le cadre du PGDA[^eew-engrais].

Pourquoi vague 3 : ces filières dépendent des stations d'épuration et des incinérateurs, pas de l'agriculteur. Elles ne sont pas encore rentables pour elles-mêmes. Dans le procédé EuPhoRe de Phos4You, c'est la chaleur revendue qui fait la recette, pas le phosphore, vendu 0,05 €/kg de P2O5[^phos4you]. L'agriculteur peut s'y préparer en suivant les produits recyclés proposés par les négociants et en demandant leur teneur en contaminants.

## Ce qui ferme la boucle

- **Le stock du sol** : dans les terres riches, l'analyse de sol permet de vivre quelques années sur le phosphore accumulé avant 2000.
- **Les effluents de la ferme et des voisins**, stockés à l'abri, analysés et épandus au bon moment, rendent au champ le P et le K des fourrages.
- **Une alimentation du troupeau produite sur place** évite d'importer du phosphore par les concentrés.
- **Les haies et la chaudière à bois** rendent un peu de potasse et de chaux par les cendres.
- **Le territoire** : digestat des unités de biométhanisation, compost, puis demain le phosphore des stations d'épuration de la ville voisine.

## À vérifier

- **Prix belges** : les prix du TSP et du chlorure de potassium utilisés ici sont des prix français au stade distributeur (La Dépêche Le petit meunier). Les seuls repères belges sont une page d'un négociant en ligne non datée (départ Gand) et le prix de 420 €/t de juillet 2025 cité par Fourrages Mieux[^agryco] [^fm-bache]. À remplacer par une cotation belge datée ou une facture.
- **Cotations Terre-net** : le 26 novembre 2026, Terre-net affichait le TSP à 567,25 €/t et le binaire PK à 517,25 €/t[^terrenet], soit les niveaux de novembre 2025 (TSP 565-567 €/t, PK 517 €/t)[^depeche-janv], bien en dessous des 675-680 €/t de septembre 2026 pour le TSP. Ces cotations semblent ne pas avoir été mises à jour et n'ont pas été retenues.
- **Prix de novembre 2026** : le dernier tableau de prix complet lu porte sur septembre 2026 ; pour octobre, l'article ne donne que l'évolution (phosphatés stables, potasse − 5 €/t)[^depeche-nov].
- **Énergie fossile de l'extraction et de la fabrication** : aucune donnée lue sur l'énergie (en MJ ou en litres de gasoil) par kg de P2O5 ou de K2O, ni sur la part du soufre qui vient de la désulfuration du pétrole et du gaz.
- **Origine des engrais vendus en Belgique** : parts du Maroc, de la Russie, du Canada et de l'Allemagne dans les importations belges de phosphate et de potasse (Statbel).
- **Teneurs du digestat** : la fiche FIWAP donne 886 mg de P2O5 par kg dans son tableau de composition, mais 2,35 kg/t dans son tableau de valorisation. Les valeurs retenues ici sont celles du tableau de composition.
- **Teneurs des cendres de bois** : la source (ADEME, 2005) est française et ancienne ; son tableau parle de « phosphore total » et de « potassium total », ses graphiques de P2O5 et de K2O. Chercher des analyses wallonnes de cendres de chaudières à plaquettes, et la quantité de cendres produite par MAP brûlé.
- **Statut légal des cendres de bois en Wallonie** : déchet soumis à autorisation, sous-produit ou matière fertilisante ? Conditions pour les épandre sur ses propres terres. À demander au SPW (Département du Sol et des Déchets).
- **PGDA** : vérifier la norme d'azote organique en vigueur (PGDA IV) pour les prairies et les cultures, et les règles de stockage au champ ; la fiche Protect'eau date de 2018 (PGDA III).
- **Boues d'épuration** : vérifier que l'arrêté wallon du 12 janvier 1995 est toujours la règle en vigueur et la part des boues wallonnes épandues en agriculture.
- **Recyclage du phosphore en Wallonie** : projets de struvite ou d'incinération des boues avec récupération du phosphore (SPGE, intercommunales) ; état actuel de l'installation d'Aquafin à Louvain (source de 2019).
- **Règlement européen** : catégories de matières recyclées admises (sels de phosphate précipités, cendres) et produits à base de struvite disponibles en Belgique ; EUR-Lex n'a pas pu être lu.

## Sources

[^eew-engrais]: « Consommation d'engrais en agriculture », État de l'environnement wallon, SPW, mise à jour du 5 décembre 2024. https://etat.environnement.wallonie.be/contents/indicatorsheets/AGRI%205.eewGeneratePdf.do
[^eew-sols-p]: « Bilan du phosphore des sols agricoles et flux de phosphore vers les eaux de surface », État de l'environnement wallon, SPW (modèle EPICgrid et base de données Requasud), mise à jour du 5 novembre 2026. https://etat.environnement.wallonie.be/contents/indicatorsheets/SOLS%206.eewGeneratePdf.do
[^requasud-2023]: G. Colinet et C. Mariage (ULiège Gembloux Agro-Bio Tech), « Statut de fertilité chimique des sols agricoles en Wallonie d'après la BD de REQUASUD », journée d'étude sol, SPW Agriculture, 16 novembre 2023. https://agriculture.wallonie.be/files/accueil/Recherche%20et%20d%c3%a9veloppement/agenda/Journ%c3%a9e%20d'%c3%a9tude%20sol%20la%20reid%20huy%20nov%202023/Statut%20de%20fertilit%c3%a9%20chimique%20des%20sols%20agricoles%20en%20Wallonie-%20REQUASUD.pdf
[^depeche-nov]: K. Floquet, « Marché des engrais : les prix de l'azote continuent de progresser, ceux du phosphore se maintiennent et celui de la potasse s'érode », La Dépêche Le petit meunier (Réussir), 6 novembre 2026 (prix au stade distributeur, France). https://www.reussir.fr/articles/marche-des-engrais-les-prix-de-lazote-continuent-de-progresser-ceux-du-phosphore-se
[^depeche-mars]: D. Jouen, « Marché des engrais : la tension accrue au Moyen-Orient soutient les engrais azotés », La Dépêche Le petit meunier (Réussir), 9 mars 2026 (prix de février 2026, France). https://www.reussir.fr/articles/marche-des-engrais-la-tension-accrue-au-moyen-orient-soutient-les-engrais-azotes
[^depeche-janv]: « Marché des engrais : incertitudes, tensions et ajustements face au MACF », La Dépêche Le petit meunier (Réussir), 12 janvier 2026 (prix de novembre et décembre 2025, France). https://www.reussir.fr/ladepeche/marche-des-engrais-incertitudes-tensions-et-ajustements-face-au-macf
[^agryco]: « Les tendances des marchés » (page engrais), Agryco Belgique (site commercial), non datée, consultée le 26 novembre 2026. https://www.agryco.be/fr_BE/engrais/pc975
[^escp]: A. Kateb, « Géopolitique et géoéconomie : le secteur des engrais au miroir de la crise d'Ormuz », ESCP Geopolitics Institute, Policy Paper IP n° 2026-12, 2026 (document de travail non relu par des pairs). https://escp.eu/sites/default/files/inline-images/Instituts/ESCP_Geopolitics/Policy_Paper_Kateb_2026_ESCP%20Geopolitics%20Institute.pdf
[^protecteau]: « Valeur fertilisante des engrais de ferme », fiche technique Protect'eau, décembre 2018 (sources PGDA et Requasud). https://www.protecteau.be/sites/default/files/2022-07/FT_valeur_fertilisante_engrais.pdf
[^fm-bache]: A. Stifkens et S. Leriche, « Stockage des fumiers au champ : comment réduire les pertes de potassium d'un facteur 3 à 4. Résultats d'un essai mené dans les fermes du Réseau Terraé (2022-2025) », rapport complet, Fourrages Mieux, 2025. https://www.fourragesmieux.be/Documents_telechargeables/2026_Rapport%20complet_Couverture%20des%20tas%20de%20fumier.pdf
[^fiwap]: M. De Toffoli (UCLouvain, Protect'eau), « Digestat de biométhanisation en culture de pomme de terre », FIWAP-Info n° 177, janvier-mars 2023 (teneurs moyennes Requasud 2021). https://fiwap.be/wp-content/uploads/2023/03/2303DigestaBiometPdt.pdf
[^solagro]: « Gestion et valorisation des cendres de chaufferies bois », fiche de référence Solagro, étude pour l'ADEME, 2005-2006 (France). https://solagro.org/fiche-pdf-reference-80
[^ademe-cendres]: C. Couturier (Solagro) et T. Brasset (Aquasol), « Gestion et valorisation des cendres de chaufferies bois : analyses moyennes des cendres », ADEME, décembre 2005 (France). https://www.bioenergie-promotion.fr/wp-content/uploads/2012/03/2-analyses_moyennes_cendres.pdf
[^aquafin]: B. Saerens, S. Geerts et M. Weemaes (Aquafin), « Phosphorus recovery as struvite from digested sludge: experience from the full scale », 5th European Conference on Sludge Management, 8 octobre 2019. https://vb.nweurope.eu/media/8137/bsaerens.pdf
[^phos4you]: Partenariat Phos4You (Interreg Europe du Nord-Ouest), « Technical report on processes to recover P from wastewater », septembre 2021. https://orbi.uliege.be/bitstream/2268/266587/1/Phos4You_Technical_report_September_2021.pdf
[^terrenet]: Cotations « Super Phosphate Triple » (port départ) et « PK » (silo rendu), Terre-net, consultées le 26 novembre 2026 (France). https://www.terre-net.fr/marche-agricole/super-phosphate-triple/engrais et https://www.terre-net.fr/marche-agricole/pk/engrais
[^agw-boues]: Arrêté du Gouvernement wallon du 12 janvier 1995 portant réglementation de l'utilisation sur ou dans les sols des boues d'épuration ou de boues issues de centres de traitement de gadoues de fosses septiques, article 9, Wallex, consulté le 26 novembre 2026. https://wallex.wallonie.be/contents/acts/11/11130/1.html
