---
id: tracteur-diesel
titre: Tracteur diesel
domaine: traction
dependance_fossile: gasoil
alternatives: [réduction du travail du sol, tracteur électrique compact, tracteur au biométhane, huile de colza pure, gros tracteur électrique]
vague_meilleure_alternative: 1
statut: relu
maj: 2026-11-27
---

# Tracteur diesel

## En bref

Le tracteur diesel tire, porte et entraîne presque tout sur une exploitation, et son seul carburant est le gasoil : {{ v('gasoil_agricole_htva') }} HTVA en novembre 2026, contre {{ v('gasoil_agricole_fev2026_htva') }} en moyenne en février. Au prix actuel, un kWh de travail utile coûte {{ v('gasoil_kwh_utile') }} au gasoil et {{ v('pv_kwh_utile') }} avec l'électricité de ses propres panneaux, soit {{ v('ratio_gasoil_pv', 1) }} plus cher ; l'écart tient au prix d'avant-crise ({{ v('ratio_gasoil_pv', 1, scenario='bas') }}). La meilleure alternative n'est pas un autre tracteur : c'est d'avoir moins besoin de traction (vague 1). Les tracteurs légers peuvent passer à l'électrique, mais seulement derrière des panneaux photovoltaïques (vague 2) ; les lourds au biométhane, plutôt en collectif (vague 2). L'huile de colza, plus chère que le gasoil dans les trois scénarios de prix une fois le pressage payé, et le gros tracteur électrique à batterie restent à préparer (vague 3).

## Comment ça marche aujourd'hui

Un moteur diesel de quelques dizaines à plus de 300 kW entraîne les roues, la prise de force et l'hydraulique. Au travail, seule une partie de l'énergie du gasoil devient du travail utile : environ {{ v('rendement_moteur_diesel', 0) }} pour un tracteur récent en travaux des champs (estimé d'après les mesures de la DLG, moins au ralenti et en transport)[^dlg-pm], d'un litre qui contient {{ v('energie_litre_gasoil') }}[^red2].

Le poste le plus gourmand est le travail du sol. Dans un essai de longue durée d'Arvalis, en France (moyennes 1998-2008), l'itinéraire avec labour consommait environ 78 L/ha, contre 49 L/ha en semis direct[^tn].

Le prix du gasoil agricole suit celui du gasoil de chauffage. Le gasoil agricole se vendait autour de 80 centimes TVAC fin février 2026, puis autour de 1,2 € fin avril, après le début de la guerre au Moyen-Orient[^lalibre]. Dans ce projet, on l'estime à {{ v('gasoil_agricole_htva') }} HTVA en novembre 2026, contre {{ v('gasoil_agricole_fev2026_htva') }} en moyenne en février.

## Où entrent le pétrole et le gaz

- **Carburant** : le gasoil, raffiné à partir du pétrole brut.
- **AdBlue** : solution d'urée injectée dans l'échappement des moteurs récents. L'urée est fabriquée à partir d'ammoniac, donc de gaz naturel.
- **Lubrifiants, pneus, flexibles** : issus de la pétrochimie.
- **Logistique** : livraison du carburant et des pièces.

## Les alternatives

### 1. Réduire le besoin de traction (vague 1)

Moins travailler le sol diminue directement la consommation. Une comparaison française (essai Arvalis, moyennes 1998-2008) donne 78 L/ha en labour et 49 L/ha en semis direct, pour une marge nette quasi identique (171 €/ha contre 179 €/ha, aux prix de l'époque)[^tn]. Le travail superficiel, plus courant, économise en moyenne une vingtaine de litres par hectare et par an en sol limoneux, et jusqu'au double en sol argileux[^cirad].

Avec les prix de ce projet, le passage du labour au semis direct économise {{ v('gasoil_economise_semis_direct') }}, soit {{ v('valeur_gasoil_economise') }}.

Limites :

- le semis direct repose souvent sur le glyphosate pour détruire couverts et adventices : la dépendance fossile est déplacée vers la chimie, pas supprimée. À partir de 2027, le couvert de l'éco-régime « couverture longue du sol » ne pourra plus être détruit chimiquement, quelle que soit la date : le semis direct qui détruit ce couvert au glyphosate perd cette aide ({{ v('er_cls_entree_eur_ha', 0) }} à {{ v('er_cls_superieur_eur_ha', 0) }} sur toute la SAU, montants prévus)[^cls] [^am-er]. Voir la fiche [Herbicides](../protection/herbicides.md) ;
- il demande un semoir adapté et une bonne maîtrise technique : risque de manque d'eau pour la culture, de pullulation de limaces, de sol qui ressuie et se réchauffe plus lentement[^spw-sd] ;
- en France, il ne couvrait qu'environ 3 % des surfaces de grandes cultures selon une enquête Agreste de 2014[^tn-temoin].

**Aides.** Le semoir de semis direct ou simplifié figure dans la liste de l'aide aux investissements (AII), avec la case « architecture verte » : {{ v('aii_taux_pv', 0) }} du coût simplifié pour un agriculteur sans autre majoration, {{ v('aii_taux_cuma_av', 0) }} en CUMA d'au moins six membres (calculé)[^aii-liste][^am-aii]. La MAEC « Sol » (MR14) paie jusqu'à {{ v('maec_mr14_favorable_eur_ha', 0) }} quand le carbone du sol atteint l'état « favorable », mesuré en début et en fin de contrat[^mr14]. Elle n'accepte plus de nouvel engagement en 2027 : seuls les engagements en cours restent payés jusqu'à leur terme[^maec-sol-2027]. Ces aides confortent la vague 1 sans la conditionner. Voir [les aides publiques](../../aides.md).

### 2. Tracteur électrique compact (vague 2)

Le Fendt e107 Vario, le tracteur électrique de série de Fendt, affiche 50 kW en puissance nominale et 66 kW en pointe[^fendt], avec une batterie de 100 kWh[^fc]. Une étude de 2017 sur un tracteur électrique mesurait environ 26 kWh/h en déplacement, 32 kWh/h avec une herse rotative et 47 kWh/h avec un pulvérisateur à turbine, soit de 1,5 à 7 heures d'autonomie selon le travail[^t3n].

Coût de l'énergie par heure de travail (calculé, pertes de charge de la batterie comprises) :

| Énergie | Prix actuel | Fourchette des scénarios |
|---|---|---|
| Gasoil | {{ v('tracteur_gasoil_eur_h') }} | {{ fourchette('tracteur_gasoil_eur_h') }} |
| Électricité du réseau | {{ v('tracteur_reseau_eur_h') }} | {{ fourchette('tracteur_reseau_eur_h') }} |
| Photovoltaïque de la ferme | {{ v('tracteur_pv_eur_h') }} | fixe |

Sur {{ v('heures_tracteur_an') }} (base d'un barème d'entraide français)[^bareme-cuma], l'économie d'énergie atteint {{ v('tracteur_economie_an') }} avec du photovoltaïque, et encore {{ v('tracteur_economie_an', scenario='bas') }} au prix d'avant-crise. Sur le réseau, il n'y a pas d'économie : une fois les pertes de charge comptées, l'électricité du réseau revient plus cher que le gasoil, dans tous les scénarios. Le tracteur électrique n'a donc de sens que derrière ses propres panneaux. Le frein est le prix d'achat : un e107 d'occasion récente (360 h, mis en service en février 2025) s'affichait à 179 950 € HTVA en Allemagne[^topagrar-occ].

Conditions : beaucoup d'heures par an en travaux légers (cour, serre, maraîchage, vigne), recharge sur photovoltaïque, et des journées compatibles avec l'autonomie.

**Aides.** Aucune aide ne vise le surcoût du tracteur électrique compact. La liste de l'AII n'a de ligne propre au tracteur électrique qu'au-delà de 150 ch ; en dessous, elle ne le distingue pas du diesel[^aii-liste]. Seuls les panneaux qui le rechargent sont aidés, par l'AII ({{ v('aii_taux_pv', 0) }} du coût simplifié) ; GREEN exclut le photovoltaïque[^aii-liste][^green-agw]. Voir la fiche [Électricité du réseau](../energie/electricite-reseau.md). La déduction fédérale pour investissement de {{ v('dpi_thematique_pp', 0) }} ne s'applique pas : la liste des transports sans émission de CO₂ ne vise que les cycles et deux-roues, les utilitaires et camions, et les bus, pas les tracteurs[^arcir-dpi]. Au régime réel, il reste la déduction de base de 10 %, la même que pour un tracteur diesel[^cir-dpi]. La vague 2 est inchangée.

### 3. Tracteur au biométhane (vague 2)

Le New Holland T7.270 Methane Power se commande en Europe depuis fin 2025, avec des premières livraisons au printemps 2026[^nh]. Son réservoir standard contient 657 litres de gaz, et un réservoir additionnel de 480 litres porte l'autonomie jusqu'à 11 heures en transport[^nh]. Il peut rouler au biométhane tiré des effluents d'élevage, donc avec un carburant produit sur la ferme[^nh].

Conditions : un méthaniseur avec épuration du biogaz en biométhane et compression, sur la ferme ou à proximité. L'investissement se pense plutôt à plusieurs (CUMA, groupe de fermes, méthaniseur collectif) qu'à l'échelle d'une seule exploitation.

**Accises.** Le gaz naturel utilisé comme carburant est taxé à 0 € par MWh (droit d'accise, droit spécial et cotisation sur l'énergie), pour tout usage et pas seulement agricole[^lp-2004]. Le biométhane suit ce taux zéro : un produit énergétique sans taux propre est taxé comme le carburant équivalent[^lp-2004]. Comme le gasoil agricole est lui aussi exonéré, l'accise ne fait pas de différence entre les deux : seuls comptent le prix du gaz et l'investissement. Un taux zéro peut toutefois être relevé par une simple loi.

**Aides.** L'AII a une ligne « tracteur électrique ou au biogaz de plus de 150 ch », au coût simplifié de {{ v('aii_tracteur_elec_forfait', 0) }}, avec les cases « architecture verte » et « résilience économique »[^aii-liste]. Un tracteur au biométhane de plus de 150 ch en relève. L'aide vaut {{ v('aii_taux_pv', 0) }} de ce coût pour un agriculteur sans autre majoration, {{ v('aii_taux_cuma_av', 0) }} pour une CUMA d'au moins six membres (calculé)[^am-aii]. La voie collective est donc aussi la mieux aidée. L'aide ne couvre ni l'épuration ni la compression du biogaz. La vague 2 est inchangée.

### 4. Huile de colza pure (vague 3)

L'huile de colza pressée à froid peut alimenter un moteur diesel adapté. Des tracteurs ont été vendus d'usine avec un double réservoir, comme le Deutz-Fahr Agrotron M650 « Natural Power » testé à Gembloux : démarrage au gasoil, puis passage à l'huile[^lumaye]. En France, une petite presse de 2 à 4 L/h coûtait de l'ordre de 5 000 à 6 000 € en 2005 (référence ancienne)[^an-presse].

Avec les données du projet, un litre d'huile revient à {{ v('huile_cout_litre') }} une fois le tourteau vendu ou donné aux animaux (calculé). Ce coût comprend le pressage, compté à {{ v('pressage_cout', 2) }} : c'est le tarif d'une CUMA française dont la presse est amortie, qui facturait 0,50 à 0,60 €/L avant cet amortissement[^entraid-presse]. Ramené à l'énergie d'un litre de gasoil, cela fait {{ v('huile_cout_eq_gasoil') }}, contre {{ v('gasoil_agricole_htva') }} pour le gasoil agricole, hors accises dans les deux cas : l'huile revient {{ v('huile_ecart_gasoil', 2) }} plus cher par litre équivalent (calculé). Les démarches administratives décrites plus bas ne sont pas comptées. Pour couvrir ses besoins, une ferme en labour devrait cultiver du colza sur environ {{ v('part_surface_colza', 0) }} de sa surface (calculé).

L'huile reste plus chère que le gasoil dans les trois scénarios : de {{ v('huile_ecart_gasoil', 2, scenario='haut') }} par litre équivalent au prix haut à {{ v('huile_ecart_gasoil', 2, scenario='bas') }} au prix d'avant-crise (calculé). Quand le gasoil monte, la graine de colza monte aussi, et l'huile ne prend pas l'avantage. Le pressage pèse lourd : une presse fermière déjà amortie, qui ne coûterait que quelques centimes par litre, ramènerait l'écart à peu près à zéro au prix de crise, mais sans gain net (référence française ancienne, voir « À vérifier »).

**Pourquoi vague 3.** Avec les coûts sourcés, l'huile de colza n'est rentable dans aucun scénario de prix. Elle garde deux intérêts que ce calcul ne chiffre pas : l'autonomie, avec un stock de carburant produit sur la ferme en cas de rupture d'approvisionnement, et le tourteau gras pour les animaux (voir la fiche [Concentrés importés](../elevage/concentres-importes.md)). Elle ne deviendrait rentable qu'avec un pressage bon marché et un gasoil durablement cher face au colza : c'est à préparer, pas à généraliser.

**Est-ce autorisé ?** Oui, sous conditions, pour l'agriculteur qui utilise sa propre huile dans ses tracteurs. Les textes officiels lus en novembre 2026 donnent ceci :

- l'huile de colza destinée à servir de carburant est un « produit énergétique » au sens de la loi sur les accises (codes NC 1507 à 1518). Sans exonération, elle est taxée au taux du gasoil qu'elle remplace[^lp-2004] ;
- l'article 429, § 2, i), de la loi-programme du 27 décembre 2004 exonère d'accise les produits énergétiques et l'électricité utilisés exclusivement pour des travaux agricoles et horticoles, la pisciculture et la sylviculture. Le § 3 précise que cela vaut comme carburant pour les tracteurs agricoles et les engins agricoles automoteurs. Ce texte vise tous les produits énergétiques, sans exclure l'huile de colza ; c'est la même exonération que celle du gasoil rouge[^lp-2004] ;
- l'ancienne exonération propre à l'huile de colza (point m de l'article 429, § 2) visait l'huile vendue directement par l'agriculteur à l'utilisateur final. Après une autorisation européenne d'aide d'État obtenue en 2014, la Commission l'a jugée caduque. La loi du 25 décembre 2017 l'a abrogée, à partir du 8 janvier 2018[^chambre-2017][^loi-2017]. Le texte consolidé au 1er novembre 2026 confirme que ce point m) est vide[^lp-2004] ;
- la circulaire des accises en vigueur (2026/C/82 du 7 septembre 2026) précise la marche à suivre. Pour bénéficier de l'exonération agricole, il faut une autorisation « produits énergétiques et électricité » de type « utilisateur final », et l'huile de colza figure parmi les produits que cette autorisation peut couvrir. L'huile carburant doit être produite dans un entrepôt fiscal, donc par un entrepositaire agréé, avec un registre « 592 Colza » qui suit graines et huile. Ce registre prévoit une ligne pour l'huile sortie en exonération contre le numéro d'autorisation « utilisateur final »[^circ-2026]. Une dérogation du SPF Économie n'est exigée que si l'huile est mise sur le marché[^circ-2026] ;
- la circulaire de 2017 décrivait explicitement « la vente ou l'usage propre » d'huile de colza dans le cadre de l'exonération agricole, avec le code produit 7913. Elle dispensait du statut d'entrepositaire l'agriculteur qui fait presser ses graines par un tiers et ne vend pas l'huile[^circ-2017]. Ce passage a disparu de la circulaire de 2026, qui exige toujours un entrepôt fiscal pour produire l'huile[^circ-2026].

En résumé, presser son colza et brûler l'huile dans ses propres tracteurs, pour des travaux agricoles, se fait sans accise. Il faut pour cela deux démarches auprès des Douanes et Accises (statut d'entrepositaire agréé pour le pressage, autorisation « utilisateur final » pour l'usage) et tenir le registre. Vendre de l'huile carburant à ses voisins sans accise n'est plus possible depuis 2018, sauf à un acheteur qui détient lui-même une autorisation « utilisateur final ». Le pressage peut aussi se faire chez un tiers (CUMA, voisin, huilerie) s'il est entrepositaire agréé : il tient le registre, qui prévoit des graines d'autres producteurs, et livre l'huile sans accise à l'agriculteur qui présente son autorisation « utilisateur final »[^circ-2026]. L'agriculteur n'a alors pas besoin du statut d'entrepositaire[^circ-2017]. On ne sait pas si le presseur doit aussi obtenir la dérogation du SPF Économie dans ce cas. Côté technique, le moteur doit être prévu pour l'huile ou converti par un atelier spécialisé.

**Aides.** Aucune : la presse à huile ne figure pas dans la liste de l'AII[^aii-liste].

### 5. Gros tracteur électrique à batterie (vague 3)

Un tracteur d'environ 200 kW consomme près de {{ v('tracteur_lourd_conso_gasoil', 0) }} de gasoil en travail du sol lourd (labour, déchaumage), selon les mesures de la DLG[^dlg-pm]. Pour une journée de ce travail, il faudrait une batterie d'environ {{ v('batterie_journee_lourde', 0) }} (calculé, pertes de recharge comprises), soit {{ v('batterie_masse_journee_lourde', 1) }} de batteries. Le prototype HUE-Trac 620, une conversion de Fendt série 600 par le néerlandais Humabo, embarque 400 kWh, et John Deere a présenté un tracteur électrique avec recharge rapide Kreisel à la Grüne Woche 2026[^topagrar]. L'électrique ne représentait que 0,18 % environ du marché mondial des tracteurs en 2025[^gmi].

L'AII aide le tracteur électrique de plus de 150 ch : {{ v('aii_taux_pv', 0) }} d'un coût simplifié de {{ v('aii_tracteur_elec_forfait', 0) }} pour un agriculteur sans autre majoration (calculé)[^aii-liste][^am-aii]. Cela ne change pas la vague : la limite est la batterie, pas le prix.

Pistes pour contourner la batterie : alimentation par câble, batteries échangeables, ou remplacement d'un gros tracteur par plusieurs petits robots.

## Ce qui ferme la boucle

- Le soleil sur les toitures alimente les tracteurs légers et les engins de cour.
- Les effluents d'élevage deviennent du biométhane pour les tracteurs lourds, et le digestat retourne au champ.
- Le colza donne l'huile pour le moteur et le tourteau pour les animaux, dont le fumier fertilise le colza suivant.
- L'ordre logique : d'abord réduire la traction, ensuite électrifier le léger, puis convertir le lourd avec un carburant produit à la ferme, en collectif.

## À vérifier

- Prix réel du gasoil agricole sur facture (ici estimé à partir du gasoil de chauffage).
- Huile de colza pressée par un tiers : la dérogation du SPF Économie (arrêté royal du 4 mars 2005) est-elle exigée quand l'huile est rendue à l'agriculteur ? Code produit agricole actuel de l'huile de colza (7913 en 2017). Texte consolidé de l'article 429 vérifié sur Fisconetplus, pas sur Justel (inaccessible).
- Historique de l'exonération de l'huile de colza entre 2006 et 2015 (suspension annoncée fin 2012 par le Conseil des ministres) : communiqués news.belgium.be inaccessibles.
- Norme de qualité de l'huile carburant (DIN 51605 citée couramment) : non sourcée ici.
- Autonomie du T7.270 Methane Power pour un poste d'ensilage de 8 heures (communiqué CNH du 29 septembre 2025, non lu) et article The Western Producer du 14 novembre 2025 (non lu).
- Semis direct sur les sols limoneux wallons sensibles au tassement : la fiche des Chambres d'agriculture citée jusqu'ici n'est plus en ligne.
- Formalités d'accise d'une ferme qui comprime et utilise son propre biométhane (statut de distributeur, article 424 de la loi-programme de 2004).
- Garantie constructeur et conformité des émissions (Stage V) d'un moteur converti à l'huile.
- Prix neuf d'un Fendt e107 face à un Fendt 207 diesel équivalent.
- Résultats du test 2026 de la Landwirtschaftskammer Niedersachsen comparant e107 et 207, annoncés pour octobre 2026[^topagrar].
- Disponibilité du T7.270 Methane Power et des stations de biométhane en Belgique.
- Consommations horaires réelles sur l'exploitation, qui remplacent les estimations (barème Cuma français, mesures DLG sur banc).
- Coût du pressage de l'huile de colza en Wallonie : aucune référence récente trouvée (fiche économique n° 4 de ValBiom retirée et non archivée ; fiches 2, 3 et 7 lisibles dans l'archive web, sans coût). Une presse fermière amortie ne coûtait que quelques centimes par litre en France en 2006 (Brunschwig et Lamy, revue Fourrages n° 187, citée par la note de l'hypothèse sur le coût du pressage), référence introuvable en ligne (table du n° 187 absente du site de l'AFPF) : c'est elle qui décide si l'huile rejoint le prix du gasoil au prix de crise.
- Rendement en huile d'une presse fermière (de 240 à 400 L/t selon les sources et le réglage de la presse) : à mesurer sur la presse utilisée.
- Points de sélection AII du tracteur au biogaz (« architecture verte » et « résilience économique ») : 10 selon la grille de l'annexe 2, 5 selon l'article 6. Dans les deux cas, il faut au moins un autre critère (jeune, bio, zone à contraintes, polyculture, prairie permanente) pour atteindre 15 points. À demander à l'Organisme payeur de Wallonie.

## Sources

[^tn]: « Non-labour : comparatif économique semis direct, travail simplifié », Terre-net, 2 juin 2009 (mis à jour le 12 avril 2023), d'après l'essai de longue durée d'Arvalis (moyennes 1998-2008). https://www.terre-net.fr/observatoire-technique-culturale/appros-phytosanitaire/article/non-labour-comparatif-economique-semis-direct-travail-simplifie-culture-216-55967.html
[^cirad]: Labreuche J., Lellahi A., Malaval C., Germon J.-C., « Impact des techniques culturales sans labour (TCSL) sur le bilan énergétique et le bilan des gaz à effet de serre des systèmes de culture », Cahiers Agricultures, vol. 20, n° 3, mai-juin 2011, p. 204-215. https://revues.cirad.fr/index.php/cahiers-agricultures/article/download/30920/30680/31155
[^spw-sd]: Fiche technique n° 11 « Semis direct » (BCAE 5), SPW Agriculture, Ressources naturelles et Environnement, version du 1er octobre 2026. https://agriculture.wallonie.be/files/accueil/ruralit%c3%a9/Protection_Sols_Agricoles/BCAE%205(2026)/Fiche%2011-%20Semis%20direct.pdf
[^tn-temoin]: « Trois producteurs témoignent des atouts et contraintes de leurs pratiques », Terre-net, 14 juin 2019 (mis à jour le 15 septembre 2022). https://www.terre-net.fr/travail-du-sol/article/149029/trois-producteurs-temoignent-des-atouts-et-contraintes-de-leurs-pratiques
[^lalibre]: « Notre système agricole n'est pas viable dans un monde instable », La Libre, 27 avril 2026. https://www.lalibre.be/belgique/2026/04/27/notre-systeme-agricole-nest-pas-viable-dans-un-monde-instable-ZGHFBVHRJVAXXAAPLCPOTVD7KM/
[^fendt]: Fendt e100 Vario, fiche constructeur (non datée, consultée le 26 novembre 2026). https://fendt.com/e100-vario
[^fc]: « Tractor of the Year 2025 : TotY Utility – Fendt e107 Vario », Farm Contractor & Large Scale Farmer, 19 septembre 2024. https://www.farmcontractormagazine.com/?p=104941
[^t3n]: « Erster Elektro-Traktor von Fendt », t3n, 24 novembre 2024. https://t3n.de/news/erster-elektro-traktor-von-fendt-fahrzeug-landwirtschaft-1657809/
[^topagrar-occ]: Annonce Fendt e107 V Vario Profi+, top agrar (non datée, consultée le 26 novembre 2026). https://www.topagrar.com/technik/landtechnik/traktoren/e107%20v%20vario%20profi+/8548625/
[^nh]: « New Holland T7.270 Methane Power tractor now available to order », New Holland, 23 septembre 2025. https://www.newholland.com/en-ie/europe/new-holland-world/news/2025/t7-270-methane-power-tractor-now-available-to-order
[^lumaye]: Lumaye F., « Comparaison entre l'huile de colza pure et le gasoil EN590 » (texte : « L'utilisation de l'huile de colza dans les tracteurs agricoles »), Livre Blanc Céréales, Gembloux Agro-Bio Tech (ULiège), 29 février 2012. https://orbi.uliege.be/bitstream/2268/121592/1/LB%202012%20F%20Lumaye%20final.doc
[^an-presse]: Question écrite n° 70575 sur les biocarburants agricoles, Assemblée nationale (12e législature), publiée le 26 juillet 2005, réponse du 20 septembre 2005. https://questions.assemblee-nationale.fr/dyn/12/questions/QANR5L12QE70575.pdf
[^lp-2004]: Loi-programme du 27 décembre 2004, chapitre XVIII « La taxation des produits énergétiques et de l'électricité », articles 415, 416, 418, 419 et 429, version consolidée au 1er novembre 2026, Fisconetplus (SPF Finances), consultée le 26 novembre 2026. https://eservices.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/26dabd4c-8544-45a7-a6a2-32e0e99e6349
[^chambre-2017]: Projet de loi portant des dispositions fiscales diverses IV, Chambre des représentants, doc. 54 2792/001, 24 novembre 2017 (exposé des motifs de l'abrogation de l'article 429, § 2, m). https://www.lachambre.be/FLWB/pdf/54/2792/54K2792001.pdf
[^loi-2017]: Loi du 25 décembre 2017 portant des dispositions fiscales diverses IV, article 26, Moniteur belge du 29 décembre 2017, en vigueur le 8 janvier 2018, Fisconetplus (SPF Finances). https://eservices.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/d72db282-5973-4377-b1ca-ecfe0e81df77
[^circ-2017]: Circulaire 2017/C/51 concernant le code accises produits énergétiques et électricité, SPF Finances, 1er août 2017, §§ 307 à 318, dont §§ 314 et 315 (pressage par un tiers) (copie Lex.be, abrogée depuis). https://lex.be/en/doc/be/fisconet-fiscal-discipline/circulaire-2017c51-concernant-le-code-accises-produits-energetiques-et-electricite-1-august-2017-befp_201708014a3f4d58_fr
[^circ-2026]: Circulaire 2026/C/82 concernant les produits énergétiques et l'électricité, SPF Finances (Administration générale des Douanes et Accises), 7 septembre 2026, §§ 21 à 23, 113, 115, 116, 292 et 293, annexe III (registre 592 « Colza », colonnes 3b et 4c), Fisconetplus. https://eservices.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/7c2dec9f-a0dc-4c3b-9fce-27f229f26a17
[^topagrar]: « John Deere, Fendt, China-Traktor : was neue E-Schlepper Landwirten bieten », top agrar, 8 juin 2026. https://www.topagrar.com/technik/news/john-deere-fendt-china-traktor-was-neue-e-schlepper-landwirten-bieten-20026099.html
[^cls]: « Eco-régime couverture longue du sol », Portail de l'agriculture wallonne (SPW), page modifiée le 17 avril 2026, consultée le 27 novembre 2026. https://agriculture.wallonie.be/home/aides/pac-2023-2027-description-des-interventions/eco-regimes/eco-regime-couverture-longue-du-sol.html
[^mr14]: « MAEC Sol – MR14 », Portail de l'agriculture wallonne (SPW), page modifiée le 4 juin 2026, consultée le 27 novembre 2026. https://agriculture.wallonie.be/home/aides/pac-2023-2027-description-des-interventions/mesures-agro-environnementales-et-climatiques/maec-sol---mr14.html
[^aii-liste]: « Liste des investissements admissibles » (aide aux investissements agricoles, AII), SPW Agriculture, janvier 2026, consultée le 27 novembre 2026. https://agriculture.wallonie.be/files/accueil/Aides/AII/outils/Liste%20des%20investissements%20admissibles.pdf
[^am-aii]: Arrêté ministériel du 23 février 2023 exécutant l'arrêté du Gouvernement wallon du 23 février 2023 relatif aux aides à l'installation et aux investissements, version consolidée (modifications des 15 janvier et 11 mai 2026), articles 5 et 6, annexe 3, Wallex, consulté le 27 novembre 2026. https://wallex.wallonie.be/eli/arrete/2023/02/23/2023042748
[^green-agw]: Arrêté du Gouvernement wallon du 23 mai 2024 relatif aux primes à l'investissement (aides GREEN), article 10, Wallex, consulté le 27 novembre 2026. https://wallex.wallonie.be/sites/wallex/contents/acts/108/108350/1.html
[^dlg-pm]: Fiche de mesures DLG PowerMix du Massey Ferguson 8S.265, DLG (Deutsche Landwirtschafts-Gesellschaft), 9 mars 2026, lue le 27 novembre 2026 ; consommations comparées avec les fiches DLG des John Deere 6R 250 et Fendt 724 (non datées). https://pruefberichte.dlg.org/filestorage/PM%20Datenblatt_MF_8S265_DVT_20260309.pdf
[^red2]: Directive (UE) 2018/2001 relative à la promotion de l'utilisation de l'énergie produite à partir de sources renouvelables (RED II), annexe III (pouvoir calorifique inférieur des carburants), 11 décembre 2018, texte lu sur legislation.gov.uk le 27 novembre 2026. https://www.legislation.gov.uk/eudr/2018/2001/annex/III
[^bareme-cuma]: « Barème d'entraide 2024-2025 », Cuma de l'Est de la France, novembre 2024 (coûts des tracteurs sur une base de 700 h/an, variantes à 500 et 900 h/an ; données françaises), lu le 27 novembre 2026. https://www.cuma.fr/app/uploads/sites/20/2024/11/bareme-entraide-2024-2025.pdf
[^entraid-presse]: « Une presse pour l'huile carburant et l'autonomie protéique », Entraid, 24 mai 2023 (CUMA de la Verte Prairie du Lyonnais), prix français, lu le 27 novembre 2026. https://www.entraid.com/articles/une-presse-a-huile-pour-le-carburant-et-lautonomie-proteique
[^gmi]: « Electric Tractor Market Size & Share 2026-2035 », Global Market Insights, rapport GMI8868, août 2026. https://www.gminsights.com/industry-analysis/electric-tractor-market
[^am-er]: Arrêté ministériel du 23 février 2023 exécutant l'arrêté du Gouvernement wallon du 23 février 2023 relatif à l'aide aux éco-régimes, version consolidée en vigueur au 1er janvier 2026, articles 4 et 8, Wallex, consulté le 27 novembre 2026. https://wallex.wallonie.be/files/pdfs/22/87955_Arr%C3%AAt%C3%A9_minist%C3%A9riel_ex%C3%A9cutant_l'arr%C3%AAt%C3%A9_du_Gouvernement_wallon_du_23_f%C3%A9vrier_2023_relatif_%C3%A0_l'aide_aux_%C3%A9co-r%C3%A9gimes_01-01-2026-.pdf
[^maec-sol-2027]: « MAEC Sol : pas de nouveaux engagements en 2027, les engagements en cours maintenus jusqu'à leur terme », communiqué, Portail de l'agriculture wallonne, 18 novembre 2026, consulté le 27 novembre 2026. https://agriculture.wallonie.be/home/communiques/presses/maec-sol-pas-de-nouveaux-engagements-en-2027-les-engagements-en-cours-maintenus-jusqu-a-leur-terme.html
[^cir-dpi]: Code des impôts sur les revenus 1992, articles 68 à 75, texte coordonné « CIR 92 – Revenus 2026 » (PDF), Fisconetplus (SPF Finances), 20 août 2026, consulté le 27 novembre 2026. https://eservices.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/65b63636-1955-4c59-bac2-dd3d85db6b30
[^arcir-dpi]: Arrêté royal d'exécution du CIR 92, articles 47 et 49 et annexes II et IIbis (listes des investissements énergétiques et des transports sans émission de CO₂), texte coordonné « AR/CIR 92 – Revenus 2026 – Région wallonne » (PDF), Fisconetplus (SPF Finances), 20 août 2026, consulté le 27 novembre 2026. https://eservices.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/5870e65b-ae47-46c0-bc78-c690e4e9b727
