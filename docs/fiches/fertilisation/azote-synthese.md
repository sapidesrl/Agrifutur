---
id: azote-synthese
titre: Engrais azoté de synthèse
domaine: fertilisation
dependance_fossile: gaz naturel
alternatives: [légumineuses, effluents et digestat, ammoniac vert local]
vague_meilleure_alternative: 1
statut: brouillon
maj: 2026-11-26
---

# Engrais azoté de synthèse

## En bref

L'ammonitrate, l'urée et la solution azotée sont fabriqués à partir de gaz naturel. On estime qu'environ la moitié de l'humanité est nourrie grâce à eux[^wef]. Au prix d'avril 2026 en France, l'azote de l'ammonitrate coûte {{ v('prix_kg_n') }} ({{ fourchette('prix_kg_n') }} selon les scénarios de prix).

Les alternatives rentables existent déjà : les légumineuses, qui fixent l'azote de l'air, et une meilleure valorisation des effluents (vague 1). L'ammoniac « vert » fabriqué localement avec de l'électricité renouvelable reste à préparer (vague 3).

## Comment ça marche aujourd'hui

Le procédé Haber-Bosch combine l'azote de l'air avec de l'hydrogène pour former de l'ammoniac, à haute pression et haute température. L'hydrogène est tiré du gaz naturel, qui fournit aussi la chaleur du procédé. L'ammoniac est ensuite transformé en nitrate d'ammonium (ammonitrate), en urée ou en solution azotée.

Le gaz reste le premier facteur de coût de ces engrais[^comparateur]. Quand le prix du gaz en Europe du Nord-Ouest a dépassé 60 €/MWh le 9 mars 2026, le coût de production de l'ammoniac a été estimé autour de 740 $/t[^spglobal]. La guerre en Iran, commencée fin février 2026, a entraîné toute la gamme azotée à la hausse ; l'ammonitrate 33,5 % s'échangeait autour de 550 €/t en avril[^reussir-avril].

S'y ajoute depuis le 1er janvier 2026 le mécanisme d'ajustement carbone aux frontières de l'Union (MACF), qui taxe les engrais importés ; le surcoût pourrait atteindre 150 €/t selon le négoce, et les producteurs européens, soumis aux quotas carbone, ont aussi relevé leurs prix[^reussir-macf].

## Où entrent le pétrole et le gaz

- **Matière première** : l'hydrogène de l'ammoniac vient du gaz naturel.
- **Énergie du procédé** : chaleur et compression, au gaz.
- **Transport** : par bateau, camion ou train depuis les usines, souvent hors d'Europe pour l'urée.
- **Épandage** : passages de tracteur au gasoil.

## Les alternatives

### 1. Légumineuses (vague 1)

Les légumineuses (trèfle, luzerne, féverole, pois, lupin) vivent en symbiose avec des bactéries qui fixent l'azote de l'air dans leurs racines. Dans une prairie, le trèfle nourrit aussi la graminée voisine ; dans une rotation, la culture qui suit profite de l'azote laissé par la légumineuse.

Ordre de grandeur (calculé) : si les légumineuses fixent {{ v('azote_fixe_legumineuses') }} (hypothèse, très variable selon leur part dans la prairie ou la rotation), elles évitent l'achat de {{ v('valeur_n_fixe') }} d'ammonitrate, et encore {{ v('valeur_n_fixe', scenario='bas') }} si le prix de l'engrais redescend de 30 % (scénario bas, hypothèse). L'avantage des légumineuses ne dépend donc pas de la crise.

Deux essais sur prairie pâturée :

- en Belgique, sur une prairie permanente pâturée par de jeunes bovins, la fixation symbiotique représentait 41 % des apports d'azote sur six années d'essai[^stilmant] ;
- dans un essai publié par l'Université de Liège, sur une prairie pâturée en rotation, réduire d'un tiers la fumure azotée minérale n'a pas modifié la production de lait par vache[^dieguez].

Conditions : une part suffisante de légumineuses, une rotation adaptée et un débouché pour les protéagineux. Bonus : un fourrage plus riche en protéines réduit les achats de soja importé.

### 2. Effluents et digestat (vague 1)

Le fumier, le lisier, le compost et le digestat de méthanisation contiennent de l'azote, du phosphore et du potassium. Bien stockés et épandus au bon moment, ils remplacent une partie des engrais achetés. Dans l'essai belge sur prairie pâturée cité plus haut, la fertilisation organique apportait deux fois plus d'azote que la fertilisation minérale (62,4 contre 31,8 kg N/ha)[^stilmant].

Conditions : analyses d'effluents, capacité de stockage pour épandre au bon moment, respect des plafonds d'épandage, et échanges paille-fumier avec les céréaliers voisins pour les fermes sans élevage.

### 3. Ammoniac vert produit localement (vague 3)

On peut faire de l'ammoniac sans gaz : l'hydrogène vient alors de l'électrolyse de l'eau, avec de l'électricité renouvelable. Au Kenya, une petite unité solaire installée sur une ferme de noix produit de l'ammoniac sur place (capacité à vérifier, environ une tonne par jour)[^yale]. Une étude publiée dans *Nature Food* estime qu'une production décentralisée à petite échelle pourrait fournir la majorité de l'azote de synthèse d'ici la fin de la décennie[^carnegie].

Limites : forte consommation d'électricité et rendement moindre à petite échelle[^rsc], toxicité de l'ammoniac pour le stockage et le transport[^wef]. L'échelle pertinente est probablement le territoire (coopérative, zone d'activité) plutôt que la ferme.

## Ce qui ferme la boucle

- L'azote de l'air est fixé sur la ferme par les légumineuses.
- Les animaux le recyclent : ce qu'ils mangent revient au champ sous forme d'effluents.
- La méthanisation produit de l'énergie et rend un digestat épandable.
- L'azote qui manque encore peut être fabriqué localement avec l'électricité du territoire.

## À vérifier

- Prix de l'ammonitrate en Belgique sur facture (ici, prix français d'avril 2026). Les cotations françaises de novembre 2026 sont un peu plus hautes qu'en avril (relevés consultés par extraits seulement, voir `data/sources-collectees.md`).
- Prix de l'ammonitrate en février 2026, pour remplacer le scénario bas à −30 %.
- Durée de l'essai Diéguez et al. (« six ans » à confirmer pour les deux essais).
- Plusieurs sources ne sont pas datées (World Economic Forum, Réussir, Université de Liège, Yale e360, Carnegie Science) : ajouter les dates.
- Quantité d'azote réellement fixée sur l'exploitation, selon la part de trèfle ou de luzerne.
- Contraintes du Programme de gestion durable de l'azote (PGDA) en Wallonie pour l'épandage des effluents.
- Effet réel du MACF sur les prix belges en 2026 et 2027.
- Aides de la PAC pour les cultures protéagineuses en Wallonie.

## Sources

[^wef]: « From fuel to fertilizer, how green ammonia could help curb emissions », World Economic Forum. https://www.weforum.org/stories/nature-and-biodiversity/green-ammonia-climate-change-energy-transition/
[^comparateur]: « Analyse engrais mai 2026 », Comparateur agricole. https://res.cloudinary.com/comparateuragricole/image/upload/v1777989677/strapi/Analyse_engrais_MAI_2026_a7cff53f79.pdf
[^spglobal]: « European nitrogen market rallies on gas price hike, Iran conflicts », S&P Global, mars 2026. https://www.spglobal.com/energy/en/news-research/latest-news/agriculture/030926-european-nitrogen-market-rallies-on-gas-price-hike-iran-conflicts
[^reussir-avril]: « Prix des engrais : les achats des agriculteurs sous tension pour la prochaine campagne », Réussir, 2026. https://www.reussir.fr/grandes-cultures/prix-des-engrais-les-achats-des-agriculteurs-sous-tension-pour-la-prochaine-campagne
[^reussir-macf]: « Marché des engrais : sous tension avec l'application de la taxe MACF au 1er janvier 2026 », Réussir. https://www.reussir.fr/ladepeche/marche-des-engrais-sous-tension-avec-flambee-des-prix-en-produits-azotes
[^stilmant]: Stilmant et al., bilan azoté d'une prairie permanente pâturée par de jeunes bovins (synthèse de six années d'essai), Rencontres Recherches Ruminants, 2004. https://journees3r.fr/wp-content/uploads/2006/02/2004_paturage_01_Stilmant-1f6.pdf
[^dieguez]: Diéguez et al., essai de fertilisation azotée sur prairie pâturée, Université de Liège. https://orbi.uliege.be/bitstream/2268/148127/1/dieguez%5b1%5d.pdf
[^yale]: « Farm in Kenya First to Produce Fossil-Free Fertilizer On Site », Yale Environment 360. https://e360.yale.edu/digest/small-green-ammonia-plant-farm-kenya
[^carnegie]: « Green fertilizers could revolutionize agriculture and increase food security », Carnegie Science. https://carnegiescience.edu/green-fertilizers-could-revolutionize-agriculture-and-increase-food-security
[^rsc]: « Optimal design of decentralized ammonia production via electric Haber–Bosch systems », Green Chemistry, 2026. https://pubs.rsc.org/en/content/articlehtml/2026/gc/d5gc06782k
