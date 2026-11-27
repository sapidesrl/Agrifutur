---
id: sechage-grains
titre: Séchage des grains au gaz ou au fioul
domaine: énergie
dependance_fossile: gaz; fioul
alternatives: [Moins d'eau à retirer (variété, récolte, maïs grain humide), chaudière biomasse, chaleur d'un méthaniseur, air ambiant ou chauffé au solaire, pompe à chaleur]
vague_meilleure_alternative: 1
statut: relu
maj: 2026-11-27
---

# Séchage des grains au gaz ou au fioul

!!! warning "Sources à compléter"
    Les sources citées ont été lues sur la page d'origine le 26 novembre 2026. Plusieurs chiffres techniques viennent de France ou de l'Ontario (Canada), faute de source belge récente : consommation d'un séchoir, coût d'une chaudière biomasse, pompe à chaleur. Le barème de séchage de la FEGRA (négociants belges) est réservé à ses membres et n'a pas pu être lu. Les aides publiques ont été relues le 27 novembre 2026 (voir [les aides publiques](../../aides.md)).

## En bref

Le maïs grain se récolte en Belgique entre 25 et 38 % d'humidité et doit être ramené à 15 % pour se conserver[^cipf] : le séchoir chauffe l'air avec du propane, du gaz naturel ou du fioul. Pour un maïs récolté à {{ v('mais_humidite_recolte', 0) }} (hypothèse), l'énergie seule coûte {{ v('sechage_propane_eur_t', 0, unite=False) }} € par tonne humide au propane, hors amortissement et main-d'œuvre (calculé). Le moyen le plus simple d'éviter ce fossile est de retirer moins d'eau : variété plus précoce, et pour un éleveur, maïs grain humide conservé sans séchage (vague 1). Pour le grain à vendre sec, l'énergie des plaquettes revient à {{ v('sechage_plaquettes_eur_t', 0, unite=False) }} € par tonne (calculé), et la chaleur d'un méthaniseur est souvent perdue en automne. Ces deux solutions demandent un gros investissement qui ne se justifie qu'avec un gros tonnage, souvent en collectif, même avec l'aide régionale GREEN de {{ v('green_taux_chaudiere_biomasse', 0) }} pour la chaudière (vague 2).

## Comment ça marche aujourd'hui

**Quelles cultures ?** Surtout le maïs grain. En Belgique, il se récolte à 25 % d'humidité dans les meilleures conditions et jusqu'à 38 % dans les moins favorables ; en 2007, année froide, il sortait du champ à 30 à 35 %[^cipf]. Les céréales d'été (froment, escourgeon) et le colza se récoltent normalement assez secs ; on ne les sèche que les années humides, sur quelques points (voir le barème plus bas).

**Combien d'eau ?** 100 kg de maïs à 30 % donnent 82,35 kg de maïs à 15 % : chaque point d'humidité au-dessus de 15 % retire en théorie 1,176 kg d'eau par 100 kg livrés[^cipf]. En pratique, on récupère plutôt 78,5 à 79,75 kg de grain sec, car le séchage et la manutention ajoutent des pertes (poussières, brisures)[^cipf]. Pour un maïs à {{ v('mais_humidite_recolte', 0) }} (hypothèse), il faut retirer {{ v('sechage_eau_t', 0, unite=False) }} kg d'eau par tonne humide (calculé).

**Combien d'énergie ?** Un séchoir à air chaud consomme environ 20 L de fioul ou 16 kg de gaz naturel pour sécher une tonne de maïs de 32 à 15 % (chiffres français)[^civam]. Le fournisseur de gaz Antargaz compte 0,08 kg de propane par kg d'eau évaporée[^reussir-bois]. En Ontario, un séchoir à flux croisés, sans récupération de chaleur, consomme 860 000 kJ (34 L de propane) pour retirer 134 kg d'eau ; un séchoir à flux mixte consomme en moyenne 30 % de moins[^omafra-energie]. La fiche retient {{ v('sechage_kwh_kg_eau', 1) }} (estimé à partir de ces chiffres), soit {{ v('sechage_kwh_t', 0, unite=False) }} kWh par tonne de maïs humide et {{ v('sechage_kwh_t_point', 1) }} (calculé). Le ventilateur du séchoir ajoute environ 5 kWh d'électricité par tonne[^omafra-energie].

**Qui sèche ?** Le plus souvent le négociant ou la coopérative qui reçoit le grain. En Belgique, les négociants appliquent des barèmes qui retirent du prix l'eau, les pertes et les frais de séchage[^cipf]. Quelques exploitations ou groupes d'agriculteurs ont leur propre séchoir.

**Combien ça coûte ?**

- *Maïs grain* : la FEGRA (fédération des négociants belges) publie chaque jour un prix indicatif du maïs humide à 30 %. Le 26 novembre 2026, il valait 167 € la tonne, à corriger de 6 € par tonne et par point d'humidité en plus ou en moins[^fegra]. Cette correction paie à la fois l'eau retirée, les pertes et le séchage (lecture de ce projet). En 2007, le barème des négociants (Synagra) facturait 21,40 € par tonne humide à 25 %, 28,50 € à 30 % et 38,06 € à 35 %, et un négociant moins cher 16,96 à 24,51 € pour les mêmes humidités[^cipf].
- *Céréales* : les organisations agricoles (Agrofront : ABS, Boerenbond, FWA) et les négociants (FEGRA) négocient chaque printemps les frais de séchage des céréales. Les repères de l'Agrofront pour 2025 vont de 2,36 € par tonne pour un grain à 15,6-16 % à 6,72 € à 17 % et 9,40 € à 17,3 %[^boerenbond-2025]. En 2022, la FEGRA a doublé les frais de séchage après la hausse de l'énergie ; en 2023, elle ne les a baissés que de 16,5 % alors que l'énergie avait baissé de 44 %[^boerenbond-2025]. Il n'y a eu d'accord ni en 2025 ni en 2026 : chacun doit négocier ses frais de séchage avec son négociant[^boerenbond-2025] [^boerenbond-2026].

Coût de l'énergie seule pour une tonne de maïs humide séchée de {{ v('sechage_points', 0, unite=False) }} points (calculé, HTVA, à rendement égal) :

| Combustible | Coût actuel | Fourchette des scénarios | Par point (actuel) |
|---|---|---|---|
| Propane en vrac | {{ v('sechage_propane_eur_t') }} | {{ fourchette('sechage_propane_eur_t') }} | {{ v('sechage_propane_eur_t_point', 2) }} |
| Mazout (fioul) | {{ v('sechage_mazout_eur_t') }} | {{ fourchette('sechage_mazout_eur_t') }} | |

Le propane en vrac (au moins 2 000 L) coûtait en moyenne {{ v('propane_vrac_tvac', 3) }} TVAC du 1er au 26 novembre 2026, contre {{ v('propane_vrac_tvac', 3, scenario='bas') }} en février 2026 (prix maximums officiels, voir [les hypothèses](../../hypotheses.md)). Le propane a beaucoup moins augmenté que le mazout. Au prix d'avant-crise, le séchage au mazout coûtait {{ v('sechage_mazout_eur_t', scenario='bas') }}, contre {{ v('sechage_propane_eur_t', scenario='bas') }} au propane ; aujourd'hui, les deux se valent (calculé). Les grands séchoirs au gaz naturel paient un autre prix, non étudié ici.

## Où entrent le pétrole et le gaz

- **Combustible** : propane (issu du raffinage du pétrole et du traitement du gaz naturel), gaz naturel ou fioul. C'est de loin le premier poste : en Ontario, le séchage représente plus de 30 % de l'énergie utilisée pour cultiver et récolter le grain[^omafra-air].
- **Électricité** des ventilateurs, de la manutention et de la ventilation de refroidissement en cellule, en partie produite au gaz.
- **Transport** : le grain humide part au séchoir avec son eau, soit {{ v('sechage_eau_t', 0, unite=False) }} kg d'eau en plus par tonne transportée (calculé).
- **Coût caché** : quand l'énergie flambe, les frais de séchage suivent vite, mais redescendent lentement (voir les frais de 2022 et 2023 plus haut).

## Les alternatives

### 1. Retirer moins d'eau (vague 1)

Le point d'humidité le moins cher est celui qu'on ne retire pas.

- **Variété adaptée** : en Basse et Moyenne Belgique, le maïs grain à sécher se conduit au mieux avec des variétés d'indice FAO 200 à 230, semées tôt ; les indices plus tardifs (jusqu'à 250-260) sont réservés au maïs grain humide[^cipf]. Chaque point gagné à la récolte économise {{ v('sechage_propane_eur_t_point', 2, unite=False) }} € d'énergie par tonne au propane (calculé), plus la part du point dans le barème du négociant. Il faut comparer cette économie avec le rendement perdu par une variété plus précoce (à chiffrer avec les essais variétaux belges, voir « À vérifier »).
- **Date de récolte** : laisser sécher le maïs sur pied économise du séchage, mais augmente le risque de mycotoxines quand l'année est favorable aux fusarioses. Arvalis conseille d'éviter les récoltes tardives, qu'il situe au-delà du 25 octobre au 5 novembre selon les régions de France[^arvalis-sobriete].
- **Maïs grain humide pour ses animaux** : récolté vers 35 % d'humidité, broyé et ensilé, ou conservé en grain entier à l'abri de l'air, il se garde un an et demi sans aucun séchage. Le Réseau des CIVAM normands chiffre l'économie à environ 173 € par hectare en gaz naturel ou 212 € en fioul, pour 10 t/ha à 35 % (prix français, 2024)[^civam]. Le CIPF cite le grain humide et l'épi broyé (MKS, CCM) parmi les trois formes de récolte du maïs grain en Belgique[^cipf].

Limites : le maïs grain humide ne sert qu'à l'élevage de la ferme ou d'un voisin, il ne se vend pas au négoce. Il déplace une partie de la dépendance vers le plastique (silo boudin, bâches, poches de big bags)[^civam] (voir la fiche [plastiques agricoles](../materiaux/plastiques-agricoles.md)). Enfin, un maïs grain sec n'est pas parfaitement stable à 15 % : il faut le refroidir vite par ventilation[^arvalis-ventilation].

### 2. Chaudière biomasse (vague 2)

Un générateur d'air chaud brûle des plaquettes de bois (ou des rafles de maïs, des granulés) et chauffe l'air du séchoir par un échangeur.

Coût de l'énergie pour une tonne de maïs humide (calculé, même séchoir, rendement du générateur de {{ v('rendement_generateur_biomasse', 0) }}, hypothèse) :

| Énergie | Coût actuel | Fourchette des scénarios |
|---|---|---|
| Propane | {{ v('sechage_propane_eur_t') }} | {{ fourchette('sechage_propane_eur_t') }} |
| Plaquettes sèches | {{ v('sechage_plaquettes_eur_t') }} | {{ fourchette('sechage_plaquettes_eur_t') }} |

Il faut environ {{ v('sechage_map_t', 2, unite=False) }} MAP de plaquettes par tonne humide (calculé). L'économie d'énergie atteint {{ v('sechage_economie_plaquettes_t') }} au prix actuel, et encore {{ v('sechage_economie_plaquettes_t', scenario='bas') }} au prix d'avant-crise (calculé, hors main-d'œuvre, entretien et amortissement). Face au mazout d'avant-crise, l'avantage des plaquettes fondait à quelques euros par tonne ({{ v('sechage_mazout_eur_t', scenario='bas') }} contre {{ v('sechage_plaquettes_eur_t', scenario='bas') }}). Un agriculteur landais qui sèche au bois estime que la biomasse lui coûte 25 à 30 % du prix du gaz par kWh produit[^reussir-bois], un peu moins que le calcul ci-dessus, qui compte aussi les pertes du générateur.

L'investissement est lourd. Exemples français :

- dans les Landes, deux exploitations ont investi 350 000 € dans une chaudière à plaquettes, « dix fois plus cher qu'une chaudière à gaz », avec 130 000 € d'aide régionale. Le séchoir passe 192 t de grain de 30 à 15 % en 24 heures et sèche 5 000 à 6 000 t par an pour plusieurs exploitations. Retour espéré : sept ans[^reussir-bois] ;
- dans les Pyrénées-Atlantiques, une Cuma a étudié la biomasse puis choisi le gaz : le prix de la chaudière lui a paru rédhibitoire pour un mois d'utilisation par an[^reussir-bois].

Pour une exploitation qui sèche {{ v('sechage_tonnage_ferme', 0, unite=False) }} t de maïs par an (hypothèse), l'économie d'énergie serait de {{ v('sechage_economie_plaquettes_an', 0) }} au prix actuel, {{ v('sechage_economie_plaquettes_an', 0, scenario='bas') }} au prix d'avant-crise (calculé) : trop peu pour payer seule une chaudière de cette taille. Au tonnage de l'exemple landais (5 000 à 6 000 t), la même économie par tonne est dix à douze fois plus grande (calculé). La chaudière biomasse est donc une affaire de négoce, de coopérative ou de groupe d'agriculteurs, ou d'une exploitation qui l'utilise aussi le reste de l'année (chauffage, séchage de bois ou de foin).

**Aides.** L'aide wallonne aux investissements agricoles (AII) ne finance pas la chaudière biomasse : elle est absente de sa liste de 2026[^aii-liste]. L'aide utile est **GREEN**, la prime régionale aux entreprises pour l'énergie renouvelable, ouverte aux agriculteurs (voir [les aides publiques](../../aides.md#green))[^green-agw] [^decret-2004] :

- pour une PME, {{ v('green_taux_chaudiere_biomasse', 0) }} d'une chaudière biomasse jusqu'à 300 kW, sur un coût éligible plafonné à {{ v('green_plafond_chaudiere_kw') }} jusqu'à 100 kW et 880 €/kW de 100 à 300 kW ; 30 % de 300 kW à 1 MW, sur 660 €/kW au plus[^green-spw] ;
- un investissement d'au moins {{ v('green_seuil_pme', 0) }}, une demande avant les travaux et un audit ou une étude de faisabilité AMUREBA préalable, subventionné à {{ v('amureba_taux_pme', 0) }} pour une PME[^green-agw] [^amureba-memo] [^amureba].

Effet sur la rentabilité (calculé, {{ v('sechage_tonnage_ferme', 0, unite=False) }} t de maïs par an, temps de retour visé de {{ v('duree_retour_visee', 0) }}, hypothèse, hors entretien et main-d'œuvre) : l'économie d'énergie rembourse une installation de {{ v('sechage_chaudiere_invest_max', 0) }} au plus sans aide ({{ fourchette('sechage_chaudiere_invest_max', 0) }} selon les scénarios), et de {{ v('sechage_chaudiere_invest_max_green', 0) }} avec GREEN ({{ fourchette('sechage_chaudiere_invest_max_green', 0) }}), si le coût reste sous le coût éligible maximal. L'aide relève donc nettement le prix acceptable. Mais le prix d'une installation de séchage biomasse pour ce tonnage n'est pas connu en Belgique, et l'exemple landais coûte bien plus, pour dix fois plus de grain. Le calcul ne justifie donc pas un passage en vague 1 : la chaudière biomasse reste en vague 2, à comparer avec un devis.

Une coopérative ou un négoce qui est une PME peut aussi demander GREEN ; une installation plus puissante que 300 kW ne reçoit que 30 %. Un exploitant qui a reçu l'AII ne peut demander aucune autre aide wallonne pour ses investissements pendant cinq ans, sauf les soutiens à la production d'énergie renouvelable[^agw-aii] : une chaudière biomasse aidée par GREEN entre a priori dans cette exception (lecture à confirmer).

Conditions :

- un gros tonnage séché chaque année, ou d'autres usages de la chaleur hors saison ;
- des plaquettes sèches et propres : sans terre, racines ni morceaux filandreux, et un bâtiment pour les stocker[^reussir-bois] ;
- du temps : environ une heure par jour pour l'alimentation et l'entretien en saison, et un réglage plus délicat qu'au gaz[^reussir-bois] ;
- pour l'aide GREEN : un audit AMUREBA et une demande avant les travaux (voir « Aides » ci-dessus et la fiche [chauffage au mazout](chauffage-mazout.md)).

### 3. Chaleur d'un méthaniseur (vague 2)

Une unité de biométhanisation en cogénération produit plus de chaleur que d'électricité : dans l'exemple ci-dessous, 40 % de l'énergie sort en électricité et le reste en chaleur[^reussir-demeter]. L'automne est justement une saison où cette chaleur cherche preneur. En Wallonie, les unités agricoles vendent la majeure partie de leur électricité mais valorisent peu leur chaleur, faute de débouchés ; la chaleur verte seule n'y est pas soutenue[^panorama]. Le séchage figure parmi les activités qui permettent d'utiliser cette chaleur[^panorama].

Exemple français : une unité de 500 kWé dans les Deux-Sèvres a installé une cellule sécheuse de 180 t, alimentée par l'air chaud de son séchoir à foin. Elle a séché environ 2 000 t à l'automne 2020, à 50-60 °C, en un à trois jours par lot. Les deux séchoirs (foin et grain) ont coûté 220 000 € avec le réseau de chaleur ; le séchage est facturé au prix des coopératives locales, et l'exploitant prévoit un retour en six campagnes[^reussir-demeter].

Conditions : un méthaniseur en cogénération à proximité (voir la micro-biométhanisation dans la fiche [électricité du réseau](electricite-reseau.md)), une chaleur disponible à l'automne et un séchage plus lent que dans un séchoir au gaz, qui demande de la surveillance[^reussir-demeter].

Aides : un méthaniseur de 10 à 200 kW électriques qui consomme son énergie sur place peut recevoir {{ v('green_taux_biometh', 0) }} de GREEN, sur un coût éligible plafonné à {{ v('green_plafond_biometh_kw') }}[^green-spw], en plus des certificats verts sur l'électricité (voir la fiche [électricité du réseau](electricite-reseau.md)). Un méthaniseur de plus de 200 kW, comme l'exemple des Deux-Sèvres, sort de cette ligne. La chaleur elle-même n'est pas soutenue[^panorama], et aucune aide propre au réseau de chaleur ou à la cellule de séchage n'a été trouvée. La vague 2 est maintenue.

### 4. Air ambiant ou chauffé au solaire (vague 2)

Un ventilateur pousse de l'air extérieur à travers le grain stocké en cellule. Le grain sèche lentement, par une couche qui monte du fond vers le haut[^omafra-air].

- **Limites d'humidité** : en Ontario, seuls le maïs sous 20 à 22 %, le soja sous 16 à 18 % et le blé sous 18 à 20 % sèchent assez vite à l'air ambiant sans s'abîmer[^omafra-air]. Le maïs belge, récolté à 25 % et plus[^cipf], ne se sèche donc pas de cette façon. La méthode convient aux céréales et au colza un peu humides, et à la finition du maïs en sortie de séchoir.
- **Durée** : en Ontario, un maïs à 22 % sèche en 14 jours en septembre et en 20 jours en octobre ; en décembre, il ne descend qu'à 19 % en 88 jours[^omafra-air].
- **Air chauffé au solaire** : des capteurs à air réchauffent l'air de 5 à 6 °C en journée, mais seulement de 0,5 à 1 °C en moyenne sur 24 heures[^omafra-air]. Ils accélèrent le séchage sans le remplacer. C'est le principe du séchage du foin en grange (voir la fiche [ensilage et enrubannage](../elevage/fourrages-recoltes.md)).
- **Finition en cellule (dryération)** : on sort le maïs du séchoir chaud à 17-18 % et on retire les derniers points en le refroidissant dans une cellule bien ventilée. Arvalis la présente comme une source d'économie d'énergie, à condition d'avoir des cellules à ventilation renforcée (40 à 50 m³ d'air par heure et par m³ de grain)[^arvalis-sobriete].
- **Ventilation automatique** : un thermostat qui lance la ventilation de refroidissement seulement quand l'air extérieur est assez froid économise de l'électricité ; une étude du CRA-W (Gembloux) publiée en 2011 estimait le gain à environ 48 %[^arvalis-ventilation].

Conditions : des cellules ventilées en nombre suffisant, un grain pas trop humide, et la patience de laisser sécher plusieurs semaines.

Aides : l'AII reprend le ventilateur ou extracteur d'air (coût simplifié de 540 € par ventilateur d'au moins 450 m³/min) et le hall de séchage pour vrac ({{ v('aii_hall_sechage_forfait') }})[^am-aii]. Le ventilateur ne coche ni « architecture verte » ni « résilience économique » : il est aidé au taux de base de {{ v('aii_taux_base', 0) }} et passe difficilement le seuil de {{ v('aii_seuil_points', 0, unite=False) }} points de sélection ; le hall coche les deux, soit {{ v('aii_taux_pv', 0) }} sans autre majoration (calculé)[^am-aii]. Aucune aide ne vise les capteurs solaires à air. L'aide reste modeste et ne change pas la vague.

### 5. Pompe à chaleur (vague 3)

Une pompe à chaleur réchauffe l'air de séchage avec un compresseur électrique, comme un réfrigérateur qui fonctionnerait à l'envers. Dans un essai en Ontario sur un séchage en cellule à basse température, elle a fourni 6,93 kWh de chaleur par kWh d'électricité ; ses coûts de fonctionnement étaient de 60 % inférieurs à ceux d'un chauffage au propane et proches de ceux du gaz naturel, pour un investissement plus élevé[^omafra-air].

Avec un rendement plus prudent de {{ v('pac_cop_sechage', 0) }} (hypothèse) et l'électricité du réseau, l'énergie coûte {{ v('sechage_pac_eur_t') }} de maïs humide (calculé), autant ou plus qu'au propane ({{ v('sechage_propane_eur_t') }}). Sur de l'électricité photovoltaïque produite sur place, ce coût tomberait à {{ v('sechage_pac_pv_eur_t') }} (calculé), mais le maïs se sèche en octobre et novembre, quand les panneaux produisent peu. Aucune référence belge de séchoir à grain par pompe à chaleur n'a été trouvée. GREEN paie {{ v('green_taux_pac', 0) }} d'une pompe à chaleur air-eau ou eau-eau jusqu'à 45 kW thermiques et 20 % au-delà[^green-spw] ; un séchoir à grain dépasse souvent cette puissance, et son éligibilité n'est pas confirmée. L'AII ne finance pas la pompe à chaleur[^aii-liste]. L'aide ne suffit pas à rendre l'énergie moins chère que le propane : à préparer (vague 3), d'abord pour la finition à basse température et les petits lots.

## Ce qui ferme la boucle

- **Les haies et le bois de la ferme** : pour {{ v('sechage_tonnage_ferme', 0, unite=False) }} t de maïs par an, il faut environ {{ v('sechage_map_an', 0, unite=False) }} MAP de plaquettes par an (calculé), de l'ordre de 5 à 10 km de haies avec les productivités citées dans la fiche [chauffage au mazout](chauffage-mazout.md) (ordre de grandeur, calculé).
- **Les rafles de maïs** : récoltées à part, elles peuvent servir de combustible au séchoir ; un projet complet dans les Landes (récolte, transport, stockage, séchage, granulés) a coûté plus de 500 000 € en 2006[^reussir-rafles].
- **La chaleur du méthaniseur**, perdue en automne si elle ne sèche rien.
- **Le maïs grain humide et l'épi broyé**, mangés à la ferme, évitent le séchage et le transport de l'eau.
- **Les cendres** de la chaudière retournent au champ (voir la fiche [engrais phosphatés et potassiques](../fertilisation/engrais-p-k.md)).

## À vérifier

- Barème indicatif des frais de séchage du maïs de la FEGRA pour 2025 et 2026 (réservé aux membres) et frais réellement facturés en Wallonie en 2026 (SCAM, Walagri, négociants).
- Repères de l'Agrofront pour les frais de séchage des céréales en 2026 : seuls ceux de 2024 et 2025 ont été lus.
- Part des séchoirs belges au gaz naturel, au propane et au fioul, et prix du gaz naturel payé par un séchoir professionnel.
- Consommation mesurée d'un séchoir belge (kWh par kg d'eau) : la fiche s'appuie sur des chiffres français et canadiens.
- Humidité moyenne du maïs grain à la récolte en Wallonie ces dernières années (essais du CIPF, Livre blanc céréales) et surface de maïs grain sec en Wallonie.
- Écart de rendement entre variétés de maïs grain précoces et tardives dans les essais belges, pour chiffrer l'intérêt d'une variété plus précoce.
- Statut TVA du prix des plaquettes du relevé Valbiom : s'il est TVAC, le coût des plaquettes est un peu surestimé face au propane et au mazout comptés HTVA.
- Rendement réel d'un générateur d'air chaud biomasse et prix d'une installation pour un séchoir de ferme ou de coopérative en Belgique.
- Exemples belges de séchage de grain à la chaleur d'un méthaniseur, au bois ou par pompe à chaleur.
- Prix d'une installation de séchage biomasse pour {{ v('sechage_tonnage_ferme', 0, unite=False) }} t de maïs par an, et puissance nécessaire (au-delà de 300 kW, GREEN tombe à 30 %).
- Éligibilité à GREEN d'un générateur d'air chaud biomasse de séchoir, d'une pompe à chaleur de séchage et d'une CUMA ; accès d'une exploitation agricole à la subvention AMUREBA (règle *de minimis*).
- Cumul de GREEN avec l'AII reçue pour d'autres investissements (exception « énergie renouvelable » de l'AGW de 2026) et avec la déduction fédérale pour investissement.
- Les taux de GREEN viennent du tableau du SPW Économie : l'annexe officielle de l'arrêté n'a pas pu être lue.
- Étude du CRA-W de 2011 sur la ventilation automatisée des grains : chiffre de 48 % connu par un article d'Arvalis seulement.

## Sources

[^cipf]: « Cultiver du maïs grain à sécher en suivant un itinéraire technique adapté », F. Renard, G. Foucart, J.-F. Oost, CIPF (Centre pilote en culture de maïs) et UCLouvain, mars 2008. https://cipf.be/shared/files/fr/ititecgrain.pdf
[^fegra]: « Cotation culture (indicatif) », FEGRA (Fédération belge des négociants en céréales), prix du 26 novembre 2026, consulté le 26 novembre 2026. https://fegra.be/home/agriculturalprices?lang=fr
[^boerenbond-2025]: « Geen akkoord met graanhandel over droogkosten 2025 », Boerenbond, 19 juin 2025, mis à jour le 26 septembre 2025 (tableau des repères de l'Agrofront). https://www.boerenbond.be/node/17908
[^boerenbond-2026]: « Geen akkoord met graanhandel over droogkosten 2026 », Boerenbond, 29 mai 2026. https://www.boerenbond.be/nieuws/geen-akkoord-met-graanhandel-over-droogkosten-2026
[^civam]: « Le maïs grain humide : un aliment énergétique économique », Réseau des CIVAM normands (France), mis à jour le 6 novembre 2024. https://www.civam-normands.org/index.php/actualites-elevage/1729-le-mais-grain-humide-un-aliment-energetique-economique
[^reussir-bois]: « Maïs grain : le coût du gaz renforce l'intérêt du séchage au bois », Réussir Grandes cultures (France), 9 septembre 2022. https://www.reussir.fr/grandes-cultures/mais-grain-le-cout-du-gaz-renforce-linteret-du-sechage-au-bois
[^reussir-demeter]: « Demeter Énergies : nous séchons le grain avec la chaleur de la méthanisation », Réussir Lait (France), 23 septembre 2021. https://www.reussir.fr/lait/demeter-energies-nous-sechons-le-grain-avec-la-chaleur-de-la-methanisation
[^reussir-rafles]: « Récupérer et valoriser ses rafles de maïs », Réussir Machinisme (France), consulté le 26 novembre 2026. https://www.reussir.fr/machinisme/recuperer-et-valoriser-ses-rafles-de-mais
[^omafra-energie]: « Réduction de l'énergie consommée par les séchoirs à grain », fiche technique n° 24-006, ministère de l'Agriculture, de l'Alimentation et des Affaires rurales de l'Ontario (Canada), mars 2024. https://www.ontario.ca/files/2024-04/omafra-reducing-energy-in-grain-dryers-24-006-fr-05-04-2024.pdf
[^omafra-air]: « Séchage des grains à l'air ambiant », fiche technique n° 20-044, ministère de l'Agriculture, de l'Alimentation et des Affaires rurales de l'Ontario (Canada), juin 2020. https://files.ontario.ca/omafra-natural-air-grain-drying-20-044-fr-2023-05-16.pdf
[^arvalis-sobriete]: « Économiser en séchant moins le maïs grain : attention au risque de dégradation de la qualité », K. Crépon et B. Orlando, Arvalis, publié sur Pleinchamp (France), 12 octobre 2022. https://www.pleinchamp.com/actualite/economiser-en-sechant-moins-le-mais-grain-attention-au-risque-de-degradation-de-la-qualite
[^arvalis-ventilation]: « Conservation des stocks : refroidir rapidement les cellules de maïs grain après séchage », J.-Y. Moreau et A. Tanguy, Arvalis, publié sur Pleinchamp (France), 9 octobre 2023. https://www.pleinchamp.com/actualite/conservation-des-stocks-refroidir-rapidement-les-cellules-de-mais-grain-apres-sechage
[^panorama]: « Panorama de la biométhanisation en Wallonie », Valbiom, édition 2025 (chiffres 2024), hébergé par le SPW Énergie. https://energie.wallonie.be/files/%c3%89nergies%20vertes/Bio%c3%a9nergie/Biom%c3%a9thanisation/panorama-biometh-2025.pdf
[^am-aii]: Arrêté ministériel du 23 février 2023 exécutant l'arrêté du Gouvernement wallon du 23 février 2023 relatif aux aides à l'installation et aux investissements, version consolidée (modifications des 15 janvier et 11 mai 2026) : articles 5 et 6, annexes 2 et 3 (lignes 238 et 465). Wallex, consulté le 27 novembre 2026. https://wallex.wallonie.be/eli/arrete/2023/02/23/2023042748
[^aii-liste]: « Liste des investissements admissibles », SPW Agriculture, janvier 2026, consultée le 27 novembre 2026. https://agriculture.wallonie.be/files/accueil/Aides/AII/outils/Liste%20des%20investissements%20admissibles.pdf
[^agw-aii]: Arrêté du Gouvernement wallon du 23 février 2023 relatif aux aides à l'installation et aux investissements, version en vigueur depuis le 1er janvier 2026 : article 36. Wallex, consulté le 27 novembre 2026. https://wallex.wallonie.be/eli/arrete/2023/02/23/2023042313/2026/01/01
[^green-agw]: Arrêté du Gouvernement wallon du 23 mai 2024 relatif aux primes à l'investissement (aides GREEN), en vigueur le 1er janvier 2025 : articles 4 à 16 et 26. Wallex, consulté le 27 novembre 2026. https://wallex.wallonie.be/sites/wallex/contents/acts/108/108350/1.html
[^green-spw]: « Réforme des aides spécifiques à la protection de l'environnement et à l'utilisation de l'énergie », SPW Économie, Emploi, Recherche, publié le 28 novembre 2024, mis à jour le 23 janvier 2025, consulté le 27 novembre 2026. https://economie.wallonie.be/fr/home/actualites/actualites/reforme-des-aides-specifiques-a-la-protection-de-l-environnement-et-a-l-utilisation-de-l-energie.html
[^decret-2004]: Décret du 11 mars 2004 relatif aux incitants régionaux en faveur des petites ou moyennes entreprises, version en vigueur depuis le 1er janvier 2025, articles 3 à 5. Wallex, consulté le 27 novembre 2026. https://wallex.wallonie.be/eli/loi-decret/2004/03/11/2004200990
[^amureba]: Arrêté du Gouvernement wallon du 1er février 2024 relatif à l'octroi de subventions à l'audit ou à l'étude dans le secteur non résidentiel (AMUREBA), annexe 5. Wallex, consulté le 27 novembre 2026. https://wallex.wallonie.be/eli/arrete/2024/02/01/2024004275
[^amureba-memo]: « Mémo Table ronde des auditeurs du 6 février 2026 », SPW Énergie, consulté le 27 novembre 2026. https://energie.wallonie.be/files/Actualit%c3%a9s/20260206_m%c3%a9mo%20Table%20ronde%20auditeurs.pdf
