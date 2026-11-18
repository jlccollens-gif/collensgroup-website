#!/usr/bin/env python3
"""Groeisysteem Collens Group: meten, onthouden, leren, verbeteren.

  python3 tools/groei/groei.py init                 database aanmaken + startbacklog
  python3 tools/groei/groei.py run                  processor: site meten, vergelijken, backlog bijwerken
  python3 tools/groei/groei.py report [--out f.md]  weekrapport
  python3 tools/groei/groei.py backlog [--top 10]   wat nu het meest oplevert
  python3 tools/groei/groei.py klaar ID "notitie"   punt afronden (met effect-notitie)
  python3 tools/groei/groei.py nieuw "titel" --cat seo --impact 4 --moeite 2 [--wie claude|jeffrey] [--auto]
  python3 tools/groei/groei.py leer "onderwerp" "les" [--bewijs "..."]
  python3 tools/groei/groei.py exp "hypothese" "wijziging" "metric" --dagen 14
  python3 tools/groei/groei.py exp-sluit ID "resultaat" "les"
  python3 tools/groei/groei.py lead "bron" "type" [--waarde 995] [--status nieuw]
  python3 tools/groei/groei.py metric naam waarde [--scope site]   handmatige meting (Search Console, GoatCounter)
  python3 tools/groei/groei.py dump bestand.sql | restore bestand.sql

Database: SQLite, pad via GROEI_DB (standaard ./groei.db). Alleen standaardbibliotheek.
De database bevat geen persoonsgegevens van klanten; leads zijn anoniem (bron, type, status, bedrag).
"""
import sqlite3, sys, os, re, json, hashlib, datetime, argparse, time, statistics, urllib.request, urllib.parse
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
import sitecheck

DB = os.environ.get("GROEI_DB", "groei.db")
SITE = os.environ.get("GROEI_SITE", "https://collensgroup.com").rstrip("/")

SCHEMA = """
CREATE TABLE IF NOT EXISTS runs(id INTEGER PRIMARY KEY, ts TEXT, site TEXT, score REAL, n_rood INT, n_geel INT, n_blauw INT, paginas INT, opmerking TEXT);
CREATE TABLE IF NOT EXISTS metrics(id INTEGER PRIMARY KEY, run_id INT, ts TEXT, scope TEXT, naam TEXT, waarde REAL);
CREATE INDEX IF NOT EXISTS ix_metrics ON metrics(scope, naam, ts);
CREATE TABLE IF NOT EXISTS findings(fp TEXT PRIMARY KEY, ernst TEXT, tekst TEXT, eerste_run INT, laatste_run INT, status TEXT, opgelost_run INT);
CREATE TABLE IF NOT EXISTS backlog(id INTEGER PRIMARY KEY, titel TEXT, categorie TEXT, impact INT, moeite INT, status TEXT DEFAULT 'todo',
  wie TEXT DEFAULT 'claude', auto_ok INT DEFAULT 0, blokkade TEXT, bron TEXT, aangemaakt TEXT, klaar_op TEXT, notitie TEXT);
CREATE TABLE IF NOT EXISTS experiments(id INTEGER PRIMARY KEY, hypothese TEXT, wijziging TEXT, metric TEXT, baseline REAL, start TEXT, einde TEXT, status TEXT DEFAULT 'loopt', resultaat TEXT, les TEXT);
CREATE TABLE IF NOT EXISTS learnings(id INTEGER PRIMARY KEY, datum TEXT, onderwerp TEXT, les TEXT, bewijs TEXT);
CREATE TABLE IF NOT EXISTS leads(id INTEGER PRIMARY KEY, datum TEXT, bron TEXT, type TEXT, status TEXT DEFAULT 'nieuw', waarde REAL);
CREATE TABLE IF NOT EXISTS doelen(naam TEXT PRIMARY KEY, doel REAL, deadline TEXT, toelichting TEXT);
"""

# titel, categorie, impact, moeite, wie, auto_ok, blokkade
SEED = [
 ("GoatCounter activeren (cookieloos meten)", "meten", 5, 1, "jeffrey", 0, "Account/code aanmaken; daarna zet Claude de code in de site"),
 ("Google Search Console + Bing Webmaster aanmelden, sitemap indienen", "meten", 5, 1, "jeffrey", 0, "Inloggen met Google-account en eigendom bevestigen"),
 ("Titels inkorten tot maximaal 60 tekens", "seo", 3, 1, "claude", 1, ""),
 ("/tester en /tester/qr op noindex", "seo", 2, 1, "claude", 1, ""),
 ("Beveiligingsheaders (HSTS e.d.) via _headers", "techniek", 2, 1, "claude", 1, ""),
 ("Contactformulier: generieke kop, nette uploadknop, bevestigingstekst", "ux", 3, 2, "claude", 0, ""),
 ("Mobiele header: ruimte tussen naam en taalknop, Advies-knop niet over hero", "ux", 3, 2, "claude", 0, ""),
 ("Hero verbeteren: minder lege ruimte, echte voorbeelden incl. website", "visueel", 4, 3, "claude", 0, ""),
 ("Vervang 'jouwbedrijf.nl'-illustratie door echt project-screenshot", "visueel", 3, 2, "claude", 0, ""),
 ("Prijzenpagina met alle pakketten op een plek", "seo", 4, 2, "claude", 0, ""),
 ("Over ons-pagina (werkwijze, eigen apps, wie)", "vertrouwen", 5, 2, "claude", 0, "Naam en foto van Jeffrey alleen na zijn akkoord"),
 ("Casepagina per eigen app/game (probleem, aanpak, resultaat)", "vertrouwen", 4, 3, "claude", 0, ""),
 ("Home korter en overzichtelijker (vaste volgorde)", "ux", 3, 3, "claude", 0, ""),
 ("Dunne pagina's uitbreiden (apps, mvp, chatbot, app-detail)", "seo", 4, 3, "claude", 0, ""),
 ("Footer: Over ons, voorwaarden, WhatsApp", "vertrouwen", 2, 1, "claude", 0, "WhatsApp-nummer van Jeffrey nodig"),
 ("Pakketkiezer in 3 vragen", "ux", 4, 4, "claude", 0, ""),
 ("Leesbaarheid: tekst minimaal 14 px, contrast, focusranden, alt-teksten", "ux", 3, 2, "claude", 0, ""),
 ("Vergelijkpagina's: app of website, Wix of laten maken", "seo", 4, 3, "claude", 0, ""),
 ("Artikelen: 8 stuks op echte zoekvragen", "seo", 5, 5, "claude", 0, ""),
 ("Pagina 'Website laten maken in België' (nl-BE)", "seo", 3, 2, "claude", 0, ""),
 ("Extra brancheblokken (fotograaf, aannemer, coach, vakantiehuis)", "seo", 3, 3, "claude", 0, ""),
 ("Kostencalculator app/website", "groei", 4, 4, "claude", 0, ""),
 ("Gratis website-check (lead-magneet op basis van sitecheck)", "groei", 5, 4, "claude", 0, ""),
 ("Backlinks via eigen kanalen (YouTube, Pinterest, Instagram, TikTok)", "groei", 4, 2, "claude", 0, "Per kanaal akkoord op openbare link"),
 ("Schema uitbreiden: sameAs, Person, VideoObject, SoftwareApplication", "seo", 3, 2, "claude", 0, ""),
 ("Eerste echte reviews/klantquotes verzamelen", "vertrouwen", 5, 3, "jeffrey", 0, "Alleen echte klanten; nooit verzinnen"),
 ("Google Bedrijfsprofiel aanvragen", "groei", 3, 2, "jeffrey", 0, "Verificatie door eigenaar"),
]
DOELEN = [  # voorstel; pas aan met: groei.py doel naam waarde deadline
 ("score", 90, "2026-12-31", "Sitecheck-score (0-100)"),
 ("artikelen", 8, "2027-02-28", "Aantal artikelpagina's met Article-schema"),
 ("leads_per_maand", 4, "2027-01-31", "Echte aanvragen per maand"),
 ("gewonnen_per_maand", 1, "2027-02-28", "Betaalde opdrachten per maand"),
 ("dunne_paginas", 0, "2027-01-31", "Pagina's onder 300 woorden"),
]

def nu(): return datetime.datetime.now().replace(microsecond=0).isoformat(sep=" ")
def vandaag(): return datetime.date.today().isoformat()
def verbind():
    c = sqlite3.connect(DB); c.row_factory = sqlite3.Row; c.executescript(SCHEMA); return c

def init(c):
    if not c.execute("SELECT 1 FROM backlog LIMIT 1").fetchone():
        for t, cat, i, m, wie, auto, blok in SEED:
            c.execute("INSERT INTO backlog(titel,categorie,impact,moeite,wie,auto_ok,blokkade,bron,aangemaakt) VALUES(?,?,?,?,?,?,?,?,?)",
                      (t, cat, i, m, wie, auto, blok, "audit 18-11-2026", vandaag()))
    for n, d, dl, t in DOELEN:
        c.execute("INSERT OR IGNORE INTO doelen VALUES(?,?,?,?)", (n, d, dl, t))
    c.commit(); print("database klaar:", DB)

# ---------- processor ----------
def norm_tekst(s):
    s = s.replace(SITE, "").replace(".html", "")
    return re.sub(r"\s+", " ", s).strip()

def fingerprint(ernst, tekst):
    return hashlib.sha1((ernst + re.sub(r"\d+", "#", norm_tekst(tekst))).encode()).hexdigest()[:12]

def http_tijd(url):
    t0 = time.time()
    try:
        r = urllib.request.Request(url, headers={"User-Agent": "groei/1.0 (leesverkeer)"})
        with urllib.request.urlopen(r, timeout=20) as f:
            b = f.read(); return f.status, (time.time() - t0) * 1000, len(b)
    except Exception as e:
        return getattr(e, "code", 0), (time.time() - t0) * 1000, 0

def sitemap_urls():
    try:
        r = urllib.request.Request(SITE + "/sitemap.xml", headers={"User-Agent": "groei/1.0"})
        return re.findall(r"<loc>([^<]+)</loc>", urllib.request.urlopen(r, timeout=20).read().decode())
    except Exception:
        return []

def goatcounter():
    code, tok = os.environ.get("GROEI_GOATCOUNTER"), os.environ.get("GROEI_GOATCOUNTER_TOKEN")
    if not (code and tok): return {}
    try:
        start = (datetime.date.today() - datetime.timedelta(days=7)).isoformat()
        r = urllib.request.Request(f"https://{code}.goatcounter.com/api/v0/stats/total?start={start}&end={vandaag()}",
                                   headers={"Authorization": "Bearer " + tok})
        d = json.loads(urllib.request.urlopen(r, timeout=20).read().decode())
        return {"bezoeken_7d": d.get("total", 0), "bezoekers_7d": d.get("total_unique", d.get("total", 0))}
    except Exception as e:
        print("GoatCounter niet bereikbaar:", e); return {}

def run(c):
    pag, assets, rood, geel, blauw = sitecheck.analyseer(SITE)
    ts = nu()
    uniek = {}
    for ernst, lijst in (("rood", rood), ("geel", geel), ("blauw", blauw)):
        for t in lijst:
            uniek.setdefault(fingerprint(ernst, t), (ernst, norm_tekst(t)))
    n = {e: sum(1 for x in uniek.values() if x[0] == e) for e in ("rood", "geel", "blauw")}
    score = max(0, 100 - 6 * n["rood"] - 1 * n["geel"])
    cur = c.execute("INSERT INTO runs(ts,site,score,n_rood,n_geel,n_blauw,paginas) VALUES(?,?,?,?,?,?,?)",
                    (ts, SITE, score, n["rood"], n["geel"], n["blauw"], len(pag)))
    rid = cur.lastrowid
    # findings vergelijken met vorige run
    bekend = {r["fp"]: r for r in c.execute("SELECT * FROM findings")}
    for fp, (ernst, tekst) in uniek.items():
        if fp in bekend:
            c.execute("UPDATE findings SET laatste_run=?,tekst=?,ernst=?,status='open',opgelost_run=NULL WHERE fp=?", (rid, tekst, ernst, fp))
        else:
            c.execute("INSERT INTO findings VALUES(?,?,?,?,?,?,NULL)", (fp, ernst, tekst, rid, rid, "open"))
    opgelost = [r for r in bekend.values() if r["status"] == "open" and r["fp"] not in uniek]
    for r in opgelost:
        c.execute("UPDATE findings SET status='opgelost',opgelost_run=? WHERE fp=?", (rid, r["fp"]))
        c.execute("UPDATE backlog SET status='done',klaar_op=?,notitie=COALESCE(notitie,'')||' [automatisch gemeten als opgelost]' WHERE bron=? AND status!='done'", (vandaag(), r["fp"]))
    # backlog automatisch uit nieuwe 🔴/🟡 bevindingen
    nieuw = 0
    for fp, (ernst, tekst) in uniek.items():
        if ernst == "blauw": continue
        if c.execute("SELECT 1 FROM backlog WHERE bron=?", (fp,)).fetchone(): continue
        c.execute("INSERT INTO backlog(titel,categorie,impact,moeite,wie,auto_ok,bron,aangemaakt) VALUES(?,?,?,?,?,?,?,?)",
                  (tekst[:160], "gemeten", 5 if ernst == "rood" else 3, 2, "claude", 0, fp, vandaag())); nieuw += 1
    # metrics
    def m(scope, naam, waarde): c.execute("INSERT INTO metrics(run_id,ts,scope,naam,waarde) VALUES(?,?,?,?,?)", (rid, ts, scope, naam, waarde))
    woorden, dun, artikelen, titels_lang = [], 0, 0, 0
    for u, h in pag.items():
        if not h: continue
        p = sitecheck.P(); p.feed(h)
        w = len(re.sub(r"\s+", " ", " ".join(p.txt)).split()); woorden.append(w)
        pad = norm_tekst(u) or "/"
        if "noindex" in p.m.get("robots", ""): continue
        m(pad, "woorden", w); m(pad, "titel_tekens", len(p.t.strip())); m(pad, "desc_tekens", len(p.m.get("description", "")))
        if w < 300 and not re.search(r"(404|privacy|voorwaarden|tester)", pad): dun += 1
        if len(p.t.strip()) > 60: titels_lang += 1
        if '"Article"' in "".join(p.ld): artikelen += 1
    su = sitemap_urls(); stat = [http_tijd(x) for x in su[:60]]
    kapot = sum(1 for s in stat if s[0] != 200)
    tijden = [s[1] for s in stat if s[0] == 200]
    site = {"score": score, "paginas": len(pag), "paginas_sitemap": len(su), "sitemap_kapot": kapot,
            "woorden_totaal": sum(woorden), "woorden_gemiddeld": round(statistics.mean(woorden)) if woorden else 0,
            "dunne_paginas": dun, "titels_te_lang": titels_lang, "artikelen": artikelen,
            "ttfb_mediaan_ms": round(statistics.median(tijden)) if tijden else 0,
            "html_kb_home": round((stat[0][2] if stat else 0) / 1024, 1)}
    site.update(goatcounter())
    for k, v in site.items(): m("site", k, v)
    c.commit()
    print(f"run {rid}: score {score} | 🔴{n['rood']} 🟡{n['geel']} 🔵{n['blauw']} | {len(pag)} pagina's | opgelost {len(opgelost)} | nieuw in backlog {nieuw}")
    return rid

# ---------- rapport ----------
def laatste_metric(c, naam, scope="site", n=1, voor=None):
    q = "SELECT waarde,ts FROM metrics WHERE scope=? AND naam=?" + (" AND run_id<?" if voor else "") + " ORDER BY ts DESC LIMIT ?"
    a = (scope, naam, voor, n) if voor else (scope, naam, n)
    return [r["waarde"] for r in c.execute(q, a)]

def pijl(nu_, voor):
    if voor is None: return ""
    d = nu_ - voor
    return " (±0)" if d == 0 else f" ({'+' if d > 0 else ''}{round(d, 1)})"

def report(c, uit=None):
    r = c.execute("SELECT * FROM runs ORDER BY id DESC LIMIT 1").fetchone()
    if not r: return "Nog geen meting. Draai eerst: groei.py run"
    vorige = c.execute("SELECT * FROM runs WHERE id<? ORDER BY id DESC LIMIT 1", (r["id"],)).fetchone()
    L = [f"# Groeirapport Collens Group, {r['ts'][:10]}", ""]
    L.append(f"**Score {r['score']:.0f}/100**{pijl(r['score'], vorige['score'] if vorige else None)} · 🔴 {r['n_rood']} · 🟡 {r['n_geel']} · {r['paginas']} pagina's gecontroleerd")
    L += ["", "## Kerncijfers"]
    for naam, label in [("woorden_totaal", "Woorden op de site"), ("dunne_paginas", "Dunne pagina's (<300 woorden)"), ("artikelen", "Artikelen"),
                        ("titels_te_lang", "Titels > 60 tekens"), ("paginas_sitemap", "Pagina's in sitemap"), ("sitemap_kapot", "Kapotte sitemap-links"),
                        ("ttfb_mediaan_ms", "Reactietijd mediaan (ms)"), ("bezoeken_7d", "Bezoeken laatste 7 dagen"), ("bezoekers_7d", "Unieke bezoekers 7 dagen")]:
        w = laatste_metric(c, naam, n=2)
        if w: L.append(f"- {label}: **{round(w[0], 1):g}**{pijl(w[0], w[1] if len(w) > 1 else None)}")
    if not laatste_metric(c, "bezoeken_7d"): L.append("- Bezoekers: **nog niet gemeten** (GoatCounter of Search Console is nog niet gekoppeld)")
    L += ["", "## Doelen"]
    for d in c.execute("SELECT * FROM doelen"):
        wn = {"leads_per_maand": None, "gewonnen_per_maand": None}.get(d["naam"], "x")
        if d["naam"] in ("leads_per_maand", "gewonnen_per_maand"):
            maand = vandaag()[:7]
            huidig = c.execute("SELECT COUNT(*) FROM leads WHERE datum LIKE ?" + (" AND status='gewonnen'" if d["naam"].startswith("gew") else ""), (maand + "%",)).fetchone()[0]
        else:
            w = laatste_metric(c, d["naam"]); huidig = w[0] if w else None
        L.append(f"- {d['toelichting']}: {'?' if huidig is None else round(huidig, 1):g} van {d['doel']:g} (uiterlijk {d['deadline']})" if huidig is not None else f"- {d['toelichting']}: nog niet gemeten, doel {d['doel']:g} ({d['deadline']})")
    if vorige:
        nw = c.execute("SELECT ernst,tekst FROM findings WHERE eerste_run=? AND ernst!='blauw'", (r["id"],)).fetchall()
        op = c.execute("SELECT tekst FROM findings WHERE opgelost_run=?", (r["id"],)).fetchall()
        L += ["", f"## Sinds vorige meting: {len(op)} opgelost, {len(nw)} nieuw"]
        L += [f"- ✅ {x['tekst'][:140]}" for x in op[:10]] + [f"- ⚠️ nieuw: {x['tekst'][:140]}" for x in nw[:10]]
    L += ["", "## Volgende stappen (hoogste opbrengst per moeite)"]
    for b in c.execute("SELECT * FROM backlog WHERE status IN ('todo','doing') ORDER BY impact*1.0/moeite DESC, impact DESC LIMIT 8"):
        tag = "🤖 Claude" if b["wie"] == "claude" else "👤 Jeffrey"
        L.append(f"- #{b['id']} {b['titel']} · {b['categorie']} · impact {b['impact']}/moeite {b['moeite']} · {tag}" + (f" · wacht op: {b['blokkade']}" if b["blokkade"] and b["wie"] == "jeffrey" else ""))
    kl = c.execute("SELECT titel,klaar_op FROM backlog WHERE status='done' ORDER BY klaar_op DESC LIMIT 5").fetchall()
    if kl: L += ["", "## Recent afgerond"] + [f"- {x['titel']} ({x['klaar_op']})" for x in kl]
    ex = c.execute("SELECT * FROM experiments WHERE status='loopt'").fetchall()
    if ex:
        L += ["", "## Lopende experimenten"]
        for e in ex: L.append(f"- #{e['id']} {e['hypothese']} → meten: {e['metric']}; einde {e['einde']}" + (" **(afsluiten!)**" if e["einde"] <= vandaag() else ""))
    ls = c.execute("SELECT bron,COUNT(*) n,SUM(status='gewonnen') w,COALESCE(SUM(CASE WHEN status='gewonnen' THEN waarde END),0) om FROM leads GROUP BY bron ORDER BY n DESC").fetchall()
    L += ["", "## Leads per bron"]
    L += [f"- {x['bron']}: {x['n']} leads, {x['w']} gewonnen, € {x['om']:,.0f}" for x in ls] or ["- Nog geen leads vastgelegd (leg elke echte aanvraag vast met: groei.py lead \"bron\" \"type\")"]
    lr = c.execute("SELECT datum,onderwerp,les FROM learnings ORDER BY id DESC LIMIT 5").fetchall()
    if lr: L += ["", "## Wat we geleerd hebben"] + [f"- {x['datum']} {x['onderwerp']}: {x['les']}" for x in lr]
    L += ["", "## Verloop score"]
    L.append(" → ".join(f"{x['score']:.0f}" for x in reversed(c.execute("SELECT score FROM runs ORDER BY id DESC LIMIT 8").fetchall())))
    out = "\n".join(L) + "\n"
    if uit: open(uit, "w", encoding="utf-8").write(out)
    return out

def toon_backlog(c, top):
    for b in c.execute("SELECT * FROM backlog WHERE status IN ('todo','doing') ORDER BY impact*1.0/moeite DESC, impact DESC LIMIT ?", (top,)):
        print(f"#{b['id']:>3} [{b['status']}] i{b['impact']} m{b['moeite']} {'auto' if b['auto_ok'] else '    '} {b['wie']:<7} {b['titel'][:90]}" + (f"  (wacht op: {b['blokkade']})" if b['blokkade'] else ""))

def main():
    ap = argparse.ArgumentParser(); ap.add_argument("cmd"); ap.add_argument("args", nargs="*")
    ap.add_argument("--out"); ap.add_argument("--top", type=int, default=12); ap.add_argument("--cat", default="algemeen")
    ap.add_argument("--impact", type=int, default=3); ap.add_argument("--moeite", type=int, default=3); ap.add_argument("--wie", default="claude")
    ap.add_argument("--auto", action="store_true"); ap.add_argument("--bewijs", default=""); ap.add_argument("--dagen", type=int, default=14)
    ap.add_argument("--waarde", type=float, default=0); ap.add_argument("--status", default="nieuw"); ap.add_argument("--scope", default="site")
    a = ap.parse_args(); cmd = a.cmd
    if cmd == "restore":
        if os.path.exists(DB): os.remove(DB)
        c = sqlite3.connect(DB); c.executescript(open(a.args[0], encoding="utf-8").read()); c.commit(); print("hersteld uit", a.args[0]); return
    c = verbind()
    if cmd == "init": init(c)
    elif cmd == "run": init(c); run(c)
    elif cmd == "report": print(report(c, a.out))
    elif cmd == "backlog": toon_backlog(c, a.top)
    elif cmd == "klaar":
        c.execute("UPDATE backlog SET status='done',klaar_op=?,notitie=? WHERE id=?", (vandaag(), a.args[1] if len(a.args) > 1 else "", int(a.args[0]))); c.commit(); print("afgerond")
    elif cmd == "nieuw":
        c.execute("INSERT INTO backlog(titel,categorie,impact,moeite,wie,auto_ok,bron,aangemaakt) VALUES(?,?,?,?,?,?,?,?)", (a.args[0], a.cat, a.impact, a.moeite, a.wie, int(a.auto), "handmatig", vandaag())); c.commit(); print("toegevoegd")
    elif cmd == "leer":
        c.execute("INSERT INTO learnings(datum,onderwerp,les,bewijs) VALUES(?,?,?,?)", (vandaag(), a.args[0], a.args[1], a.bewijs)); c.commit(); print("les opgeslagen")
    elif cmd == "exp":
        base = laatste_metric(c, a.args[2]); eind = (datetime.date.today() + datetime.timedelta(days=a.dagen)).isoformat()
        c.execute("INSERT INTO experiments(hypothese,wijziging,metric,baseline,start,einde) VALUES(?,?,?,?,?,?)", (a.args[0], a.args[1], a.args[2], base[0] if base else None, vandaag(), eind)); c.commit(); print("experiment gestart, einde", eind)
    elif cmd == "exp-sluit":
        c.execute("UPDATE experiments SET status='klaar',resultaat=?,les=? WHERE id=?", (a.args[1], a.args[2], int(a.args[0])))
        c.execute("INSERT INTO learnings(datum,onderwerp,les,bewijs) VALUES(?,?,?,?)", (vandaag(), "experiment " + a.args[0], a.args[2], a.args[1])); c.commit(); print("experiment gesloten, les opgeslagen")
    elif cmd == "lead":
        c.execute("INSERT INTO leads(datum,bron,type,status,waarde) VALUES(?,?,?,?,?)", (vandaag(), a.args[0], a.args[1], a.status, a.waarde)); c.commit(); print("lead vastgelegd")
    elif cmd == "metric":
        c.execute("INSERT INTO metrics(run_id,ts,scope,naam,waarde) VALUES(NULL,?,?,?,?)", (nu(), a.scope, a.args[0], float(a.args[1]))); c.commit(); print("meting opgeslagen")
    elif cmd == "doel":
        c.execute("INSERT OR REPLACE INTO doelen VALUES(?,?,?,?)", (a.args[0], float(a.args[1]), a.args[2], a.args[3] if len(a.args) > 3 else a.args[0])); c.commit(); print("doel gezet")
    elif cmd == "dump":
        open(a.args[0], "w", encoding="utf-8").write("\n".join(c.iterdump()) + "\n"); print("database geschreven naar", a.args[0])
    else: sys.exit(__doc__)

if __name__ == "__main__":
    main()
