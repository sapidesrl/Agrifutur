---
id: vehicules-livraison
titre: Utilitaire diesel de livraison
domaine: transport
dependance_fossile: gasoil
alternatives: [Utilitaire électrique, tournées groupées, vélo-cargo en ville]
vague_meilleure_alternative: 1
statut: relu
maj: 2026-11-26
---

# Utilitaire diesel de livraison

!!! warning "Limites des sources"
    Les sources ont été lues sur la page d'origine le 26 novembre 2026. Aucun tarif belge HTVA d'un même fourgon en diesel et en électrique n'a pu être lu : l'écart de prix d'achat vient d'un article français. Les consommations viennent d'essais allemands et français. Le texte du Code de la TVA sur la déduction pour les camionnettes n'a pas pu être lu : la règle vient d'un loueur belge.

## En bref

En vente directe, la camionnette diesel porte les produits de la ferme vers les magasins, les points de dépôt, les marchés et les clients : environ {{ v('utilitaire_litres_an', 0) }} de diesel routier pour {{ v('utilitaire_km_an') }} (hypothèses), soit {{ v('utilitaire_diesel_eur_an') }} HTVA au prix maximum officiel de novembre 2026 ({{ fourchette('utilitaire_diesel_eur_an') }} selon les scénarios). Le même trajet en utilitaire électrique, rechargé pour moitié sur les panneaux de la ferme (hypothèse), coûte {{ v('utilitaire_mix_eur_an') }} d'électricité. L'électrique reste moins cher au kilomètre dans tous les scénarios, même rechargé entièrement sur le réseau, mais il coûte plus cher à l'achat : il est rentable aujourd'hui en occasion récente, et en neuf seulement avec un fourgon bon marché, beaucoup de kilomètres ou une aide (vague 1). Grouper les tournées entre producteurs réduit les kilomètres eux-mêmes, mais demande une organisation collective (vague 2). En ville, le vélo-cargo assure le dernier kilomètre depuis un point de dépôt, là où un service de livraison à vélo tient économiquement (vague 2).

## Comment ça marche aujourd'hui

Un producteur en circuit court livre lui-même, le plus souvent avec un fourgon compact ou une camionnette de moins de 3,5 tonnes, parfois réfrigérée. Une tournée part de la ferme, passe par un ou plusieurs points de vente et revient souvent à vide.

Ordres de grandeur :

- en Hainaut, 83 producteurs qui livraient la grande distribution faisaient des tournées de 40 km en moyenne pour un seul magasin, et de 240 km pour six magasins. Le coût logistique moyen d'une tournée allait de 29 € à 164 €, chauffeur compris, avec les paramètres de l'étude (15,33 €/h et 0,50 €/km, chiffres de 2014)[^diversiferm] ;
- dans une autre enquête citée par DiversiFerm, 22 producteurs en milieu rural et périurbain passaient en moyenne 3 h 45 par semaine sur la route pour leurs livraisons (de 25 minutes à 8 h 20), pour un coût moyen de 136 € par semaine[^diversiferm] ;
- en exploitation agricole, les trajets dépassent rarement 100 km par jour (observation française)[^reussir].

Ce projet retient {{ v('utilitaire_km_an', unite=False) }} km par an (hypothèse : deux tournées de 150 km par semaine).

Consommation : l'ADAC a mesuré 7,1 L/100 km pour un VW T7 Multivan diesel, version transport de personnes[^adac]. Ce projet retient {{ v('utilitaire_conso_diesel', 0) }} pour un fourgon chargé, avec des arrêts fréquents (hypothèse).

**Le prix du diesel routier.** Le tarif officiel du SPF Économie fixe un prix maximum à la pompe pour le diesel B7. Du 1er au 26 novembre 2026, il a valu en moyenne {{ v('diesel_b7_tvac') }} TVAC (calculé à partir des prix journaliers) ; il est passé de 2,452 €/L au début du mois à 2,203 €/L le 26[^statbel-nov]. En février 2026, avant la crise, la moyenne mensuelle était de {{ v('diesel_b7_tvac', scenario='bas') }}[^statbel-moy]. Le prix réel à la pompe est souvent un peu plus bas que le maximum.

Le diesel routier a moins augmenté en proportion que le gasoil agricole, parce que son accise par litre, qui ne suit pas le prix du pétrole, est beaucoup plus élevée. Le litre revient malgré tout à {{ v('diesel_routier_htva') }} HTVA, contre {{ v('gasoil_agricole_htva') }} pour le gasoil agricole (voir la fiche [tracteur diesel](../traction/tracteur-diesel.md)). L'accord budgétaire fédéral de fin 2025 prévoit en outre une hausse des accises sur l'essence, le diesel et le gaz[^kbc].

**TVA : deux situations.**

- Un agriculteur assujetti au régime normal récupère la TVA sur le carburant d'une camionnette utilisée seulement à des fins professionnelles. S'il y a un usage privé, la déduction suit la part professionnelle, ou un forfait de 85 % quand le véhicule sert surtout au transport de marchandises[^athlon]. Il paie donc le diesel {{ v('diesel_routier_htva') }}.
- Un agriculteur au régime forfaitaire agricole ne déduit aucune TVA : la compensation forfaitaire qu'il facture sur ses ventes à des assujettis « exclut toute autre forme de déduction »[^ctva]. Il paie le diesel TVAC, soit {{ v('utilitaire_diesel_eur_100km_tvac') }} au lieu de {{ v('utilitaire_diesel_eur_100km') }}. L'électricité achetée au réseau lui coûte aussi la TVA, donc l'écart entre diesel et électrique se maintient en proportion.

Les calculs de cette fiche sont faits HTVA.

## Où entrent le pétrole et le gaz

- **Carburant** : le diesel routier B7, raffiné à partir du pétrole brut, avec une petite part de biodiesel.
- **AdBlue** : solution d'urée des moteurs diesel récents, fabriquée à partir d'ammoniac, donc de gaz naturel.
- **Froid** : le groupe frigorifique d'un utilitaire réfrigéré tourne souvent sur le moteur du véhicule.
- **Véhicule** : pneus, plastiques, huiles et peintures issus de la pétrochimie.
- **Emballages** : caisses, films et barquettes de livraison, souvent en plastique.

## Les alternatives

### 1. Utilitaire électrique (vague 1)

Les fourgons compacts électriques existent chez la plupart des constructeurs, avec la même caisse que la version diesel. Le Ford E-Transit Custom garde par exemple 5,8 m³ de volume utile en L1H1 et 6,8 m³ en L2H1, comme le diesel ; sa batterie utile de 64 kWh annonce 325 km d'autonomie homologuée dans sa version de base[^argus]. Les modèles à petite batterie font 170 à 200 km en conduite souple, 90 à 120 km en conduite rapide, ce qui suffit à la plupart des usages agricoles[^reussir].

**Énergie aux 100 km** (calculé, HTVA, avec {{ v('utilitaire_conso_diesel', 0) }} de diesel ou {{ v('utilitaire_conso_elec', 0) }} d'électricité mesurés à la prise, hypothèses) :

| Énergie | Prix actuel | Fourchette des scénarios |
|---|---|---|
| Diesel routier | {{ v('utilitaire_diesel_eur_100km') }} | {{ fourchette('utilitaire_diesel_eur_100km') }} |
| Électricité du réseau | {{ v('utilitaire_reseau_eur_100km') }} | {{ fourchette('utilitaire_reseau_eur_100km') }} |
| Photovoltaïque de la ferme | {{ v('utilitaire_pv_eur_100km') }} | fixe |
| Moitié photovoltaïque, moitié réseau | {{ v('utilitaire_mix_eur_100km') }} | {{ fourchette('utilitaire_mix_eur_100km') }} |

La consommation électrique retenue s'appuie sur l'ADAC, qui a mesuré 23,3 kWh/100 km pertes de charge comprises pour un VW ID. Buzz, du même gabarit que le T7 diesel[^adac]. L'argus a relevé 18 kWh/100 km à l'ordinateur de bord d'un E-Transit Custom, sur un parcours mêlant ville, route et voie express[^argus].

Contrairement au [tracteur électrique](../traction/tracteur-diesel.md#2-tracteur-electrique-compact-vague-2), l'utilitaire électrique est moins cher au kilomètre que le diesel même rechargé entièrement sur le réseau, dans tous les scénarios : l'accise du diesel routier pèse lourd. Sur {{ v('utilitaire_km_an') }}, l'économie d'énergie atteint {{ v('utilitaire_economie_an') }} avec la recharge mixte ({{ fourchette('utilitaire_economie_an') }} selon les scénarios), et {{ v('utilitaire_economie_an_reseau') }} tout sur le réseau ({{ fourchette('utilitaire_economie_an_reseau') }}).

**La recharge sur les panneaux est limitée par l'horaire.** L'utilitaire roule en journée, quand les panneaux produisent. Il ne se recharge au soleil que les jours sans tournée ou entre deux tournées. Ce projet suppose que {{ v('utilitaire_part_recharge_pv', 0) }} de la recharge vient des panneaux (hypothèse). Pour la ferme, la recharge représente {{ v('utilitaire_kwh_an') }}, de quoi relever le taux d'autoconsommation d'une installation photovoltaïque les jours où le véhicule reste à la ferme (voir la fiche [électricité du réseau](../energie/electricite-reseau.md)).

**Le prix d'achat fait la différence.** En France, un utilitaire électrique neuf coûte 35 à 50 % de plus que son équivalent diesel, mais il perd sa valeur 20 à 25 % plus vite : au bout de trois ans, l'écart de prix en occasion n'est plus que de 10 à 15 % (constat sur les sites de vente en ligne, prix français)[^reussir]. Sur {{ v('utilitaire_duree_detention', 0) }} de détention (hypothèse), l'économie d'énergie rembourse un surcoût d'achat de {{ v('utilitaire_surcout_rembourse') }} ({{ fourchette('utilitaire_surcout_rembourse') }} selon les scénarios, calculé sans frais financiers ni écart de revente). Autrement dit (calculé) :

- **en occasion de trois ans**, avec un écart de {{ v('utilitaire_ecart_prix_occasion', 0) }}, l'électrique se rembourse tant que le diesel équivalent coûte moins de {{ v('utilitaire_prix_max_occasion') }} ({{ fourchette('utilitaire_prix_max_occasion') }}) ;
- **en neuf**, même avec l'écart le plus faible ({{ v('utilitaire_ecart_prix_neuf', 0) }}), il ne se rembourse que si le diesel équivalent coûte moins de {{ v('utilitaire_prix_max_neuf') }} ({{ fourchette('utilitaire_prix_max_neuf') }}). Le neuf ne se rembourse donc qu'avec un fourgon bon marché, beaucoup de kilomètres ou une aide, surtout au prix d'avant-crise. Il faut comparer avec les devis réels (voir « À vérifier »). L'entretien joue aussi en faveur de l'électrique : pas de vidange, de filtres ni de distribution, moins de vibrations et d'usure[^reussir]. Le gain d'entretien n'a pas été chiffré ici (voir « À vérifier »).

**La batterie.** Elle représente 30 à 40 % du prix d'un véhicule neuf. La plupart des constructeurs la garantissent 8 ans ou 160 000 km. Sa durée de vie est donnée pour 1 000 à 2 000 cycles de charge complets. En occasion, on demande son état de santé (SOH) : en dessous de 70 à 75 %, il faut la remplacer[^reussir].

**Fiscalité belge.**

- Une camionnette reste déductible à 100 % à l'impôt, même en diesel : la fin de la déductibilité des voitures non « zéro émission » commandées depuis le 1er janvier 2026 ne la concerne pas[^athlon].
- Une déduction pour investissement majorée (130 à 140 %) était prévue pour les camionnettes électriques, rétroactive au 1er janvier 2025. L'accord budgétaire fédéral de novembre 2025 l'a supprimée selon Fleet.be[^kbc], alors qu'un loueur la présentait encore en janvier 2026 à 40 % pour l'électrique contre 10 % pour le diesel[^athlon]. Le régime applicable doit être confirmé par un comptable (voir « À vérifier »).
- L'aide wallonne aux investissements agricoles (AII) cite le « véhicule utilitaire réfrigéré » pour la diversification agricole, avec un coût simplifié de 24 424 €, sans distinguer le diesel de l'électrique[^aii].
- À Bruxelles, une PME qui a un siège d'exploitation dans la Région peut recevoir de 5 à 40 % de l'achat d'un utilitaire électrique (catégorie N1), borne de recharge comprise, avec un maximum de 16 000 € par véhicule[^bee-util]. Une ferme wallonne n'y a pas droit.

Conditions : des tournées compatibles avec l'autonomie, une prise ou une borne à la ferme, et de préférence un véhicule d'occasion récent dont la batterie est en bon état.

Limites : l'électrique remplace le diesel par l'électricité, mais la batterie dépend du lithium et de métaux importés. Le réseau reste nécessaire pour la recharge du soir, et son prix suit en partie celui du gaz.

### 2. Tournées groupées (vague 2)

Le kilomètre le moins cher est celui qu'on ne fait pas. Plusieurs producteurs mettent en commun un trajet, un véhicule ou un chauffeur :

- un producteur passe chez ses voisins sur la route du point de vente et prend leurs produits, à tour de rôle ;
- la tournée dépose dans un point relais (un producteur, un commerce, un lieu de passage), d'où les clients ou un autre transporteur repartent ;
- la tournée ramène des marchandises au retour (achats groupés, emballages vides) au lieu de rentrer à vide ;
- plusieurs structures achètent ensemble une camionnette ou engagent un chauffeur[^ulb].

Selon une étude de modélisation citée par l'ULB, les gains par exploitation et pour le collectif sont « très importants » quand on passe de trajets directs individuels à des tournées. Intégrer la livraison dans les tournées de collecte apporte un gain de plus, mais moindre, en émissions et en coût d'exploitation[^ulb].

C'est pourtant peu pratiqué : sur 34 producteurs qui livraient la grande distribution en Hainaut, 4 seulement livraient avec d'autres, alors que 23 se disaient intéressés[^diversiferm].

Exemples en Wallonie :

- le Collectif 5C regroupait en 2021 plus d'une trentaine de coopératives citoyennes en circuit court de Wallonie et de Bruxelles. Avec Gembloux Agro-Bio Tech, il travaillait à mutualiser collecte et tournées, outils de transformation et commandes, autour de hubs logistiques locaux, dans une recherche-action subsidiée par la Wallonie de 2021 à 2024[^noel] ;
- à Liège, le chantier du Hub circuit court, une plateforme de 3 000 m² à Bressoux-Droixhe avec légumerie et conserverie, a démarré en avril 2024 pour une fin annoncée début 2025. La Wallonie y consacre 7,6 millions d'euros, et le projet vise notamment à réduire les intermédiaires et l'impact du transport[^spi] ;
- dès 2016, la criée de Wépion servait de plateforme logistique en circuit court en province de Namur, et l'asbl Futur Simple, à Saint-Ode, montait chaque semaine une camionnette vers Bruxelles[^ulb].

Conditions :

- des producteurs proches, avec des points de vente communs ou sur la même route ;
- des règles écrites : horaires, responsabilité des produits, chaîne du froid, partage des frais. Les arrangements informels souffrent souvent de retards et d'erreurs de manipulation[^ulb] ;
- un calendrier partagé : « tout le monde a besoin de la camionnette du mercredi au vendredi », résume un groupement de producteurs[^ulb].

Limites : la coordination prend du temps et ce temps a un coût. Les plateformes logistiques sont souvent subsidiées : un opérateur privé qui demanderait 10 à 30 % de la valeur des produits ferait dépasser certains plafonds de prix, selon Hainaut Développement[^ulb]. La rentabilité dépend donc du collectif et de l'aide publique, d'où la vague 2.

### 3. Vélo-cargo en ville (vague 2)

Un vélo-cargo, le plus souvent à assistance électrique, porte au moins 100 kg (définition bruxelloise)[^bee-velo]. Il ne remplace pas la camionnette depuis la ferme : il assure le dernier kilomètre dans un centre-ville, depuis un point de dépôt ou un hub.

En ville, il évite les embouteillages et livre souvent plus vite qu'une camionnette. Selon Rayon 9 à Liège, ce qui compte est le rapport entre la surface couverte et la densité des livraisons dans cette surface. Le Cargo Bike and Cycle Logistics Experts Group estimait en 2019 que le vélo-cargo pourrait remplacer la camionnette pour plus de 30 % des livraisons de colis en ville, et jusqu'à 50 % pour les services[^rtbf].

Exemples :

- à Liège, la coopérative Rayon 9 livre en vélo-cargo[^rtbf] ;
- à Namur, la coopérative Coopcyclette faisait en juillet 2025, depuis neuf mois, de la cyclo-logistique, de la location et un atelier : c'est l'ensemble qui lui permet d'atteindre l'équilibre. Elle relie par exemple Dave et Bouge en une heure, sur une boucle de 18 km, à une heure où les camionnettes circulent mal[^lavenir] ;
- à Bruxelles, Urbike pratique la cyclo-logistique[^rtbf].

Aides :

- en Wallonie, une prime couvre 50 % du prix HTVA d'un vélo, d'un vélo-cargo ou d'une remorque, neufs ou d'occasion, pour des activités professionnelles de livraison. Le plafond est de 5 000 € pour un vélo-cargo neuf à assistance électrique et de 3 500 € pour une remorque neuve, avec un maximum de 50 000 € par bénéficiaire sur trois exercices. Il faut un siège d'activité en Wallonie, 75 % des activités en Wallonie et garder le matériel trois ans[^prime-velo-w]. Selon une fiche du SPW de mars 2026, 93 primes avaient été accordées depuis janvier 2024, pour 79 vélos-cargos, 41 vélos et 15 remorques[^spw-velo] ;
- à Bruxelles, une PME qui y a un siège d'exploitation peut recevoir de 40 à 70 % du prix, avec un maximum de 4 000 € par vélo-cargo et 2 000 € par remorque[^bee-velo].

Limites : le modèle économique est fragile. À Namur, Coursier wallon a cessé ses activités en juin 2025, après sept ans sur un capital de départ de 200 000 € ; l'un des fondateurs n'a connu qu'un exercice bénéficiaire en douze ans d'activité, faute de volumes suffisants[^lavenir]. Le vélo-cargo a du sens pour un producteur qui livre souvent dans un même centre-ville, en confiant le dernier kilomètre à une coopérative existante ou en déposant ses produits dans un hub. Il gagne du terrain quand les camionnettes ne peuvent plus entrer dans les piétonniers[^lavenir]. Il demande toujours un véhicule pour venir de la ferme.

## Ce qui ferme la boucle

- Les toitures de la ferme rechargent l'utilitaire les jours où il reste à la ferme (voir la fiche [électricité du réseau](../energie/electricite-reseau.md)).
- Les tournées groupées et la logistique inverse remplissent le véhicule à l'aller et au retour : caisses vides, emballages consignés et achats groupés reviennent vers la ferme.
- Les hubs et les points relais concentrent les flux ; le vélo-cargo prend le relais en ville.
- L'ordre logique : d'abord réduire les kilomètres (tournées groupées, points relais), ensuite électrifier ceux qui restent, enfin passer le dernier kilomètre urbain au vélo.

## À vérifier

- Prix belges HTVA d'un même fourgon compact en diesel et en électrique, neuf et d'occasion (configurateurs belges et tarifs constructeurs inaccessibles ; écart de 35 à 50 % lu dans une source française).
- Texte du Code de la TVA (article 45) sur la déduction de la TVA pour les camionnettes : la règle citée vient d'un loueur (Athlon), pas du texte légal.
- Déduction pour investissement des camionnettes électriques en 2026 : Fleet.be (novembre 2025) annonce sa suppression, Athlon (janvier 2026) la présente encore à 40 %. Vérifier la loi votée.
- Existence d'une aide wallonne à l'achat d'un utilitaire électrique pour une entreprise ou une exploitation agricole ; conditions exactes de l'AII pour un utilitaire réfrigéré électrique.
- Consommation réelle d'un fourgon compact diesel et électrique chargé, en tournée, été comme hiver, et consommation du groupe frigorifique.
- Coût d'entretien comparé du diesel et de l'électrique sur un utilitaire (non chiffré).
- Remboursement du « diesel professionnel » : il vise les camions et ne devrait pas concerner une camionnette, mais ce point n'a pas été lu.
- Calendrier des zones de basses émissions (Bruxelles, Gand, Anvers, projets wallons) pour les utilitaires diesel : page lez.brussels non lisible par notre outil.
- Ouverture effective du Hub circuit court de Liège et services offerts aux producteurs (collecte, stockage, livraison).
- Activité actuelle du Collectif 5C en matière de tournées mutualisées et de hubs (données lues de 2021).
- Gains chiffrés d'une tournée groupée (kilomètres et heures économisés) sur des cas wallons.
- Kilométrage annuel réel de l'utilitaire de l'exploitation, qui remplace l'hypothèse de {{ v('utilitaire_km_an') }}.

## Sources

[^statbel-nov]: « Tarif officiel des produits pétroliers en euros », SPF Économie, publié par Statbel (Bestat), prix journaliers du 29 octobre au 27 novembre 2026, colonne « Diesel B7 », consulté le 26 novembre 2026. https://bestat.statbel.fgov.be/bestat/api/views/cee4903e-c302-45be-9e43-e4b724ffb592/result/PDF
[^statbel-moy]: « Tarif officiel moyen des produits pétroliers en euros », SPF Économie, publié par Statbel (Bestat), moyennes mensuelles de novembre 2024 à octobre 2026, colonne « Diesel B7 », consulté le 26 novembre 2026. https://bestat.statbel.fgov.be/bestat/api/views/90a3de47-97fc-4870-9936-f55ed85f15fd/result/PDF
[^adac]: Wieler J., « VW Busse im Vergleich: Elektro oder Verbrenner? », ADAC, 28 mai 2024 (mesures ADAC Ecotest). https://www.adac.de/rund-ums-fahrzeug/autokatalog/marken-modelle/auto/vergleich-vw-t7-vw-id-buzz
[^argus]: Geneste G., « Essai Ford E-Transit Custom (2024). Un fourgon électrique moderne et agréable », L'argus, 3 juillet 2024. https://www.largus.fr/actualite-automobile/essai-ford-e-transit-custom-2024-un-fourgon-electrique-moderne-et-agreable-30034830.html
[^reussir]: Vimond L., « Véhicule utilitaire électrique – Les clés pour trouver les bonnes occasions », Réussir, 3 février 2026 (France). https://www.reussir.fr/bovins-viande/vehicule-utilitaire-electrique-les-cles-pour-trouver-les-bonnes-occasions
[^diversiferm]: Winandy S. (DiversiFerm) et Jolly C.-E. (AEI), « Coûts cachés de la logistique et circuits courts », présentation du 27 janvier 2016, d'après Van Den Henden S. (2014) et Arcusa V. (2011). https://orbi.uliege.be/bitstream/2268/198659/1/Couts%20cach%c3%a9s%20de%20la%20logistique%20et%20circuits%20courts%20-%20Winandy%20S.%202016.pdf
[^ulb]: Plateau L. et Holzemer L., « La durabilité vécue et mise en œuvre par les acteurs des circuits courts, cahier III : les enjeux logistiques », CEESE (ULB), pour Inter-Environnement Wallonie, mai 2016. https://dipot.ulb.ac.be/dspace/bitstream/2013/337199/3/ADDOCC_Plateau-Holzemer2016_EnjeuxLogistiques.pdf
[^noel]: Noël J., Raimbert C., Lanzi F. et al., « Des ateliers logistiques pour renforcer les structurations territoriales d'un réseau d'échange alimentaire alternatif et solidaire. Le cas du Collectif 5C (Wallonie) », Forum Origine Diversité Territoires, Gembloux Agro-Bio Tech (ULiège) et Collectif 5C, 2021. https://orbi.uliege.be/bitstream/2268/265514/1/2_1_4_FR_Noel.pdf
[^spi]: « La construction du Hub circuit court liégeois a démarré ! », communiqué de presse, Spi (agence de développement territorial de la province de Liège), 5 avril 2024. https://www.spi.be/wp-content/uploads/20240405-cp-hub.pdf
[^kbc]: « Accord budgétaire fédéral : la voiture (relativement) épargnée, la camionnette électrique reléguée », Fleet.be, publié par KBC Autolease, 28 novembre 2025. https://www.kbc.be/autolease/fr/a-la-une/federaal-begrotingsakkoord-bedrijfswagen-grotendeels-buiten-schot-elektrische-bestelwagen-verliest-terrein.html
[^athlon]: « Quelles sont les règles fiscales pour les véhicules utilitaires légers ? », Athlon Belgique (loueur, site commercial), 7 janvier 2026. https://www.athlon.com/be-fr/actualite-conseils/quelles-sont-les-regles-fiscales-pour-les-vehicules-utilitaires-legers/
[^ctva]: Projet de loi portant des dispositions diverses en matière de taxe sur la valeur ajoutée, Chambre des représentants, doc. 55 2279/001, 26 octobre 2021 : coordination de l'article 57, § 2, du Code de la TVA (régime forfaitaire agricole). https://www.dekamer.be/FLWB/PDF/55/2279/55K2279001.pdf
[^aii]: Arrêté ministériel du 23 février 2023 relatif aux aides à l'installation et aux investissements (secteurs agricole et horticole), version consolidée en vigueur depuis le 1er janvier 2026, annexe 3, ligne 462. Wallex, consulté le 26 novembre 2026. https://wallex.wallonie.be/eli/arrete/2023/02/23/2023042748
[^bee-util]: « Prime Utilitaire électrique », Bruxelles Économie et Emploi (SPRB), page non datée, consultée le 26 novembre 2026. https://economie-emploi.brussels/prime-utilitaire-electrique
[^bee-velo]: « Prime Vélo-cargo ou remorque », Bruxelles Économie et Emploi (SPRB), page non datée, consultée le 26 novembre 2026. https://economie-emploi.brussels/prime-velo-cargo
[^prime-velo-w]: « Obtenir une prime régionale destinée à l'achat d'un vélo, d'un vélo cargo ou d'une remorque de vélo pour des activités de cyclologistique », démarche n° 4091, Wallonie (SPW Mobilité et Infrastructures), mise à jour du 25 novembre 2026. https://www.wallonie.be/fr/demarches/obtenir-une-prime-regionale-destinee-lachat-dun-velo-dun-velo-cargo-ou-dune-remorque-de-velo-pour-des-activites-de-cyclologistique
[^spw-velo]: « Prime vélo cargo pour les professionnels », fiche du SPW Mobilité et Infrastructures (Direction du Transport et de l'Intermodalité des Marchandises), 19 mars 2026. https://mobilite.wallonie.be/files/Transport%20de%20marchandises/2026_03_19_fiche_prime_velo_cargo_vDEF_web_SPW-DTIM.pdf
[^rtbf]: « Les vélos cargo, l'avenir de la livraison de colis en ville ? », RTBF, 19 août 2021. https://www.rtbf.be/article/les-velos-cargo-l-avenir-de-la-livraison-de-colis-en-ville-10825376
[^lavenir]: Desguin V., « Ils ont livré des repas, des courses, des documents… à vélo durant 7 ans : c'est fini pour cette entreprise namuroise », L'Avenir, 14 juillet 2025. https://www.lavenir.net/actu/discover/2025/07/14/ils-ont-livre-des-repas-des-courses-des-documents-a-velo-durant-7-ans-cest-fini-pour-cette-entreprise-namuroise-J6UDGHOM4JDADF2IML5LJ5W5HE/
