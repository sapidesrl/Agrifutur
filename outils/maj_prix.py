"""Met à jour les prix publics de data/hypotheses.yaml à partir des sources officielles.

Sources lues automatiquement :
  - Statbel (Bestat) : prix maximum officiels du SPF Économie, jour par jour, TVA comprise
    (gasoil de chauffage, gasoil agricole, diesel B7, diesel XTL, propane) ;
  - FEGRA : cotations indicatives du blé (export CSV de la page) ;
  - CREG : tableau de bord mensuel, prix « all in » hors TVA d'une PME (50 MWh/an) en Wallonie.

Chaque prix est la moyenne du mois de référence (jours publiés jusqu'à aujourd'hui).
Le scénario bas (février 2026, avant la crise) est recalculé avec la même méthode.

Usage :
  python outils/maj_prix.py --mois 2026-11            # affiche les écarts, ne modifie rien
  python outils/maj_prix.py --mois 2026-11 --ecrire   # écrit dans data/hypotheses.yaml
Puis : python calc/couts.py && python outils/verifier_fiches.py && mkdocs build --strict

Attention : les fiches parlent des « prix de novembre 2026 ». Changer de mois de référence
demande de relire leurs textes.

Dépendance en plus de requirements.txt : pypdf (pip install -r outils/requirements-maj.txt).
"""
import argparse
import csv
import datetime as dt
import io
import re
import sys
import urllib.parse
import urllib.request
from pathlib import Path

import yaml

RACINE = Path(__file__).resolve().parent.parent
HYPOTHESES = RACINE / "data" / "hypotheses.yaml"
MOIS_BAS = "2026-02"
UA = {"User-Agent": "Agrifutur-maj-prix/1.0 (base de connaissances agricole)"}

STATBEL_CSV = "https://bestat.statbel.fgov.be/bestat/api/views/939c67bb-39fa-4f49-9d05-c446187bef1d/result/CSV"
STATBEL_PAGE = "https://bestat.statbel.fgov.be/bestat/crosstable.xhtml?view=939c67bb-39fa-4f49-9d05-c446187bef1d"
FEGRA_PAGE = "https://fegra.be/home/agriculturalprices?lang=fr"
FEGRA_CSV = "https://fegra.be/Home/DownloadPrices"
CREG_PDF = "https://www.creg.be/sites/default/files/assets/Prices/Dashboard/tableaudebord{aaaamm}.pdf"

MOIS_FR = ["janvier", "février", "mars", "avril", "mai", "juin", "juillet", "août",
           "septembre", "octobre", "novembre", "décembre"]
MOIS_ABR = {m: i + 1 for i, m in enumerate(
    ["JAN", "FEB", "MAR", "APR", "MAY", "JUN", "JUL", "AUG", "SEP", "OCT", "NOV", "DEC"])}

CHAUFFAGE = "Gasoil chauffage (H0/H7) (à partir de 2000 l) (€/L)"
AGRICOLE = "Gasoil Diesel Agriculture (à partir de 2000 l) (€/L)"
B7 = "Diesel B7 (€/L)"
XTL = "Diesel XTL (€/L)"
PROPANE = "Propane en vrac (à partir de 2000 l) (€/L)"


def lire(url: str, donnees: dict | None = None) -> bytes:
    corps = urllib.parse.urlencode(donnees).encode() if donnees else None
    req = urllib.request.Request(url, data=corps, headers=UA)
    with urllib.request.urlopen(req, timeout=60) as r:
        return r.read()


def nom_mois(aaaa_mm: str) -> str:
    a, m = aaaa_mm.split("-")
    return f"{MOIS_FR[int(m) - 1]} {a}"


def fr(x: float, d: int = 4) -> str:
    return f"{x:.{d}f}".replace(".", ",")


# --- Statbel ------------------------------------------------------------------

def statbel() -> dict[str, dict[dt.date, float]]:
    texte = lire(STATBEL_CSV).decode("utf-8-sig")
    series: dict[str, dict[dt.date, float]] = {}
    for ligne in list(csv.reader(io.StringIO(texte)))[1:]:
        if len(ligne) < 5 or not ligne[4].strip():
            continue
        j = ligne[1]  # ex. 26NOV26
        jour = dt.date(2000 + int(j[5:7]), MOIS_ABR[j[2:5]], int(j[:2]))
        series.setdefault(ligne[3], {})[jour] = float(ligne[4])
    return series


def moyenne_mois(serie: dict[dt.date, float], aaaa_mm: str) -> tuple[float, int, dt.date]:
    a, m = map(int, aaaa_mm.split("-"))
    jours = sorted(d for d in serie if d.year == a and d.month == m and d <= dt.date.today())
    if not jours:
        raise ValueError(f"aucune donnée pour {aaaa_mm}")
    return sum(serie[d] for d in jours) / len(jours), len(jours), jours[-1]


# --- FEGRA --------------------------------------------------------------------

def fegra(aaaa_mm: str) -> tuple[float, int, dt.date]:
    a, m = map(int, aaaa_mm.split("-"))
    debut = dt.date(a, m, 1)
    fin = min(dt.date(a + (m == 12), m % 12 + 1, 1) - dt.timedelta(days=1), dt.date.today())
    brut = lire(FEGRA_CSV, {"DateFrom": debut.strftime("%d-%m-%Y"), "DateTo": fin.strftime("%d-%m-%Y")})
    texte = brut.decode("utf-16-le").lstrip("﻿")
    lignes = list(csv.reader(io.StringIO(texte), delimiter=";"))
    # En-têtes en français ou en néerlandais selon la langue de la session.
    col = next(i for i, h in enumerate(lignes[0])
               if h.startswith("BLE STANDARD certifi") or h.strip() == "STANDAARD TARWE gecertificeerd")
    # Dates en 03-11-2026 ou 03/11/2026 selon la langue de la session.
    valeurs = [(dt.datetime.strptime(l[0].replace("/", "-"), "%d-%m-%Y").date(),
                float(l[col].replace(",", ".")))
               for l in lignes[1:] if len(l) > col and l[col].strip()]
    if not valeurs:
        raise ValueError(f"aucune cotation FEGRA pour {aaaa_mm}")
    return sum(v for _, v in valeurs) / len(valeurs), len(valeurs), max(d for d, _ in valeurs)


# --- CREG ---------------------------------------------------------------------

def creg(aaaa_mm: str) -> tuple[float, str]:
    """Prix PME 50 MWh, Wallonie, du mois demandé (dernier groupe du tableau de la page « PME »)."""
    from pypdf import PdfReader  # dépendance de outils/requirements-maj.txt

    url = CREG_PDF.format(aaaamm=aaaa_mm.replace("-", ""))
    lecteur = PdfReader(io.BytesIO(lire(url)))
    attendu = nom_mois(aaaa_mm).upper()
    for page in lecteur.pages:
        lignes = (page.extract_text() or "").splitlines()
        if not any(attendu in l.upper() for l in lignes[:3]):
            continue  # la page doit porter le mois demandé dans son titre
        for i, l in enumerate(lignes):
            if l.strip() != "50.000 kWh":
                continue
            # La ligne en c€/kWh suit celle en €/an. Trois mois par ligne (BE, VL, BR, WAL),
            # le dernier groupe est le mois du tableau de bord : la valeur wallonne est la 12e.
            for suivante in lignes[i + 1:i + 4]:
                if suivante.startswith("CREG c€/kWh"):
                    nombres = re.findall(r"\d+,\d+", suivante)
                    if len(nombres) >= 12:
                        return float(nombres[11].replace(",", ".")) / 100, url
    raise ValueError(f"prix PME de {nom_mois(aaaa_mm)} introuvable dans {url}")


# --- Écriture -----------------------------------------------------------------

def remplacer_champ(texte: str, cle: str, champ: str, valeur: str) -> str:
    m = re.search(rf"^{cle}:\n(?:[ ]{{2}}.*\n)*", texte, re.M)
    if not m:
        raise KeyError(cle)
    bloc = m.group(0)
    nouvelle = f"  {champ}: {valeur}"
    if re.search(rf"^  {champ}:", bloc, re.M):
        bloc2 = re.sub(rf"^  {champ}:.*$", lambda _: nouvelle, bloc, count=1, flags=re.M)
    else:
        bloc2 = bloc + nouvelle + "\n"
    return texte[:m.start()] + bloc2 + texte[m.end():]


def guillemets(s: str) -> str:
    return '"' + s.replace("\\", "\\\\").replace('"', '\\"') + '"'


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    p.add_argument("--mois", required=True, help="mois de référence, AAAA-MM (ex. 2026-11)")
    p.add_argument("--ecrire", action="store_true", help="écrire dans data/hypotheses.yaml")
    args = p.parse_args()
    if not re.fullmatch(r"\d{4}-\d{2}", args.mois):
        p.error("--mois doit être au format AAAA-MM")

    lu = dt.date.today().strftime("%d/%m/%Y")
    mois, mois_bas = nom_mois(args.mois), nom_mois(MOIS_BAS)
    maj: dict[str, dict] = {}

    s = statbel()
    def carburant(cle, produit, libelle):
        v, n, der = moyenne_mois(s[produit], args.mois)
        b, nb, _ = moyenne_mois(s[produit], MOIS_BAS)
        maj[cle] = {
            "valeur": round(v, 4), "date": der.isoformat(), "source": STATBEL_CSV,
            "note": f"{libelle} : moyenne des prix maximums officiels de {mois} ({n} jours publiés, "
                    f"jusqu'au {der.strftime('%d/%m/%Y')}), TVA comprise, tarif officiel du SPF Économie "
                    f"publié par Statbel ; calculée par outils/maj_prix.py le {lu}.",
            "bas": round(b, 4),
            "bas_note": f"{mois_bas.capitalize()} (avant-crise) : moyenne des {nb} prix maximums officiels "
                        f"du mois, même source ({STATBEL_PAGE}).",
        }
    carburant("gasoil_chauffage_2000l_tvac", CHAUFFAGE, "Gasoil de chauffage (H0/H7), au moins 2 000 L")
    carburant("diesel_b7_tvac", B7, "Diesel routier B7 à la pompe")
    carburant("diesel_xtl_tvac", XTL, "Diesel XTL (de synthèse, dont HVO) à la pompe")
    carburant("propane_vrac_tvac", PROPANE, "Propane en vrac, au moins 2 000 L")

    ch, _, der = moyenne_mois(s[CHAUFFAGE], args.mois)
    ag, n, _ = moyenne_mois(s[AGRICOLE], args.mois)
    chb, _, _ = moyenne_mois(s[CHAUFFAGE], MOIS_BAS)
    agb, _, _ = moyenne_mois(s[AGRICOLE], MOIS_BAS)
    maj["ecart_gasoil_agricole_chauffage"] = {
        "valeur": round(ch - ag, 4), "date": der.isoformat(), "source": STATBEL_CSV,
        "note": f"Écart TVA comprise entre les moyennes de {mois} du gasoil de chauffage ({fr(ch)} €/L) "
                f"et du gasoil agricole ({fr(ag)} €/L), au moins 2 000 L, prix maximums officiels "
                f"(SPF Économie, Statbel) ; calculé par outils/maj_prix.py le {lu}.",
        "bas": round(chb - agb, 4),
        "bas_note": f"{mois_bas.capitalize()} : chauffage {fr(chb)} €/L moins agricole {fr(agb)} €/L "
                    f"(moyennes officielles du mois), pour que le scénario bas retombe sur le prix agricole de février.",
    }

    v, n, der = fegra(args.mois)
    b, nb, _ = fegra(MOIS_BAS)
    maj["ble_prix"] = {
        "valeur": round(v, 1), "date": der.isoformat(), "source": FEGRA_PAGE,
        "note": f"Moyenne des {n} cotations indicatives FEGRA/Synagra de {mois} en blé standard "
                f"certifié Vegaplan (jusqu'au {der.strftime('%d/%m/%Y')}), export CSV de la page. "
                f"Prix indicatifs, hors TVA, base de livraison non précisée ; le prix réel est fixé par "
                f"le négociant. Calculée par outils/maj_prix.py le {lu}.",
        "bas": round(b, 1),
        "bas_note": f"{mois_bas.capitalize()} (avant-crise) : moyenne des {nb} cotations FEGRA du mois, "
                    f"même source et même base.",
    }

    v, url = creg(args.mois)
    b, url_bas = creg(MOIS_BAS)
    maj["electricite_reseau_htva"] = {
        "valeur": round(v, 4), "date": args.mois + "-01", "source": url,
        "note": f"CREG, tableau de bord mensuel de {mois} : prix moyen « all in » hors TVA (énergie, "
                f"réseau, surcharges) pour une PME de 50 000 kWh/an en Wallonie, offres des grands "
                f"fournisseurs ; lu par outils/maj_prix.py le {lu}. Un contrat négocié peut être moins "
                f"cher : remplacer par le prix de la facture.",
        "bas": round(b, 4),
        "bas_note": f"{mois_bas.capitalize()}, même profil, CREG ({url_bas}).",
    }

    actuel = yaml.safe_load(HYPOTHESES.read_text(encoding="utf-8"))
    print(f"{'clé':34} {'actuel':>9} {'nouveau':>9}   {'bas actuel':>10} {'bas nouv.':>10}")
    for cle, e in maj.items():
        a = actuel.get(cle, {})
        print(f"{cle:34} {a.get('valeur')!s:>9} {e['valeur']!s:>9}   {a.get('bas')!s:>10} {e['bas']!s:>10}")

    if not args.ecrire:
        print("\nRien n'est écrit. Relancer avec --ecrire pour mettre à jour data/hypotheses.yaml.")
        return 0

    texte = HYPOTHESES.read_text(encoding="utf-8")
    for cle, e in maj.items():
        if cle not in actuel:
            print(f"clé absente de hypotheses.yaml, ignorée : {cle}", file=sys.stderr)
            continue
        texte = remplacer_champ(texte, cle, "valeur", str(e["valeur"]))
        texte = remplacer_champ(texte, cle, "statut", "sourcé")
        texte = remplacer_champ(texte, cle, "date", e["date"])
        texte = remplacer_champ(texte, cle, "source", e["source"])
        texte = remplacer_champ(texte, cle, "note", guillemets(e["note"]))
        texte = remplacer_champ(texte, cle, "bas", str(e["bas"]))
        texte = remplacer_champ(texte, cle, "bas_note", guillemets(e["bas_note"]))
    yaml.safe_load(texte)  # le fichier doit rester lisible
    HYPOTHESES.write_text(texte, encoding="utf-8")
    print("\ndata/hypotheses.yaml mis à jour. Lancer ensuite : python calc/couts.py")
    return 0


if __name__ == "__main__":
    sys.exit(main())
