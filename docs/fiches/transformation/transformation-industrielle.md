---
id: transformation-industrielle
titre: Transformation industrielle centralisée
domaine: transformation
dependance_fossile: gasoil (transport); gaz (procédés)
alternatives: [Atelier de découpe, presse à huile, moulin à meules, légumerie-conserverie]
vague_meilleure_alternative: 1
statut: relu
maj: 2026-11-27
---

# Transformation industrielle centralisée

## En bref

La plupart des produits de la ferme quittent l'exploitation bruts (grain, graines, carcasses, légumes) et sont transformés dans quelques grandes usines, souvent loin de la ferme, parfois hors de Wallonie. Le fossile entre par le transport, par les procédés qui chauffent ou refroidissent et par les emballages : l'industrie alimentaire wallonne a consommé 6 397 GWh d'énergie en 2023, et le gaz naturel est le premier vecteur d'énergie de l'industrie wallonne (38 %)[^indus]. Transformer soi-même, à la ferme ou à plusieurs, raccourcit le trajet et garde la valeur ajoutée : la découpe de viande pour la vente en colis est rentable aujourd'hui quand la clientèle existe (vague 1). La presse à huile et le moulin à meules rapportent environ {{ v('huile_alim_ecart_tonne', 0) }} et {{ v('farine_ecart_tonne_ble', 0) }} de plus que la vente en vrac (calculé, avant travail et emballages), mais demandent un investissement, du temps et un réseau de clients (vague 2). La légumerie-conserverie se monte surtout en collectif, avec des aides et des contrats avec les cuisines de collectivités (vague 2).

## Comment ça marche aujourd'hui

**Le schéma centralisé.** L'agriculteur vend une matière première au prix du marché, et la transformation se fait ailleurs. Quelques exemples wallons :

- **Farine.** En 2015, la meunerie wallonne ne pesait que 2 % de la farine belge. Elle transformait environ 20 000 t de grain, soit 8 % du blé panifiable wallon ; le reste était moulu en Flandre. Trois moulins produisaient 75 % de la farine belge[^winandy]. Les grands moulins du nord du pays sont approvisionnés par bateau ou par train, souvent en blés étrangers, par milliers de tonnes[^farwal]. Pour les fondateurs de la coopérative Bel'grains, la majorité de la farine vendue en Belgique n'est ni produite, ni transformée, ni emballée dans le pays[^belgrains].
- **Viande.** Peu d'abattoirs wallons acceptent encore de petits lots avec reprise de la carcasse : 10 en 2021 selon le CRA-W, après la fermeture de 3 autres depuis 2018[^craw-viande]. Dans l'échantillon d'éleveurs étudié, la ferme était en moyenne à 49 km de l'abattoir, l'abattoir à 36 km de l'atelier de découpe, et l'atelier à 24 km de la ferme[^craw-viande].
- **Légumes.** La consommation d'énergie de l'industrie alimentaire wallonne a augmenté de 112 % entre 1990 et 2023, poussée par la transformation de la pomme de terre[^indus].

**Ce que reçoit l'agriculteur.** Le prix de la matière brute. Fin novembre 2026, le blé tendre vaut environ {{ v('ble_prix') }} (cotation indicative belge de la FEGRA)[^fegra]. La graine de colza valait environ {{ v('colza_prix') }} le 24 novembre 2026 sur le marché à terme Euronext (Paris, échéance février 2027)[^reussir-colza]. En 2020, une carcasse de bovin se payait de 3,37 €/kg (vache de race étrangère) à 4,72 €/kg (jeune taureau Blanc Bleu Belge) HTVA[^craw-viande]. La valeur ajoutée de la mouture, du pressage, de la découpe et de l'emballage revient à l'aval.

## Où entrent le pétrole et le gaz

- **Transport.** Camions entre la ferme, le négociant, l'usine, l'entrepôt et le magasin ; bateaux et trains pour les grains importés. Tout cela roule au gasoil.
- **Procédés de chauffe.** Séchage, cuisson, friture, blanchiment et stérilisation des conserves : dans l'industrie, la chaleur vient surtout du gaz naturel, premier vecteur d'énergie de l'industrie wallonne en 2023 (14 572 GWh, 38 % de sa consommation finale)[^indus]. La part du gaz propre à l'industrie alimentaire n'a pas été trouvée.
- **Froid.** Chambres froides, surgélation, camions frigorifiques : électricité du réseau (en partie produite au gaz) et gasoil des groupes frigorifiques.
- **Emballages.** Films, barquettes, sachets sous vide et bouteilles en plastique sont tirés du pétrole ; le verre et le métal demandent beaucoup de chaleur à la fabrication.
- **Concentration des outils.** Moins il y a d'usines et d'abattoirs, plus les trajets s'allongent. La fermeture d'un outil local se paie en kilomètres.

## Les alternatives

Toutes les alternatives qui suivent ont un point commun : on garde le produit plus longtemps sur la ferme ou dans la région, on le transforme avec des outils plus petits, souvent électriques, et on le vend plus près. Elles ne suppriment pas tout le fossile (voir les limites de chaque alternative), mais elles raccourcissent les trajets et rapportent davantage par tonne.

**Les aides wallonnes à connaître :**

- **Aide aux investissements (AII), transformation et diversification.** Pour un agriculteur actif, l'aide vaut {{ v('aii_diversif_taux_base', 0) }} d'un montant forfaitaire fixé par type d'investissement (le « coût simplifié »), plus 10 % pour un jeune agriculteur et 10 % pour des produits biologiques ou de qualité. Ce n'est pas un pourcentage du prix réel : quand le matériel coûte bien plus que le forfait, l'aide en couvre une petite part. Pour une coopérative de transformation et de commercialisation (SCTC), le taux de base est aussi de {{ v('aii_diversif_taux_base', 0) }}, avec des bonus selon le nombre de membres et la part de production bio ou de qualité. Sur 2023-2027, l'aide totale est plafonnée à 200 000 € par agriculteur et à 500 000 € par SCTC ou entreprise[^am-aii]. La demande d'un agriculteur doit atteindre {{ v('aii_seuil_points', 0, unite=False) }} points de sélection, une seule demande par trimestre, et le matériel d'occasion est exclu[^am-aii].
- **Halls relais agricoles.** Un bâtiment de stockage, de transformation, de conditionnement ou de vente partagé par des agriculteurs ou une SCTC peut recevoir une subvention de {{ v('hra_taux_base', 0) }} des investissements admissibles, avec au plus deux bonus de 15 % (par exemple un engagement écrit d'au moins cinq agriculteurs, ou deux emplois à temps plein créés). La subvention est plafonnée à 200 000 € ; pour un pouvoir public, elle monte à 80 %[^hra]. Une aide à la consultance (10 000 € au plus) et une aide au fonctionnement (20 000 € au plus sur trois ans) sont prévues, et le hall doit fonctionner dans les 36 mois[^hra]. L'aide va à un « promoteur » (commune, ou structure qui valorise des produits agricoles), jamais à un agriculteur seul. Le Ministre ouvre des appels à projets : aucun n'a été trouvé pour 2026, les derniers trouvés datent de 2015 et 2018[^hra].
- Les montants et les règles de cumul sont rassemblés dans [les aides publiques](../../aides.md#les-aides-a-linvestissement-agricole-aii).
- **Accompagnement.** La cellule DiversiFerm (Gembloux Agro-Bio Tech et Accueil Champêtre en Wallonie) conseille les agriculteurs-transformateurs sur l'hygiène, les démarches AFSCA et l'économie de leur projet[^vm2019].

**La règle AFSCA de base.** La production primaire demande un simple enregistrement. La transformation (atelier de découpe, meunerie, fabrication de produits à base de fruits et légumes…) et la vente au détail demandent en général une autorisation ou un agrément[^vm2019]. Les petites structures qui vendent directement au consommateur (au plus cinq équivalents temps plein ou moins de 400 m²) bénéficient d'un autocontrôle et d'une traçabilité « assouplis », basés sur un guide sectoriel[^vm2019].

### 1. Atelier de découpe (vague 1)

**Principe.** L'animal est toujours abattu dans un abattoir agréé par l'AFSCA[^vm2019]. La carcasse est ensuite découpée et emballée, soit par un boucher prestataire ou dans un atelier partagé, soit dans un atelier à la ferme, puis vendue en colis ou au détail. La viande fraîche non emballée ne peut être manipulée que par une personne qui a l'accès à la profession de boucher[^craw-viande].

**Les chiffres wallons (CRA-W, données 2020).** Sur sept fermes qui font découper hors de l'exploitation et vendent du bœuf en colis[^craw-viande] :

| Poste | Valeur |
|---|---|
| Investissement de départ | environ 1 300 €[^craw-viande] |
| Abattage d'un bovin adulte | de 96,50 à 136 € HTVA selon l'abattoir[^craw-viande] |
| Abattage, découpe et transformation | 2,26 €/kg de carcasse, soit 734 € par bovin en moyenne[^craw-viande] |
| Chiffre d'affaires | 8,9 €/kg de carcasse[^craw-viande] |
| Coût de revient total (carcasse comptée au prix du marché, travail payé) | 7,7 €/kg de carcasse[^craw-viande] |
| Marge | 1,2 €/kg de carcasse, soit 288 € par bovin de 330 kg[^craw-viande] |

Le coût de revient compte la carcasse au prix du marché et rémunère le travail de l'éleveur à 15 €/h brut (bénévoles à 10 €/h)[^craw-viande]. La marge vient donc en plus de la vente de la carcasse au marché et du salaire. Elle varie beaucoup : une ferme sur sept perdait de l'argent[^craw-viande]. Le colis moyen se vendait 13,9 €/kg[^craw-viande].

Une boucherie à la ferme coûte beaucoup plus cher : 65 000 € d'investissement en moyenne, et 2 jours de travail à deux personnes par bovin, plus une demi-journée de nettoyage[^craw-viande].

**En collectif.** Huit éleveurs de Wallonie picarde ont créé la coopérative Wapicowp et repris en 2022 une salle de découpe à côté de l'abattoir d'Ath. Deux bouchers devaient y traiter de 8 à 10 bêtes par semaine. La part de coopérateur valait 2 500 €, dont 2 000 € récupérables par une aide de la Région wallonne[^dh-wapi]. À Perwez, la coopérative « En direct de mon élevage », lancée en 2018 avec une centaine d'éleveurs, a ouvert son propre hall de découpe en 2019[^dh-perwez].

**AFSCA.** Pour du bœuf, du porc ou du mouton, les démarches dépendent du lieu de découpe et du mode de vente[^vm2019] :

- découpe hors de la ferme et vente directe en colis : autorisation « commerce de détail » ;
- découpe à la ferme et vente directe : autorisation « boucherie » ;
- vente à des intermédiaires : agrément (grossiste, atelier de découpe, fabricant de préparations ou de viande hachée).

La vente directe peut inclure jusqu'à 30 % du chiffre d'affaires annuel en vente indirecte[^vm2019].

**Aides.** La découpe chez un prestataire n'a presque pas d'investissement à aider. Pour un atelier à la ferme, l'AII paie {{ v('aii_diversif_taux_base', 0) }} de base de coûts simplifiés : 512 €/m² pour aménager un local de transformation, 1 144 €/m² pour le construire, 19 € par m³ de local réfrigéré pour le groupe frigorifique[^am-aii]. Pour un atelier partagé, deux voies : l'AII d'une SCTC (plafond de 500 000 € d'aide) ou un hall relais agricole porté par un promoteur ({{ v('hra_taux_base', 0) }} et plus), sous réserve d'un appel ouvert[^am-aii] [^hra]. Ces aides allègent l'atelier collectif, sans changer la vague.

**Pourquoi vague 1.** La vente en colis avec découpe chez un prestataire demande peu d'investissement et dégage une marge positive en moyenne, travail payé. Elle est rentable aujourd'hui quand on a la clientèle et le temps de vendre.

Limites :

- l'abattoir reste un passage obligé, et chaque fermeture d'abattoir rallonge les trajets ;
- les trajets se multiplient en petites quantités : dans l'étude du CRA-W, les trajets cumulés (ferme, abattoir, atelier, retour) allaient de 3 à 366 km selon les fermes[^craw-viande]. Un atelier collé à l'abattoir, comme à Ath, évite un trajet[^dh-wapi] ;
- le sous-vide reste en plastique et le froid consomme de l'électricité ;
- le travail : de 2,4 à 16 heures par bovin pour l'éleveur et ses bénévoles, hors transport[^craw-viande].

### 2. Presse à huile (vague 2)

**Principe.** Une presse à vis écrase la graine de colza (ou de tournesol) à froid. On obtient de l'huile, qu'on laisse décanter puis qu'on filtre, et un tourteau gras pour les animaux. Il n'y a ni hexane ni vapeur, contrairement à l'huilerie industrielle. Les détails techniques du pressage, l'usage de l'huile comme carburant et la valeur du tourteau sont dans les fiches [Tracteur diesel](../traction/tracteur-diesel.md) et [Concentrés et soja importés](../elevage/concentres-importes.md).

**Rendement.** Ce projet compte {{ v('huile_par_tonne', unite=False) }} L d'huile et {{ v('tourteau_par_tonne', 2, unite=False) }} t de tourteau par tonne de graines (valeurs centrales d'une fiche du CRA-W et de l'Idele, qui donne 240 à 350 L d'huile et 0,68 à 0,78 t de tourteau par tonne selon la presse)[^autoprot]. Une étude ancienne de Loire-Atlantique donnait en moyenne 273 L d'huile et 670 kg de tourteau par tonne[^reussir-presses]. Un producteur français obtient environ 80 L d'huile avec 200 kg de graines, en six à sept heures de pressage[^tn-prodel].

**Un exemple chiffré (France, 2026).** Entre Corrèze et Dordogne, un céréalier presse 10 ha de colza et 10 ha de tournesol. Il a investi 60 000 € hors stockage (trieur neuf acheté avec un voisin, presse d'occasion, filtres)[^tn-prodel]. Il vend près de 20 000 L d'huile par an, de plus en plus en bidons de 5 L à 4 €/L, et estime que la tonne de graines ainsi valorisée rapporte 1 500 €, contre 500 € en négoce[^tn-prodel].

**Le calcul du projet.** Avec ce prix de vente, la tonne de graines pressée rapporte {{ v('huile_alim_valeur_tonne', unite=False) }} € (huile et tourteau, calculé), soit {{ v('huile_alim_ecart_tonne', unite=False) }} € de plus que la graine vendue au prix du marché ({{ v('colza_prix') }}). Ce chiffre bouge peu entre les scénarios ({{ fourchette('huile_alim_ecart_tonne') }}) : c'est le prix de vente de l'huile qui fait tout. Il faut encore payer le travail, les bidons et les étiquettes. L'investissement de l'exemple français revient à {{ v('presse_amortissement_litre', 2, unite=False) }} € par litre vendu, sur {{ v('atelier_duree_amortissement', 0) }} (hypothèse).

À comparer avec l'usage carburant : ramenée à l'énergie d'un litre de gasoil, l'huile revient à {{ v('huile_cout_eq_gasoil') }} une fois le tourteau déduit (calculé), contre {{ v('gasoil_agricole_htva') }} HTVA pour le gasoil agricole. Pressage compris ({{ v('pressage_cout', 2) }}, tarif d'une CUMA française à presse amortie), elle est plus chère que le gasoil dans les trois scénarios de prix : de {{ v('huile_ecart_gasoil', 2, scenario='haut') }} de plus au prix haut à {{ v('huile_ecart_gasoil', 2, scenario='bas') }} de plus au prix de février 2026, quand le gasoil valait {{ v('gasoil_agricole_htva', scenario='bas') }} (calculé). Vendue en cuisine, la même huile vaut plusieurs fois plus. L'huile carburant ne se justifie que par l'autonomie ; l'huile alimentaire est un produit qui se vend.

**Conditions :**

- trouver les clients : le producteur français a distribué plus de deux mille dépliants et mis un an à construire son réseau[^tn-prodel] ;
- des graines saines, sans échauffement, et triées pour que l'huile ne soit pas amère ; trois semaines de décantation en fûts[^tn-prodel] ;
- un local propre ; selon le même producteur, transformer des végétaux impose moins de contraintes que le lait ou la viande[^tn-prodel] ;
- **aucune aide pour un agriculteur seul** : l'AII ne prévoit pas de forfait « presse à huile » dans la liste de ses investissements admissibles, même si la fabrication d'huiles et de graisses fait partie des activités agroalimentaires visées, et elle exclut de toute façon le matériel d'occasion, comme la presse de l'exemple français[^am-aii]. La seule voie trouvée est une presse partagée dans un hall relais agricole ({{ v('hra_taux_base', 0) }} des investissements, porté par un collectif ou une commune), mais aucun appel n'a été trouvé pour 2026[^hra]. Le trieur et le local de stockage peuvent relever d'autres lignes de l'AII (non vérifié pour un usage de pressage).

**Pourquoi vague 2.** La valeur ajoutée par tonne est très forte, mais tout repose sur la vente directe d'un produit que les clients achètent en petites quantités. Aucun prix wallon de l'huile de colza fermière n'a été trouvé.

Limites : les bouteilles et bidons (plastique ou verre) restent à fabriquer, et la livraison en petites quantités consomme du carburant par litre vendu. Les bidons consignés limitent l'emballage : le producteur français estime qu'un bidon est amorti en trois allers-retours[^tn-prodel].

### 3. Moulin à meules (vague 2)

**Principe.** Le grain nettoyé passe entre deux meules en pierre. Une meule mesure environ 1,5 m et pèse environ 1,5 t[^farwal]. Une paire de meules écrase de 250 à 300 kg de grain par heure et donne des farines bises à complètes (T80 à T150). La mouture sur cylindres, qui fait plus de 99 % de la farine, produit aussi les farines blanches[^farwal]. Les moulins wallons tournent surtout à l'électricité (trois à l'eau et un au vent en 2015)[^winandy]. Le moulin de Vencimont produit son énergie avec trois installations hydroélectriques et du photovoltaïque[^farwal].

**Ce que coûte un moulin.** Le vade-mecum FARWAL du CRA-W (2024) donne des ordres de grandeur, à ± 30 % selon l'automatisation et l'installation[^farwal] :

| Équipement | Coût indicatif |
|---|---|
| Petit système de réception et de nettoyage du grain | environ 200 000 €[^farwal] |
| Moulin à meules à diagramme simple avec son plansichter (tamis) | 150 000 à 200 000 €[^farwal] |
| Moulin à cylindres complet (pour comparaison) | environ 400 000 €[^farwal] |
| Ensachage simple | 10 000 à 15 000 €[^farwal] |
| Ensachage semi-automatique ou automatique | 50 000 à 100 000 €[^farwal] |

À la ferme, on peut faire plus petit. À la ferme de Corioule (Assesse, 120 ha en bio), l'agriculteur a investi 120 000 € dans un petit moulin à meule de pierre dimensionné pour 20 ha de céréales panifiables[^corioule]. La première année, il a moulu environ 40 t de grain, l'équivalent de 10 ha. Le moulin tourne deux jours par semaine ; la farine part en sacs de 25 kg chez quatre à cinq boulangers réguliers et quatre à cinq occasionnels[^corioule].

**Le calcul du projet.** Un moulin à la ferme wallon annonce sa farine sur pierre de 1 300 à 1 500 €/t[^guide-moulins]. Avec {{ v('farine_rendement', 2, unite=False) }} t de farine par tonne de grain[^winandy], une tonne de blé moulue rapporte {{ v('farine_valeur_tonne_ble', unite=False) }} € (calculé, sans compter le son), soit {{ v('farine_ecart_tonne_ble', unite=False) }} € de plus que le blé vendu au marché ({{ v('ble_prix') }}). Au prix du blé de février 2026, l'écart est même de {{ v('farine_ecart_tonne_ble', unite=False, scenario='bas') }} €. Sur l'exemple de Corioule, l'investissement pèse {{ v('moulin_amortissement_t', unite=False) }} € par tonne de grain (calculé sur {{ v('moulin_tonnage_an', 0) }}, estimé, et {{ v('atelier_duree_amortissement', 0) }}, hypothèse). Restent à payer le travail, le nettoyage et le stockage du grain, les sacs, l'électricité et les analyses.

Une présentation de DiversiFerm citait en 2015 un projet français : blé panifiable vendu 0,40 €/kg, farine de 0,80 à 1,20 €/kg, pain 4 €/kg. Elle rappelait que ces chiffres cachent l'investissement, le temps de travail et les compétences nécessaires[^winandy].

**La mouture à façon.** Sans moulin, on peut faire moudre son grain par un meunier et vendre sa propre farine. Le moulin de Vencimont (Gedinne) a relancé ce service, lancé en 2019 et vraiment démarré en 2021, pour des lots de 500 kg à 12 t. Le vade-mecum FARWAL recommande d'apporter un grain trié, bien stocké, analysé pour les mycotoxines et sans insectes[^farwal].

**AFSCA et permis :**

- la mouture de céréales pour l'alimentation humaine demande une autorisation « Meunerie » ; la farine moulue à façon puis reconditionnée à la ferme demande une autorisation « Conditionneur de denrées alimentaires »[^vm2019] ;
- vendre le son aux animaux d'autres éleveurs demande un enregistrement de fabricant de matières premières pour l'alimentation animale[^vm2019] ;
- hors zone d'activité économique, des machines de 10 à 20 kW relèvent d'une déclaration de classe 3, et à partir de 20 kW d'un permis d'environnement de classe 2[^vm2019].

**Aides.** L'AII prévoit un forfait de {{ v('aii_moulin_petit_forfait') }} pour un moulin sur pierre à meules de 50 à 100 cm, de 22 000 € pour des meules d'un mètre et plus, de 18 150 € pour une ensacheuse à farine et de 14 850 € pour une tamiseuse[^am-aii]. L'aide vaut {{ v('aii_diversif_taux_base', 0) }} de ce forfait pour un agriculteur actif (30 à 40 % pour un jeune agriculteur, en bio ou en qualité différenciée), pas du prix réel[^am-aii]. Face aux 120 000 € investis à Corioule[^corioule], l'aide ne couvre qu'une petite part de l'investissement : elle ne change ni le calcul par tonne ni la vague. Un moulin partagé en SCTC ou dans un hall relais agricole ({{ v('hra_taux_base', 0) }} et plus, sous réserve d'un appel) est la voie où l'aide pèse le plus[^hra].

**Pourquoi vague 2.** La valeur ajoutée par tonne est forte, mais il faut un blé de qualité panifiable, un investissement de plus de 100 000 €, du temps et des boulangers clients[^corioule]. « Le meilleur des investissements n'est rien sans une bonne clientèle », résume le meunier de Vencimont[^farwal]. La mouture à façon permet de tester le marché avant d'investir.

Limites : le moulin consomme de l'électricité (la dépendance passe du gasoil au réseau, sauf avec du photovoltaïque ou de l'hydraulique). Le grain doit être séché et stocké proprement, ce qui peut demander du séchage au gaz (voir la fiche [Séchage des grains](../energie/sechage-grains.md)).

### 4. Légumerie-conserverie (vague 2)

**Principe.** Une légumerie lave, épluche, découpe et emballe les légumes (4e gamme) pour les cuisines de collectivités, qui n'ont souvent plus le personnel ni l'outillage pour traiter des légumes bruts[^dh-liege]. Une conserverie les cuit et les stérilise en bocaux, ce qui permet de vendre toute l'année.

**Les exemples wallons :**

- À Chênée (Liège), la coopérative Terra Alter (Groupe Terre) a ouvert en 2024 une légumerie bio : 5 à 10 personnes, cinq machines, légumes de producteurs bio locaux conditionnés sous vide en sachets de 5 kg pour les écoles, crèches, hôpitaux et maisons de repos. Objectif : 2 t de légumes par jour[^rtbf-terra].
- À Droixhe (Liège), un hub du circuit court avec légumerie et conserverie a été inauguré le 12 novembre 2025 : 3 100 m², 1 400 t de légumes lavés, découpés, emballés et stockés par an, exploité par Terra Alter sur un projet de la SPI[^dh-liege].
- À Charleroi, le hub de la Ceinture alimentaire prévoyait en 2023 de traiter de 1 000 à 2 000 t de légumes locaux par an. Il fait partie des 57 projets de relocalisation alimentaire qui se partageaient 45 M€ de la Région[^lavenir].

**À la ferme.** L'AII prévoit des forfaits pour une laveuse à légumes (5 786 €), un groupe frigorifique (19 € par m³ de local), l'aménagement d'un local de transformation (512 €/m²) ou sa construction (1 144 €/m²)[^am-aii]. Pour les produits à base de pommes de terre (4e gamme comprise), la vente directe demande une autorisation « commerce de détail avec transformation ». On peut aussi livrer d'autres magasins dans un rayon de 80 km, à condition que ces livraisons ne dépassent pas 30 % du chiffre d'affaires. Au-delà, une autorisation de fabricant est nécessaire[^vm2019].

**Aides.** À la ferme, l'AII paie {{ v('aii_diversif_taux_base', 0) }} de base des forfaits ci-dessus[^am-aii]. En collectif, une SCTC peut demander l'AII (plafond de 500 000 € d'aide), et un hall relais agricole peut porter le bâtiment ({{ v('hra_taux_base', 0) }}, jusqu'à 80 % pour une commune, plafond de 200 000 €)[^am-aii] [^hra]. Ces aides ne changent pas la vague : la rentabilité dépend d'abord des contrats avec les cuisines de collectivités.

**Pourquoi vague 2.** Les légumeries wallonnes existent, mais elles sont collectives, portées par l'économie sociale ou des intercommunales, et soutenues par des fonds publics. Leur rentabilité dépend de contrats réguliers avec les cuisines de collectivités. Aucun chiffre de coût ni de prix payé aux producteurs n'a été trouvé.

Limites : la stérilisation demande beaucoup de chaleur. Pour que le gain soit complet, l'autoclave doit chauffer à l'électricité solaire, au bois ou au biogaz plutôt qu'au gaz naturel. Les bocaux en verre sont lourds à transporter ; leur réemploi (consigne) est une condition de cohérence.

## Ce qui ferme la boucle

- Le grain moulu à la ferme laisse son son pour les animaux ; le colza pressé laisse son tourteau. Les coproduits restent sur place ou chez le voisin éleveur, au lieu de faire l'aller-retour vers l'usine et le fabricant d'aliments.
- Un atelier collé à l'abattoir ou à la ferme supprime un trajet, et l'éleveur peut suivre sa bête jusqu'au colis[^dh-wapi].
- Les moulins, presses et légumeries tournent à l'électricité : avec du photovoltaïque ou de l'hydraulique sur place, comme au moulin de Vencimont[^farwal], le procédé ne dépend plus du gaz.
- Les ateliers partagés (halls relais, coopératives, mouture à façon) rendent l'outil accessible aux petites fermes et répartissent l'investissement.
- La vente directe et les cuisines de collectivités proches remplacent la logistique longue. Les emballages réemployés (bidons, bocaux consignés) ferment la boucle des contenants.

## À vérifier

- Part du gaz naturel dans la consommation d'énergie de l'industrie alimentaire wallonne (bilans énergétiques du SPW, devenus inaccessibles à leur ancienne adresse).
- Consommation de gasoil du transport des matières premières agricoles wallonnes vers les usines (céréales vers la Flandre, animaux vers les abattoirs) : aucune donnée trouvée. À comparer avec les trajets en petites quantités du circuit court, qui ne sont pas toujours plus sobres par kilo.
- Prix wallon du blé payé départ ferme : le projet utilise la cotation indicative belge de la FEGRA, dont la base de livraison n'est pas précisée. Prix du colza payé départ ferme en Wallonie : le projet utilise la cotation Euronext (Paris).
- Prix de vente de la farine sur meule : un seul moulin wallon publie une fourchette ; TVA comprise ou non, à confirmer. Rendement réel en farine d'un moulin à meules à la ferme (le chiffre utilisé est une moyenne de toute la meunerie wallonne, 2011).
- Prix wallon de l'huile de colza fermière alimentaire et coût d'une presse en Wallonie en 2026 : seul un exemple français a été lu. Les fiches techniques et économiques de Valbiom sur la trituration à la ferme (années 2000) ne sont plus en ligne à leur adresse.
- Statut AFSCA du pressage d'huile à la ferme et assouplissements actuels : le vade-mecum DiversiFerm lu date de 2019. Le site de l'AFSCA (brochure « vente à la ferme » de juillet 2025, fiche sur les différences entre agrément et autorisation) n'était pas accessible depuis notre outil.
- Coût d'investissement et prix payés aux producteurs par les légumeries de Chênée, Droixhe et Charleroi ; existence de conserveries partagées accessibles aux agriculteurs en Wallonie et leurs tarifs.
- Chiffres du CRA-W sur la viande (données 2020) : à actualiser avec les prix de 2026 (carcasses, abattage, découpe).
- Investissement et fonctionnement actuels des ateliers de Wapicowp (Ath) et d'« En direct de mon élevage » (Perwez).
- Appels à projets « halls relais agricoles » ouverts en 2026 (aucun trouvé ; derniers appels : 2015 et 2018) et forfait AII éventuel pour une presse à huile.
- Plafond de 40 % du forfait pour l'AII à la transformation et à la diversification : écrit pour l'investissement productif, pas retrouvé à l'article 15 de l'arrêté.
- Cumul de l'AII d'un membre et de l'aide d'une SCTC ou d'un hall relais pour un même outil partagé.

## Sources

[^indus]: « Consommation d'énergie de l'industrie », État de l'environnement wallon, SPW, fiche INDUS 1, mise à jour du 19 mai 2026 (d'après les bilans énergétiques du SPW). https://etat.environnement.wallonie.be/contents/indicatorsheets/INDUS%201.eewGeneratePdf.do
[^winandy]: Winandy S., « Du grain au pain : les outils de 1re transformation », DiversiFerm, présentation du 13 juin 2015 (d'après le rapport ALT-4-CER, 2011). https://orbi.uliege.be/bitstream/2268/198657/1/Du%20grain%20au%20pain%20les%20outils%20de%20premi%c3%a8re%20transformation%20-%20Winandy%20S.%202015.pdf
[^farwal]: « Projet FARWAL. Vade mecum sur la création d'une filière céréalière complète », CRA-W, Moulin de Vencimont et Ferme de la Motte, novembre 2024 (récoltes 2021 à 2023). https://cra.wallonie.be/uploads/2025/01/farwal-vadecum-v9.pdf
[^belgrains]: « Bel'grains. Repenser la filière céréales alimentaires », fiche de présentation de la coopérative, Province de Liège (non datée, coopérative créée en septembre 2021), consultée le 26 novembre 2026. https://provincedeliege.be/sites/default/files/media/17335/Bel'grains.pdf
[^craw-viande]: Turlot A. (CRA-W), Jérôme E., Beuve-Mery J. (Accueil Champêtre en Wallonie), « Production et commercialisation de viande bovine en circuits courts. Repères socio-économiques », CRA-W, projet OTEl, avril 2021 (données 2020). https://www.cra.wallonie.be/uploads/2021/04/2021_Production_et_commercialisation_de_viande_bovine_en_circuits_courts_rep%C3%A8res_socio-%C3%A9conomiques.pdf
[^fegra]: Cotations indicatives des produits agricoles (blé standard certifié), FEGRA (fédération belge du négoce de grains), 26 novembre 2026 ; prix hors TVA, base non précisée, non contraignants. https://fegra.be/home/agriculturalprices?lang=fr
[^reussir-colza]: « Marché des oléagineux du 24 novembre 2026 : Le prix du soja engrange une troisième séance de gain sur le CBOT, tandis que le cours du colza sur Euronext cède du terrain », Réussir (France), 24 novembre 2026 (clôture Euronext du colza : 536,50 €/t pour les échéances février et mai 2027), lu le 27 novembre 2026. https://www.reussir.fr/articles/marche-des-oleagineux-du-24-novembre-2026-le-prix-du-soja-engrange-une-troisieme-seance-de
[^autoprot]: « Production de tourteau de colza gras à la ferme », fiche Autoprot C1, CRA-W et Idele, juin 2021, lue le 27 novembre 2026. https://www.autoprot.eu/wp-content/uploads/2021/10/Fiche-C1-Production-de-tourteau-de-colza-gras-a-la-ferme.pdf
[^am-aii]: Arrêté ministériel du 23 février 2023 exécutant l'arrêté du Gouvernement wallon du 23 février 2023 relatif aux aides à l'installation et aux investissements (secteurs agricole et horticole, coopératives et entreprises de transformation et de commercialisation), articles 3 à 5 et 13 à 16, annexes 1 et 3, version consolidée (dernière modification lue : arrêté ministériel du 11 mai 2026), Wallex, consultée le 27 novembre 2026. https://wallex.wallonie.be/eli/arrete/2023/02/23/2023042748
[^hra]: Arrêté du Gouvernement wallon du 30 août 2018 fixant les conditions d'octroi des subventions relatives aux halls relais agricoles et déterminant les modalités de leur mise à disposition, articles 1 à 4, version en vigueur depuis le 9 novembre 2023, Wallex, consultée le 26 novembre 2026. https://wallex.wallonie.be/contents/acts/3/3926.html
[^vm2019]: « Vade-mecum de la valorisation des produits agricoles et de leur commercialisation en circuit court », édition 2019, DiversiFerm (Gembloux Agro-Bio Tech - ULiège, Accueil Champêtre en Wallonie) pour le SPW. https://culturalite.be/wp-content/uploads/2021/10/vade-mecum-diversiferm-2019.pdf
[^dh-wapi]: « Une salle de découpe partagée par les éleveurs et pour les éleveurs de Wapi », La DH, 5 mars 2022. https://www.dhnet.be/regions/tournai-ath-mouscron/une-salle-de-decoupe-partagee-par-les-eleveurs-et-pour-les-eleveurs-de-wapi-6223161d9978e25398e9af82
[^dh-perwez]: Geerts S. (avec Belga), « La première coopérative agricole de Wallonie à se doter d'un hall de découpe à Perwez », La DH, 12 juin 2019. https://www.dhnet.be/regions/brabant/la-premiere-cooperative-agricole-de-wallonie-a-se-doter-d-un-hall-de-decoupe-a-perwez-5d010c169978e2779637433d
[^reussir-presses]: Griffoul B., « Produire carburant et tourteaux. Les presses à huile gagnent du terrain », Réussir Bovins viande (France), 13 juin 2005 (légende d'après une étude en Loire-Atlantique). https://www.reussir.fr/bovins-viande/les-presses-huile-gagnent-du-terrain
[^tn-prodel]: Mahey N., « Romain Prodel reprend la main sur la commercialisation de son colza et de son tournesol », Terre-net (France), 22 mai 2026. https://www.terre-net.fr/diversification-agricole/article/898662/romain-prodel-reprend-la-main-sur-la-commercialisation-de-son-colza-et-de-son-to
[^corioule]: Toussaint G., « Le fermier meunier de Corioule », La Libre Belgique, 13 février 2023. https://www.lalibre.be/planete/2023/02/13/le-fermier-meunier-de-corioule-EYPCH4C3KZBPBP36EREKCMXJU4/
[^guide-moulins]: « Base de données moulins belges pour Bruxelles », Service Good Food B2B (Bruxelles), 2026 (fichier du 4 juin 2026), fiche « Les Cocottes en Ribote » (Bousval). https://goodfood.brussels/sites/default/files/inline-files/Guide%20Moulins%20-%20Gids%20Molens_4.pdf
[^rtbf-terra]: Dagonnier E., Adam C., « Le groupe Terre se lance dans l'alimentation durable et ouvre une légumerie bio à Liège », RTBF, 18 juin 2024. https://www.rtbf.be/article/le-groupe-terre-se-lance-dans-l-alimentation-durable-et-ouvre-une-legumerie-bio-a-liege-11391134
[^dh-liege]: Neirynck L., « 1 400 tonnes de légumes découpés par an dans le premier hub wallon dédié à l'alimentation locale à Liège », La DH, 12 novembre 2025. https://www.dhnet.be/regions/liege/2025/11/12/1-400-tonnes-de-legumes-decoupes-par-an-dans-le-premier-hub-wallon-dedie-a-lalimentation-locale-a-liege-5UQ37MLXKVDC7CNV3GHOUVJKKU/
[^lavenir]: Serret P., « De quoi manger malgré les crises : 45 millions pour relocaliser le contenu de nos assiettes », L'Avenir, 14 avril 2023. https://www.lavenir.net/actu/belgique/2023/04/14/de-quoi-manger-malgre-les-crises-45-millions-pour-relocaliser-le-contenu-de-nos-assiettes-N65SIEITZVDMBHFRS2CJXV7D6A/
