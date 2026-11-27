"""Moteur du diagnostic d'exploitation (version Python).

Le diagnostic est décrit dans data/diagnostic.yaml : questions, consommations estimées,
postes de dépense fossile et recommandations. Les formules y sont écrites dans un petit
langage commun, interprété à l'identique ici et dans docs/javascripts/diagnostic-moteur.js :

  nombres (1.5), noms (sau_ha, gasoil_agricole_htva), + - * /, parenthèses,
  comparaisons < <= > >= == !=, et / ou / non, fonctions min(a, b, …), max(a, b, …),
  si(condition, valeur_si_vraie, valeur_si_fausse).
  Vrai vaut 1, faux vaut 0. Une division par zéro vaut 0.

Un nom désigne d'abord une réponse ou une consommation de la ferme, sinon une clé de
data/hypotheses.yaml ou de data/calculs.yaml (valeur du scénario de prix en cours).
"""
import re

SCENARIOS = ("actuel", "bas", "haut")
_JETON = re.compile(r"\s*(?:(\d+(?:\.\d+)?)|([a-z_][a-z0-9_]*)|(<=|>=|==|!=|[-+*/(),<>]))")
MOTS = {"et", "ou", "non"}


class ErreurFormule(ValueError):
    pass


def decouper(texte: str) -> list[tuple[str, str]]:
    jetons, pos = [], 0
    texte = texte.strip()
    while pos < len(texte):
        m = _JETON.match(texte, pos)
        if not m or m.end() == pos:
            raise ErreurFormule(f"caractère inattendu à la position {pos} : {texte[pos:pos + 10]!r}")
        nombre, nom, op = m.groups()
        if nombre is not None:
            jetons.append(("nombre", nombre))
        elif nom is not None:
            jetons.append(("mot" if nom in MOTS else "nom", nom))
        else:
            jetons.append(("op", op))
        pos = m.end()
        while pos < len(texte) and texte[pos].isspace():
            pos += 1
    return jetons


class _Analyseur:
    """Analyse descendante : produit un arbre de tuples."""

    def __init__(self, texte: str):
        self.jetons = decouper(texte)
        self.i = 0
        self.texte = texte

    def voir(self):
        return self.jetons[self.i] if self.i < len(self.jetons) else (None, None)

    def prendre(self, genre=None, valeur=None):
        g, v = self.voir()
        if (genre and g != genre) or (valeur and v != valeur):
            raise ErreurFormule(f"attendu {valeur or genre}, trouvé {v!r} dans « {self.texte} »")
        self.i += 1
        return v

    def analyser(self):
        arbre = self.ou()
        if self.i != len(self.jetons):
            raise ErreurFormule(f"fin inattendue « {self.voir()[1]} » dans « {self.texte} »")
        return arbre

    def ou(self):
        a = self.et()
        while self.voir() == ("mot", "ou"):
            self.i += 1
            a = ("ou", a, self.et())
        return a

    def et(self):
        a = self.non()
        while self.voir() == ("mot", "et"):
            self.i += 1
            a = ("et", a, self.non())
        return a

    def non(self):
        if self.voir() == ("mot", "non"):
            self.i += 1
            return ("non", self.non())
        return self.comparaison()

    def comparaison(self):
        a = self.somme()
        g, v = self.voir()
        if g == "op" and v in ("<", "<=", ">", ">=", "==", "!="):
            self.i += 1
            return (v, a, self.somme())
        return a

    def somme(self):
        a = self.produit()
        while self.voir()[0] == "op" and self.voir()[1] in "+-":
            op = self.prendre()
            a = (op, a, self.produit())
        return a

    def produit(self):
        a = self.unaire()
        while self.voir()[0] == "op" and self.voir()[1] in "*/":
            op = self.prendre()
            a = (op, a, self.unaire())
        return a

    def unaire(self):
        if self.voir() == ("op", "-"):
            self.i += 1
            return ("neg", self.unaire())
        return self.primaire()

    def primaire(self):
        g, v = self.voir()
        if g == "nombre":
            self.i += 1
            return ("num", float(v))
        if g == "nom":
            self.i += 1
            if self.voir() == ("op", "("):
                self.i += 1
                args = []
                if self.voir() != ("op", ")"):
                    args.append(self.ou())
                    while self.voir() == ("op", ","):
                        self.i += 1
                        args.append(self.ou())
                self.prendre("op", ")")
                if v not in ("min", "max", "si"):
                    raise ErreurFormule(f"fonction inconnue {v}() dans « {self.texte} »")
                if v == "si" and len(args) != 3:
                    raise ErreurFormule(f"si() prend 3 arguments dans « {self.texte} »")
                return ("appel", v, args)
            return ("var", v)
        if (g, v) == ("op", "("):
            self.i += 1
            a = self.ou()
            self.prendre("op", ")")
            return a
        raise ErreurFormule(f"terme attendu, trouvé {v!r} dans « {self.texte} »")


_CACHE: dict[str, tuple] = {}


def analyser(texte) -> tuple:
    texte = str(texte)
    if texte not in _CACHE:
        _CACHE[texte] = _Analyseur(texte).analyser()
    return _CACHE[texte]


def noms(texte) -> set[str]:
    """Noms de variables utilisés par une formule (pour la vérification)."""
    out: set[str] = set()

    def parcourir(n):
        if n[0] == "var":
            out.add(n[1])
        elif n[0] == "num":
            pass
        elif n[0] == "appel":
            for a in n[2]:
                parcourir(a)
        else:
            for a in n[1:]:
                parcourir(a)

    parcourir(analyser(texte))
    return out


def evaluer(texte, env: dict) -> float:
    def ev(n):
        t = n[0]
        if t == "num":
            return n[1]
        if t == "var":
            if n[1] not in env:
                raise ErreurFormule(f"nom inconnu « {n[1]} »")
            return float(env[n[1]] or 0)
        if t == "neg":
            return -ev(n[1])
        if t == "non":
            return 0.0 if ev(n[1]) else 1.0
        if t == "et":
            return 1.0 if (ev(n[1]) and ev(n[2])) else 0.0
        if t == "ou":
            return 1.0 if (ev(n[1]) or ev(n[2])) else 0.0
        if t == "appel":
            nom, args = n[1], n[2]
            if nom == "si":
                return ev(args[1]) if ev(args[0]) else ev(args[2])
            valeurs = [ev(a) for a in args]
            return min(valeurs) if nom == "min" else max(valeurs)
        a, b = ev(n[1]), ev(n[2])
        if t == "+":
            return a + b
        if t == "-":
            return a - b
        if t == "*":
            return a * b
        if t == "/":
            return 0.0 if b == 0 else a / b
        return 1.0 if {"<": a < b, "<=": a <= b, ">": a > b, ">=": a >= b,
                       "==": a == b, "!=": a != b}[t] else 0.0

    return ev(analyser(texte))


def _arrondi(x):
    return None if x is None else round(x, 2)


def diagnostiquer(modele: dict, valeurs: dict, profil: dict) -> dict:
    """modele : contenu de data/diagnostic.yaml (enrichi de vague et lien par l'export) ;
    valeurs : {scenario: {cle: valeur}} ; profil : {nom: valeur} saisi pour la ferme."""
    profil = profil or {}
    reponses = {}
    for q in modele.get("questions", []):
        v = profil.get(q["id"])
        reponses[q["id"]] = float(q.get("defaut", 0) if v in (None, "") else v)

    env_actuel = {**valeurs["actuel"], **reponses}
    consommations, estimees = {}, {}
    for c in modele.get("consommations", []):
        estime = evaluer(c["estimation"], env_actuel)
        estimees[c["id"]] = estime
        saisi = profil.get(c["id"])
        consommations[c["id"]] = estime if saisi in (None, "") else float(saisi)
        env_actuel[c["id"]] = consommations[c["id"]]

    resultat = {"reponses": reponses, "consommations": consommations, "estimations": estimees,
                "postes": [], "recommandations": []}
    envs = {s: {**valeurs[s], **reponses, **consommations} for s in SCENARIOS}

    for p in modele.get("postes", []):
        dep = {s: _arrondi(evaluer(p["depense"], envs[s])) for s in SCENARIOS}
        resultat["postes"].append({"id": p["id"], "depense": dep})

    for r in modele.get("recommandations", []):
        if not evaluer(r["condition"], envs["actuel"]):
            continue
        sortie = {"id": r["id"], "economie": {}, "investissement": None, "aide": None, "retour": {}}
        for s in SCENARIOS:
            sortie["economie"][s] = _arrondi(evaluer(r["economie"], envs[s]))
        if r.get("investissement"):
            sortie["investissement"] = _arrondi(evaluer(r["investissement"], envs["actuel"]))
            sortie["aide"] = _arrondi(evaluer(r["aide"], envs["actuel"])) if r.get("aide") else 0.0
            net = max(sortie["investissement"] - sortie["aide"], 0.0)
            for s in SCENARIOS:
                e = sortie["economie"][s]
                sortie["retour"][s] = _arrondi(net / e) if e and e > 0 else None
        resultat["recommandations"].append(sortie)
    return resultat
