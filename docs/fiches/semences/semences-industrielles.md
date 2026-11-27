---
id: semences-industrielles
titre: Semences hybrides achetées chaque année
domaine: semences
dependance_fossile: transport; intrants de production
alternatives: [Semences de ferme, semences paysannes reproductibles, sélection à la ferme]
vague_meilleure_alternative: 1
statut: relu
maj: 2026-11-27
---

# Semences hybrides achetées chaque année

## En bref

La plupart des cultures sont semées chaque année avec des semences achetées : semences certifiées de céréales, hybrides de maïs, de betterave, de chicorée et de beaucoup de légumes, plants de pommes de terre. En Wallonie, les semences coûtaient 199 €/ha de surface agricole en 2024 dans les exploitations de grandes cultures, autant que les engrais[^eaw-gc]. Le fossile entre surtout par la culture qui produit la semence (engrais, phytos, gasoil), puis par le séchage, le tri, l'enrobage, l'emballage et le transport ; pour une céréale, cela reste peu d'énergie par hectare, et c'est l'argent et l'autonomie qui sont en jeu, plus que le pétrole. La meilleure alternative, la semence de ferme de céréales et de protéagineux, est rentable aujourd'hui (vague 1) : en froment, elle économise environ {{ v('semence_ferme_froment_economie_ha', 0) }} ({{ fourchette('semence_ferme_froment_economie_ha', 0) }} selon le prix du grain, calculé avec des prix de semence et de triage français). Pour les hybrides (maïs, betterave), il n'existe pas d'alternative rentable à court terme.

## Comment ça marche aujourd'hui

Trois sortes de semences coexistent.

- **Variétés lignées** (froment, orge, épeautre, pois, féverole) : la plante se reproduit à l'identique. On peut ressemer sa récolte, mais la plupart des variétés sont protégées par un certificat d'obtention végétale. On achète de la semence certifiée, ou on ressème sa propre récolte en payant une rémunération à l'obtenteur (voir plus bas).
- **Hybrides F1** (maïs, betterave, chicorée, beaucoup de légumes, certains escourgeons) : on croise deux lignées choisies pour obtenir des plantes très homogènes. La descendance n'est pas stérile mais elle est hétérogène et ne reproduit pas les qualités de la F1 : il faut racheter chaque année[^cra-potager]. Le règlement européen exclut d'ailleurs les variétés hybrides et synthétiques de la dérogation qui autorise la semence de ferme[^r2100].
- **Plants de pommes de terre** : on peut produire ses plants fermiers, sous conditions sanitaires strictes[^fiwap].

Le poids des semences dans les charges, en Wallonie, en 2024 (charges opérationnelles hors travaux par tiers, comptabilités suivies par le SPW) :

| Culture | Semences ou plants | Remarque |
|---|---|---|
| Exploitation spécialisée en grandes cultures | 199 €/ha de surface agricole[^eaw-gc] | autant que les engrais (199 €/ha), un peu moins que les phytos (211 €/ha) |
| Colza | 80 €/ha, 14 % des charges[^eaw-colza] | |
| Betterave sucrière | 370 €/ha (335 €/ha en 2023)[^eaw-betterave] | semence hybride |
| Chicorée industrielle | 536 €/ha, environ 51 % des charges[^eaw-chicoree] | premier poste ; semence souvent fournie par l'usine, mais comptée |
| Pomme de terre de conservation | 1 581 €/ha, 50 % des charges[^eaw-pdt] | contre environ 835 €/ha en moyenne sur les dix années précédentes |

Pour le froment, le SPW ne détaille pas le poste semences : sur 597 €/ha de charges opérationnelles en 2024, les engrais font 225 €/ha et les phytos 266 €/ha[^eaw-froment]. Avec une dose de {{ v('semence_froment_dose') }} (fourchette conseillée de 100 à 170 kg/ha en octobre[^lb2016]), le poste reste modeste : {{ v('semence_certifiee_froment_eur_ha', 0) }} en semence certifiée (calculé, avec un prix français de 2021, faute de prix belge).

Pour le maïs, on sème 85 000 à 95 000 grains/ha selon les conseils d'un semencier pour la Belgique[^kws] : environ deux doses de 50 000 grains par hectare. Le prix belge d'une dose n'a pas été trouvé (voir « À vérifier »).

Le Livre Blanc Céréales rappelle qu'une dose de semis trop forte coûte sans rien rapporter : au-delà de 250 grains/m² pour un froment semé fin octobre, le rendement n'augmentait pas dans un essai 2015-2016, et réduire la dose réduit aussi les produits de traitement des semences par hectare[^lb2016].

## Où entrent le pétrole et le gaz

- **Culture de multiplication** : la parcelle qui produit la semence reçoit engrais azotés (gaz naturel), phytos et passages de tracteur, comme une culture de grain, avec en plus un rendement souvent moindre et des contrôles au champ.
- **Séchage, triage, conditionnement** : séchage au gaz ou au fioul quand la récolte est humide (surtout le maïs), électricité des trieurs et des stations de semences.
- **Traitement de semences** : fongicides et insecticides de synthèse, issus de la chimie du pétrole et du gaz.
- **Emballage** : sacs et big-bags en plastique.
- **Transport** : les semences hybrides de maïs, de betterave et de légumes sont produites dans quelques bassins spécialisés, souvent loin de la Belgique, puis acheminées par camion.

Ordre de grandeur pour une céréale : un kg de semence de blé, d'avoine ou de triticale représente 3 à 4 MJ d'énergie fossile selon les références françaises GESTIM, contre 15,9 MJ pour un kg d'ammonitrate[^gestim]. Pour un hectare de froment, cela fait {{ v('semence_froment_energie_kwh_ha', 0) }}, soit l'énergie d'environ {{ v('semence_froment_eq_gasoil_l_ha', 0) }} de gasoil (calculé). C'est peu à côté des engrais. Pour les hybrides, le coefficient n'a pas été trouvé ; il est probablement plus élevé (production plus intensive, séchage du maïs), mais cela reste à vérifier.

La dépendance aux semences achetées est donc d'abord **économique et stratégique** : prix fixé par quelques entreprises, souvent liées aux groupes qui vendent aussi engrais et phytos[^cra-potager], et variétés sélectionnées pour des systèmes à fort usage d'intrants.

## Les alternatives

### 1. Semences de ferme de céréales et de protéagineux (vague 1)

**Principe.** On garde une partie de sa récolte de variétés lignées, on la fait trier (et éventuellement traiter) par un trieur à façon agréé, puis on la ressème sur sa propre exploitation. C'est le « privilège de l'agriculteur », légal et encadré[^spw-regles].

**Règles en Belgique.**

- Le règlement européen sur la protection des obtentions végétales (n° 2100/94, article 14) autorise l'agriculteur à ressemer, sur sa propre exploitation, la récolte d'une variété protégée, sauf hybride ou synthétique, et seulement pour une liste d'espèces : céréales (blé, blé dur, épeautre, orge, avoine, seigle, triticale), pomme de terre, colza, navette, lin oléagineux et plusieurs fourragères (pois fourrager, féverole, luzerne, vesce, lupin jaune, trèfles d'Alexandrie et de Perse)[^r2100]. Le maïs et la betterave n'en font pas partie.
- L'agriculteur doit une **rémunération équitable** à l'obtenteur, « sensiblement inférieure » à la redevance comprise dans la semence certifiée. Les **petits agriculteurs** en sont dispensés : ceux qui ne cultivent pas plus que la surface nécessaire pour produire 92 t de céréales[^r2100].
- En Belgique, pour 2025-2026, la rémunération est de {{ v('royalties_semence_ferme_cereales', unite=False) }} €/kg (4,80 €/100 kg) pour le froment, l'orge, le seigle et l'avoine, 8,01 €/100 kg pour le triticale et 9,60 €/100 kg pour l'épeautre[^assobio]. Depuis 2016, les trieurs à façon la facturent pour le compte de Seed@bel[^spw-taf].
- Une variété libre de droits se ressème sans redevance[^spw-taf].
- En Wallonie, le triage à façon ne peut être fait que par un trieur agréé par le SPW (installation fixe ou mobile, agrément renouvelé chaque année). Chaque lot suit un document unique ; le trieur prélève trois échantillons ; l'agriculteur garde la facture de la semence certifiée d'origine pour prouver la parenté du lot[^spw-regles].
- **Interdit** : vendre, donner ou échanger la semence de ferme, même à un voisin ; mélanger ou subdiviser des lots ; racheter la récolte d'un autre agriculteur pour la revendre comme semence[^spw-taf][^spw-regles].
- **Pommes de terre** : les plants fermiers sont possibles, mais demandent une déclaration de production à l'AFSCA, des analyses (pourritures brune et annulaire, nématodes) et, au-delà de 4 ha, une déclaration d'utilisation des variétés protégées sur le site des plants de ferme (accord entre Breeders Trust et l'Agrofront)[^fiwap].

**Maturité.** La pratique est courante. En 2024, les trieurs à façon wallons ont trié {{ v('tri_froment_wallonie_kg', 0, unite=False) }} kg de froment, sur un total de 8,4 millions de kg toutes espèces[^spw-tri]. À {{ v('semence_froment_dose') }}, cela suffit pour semer environ {{ v('froment_semence_ferme_part_surface', 0) }} de la surface wallonne de froment (calculé, ordre de grandeur qui ne compte ni le grain trié par l'agriculteur lui-même ni les écarts de dose).

**Coût, froment conventionnel** (calculé, avec des prix français faute de prix belges) :

- semence certifiée traitée : {{ v('semence_froment_certifiee_prix') }} (milieu de 55 à 70 €/100 kg en Hauts-de-France en 2021[^staff-2021]), soit {{ v('semence_certifiee_froment_eur_ha', 0) }} ;
- semence de ferme : grain gardé au prix du marché ({{ v('ble_prix', 0) }}, cotation belge[^fegra]), triage, traitement et ensachage à façon ({{ v('triage_traitement_facon_froment', 2) }}, prix français de 2019[^terrenet-2019]) et rémunération de l'obtenteur, soit {{ v('semence_ferme_froment_eur_kg') }} et {{ v('semence_ferme_froment_eur_ha', 0) }} ;
- **économie : {{ v('semence_ferme_froment_economie_ha', 0) }}**, soit {{ v('semence_ferme_froment_economie_part', 0) }} du coût de la semence certifiée ; {{ fourchette('semence_ferme_froment_economie_ha', 0) }} selon le prix du grain.

La semence de ferme reste moins chère dans les trois scénarios. L'écart se réduit quand le blé est cher, car le grain gardé vaut alors plus ; le calcul garde le prix de la semence certifiée fixe, alors qu'il suit en partie le prix du grain (hypothèse).

**Coût, en bio** (données belges du CRA-W, octobre 2025, pour une exploitation suivie) : la semence de froment fourrager du commerce coûte 1,20 €/kg, soit 180 €/ha à 150 kg/ha, contre 0,45 €/kg et 67,50 €/ha en semence de ferme triée par un trieur agréé, redevance comprise[^assobio]. Pour la féverole bio, l'écart est plus fort : 2,50 €/kg contre 0,61 €/kg, soit 562,50 €/ha contre 137,25 €/ha à 225 kg/ha dans une association féverole-avoine[^assobio].

**Conditions et limites.**

- Un trieur agréé à proximité, ou un trieur mobile qui vient à la ferme.
- Une capacité de stockage propre et sèche entre la moisson et le semis.
- Un grain sain : la semence de ferme peut transmettre les maladies portées par la graine, comme la carie. Une analyse de germination et un contrôle sanitaire avant le semis évitent les mauvaises surprises ; les doses conseillées supposent une semence de bonne qualité germinative[^lb2016].
- Repartir de semence certifiée de temps en temps, pour changer de variété ou rafraîchir le lot.
- **Ce n'est pas une sortie du fossile** : la culture qui produit la semence reste la même, et le traitement de semences reste souvent chimique. On supprime surtout la marge, l'emballage et une partie du transport de la filière semencière.

**Aides** (voir [les aides publiques](../../aides.md)). Ressemer son grain n'est pas aidé en soi, et le calcul ci-dessus n'en compte aucune. Deux aides touchent pourtant la semence de ferme :

- **mélanges céréales-légumineuses** (comme l'association féverole-avoine ci-dessus) : l'éco-régime « cultures favorables à l'environnement », variante V3, paie {{ v('er_cfe_v3a_eur_ha', 0) }} prévus si la récolte a lieu après le 31 mai, {{ v('er_cfe_v3b_eur_ha', 0) }} après le 15 juin. Il faut au moins 50 % de céréales et 20 % de légumineuses, et **aucun insecticide, même en enrobage** : la semence de ferme ne doit donc recevoir aucun traitement insecticide[^cfe]. Le montant payé est fixé après la campagne et peut être plus bas que le montant prévu[^cfe]. Cette aide ne se cumule ni avec le soutien couplé aux protéagineux, ni avec l'éco-régime réduction d'intrants sur la même parcelle[^cumuls] ; le choix entre les deux voies est chiffré dans la fiche [concentrés et soja importés](../elevage/concentres-importes.md) ;
- **triage en CUMA** : la liste de l'AII contient un « trieur à grains mobile pour cultures associées », réservé aux CUMA, avec la case « architecture verte » ; une CUMA de six membres ou plus reçoit {{ v('aii_taux_cuma_av', 0) }} de son coût simplifié (calculé)[^am-aii]. Un agriculteur seul n'y a pas accès.

Ces aides rendent les mélanges plus intéressants ; elles ne changent pas la vague 1 de la semence de ferme, déjà rentable sans aide.

### 2. Semences paysannes reproductibles (vague 2)

**Principe.** On cultive des **variétés populations** : des plantes qui se reproduisent entre elles et restent reproductibles, au lieu d'hybrides F1. Une population garde une diversité génétique qui lui permet de s'adapter, génération après génération, au sol, au climat et aux pratiques de la ferme[^cra-potager]. Pour les céréales, on parle de **populations issues de croisements multiples** (en anglais *composite cross populations*) : on croise de nombreuses variétés, puis on laisse la population évoluer.

**En Belgique.**

- Le CRA-W a créé trois variétés-populations : un froment « participatif » issu de croisements entre 11 blés anciens choisis par sélection participative, pour la boulangerie artisanale, et deux épeautres (8 variétés locales anciennes d'un côté, 8 variétés modernes de l'autre). Elles sont suivies à Gembloux, en Gaume et en Flandre[^ccp].
- En 2015-2016, une population de froment d'hiver a été cultivée à côté d'une variété lignée dans quatre fermes bio belges et néerlandaises. Les auteurs notent que les variétés lignées disponibles conviennent mal à la diversité des fermes bio, avec des rendements et une qualité meunière souvent décevants ; la population se différencie davantage quand les plantes sont semées moins dense[^baltazar].
- En légumes, la coopérative Cycle en Terre (Havelange) produit des semences bio de variétés reproductibles, en partie multipliées par des maraîchers wallons[^rtbf-cet]. La maison wallonne Semailles ne vend que des variétés populations libres de droits[^cra-maraichers]. Le projet Semences d'Ici (Les Marequiers, Biowallonie, Hortiforum, CRA-W, UCLouvain) soutient la production de semences et la sélection potagère en Wallonie[^cra-potager].
- En France, le Réseau Semences Paysannes anime des groupes sur les céréales à paille, les potagères, le maïs, l'arboriculture et les fourragères[^rsp] ; c'est la référence la plus proche pour les échanges de pratiques.

**Cadre légal.**

- Depuis janvier 2022, le règlement bio européen (2018/848) permet de commercialiser du **matériel hétérogène biologique** : une population très diverse, qui n'est ni une variété au sens du catalogue ni un mélange de variétés, produite en bio. Il faut la notifier à l'autorité compétente ; les règles de production et de commercialisation sont fixées par le règlement délégué 2021/1189. L'Allemagne a confirmé ses premières notifications en février 2022[^bsa]. Aucune notification belge n'a été trouvée.
- Le futur **règlement européen sur le matériel de reproduction des végétaux** a fait l'objet d'un accord provisoire entre le Conseil et le Parlement le 15 juin 2026. Il doit encore être adopté formellement et s'appliquera quatre ans après son entrée en vigueur. Il annonce des règles plus légères pour les variétés de conservation, les variétés adaptées localement et le matériel destiné au bio[^conseil-prm]. Selon Inf'OGM, les réseaux et banques de semences pourront vendre et échanger du matériel non enregistré sans but lucratif, mais les échanges entre agriculteurs restent limités en zone et en quantité, voire interdits pour certaines espèces comme la pomme de terre[^infogm-juin]. Le texte final reste à lire.

**Rentabilité.** Elle dépend du débouché plus que du coût de la semence.

- **Rentable sous conditions** (vague 2) : en bio, en circuit court, pour une boulangerie paysanne ou un maraîchage diversifié qui valorise le goût et la diversité. Les maraîchers wallons interrogés par le CRA-W privilégient les populations par conviction, mais plusieurs doivent garder des hybrides F1 pour tenir les exigences d'homogénéité du marché ; ils évoquent des rendements et une tenue en culture parfois limités, faute de sélection[^cra-maraichers].
- **Pas rentable aujourd'hui** en circuit long standardisé, où l'homogénéité est payée.

**Aides.** Aucune aide ne paie le choix d'une variété population. Ces variétés sont surtout rentables en bio (voir ci-dessus), où compte l'aide au maintien en agriculture biologique : {{ v('bio_autres_cultures_eur_ha', 0) }} en grandes cultures et {{ v('bio_maraichage_eur_ha', 0) }} sur les premiers hectares du groupe « arboriculture, maraîchage et semences », où figure aussi la multiplication de semences[^bio]. Elle se cumule avec l'éco-régime « cultures favorables » pour un mélange céréales-légumineuses[^cumuls]. Elle paie le système bio, pas la population : la vague 2 ne change pas.

### 3. Sélection à la ferme (vague 3)

**Principe.** L'agriculteur choisit lui-même, chaque année, les plantes ou les épis qui serviront de semence (sélection massale), dans ses parcelles et selon ses critères : vigueur, résistance aux maladies, tenue, qualité boulangère. Sur une population, la sélection naturelle et celle de l'agriculteur travaillent ensemble ; dans les essais du CRA-W, des agriculteurs volontaires éliminent au champ les plantes qui ne les intéressent pas[^ccp].

**Maturité.** Encore expérimentale en Wallonie : essais de recherche, peu d'agriculteurs, pas de sélection variétale améliorante spécifique à la Wallonie en légumes à ce jour[^cra-maraichers].

**Limites.**

- Travail et savoir-faire : il faut des années pour obtenir une population stable et performante.
- Pas de vente ni d'échange de semence de ferme hors des cadres prévus (matériel hétérogène biologique, futur règlement)[^spw-taf].
- **Hybrides sans alternative à court terme.** Pour le maïs, la betterave et la chicorée, les populations existent ou sont en sélection (le Réseau Semences Paysannes a un groupe maïs[^rsp]), mais on ne connaît pas de population capable de rivaliser avec les hybrides en rendement dans les filières wallonnes. Ces cultures restent dépendantes des semences achetées. La chicorée est en outre cultivée sous contrat avec une raffinerie, qui fournit souvent la semence[^eaw-chicoree].

## Ce qui ferme la boucle

- **La récolte devient la semence** : pour les céréales et les protéagineux, garder et trier son grain remplace l'achat chaque année.
- **Le trieur local** (fixe, mobile, en entreprise ou en CUMA) remplace la station de semences lointaine et l'emballage.
- **La dose juste** : semer en grains/m² et non en kg/ha, et réduire la dose quand les conditions sont bonnes, économise semence et traitement[^lb2016].
- **La diversité cultivée** : populations, mélanges de variétés et associations (céréale et légumineuse) gardent une capacité d'adaptation que les variétés homogènes n'ont pas[^ccp].
- **Les réseaux** : coopératives semencières wallonnes, maisons de semences et échanges encadrés entre fermes.

## À vérifier

- **Prix belge de la semence certifiée de froment** (conventionnel, traitée), campagne 2026-2027 : le calcul utilise un repère français de 2021.
- **Tarif d'un trieur à façon wallon** (triage, traitement, ensachage, en €/100 kg) : le calcul utilise un prix français de 2019 ; la liste des trieurs agréés 2025-2026 du SPW n'a pas pu être lue.
- **Seed@bel** : barème complet et application de la dispense des petits agriculteurs (92 t de céréales) en Belgique.
- **Plants fermiers de pommes de terre** : montant de la rémunération des obtenteurs (accord Breeders Trust - Agrofront).
- **Maïs** : prix belge d'une dose de 50 000 grains et coût par hectare.
- **Légumes** : coût des semences hybrides F1 et des variétés populations par hectare, en maraîchage wallon.
- **Énergie fossile des semences hybrides** (maïs, betterave), lieux de production et transport.
- **Matériel hétérogène biologique** : notifications en Belgique, autorité compétente.
- **Futur règlement sur le matériel de reproduction** : texte final sur les échanges entre agriculteurs et les variétés de conservation de céréales.
- **Rendement des populations de froment** comparé aux lignées dans les essais belges.
- « Biosemences » : acteur à identifier (activité, espèces, lien avec la Wallonie).
- Éco-régime « cultures favorables », variante V3 : base des seuils de 50 % de céréales et 20 % de légumineuses (grains, poids de semence ou surface) pour une association féverole-avoine semée en semence de ferme ; montant 2026 payé (seul le montant prévu est publié).
- Coût simplifié de l'AII pour le trieur mobile de cultures associées en CUMA (pas encore repris dans les données du projet).
- Prix départ ferme du froment en Wallonie : le calcul utilise la cotation indicative belge de la FEGRA, dont la base de livraison n'est pas précisée.

## Sources

[^eaw-gc]: « Produits et charges - grandes cultures », État de l'agriculture wallonne, SPW, données 2024, mise à jour 2025. https://etat-agriculture.wallonie.be/contents/indicatorsheets/EAW-C_III_a.html
[^eaw-froment]: « Froment d'hiver », État de l'agriculture wallonne, SPW, données 2024, mise à jour du 8 décembre 2025. https://etat-agriculture.wallonie.be/contents/indicatorsheets/EAW-C_III_b_2.html
[^eaw-colza]: « Colza », État de l'agriculture wallonne, SPW, données 2024, mise à jour du 8 décembre 2025. https://etat-agriculture.wallonie.be/contents/indicatorsheets/EAW-C_III_b_6.html
[^eaw-betterave]: « Betterave sucrière », État de l'agriculture wallonne, SPW, données 2023 et 2024 (provisoires), mise à jour du 8 décembre 2025. https://etat-agriculture.wallonie.be/contents/indicatorsheets/EAW-C_III_b_5.html
[^eaw-chicoree]: « Chicorée industrielle », État de l'agriculture wallonne, SPW, données 2024, mise à jour du 8 décembre 2025. https://etat-agriculture.wallonie.be/contents/indicatorsheets/EAW-C_III_b_7.html
[^eaw-pdt]: « Pommes de terre de conservation », État de l'agriculture wallonne, SPW, données 2024, mise à jour du 8 décembre 2025. https://etat-agriculture.wallonie.be/contents/indicatorsheets/EAW-C_III_b_8.html
[^lb2016]: « Implantation des cultures », Livre Blanc Céréales, Gembloux Agro-Bio Tech et CRA-W, septembre 2016. https://orbi.uliege.be/bitstream/2268/206243/1/1_Implantation_LB_09_16.pdf
[^kws]: Brochure maïs 2025, Belgique, KWS (semencier), 2025. https://www.kws.com/be/media/producten/kws_brochure_maize_fr_2025.pdf
[^r2100]: Règlement (CE) n° 2100/94 du Conseil du 27 juillet 1994 instituant un régime de protection communautaire des obtentions végétales, article 14, texte publié par l'Office communautaire des variétés végétales. https://cpvo.europa.eu/sites/default/files/documents/lex/394R2100/FR394R2100.pdf
[^spw-taf]: « Fiche d'information : semences fermières et triage à façon », SPW Agriculture, version du 15 avril 2026. https://agriculture.wallonie.be/files/accueil/Produits/Productions%20v%c3%a9g%c3%a9tales/FO_producteur_TAF%20VF_15-04-2026.docx
[^spw-regles]: « Triage à façon de semences fermières : rappel des règles », SPW (Direction de la qualité), projet d'article de presse du 23 juillet 2013. https://agriculture.wallonie.be/files/20182/21921/Triage%20a%20facon%20rappel%20des%20r%c3%a8gles.pdf
[^spw-tri]: « Évolution des quantités de graines triées en Wallonie (kg/an), 2020-2024 », SPW Agriculture, 2025. https://agriculture.wallonie.be/files/20182/42099/Evolution%20des%20quantit%c3%a9s%20de%20semences%20fermi%c3%a8res%20tri%c3%a9es%20en%20Wallonie.pdf
[^assobio]: « Bilan économique des cultures associées du projet PRW D65-1442 AssoBIO », annexe 7, CRA-W, données d'octobre 2025, publié en juillet 2026. https://www.cra.wallonie.be/uploads/2026/07/annexe7-assobio-couts-.pdf
[^staff-2021]: « Semences de ferme : les trieurs à façon du Staff intègrent Semae avec leurs conditions », Réussir Grandes cultures (France), 13 juillet 2021. https://www.reussir.fr/articles/semences-de-ferme-les-trieurs-facon-du-staff-integrent-semae-avec-leurs-conditions
[^terrenet-2019]: « Les atouts du triage à façon pour la semence de ferme », Terre-net (France), 20 juin 2019. https://www.terre-net.fr/semences/article/149099/les-trieurs-a-facon-defendent-leurs-atouts-pour-la-transition-agricole
[^gestim]: C. Colnenne-David et al., « Conception et évaluation de systèmes de culture innovants : résultats de performances énergétiques », INRAE, séminaire Sobriété énergétique en agriculture, 24 mai 2022 (coefficients GESTIM 2019). https://www.inrae.fr/sites/default/files/4_grandes_cultures-cc.pdf
[^fiwap]: « Gestion administrative des plants fermiers », Fiwap-Info n° 181, janvier-mars 2024. https://fiwap.be/wp-content/uploads/2024/03/2403GestionAdminPlantFermier.pdf
[^cra-potager]: J. Martens, « Pourquoi créer des variétés potagères adaptées à l'agriculture biologique et au contexte pédoclimatique de la Wallonie », CRA-W, projet Semences d'Ici, mai 2026. https://www.cra.wallonie.be/uploads/2026/08/pourquoi-creer-des-varietes-potageres-adaptees-a-l-agriculture-bilogique-pdf.pdf
[^cra-maraichers]: J. Martens, « Attentes et perceptions de maraîchers envers la qualité des variétés et la sélection variétale en Wallonie », CRA-W, projet Semences d'Ici, février 2026. https://www.cra.wallonie.be/uploads/2026/05/attentes-et-perceptions-de-maraichers-.pdf
[^rtbf-cet]: « Cycle en Terre : semer les graines de l'autonomie alimentaire », RTBF, 28 novembre 2022. https://www.rtbf.be/article/cycle-en-terre-semer-les-graines-de-lautonomie-alimentaire-11112936
[^ccp]: « Les variétés-populations en froment et épeautre (CCPs : Composite Cross Populations) », poster, CRA-W, 2023. https://www.cra.wallonie.be/uploads/2023/06/poster-ccp-cereale.pdf
[^baltazar]: S. Baltazar et al., « Questioning Seeding Rates and its Influence on Phenotypic Expression of Wheat Populations for Participatory Plant Breeding: First Findings from Field Research across Organic Farms in Belgium and the Netherlands », notice de la base documentaire du CRA-W (fiche ajoutée le 28 octobre 2020). https://fredo.cra.wallonie.be/publications/3SB4GTE8
[^bsa]: « Regulations on organic heterogeneous material », Bundessortenamt (office fédéral allemand des variétés), page consultée le 26 novembre 2026. https://www.bundessortenamt.de/bsa/en/seeds/organic-heterogeneous-material
[^conseil-prm]: « Regulation on the production and marketing of plant reproductive material: state of play », note de la présidence, Conseil de l'Union européenne, document 10718/26, 18 juin 2026. https://data.consilium.europa.eu/doc/document/ST-10718-2026-INIT/en/pdf
[^rsp]: Site du Réseau Semences Paysannes (France), page d'accueil consultée le 26 novembre 2026. https://www.semencespaysannes.org/
[^infogm-juin]: D. Meshaka, « Veille juridique Inf'OGM du 9 au 23 juin 2026 », Inf'OGM, 22 juin 2026. https://infogm.org/juridique/veille-juridique-infogm-du-9-au-23-juin-2026/
[^fegra]: Cotations indicatives des produits agricoles (blé standard certifié), FEGRA (fédération belge du négoce de grains), 26 novembre 2026 ; prix hors TVA, base non précisée, non contraignants. https://fegra.be/home/agriculturalprices?lang=fr
[^cfe]: « Eco-régime cultures favorables à l'environnement », Portail de l'agriculture wallonne, page modifiée le 17 avril 2026, consultée le 27 novembre 2026. https://agriculture.wallonie.be/home/aides/pac-2023-2027-description-des-interventions/eco-regimes/eco-regime-culture-favorable-a-l-environnement.html
[^cumuls]: « Cumuls entre les aides », Portail de l'agriculture wallonne, page modifiée le 18 septembre 2025 (tableau « culture »), consultée le 27 novembre 2026. https://agriculture.wallonie.be/home/aides/pac-2023-2027-description-des-interventions/cumuls-entre-les-aides.html
[^bio]: « Soutien à l'agriculture biologique », Portail de l'agriculture wallonne, page modifiée le 17 avril 2026, consultée le 27 novembre 2026. https://agriculture.wallonie.be/home/aides/pac-2023-2027-description-des-interventions/soutien-a-l-agriculture-biologique.html
[^am-aii]: Arrêté ministériel du 23 février 2023 exécutant l'arrêté du Gouvernement wallon du 23 février 2023 relatif aux aides à l'installation et aux investissements, version consolidée (modifications des 15 janvier et 11 mai 2026), article 5 et annexe 3 (ligne 457), Wallex, consulté le 27 novembre 2026. https://wallex.wallonie.be/eli/arrete/2023/02/23/2023042748
