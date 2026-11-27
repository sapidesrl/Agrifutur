/* Page « Diagnostic de sa ferme » : formulaire, calcul et affichage.
 * Tout se passe dans le navigateur : rien n'est envoyé. Le profil peut être gardé dans ce
 * navigateur (localStorage), téléchargé en JSON et rechargé, ou passé au script
 * outils/diagnostic.py pour un rapport détaillé. Le calcul vient de diagnostic-moteur.js. */
(function () {
  "use strict";
  var script = document.currentScript;
  var base = script ? script.src : location.href;
  var URL_DONNEES = new URL("../assets/diagnostic/donnees.json", base).href;
  var RACINE_SITE = new URL("../", base).href;
  var CLE_STOCKAGE = "agrifutur-diagnostic-profil";
  var nf0 = new Intl.NumberFormat("fr-BE", { maximumFractionDigits: 0 });
  var nf1 = new Intl.NumberFormat("fr-BE", { minimumFractionDigits: 1, maximumFractionDigits: 1 });

  function el(tag, attrs, enfants) {
    var e = document.createElement(tag);
    for (var k in (attrs || {})) {
      if (k === "texte") e.textContent = attrs[k];
      else if (k === "classe") e.className = attrs[k];
      else e.setAttribute(k, attrs[k]);
    }
    (enfants || []).forEach(function (c) { if (c) e.appendChild(typeof c === "string" ? document.createTextNode(c) : c); });
    return e;
  }
  function euros(x) { return x === null || x === undefined ? "—" : nf0.format(x) + " €"; }
  function lireStockage() { try { return JSON.parse(localStorage.getItem(CLE_STOCKAGE) || "{}"); } catch (e) { return {}; } }
  function ecrireStockage(p) { try { localStorage.setItem(CLE_STOCKAGE, JSON.stringify(p)); } catch (e) { /* stockage indisponible */ } }

  function demarrer(conteneur) {
    fetch(URL_DONNEES).then(function (r) { return r.json(); }).then(function (donnees) {
      construire(conteneur, donnees);
    }).catch(function () {
      conteneur.textContent = "Les données du diagnostic n'ont pas pu être chargées.";
    });
  }

  function construire(conteneur, donnees) {
    var modele = donnees.modele, profil = lireStockage(), champs = {};
    conteneur.textContent = "";
    var formulaire = el("form", { classe: "diag-formulaire", autocomplete: "off" });
    var resultats = el("div", { classe: "diag-resultats", "aria-live": "polite" });

    modele.groupes.forEach(function (g) {
      var bloc = el("fieldset", { classe: "diag-groupe" }, [el("legend", { texte: g.titre })]);
      var liste = g.id === "consommations" ? modele.consommations : modele.questions.filter(function (q) { return q.groupe === g.id; });
      liste.forEach(function (q) {
        var id = "diag-" + q.id, champ;
        if (q.type === "oui_non") {
          champ = el("input", { type: "checkbox", id: id });
          champ.checked = q.id in profil ? !!Number(profil[q.id]) : !!q.defaut;
          bloc.appendChild(el("div", { classe: "diag-ligne diag-case" }, [champ, el("label", { "for": id, texte: q.libelle })]));
        } else {
          champ = el("input", { type: "number", id: id, min: "0", step: "any", inputmode: "decimal" });
          if (profil[q.id] !== undefined && profil[q.id] !== "") champ.value = profil[q.id];
          else if (g.id !== "consommations" && q.defaut) champ.value = q.defaut;
          bloc.appendChild(el("div", { classe: "diag-ligne" }, [
            el("label", { "for": id, texte: q.libelle }), champ, el("span", { classe: "diag-unite", texte: q.unite || "" })]));
        }
        champs[q.id] = champ;
      });
      formulaire.appendChild(bloc);
    });

    function profilCourant() {
      var p = {};
      for (var k in champs) {
        var c = champs[k];
        if (c.type === "checkbox") p[k] = c.checked ? 1 : 0;
        else if (c.value !== "") p[k] = Number(c.value);
      }
      return p;
    }

    function calculer() {
      var p = profilCourant();
      ecrireStockage(p);
      var r = DiagnosticMoteur.diagnostiquer(modele, donnees.valeurs, p);
      modele.consommations.forEach(function (c) {
        champs[c.id].placeholder = "estimé : " + nf0.format(r.estimations[c.id]);
      });
      afficher(r);
    }

    function afficher(r) {
      resultats.textContent = "";
      var postes = {}; modele.postes.forEach(function (p) { postes[p.id] = p; });
      var tot = { actuel: 0, bas: 0, haut: 0 };
      var tbody = el("tbody");
      r.postes.forEach(function (p) {
        if (!p.depense.actuel) return;
        ["actuel", "bas", "haut"].forEach(function (s) { tot[s] += p.depense[s] || 0; });
        var def = postes[p.id];
        tbody.appendChild(el("tr", {}, [
          el("td", {}, [el("a", { href: RACINE_SITE + def.lien, texte: def.libelle })]),
          el("td", { texte: euros(p.depense.actuel) }), el("td", { texte: euros(p.depense.bas) }), el("td", { texte: euros(p.depense.haut) })]));
      });
      tbody.appendChild(el("tr", { classe: "diag-total" }, [el("td", { texte: "Total" }),
        el("td", { texte: euros(tot.actuel) }), el("td", { texte: euros(tot.bas) }), el("td", { texte: euros(tot.haut) })]));
      resultats.appendChild(el("h2", { texte: "Vos dépenses liées au pétrole et au gaz" }));
      if (!tot.actuel) {
        resultats.appendChild(el("p", { texte: "Renseignez les surfaces, les animaux ou les consommations pour voir le diagnostic." }));
        return;
      }
      resultats.appendChild(el("p", { texte: "Au prix actuel, ces postes coûtent environ " + euros(tot.actuel) +
        " par an, contre " + euros(tot.bas) + " au prix de février 2026 : la crise de l'énergie vous coûte environ " +
        euros(tot.actuel - tot.bas) + " par an (estimation)." }));
      resultats.appendChild(el("table", {}, [el("thead", {}, [el("tr", {}, [el("th", { texte: "Poste" }),
        el("th", { texte: "Prix actuel" }), el("th", { texte: "Avant la crise" }), el("th", { texte: "Prix haut" })])]), tbody]));

      var infos = {}; modele.recommandations.forEach(function (x) { infos[x.id] = x; });
      var recos = r.recommandations.slice().sort(function (a, b) {
        var va = infos[a.id].vague, vb = infos[b.id].vague;
        if (va !== vb) return va - vb;
        var ra = a.retour.actuel, rb = b.retour.actuel;
        if ((ra || 0) !== (rb || 0)) return (ra || 0) - (rb || 0);
        return (b.economie.actuel || 0) - (a.economie.actuel || 0);
      });
      resultats.appendChild(el("h2", { texte: "Les changements à étudier" }));
      if (!recos.length) {
        resultats.appendChild(el("p", { texte: "Aucun changement chiffré ne correspond à ce profil." }));
      } else {
        resultats.appendChild(el("p", { texte: "Classés par vague (1 = rentable aujourd'hui, 2 = sous conditions), puis par temps de retour." }));
        var liste = el("div", { classe: "diag-recos" });
        recos.forEach(function (x) {
          var i = infos[x.id];
          var chiffres = "Économie : " + euros(x.economie.actuel) + " par an (" + euros(x.economie.bas) + " avant la crise)";
          if (x.investissement !== null) {
            chiffres += ". Investissement : " + euros(x.investissement) + (x.aide ? ", aide " + euros(x.aide) : "");
            chiffres += x.retour.actuel !== null ? ". Retour : " + nf1.format(x.retour.actuel) + " ans" : ". Pas de retour sur l'énergie seule";
          }
          liste.appendChild(el("div", { classe: "diag-reco" }, [
            el("p", { classe: "diag-reco-titre" }, [el("span", { classe: "diag-vague diag-vague-" + i.vague, texte: "vague " + i.vague }), " ",
              el("a", { href: RACINE_SITE + i.lien, texte: i.titre })]),
            el("p", { classe: "diag-reco-chiffres", texte: chiffres + "." }),
            el("p", { classe: "diag-reco-texte", texte: i.texte })]));
        });
        resultats.appendChild(liste);
      }
    }

    var actions = el("div", { classe: "diag-actions" });
    var bTelecharger = el("button", { type: "button", classe: "md-button", texte: "Télécharger le profil" });
    var bCharger = el("button", { type: "button", classe: "md-button", texte: "Charger un profil" });
    var bEffacer = el("button", { type: "button", classe: "md-button", texte: "Tout effacer" });
    var fichier = el("input", { type: "file", accept: ".json,application/json", hidden: "hidden" });
    bTelecharger.addEventListener("click", function () {
      var blob = new Blob([JSON.stringify({ profil: profilCourant() }, null, 1)], { type: "application/json" });
      var a = el("a", { href: URL.createObjectURL(blob), download: "profil-ferme.json" });
      document.body.appendChild(a); a.click(); a.remove();
    });
    bCharger.addEventListener("click", function () { fichier.click(); });
    fichier.addEventListener("change", function () {
      var f = fichier.files[0]; if (!f) return;
      f.text().then(function (t) {
        var d = JSON.parse(t); ecrireStockage(d.profil || d); construire(conteneur, donnees);
      }).catch(function () { resultats.prepend(el("p", { texte: "Ce fichier n'est pas un profil valide." })); });
    });
    bEffacer.addEventListener("click", function () { ecrireStockage({}); construire(conteneur, donnees); });
    [bTelecharger, bCharger, bEffacer, fichier].forEach(function (b) { actions.appendChild(b); });

    var minuterie;
    formulaire.addEventListener("input", function () { clearTimeout(minuterie); minuterie = setTimeout(calculer, 250); });
    formulaire.addEventListener("submit", function (e) { e.preventDefault(); });
    conteneur.appendChild(formulaire);
    conteneur.appendChild(actions);
    conteneur.appendChild(resultats);
    calculer();
  }

  function lancer() {
    var c = document.getElementById("diagnostic");
    if (c && window.DiagnosticMoteur) demarrer(c);
  }
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", lancer);
  else lancer();
  // Navigation instantanée du thème : relancer à chaque changement de page.
  if (window.document$ && window.document$.subscribe) window.document$.subscribe(lancer);
})();
