---
id: fourrages-recoltes
titre: Ensilage et enrubannage
domaine: élevage
dependance_fossile: gasoil; plastique
alternatives: [Pâturage tournant, séchage du foin en grange]
vague_meilleure_alternative: 1
statut: relu
maj: 2026-11-26
---

# Ensilage et enrubannage

## En bref

L'ensilage et l'enrubannage conservent l'herbe et le maïs pour l'hiver par fermentation, à l'abri de l'air, sous bâche ou sous film plastique. Un hectare d'ensilage d'herbe consomme environ 180 L de gasoil de la récolte à l'auge selon un modèle français[^devun], soit {{ v('gasoil_eur_ensilage_herbe_ha', 0) }} au prix actuel ({{ fourchette('gasoil_eur_ensilage_herbe_ha', 0) }} selon les scénarios, calculé). En Belgique, environ 14 000 t de films d'enrubannage et d'ensilage sont mises sur le marché chaque année[^recydata]. La meilleure alternative est de laisser les vaches récolter elles-mêmes : le pâturage tournant dynamique donne l'herbe la moins chère, sans gasoil de récolte ni plastique (vague 1). Pour le stock d'hiver, le séchage du foin en grange supprime le plastique, mais demande un gros investissement et beaucoup d'électricité, à produire de préférence sur son propre toit (vague 2).

## Comment ça marche aujourd'hui

**Ensilage d'herbe.** On fauche, on laisse préfaner au champ, on andaine, puis une ensileuse ou une autochargeuse ramasse l'herbe et la hache. Des remorques l'amènent au silo couloir, où un tracteur la tasse pour chasser l'air. Le tas est fermé sous bâche plastique et lesté. Sans oxygène, des bactéries transforment les sucres en acides et stabilisent le fourrage.

**Enrubannage.** L'herbe préfanée est pressée en balles rondes ou carrées, puis chaque balle est entourée d'un film plastique étirable. On recommande au moins 4 couches de film sur une balle ronde, 6 sur une balle carrée ou en boudin continu (conseil australien)[^mickan]. L'enrubannage convient aux petites parcelles et aux petites quantités, mais il coûte plus cher à la tonne.

**Ensilage de maïs.** Le maïs est haché sur pied par une ensileuse automotrice, puis tassé et bâché comme l'herbe. C'est la culture fourragère la plus gourmande en gasoil, car elle cumule travail du sol, semis, traitements et récolte.

**Ce que coûtent les fourrages.** Les références belges sont rares. Un document du CRA-W de 2022 retient 0,05 € le kg de matière sèche (MS) d'herbe pâturée contre 0,15 € pour l'ensilage d'herbe, d'après Fourrages Mieux, soit 50 contre 150 € la tonne de MS (prix de 2021)[^craw-ptd]. Les références françaises vont dans le même sens :

| Fourrage | Coût indicatif | Source |
|---|---|---|
| Herbe pâturée | 17 €/t MS | BCEL Ouest, cité en 2023 (prix français)[^bcel] |
| Ensilage de maïs | 50 €/t MS | même source[^bcel] |
| Enrubannage d'herbe | 75 €/t MS | même source[^bcel] |
| Récolte seule, ensilage d'herbe | 85 €/t MS hors travail, 105 € avec | Chambre d'agriculture, 2025 (prix français)[^ca17] |
| Récolte seule, foin séché au champ | 70 €/t MS hors travail, 95 € avec | même source[^ca17] |
| Récolte seule, enrubannage | 115 €/t MS hors travail, 140 € avec | même source[^ca17] |

Les méthodes diffèrent d'une source à l'autre (avec ou sans la production de l'herbe, avec ou sans main-d'œuvre) : seul l'ordre est fiable. L'herbe pâturée est toujours la moins chère et l'enrubannage le plus cher. La même chambre d'agriculture chiffre la production de l'herbe sur pied entre 50 et 104 €/t MS selon le type de prairie, et celle du maïs ensilage entre 65 et 110 €/t MS[^ca17].

## Où entrent le pétrole et le gaz

- **Gasoil des chantiers.** Un modèle établi sur 171 exploitations françaises donne, récolte et distribution comprises, environ 76 L de gasoil par hectare de foin, 122 L par hectare d'enrubannage, 180 L par hectare d'ensilage d'herbe et 466 L par hectare de maïs ensilage (culture comprise)[^devun]. Un parcellaire éclaté et éloigné augmente la consommation d'environ 13 %, un parcellaire groupé la réduit d'environ 11 %[^devun]. Au prix actuel du gasoil (calculé) :

| Mode de récolte | Gasoil par hectare | Fourchette des scénarios |
|---|---|---|
| Foin au champ | {{ v('gasoil_eur_foin_ha', 0) }} | {{ fourchette('gasoil_eur_foin_ha', 0) }} |
| Enrubannage | {{ v('gasoil_eur_enrubannage_ha', 0) }} | {{ fourchette('gasoil_eur_enrubannage_ha', 0) }} |
| Ensilage d'herbe | {{ v('gasoil_eur_ensilage_herbe_ha', 0) }} | {{ fourchette('gasoil_eur_ensilage_herbe_ha', 0) }} |
| Maïs ensilage | {{ v('gasoil_eur_mais_ensilage_ha', 0) }} | {{ fourchette('gasoil_eur_mais_ensilage_ha', 0) }} |

- **Plastique.** Les films sont du polyéthylène, issu du pétrole ou du gaz. En Belgique, environ 20 000 t de plastiques agricoles sont mises sur le marché chaque année : 38 % de films d'enrubannage (7 800 t), 30 % de films d'ensilage (6 100 t), 5 % de filets et 4 % de ficelles[^recydata]. Seuls 37 % environ de ces quantités sont collectés (poids net)[^recydata].
- **Engrais azoté.** Prairies fauchées et maïs reçoivent souvent de l'azote de synthèse, fabriqué au gaz : voir la fiche [Azote de synthèse](../fertilisation/azote-synthese.md).
- **Conservateurs.** Certains ensilages reçoivent un conservateur à base d'acides de synthèse. Les inoculants bactériens, eux, ne sont pas d'origine fossile.

## Les alternatives

### 1. Pâturage tournant dynamique (vague 1)

Le troupeau change de parcelle tous les 0,5 à 3 jours, avec un chargement instantané élevé (50 à 200 unités de gros bétail par hectare) et un repos de 20 à 40 jours entre deux passages selon la saison[^craw-poster]. L'herbe est mangée au bon stade et repousse vite. Un exemple du CRA-W découpe 19 paddocks pour 40 à 50 vaches laitières[^craw-poster]. Les vaches récoltent elles-mêmes : pas de fauche, pas de transport, pas de plastique, et les bouses restent sur la prairie.

**Résultats en Wallonie.** Le CRA-W a interrogé 12 fermes laitières wallonnes passées d'un pâturage continu ou tournant long au pâturage tournant dynamique, 2 à 8 ans plus tôt[^craw-ptd]. Toutes se disent satisfaites et mieux valoriser leurs prairies ; 8 sur 12 constatent un gain économique et 8 sur 12 une production d'herbe plus élevée sur l'année ; 6 sur 12 gagnent du temps de travail, 4 sur 12 jugent en revanche que la conduite demande plus de suivi[^craw-ptd]. Le gain vient de l'écart de prix : herbe pâturée à 0,05 €/kg MS contre 0,15 €/kg MS pour l'ensilage d'herbe[^craw-ptd].

**Résultats chiffrés en France.** À la ferme expérimentale de Trévarez (Bretagne, 2012-2017), le système avec 40 ares pâturables par vache a eu un coût alimentaire inférieur de 21 €/1 000 L à celui avec 15 ares par vache et plus de maïs[^trevarez]. À troupeau égal (60 vaches), l'écart de revenu atteignait environ 11 250 € par an, chaque année, quel que soit le contexte de prix[^trevarez].

Conditions :

- assez de prairie accessible depuis la salle de traite (40 ares par vache à Trévarez)[^trevarez] ;
- aménager le parcellaire : chemins, clôtures (souvent un fil mobile), points d'eau, ombre. C'est le premier frein cité (6 fermes sur 12), mais les éleveurs jugent l'investissement rentabilisé[^craw-ptd] ;
- accepter de moins complémenter et suivre la pousse de l'herbe, par exemple à l'herbomètre.

Limites : le pâturage ne supprime pas le stock d'hiver. Il faut encore récolter les excédents de printemps et nourrir l'hiver. Pour faucher les petites parcelles en excédent, 3 des 12 fermes ont acheté une presse-enrubanneuse[^craw-ptd] : une partie de la dépendance au plastique reste.

### 2. Séchage du foin en grange (vague 2)

L'herbe est fauchée jeune, préfanée au champ, puis rentrée en vrac à l'autochargeuse dans des cellules ventilées. Des ventilateurs soufflent à travers le tas de l'air réchauffé sous la toiture, qui sert de capteur solaire. Le séchoir est aussi le lieu de stockage ; une griffe fixée dans la grange charge et distribue le foin. Sans fermentation ni plastique, on obtient un foin très riche et appétant, et on récolte l'herbe au bon stade sans attendre plusieurs jours de beau temps[^trame].

**En Wallonie.** Le premier séchoir solaire wallon date de 2007 ; on en comptait 6 en 2018[^trame]. Le « lait de foin » est une Spécialité traditionnelle garantie européenne, et une association wallonne d'éleveurs et de fromagers existe depuis 2018[^trame]. La ferme du Centre de référence et d'expérimentation suivie par le SPW à Froidchapelle (73 ha de prairies, sans maïs) sèche son foin en grange depuis 2019 : autonomie fourragère de 100 %, pressage et enrubannage quasi supprimés[^spw-cre].

**Coût.** L'investissement est lourd : de 340 à 1 200 € par tonne stockable en Belgique selon l'équipement, la taille et l'auto-construction[^trame] ; 770 €/t MS en moyenne (de 100 à 1 900 €) dans une enquête française de 2011, soit 163 000 € par installation[^ademe]. Les éleveurs wallons en vrac parlent de « plusieurs centaines de milliers d'euros »[^craw-ptd]. Dans huit séchoirs suivis dans les Pyrénées-Atlantiques, l'annuité (aides déduites, prêt de 12 ans) va de 38 à 136 € par tonne de MS ventilée (prix français)[^ca64].

**Électricité.** Un séchoir consomme en moyenne 97 kWh par tonne de MS, de 30 à 230 kWh selon la conduite (enquête française)[^ademe]. Le séchage représentait en moyenne 46 % de l'électricité de ces fermes[^ademe]. Le coût de l'énergie change tout (calculé) :

| Électricité | Par tonne de MS séchée | Fourchette des scénarios |
|---|---|---|
| Réseau | {{ v('sechage_grange_reseau_tms', 0) }} | {{ fourchette('sechage_grange_reseau_tms', 0) }} |
| Photovoltaïque de la ferme | {{ v('sechage_grange_pv_tms', 0) }} | fixe |

Sur le réseau, l'électricité coûte par tonne à peu près autant que l'annuité du séchoir le moins cher suivi dans les Pyrénées-Atlantiques (38 €/t MS[^ca64]). Sur des panneaux posés sur le séchoir, elle devient marginale. On sèche pendant la saison de pousse, au printemps et en été, quand les panneaux produisent le plus : 80 % des projets de séchoir intègrent désormais du photovoltaïque, et les panneaux augmentent un peu le rendement du capteur solaire (40 % au lieu de 35 % avec un bac acier)[^segrafo]. Dans un exemple français, un toit thermovoltaïque de 45 kW alimente le séchoir avec 9 kW et vend le reste[^thermo].

**Travail et gasoil.** Dans les Pyrénées-Atlantiques, un éleveur passé au séchoir n'a plus de frais d'enrubannage et compte 200 heures de tracteur en moins par an[^ca64]. La fauche, le fanage, l'andainage et l'autochargeuse restent au gasoil : le séchoir supprime le plastique, pas le tracteur.

**Aide wallonne.** L'aide aux investissements agricoles (AII) prévoit un forfait de 498 €/m² pour un hall de séchage en vrac et de 953 €/m² pour un séchoir compact à balles[^am-aii]. L'aide est un pourcentage de ce forfait : 10 % de base, majoré notamment pour un jeune agriculteur, un système herbager, le bio ou une filière de qualité, avec un plafond de 40 %, limité aux premiers 1 000 m², et 200 000 € d'aide au total par bénéficiaire sur 2023-2027[^am-aii].

Conditions :

- un débouché qui paie la qualité, ou de gros gains sur les concentrés. Le lait de foin peut rapporter 0,05 à 0,10 €/L de plus, jusqu'à 0,30 €/L en filière fromagère, mais le label est encore peu reconnu en Wallonie[^trame][^craw-ptd] ;
- des prairies proches du séchoir : l'herbe est rentrée en vrac, souvent en plusieurs petits chantiers ;
- une production visée raisonnable : il ne faut pas espérer plus de 8 000 L par vache et par an avec une ration à base de foin[^trame] ;
- du temps de préparation : 2 à 3 ans avant la première récolte, puis un an pour maîtriser l'outil[^trame] ;
- une toiture photovoltaïque, sinon l'électricité du réseau pèse lourd et reste en partie produite au gaz.

Pourquoi vague 2 : l'économie de plastique et de concentrés est réelle, mais l'investissement ne se rembourse que sous conditions (valorisation du lait, bio, aides, auto-construction, photovoltaïque). Le séchoir peut aussi sécher du grain, du bois ou de la luzerne le reste de l'année, ce qui améliore sa rentabilité[^segrafo].

## Ce qui ferme la boucle

- Les vaches récoltent l'herbe et rendent les bouses à la prairie : ni gasoil de récolte, ni plastique, ni épandage.
- Le trèfle des prairies pâturées fixe l'azote de l'air et remplace une partie de l'engrais de synthèse.
- Le toit du séchoir capte la chaleur du soleil et produit l'électricité des ventilateurs, à la saison où l'on sèche.
- Le plastique qui reste se réduit et se recycle : une enrubanneuse en continu économise environ 40 % de film par rapport à une enrubanneuse traînée (référence française ancienne)[^reussir-2010]. Les intercommunales wallonnes collectent les films à des points avec pont-bascule, propres, triés et en paquets de 20 kg maximum. Depuis la fin des subsides régionaux en janvier 2025, la collecte coûte en moyenne {{ v('collecte_plastique_agricole_t', 0) }} à l'agriculteur[^recydata]. Aucun recycleur de plastiques agricoles n'est actif en Belgique, et les filets et ficelles ne sont pas encore recyclés[^recydata]. L'étude réalisée pour le SPW propose un système de responsabilité élargie des producteurs, qui ferait payer la filière aux fabricants de films[^recydata].

## À vérifier

- Coûts wallons récents des fourrages par tonne de MS (herbe pâturée, ensilage d'herbe, maïs, enrubannage, foin ventilé) : la référence de Fourrages Mieux (Glesner, 2021, *Lettre paysanne* de la FUGEA) n'a été lue que par la citation du CRA-W.
- Tarifs belges d'entreprise pour l'ensilage, le pressage et l'enrubannage (par hectare ou par balle).
- Consommation de gasoil par chantier en Belgique ; le modèle cité est français (bassin charolais, bovins viande) et inclut la distribution.
- Quantité de film par balle enrubannée (en kg) et prix du film : aucune source fiable lue.
- Coût d'aménagement d'un parcellaire en pâturage tournant (clôtures, chemins, abreuvement) en Wallonie, et éligibilité à l'AII.
- Investissement et consommation d'électricité de séchoirs wallons existants ; les chiffres d'énergie et d'annuité cités sont français.
- Séchage en grange avec la chaleur d'un méthaniseur ou d'une chaudière à plaquettes.
- Tarif de collecte des plastiques en 2026 dans chaque intercommunale wallonne, et avancement du projet de responsabilité élargie des producteurs.
- Part des conservateurs chimiques dans les ensilages wallons.
- Date de reconnaissance du lait de foin comme Spécialité traditionnelle garantie : 2016 selon Tr@me, 2014 selon le CRA-W.

## Sources

[^devun]: Devun J. et al., « Conséquences des pratiques fourragères et des caractéristiques du parcellaire sur la consommation de carburant dans les exploitations bovin viande du bassin Charolais », Rencontres Recherches Ruminants, n° 21, 2014, p. 44 (Institut de l'élevage, INRA). https://journees3r.fr/wp-content/uploads/2015/01/Texte_4_affiche_Environnement_J-Devun-f12.pdf
[^recydata]: Claeys K., Van den Plas M., « Étude sur un système de responsabilité élargie du producteur (REP) pour la gestion des déchets de plastiques agricoles en Belgique », Recydata, étude subventionnée par le Service public de Wallonie, 15 juillet 2026. https://environnement.wallonie.be/files/Publications/Vers-un-systeme-de-gestion-des-dechets-des-plastiques-agricoles.pdf
[^mickan]: Mickan F., « Wrapping silage bales is becoming very confusing », Department of Economic Development, Jobs, Transport and Resources (Victoria, Australie), publié par Dairy Australia, 2017. https://enlight.dairyaustralia.com.au/pluginfile.php/15405/mod_page/content/13/Wrapping%20silage%20bales%20is%20becoming%20confusing.pdf
[^craw-ptd]: Lefèvre A., « Motivations, freins et leviers face à des changements de pratiques visant à optimiser la valorisation des fourrages. Retour d'expérience d'éleveurs laitiers wallons », CRA-W, mai 2022 (chiffre du coût de l'herbe d'après Glesner N., Lefèvre A., *Lettre paysanne* FUGEA, numéro spécial 2021). https://www.cra.wallonie.be/uploads/2022/06/delivrable-3-4-retour-dexperience-deleveurs-laitiers-wallons-motivations-freins-leviers-face-a-des-changements-de-pratiques-visant-a-ameliorer-lerf.pdf
[^bcel]: « Valoriser l'herbe d'automne pour maîtriser ses charges en élevage laitier », Réussir Lait (France), 10 novembre 2023, d'après des calculs de BCEL Ouest (années 2018-2019). https://www.reussir.fr/lait/valoriser-lherbe-dautomne-pour-maitriser-ses-charges-en-elevage-laitier
[^ca17]: « Fourrages 2025 : des repères de prix », Chambre d'agriculture Charente-Maritime Deux-Sèvres (France), avril 2025. https://cmds.chambres-agriculture.fr/fileadmin/user_upload/Nouvelle-Aquitaine/Medias_Externes/Synthese_prix_fourrages_2025.pdf
[^craw-poster]: Lefèvre A., Glesner N., « Le pâturage tournant dynamique, en quoi ça consiste ? Résultats d'enquêtes menées dans des fermes laitières wallonnes », poster, CRA-W et Fourrages Mieux, 2021. https://www.cra.wallonie.be/uploads/2021/09/poster_ptd1.pdf
[^trevarez]: « La ferme expérimentale de Trévarez : 50 000 euros en cinq ans pour le système plus pâturant », Réussir Lait (France), 17 avril 2021. https://www.reussir.fr/lait/la-ferme-experimentale-de-trevarez-50-000-euros-en-cinq-ans-pour-le-systeme-plus-paturant
[^trame]: Delaite B., « Le séchage du foin en grange, un profond changement dans la gestion d'une ferme », notice technique, Tr@me, groupe opérationnel du Réseau wallon de Développement rural, publiée sur Encyclopedia Pratensis, novembre 2019. https://www.encyclopediapratensis.eu/wp-content/uploads/2019/11/BELGIUM_TRAME_BarnDrying_SechageEnGrange_French.pdf
[^spw-cre]: « Bovins laitiers bio avec séchage de foin en grange et transformation en circuit court », Centre de référence et d'expérimentation 2022-2024, SPW Agriculture (services extérieurs de Thuin et de Ciney), document non daté, consulté le 26 novembre 2026. https://agriculture.wallonie.be/files/20182/21876/Bovins%20laitiers%20BIO%20avec%20s%c3%a9chage%20de%20foin%20en%20grange%20et%20transformation%20en%20circuit%20-court.pdf
[^ademe]: « Utilisation rationnelle de l'énergie pour le séchage des grains et des fourrages. Séchage des fourrages », rapport final, ADEME, Coop de France, Arvalis et Solagro (France), septembre 2011. https://solagro.org/medias/publications/f16_utilisationrationnellesechagefourrages.pdf
[^ca64]: « Le séchage en grange dans le 64 : témoignages d'éleveurs », projet Ô ton herbe, Chambre d'agriculture des Pyrénées-Atlantiques (France), novembre 2023. https://pa.chambres-agriculture.fr/fileadmin/user_upload/298_chambre_dagriculture_des_pyrenees-atlantiques/1-s_informer/Agir_face_au_changement_climatique/Sechage_en_grange_Temoignage_eleveurs_221123.pdf
[^segrafo]: « Foin : concevoir son séchoir en grange en six questions », Réussir Lait (France), 29 mai 2024, entretien avec un conseiller de Segrafo. https://www.reussir.fr/lait/foin-concevoir-son-sechoir-en-grange-en-six-questions
[^thermo]: « 300 000 € investis dans un séchoir en grange thermovoltaïque », Réussir Lait (France), 18 mars 2021. https://www.reussir.fr/lait/300-000-eu-investis-dans-un-sechoir-en-grange-thermovoltaique
[^am-aii]: Arrêté ministériel du 23 février 2023 exécutant l'arrêté du Gouvernement wallon du 23 février 2023 relatif aux aides à l'installation et aux investissements (secteurs agricole et horticole…), articles 4 et 5 et annexe 3, version consolidée en vigueur au 1er janvier 2026, Wallex. https://wallex.wallonie.be/sites/wallex/contents/acts/87/87905/4.html
[^reussir-2010]: « Les coûts de récolte de l'herbe à la loupe », Réussir Lait (France), 14 septembre 2010, d'après la chambre d'agriculture de la Creuse. https://www.reussir.fr/lait/les-couts-de-recolte-de-lherbe-la-loupe
