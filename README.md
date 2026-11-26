# L'agriculture après le pétrole

Base de connaissances prospective. Pour chaque technologie agricole qui dépend aujourd'hui du pétrole ou du gaz : comment elle fonctionne, où entre le fossile, et quelles alternatives sont déjà rentables, rentables sous conditions, ou encore à préparer.

Contexte : Belgique (Wallonie), prix de novembre 2026. Objectif : un système le plus circulaire possible, sans sacrifier la rentabilité.

## Démarrer

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python calc/couts.py               # recalcule data/calculs.yaml (scénarios actuel, bas, haut)
python outils/verifier_fiches.py   # contrôle gabarit, clés de prix, chiffres sans source
mkdocs serve                       # site local sur http://127.0.0.1:8000
```

Avec Claude Code : lance `claude` à la racine du repo. Les règles de rédaction sont dans `CLAUDE.md`.

## Structure

```
.
├── CLAUDE.md                  règles pour Claude Code
├── LICENSE.md                 CC BY 4.0 (contenu) et MIT (code)
├── .github/workflows/        contrôles automatiques
├── data/
│   ├── hypotheses.yaml        tous les prix et paramètres, avec source et date
│   ├── calculs.yaml           généré par calc/couts.py (ne pas éditer à la main)
│   ├── technologies.csv       index des technologies actuelles
│   └── sources-collectees.md  sources déjà trouvées pour les fiches à rédiger
├── calc/couts.py              calculs de comparaison
├── outils/
│   ├── macros.py              macros MkDocs : {{ v('cle') }} insère une valeur
│   ├── nouvelle_fiche.py      crée une fiche à partir du gabarit
│   └── verifier_fiches.py     contrôles avant commit
├── templates/fiche.md         gabarit d'une fiche
└── docs/                      le site (MkDocs Material)
    ├── index.md, methode.md, hypotheses.md, calculs.md
    └── fiches/<domaine>/<id>.md
```

## Ajouter ou rédiger une fiche

1. Ajouter une ligne dans `data/technologies.csv`.
2. `python outils/nouvelle_fiche.py <id>` crée la fiche vide au bon endroit.
3. Rédiger en suivant `CLAUDE.md`. Tout nouveau prix va d'abord dans `data/hypotheses.yaml`.
4. `python calc/couts.py && python outils/verifier_fiches.py && mkdocs build --strict`

## Licence

Contenu (fiches, données) sous [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/deed.fr), code sous licence MIT. Détails dans `LICENSE.md`.

## Intégration continue

À chaque push et pull request, `.github/workflows/verifier.yml` lance le recalcul, le vérificateur et `mkdocs build --strict`. Il signale aussi quand `data/calculs.yaml` n'a pas été régénéré.

## Site publié

À chaque push sur `main`, `.github/workflows/publier.yml` construit le site et le publie sur https://sapidesrl.github.io/Agrifutur/. Réglage à faire une seule fois dans GitHub : *Settings → Pages → Build and deployment → Source : GitHub Actions*.

## Chantiers

- Migrer de MkDocs 1.6 vers [Zensical](https://zensical.org/docs/compatibility/mkdocs/migration/), le successeur maintenu par l'équipe de Material for MkDocs. D'ici là, `requirements.txt` plafonne MkDocs sous la version 2.
- Remplacer les prix français (ammonitrate, gasoil labour / semis direct) par des sources belges.

## État

- Les 19 fiches sont relues (statut « relu », 26/11/2026) : cohérence entre le texte et les chiffres recalculés, règles de `CLAUDE.md`, sources datées. Les données manquantes sont listées dans la section « À vérifier » de chaque fiche.
- Plusieurs prix restent français, faute de source belge publique (ammonitrate 33,5 %, colza, tourteaux, pois, semence certifiée, triage, paillages, huile alimentaire). Les remplacer par des prix belges sur facture est la priorité.
