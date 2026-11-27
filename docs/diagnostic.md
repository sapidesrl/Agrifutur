# Diagnostic de sa ferme

Cet outil estime ce que les postes liés au pétrole et au gaz coûtent à votre exploitation, et quels changements décrits dans les fiches pourraient s'y appliquer, avec leur économie et leur temps de retour.

!!! note "Vos données restent sur votre ordinateur"
    Le calcul se fait dans votre navigateur : rien n'est envoyé. Les réponses sont gardées dans ce navigateur pour la prochaine visite ; le bouton « Tout effacer » les supprime. Le profil peut être téléchargé, puis rechargé ici ou passé au script `outils/diagnostic.py` du projet pour obtenir un rapport détaillé.

**Comment l'utiliser.** Renseignez les surfaces, les animaux et les équipements. Les consommations (gasoil, électricité, engrais…) sont alors estimées à partir de références moyennes wallonnes ; remplacez-les par les chiffres de vos factures quand vous les avez, le diagnostic sera plus juste. Les prix sont ceux de novembre 2026 ; « avant la crise » donne le même calcul au prix de février 2026.

**Ce que l'outil ne fait pas.** Il ne remplace ni un audit ni un devis. Il chiffre l'énergie, les engrais, le soja, quelques économies de produits phytosanitaires et le pâturage ; les plastiques, la transformation et la vente sont traités dans leurs fiches. Les estimations valent pour une ferme moyenne de la même structure.

<div id="diagnostic" class="diag">Chargement du diagnostic…</div>

## D'où viennent les chiffres

- Les références moyennes (gasoil par hectare, électricité par litre de lait, engrais par hectare…) et tous les prix sont listés, avec leur source, dans [les hypothèses](hypotheses.md).
- Les engrais minéraux sont estimés avec la moyenne wallonne mesurée par hectare de surface agricole, prairies comprises : aucune moyenne mesurée par culture n'est publiée. L'estimation peut donc s'écarter nettement de la réalité d'une ferme donnée, dans un sens ou dans l'autre, selon ses cultures. Les quantités des factures corrigent ce biais.
- Le gasoil est estimé par culture de vente (références françaises et néerlandaises, faute de référence belge par culture) et, pour l'élevage, par vache pour toute l'exploitation, fourrages compris (référence flamande pour les laitières, française pour les allaitantes). Les références néerlandaises de la betterave et du maïs grain sont probablement hautes pour la Wallonie.
- L'électricité est estimée pour le lait, les vaches allaitantes et le stockage ventilé des pommes de terre. Il n'existe pas de référence pour le reste d'une ferme de grandes cultures (stockage et ventilation des céréales, ateliers) : saisir alors la consommation de la facture.
- Les règles du diagnostic (estimations, conditions et calcul de chaque changement) sont dans le fichier `data/diagnostic.yaml` du projet, lisible et modifiable.
- Le classement par vague et les conditions de chaque changement viennent des fiches, reprises sur [la page de synthèse](synthese.md).
