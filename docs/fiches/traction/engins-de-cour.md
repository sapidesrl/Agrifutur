---
id: engins-de-cour
titre: Télescopique et chargeur de cour diesel
domaine: traction
dependance_fossile: gasoil
alternatives: [Télescopique ou chargeur électrique, télescopique hybride au biométhane]
vague_meilleure_alternative: 2
statut: relu
maj: 2026-11-27
---

# Télescopique et chargeur de cour diesel

## En bref

Le télescopique et le chargeur articulé (« valet de ferme ») font la manutention quotidienne : paillage, alimentation, curage, chargement. Ils roulent au gasoil, peu d'heures par jour mais tous les jours. Leur version électrique fait le même travail et coûte beaucoup moins cher en énergie derrière ses propres panneaux ; sur le réseau, l'avantage n'existe qu'au prix de crise. Le frein est le prix d'achat, plus élevé d'environ 35 à 60 % selon les essais[^lwk-aide][^topagrar-h][^fwi]. Sur une exploitation qui les utilise peu, l'économie d'énergie ne rembourse pas ce surcoût, et l'aide wallonne aux investissements paie le même montant pour l'électrique et le diesel : l'électrique est rentable sous conditions (vague 2).

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

Coût de l'énergie par heure pour un valet de ferme (calculé à partir des consommations de l'essai de Basse-Saxe ; l'électricité y était mesurée à la borne de recharge, pertes de charge comprises) :

| Énergie | Prix actuel | Fourchette des scénarios |
|---|---|---|
| Gasoil | {{ v('valet_gasoil_eur_h') }} | {{ fourchette('valet_gasoil_eur_h') }} |
| Électricité du réseau | {{ v('valet_reseau_eur_h') }} | {{ fourchette('valet_reseau_eur_h') }} |
| Photovoltaïque de la ferme | {{ v('valet_pv_eur_h') }} | fixe |

Sur {{ v('heures_valet_an') }} (le haut de la fourchette bavaroise citée plus haut), l'économie d'énergie atteint {{ v('valet_economie_an_pv') }} sur photovoltaïque et {{ v('valet_economie_an_reseau') }} sur le réseau. Au prix d'avant-crise, elle tombe à {{ v('valet_economie_an_pv', scenario='bas') }} sur photovoltaïque. Contrairement au [tracteur](tracteur-diesel.md), l'électrique reste ici moins cher que le gasoil même sur le réseau au prix actuel, parce que le moteur diesel d'un petit engin qui tourne souvent au ralenti a un mauvais rendement[^lwk]. Au prix d'avant-crise, l'avantage sur le réseau disparaît ({{ v('valet_economie_an_reseau', scenario='bas') }}) : seul le photovoltaïque garde un gain net.

Le frein est le prix d'achat :

- dans l'essai de Basse-Saxe, les valets de ferme électriques coûtaient en moyenne 69 000 € au prix catalogue, contre 45 500 € pour les diesel, soit plus de 23 000 € d'écart (environ + 50 %)[^lwk-aide] ;
- en Bavière, le Weidemann 1190e électrique était affiché à 54 800 € HTVA, environ 20 000 € de plus qu'un diesel comparable[^topagrar-h] ;
- au Royaume-Uni, le télescopique JCB 525-60E était affiché à 87 435 £, contre 64 270 £ pour le diesel équivalent (environ + 36 %)[^fwi] ;
- chez Weidemann, les prix catalogue HTVA vont de 56 000 € pour un petit valet de ferme électrique à 90 500 € pour un télescopique[^weidemann] ;
- la presse française cite un surcoût d'au moins 30 % (batterie au plomb) à près du double (certains modèles au lithium)[^pleinchamp].

Pour un valet de ferme, le surcoût est donc d'environ 20 000 à 23 000 €[^lwk-aide][^topagrar-h]. Face à une économie d'énergie de {{ v('valet_economie_an_pv') }}, le retour sur investissement dépasse 15 ans. C'est au moins la durée de vie annoncée d'une batterie : 2 000 à 5 000 cycles selon les marques[^pleinchamp], soit environ sept ans à deux charges par jour pour les 5 000 cycles de JCB[^fwi]. Les constructeurs avancent un retour de deux à cinq ans[^pleinchamp], ce qui suppose un usage bien plus intensif que {{ v('heures_valet_an') }}. L'entretien réduit (pas de vidange moteur, pas de filtres, pas d'AdBlue) améliore le bilan, mais il n'est pas chiffré ici : sur l'exploitation bavaroise, la batterie d'origine (au gel) n'a tenu que 1 500 heures et son remplacement a coûté 4 000 €, ce qui a effacé le gain d'entretien[^topagrar-h].

L'autonomie réelle est un autre point de vigilance. Les constructeurs annoncent 3,5 à 8 heures en usage classique et 2,5 à 5 heures en usage intensif[^pleinchamp]. Un exploitant autrichien obtient 2,5 à 3 heures de travail productif par charge avec un JCB 525-60E[^topagrar-jcb]. Cela suffit pour le paillage et l'alimentation du matin et du soir, avec une recharge entre les deux, mais pas pour une longue journée d'ensilage.

Conditions de rentabilité :

- beaucoup d'heures par an (au-delà de 400 à 500 h, hypothèse), ce qui ne suffit pas seul à rembourser le surcoût ;
- recharge sur son propre photovoltaïque, entre deux chantiers ;
- travail en bâtiment fermé, où l'absence de gaz d'échappement et de bruit compte pour les animaux et les personnes ;
- une aide qui paie le surcoût. En Allemagne, une subvention fédérale de 20 % (programme d'efficacité énergétique, guichet fermé à l'été 2025) rendait le coût annuel total de l'électrique légèrement inférieur à celui du diesel[^topagrar-h] ; l'essai de Basse-Saxe conclut aussi que l'aide et une part de courant photovoltaïque rendent l'électrique compétitif[^lwk-aide]. Il n'existe pas d'aide équivalente en Wallonie (voir ci-dessous).

**Aides en Wallonie.** Aucune aide accessible ne réduit l'écart de prix entre l'électrique et le diesel. Voir [les aides publiques](../../aides.md).

- **AII.** La ligne « chargeur compact / nettoyeur d'étable / télescopique » est classée par puissance, avec un coût simplifié de {{ v('aii_chargeur_50ch_forfait', 0) }} sous 50 ch à 83 050 € à partir de 100 ch, quelle que soit la motorisation[^aii][^aii-liste]. L'aide se calcule sur ce coût simplifié, sans dépasser le prix réel[^aii]. Un valet de ferme de moins de 50 ch coûte plus que ce plafond en diesel comme en électrique : l'aide est donc la même pour les deux et ne paie pas le surcoût de l'électrique. La ligne ne coche ni « architecture verte » ni « résilience économique » : l'agriculteur seul touche le taux de base de {{ v('aii_taux_base', 0) }}[^aii], et l'investissement ne lui apporte aucun point pour atteindre le seuil de {{ v('aii_seuil_points', 0) }}[^aii]. Une CUMA touche {{ v('aii_cuma_taux_base', 0) }}, plus {{ v('aii_cuma_maj_6_membres', 0) }} avec au moins six membres, mais pas la majoration « architecture verte »[^aii]. Elle atteint le seuil de sélection de {{ v('aii_cuma_seuil_points', 0, unite=False) }} points dès quatre membres admissibles, sans case « architecture verte »[^aii]. Seul le tracteur électrique ou au biogaz de plus de 150 ch a une ligne propre[^aii-liste].
- **GREEN** : ses filières d'énergie renouvelable ne visent pas les engins, et il exclut le photovoltaïque et les batteries[^green-agw]. Le volet « économie d'énergie » exige au moins {{ v('green_seuil_pme', 0) }} d'investissement et un audit AMUREBA ; son application à un engin électrique n'a pas été trouvée[^green-agw]. GREEN ne se cumule pas avec l'AII sur le même investissement[^decret-2004]. Un exploitant aidé par l'AII ne peut pas non plus demander ce volet pendant cinq ans : il n'entre pas dans l'exception « énergie renouvelable » de l'AII (lecture de ce projet). Une CUMA n'est pas soumise à cet engagement[^agw-aii].
- **Déduction fédérale pour investissement.** Le télescopique et le chargeur électriques ne figurent pas sur la liste des transports sans émission de CO₂, qui ne vise que les cycles et deux-roues, les utilitaires, les camions et les bus[^arcir-dpi]. Au régime réel, seule la déduction de base de 10 % s'applique, comme pour un engin diesel ; au forfait, rien[^cir-dpi].
- **Le photovoltaïque** qui recharge l'engin est aidé par l'AII (fiche [Électricité du réseau](../energie/electricite-reseau.md)). C'est la seule aide qui améliore le bilan, par l'énergie et non par l'achat.

La vague 2 est inchangée.

### 2. Télescopique hybride au biométhane (vague 3)

New Holland a présenté à l'Agritechnica 2025 un prototype de télescopique hybride, le TH Hybrid Power : une batterie de 70 kWh et un moteur au gaz naturel comprimé de 75 kW (utilisable au biométhane) qui apporte la puissance des gros travaux et recharge la batterie. L'autonomie électrique annoncée est de 4 à 6 heures, pour une capacité de 4,2 t et une hauteur de levage de 7 à 9 m[^nh]. Aucun prix ni date de commercialisation n'étaient connus en novembre 2026.

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
- Éligibilité d'un chargeur électrique au volet « économie d'énergie » de GREEN (aucun texte ne parle d'engins). Le cumul de GREEN et de l'AII sur un même investissement est interdit (décret de 2004, article 3).
- Consommation réelle de l'exploitation, en litres par heure et en heures par an, pour remplacer les hypothèses.

## Sources

[^lwk]: Martin Vaupel (Landwirtschaftskammer Niedersachsen), « Hoflader im Test: Diesel oder elektrisch? », Bayerisches Landwirtschaftliches Wochenblatt, 29 octobre 2023, avec ses tableaux de mesures. https://www.wochenblatt-dlv.de/feld-stall/landtechnik/hoflader-test-diesel-elektrisch-574598
[^lwk-aide]: « Hofladertest Teil 3: Finanzielle Förderung macht E-Lader interessant », Land & Forst, 13 novembre 2023 (partie visible sans abonnement). https://www.landundforst.de/landwirtschaft/landtechnik/hofladertest-teil-3-finanzielle-foerderung-macht-e-lader-interessant-570303
[^faresin]: « Essai chargeur télescopique Faresin FS 7.40 Middle Excellence 100 », Réussir, 27 mai 2025. https://www.reussir.fr/machinisme/essai-chargeur-telescopique-faresin-fs-740-middle-excellence-100-un-engin-particulierement-stable
[^topagrar-h]: Josef Neiber (LfL Bayern), « Hoffahrzeuge mit Strom oder Diesel antreiben », top agrar, 9 juillet 2025. https://www.topagrar.com/betriebsleitung/news/hoffahrzeuge-mit-strom-oder-diesel-antreiben-20016039.html
[^topagrar-jcb]: « E-Lader von JCB mit leisen Sohlen und viel Kraft », top agrar Österreich, 23 février 2026. https://www.topagrar.com/oesterreich/e-lader-von-jcb-mit-leisen-sohlen-und-viel-kraft-20022753.html
[^weidemann]: « E-Flotte von Weidemann: Strom schlägt Diesel », top agrar Österreich, 27 avril 2026. https://www.topagrar.com/oesterreich/e-flotte-von-weidemann-strom-schlagt-diesel-20025026.html
[^dieci]: Fiche technique Dieci Mini Agri-e 26.6 (révision 04), Dieci, non datée, consultée en novembre 2026. https://dieci.com/ASSETS//Scheda_Tecnica/DOCCT0000139-EN-04.pdf
[^fwi]: « On test : JCB's debut battery-electric Loadall, the 525-60E », Farmers Weekly, 25 octobre 2021. https://fwi.co.uk/machinery/telehandlers/on-test-jcbs-debut-battery-electric-loadall-the-525-60e
[^pleinchamp]: « Les engins de manutention agricole se mettent à l'électrique », Pleinchamp (France), 16 juillet 2022. https://www.pleinchamp.com/actualite/les-engins-de-manutention-agricole-se-mettent-a-l-electrique
[^aii]: Arrêté ministériel du 23 février 2023 (aides aux investissements dans les exploitations agricoles), Wallex, version consolidée (dernière modification : arrêté ministériel du 11 mai 2026), annexe des coûts plafonds. https://wallex.wallonie.be/eli/arrete/2023/02/23/2023042748
[^aii-liste]: « Liste des investissements admissibles » (aide aux investissements agricoles, AII), SPW Agriculture, janvier 2026, consultée le 27 novembre 2026. https://agriculture.wallonie.be/files/accueil/Aides/AII/outils/Liste%20des%20investissements%20admissibles.pdf
[^green-agw]: Arrêté du Gouvernement wallon du 23 mai 2024 relatif aux primes à l'investissement (aides GREEN), article 10, Wallex, consulté le 27 novembre 2026. https://wallex.wallonie.be/sites/wallex/contents/acts/108/108350/1.html
[^nh]: « Ce chargeur télescopique hybride New Holland fonctionne au gaz et à l'électricité », Terre-net, 10 décembre 2025. https://www.terre-net.fr/new-holland/article/891389/ce-chargeur-telescopique-hybride-new-holland-fonctionne-au-gaz-et-a-l-electricit
[^decret-2004]: Décret du 11 mars 2004 relatif aux incitants destinés à favoriser la protection de l'environnement et l'utilisation durable de l'énergie, version en vigueur depuis le 1er janvier 2025, articles 3 (non-cumul, alinéas 4 et 5) à 5, Wallex, consulté le 27 novembre 2026. https://wallex.wallonie.be/eli/loi-decret/2004/03/11/2004200990
[^agw-aii]: Arrêté du Gouvernement wallon du 23 février 2023 relatif aux aides à l'installation et aux investissements, version en vigueur depuis le 1er janvier 2026, article 36, Wallex, consulté le 27 novembre 2026. https://wallex.wallonie.be/eli/arrete/2023/02/23/2023042313/2026/01/01
[^arcir-dpi]: Arrêté royal d'exécution du CIR 92, articles 47 et 49 et annexes II et IIbis (listes des investissements énergétiques et des transports sans émission de CO₂), texte coordonné « AR/CIR 92 – Revenus 2026 – Région wallonne » (PDF), Fisconetplus (SPF Finances), 20 août 2026, consulté le 27 novembre 2026. https://eservices.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/5870e65b-ae47-46c0-bc78-c690e4e9b727
[^cir-dpi]: Code des impôts sur les revenus 1992, articles 68 à 75, texte coordonné « CIR 92 – Revenus 2026 » (PDF), Fisconetplus (SPF Finances), 20 août 2026, consulté le 27 novembre 2026. https://eservices.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/65b63636-1955-4c59-bac2-dd3d85db6b30
