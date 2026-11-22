"""Backlink-database en -controle voor collensgroup.com (gratis, lokaal, SQLite).

Gebruik:
  BL_DB=pad.db python3 -I backlinks.py init
  BL_DB=pad.db python3 -I backlinks.py add <bron_url> <doel_url> <soort> [status] [notitie]
      soort: vermelding | klantsite | redactioneel | forum | social | eigen
      status: idee (standaard) | aangevraagd | live | weg
  BL_DB=pad.db python3 -I backlinks.py check      # controleert alle 'live' en 'aangevraagd' links
  BL_DB=pad.db python3 -I backlinks.py report     # overzicht in Markdown
  BL_DB=pad.db python3 -I backlinks.py import-gsc <csv>  # Search Console > Links > Top linkende sites (export)
Regels: alleen echte, verdiende links. Nooit kopen, ruilen of spammen (Google spam policies).
"""
import csv, datetime, os, re, sqlite3, subprocess, sys
from urllib.parse import urlparse

DB = os.environ.get("BL_DB", os.path.join(os.path.dirname(os.path.abspath(__file__)), "backlinks.db"))
ONS = "collensgroup.com"


def db():
    c = sqlite3.connect(DB)
    c.execute("""create table if not exists backlinks(
        id integer primary key, bron_url text unique, bron_domein text, doel_url text,
        ankertekst text default '', soort text, follow text default '?', status text default 'idee',
        datum_live text default '', laatst_gecontroleerd text default '', notitie text default '')""")
    c.execute("""create table if not exists verwijzende_domeinen(
        domein text primary key, links integer, bron text, datum text)""")
    return c


def vandaag():
    return datetime.date.today().isoformat()


def haal(url):
    r = subprocess.run(["curl", "-sL", "--max-time", "25", "-A", "Mozilla/5.0 (CollensGroup backlink-check)", url],
                       capture_output=True)
    return r.stdout.decode("utf8", "replace")


def vind_link(html):
    """Zoek <a ... href="...collensgroup.com..."> en geef (ankertekst, follow) of None."""
    for m in re.finditer(r'<a\b([^>]*href=["\'][^"\']*' + re.escape(ONS) + r'[^"\']*["\'][^>]*)>(.*?)</a>', html, re.S | re.I):
        attrs, tekst = m.group(1), re.sub(r"<[^>]+>", "", m.group(2)).strip()
        rel = re.search(r'rel=["\']([^"\']*)', attrs, re.I)
        follow = "nofollow" if rel and re.search(r"nofollow|ugc|sponsored", rel.group(1), re.I) else "follow"
        return tekst[:120], follow
    return None


def cmd_add(args):
    bron, doel, soort = args[:3]
    status = args[3] if len(args) > 3 else "idee"
    notitie = args[4] if len(args) > 4 else ""
    c = db()
    c.execute("insert or ignore into backlinks(bron_url,bron_domein,doel_url,soort,status,notitie) values(?,?,?,?,?,?)",
              (bron, urlparse(bron).netloc.lower().removeprefix("www."), doel, soort, status, notitie))
    c.commit()
    print("toegevoegd:", bron)


def cmd_check(_):
    c = db()
    rijen = c.execute("select id,bron_url,status,datum_live from backlinks where status in ('live','aangevraagd')").fetchall()
    for i, url, status, live in rijen:
        res = vind_link(haal(url))
        if res:
            anker, follow = res
            nieuw = "live"
            live = live or vandaag()
        else:
            anker, follow = "", "?"
            nieuw = "weg" if status == "live" else "aangevraagd"
        c.execute("update backlinks set status=?, ankertekst=?, follow=?, datum_live=?, laatst_gecontroleerd=? where id=?",
                  (nieuw, anker, follow, live, vandaag(), i))
        print(f"{nieuw:11} {follow:8} {url}")
    c.commit()


def cmd_import_gsc(args):
    c = db()
    n = 0
    with open(args[0], newline="", encoding="utf8") as f:
        for rij in csv.reader(f):
            if len(rij) < 2 or not rij[1].strip().isdigit():
                continue
            c.execute("insert or replace into verwijzende_domeinen values(?,?,?,?)",
                      (rij[0].strip().lower(), int(rij[1]), "search-console", vandaag()))
            n += 1
    c.commit()
    print(n, "verwijzende domeinen ingelezen")


def cmd_report(_):
    c = db()
    print(f"# Backlinks collensgroup.com – {vandaag()}\n")
    for status in ("live", "aangevraagd", "idee", "weg"):
        rijen = c.execute("select bron_url,soort,follow,ankertekst,notitie from backlinks where status=? order by soort", (status,)).fetchall()
        print(f"## {status} ({len(rijen)})")
        for r in rijen:
            print(f"- {r[0]} · {r[1]} · {r[2]} · {r[3] or '-'} · {r[4]}")
        print()
    d = c.execute("select count(*) from verwijzende_domeinen").fetchone()[0]
    print(f"Verwijzende domeinen volgens Search Console: {d if d else 'nog niet ingelezen'}")


if __name__ == "__main__":
    cmds = {"init": lambda a: (db(), print("ok", DB)), "add": cmd_add, "check": cmd_check,
            "report": cmd_report, "import-gsc": cmd_import_gsc}
    if len(sys.argv) < 2 or sys.argv[1] not in cmds:
        print(__doc__)
        sys.exit(1)
    cmds[sys.argv[1]](sys.argv[2:])
