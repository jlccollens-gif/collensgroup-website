"""Maakt het zelfstandige pakket voor Kim: haar eigen webshop zonder enige koppeling met Collens Group.
Uitvoer: /home/claude/export/suismuis-webshop/{website,server,HANDLEIDING.md}
Gebruik: python3 tools/suismuis_live/export.py  (na python3 build.py)"""
import glob, json, os, re, shutil

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
BRON = os.path.join(ROOT, "dist", "concept", "suismuis")
UIT = "/home/claude/export/suismuis-webshop"
WEB = os.path.join(UIT, "website")

shutil.rmtree(UIT, ignore_errors=True)
os.makedirs(os.path.join(WEB, "assets")); os.makedirs(os.path.join(UIT, "server"))

# ---------- producten die echt in de shop staan ----------
s = open(os.path.join(BRON, "assets", "scouting.js"), encoding="utf-8").read()
data = json.loads(s[s.index("["):s.rindex("]") + 1])
js = open(os.path.join(BRON, "assets", "suismuis.js"), encoding="utf-8").read()
weg = {int(x) for x in re.search(r"var WEG = \[([0-9,\s]*)\]", js).group(1).split(",") if x.strip()}
actief = json.dumps([p for p in data if p.get("nr") not in weg])

# ---------- html opschonen ----------
tekst_alles = ""
for f in [x for x in glob.glob(os.path.join(BRON, "*.html")) if not x.endswith("account.html")]:
    h = open(f, encoding="utf-8").read()
    h = re.sub(r'<div class="wm alleen-concept"[^>]*></div>\n?', "", h)
    h = re.sub(r'<li class="alleen-concept">.*?</li>', "", h)
    h = re.sub(r'<div class="concept alleen-concept">.*?</div>\n?', "", h)
    h = re.sub(r'<meta name="robots"[^>]*>', '<meta name="robots" content="noindex">' if f.endswith(("beheer.html", "afrekenen.html")) else "", h)
    h = re.sub(r'<meta name="generator"[^>]*>|<meta name="copyright"[^>]*>', "", h)
    h = re.sub(r'<meta property="og:image"[^>]*>', "", h)
    h = h.replace(" (concept)", "")
    h = h.replace('<script src="assets/scouting.js', '<script src="assets/instellingen.js"></script><script src="assets/scouting.js')
    h = h.replace("-m.jpg", ".jpg")  # alleen de grote foto's meenemen (minder bestanden)
    h = re.sub(r"\n{2,}", "\n", h)
    assert "collens" not in h.lower(), f
    open(os.path.join(WEB, os.path.basename(f)), "w", encoding="utf-8").write(h)
    tekst_alles += h

# ---------- assets ----------
for n in ("suismuis.css", "scouting.js", "favicon.svg"):
    shutil.copy(os.path.join(BRON, "assets", n), os.path.join(WEB, "assets", n))
js2 = js
js2 = re.sub(r"var WEG = \[[0-9,\s]*\];[^\n]*", "var WEG = [];", js2)
js2 = re.sub(r"var GRATIS = [0-9.]+, VERZEND = [0-9.]+, CADEAU = [0-9.]+;", "var K = window.SUIS_KOSTEN || {}, GRATIS = K.gratis, VERZEND = K.verzend, CADEAU = K.cadeau;", js2)
js2 = re.sub(r'  var API = "https://[^"]+";', '  var API = window.SUIS_API || "";', js2)
js2 = js2.replace("/* Suismuis Home – webshop (Collens Group).", "/* Suismuis Home – webshop.")
js2 = js2.replace('(groot ? "" : "-m")', '""').replace("'-m.jpg", "'.jpg").replace("-m.jpg 1080w, img/", ".jpg 1080w, img/")
assert "collens" not in js2.lower() and "eyrfizayagcwaxbxyeuh" not in js2
open(os.path.join(WEB, "assets", "suismuis.js"), "w", encoding="utf-8").write(js2)
css = open(os.path.join(BRON, "assets", "suismuis.css"), encoding="utf-8").read()
css = re.sub(r'--wm:url\("[^"]*"\)', '--wm:none', css).replace("-m.jpg", ".jpg")
open(os.path.join(WEB, "assets", "suismuis.css"), "w", encoding="utf-8").write(css)
sc = open(os.path.join(WEB, "assets", "scouting.js"), encoding="utf-8").read()
sc = sc.replace("Productselectie voor de conceptversie van Suismuis Home (Collens Group).", "Producten van Suismuis Home. Hier staan alle producten en prijzen; de betaalserver rekent met precies deze prijzen.")
sc = sc.replace("inkoopgegevens horen niet in deze publieke versie.", "zet hier nooit inkoopprijzen in (dit bestand is openbaar).")
_lijst = [p for p in json.loads(sc[sc.index("["):sc.rindex("]") + 1]) if p.get("nr") not in weg]
_kop = sc[:sc.index("[")]
_k = re.search(r"var GRATIS = ([0-9.]+), VERZEND = ([0-9.]+), CADEAU = ([0-9.]+);", js)
sc = _kop + json.dumps(_lijst, ensure_ascii=False, separators=(",", ":")) + ";\n/* Verzendkosten: gratis vanaf, verzendkosten, cadeauverpakking (in euro) */\nwindow.SUIS_KOSTEN = " + json.dumps({"gratis": float(_k.group(1)), "verzend": float(_k.group(2)), "cadeau": float(_k.group(3))}) + ";\n"
open(os.path.join(WEB, "assets", "scouting.js"), "w", encoding="utf-8").write(sc)
open(os.path.join(WEB, "assets", "instellingen.js"), "w", encoding="utf-8").write(
    '/* STAP 3 VAN DE HANDLEIDING: vervang JOUW-PROJECT door de code van je eigen Supabase-project. */\n'
    'window.SUIS_API = "https://JOUW-PROJECT.supabase.co/functions/v1/suismuis";\n')
tekst_alles += css + re.sub(r"var P = \[.*?\n  \];", "", js2, flags=re.S)  # oude voorbeeldproducten in de code tellen niet mee

# ---------- alleen gebruikte afbeeldingen ----------
n = 0
for f in glob.glob(os.path.join(BRON, "img", "**", "*.*"), recursive=True):
    rel = os.path.relpath(f, os.path.join(BRON, "img")).replace(os.sep, "/")
    if rel.endswith("-m.jpg") or rel == "og.jpg":
        continue
    stem = re.sub(r"\.(jpg|png|webp|svg)$", "", rel)
    if ("img/" + rel) in tekst_alles or ("img/" + rel) in actief or stem in tekst_alles or stem in actief:
        os.makedirs(os.path.dirname(os.path.join(WEB, "img", rel)), exist_ok=True)
        shutil.copy(f, os.path.join(WEB, "img", rel)); n += 1
# grote versie ontbreekt soms naast -m: dan de -m-versie onder de grote naam
for ref in set(re.findall(r"img/[A-Za-z0-9_./-]+\.jpg", tekst_alles + actief)):
    doel = os.path.join(WEB, ref)
    if not os.path.exists(doel):
        m = os.path.join(BRON, ref[:-4] + "-m.jpg")
        if os.path.exists(m):
            os.makedirs(os.path.dirname(doel), exist_ok=True); shutil.copy(m, doel); n += 1

open(os.path.join(WEB, "_headers"), "w").write(
    "/*\n  Strict-Transport-Security: max-age=31536000; includeSubDomains\n  X-Content-Type-Options: nosniff\n  X-Frame-Options: SAMEORIGIN\n  Referrer-Policy: strict-origin-when-cross-origin\n"
    "/*.html\n  Cache-Control: no-cache\n/assets/*\n  Cache-Control: no-cache\n/img/*\n  Cache-Control: public, max-age=604800\n/beheer.html\n  X-Robots-Tag: noindex\n")
open(os.path.join(WEB, "robots.txt"), "w").write("User-agent: *\nAllow: /\nDisallow: /beheer.html\nDisallow: /afrekenen.html\n")

# ---------- server ----------
fn = open(os.path.join(ROOT, "tools", "suismuis_live", "functie", "index.ts"), encoding="utf-8").read()
fn = fn.replace("Gebouwd door Collens Group.", "")
fn = re.sub(r'env\("SUISMUIS_CATALOGUS", "[^"]*"\)', 'env("SUISMUIS_SITE").replace(/\\/$/, "") + "/assets/scouting.js"', fn)
fn = re.sub(r'env\("SUISMUIS_IBAN", "[^"]*"\)', 'env("SUISMUIS_IBAN")', fn)
fn = re.sub(r'env\("SUISMUIS_KIM_EMAIL", "[^"]*"\)', 'env("SUISMUIS_KIM_EMAIL")', fn)
fn = re.sub(r'env\("SUISMUIS_AFZENDER", "[^"]*"\)', 'env("SUISMUIS_AFZENDER", env("SUISMUIS_KIM_EMAIL"))', fn)
fn = fn.replace('"https://collensgroup.com/concept/suismuis"', 'env("SUISMUIS_SITE").replace(/\\/$/, "")')
assert "collens" not in fn.lower(), [l for l in fn.splitlines() if "collens" in l.lower()]
open(os.path.join(UIT, "server", "2-functie-suismuis.ts"), "w", encoding="utf-8").write(fn)
sql = open(os.path.join(ROOT, "tools", "suismuis_live", "database.sql"), encoding="utf-8").read().rstrip() + "\n\n" + open(os.path.join(ROOT, "tools", "suismuis_live", "leveranciers.sql"), encoding="utf-8").read()
assert "collens" not in sql.lower()
open(os.path.join(UIT, "server", "1-database.sql"), "w", encoding="utf-8").write(sql)
ci = open(os.path.join(ROOT, "tools", "suismuis_live", "CLAUDE-INSTRUCTIES.md"), encoding="utf-8").read()
assert "collens" not in ci.lower()
open(os.path.join(UIT, "CLAUDE-INSTRUCTIES.md"), "w", encoding="utf-8").write(ci)
shutil.copy(os.path.join(ROOT, "tools", "suismuis_live", "HANDLEIDING.html"), os.path.join(UIT, "HANDLEIDING.html"))

# ---------- productfoto's verdelen over twee Cloudflare-projecten (max 1000 bestanden per keer slepen) ----------
FOTOS = os.path.join(UIT, "fotos")
SC = os.path.join(WEB, "img", "sc")
os.makedirs(os.path.join(FOTOS, "img", "sc"))
overig = sum(len(fs) for _, _, fs in os.walk(WEB)) - len(os.listdir(SC))
groepen = {}
for f in os.listdir(SC):
    groepen.setdefault(int(re.match(r"\d+", f).group()), []).append(f)
plaats, naar_b = overig, []
for nr in sorted(groepen):
    if plaats + len(groepen[nr]) <= 900: plaats += len(groepen[nr])
    else:
        naar_b.append(nr)
        for f in groepen[nr]: shutil.move(os.path.join(SC, f), os.path.join(FOTOS, "img", "sc", f))
open(os.path.join(FOTOS, "_headers"), "w").write("/*\n  Cache-Control: public, max-age=604800\n  X-Robots-Tag: noindex\n")
open(os.path.join(FOTOS, "index.html"), "w").write('<!doctype html><meta charset="utf-8"><title>Suismuis Home</title><meta name="robots" content="noindex"><p>Foto\'s van Suismuis Home.</p>')
open(os.path.join(WEB, "assets", "scouting.js"), "a", encoding="utf-8").write(
    "/* De foto's van deze productnummers staan in je tweede Cloudflare-project (adres in instellingen.js). */\n"
    "(function(){var B=window.SUIS_FOTOS||\"\",N=" + json.dumps(naar_b) + ";if(!B||/JOUW-/.test(B))return;B=B.replace(/\\/?$/,\"/\");"
    "function f(x){return typeof x===\"string\"&&x.indexOf(\"img/sc/\")===0&&N.indexOf(parseInt(x.slice(7),10))>-1?B+x:x}"
    "(window.SUIS_EXTRA||[]).forEach(function(p){if(p.u)p.u=p.u.map(f);p.img=f(p.img);(p.var||[]).forEach(function(v){v.b=f(v.b)})})})();\n")
open(os.path.join(WEB, "assets", "instellingen.js"), "a", encoding="utf-8").write(
    '/* STAP 5 VAN DE HANDLEIDING: het adres van je fotoproject bij Cloudflare. */\n'
    'window.SUIS_FOTOS = "https://JOUW-FOTOPROJECT.pages.dev";\n')
aantal = sum(len(fs) for _, _, fs in os.walk(WEB)); aantal_f = sum(len(fs) for _, _, fs in os.walk(FOTOS))
print(f"website: {aantal} bestanden, fotos: {aantal_f} bestanden ({len(naar_b)} producten)")
assert aantal <= 1000 and aantal_f <= 1000, "te veel bestanden voor slepen-en-neerzetten bij Cloudflare (max 1000)"

# ---------- foto's lichter maken (zelfde afmetingen, max 2400 px) ----------
from PIL import Image
import io
for f in glob.glob(os.path.join(WEB, "img", "**", "*.jpg"), recursive=True) + glob.glob(os.path.join(UIT, "fotos", "img", "**", "*.jpg"), recursive=True):
    s0 = os.path.getsize(f); im = Image.open(f)
    im = im.convert("RGB") if im.mode != "RGB" else im
    if max(im.size) > 2400: im.thumbnail((2400, 2400))
    b = io.BytesIO(); im.save(b, "JPEG", quality=84, optimize=True, progressive=True)
    if b.tell() < s0 * 0.92: open(f, "wb").write(b.getvalue())
shutil.make_archive(UIT, "zip", os.path.dirname(UIT), os.path.basename(UIT))
print("zip:", UIT + ".zip")
