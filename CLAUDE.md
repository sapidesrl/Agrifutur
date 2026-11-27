# CLAUDE.md — L'agriculture après le pétrole

## Le projet

Une fiche par technologie agricole utilisée aujourd'hui qui dépend du pétrole ou du gaz. Chaque fiche explique comment la technologie fonctionne, où entre le fossile, puis détaille ses alternatives et leur rentabilité actuelle.

- Contexte : Belgique, surtout Wallonie. Prix de référence : novembre 2026.
- But : un système le plus circulaire possible, en gardant la rentabilité.
- Public : publication ouverte. Lecteur visé : agriculteur ou conseiller agricole. Texte concret, chiffré, sans jargon inutile. Aucune donnée d'une exploitation particulière dans le repo.
- Licence : contenu sous CC BY 4.0, code sous MIT (voir `LICENSE.md`).

## Règles de rédaction

1. **Français**, registre neutre (« on », impersonnel). Phrases courtes.
2. **Chaque chiffre a un statut visible :**
   - *sourcé* : note de bas de page `[^cle]` vers une source datée dans la section « Sources » ;
   - *hypothèse* : marqué « (hypothèse) » dans le texte ;
   - *calculé* : inséré par macro depuis `data/calculs.yaml`.
3. **Aucun prix ni coût en dur pour les grandeurs qui bougent** (carburant, électricité, engrais, matières premières) : ils viennent de `data/hypotheses.yaml` ou `data/calculs.yaml` via `{{ v('cle') }}`. Exception : un chiffre tiré d'une source précise (prix d'une machine dans un essai, résultat d'étude) reste écrit en dur, avec sa note de bas de page.
4. **Ne jamais inventer une source.** Si un chiffre ne se trouve pas, il va dans « À vérifier ».
5. **Paraphraser** les sources. Pas de citation longue.
6. **Gabarit obligatoire** : `templates/fiche.md`. Les sections suivantes doivent toutes être présentes, dans cet ordre :
   `## En bref`, `## Comment ça marche aujourd'hui`, `## Où entrent le pétrole et le gaz`, `## Les alternatives`, `## Ce qui ferme la boucle`, `## À vérifier`, `## Sources`.
7. **Une fiche = une technologie actuelle.** Les alternatives sont des sous-sections `### n. Nom (vague X)`, de la plus mature à la moins mature.
8. **Vagues** :
   - 1 = rentable aujourd'hui dans le bon contexte ;
   - 2 = rentable sous conditions précises (taille, usage, aides, collectif) ;
   - 3 = pas encore rentable, à préparer.
9. **Honnêteté sur les limites** : signaler quand une alternative déplace une dépendance au lieu de la supprimer (ex. semis direct et glyphosate).
10. La vague d'une fiche « à rédiger » est provisoire. À la rédaction, la confirmer ou la corriger, dans `data/technologies.csv` **et** dans le frontmatter.
11. Mettre à jour la colonne `statut` de `data/technologies.csv` : `à rédiger` → `brouillon` → `relu`.

## Prix et calculs

- `data/hypotheses.yaml` : chaque entrée a `libelle`, `valeur`, `unite`, `statut` (sourcé, estimé, hypothèse, à saisir), `date`, `source`, `note`.
- `unite: "%"` signifie que `valeur` est une fraction (0.35 s'affiche 35 %).
- Un nouveau calcul s'ajoute dans `calc/couts.py` (liste `CALCULS`), jamais à la main dans `data/calculs.yaml`.
- Macro dans les fiches : `{{ v('cle') }}` (valeur + unité), `{{ v('cle', 1) }}` (1 décimale), `{{ v('cle', unite=False) }}`.
- **Trois scénarios de prix** : actuel, bas, haut. Une hypothèse qui bouge porte `scenario: true` ; sa borne basse est le prix d'avant-crise (février 2026) si on le connaît (champ `bas` + `bas_note`), sinon valeur × `scenario_bas_facteur`. Même logique pour `haut`. `calc/couts.py` écrit `bas` et `haut` dans `data/calculs.yaml` pour chaque calcul qui en dépend.
- Macros de scénario : `{{ v('cle', scenario='bas') }}`, `{{ fourchette('cle') }}` (« X à Y unité »). Quand une conclusion de rentabilité change entre scénarios, la fiche le dit (ex. l'huile de colza n'est moins chère que le gasoil qu'au prix de crise).

## Après chaque modification

```bash
python calc/couts.py
python outils/verifier_fiches.py
zensical build --clean --strict
```

Le vérificateur échoue si une macro appelle une clé inconnue, si une section manque ou si une fiche de l'index n'existe pas. Il avertit quand une ligne contient un montant en euros sans note de bas de page ni macro.

## Rédiger une fiche : la marche à suivre

1. Lire la ligne de la technologie dans `data/technologies.csv`, puis la section correspondante de `data/sources-collectees.md` (sources déjà trouvées, à revérifier).
2. Chercher des sources récentes : **belges ou wallonnes d'abord** (SPF Économie, SPW, CRA-W, Valbiom, Fugea, FWA, presse agricole belge). Une source française ou européenne reste possible en repli, mais la note de l'hypothèse ou le texte le signale (« prix français ») ; on la remplace dès qu'une source belge existe. Organismes publics, instituts techniques et presse agricole avant les blogs commerciaux.
3. Ajouter les nouveaux prix dans `data/hypotheses.yaml`, avec source et date.
4. Si un calcul est utile, l'ajouter dans `calc/couts.py`.
5. Rédiger la fiche, puis lancer les trois commandes ci-dessus.
6. Passer le statut à `brouillon` dans le CSV.
7. Si une alternative de vague 1 ou 2 est ajoutée, renommée ou change de vague, mettre à jour `data/synthese.yaml` (page « Par où commencer sur sa ferme ») : le vérificateur échoue si une ligne ne retrouve plus son alternative ou une clé.

Les deux fiches `traction/tracteur-diesel.md` et `fertilisation/azote-synthese.md` servent d'exemples de niveau de détail attendu.
