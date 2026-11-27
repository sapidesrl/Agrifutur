/* Moteur du diagnostic d'exploitation (version JavaScript).
 * Même langage de formules et mêmes règles que outils/moteur_diagnostic.py :
 * nombres, noms, + - * /, parenthèses, < <= > >= == !=, et / ou / non,
 * min(…), max(…), si(condition, a, b). Vrai = 1, faux = 0, division par zéro = 0.
 * Toute modification ici doit être reportée dans la version Python
 * (outils/tester_diagnostic.py compare les deux). */
(function (racine) {
  "use strict";
  var SCENARIOS = ["actuel", "bas", "haut"];
  var MOTS = { et: 1, ou: 1, non: 1 };
  var JETON = /\s*(?:(\d+(?:\.\d+)?)|([a-z_][a-z0-9_]*)|(<=|>=|==|!=|[-+*/(),<>]))/y;

  function decouper(texte) {
    var jetons = [], pos = 0;
    texte = String(texte).trim();
    while (pos < texte.length) {
      JETON.lastIndex = pos;
      var m = JETON.exec(texte);
      if (!m || JETON.lastIndex === pos) throw new Error("caractère inattendu : " + texte.slice(pos, pos + 10));
      if (m[1] !== undefined) jetons.push(["nombre", m[1]]);
      else if (m[2] !== undefined) jetons.push([MOTS[m[2]] ? "mot" : "nom", m[2]]);
      else jetons.push(["op", m[3]]);
      pos = JETON.lastIndex;
      while (pos < texte.length && /\s/.test(texte[pos])) pos++;
    }
    return jetons;
  }

  function analyser(texte) {
    var j = decouper(texte), i = 0;
    function voir() { return j[i] || [null, null]; }
    function est(g, v) { var t = voir(); return t[0] === g && t[1] === v; }
    function prendre(g, v) {
      var t = voir();
      if ((g && t[0] !== g) || (v && t[1] !== v)) throw new Error("attendu " + (v || g) + ", trouvé " + t[1] + " dans « " + texte + " »");
      i++; return t[1];
    }
    function ou() { var a = et(); while (est("mot", "ou")) { i++; a = ["ou", a, et()]; } return a; }
    function et() { var a = non(); while (est("mot", "et")) { i++; a = ["et", a, non()]; } return a; }
    function non() { if (est("mot", "non")) { i++; return ["non", non()]; } return comparaison(); }
    function comparaison() {
      var a = somme(), t = voir();
      if (t[0] === "op" && ["<", "<=", ">", ">=", "==", "!="].indexOf(t[1]) >= 0) { i++; return [t[1], a, somme()]; }
      return a;
    }
    function somme() { var a = produit(); while (voir()[0] === "op" && (voir()[1] === "+" || voir()[1] === "-")) { var op = prendre(); a = [op, a, produit()]; } return a; }
    function produit() { var a = unaire(); while (voir()[0] === "op" && (voir()[1] === "*" || voir()[1] === "/")) { var op = prendre(); a = [op, a, unaire()]; } return a; }
    function unaire() { if (est("op", "-")) { i++; return ["neg", unaire()]; } return primaire(); }
    function primaire() {
      var t = voir();
      if (t[0] === "nombre") { i++; return ["num", parseFloat(t[1])]; }
      if (t[0] === "nom") {
        i++;
        if (est("op", "(")) {
          i++;
          var args = [];
          if (!est("op", ")")) { args.push(ou()); while (est("op", ",")) { i++; args.push(ou()); } }
          prendre("op", ")");
          if (["min", "max", "si"].indexOf(t[1]) < 0) throw new Error("fonction inconnue " + t[1] + "()");
          if (t[1] === "si" && args.length !== 3) throw new Error("si() prend 3 arguments");
          return ["appel", t[1], args];
        }
        return ["var", t[1]];
      }
      if (est("op", "(")) { i++; var a = ou(); prendre("op", ")"); return a; }
      throw new Error("terme attendu, trouvé " + t[1] + " dans « " + texte + " »");
    }
    var arbre = ou();
    if (i !== j.length) throw new Error("fin inattendue dans « " + texte + " »");
    return arbre;
  }

  var cache = {};
  function evaluer(texte, env) {
    var cle = String(texte);
    var arbre = cache[cle] || (cache[cle] = analyser(cle));
    function ev(n) {
      var t = n[0], a, b;
      if (t === "num") return n[1];
      if (t === "var") {
        if (!(n[1] in env)) throw new Error("nom inconnu « " + n[1] + " »");
        return Number(env[n[1]] || 0);
      }
      if (t === "neg") return -ev(n[1]);
      if (t === "non") return ev(n[1]) ? 0 : 1;
      if (t === "et") return (ev(n[1]) && ev(n[2])) ? 1 : 0;
      if (t === "ou") return (ev(n[1]) || ev(n[2])) ? 1 : 0;
      if (t === "appel") {
        if (n[1] === "si") return ev(n[2][0]) ? ev(n[2][1]) : ev(n[2][2]);
        var vals = n[2].map(ev);
        return n[1] === "min" ? Math.min.apply(null, vals) : Math.max.apply(null, vals);
      }
      a = ev(n[1]); b = ev(n[2]);
      switch (t) {
        case "+": return a + b;
        case "-": return a - b;
        case "*": return a * b;
        case "/": return b === 0 ? 0 : a / b;
        case "<": return a < b ? 1 : 0;
        case "<=": return a <= b ? 1 : 0;
        case ">": return a > b ? 1 : 0;
        case ">=": return a >= b ? 1 : 0;
        case "==": return a === b ? 1 : 0;
        case "!=": return a !== b ? 1 : 0;
      }
      throw new Error("opération inconnue " + t);
    }
    return ev(arbre);
  }

  function arrondi(x) { return x === null || x === undefined ? null : Math.round(x * 100) / 100; }
  function vide(v) { return v === null || v === undefined || v === ""; }
  function copie(o) { var r = {}; for (var k in o) r[k] = o[k]; return r; }
  function fusion() { var r = {}; for (var i = 0; i < arguments.length; i++) for (var k in arguments[i]) r[k] = arguments[i][k]; return r; }

  function diagnostiquer(modele, valeurs, profil) {
    profil = profil || {};
    var reponses = {}, i, s;
    (modele.questions || []).forEach(function (q) {
      var v = profil[q.id];
      reponses[q.id] = Number(vide(v) ? (q.defaut || 0) : v);
    });
    var envActuel = fusion(valeurs.actuel, reponses), consommations = {}, estimees = {};
    (modele.consommations || []).forEach(function (c) {
      var estime = evaluer(c.estimation, envActuel);
      estimees[c.id] = estime;
      var saisi = profil[c.id];
      consommations[c.id] = vide(saisi) ? estime : Number(saisi);
      envActuel[c.id] = consommations[c.id];
    });
    var resultat = { reponses: reponses, consommations: consommations, estimations: estimees, postes: [], recommandations: [] };
    var envs = {};
    SCENARIOS.forEach(function (s) { envs[s] = fusion(valeurs[s], reponses, consommations); });

    (modele.postes || []).forEach(function (p) {
      var dep = {};
      SCENARIOS.forEach(function (s) { dep[s] = arrondi(evaluer(p.depense, envs[s])); });
      resultat.postes.push({ id: p.id, depense: dep });
    });
    (modele.recommandations || []).forEach(function (r) {
      if (!evaluer(r.condition, envs.actuel)) return;
      var sortie = { id: r.id, economie: {}, investissement: null, aide: null, retour: {} };
      SCENARIOS.forEach(function (s) { sortie.economie[s] = arrondi(evaluer(r.economie, envs[s])); });
      if (r.investissement) {
        sortie.investissement = arrondi(evaluer(r.investissement, envs.actuel));
        sortie.aide = r.aide ? arrondi(evaluer(r.aide, envs.actuel)) : 0;
        var net = Math.max(sortie.investissement - sortie.aide, 0);
        SCENARIOS.forEach(function (s) {
          var e = sortie.economie[s];
          sortie.retour[s] = e && e > 0 ? arrondi(net / e) : null;
        });
      }
      resultat.recommandations.push(sortie);
    });
    return resultat;
  }

  var api = { evaluer: evaluer, analyser: analyser, diagnostiquer: diagnostiquer, SCENARIOS: SCENARIOS };
  if (typeof module !== "undefined" && module.exports) module.exports = api;
  else racine.DiagnosticMoteur = api;
})(typeof window !== "undefined" ? window : this);
