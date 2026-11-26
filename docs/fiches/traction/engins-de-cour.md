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

## En bref

Le télescopique et le chargeur articulé (« valet de ferme ») font la manutention quotidienne : paillage, alimentation, curage, chargement. Ils roulent au gasoil, peu d'heures par jour mais tous les jours. Leur version électrique fait le même travail et coûte beaucoup moins cher en énergie, surtout derrière ses propres panneaux. Le frein est le prix d'achat, plus élevé d'environ 35 à 60 % selon les essais. Sur une exploitation qui les utilise peu, l'économie d'énergie ne rembourse pas ce surcoût : l'électrique est rentable sous conditions (vague 2).

## Comment ça marche aujourd'hui

Un moteur diesel de moins de 20 kW (valet de ferme)[^lwk] à 100 kW (gros télescopique)[^faresin] entraîne la transmission hydrostatique et la pompe hydraulique qui fait monter le bras. Le chargeur articulé est petit et agile, le télescopique lève plus haut et plus lourd.

Les consommations sont modestes. Dans un essai de la chambre d'agriculture de Basse-Saxe en 2023, des valets de ferme diesel consommaient en moyenne 3,1 L/h en travail de chargement, et encore 0,78 L/h moteur au ralenti[^lwk]. Un gros télescopique agricole de 136 ch a consommé 7,8 L/h en moyenne sur 12 heures de travail[^faresin]. Un valet de ferme d'un élevage laitier bavarois tourne 250 à 300 heures par an[^topagrar-h] ; un exploitant autrichien compte environ 400 heures par an pour son télescopique électrique[^topagrar-jcb].

## Où entrent le pétrole et le gaz

- **Carburant** : le gasoil.
- **AdBlue** sur les moteurs récents : urée fabriquée à partir de gaz naturel.
- **Huile hydraulique, pneus, flexibles** : issus de la pétrochimie. L'électrique ne supprime pas ce poste.

## Les alternatives

### 1. Chargeur ou télescopique électrique (vague 2)

La plupart des constructeurs en proposent, par exemple Weidemann, Schäffer, Giant, JCB, Merlo, Dieci et Faresin[^lwk][^pleinchamp][^dieci][^faresin]. Les batteries vont d'environ 14 kWh pour un petit valet de ferme[^weidemann] à 24 kWh pour le télescopique JCB 525-60E[^fwi] et 22 ou 44 kWh pour le télescopique compact Dieci Mini Agri-e[^dieci]. Dans l'essai de Basse-Saxe, la force de poussée des électriques était, selon la marque, égale, supérieure ou inférieure à celle du diesel ; pour le même travail, ils consommaient 79 % d'énergie en moins[^lwk]. Constructeurs et premiers utilisateurs ne constatent pas de différence notable de débit de chantier[^pleinchamp].

Coût de l'énergie par heure pour un valet de ferme (calculé à partir des consommations de l'essai de Basse-Saxe ; l'électricité y était mesurée à la borne de recharge, et le calcul ajoute encore des pertes de charge, ce qui est prudent) :

| Énergie | Prix actuel | Fourchette des scénarios |
|---|---|---|
| Gasoil | {{ v('valet_gasoil_eur_h') }} | {{ fourchette('valet_gasoil_eur_h') }} |
| Électricité du réseau | {{ v('valet_reseau_eur_h') }} | {{ fourchette('valet_reseau_eur_h') }} |
| Photovoltaïque de la ferme | {{ v('valet_pv_eur_h') }} | fixe |

Sur {{ v('heures_valet_an') }}, l'économie d'énergie atteint {{ v('valet_economie_an_pv') }} sur photovoltaïque et {{ v('valet_economie_an_reseau') }} sur le réseau. Au prix d'avant-crise, elle tombe à {{ v('valet_economie_an_pv', scenario='bas') }} sur photovoltaïque. Contrairement au tracteur, l'électrique reste ici moins cher que le gasoil même sur le réseau : le moteur diesel d'un petit engin qui tourne souvent au ralenti a un mauvais rendement[^lwk].

Le frein est le prix d'achat :

- dans l'essai de Basse-Saxe, les valets de ferme électriques coûtaient en moyenne 69 000 € au prix catalogue, contre 45 500 € pour les diesel, soit plus de 23 000 € d'écart (environ + 50 %)[^lwk-aide] ;
- en Bavière, le Weidemann 1190e électrique était affiché à 54 800 € HTVA, environ 20 000 € de plus qu'un diesel comparable[^topagrar-h] ;
- au Royaume-Uni, le télescopique JCB 525-60E était affiché à 87 435 £, contre 64 270 £ pour le diesel équivalent (environ + 36 %)[^fwi] ;
- chez Weidemann, les prix catalogue HTVA vont de 56 000 € pour un petit valet de ferme électrique à 90 500 € pour un télescopique[^weidemann] ;
- la presse française cite un surcoût d'au moins 30 % (batterie au plomb) à près du double (certains modèles au lithium)[^pleinchamp].

Pour un valet de ferme, le surcoût est donc d'environ 20 000 à 23 000 €[^lwk-aide][^topagrar-h]. Face à une économie d'énergie de {{ v('valet_economie_an_pv') }}, le retour sur investissement dépasse 15 ans. C'est au moins la durée de vie annoncée d'une batterie : 2 000 à 5 000 cycles selon les marques[^pleinchamp], soit environ sept ans à deux charges par jour pour les 5 000 cycles de JCB[^fwi]. Les constructeurs avancent un retour de deux à cinq ans[^pleinchamp], ce qui suppose un usage bien plus intensif que 300 heures par an. L'entretien réduit (pas de vidange moteur, pas de filtres, pas d'AdBlue) améliore le bilan, mais il n'est pas chiffré ici : sur l'exploitation bavaroise, la batterie d'origine (au gel) n'a tenu que 1 500 heures et son remplacement a coûté 4 000 €, ce qui a effacé le gain d'entretien[^topagrar-h].

L'autonomie réelle est un autre point de vigilance. Les constructeurs annoncent 3,5 à 8 heures en usage classique et 2,5 à 5 heures en usage intensif[^pleinchamp]. Un exploitant autrichien obtient 2,5 à 3 heures de travail productif par charge avec un JCB 525-60E[^topagrar-jcb]. Cela suffit pour le paillage et l'alimentation du matin et du soir, avec une recharge entre les deux, mais pas pour une longue journée d'ensilage.

Conditions de rentabilité :

- beaucoup d'heures par an (au-delà de 400 à 500 h, hypothèse), ce qui ne suffit pas seul à rembourser le surcoût ;
- recharge sur son propre photovoltaïque, entre deux chantiers ;
- travail en bâtiment fermé, où l'absence de gaz d'échappement et de bruit compte pour les animaux et les personnes ;
- une aide à l'investissement. En Allemagne, une subvention fédérale de 20 % (programme d’efficacité énergétique, guichet fermé à l’été 2025) rendait le coût annuel total de l'électrique légèrement inférieur à celui du diesel[^topagrar-h] ; l'essai de Basse-Saxe conclut aussi que l'aide et une part de courant photovoltaïque rendent l'électrique compétitif[^lwk-aide]. En Wallonie, l'aide aux investissements (AII) prévoit une ligne « chargeur compact / nettoyeur d'étable / télescopique », classée par puissance en chevaux, avec un coût plafond de 35 387 € (moins de 50 ch) à 83 050 € (100 ch et plus). Rien n'y vise l'engin électrique, alors qu'une ligne existe pour le tracteur électrique ou au biogaz[^aii].

### 2. Télescopique hybride au biométhane (vague 3)

New Holland a présenté à l'Agritechnica 2025 un prototype de télescopique hybride, le TH Hybrid Power : une batterie de 70 kWh et un moteur au gaz naturel comprimé de 75 kW (utilisable au biométhane) qui apporte la puissance des gros travaux et recharge la batterie. L'autonomie électrique annoncée est de 4 à 6 heures, pour une capacité de 4,2 t et une hauteur de levage de 7 à 9 m[^nh]. Aucun prix ni date de commercialisation n'étaient connus fin 2026.

C'est une piste pour les longues journées, à condition d'avoir accès à du biométhane comprimé sur la ferme ou à proximité.

## Ce qui ferme la boucle

- Le toit de l'étable porte les panneaux qui rechargent le chargeur entre la traite du matin et celle du soir.
- La batterie du chargeur peut absorber le surplus de production de midi, au lieu de l'injecter sur le réseau à bas prix.
- Pour les gros chantiers, le biométhane des effluents de l'élevage peut un jour remplacer le gasoil.

## À vérifier

- Prix du Manitou MLT 625e face à sa version diesel (test de profi : https://www.profi.co.uk/test-centre/manitou-mlt-625e-fully-electric-compact-telehandler-elevating-electrons/ , page inaccessible en novembre 2026).
- Détail du calcul de coût total de l'essai de Basse-Saxe (partie 3, réservée aux abonnés).
- Prix belges neufs, en euros, d'un valet de ferme et d'un télescopique électriques face à leurs équivalents diesel.
- Coût et durée de vie réelle d'une batterie lithium de remplacement (les constructeurs annoncent 2 000 à 5 000 cycles).
- Gain d'entretien de l'électrique, en euros par an.
- Traitement des engins électriques dans l'aide wallonne aux investissements (AII).
- Consommation réelle de l'exploitation, en litres par heure et en heures par an, pour remplacer les hypothèses.

## Sources

[^lwk]: Martin Vaupel (Landwirtschaftskammer Niedersachsen), « Hoflader im Test: Diesel oder elektrisch? », Bayerisches Landwirtschaftliches Wochenblatt, 29 octobre 2023, avec ses tableaux de mesures. https://www.wochenblatt-dlv.de/feld-stall/landtechnik/hoflader-test-diesel-elektrisch-574598
[^lwk-aide]: « Hofladertest Teil 3: Finanzielle Förderung macht E-Lader interessant », Land & Forst, 13 novembre 2023 (partie visible sans abonnement). https://www.landundforst.de/landwirtschaft/landtechnik/hofladertest-teil-3-finanzielle-foerderung-macht-e-lader-interessant-570303
[^faresin]: « Essai chargeur télescopique Faresin FS 7.40 Middle Excellence 100 », Réussir, 27 mai 2025. https://www.reussir.fr/machinisme/essai-chargeur-telescopique-faresin-fs-740-middle-excellence-100-un-engin-particulierement-stable
[^topagrar-h]: Josef Neiber (LfL Bayern), « Hoffahrzeuge mit Strom oder Diesel antreiben », top agrar, 9 juillet 2025. https://www.topagrar.com/betriebsleitung/news/hoffahrzeuge-mit-strom-oder-diesel-antreiben-20016039.html
[^topagrar-jcb]: « E-Lader von JCB mit leisen Sohlen und viel Kraft », top agrar Österreich, 23 février 2026. https://www.topagrar.com/oesterreich/e-lader-von-jcb-mit-leisen-sohlen-und-viel-kraft-20022753.html
[^weidemann]: « E-Flotte von Weidemann: Strom schlägt Diesel », top agrar Österreich, 27 avril 2026. https://www.topagrar.com/oesterreich/e-flotte-von-weidemann-strom-schlagt-diesel-20025026.html
[^dieci]: Fiche technique Dieci Mini Agri-e 26.6 (révision 04), Dieci, consultée en novembre 2026. https://dieci.com/ASSETS//Scheda_Tecnica/DOCCT0000139-EN-04.pdf
[^fwi]: « On test : JCB's debut battery-electric Loadall, the 525-60E », Farmers Weekly, 25 octobre 2021. https://fwi.co.uk/machinery/telehandlers/on-test-jcbs-debut-battery-electric-loadall-the-525-60e
[^pleinchamp]: « Les engins de manutention agricole se mettent à l'électrique », Pleinchamp (France), 16 juillet 2022. https://www.pleinchamp.com/actualite/les-engins-de-manutention-agricole-se-mettent-a-l-electrique
[^aii]: Arrêté ministériel du 23 février 2023 (aides aux investissements dans les exploitations agricoles), Wallex, version consolidée (dernière modification : arrêté ministériel du 11 mai 2026), annexe des coûts plafonds. https://wallex.wallonie.be/eli/arrete/2023/02/23/2023042748
[^nh]: « Ce chargeur télescopique hybride New Holland fonctionne au gaz et à l'électricité », Terre-net, 10 décembre 2025. https://www.terre-net.fr/new-holland/article/891389/ce-chargeur-telescopique-hybride-new-holland-fonctionne-au-gaz-et-a-l-electricit
