---
id: azote-synthese
titre: Engrais azoté de synthèse
domaine: fertilisation
dependance_fossile: gaz naturel
alternatives: [légumineuses, effluents et digestat, ammoniac vert local]
vague_meilleure_alternative: 1
statut: relu
maj: 2026-11-27
---

# Engrais azoté de synthèse

## En bref

L'ammonitrate, l'urée et la solution azotée sont fabriqués à partir de gaz naturel. Environ la moitié de la population mondiale (3,8 milliards de personnes) est nourrie grâce à eux[^carnegie]. Au prix français de fin novembre 2026 ({{ v('ammonitrate_prix') }} franco), l'azote de l'ammonitrate coûte {{ v('prix_kg_n') }} ({{ fourchette('prix_kg_n') }} selon les scénarios de prix).

Les alternatives rentables existent déjà : les légumineuses, qui fixent l'azote de l'air, et une meilleure valorisation des effluents (vague 1). L'ammoniac « vert » fabriqué localement avec de l'électricité renouvelable reste à préparer (vague 3).

## Comment ça marche aujourd'hui

Le procédé Haber-Bosch combine l'azote de l'air avec de l'hydrogène pour former de l'ammoniac, à haute pression et haute température. L'hydrogène est tiré du gaz naturel, qui fournit aussi la chaleur du procédé. L'ammoniac est ensuite transformé en nitrate d'ammonium (ammonitrate), en urée ou en solution azotée.

Le gaz reste le premier facteur de coût de ces engrais[^comparateur]. Quand le prix du gaz en Europe du Nord-Ouest a dépassé 60 €/MWh le 9 mars 2026, le coût de production de l'ammoniac a été estimé autour de 740 $/t[^spglobal]. La guerre en Iran, commencée fin février 2026, a entraîné toute la gamme azotée à la hausse ; l'ammonitrate 33,5 % s'échangeait autour de 550 €/t en avril[^reussir-avril].

S'y ajoute depuis le 1er janvier 2026 le mécanisme d'ajustement carbone aux frontières de l'Union (MACF), qui taxe les engrais importés ; le surcoût était estimé entre 120 et 150 €/t par les organisations syndicales agricoles fin 2025, et les producteurs européens d'ammonitrate, déjà soumis aux quotas carbone, ont aussi relevé leurs prix[^reussir-macf].

## Où entrent le pétrole et le gaz

- **Matière première** : l'hydrogène de l'ammoniac vient du gaz naturel.
- **Énergie du procédé** : chaleur et compression, au gaz.
- **Transport** : par bateau, camion ou train depuis les usines, souvent hors d'Europe pour l'urée.
- **Épandage** : passages de tracteur au gasoil.

## Les alternatives

### 1. Légumineuses (vague 1)

Les légumineuses (trèfle, luzerne, féverole, pois, lupin) vivent en symbiose avec des bactéries qui fixent l'azote de l'air dans leurs racines. Dans une prairie, le trèfle nourrit aussi la graminée voisine ; dans une rotation, la culture qui suit profite de l'azote laissé par la légumineuse.

Ordre de grandeur (calculé) : si les légumineuses fixent {{ v('azote_fixe_legumineuses') }}, elles évitent l'achat de {{ v('valeur_n_fixe') }} d'ammonitrate, et encore {{ v('valeur_n_fixe', scenario='bas') }} au prix d'avant-crise de l'ammonitrate ({{ v('ammonitrate_prix', scenario='bas') }} en février 2026, prix français, scénario bas). L'avantage des légumineuses ne dépend donc pas de la crise.

La centaine d'unités est l'ordre de grandeur d'une fixation active selon une synthèse de la revue *Fourrages* (estimé)[^vertes]. Les écarts sont grands : environ 50 à 130 kg N/ha/an pour le pois et la féverole, 150 à 200 pour un trèfle blanc bien implanté dans une prairie d'association, 300 à 500 pour une luzerne ou un trèfle violet très productifs[^vertes]. Pour les protéagineux récoltés en grain, la plus grande part de cet azote part avec la récolte : ce qui reste pour la culture suivante est bien plus faible que l'azote fixé (voir « À vérifier »).

Deux essais sur prairie pâturée :

- en Belgique (CRA-W, Libramont), sur une prairie permanente pâturée par de jeunes bovins viandeux, la fixation symbiotique par le trèfle blanc représentait 41 % des apports d'azote utile sur six années d'essai (1995-2000)[^stilmant] ;
- dans un essai de l'Université de Liège mené six années de suite (1993-1998) en région liégeoise, sur une prairie permanente pâturée en rotation par des vaches laitières, réduire d'un tiers la fertilisation azotée (de 136 à 91 kg N/ha/an), à chargement égal, n'a pas modifié la production de lait par vache[^dieguez].

Conditions : une part suffisante de légumineuses, une rotation adaptée et un débouché pour les protéagineux. Bonus : un fourrage plus riche en protéines réduit les achats de soja importé.

**Aides.** Plusieurs aides de la PAC s'ajoutent à l'azote évité (voir [les aides publiques](../../aides.md#pac-1er-pilier-eco-regimes-et-aides-couplees)) :

- **légumineuses fourragères** (luzerne, lupuline, sainfoin, lotier, vesce) sur terre arable : éco-régime « cultures favorables » V1_A, {{ v('er_cfe_v1a_eur_ha', 0) }} prévus, sans aucun insecticide (même en enrobage) et avec 10 % de zone refuge[^cfe]. C'est plus que l'azote fixé dans l'ordre de grandeur ci-dessus ({{ v('valeur_n_fixe', 0) }}). Le trèfle n'est pas dans la liste[^cfe] ;
- **protéagineux** (pois, féverole, lupin, soja) récoltés après le 15 juin : soutien couplé aux protéines végétales, {{ v('soutien_proteines_eur_ha', 0) }} prévus, non cumulable avec les cultures favorables sur la même parcelle[^couple-prot] [^cumuls]. Le détail et le choix entre les deux voies sont dans la fiche [Concentrés et soja importés](../elevage/concentres-importes.md) ;
- **couverts d'interculture** (avec ou sans légumineuses) : éco-régime « couverture longue du sol », si le sol est couvert du 1er janvier au 15 février sur 70, 80 ou 90 % de la surface de la ferme. Il paie {{ v('er_cls_entree_eur_ha', 0) }}, {{ v('er_cls_intermediaire_eur_ha', 0) }} ou {{ v('er_cls_superieur_eur_ha', 0) }} prévus **sur toute la SAU**, selon le seuil atteint[^cls]. La destruction chimique du couvert y sera interdite à partir de 2027[^cls].

Ce sont des montants prévus d'engagements d'un an : le montant payé est fixé après la campagne (220 à 420 €/ha pour la V1_A)[^cfe]. L'aide renforce une alternative déjà rentable sans elle : la vague 1 est confirmée.

### 2. Effluents et digestat (vague 1)

Le fumier, le lisier, le compost et le digestat de méthanisation contiennent de l'azote, du phosphore et du potassium. Bien stockés et épandus au bon moment, ils remplacent une partie des engrais achetés. Dans l'essai belge sur prairie pâturée cité plus haut, la fertilisation organique (compost) apportait deux fois plus d'azote utile que la fertilisation minérale (62,4 contre 31,8 kg N/ha)[^stilmant].

Conditions : analyses d'effluents, capacité de stockage pour épandre au bon moment, respect des plafonds d'épandage, et échanges paille-fumier avec les céréaliers voisins pour les fermes sans élevage.

**Aides.** Aucune aide ne paie directement l'épandage d'effluents. La MAEC « Sol » (MR14) paie le résultat qu'ils contribuent à obtenir : un sol plus riche en carbone organique. Elle verse jusqu'à {{ v('maec_mr14_favorable_eur_ha', 0) }} quand le sol est en état « favorable » (rapport carbone organique sur argile mesuré par un laboratoire au début et à la fin du contrat de cinq ans), jusqu'à 80 €/ha en état « transition », rien en état « défavorable »[^mr14]. Il faut engager au moins 90 % de sa surface ; le montant est réduit, voire nul, quand les terres arables font moins de 60 % de la surface (nul sous 30 %)[^mr14]. La prime de fin de contrat exige d'avoir activé l'éco-régime couverture longue les cinq ans[^mr14]. Le montant dépend donc de l'état du sol, pas des pratiques : on ne peut pas le compter d'avance. La vague 1 tient sans aide.

### 3. Ammoniac vert produit localement (vague 3)

On peut faire de l'ammoniac sans gaz : l'hydrogène vient alors de l'électrolyse de l'eau, avec de l'électricité renouvelable. Au Kenya, une petite unité solaire construite par la jeune entreprise Talus Renewables sur une ferme de noix près de Nairobi devait produire une tonne d'ammoniac par jour, sur place (annonce de 2023)[^yale]. Une étude publiée dans *Nature Food* en 2024 estime qu'une production décentralisée à petite échelle pourrait fournir la majorité de l'azote de synthèse d'ici la fin de la décennie[^carnegie].

Limites : forte consommation d'électricité et rendement moindre à petite échelle[^rsc], toxicité de l'ammoniac pour le stockage et le transport[^wef]. L'échelle pertinente est probablement le territoire (coopérative, zone d'activité) plutôt que la ferme.

## Ce qui ferme la boucle

- L'azote de l'air est fixé sur la ferme par les légumineuses.
- Les animaux le recyclent : ce qu'ils mangent revient au champ sous forme d'effluents.
- La méthanisation produit de l'énergie et rend un digestat épandable.
- L'azote qui manque encore peut être fabriqué localement avec l'électricité du territoire.

## À vérifier

- Prix de l'ammonitrate en Belgique : le prix utilisé ici est un prix français (franco, novembre 2026). Un négociant en ligne affichait fin novembre 2026 l'ammonitrate 27 (CAN) autour de 445 €/t départ Gand (page non datée, consultée le 26/11/2026)[^agryco] ; à confirmer par une source belge indépendante ou une facture, puis reporter dans `data/hypotheses.yaml`.
- Prix de l'ammonitrate en février 2026 : le scénario bas reprend une cotation française d'environ 500 €/t franco fin février 2026[^reussir-fevrier]. Le prix actuel est pris sur la même base (franco) ; un prix belge de février, sur facture, reste à trouver.
- Pages non lues (accès bloqué) : World Economic Forum (toxicité de l'ammoniac), S&P Global (prix du gaz et coût de l'ammoniac en mars 2026) et l'article de *Green Chemistry* (consommation d'électricité et rendement à petite échelle).
- Suspension éventuelle du MACF sur les engrais : la presse évoquait en mars 2026 une possible suspension rétroactive ; vérifier ce qui s'applique réellement en 2026 et 2027, et son effet sur les prix belges.
- Quantité d'azote réellement fixée sur l'exploitation, selon la part de trèfle ou de luzerne.
- Arrière-effet azoté des légumineuses pour la culture suivante (une fiche Protect'eau, Fourrages Mieux et UCLouvain de 2018 donne 10 à 60 kg N/ha pour le trèfle blanc et le pois, 60 à 100 pour la luzerne) : fiche citée par la note de l'hypothèse, à relire et à référencer ici.
- Contraintes du Programme de gestion durable de l'azote (PGDA) en Wallonie pour l'épandage des effluents.
- Montants **payés** en 2025 et 2026 des éco-régimes cultures favorables et couverture longue : seuls les montants prévus et ceux de 2024 sont publiés.
- Couverts de légumineuses détruits par roulage ou broyage avant le 15 février : compatibilité avec un semis de printemps sans glyphosate, à partir de 2027.
- MAEC Sol : montant réellement atteint selon l'état de départ des sols wallons (état « transition » ou « favorable »).
- Mise en service effective et production réelle de l'unité d'ammoniac vert au Kenya (la source de 2023 annonce la capacité prévue).

## Sources

[^vertes]: Vertès F., Jeuffroy M.-H., Louarn G., Voisin A.-S., Justes E., « Légumineuses et prairies temporaires : des fournitures d'azote pour les rotations », *Fourrages* n° 223, AFPF, 2015, lue le 27 novembre 2026. https://afpf-asso.fr/index.php?download=2149&token=c16b0ba6e27c1efb0d74a94026afe433
[^cfe]: « Eco-régime cultures favorables à l'environnement », Portail de l'agriculture wallonne, page modifiée le 17 avril 2026, consultée le 27 novembre 2026. https://agriculture.wallonie.be/home/aides/pac-2023-2027-description-des-interventions/eco-regimes/eco-regime-culture-favorable-a-l-environnement.html
[^couple-prot]: « Soutien couplé aux cultures de protéines végétales », Portail de l'agriculture wallonne, page modifiée le 21 novembre 2025, consultée le 27 novembre 2026. https://agriculture.wallonie.be/home/aides/pac-2023-2027-description-des-interventions/soutien-couple/soutien-couple-aux-cultures-de-proteines-vegetales.html
[^cumuls]: « Cumuls entre les aides », Portail de l'agriculture wallonne, page modifiée le 18 septembre 2025, consultée le 27 novembre 2026. https://agriculture.wallonie.be/home/aides/pac-2023-2027-description-des-interventions/cumuls-entre-les-aides.html
[^cls]: « Eco-régime couverture longue du sol », Portail de l'agriculture wallonne, page modifiée le 17 avril 2026, consultée le 27 novembre 2026. https://agriculture.wallonie.be/home/aides/pac-2023-2027-description-des-interventions/eco-regimes/eco-regime-couverture-longue-du-sol.html
[^mr14]: « MAEC Sol – MR14 », Portail de l'agriculture wallonne, page modifiée le 4 juin 2026, consultée le 27 novembre 2026. https://agriculture.wallonie.be/home/aides/pac-2023-2027-description-des-interventions/mesures-agro-environnementales-et-climatiques/maec-sol---mr14.html
[^wef]: « From fuel to fertilizer, how green ammonia could help curb emissions », World Economic Forum, 2023 (année tirée de l'adresse d'origine, page non lue). https://www.weforum.org/stories/nature-and-biodiversity/green-ammonia-climate-change-energy-transition/
[^comparateur]: « Analyse du marché des engrais – Avril 2026 », Comparateur agricole, 5 mai 2026. https://res.cloudinary.com/comparateuragricole/image/upload/v1777989677/strapi/Analyse_engrais_MAI_2026_a7cff53f79.pdf
[^spglobal]: « European nitrogen market rallies on gas price hike, Iran conflicts », S&P Global, 9 mars 2026 (page non lue). https://www.spglobal.com/energy/en/news-research/latest-news/agriculture/030926-european-nitrogen-market-rallies-on-gas-price-hike-iran-conflicts
[^reussir-avril]: V. Charpenet, « Prix des engrais : les achats des agriculteurs sous tension pour la prochaine campagne », Réussir Grandes cultures, 1er juin 2026. https://www.reussir.fr/grandes-cultures/prix-des-engrais-les-achats-des-agriculteurs-sous-tension-pour-la-prochaine-campagne
[^reussir-macf]: M. Descamps, « Marché des engrais : sous tension avec l'application de la taxe MACF au 1er janvier 2026 », La Dépêche (Réussir), 8 décembre 2025. https://www.reussir.fr/ladepeche/marche-des-engrais-sous-tension-avec-flambee-des-prix-en-produits-azotes
[^stilmant]: D. Stilmant, V. Decruyenaere, C. Belge, C. Clément, P. Limbourg (CRA-W, Libramont), « Bilan azoté au sein d'une prairie permanente pâturée par des jeunes bovins de type viande : synthèse de 6 années de suivi », Rencontres Recherches Ruminants, 11, 2004. https://journees3r.fr/wp-content/uploads/2006/02/2004_paturage_01_Stilmant-1f6.pdf
[^dieguez]: F. Diéguez, J.-L. Hornick, V. De Behr, L. Istasse, I. Dufrasne (Université de Liège), « Incidences phytotechniques et zootechniques d'une réduction ou d'une suppression de la fertilisation azotée sur des prairies pâturées par des vaches laitières », Animal Research, 50, 299-314, 2001. https://orbi.uliege.be/bitstream/2268/148127/1/dieguez%5b1%5d.pdf
[^reussir-fevrier]: D. Jouen, « Marché des engrais : la tension accrue au Moyen-Orient soutient les engrais azotés », La Dépêche (Réussir), 9 mars 2026. https://www.reussir.fr/articles/marche-des-engrais-la-tension-accrue-au-moyen-orient-soutient-les-engrais-azotes
[^agryco]: « Les tendances des marchés » (page engrais), Agryco Belgique, non datée, consultée le 26 novembre 2026. https://www.agryco.be/fr_BE/engrais/pc975
[^yale]: « Farm in Kenya First to Produce Fossil-Free Fertilizer On Site », Yale Environment 360, 11 octobre 2023. https://e360.yale.edu/digest/small-green-ammonia-plant-farm-kenya
[^carnegie]: « Green fertilizers could revolutionize agriculture and increase food security », Carnegie Science, 16 mai 2024 (étude de L. Rosa et D. Tonelli, *Nature Food*). https://carnegiescience.edu/green-fertilizers-could-revolutionize-agriculture-and-increase-food-security
[^rsc]: L. Rosa et D. Tonelli, « Optimal design of decentralized ammonia production via electric Haber–Bosch systems », Green Chemistry, 28, 2026 (page non lue, références tirées du moteur de recherche). https://pubs.rsc.org/en/content/articlehtml/2026/gc/d5gc06782k
