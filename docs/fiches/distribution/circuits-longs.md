---
id: circuits-longs
titre: Logistique longue et grande distribution
domaine: distribution
dependance_fossile: gasoil
alternatives: [Vente directe groupée, points de dépôt, abonnements payés d'avance]
vague_meilleure_alternative: 2
statut: relu
maj: 2026-11-27
---

# Logistique longue et grande distribution

!!! warning "Sources à relire"
    Les sources ont été lues sur la page d'origine le 26 novembre 2026. Les études de l'Observatoire des prix (SPF Économie) n'ont pas pu être lues : le site renvoie un captcha. La part de la valeur qui revient aux agriculteurs vient d'une audition parlementaire rapportée par la presse, et l'exemple de la pomme de terre d'une estimation d'ONG. Les chiffres des fermes en abonnement (CSA) les plus complets datent de 2014 et viennent de Flandre. Les sites du Réseau des GASAP et des réseaux CSA bloquent les robots : leurs chiffres actuels n'ont pas été lus.

## En bref

La plupart des produits agricoles belges rejoignent l'assiette par une chaîne longue : collecteur ou criée, transformateur, centrale d'achat, supermarché ; elle roule au diesel, garde le froid à l'électricité et emballe dans du plastique. Le producteur n'y touche qu'une petite part du prix : 11 % de la valeur de la chaîne alimentaire reviennent aux agriculteurs en Belgique, contre 26 % en moyenne dans l'Union[^lalibre-comeos]. En circuit court, le producteur fixe son prix et garde 70 à 80 % du prix final quand une coopérative vend pour lui[^alterechos]. Ces circuits courts ne suppriment pas le pétrole : une camionnette mal remplie peut consommer plus par kilo qu'un camion plein (chiffres français)[^ademe]. Ils sont rentables sous conditions : un collectif, des volumes réguliers, des clients proches et du temps pour vendre ; les aides (AII, halls relais, bio) allègent l'investissement sans changer ce classement (vague 2).

## Comment ça marche aujourd'hui

En Belgique, 88 % des achats de fruits et légumes frais se font dans la grande distribution, environ 7 % dans les magasins spécialisés et environ 5 % en circuit court (chiffres de 2018)[^ucl-legumes]. Pour les autres produits, le chemin est le même : le lait part à la laiterie, les céréales et les pommes de terre chez le négociant ou l'industriel, la viande à l'abattoir. Les pommes de terre se vendent pour 70 à 75 % sous contrat, le reste sur le marché libre, dont les prix sont fixés chaque semaine par l'organisation du négoce et de l'industrie (Belgapom)[^greenpeace-pdt].

**Qui garde le prix ?** Selon une représentante de la Commission européenne entendue par la Chambre en mars 2024, 11 % de la valeur totale de la chaîne alimentaire reviennent aux agriculteurs en Belgique, contre 26 % en moyenne dans l'Union[^lalibre-comeos]. Le reste paie la transformation, le transport, le stockage, la vente et les importations. La grande distribution n'en garde pas l'essentiel en bénéfice : l'Observatoire des prix chiffre sa marge nette moyenne à 0,91 % en 2022, selon une proposition de loi qui cite son étude de février 2024[^chambre-prix]. Le prix final sert surtout à payer les étapes de la chaîne.

**Un exemple : la pomme de terre.** En 2022, les pommes de terre coûtaient en moyenne {{ v('pdt_prix_detail_2022') }} en supermarché et les frites surgelées 1,75 €/kg[^greenpeace-pdt]. Greenpeace estime que l'agriculteur en recevait {{ v('pdt_prix_agriculteur_2022', 2) }} en moyenne, et qu'après ses coûts il lui restait environ 0,02 €/kg pour se rémunérer[^greenpeace-pdt]. C'est une estimation d'ONG, faite à partir du revenu agricole publié par Statbel : un ordre de grandeur, pas une mesure. Elle donne une part de {{ v('pdt_part_agriculteur_long', 0) }} du prix final (calculé), proche des 11 % de l'ensemble de la chaîne.

Pour l'exploitation, la chaîne longue a de vrais avantages : de gros volumes, un enlèvement à la ferme, peu de temps de vente et souvent un contrat. Un cofondateur d'Ethiquable résume le dilemme : en proximité, les producteurs vendent à très bon prix, mais de petites quantités ; en chaîne longue, ils vendent de gros volumes à des prix peu satisfaisants[^oxfam].

## Où entrent le pétrole et le gaz

Dans l'Union européenne, produire, transformer, emballer et amener la nourriture jusqu'à la table consommait 17 % de l'énergie brute en 2013[^jrc]. Selon le Centre commun de recherche de la Commission (JRC) :

- **Agriculture** : près d'un tiers de l'énergie de la chaîne alimentaire. Ce poste est traité dans les autres fiches[^jrc].
- **Transformation industrielle** : 28 %[^jrc].
- **Transport et logistique** : 9,4 % de l'énergie contenue dans la nourriture consommée. Le transport routier assure 90 % des trajets de nourriture à l'intérieur de l'Union, le plus souvent au diesel ; 83 % des importations alimentaires arrivent par bateau[^jrc].
- **Froid et magasins** : la vente au détail représente environ 12 % de l'énergie de la logistique. Dans les petits magasins, le froid peut absorber jusqu'à 60 % de l'électricité, selon une étude britannique citée par le JRC[^jrc]. L'électricité suit en partie le prix du gaz (voir la fiche [électricité du réseau](../energie/electricite-reseau.md)).
- **Emballages** : 10,7 % de l'énergie (plastiques issus du pétrole, cartons, verre)[^jrc].
- **Déplacement du consommateur** : la voiture jusqu'au supermarché. L'ADEME (France) le compte parmi les postes majeurs du transport de l'alimentation[^ademe].

Ces chiffres sont européens et datent de 2013 : aucun équivalent belge n'a été trouvé (voir « À vérifier »).

## Les alternatives

Les trois alternatives raccourcissent la chaîne : au plus un intermédiaire entre le producteur et le mangeur. Elles se combinent souvent sur une même ferme. Le transport lui-même (camionnette électrique, tournées groupées, vélo-cargo) est traité dans la fiche [utilitaire diesel de livraison](../transport/vehicules-livraison.md).

**La part du prix qui reste au producteur** (au même prix final, exemple de la pomme de terre à {{ v('pdt_prix_detail_2022') }}, calculé) :

| Canal | Part du prix final pour le producteur | Recette par kg |
|---|---|---|
| Chaîne longue (estimation pour la pomme de terre) | {{ v('pdt_part_agriculteur_long', 0) }} | {{ v('pdt_prix_agriculteur_2022', 2) }} |
| Magasin coopératif (marge de {{ v('marge_coop_magasin', 0) }}) | {{ v('part_producteur_coop_magasin', 0) }} | {{ v('pdt_recette_coop_magasin') }} |
| Coopérative en ligne avec point de dépôt (marge de {{ v('marge_coop_en_ligne', 0) }}) | {{ v('part_producteur_coop_en_ligne', 0) }} | {{ v('pdt_recette_coop_en_ligne') }} |
| Plateforme de type La Ruche qui dit Oui (commission de {{ v('marge_plateforme_ruche', 0) }}) | {{ v('part_producteur_ruche', 0) }} | {{ v('pdt_recette_ruche') }} |
| Abonnement ou vente à la ferme | 100 %, moins les frais de vente | prix fixé par le producteur |

Au même prix final, le producteur reçoit {{ v('pdt_ratio_coop_long', 1) }} plus en vendant par une coopérative en ligne qu'en chaîne longue (calculé). **Ce rapport surestime le gain.** En circuit court, le producteur lave, trie, emballe, étiquette et livre lui-même : il fait une partie du travail que la chaîne longue payait. Les marges des coopératives et des plateformes viennent de sources de 2020 et 2021 ; le prix de la pomme de terre et l'estimation de Greenpeace datent de 2022.

### 1. Vente directe groupée (vague 2)

Plusieurs producteurs vendent ensemble, sans grossiste ni centrale d'achat : magasin de producteurs, coopérative citoyenne, marché de producteurs. Le producteur fixe son prix ; la coopérative ajoute sa marge pour payer le magasin, le personnel et la logistique[^oxfam].

**Le cas de Paysans-Artisans.** Cette coopérative de producteurs et de consommateurs du Namurois réunissait fin 2021 environ 120 producteurs, 8 magasins, 18 points de retrait et 5 000 consommateurs, pour un chiffre d'affaires de 7,5 millions d'euros par an. Elle employait 44 salariés et s'appuyait sur près de 500 bénévoles[^alterechos]. Sa marge est de {{ v('marge_coop_en_ligne', 0) }} en vente en ligne et de {{ v('marge_coop_magasin', 0) }} en magasin[^alterechos]. En magasin, cette marge se partage entre la logistique (10 %) et les frais du magasin (20 %). La vente aux professionnels ne prend que 10 %, et les marchés organisés par la coopérative ne prennent pas de marge[^unamur].

**Le Collectif 5C.** Fin 2022, ce collectif fédérait une quarantaine de coopératives citoyennes de circuit court en Wallonie et à Bruxelles, soit plus de 11 000 coopérateurs et 1 150 producteurs[^oxfam]. Les coopératives n'ont pas de règle commune de prix : certaines appliquent une marge unique, d'autres une marge par produit (pour couvrir les pertes en fruits et légumes), d'autres encore fixent les prix avec les maraîchers en début de saison[^oxfam]. La Wallonie a financé trois hubs logistiques à Liège, Namur et Charleroi, pour que les producteurs livrent un seul point au lieu que la coopérative fasse le tour des fermes[^oxfam] (voir la fiche [utilitaire diesel de livraison](../transport/vehicules-livraison.md)).

**La demande existe.** En 2025, 34 % des Belges francophones achetaient au moins une fois par mois par un canal « alternatif » : 30 % sur des marchés de producteurs, 26 % dans des magasins à la ferme, 21 % auprès de producteurs ou de coopératives[^apaq-2026]. Mais 91 % passent au moins une fois par mois en grande surface[^apaq-2026].

Conditions :

- un collectif qui porte le magasin ou la plateforme, avec des salariés et souvent des bénévoles ;
- une gamme large : un client ne fait pas ses courses à plusieurs adresses ;
- des aides publiques pour les bâtiments et les hubs. Selon la méta-analyse de l'INRAE citée par Oxfam, vendre ensemble (par exemple en magasin de producteurs) fait partie des conditions pour que le circuit court augmente le revenu[^oxfam].

Limites :

- le prix : 53 % des Belges francophones citent le prix plus élevé comme premier frein, et 70 % jugent les prix de ces canaux trop élevés, même si 55 % en comprennent les raisons[^apaq-2026] ;
- les volumes : 5 % des fruits et légumes frais seulement passent par les circuits courts[^ucl-legumes] ;
- le temps de travail : prises de commande, livraisons, communication et comptabilité s'ajoutent à la production. L'épuisement guette, surtout les premières années[^oxfam].

Aides (voir [les aides publiques](../../aides.md)) :

- **à la ferme**, l'AII « diversification » paie {{ v('aii_diversif_taux_base', 0) }} de base d'un coût simplifié, plus 10 % pour un jeune agriculteur et 10 % en bio ou en qualité : 512 €/m² pour aménager un local de vente, 1 144 €/m² pour le construire, 1 100 € pour une balance-étiqueteuse[^am-aii]. L'AII exclut le commerce de détail, sauf la vente à la ferme de produits issus en partie de la production du demandeur[^agw-aii] : un magasin de producteurs en ville ne passe pas par l'AII d'un agriculteur seul ;
- **en collectif**, une coopérative de transformation et de commercialisation (SCTC) peut demander l'AII ({{ v('aii_diversif_taux_base', 0) }} de base, avec des bonus selon le nombre de membres, plafond de 500 000 € d'aide sur 2023-2027)[^am-aii]. Un bâtiment de vente ou de stockage partagé peut aussi devenir un hall relais agricole : {{ v('hra_taux_base', 0) }} des investissements, plus deux bonus de 15 % au maximum, plafond de 200 000 €, pour un promoteur (commune ou structure qui valorise des produits agricoles), jamais pour un agriculteur seul. Aucun appel n'a été trouvé pour 2026[^hra] ;
- ces aides allègent le bâtiment et le matériel, pas le salaire du personnel ni le temps de vente : la vague 2 ne change pas.

### 2. Points de dépôt (vague 2)

Le client commande en ligne avant une date limite ; le producteur ou la coopérative livre les commandes dans un point de retrait (une salle, un commerce, une école, une ferme) à jour et heure fixes. Le producteur ne vend que ce qui est commandé.

Exemples :

- chez Paysans-Artisans, la vente en ligne réunissait en 2021 en moyenne 550 consommateurs par semaine, pour un panier moyen de 55 euros. C'était l'activité la plus rentable de la coopérative, parce qu'elle ne fait presque pas de pertes : ce qui est commandé est déjà vendu[^unamur]. Les commandes sont réparties par des bénévoles dans les points de retrait[^alterechos] ;
- La Ruche qui dit Oui fonctionne de même, avec des points de retrait tenus par un responsable indépendant. Sur 100 € de commande, le producteur reçoit 80 €, le responsable 8,35 € et la plateforme 11,65 € (chiffres français)[^ruche] ;
- les groupes d'achats communs (GAC), nombreux en Wallonie, commandent ensemble chez un ou plusieurs producteurs[^ecoconso].

Le point de dépôt concentre la livraison : une tournée dessert des dizaines de clients au lieu que chacun vienne en voiture à la ferme. À Liège, l'analyse de cycle de vie de Point Ferme, qui livrait les légumes d'un maraîcher dans des points de collecte en camionnette réfrigérée, a montré que ce système limite l'impact face à des clients qui se déplaceraient seuls. Distribuer 2 kg de légumes émettait 0,735 kg d'équivalent CO₂, à 91 % pour la tournée en camionnette[^pointferme].

Conditions :

- assez de clients près du point de dépôt pour remplir la tournée ;
- un outil de commande en ligne (souvent mutualisé : le Collectif 5C a développé un outil commun de vente en ligne[^oxfam]) ;
- des bénévoles ou un responsable pour tenir le point de retrait.

Aides :

- un **distributeur automatique** à la ferme est une variante du point de retrait sans personne : l'AII « diversification » paie {{ v('aii_diversif_taux_base', 0) }} de base d'un coût simplifié de 275 € par casier non réfrigéré, 440 € par casier réfrigéré, ou 11 000 € pour un carrousel réfrigéré[^am-aii] ;
- pour la tournée, voir la fiche [utilitaire diesel de livraison](../transport/vehicules-livraison.md#1-utilitaire-electrique-vague-1) : la déduction fédérale pour investissement de {{ v('dpi_thematique_pp', 0) }} vaut pour une camionnette ou un vélo-cargo électrique neuf à usage exclusivement professionnel, au régime réel seulement[^dpi-tm] ;
- aucune aide ne paie l'outil de commande en ligne ni la tenue du point de retrait. La vague 2 ne change pas.

Limites :

- **le pétrole reste dans la camionnette.** Par kilomètre et par tonne, un poids lourd de 32 tonnes émet environ dix fois moins qu'une camionnette de moins de 3,5 tonnes, selon l'ADEME (France)[^ademe]. Une camionnette peu remplie qui rentre à vide peut donc consommer plus de carburant par kilo qu'un camion plein venu de loin. À Liège, sans compter le trajet du client, la tournée de Point Ferme avait un impact plus élevé que des légumes de supermarché arrivés par bateau, mais plus faible que des légumes arrivés par avion[^pointferme] ;
- seuls 8 % des Belges francophones utilisent chaque mois un groupe d'achats ou une plateforme de commande groupée, et la commande en ligne attire peu[^apaq-2026] ;
- la camionnette elle-même : voir la fiche [utilitaire diesel de livraison](../transport/vehicules-livraison.md), qui chiffre le diesel d'une camionnette de livraison à {{ v('utilitaire_diesel_eur_an') }} (calculé) pour {{ v('utilitaire_km_an') }} (hypothèse).

### 3. Abonnements payés d'avance (vague 2)

Les mangeurs s'engagent pour une saison ou une année et paient d'avance. En échange, ils reçoivent une part de la récolte, en panier ou en autocueillette. Le producteur connaît ses débouchés avant de semer, encaisse avant les dépenses de la saison et écoule toute sa production[^ecoconso]. Le mangeur partage le risque : une mauvaise année donne des paniers plus légers.

Plusieurs formes coexistent en Belgique :

- **GASAP** (groupes d'achat solidaires de l'agriculture paysanne), surtout à Bruxelles : un groupe de ménages s'engage pour l'année auprès d'un maraîcher. Le premier est né en 2006 ; la Région en comptait plus de 75 en 2016. Le réseau conseille au moins 15 paniers par groupe, sinon le producteur ne se déplace pas. Le paiement se fait au trimestre : 120 € d'un coup, soit 10 € par panier, ce qui freine les ménages modestes[^gasap] ;
- **CSA ou ASC** (agriculture soutenue par la communauté), souvent en autocueillette : les membres viennent récolter au champ[^ecoconso]. En Flandre, en 2014, 19 fermes CSA cultivaient en moyenne {{ v('csa_surface_moyenne_2014') }} pour {{ v('csa_membres_moyen_2014', 0, unite=False) }} équivalents adultes chacune. La part d'autocueillette coûtait environ {{ v('csa_part_adulte_2014', 0, unite=False) }} € par adulte et par an (de 220 à 265 €)[^vl-csa-2015]. Exemples wallons plus récents : 350 € par an à Gesves en 2024[^dh-gesves], 520 € par adulte à Jambes en 2025, sur 0,7 ha de légumes bio[^dh-jambes].

**Ce que cela rapporte.** Avec les chiffres flamands de 2014, une ferme CSA moyenne encaisse {{ v('csa_recette_ferme') }} de parts, soit {{ v('csa_recette_ha') }} (calculé). Cet argent arrive avant la saison, sans intermédiaire, sans emballage ni livraison en autocueillette. Il doit pourtant payer les semences, l'eau, les serres, l'amortissement et le travail de toute une année. Un maraîcher wallon interrogé par La Libre en 2024 estimait gagner 7 à 8 € de l'heure en comptant toutes ses heures[^lalibre-maraicher]. Aucune donnée récente sur le revenu des fermes en abonnement en Wallonie n'a été trouvée (voir « À vérifier »).

Conditions :

- une ferme diversifiée (maraîchage, petit élevage), près d'une ville ou d'un village ;
- une communauté de mangeurs à animer : réunions, journées de travail, lettres d'information ;
- de la sécurité sur la terre : plusieurs fermes CSA flamandes citent l'accès sûr à la terre comme leur principale incertitude[^vl-csa-2015].

Limites :

- le modèle convient au maraîchage et au petit élevage, pas aux grandes cultures ni au lait livré en gros ;
- peu de mangeurs s'engagent : l'abonnement, la prise de parts et le bénévolat attirent moins de 15 % des Belges francophones[^apaq-2026] ;
- le paiement d'avance exclut une partie des ménages, sauf solidarité interne au groupe[^gasap].

Aides : aucune aide ne vise l'abonnement lui-même. Si la ferme est certifiée bio, elle touche l'aide au maintien en bio : {{ v('bio_maraichage_eur_ha', 0) }} sur les premiers hectares de maraîchage, ou un forfait de 4 000 €/ha pour le petit maraîchage diversifié bio (3 ha au plus sur ce code, 10 ha en tout, 12 catégories de légumes)[^bio]. C'est une petite part de la recette par hectare d'une ferme en abonnement ({{ v('csa_recette_ha') }} avec les chiffres flamands de 2014, calculé) : l'aide soutient le revenu sans changer la vague.

## Ce qui ferme la boucle

- Le circuit court garde la valeur sur le territoire. La part retenue par les intermédiaires paie des emplois locaux (magasins, logistique, transformation) au lieu de partir dans une chaîne nationale ou internationale.
- Les points de dépôt et les hubs remplacent les trajets de chaque client vers chaque ferme par une tournée unique. Leur bilan dépend du remplissage du véhicule et du trajet du client.
- Les caisses consignées et les emballages réutilisés reviennent au producteur à la tournée suivante. Le réemploi évite des emballages sans ajouter de transport[^ademe].
- Les légumes hors calibre trouvent preneur en vente directe ou en transformation locale, au lieu d'être écartés par la chaîne longue[^ademe].
- L'ordre logique : d'abord regrouper les ventes et les livraisons, ensuite électrifier la camionnette (voir la fiche [utilitaire diesel de livraison](../transport/vehicules-livraison.md)), enfin rapprocher les points de dépôt des clients.

## À vérifier

- Études de l'Observatoire des prix (SPF Économie, Institut des comptes nationaux) sur la formation des prix et des marges, dont « Évolution des prix et des marges dans la chaîne alimentaire » (9 février 2024) et l'analyse de la filière pomme de terre (2019) : site inaccessible (captcha). Elles doivent remplacer le chiffre de 11 % rapporté par la presse et l'estimation de Greenpeace.
- Part du prix payée au producteur pour quelques produits belges types (lait, pain, pommes de terre de consommation, carottes) en grande distribution.
- Énergie du transport, du froid et des emballages dans la chaîne alimentaire belge (chiffres trouvés : moyenne européenne de 2013).
- Marges actuelles de Paysans-Artisans et d'autres coopératives du Collectif 5C (chiffres lus de 2021) ; barème belge de La Ruche qui dit Oui (chiffres lus : France, 2020).
- Nombre actuel de GASAP, de GAC et de fermes CSA en Wallonie et à Bruxelles, et prix des paniers et des parts (sites du Réseau des GASAP et des réseaux CSA inaccessibles à notre outil).
- Revenu et temps de travail des fermes en circuit court en Wallonie : temps de vente, de préparation des commandes et de livraison par semaine, revenu horaire.
- Mise en service et services des hubs logistiques de Liège, Namur et Charleroi.
- Bilan énergétique d'une tournée de points de dépôt bien remplie, comparé à la chaîne longue pour un produit belge.
- Accès d'un magasin de producteurs ou d'un point de dépôt hors de la ferme à l'AII (exclusion du commerce de détail) ; appel 2026 aux halls relais agricoles (aucun trouvé).
- Déduction fédérale pour investissement : cas d'un agriculteur imposé au forfait (non vérifié).

## Sources

[^lalibre-comeos]: « Crise agricole : "Le consommateur paye trop peu pour ses aliments" », Belga, La Libre, 12 mars 2024 (audition de Comeos et de la Commission européenne en commission de l'Économie de la Chambre). https://www.lalibre.be/economie/entreprises-startup/2024/03/12/crise-agricole-le-consommateur-paye-trop-peu-pour-ses-aliments-PFQ75KO24RG5PCXRQQQUBKMWEY/
[^chambre-prix]: Proposition de loi modifiant le Code de droit économique et visant à permettre un contrôle accru de la chaîne d'approvisionnement agricole et alimentaire, Chambre des représentants, doc. 55 3889/001, 8 mars 2024 (cite Observatoire des prix – Institut des comptes nationaux, « Evolution des prix et des marges dans la chaîne alimentaire », 9 février 2024). https://www.dekamer.be/FLWB/PDF/55/3889/55K3889001.pdf
[^greenpeace-pdt]: « Bénéfices records pour l'industrie de la pomme de terre, les miettes pour le monde agricole », résumé du rapport, Greenpeace Belgique, juin 2024 (d'après Test-Achats, Statbel et l'Analyse des prix 2019 du SPF Économie). https://www.greenpeace.org/static/planet4-belgium-stateless/2024/06/136d1eab-rapport-greenpeace_resume-fr_benefices-records-pour-lindustrie-de-la-pomme-de-terre-les-miettes-pour-le-monde-agricole.pdf
[^ucl-legumes]: Riera A., Antier C. et Baret P., « État des lieux et scénarios à horizon 2050 de la filière légumière en Région wallonne », UCLouvain pour la Wallonie, 31 janvier 2020 (d'après Collège des producteurs et FWH, 2018). https://agriculture.wallonie.be/files/20182/21867/UCLouvain_Etude_le%C2%B4gumes_Rapport_200131.pdf
[^oxfam]: Veillard P., « Développement de filières agroécologiques en Belgique. Pour une approche territoriale et équitable », Oxfam-Magasins du monde, décembre 2022. https://www.oxfammagasinsdumonde.be/content/uploads/2023/09/Etude-Developpement-de-filieres-agroecologiques-en-Belgique.pdf
[^jrc]: Monforti-Ferrario F., Pinedo Pascua I. (dir.), « Energy use in the EU food sector: State of play and opportunities for improvement », Centre commun de recherche (JRC), Commission européenne, rapport EUR 27247 EN, 2015 (données de 2013). https://publications.jrc.ec.europa.eu/repository/bitstream/JRC96121/ldna27247enn.pdf
[^ademe]: « Alimentation – Les circuits courts de proximité », Les avis de l'ADEME, juin 2017 (France). https://agir-ese.org/sites/default/files/externe/avis-ademe_circuits-courts_201706.pdf.pdf
[^alterechos]: Legrand M., reportage sur la coopérative Paysans-Artisans (rubrique « Focales »), Alter Échos n° 499, décembre 2021, p. 58-65. https://www.alterechos.be/wp-content/uploads/2021/12/AE499_WEB-30-35.pdf
[^unamur]: Legrand C., « Mémoire projet Paysans-Artisans. Comment les bénévoles communiquent-ils sur la coopérative et comment mobiliser ces derniers ainsi que des consommateurs ? », mémoire de master, Université de Namur, 2021. https://pure.unamur.be/ws/portalfiles/portal/54079275/2021_LegrandC_memoire_.pdf
[^apaq-2026]: « Baromètre. Modes alternatifs de commercialisation des produits alimentaires », Observatoire de la consommation, Apaq-W, mars 2026 (enquête de mai-juin 2025 auprès de 1 500 Belges francophones). https://www.apaqw.be/sites/default/files/uploads/Observatoire/2026/obs-edm-modescommercialisation160326.pdf
[^ruche]: « De la fourche à l'assiette : le vaste réseau de circuit court de La Ruche qui dit Oui ! », L'info durable, 13 novembre 2020 (France). https://www.linfodurable.fr/conso/de-la-fourche-lassiette-le-vaste-reseau-de-circuit-court-de-la-ruche-qui-dit-oui-21287
[^ecoconso]: « Alimentation durable : où trouver des produits locaux, bio ? », Écoconso, consulté le 26 novembre 2026. https://ecoconso.be/fr/node/6568/printable/pdf
[^pointferme]: Hollange B., « Contribution à l'étude de l'impact environnemental des circuits courts alimentaires », mémoire d'ingénieur civil, Université de Liège, 2018. https://matheo.uliege.be/bitstream/2268.2/5529/10/Contribution%20%c3%a0%20l%27%c3%a9tude%20de%20l%27impact%20environnemental%20des%20circuits%20courts%20alimentaires.pdf
[^gasap]: « Pour notre alimentation, traiter directement avec le producteur », entretien avec la coordinatrice du Réseau des GASAP, Courant Alternatives (fiche Éducation permanente), 2016. https://www.cultures-sante.be/wp-content/uploads/2023/11/ep2016-courant-alternatives-fiche-gasap.pdf
[^vl-csa-2015]: Zwaenepoel E. et Van Gijseghem D., « Landbouw in stedelijke omgeving. CSA's en andere initiatieven », Departement Landbouw en Visserij (Vlaamse overheid), 2015. https://publicaties.vlaanderen.be/view-file/16343
[^dh-gesves]: « Gesves : de l'auto-cueillette dans un grand potager », La DH, 25 avril 2024. https://www.dhnet.be/regions/namur/2024/04/25/gesves-de-lauto-cueillette-dans-un-grand-potager-VW6DEIFTMVALLHKXUDSKX4WO3E/
[^dh-jambes]: « Les Jardins D'À Côté lancent une nouvelle saison à Jambes », La DH, 14 février 2025. https://www.dhnet.be/regions/namur/2025/02/14/les-jardins-da-cote-lancent-une-nouvelle-saison-a-jambes-EZP27TT5EREEBB6Z4LII6CVHWA/
[^lalibre-maraicher]: Dath-Delcambe P., « "Si je compte toutes les heures que je passe à cultiver, je gagne 7-8 euros de l'heure" », La Libre, 26 juillet 2024 (titre et début de l'article, accès réservé aux abonnés). https://www.lalibre.be/economie/entreprises-startup/2024/07/26/si-je-compte-toutes-les-heures-que-je-passe-a-cultiver-je-gagne-7-8-euros-de-lheure-Z57MI3AE6ZBGXARDNP5TDONF2Q/
[^am-aii]: Arrêté ministériel du 23 février 2023 exécutant l'arrêté du Gouvernement wallon du 23 février 2023 relatif aux aides à l'installation et aux investissements, version consolidée (modifications des 15 janvier et 11 mai 2026), articles 13 à 16 et annexe 3, Wallex, consulté le 27 novembre 2026. https://wallex.wallonie.be/eli/arrete/2023/02/23/2023042748
[^agw-aii]: Arrêté du Gouvernement wallon du 23 février 2023 relatif aux aides à l'installation et aux investissements, version en vigueur depuis le 1er janvier 2026, article 6, Wallex, consulté le 27 novembre 2026. https://wallex.wallonie.be/eli/arrete/2023/02/23/2023042313/2026/01/01
[^hra]: Arrêté du Gouvernement wallon du 30 août 2018 fixant les conditions d'octroi des subventions relatives aux halls relais agricoles, version en vigueur depuis le 9 novembre 2023, Wallex, consulté le 27 novembre 2026. https://wallex.wallonie.be/sites/wallex/contents/acts/3/3926/2.html
[^dpi-tm]: « Véhicules à zéro émissions : la déduction pour investissement est opérationnelle », Transportmedia, 1er avril 2026, consulté le 27 novembre 2026. https://transportmedia.be/fr/2026/04/vehicules-a-zero-emissions-la-deduction-pour-investissement-est-operationnelle/
[^bio]: « Soutien à l'agriculture biologique », Portail de l'agriculture wallonne, page modifiée le 17 avril 2026, consultée le 27 novembre 2026. https://agriculture.wallonie.be/home/aides/pac-2023-2027-description-des-interventions/soutien-a-l-agriculture-biologique.html
