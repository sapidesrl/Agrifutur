---
id: engins-de-cour
titre: Télescopique et chargeur de cour diesel
domaine: traction
dependance_fossile: gasoil
alternatives: [Télescopique ou chargeur électrique, télescopique hybride au biométhane]
vague_meilleure_alternative: 2
statut: brouillon
maj: 2026-11-26
---

# Télescopique et chargeur de cour diesel

!!! warning "Sources à relire"
    Les sources de cette fiche n'ont été consultées que par les extraits d'un moteur de recherche (novembre 2026). Chaque chiffre sourcé doit être confirmé sur la page avant le passage au statut « relu ».

## En bref

Le télescopique et le chargeur articulé (« valet de ferme ») font la manutention quotidienne : paillage, alimentation, curage, chargement. Ils roulent au gasoil, peu d'heures par jour mais tous les jours. Leur version électrique fait le même travail et coûte beaucoup moins cher en énergie, surtout derrière ses propres panneaux. Le frein est le prix d'achat, plus élevé de 30 à 40 %. Sur une exploitation qui les utilise peu, l'économie d'énergie ne rembourse pas ce surcoût : l'électrique est rentable sous conditions (vague 2).

## Comment ça marche aujourd'hui

Un moteur diesel de 25 à plus de 100 kW entraîne la transmission hydrostatique et la pompe hydraulique qui fait monter le bras. Le chargeur articulé est petit et agile, le télescopique lève plus haut et plus lourd.

Les consommations sont modestes. Dans un essai de la chambre d'agriculture de Basse-Saxe en 2023, des valets de ferme diesel consommaient en moyenne 3,09 L/h[^lwk]. Un gros télescopique agricole de 136 ch tournait autour de 7,8 L/h sur une journée de 12 heures[^faresin]. Un valet de ferme en élevage laitier fait typiquement 250 à 300 heures par an[^topagrar-h] ; un télescopique très sollicité dépasse 400 heures[^topagrar-jcb].

## Où entrent le pétrole et le gaz

- **Carburant** : le gasoil.
- **AdBlue** sur les moteurs récents : urée fabriquée à partir de gaz naturel.
- **Huile hydraulique, pneus, flexibles** : issus de la pétrochimie. L'électrique ne supprime pas ce poste.

## Les alternatives

### 1. Chargeur ou télescopique électrique (vague 2)

Presque tous les constructeurs en proposent : Weidemann, Kramer, Schäffer, Manitou, Merlo, Dieci, JCB, Faresin, Avant. Les batteries vont d'environ 14 kWh pour un petit valet de ferme à 35-44 kWh pour un télescopique compact[^weidemann][^profi][^dieci]. Dans l'essai de Basse-Saxe, les machines électriques avaient des performances quasi identiques aux diesel (agilité, poussée, charge de basculement, hauteur)[^lwk].

Coût de l'énergie par heure pour un valet de ferme (calculé, à partir des consommations de l'essai de Basse-Saxe, pertes de charge comprises) :

| Énergie | Prix actuel | Fourchette des scénarios |
|---|---|---|
| Gasoil | {{ v('valet_gasoil_eur_h') }} | {{ fourchette('valet_gasoil_eur_h') }} |
| Électricité du réseau | {{ v('valet_reseau_eur_h') }} | {{ fourchette('valet_reseau_eur_h') }} |
| Photovoltaïque de la ferme | {{ v('valet_pv_eur_h') }} | fixe |

Sur {{ v('heures_valet_an') }}, l'économie d'énergie atteint {{ v('valet_economie_an_pv') }} sur photovoltaïque et {{ v('valet_economie_an_reseau') }} sur le réseau. Au prix d'avant-crise, elle tombe à {{ v('valet_economie_an_pv', scenario='bas') }} sur photovoltaïque. Contrairement au tracteur, l'électrique reste ici moins cher que le gasoil même sur le réseau : le moteur diesel d'un petit engin qui tourne souvent au ralenti a un mauvais rendement.

Le frein est le prix d'achat :

- l'électrique coûte plus de 30 % plus cher que le diesel dans l'essai de Basse-Saxe[^lwk] ;
- un Manitou MLT 625e coûtait près de 33 000 £ de plus que sa version diesel au Royaume-Uni, soit environ 40 %[^profi] ;
- le JCB 525-60E était affiché à 87 435 £, contre 64 270 £ pour le diesel équivalent[^fwi] ;
- chez Weidemann, les prix catalogue HTVA vont de 56 000 € pour un petit valet de ferme électrique à 90 500 € pour un télescopique[^weidemann].

Un surcoût de 30 à 40 % sur ces prix représente de l'ordre de 15 000 à 35 000 € (ordre de grandeur tiré des prix ci-dessus[^weidemann][^profi]). Face à une économie d'énergie de {{ v('valet_economie_an_pv') }}, le retour sur investissement dépasse 15 ans, soit plus que la durée de vie probable de la batterie (hypothèse). L'entretien réduit (pas de vidange, pas de filtres, pas d'AdBlue) améliore le bilan, mais il n'est pas chiffré ici.

L'autonomie réelle est un autre point de vigilance. Les constructeurs annoncent 3,5 à 8 heures en usage classique et 2,5 à 5 heures en usage intensif[^pleinchamp]. Un exploitant autrichien obtient 2,5 à 3 heures de travail productif par charge avec un JCB 525-60E[^topagrar-jcb]. Cela suffit pour le paillage et l'alimentation du matin et du soir, avec une recharge entre les deux, mais pas pour une longue journée d'ensilage.

Conditions de rentabilité :

- beaucoup d'heures par an (au-delà de 400 à 500 h, hypothèse) ;
- recharge sur son propre photovoltaïque, entre deux chantiers ;
- travail en bâtiment fermé, où l'absence de gaz d'échappement et de bruit compte pour les animaux et les personnes ;
- une aide à l'investissement. En Basse-Saxe, une subvention de 20 % rendait le coût total de l'électrique légèrement inférieur à celui du diesel[^lwk-aide]. En Wallonie, l'aide aux investissements (AII) prévoit une ligne « chargeur compact, télescopique », mais le traitement d'un engin électrique n'y est pas précisé[^aii].

### 2. Télescopique hybride au biométhane (vague 3)

New Holland a présenté en novembre 2025 un prototype de télescopique hybride : une batterie de 70 kWh, rechargée par un petit moteur au gaz compatible biométhane, qui prend le relais pour les gros travaux. L'autonomie électrique annoncée est de 4 à 6 heures, pour une capacité de 4,2 t à 7 m[^nh]. Aucun prix ni date de commercialisation n'étaient connus fin 2026.

C'est une piste pour les longues journées, à condition d'avoir accès à du biométhane comprimé sur la ferme ou à proximité.

## Ce qui ferme la boucle

- Le toit de l'étable porte les panneaux qui rechargent le chargeur entre la traite du matin et celle du soir.
- La batterie du chargeur peut absorber le surplus de production de midi, au lieu de l'injecter sur le réseau à bas prix.
- Pour les gros chantiers, le biométhane des effluents de l'élevage peut un jour remplacer le gasoil.

## À vérifier

- Relire toutes les sources sur la page d'origine (consultées par extraits seulement).
- Prix belges neufs, en euros, d'un valet de ferme et d'un télescopique électriques face à leurs équivalents diesel.
- Coût et durée de vie réelle d'une batterie de remplacement (les constructeurs annoncent environ 5 000 cycles).
- Gain d'entretien de l'électrique, en euros par an.
- Traitement des engins électriques dans l'aide wallonne aux investissements (AII).
- Consommation réelle de l'exploitation, en litres par heure et en heures par an, pour remplacer les hypothèses.

## Sources

[^lwk]: « Hoflader im Test: Diesel oder elektrisch? », Wochenblatt / Land & Forst, essai de la Landwirtschaftskammer Niedersachsen, 2023. https://www.wochenblatt-dlv.de/feld-stall/landtechnik/hoflader-test-diesel-elektrisch-574598
[^lwk-aide]: « Hofladertest Teil 3 : finanzielle Förderung macht E-Lader interessant », Land & Forst, 2023. https://www.landundforst.de/landwirtschaft/landtechnik/hofladertest-teil-3-finanzielle-foerderung-macht-e-lader-interessant-570303
[^faresin]: « Essai chargeur télescopique Faresin FS 7.40 Middle Excellence 100 », Réussir, date à vérifier. https://www.reussir.fr/essai-chargeur-telescopique-faresin-fs-740-middle-excellence-100-un-engin-particulierement-stable
[^topagrar-h]: « Hoffahrzeuge mit Strom oder Diesel antreiben », top agrar, date à vérifier. https://www.topagrar.com/betriebsleitung/news/hoffahrzeuge-mit-strom-oder-diesel-antreiben-20016039.html
[^topagrar-jcb]: « E-Lader von JCB mit leisen Sohlen und viel Kraft », top agrar Österreich, date à vérifier. https://www.topagrar.com/oesterreich/e-lader-von-jcb-mit-leisen-sohlen-und-viel-kraft-20022753.html
[^weidemann]: « E-Flotte von Weidemann : Strom schlägt Diesel », top agrar Österreich, date à vérifier. https://www.topagrar.com/oesterreich/e-flotte-von-weidemann-strom-schlagt-diesel-20025026.html
[^profi]: « Manitou MLT 625e fully electric compact telehandler », profi, date à vérifier. https://www.profi.co.uk/test-centre/manitou-mlt-625e-fully-electric-compact-telehandler-elevating-electrons/
[^dieci]: Fiche technique Dieci Mini Agri-e 26.6, Dieci. https://dieci.com/ASSETS//Scheda_Tecnica/DOCCT0000139-EN-00.pdf
[^fwi]: « On test : JCB's debut battery-electric Loadall, the 525-60E », Farmers Weekly, date à vérifier. https://fwi.co.uk/machinery/telehandlers/on-test-jcbs-debut-battery-electric-loadall-the-525-60e
[^pleinchamp]: « Les engins de manutention agricole se mettent à l'électrique », Pleinchamp (France), date à vérifier. https://www.pleinchamp.com/actualite/les-engins-de-manutention-agricole-se-mettent-a-l-electrique
[^aii]: Arrêté ministériel du 23 février 2023 (aides aux investissements dans les exploitations agricoles), Wallex, version consolidée. https://wallex.wallonie.be/eli/arrete/2023/02/23/2023042748
[^nh]: « Ce chargeur télescopique hybride New Holland fonctionne au gaz et à l'électricité », Terre-net, novembre 2025. https://www.terre-net.fr/new-holland/article/891389/ce-chargeur-telescopique-hybride-new-holland-fonctionne-au-gaz-et-a-l-electricit
