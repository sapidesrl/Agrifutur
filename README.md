# L'agriculture après le pétrole

Base de connaissances prospective. Pour chaque technologie agricole qui dépend aujourd'hui du pétrole ou du gaz : comment elle fonctionne, où entre le fossile, et quelles alternatives sont déjà rentables, rentables sous conditions, ou encore à préparer.

Contexte : Belgique (Wallonie), prix de novembre 2026. Objectif : un système le plus circulaire possible, sans sacrifier la rentabilité.

## Démarrer

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python calc/couts.py               # recalcule data/calculs.yaml (scénarios actuel, bas, haut)
python outils/verifier_fiches.py   # contrôle gabarit, clés de prix, chiffres sans source
zensical serve                     # site local sur http://127.0.0.1:8000
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
│   ├── synthese.yaml          lignes de la page « Par où commencer sur sa ferme »
│   ├── diagnostic.yaml        modèle du diagnostic d'exploitation (questions, estimations, changements)
│   └── sources-collectees.md  sources déjà trouvées pour les fiches à rédiger
├── calc/couts.py              calculs de comparaison
├── outils/
│   ├── macros.py              macros du site : {{ v('cle') }} insère une valeur
│   ├── diagnostic.py          rapport de diagnostic d'une ferme (Markdown)
│   ├── moteur_diagnostic.py   calcul du diagnostic (même moteur que la page web)
│   ├── exporter_diagnostic.py écrit docs/assets/diagnostic/donnees.json
│   ├── tester_diagnostic.py   compare les moteurs Python et JavaScript
│   ├── nouvelle_fiche.py      crée une fiche à partir du gabarit
│   └── verifier_fiches.py     contrôles avant commit
├── exemples/                  profils de fermes fictives pour le diagnostic
├── templates/fiche.md         gabarit d'une fiche
└── docs/                      le site (Zensical, thème Material classique)
    ├── index.md, synthese.md, diagnostic.md, methode.md, hypotheses.md, calculs.md, aides.md
    ├── javascripts/, stylesheets/, assets/diagnostic/   page du diagnostic
    └── fiches/<domaine>/<id>.md
```

## Mettre à jour les prix

```bash
pip install -r outils/requirements-maj.txt          # une fois (lecture des PDF de la CREG)
python outils/maj_prix.py --mois 2026-11            # affiche les écarts, ne modifie rien
python outils/maj_prix.py --mois 2026-11 --ecrire   # écrit dans data/hypotheses.yaml
python calc/couts.py && python outils/verifier_fiches.py && zensical build --clean --strict
```

Le script relit les prix maximums officiels du SPF Économie publiés par Statbel (gasoil de chauffage et agricole, diesel B7 et XTL, propane), les cotations du blé de la FEGRA et le prix PME wallon du tableau de bord de la CREG. Chaque prix est la moyenne du mois demandé ; la borne d'avant-crise (février 2026) est recalculée de la même façon. Après une mise à jour, relire les phrases des fiches qui comparent deux prix proches, et changer de mois de référence demande de relire les fiches, qui parlent des « prix de novembre 2026 ».

## Diagnostic d'une exploitation

La page « Diagnostic de sa ferme » du site estime les dépenses liées au pétrole et au gaz d'une ferme à partir de sa structure (surfaces, animaux, équipements), puis liste les changements chiffrés qui la concernent, par vague. Les consommations estimées se remplacent par celles des factures. Le calcul se fait dans le navigateur : rien n'est envoyé.

Le même calcul existe en script, pour un conseiller qui veut un rapport :

```bash
python outils/diagnostic.py exemples/ferme-laitiere.yaml                 # rapport à l'écran
python outils/diagnostic.py profil-ferme.json --sortie rapport.md        # profil téléchargé depuis la page
```

Les profils de vraies exploitations ne vont pas dans le dépôt : les garder ailleurs ou dans `profils/` (ignoré par git). Le modèle est dans `data/diagnostic.yaml` ; les moyennes qui servent à estimer (clés `ref_*`) sont sourcées dans `data/hypotheses.yaml`. Après une modification, `python calc/couts.py` régénère les données de la page et `python outils/tester_diagnostic.py` vérifie que la page et le script donnent les mêmes résultats.

## Ajouter ou rédiger une fiche

1. Ajouter une ligne dans `data/technologies.csv`.
2. `python outils/nouvelle_fiche.py <id>` crée la fiche vide au bon endroit. L'ajouter au menu (`nav` dans `mkdocs.yml`), dans son domaine.
3. Rédiger en suivant `CLAUDE.md`. Tout nouveau prix va d'abord dans `data/hypotheses.yaml`.
4. `python calc/couts.py && python outils/verifier_fiches.py && zensical build --clean --strict`

## Licence

Contenu (fiches, données) sous [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/deed.fr), code sous licence MIT. Détails dans `LICENSE.md`.

## Intégration continue

À chaque push et pull request, `.github/workflows/verifier.yml` lance le recalcul, le vérificateur et `zensical build --clean --strict`. Il signale aussi quand `data/calculs.yaml` ou les données du diagnostic n'ont pas été régénérés, et compare les moteurs Python et JavaScript du diagnostic.

## Site publié

À chaque push sur `main`, `.github/workflows/publier.yml` construit le site et le publie sur https://sapidesrl.github.io/Agrifutur/. Réglage à faire une seule fois dans GitHub : *Settings → Pages → Build and deployment → Source : GitHub Actions*.

## Chantiers

- **Prix belges des sites protégés** : lus le 27/11/2026 depuis le navigateur (Claude in Chrome) pour le Sillon belge (paille, tourteaux de soja et de colza) et Statbel (indice des prix des engrais). Restent : Pleinchamp.be (site injoignable), l'historique des tourteaux du Sillon belge (réservé aux abonnés), un prix belge de l'ammonitrate.
- **Mise à jour mensuelle des prix publics** : `outils/maj_prix.py` (voir « Mettre à jour les prix ») relit Statbel, la FEGRA et la CREG. Restent à la main : paille et tourteaux (Sillon belge, via le navigateur), engrais (Agryco, Statbel), plaquettes (Valbiom). Peut devenir une tâche planifiée.
- **Prix locaux sur devis ou facture** (semence certifiée, triage à façon, paillages, huile fermière, tarifs d'entrepreneurs) : à noter sous la forme « relevé chez un négoce wallon, mois année », sans nom d'exploitation.
- Remplacer les prix français (ammonitrate, gasoil labour / semis direct, gasoil par culture) par des sources belges. Recherche du 27/11/2026 sans résultat par culture ni prix belge de novembre (Agryco et Sillon belge fermés aux outils automatiques) ; repères belges ajoutés dans les notes. Pistes : factures, Agryco via le navigateur, van Stappen et al. 2018 (inventaire des céréales wallonnes, accès payant).

## État

- Les 19 fiches sont relues (statut « relu », 26/11/2026) : cohérence entre le texte et les chiffres recalculés, règles de `CLAUDE.md`, sources datées. Les données manquantes sont listées dans la section « À vérifier » de chaque fiche.
- Plusieurs prix restent français, faute de source belge publique (ammonitrate 33,5 %, colza, tourteaux, pois, semence certifiée, triage, paillages, huile alimentaire). Les remplacer par des prix belges sur facture est la priorité.
