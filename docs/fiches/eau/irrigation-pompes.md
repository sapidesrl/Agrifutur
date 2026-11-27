---
id: irrigation-pompes
titre: Pompes thermiques d'irrigation et d'abreuvement
domaine: eau
dependance_fossile: gasoil
alternatives: [Gravité, pompe à museau, bélier hydraulique, pompe solaire, électropompe d'irrigation sur réseau ou photovoltaïque]
vague_meilleure_alternative: 1
statut: relu
maj: 2026-11-27
---

# Pompes thermiques d'irrigation et d'abreuvement

!!! warning "Sources à relire"
    Les sources ont été lues sur la page d'origine le 26 novembre 2026. Les mesures de consommation des motopompes d'irrigation, les prix des pompes solaires et du bélier hydraulique et presque tous les exemples d'abreuvement sont français : aucune mesure ni aucun prix wallon n'a été trouvé. Ils sont signalés dans le texte et listés dans « À vérifier ». Les aides publiques ont été relues le 27 novembre 2026 (voir [les aides publiques](../../aides.md)).

## En bref

Deux usages de l'eau dépendent du gasoil. L'irrigation des pommes de terre et des légumes, d'abord : un enrouleur à canon est souvent alimenté par une motopompe diesel, qui brûle environ {{ v('irr_gasoil_l_m3', 2, unite=False) }} L de gasoil par m³ d'eau, soit {{ v('irr_gasoil_l_ha_mm', 1, unite=False) }} L par hectare et par millimètre (calculé à partir de mesures françaises). L'abreuvement au pâturage, ensuite, quand on apporte l'eau à la tonne tirée par un tracteur. Pour l'abreuvement, les solutions sans moteur (gravité, pompe à museau, bélier hydraulique) et la pompe solaire sont rentables aujourd'hui dans le bon contexte (vague 1) : elles économisent surtout du temps, et aucune aide publique ne les finance. Pour l'irrigation, une électropompe ne revient moins cher que le diesel que si elle tourne sur l'électricité de ses propres panneaux ; sur le réseau, le m³ coûte un peu plus cher qu'au diesel au prix de crise ({{ v('irr_ratio_reseau_gasoil', 2) }}) et nettement plus avant ; l'économie ne paie l'investissement que sur une grande surface irriguée ou au renouvellement de la pompe (vague 2).

## Comment ça marche aujourd'hui

**Irrigation.** En Wallonie, l'irrigation reste peu répandue : elle concerne 4 à 5 % des surfaces de pommes de terre, souvent avec des légumes industriels[^craw-irr]. La technique la plus courante en Belgique est l'enrouleur à canon : un tuyau en polyéthylène de 70 à 150 mm de diamètre et de 100 à 500 m de long, enroulé sur une bobine, avec un canon au bout. L'eau arrive d'un forage, d'un puits ou d'un plan d'eau. Le SPW cite deux sources d'énergie : un groupe électrogène ou le réseau[^spw-enrouleur] ; dans la plaine d'Alsace, les irrigants utilisent surtout une motopompe au gasoil[^irstea]. Le canon demande 4 à 12 bars, arrose 8 à 20 mm par heure et porte à 25 à 80 m. Un enrouleur coûte 20 000 à 40 000 € selon la longueur et le diamètre du tuyau ; la fiche du SPW indique une durée de vie de 10 à 20 ans[^spw-enrouleur]. Le SPW cite sa forte consommation d'énergie parmi ses points faibles, parce qu'il faut beaucoup de pression pour projeter l'eau[^spw-enrouleur].

Les doses se règlent au tour d'eau. Dans l'essai Patat'Up à Gembloux, en 2022, une année sèche, les pommes de terre irriguées ont reçu 9 apports de 5 à 25 mm entre mi-juin et mi-août ; l'irrigation a relevé le rendement de 15 à 20 t/ha selon la variété[^patatup]. Un millimètre sur un hectare représente 10 m³. Dans le projet DuraTechFarm du CRA-W, un passage de canon sur 516 m à 20 mm demandait environ 702 m³[^dtf].

Toute prise d'eau souterraine est soumise à déclaration ou à permis d'environnement et doit avoir un compteur dès qu'elle est équipée d'une pompe à moteur. Les volumes et les usages (code 62 pour l'irrigation, 61 pour l'abreuvement) sont déclarés chaque année. En 2023, la contribution de prélèvement allait de 0,0384 €/m³ jusqu'à 20 000 m³ à 0,1153 €/m³ au-delà de 100 000 m³ ; l'eau non potabilisable était exonérée sous 3 000 m³ par an[^spw-taxe].

**Abreuvement.** Au pâturage, on compte environ 60 L d'eau par UGB et par jour, et près de 115 L pour une vache et son veau par forte chaleur (références françaises)[^creuse-poste]. Une vache laitière boit environ 70 L par jour, et ce volume doit pouvoir être bu en 5 heures environ[^finistere]. Depuis le 1er janvier 2023, les pâtures qui bordent un cours d'eau classé doivent être clôturées en Wallonie : les dérogations qui permettaient au bétail de boire dans le ruisseau ont pris fin[^natagriwal]. Sans réseau d'eau dans la parcelle, il faut alors apporter l'eau à la tonne tirée par un tracteur, ou installer une pompe.

## Où entrent le pétrole et le gaz

- **Gasoil de la motopompe d'irrigation.** Dans des essais de six enrouleurs menés en Alsace, le groupe motopompe a consommé 0,86 à 1,26 kWh de gasoil par m³ d'eau. Seulement 18 à 22 % de l'énergie du gasoil devenait de l'énergie hydraulique en sortie de pompe ; le reste partait en chaleur[^irstea]. Avec {{ v('irr_pression_pompe', 0) }} en sortie de pompe (estimé) et {{ v('irr_rendement_motopompe_diesel', 0) }} de rendement, il faut {{ v('irr_gasoil_l_m3', 3) }} de gasoil, soit {{ v('irr_gasoil_l_ha_mm', 1) }} (calculé). Au prix de novembre 2026, cela coûte {{ v('irr_gasoil_eur_ha_mm', 2) }} ({{ fourchette('irr_gasoil_eur_ha_mm', 2) }} selon les scénarios).
- **Gasoil du tracteur.** Le tracteur déroule le tuyau de l'enrouleur à chaque position[^spw-enrouleur]. Il tire aussi la tonne à eau au pâturage.
- **Électricité du réseau.** Une électropompe consomme de l'électricité en partie produite au gaz (voir la fiche [électricité du réseau](../energie/electricite-reseau.md)).
- **Matériel.** Le tuyau des enrouleurs, les réseaux d'abreuvement et les bacs sont en polyéthylène, issu de la pétrochimie.

**Exemple : {{ v('irr_surface', 0) }} irrigués à {{ v('irr_dose_an', 0) }}** (hypothèses), soit {{ v('irr_volume_an', 0) }} et {{ v('irr_heures_an', 0) }} de pompage à {{ v('irr_debit', 0) }} (estimé) : la motopompe brûle {{ v('irr_gasoil_l_an', 0) }}, pour {{ v('irr_gasoil_eur_an', 0) }} ({{ fourchette('irr_gasoil_eur_an', 0) }}) (calculé).

## Les alternatives

Les quatre premières alternatives concernent l'abreuvement ; la cinquième, l'irrigation. Le guide « Quel abreuvoir pour quels besoins ? » des GAL du Condroz aide à choisir selon la qualité de l'eau du ruisseau, l'existence d'une source ou d'un puits, l'accès au réseau électrique, la pente, la distance et le type de bétail[^gal-choix].

Aucune des quatre solutions d'abreuvement n'est aidée en Wallonie : l'aide aux investissements agricoles (AII) ne contient ni pompe d'abreuvement, ni forage, ni réseau d'abreuvement, ni clôture de pâturage[^aii-liste]. Elles sont rentables sans aide (détail dans la pompe solaire).

### 1. Gravité (vague 1)

Quand l'eau se trouve plus haut que la pâture, elle descend seule. Une source captée remplit une cuve, et des bacs à niveau constant, munis d'un flotteur, sont alimentés par simple gravité[^belier]. Le guide wallon oriente le choix selon la pente (plus ou moins de 5 %) et la position de la prise d'eau, plus haute ou plus basse que l'abreuvoir ; l'abreuvoir gravitaire fait partie des solutions proposées[^gal-choix]. Il n'y a ni moteur ni énergie à payer : seulement le captage, les tuyaux et les bacs.

Repères de prix (exemples français) :

- un éleveur des Côtes-d'Armor a raccordé ses paddocks au réseau d'eau collectif pour près de 2 200 € HTVA de tuyaux, raccords, vannes et flotteurs (article de 2025). L'eau vient ici du réseau public, sous pression : la solution supprime la tonne, pas le pompage[^desbois] ;
- un élevage du Finistère a installé 5,7 km de tuyau de 20 mm pour 3 000 €, en 2015[^finistere].

Conditions : une source ou une réserve plus haute que les bacs, avec un débit suffisant en été ; des bacs placés à moins de 200 m du fond de la parcelle, sinon les vaches n'y vont pas boire régulièrement[^creuse-poste] ; une pression suffisante en bout de tuyau. On vise 3 à 5 bars en bout de réseau en tuyau de 19/25 mm, qui perd 1 bar tous les 100 m[^finistere].

Limites : la gravité ne convient pas à l'irrigation par aspersion. Un canon demande 4 à 12 bars[^spw-enrouleur] et une colonne d'eau donne 1 bar tous les 10 m de hauteur[^belier] : il faudrait 40 à 120 m de dénivelé (calculé). Une prise d'eau à l'émergence d'une source demande un permis d'environnement ; toute prise dans un cours d'eau demande l'autorisation de son gestionnaire[^gal-choix].

### 2. Pompe à museau (vague 1)

La vache pousse une palette avec son mufle, ce qui actionne la pompe : l'eau monte d'un ruisseau, d'une mare, d'un puits ou d'une source jusqu'au bol. Les GAL du Condroz l'ont diffusée dans le cadre du projet wallon Coopération Berges, avec une fiche de montage. Une pompe suffit pour 10 à 15 bovins ou chevaux, remonte l'eau sur 7 m de hauteur ou 70 m de longueur au plus, et coûte environ 40 € par UGB, montage compris et TVAC[^gal-pam]. Les animaux ont besoin de 3 à 4 jours pour s'y habituer ; un modèle existe pour les veaux. Elle ne suffit pas pour des vaches laitières en production[^gal-pam]. Une seule ou deux bêtes peuvent boire en même temps[^solaire2007].

La pompe à museau ne consomme aucune énergie achetée et coûte peu : c'est la solution la plus simple pour un petit lot de bovins allaitants ou de génisses le long d'un cours d'eau clôturé.

### 3. Bélier hydraulique (vague 1)

Le bélier utilise l'énergie d'une petite chute d'eau pour en remonter une partie beaucoup plus haut. L'eau descend dans une conduite rigide, un clapet se ferme brusquement, et le coup de bélier pousse une partie de l'eau vers le haut ; le reste retourne au ruisseau[^belier].

Exemple (Creuse, France, 2020) : deux éleveurs alimentent une citerne de 3 000 L en haut d'une colline avec un bélier placé sous une source. La conduite motrice fait 65 m pour 12 m de chute ; le bélier reçoit 16 L/min et en remonte 3,5 L/min, soit 5 000 L par jour, sur 380 m et 65 m de dénivelé. Les bacs des pâtures se remplissent ensuite par gravité. L'installation, faite par les éleveurs avec un ferronnier, a coûté 6 000 € de fournitures (2,5 km de tuyaux, citerne, fosse, location de matériel), main-d'œuvre non comptée. L'unique fabricant français vendait alors un bélier autour de 3 000 €. L'entretien se limite à deux clapets, 45 € par an. Elle fonctionne depuis dix ans, y compris pendant la sécheresse de 2019[^belier]. En 2007, un fabricant annonçait des béliers dès 687 € et une durée de vie d'au moins 30 ans, tout en reconnaissant qu'ils sont parfois difficiles à régler[^solaire2007].

Conditions : une source ou un ruisseau au débit régulier même en été, et une chute de quelques mètres en aval de la prise ; une conduite motrice rigide (acier ou fonte) de 3 à 5 fois la hauteur de chute ; une installation parfaitement étanche, car la moindre entrée d'air la dérègle[^belier].

Limites : le bélier ne remonte qu'une petite partie de l'eau qu'il reçoit (moins d'un quart dans l'exemple). Il convient au relief ardennais ou condrusien, pas aux plateaux sans source. Aucun exemple wallon récent n'a été trouvé (voir « À vérifier »).

### 4. Pompe solaire (vague 1)

Des panneaux photovoltaïques alimentent une pompe immergée dans un puits, un forage ou un cours d'eau, ou une pompe de surface. L'eau part vers une cuve en hauteur ou directement vers des bacs à flotteur. Les petits kits d'abreuvement débitent 160 à 1 400 L/h selon les modèles, assez pour 20 à 30 bovins[^solaire2007]. Un kit récent sans batterie, avec un panneau de 305 W, annonce jusqu'à 1 200 L/h en plein soleil (chiffre du constructeur) ; il faut alors une réserve d'eau pour les jours couverts[^buvette]. D'autres kits stockent l'énergie dans une batterie de 12 V[^solaire2007].

Exemple (Creuse, France, 2023) : un élevage de 95 vaches allaitantes a creusé un puits filtrant à 700 m du bâtiment, trop loin pour tirer un câble électrique à un prix raisonnable. Quatre panneaux alimentent sans batterie une pompe immergée de 600 W, 4,5 m³/h et 8 bars. Elle remonte l'eau de 25 m jusqu'à une cuve de 5 000 L au bâtiment et alimente deux îlots de prairies, soit 60 à 70 vaches suitées. La pompe ne tourne ni la nuit ni par temps très couvert, mais elle fonctionne toute l'année et le gel n'a pas posé de problème. L'investissement total a atteint 12 000 €, dont environ 3 000 € pour le puits, avec 2 500 € d'aide régionale et un mois de travail des éleveurs[^picaud]. La chambre d'agriculture note un gain de temps et de carburant, et moins de risque de griller la pompe lors des orages qu'avec une pompe sur le réseau[^picaud-ca].

**Comparaison avec la tonne à eau** (hypothèses : {{ v('abreuv_ugb', 0) }}, {{ v('abreuv_jours', 0) }}, {{ v('tonne_heures_jour', 0) }} de tracteur et de tonne, tracteur à {{ v('tracteur_compact_conso_gasoil', 0) }} ; sourcés : {{ v('abreuv_l_ugb_jour', 0) }} et main-d'œuvre à {{ v('main_oeuvre_eur_h', 0) }}) :

| Calculé | Valeur |
|---|---|
| Eau bue au pâturage | {{ v('abreuv_volume_an', 0) }} |
| Heures de tonne | {{ v('tonne_heures_an', 0) }} |
| Gasoil | {{ v('tonne_gasoil_l_an', 0) }}, soit {{ v('tonne_gasoil_eur_an', 0) }} ({{ fourchette('tonne_gasoil_eur_an', 0) }}) |
| Gasoil et main-d'œuvre | {{ v('tonne_cout_an', 0) }} ({{ fourchette('tonne_cout_an', 0) }}) |
| Temps de retour de l'installation de l'exemple ({{ v('abreuv_solaire_invest', 0) }}), sans aide | {{ v('abreuv_solaire_retour_ans', 1) }} ({{ fourchette('abreuv_solaire_retour_ans', 1) }}) |
| Même calcul sur le seul gasoil | {{ v('abreuv_solaire_retour_gasoil_ans', 1) }} ({{ fourchette('abreuv_solaire_retour_gasoil_ans', 1) }}) |

Le calcul ne compte ni l'usure du tracteur et de la tonne, ni l'entretien de la pompe. Le temps de travail fait l'essentiel du gain. Sur le seul gasoil, l'installation de l'exemple se rembourse en {{ v('abreuv_solaire_retour_gasoil_ans', 1) }} au prix de crise, mais en {{ v('abreuv_solaire_retour_gasoil_ans', 1, scenario='bas') }} au prix de février 2026. Les références de terrain vont dans le même sens : la chambre d'agriculture de la Creuse compte 33 € par heure de tonne (main-d'œuvre, tracteur, tonne et carburant, hors eau, 2021)[^creuse-poste], et un élevage du Finistère estimait sa tonne à 4 300 € par an (2015). Ce dernier a remboursé en trois ans un forage et un réseau de 10 700 €[^finistere].

Conditions : un point d'eau (puits, forage, source, cours d'eau) dans ou près de la parcelle ; des panneaux à l'écart de l'ombre[^solaire2007] ; une cuve ou des bacs assez grands pour passer la nuit et les jours couverts[^buvette] ; une analyse régulière de l'eau d'un puits ou d'une source privée[^finistere].

**Aides : aucune n'est accessible.** L'exemple de la Creuse a reçu une aide régionale française ; rien d'équivalent n'existe en Wallonie en 2026 :

- l'AII retient un coût simplifié de 6 050 € pour un tonneau à eau[^am-aii], mais sa liste de 2026 ne contient ni pompe solaire, ni forage, ni réseau d'abreuvement ou d'irrigation, ni clôture de pâturage[^aii-liste]. L'aide va donc à la tonne, pas à ce qui la remplace ;
- l'aide GREEN de la Région exclut le photovoltaïque[^green-agw], et un kit d'abreuvement reste loin de son seuil de {{ v('green_seuil_pme', 0) }}[^green-agw] ;
- les investissements non productifs, payés à 100 % des forfaits jusqu'à {{ v('inp_plafond_eur', 0) }} par bénéficiaire sur 2023-2027, ne visent que des ouvrages contre l'érosion et le ruissellement (fascines, noues, mares tampons, bassins), pas l'abreuvement ni les clôtures[^inp] [^am-aii].

Le temps de retour calculé plus haut est donc aussi le temps de retour réel. La vague 1 tient sans aide.

Limites : la pompe solaire remplace le gasoil de la tonne, mais ajoute des panneaux, une électronique et parfois une batterie. Aucun prix belge de kit d'abreuvement solaire n'a été trouvé.

### 5. Électropompe d'irrigation sur réseau ou photovoltaïque (vague 2)

**D'abord, pomper moins d'eau et à moins de pression.** L'énergie suit le volume et la pression. Dans le projet DuraTechFarm, les chevauchements entre passages de canon ont apporté 11,3 à 15,8 m³/ha de trop par tour d'eau ; une coupure de section, compatible avec le matériel existant, aurait économisé 124 à 174 m³ par tour sur une parcelle d'environ 10 ha[^dtf]. Le CRA-W juge la coupure de section simple à mettre en œuvre, avec des bénéfices immédiats, et voit dans le pilotage par bilan hydrique une base robuste et accessible pour décider quand irriguer[^dtf-synth]. En France, une rampe ou un pivot demande 6 à 7 bars, contre 11 à 12 bars pour un canon sur enrouleur[^arvalis].

**Ensuite, changer de moteur.** Une pompe neuve a un rendement de plus de 75 % ; un moteur immergé, 88 à 89 % ; un moteur de surface récent, jusqu'à 95 %[^rovatti]. Pompe et moteur ensemble transforment donc environ deux tiers de l'électricité en énergie hydraulique (calculé). Une pompe fatiguée peut tomber à 50 %[^arvalis]. Pour le même enrouleur, il faut {{ v('irr_elec_kwh_m3', 2) }} d'électricité (calculé avec {{ v('irr_rendement_electropompe', 0) }}, estimé), contre {{ v('irr_gasoil_kwh_m3', 2) }} de gasoil. Sur le terrain, Arvalis mesure plutôt 0,6 à 1 kWh/m³ pour un enrouleur en pompage de surface, et environ 0,4 kWh/m³ pour un pivot[^arvalis] : pressions plus fortes, pompes usées, hauteur d'aspiration.

Coût de l'énergie par hectare et par mm (calculé) :

| Énergie | Novembre 2026 | Scénarios bas à haut |
|---|---|---|
| Motopompe diesel | {{ v('irr_gasoil_eur_ha_mm', 2) }} | {{ fourchette('irr_gasoil_eur_ha_mm', 2) }} |
| Électropompe sur réseau | {{ v('irr_reseau_eur_ha_mm', 2) }} | {{ fourchette('irr_reseau_eur_ha_mm', 2) }} |
| Électropompe sur photovoltaïque | {{ v('irr_pv_eur_ha_mm', 2) }} | identique |

Sur le réseau, le m³ coûte {{ v('irr_ratio_reseau_gasoil', 2) }} celui du diesel au prix de crise, et {{ v('irr_ratio_reseau_gasoil', 2, scenario='bas') }} au prix de février 2026 : passer au réseau ne paie pas par l'énergie seule. Le gain vient du photovoltaïque. L'irrigation tombe en été, quand les panneaux produisent le plus. Sur l'exemple de {{ v('irr_surface', 0) }} à {{ v('irr_dose_an', 0) }}, une électropompe consomme {{ v('irr_elec_kwh_an', 0) }}. Sur photovoltaïque, l'économie d'énergie atteint {{ v('irr_economie_pv_an', 0) }} face au diesel ({{ fourchette('irr_economie_pv_an', 0) }}) (calculé, hors investissement).

Conditions :

- un forage ou un puits proche de la ferme ou d'un raccordement électrique. L'enrouleur de l'exemple appelle environ {{ v('irr_puissance_elec_kw', 0) }} (calculé) pendant {{ v('irr_heures_an', 0) }} : une toiture de la ferme peut couvrir cette puissance en journée, mais pas un forage au milieu des champs ;
- un pompage en journée, ou une réserve d'eau qui se remplit en journée ;
- un investissement qui se compte en dizaines de milliers d'euros : un agriculteur du Loiret a payé 40 000 € en 2024 une pompe immergée à 40 m avec variateur de fréquence, contre 32 000 € en 2017. Le variateur règle le débit de la pompe sur le besoin de l'enrouleur et a réduit sa consommation d'électricité[^delorme].

Aides : l'AII ne finance ni la pompe, ni le forage, ni l'armoire électrique[^aii-liste]. Elle finance en revanche les panneaux photovoltaïques qui alimentent la pompe, à {{ v('aii_taux_pv', 0) }} d'un coût simplifié de {{ v('aii_pv_forfait') }} pour un agriculteur sans autre majoration (calculé), et une installation de plus de 10 kW peut recevoir des certificats verts (voir la fiche [électricité du réseau](../energie/electricite-reseau.md))[^am-aii]. Ces aides allègent la part solaire, pas la pompe : l'électropompe reste en vague 2.

Limites : l'économie annuelle d'une petite surface irriguée reste modeste face au prix d'un raccordement, d'une pompe et d'une armoire électrique. Sur l'exemple de {{ v('irr_surface', 0) }}, elle ne rembourserait pas une pompe du prix de celle du Loiret en moins de plusieurs dizaines d'années. Le passage à l'électrique se justifie surtout quand on renouvelle la pompe, que le forage est près de la ferme et que la toiture produit déjà. Des panneaux au sol au bord du champ sont dérogatoires au CoDT en zone agricole (voir la fiche [électricité du réseau](../energie/electricite-reseau.md)). Les pompages longs, de nuit, restent sur le réseau ou sur le diesel.

## Ce qui ferme la boucle

- **Garder l'eau dans le sol.** Le SPW conseille de maximiser d'abord la capacité du sol à stocker l'eau avant de compter sur l'irrigation, qui ne convient pas à tous les contextes[^spw-resil]. Dans les essais du CRA-W de 2009 et 2010, les diguettes entre les buttes de pommes de terre ont réduit le ruissellement de 70 % en moyenne ; 10 000 diguettes par hectare retiennent environ 300 m³, l'équivalent d'une pluie de 30 mm[^spw-resil]. Les ouvrages qui retiennent l'eau et la terre (fascines, noues, mares tampons, bassins de rétention) sont payés à 100 % des forfaits par l'aide aux investissements non productifs, jusqu'à {{ v('inp_plafond_eur', 0) }} par bénéficiaire sur 2023-2027, avec une étude hydrologique préalable[^inp].
- **Choisir des variétés qui supportent la sécheresse.** Dans l'essai Patat'Up, Sevilla et Fontane ont le moins perdu de rendement sans irrigation, la variété hâtive Camméo le plus[^patatup].
- **Utiliser l'eau sur place.** Sources, puits peu profonds et eau de pluie des toitures alimentent les bacs par gravité ou par une pompe solaire, sans tonne ni tracteur. L'eau de puits qui a refroidi le lait dans le pré-refroidisseur part ensuite à l'abreuvement (voir la fiche [refroidissement du lait](../elevage/tank-a-lait.md)).
- **Protéger les cours d'eau.** La clôture des berges, avec un cordon rivulaire, retient l'eau et stabilise les berges ; en Wallonie, une MAEC prévoit 470 € par hectare et par an pour un cordon rivulaire en prairie, sur 20 m de large (montant valable à partir du 1er janvier 2023)[^natagriwal].
- **Pomper avec le soleil de la ferme.** L'irrigation tombe en plein été : les panneaux des toitures, qui produisent alors plus que la ferme ne consomme, peuvent la couvrir en journée (voir la fiche [électricité du réseau](../energie/electricite-reseau.md)).

## À vérifier

- Surfaces irriguées et volumes prélevés pour l'irrigation en Wallonie (recensement agricole 2020 de Statbel, déclarations de prélèvement au SPW) : seul le chiffre de 4 à 5 % des surfaces de pommes de terre (CRA-W, 2024) a été trouvé.
- Part des enrouleurs alimentés par une motopompe diesel, par un groupe électrogène ou par le réseau en Wallonie.
- Consommation de gasoil mesurée sur des motopompes wallonnes (le projet retient des mesures françaises de 2010) et dose annuelle réelle des cultures irriguées (le projet retient {{ v('irr_dose_an', 0) }}, hypothèse).
- Consommation électrique mesurée des électropompes d'irrigation en Wallonie, en kWh/m³ (le calcul donne {{ v('irr_elec_kwh_m3', 2) }} ; Arvalis mesure 0,6 à 1 kWh/m³ en France).
- Coût d'un raccordement électrique pour un forage d'irrigation, et prix d'une électropompe avec armoire et variateur en Belgique.
- Prix belges de kits de pompage solaire pour l'abreuvement, de pompes à museau (la fiche des GAL du Condroz n'est pas datée) et de béliers hydrauliques ; exemples wallons de béliers en service.
- Temps réel passé à la tonne à eau sur une exploitation wallonne (le projet retient {{ v('tonne_heures_jour', 0) }}, hypothèse) et consommation d'un tracteur au transport de la tonne.
- Aides des contrats de rivière, de Natagriwal, du réseau Natura 2000 ou des communes aux points d'abreuvement et aux clôtures de berges : aucune n'a été trouvée (l'AII, GREEN et les investissements non productifs ne les couvrent pas).
- Taux 2026 de la contribution de prélèvement sur les prises d'eau souterraine (la notice lue donne les taux de 2023).

## Sources

[^craw-irr]: Tourneur D., Limbourg Q., Artois J., « La pomme de terre en Wallonie – L'irrigation mesurée : les nouvelles technologies et l'optimisation de la ressource en eau », présentation, CRA-W, 12 novembre 2024. https://cra.wallonie.be/uploads/2024/11/5-irrigation.pdf
[^spw-enrouleur]: « Canon enrouleur », fiche technique d'irrigation, SPW Agriculture, Ressources naturelles et Environnement, août 2023. https://agriculture.wallonie.be/files/accueil/Recherche%20et%20d%c3%a9veloppement/Secheresse/irrigation/202308%20-%20CanonEnrouleur.pdf
[^patatup]: Ben Abdallah F., Decruyenaere F., Berthet V., « Vers la production d'une pomme de terre bas intrants : résultats de la première année d'essai (suite) », Fiwap-info, 2023 (projet Patat'Up, essai 2022 à Gembloux), mis en ligne par le CRA-W. https://www.cra.wallonie.be/uploads/2024/04/fi178-article-eau-patat-up.pdf
[^dtf]: « Rapport de mise en place et d'évaluation d'une solution (optimisation de l'irrigation dans l'espace) », projet DuraTechFarm, CRA-W, 29 juin 2026. https://www.cra.wallonie.be/uploads/2026/06/dtf-optimisation-irrigation-espace-290626.pdf
[^dtf-synth]: « Rapport de synthèse du projet DuraTechFarm (D65-7390 / D65-7452) », CRA-W, UCLouvain et WalDigiFarm, 29 juin 2026. https://www.cra.wallonie.be/uploads/2026/06/rapport-de-synthese-dtf-290626-.pdf
[^spw-taxe]: « Notice explicative de la formule de déclaration des volumes et des usages de l'eau prélevée en 2023 – secteur agricole », SPW Agriculture, Ressources naturelles et Environnement, 2024. https://demarchesenvironnement.wallonie.be/files/138327-taxes-prelevement-eau/Declaration-usage-eau-prelevee-notice-agricole-2022
[^irstea]: Huet L., Granier J.-M., Molle B., « Influence de la stratégie d'équipement sur la demande énergétique en irrigation par canon enrouleur », rapport technique, Irstea, 2010 (essais du 17 septembre 2010, Bas-Rhin ; tableaux 2 à 4). https://hal.inrae.fr/hal-02595057/document
[^creuse-poste]: « L'abreuvement, un poste clé », Réussir Agriculture Massif central, 23 juillet 2021 (conseils de la chambre d'agriculture de la Creuse). https://www.reussir.fr/agriculture-massif-central/labreuvement-un-poste-cle
[^finistere]: « Abreuvement au pâturage : ne vous laissez pas déborder », Réussir Lait, 11 juin 2015. https://www.reussir.fr/lait/abreuvement-au-paturage-ne-vous-laissez-pas-deborder
[^natagriwal]: « Des haies, une réponse naturelle à l'obligation de clôture », Natagriwal asbl, article publié par la commune de Jalhay, janvier 2023. https://www.jalhay.be/wp-content/uploads/2023/01/Article_cloturescoursdeau_Natagriwal_DEF86.pdf
[^gal-choix]: « Quel abreuvoir pour quels besoins ? », fiche technique n° 4 du projet Coopération Berges, GAL Pays des Tiges et Chavées, GAL Saveurs et Patrimoine en Vrai Condroz, GAL Pays des Condruses et Contrat de rivière Ourthe (projet Riparia), non datée, mise en ligne par le Contrat de rivière Sambre en octobre 2022. https://www.crsambre.be/wp-content/uploads/2022/10/Annexe-1-Quel-abreuvoir-pour-quels-besoins.pdf
[^gal-pam]: « La pompe à museau », fiche technique n° 1 du projet Coopération Berges, mêmes GAL, non datée, mise en ligne par le Contrat de rivière Sambre en octobre 2022. https://www.crsambre.be/wp-content/uploads/2022/10/Fiche_PAM.pdf
[^belier]: « Un bélier hydraulique pour remplir les abreuvoirs », Réussir, 13 janvier 2020. https://www.reussir.fr/un-belier-hydraulique-pour-remplir-les-abreuvoirs
[^solaire2007]: « L'énergie solaire se développe plus que l'éolien ou d'autres systèmes autonomes », Réussir Bovins viande, 19 avril 2007 (référence ancienne). https://www.reussir.fr/bovins-viande/lenergie-solaire-se-developpe-plus-que-leolien-ou-dautres-systemes-autonomes
[^buvette]: « La Buvette – Un kit de pompage solaire pour l'abreuvement des grands troupeaux », Réussir Machinisme, 16 août 2024 (présentation d'un produit). https://www.reussir.fr/machinisme/la-buvette-un-kit-de-pompage-solaire-pour-labreuvement-des-grands-troupeaux
[^picaud]: « Abreuvement au pâturage : « Nous avons opté pour une pompe solaire sur un puits filtrant » », Réussir Bovins viande, 6 juin 2023. https://www.reussir.fr/bovins-viande/une-pompe-solaire-sur-un-puits-filtrant-pour-gagner-en-autonomie-pour-leau-dabreuvement
[^picaud-ca]: « [Retour d'expérience] Pompage avec système solaire : une solution pour l'abreuvement aux champs et aux bâtiments », Pleinchamp (chambre d'agriculture de la Creuse), 23 novembre 2022. https://www.pleinchamp.com/actualite/retour-d-experience-pompage-avec-systeme-solaire-une-solution-pour-l-abreuvement-aux-champs-et-aux-batiments
[^desbois]: « Abreuvement au pâturage : « Un gain de temps avec mon réseau d'eau, comparé à la tonne à eau » », Réussir Lait, 10 mai 2025. https://www.reussir.fr/lait/abreuvement-au-paturage-un-gain-de-temps-avec-mon-reseau-deau-compare-la-tonne-eau
[^am-aii]: Arrêté ministériel du 23 février 2023 exécutant l'arrêté du Gouvernement wallon du 23 février 2023 relatif aux aides à l'installation et aux investissements (secteurs agricole et horticole), version consolidée en vigueur depuis le 1er janvier 2026 : article 5, annexe 3 (lignes « Tonneau à eau » et « panneaux photovoltaïques ») et annexe 4 (investissements non productifs). Wallex, consulté le 27 novembre 2026. https://wallex.wallonie.be/eli/arrete/2023/02/23/2023042748
[^arvalis]: « Irrigation : réduire sa facture électrique en agissant sur la pompe », Réussir Grandes cultures, 7 mai 2024 (avec Arvalis et le constructeur Rovatti). https://www.reussir.fr/grandes-cultures/irrigation-reduire-sa-facture-electrique-en-agissant-sur-la-pompe
[^rovatti]: « Irrigation – Des rendements supérieurs pour les pompes de surface », Réussir Grandes cultures, 14 mai 2024. https://www.reussir.fr/grandes-cultures/des-rendements-superieurs-pour-les-pompes-de-surface
[^delorme]: « J'ai réduit ma facture d'électricité en équipant ma pompe d'irrigation d'un variateur de fréquence », Réussir Machinisme, 9 mai 2024. https://www.reussir.fr/machinisme/jai-reduit-ma-facture-delectricite-en-equipant-ma-pompe-dirrigation-dun-variateur-de-frequence
[^spw-resil]: Nihoul P., Courtois P., Desmet F., Pochet P., « Rendre ses sols plus résilients face à la sécheresse en grandes cultures », SPW Agriculture, Ressources naturelles et Environnement, Direction de la Recherche et du Développement (non daté, cite des travaux de 2024 ; consulté le 26 novembre 2026). https://agriculture.wallonie.be/files/accueil/Recherche%20et%20d%c3%a9veloppement/Secheresse/r%c3%a9silience%20grande%20culture/Rendre%20ses%20sols%20plus%20r%c3%a9silients%20face%20%c3%a0%20la%20s%c3%a9cheresse%20en%20grandes%20cultures-1.pdf
[^aii-liste]: « Liste des investissements admissibles », SPW Agriculture, janvier 2026, consultée le 27 novembre 2026. https://agriculture.wallonie.be/files/accueil/Aides/AII/outils/Liste%20des%20investissements%20admissibles.pdf
[^green-agw]: Arrêté du Gouvernement wallon du 23 mai 2024 relatif aux primes à l'investissement (aides GREEN), en vigueur le 1er janvier 2025 : articles 10 et 11. Wallex, consulté le 27 novembre 2026. https://wallex.wallonie.be/sites/wallex/contents/acts/108/108350/1.html
[^inp]: « Aides aux investissements non-productifs dans les exploitations agricoles », Portail de l'agriculture wallonne, page modifiée le 17 avril 2026, consultée le 27 novembre 2026. https://agriculture.wallonie.be/home/aides/pac-2023-2027-description-des-interventions/aides-aux-investissements/aides-aux-investissements-non-productifs-dans-les-exploitations-agricoles.html
