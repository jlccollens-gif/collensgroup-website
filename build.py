#!/usr/bin/env python3
"""Collens Group website generator.
Bewerk CONFIG en APPS, run `python3 build.py`, de site staat in ./dist.
"""
import json, os, shutil, html, datetime
from talen import TALEN, taal_paginas

ROOT = os.path.dirname(os.path.abspath(__file__))
DIST = os.path.join(ROOT, "dist")

CONFIG = {
    "naam": "Collens Group",
    "base_url": os.environ.get("BASE_URL", "https://collensgroup.com").rstrip("/"),   # gekozen domein
    "email": "jlccollens@gmail.com",  # contactadres op de site
    "whatsapp": "",         # bv. 31612345678
    "gsc_verificatie": "",  # Google Search Console HTML-tag content-waarde
    "goatcounter": "",      # bv. lanceerbaan  -> https://lanceerbaan.goatcounter.com (cookieloos, gratis)
    "kvk": "",              # KvK-nummer, tonen in footer zodra bekend
}
VANDAAG = datetime.date.today().isoformat()
import hashlib
CSS_V = hashlib.md5(open(os.path.join(ROOT, 'src', 'site.css'), 'rb').read()).hexdigest()[:8]

# Eigen apps. Alleen apps met publiceer=True komen op de site.
LUBBYC_PRIVACY = '''<p>Laatst bijgewerkt: 14-11-2026. Contact: <a href="mailto:collens-inc@outlook.com">collens-inc@outlook.com</a>.</p>
<h3>Welke gegevens</h3>
<ul>
<li><strong>Account:</strong> naam, e-mailadres en gebruikers-ID (verplicht, voor je account).</li>
<li><strong>Profiel (optioneel):</strong> geboortejaar, land, bio, interesses en profielfoto.</li>
<li><strong>Wat je zelf maakt:</strong> plannen, berichten in groeps- en evenementenchats, recensies en foto's.</li>
<li><strong>Locatie (optioneel):</strong> alleen terwijl je de app gebruikt, om de kaart en plekken rond jou te tonen, en om je reisroute vast te leggen als je dat zelf aanzet. Je exacte locatie wordt nooit aan andere gebruikers getoond.</li>
<li><strong>Apparaat-ID:</strong> alleen om misbruik van de gratis proefperiode te voorkomen.</li>
</ul>
<h3>Waarvoor</h3>
<p>Alleen om de app te laten werken: je account, plannen maken en aansluiten, chatten, de kaart en de reisgids. We verkopen je gegevens niet en tonen geen advertenties.</p>
<h3>Met wie</h3>
<p>Je gegevens staan bij onze databasedienst Supabase (verwerker). Vraag je plekken in de buurt op, dan gaat je locatie op dat moment naar openbare kaartdiensten (OpenFreeMap, Overpass) om die plekken op te halen. Andere gebruikers zien alleen wat jij in je profiel en plannen deelt; basisleden zien minder profielgegevens dan Premium-leden.</p>
<h3>Bewaren en verwijderen</h3>
<p>Gegevens worden versleuteld verstuurd. Je kunt je account en gegevens laten verwijderen in de app of via <a href="mailto:collens-inc@outlook.com">collens-inc@outlook.com</a>.</p>
<h3>Leeftijd</h3>
<p>LubbyC is alleen voor volwassenen (18+).</p>
<h3>Je rechten</h3>
<p>Je kunt inzage, correctie of verwijdering vragen via het e-mailadres hierboven, en een klacht indienen bij de Autoriteit Persoonsgegevens.</p>'''

# Eigen apps, games en projecten. Alleen items met publiceer=True komen op de site.
APPS = [
    {
        "slug": "lubbyc", "naam": "LubbyC", "soort": "App", "kleur": "#0E4433", "letter": "L", "icoon": "img/lubbyc-icon.png", "publiceer": True,
        "kort": "Ontmoet reizigers in de buurt en plan samen eten, strand of een tour in Thailand.",
        "titel": "LubbyC – samen reizen in Thailand: ontmoet reizigers in de buurt",
        "kop": "Alleen op reis, maar niet alleen eten vanavond.",
        "intro": "LubbyC verbindt reizigers die op dezelfde plek zijn en hetzelfde willen doen. Open de kaart, zie wat mensen in de buurt van plan zijn en sluit aan, of maak zelf een plan. We starten in Krabi en Ao Nang, Phuket, Pattaya en Bangkok.",
        "kenmerken": ["Plannen in de buurt op de kaart: eten, strand, dagtrips, tempels", "In een paar tikken zelf een plan maken", "Groepschat zodra je bent geaccepteerd", "Reisgids, weer en plekken in de buurt", "Noodhulp met één tik", "In 12 talen"],
        "beelden": [("img/lubbyc-kaart.jpg", "Kaart met plannen in de buurt"), ("img/lubbyc-evenementen.jpg", "Feesten en evenementen"), ("img/lubbyc-ontdekken.jpg", "Ontdekken"), ("img/lubbyc-noodhulp.jpg", "Noodhulp")],
        "status": "Binnenkort in Google Play",
        "categorie": "TravelApplication", "schema": "MobileApplication",
        "appstore": "", "playstore": "",
        "privacy": LUBBYC_PRIVACY,
    },
    {
        "slug": "koffer-vol", "naam": "Koffer Vol!", "soort": "Game", "kleur": "#1F7A70", "letter": "🧳", "icoon": "img/koffervol-icon.png", "publiceer": True,
        "kort": "Pak de juiste spullen in voor elke reis. Een slimme, vrolijke inpakpuzzel met 100 levels in 10 landen.",
        "titel": "Koffer Vol! – inpakpuzzel met 100 levels in 10 landen",
        "kop": "Past alles in de koffer?",
        "intro": "Koffer Vol! is een vrolijke puzzelgame: pak voor elke reis precies de juiste spullen in. 100 levels, verspreid over 10 landen, in 12 talen. Een game van het team achter LubbyC.",
        "kenmerken": ["100 levels in 10 landen, van Thailand tot Japan en Italië", "Kies de juiste spullen voor weer en activiteiten, en laat alles passen", "Sterren, munten en een ansichtkaart per bestemming", "Avatars vrijspelen in de winkel", "In 12 talen"],
        "beelden": [("img/koffer-spel.jpg", "Inpakken in Kyoto"), ("img/koffer-gewonnen.jpg", "Koffer dicht!"), ("img/koffer-fout.jpg", "Uitleg bij foute keuzes"), ("img/koffer-winkel.jpg", "Avatars in de winkel")],
        "status": "Binnenkort in Google Play",
        "categorie": "GameApplication", "schema": "VideoGame",
        "appstore": "", "playstore": "",
        "privacy": "",
    },
    {
        "slug": "eiland-express", "naam": "Eiland Express", "soort": "Game", "kleur": "#0F766E", "letter": "E", "icoon": "img/eiland-icon.jpg", "publiceer": True,
        "kort": "Rij je songthaew over een tropisch eiland en breng passagiers heelhuids naar hun halte.",
        "titel": "Eiland Express – 3D-rijgame met een songthaew op een tropisch eiland",
        "kop": "Rij je songthaew over het eiland.",
        "intro": "Eiland Express is een vrolijke 3D-rijgame. Je bestuurt een songthaew, de open taxi-pick-up uit Thailand, over kronkelende wegen langs het strand en door de heuvels. Pik passagiers op, breng ze heelhuids naar hun halte en verdien munten. Een game van het team achter LubbyC en Koffer Vol! In het Engels heet hij Island Express.",
        "kenmerken": ["3D-rijden over een tropisch eiland", "Passagiers ophalen en afzetten bij haltes", "Munten verdienen en je beste dienst verbeteren", "Kies de kleur van je songthaew"],
        "beelden": [("img/eiland-menu.jpg", "Startscherm"), ("img/eiland-rood.jpg", "Langs de kust"), ("img/eiland-groen.jpg", "Door de heuvels"), ("img/eiland-weg.jpg", "Bij de halte")],
        "video": ("img/eiland-express.mp4", "img/eiland-poster.jpg"),
        "status": "In ontwikkeling",
        "categorie": "GameApplication", "schema": "VideoGame",
        "appstore": "", "playstore": "",
        "privacy": "",
    },
    {
        "slug": "manu-en-khanun", "naam": "Manu en Khanun", "soort": "Kinderserie", "kleur": "#B45309", "letter": "M", "icoon": "img/manu-icon.jpg", "publiceer": True,
        "kort": "Animatieserie voor kinderen: een Nederlandse jongen en een babyolifant in het noorden van Thailand.",
        "titel": "Manu en Khanun – animatieserie voor kinderen in Thailand",
        "kop": "Een jongen uit Nederland. Een olifant in het klooster.",
        "intro": "Manu verhuist met zijn vader en broertje Leon naar een klein dorp tussen de rijstvelden in het noorden van Thailand. Alles is daar anders, tot hij in het bamboebos Khanun ontmoet, een babyolifant uit het klooster. Een serie over vriendschap en een nieuwe cultuur ontdekken, gemaakt met AI-animatie.",
        "kenmerken": ["Animatieserie voor kinderen, in het Nederlands", "Over vriendschap, Thailand en een nieuwe cultuur", "Gemaakt met AI-beeld, -stem en -muziek"],
        "beelden": [("img/manu-en-khanun.jpg", "Manu en Khanun in de rijstvelden"), ("img/manu-personages.jpg", "De personages"), ("img/manu-lantaarnfeest.jpg", "Lantaarnfeest")],
        "status": "In productie",
        "categorie": "", "schema": "CreativeWorkSeries",
        "appstore": "", "playstore": "",
        "privacy": "",
    },
]

FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
         '<link href="https://fonts.googleapis.com/css2?family=Atkinson+Hyperlegible:wght@400;700&family=Bricolage+Grotesque:opsz,wdth,wght@12..96,75..100,600..800&display=swap" rel="stylesheet">')
LOGO = ('<svg width="30" height="30" viewBox="0 0 30 30" aria-hidden="true"><rect width="30" height="30" rx="8" fill="#14213D"/>'
        '<rect x="13.5" y="4" width="3" height="5" rx="1" fill="#F2B705"/><rect x="13.5" y="12" width="3" height="5" rx="1" fill="#F2B705"/>'
        '<rect x="13.5" y="20" width="3" height="6" rx="1" fill="#F2B705"/></svg>')

def e(s): return html.escape(s, quote=True)

def abs_url(path):
    # Cloudflare Pages serveert pagina's zonder .html (308-redirect); canonical en sitemap wijzen direct naar die URL
    clean = "" if path == "index.html" else (path[:-5] if path.endswith(".html") else path)
    return f'{CONFIG["base_url"]}/{clean}' if CONFIG["base_url"] else ""

def ld(obj): return '<script type="application/ld+json">' + json.dumps(obj, ensure_ascii=False) + '</script>'

ORG = {"@type": "ProfessionalService", "@id": "#org", "name": CONFIG["naam"],
       "description": "Websites, apps, games en AI-automatisering tegen vaste prijzen onder het marktgemiddelde.",
       "areaServed": [{"@type": "Country", "name": "Nederland"}, {"@type": "Country", "name": "België"}],
       "priceRange": "€395 – €13.050+", "knowsLanguage": ["nl", "en"]}

GLOBE = '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3c2.5 2.7 3.8 5.7 3.8 9s-1.3 6.3-3.8 9c-2.5-2.7-3.8-5.7-3.8-9S9.5 5.7 12 3z"/></svg>'
NL_NAAR_EN = {"website-laten-maken.html": "en-website-design.html", "goedkope-website-laten-maken.html": "en-website-design.html", "webshop-laten-maken.html": "en-website-design.html",
              "app-laten-maken-kosten.html": "en-app-development.html", "mvp-app-laten-maken.html": "en-app-development.html",
              "apps.html": "en-projects.html", "app-lubbyc.html": "en-projects.html", "app-koffer-vol.html": "en-projects.html", "app-eiland-express.html": "en-projects.html", "app-manu-en-khanun.html": "en-projects.html"}
EN_NAAR_NL = {"en-website-design.html": "website-laten-maken.html", "en-app-development.html": "app-laten-maken-kosten.html", "en-projects.html": "apps.html", "en-lubbyc-privacy.html": "app-lubbyc.html"}

SNEL_JS = """<script>(()=>{document.querySelectorAll('details.snel,details.taalkeuze').forEach(d=>{document.addEventListener('click',e=>{if(d.open&&!d.contains(e.target))d.open=false});document.addEventListener('keydown',e=>{if(e.key==='Escape'&&d.open){d.open=false;d.querySelector('summary').focus()}});d.querySelectorAll('nav a').forEach(a=>a.addEventListener('click',()=>{d.open=false}))})})();</script>"""

def page(path, title, desc, body, crumbs=None, extra_ld=None, extra_head="", lang="nl", alt=None):
    url = abs_url(path)
    if lang == "en":
        taal_href = alt[0] if alt else EN_NAAR_NL.get(path, "index.html")
    else:
        taal_href = alt[1] if alt else NL_NAAR_EN.get(path, "en.html")
    from talen import TALEN
    doel = {"nl": path if lang == "nl" else (taal_href if lang == "en" else "index.html"),
            "en": path if lang == "en" else (taal_href if lang == "nl" else "en.html")}
    for c in TALEN: doel[c] = f"{c}.html"
    namen = {"nl": "Nederlands", "en": "English", **{c: T["naam"] for c, T in TALEN.items()}}
    taal_menu = ('<details class="taalkeuze"><summary aria-label="Taal / Language">' + GLOBE + f'<span>{lang.upper()}</span></summary><nav class="taal-paneel">' +
                 "".join(f'<a href="{doel[c]}" hreflang="{c}" lang="{c}"{" aria-current=\"true\"" if c == lang else ""}>{namen[c]}</a>' for c in namen) + '</nav></details>')
    head = [f'<!DOCTYPE html><html lang="{lang}"><head><meta charset="utf-8">',
            '<meta name="viewport" content="width=device-width, initial-scale=1">',
            f'<title>{e(title)}</title><meta name="description" content="{e(desc)}">',
            '<meta name="theme-color" content="#14213D"><link rel="icon" href="favicon.svg" type="image/svg+xml">',
            f'<meta property="og:type" content="website"><meta property="og:locale" content="{ {"en": "en_US", "nl": "nl_NL", "de": "de_DE", "fr": "fr_FR", "es": "es_ES"}.get(lang, "nl_NL") }"><meta property="og:site_name" content="{CONFIG["naam"]}">',
            f'<meta property="og:title" content="{e(title)}"><meta property="og:description" content="{e(desc)}">',
            '<meta name="twitter:card" content="summary_large_image">']
    if url:
        head.append(f'<link rel="canonical" href="{url}"><meta property="og:url" content="{url}">')
        head.append(f'<meta property="og:image" content="{CONFIG["base_url"]}/og.png">')
    HOMES = {"nl": "index.html", "en": "en.html", "de": "de.html", "fr": "fr.html", "es": "es.html"}
    if path in HOMES.values() and CONFIG["base_url"]:
        head.append("".join(f'<link rel="alternate" hreflang="{c}" href="{abs_url(p)}">' for c, p in HOMES.items()) + f'<link rel="alternate" hreflang="x-default" href="{abs_url("en.html")}">')
    elif alt and CONFIG["base_url"]:
        nl_p, en_p = alt
        head.append(f'<link rel="alternate" hreflang="nl" href="{abs_url(nl_p)}"><link rel="alternate" hreflang="en" href="{abs_url(en_p)}"><link rel="alternate" hreflang="x-default" href="{abs_url(en_p)}">')
    if CONFIG["gsc_verificatie"]:
        head.append(f'<meta name="google-site-verification" content="{e(CONFIG["gsc_verificatie"])}">')
    head.append(FONTS + f'<link rel="stylesheet" href="site.css?v={CSS_V}">' + extra_head)
    graph = [dict(ORG, **({"url": CONFIG["base_url"]} if CONFIG["base_url"] else {}))]
    if crumbs:
        graph.append({"@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": i + 1, "name": n, **({"item": abs_url(p)} if url else {})}
            for i, (n, p) in enumerate(crumbs)]})
    graph += extra_ld or []
    head.append(ld({"@context": "https://schema.org", "@graph": graph}))
    if CONFIG["goatcounter"]:
        head.append(f'<script data-goatcounter="https://{CONFIG["goatcounter"]}.goatcounter.com/count" async src="https://gc.zgo.at/count.js"></script>')
    if lang in TALEN:
        T = TALEN[lang]
        head.append(f'</head><body><a class="skip" href="#inhoud">{T["skip"]}</a>')
        home = f"{lang}.html"
        nav = "".join(f'<a href="{home + h if h.startswith("#") else h}">{t}</a>' for h, t in T["nav"])
        header = f'''<header class="top"><div class="wrap">
<div class="links"><details class="snel"><summary aria-label="{T["menu"]}"><span></span><span></span><span></span></summary><nav class="snel-paneel" aria-label="{T["menu"]}"><a href="{home}">Home</a>{nav}<a href="{home}#contact">{T["cta"][0]}</a><a href="en.html">English</a><a href="index.html">Nederlands</a></nav></details><a class="merk" href="{home}" aria-label="{CONFIG["naam"]}, home">{LOGO}{CONFIG["naam"]}</a></div>
<nav class="menu" aria-label="{T["hoofdmenu"]}">{nav}{taal_menu}<a class="knop" href="{home}#contact"><span class="lang">{T["cta"][0]}</span><span class="kort">{T["cta"][1]}</span></a></nav>
</div></header>'''
    elif lang == "en":
        head.append('</head><body><a class="skip" href="#inhoud">Skip to content</a>')
        header = f'''<header class="top"><div class="wrap">
<div class="links"><details class="snel"><summary aria-label="Quick menu"><span></span><span></span><span></span></summary><nav class="snel-paneel" aria-label="Quick menu"><a href="en.html">Home</a><a href="en.html#services">Services</a><a href="en.html#pricing">Pricing</a><a href="en-app-development.html">App development</a><a href="en-website-design.html">Website design</a><a href="en-projects.html">Our work</a><a href="en.html#contact">Get a quote</a><a href="index.html">Nederlands</a></nav></details><a class="merk" href="en.html" aria-label="{CONFIG["naam"]}, home">{LOGO}{CONFIG["naam"]}</a></div>
<nav class="menu" aria-label="Main menu"><a href="en.html#services">Services</a><a href="en.html#pricing">Pricing</a><a href="en-projects.html">Our work</a>{taal_menu}<a class="knop" href="en.html#contact"><span class="lang">Get a quote</span><span class="kort">Quote</span></a></nav>
</div></header>'''
    else:
        head.append('</head><body><a class="skip" href="#inhoud">Naar de inhoud</a>')
        header = f'''<header class="top"><div class="wrap">
<div class="links"><details class="snel"><summary aria-label="Snelmenu"><span></span><span></span><span></span></summary><nav class="snel-paneel" aria-label="Snelmenu"><a href="index.html">Home</a><a href="website-laten-maken.html">Website laten maken</a><a href="goedkope-website-laten-maken.html">Goedkope website</a><a href="webshop-laten-maken.html">Webshop laten maken</a><a href="app-laten-maken-kosten.html">Wat kost een app?</a><a href="mvp-app-laten-maken.html">MVP-app</a><a href="game-laten-maken.html">Game laten maken</a><a href="ai-automatisering.html">AI & automatisering</a><a href="chatbot-laten-maken.html">AI-chatbot</a><a href="apps.html">Onze apps & games</a><a href="index.html#contact">Offerte aanvragen</a><a href="en.html">English</a></nav></details><a class="merk" href="index.html" aria-label="{CONFIG["naam"]}, naar de startpagina">{LOGO}{CONFIG["naam"]}</a></div>
<nav class="menu" aria-label="Hoofdmenu"><a href="website-laten-maken.html">Websites</a><a href="app-laten-maken-kosten.html">Apps</a><a href="game-laten-maken.html">Games</a><a href="ai-automatisering.html">AI</a>{taal_menu}<a class="knop" href="index.html#contact"><span class="lang">Vraag een offerte</span><span class="kort">Offerte</span></a></nav>
</div></header>'''
    bc = ""
    if crumbs and len(crumbs) > 1:
        bc = '<nav class="kruimel wrap" aria-label="Kruimelpad">' + ' / '.join(
            f'<a href="{p}">{e(n)}</a>' if i < len(crumbs) - 1 else f'<span aria-current="page">{e(n)}</span>'
            for i, (n, p) in enumerate(crumbs)) + '</nav>'
    kvk = f' · KvK {e(CONFIG["kvk"])}' if CONFIG["kvk"] else ""
    if lang in TALEN:
        footer = f'''<footer><div class="wrap">
<span>© {datetime.date.today().year} {CONFIG["naam"]} · {TALEN[lang]["footer"]}</span>
<span><a href="{lang}.html">Home</a> · <a href="en-projects.html">Projects</a> · <a href="en.html">English</a> · <a href="index.html">Nederlands</a></span>
</div></footer>'''
    elif lang == "en":
        footer = f'''<footer><div class="wrap">
<span>© {datetime.date.today().year} {CONFIG["naam"]} · Websites, apps, games and AI · worldwide</span>
<span><a href="en.html">Home</a> · <a href="en-app-development.html">App development</a> · <a href="en-website-design.html">Website design</a> · <a href="en-projects.html">Our work</a> · <a href="en-lubbyc-privacy.html">LubbyC privacy</a> · <a href="index.html">Nederlands</a></span>
</div></footer>'''
    else:
      footer = f'''<footer><div class="wrap">
<span>© {datetime.date.today().year} {CONFIG["naam"]} · Websites, apps, games en AI{kvk}</span>
<span><a href="website-laten-maken.html">Websites</a> · <a href="goedkope-website-laten-maken.html">Goedkope website</a> · <a href="webshop-laten-maken.html">Webshop</a> · <a href="app-laten-maken-kosten.html">Apps</a> · <a href="mvp-app-laten-maken.html">MVP</a> · <a href="chatbot-laten-maken.html">Chatbot</a> · <a href="game-laten-maken.html">Games</a> · <a href="ai-automatisering.html">AI</a> · <a href="apps.html">Onze apps</a> · <a href="privacy.html">Privacy</a></span>
</div></footer>'''
    out = "".join(head) + header + bc + f'<main id="inhoud">{body}</main>' + footer + SNEL_JS + "</body></html>"
    with open(os.path.join(DIST, path), "w", encoding="utf-8") as f: f.write(out)
    return path

# ---------- inhoud ----------
FAQ = [
    ("Wat kost een app laten maken bij Collens Group?", "Een Basis-app begint bij €3.150, een Standaard-app met accounts en database bij €6.750 en een Maatwerk-app bij €13.050, allemaal zonder btw. Na een korte intake per mail krijg je een vaste prijs."),
    ("Waarom zijn jullie goedkoper dan andere bureaus?", "We bouwen één app voor iPhone en Android tegelijk, met bewezen bouwstenen en veel automatisering. Dat scheelt uren, en die besparing zie je terug in de prijs."),
    ("Ben ik eigenaar van mijn app?", "Ja. Na de laatste betaling is de broncode van jou. De app staat op jouw eigen Apple- en Google-account."),
    ("Wat kost een app na de lancering?", "Apple rekent $99 per jaar, Google $25 eenmalig. Hosting is voor kleine apps vaak €0 tot €25 per maand. Ons onderhoud is optioneel, vanaf €85,50 per maand. Dit staat altijd vooraf in de offerte."),
    ("Hoe lang duurt het bouwen van een app?", "Een Basis-app 3–5 weken, een Standaard-app 6–10 weken en een Maatwerk-app 10–16 weken of langer."),
    ("Hoe betaal ik?", "In drie delen: 40% bij akkoord, 40% bij een goedgekeurde testversie en 20% bij oplevering."),
    ("Maken jullie ook websites, games en automatiseringen?", "Ja. Websites beginnen bij €495, games bij €1.950 en AI-automatisering bij €395, allemaal zonder btw."),
    ("Werken jullie ook in België?", "Ja, we werken voor klanten in heel Nederland en België, volledig online."),
]

def faq_html(items):
    return "".join(f'<details><summary>{e(q)}</summary><p>{e(a)}</p></details>' for q, a in items)

def faq_ld(items):
    return {"@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in items]}

PAKKETTEN = '''<div class="pakketten">
<article class="pakket"><h3>Basis / MVP</h3><p class="voor">Je idee snel testen met echte gebruikers.</p>
<div class="prijs">€3.150<small>vanaf, geen btw</small></div>
<ul><li>Tot 5 schermen</li><li>Eenvoudige navigatie en content</li><li>Strak basisontwerp</li><li>Publicatieklaar voor iOS of Android</li></ul>
<p class="duur">Klaar in 3–5 weken</p></article>
<article class="pakket mid"><h3>Standaard</h3><p class="voor">Een complete app voor je klanten of team.</p>
<div class="prijs">€6.750<small>vanaf, geen btw</small></div>
<ul><li>5 tot 12 schermen</li><li>Accounts en inloggen</li><li>Eigen database en API-koppelingen</li><li>Pushmeldingen</li><li>Live in App Store én Google Play</li></ul>
<p class="duur">Klaar in 6–10 weken</p></article>
<article class="pakket"><h3>Maatwerk / Pro</h3><p class="voor">Een volledig digitaal platform.</p>
<div class="prijs">€13.050<small>vanaf, geen btw</small></div>
<ul><li>12+ schermen en complexe flows</li><li>Uitgebreide backend en beheerdashboard</li><li>Betalingen en abonnementen</li><li>Meerdere gebruikersrollen</li><li>Extra beveiliging</li></ul>
<p class="duur">Klaar in 10–16+ weken</p></article></div>'''

OFFERS = [{"@type": "Offer", "name": n, "price": p, "priceCurrency": "EUR",
           }
          for n, p in [("Basis / MVP app", 3150), ("Standaard app", 6750), ("Maatwerk / Pro app", 13050)]]
SERVICE = {"@type": "Service", "serviceType": "App-ontwikkeling", "name": "App laten maken voor iOS en Android",
           "provider": {"@id": "#org"}, "areaServed": ["NL", "BE"],
           "offers": OFFERS}

def contact_section():
    return '''<section id="contact" class="donker" aria-labelledby="contact-kop"><div class="wrap contact">
<div><h2 id="contact-kop">Vertel over je app-idee</h2>
<p>Beschrijf kort wat je wilt bouwen. Je krijgt snel een reactie met een paar korte vragen, en daarna een vaste prijs. Alles per mail, gratis en zonder verplichtingen.</p>
<p id="kanaal" style="color:#AEBBD2"></p></div>
<form id="aanvraag" name="aanvraag" method="POST" data-netlify="true" netlify-honeypot="bot-veld" novalidate>
<input type="hidden" name="form-name" value="aanvraag"><p hidden><label>Niet invullen<input name="bot-veld"></label></p>
<div class="rij2"><label>Naam<input name="naam" required autocomplete="name"></label>
<label>E-mail<input name="email" type="email" required autocomplete="email" inputmode="email"></label></div>
<div class="rij2"><label>Bedrijf (optioneel)<input name="bedrijf" autocomplete="organization"></label>
<label>Wat wil je laten maken?<select name="pakket"><option>Weet ik nog niet</option><option>App</option><option>Website of webshop</option><option>Game</option><option>AI of automatisering</option></select></label></div>
<label>Je idee<textarea name="idee" required placeholder="Wat moet de app doen, en voor wie?"></textarea></label>
<button class="knop geel" type="submit">Verstuur aanvraag</button>
<div class="melding" id="melding" role="status" aria-live="polite"></div>
</form></div></section>
<script>
const CONTACT = ''' + json.dumps({"email": CONFIG["email"], "whatsapp": CONFIG["whatsapp"]}) + r''';
const kanaal = document.getElementById("kanaal");
if (CONTACT.email) kanaal.textContent = "Liever direct mailen? " + CONTACT.email;
document.getElementById("aanvraag").addEventListener("submit", async e => {
  e.preventDefault();
  const f = e.target, m = document.getElementById("melding");
  const d = Object.fromEntries(new FormData(f));
  m.className = "melding aan"; m.innerHTML = "";
  if (!d.naam || !d.email || !d.idee || !f.email.checkValidity()) { m.textContent = "Vul je naam, een geldig e-mailadres en je idee in."; return; }
  /* Op Netlify: direct versturen. Elders (of bij een fout): terugvallen op mail/kopiëren. */
  try {
    const r = await fetch("/", {method: "POST", headers: {"Content-Type": "application/x-www-form-urlencoded"}, body: new URLSearchParams(new FormData(f)).toString()});
    if (r.ok && location.hostname.endsWith(".nl") || r.ok && location.hostname.endsWith("netlify.app")) {
      m.textContent = "Bedankt " + d.naam + "! Je aanvraag is verstuurd. Je krijgt snel antwoord op " + d.email + ".";
      f.reset();
      if (window.goatcounter && goatcounter.count) goatcounter.count({path: "aanvraag-verstuurd", event: true});
      return;
    }
  } catch (_) {}
  const tekst = `Aanvraag ${d.pakket}\nNaam: ${d.naam}\nE-mail: ${d.email}\nBedrijf: ${d.bedrijf||"-"}\nSoort: ${d.pakket}\n\nIdee:\n${d.idee}`;
  const link = (href, txt) => { const a = document.createElement("a"); a.href = href; a.textContent = txt; a.className = "knop geel"; a.style.marginRight = "8px"; return a; };
  m.append("Je aanvraag staat klaar. Kies hoe je hem verstuurt:");
  const rij = document.createElement("p"); rij.style.marginTop = "12px";
  if (CONTACT.whatsapp) rij.append(link("https://wa.me/" + CONTACT.whatsapp + "?text=" + encodeURIComponent(tekst), "Via WhatsApp"));
  if (CONTACT.email) rij.append(link("mailto:" + CONTACT.email + "?subject=" + encodeURIComponent("Aanvraag app – " + d.naam) + "&body=" + encodeURIComponent(tekst), "Via e-mail"));
  m.append(rij);
  const pre = document.createElement("pre"); pre.textContent = tekst; m.append(pre);
  const k = document.createElement("button"); k.type = "button"; k.className = "knop"; k.textContent = "Kopieer aanvraag";
  k.onclick = async () => { try { await navigator.clipboard.writeText(tekst); k.textContent = "Gekopieerd"; } catch { k.textContent = "Selecteer de tekst hierboven en kopieer"; } };
  m.append(k);
  if (window.goatcounter && goatcounter.count) goatcounter.count({path: "aanvraag-verstuurd", event: true});
});
</script>'''

# ---------- extra diensten: websites, games, AI ----------
DIENSTEN = [
    {
        "slug": "website-laten-maken", "kort": "Websites", "kleur": "#2457D6",
        "titel": "Website laten maken vanaf €495 | Collens Group",
        "desc": "Website of webshop laten maken onder de marktprijs: one-page vanaf €495, bedrijfswebsite vanaf €995, webshop vanaf €1.950. Snel, vindbaar in Google en van jou.",
        "h1": "Website laten maken", "intro": "Snelle, vindbare websites en webshops voor ondernemers. Vaste prijs vooraf, ruim onder wat bureaus vragen, en alles staat op jouw naam.",
        "markt": ("Een eenvoudige zakelijke website kost bij Nederlandse freelancers meestal €800 tot €3.000 en bij bureaus €2.500 tot €12.000.",
                  "https://www.appypie.com/nl/?p=2729541", "Appy Pie, Website laten maken: wat het kost (okt. 2026)"),
        "pakketten": [
            ("One-page", 495, "1–2 weken", ["1 pagina met alle info", "Contactformulier", "Mobielvriendelijk en snel", "Basis-SEO en Google-koppeling"]),
            ("Bedrijfswebsite", 995, "2–3 weken", ["Tot 6 pagina's", "Teksten op Google afgestemd", "Contact- en offerteformulier", "Snelheid en Core Web Vitals in orde", "Gratis hosting mogelijk"]),
            ("Webshop", 1950, "3–5 weken", ["Tot 50 producten ingericht", "iDEAL en andere betaalmethoden", "Verzending en btw ingesteld", "Je beheert zelf je producten"]),
        ],
        "extra": [("Website-onderhoud", "€29 / maand", "Updates, back-ups, kleine wijzigingen tot 30 min per maand"),
                  ("Extra pagina", "€95", "Per pagina, inclusief SEO-tekst")],
        "faq": [("Wat kost een website laten maken?", "Bij ons begint een one-page website bij €495, een bedrijfswebsite bij €995 en een webshop bij €1.950, zonder btw."),
                ("Word ik gevonden in Google?", "Elke site bouwen we snel, mobielvriendelijk en met de technische basis die Google verwacht. Een toppositie kan niemand garanderen; wel helpen we je op weg met de juiste zoekwoorden."),
                ("Wat kost een webshop laten maken?", "Volgens de kostengids van Searchlab (2026) betaal je bij een freelancer meestal €2.000 tot €8.000 en bij een bureau voor het mkb €5.000 tot €15.000. Bij ons begint een webshop bij €1.950 zonder btw, met tot 50 producten ingericht. Platformkosten komen daar los bij en staan vooraf in de offerte."),
                ("Wat kost een website per maand?", "Hosting kan voor de meeste kleine sites gratis. Een domeinnaam kost rond €5 tot €15 per jaar. Onderhoud is optioneel vanaf €29 per maand.")],
    },
    {
        "slug": "game-laten-maken", "kort": "Games", "kleur": "#7A3BD1",
        "titel": "Game laten maken vanaf €1.950 | Collens Group",
        "desc": "Mobiele game of webgame laten maken: merkgame vanaf €1.950, casual game vanaf €4.950, 2D-game met levels vanaf €9.950. Voor iOS, Android en browser.",
        "voorbeeld": ("Bekijk onze eigen games Koffer Vol! en Eiland Express", "apps.html"),
        "h1": "Game laten maken", "intro": "Casual 2D-games voor de browser, iPhone en Android. Voor je merk, je klanten of als eigen product. Vaste prijs, onder het marktgemiddelde.",
        "markt": ("Een eenvoudige mobiele game laten maken begint in Nederland rond €10.000.",
                  "https://www.juegostudio.com/blog/cost-of-game-development-netherlands", "Juego Studios, Cost of Game Development in the Netherlands (2026)"),
        "pakketten": [
            ("Merkgame", 1950, "2–3 weken", ["Webgame met jouw huisstijl", "1 spelprincipe, bijv. quiz of reactiespel", "Scorebord en deelknop", "Ideaal voor acties en beurzen"]),
            ("Casual game", 4950, "4–6 weken", ["1 uitgewerkt spelprincipe", "Geluid en animaties", "Voor iOS, Android of browser", "Advertenties of aankopen mogelijk"]),
            ("2D-game met levels", 9950, "8–12 weken", ["Meerdere levels en voortgang", "Eigen personages en wereld", "Live in App Store en Google Play", "Ranglijst en beloningen"]),
        ],
        "extra": [("Extra level of spelmodus", "vanaf €395", "Na de eerste versie"),
                  ("Game-onderhoud", "€85,50 / maand", "Updates voor nieuwe iOS- en Android-versies")],
        "faq": [("Welke games maken jullie?", "Casual 2D-games: puzzels, quizzen, reactie- en arcadespellen. Grote 3D-games of online multiplayer doen we niet."),
                ("Kan ik geld verdienen met mijn game?", "Ja, we kunnen advertenties of aankopen in de game inbouwen volgens de regels van Apple en Google."),
                ("Ben ik eigenaar van de game?", "Ja. Na betaling zijn de code en de game van jou.")],
    },
    {
        "slug": "ai-automatisering", "kort": "AI & automatisering", "kleur": "#0E7C86",
        "titel": "AI-chatbot en automatisering laten maken vanaf €395 | Collens Group",
        "desc": "Bespaar uren per week: automatisering vanaf €395, AI-chatbot op je eigen kennis vanaf €995, AI-assistent met meerdere koppelingen vanaf €1.950.",
        "h1": "AI en automatisering", "intro": "Laat terugkerend werk vanzelf gaan: mails, offertes, planning, social media en klantvragen. Met AI-tools die je bestaande apps aan elkaar koppelen.",
        "markt": ("Een AI-agent met no-code tools zoals Zapier of Make kost in Nederland eenmalig €2.000 tot €8.000.",
                  "https://searchlab.nl/kosten/wat-kost-een-ai-agent-laten-bouwen", "Searchlab, Wat kost een AI-agent laten bouwen (2026)"),
        "pakketten": [
            ("Automatisering", 395, "1 week", ["1 workflow, bijv. formulier → CRM → mail", "Koppelt je bestaande apps", "Getest en gedocumenteerd"]),
            ("AI-chatbot", 995, "1–2 weken", ["Beantwoordt vragen op je website", "Getraind op je eigen teksten", "Doorsturen naar jou bij twijfel"]),
            ("AI-assistent", 1950, "2–4 weken", ["Meerdere workflows en koppelingen", "Mail, agenda, documenten en CRM", "Jij houdt altijd de eindcontrole"]),
        ],
        "extra": [("Extra workflow", "vanaf €195", "Per extra automatisering"),
                  ("Beheer", "€49 / maand", "Monitoring en kleine aanpassingen")],
        "faq": [("Wat kost AI-automatisering per maand?", "De tools zelf zijn vaak gratis tot enkele tientjes per maand, afhankelijk van het gebruik. Dat staat altijd vooraf in de offerte."),
                ("Is mijn data veilig?", "We werken met officiële koppelingen, zonder wachtwoorden te delen, en richten alleen in wat nodig is."),
                ("Wat kan ik automatiseren?", "Bijna alles wat steeds hetzelfde gaat: aanvragen verwerken, offertes maken, afspraken plannen, social media inplannen en rapportages.")],
    },
]

def dienst_pagina(d):
    kaarten = "".join(f'''<article class="pakket{' mid' if i == 1 else ''}"><h3>{e(n)}</h3>
<div class="prijs">€{f"{p:,}".replace(",", ".")}<small>vanaf, geen btw</small></div>
<ul>{''.join(f'<li>{e(x)}</li>' for x in items)}</ul><p class="duur">Klaar in {e(t)}</p></article>'''
        for i, (n, p, t, items) in enumerate(d["pakketten"]))
    extra = "".join(f'<tr><td>{e(n)}<small>{e(s)}</small></td><td>{e(p)}</td></tr>' for n, p, s in d["extra"])
    tekst, url, bron = d["markt"]
    offers = [{"@type": "Offer", "name": n, "price": p, "priceCurrency": "EUR"} for n, p, _, _ in d["pakketten"]]
    return page(f'{d["slug"]}.html', d["titel"], d["desc"],
        f'''<article class="tekst breed">
<h1>{e(d["h1"])}</h1>
<p class="lead2">{e(d["intro"])}</p>
{f'<p><a href="{d["voorbeeld"][1]}">{e(d["voorbeeld"][0])}</a></p>' if d.get("voorbeeld") else ""}
<h2>Vergeleken met de markt</h2><p>{e(tekst)} <span class="bron">Bron: <a href="{url}" rel="nofollow noopener">{e(bron)}</a>.</span></p>
<h2>Onze pakketten</h2><div class="pakketten">{kaarten}</div>
<h2>Extra</h2><table class="lijst">{extra}</table>
<p class="noot">Alle prijzen zonder btw. Externe kosten (zoals domein, tools of store-accounts) staan vooraf in de offerte.</p>
<h2>Veelgestelde vragen</h2>{faq_html(d["faq"])}
<p style="margin-top:32px"><a class="knop geel" href="index.html#contact">Vraag een vaste prijs aan</a></p>
</article>''', crumbs=[("Home", "index.html"), (d["kort"], f'{d["slug"]}.html')],
        extra_ld=[{"@type": "Service", "name": d["h1"], "provider": {"@id": "#org"}, "areaServed": ["NL", "BE"], "offers": offers}, faq_ld(d["faq"])])

def diensten_blok():
    items = [("Apps", "iPhone en Android", "vanaf €3.150", "app-laten-maken-kosten.html", "#14213D")] + \
            [(d["kort"], d["pakketten"][0][0] + " en meer", f'vanaf €{d["pakketten"][0][1]:,}'.replace(",", "."), f'{d["slug"]}.html', d["kleur"]) for d in DIENSTEN]
    return '<div class="diensten">' + "".join(
        f'<a class="dienst" href="{h}" style="--k:{k}"><span class="dienst-naam">{e(n)}</span><span class="dienst-sub">{e(s)}</span><span class="dienst-prijs">{e(p)}</span></a>'
        for n, s, p, h, k in items) + '</div>'

def app_rijen():
    rows = ""
    for a in APPS:
        if not a.get("publiceer"): continue
        ico = f'<img src="{a["icoon"]}" alt="" width="76" height="76" style="border-radius:20px">' if a.get("icoon") else f'<div class="app-ico" style="background:{a["kleur"]};color:#fff" aria-hidden="true">{a["letter"]}</div>'
        rows += f'''<div class="app-rij">{ico}
<div><span class="soort">{e(a["soort"])} · {e(a["status"])}</span><h3>{e(a["naam"])}</h3><p style="margin:6px 0 0;color:var(--zacht)">{e(a["kort"])}</p></div>
<a class="knop" href="app-{a["slug"]}.html">Bekijk {e(a["naam"])}</a></div>'''
    return rows

# ---------- English (worldwide) ----------
EN_CONTACT_MAP = [
    ("Vertel over je app-idee", "Tell us about your project"),
    ("Beschrijf kort wat je wilt bouwen. Je krijgt snel een reactie met een paar korte vragen, en daarna een vaste prijs. Alles per mail, gratis en zonder verplichtingen.",
     "Describe what you want to build. You'll get a quick reply with a few short questions, then a fixed price. All by email, free and without obligation."),
    (">Naam<", ">Name<"), (">E-mail<", ">Email<"), ("Bedrijf (optioneel)", "Company (optional)"),
    ("Wat wil je laten maken?", "What do you need?"), ("<option>Weet ik nog niet</option>", "<option>Not sure yet</option>"),
    ("<option>Website of webshop</option>", "<option>Website or web shop</option>"), ("<option>AI of automatisering</option>", "<option>AI or automation</option>"),
    (">Je idee<", ">Your idea<"), ("Wat moet de app doen, en voor wie?", "What should it do, and for whom?"),
    ("Verstuur aanvraag", "Send request"), ('"Liever direct mailen? "', '"Prefer email? "'),
    ("Vul je naam, een geldig e-mailadres en je idee in.", "Please enter your name, a valid email address and your idea."),
    ('"Bedankt " + d.naam + "! Je aanvraag is verstuurd. Je krijgt snel antwoord op " + d.email + "."', '"Thanks " + d.naam + "! Your request has been sent. We\'ll reply soon to " + d.email + "."'),
    ("Je aanvraag staat klaar. Kies hoe je hem verstuurt:", "Your request is ready. Choose how to send it:"),
    ('"Via e-mail"', '"By email"'), ('"Kopieer aanvraag"', '"Copy request"'), ('"Gekopieerd"', '"Copied"'),
    ('"Selecteer de tekst hierboven en kopieer"', '"Select the text above and copy it"'),
    ("Aanvraag ${d.pakket}\\nNaam: ${d.naam}\\nE-mail: ${d.email}\\nBedrijf: ${d.bedrijf||\"-\"}\\nSoort: ${d.pakket}\\n\\nIdee:\\n${d.idee}",
     "Request ${d.pakket}\\nName: ${d.naam}\\nEmail: ${d.email}\\nCompany: ${d.bedrijf||\"-\"}\\nType: ${d.pakket}\\n\\nIdea:\\n${d.idee}"),
    ('"Aanvraag app – " + d.naam', '"Aanvraag app – " + d.naam + " (EN)"'),
]

def contact_en():
    h = contact_section()
    for a, b in EN_CONTACT_MAP:
        h = h.replace(a, b)
    return h

EN_SERVICES = [
    ("Websites", "One-page site", "from €495", "en.html#pricing", "#2457D6"),
    ("Apps", "iPhone and Android", "from €3,150", "en.html#pricing", "#14213D"),
    ("Games", "Casual 2D games", "from €1,950", "en.html#pricing", "#7A3BD1"),
    ("AI & automation", "Chatbots and workflows", "from €395", "en.html#pricing", "#0E7C86"),
]
EN_PRICES = [
    ("Websites", [("One-page website", "€495", "1–2 weeks"), ("Business website (up to 6 pages)", "€995", "2–3 weeks"), ("Web shop (up to 50 products)", "€1,950", "3–5 weeks")]),
    ("Apps (iOS and Android)", [("Basic / MVP app (up to 5 screens)", "€3,150", "3–5 weeks"), ("Standard app (accounts, database, push)", "€6,750", "6–10 weeks"), ("Custom / Pro app (payments, admin, roles)", "€13,050", "10–16+ weeks")]),
    ("Games (casual 2D)", [("Branded mini-game (web)", "€1,950", "2–3 weeks"), ("Casual game", "€4,950", "4–6 weeks"), ("2D game with levels", "€9,950", "8–12 weeks")]),
    ("AI & automation", [("Automation (1 workflow)", "€395", "1 week"), ("AI chatbot trained on your content", "€995", "1–2 weeks"), ("AI assistant (multiple workflows)", "€1,950", "2–4 weeks")]),
]
EN_FAQ = [
    ("Do you work with clients outside the Netherlands?", "Yes. We work fully online with clients worldwide, in English or Dutch. Prices are in euros."),
    ("Why are your prices lower than most agencies?", "We build one app for iPhone and Android at once, reuse proven building blocks and automate a lot of the work. That saves hours, and you see the savings in the price."),
    ("Do I own the result?", "Yes. After the final payment the code, design and content are yours. Apps are published on your own Apple and Google accounts."),
    ("How do I pay?", "In three parts: 40% at the start, 40% when you approve the test version and 20% on delivery."),
    ("What does it cost after launch?", "Apple charges $99 per year and Google $25 once. Hosting for small projects is often free to $25 per month. Maintenance is optional. All of this is listed in your quote."),
    ("Can I see something before I pay?", "Yes. After a short intake by email we make a free clickable concept of 1–3 screens, so you can see we can really build it."),
]

def en_pages(pages):
    price_html = "".join(
        f'<div class="prijsblok"><h3>{e(cat)}</h3><table class="lijst">' +
        "".join(f'<tr><td>{e(n)}<small>Ready in {e(t)}</small></td><td>from {e(p)}</td></tr>' for n, p, t in rows) +
        '</table></div>' for cat, rows in EN_PRICES)
    services = '<div class="diensten">' + "".join(
        f'<a class="dienst" href="{h}" style="--k:{k}"><span class="dienst-naam">{e(n)}</span><span class="dienst-sub">{e(s)}</span><span class="dienst-prijs">{e(p)}</span></a>'
        for n, s, p, h, k in EN_SERVICES) + '</div>'
    en_offers = [{"@type": "Offer", "name": n, "price": int(p.replace("€", "").replace(",", "")), "priceCurrency": "EUR"} for _, rows in EN_PRICES for n, p, _ in rows]
    pages.append(page("en.html", "Websites, apps, games and AI at fair fixed prices | " + CONFIG["naam"],
        "We build websites from €495, apps from €3,150, games from €1,950 and AI automation from €395 for clients worldwide. Fixed price, free concept, you own everything.",
        f'''<section class="hero" aria-labelledby="kop"><div class="wrap"><div>
<h1 id="kop">Your app, website or game live. In weeks, not months.</h1>
<p class="lead">We build apps, websites, games and AI automation for businesses worldwide. Fixed price up front, well below typical agency rates, and you own everything.</p>
<div class="acties"><a class="knop geel" href="#contact">Get a free quote</a><a class="zacht" href="#services">See what we build</a></div></div>
<div class="etalage"><figure class="tel-links"><img src="img/koffer-spel.jpg" alt="Koffer Vol! puzzle game" width="240" height="480"></figure><figure class="tel-midden"><img src="img/lubbyc-kaart.jpg" alt="LubbyC travel app" width="240" height="480" fetchpriority="high"></figure><figure class="tel-rechts"><img src="img/eiland-rood.jpg" alt="Island Express driving game" width="240" height="480"></figure></div></div></section>

<section id="services" class="wit" aria-labelledby="s-kop"><div class="wrap">
<div class="intro"><h2 id="s-kop">What we build</h2><p>Everything digital under one roof, at fixed prices.</p></div>
{services}
<div class="feiten" style="margin-top:48px">
<div><h3>Fixed price</h3><p>You know the price before we start. Extra work only with your approval.</p></div>
<div><h3>You own it</h3><p>No lock-in to a platform. After payment the code is yours.</p></div>
<div><h3>Free concept</h3><p>See a clickable concept of your project before you decide.</p></div>
<div><h3>Worldwide, online</h3><p>We work by email and video, in English or Dutch.</p></div>
</div></div></section>

<section id="pricing" aria-labelledby="p-kop"><div class="wrap">
<div class="intro"><h2 id="p-kop">Pricing</h2><p>Starting prices in euros. After a short intake by email you get a fixed quote.</p></div>
<div class="prijsgrid">{price_html}</div>
<p class="noot">Maintenance from €29 per month (websites) or €85.50 per month (apps and games). External costs such as domains, hosting and store accounts are always listed separately.</p>
</div></section>

<section class="donker" aria-labelledby="w-kop"><div class="wrap">
<div class="intro"><h2 id="w-kop">How it works</h2><p>Every step ends with your approval.</p></div>
<ol class="stappen"><li><h3>Intake by email</h3><p>Answer a few short questions about your idea, users and budget.</p></li>
<li><h3>Free concept</h3><p>A clickable concept of 1–3 screens, so you can see it.</p></li>
<li><h3>Fixed quote</h3><p>Price, planning and exactly what is included.</p></li>
<li><h3>Build and test</h3><p>A new test version every week.</p></li>
<li><h3>Launch</h3><p>We help you publish on the web, App Store or Google Play.</p></li></ol></div></section>

<section class="wit" aria-labelledby="o-kop"><div class="wrap">
<div class="intro"><h2 id="o-kop">Our own projects</h2><p>We build for ourselves too: a travel app, two games and an animated series. <a href="en-projects.html">See our work</a>.</p></div></div></section>

<section aria-labelledby="f-kop"><div class="wrap" style="max-width:820px">
<h2 id="f-kop">Frequently asked questions</h2>{faq_html(EN_FAQ)}</div></section>
{contact_en()}''', crumbs=[("Home", "en.html")], extra_ld=[faq_ld(EN_FAQ), {"@type": "Service", "name": "Websites, apps, games and AI automation", "provider": {"@id": "#org"}, "areaServed": "Worldwide", "offers": en_offers}],
        lang="en", alt=("index.html", "en.html")))

    en_apps = [
        ("LubbyC", "App · Coming soon on Google Play", "Meet travelers nearby. Plan dinners, beaches and trips together in Thailand. Available in 12 languages.", "img/lubbyc-icon.png", "#0E4433", "L"),
        ("Koffer Vol!", "Game · Coming soon on Google Play", "Pack the right things for every trip. A clever, cheerful packing puzzle with 100 levels in 10 countries.", "img/koffervol-icon.png", "#C2410C", "🧳"),
        ("Island Express", "Game · In development", "Drive your songthaew around a tropical island and take passengers safely to their stop. A cheerful 3D driving game.", "img/eiland-icon.jpg", "#0F766E", "E"),
        ("Manu en Khanun", "Animated kids' series · In production", "A Dutch boy and a baby elephant in northern Thailand. A series about friendship and a new culture, made with AI animation.", "img/manu-icon.jpg", "#B45309", "M"),
    ]
    rows = "".join(
        f'''<div class="app-rij">{f'<img src="{ic}" alt="" width="76" height="76" style="border-radius:20px">' if ic else f'<div class="app-ico" style="background:{k};color:#fff" aria-hidden="true">{l}</div>'}
<div><span class="soort">{e(t)}</span><h3>{e(n)}</h3><p style="margin:6px 0 0;color:var(--zacht)">{e(d)}</p></div></div>''' for n, t, d, ic, k, l in en_apps)
    gal = '<div class="galerij tel">' + "".join(f'<figure><img src="img/{f}" alt="LubbyC screenshot" loading="lazy"></figure>' for f in ["lubbyc-kaart.jpg", "lubbyc-evenementen.jpg", "lubbyc-ontdekken.jpg", "lubbyc-noodhulp.jpg"]) + '</div>'
    pages.append(page("en-projects.html", "Our work: apps, games and series | " + CONFIG["naam"],
        "Our own projects: the travel app LubbyC, the games Koffer Vol! and Island Express and the animated kids' series Manu en Khanun.",
        f'''<section><div class="wrap"><div class="intro"><h1 style="font-size:clamp(36px,5vw,56px)">Our own apps, games and series</h1>
<p style="margin-top:14px">What we build for ourselves, we build for you. We test our own way of working first.</p></div>
{rows}
<h2 style="margin-top:48px">LubbyC screenshots</h2>{gal}
<p><a class="knop geel" href="en.html#contact">Build something with us</a></p></div></section>''',
        crumbs=[("Home", "en.html"), ("Our work", "en-projects.html")], lang="en", alt=("apps.html", "en-projects.html")))

    pages.append(page("en-lubbyc-privacy.html", "LubbyC privacy policy", "How LubbyC handles your data.",
        '''<article class="tekst"><h1>LubbyC privacy policy</h1>
<p>Last updated: 14 November 2026. Contact: <a href="mailto:collens-inc@outlook.com">collens-inc@outlook.com</a>.</p>
<h2>What we collect</h2><ul>
<li><strong>Account:</strong> name, email address and user ID (required, for your account).</li>
<li><strong>Profile (optional):</strong> birth year, country, bio, interests and profile photo.</li>
<li><strong>What you create:</strong> plans, messages in group and event chats, reviews and photos.</li>
<li><strong>Location (optional):</strong> only while you use the app, to show the map and places around you, and to record your travel route if you turn that on. Your exact location is never shown to other users.</li>
<li><strong>Device ID:</strong> only to prevent abuse of the free trial.</li></ul>
<h2>Why</h2><p>Only to make the app work: your account, creating and joining plans, chat, the map and the travel guide. We do not sell your data and we do not show ads.</p>
<h2>Who receives it</h2><p>Your data is stored with our database provider Supabase (processor). When you look up places nearby, your location is sent at that moment to public map services (OpenFreeMap, Overpass) to fetch those places. Other users only see what you share in your profile and plans; basic members see fewer profile details than Premium members.</p>
<h2>Storage and deletion</h2><p>Data is encrypted in transit. You can delete your account and data in the app or by emailing <a href="mailto:collens-inc@outlook.com">collens-inc@outlook.com</a>.</p>
<h2>Age</h2><p>LubbyC is for adults only (18+).</p>
<h2>Your rights</h2><p>You can request access, correction or deletion via the email address above, and you can file a complaint with your data protection authority (in the Netherlands: the Autoriteit Persoonsgegevens).</p></article>''',
        crumbs=[("Home", "en.html"), ("LubbyC privacy", "en-lubbyc-privacy.html")], lang="en", alt=("app-lubbyc.html", "en-lubbyc-privacy.html")))

def build():
    shutil.rmtree(DIST, ignore_errors=True); os.makedirs(DIST)
    for n in ("site.css", "og.png", "_headers"): shutil.copy(os.path.join(ROOT, "src", n), os.path.join(DIST, n))
    shutil.copytree(os.path.join(ROOT, "src", "img"), os.path.join(DIST, "img"))
    with open(os.path.join(DIST, "favicon.svg"), "w") as f: f.write(LOGO.replace('aria-hidden="true"', 'xmlns="http://www.w3.org/2000/svg"'))
    pages = []

    # HOME
    pages.append(page("index.html", "App, website of game laten maken onder de marktprijs | Collens Group",
        "Apps vanaf €3.150, websites vanaf €495, games vanaf €1.950 en AI-automatisering vanaf €395. Vaste prijs vooraf, onder het marktgemiddelde, en alles is van jou.",
        f'''<section class="hero" aria-labelledby="kop"><div class="wrap"><div>
<h1 id="kop">Je app, website of game live. In weken, niet maanden.</h1>
<p class="lead">Wij bouwen apps, websites, games en AI-automatisering voor ondernemers in Nederland en België. Vaste prijs vooraf, onder het marktgemiddelde, en alles is van jou.</p>
<div class="acties"><a class="knop geel" href="#contact">Vraag gratis een prijs aan</a><a class="zacht" href="#diensten">Bekijk wat we maken</a></div></div>
<div class="etalage"><figure class="tel-links"><img src="img/koffer-spel.jpg" alt="Puzzelgame Koffer Vol!" width="240" height="480"></figure><figure class="tel-midden"><img src="img/lubbyc-kaart.jpg" alt="Reisapp LubbyC" width="240" height="480" fetchpriority="high"></figure><figure class="tel-rechts"><img src="img/eiland-rood.jpg" alt="Rijgame Eiland Express" width="240" height="480"></figure></div></div></section>

<section id="diensten" class="wit" aria-labelledby="diensten-kop"><div class="wrap">
<div class="intro"><h2 id="diensten-kop">Wat we maken</h2><p>Alles digitaal onder één dak, met vaste prijzen onder het marktgemiddelde.</p></div>
{diensten_blok()}</div></section>

<section aria-labelledby="waarom"><div class="wrap">
<div class="intro"><h2 id="waarom">Een app laten maken hoeft geen €25.000 te kosten</h2>
<p>Nederlandse kostengidsen noemen voor een eenvoudige app €5.000 tot €25.000. Wij bouwen sneller met moderne tools en automatisering, en geven dat voordeel door. <a href="app-laten-maken-kosten.html">Lees wat een app kost</a>.</p></div>
<div class="feiten">
<div><h3>Vaste prijs vooraf</h3><p>Je weet wat je betaalt voordat we beginnen. Meerwerk alleen na jouw akkoord.</p></div>
<div><h3>Code van jou</h3><p>Geen afhankelijkheid van een bouwplatform. Na betaling is de broncode van jou.</p></div>
<div><h3>Eén app, twee stores</h3><p>Gebouwd met React Native, de techniek achter veel grote apps, voor iPhone en Android.</p></div>
<div><h3>Geen verborgen kosten</h3><p>Hosting, store-accounts en andere externe kosten staan vooraf zwart op wit in de offerte.</p></div>
</div></div></section>

<section id="pakketten" aria-labelledby="prijzen"><div class="wrap">
<div class="intro"><h2 id="prijzen">App-pakketten</h2><p>Richtprijzen, zonder btw. Na een korte intake krijg je een definitieve prijsopgave op maat.</p></div>
{PAKKETTEN}
<div class="extra"><div><h3 style="margin-bottom:10px">Losse diensten</h3><table class="lijst">
<tr><td>Ontwikkeling per uur<small>Uitbreidingen en losse opdrachten</small></td><td>€67,50 / uur</td></tr>
<tr><td>Schermontwerp (UI/UX)<small>Klikbaar prototype vóór de bouw start</small></td><td>€675 – €1.800</td></tr>
<tr><td>App Store &amp; Google Play setup<small>Begeleiding en publicatie in beide stores</small></td><td>€315</td></tr>
<tr><td>Koppeling externe API of betaalprovider<small>Bijv. Mollie, Stripe, boekhouding of CRM</small></td><td>€450 – €1.350</td></tr></table></div>
<div><h3 style="margin-bottom:10px">Onderhoud per maand</h3><table class="lijst">
<tr><td>Basis Onderhoud<small>Monitoring, kritieke bugfixes, kleine iOS- en Android-updates</small></td><td>€85,50</td></tr>
<tr><td>Groei &amp; Support<small>Alles uit Basis, tot 4 uur kleine aanpassingen, voorrang bij storingen</small></td><td>€265,50</td></tr></table>
<p class="noot">Externe kosten betaal je rechtstreeks: Apple Developer Account $99 per jaar, Google Play $25 eenmalig, en eventuele hosting. Je account, je app.</p></div></div>
</div></section>

<section id="werkwijze" class="donker" aria-labelledby="stappen-kop"><div class="wrap">
<div class="intro"><h2 id="stappen-kop">Van idee tot app in de stores</h2><p>Elke stap rond je af met een akkoord. Je ziet de app groeien op je eigen telefoon.</p></div>
<ol class="stappen"><li><h3>Intake per mail</h3><p>Je beantwoordt een paar korte vragen over je idee, doelgroep en budget. Geen afspraak nodig.</p></li>
<li><h3>Voorstel</h3><p>Vaste prijs, planning en een overzicht van alle schermen.</p></li>
<li><h3>Ontwerp</h3><p>Je keurt het ontwerp goed voordat we gaan bouwen.</p></li>
<li><h3>Bouwen en testen</h3><p>Elke week een testversie op je telefoon.</p></li>
<li><h3>Live</h3><p>Wij begeleiden de publicatie in de App Store en Google Play.</p></li></ol></div></section>

<section id="apps" class="wit" aria-labelledby="apps-kop"><div class="wrap">
<div class="intro"><h2 id="apps-kop">Eigen apps, games en series</h2><p>Wat we voor onszelf maken, maken we ook voor jou. Zo testen we onze werkwijze eerst op onszelf.</p></div>
{app_rijen()}</div></section>

<section id="vragen" aria-labelledby="vragen-kop"><div class="wrap" style="max-width:820px">
<h2 id="vragen-kop">Veelgestelde vragen</h2>{faq_html(FAQ)}</div></section>
{contact_section()}''', crumbs=[("Home", "index.html")], extra_ld=[SERVICE, faq_ld(FAQ)], alt=("index.html", "en.html")))

    # KOSTEN-GIDS
    kosten_faq = [
        ("Wat kost een simpele app?", "Bij Nederlandse bureaus en freelancers kost een eenvoudige app of MVP volgens kostengidsen €5.000 tot €25.000. Bij Collens Group begint een Basis-app bij €3.150 zonder btw."),
        ("Wat kost een app per jaar aan onderhoud?", "Dat hangt af van hoeveel er na de lancering nog verandert. Bij ons is onderhoud een vast maandbedrag vanaf €85,50, met monitoring, kritieke fixes en updates voor nieuwe iOS- en Android-versies."),
        ("Wat kost een MVP-app laten maken?", "Bij Collens Group begint een MVP (Basis-pakket, tot 5 schermen) bij €3.150 zonder btw en is hij klaar in 3–5 weken. Accounts, een database of betalingen vallen onder het Standaard-pakket vanaf €6.750."),
        ("Is een app voor iPhone én Android duurder?", "Bij aparte native apps vaak bijna het dubbele. Wij bouwen met React Native, dus één codebase voor beide."),
    ]
    pages.append(page("app-laten-maken-kosten.html", "Wat kost een app laten maken in 2026? Prijzen en rekenvoorbeelden | Collens Group",
        "Wat kost een app laten maken in 2026? Marktprijzen in Nederland, alle bijkomende kosten (Apple, Google, hosting, onderhoud) en onze vaste prijzen vanaf €3.150.",
        f'''<article class="tekst breed">
<h1>Wat kost een app laten maken in 2026?</h1>
<p class="lead2">Kort antwoord: bij Nederlandse bureaus en freelancers betaal je voor een eenvoudige app meestal €5.000 tot €25.000. Bij Collens Group begint een Basis-app bij €3.150 en een complete app met accounts en database bij €6.750, zonder btw.</p>
<p class="bijgewerkt">Bijgewerkt op {datetime.date.today().strftime("%d-%m-%Y")}</p>
<nav class="toc" aria-label="Inhoud"><a href="#markt">Marktprijzen</a> · <a href="#prijzen">Onze prijzen</a> · <a href="#bijkomend">Bijkomende kosten</a> · <a href="#prijsbepalers">Wat bepaalt de prijs</a> · <a href="#besparen">Besparen</a> · <a href="#faq">Vragen</a></nav>

<h2 id="markt">Marktprijzen in Nederland</h2>
<div class="scroll"><table class="tabel">
<tr><th>Soort app</th><th>Markt (NL)</th><th>Doorlooptijd</th></tr>
<tr><td>Eenvoudige app / MVP</td><td>€5.000 – €25.000</td><td>2 – 3 maanden</td></tr>
<tr><td>Gemiddelde app</td><td>€25.000 – €75.000</td><td>3 – 6 maanden</td></tr>
<tr><td>Complexe app</td><td>€75.000 – €150.000</td><td>6 – 9 maanden</td></tr></table></div>
<p class="bron">Bron: <a href="https://searchlab.nl/kosten/wat-kost-een-app-laten-maken" rel="nofollow noopener">Searchlab, Wat kost een app laten maken (2026)</a>.</p>
<p>Uurtarieven van ontwikkelaars lopen in Nederland sterk uiteen. Het gemiddelde uurtarief van een zzp software developer ligt in 2026 rond €94 zonder btw (<a href="https://bieb.knab.nl/ondernemen/wat-verdient-een-software-developer-zzp-bekijk-uurtarief-en-winst" rel="nofollow noopener">Knab Zzp Uurtarievenboekje 2026</a>). Ons uurtarief is €67,50.</p>
<h3>Freelancer, bureau of zelf bouwen?</h3>
<div class="scroll"><table class="tabel">
<tr><th>Aanpak</th><th>Eenvoudige app</th></tr>
<tr><td>No-code bouwer (zelf)</td><td>€500 – €10.000</td></tr>
<tr><td>Freelancer of bureau (NL)</td><td>€5.000 – €25.000</td></tr>
<tr><td>Collens Group Basis / MVP</td><td>vanaf €3.150</td></tr></table></div>
<p class="bron">Bedragen no-code en freelancer/bureau: Searchlab (2026), zie hierboven.</p>

<h2 id="prijzen">Onze vaste prijzen</h2>
{PAKKETTEN}

<h2 id="bijkomend">Welke kosten komen erbij?</h2>
<p>Dit zijn de kosten die je naast de bouw rechtstreeks betaalt. Ze staan altijd vooraf in onze offerte.</p>
<table class="tabel">
<tr><th>Kostenpost</th><th>Bedrag</th></tr>
<tr><td>Apple Developer Program</td><td>$99 per jaar</td></tr>
<tr><td>Google Play-account</td><td>$25 eenmalig</td></tr>
<tr><td>Database en hosting (bijv. Supabase)</td><td>gratis tot $25 per maand voor de meeste kleine apps</td></tr>
<tr><td>Onderhoud (optioneel)</td><td>vanaf €85,50 per maand</td></tr></table>
<p class="bron">Supabase-prijzen: <a href="https://supabase.com/pricing" rel="nofollow noopener">supabase.com/pricing</a>.</p>

<h2 id="prijsbepalers">Wat bepaalt de prijs van een app?</h2>
<ul>
<li><strong>Aantal schermen en functies.</strong> Elk extra scherm of elke koppeling kost bouw- en testtijd.</li>
<li><strong>Accounts en data.</strong> Inloggen, profielen en een eigen database maken een app een stuk groter.</li>
<li><strong>Betalingen.</strong> Voor digitale abonnementen in een app gelden de betaalregels van Apple en Google.</li>
<li><strong>Ontwerp.</strong> Standaard componenten zijn sneller dan een volledig eigen ontwerp.</li>
<li><strong>Eén of twee platforms.</strong> Met React Native bouw je iPhone en Android tegelijk.</li></ul>

<h2 id="besparen">Zo bespaar je op je app</h2>
<ol>
<li>Begin met een <a href="mvp-app-laten-maken.html">MVP</a>: alleen wat gebruikers echt nodig hebben.</li>
<li>Kies één codebase voor iPhone en Android.</li>
<li>Gebruik bestaande diensten voor betalingen, inloggen en hosting in plaats van alles zelf te bouwen.</li>
<li>Leg vooraf vast wat wel en niet in de prijs zit.</li></ol>

<h2 id="faq">Veelgestelde vragen over app-kosten</h2>
{faq_html(kosten_faq)}
<p style="margin-top:32px"><a class="knop geel" href="index.html#contact">Vraag een vaste prijs aan</a></p>
</article>''', crumbs=[("Home", "index.html"), ("Kosten", "app-laten-maken-kosten.html")],
        extra_ld=[{"@type": "Article", "headline": "Wat kost een app laten maken in 2026?", "dateModified": VANDAAG, "inLanguage": "nl", "author": {"@id": "#org"}, "publisher": {"@id": "#org"}}, faq_ld(kosten_faq)]))

    # MVP
    mvp_faq = [
        ("Wat is een MVP-app?", "Een Minimum Viable Product is de kleinste versie van je app waarmee echte gebruikers je idee kunnen testen."),
        ("Hoe snel is een MVP klaar?", "Ons Basis-pakket is in 3–5 weken klaar."),
        ("Kan ik later uitbreiden?", "Ja. Omdat de code van jou is en we standaard bouwstenen gebruiken, bouwen we je MVP later uit tot een Standaard- of Maatwerk-app."),
    ]
    pages.append(page("mvp-app-laten-maken.html", "MVP app laten maken vanaf €3.150, in 3–5 weken | Collens Group",
        "Test je app-idee snel met een MVP. Tot 5 schermen, strak ontwerp, klaar in 3–5 weken vanaf €3.150. Daarna uitbreiden naar een volledige app.",
        f'''<article class="tekst breed">
<h1>MVP app laten maken</h1>
<p class="lead2">Een MVP is de kleinste versie van je app waarmee je kunt testen of mensen hem willen gebruiken. Je investeert eerst weinig, leert van echte gebruikers en bouwt daarna pas verder.</p>

<h2>Wanneer is een MVP slim?</h2>
<ul><li>Je hebt een nieuw idee en wilt weten of er vraag naar is.</li>
<li>Je wilt investeerders of partners iets tastbaars laten zien.</li>
<li>Je wilt een eerste versie live hebben voordat een concurrent dat doet.</li></ul>

<h2>Wat zit er in ons Basis / MVP-pakket?</h2>
<table class="tabel"><tr><th>Onderdeel</th><th>Inbegrepen</th></tr>
<tr><td>Schermen</td><td>Tot 5</td></tr><tr><td>Navigatie en content</td><td>Eenvoudig en duidelijk</td></tr>
<tr><td>Ontwerp</td><td>Strak, met standaard componenten</td></tr><tr><td>Platform</td><td>Publicatieklaar voor iOS of Android</td></tr>
<tr><td>Prijs</td><td>vanaf €3.150 geen btw</td></tr><tr><td>Doorlooptijd</td><td>3 – 5 weken</td></tr></table>
<p>Accounts, een database of betalingen nodig? Dan past het <a href="app-laten-maken-kosten.html">Standaard-pakket vanaf €6.750</a> beter.</p>

<h2>Zo verloopt het</h2>
<ol><li>Gratis intake per mail: een paar korte vragen.</li><li>Voorstel met vaste prijs en schermoverzicht.</li><li>Ontwerp ter goedkeuring.</li><li>Bouwen, met elke week een testversie op je telefoon.</li><li>Oplevering en hulp bij publicatie.</li></ol>

<h2>Veelgestelde vragen</h2>{faq_html(mvp_faq)}
<p style="margin-top:32px"><a class="knop geel" href="index.html#contact">Bespreek je MVP</a></p>
</article>''', crumbs=[("Home", "index.html"), ("MVP", "mvp-app-laten-maken.html")],
        extra_ld=[dict(SERVICE, name="MVP app laten maken", offers=[OFFERS[0]]), faq_ld(mvp_faq)]))

    for d in DIENSTEN: pages.append(dienst_pagina(d))
    from landings import landing_pages
    landing_pages(page, e, faq_html, faq_ld, pages)

    # APPS-OVERZICHT
    pages.append(page("apps.html", "Eigen apps, games en series | Collens Group",
        "Wat Collens Group zelf maakt: de reisapp LubbyC, de games Koffer Vol! en Eiland Express en de animatieserie Manu en Khanun.",
        f'''<section><div class="wrap"><div class="intro"><h1 style="font-size:clamp(36px,5vw,56px)">Eigen apps, games en series</h1>
<p style="margin-top:14px">We maken niet alleen dingen voor klanten, maar ook voor onszelf: een reisapp, twee games en een animatieserie. Zo weten we precies wat werkt, van ontwerp tot store.</p></div>
{app_rijen()}</div></section>''', crumbs=[("Home", "index.html"), ("Onze apps", "apps.html")]))

    # APP-PAGINA'S
    for a in APPS:
        if not a.get("publiceer"): continue
        winkels = ""
        if a["appstore"]: winkels += f'<a class="knop" href="{a["appstore"]}">Download in de App Store</a> '
        if a["playstore"]: winkels += f'<a class="knop" href="{a["playstore"]}">Download in Google Play</a>'
        privacy = f'<h2 id="privacy" style="margin-top:40px">Privacybeleid {e(a["naam"])}</h2>{a["privacy"]}' if a["privacy"] else ""
        app_ld = {"@type": a["schema"], "name": a["naam"], "inLanguage": "nl", "author": {"@id": "#org"}, "description": a["kort"]}
        if a["schema"] in ("MobileApplication", "VideoGame"):
            app_ld.update({"applicationCategory": a["categorie"], "operatingSystem": "Android"})
        if a["appstore"] or a["playstore"]:
            app_ld["offers"] = {"@type": "Offer", "price": 0, "priceCurrency": "EUR"}
        beelden = ""
        if a["beelden"]:
            klasse = "galerij tel" if a["soort"] in ("App", "Game") else "galerij breed"
            beelden = f'<div class="{klasse}">' + "".join(f'<figure><img src="{src}" alt="{e(alt)}" loading="lazy"><figcaption>{e(alt)}</figcaption></figure>' for src, alt in a["beelden"]) + '</div>'
        kenmerken = "<ul class='kenmerken'>" + "".join(f"<li>{e(k)}</li>" for k in a["kenmerken"]) + "</ul>"
        cta = {"App": "Zelf een app laten maken?", "Game": "Zelf een game laten maken?", "Kinderserie": "Ook iets moois laten maken?"}[a["soort"]]
        pages.append(page(f'app-{a["slug"]}.html', a["titel"], a["kort"] + " " + a["status"] + ".",
            f'''<section class="app-hero" style="background:{a["kleur"]}"><div class="wrap">
<span class="status">{e(a["soort"])} · {e(a["status"])}</span>
<h1>{e(a["kop"])}</h1><p>{e(a["kort"])}</p>{winkels}</div></section>
<section><div class="wrap" style="max-width:980px">
<h2>Over {e(a["naam"])}</h2><p>{e(a["intro"])}</p>{kenmerken}
{beelden}
{f'<div style="max-width:360px;margin:0 0 30px"><video src="{a["video"][0]}" poster="{a["video"][1]}" controls muted playsinline loop preload="none" style="width:100%;border-radius:22px;border:6px solid #0E1830"></video><p class="bron">Proefrit, 10 seconden</p></div>' if a.get("video") else ""}
{privacy}
<p style="margin-top:30px"><a class="knop" href="index.html#contact">{cta}</a></p></div></section>''',
            crumbs=[("Home", "index.html"), ("Onze apps", "apps.html"), (a["naam"], f'app-{a["slug"]}.html')], extra_ld=[app_ld]))

    # PRIVACY
    pages.append(page("privacy.html", "Privacy | Collens Group", "Hoe Collens Group omgaat met je gegevens.",
        f'''<article class="tekst"><h1>Privacy</h1><p>Laatst bijgewerkt: {datetime.date.today().strftime("%d-%m-%Y")}</p>
<h2>Wat deze website verzamelt</h2><p>Deze website plaatst geen trackingcookies. {"We tellen bezoeken met GoatCounter, dat geen cookies gebruikt en geen persoonsgegevens opslaat." if CONFIG["goatcounter"] else "We gebruiken geen analytics."} Vul je het aanvraagformulier in, dan zet het formulier je bericht klaar zodat je het zelf naar ons mailt. Onze website wordt gehost door Cloudflare.</p>
<h2>Als je contact met ons opneemt</h2><p>Stuur je ons een aanvraag, dan gebruiken we je naam, e-mailadres, bedrijfsnaam en je beschrijving alleen om je aanvraag te beantwoorden en, als je klant wordt, om het project uit te voeren. We bewaren deze gegevens niet langer dan nodig en delen ze niet met anderen, behalve als dat nodig is voor het project en je daarmee akkoord gaat.</p>
<h2>Lettertypes</h2><p>Deze website laadt lettertypes via Google Fonts. Daarbij ziet Google je IP-adres.</p>
<h2>Je rechten</h2><p>Je kunt ons altijd vragen welke gegevens we van je hebben, en vragen om ze aan te passen of te verwijderen. Ook kun je een klacht indienen bij de Autoriteit Persoonsgegevens.</p>
<h2>Apps van Collens Group</h2><p>Elke app heeft een eigen privacybeleid op zijn eigen pagina, zie <a href="apps.html">onze apps</a>.</p></article>''',
        crumbs=[("Home", "index.html"), ("Privacy", "privacy.html")]))

    en_pages(pages)
    taal_paginas(page, e, faq_html, faq_ld, contact_section, pages)

    # 404
    page("404.html", "Pagina niet gevonden | Collens Group", "Deze pagina bestaat niet.",
         '<article class="tekst"><h1>Deze pagina bestaat niet</h1><p>De link is misschien verouderd. Ga naar de <a href="index.html">startpagina</a> of bekijk <a href="app-laten-maken-kosten.html">wat een app kost</a>.</p></article>')

    # robots, sitemap, llms.txt
    with open(os.path.join(DIST, "robots.txt"), "w") as f:
        f.write("User-agent: *\nAllow: /\n" + (f"Sitemap: {CONFIG['base_url']}/sitemap.xml\n" if CONFIG["base_url"] else ""))
    if CONFIG["base_url"]:
        with open(os.path.join(DIST, "sitemap.xml"), "w") as f:
            f.write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' +
                    "".join(f"<url><loc>{abs_url(p)}</loc><lastmod>{VANDAAG}</lastmod></url>\n" for p in pages) + "</urlset>\n")
    with open(os.path.join(DIST, "llms.txt"), "w") as f:
        f.write(f"# {CONFIG['naam']}\n\n> Websites, apps, games en AI-automatisering in Nederland en België, tegen vaste prijzen onder het marktgemiddelde.\n\n"
                "## Prijzen (geen btw)\n- Websites: one-page €495, bedrijfswebsite €995, webshop €1.950\n- Games: merkgame €1.950, casual game €4.950, 2D-game met levels €9.950\n- AI: automatisering €395, AI-chatbot €995, AI-assistent €1.950\n- Basis / MVP app: vanaf €3.150, 3–5 weken\n- Standaard app: vanaf €6.750, 6–10 weken\n- Maatwerk / Pro app: vanaf €13.050, 10–16+ weken\n- Uurtarief: €67,50\n- Onderhoud: €85,50 of €265,50 per maand\n\n"
                "## Pagina's\n" + "".join(f"- [{p}]({abs_url(p) or p})\n" for p in pages))
    print("Gebouwd:", ", ".join(pages))

if __name__ == "__main__":
    build()
