---
id: automoteurs-recolte
titre: Moissonneuse et ensileuse
domaine: traction
dependance_fossile: gasoil
alternatives: [mutualisation de la récolte, HVO, huile végétale, moissonneuse hybride ou électrique, biométhane]
vague_meilleure_alternative: 1
statut: relu
maj: 2026-11-27
---

# Moissonneuse et ensileuse

## En bref

La moissonneuse-batteuse et l'ensileuse automotrice sont les plus gros moteurs de la ferme : de 190 à 700 chevaux selon le barème français cité plus bas, pour quelques centaines d'heures par an[^bareme]. Une moissonneuse de 300 ch brûle environ {{ v('moisson_conso_l_h', 0) }} de gasoil, soit {{ v('moisson_conso_l_ha', 0) }} de céréales : au prix actuel du gasoil agricole, cela fait {{ v('moisson_gasoil_eur_ha', 0) }} pour la moisson et {{ v('ensileuse_gasoil_eur_ha', 0) }} pour l'ensileuse en maïs (calculé). Partager la machine (CUMA, entreprise) réduit nettement le coût à l'hectare (vague 1), mais pas le gasoil brûlé ; en Wallonie, l'aide à l'investissement pour une moissonneuse ou une ensileuse est réservée aux CUMA. Le seul carburant renouvelable prêt à l'emploi est le HVO100, autorisé par Claas dans ses machines récentes : il coûte environ {{ v('hvo_surcout_litre', 2) }} de plus par litre de gasoil remplacé, soit {{ v('moisson_hvo_surcout_ha', 0) }} de plus à la moisson (calculé), et n'est moins cher que le gasoil dans aucun scénario (vague 3). L'huile végétale pure, les moissonneuses hybrides ou électriques et le biométhane restent à préparer (vague 3).

## Comment ça marche aujourd'hui

**La moissonneuse-batteuse** coupe la céréale, la bat (batteur et secoueurs, ou rotor), nettoie le grain et broie ou dépose la paille. Le barème d'entraide des chambres d'agriculture et des Cuma de l'Est de la France (données françaises) décrit des machines de 190 à plus de 530 ch, pour 125 à 900 ha par an et des débits de 1,5 à 4,6 ha/h[^bareme]. Pour une machine de 290 à 320 ch et une coupe de 6 m, il retient {{ v('moisson_debit_ha_h') }} et {{ v('moisson_surface_an', 0) }}, soit environ {{ v('moisson_heures_an', 0) }} de battage (calculé).

**L'ensileuse automotrice** ramasse l'herbe préfanée ou coupe le maïs sur pied, le hache et l'éclate, puis le souffle dans une remorque tirée à côté. Le même barème décrit des ensileuses de 330 à 700 ch, qui récoltent de 1,5 à 3,6 ha de maïs par heure[^bareme]. Le chantier complet (remorques, tassement au silo) est traité dans la fiche [Ensilage et enrubannage](../elevage/fourrages-recoltes.md).

**Ce qu'elles consomment.** Le barème calcule la consommation à partir de la puissance : 0,21 L par cheval et par heure, à 70 % de charge moteur[^bareme]. Ce sont donc des valeurs de calcul, pas des mesures :

| Machine (barème français 2024-2025) | Consommation horaire | Consommation par hectare |
|---|---|---|
| Moissonneuse de 190 à 220 ch | 30,9 L/h | 20,6 L/ha[^bareme] |
| Moissonneuse de 290 à 320 ch | {{ v('moisson_conso_l_h', 1) }} | {{ v('moisson_conso_l_ha', 1) }} |
| Moissonneuse de plus de 530 ch | 79,4 L/h | 17,3 L/ha[^bareme] |
| Ensileuse de 330 à 350 ch (maïs) | 50,0 L/h | 33,3 L/ha[^bareme] |
| Ensileuse de 500 ch (maïs) | {{ v('ensileuse_conso_l_h', 1) }} | {{ v('ensileuse_conso_l_ha', 1) }} |
| Ensileuse de 700 ch (maïs) | 102,9 L/h | 28,6 L/ha[^bareme] |

Les grosses machines brûlent plus par heure mais à peu près autant par hectare, car elles avancent plus vite.

**Ce qu'elles coûtent.** Ce sont des machines chères pour peu d'heures. Dans le barème, une moissonneuse de 290 à 320 ch neuve vaut 252 120 € HT[^bareme]. Le prix moyen d'une ensileuse de 500 ch était de 378 000 € en 2024 en France, selon Chambres d'agriculture France[^agreste]. Sur 576 moissonneuses de Cuma françaises, le prix de revient moyen est de 85 €/ha, hors carburant et chauffeur. L'amortissement en représente 70 %[^entraid].

**Qui récolte ?** En France, en 2023, 52 % des exploitations qui utilisent une automotrice de récolte en sont propriétaires. Pour l'ensileuse, 53,2 % des utilisateurs passent par une Cuma et 13 % seulement en possèdent une[^agreste]. On n'a pas trouvé de chiffre équivalent pour la Wallonie (voir « À vérifier »). La profession y est représentée par Agro-Service (Landbouw-Service), qui regroupe plus de 800 entrepreneurs de travaux agricoles, entrepreneurs de pulvérisation et négociants en Belgique[^agroservice].

## Où entrent le pétrole et le gaz

- **Carburant** : le gasoil, raffiné à partir du pétrole. C'est de loin le premier poste fossile de la machine.
- **AdBlue** : les moteurs récents (norme Stage V) injectent une solution d'urée dans l'échappement ; le barème la compte dans le coût d'utilisation[^bareme]. L'urée est fabriquée à partir d'ammoniac, donc de gaz naturel.
- **Lubrifiants, pneus, chenilles, courroies** : issus de la pétrochimie.
- **Fabrication** : plusieurs tonnes d'acier et de composants par machine, pour quelques centaines d'heures de travail par an. Moins on a de machines pour la même surface, moins ce poste pèse.
- **Logistique du chantier** : les tracteurs et remorques qui suivent la machine (transport du grain ou du fourrage, tassement du silo).

## Les alternatives

### 1. Mutualiser la récolte : CUMA, entreprise, copropriété (vague 1)

Le coût d'une machine de récolte dépend surtout de la surface sur laquelle on l'amortit. Dans le barème français, la même moissonneuse de 290 à 320 ch revient, carburant et chauffeur compris (gasoil à 1,20 € HT/L), à 144 €/ha sur 230 ha par an, 122 €/ha sur 300 ha et 109 €/ha sur 370 ha[^bareme]. Dans l'échantillon des Cuma françaises, dépasser 450 ha par an fait passer sous la moyenne de 85 €/ha, hors carburant et chauffeur[^entraid].

Repères de prix (prix français, faute de barème belge publié) :

| Mode de récolte | Moisson | Ensilage de maïs |
|---|---|---|
| Cuma, Bretagne, 2024 | 35 à 50 €/ha (cotisation et chauffeur en plus)[^pb] | non indiqué |
| Entreprise de travaux agricoles, Bretagne, 2024 | 70 à 85 €/ha[^pb] | 130 à 160 €/ha[^pb] |
| Coût de revient complet d'une moissonneuse, barème de l'Est | 109 à 144 €/ha selon la surface[^bareme] | ensileuse seule : 160 à 208 €/ha avec chauffeur[^bareme] |

En Wallonie, la Cuma « Système D », créée en 1992 autour de l'achat d'une moissonneuse, estimait en 2013 ses coûts à environ 60 % de ceux d'une entreprise de travaux agricoles. Elle couvrait alors plus de 400 ha et servait aussi aux achats groupés de carburant[^sysd].

**Aides.** Dans la liste de l'aide aux investissements (AII), la moissonneuse-batteuse et l'ensileuse automotrice à maïs ont chacune une ligne **réservée aux CUMA** : un agriculteur seul n'y a pas droit[^aii-liste]. Ces lignes ne cochent ni « architecture verte » ni « résilience économique »[^aii-liste]. Une CUMA touche donc le taux de base de {{ v('aii_cuma_taux_base', 0) }} du coût simplifié, plus {{ v('aii_cuma_maj_6_membres', 0) }} avec au moins six membres admissibles, sans dépasser le prix réel[^am-aii]. Le taux de {{ v('aii_taux_cuma_av', 0) }} (calculé) ne vaut que pour les lignes « architecture verte » et ne s'applique pas ici. L'aide abaisse l'amortissement, qui fait 70 % du coût de revient d'une moissonneuse de Cuma[^entraid] : elle renforce la voie collective. Aucune aide ne vise le gasoil ni le HVO. Voir [les aides publiques](../../aides.md).

Pour situer l'enjeu : le gasoil de la moissonneuse ne pèse que {{ v('moisson_gasoil_eur_ha', 0) }} au prix actuel (calculé), contre 85 €/ha pour la seule détention et l'entretien de la machine[^entraid]. C'est donc sur la machine, plus que sur le carburant, que la mutualisation fait gagner.

Limites :

- **La mutualisation ne supprime pas le gasoil.** Une machine partagée brûle à peu près autant par hectare qu'une machine en propre. Les trajets sur route entre les fermes peuvent même en ajouter (hypothèse). Elle réduit le nombre de machines à fabriquer, mais pas la dépendance au carburant.
- Elle a un prix en organisation : la récolte se fait à la date de la machine, pas forcément au meilleur jour pour chaque parcelle. Le recours à l'entreprise pose le même problème de disponibilité en pointe[^pb].
- Son vrai intérêt pour sortir du pétrole est indirect : un groupe qui partage une machine peut aussi partager le surcoût d'un carburant renouvelable (HVO), une cuve, ou plus tard une station de biométhane.

### 2. HVO100 (vague 3)

**Ce que c'est.** Le HVO (huile végétale hydrotraitée) est un diesel paraffinique fabriqué en faisant réagir avec de l'hydrogène des huiles et graisses, surtout des déchets et résidus (huiles de friture usagées, graisses animales), avec aussi des huiles végétales[^claas]. Il relève de la norme EN 15940 des diesels paraffiniques et se mélange au gasoil en toute proportion[^claas]. Une machine Stage V autorisée n'a besoin d'aucune modification, et la cuve de la ferme reste utilisable[^claas][^dlg].

**Compatibilité.** Depuis le 1er octobre 2023, Claas autorise le HVO dans toutes ses machines Stage V : moissonneuses Lexion et Trion, ensileuses Jaguar, tracteurs. Elles quittent même l'usine avec un plein de HVO[^claas]. Dans un essai de la DLG sur un tracteur Valtra, la puissance est restée la même ; il a fallu environ 3 à 4 % de litres en plus, car le HVO est moins dense[^dlg]. On n'a pas lu les positions de John Deere, New Holland, Case IH ou Fendt pour leurs machines de récolte (voir « À vérifier »).

**Disponibilité en Belgique.** MAES vend du HVO100 dans 25 stations en Belgique (mai 2025)[^maes25]. Le tarif officiel belge des produits pétroliers ne publie pas de prix propre au HVO : il le range dans le « diesel XTL »[^carbu]. Son prix maximum à la pompe a été en moyenne de {{ v('diesel_xtl_tvac', 2) }} TVAC du 1er au 26 novembre 2026, contre {{ v('diesel_b7_tvac', 2) }} pour le diesel B7[^statbel-nov]. En février 2026, avant la crise, il était de {{ v('diesel_xtl_tvac', 2, scenario='bas') }} contre {{ v('diesel_b7_tvac', 2, scenario='bas') }}[^statbel-mois]. Le prix du XTL a donc beaucoup moins monté que celui du gasoil.

**Fiscalité.** La circulaire des accises de 2026 cite les moissonneuses parmi les engins agricoles automoteurs qui peuvent rouler en exonération d'accise, et l'exonération agricole vise tous les produits énergétiques, pas seulement le gasoil rouge[^circ-2026]. Il faut, comme pour le gasoil rouge, une autorisation « utilisateur final »[^circ-2026]. Le régime général de cette exonération est décrit dans la fiche [Tracteur diesel](tracteur-diesel.md#4-huile-de-colza-pure-vague-3). Une difficulté pratique reste : un commerçant qui n'est pas entrepositaire agréé ne peut livrer en exonération agricole que du gasoil marqué (rouge), du pétrole lampant marqué, du fioul lourd ou du GPL[^circ-2026]. Le HVO exonéré doit donc probablement venir d'un entrepositaire agréé (à confirmer, voir « À vérifier »).

**Ce que ça coûte.** Faute de prix publié pour le HVO agricole, on l'estime : au prix routier du XTL, on retire le même écart que celui qui sépare le diesel routier du gasoil agricole (accises et autres différences). Cela donne {{ v('hvo_agricole_htva') }} HTVA (estimation calculée, {{ fourchette('hvo_agricole_htva') }} selon les scénarios).

| Au prix… | Surcoût par litre de gasoil remplacé | Moisson | Ensileuse (maïs) | Moissonneuse sur {{ v('moisson_surface_an', 0) }} |
|---|---|---|---|---|
| actuel (novembre 2026) | {{ v('hvo_surcout_litre', 2) }} | {{ v('moisson_hvo_surcout_ha', 0) }} | {{ v('ensileuse_hvo_surcout_ha', 0) }} | {{ v('moisson_hvo_surcout_an', 0) }} |
| d'avant-crise (février 2026) | {{ v('hvo_surcout_litre', 2, scenario='bas') }} | {{ v('moisson_hvo_surcout_ha', 0, scenario='bas') }} | {{ v('ensileuse_hvo_surcout_ha', 0, scenario='bas') }} | {{ v('moisson_hvo_surcout_an', 0, scenario='bas') }} |
| haut (+ 30 %) | {{ v('hvo_surcout_litre', 2, scenario='haut') }} | {{ v('moisson_hvo_surcout_ha', 0, scenario='haut') }} | {{ v('ensileuse_hvo_surcout_ha', 0, scenario='haut') }} | {{ v('moisson_hvo_surcout_an', 0, scenario='haut') }} |

Calculé, consommation en plus de {{ v('hvo_surconsommation', 1) }} comprise. Le HVO revient à {{ v('hvo_ratio_gasoil', 1) }} le prix du gasoil agricole au prix actuel, et à {{ v('hvo_ratio_gasoil', 1, scenario='bas') }} au prix d'avant-crise. La crise a donc réduit l'écart, sans l'inverser : dans aucun scénario le HVO n'est moins cher que le gasoil.

**Aides.** Aucune aide trouvée pour un carburant renouvelable : ni la PAC ni l'AII n'en paient.

**Pourquoi vague 3.** Le HVO100 coûte plus cher que le gasoil dans les trois scénarios de prix : il n'est rentable dans aucun cas sans que quelqu'un d'autre paie la différence. Le surcoût reste modeste à l'échelle de la récolte, environ {{ v('moisson_hvo_surcout_ha', 0) }} en moisson, à comparer aux 85 €/ha que coûte la seule détention d'une moissonneuse de Cuma[^entraid]. Il peut être supporté si un acheteur ou un cahier des charges rémunère une récolte à faible carbone, ou si un entrepreneur le refacture à ses clients. C'est une solution à préparer, pas une économie.

Limites :

- **Le HVO déplace la dépendance.** Il vient d'huiles et de graisses achetées sur un marché européen et mondial, et non de la ferme. La DLG note qu'il n'est pas encore produit en quantité suffisante et que l'aviation et le transport maritime le recherchent aussi[^dlg]. MAES le présente comme fabriqué à partir de déchets, sans soja ni palme[^maes] : c'est un argument du vendeur, à vérifier auprès du fournisseur.
- Il ne réduit pas la consommation, il la remplace (et l'augmente un peu en litres).

### 3. Huile végétale pure (vague 3)

L'huile de colza pressée à froid peut alimenter un moteur diesel adapté. La fiche [Tracteur diesel](tracteur-diesel.md#4-huile-de-colza-pure-vague-3) détaille la technique, le coût de l'huile et le régime d'accises (exonération agricole, entrepositaire agréé pour le pressage, autorisation « utilisateur final »). On ne le refait pas ici.

Ramenée à la moisson, l'huile coûte plus cher que le gasoil dans les trois scénarios : {{ v('moisson_huile_ecart_ha', 1) }} de plus au prix actuel, {{ v('moisson_huile_ecart_ha', 1, scenario='haut') }} au prix haut et {{ v('moisson_huile_ecart_ha', 1, scenario='bas') }} au prix d'avant-crise (calculé, pressage compris, hors accises et hors conversion du moteur). Elle reste moins chère que le HVO100.

Pourquoi vague 3 pour les machines de récolte, comme pour le tracteur :

- l'autorisation de Claas porte sur le HVO, pas sur l'huile pure[^claas] ; convertir un moteur Stage V de 300 à 500 ch d'une machine à plus de 250 000 € pose la question de la garantie et des émissions[^bareme] ;
- la conversion s'amortit sur peu d'heures : environ {{ v('moisson_heures_an', 0) }} de battage (calculé), contre plusieurs centaines pour un tracteur ;
- il n'y a pas de gain par hectare à attendre : l'huile coûte un peu plus que le gasoil au prix actuel et nettement plus au prix d'avant-crise.

L'huile garde un intérêt dans un système où la ferme presse déjà son colza pour ses tracteurs : le stock d'huile peut alors servir de réserve si le gasoil vient à manquer. Ce n'est pas une protection contre les prix hauts : même au prix haut, l'huile reste plus chère.

### 4. Moissonneuse hybride ou électrique (vague 3)

- **Hybride léger.** Claas a testé au champ un concept de moissonneuse de classe 12 avec un moteur diesel de 400 kW, un moteur électrique de 40 kW et une batterie de 3 kWh. Le moteur électrique soutient le diesel dans les pointes ; Claas annonce jusqu'à 10 % de carburant en moins[^fj].
- **Hybride série.** À l'Agritechnica 2025, le chinois Zoomlion a montré la H7-600E : un diesel de 480 ch charge une grosse batterie, et des moteurs électriques entraînent les roues, les rotors et la coupe. Prix annoncé au Royaume-Uni : environ 350 000 £ avec une coupe de 9,2 m[^fwi]. La machine reste au gasoil.
- **Tout électrique.** Le français Terafield a présenté en juin 2026 un concept de moissonneuse 100 % électrique de 340 ch, rechargeable jusqu'à 1 MW et utilisable comme batterie stationnaire hors saison[^tera]. Ce n'est encore qu'un concept.

Claas estime qu'une ensileuse Jaguar à batterie devrait être au moins deux fois plus grosse et plus lourde pour égaler un modèle actuel[^claas]. Pour la récolte, la batterie bute sur la même limite que le gros tracteur (voir la fiche [Tracteur diesel](tracteur-diesel.md#5-gros-tracteur-electrique-a-batterie-vague-3)) : de longues journées à pleine puissance, au moment précis où la récolte ne peut pas attendre.

### 5. Biométhane (vague 3)

Il existe des tracteurs au biométhane (New Holland T7.270 Methane Power, voir la fiche [Tracteur diesel](tracteur-diesel.md#3-tracteur-au-biomethane-vague-2)), mais on n'a trouvé aucune moissonneuse ni ensileuse au méthane, même à l'état de prototype. Claas juge les carburants gazeux pénalisés par leur faible densité d'énergie, donc par la taille des réservoirs[^claas]. La DLG estime qu'ils demandent des réservoirs de plusieurs mètres cubes, même en puissance moyenne[^dlg].

Le biométhane a pourtant une place sur le chantier : les tracteurs qui transportent le grain ou le fourrage, et celui qui tasse le silo, peuvent déjà rouler au méthane, même si la machine de récolte reste au HVO ou au gasoil.

## Ce qui ferme la boucle

- **Partager les machines** : moins de machines à fabriquer et à financer pour la même surface, et un collectif capable de porter un carburant renouvelable.
- **Le colza de la ferme** donne l'huile, et son tourteau nourrit les animaux. Pour les machines de récolte, c'est une réserve en cas de crise plus qu'une solution de tous les jours.
- **Les effluents et résidus** deviennent du biométhane pour les tracteurs du chantier, et le digestat retourne au champ.
- **Le HVO** recycle des huiles et graisses usagées, mais hors de la ferme : il ferme une boucle à l'échelle du pays, pas de l'exploitation.
- L'ordre logique : mutualiser les machines, passer les machines récentes au HVO quand le surcoût peut être partagé, passer les tracteurs du chantier au biométhane, et préparer l'hybride ou l'électrique au renouvellement.

## À vérifier

- **Coût simplifié AII** de la moissonneuse-batteuse et de l'ensileuse automotrice (lignes réservées aux CUMA) : à reprendre dans les données du projet pour chiffrer l'aide. Seuil de sélection d'une CUMA (5 points) pour une ligne sans case « architecture verte » ni « résilience économique » : comment le dépasser.
- **Barèmes belges** : aucun tarif publié d'entrepreneur ni de CUMA pour la moisson ou l'ensilage en Wallonie. L'outil Mecacost du CRA-W calcule le coût d'une machine aux conditions belges, après inscription : à utiliser pour remplacer les références françaises.
- **Part de la récolte faite par entreprise ou CUMA en Wallonie** : aucune statistique trouvée (recensement agricole, SPW, Agro-Service). Nombre de CUMA actives en Wallonie.
- **Consommations réelles** : les valeurs du barème sont calculées à partir de la puissance. Les remplacer par des relevés de machines (ordinateur de bord, factures de l'entrepreneur), en céréales, en maïs grain et en ensilage d'herbe.
- **Prix réel du HVO100 livré en vrac à une ferme ou un entrepreneur**, hors accises : l'estimation de cette fiche repose sur le prix maximum routier du diesel XTL, qui n'est pas propre au HVO. Un devis d'un fournisseur belge la remplacera.
- **Régime d'accises du HVO en usage agricole** : confirmer auprès des Douanes et Accises qu'il peut être livré en exonération à un titulaire d'une autorisation « utilisateur final », par quel type de fournisseur et sous quel code produit, et s'il doit être marqué.
- **Homologation HVO** des moissonneuses et ensileuses John Deere, New Holland, Case IH, Fendt et Massey Ferguson (manuels ou concessionnaires).
- **Origine des matières premières du HVO vendu en Belgique** (certificat de durabilité du fournisseur).
- **Stations de biométhane carburant (bio-GNC) en Wallonie** accessibles aux tracteurs du chantier.
- **Résultats chiffrés de l'hybride Claas et de la Zoomlion H7-600E** en conditions de récolte, et suite du concept Terafield.

## Sources

[^bareme]: « Barème d'entraide 2024-2025 », chambres d'agriculture et fédérations de Cuma du Grand Est, du Centre-Val de Loire et des Hauts-de-France, novembre 2024, pages « Moissonneuses-batteuses » et « Ensilage » (données françaises, gasoil non routier à 1,20 € HT/L). https://www.cuma.fr/app/uploads/sites/20/2024/11/bareme-entraide-2024-2025.pdf
[^entraid]: Nugues V., Levillain N., « Quel prix de revient pour la moissonneuse-batteuse pour la moisson 2026 ? », Entraid, 18 juin 2026 (données du service Agrodev de la FNCUMA, 576 machines ; article lu en partie). https://www.entraid.com/articles/prix-de-revient-moissonneuse-batteuse
[^agreste]: Godement V., « Machines de récolte : une mutualisation croissante entre agriculteurs », Réussir, 2 juillet 2026, d'après une note Agreste du 24 juin 2026. https://www.reussir.fr/machines-de-recolte-mutualisation-croissante-entre-agriculteurs
[^pb]: « Bien choisir sa stratégie de mécanisation », Paysan Breton, 8 août 2025. https://www.paysan-breton.fr/2025/08/bien-choisir-sa-strategie-de-mecanisation/
[^sysd]: Guilleaume L., « Fiche ressource n° 64 – Système D Scrl – Coopérative d'utilisation en commun de matériel agricole », Réseau wallon de développement rural, janvier 2013. https://reseauwallonpac.be/sites/default/files/504342_150115_fress64_systemed_cuma.pdf
[^agroservice]: « Kerncijfers », Nationale Centrale Landbouw-Service (Agro-Service), page non datée, consultée le 26 novembre 2026. https://www.landbouwservice.be/nl/node/10
[^aii-liste]: « Liste des investissements admissibles » (aide aux investissements agricoles, AII), SPW Agriculture, janvier 2026, consultée le 27 novembre 2026. https://agriculture.wallonie.be/files/accueil/Aides/AII/outils/Liste%20des%20investissements%20admissibles.pdf
[^am-aii]: Arrêté ministériel du 23 février 2023 exécutant l'arrêté du Gouvernement wallon du 23 février 2023 relatif aux aides à l'installation et aux investissements, version consolidée (modifications des 15 janvier et 11 mai 2026), articles 5 et 6, annexe 3, Wallex, consulté le 27 novembre 2026. https://wallex.wallonie.be/eli/arrete/2023/02/23/2023042748
[^claas]: « CLAAS: HVO Approval and Initial Factory Fill for Tractors, Combine Harvesters and Forage Harvesters », communiqué Claas repris par Advanced BioFuels USA, 10 octobre 2023. https://advancedbiofuelsusa.info/claas-hvo-approval-and-initial-factory-fill-for-tractors-combine-harvesters-and-forage-harvesters
[^dlg]: « HVO in practical DLG testing », DLG (Deutsche Landwirtschafts-Gesellschaft), non daté, consulté le 26 novembre 2026. https://www.dlg.org/en/magazine/hvo-in-practical-dlg-testing
[^maes]: « HVO100 : le diesel propre du futur en Europe et en Belgique », MAES, 12 août 2024 (mis à jour le 11 juin 2025). https://www.maesmobility.be/fr/blog/maes-general/hvo100-le-diesel-propre-du-futur-en-europe-et-en-belgique/
[^maes25]: « MAES Energy & Mobility further expands network for HVO100 to 25 locations in Belgium », MAES, 15 mai 2025. https://www.maesmobility.be/en/blog/fuel/maes-energy-mobility-breidt-netwerk-voor-hvo100-verder-uit-naar-25-locaties-in-belgie/
[^carbu]: « Prix maximum des carburants en Belgique », Carbu.com (catégorie « Diesel (XTL / HVO) »), consulté le 26 novembre 2026. https://carbu.com/belgique/index.php/prixmaximum
[^statbel-nov]: « Tarif officiel des produits pétroliers en euros », 30 derniers jours (29 octobre au 27 novembre 2026), SPF Économie, publié par Statbel ; moyennes du 1er au 26 novembre calculées dans ce projet. https://bestat.statbel.fgov.be/bestat/api/views/cee4903e-c302-45be-9e43-e4b724ffb592/result/PDF
[^statbel-mois]: « Tarif officiel moyen des produits pétroliers en euros », moyennes mensuelles de novembre 2024 à octobre 2026, SPF Économie, publié par Statbel. https://bestat.statbel.fgov.be/bestat/api/views/90a3de47-97fc-4870-9936-f55ed85f15fd/result/PDF
[^circ-2026]: Circulaire 2026/C/82 concernant les produits énergétiques et l'électricité, SPF Finances (Administration générale des Douanes et Accises), 7 septembre 2026, §§ 3, 122, 281, 284/1 et 292, Fisconetplus. https://eservices.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/7c2dec9f-a0dc-4c3b-9fce-27f229f26a17
[^fj]: « Claas brings semi-electric hybrid combine concept to the field », Irish Farmers Journal, 28 décembre 2023. https://www.farmersjournal.ie/machinery/news/claas-brings-semi-electric-hybrid-combine-concept-to-the-field-793491
[^fwi]: « Agritechnica 2025: Electric drivetrain for Zoomlion combine », Farmers Weekly, 13 novembre 2025. https://www.fwi.co.uk/machinery/harvest-equipment/combines/agritechnica-2025-electric-drivetrain-for-zoomlion-combine
[^tera]: « Terafield Unveils Concept for Fully Electric Combine Harvester », Maquinac, 5 juin 2026. https://maquinac.com/english/terafield-unveils-concept-for-fully-electric-combine-harvester/
