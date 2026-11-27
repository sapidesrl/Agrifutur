---
id: electricite-reseau
titre: Électricité du réseau
domaine: énergie
dependance_fossile: gaz naturel (part de la production électrique)
alternatives: [Photovoltaïque en autoconsommation, micro-biométhanisation]
vague_meilleure_alternative: 1
statut: relu
maj: 2026-11-27
---

# Électricité du réseau

!!! warning "Sources à relire"
    Les sources ont été lues sur la page d'origine le 26 novembre 2026. Le site d'Elia reste inaccessible à notre outil : son communiqué sur le mix électrique 2025 a été lu dans la version néerlandaise publiée par la fédération VFB. Les prix d'installation photovoltaïque de 36 à 250 kWc viennent du régulateur bruxellois : aucune source wallonne équivalente n'a été trouvée. Les aides publiques ont été relues le 27 novembre 2026 (voir [les aides publiques](../../aides.md)).

## En bref

Une ferme achète son électricité au réseau pour la traite, le refroidissement du lait, l'eau chaude, la ventilation, l'éclairage et les moteurs. En 2025, les centrales au gaz ont produit 19 % de l'électricité belge, mais le prix de gros de l'électricité suit celui du gaz : la crise du gaz de 2026 a fait monter la facture. Une PME wallonne paie en moyenne {{ v('electricite_reseau_htva', 2) }} HTVA tout compris, contre {{ v('electricite_reseau_htva', 2, scenario='bas') }} en février 2026. Un kWh produit par ses propres panneaux coûte {{ v('pv_kwh_production', 3) }} (calculé, hors frais financiers) : le photovoltaïque en autoconsommation est rentable aujourd'hui, et il le restait avant la crise (vague 1). La micro-biométhanisation du lisier produit jour et nuit, mais elle ne se rembourse qu'avec les certificats verts et l'aide GREEN : {{ v('microbiometh_retour_aides_ans', 0) }} au lieu de {{ v('microbiometh_retour_ans', 0) }} (calculé), avec des taux 2026 encore inconnus (vague 2).

## Comment ça marche aujourd'hui

L'électricité arrive par le réseau de distribution (ORES ou RESA en Wallonie). Une ferme paie trois choses : l'énergie (au fournisseur), le transport et la distribution (au gestionnaire de réseau), et les taxes et surcharges. Pour un ménage wallon, en octobre 2026, l'énergie représentait 47 % de la facture, le réseau 28 %, les taxes 20 % et la TVA 6 %[^creg].

Le prix de référence de ce projet est le prix moyen calculé par la CREG pour une PME de 50 000 kWh par an en Wallonie : {{ v('electricite_reseau_htva', 4) }} HTVA en octobre 2026, {{ v('electricite_reseau_htva', 4, scenario='bas') }} en février 2026 (voir [les hypothèses](../../hypotheses.md)). Un contrat négocié peut être moins cher.

Sur une ferme laitière, la traite, le refroidissement du lait et l'eau chaude de lavage sont les plus gros postes. Ils se concentrent le matin et le soir, autour des deux traites[^save]. Le projet flamand SAVE a simulé une ferme de 120 vaches qui livre 1 million de litres par an : elle consomme 36 000 kWh par an[^save]. La ferme de Gozée équipée en micro-biométhanisation consommait 40 000 à 50 000 kWh par an[^rtbf]. Ce projet retient {{ v('ferme_conso_elec') }} pour une ferme laitière type (hypothèse). Une ferme de grandes cultures consomme surtout pour le séchage, la ventilation et le stockage au froid, souvent en saison.

## Où entrent le pétrole et le gaz

- **Production au gaz** : en 2025, les centrales au gaz ont produit 12,6 TWh, soit 19 % de la production d'électricité en Belgique. Le nucléaire en a produit 34 % et les renouvelables autant. La Belgique a aussi importé 14 TWh nets, surtout de France et des Pays-Bas[^elia].
- **Le prix suit celui du gaz** : les centrales au gaz servent d'appoint au réseau, et le prix de gros de l'électricité évolue avec celui du gaz. Une centrale au gaz de rendement 50 % brûle 2 MWh de gaz pour produire 1 MWh d'électricité, et la CREG suit l'écart entre ces deux prix (« spark spread »)[^creg]. Entre juillet et septembre 2026, le prix de gros du gaz (TTF) a augmenté d'environ 37 % et celui de l'électricité livrée le mois suivant d'environ 41 % (calculé à partir du tableau de bord de la CREG)[^creg].
- **Une part seulement de la facture suit le gaz** : le réseau et les taxes ne suivent pas le prix du gaz : en proportion, la facture monte donc moins que le prix de gros.
- **Matériel** : câbles, isolants et coffrets contiennent des plastiques issus de la pétrochimie.

## Les alternatives

### 1. Photovoltaïque en autoconsommation (vague 1)

Des panneaux sur la toiture des hangars ou des étables produisent de l'électricité en journée. L'électricité consommée au moment où elle est produite remplace un kWh acheté. Le surplus part sur le réseau et le fournisseur le rachète à bas prix.

**Ce que coûte un kWh produit.** Avec un prix installé de {{ v('pv_prix_installe') }} (estimé), une production de {{ v('pv_production') }} (estimé), {{ v('pv_duree_vie', 0) }} de durée de vie et des frais d'entretien et d'onduleur de {{ v('pv_entretien_part', 0) }} du prix sur toute la durée, soit {{ v('pv_om_annuel_spw', 1) }} par an, la référence wallonne du SPW pour les installations de 10 à 1 000 kW[^spw-cpma], un kWh revient à {{ v('pv_kwh_production', 3) }} (calculé, sans frais financiers). Le kWh du réseau coûte {{ v('ratio_reseau_pv', 1) }} plus cher ({{ fourchette('ratio_reseau_pv', 1) }} selon les scénarios).

Repères de prix :

- le régulateur bruxellois Brugel a relevé, sur les factures de 2025 et 2026, raccordement, compteur et frais administratifs compris, 1 289 €/kWc de 5 à 36 kWc, 934 €/kWc de 36 à 100 kWc et 800 €/kWc de 100 à 250 kWc (prix bruxellois, échantillon réduit au-delà de 36 kWc). Il juge probable une remontée du prix des modules en 2026[^brugel] ;
- l'aide wallonne aux investissements agricoles calcule son aide sur un coût simplifié de {{ v('aii_pv_forfait') }}[^am-aii].

Repères de production : la CWaPE compte 910 kWh par kWe et par an pour une installation domestique[^cwape-prosumer]. Brugel mesure une médiane de 850 kWh/kWc à Bruxelles et une perte de production de 0,7 % par an[^brugel]. Fin 2023, le parc wallon comptait 2 184 MWc pour une production estimée à 1 778 GWh, soit environ 815 kWh/kWc (calculé), anciennes installations et mauvaises orientations comprises[^livre-blanc].

**Tout se joue sur l'autoconsommation.** Un kWh consommé sur place vaut {{ v('electricite_reseau_htva', 2) }} ; un kWh injecté vaut {{ v('pv_injection_prix', 3) }}. Test-Achats relevait en mai 2026 des prix de rachat de 3 à 4 c€/kWh en moyenne, moins de 3 c€ avant la crise, pour la plupart indexés sur le marché de gros et parfois négatifs[^testachats]. La CWaPE parlait d'environ 20 €/MWh en 2025[^cwape-batt]. Elia a observé des prix de gros négatifs 6,1 % du temps en 2025, surtout les jours de forte production et de faible demande[^elia].

Le photovoltaïque est rentable dès que l'exploitation consomme sur place au moins {{ v('pv_autoconso_mini', 0) }} de sa production ({{ fourchette('pv_autoconso_mini', 0) }} selon les scénarios, calculé sans frais financiers). En 2018, avec des prix bien plus bas, le projet SAVE estimait ce seuil à près de 50 %[^save].

Le taux d'autoconsommation dépend du profil de la ferme :

- **ferme laitière à deux traites** : la consommation tombe le matin et le soir, hors du pic solaire. Dans la simulation SAVE (30 kWc, 36 000 kWh par an), l'autoconsommation n'atteint que 13 % si le chauffe-eau tourne la nuit, et 41 % s'il tourne de 10 h à 16 h. Une commande intelligente n'ajoute qu'un point (42 %) quand elle ne pilote qu'un appareil[^save] ;
- **ferme laitière avec robot de traite** : la consommation est étalée sur la journée, l'autoconsommation est plus haute. SAVE conseille de limiter la puissance à 0,3 kWc par MWh consommé avec deux traites, et 0,6 kWc avec des robots[^save] ;
- **grandes cultures** : l'autoconsommation est forte pendant le séchage ou la ventilation des stocks, faible le reste de l'année. Il faut la mesurer au cas par cas (voir « À vérifier ») ;
- à Bruxelles, tous secteurs confondus, Brugel retient 45 % pour les installations de 36 à 100 kWc et 69 % au-delà[^brugel].

**Exemple : ferme laitière type** (hypothèses : {{ v('pv_ferme_kwc', 0) }}, {{ v('pv_autoconsommation', 0) }} d'autoconsommation avec l'eau chaude produite en journée, {{ v('ferme_conso_elec') }} de consommation) :

| Calculé | Valeur |
|---|---|
| Production | {{ v('pv_ferme_production_an') }} |
| Consommée sur place | {{ v('pv_ferme_autoconso_kwh') }}, soit {{ v('pv_ferme_couverture', 0) }} des besoins de la ferme |
| Injectée | {{ v('pv_ferme_injection_kwh') }} |
| Investissement | {{ v('pv_ferme_investissement') }} |
| Aide AII (taux de base et architecture verte) | {{ v('pv_ferme_aide_aii') }} |
| Valeur de l'électricité produite | {{ v('pv_ferme_valeur_an') }} ({{ fourchette('pv_ferme_valeur_an') }}) |
| Coût annuel (investissement et entretien étalés, sans aide) | {{ v('pv_ferme_cout_an') }} |
| Gain net annuel | {{ v('pv_ferme_gain_net_an') }} ({{ fourchette('pv_ferme_gain_net_an') }}) |
| Temps de retour simple, aide déduite | {{ v('pv_ferme_retour_ans', 1) }} ({{ fourchette('pv_ferme_retour_ans', 1) }}) |
| Temps de retour avec les certificats verts (au-delà de 10 kW, sur réservation) | {{ v('pv_ferme_retour_cv_ans', 1) }} ({{ fourchette('pv_ferme_retour_cv_ans', 1) }}) |

Si toute la production était injectée, elle ne rapporterait que {{ v('pv_ferme_valeur_an_sans_autoconso') }} : l'électricité consommée sur place fait presque toute la rentabilité. L'installation reste rentable dans le scénario d'avant-crise. Le calcul ne compte ni les frais financiers, ni la perte de rendement des panneaux.

**Injection et compteur.** En Wallonie, la compensation (le compteur qui tourne à l'envers) a pris fin le 31 décembre 2023. Elle reste en place jusqu'au 31 décembre 2030 pour les installations de 10 kW au plus mises en service avant le 1er janvier 2024, qui paient en échange le tarif prosumer. Les installations plus récentes, et toutes celles de plus de 10 kW, sont rémunérées au prix d'injection du fournisseur[^cwape-batt]. Une installation agricole de {{ v('pv_ferme_kwc', 0) }} n'a donc jamais droit à la compensation. Le tarif prosumer ne concerne que les petites installations domestiques : il est calculé en supposant que 40,26 % de la production est autoconsommée[^cwape-batt] [^cwape-prosumer].

**Aides.** L'aide wallonne aux investissements agricoles (AII) retient le photovoltaïque comme « énergie renouvelable professionnelle ». L'aide est un pourcentage du coût simplifié de {{ v('aii_pv_forfait') }}, compté sur la puissance des panneaux plafonnée à ce que l'onduleur accepte en entrée[^am-aii] [^aii-ni2]. Pour un agriculteur actif, le taux de base est de {{ v('aii_taux_base', 0) }}, plus {{ v('aii_maj_av_re', 0) }} pour un investissement lié à l'architecture verte ou à la résilience économique, deux critères cochés pour le photovoltaïque : {{ v('aii_taux_pv', 0) }} sans autre majoration (calculé). D'autres majorations s'ajoutent ({{ v('aii_maj_jeune', 0) }} pour un jeune agriculteur, {{ v('aii_maj_bio_total', 0) }} pour une ferme totalement bio, {{ v('aii_maj_herbager', 0) }} en zone à contraintes ou en système herbager…), avec un plafond de {{ v('aii_plafond_taux', 0) }} et {{ v('aii_plafond_beneficiaire', 0) }} d'aide par bénéficiaire sur 2023-2027[^am-aii]. L'aide ne vaut que pour l'énergie produite dans le cadre de l'activité professionnelle[^aii-ni2]. La demande doit atteindre {{ v('aii_seuil_points', 0, unite=False) }} points de sélection : un éleveur sans majoration ne les atteint que si les points « architecture verte » et « résilience » s'additionnent, ce qui reste à confirmer[^am-aii]. L'aide AII est déjà déduite dans l'exemple ci-dessus.

Deux soutiens peuvent s'y ajouter :

- **certificats verts**, au-delà de 10 kW et sur réservation préalable[^cv-cpma]. Pour les demandes de 2025, le photovoltaïque de 10 à 1 000 kW reçoit {{ v('cv_pv_taux', 3) }}[^cv-tableau], rachetés au prix garanti de {{ v('cv_prix_garanti', 0) }}[^cv-rapport] : {{ v('pv_cv_eur_mwh', 1) }} produit, soit environ {{ v('pv_ferme_cv_an', 0) }} pour la ferme type (calculé), en plus du gain net. Les taux 2026 et la durée d'octroi n'étaient pas publiés au 27 novembre 2026. Depuis janvier 2026, les soutiens régionaux à l'énergie renouvelable sont une exception à la règle de non-cumul de l'AII[^agw-aii] ;
- **déduction fédérale pour investissement** : un indépendant ou une petite société imposé sur ses bénéfices réels déduit {{ v('dpi_thematique_pp', 0) }} du prix d'un investissement dans l'énergie renouvelable[^dpi-barreau]. Elle n'aide pas un agriculteur imposé au forfait (point non vérifié).

L'aide GREEN de la Région ne finance pas le photovoltaïque[^green-agw]. Les aides ne changent pas la conclusion : le photovoltaïque est rentable sans elles et reste en vague 1.

**Batteries.** Une batterie stocke le surplus de midi pour la traite du soir. La CWaPE estime qu'elle peut relever le taux d'autoconsommation de 15 à 20 %[^cwape-batt]. Une batterie de 10 ou 13,5 kWh coûte environ 8 000 € installée (modèles résidentiels, janvier 2026)[^lavenir-batt]. Avec {{ v('batterie_prix_kwh') }} (estimé) et {{ v('batterie_cycles_an') }} (hypothèse), chaque kWh de capacité rapporte {{ v('batterie_gain_kwh_an', 0) }} et se rembourse en {{ v('batterie_retour_ans', 1) }} ({{ fourchette('batterie_retour_ans', 1) }} selon les scénarios, calculé, hors remplacement). En 2018, SAVE jugeait les batteries non rentables pour la seule autoconsommation, sauf si elles servent aussi de groupe de secours[^save]. Leur rentabilité dépend donc de leur durée de vie réelle, non chiffrée ici (voir « À vérifier »). Aucune aide régionale ne finance une batterie : elle est absente de la liste de l'AII[^aii-liste] et GREEN exclut le stockage d'électricité[^green-agw]. Seule la déduction fédérale de {{ v('dpi_thematique_pp', 0) }} peut jouer, au régime réel, car elle couvre le stockage d'énergie[^dpi-barreau]. Les batteries ajoutent aussi une dépendance au lithium et aux métaux importés. Avant d'en acheter, on déplace d'abord ce qui peut l'être vers la journée : chauffe-eau, pompes, ventilation, recharge des engins.

Conditions :

- une toiture solide, bien orientée et sans amiante ;
- une consommation en journée, ou des usages qu'on peut y déplacer ;
- un raccordement qui accepte l'injection : sur les réseaux saturés, l'onduleur décroche quand la tension dépasse 253 V en moyenne sur 10 minutes[^cwape-batt]. Un régime d'indemnisation de ces décrochages est en préparation en Wallonie[^cwape-indemn].

Limites : les panneaux ne produisent ni la nuit ni guère en hiver. La ferme reste raccordée et achète encore au réseau la majorité de son électricité ({{ v('pv_ferme_couverture', 0) }} des besoins couverts dans l'exemple). Le prix des modules dépend de la production chinoise : Brugel juge probable une hausse en 2026 après la suppression, au 1er avril 2026, des remboursements de TVA à l'exportation en Chine[^brugel].

**Agrivoltaïsme.** Le livre blanc de l'agrivoltaïsme en Wallonie (ULiège, fédérations agricoles et secteur, juillet 2024) recommande de privilégier l'autoconsommation par l'exploitant, et d'équiper d'abord les toitures de la ferme avant tout projet au sol. Il rappelle que les panneaux au sol en zone agricole sont dérogatoires au CoDT, sauf sur les toitures ou à l'arrière des bâtiments pour l'autoconsommation[^livre-blanc]. Les parcs au sol relèvent d'un autre modèle (vente d'électricité, location de terres) que cette fiche ne traite pas.

### 2. Micro-biométhanisation (vague 2)

Le lisier frais est pompé chaque jour dans une cuve chauffée vers 40 °C, où il fermente environ un mois. Le biogaz (méthane et CO₂) alimente un moteur qui produit de l'électricité et de la chaleur. Le reste, le digestat, retourne aux champs[^lavenir-marbais]. En Wallonie, une unité « micro » fait moins de 50 kW électriques et vise l'autonomie énergétique de l'exploitation[^panorama].

La filière grandit : la Wallonie comptait 84 unités de biométhanisation en 2024, dont 59 agricoles, parmi lesquelles 32 micro-unités, 15 de plus qu'en 2023. Selon Valbiom, cette hausse vient surtout du déblocage, depuis 2024, d'un nombre plus cohérent de certificats verts pour le biogaz, « soutien indispensable » à l'équilibre économique de presque toutes les unités[^panorama].

Exemples :

- à Marbais (Villers-la-Ville), la ferme du Petit Mont a installé une unité de 20 kW sur le seul lisier de ses 120 vaches laitières. L'investissement avoisine 400 000 €, avec un retour espéré en huit ans, mais seulement grâce aux aides et aux certificats verts. Le coût du raccordement a pesé lourd, et la chaleur, trop faible en hiver, ira plutôt à un séchoir[^lavenir-marbais] ;
- à Gozée, une ferme laitière produit plus que ses 40 000 à 50 000 kWh annuels et injecte 15 à 20 % de surplus. Selon le reportage, ce système belge coûte plutôt 250 000 €, contre plusieurs millions pour les grandes unités, et une ferme d'une cinquantaine de vaches peut s'en équiper[^rtbf] ;
- le constructeur Biolectric annonce environ 100 MWh par an pour 11 kW avec le lisier de 60 vaches (chiffre commercial)[^biolectric]. Un éleveur allemand décrit 5 à 10 minutes de suivi par jour et un entretien du moteur toutes les 800 heures[^biolectric-groven].

Rentabilité, électricité seule (calculé, unité de {{ v('microbiometh_kw', 0) }} à {{ v('microbiometh_cout_kw') }} comme à Marbais, {{ v('microbiometh_heures') }} de fonctionnement, hypothèses) :

- production : {{ v('microbiometh_production_an') }}, dont {{ v('microbiometh_autoconso_kwh') }} consommés par la ferme type et le reste injecté ;
- valeur : {{ v('microbiometh_valeur_an') }} ({{ fourchette('microbiometh_valeur_an') }} selon les scénarios) ;
- temps de retour : {{ v('microbiometh_retour_ans', 0) }} ({{ fourchette('microbiometh_retour_ans', 0) }}), sans aide, certificats verts ni chaleur, et avant entretien.

Sans soutien, l'électricité seule ne rembourse donc pas l'unité dans un délai raisonnable, même au prix de crise : la plus grande partie de la production est injectée à bas prix. Les certificats verts, l'aide à l'investissement et la valeur de la chaleur et du digestat font la différence, comme à Marbais.

**Aides.** Deux soutiens changent le calcul (voir [les aides publiques](../../aides.md#lenergie-green-amureba-certificats-verts)) :

- **certificats verts** : pour les demandes de 2025, une unité de 200 kW au plus alimentée à plus de 50 % d'effluents d'élevage reçoit {{ v('cv_biogaz_taux', 1) }}, le maximum légal[^cv-tableau] [^cv-cpma]. Au prix garanti de {{ v('cv_prix_garanti', 0) }}[^cv-rapport], l'unité type en tire {{ v('microbiometh_cv_an', 0) }} (calculé) ;
- **aide GREEN** de la Région, pour une unité de 10 à 200 kW qui consomme sur place : {{ v('green_taux_biometh', 0) }} d'un coût éligible plafonné à {{ v('green_plafond_biometh_kw') }}[^green-spw], soit {{ v('microbiometh_aide_invest', 0) }} pour l'unité type (calculé). Une unité de 10 kW au plus relève de l'AII, sur un coût simplifié de {{ v('aii_biometh_forfait') }}[^am-aii], et pas de GREEN, qui l'exclut[^green-agw].

| Calculé | Temps de retour simple |
|---|---|
| Électricité seule, sans soutien | {{ v('microbiometh_retour_ans', 1) }} ({{ fourchette('microbiometh_retour_ans', 1) }}) |
| Avec certificats verts | {{ v('microbiometh_retour_cv_ans', 1) }} ({{ fourchette('microbiometh_retour_cv_ans', 1) }}) |
| Avec certificats verts et GREEN | {{ v('microbiometh_retour_aides_ans', 1) }} ({{ fourchette('microbiometh_retour_aides_ans', 1) }}) |

Ces temps de retour ne comptent ni la chaleur, ni l'entretien, ni le coût de l'audit. Avec les deux soutiens, on retrouve les huit ans annoncés à Marbais. Le résultat dépend presque entièrement des aides, et leur niveau 2026 n'est pas connu : l'alternative reste en vague 2.

Conditions de GREEN : un investissement d'au moins {{ v('green_seuil_pme', 0) }}, une demande avant le début des travaux et, depuis 2026, un **audit ou une étude de faisabilité AMUREBA** obligatoire par un auditeur agréé[^green-agw] [^amureba-memo]. La Région subventionne cet audit à {{ v('amureba_taux_pme', 0) }} pour une PME[^amureba] ; l'accès d'une exploitation agricole à cette subvention reste à vérifier. GREEN ne se cumule pas avec une autre aide régionale pour le même programme d'investissements[^decret-2004] : le cumul avec les certificats verts n'est pas confirmé. Le taux d'octroi des certificats verts tient aussi compte de l'aide reçue à l'investissement[^am-cpma] : GREEN peut donc réduire les certificats verts (voir « À vérifier »).

Repères de coût : le SPW retenait en 2019 un coût de référence de 19 000 €/kW en dessous de 10 kW et de 8 500 €/kW de 10 à 200 kW[^spw-cpma].

Conditions :

- un troupeau d'au moins une cinquantaine de vaches[^rtbf] et du lisier frais tous les jours[^biolectric-groven] ;
- une réservation de certificats verts et un permis d'environnement ; le SPW et Valbiom publient un guide des étapes d'un projet (implantation, permis, raccordement, aides)[^spw-etapes] ;
- un usage de la chaleur toute l'année (séchoir, eau chaude), sinon elle est perdue ;
- un raccordement au réseau dont le coût est connu dès l'étude[^lavenir-marbais].

Limites : la micro-biométhanisation remplace l'électricité fossile par une électricité qui produit en continu, mais elle dépend d'un soutien public révisable. Elle réduit les émissions de méthane du stockage de lisier[^lavenir-marbais].

## Ce qui ferme la boucle

- Les toitures de la ferme produisent l'électricité de la journée. L'eau chaude, la ventilation, le pompage et la recharge des engins électriques se déplacent vers les heures de soleil (voir les fiches [tracteur diesel](../traction/tracteur-diesel.md) et [refroidissement du lait](../elevage/tank-a-lait.md)).
- Le lisier produit l'électricité de la nuit et la chaleur ; le digestat garde les éléments fertilisants et retourne aux prairies et aux cultures[^lavenir-marbais].
- La chaleur du moteur sert au séchage du fourrage, du bois ou des céréales.
- Le livre blanc de l'agrivoltaïsme propose de valoriser localement le surplus, notamment par des communautés d'énergie renouvelable[^livre-blanc] : le voisinage consomme ce que la ferme injecterait à bas prix.

## À vérifier

- Part du gaz en 2025 sur le communiqué d'Elia en français (lu en néerlandais via VFB ; Elia indique des chiffres provisoires, à consolider début 2026).
- Prix installé d'une toiture agricole de 30 à 100 kWc en Wallonie en 2026 : aucune source wallonne trouvée. Les prix de Brugel sont bruxellois et reposent sur peu d'installations au-delà de 36 kWc. À comparer avec des devis.
- Frais d'entretien réels du photovoltaïque sur une ferme (le projet retient la référence du SPW, 2,2 % par an ; Brugel retient 2,5 %).
- Production spécifique mesurée en Wallonie pour des toitures récentes (la valeur de 950 kWh/kWc citée par le guide du SPW pour une installation plein sud n'a pas pu être lue).
- Taux d'autoconsommation mesurés sur des fermes wallonnes, en lait (traite classique et robot) et en grandes cultures. Les chiffres de SAVE sont simulés et datent de 2018.
- Prix d'injection d'un contrat professionnel (plus de 10 kVA) en Wallonie en novembre 2026 ; existence d'un tarif d'injection payé au gestionnaire de réseau pour ces installations dans les tarifs 2026-2029.
- Certificats verts 2026 pour le photovoltaïque de plus de 10 kW et pour la micro-biométhanisation : taux d'octroi et durée d'octroi (régime Cpma), non publiés au 27 novembre 2026.
- Cumul de l'aide GREEN et des certificats verts pour un même méthaniseur, et effet de GREEN sur le taux d'octroi (« taux de subsidiation » du régime Cpma) : à demander au SPW Énergie.
- L'AII ne cite la biométhanisation que pour les unités de 10 kW au plus : une unité de 20 kW n'y semble pas aidée et relèverait de GREEN (lecture à confirmer auprès de l'Organisme payeur de Wallonie).
- Accès d'une exploitation agricole à la subvention AMUREBA de l'audit (règle *de minimis*) et coût réel de l'audit pour un méthaniseur.
- Addition des points « architecture verte » et « résilience économique » dans la sélection AII du photovoltaïque.
- Déduction fédérale pour investissement : cas de l'agriculteur au forfait, cumul avec GREEN.
- Coût d'entretien annuel et consommation propre d'une micro-unité (chauffage du digesteur, pompes).
- Prix d'une batterie professionnelle de 30 à 100 kWh, installée, et sa durée de vie en cycles et en années.
- Consommation réelle de l'exploitation, qui remplace l'hypothèse de {{ v('ferme_conso_elec') }}.

## Sources

[^creg]: « Tableau de bord mensuel électricité et gaz naturel, octobre 2026 », CREG, octobre 2026 : composantes du prix résidentiel en Wallonie, prix PME, Endex Power BE M+1 et TTF de juillet à septembre 2026, définition du spark spread. https://www.creg.be/sites/default/files/assets/Prices/Dashboard/tableaudebord202610.pdf
[^elia]: « Elektriciteitsmix 2025: zonneproductie stijgt met 21%… », communiqué d'Elia, 26 décembre 2025 (chiffres provisoires), version néerlandaise publiée par la VFB. https://www.vfb.be/Media/Default/pdf/20251226_Elektriciteitsmix%202025_NL.pdf
[^save]: « Slim aansturen van elektriciteit – Melkveebedrijven », brochure du projet SAVE (Boerenbond, ILVO, Inagro et partenaires), 2018 (dépôt légal D/2018/0728/20). https://www.boerenbond.be/sites/default/files/media/files/2022-08/SAVE%20brochure%20-%20Melkveebedrijven.pdf
[^rtbf]: « Un Œil sur demain : la micro méthanisation, le lisier comme source d'énergie », RTBF, 16 octobre 2022. https://www.rtbf.be/article/un-oeil-sur-demain-la-micro-methanisation-le-lisier-comme-source-d-energie-11078773
[^spw-cpma]: « Consultation publique sur les propositions de valeurs de référence 2026 … régimes d'octroi de certificats verts « Cpma » », SPW Énergie, proposition du 14 janvier 2026 (§ 22, 30 à 32). https://energie.wallonie.be/files/Soutiens%20financiers/%c3%a9lectricit%c3%a9%20verte/Consultations%20publiques%20portant%20sur%20les%20valeurs%20de%20r%c3%a9f%c3%a9rence%20du%20m%c3%a9canisme%20CPMA/2025/251006-Proposition%20nouveau%20r%c3%a9gime.pdf
[^brugel]: « Proposition relative au coefficient multiplicateur appliqué au photovoltaïque – analyse des paramètres économiques », Brugel (régulateur bruxellois), proposition 37, 23 juin 2026. https://brugel.brussels/publication/document/propositions/2026/fr/PROPOSITION-37-COEFFICIENT-MULTIPLICATEUR-PV.pdf
[^am-aii]: Arrêté ministériel du 23 février 2023 exécutant l'arrêté du Gouvernement wallon du 23 février 2023 relatif aux aides à l'installation et aux investissements (secteurs agricole et horticole), version consolidée en vigueur depuis le 1er janvier 2026 : article 5 et annexe 3, lignes 203 et 205. Wallex, consulté le 26 novembre 2026. https://wallex.wallonie.be/eli/arrete/2023/02/23/2023042748
[^aii-ni2]: « AII – Note interprétative n° 2 : énergie renouvelable professionnelle, panneaux photovoltaïques et éolienne », SPW Agriculture, Organisme payeur de Wallonie (non datée, lue le 26 novembre 2026). https://agriculture.wallonie.be/files/accueil/Aides/AII/legislation/AII_NI_2.pdf
[^cwape-prosumer]: « Note explicative relative au tarif prosumer », CWaPE, mise à jour du 18 avril 2023. https://www.cwape.be/sites/default/files/cwape-documents/2023.04.18-Note%20explicative%20tarif%20prosumer-mise%20%C3%A0%20jour.pdf
[^livre-blanc]: « Vers un cadre pour le développement de l'agrivoltaïsme en Wallonie », livre blanc, ULiège (Gembloux Agro-Bio Tech) et cosignataires, juillet 2024. https://orbi.uliege.be/bitstream/2268/335242/1/_Livre%20Blanc%20-%20Agrivoltai%cc%88sme%20en%20Wallonie.pdf
[^testachats]: « De nombreux prosumers payent pour injecter de l'électricité dans le réseau : comment éviter cela ? », Test-Achats, 28 mai 2026. https://www.test-achats.be/maison-energie/energie-renouvelable/news/cout-energie-solaire-injectee
[^cwape-batt]: « Proposition d'initiative relative au risque d'interruption du cycle de compensation », CWaPE, 26 mars 2026, avec en annexe la note « Compensation et stockage » du 12 septembre 2025. https://www.cwape.be/sites/default/files/cwape-documents/2026.03.26-0974-Proposition%20d%27initiative%20batterie%20intelligente%20vs%20compensation%20-%20avec%20annexe.pdf
[^cwape-indemn]: « Avis sur le projet d'arrêté du Gouvernement wallon relatif au régime d'indemnisation pour les limitations d'injection », CWaPE, 9 juillet 2026 (titre lu, contenu non détaillé ici). https://www.cwape.be/sites/default/files/cwape-documents/2026.07.09-0979-Avis%20sur%20projet%20AGW%20indemnisations%20prosumers.pdf
[^lavenir-batt]: « Nouveaux tarifs électricité de 2026 : pourquoi une batterie domestique intelligente peut faire la différence sur votre facture », L'Avenir, 14 janvier 2026. https://www.lavenir.net/actu/2026/01/14/batterie-domestique-et-nouveaux-tarifs-electricite-le-combo-gagnant-PESZX4B27RFPJKBZH773RKVRQM/
[^lavenir-marbais]: « Le lisier produira de l'électricité à Marbais », L'Avenir, 11 février 2024. https://www.lavenir.net/regions/brabantwallon/villers-la-ville/2024/02/11/le-lisier-produira-de-lelectricite-a-marbais-UJUVTV6G6NHHHND76NN6SMNYUQ/
[^panorama]: « Panorama de la biométhanisation en Wallonie, édition 2025 (chiffres 2024) », Valbiom, 2025, hébergé par le SPW Énergie. https://energie.wallonie.be/files/%c3%89nergies%20vertes/Bio%c3%a9nergie/Biom%c3%a9thanisation/panorama-biometh-2025.pdf
[^biolectric]: « Électricité et chaleur (CHP) », Biolectric (constructeur, site commercial), consulté le 26 novembre 2026. https://biolectric.com/fr/electricite-et-chaleur-chp/
[^biolectric-groven]: « Ferme laitière Groven : une électricité presque autonome grâce à son propre lisier », Biolectric (site commercial), 18 septembre 2026. https://biolectric.com/fr/2026/09/18/ferme-laitiere-groven-electricite-presque-autonome-grace-a-son-propre-lisier/
[^spw-etapes]: « Les étapes clés d'un projet de biométhanisation », SPW Énergie et Valbiom, septembre 2023 (sommaire lu). https://energie.wallonie.be/files/%c3%89nergies%20vertes/Bio%c3%a9nergie/Biom%c3%a9thanisation/Etapes%20cl%c3%a9s%20projets%20biometh%20sept.2023.pdf
[^aii-liste]: « Liste des investissements admissibles », SPW Agriculture, janvier 2026, consultée le 27 novembre 2026. https://agriculture.wallonie.be/files/accueil/Aides/AII/outils/Liste%20des%20investissements%20admissibles.pdf
[^agw-aii]: Arrêté du Gouvernement wallon du 23 février 2023 relatif aux aides à l'installation et aux investissements, version en vigueur depuis le 1er janvier 2026 : article 36. Wallex, consulté le 27 novembre 2026. https://wallex.wallonie.be/eli/arrete/2023/02/23/2023042313/2026/01/01
[^green-agw]: Arrêté du Gouvernement wallon du 23 mai 2024 relatif aux primes à l'investissement (aides GREEN), en vigueur le 1er janvier 2025 : articles 4 à 16 et 26. Wallex, consulté le 27 novembre 2026. https://wallex.wallonie.be/sites/wallex/contents/acts/108/108350/1.html
[^green-spw]: « Réforme des aides spécifiques à la protection de l'environnement et à l'utilisation de l'énergie », SPW Économie, Emploi, Recherche, publié le 28 novembre 2024, mis à jour le 23 janvier 2025, consulté le 27 novembre 2026. https://economie.wallonie.be/fr/home/actualites/actualites/reforme-des-aides-specifiques-a-la-protection-de-l-environnement-et-a-l-utilisation-de-l-energie.html
[^decret-2004]: Décret du 11 mars 2004 relatif aux incitants régionaux en faveur des petites ou moyennes entreprises, version en vigueur depuis le 1er janvier 2025, article 3. Wallex, consulté le 27 novembre 2026. https://wallex.wallonie.be/eli/loi-decret/2004/03/11/2004200990
[^amureba]: Arrêté du Gouvernement wallon du 1er février 2024 relatif à l'octroi de subventions à l'audit ou à l'étude dans le secteur non résidentiel (AMUREBA), annexe 5. Wallex, consulté le 27 novembre 2026. https://wallex.wallonie.be/eli/arrete/2024/02/01/2024004275
[^amureba-memo]: « Mémo Table ronde des auditeurs du 6 février 2026 », SPW Énergie, consulté le 27 novembre 2026. https://energie.wallonie.be/files/Actualit%c3%a9s/20260206_m%c3%a9mo%20Table%20ronde%20auditeurs.pdf
[^cv-cpma]: « Régime Cpma », SPW Énergie (réservation préalable, plafond de 2,5 certificats verts par MWh, exclusion du photovoltaïque de moins de 10 kW), consulté le 27 novembre 2026. https://energie.wallonie.be/home/soutiens-financiers/soutien-a-la-production-d-electricite-verte/mecanismes-de-soutien/regime-cpma.html
[^cv-tableau]: « Tableau récapitulatif des taux d'octroi forfaitaires applicables aux nouvelles installations pour les demandes introduites en 2025 », SPW Énergie, consulté le 27 novembre 2026. https://energie.wallonie.be/files/Soutiens%20financiers/%c3%a9lectricit%c3%a9%20verte/M%c3%a9canismes%20de%20soutiens/R%c3%a9gime%20CPMA/Tableau%20nouvelles%20installations%20-%20Taux%20octrois%20et%20CPMA%20des%20cat%c3%a9gories%20-%202025.pdf
[^cv-rapport]: « Rapport marché CV 2025 T3-T4 », SPW Énergie, 12 juin 2026 (prix garanti de rachat par Elia), consulté le 27 novembre 2026. https://energie.wallonie.be/files/Les%20march%c3%a9s/Les%20CV/Rapports%20trimestriels/rapport-marche-cv-2025-t3_t4.pdf
[^am-cpma]: Arrêté ministériel du 1er octobre 2025 fixant les valeurs de référence et les taux d'octroi de certificats verts (méthodologies Cpma), version consolidée au 19 juin 2026, copie non officielle de la base Justel (refli.be), consultée le 27 novembre 2026. https://refli.be/en/lex/2025008208
[^dpi-barreau]: « Nouvelle déduction pour investissement à partir de 2025 : cap sur la durabilité et le numérique », Barreau de Liège-Huy, 12 juin 2025, consulté le 27 novembre 2026. https://barreaudeliege-huy.be/fr/actualites/nouvelle-deduction-pour-investissement-partir-de-2025-cap-sur-la-durabilite-et-le
