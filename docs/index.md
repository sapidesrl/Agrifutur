# L'agriculture après le pétrole

Ce site passe en revue les technologies agricoles qui dépendent aujourd'hui du pétrole ou du gaz. Pour chacune : comment elle fonctionne, où entre le fossile, et quelles alternatives existent, avec leur rentabilité actuelle.

Le contexte est celui de la Belgique, surtout de la Wallonie, avec les prix de novembre 2026. Le but est un système le plus circulaire possible, sans sacrifier la rentabilité.

## Le constat de départ

Au prix actuel, un kWh de travail utile coûte {{ v('gasoil_kwh_utile') }} au gasoil, contre {{ v('pv_kwh_utile') }} avec l'électricité de ses propres panneaux : {{ v('ratio_gasoil_pv', 1) }} plus cher. L'électricité du réseau, elle, ne fait pas mieux que le gasoil : au prix d'une PME wallonne (CREG), le kWh utile coûte {{ v('reseau_kwh_utile') }}, plus cher que le gasoil. On électrifie donc derrière son propre photovoltaïque, et ce qui freine, c'est le prix d'achat du matériel plus que l'énergie.

Cet écart tient même si les prix redescendent : au prix d'avant-crise, le kWh utile au gasoil coûte encore {{ v('ratio_gasoil_pv', 1, scenario='bas') }} celui du photovoltaïque. Selon le scénario, le rapport va de {{ fourchette('ratio_gasoil_pv', 1) }} (voir [les trois scénarios](methode.md#trois-scenarios-de-prix)).

## Les trois vagues

| Vague | Signification |
|---|---|
| 1 | Rentable aujourd'hui dans le bon contexte |
| 2 | Rentable sous conditions précises : taille, usage, aides, organisation collective |
| 3 | Pas encore rentable, à préparer |

## Par où commencer

- [Les fiches](fiches/index.md), une par technologie actuelle.
- [La méthode](methode.md) : comment lire les chiffres.
- [Les hypothèses](hypotheses.md) : tous les prix utilisés, avec leur source et leur date.
- [Les calculs](calculs.md) : les comparaisons, recalculées à chaque mise à jour des prix.
