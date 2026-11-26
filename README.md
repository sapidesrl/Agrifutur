# L'agriculture après le pétrole

Base de connaissances prospective. Pour chaque technologie agricole qui dépend aujourd'hui du pétrole ou du gaz : comment elle fonctionne, où entre le fossile, et quelles alternatives sont déjà rentables, rentables sous conditions, ou encore à préparer.

Contexte : Belgique (Wallonie), prix de novembre 2026. Objectif : un système le plus circulaire possible, sans sacrifier la rentabilité.

## Démarrer

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python calc/couts.py               # recalcule data/calculs.yaml depuis data/hypotheses.yaml
python outils/verifier_fiches.py   # contrôle gabarit, clés de prix, chiffres sans source
mkdocs serve                       # site local sur http://127.0.0.1:8000
```

Avec Claude Code : lance `claude` à la racine du repo. Les règles de rédaction sont dans `CLAUDE.md`.

## Structure

```
.
├── CLAUDE.md                  règles pour Claude Code
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

## État

- 2 fiches en brouillon : `traction/tracteur-diesel`, `fertilisation/azote-synthese`.
- 17 fiches à rédiger (voir `data/technologies.csv`).
