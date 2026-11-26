# Méthode

## Une fiche par technologie actuelle

Chaque fiche part d'une technologie utilisée aujourd'hui (tracteur diesel, engrais azoté de synthèse…) et suit le même plan : en bref, fonctionnement, place du pétrole et du gaz, alternatives classées de la plus mature à la moins mature, ce qui ferme la boucle, points à vérifier, sources.

## Trois sortes de chiffres

- **Sourcés** : suivis d'une note de bas de page qui renvoie à une source datée.
- **Hypothèses** : marqués « (hypothèse) ». Ils sont listés dans [les hypothèses](hypotheses.md) et chacun peut les remplacer par ses propres valeurs.
- **Calculés** : obtenus à partir des prix et hypothèses, et recalculés à chaque mise à jour. Le détail est dans [les calculs](calculs.md).

Les prix qui bougent (carburant, électricité, engrais, matières premières) ne sont jamais écrits en dur dans les fiches : ils viennent tous d'un seul fichier, `data/hypotheses.yaml`.

## Les vagues

| Vague | Signification |
|---|---|
| 1 | Rentable aujourd'hui dans le bon contexte |
| 2 | Rentable sous conditions précises : taille, usage, aides, organisation collective |
| 3 | Pas encore rentable, à préparer |

## Limites

- Les prix sont ceux de novembre 2026, dans un contexte de crise pétrolière et gazière : ils peuvent baisser comme monter.
- Les calculs comparent des coûts d'énergie et d'intrants. Ils ne remplacent pas un calcul d'investissement complet pour une exploitation donnée.
- Une alternative peut déplacer une dépendance au lieu de la supprimer. Les fiches le signalent.
