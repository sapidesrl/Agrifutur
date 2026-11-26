---
id: herbicides
titre: Herbicides de synthèse
domaine: protection des cultures
dependance_fossile: pétrochimie
alternatives: [Désherbage mécanique, robot solaire de binage]
vague_meilleure_alternative: 1
statut: relu
maj: 2026-11-26
---

# Herbicides de synthèse

## En bref

Les herbicides de synthèse sont des molécules de la chimie organique, pulvérisées pour détruire les adventices avant ou après la levée de la culture. Le fossile entre surtout par leur fabrication : celle du glyphosate demande environ {{ v('glyphosate_energie_mj_kg') }}[^ppdb], soit l'équivalent de {{ v('glyphosate_eq_gasoil_l_ha', 0) }} de gasoil pour un traitement (calculé). En Wallonie, les herbicides coûtaient en 2023 de 63 €/ha en orge à plus de 280 €/ha en chicorée[^base1].

La meilleure alternative est le désherbage mécanique (herse étrille, houe rotative, bineuse), seul ou combiné à un traitement localisé : il est rentable aujourd'hui dans les cultures où les herbicides coûtent cher, sur sols peu caillouteux (vague 1), mais il déplace une partie de la dépendance vers le gasoil. Le robot solaire de binage supprime presque tout le fossile au champ, mais ne se rentabilise que là où il remplace du désherbage manuel, en bio ou en légumes (vague 2).

## Comment ça marche aujourd'hui

On distingue trois usages :

- **en prélevée** : un herbicide racinaire épandu sur le sol juste après le semis ;
- **en post-levée** : un ou plusieurs traitements foliaires sélectifs pendant les premières semaines de la culture ;
- **en interculture** : un herbicide total, en général le glyphosate, détruit les repousses, les vivaces ou un couvert avant le semis suivant. En France, 98 % des traitements au glyphosate des grandes cultures se faisaient en interculture (enquête de 2017), à une dose moyenne de 824,5 g de matière active par hectare traité[^inrae].

Le pulvérisateur traîné de 28 à 30 m travaille vite, environ 8,5 ha/h dans les hypothèses du CRA-W, et sert aussi aux engrais liquides et aux fongicides[^base1]. C'est ce qui rend le chimique difficile à battre sur le coût de passage.

Ce que coûtent les herbicides en Wallonie (comptabilités des fermes du réseau européen, moyennes pondérées par la surface, en €/ha)[^base1] :

| Culture | 2020 | 2021 | 2022 | 2023 |
|---|---|---|---|---|
| Orge | 64 | 61 | 61 | 63 |
| Froment d'hiver | 74 | 75 | 84 | 82 |
| Maïs | 88 | 86 | 95 | 109 |
| Pomme de terre | 137 | 146 | 155 | 167 |
| Betterave sucrière | 258 | 234 | 258 | 263 |
| Chicorée | 296 | 299 | 281 | 282 |

L'écart entre fermes est grand : l'écart-type dépasse souvent 40 €/ha[^base1]. Les cultures de printemps à démarrage lent (betterave, chicorée) reçoivent le plus de produits.

**Le cadre réglementaire en 2026**

- Le glyphosate est approuvé dans l'Union européenne jusqu'au 15 décembre 2033, sous conditions. Le renouvellement au-delà doit être demandé avant le 15 décembre 2030[^ec].
- En Wallonie, l'arrêté du 30 mars 2017 interdit tout produit à base de glyphosate. Il prévoit une dérogation pour les utilisateurs professionnels titulaires d'une phytolicence P1, P2 ou P3, dans le cadre d'une activité agricole[^agw2017]. L'agriculteur peut donc encore l'employer.
- Depuis le 1er janvier 2026, toute pulvérisation en Belgique doit réduire la dérive d'au moins 75 % (buses ou techniques reconnues), sauf en serre et en post-récolte. En Wallonie s'ajoutent l'interdiction de commencer à pulvériser par vent de 20 km/h ou plus, une zone tampon de 50 m autour des écoles et crèches pendant les heures d'ouverture, des zones tampons minimales (6 m le long des eaux de surface, 1 m, cours d'eau sans eau permanente) et les zones tampons de l'étiquette ; on respecte toujours la plus large[^protecteau].
- Le programme wallon de réduction des pesticides en cours (PWRP III) couvre 2023-2027[^base1]. Les arrêtés qui délimitent les zones de protection des captages peuvent imposer un diagnostic des contaminations par les nitrates et les pesticides sur toutes les parcelles agricoles de la zone, comme celui du 17 mars 2026 pour la galerie de l'Ornoy à Mont-Saint-Guibert[^captage]. En avril 2026, la ministre de l'Agriculture a annoncé que les États généraux de la protection des cultures alimenteraient le futur plan wallon de réduction des pesticides[^lavenir].

## Où entrent le pétrole et le gaz

- **Matières actives** : ce sont des molécules de synthèse. Le glyphosate, par exemple, est fabriqué à partir de glycine (ou d'acide iminodiacétique), de formaldéhyde et d'acide phosphoreux[^ppdb].
- **Énergie de fabrication** : environ {{ v('glyphosate_energie_mj_kg') }} de glyphosate, selon une estimation de 2009 reprise par la base de données des pesticides de l'université du Hertfordshire[^ppdb]. Aucun fabricant ne publie de données, et les estimations varient beaucoup[^ppdb]. Avec la dose moyenne d'un traitement (dose française citée plus haut), cela fait {{ v('glyphosate_energie_kwh_ha', 0) }} traité, soit l'énergie de {{ v('glyphosate_eq_gasoil_l_ha', 0) }} de gasoil (calculé). Cette énergie compte toutes les sources (gaz, pétrole, électricité) ; la part fossile n'est pas connue.
- **Formulation et emballage** : solvants, adjuvants et bidons en plastique (non chiffrés ici).
- **Pulvérisation** : environ {{ v('gasoil_passage_pulverisateur', 2) }} de gasoil par passage d'un pulvérisateur traîné de 28 m, d'après le référentiel français des coûts des opérations culturales[^coc].
- **Transport et distribution** des produits.

## Les alternatives

### 1. Désherbage mécanique (vague 1)

**Principe.** Des outils tirés par le tracteur arrachent, recouvrent ou coupent les jeunes adventices[^base2] :

- la **herse étrille** (3 à 32 m de large, 4 à 10 km/h) fait vibrer des dents souples qui déracinent les plantules, en plein, y compris sur le rang ;
- la **houe rotative** (6 à 18 m, 15 à 20 km/h) arrache les plantules avec des roues à cuillères et casse la croûte de battance ;
- la **bineuse** (3 à 18 m, 4 à 12 km/h) scalpe l'inter-rang et peut butter le rang ; elle travaille des écartements de 15 à 75 cm, avec un guidage par caméra ou GPS pour gagner en précision.

Ces outils sont surtout efficaces sur des adventices très jeunes (jusqu'à deux feuilles) et sur les dicotylédones ; ils sont moins efficaces sur les graminées et peu efficaces sur les vivaces. Un seul passage ne suffit pas : il faut une stratégie de plusieurs interventions[^base2]. Sur le rang, l'efficacité reste plus faible que dans l'inter-rang[^base2].

**Où ça marche en Wallonie.** Le CRA-W estime que 303 823 ha (42 % de la surface agricole) conviennent au désherbage physique, surtout dans les régions limoneuse et sablo-limoneuse, peu caillouteuses et peu pentues[^base1]. Le climat est le premier frein : certaines années, le nombre de jours favorables est nul, quelle que soit la région[^base1]. Il faut un sol ressuyé et pas de pluie dans les deux jours qui suivent, sinon les adventices se repiquent[^ca60]. En maïs, dans le nord de la France, on compte en moyenne 2 jours favorables pour la houe ou la herse avant la levée, 3,5 jours au stade 2 à 6 feuilles et 7 à 9 jours pour la bineuse (prix et données français)[^ca60].

**Coût d'un passage** (outil CRA-W Mecacost, matériel, tracteur et main-d'œuvre à {{ v('main_oeuvre_eur_h', 0) }}, hors produit)[^base1] :

| Passage | Coût | Gasoil par passage (référentiel français)[^coc] |
|---|---|---|
| Pulvérisateur traîné 28-30 m | {{ v('cout_passage_pulverisateur', 0) }} | {{ v('gasoil_passage_pulverisateur', 2) }} |
| Herse étrille 12 m | {{ v('cout_passage_herse_etrille', 0) }} | {{ v('gasoil_passage_herse_etrille') }} |
| Houe rotative 6 m | {{ v('cout_passage_houe_rotative', 0) }} | {{ v('gasoil_passage_houe_rotative') }} |
| Bineuse 6 m à caméra | {{ v('cout_passage_bineuse', 0) }} | {{ v('gasoil_passage_bineuse') }} (bineuse 12 rangs) |

Les coûts CRA-W supposent un outil utilisé sur 100 ha par an et un pulvérisateur sur 1 000 ha. La bineuse coûte cher surtout parce qu'elle avance lentement (2 ha/h contre 8,5 ha/h pour le pulvérisateur) : la traction et la main-d'œuvre passent de 7 € par passage de pulvérisateur à 30 € par binage[^base1]. Une bineuse 12 rangs sans caméra, partagée sur plus d'hectares, revient à 21 €/ha dans le référentiel des Hauts-de-France (prix français, 2022)[^ca60]. Le partage en CUMA ou le recours à un entrepreneur abaisse donc fortement le coût du passage.

**Rentabilité.** Le passage mécanique coûte plus cher que le passage de pulvérisateur, mais il ne demande pas de produit. Le bilan dépend donc du prix des herbicides de la culture :

- **Maïs** (calculé avec les références wallonnes) : le chimique, soit les herbicides de 2023 et {{ v('passages_pulverisateur_mais', 0) }} de pulvérisateur, revient à {{ v('mais_chimique_eur_ha') }} ; un programme tout mécanique d'une herse étrille et de {{ v('passages_bineuse_mais', 0) }} de bineuse à caméra (hypothèse) revient à {{ v('mais_mecanique_eur_ha') }}. Les deux sont à égalité à quelques euros près ; avec une bineuse moins chère ou mieux utilisée, le mécanique devient le moins cher. Dans le nord de la France, une stratégie de binage demande 2 à 3 passages et une stratégie herse étrille ou houe 3 à 4 passages, contre 2 passages en chimique[^ca60-mais].
- **Betterave** : dans une étude wallonne, les herbicides représentaient 79 % du coût total du désherbage, ce qui rendait le désherbage chimique plus cher que le mécanique sur la saison[^base1]. Les herbicides y coûtent {{ v('herbicides_betterave_eur_ha') }} en moyenne (2023)[^base1].
- **Colza** : traitement localisé sur le rang au semis, puis un binage, pour 114 €/ha, contre 144 €/ha pour un désherbage chimique en plein (Terres Inovia, prix français, herbicide à 100 €/ha). L'efficacité est équivalente, à condition de semer au monograine avec un écartement d'au moins 45 cm[^inovia].
- **Céréales** : les herbicides coûtent moins (63 à 82 €/ha en 2023)[^base1] ; le mécanique y est surtout intéressant contre la résistance des graminées ou en bio.

Le désherbage **mixte** (mécanique dans l'inter-rang, traitement localisé ou réduit sur le rang) est souvent le plus sûr : en maïs, il divise par deux environ l'indice de fréquence de traitement (0,7 à 1,1 contre 1,4 à 2,3)[^ca60-mais], et en colza l'herbisemis réduit l'IFT herbicide des deux tiers[^inovia]. Il demande 15 à 20 minutes de travail en plus par hectare en féverole[^ca60].

**Ce que ça déplace.** Le désherbage mécanique remplace un produit de synthèse par du gasoil et du temps de tracteur. En maïs, l'itinéraire ci-dessus consomme {{ v('mais_meca_gasoil_supp_l_ha', 1) }} de gasoil de plus que le chimique, soit {{ v('mais_meca_gasoil_supp_eur_ha') }} au prix actuel ({{ fourchette('mais_meca_gasoil_supp_eur_ha') }} selon les scénarios, calculé). C'est peu face au prix des herbicides, et la conclusion ne change pas d'un scénario à l'autre. En énergie, c'est du même ordre que la fabrication d'un seul traitement au glyphosate ({{ v('glyphosate_eq_gasoil_l_ha', 0) }} équivalent gasoil, voir plus haut). La dépendance passe de l'usine au réservoir du tracteur : elle ne disparaît que si le tracteur roule à l'huile, au biométhane ou à l'électricité (voir la fiche [Tracteur diesel](../traction/tracteur-diesel.md)).

**Le cas du semis direct.** Sans travail du sol, le glyphosate détruit les couverts et les repousses avant le semis. S'en passer est la limite la plus dure :

- le rouleau type faca détruit bien les couverts hauts et dressés (phacélie, tournesol, sarrasin), la moutarde, la vesce ou la féverole après un gel marqué, mais il est inefficace sur les graminées (seigle, ray-grass). Les hivers ont de moins en moins de jours de gel consécutifs. Des rouleaux hacheurs plus agressifs marchent sans gel, au prix d'un travail plus proche du broyage[^faca] ;
- un couvert dense et gélif (légumineuses, avoine rude) étouffe les adventices et se roule plus facilement ; avant une culture d'hiver, un agriculteur normand en semis direct ne voyait pas d'autre solution qu'un travail du sol intensif, risqué sur ses limons battants sensibles à l'érosion[^chedru] ;
- en France, passer une parcelle de semis direct au labour fréquent sans glyphosate coûtait environ 80 €/ha/an de plus (prix de 2020), avec {{ v('gasoil_supp_sd_sans_glyphosate', 1) }} de gasoil et 1,43 h/ha de travail en plus[^inrae]. Au prix actuel, ce gasoil vaut à lui seul {{ v('sd_sans_glyphosate_gasoil_eur_ha') }} (calculé). Le gasoil ajouté pèse alors près de trois fois l'énergie de fabrication d'un traitement au glyphosate : remplacer le glyphosate par le labour augmente le fossile au lieu de le réduire.

Le semis direct sans glyphosate reste donc un chantier ouvert : en pratique, on le garde à dose réduite et occasionnelle contre les graminées que le rouleau ne détruit pas.

**Aides.** La liste des investissements admissibles à l'aide wallonne (AII, janvier 2026) comprend la herse étrille, la houe rotative, les bineuses à guidage par caméra ou par ultrasons et les robots autonomes[^aii].

**Vague 1** : rentable aujourd'hui en betterave, chicorée et colza sur les sols limoneux peu caillouteux, surtout en désherbage mixte et avec du matériel partagé. En maïs, le coût est à égalité avec le chimique : le matériel partagé ou le désherbage mixte fait pencher la balance. Moins intéressant en céréales, sur sols lourds ou caillouteux, et en semis direct.

### 2. Robot solaire de binage (vague 2)

**Principe.** Le FarmDroid FD20 sème et bine seul. Il enregistre par GPS RTK la position de chaque graine au semis, puis bine l'inter-rang et entre les plants sans caméra, puisqu'il sait où sont les graines. Des panneaux solaires et des batteries le font tourner jusqu'à 24 heures par jour, sur environ 6,5 ha par jour selon le constructeur[^fao]. Il pèse environ 800 kg, mesure 3 m de large et avance à environ 700 m/h ; sa légèreté lui permet de travailler sans chauffeur et limite le tassement[^pc2020]. Plus de 500 robots étaient en service dans plus de 23 pays en septembre 2025[^fao].

**Coût.** De 75 000 à 97 000 € HTVA, station RTK en plus[^fao] ; « autour de 100 000 € » en France en 2026[^tn2026]. Le robot ne peut pas travailler plus d'une vingtaine d'hectares par an[^tn2026]. Sur {{ v('farmdroid_duree', 0) }} (hypothèse) et {{ v('farmdroid_surface', 0) }}, l'amortissement seul atteint {{ v('farmdroid_amort_eur_ha') }}, soit le prix de {{ v('farmdroid_eq_heures_ha', 0) }} de main-d'œuvre à {{ v('main_oeuvre_eur_h', 0) }} (calculé, sans frais financiers ni entretien). C'est près du double des herbicides d'une betterave conventionnelle ({{ v('herbicides_betterave_eur_ha') }}) : face au chimique, le robot n'est pas rentable.

**Où il se rentabilise : à la place du désherbage manuel.** En betterave bio, le désherbage manuel prend 150 à 200 heures par hectare chez un agriculteur bio de Poperinge[^vrt]. Dans la Marne, une exploitation bio qui avait arrêté la betterave pour cette raison (environ 200 h/ha la première année) est descendue à 20 à 30 h/ha de finitions manuelles avec le robot ; elle estime son coût à l'équivalent de 50 h/ha de désherbage manuel, sur 5 ans et 20 ha. Elle utilise aussi le robot en colza, semé fin août, ce qui étale l'investissement sur deux cultures[^tn2022].

**Limites** (témoignages français de 2026)[^tn2026] :

- 4 ha par jour au maximum en pratique, en tournant jour et nuit ;
- une surveillance deux à trois fois par jour en mars-avril : une pierre ou une motte coince l'outil, les alertes arrivent la nuit ;
- des chénopodes trop développés ne sont plus arrachés ;
- « en conventionnel, cela ne passerait pas » ; un producteur avec trois robots juge qu'ils ne seraient pas rentables sur la seule betterave sucrière ;
- les sols argileux lourds et caillouteux limitent les créneaux d'intervention.

**Autres robots.** Des robots à caméra, à bras articulés ou à laser apparaissent. Les désherbeurs laser ne traitent que 0,5 à 1 ha/h[^base2]. En Flandre, Inagro teste à grande échelle des robots du commerce ; le prix d'achat reste le principal frein en agriculture conventionnelle, et Inagro travaille sur un modèle de simulation de la surface nécessaire pour rentabiliser l'achat[^vrt]. Certains robots pulvérisent un herbicide seulement sur l'adventice repérée : un FarmDroid équipé d'une caméra et d'une pulvérisation localisée a réduit de 90 % l'usage d'herbicide chez un betteravier néerlandais[^ff2023]. La dose baisse, mais la dépendance à la chimie reste.

**Aides.** L'AII wallonne retient pour un robot autonome guidé par GPS RTK un coût raisonnable maximal de 30 050 € (débit jusqu'à 2,5 ha/jour) ou de 150 000 € (au-delà)[^aii]. Le taux d'aide applicable n'a pas été vérifié.

**Vague 2** : rentable sous conditions, en bio ou en légumes, quand le robot remplace des dizaines d'heures de désherbage manuel par hectare, sur une vingtaine d'hectares de cultures semées (betterave, colza, chicorée, oignon), et sur des sols peu caillouteux.

## Ce qui ferme la boucle

- **L'agronomie d'abord** : une rotation diversifiée avec des cultures de printemps et d'hiver casse les cycles des adventices. Un faux semis fin mars ou début avril peut réduire de 60 % le nombre d'adventices d'un maïs[^ca60-mais].
- **Les couverts** : un couvert dense et gélif occupe le sol, puis se roule au lieu d'être désherbé.
- **Le soleil** : le robot de binage tourne à l'énergie solaire, sans carburant.
- **Le carburant de la ferme** : l'huile de colza ou le biométhane peuvent alimenter les passages mécaniques (fiche [Tracteur diesel](../traction/tracteur-diesel.md)).
- **Le collectif** : le matériel coûteux et propre à une culture (bineuse à caméra, robot) se rentabilise mieux en CUMA ou chez un entrepreneur, comme le recommande le CRA-W[^base1].

## À vérifier

- Prix des herbicides en 2026 : les coûts wallons s'arrêtent en 2023 (avant la crise). Pas de prix de février 2026 ni de novembre 2026, donc pas de scénarios de prix pour les herbicides.
- Coûts Mecacost du CRA-W : prix du gasoil retenu dans la simulation, et mise à jour aux prix de 2026.
- Consommation de gasoil des passages mécaniques mesurée en Belgique (ici, référentiel français de 2023).
- Tarifs belges d'entrepreneurs et de CUMA pour le binage et le hersage (non trouvés).
- Énergie de fabrication des herbicides autres que le glyphosate, et part du gaz et du pétrole dans cette énergie. Rapport Audsley et al. (2009, Cranfield) non lu directement : chiffre repris de la base PPDB.
- Arrêté wallon du 30 mars 2017 sur le glyphosate : confirmer qu'il est toujours en vigueur (texte affiché sur Wallex sans mention d'annulation ; un recours au Conseil d'État a été évoqué dans la presse, non vérifié).
- Contenu des autres arrêtés de 2026 sur les zones de captage (certains limiteraient l'emploi de pesticides en zone rapprochée : extraits non lus).
- Taux de l'aide AII pour la herse étrille, la bineuse et les robots.
- Résultats belges du FarmDroid (aucun essai wallon ou flamand publié trouvé) et résultats du modèle de simulation d'Inagro.
- Destruction des couverts sans glyphosate en semis direct en Wallonie : résultats d'essais belges (Greenotec, CRA-W) non trouvés.
- Nombre de jours favorables au désherbage mécanique par région agricole wallonne (figures de l'article du CRA-W non reprises ici).

## Sources

[^base1]: Rabier F., Limbourg Q., Miserque O., Huyghebaert B. (CRA-W), « Physical weed control: a review in Belgian conditions. Part 1: Specificities of Walloon agriculture and their impact on the potential of physical weeding », Biotechnologie, Agronomie, Société et Environnement (BASE), vol. 30, n° 2, mis en ligne le 12 mai 2026, section 3.4, figure 5 et tableau 10. https://popups.uliege.be/1780-4507/index.php?id=21943
[^base2]: Rabier F., Huyghebaert B., Parafiniuk S., Limbourg Q., « Physical weed control: a review in Belgian conditions. Part 2: Technical description of implements, effectiveness and selectivity », BASE, vol. 30, n° 2, 2026, p. 142-156. https://popups.uliege.be/1780-4507/index.php?id=21958
[^ca60]: « Désherbage mixte : l'alliance du chimique avec le mécanique », Chambres d'agriculture des Hauts-de-France, note technique, novembre 2022 (coûts tirés du référentiel « Coûts des opérations culturales 2022 » ; données de féverole et fiches outils). https://hautsdefrance.chambres-agriculture.fr/fileadmin/user_upload/National/FAL_commun/publications/Hauts-de-France/NOTE_TECHNIQUE_DESHERBAGE_MIXTE_2022_CA60.pdf
[^ca60-mais]: Même note, Chambres d'agriculture des Hauts-de-France, novembre 2022, page « Maïs » (jours disponibles d'après Arvalis, station d'Abbeville ; comparaison des stratégies de désherbage). https://hautsdefrance.chambres-agriculture.fr/fileadmin/user_upload/National/FAL_commun/publications/Hauts-de-France/NOTE_TECHNIQUE_DESHERBAGE_MIXTE_2022_CA60.pdf
[^coc]: « Matériels agricoles – Coûts des opérations culturales 2023 », Chambres d'agriculture France, 2023 (gasoil non routier à 1,20 €/L HT), p. 22 à 25. https://cher.chambres-agriculture.fr/fileadmin/user_upload/FAL_COMMUN/Exemples_Modeles/cout_operation_culturales_2023.pdf
[^inovia]: Gloria C., « Colza : désherber mécaniquement en complément des herbicides », Réussir Grandes Cultures, 20 septembre 2023 (mis à jour le 7 février 2024), d'après Terres Inovia. https://reussir.fr/grandes-cultures/colza-desherber-mecaniquement-en-complement-des-herbicides
[^inrae]: Carpentier A. et al., « Alternatives au glyphosate en grandes cultures. Évaluation économique », résumé exécutif, INRAE, 2020. https://www.inrae.fr/sites/default/files/pdf/ExecutiveSummary-Glyphosate%5B1%5D.pdf
[^ppdb]: « Glyphosate », Pesticide Properties DataBase (PPDB), université du Hertfordshire, fiche mise à jour le 16 novembre 2026, rubrique « Impact on climate of production and use » (cite Audsley et al., 2009). https://sitem.herts.ac.uk/aeru/ppdb/en/Reports/373.htm
[^ec]: « Status of glyphosate in the EU », Commission européenne, DG Santé, page consultée le 26 novembre 2026 (renouvellement par le règlement d'exécution (UE) 2023/2660). https://food.ec.europa.eu/plants/pesticides/approval-active-substances-safeners-and-synergists/renewal-approval/glyphosate_en
[^agw2017]: Arrêté du Gouvernement wallon du 30 mars 2017 interdisant l'utilisation de produits phytopharmaceutiques contenant du glyphosate, article 2, Wallex (SPW), consulté le 26 novembre 2026. https://wallex.wallonie.be/eli/arrete/2017/03/30/2017202131/
[^protecteau]: Lebrun J. (Protect'eau), « Réduction de la dérive de minimum 75 % à partir de 2026 », présentation, Gembloux, 15 janvier 2026 (publiée par la Fiwap). https://fiwap.be/wp-content/uploads/2026/01/PM2-2026-01-15-ProtectEauReduction-derive.pdf
[^lavenir]: « Réduction des pesticides en Wallonie : "Ce n'est pas aux fermes d'en porter seules la responsabilité" », L'Avenir, 22 avril 2026. https://www.lavenir.net/actu/environnement/2026/04/22/reduction-des-pesticides-en-wallonie-ce-nest-pas-aux-fermes-den-porter-seules-la-responsabilite-CMISKQJ425BI3IQQWVLV7EAELE/
[^faca]: « Le rouleau destructeur de couverts fait sa mue », Réussir, 12 février 2020. https://www.reussir.fr/le-rouleau-destructeur-de-couverts-fait-sa-mue
[^chedru]: « Sans glyphosate, un gros point d'interrogation avant les cultures d'hiver pour Antoine Chédru », Réussir, 19 avril 2018. https://www.reussir.fr/grandes-cultures/sans-glyphosate-un-gros-point-dinterrogation-avant-les-cultures-dhiver-pour-antoine-chedru
[^aii]: « Liste des investissements admissibles » (aide aux investissements agricoles, AII), SPW Agriculture, Ressources naturelles et Environnement, version de janvier 2026. https://agriculture.wallonie.be/files/accueil/Aides/AII/outils/Liste%20des%20investissements%20admissibles.pdf
[^fao]: « FarmDroid FD20 », AgriTech Observatory, FAO (fiche non datée, données de septembre 2025, consultée le 26 novembre 2026). https://agritechobservatory.review.fao.org/en/farmdroid-fd20
[^pc2020]: Lecocq R., « FarmDroid, un robot à 75 000 € pour semer et biner 20 hectares », Pleinchamp, 8 décembre 2020. https://www.pleinchamp.com/actualite/farmdroid-un-robot-a-75-000-pour-semer-et-biner-20-ha
[^tn2026]: « Entre robotique et mécanique, ils témoignent de leur stratégie de désherbage en betteraves », Terre-net, 5 janvier 2026. https://www.terre-net.fr/betterave/article/891356/betteraves-entre-robotique-et-mecanique-le-desherbage-au-cas-par-cas
[^tn2022]: « Semis et binage des betteraves et colzas bio sont gérés par le robot Farmdroïd », Terre-net, 17 octobre 2022 (mis à jour le 14 février 2024). https://www.terre-net.fr/desherbage/article/221595/le-semis-et-le-binage-des-betteraves-et-des-colzas-bio-est-gere-par-le-farmdroid
[^captage]: Arrêté ministériel du 17 mars 2026 relatif à l'établissement des zones de prévention rapprochée et éloignée de l'ouvrage de prise d'eau souterraine dénommé Galerie de l'Ornoy (Mont-Saint-Guibert), extrait, Wallex (SPW). https://wallex.wallonie.be/contents/djas/133/133663.html
[^ff2023]: Tholhuijsen L., « Reducing herbicide usage dramatically with Farmdroid robot », Future Farming, 6 juin 2023 (chapeau seul, article réservé aux abonnés). https://futurefarming.com/tech-in-focus/field-robots/reducing-herbicide-usage-dramatically-with-farmdroid
[^vrt]: « Des robots désherbeurs testés dans l'agriculture flamande », VRT NWS, 2 juin 2026. https://www.vrt.be/vrtnws/fr/2026/06/02/des-robots-desherbeurs-testes-dans-l-agriculture-flamande-les/
