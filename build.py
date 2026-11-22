#!/usr/bin/env python3
"""Collens Group website generator.
Bewerk CONFIG en APPS, run `python3 build.py`, de site staat in ./dist.
"""
import json, os, re, shutil, html, datetime
from talen import TALEN, taal_paginas
from boek import boek_rel

ROOT = os.path.dirname(os.path.abspath(__file__))
DIST = os.path.join(ROOT, "dist")

CONFIG = {
    "naam": "Collens Group",
    "base_url": os.environ.get("BASE_URL", "https://collensgroup.com").rstrip("/"),   # gekozen domein
    "email": json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "contact.json")))["email"],  # contactadres staat in contact.json
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
        "slug": "lubbyc", "naam": "LubbyC", "soort": "App", "kleur": "#0E4433", "letter": "L", "icoon": "img/lubbyc-icon.png", "publiceer": True, "tester": "com.lubbyc.app", "test_vrij": True,
        "kort": "Ontmoet reizigers in de buurt en plan samen eten, strand of een tour in Thailand.",
        "titel": "LubbyC: reis samen in Thailand en ontmoet reizigers",
        "kop": "Alleen op reis, maar niet alleen eten vanavond.",
        "intro": "LubbyC verbindt reizigers die op dezelfde plek zijn en hetzelfde willen doen. Open de kaart, zie wat mensen in de buurt van plan zijn en sluit aan, of maak zelf een plan. We starten in Krabi en Ao Nang, Phuket, Pattaya en Bangkok.",
        "kenmerken": ["Plannen in de buurt op de kaart: eten, strand, dagtrips, tempels", "In een paar tikken zelf een plan maken", "Groepschat zodra je bent geaccepteerd", "Reisgids, weer en plekken in de buurt", "Noodhulp met één tik", "In 13 talen"],
        "beelden": [("img/lubbyc-kaart.jpg", "Kaart met plannen in de buurt"), ("img/lubbyc-evenementen.jpg", "Feesten en evenementen"), ("img/lubbyc-ontdekken.jpg", "Ontdekken"), ("img/lubbyc-noodhulp.jpg", "Noodhulp")],
        "status": "Binnenkort in Google Play",
        "categorie": "TravelApplication", "schema": "MobileApplication",
        "appstore": "", "playstore": "",
        "privacy": LUBBYC_PRIVACY,
    },
    {
        "slug": "koffer-vol", "naam": "Koffer Vol!", "soort": "Game", "kleur": "#1F7A70", "letter": "🧳", "icoon": "img/koffervol-icon.png", "publiceer": True, "tester": "com.collensgroup.koffervol",
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
        "titel": "Eiland Express – 3D-rijgame door een tropisch eiland",
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
         '<link href="https://fonts.googleapis.com/css2?family=Geist:wght@500;600;700&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">')
LOGO = '<img src="img/logo-icon-96.png" width="32" height="32" alt="" style="border-radius:50%;display:block">'

def e(s): return html.escape(s, quote=True)

def abs_url(path):
    # Cloudflare Pages serveert pagina's zonder .html (308-redirect); canonical en sitemap wijzen direct naar die URL
    clean = "" if path == "index.html" else (path[:-5] if path.endswith(".html") else path)
    return f'{CONFIG["base_url"]}/{clean}' if CONFIG["base_url"] else ""

def ld(obj):
    # één vaste, absolute @id voor de organisatie op alle pagina's (beter herkenbaar als entiteit voor Google en AI-zoekmachines)
    js = json.dumps(obj, ensure_ascii=False).replace('"#org"', json.dumps(CONFIG["base_url"] + "/#org"))
    return '<script type="application/ld+json">' + js + '</script>'

ORG = {"@type": "ProfessionalService", "@id": "#org", "name": CONFIG["naam"],
       "description": "Websites, apps, games en AI-automatisering tegen vaste prijzen onder het marktgemiddelde.",
       "areaServed": "Worldwide",
       "priceRange": "€395 – €13.050+", "knowsLanguage": ["nl", "en"],
       "logo": CONFIG["base_url"] + "/img/collens-group-logo.png", "image": CONFIG["base_url"] + "/img/collens-group-logo.png",
       "email": json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "contact.json")))["email"]}

GLOBE = '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3c2.5 2.7 3.8 5.7 3.8 9s-1.3 6.3-3.8 9c-2.5-2.7-3.8-5.7-3.8-9S9.5 5.7 12 3z"/></svg>'
NL_NAAR_EN = {"website-laten-maken.html": "en-website-design.html", "goedkope-website-laten-maken.html": "en-website-design.html", "webshop-laten-maken.html": "en-web-shop.html", "prijzen.html": "en-pricing.html", "over-ons.html": "en-about.html", "game-laten-maken.html": "en-game-development.html", "merkgame-laten-maken-kerst.html": "en-game-development.html",
              "app-laten-maken-kosten.html": "en-app-development.html", "mvp-app-laten-maken.html": "en-app-development.html",
              "apps.html": "en-projects.html", "app-lubbyc.html": "en-projects.html", "app-koffer-vol.html": "en-projects.html", "app-eiland-express.html": "en-projects.html", "app-manu-en-khanun.html": "en-projects.html", "chatbot-laten-maken.html": "en-ai-chatbot.html", "ai-automatisering.html": "en-ai-automation.html"}
EN_NAAR_NL = {"en-website-design.html": "website-laten-maken.html", "en-app-development.html": "app-laten-maken-kosten.html", "en-projects.html": "apps.html", "en-lubbyc-privacy.html": "app-lubbyc.html", "en-ai-chatbot.html": "chatbot-laten-maken.html", "en-pricing.html": "prijzen.html", "en-about.html": "over-ons.html", "en-web-shop.html": "webshop-laten-maken.html", "en-game-development.html": "game-laten-maken.html", "en-ai-automation.html": "ai-automatisering.html"}

FOOT = {
 "nl": {"tag": "Websites, apps, games en AI-automatisering voor ondernemers in Nederland, België en wereldwijd. Vaste prijs vooraf.",
        "kol": [("Diensten", [("website-laten-maken.html", "Website laten maken"), ("webshop-laten-maken.html", "Webshop laten maken"), ("app-laten-maken-kosten.html", "App laten maken"), ("game-laten-maken.html", "Game laten maken"), ("ai-automatisering.html", "AI & automatisering"), ("chatbot-laten-maken.html", "AI-chatbot")]),
                ("Meer", [("prijzen.html", "Prijzen"), ("pakketkiezer.html", "Pakketkiezer"), ("kostencalculator.html", "Kostencalculator"), ("over-ons.html", "Over ons"), ("apps.html", "Onze apps & games"), ("boeken.html", "Boeken"), ("artikelen.html", "Artikelen en gidsen"), ("privacy.html", "Privacy")]),
                ("Contact", [("index.html#contact", "Offerte aanvragen"), ("mailto:" + CONFIG["email"], CONFIG["email"])] + ([("https://wa.me/" + CONFIG["whatsapp"], "WhatsApp")] if CONFIG["whatsapp"] else []))],
        "copy": "Alle prijzen zijn eindprijzen: we rekenen geen btw."},
 "en": {"tag": "Websites, apps, games and AI automation for businesses worldwide. Fixed price up front.",
        "kol": [("Services", [("en-website-design.html", "Website design"), ("en-app-development.html", "App development"), ("en-web-shop.html", "Web shop"), ("en-game-development.html", "Game development"), ("en-ai-automation.html", "AI automation"), ("en-ai-chatbot.html", "AI chatbot"), ("en-pricing.html", "Pricing")]),
                ("More", [("en-about.html", "About us"), ("en-projects.html", "Our work"), ("en-lubbyc-privacy.html", "LubbyC privacy")]),
                ("Contact", [("en.html#contact", "Get a quote"), ("mailto:" + CONFIG["email"], CONFIG["email"])])],
        "copy": "Prices in euros."},
}

def footer_html(lang, kvk=""):
    if lang in TALEN:
        T = TALEN[lang]
        F = {"tag": T["footer"], "kol": [(T["s_kop"], [(f"{lang}.html#" + T["nav"][0][0].lstrip("#"), T["nav"][0][1]), (f"{lang}.html#" + T["nav"][1][0].lstrip("#"), T["nav"][1][1]), ("en-projects.html", T["nav"][2][1])]),
             ("Contact", [(f"{lang}.html#contact", T["cta"][0]), ("mailto:" + CONFIG["email"], CONFIG["email"])])], "copy": ""}
        home = f"{lang}.html"
    else:
        F = FOOT[lang]; home = "en.html" if lang == "en" else "index.html"
    kols = "".join(f'<div class="voet-kol"><h2>{e(k)}</h2><ul>' + "".join(f'<li><a href="{h}">{e(t)}</a></li>' for h, t in links) + '</ul></div>' for k, links in F["kol"])
    return (f'<footer class="voet"><div class="wrap voet-grid"><div class="voet-merk"><a class="merk merk-licht" href="{home}">{LOGO}{CONFIG["naam"]}</a><p>{e(F["tag"])}</p></div>{kols}</div>'
            f'<div class="wrap voet-onder"><span>© {datetime.date.today().year} {CONFIG["naam"]}{kvk}</span><span>{e(F["copy"])}</span></div></footer>')

SNEL_JS = """<script>(()=>{const t=document.querySelector('[data-terug]');if(t){t.addEventListener('click',e=>{try{if(document.referrer&&new URL(document.referrer).host===location.host&&history.length>1){e.preventDefault();history.back()}}catch(_){}})}document.querySelectorAll('details.snel,details.taalkeuze').forEach(d=>{document.addEventListener('click',e=>{if(d.open&&!d.contains(e.target))d.open=false});document.addEventListener('keydown',e=>{if(e.key==='Escape'&&d.open){d.open=false;d.querySelector('summary').focus()}});d.querySelectorAll('nav a').forEach(a=>a.addEventListener('click',()=>{d.open=false}))})})();</script>"""

def page(path, title, desc, body, crumbs=None, extra_ld=None, extra_head="", lang="nl", alt=None):
    if alt is None:  # wederzijdse NL/EN-paren automatisch koppelen (hreflang), alleen als beide kanten naar elkaar wijzen
        if lang == "en" and path in EN_NAAR_NL and NL_NAAR_EN.get(EN_NAAR_NL[path]) == path:
            alt = (EN_NAAR_NL[path], path)
        elif lang == "nl" and path in NL_NAAR_EN and EN_NAAR_NL.get(NL_NAAR_EN[path]) == path:
            alt = (path, NL_NAAR_EN[path])
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
            '<meta name="theme-color" content="#14213D"><link rel="icon" href="img/favicon-48.png" type="image/png" sizes="48x48"><link rel="apple-touch-icon" href="img/apple-touch-icon.png">',
            f'<meta property="og:type" content="website"><meta property="og:locale" content="{ {"en": "en_US", "nl": "nl_NL", "de": "de_DE", "fr": "fr_FR", "es": "es_ES", "th": "th_TH", "my": "my_MM"}.get(lang, "nl_NL") }"><meta property="og:site_name" content="{CONFIG["naam"]}">',
            f'<meta property="og:title" content="{e(title)}"><meta property="og:description" content="{e(desc)}">',
            '<meta name="twitter:card" content="summary_large_image">']
    if url:
        head.append(f'<link rel="canonical" href="{url}"><meta property="og:url" content="{url}">')
        head.append(f'<meta property="og:image" content="{CONFIG["base_url"]}/og.png">')
    HOMES = {"nl": "index.html", "en": "en.html", "de": "de.html", "fr": "fr.html", "es": "es.html", "th": "th.html", "my": "my.html"}
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
<div class="links"><details class="snel"><summary aria-label="{T["menu"]}"><span></span><span></span><span></span></summary><nav class="snel-paneel" aria-label="{T["menu"]}"><a href="{home}">Home</a>{nav}</nav></details><a class="merk" href="{home}" aria-label="{CONFIG["naam"]}, home">{LOGO}{CONFIG["naam"]}</a></div>
<nav class="menu" aria-label="{T["hoofdmenu"]}">{nav}{taal_menu}<a class="knop" href="{home}#contact"><span class="lang">{T["cta"][0]}</span><span class="kort">{T["cta"][1]}</span></a></nav>
</div></header>'''
    elif lang == "en":
        head.append('</head><body><a class="skip" href="#inhoud">Skip to content</a>')
        header = f'''<header class="top"><div class="wrap">
<div class="links"><details class="snel"><summary aria-label="Quick menu"><span></span><span></span><span></span></summary><nav class="snel-paneel" aria-label="Quick menu"><a href="en.html">Home</a><a href="en.html#services">Services</a><a href="en-pricing.html">Pricing</a><a href="en-website-design.html">Website design</a><a href="en-web-shop.html">Web shop</a><a href="en-app-development.html">App development</a><a href="en-game-development.html">Game development</a><a href="en-ai-automation.html">AI automation</a><a href="en-ai-chatbot.html">AI chatbot</a><a href="en-projects.html">Our work</a><a href="en-about.html">About us</a><a href="tester/index.html">Become a tester</a><a href="tester/qr.html">Tester QR</a></nav></details><a class="merk" href="en.html" aria-label="{CONFIG["naam"]}, home">{LOGO}{CONFIG["naam"]}</a></div>
<nav class="menu" aria-label="Main menu"><a href="en.html#services">Services</a><a href="en.html#pricing">Pricing</a><a href="en-projects.html">Our work</a>{taal_menu}<a class="knop" href="en.html#contact"><span class="lang">Get a quote</span><span class="kort">Quote</span></a></nav>
</div></header>'''
    else:
        head.append('</head><body><a class="skip" href="#inhoud">Naar de inhoud</a>')
        header = f'''<header class="top"><div class="wrap">
<div class="links"><details class="snel"><summary aria-label="Snelmenu"><span></span><span></span><span></span></summary><nav class="snel-paneel" aria-label="Snelmenu"><a href="index.html">Home</a><a href="boeken.html">Boeken: leer het jezelf</a><a href="website-laten-maken.html">Website laten maken</a><a href="webshop-laten-maken.html">Webshop laten maken</a><a href="app-laten-maken-kosten.html">App laten maken</a><a href="game-laten-maken.html">Game laten maken</a><a href="ai-automatisering.html">AI & automatisering</a><a href="chatbot-laten-maken.html">AI-chatbot</a><a href="prijzen.html">Prijzen</a><a href="pakketkiezer.html">Pakketkiezer</a><a href="apps.html">Onze apps & games</a><a href="over-ons.html">Over ons</a><a href="artikelen.html">Artikelen en gidsen</a></nav></details><a class="merk" href="index.html" aria-label="{CONFIG["naam"]}, naar de startpagina">{LOGO}{CONFIG["naam"]}</a></div>
<nav class="menu" aria-label="Hoofdmenu"><a href="boeken.html">Boeken</a><a href="website-laten-maken.html">Websites</a><a href="app-laten-maken-kosten.html">Apps</a><a href="game-laten-maken.html">Games</a><a href="ai-automatisering.html">AI</a><a href="prijzen.html">Prijzen</a>{taal_menu}<a class="knop" href="index.html#contact"><span class="lang">Vraag een offerte</span><span class="kort">Offerte</span></a></nav>
</div></header>'''
    bc = ""
    if crumbs and len(crumbs) > 1:
        terug_txt = {"nl": "Terug", "en": "Back", "de": "Zurück", "fr": "Retour", "es": "Volver", "th": "กลับ", "my": "နောက်သို့"}.get(lang, "Terug")
        ouder = crumbs[-2][1]
        pijl = '<svg viewBox="0 0 20 20" width="16" height="16" aria-hidden="true"><path d="M12.5 4.5L7 10l5.5 5.5" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg>'
        bc = ('<div class="paginabalk"><div class="wrap"><a class="terug" href="' + ouder + '" data-terug>' + pijl + terug_txt + '</a>'
              '<nav class="kruimel" aria-label="Kruimelpad">' + '<span class="sep">/</span>'.join(
            f'<a href="{p}">{e(n)}</a>' if i < len(crumbs) - 1 else f'<span aria-current="page">{e(n)}</span>'
            for i, (n, p) in enumerate(crumbs)) + '</nav></div></div>')
    kvk = f' · KvK {e(CONFIG["kvk"])}' if CONFIG["kvk"] else ""
    footer = footer_html(lang, kvk)
    header = header.replace(f'<a href="{path}">', f'<a href="{path}" aria-current="page">', 1) if 'class="snel-paneel"' in header else header
    vast = ""
    if lang == "nl" and "noindex" not in extra_head:
        wa = f'<a class="knop" href="https://wa.me/{CONFIG["whatsapp"]}">WhatsApp</a>' if CONFIG["whatsapp"] else ""
        vast = f'<div class="vastecta" id="vastecta" hidden>{wa}<a class="knop geel" href="index.html#contact">Vraag je gratis concept aan</a></div><script>(()=>{{const b=document.getElementById("vastecta");if(!b)return;const c=document.getElementById("contact");const t=()=>{{const h=c&&c.getBoundingClientRect().top<innerHeight;b.hidden=window.scrollY<400||h}};addEventListener("scroll",t,{{passive:true}});t()}})();</script>'
    out = "".join(head) + header + bc + f'<main id="inhoud">{body}</main>' + footer + vast + SNEL_JS + "</body></html>"
    with open(os.path.join(DIST, path), "w", encoding="utf-8") as f: f.write(out)
    return path

# ---------- inhoud ----------
FAQ = [
    ("Wat kost een app laten maken bij Collens Group?", "Een Basis-app begint bij €3.150, een Standaard-app met accounts en database bij €6.750 en een Maatwerk-app bij €13.050, allemaal eindprijzen, geen btw erbij. Na een korte intake per mail krijg je een vaste prijs."),
    ("Waarom zijn jullie goedkoper dan andere bureaus?", "We bouwen één app voor iPhone en Android tegelijk, met bewezen bouwstenen en veel automatisering. Dat scheelt uren, en die besparing zie je terug in de prijs. Er zit ook geen accountmanager of grote organisatie tussen: je mailt rechtstreeks met de maker. De kwaliteit bewaken we zelf: elk concept, elke tekst en elke oplevering wordt gecontroleerd voordat je hem krijgt."),
    ("Ben ik eigenaar van mijn app?", "Ja. Na de laatste betaling is de broncode van jou. De app staat op jouw eigen Apple- en Google-account, dus de app, de reviews en de gebruikers blijven altijd bij jou. Wil je later met een andere ontwikkelaar verder, dan kan dat zonder opnieuw te beginnen. Je zit nergens aan vast, ook niet aan ons onderhoud."),
    ("Wat kost een app na de lancering?", "Er zijn drie soorten kosten. Apple rekent $99 per jaar voor een ontwikkelaarsaccount en Google $25 eenmalig; die betaal je rechtstreeks aan hen. Hosting en database kosten voor kleine apps vaak €0 tot €25 per maand. Ons onderhoud is optioneel: vanaf €85,50 per maand houden we de app werkend bij nieuwe iOS- en Android-versies. Al deze kosten staan vooraf in de offerte, zodat je weet waar je aan toe bent."),
    ("Hoe lang duurt het bouwen van een app?", "Een Basis-app duurt 3 tot 5 weken, een Standaard-app 6 tot 10 weken en een Maatwerk-app 10 tot 16 weken of langer. Daarna moet de app nog door de controle van Apple en Google, wat meestal een paar dagen duurt. Je krijgt vooraf een planning en tijdens het bouwen tussentijdse testversies, zodat je ziet hoe het vordert en op tijd kunt bijsturen."),
    ("Hoe betaal ik?", "Bij apps in drie delen: 40% bij akkoord op de offerte, 40% als je een testversie hebt goedgekeurd en 20% bij oplevering. Zo betaal je nooit alles vooraf en zie je steeds eerst resultaat. Bij kleinere opdrachten, zoals een website of automatisering, staat de betaling vooraf in de offerte. Alle prijzen zijn eindprijzen: er komt geen btw bij."),
    ("Maken jullie ook websites, games en automatiseringen?", "Ja. Websites beginnen bij €495, webshops bij €1.950, games bij €1.950 en AI-automatisering bij €395, allemaal eindprijzen zonder btw erbij. Alles komt uit één hand, dus je website, app en automatiseringen sluiten op elkaar aan en je hebt één aanspreekpunt. Op de pagina van elke dienst zie je wat er in de pakketten zit en hoe lang het duurt."),
    ("Werken jullie ook in België en buiten Nederland?", "Ja. We werken volledig online, per mail en video, voor klanten in Nederland, België en de rest van de wereld. Dat kan in het Nederlands of het Engels, en de prijzen zijn overal dezelfde eindprijzen in euro."),
]

def faq_html(items):
    return "".join(f'<details><summary>{e(q)}</summary><p>{e(a)}</p></details>' for q, a in items)

def faq_ld(items):
    return {"@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in items]}

PAKKETTEN = '''<div class="pakketten">
<article class="pakket"><h3>Basis / MVP</h3><p class="voor">Je idee snel testen met echte gebruikers.</p>
<div class="prijs">€3.150<small>vanaf, eindprijs, geen btw erbij</small></div>
<ul><li>Tot 5 schermen</li><li>Eenvoudige navigatie en content</li><li>Strak basisontwerp</li><li>Publicatieklaar voor iOS of Android</li></ul>
<p class="duur">Klaar in 3–5 weken</p></article>
<article class="pakket mid"><h3>Standaard</h3><p class="voor">Een complete app voor je klanten of team.</p>
<div class="prijs">€6.750<small>vanaf, eindprijs, geen btw erbij</small></div>
<ul><li>5 tot 12 schermen</li><li>Accounts en inloggen</li><li>Eigen database en API-koppelingen</li><li>Pushmeldingen</li><li>Live in App Store én Google Play</li></ul>
<p class="duur">Klaar in 6–10 weken</p></article>
<article class="pakket"><h3>Maatwerk / Pro</h3><p class="voor">Een volledig digitaal platform.</p>
<div class="prijs">€13.050<small>vanaf, eindprijs, geen btw erbij</small></div>
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
<div><h2 id="contact-kop">Vertel wat je wilt laten maken</h2>
<p>Een paar zinnen zijn genoeg. Je krijgt binnen 48 uur een reactie met een paar korte vragen, en daarna een gratis concept en een vaste prijs. Alles per mail en zonder verplichtingen.</p>
<ul class="vertrouwen-lijst"><li>Vaste prijs vooraf, eindprijs zonder btw erbij</li><li>Gratis concept voordat je iets betaalt</li><li>Snel live, zonder lange trajecten</li></ul>
<p id="kanaal" style="color:#AEBBD2"></p></div>
<form id="aanvraag" name="aanvraag" method="POST" data-netlify="true" netlify-honeypot="bot-veld" novalidate>
<input type="hidden" name="form-name" value="aanvraag"><p hidden><label>Niet invullen<input name="bot-veld"></label></p>
<div class="rij2"><label>Naam<input name="naam" required autocomplete="name"></label>
<label>E-mail<input name="email" type="email" required autocomplete="email" inputmode="email"></label></div>
<div class="rij2"><label>Bedrijf (optioneel)<input name="bedrijf" autocomplete="organization"></label>
<label>Wat wil je laten maken?<select name="pakket"><option>Weet ik nog niet</option><option>Website</option><option>Webshop</option><option>App</option><option>Game</option><option>AI of automatisering</option></select></label></div>
<label>Je idee<textarea name="idee" required placeholder="Wat wil je laten maken, en voor wie? Bijvoorbeeld: een website voor mijn kapsalon met online afspraken."></textarea></label>
<p class="hulp-idee" data-chat-blok hidden><button type="button" class="hulp-knop" data-chat-open data-chat-vraag="Kun je me helpen mijn aanvraag goed te omschrijven?"><svg viewBox="0 0 20 20" width="16" height="16" aria-hidden="true"><path d="M10 2l1.6 4.4L16 8l-4.4 1.6L10 14l-1.6-4.4L4 8l4.4-1.6z" fill="currentColor"/></svg>Hulp bij het omschrijven? Laat Jeff meedenken</button></p>
<details class="fotos-veld"><summary>Voorbeelden van je smaak meesturen (optioneel)</summary>
<p class="fotos-uitleg">Upload tot 6 foto's of screenshots van websites of apps die je mooi vindt, of je logo en huisstijl. Zo weten we welke stijl je zoekt. We gebruiken ze alleen als inspiratie.</p>
<label class="uploadknop" for="fotos">Foto's kiezen</label><input class="verborgen-invoer" id="fotos" name="fotos" type="file" accept="image/jpeg,image/png,image/webp,image/heic" multiple>
<div class="fotos-voorbeeld" id="fotos-voorbeeld" aria-live="polite"></div></details>
<button class="knop geel" type="submit">Verstuur aanvraag</button>
<div class="melding" id="melding" role="status" aria-live="polite"></div>
</form></div></section>
<script>
const CONTACT = ''' + json.dumps({"email": CONFIG["email"], "whatsapp": CONFIG["whatsapp"]}) + r''';
const kanaal = document.getElementById("kanaal");
try { const q = new URLSearchParams(location.search), f0 = document.getElementById("aanvraag");
  if (q.get("pakket")) { const o = [...f0.pakket.options].find(x => x.text === q.get("pakket")); if (o) f0.pakket.value = o.text; }
  if (q.get("idee")) f0.idee.value = q.get("idee").slice(0, 600); } catch (_) {}
if (CONTACT.email) kanaal.textContent = "Liever direct mailen? " + CONTACT.email;
/* Foto's van de smaak van de klant: verkleinen in de browser, uploaden naar Supabase Storage, aanvraag opslaan. */
const SB = {url: "https://eyrfizayagcwaxbxyeuh.supabase.co", key: "sb_publishable_OXoe3_8uenkdDoeuCq4G9A_MXOTuWjb", bucket: "website-aanvraag"};
const fotoInput = document.getElementById("fotos"), fotoVb = document.getElementById("fotos-voorbeeld");
let fotos = [];
fotoInput.addEventListener("change", () => {
  const nieuw = [...fotoInput.files].filter(x => /^image\//.test(x.type) || /\.heic$/i.test(x.name));
  fotos = fotos.concat(nieuw).slice(0, 6);
  if (fotos.length + nieuw.length > 6) fotoVb.dataset.melding = "Maximaal 6 foto's.";
  fotoInput.value = ""; toonFotos();
});
function toonFotos() {
  fotoVb.innerHTML = "";
  fotos.forEach((x, i) => {
    const w = document.createElement("figure"), img = document.createElement("img"), b = document.createElement("button");
    img.src = URL.createObjectURL(x); img.alt = x.name; b.type = "button"; b.textContent = "×"; b.setAttribute("aria-label", "Verwijder foto");
    b.onclick = () => { fotos.splice(i, 1); toonFotos(); };
    w.append(img, b); fotoVb.append(w);
  });
}
function verklein(file) {
  return new Promise((ok, fout) => {
    const img = new Image(); img.onload = () => {
      const s = Math.min(1, 1600 / Math.max(img.width, img.height)), c = document.createElement("canvas");
      c.width = Math.round(img.width * s); c.height = Math.round(img.height * s);
      c.getContext("2d").drawImage(img, 0, 0, c.width, c.height);
      c.toBlob(b => b ? ok(b) : fout(new Error("blob")), "image/jpeg", 0.82);
    }; img.onerror = fout; img.src = URL.createObjectURL(file);
  });
}
async function verstuurOnline(d) {
  const id = crypto.randomUUID(), paden = [];
  for (let i = 0; i < fotos.length; i++) {
    const blob = await verklein(fotos[i]), pad = id + "/" + (i + 1) + ".jpg";
    const r = await fetch(SB.url + "/storage/v1/object/" + SB.bucket + "/" + pad, {method: "POST", headers: {apikey: SB.key, Authorization: "Bearer " + SB.key, "Content-Type": "image/jpeg", "x-upsert": "false"}, body: blob});
    if (!r.ok) throw new Error("upload " + r.status);
    paden.push(SB.url + "/storage/v1/object/public/" + SB.bucket + "/" + pad);
  }
  const r = await fetch(SB.url + "/rest/v1/website_aanvragen", {method: "POST", headers: {apikey: SB.key, Authorization: "Bearer " + SB.key, "Content-Type": "application/json", Prefer: "return=minimal"},
    body: JSON.stringify({id, naam: d.naam, email: d.email, bedrijf: d.bedrijf || null, pakket: d.pakket || null, idee: d.idee, fotos: paden, taal: document.documentElement.lang || null, pagina: location.pathname})});
  if (!r.ok) throw new Error("opslaan " + r.status);
}
document.getElementById("aanvraag").addEventListener("submit", async e => {
  e.preventDefault();
  const f = e.target, m = document.getElementById("melding"), knop = f.querySelector('button[type="submit"]');
  const d = Object.fromEntries(new FormData(f));
  m.className = "melding aan"; m.innerHTML = "";
  if (d["bot-veld"]) return;
  if (!d.naam || !d.email || !d.idee || !f.email.checkValidity()) { m.textContent = "Vul je naam, een geldig e-mailadres en je idee in."; return; }
  knop.disabled = true; m.textContent = "Je aanvraag wordt verstuurd…";
  try {
    await verstuurOnline(d);
    if (window.goatcounter && goatcounter.count) goatcounter.count({path: "aanvraag-verstuurd", event: true});
    f.reset(); fotos = []; toonFotos();
    location.href = "bedankt?n=" + encodeURIComponent(d.naam.split(" ")[0]);
    return;
  } catch (_) { knop.disabled = false; m.textContent = ""; }
  const tekst = `Aanvraag ${d.pakket}\nNaam: ${d.naam}\nE-mail: ${d.email}\nBedrijf: ${d.bedrijf||"-"}\nSoort: ${d.pakket}\n\nIdee:\n${d.idee}`;
  if (fotos.length) m.append(Object.assign(document.createElement("p"), {textContent: "Stuur je voorbeeldfoto's als bijlage mee in je mail."}));
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
        "desc": "Website of webshop laten maken onder de marktprijs: one-page vanaf €495, bedrijfswebsite vanaf €995, webshop vanaf €1.950. Snel en vindbaar in Google.",
        "h1": "Website laten maken", "intro": "Snelle, vindbare websites en webshops voor ondernemers. Vaste prijs vooraf, ruim onder wat bureaus vragen.",
        "markt": ("Een eenvoudige website kost volgens Trustoo gemiddeld €500 tot €2.000, een geavanceerde website €2.000 tot €5.000 en een maatwerkwebsite €10.000 of meer.",
                  "https://trustoo.nl/kosten/webdesign-kosten/", "Trustoo, Wat kost een website laten maken? (aangepast 03-11-2026)"),
        "pakketten": [
            ("One-page", 495, "3–5 dagen", ["1 pagina met alle info", "Contactformulier", "Mobielvriendelijk en snel", "Basis-SEO en Google-koppeling"]),
            ("Bedrijfswebsite", 995, "2–3 weken", ["Tot 6 pagina's", "Teksten op Google afgestemd", "Contact- en offerteformulier", "Snelheid en Core Web Vitals in orde", "Gratis hosting mogelijk"]),
            ("Webshop", 1950, "3–5 weken", ["Tot 50 producten ingericht", "iDEAL en andere betaalmethoden", "Verzending en btw ingesteld", "Je beheert zelf je producten"]),
        ],
        "extra": [("Website-onderhoud", "€29 / maand", "Updates, back-ups, kleine wijzigingen tot 30 min per maand"),
                  ("Extra pagina", "€95", "Per pagina, inclusief SEO-tekst")],
        "faq": [("Wat kost een website laten maken?", "Bij ons begint een one-page website bij €495, een bedrijfswebsite met maximaal 6 pagina's bij €995 en een webshop bij €1.950. Alle prijzen zijn eindprijzen, er komt geen btw bij. Ter vergelijking: volgens Trustoo kost een eenvoudige website in Nederland gemiddeld €500 tot €2.000. Je krijgt eerst een gratis concept en daarna een vaste prijs, dus je weet vooraf precies wat je betaalt."),
                ("Word ik gevonden in Google?", "Elke site bouwen we snel, mobielvriendelijk en met de technische basis die Google verwacht: duidelijke paginatitels, goede koppen, een sitemap en een koppeling met Google Search Console. We schrijven de teksten rond de zoekwoorden die jouw klanten echt gebruiken. Een toppositie kan niemand garanderen, want dat hangt ook af van je concurrentie en je reviews, maar je begint met een site die Google goed kan lezen."),
                ("Wat kost een webshop laten maken?", "Volgens de kostengids van Searchlab (2026) betaal je bij een freelancer meestal €2.000 tot €8.000 en bij een bureau voor het mkb €5.000 tot €15.000. Bij ons begint een webshop bij €1.950 (geen btw erbij), met tot 50 producten ingericht. Platformkosten komen daar los bij en staan vooraf in de offerte."),
                ("Wat kost een website laten maken in België?", "Volgens de prijsgids van Lunidev (2026) kost een professionele bedrijfswebsite in België €2.000 tot €6.000 en een webshop €4.000 tot €15.000 of meer. Bij ons begint een bedrijfswebsite bij €995 en een webshop bij €1.950. Alle prijzen zijn eindprijzen, er komt geen btw bij."),
                ("Wat kost een website per maand?", "Hosting kan voor de meeste kleine sites gratis. Een domeinnaam kost meestal €10 tot €25 per jaar, die betaal je rechtstreeks aan de registrar. Onderhoud is optioneel vanaf €29 per maand: daarvoor houden wij de site up-to-date, maken we back-ups en voeren we kleine wijzigingen tot 30 minuten per maand voor je door. Zonder onderhoud betaal je dus alleen je domeinnaam."),
                ("Ben ik eigenaar van de website?", "Ja. De site, het domein en de inhoud staan op jouw naam. Je zit niet vast aan een websitebouwer of aan ons: wil je later met een andere partij verder, dan neem je alles mee. Teksten en foto's die we voor je maken of plaatsen, mag je ook elders gebruiken, bijvoorbeeld op social media of in een brochure."),
                ("Hoe snel is mijn website klaar?", "Een one-page website is meestal binnen 3 tot 5 dagen klaar en een bedrijfswebsite binnen 2 tot 3 weken. Je krijgt eerst een gratis concept, daarna een vaste prijs en een planning. Hoe snel je teksten, foto's en feedback aanlevert, bepaalt mee hoe snel de site live staat. Heb je nog geen teksten, dan schrijven we die op basis van een korte intake."),
                ("Kan ik de website later uitbreiden?", "Ja. Een extra pagina kost €95 per stuk, inclusief een SEO-tekst die op Google is afgestemd. Denk aan een pagina per dienst, een Engelstalige versie of een pagina met projecten. Begin je met een one-page website, dan kunnen we die later ook uitbouwen tot een bedrijfswebsite. Wat er al staat, blijft staan; je betaalt alleen voor wat erbij komt."),
                ("Staat de btw erbij?", "Nee. Alle prijzen op onze site zijn eindprijzen: er komt geen btw bij. Wat je in de offerte ziet, is wat je betaalt voor ons werk. Externe kosten, zoals een domeinnaam of de kosten van een betaalprovider, betaal je rechtstreeks aan die partij. Die staan vooraf in de offerte, zodat je niet voor verrassingen komt te staan.")],
        "secties": [
            ("Wat zit er wel en niet in de prijs?",
             "<div class='scroll'><table class='tabel vergelijk'><tr><th>Onderdeel</th><th>One-page</th><th>Bedrijfswebsite</th></tr>"
             "<tr><td>Aantal pagina's</td><td>1</td><td>tot 6</td></tr>"
             "<tr><td>Mobielvriendelijk en snel</td><td>ja</td><td>ja</td></tr>"
             "<tr><td>Contactformulier</td><td>ja</td><td>ja, plus offerteformulier</td></tr>"
             "<tr><td>Technische basis voor Google</td><td>ja</td><td>ja, met teksten op zoekwoorden afgestemd</td></tr>"
             "<tr><td>Klaar in</td><td>3–5 dagen</td><td>2–3 weken</td></tr></table></div>"
             "<p>Niet in de pakketprijs: een domeinnaam (meestal €10 tot €25 per jaar), een extra pagina (€95) en optioneel onderhoud (vanaf €29 per maand). Hosting kan voor de meeste kleine sites gratis. Dit staat allemaal vooraf in de offerte.</p>"),
            ("Wat kost je website over 3 jaar?",
             "<p>Een eerlijke totaalprijs, voorbeeld voor een bedrijfswebsite tot 6 pagina's:</p>"
             "<div class='scroll'><table class='tabel'><tr><th>Post</th><th>Bedrag</th></tr>"
             "<tr><td>Bedrijfswebsite tot 6 pagina's (eenmalig)</td><td>€995</td></tr>"
             "<tr><td>Hosting voor een kleine site</td><td>€0 (gratis hosting mogelijk)</td></tr>"
             "<tr><td>Domeinnaam, 3 jaar (eigen kosten, op jouw naam)</td><td>± €30 – €75</td></tr>"
             "<tr><td>Onderhoud (optioneel), 36 × €29</td><td>€1.044</td></tr>"
             "<tr><td><b>Totaal over 3 jaar</b></td><td><b>± €1.025 – €1.070 zonder onderhoud, ± €2.069 – €2.114 met onderhoud</b></td></tr></table></div>"
             "<p>Ter vergelijking: bij een websitebouwer betaal je elke maand zolang de site bestaat, en de site is niet van jou. Bij ons betaal je de bouw één keer en ben je eigenaar.</p>"),
            ("Zo werkt het",
             "<ol class='stappen-licht'><li>Je vertelt per mail wat je doet en wat de site moet bereiken.</li>"
             "<li>Je krijgt een gratis concept binnen 48 uur, zodat je ziet hoe het eruit kan zien.</li>"
             "<li>Je krijgt een vaste prijs. Na akkoord bouwen we de site.</li>"
             "<li>Jij controleert alles, daarna gaat de site live.</li></ol>")],
        "rel": [("webshop-laten-maken.html", "Webshop laten maken"), ("goedkope-website-laten-maken.html", "Goedkope website laten maken"), ("website-laten-maken-horeca.html", "Website voor horeca"), ("website-laten-maken-kapper.html", "Website voor kapsalon"), ("chatbot-laten-maken.html", "AI-chatbot voor je site")],
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
        "faq": [("Wat kost een game laten maken?", "Een eenvoudige mobiele game begint in Nederland rond €10.000 (Juego Studios, 2026). Bij ons begint een merkgame voor de browser bij €1.950, een casual game bij €4.950 en een 2D-game met levels bij €9.950. Alle prijzen zijn eindprijzen, er komt geen btw bij."),
                ("Welke games maken jullie?", "Casual 2D-games: puzzels, quizzen, reactie- en arcadespellen. Dat kan een merkgame zijn die in de browser draait, bijvoorbeeld voor een actie of beurs, een casual game voor iPhone en Android, of een 2D-game met meerdere levels en eigen personages. Ons eigen voorbeeld is de puzzelgame Koffer Vol!. Grote 3D-games of online multiplayer doen we niet; daar zijn gespecialiseerde studio's beter voor."),
                ("Kan ik geld verdienen met mijn game?", "Ja. We kunnen advertenties of aankopen in de game inbouwen, zoals extra levels, munten of het uitzetten van reclame. Dat doen we volgens de regels van Apple en Google, die een deel van de opbrengst van aankopen in de app inhouden. Wat goed werkt, hangt af van je spelers en je doel. In het concept laten we zien hoe het verdienmodel in de game past, zonder dat het spelplezier eronder lijdt."),
                ("Ben ik eigenaar van de game?", "Ja. Na de laatste betaling zijn de code, de vormgeving en de game zelf van jou. Komt de game in de App Store of Google Play, dan publiceren we hem op jouw eigen ontwikkelaarsaccounts, zodat de spelers, reviews en opbrengsten altijd bij jou blijven. Wil je later met een andere partij verder, dan kan dat zonder dat je opnieuw hoeft te beginnen.")],
        "rel": [("merkgame-laten-maken-kerst.html", "Merkgame voor kerst"), ("apps.html", "Onze eigen games"), ("app-laten-maken-kosten.html", "Wat kost een app?")],
    },
    {
        "slug": "ai-automatisering", "kort": "AI & automatisering", "kleur": "#0E7C86",
        "titel": "AI-chatbot en automatisering vanaf €395 | Collens Group",
        "desc": "Bespaar uren per week: automatisering vanaf €395, AI-chatbot op je eigen kennis vanaf €995, AI-assistent met meerdere koppelingen vanaf €1.950.",
        "h1": "AI-chatbot en automatisering laten maken", "intro": "Laat terugkerend werk vanzelf gaan: mails, offertes, planning, social media en klantvragen. Met AI-tools die je bestaande apps aan elkaar koppelen.",
        "markt": ("Een AI-agent met no-code tools zoals Zapier of Make kost in Nederland eenmalig €2.000 tot €8.000.",
                  "https://searchlab.nl/kosten/wat-kost-een-ai-agent-laten-bouwen", "Searchlab, Wat kost een AI-agent laten bouwen (2026)"),
        "pakketten": [
            ("Automatisering", 395, "2–5 dagen", ["1 workflow, bijv. formulier → CRM → mail", "Koppelt je bestaande apps", "Getest en gedocumenteerd"]),
            ("AI-chatbot", 995, "1 week", ["Beantwoordt vragen op je website", "Getraind op je eigen teksten", "Doorsturen naar jou bij twijfel"]),
            ("AI-assistent", 1950, "2–4 weken", ["Meerdere workflows en koppelingen", "Mail, agenda, documenten en CRM", "Jij houdt altijd de eindcontrole"]),
        ],
        "extra": [("Extra workflow", "vanaf €195", "Per extra automatisering"),
                  ("Beheer", "€49 / maand", "Monitoring en kleine aanpassingen")],
        "faq": [("Wat kost een AI-chatbot laten maken?", "Een AI-chatbot die vragen op je website beantwoordt, getraind op je eigen teksten, begint bij ons bij €995 (geen btw erbij) en is in 1 week klaar. De kosten van de AI-dienst zelf hangen af van het gebruik en staan vooraf in de offerte."),
                ("Wat kost AI-automatisering per maand?", "Daarnaast betaal je het gebruik van de AI-dienst en de tools zelf. Bij de meeste kleine bedrijven is dat een paar euro tot enkele tientjes per maand, afhankelijk van het gebruik. We schatten het vooraf en zetten het in de offerte. Beheer door ons is optioneel vanaf €49 per maand."),
                ("Is mijn data veilig?", "Ja, daar zorgen we voor. We werken alleen met officiële koppelingen van de tools die je al gebruikt en vragen nooit om je wachtwoorden: jij logt zelf in en geeft toestemming. We geven een workflow alleen toegang tot wat hij echt nodig heeft. Jij bepaalt welke informatie een chatbot of workflow gebruikt, en je kunt die toegang altijd zelf weer intrekken. Gaat het om persoonsgegevens van klanten, dan richten we het in volgens de AVG en spreken we vooraf af waar de gegevens worden opgeslagen."),
                ("Hoe snel is het klaar?", "Een losse automatisering staat meestal binnen 2 tot 5 dagen, een AI-chatbot in ongeveer 1 week en een AI-assistent met meerdere koppelingen in 2 tot 4 weken. De klok begint te lopen na de intake, als we weten welke apps je gebruikt en hoe je werk nu verloopt. Voordat iets live gaat, testen we het met echte voorbeelden uit jouw bedrijf en laten we je zien wat er gebeurt."),
                ("Wat kan ik automatiseren?", "Bijna alles wat steeds op dezelfde manier gaat. Denk aan aanvragen van je website automatisch in je CRM of spreadsheet zetten, offertes klaarzetten op basis van een formulier, afspraken inplannen en herinneringen sturen, social media vooruit inplannen of elke week een rapportage laten maken. Twijfel je of iets kan? Beschrijf in je aanvraag wat je nu met de hand doet, dan zeggen we eerlijk of het de moeite waard is om te automatiseren.")],
        "secties": [
            ("Welk pakket past bij jou?",
             "<ul><li><strong>Automatisering (vanaf €395):</strong> je krijgt steeds hetzelfde formulier, mailtje of overzicht en wilt dat dit vanzelf gaat.</li>"
             "<li><strong>AI-chatbot (vanaf €995):</strong> klanten stellen steeds dezelfde vragen over openingstijden, prijzen of levertijden. De chatbot beantwoordt ze op basis van jouw eigen teksten en stuurt twijfelgevallen door naar jou. <a href='chatbot-laten-maken.html'>Lees meer over de AI-chatbot</a>.</li>"
             "<li><strong>AI-assistent (vanaf €1.950):</strong> meerdere workflows en koppelingen met mail, agenda, documenten en CRM, waarbij jij de eindcontrole houdt.</li></ul>"
             "<p>Niet zeker? Beschrijf kort wat je elke week opnieuw doet, dan zeggen we eerlijk welk pakket past, of dat je het zonder ons kunt oplossen.</p>"),
            ("Zo werkt het",
             "<ol class='stappen-licht'><li>Je vertelt per mail welk werk steeds terugkomt.</li><li>Je krijgt een gratis concept en een vaste prijs.</li>"
             "<li>Na akkoord bouwen we het en testen we het samen met jou.</li><li>Daarna gaat het live.</li></ol>")],
        "rel": [("chatbot-laten-maken.html", "AI-chatbot laten maken"), ("website-laten-maken.html", "Website laten maken"), ("app-laten-maken-kosten.html", "Wat kost een app?")],
    },
]

def dienst_pagina(d):
    kaarten = "".join(f'''<article class="pakket{' mid' if i == 1 else ''}"><h3>{e(n)}</h3>
<div class="prijs">€{f"{p:,}".replace(",", ".")}<small>vanaf, eindprijs, geen btw erbij</small></div>
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
<p style="margin-top:20px"><a class="knop geel" href="index.html#contact">Vraag je gratis concept aan</a></p>
<h2>Extra&rsquo;s en onderhoud</h2><table class="lijst">{extra}</table>
<p class="noot">Alle prijzen zijn eindprijzen: er komt geen btw bij. Bij &ldquo;vanaf&rdquo; hoort het pakket zoals hierboven beschreven; wijkt jouw project daarvan af, dan krijg je vooraf een vaste prijs op maat. Externe kosten (zoals domein, tools of store-accounts) staan vooraf in de offerte.</p>
{"".join(f"<h2>{e(h)}</h2>{x}" for h, x in d.get("secties", []))}
<h2>Veelgestelde vragen</h2>{faq_html(d["faq"])}
<p style="margin-top:32px"><a class="knop geel" href="index.html#contact">Vraag een vaste prijs aan</a></p>
{f'<p class="bron" style="margin-top:22px">Zie ook: ' + " · ".join(f'<a href="{h}"{" rel=\"noopener\"" if h.startswith("http") else ""}>{e(t)}</a>' for h, t in d["rel"] + (boek_rel() if d["slug"] == "ai-automatisering" else [])) + '</p>' if d.get("rel") else ""}
</article>''', crumbs=[("Home", "index.html"), (d["kort"], f'{d["slug"]}.html')],
        extra_ld=[{"@type": "Service", "name": d["h1"], "provider": {"@id": "#org"}, "areaServed": ["NL", "BE"], "offers": offers}, faq_ld(d["faq"])])

ICONEN = {
 "app": '<svg viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><rect x="6" y="2.5" width="12" height="19" rx="3"/><path d="M10.5 18.5h3"/></svg>',
 "web": '<svg viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><rect x="2.5" y="4" width="19" height="15" rx="2.5"/><path d="M2.5 8.5h19M6 6.3h.01M8.5 6.3h.01"/></svg>',
 "game": '<svg viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M7 8h10a4.5 4.5 0 0 1 4.4 5.4l-.8 3.8a2.3 2.3 0 0 1-4 1L14.8 16H9.2l-1.8 2.2a2.3 2.3 0 0 1-4-1l-.8-3.8A4.5 4.5 0 0 1 7 8z"/><path d="M8 11v3M6.5 12.5h3M15.5 12h.01M17.5 13.5h.01"/></svg>',
 "ai": '<svg viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M12 3l1.8 4.6L18.5 9l-4.7 1.6L12 15l-1.8-4.4L5.5 9l4.7-1.4z"/><path d="M18 15l.9 2.1L21 18l-2.1.9L18 21l-.9-2.1L15 18l2.1-.9z"/></svg>',
}
def icoon(naam):
    n = naam.lower()
    k = "app" if "app" in n else "game" if ("game" in n or "jeu" in n or "jueg" in n) else "ai" if ("ai" in n or "ki" in n or "ia" in n) else "web"
    return f'<span class="dienst-ico">{ICONEN[k]}</span>'

def diensten_blok():
    SUB = {"Websites": "Bedrijfssites en webshops", "Games": "Merkgames en casual games", "AI & automatisering": "Chatbots en slimme workflows"}
    rest = [(d["kort"], SUB.get(d["kort"], d["pakketten"][0][0]), f'vanaf €{d["pakketten"][0][1]:,}'.replace(",", "."), f'{d["slug"]}.html', d["kleur"]) for d in DIENSTEN]
    items = rest[:1] + [("Apps", "Voor iPhone en Android", "vanaf €3.150", "app-laten-maken-kosten.html", "#14213D")] + rest[1:]
    return '<div class="diensten">' + "".join(
        f'<a class="dienst" href="{h}" style="--k:{k}">{icoon(n)}<span class="dienst-naam">{e(n)}</span><span class="dienst-sub">{e(s)}</span><span class="dienst-prijs">{e(p)}</span></a>'
        for n, s, p, h, k in items) + '</div>'

APP_BETEKENIS = {
    "App": ("Wat dit voor jouw app betekent",
        "<p>LubbyC is geen demo maar een echte app met accounts, kaart, chat en meerdere talen. Dezelfde bouwstenen gebruiken we voor klanten, dus je betaalt niet voor uitzoekwerk dat al gedaan is.</p>"
        "<ul class='kenmerken'><li>Eén app voor iPhone én Android, dus niet dubbel betalen.</li><li>Vaste prijs vooraf: een basis-app vanaf €3.150, een standaard-app met accounts en database vanaf €6.750. Er komt geen btw bij.</li><li>Elke week een testversie op je telefoon, zodat je ziet wat je krijgt.</li><li>Eerst een gratis concept binnen 48 uur, voordat je iets beslist.</li></ul>"
        "<p>Meer over kosten en doorlooptijd lees je in <a href='app-laten-maken-kosten.html'>wat een app kost</a> en bij <a href='mvp-app-laten-maken.html'>een MVP laten maken</a>. Twijfel je tussen een app en een website? Kijk dan bij <a href='app-of-website.html'>app of website</a>.</p>"),
    "Game": ("Wat dit voor jouw game betekent",
        "<p>We maken games niet alleen voor onszelf. Een eigen game of een mini-game in jouw huisstijl werkt goed als actie, als beloning voor klanten of als product op zich.</p>"
        "<ul class='kenmerken'><li>Een game in jouw merk, bijvoorbeeld voor een campagne, vanaf €1.950.</li><li>Een speelbare versie die je op je telefoon kunt proberen voordat je goedkeurt.</li><li>Vaste prijs en vaste planning: je weet vooraf wat het kost en wanneer het klaar is.</li><li>Hulp bij publicatie in Google Play of als webversie.</li></ul>"
        "<p>Bekijk de mogelijkheden op de pagina <a href='game-laten-maken.html'>game laten maken</a>, of lees hoe een <a href='merkgame-laten-maken-kerst.html'>merkgame</a> werkt.</p>"),
    "Kinderserie": ("Wat dit voor jouw project betekent",
        "<p>Manu en Khanun laat zien wat er met AI-animatie mogelijk is voor een klein team. Diezelfde kennis van AI en automatisering zetten we in voor bedrijven die tijd willen besparen.</p>"
        "<ul class='kenmerken'><li>AI-oplossingen zoals een chatbot op je eigen website, vanaf €995.</li><li>Automatisering van terugkerend werk, vanaf €395.</li><li>Vaste prijs, geen verrassingen achteraf.</li><li>Eerst een gratis kennismaking en een voorstel op maat.</li></ul>"
        "<p>Lees meer over <a href='chatbot-laten-maken.html'>een chatbot laten maken</a> of over <a href='ai-automatisering.html'>AI en automatisering</a>. Alle prijzen staan op de <a href='prijzen.html'>prijzenpagina</a>.</p>"),
}


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
    ("Hulp bij het omschrijven? Laat Jeff meedenken", "Need help describing it? Let the advisor help"),
    ("Kun je me helpen mijn aanvraag goed te omschrijven?", "Can you help me describe my request well?"),
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
    ("Voorbeelden van je smaak meesturen (optioneel)", "Send examples of your style (optional)"),
    ("Voorbeelden van je smaak (optioneel)", "Examples of your style (optional)"),
    ("Vertel wat je wilt laten maken", "Tell us about your project"),
    ("Een paar zinnen zijn genoeg. Je krijgt binnen 48 uur een reactie met een paar korte vragen, en daarna een gratis concept en een vaste prijs. Alles per mail en zonder verplichtingen.",
     "A few sentences are enough. Within 48 hours you get a reply with a few short questions, then a free concept and a fixed price. All by email, without obligation."),
    ("<li>Vaste prijs vooraf, eindprijs zonder btw erbij</li><li>Gratis concept voordat je iets betaalt</li><li>Snel live, zonder lange trajecten</li>",
     "<li>Fixed price up front, no VAT added</li><li>Free concept before you pay anything</li><li>Live fast, no long projects</li>"),
    ("<option>Website</option><option>Webshop</option>", "<option>Website</option><option>Web shop</option>"),
    ("Wat wil je laten maken, en voor wie? Bijvoorbeeld: een website voor mijn kapsalon met online afspraken.", "What do you need, and for whom? For example: a website for my hair salon with online booking."),
    (">Foto's kiezen<", ">Choose photos<"),
    ("Upload tot 6 foto's of screenshots van websites of apps die je mooi vindt, of je logo en huisstijl. Zo weten we welke stijl je zoekt. We gebruiken ze alleen als inspiratie.",
     "Upload up to 6 photos or screenshots of websites or apps you like, or your logo and brand colours. That shows us the style you're after. We only use them as inspiration."),
    ('"Maximaal 6 foto\'s."', '"Up to 6 photos."'), ('"Verwijder foto"', '"Remove photo"'),
    ('"Je aanvraag wordt verstuurd…"', '"Sending your request…"'),
    ('"Stuur je voorbeeldfoto\'s als bijlage mee in je mail."', '"Please attach your example photos to your email."'),
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
    ("Websites", [("One-page website", "€495", "3–5 days"), ("Business website (up to 6 pages)", "€995", "2–3 weeks"), ("Web shop (up to 50 products)", "€1,950", "3–5 weeks")]),
    ("Apps (iOS and Android)", [("Basic / MVP app (up to 5 screens)", "€3,150", "3–5 weeks"), ("Standard app (accounts, database, push)", "€6,750", "6–10 weeks"), ("Custom / Pro app (payments, admin, roles)", "€13,050", "10–16+ weeks")]),
    ("Games (casual 2D)", [("Branded mini-game (web)", "€1,950", "2–3 weeks"), ("Casual game", "€4,950", "4–6 weeks"), ("2D game with levels", "€9,950", "8–12 weeks")]),
    ("AI & automation", [("Automation (1 workflow)", "€395", "2–5 days"), ("AI chatbot trained on your content", "€995", "1 week"), ("AI assistant (multiple workflows)", "€1,950", "2–4 weeks")]),
]
EN_FAQ = [
    ("Do you work with clients outside the Netherlands?", "Yes. We work fully online, by email and video, with clients worldwide, in English or Dutch. Prices are the same final prices in euros everywhere, with no VAT added. Time zones are rarely a problem: most of the work is done in writing, and calls are planned at a time that suits you."),
    ("Why are your prices lower than most agencies?", "We build one app for iPhone and Android at once, reuse proven building blocks and automate a lot of the work. That saves hours, and you see the savings in the price."),
    ("Do I own the result?", "Yes. After the final payment the code, design and content are yours. Apps are published on your own Apple and Google accounts, and websites and domains are registered in your name. If you later want to work with someone else, you take everything with you."),
    ("How do I pay?", "For apps, in three parts: 40% when you approve the quote, 40% when you approve the test version and 20% on delivery. That way you never pay everything up front and always see results first. For smaller jobs, such as a website or automation, the payment terms are stated in the quote. All prices are final prices in euros."),
    ("What does it cost after launch?", "Apple charges $99 per year and Google $25 once. Hosting for small projects is often free to $25 per month. Maintenance is optional. All of this is listed in your quote."),
    ("Can I see something before I pay?", "Yes. You get a free concept within 48 hours, designed specifically for your business, with no obligation. Only if you like it do we make a fixed price. If it is not for you, you have paid nothing and are not committed to anything."),
]

def en_pages(pages):
    price_html = "".join(
        f'<div class="prijsblok"><h3>{e(cat)}</h3><table class="lijst">' +
        "".join(f'<tr><td>{e(n)}<small>Ready in {e(t)}</small></td><td>from {e(p)}</td></tr>' for n, p, t in rows) +
        '</table></div>' for cat, rows in EN_PRICES)
    services = '<div class="diensten">' + "".join(
        f'<a class="dienst" href="{h}" style="--k:{k}">{icoon(n)}<span class="dienst-naam">{e(n)}</span><span class="dienst-sub">{e(s)}</span><span class="dienst-prijs">{e(p)}</span></a>'
        for n, s, p, h, k in EN_SERVICES) + '</div>'
    en_offers = [{"@type": "Offer", "name": n, "price": int(p.replace("€", "").replace(",", "")), "priceCurrency": "EUR"} for _, rows in EN_PRICES for n, p, _ in rows]
    pages.append(page("en.html", "Websites, apps, games and AI, fixed prices | " + CONFIG["naam"],
        "We build websites from €495, apps from €3,150, games from €1,950 and AI automation from €395 for clients worldwide. Fixed price and a free concept first.",
        f'''<section class="hero" aria-labelledby="kop"><div class="wrap"><div>
<h1 id="kop">Your idea.<br>Live in no time.</h1>
<p class="lead">Free concept within 48 hours. Websites from €495, plus apps, games and AI. Fixed price.</p>
<div class="acties"><a class="knop geel" href="#contact">Get a free quote</a><a class="zacht" href="#services">See what we build</a></div><ul class="vertrouwen"><li><svg viewBox="0 0 20 20" width="18" height="18" aria-hidden="true"><circle cx="10" cy="10" r="10" fill="#E3EBFA"/><path d="M6 10.3l2.6 2.6L14.2 7.4" fill="none" stroke="#2457D6" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg>Fixed price up front</li><li><svg viewBox="0 0 20 20" width="18" height="18" aria-hidden="true"><circle cx="10" cy="10" r="10" fill="#E3EBFA"/><path d="M6 10.3l2.6 2.6L14.2 7.4" fill="none" stroke="#2457D6" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg>Free concept first</li><li><svg viewBox="0 0 20 20" width="18" height="18" aria-hidden="true"><circle cx="10" cy="10" r="10" fill="#E3EBFA"/><path d="M6 10.3l2.6 2.6L14.2 7.4" fill="none" stroke="#2457D6" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg>Fast delivery</li></ul></div>
<div class="etalage"><figure class="tel-links"><img src="img/koffer-spel.jpg" alt="Koffer Vol! puzzle game" width="240" height="480"></figure><figure class="tel-midden"><img src="img/lubbyc-kaart.jpg" alt="LubbyC travel app" width="240" height="480" fetchpriority="high"></figure><figure class="tel-rechts"><img src="img/eiland-rood.jpg" alt="Island Express driving game" width="240" height="480"></figure></div></div></section>

<section id="services" class="wit" aria-labelledby="s-kop"><div class="wrap">
<div class="intro"><h2 id="s-kop">What we build</h2><p>Everything digital under one roof, at fixed prices.</p></div>
{services}
<div class="feiten" style="margin-top:48px">
<div><h3>Fixed price</h3><p>You know the price before we start. Extra work only with your approval.</p></div>
<div><h3>Fast</h3><p>One-page site in 3–5 days, automation in 2–5 days, chatbot in about 1 week.</p></div>
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

<section aria-labelledby="f-kop"><div class="wrap smal">
<h2 id="f-kop">Frequently asked questions</h2>{faq_html(EN_FAQ)}</div></section>
{contact_en()}''', crumbs=[("Home", "en.html")], extra_ld=[faq_ld(EN_FAQ), {"@type": "Service", "name": "Websites, apps, games and AI automation", "provider": {"@id": "#org"}, "areaServed": "Worldwide", "offers": en_offers}],
        lang="en", alt=("index.html", "en.html")))

    en_apps = [
        ("LubbyC", "App · Coming soon on Google Play", "Meet travelers nearby. Plan dinners, beaches and trips together in Thailand. Available in 13 languages.", "img/lubbyc-icon.png", "#0E4433", "L"),
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
<h2 style="margin-top:48px">What this means for your project</h2>
<p>Everything on this page was designed, built and published by us. That is why we know what an app, game or AI solution really costs and where the pitfalls are. You benefit from that experience.</p>
<ul class="kenmerken"><li><strong>App:</strong> a basic app from €3,150 and a standard app from €6,750. Fixed price, one build for iPhone and Android. See <a href="en-app-development.html">app development</a>.</li><li><strong>Game:</strong> a branded casual game from €1,950, playable on your phone before you approve it.</li><li><strong>AI and automation:</strong> from €395, including a chatbot trained on your own content from €995. See <a href="en-ai-chatbot.html">AI chatbot</a>.</li><li><strong>Website:</strong> from €495. See <a href="en-website-design.html">website design</a>.</li></ul>
<p>You always start with a free concept within 48 hours, so you can see what you get before you decide. All prices are in euros and are final.</p>
<p><a class="knop geel" href="en.html#contact">Build something with us</a></p></div></section>''',
        crumbs=[("Home", "en.html"), ("Our work", "en-projects.html")], lang="en", alt=("apps.html", "en-projects.html")))

    pages.append(page("en-lubbyc-privacy.html", "LubbyC privacy policy", "How the LubbyC travel app handles your data: what we collect, why, who receives it and your rights.",
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
        crumbs=[("Home", "en.html"), ("LubbyC privacy", "en-lubbyc-privacy.html")], lang="en"))

APP_PAKKETTEN = [
    ("Basis / MVP app", 3150, "3–5 weken", "Je idee snel testen met echte gebruikers. Tot 5 schermen, eenvoudige navigatie en content, strak basisontwerp, publicatieklaar voor iOS of Android. Geen accounts, database of betalingen."),
    ("Standaard app", 6750, "6–10 weken", "Een complete app voor klanten of team. 5 tot 12 schermen, accounts en inloggen, eigen database en API-koppelingen, pushmeldingen, live in App Store én Google Play."),
    ("Maatwerk / Pro app", 13050, "10–16+ weken", "Een volledig digitaal platform. 12+ schermen en complexe flows, uitgebreide backend en beheerdashboard, betalingen en abonnementen, meerdere gebruikersrollen, extra beveiliging."),
]

def schrijf_kennis():
    """Kennis voor de chat-adviseur, uit dezelfde gegevens als de site. Schrijft chatbot/kennis.js."""
    eur = lambda p: "€" + f"{p:,}".replace(",", ".")
    from landings import LANDINGS
    import re as _re
    r = [f"## Over Collens Group\nCollens Group maakt websites, webshops, apps (iPhone en Android tegelijk, met React Native), casual 2D-games en AI-chatbots en automatiseringen. "
         "Voor ondernemers in Nederland, België en wereldwijd (in het Nederlands of Engels). Volledig online, per mail en video. Vaste prijs vooraf, onder het marktgemiddelde. "
         "Alle prijzen zijn eindprijzen: er komt geen btw bij. Contact: " + CONFIG["email"] + ".",
         "## Werkwijze\n1. Intake per mail: een paar korte vragen over idee, doelgroep en budget, geen afspraak nodig.\n2. Gratis concept: een klikbaar concept van 1–3 schermen.\n"
         "3. Voorstel met vaste prijs, planning en precies wat erin zit.\n4. Ontwerp ter goedkeuring.\n5. Bouwen en testen, elke week een testversie.\n6. Live: hulp bij publicatie op het web, in de App Store en Google Play.\n"
         "Elke stap rond je af met een akkoord. Meerwerk alleen na akkoord van de klant.\n"
         "Betalen in drie delen: 40% bij akkoord, 40% bij een goedgekeurde testversie, 20% bij oplevering. Na de laatste betaling zijn code en design van de klant; apps staan op het eigen Apple- en Google-account van de klant.",
         "## Apps (iPhone en Android)\n" + "\n".join(f"- {n}: vanaf {eur(p)}, klaar in {t}. {o}" for n, p, t, o in APP_PAKKETTEN) +
         "\nLosse diensten: ontwikkeling per uur €67,50; schermontwerp (UI/UX, klikbaar prototype vóór de bouw) €675 – €1.800; App Store en Google Play setup €315; koppeling externe API of betaalprovider (bijv. Mollie, Stripe, boekhouding, CRM) €450 – €1.350.\n"
         "Onderhoud per maand (optioneel): Basis Onderhoud €85,50 (monitoring, kritieke bugfixes, kleine iOS- en Android-updates); Groei & Support €265,50 (alles uit Basis plus tot 4 uur kleine aanpassingen en voorrang bij storingen).\n"
         "Externe kosten die de klant zelf betaalt: Apple Developer Program $99 per jaar, Google Play $25 eenmalig, hosting/database vaak gratis tot $25 per maand voor kleine apps.\n"
         "Marktvergelijking: een eenvoudige app kost bij Nederlandse bureaus en freelancers meestal €5.000 – €25.000 (Searchlab 2026)."]
    for d in DIENSTEN:
        r.append(f"## {d['h1']}\n{d['intro']}\n" + "\n".join(f"- {n}: vanaf {eur(p)}, klaar in {t}. Inbegrepen: {'; '.join(items)}." for n, p, t, items in d["pakketten"]) +
                 "\nExtra: " + "; ".join(f"{n} {p} ({s})" for n, p, s in d["extra"]) + "." +
                 f"\nMarkt: {d['markt'][0]}\n" + "\n".join(f"- V: {q} A: {a}" for q, a in d["faq"]) + f"\nPagina: {d['slug']}.html")
    for L in LANDINGS:
        if L["lang"] != "nl": continue
        faq = " ".join(_re.sub(r"<[^>]+>", " ", f"V: {q} A: {a}") for q, a in L.get("faq", []))
        faq = _re.sub(r"\s+", " ", html.unescape(faq))
        r.append(f"## {L['titel'].split(' | ')[0]}\n{L.get('lead', '')}\n{faq}\nPagina: {L['slug']}.html")
    r.append("## Veelgestelde vragen\n" + "\n".join(f"- V: {q} A: {a}" for q, a in FAQ))
    r.append("## Eigen projecten (bewijs van ons werk)\n" + "\n".join(f"- {a['naam']} ({a['soort']}, {a['status']}): {a['kort']} Pagina: app-{a['slug']}.html" for a in APPS if a.get("publiceer")))
    r.append("## Wat we niet doen\nGrote 3D-games en online multiplayer-games. Topposities in Google garanderen. Juridisch of financieel advies.")
    r.append("## Pagina's\nNederlands: index.html (start, met contactformulier op index.html#contact), website-laten-maken.html, goedkope-website-laten-maken.html, webshop-laten-maken.html, website-laten-maken-horeca.html, website-laten-maken-kapper.html, "
             "app-laten-maken-kosten.html, mvp-app-laten-maken.html, game-laten-maken.html, ai-automatisering.html, chatbot-laten-maken.html, apps.html, artikelen.html, privacy.html.\n"
             "Engels: en.html (contact op en.html#contact), en-website-design.html, en-app-development.html, en-ai-chatbot.html, en-ai-automation.html, en-web-shop.html, en-game-development.html, en-pricing.html, en-about.html, en-projects.html. Duits: de.html, Frans: fr.html, Spaans: es.html, Thai: th.html, Birmaans: my.html.")
    tekst = "\n\n".join(r)
    os.makedirs(os.path.join(ROOT, "chatbot"), exist_ok=True)
    with open(os.path.join(ROOT, "chatbot", "kennis.js"), "w", encoding="utf-8") as f:
        f.write("// Automatisch gemaakt door build.py (schrijf_kennis). Niet met de hand bewerken.\nexport const KENNIS = " + json.dumps(tekst, ensure_ascii=False) + ";\n")

CHAT_BLOK = {
    "nl": ("Weet je nog niet precies wat je nodig hebt?", "Geen probleem, daar is Jeff voor, onze AI-adviseur. Vertel wat je wilt bereiken; hij stelt een paar vragen, denkt met je mee en adviseert welke oplossing en welk pakket bij je passen. Dag en nacht, gratis en zonder verplichtingen.", "Vraag het Jeff", "AI-adviseur · 24/7 online · antwoord binnen seconden"),
    "en": ("Not sure exactly what you need?", "No problem, that's what our online advisor is for. Tell it what you want to achieve; it asks a few questions, thinks along with you and recommends the solution and package that fit. Day and night, free and without obligation.", "Ask our advisor", "Online 24/7 · answers in seconds"),
    "de": ("Sie wissen noch nicht genau, was Sie brauchen?", "Kein Problem, dafür gibt es unseren Online-Berater. Erzählen Sie, was Sie erreichen möchten; er stellt ein paar Fragen, denkt mit und empfiehlt die passende Lösung und das passende Paket. Rund um die Uhr, kostenlos und unverbindlich.", "Fragen Sie unseren Berater", "24/7 online · Antwort in Sekunden"),
    "fr": ("Vous ne savez pas encore exactement ce qu'il vous faut ?", "Pas de souci, c'est le rôle de notre conseiller en ligne. Dites-lui ce que vous voulez accomplir ; il pose quelques questions, réfléchit avec vous et recommande la solution et la formule adaptées. Jour et nuit, gratuit et sans engagement.", "Demandez à notre conseiller", "En ligne 24h/24 · réponse en quelques secondes"),
    "es": ("¿Aún no sabes exactamente lo que necesitas?", "No pasa nada, para eso está nuestro asesor en línea. Cuéntale qué quieres conseguir; te hace unas preguntas, piensa contigo y te recomienda la solución y el paquete adecuados. Día y noche, gratis y sin compromiso.", "Pregunta a nuestro asesor", "En línea 24/7 · respuesta en segundos"),
    "th": ("ยังไม่แน่ใจว่าต้องการอะไรใช่ไหม?", "ไม่เป็นไร ที่ปรึกษาออนไลน์ของเราช่วยได้ บอกเราว่าคุณอยากทำอะไรให้สำเร็จ ที่ปรึกษาจะถามคำถามสั้น ๆ ช่วยคิด และแนะนำโซลูชันกับแพ็กเกจที่เหมาะกับคุณ ตลอด 24 ชั่วโมง ฟรีและไม่มีข้อผูกมัด", "ถามที่ปรึกษาของเรา", "ออนไลน์ 24/7 · ตอบภายในไม่กี่วินาที"),
    "my": ("ဘာလိုအပ်သလဲ မသေချာသေးဘူးလား။", "ပြဿနာမရှိပါ၊ ကျွန်ုပ်တို့၏ အွန်လိုင်းအကြံပေးက ကူညီပါမည်။ သင်ရရှိလိုသည်ကို ပြောပြပါ၊ မေးခွန်းအနည်းငယ်မေးပြီး အတူစဉ်းစားကာ သင့်တော်သော ဖြေရှင်းချက်နှင့် ပက်ကေ့ချ်ကို အကြံပြုပါမည်။ နေ့ရောညပါ၊ အခမဲ့ဖြစ်ပြီး တာဝန်ဝတ္တရား မရှိပါ။", "အကြံပေးကို မေးရန်", "24/7 အွန်လိုင်း · စက္ကန့်ပိုင်းအတွင်း ဖြေကြားသည်"),
}
CHAT_CONTACT = {
    "nl": ("Weet je nog niet precies wat je nodig hebt? Jeff, onze AI-adviseur, denkt met je mee.", "Vraag het Jeff"),
    "en": ("Not sure exactly what you need? Our online advisor will help you choose.", "Ask the advisor"),
    "de": ("Sie wissen noch nicht genau, was Sie brauchen? Unser Online-Berater hilft Ihnen.", "Berater fragen"),
    "fr": ("Vous ne savez pas encore ce qu'il vous faut ? Notre conseiller en ligne vous aide.", "Demander au conseiller"),
    "es": ("¿No sabes exactamente lo que necesitas? Nuestro asesor en línea te ayuda.", "Preguntar al asesor"),
    "th": ("ยังไม่แน่ใจว่าต้องการอะไร? ที่ปรึกษาออนไลน์ของเราช่วยคุณเลือกได้", "ถามที่ปรึกษา"),
    "my": ("ဘာလိုအပ်သလဲ မသေချာသေးဘူးလား။ ကျွန်ုပ်တို့၏ အွန်လိုင်းအကြံပေးက ကူညီပါမည်။", "အကြံပေးကို မေးရန်"),
}
CHAT_ICOON = '<svg viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M21 12a8 8 0 0 1-11.6 7.1L4 20.5l1.4-4.9A8 8 0 1 1 21 12z"/><path d="M8.5 11h.01M12 11h.01M15.5 11h.01"/></svg>'

def chat_inbouwen():
    """Chatwidget op elke pagina, en op de startpagina's een duidelijke sectie voor wie nog twijfelt.
    Beide blijven verborgen tot /api/chat meldt dat de adviseur actief is (dus pas na het instellen van de API-sleutel)."""
    shutil.copy(os.path.join(ROOT, "src", "chat.js"), os.path.join(DIST, "chat.js"))
    v = hashlib.md5(open(os.path.join(ROOT, "src", "chat.js"), "rb").read()).hexdigest()[:8]
    homes = {"index.html": "nl", "en.html": "en", "de.html": "de", "fr.html": "fr", "es.html": "es", "th.html": "th", "my.html": "my"}
    for f in os.listdir(DIST):
        if not f.endswith(".html"): continue
        p = os.path.join(DIST, f); h = open(p, encoding="utf-8").read()
        h = h.replace("</body>", f'<script src="chat.js?v={v}" defer></script></body>', 1)
        if f in homes:
            kop, tekst, knop, sub = CHAT_BLOK[homes[f]]
            blok = (f'<section class="chat-blok" data-chat-blok hidden aria-labelledby="chat-kop"><div class="wrap"><div class="chat-blok-in">'
                    f'<span class="chat-blok-ico">{CHAT_ICOON}</span><div class="chat-blok-tekst"><h2 id="chat-kop">{e(kop)}</h2><p>{e(tekst)}</p></div>'
                    f'<div class="chat-blok-actie"><button type="button" class="knop geel" data-chat-open>{e(knop)}</button><small>{e(sub)}</small></div></div></div></section>')
            # direct na de sectie 'wat we maken' (de tweede sectie in main)
            i = h.find("<section", h.find("<section", h.find('<main id="inhoud">') + 1) + 1)
            if i > 0: h = h[:i] + blok + h[i:]
        if '<p id="kanaal"' in h:
            lang = h[h.find('<html lang="') + 12:][:2]
            vraag, knop = CHAT_CONTACT.get(lang, CHAT_CONTACT["nl"])
            regel = f'<p data-chat-blok hidden style="margin-top:18px">{e(vraag)} <button type="button" class="knop geel" data-chat-open style="margin-top:10px">{e(knop)}</button></p>'
            j = h.find("</p>", h.find('<p id="kanaal"')) + 4
            h = h[:j] + regel + h[j:]
        open(p, "w", encoding="utf-8").write(h)

def engelse_screenshots(dist):
    """Pagina's in een andere taal dan Nederlands tonen de Engelse screenshots van onze apps (img/naam-en.jpg)."""
    import glob, re
    en = {os.path.basename(p)[:-7] for p in glob.glob(os.path.join(dist, "img", "*-en.jpg"))}
    for pad in glob.glob(os.path.join(dist, "*.html")):
        html_ = open(pad, encoding="utf-8").read()
        if '<html lang="nl"' in html_:
            continue
        nieuw = re.sub(r'img/([a-z0-9-]+)\.jpg', lambda m: f"img/{m.group(1)}-en.jpg" if m.group(1) in en else m.group(0), html_)
        if nieuw != html_:
            open(pad, "w", encoding="utf-8").write(nieuw)


def birmaans_afbreken(dist):
    """Browsers kennen geen Birmaans woordenboek en breken woorden midden in een lettergreep af.
    Daarom houden we elk stukje tussen twee spaties bij elkaar (de spaties in Birmaans scheiden zinsdelen)."""
    import re
    pad = os.path.join(dist, "my.html")
    if not os.path.exists(pad):
        return
    h = open(pad, encoding="utf-8").read()
    i = h.find("<body")
    kop, romp = h[:i], h[i:]
    romp = re.sub(r"(<summary[^>]*>)([^<]+)", r"\1<span>\2</span>", romp)  # flex-kinderen in <summary> bij elkaar houden
    def tekst(m):
        t = m.group(1)
        if not re.search("[\u1000-\u109f]", t):
            return m.group(0)
        delen = re.split(r"(\s+)", t)
        return "><span>" + "".join(f'<span class="nw">{d}</span>' if re.search("[\u1000-\u109f]", d) else d for d in delen) + "</span><"
    stukken = re.split(r"(<script.*?</script>|<style.*?</style>)", romp, flags=re.S)
    romp = "".join(st if st.startswith(("<script", "<style")) else re.sub(r">([^<>]+)<", tekst, st) for st in stukken)
    open(pad, "w", encoding="utf-8").write(kop + romp)


def thais_bijeen(dist):
    """Thais heeft geen spaties tussen woorden; de browser breekt soms een vaste uitdrukking in tweeën
    (bijv. 'พริบ / ตา'). Uitdrukkingen in deze lijst blijven in koppen bij elkaar."""
    import re
    pad = os.path.join(dist, "th.html")
    if not os.path.exists(pad):
        return
    h = open(pad, encoding="utf-8").read()
    for uitdr in ("ในพริบตา",):
        h = re.sub(r"(<h[1-3][^>]*>[^<]*?)" + uitdr, lambda m: m.group(1) + f'<span class="nw">{uitdr}</span>', h)
    open(pad, "w", encoding="utf-8").write(h)


def webp_varianten(dist):
    """Elke jpg/png in dist/img krijgt een kleinere .webp-versie (ca. 45% lichter).
    Elke <img> wordt <picture> met webp-bron en de jpg/png als terugval.
    picture heeft display:contents (site.css), dus de opmaak verandert niet."""
    import re, glob
    from PIL import Image
    img_map = os.path.join(dist, "img")
    gemaakt = set()
    for pad in glob.glob(os.path.join(img_map, "*")):
        naam, ext = os.path.splitext(pad)
        if ext.lower() not in (".jpg", ".jpeg", ".png"):
            continue
        im = Image.open(pad)
        if ext.lower() == ".png" and os.path.basename(naam).startswith("boek-visual"):
            im.save(naam + ".webp", "WEBP", quality=84, method=6)
        elif ext.lower() == ".png":
            im.save(naam + ".webp", "WEBP", lossless=True, method=6)
        else:
            im.save(naam + ".webp", "WEBP", quality=80, method=6)
        if os.path.getsize(naam + ".webp") < os.path.getsize(pad):
            gemaakt.add(os.path.basename(pad))
        else:
            os.remove(naam + ".webp")
    def vervang(m):
        tag, src = m.group(0), m.group(1)
        if os.path.basename(src) not in gemaakt:
            return tag
        return f'<picture><source srcset="{os.path.splitext(src)[0]}.webp" type="image/webp">{tag}</picture>'
    for pad in glob.glob(os.path.join(dist, "*.html")):
        h = open(pad, encoding="utf-8").read()
        delen = re.split(r"(<picture.*?</picture>|<script.*?</script>)", h, flags=re.S)
        h2 = "".join(d if d.startswith(("<picture", "<script")) else re.sub(r'<img [^>]*?src="(img/[^"]+\.(?:jpe?g|png))"[^>]*>', vervang, d) for d in delen)
        if h2 != h:
            open(pad, "w", encoding="utf-8").write(h2)


def build():
    schrijf_kennis()
    shutil.rmtree(DIST, ignore_errors=True); os.makedirs(DIST)
    for n in ("site.css", "og.png", "_headers", "aceaa1aae33f492c9fc3bb575567f4a2.txt"): shutil.copy(os.path.join(ROOT, "src", n), os.path.join(DIST, n))
    shutil.copytree(os.path.join(ROOT, "src", "img"), os.path.join(DIST, "img"))
    if os.path.isdir(os.path.join(ROOT, "src", "concept")): shutil.copytree(os.path.join(ROOT, "src", "concept"), os.path.join(DIST, "concept"))
    if os.path.isdir(os.path.join(DIST, "concept", "suismuis")):  # prijslijst voor de betaalserver van Suismuis
        import importlib.util as _iu
        _sp = _iu.spec_from_file_location("sm_cat", os.path.join(ROOT, "tools", "suismuis_live", "catalogus.py")); _m = _iu.module_from_spec(_sp); _sp.loader.exec_module(_m)
        _m.maak(os.path.join(DIST, "concept", "suismuis", "assets"))
        import hashlib as _hl, glob as _gl, re as _re  # versienummers tegen oude bestanden in de browsercache
        _as = os.path.join(DIST, "concept", "suismuis", "assets")
        _v = {n: _hl.md5(open(os.path.join(_as, n), "rb").read()).hexdigest()[:8] for n in ("suismuis.css", "suismuis.js", "scouting.js")}
        for _f in _gl.glob(os.path.join(DIST, "concept", "suismuis", "*.html")):
            _t = open(_f, encoding="utf-8").read()
            _t = _re.sub(r'assets/(suismuis\.css|suismuis\.js|scouting\.js)(\?v=[0-9a-z]+)?"', lambda m: f'assets/{m.group(1)}?v={_v[m.group(1)]}"', _t)
            open(_f, "w", encoding="utf-8").write(_t)
    shutil.copytree(os.path.join(ROOT, "src", "tester"), os.path.join(DIST, "tester"))  # testerpagina + QR (13 talen)
    if os.path.isdir(os.path.join(ROOT, "src", "gr")): shutil.copytree(os.path.join(ROOT, "src", "gr"), os.path.join(DIST, "gr"))  # productbeelden voor Gumroad (CORS)
    pages = []

    # HOME
    pages.append(page("index.html", "Website, app of game laten maken vanaf €495 | Collens Group",
        "Apps vanaf €3.150, websites vanaf €495, games vanaf €1.950 en AI-automatisering vanaf €395. Vaste prijs vooraf, onder het marktgemiddelde.",
        f'''<section class="hero" aria-labelledby="kop"><div class="wrap"><div>
<h1 id="kop">Jouw idee.<br>Razendsnel live.</h1>
<p class="lead">Professionele websites, webshops en apps voor ondernemers. Gratis concept binnen 48 uur, daarna een vaste prijs.</p>
<div class="acties"><a class="knop geel" href="#contact">Vraag je gratis concept aan</a><a class="zacht" href="#diensten">Bekijk wat we maken</a></div><ul class="vertrouwen"><li><svg viewBox="0 0 20 20" width="18" height="18" aria-hidden="true"><circle cx="10" cy="10" r="10" fill="#E3EBFA"/><path d="M6 10.3l2.6 2.6L14.2 7.4" fill="none" stroke="#2457D6" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg>Vaste prijs vooraf</li><li><svg viewBox="0 0 20 20" width="18" height="18" aria-hidden="true"><circle cx="10" cy="10" r="10" fill="#E3EBFA"/><path d="M6 10.3l2.6 2.6L14.2 7.4" fill="none" stroke="#2457D6" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg>Eerst een gratis concept</li><li><svg viewBox="0 0 20 20" width="18" height="18" aria-hidden="true"><circle cx="10" cy="10" r="10" fill="#E3EBFA"/><path d="M6 10.3l2.6 2.6L14.2 7.4" fill="none" stroke="#2457D6" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg>Jij blijft eigenaar</li></ul><p class="bewijs">Zelf ontworpen en gebouwd: <a href="apps.html">3 apps en games</a> en <a href="boeken.html">een boekenreeks over AI</a>. Geen sjablonen, alles op maat.</p></div>
<div class="etalage"><figure class="tel-links"><img src="img/hero-webshop.jpg" alt="Conceptwebshop voor woonaccessoires, een voorbeeld van een webshop van ons" width="240" height="427"></figure><figure class="tel-midden"><img src="img/lubbyc-kaart.jpg" alt="Reisapp LubbyC" width="240" height="480" fetchpriority="high"></figure><figure class="tel-rechts"><img src="img/eiland-rood.jpg" alt="Rijgame Eiland Express" width="240" height="480"></figure></div></div></section>

<section id="diensten" class="wit" aria-labelledby="diensten-kop"><div class="wrap">
<div class="intro"><h2 id="diensten-kop">Wat we maken</h2><p>Eén partij voor je hele digitale aanwezigheid: van website tot app, met vaste prijzen onder het marktgemiddelde.</p></div>
{diensten_blok()}</div></section>

<section aria-labelledby="waarom"><div class="wrap">
<div class="intro"><h2 id="waarom">Vakwerk, zonder bureauprijzen</h2>
<p>Een eenvoudige website kost bij een bureau in Nederland gemiddeld €500 tot €2.000, een app al snel €5.000 tot €25.000. Wij werken met moderne tools en veel automatisering en geven dat voordeel aan jou door. Op kwaliteit leveren we niet in. <a href="prijzen.html">Bekijk alle prijzen</a>.</p></div>
<div class="feiten">
<div><h3>Gebouwd om gevonden te worden</h3><p>Snelle laadtijd, nette code en technische SEO, zoals metadata en structured data, zitten standaard in elke site.</p></div>
<div><h3>Eerst ontworpen voor mobiel</h3><p>Elke pagina ontwerpen en testen we eerst op de telefoon, want daar kijken de meeste bezoekers.</p></div>
<div><h3>Vaste prijs, geen verrassingen</h3><p>Prijs, planning en externe kosten staan vooraf zwart op wit. Meerwerk alleen na jouw akkoord.</p></div>
<div><h3>Jij blijft eigenaar</h3><p>Site, domein en inhoud staan op jouw naam. Apps komen in je eigen Apple- en Google-account.</p></div>
</div></div></section>

<section id="prijzen-kort" class="wit" aria-labelledby="prijzen-kort-kop"><div class="wrap">
<div class="intro"><h2 id="prijzen-kort-kop">Prijzen in het kort</h2><p>Alle prijzen zijn eindprijzen: er komt geen btw bij. Na een korte intake krijg je een definitieve prijsopgave op maat.</p></div>
<table class="lijst"><tr><td><a href="website-laten-maken.html">Website</a><small>One-page of bedrijfswebsite</small></td><td>vanaf €495</td></tr>
<tr><td><a href="webshop-laten-maken.html">Webshop</a><small>Tot 50 producten ingericht, iDEAL</small></td><td>vanaf €1.950</td></tr>
<tr><td><a href="app-laten-maken-kosten.html">App voor iPhone en Android</a><small>Basis, Standaard en Maatwerk</small></td><td>vanaf €3.150</td></tr>
<tr><td><a href="game-laten-maken.html">Game</a><small>Merkgame, casual game, 2D met levels</small></td><td>vanaf €1.950</td></tr>
<tr><td><a href="ai-automatisering.html">AI en automatisering</a><small>Automatisering, chatbot, assistent</small></td><td>vanaf €395</td></tr></table>
<p class="knoppen"><a class="knop geel" href="pakketkiezer.html">Welk pakket past bij mij?</a><a class="knop knop-rand" href="prijzen.html">Bekijk alle prijzen en pakketten</a></p></div></section>

<section id="gidsen" aria-labelledby="gidsen-kop"><div class="wrap">
<div class="intro"><h2 id="gidsen-kop">Veelgezochte vragen, eerlijk beantwoord</h2><p>Praktische gidsen met echte prijzen, zodat je weet waar je aan toe bent voordat je contact opneemt.</p></div>
<div class="gids-rij"><a href="app-laten-maken-kosten.html"><strong>Wat kost een app laten maken?</strong><span>Marktprijzen, bijkomende kosten en onze vaste prijzen</span></a>
<a href="website-laten-maken-horeca.html"><strong>Horeca website laten maken</strong><span>Voor je restaurant, café of lunchroom</span></a>
<a href="goedkope-website-laten-maken.html"><strong>Goedkope website laten maken</strong><span>Vanaf €495, zonder dat het goedkoop oogt</span></a>
<a href="bedrijfsapp-laten-maken.html"><strong>Bedrijfsapp laten maken</strong><span>Een zakelijke app voor je klanten of team</span></a></div>
<p style="margin-top:18px"><a href="artikelen.html">Bekijk alle gidsen</a></p></div></section>

<section id="werkwijze" class="donker" aria-labelledby="stappen-kop"><div class="wrap">
<div class="intro"><h2 id="stappen-kop">Zo werkt het</h2><p>Elke stap rond je af met een akkoord. Je ziet je website, app of game groeien voordat het live gaat.</p></div>
<ol class="stappen"><li><h3>Aanvraag</h3><p>Je vertelt in een paar zinnen wat je wilt. Geen afspraak nodig.</p></li>
<li><h3>Gratis concept</h3><p>Binnen 48 uur zie je hoe het eruit kan zien, zonder verplichtingen.</p></li>
<li><h3>Vaste prijs</h3><p>Prijs, planning en wat wel en niet inbegrepen is, vooraf op papier.</p></li>
<li><h3>Bouwen en testen</h3><p>Je ziet tussentijds testversies en keurt goed voordat we verder gaan.</p></li>
<li><h3>Live</h3><p>Je website, app of game gaat live, in jouw eigen accounts. Bij apps begeleiden we de publicatie in de stores.</p></li></ol></div></section>

<section id="apps" class="wit" aria-labelledby="apps-kop"><div class="wrap">
<div class="intro"><h2 id="apps-kop">Eigen apps, games en series</h2><p>Wat we voor onszelf maken, maken we ook voor jou. Zo testen we onze werkwijze eerst op onszelf.</p></div>
{app_rijen()}</div></section>

<section aria-labelledby="past-kop"><div class="wrap">
<h2 id="past-kop">Past Collens Group bij jou?</h2>
<div class="past"><div class="past-ja"><h3>Wel als je…</h3><ul><li>een vaste prijs vooraf wilt in plaats van uurtje-factuurtje;</li><li>snel live wilt: een one-page website in 3–5 dagen, een app-MVP in 3–5 weken;</li><li>eerst een gratis concept wilt zien voordat je iets betaalt.</li></ul></div>
<div class="past-nee"><h3>Kies liever iets anders als je…</h3><ul><li>een grote 3D-game of online multiplayer zoekt;</li><li>onbeperkt werk voor een vast bedrag verwacht;</li><li>alles op locatie wilt bespreken: wij werken volledig online.</li></ul></div></div>
</div></section>
<section id="vragen" aria-labelledby="vragen-kop"><div class="wrap smal">
<h2 id="vragen-kop">Veelgestelde vragen</h2>{faq_html(FAQ)}</div></section>
{contact_section()}''', crumbs=[("Home", "index.html")], extra_ld=[SERVICE, faq_ld(FAQ)], alt=("index.html", "en.html")))

    # KOSTEN-GIDS
    kosten_faq = [
        ("Wat kost een simpele app?", "Bij Nederlandse bureaus en freelancers kost een eenvoudige app of MVP volgens kostengidsen €5.000 tot €25.000. Bij Collens Group begint een Basis-app met maximaal 5 schermen bij €3.150, een eindprijs zonder btw erbij, en is hij in 3 tot 5 weken klaar. Daarnaast betaal je de store-accounts zelf: Apple rekent $99 per jaar en Google eenmalig $25. Je krijgt eerst een gratis concept, daarna een vaste prijs."),
        ("Wat kost een app per jaar aan onderhoud?", "Dat hangt af van hoeveel er na de lancering nog verandert. Bij ons is onderhoud een vast maandbedrag. Onderhoud Basis kost €85,50 per maand, met monitoring, kritieke fixes en updates voor nieuwe iOS- en Android-versies. Wil je de app blijven verbeteren, dan kies je Groei & Support voor €265,50 per maand, met tot 4 uur aanpassingen en voorrang bij storingen. Daarnaast betaal je zelf het Apple Developer-account ($99 per jaar) en eventueel hosting. Onderhoud is niet verplicht."),
        ("Wat kost een MVP-app laten maken?", "Bij Collens Group begint een MVP (Basis-pakket, tot 5 schermen) bij €3.150 (geen btw erbij) en is hij klaar in 3–5 weken. Accounts, een database of betalingen vallen onder het Standaard-pakket vanaf €6.750."),
        ("Is een app voor iPhone én Android duurder?", "Bij aparte native apps vaak bijna het dubbele, omdat er dan twee apps los van elkaar worden gebouwd en onderhouden. Wij bouwen met React Native: één codebase die op iPhone én Android draait. Daardoor betaal je niet twee keer voor hetzelfde werk en zijn latere aanpassingen ook in één keer voor beide platforms klaar. Wel betaal je voor beide stores een eigen account."),
        ("Wat kost een app per maand?", "Na de bouw zijn de vaste kosten vaak laag. Apple rekent $99 per jaar (ruim $8 per maand), Google eenmalig $25 en hosting is voor de meeste kleine apps gratis tot $25 per maand. Kies je ons onderhoud, dan komt daar €85,50 per maand bij voor Onderhoud Basis of €265,50 per maand voor Groei & Support. Onderhoud is niet verplicht."),
        ("Kost het geld om een app in de App Store of Google Play te zetten?", "Ja, maar weinig. Voor de App Store heb je het Apple Developer Program nodig van $99 per jaar. Voor Google Play betaal je eenmalig $25. Het aanmelden en klaarzetten van je app in beide stores doen wij en zit in onze pakketten. Verkoop je digitale producten of abonnementen in de app, dan houden Apple en Google daar 15% of 30% commissie op in."),
        ("Wat kost een game-app laten maken?", "Een eenvoudige game voor de browser of telefoon begint bij ons bij €1.950. Een uitgebreidere game met meerdere levels, eigen tekeningen en geluid kost meer, afhankelijk van de inhoud. Op de pagina game laten maken staan de pakketten en voorbeelden, waaronder ons eigen spel Eiland Express."),
        ("Hoe vraag ik een offerte voor een app aan?", "Beschrijf in een paar zinnen wat de app moet doen en voor wie hij is, via het formulier onderaan deze pagina. Binnen 48 uur krijg je een paar korte vragen en daarna een gratis concept met een vaste prijs, uitgesplitst per onderdeel. Je zit nergens aan vast tot je akkoord geeft. Wil je eerst zelf een indicatie, gebruik dan de kostencalculator."),
    ]
    pages.append(page("app-laten-maken-kosten.html", "App laten maken kosten 2026: prijzen vanaf €3.150 | Collens Group",
        "Wat kost een app laten maken in 2026? Marktprijzen in Nederland, alle bijkomende kosten (Apple, Google, hosting, onderhoud) en onze vaste prijzen vanaf €3.150.",
        f'''<article class="tekst breed">
<h1>Wat kost een app laten maken in 2026?</h1>
<p class="lead2">Kort antwoord: bij Nederlandse bureaus en freelancers betaal je voor een eenvoudige app meestal €5.000 tot €25.000. Bij Collens Group begint een Basis-app bij €3.150 en een complete app met accounts en database bij €6.750. Alle prijzen zijn eindprijzen, er komt geen btw bij. Hieronder vind je de kosten per functie, een rekenvoorbeeld, de totale kosten over 3 jaar en een checklist om offertes te vergelijken.</p>
<p class="bijgewerkt">Bijgewerkt op @@BIJGEWERKT_NL@@ · Geschreven door Jeffrey Collens, oprichter van Collens Group. Opgesteld met hulp van AI-tools en door Jeffrey gecontroleerd.</p>
<p><a class="knop geel" href="kostencalculator.html">Bereken direct wat jouw app kost</a></p>
<nav class="toc" aria-label="Inhoud"><a href="#markt">Marktprijzen</a> · <a href="#prijzen">Onze prijzen</a> · <a href="#bijkomend">Bijkomende kosten</a> · <a href="#prijsbepalers">Wat bepaalt de prijs</a> · <a href="#functies">Kosten per functie</a> · <a href="#rekenvoorbeeld">Rekenvoorbeeld</a> · <a href="#drie-jaar">Kosten over 3 jaar</a> · <a href="#iphone-android">iPhone of Android</a> · <a href="#bedrijfsapp">Bedrijfsapp</a> · <a href="#offerte">Offertes vergelijken</a> · <a href="#besparen">Besparen</a> · <a href="#faq">Vragen</a></nav>

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
<p style="margin-top:20px"><a class="knop geel" href="index.html#contact">Vraag je gratis concept aan</a></p>

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

<h2 id="functies">Wat kost een functie? Uren en prijs per onderdeel</h2>
<p>Een offerte is eigenlijk een optelsom van uren. Daarom zie je hieronder per veelgevraagde functie hoeveel bouw- en testtijd die ongeveer kost. Zo kun je zelf narekenen of een offerte redelijk is, ook die van een ander bureau.</p>
<div class="scroll"><table class="tabel">
<tr><th>Functie</th><th>Uren (inschatting)</th><th>Prijs bij €67,50 per uur</th></tr>
<tr><td>Inloggen met e-mail, Apple of Google</td><td>8 – 16</td><td>€540 – €1.080</td></tr>
<tr><td>Profiel en instellingen</td><td>6 – 12</td><td>€405 – €810</td></tr>
<tr><td>Pushmeldingen</td><td>4 – 8</td><td>€270 – €540</td></tr>
<tr><td>Kaart met locaties</td><td>8 – 16</td><td>€540 – €1.080</td></tr>
<tr><td>Koppeling met een bestaand systeem (API)</td><td>8 – 24</td><td>€540 – €1.620</td></tr>
<tr><td>Betalingen of abonnementen in de app</td><td>16 – 32</td><td>€1.080 – €2.160</td></tr>
<tr><td>Chat tussen gebruikers</td><td>24 – 40</td><td>€1.620 – €2.700</td></tr>
<tr><td>Beheerdashboard voor jezelf</td><td>24 – 48</td><td>€1.620 – €3.240</td></tr>
<tr><td>Extra taal (per taal)</td><td>2 – 4</td><td>€135 – €270</td></tr></table></div>
<p class="bron">Inschatting van Collens Group op basis van eigen projecten, zoals onze reisapp <a href="app-lubbyc.html">LubbyC</a>. Bij andere bouwers verschillen de uren per team. Bij een uurtarief van €94, het gemiddelde voor zzp-developers volgens Knab (2026), liggen de bedragen ongeveer 40% hoger.</p>

<h2 id="rekenvoorbeeld">Rekenvoorbeeld: een reserveringsapp voor een salon</h2>
<p>Stel: een kapsalon wil een app waarin klanten een afspraak maken, een herinnering krijgen en hun eerdere afspraken terugzien. Dan heb je ongeveer dit nodig:</p>
<ul>
<li>8 schermen: start, behandelingen, kalender, bevestigen, mijn afspraken, profiel, inloggen, instellingen</li>
<li>Inloggen en een eigen database met afspraken</li>
<li>Pushmeldingen als herinnering</li>
<li>Live in de App Store en Google Play</li></ul>
<p>Dat past in ons <strong>Standaard-pakket vanaf €6.750</strong>, klaar in 6 tot 10 weken. Wil de salon ook vooraf laten betalen en zelf de agenda beheren in een dashboard, dan komt daar volgens de tabel hierboven ongeveer €2.700 tot €5.400 bij, of je kiest direct Maatwerk vanaf €13.050. Bij een gemiddeld Nederlands bureau valt zo'n app volgens de marktprijzen bovenaan in de klasse €25.000 – €75.000.</p>

<h2 id="drie-jaar">Wat kost een app over 3 jaar?</h2>
<p>De bouwprijs is maar een deel van het verhaal. Na de lancering betaal je store-accounts, hosting en meestal onderhoud. Bureaus rekenen voor onderhoud vaak 15 tot 20% van de bouwprijs per jaar (Searchlab, 2026). Hieronder zie je wat dat over 3 jaar betekent.</p>
<div class="scroll"><table class="tabel">
<tr><th>Over 3 jaar</th><th>Basis-app (Collens)</th><th>Standaard-app (Collens)</th><th>Gemiddelde app (markt)</th></tr>
<tr><td>Bouw</td><td>€3.150</td><td>€6.750</td><td>€25.000</td></tr>
<tr><td>Onderhoud</td><td>€3.078 (36 × €85,50)</td><td>€3.078 (36 × €85,50)</td><td>€11.250 – €15.000 (15–20% per jaar)</td></tr>
<tr><td>Hosting en database</td><td>meestal gratis</td><td>tot $900 (36 × $25)</td><td>afhankelijk van de app</td></tr>
<tr><td>Apple en Google</td><td>$297 + $25</td><td>$297 + $25</td><td>$297 + $25</td></tr>
<tr><td><strong>Totaal (zonder dollars)</strong></td><td><strong>€6.228</strong></td><td><strong>€9.828</strong></td><td><strong>€36.250 – €40.000</strong></td></tr></table></div>
<p class="bron">Onderhoud is bij ons niet verplicht; zonder onderhoud betaal je alleen de bouw, de store-accounts en eventueel hosting. Bedragen in dollars rekenen Apple, Google en Supabase zelf af in je eigen account. Marktbedragen: Searchlab (2026), zie hierboven.</p>

<h2 id="iphone-android">Wat kost een iPhone-app of een Android-app?</h2>
<p>Voor de bouw maakt het bij ons niet uit: met React Native maken we één app die op iPhone én Android draait. Het verschil zit in de stores en in het testen.</p>
<div class="scroll"><table class="tabel">
<tr><th></th><th>iPhone (App Store)</th><th>Android (Google Play)</th></tr>
<tr><td>Account</td><td>$99 per jaar</td><td>$25 eenmalig</td></tr>
<tr><td>Controle voor publicatie</td><td>Elke versie wordt door Apple beoordeeld</td><td>Elke versie wordt door Google beoordeeld; nieuwe persoonlijke accounts moeten eerst een gesloten test doen</td></tr>
<tr><td>Commissie op verkopen in de app</td><td>15% of 30%, afhankelijk van omzet en soort aankoop</td><td>15% of 30%, afhankelijk van omzet en soort aankoop</td></tr></table></div>
<p class="bron">Bronnen: <a href="https://developer.apple.com/support/enrollment/" rel="nofollow noopener">Apple Developer Program</a>, <a href="https://support.google.com/googleplay/android-developer/answer/6112435" rel="nofollow noopener">Google Play Console</a>, <a href="https://support.google.com/googleplay/android-developer/answer/112622" rel="nofollow noopener">Google Play servicekosten</a>.</p>
<p>Wil je alleen op één platform beginnen? Dat kan in het Basis-pakket. Later voegen we het andere platform toe zonder de app opnieuw te bouwen.</p>

<h2 id="bedrijfsapp">Wat kost een zakelijke app of bedrijfsapp?</h2>
<p>Een bedrijfsapp is een app voor je eigen team of je klanten: denk aan werkbonnen invullen, uren registreren, een klantportaal of een spaarkaart. Zulke apps hebben bijna altijd accounts, een database en vaak een koppeling met een systeem dat je al gebruikt. Daarom vallen ze meestal in ons <strong>Standaard-pakket (vanaf €6.750)</strong> of in <strong>Maatwerk (vanaf €13.050)</strong> als er meerdere gebruikersrollen en een beheerdashboard bij komen.</p>
<p>Een interne app hoeft niet altijd in de openbare stores. Voor een klein team kan een webapp, die je opent in de browser en op je beginscherm zet, goedkoper zijn. In het gratis concept adviseren we welke vorm het best past. Alles over prijzen en voorbeelden lees je op <a href="bedrijfsapp-laten-maken.html">bedrijfsapp laten maken</a>.</p>

<h2 id="offerte">Offertes vergelijken: zo weet je of een prijs klopt</h2>
<p>Heb je meerdere offertes? Vraag bij elke offerte naar deze punten:</p>
<ol>
<li><strong>Uren per onderdeel.</strong> Een totaalbedrag zonder uitsplitsing is niet te vergelijken. Leg de uren naast de tabel hierboven.</li>
<li><strong>Wat er niet in zit.</strong> Store-accounts, hosting, teksten, ontwerp en het aanmelden in de stores worden vaak apart gerekend.</li>
<li><strong>Wie de code en de accounts bezit.</strong> Zorg dat de app en de store-accounts op jouw naam staan.</li>
<li><strong>Onderhoud na de lancering.</strong> Vraag wat updates voor nieuwe iOS- en Android-versies kosten en of onderhoud verplicht is.</li>
<li><strong>Meerwerk.</strong> Spreek af dat extra werk alleen na jouw akkoord en tegen een vooraf bekend tarief gebeurt.</li></ol>
<p>Een offerte die veel lager is dan de rest kan kloppen, maar vraag dan naar referenties of een eerder gebouwde app die je zelf kunt downloaden. Onze eigen apps staan op <a href="apps.html">deze pagina</a>.</p>

<h2 id="besparen">Zo bespaar je op je app</h2>
<ol>
<li>Begin met een <a href="mvp-app-laten-maken.html">MVP</a>: alleen wat gebruikers echt nodig hebben.</li>
<li>Kies één codebase voor iPhone en Android.</li>
<li>Gebruik bestaande diensten voor betalingen, inloggen en hosting in plaats van alles zelf te bouwen.</li>
<li>Leg vooraf vast wat wel en niet in de prijs zit.</li></ol>

<h2 id="faq">Veelgestelde vragen over app-kosten</h2>
{faq_html(kosten_faq)}
<p style="margin-top:32px"><a class="knop geel" href="index.html#contact">Vraag een vaste prijs aan</a></p>
<p class="bron" style="margin-top:22px">Zie ook: <a href="mvp-app-laten-maken.html">MVP-app laten maken</a> · <a href="app-laten-maken-horeca.html">App voor horeca</a> · <a href="website-laten-maken.html">Website laten maken</a> · <a href="webshop-laten-maken.html">Webshop laten maken</a> · <a href="chatbot-laten-maken.html">AI-chatbot laten maken</a> · <a href="apps.html">Onze eigen apps en games</a></p>
</article>''', crumbs=[("Home", "index.html"), ("Kosten", "app-laten-maken-kosten.html")],
        extra_ld=[{"@type": "Article", "headline": "Wat kost een app laten maken in 2026?", "dateModified": "@@BIJGEWERKT_ISO@@", "inLanguage": "nl", "author": {"@type": "Person", "name": "Jeffrey Collens"}, "publisher": {"@id": "#org"}}, faq_ld(kosten_faq)]))

    # MVP
    mvp_faq = [
        ("Wat is een MVP-app?", "Een Minimum Viable Product is de kleinste versie van je app waarmee echte gebruikers je idee kunnen testen. Je bouwt alleen de functies die nodig zijn om te zien of mensen de app willen gebruiken, en laat de rest voorlopig weg. Zo weet je snel en voor een vaste, lage prijs of je idee aanslaat, voordat je investeert in accounts, betalingen of een beheerdashboard."),
        ("Hoe snel is een MVP klaar?", "Ons Basis-pakket, met maximaal 5 schermen, is in 3 tot 5 weken klaar. Je krijgt eerst een gratis concept, daarna een vaste prijs en een planning. Tijdens het bouwen krijg je tussentijdse testversies die je zelf op je telefoon probeert. Hoe snel je feedback geeft en teksten en beelden aanlevert, bepaalt mee hoe snel de app in de store staat."),
        ("Kan ik later uitbreiden?", "Ja. Omdat de code van jou is en we standaard bouwstenen gebruiken, bouwen we je MVP later uit tot een Standaard- of Maatwerk-app, met bijvoorbeeld accounts, een database, pushmeldingen of betalingen. Je begint dus niet opnieuw: wat er al staat, blijft staan. Voor een uitbreiding krijg je eerst een vaste prijs, zodat je vooraf weet wat het kost."),
    ]
    pages.append(page("mvp-app-laten-maken.html", "MVP-app laten maken vanaf €3.150 | Collens Group",
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
<tr><td>Prijs</td><td>vanaf €3.150, eindprijs, geen btw erbij</td></tr><tr><td>Doorlooptijd</td><td>3 – 5 weken</td></tr></table>
<p>Accounts, een database of betalingen nodig? Dan past het <a href="app-laten-maken-kosten.html">Standaard-pakket vanaf €6.750</a> beter.</p>

<h2>Zo verloopt het</h2>
<ol><li>Gratis intake per mail: een paar korte vragen.</li><li>Voorstel met vaste prijs en schermoverzicht.</li><li>Ontwerp ter goedkeuring.</li><li>Bouwen, met elke week een testversie op je telefoon.</li><li>Oplevering en hulp bij publicatie.</li></ol>

<h2>Veelgestelde vragen</h2>{faq_html(mvp_faq)}
<p style="margin-top:32px"><a class="knop geel" href="index.html#contact">Bespreek je MVP</a></p>
</article>''', crumbs=[("Home", "index.html"), ("MVP", "mvp-app-laten-maken.html")],
        extra_ld=[dict(SERVICE, name="MVP app laten maken", offers=[OFFERS[0]]), faq_ld(mvp_faq)]))

    for d in DIENSTEN: pages.append(dienst_pagina(d))
    from landings import landing_pages, LANDINGS
    landing_pages(page, e, faq_html, faq_ld, pages)
    from paginas_nieuw import bouw as bouw_nieuw
    nieuwe_pag, nieuwe_items = bouw_nieuw(page, e, faq_html, faq_ld, DIENSTEN, PAKKETTEN, VANDAAG, CONFIG)
    pages += nieuwe_pag

    # Artikelen & gidsen: overzicht van alle NL-artikelen (nieuwe landingspagina's komen er vanzelf bij)
    items = [("app-laten-maken-kosten.html", "Wat kost een app laten maken?", "Prijzen, doorlooptijd en vaste kosten van een app, met wat de prijs bepaalt en hoe je bespaart."),
             ("mvp-app-laten-maken.html", "MVP-app laten maken", "Test je app-idee eerst met een kleine versie: wat erin zit, wat het kost en hoe het verloopt.")]
    items += [(f'{L["slug"]}.html', L["titel"].split(" | ")[0], L["desc"]) for L in LANDINGS if L["lang"] == "nl"]
    items += nieuwe_items
    items += [("en-ai-chatbot.html", "AI chatbot for small business (Engels)", "Engelstalige gids: wat een AI-chatbot voor je bedrijf doet, wat hij kost (vanaf €995) en hoe we de antwoorden betrouwbaar houden.")]
    def _cat(u):
        if u.startswith(("boek", "boeken")): return "Boeken"
        if "game" in u: return "Games"
        if "chatbot" in u or "ai-" in u or u.startswith("ai"): return "AI en automatisering"
        if u.startswith(("app", "mvp")): return "Apps"
        return "Websites en webshops"
    _ICO = {"Websites en webshops": "Websites", "Apps": "Apps", "Games": "Games", "AI en automatisering": "AI", "Boeken": "Websites"}
    _KL = {"Websites en webshops": "#2457D6", "Apps": "#14213D", "Games": "#7A3BD1", "AI en automatisering": "#0E7C86", "Boeken": "#E8590C"}
    _volg = ["Websites en webshops", "Apps", "AI en automatisering", "Games", "Boeken"]
    groepen = {c: [] for c in _volg}
    for u, t, d in items: groepen[_cat(u)].append((u, t, d))
    kaarten = "".join(f'<section class="art-groep"><h2>{c}</h2><div class="artikelen">' + "".join(
        f'<a class="artikel" href="{u}" style="--k:{_KL[c]}">{icoon(_ICO[c])}<h3>{e(t)}</h3><p>{e(d)}</p><span class="lees">Lees het artikel</span></a>' for u, t, d in groepen[c]) + '</div></section>'
        for c in _volg if groepen[c])
    pages.append(page("artikelen.html", "Gidsen over websites, apps en AI | Collens Group",
        "Praktische gidsen over wat een website, webshop, app of AI-chatbot kost en hoe je het slim aanpakt. Eerlijke prijzen en heldere uitleg.",
        f'''<article class="tekst breed"><h1>Artikelen en gidsen</h1>
<p class="lead2">Eerlijke uitleg over wat een website, app of AI-oplossing kost en hoe je het slim aanpakt.</p>
{kaarten}</article>''', crumbs=[("Home", "index.html"), ("Artikelen", "artikelen.html")]))

    # APPS-OVERZICHT
    pages.append(page("apps.html", "Eigen apps, games en series | Collens Group",
        "Wat Collens Group zelf maakt: de reisapp LubbyC, de games Koffer Vol! en Eiland Express en de animatieserie Manu en Khanun.",
        f'''<section><div class="wrap"><div class="intro"><h1 style="font-size:clamp(36px,5vw,56px)">Eigen apps, games en series</h1>
<p style="margin-top:14px">We maken niet alleen dingen voor klanten, maar ook voor onszelf: een reisapp, twee games en een animatieserie. Zo weten we precies wat werkt, van ontwerp tot store.</p></div>
{app_rijen()}
<h2 style="margin-top:48px">Wat dit voor jouw project betekent</h2>
<p>Alles wat je hier ziet, hebben we zelf ontworpen, gebouwd en gepubliceerd. Daardoor weten we uit ervaring wat een app, game of AI-oplossing kost en waar de valkuilen zitten. Die ervaring gebruiken we voor klanten.</p>
<ul class="kenmerken"><li><strong>App:</strong> een basis-app vanaf €3.150 en een standaard-app vanaf €6.750, eindprijs, geen btw erbij. Zie <a href="app-laten-maken-kosten.html">wat een app kost</a>.</li><li><strong>Game:</strong> een game in jouw huisstijl vanaf €1.950. Zie <a href="game-laten-maken.html">game laten maken</a>.</li><li><strong>AI en automatisering:</strong> vanaf €395. Zie <a href="ai-automatisering.html">AI en automatisering</a>.</li><li><strong>Website of webshop:</strong> vanaf €495. Zie <a href="prijzen.html">alle prijzen</a>.</li></ul>
<p>Je begint altijd met een gratis concept binnen 48 uur, zodat je ziet wat je krijgt voordat je beslist.</p>
<p><a class="knop geel" href="index.html#contact">Vraag je gratis concept aan</a></p></div></section>''', crumbs=[("Home", "index.html"), ("Onze apps", "apps.html")]))

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
        tester = ""
        if a.get("tester"):
            if a.get("test_vrij"):
                noot_nl = "Werkt alleen op Android. Je e-mailadres is alleen zichtbaar voor ons, niet voor andere testers."
                noot_en = "Android only. Only we can see your email address."
            else:
                noot_nl = "Let op: krijg je bij stap 2 een melding dat de test niet beschikbaar is? Dan wordt de testversie nog vrijgegeven. Dat duurt enkele dagen; je lidmaatschap telt dan automatisch mee. Werkt alleen op Android. Je e-mailadres is alleen zichtbaar voor ons, niet voor andere testers."
                noot_en = "Android only. Does Google Play say the test is not available yet? Try again in a few days; your group membership counts automatically. Only we can see your email address."
            winkels += '<a class="knop knop-licht" href="#tester">Word tester (gratis)</a>'
            tester = f'''<div class="tester" id="tester"><h2>Word tester van {e(a["naam"])}</h2>
<p>Probeer {e(a["naam"])} als eerste op je Android-telefoon en help ons de laatste puntjes op de i te zetten. Gratis, en je zit nergens aan vast.</p>
<ol><li><strong>Word lid van de testersgroep.</strong> Log in met je Google-account en klik op "Lid worden". <a class="knop" href="https://groups.google.com/g/collens-group" target="_blank" rel="noopener">Naar de testersgroep</a></li>
<li><strong>Open de test in Google Play.</strong> Klik op "Word tester" en installeer de app. <a class="knop knop-rand" href="https://play.google.com/apps/testing/{a["tester"]}" target="_blank" rel="noopener">Naar Google Play</a></li></ol>
<p class="noot">{noot_nl}</p>
<details class="tester-en" lang="en"><summary>English: become a tester</summary>
<p>Try {e(a["naam"])} first on your Android phone and help us polish the final details. Free, no strings attached.</p>
<ol><li><strong>Join the testers group.</strong> Sign in with your Google account and click "Join group". <a class="knop" href="https://groups.google.com/g/collens-group" target="_blank" rel="noopener">Go to the testers group</a></li>
<li><strong>Open the test in Google Play.</strong> Tap "Become a tester" and install the app. <a class="knop knop-rand" href="https://play.google.com/apps/testing/{a["tester"]}" target="_blank" rel="noopener">Go to Google Play</a></li></ol>
<p class="noot">{noot_en}</p></details><script>(function(){{var d=document.querySelector('.tester-en');if(d&&(location.search.indexOf('campaign=en-')>-1||!/^nl/i.test(navigator.language||'nl')))d.open=true;}})();</script></div>'''
        cta = {"App": "Zelf een app laten maken?", "Game": "Zelf een game laten maken?", "Kinderserie": "Ook iets moois laten maken?"}[a["soort"]]
        pages.append(page(f'app-{a["slug"]}.html', a["titel"], a["kort"] + " " + a["status"] + ".",
            f'''<section class="app-hero" style="background:{a["kleur"]}"><div class="wrap">
<span class="status">{e(a["soort"])} · {e(a["status"])}</span>
<h1>{e(a["kop"])}</h1><p>{e(a["kort"])}</p>{winkels}</div></section>
<section><div class="wrap" style="max-width:980px">
<h2>Over {e(a["naam"])}</h2><p>{e(a["intro"])}</p>{kenmerken}
{beelden}
{f'<div style="max-width:360px;margin:0 0 30px"><video src="{a["video"][0]}" poster="{a["video"][1]}" controls muted playsinline loop preload="none" style="width:100%;border-radius:22px;border:6px solid #0E1830"></video><p class="bron">Proefrit, 10 seconden</p></div>' if a.get("video") else ""}
{tester}
<h2 style="margin-top:40px">{APP_BETEKENIS[a["soort"]][0]}</h2>{APP_BETEKENIS[a["soort"]][1]}
{privacy}
<p style="margin-top:30px"><a class="knop" href="index.html#contact">{cta}</a></p></div></section>''',
            crumbs=[("Home", "index.html"), ("Onze apps", "apps.html"), (a["naam"], f'app-{a["slug"]}.html')], extra_ld=[app_ld]))

    # PRIVACY
    pages.append(page("privacy.html", "Privacy | Collens Group", "Hoe Collens Group omgaat met je gegevens: wat deze website verzamelt, waarvoor, en welke rechten je hebt.",
        f'''<article class="tekst"><h1>Privacy</h1><p>Laatst bijgewerkt: 19-11-2026</p>
<h2>Wat deze website verzamelt</h2><p>Deze website plaatst geen trackingcookies. {"We tellen bezoeken met GoatCounter, dat geen cookies gebruikt en geen persoonsgegevens opslaat." if CONFIG["goatcounter"] else "We tellen bezoeken met Cloudflare Web Analytics. Dat gebruikt geen cookies en slaat geen persoonsgegevens op; we zien alleen totalen, zoals het aantal bezoeken per pagina en per land."} Vul je het aanvraagformulier in, dan slaan we je bericht en eventuele voorbeeldfoto's op bij onze database-leverancier Supabase (servers in Singapore), zodat we je aanvraag kunnen beantwoorden. Foto's staan op een niet te raden webadres; we gebruiken ze alleen als inspiratie voor jouw ontwerp en verwijderen ze als je daarom vraagt. Onze website wordt gehost door Cloudflare.</p>
<h2>Online adviseur (chat)</h2><p>Gebruik je de chat-adviseur, dan worden je berichten verwerkt door het AI-model Claude van Anthropic om een antwoord te maken. Het gesprek blijft alleen in je eigen browser bewaard tot je het tabblad sluit; wij slaan het niet op. Geef je in de chat je naam en e-mailadres en vraag je ons contact op te nemen, dan sturen we het gesprek als mail naar ons team (via de maildienst Brevo) en gebruiken we het alleen om je te antwoorden. Deel in de chat geen gevoelige gegevens.</p>
<h2>Als je contact met ons opneemt</h2><p>Stuur je ons een aanvraag, dan gebruiken we je naam, e-mailadres, bedrijfsnaam en je beschrijving alleen om je aanvraag te beantwoorden en, als je klant wordt, om het project uit te voeren. We bewaren deze gegevens niet langer dan nodig en delen ze niet met anderen, behalve als dat nodig is voor het project en je daarmee akkoord gaat.</p>
<h2>Lettertypes</h2><p>Deze website laadt lettertypes via Google Fonts. Daarbij ziet Google je IP-adres.</p>
<h2>Je rechten</h2><p>Je kunt ons altijd vragen welke gegevens we van je hebben, en vragen om ze aan te passen of te verwijderen. Ook kun je een klacht indienen bij de Autoriteit Persoonsgegevens.</p>
<h2>Apps van Collens Group</h2><p>Elke app heeft een eigen privacybeleid op zijn eigen pagina, zie <a href="apps.html">onze apps</a>.</p></article>''',
        crumbs=[("Home", "index.html"), ("Privacy", "privacy.html")]))

    en_pages(pages)
    taal_paginas(page, e, faq_html, faq_ld, contact_section, pages, icoon)

    # 404
    page("404.html", "Pagina niet gevonden | Collens Group", "Deze pagina bestaat niet (meer). Ga naar de startpagina of bekijk onze websites, apps, games en AI.", extra_head='<meta name="robots" content="noindex">', body=
         '<article class="tekst"><h1>Deze pagina bestaat niet</h1><p>De link is misschien verouderd. Ga naar de <a href="index.html">startpagina</a> of bekijk <a href="app-laten-maken-kosten.html">wat een app kost</a>.</p></article>')

    from illustraties import verrijk
    verrijk(DIST)
    from grafieken import verrijk_grafieken
    verrijk_grafieken(DIST)
    engelse_screenshots(DIST)
    birmaans_afbreken(DIST)
    thais_bijeen(DIST)
    chat_inbouwen()
    webp_varianten(DIST)
    schone_links(DIST)
    datums = datums_vastzetten(DIST)

    # robots, sitemap, llms.txt
    with open(os.path.join(DIST, "robots.txt"), "w") as f:
        f.write("User-agent: *\nAllow: /\n" + (f"Sitemap: {CONFIG['base_url']}/sitemap.xml\n" if CONFIG["base_url"] else ""))
    # noindex-pagina's (bv. bedankt) horen niet in sitemap en llms.txt
    def _noindex(pg):
        try: return re.search(r'name="robots"[^>]*noindex', open(os.path.join(DIST, pg), encoding="utf-8").read(40000)) is not None
        except OSError: return False
    pages = [pg for pg in pages if not _noindex(pg)]
    if CONFIG["base_url"]:
        with open(os.path.join(DIST, "sitemap.xml"), "w") as f:
            f.write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' +
                    "".join(f"<url><loc>{abs_url(p)}</loc><lastmod>{datums.get(p, {}).get('bijgewerkt', VANDAAG)}</lastmod></url>\n" for p in pages if "noindex" not in open(os.path.join(DIST, p), encoding="utf-8").read(6000)) + "</urlset>\n")
    with open(os.path.join(DIST, "llms.txt"), "w") as f:
        f.write(f"# {CONFIG['naam']}\n\n> Websites, apps, games en AI-automatisering voor ondernemers in Nederland, België en wereldwijd, tegen vaste prijzen onder het marktgemiddelde.\n\n"
                "## Prijzen (geen btw)\n- Websites: one-page €495, bedrijfswebsite €995, webshop €1.950\n- Games: merkgame €1.950, casual game €4.950, 2D-game met levels €9.950\n- AI: automatisering €395, AI-chatbot €995, AI-assistent €1.950\n- Basis / MVP app: vanaf €3.150, 3–5 weken\n- Standaard app: vanaf €6.750, 6–10 weken\n- Maatwerk / Pro app: vanaf €13.050, 10–16+ weken\n- Uurtarief: €67,50\n- Onderhoud: €85,50 of €265,50 per maand\n\n"
                "## Pagina's\n" + "".join(f"- [{p}]({abs_url(p) or p})\n" for p in pages))
    print("Gebouwd:", ", ".join(pages))

DATUMS_JSON = os.path.join(os.path.dirname(os.path.abspath(__file__)), "datums.json")

def datums_vastzetten(dist):
    """Eerlijke datums i.p.v. de builddatum (19-11).
    Pagina's bevatten @@BIJGEWERKT_NL@@ / @@BIJGEWERKT_ISO@@ / @@GEPUBLICEERD_ISO@@.
    Per pagina bewaart datums.json een hash van de inhoud (met plaatshouders):
    alleen als de inhoud echt verandert, wordt 'bijgewerkt' vandaag. Nieuwe pagina = beide vandaag.
    Ook de sitemap gebruikt deze datum (lastmod), dus dist verandert niet meer elke dag vanzelf."""
    import hashlib
    try:
        oud = json.load(open(DATUMS_JSON))
    except (OSError, ValueError):
        oud = {}
    nieuw = {}
    for fn in sorted(os.listdir(dist)):
        if not fn.endswith(".html"):
            continue
        pad = os.path.join(dist, fn)
        s = open(pad, encoding="utf-8").read()
        # alleen zichtbare tekst telt (head, scripts en structured data niet): technische SEO-wijzigingen zijn geen inhoudelijke update
        zicht = re.sub(r"<script[\s\S]*?</script>|<style[\s\S]*?</style>", " ", s.split("<body", 1)[-1])
        zicht = re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", zicht)).strip()
        h = hashlib.sha256(zicht.encode("utf-8")).hexdigest()[:16]
        r = dict(oud.get(fn) or {})
        if not r:
            r = {"gepubliceerd": VANDAAG, "bijgewerkt": VANDAAG}
        if "hash2" not in r:          # overstap naar tekst-hash: datum laten staan
            r.pop("hash", None); r["hash2"] = h
        if r["hash2"] != h:
            r["hash2"], r["bijgewerkt"] = h, VANDAAG
        nieuw[fn] = r
        if "@@" in s:
            j, m, d = r["bijgewerkt"].split("-")
            s = (s.replace("@@BIJGEWERKT_NL@@", f"{d}-{m}-{j}")
                  .replace("@@BIJGEWERKT_ISO@@", r["bijgewerkt"])
                  .replace("@@GEPUBLICEERD_ISO@@", r["gepubliceerd"]))
            open(pad, "w", encoding="utf-8").write(s)
    with open(DATUMS_JSON, "w") as f:
        json.dump(nieuw, f, indent=1, sort_keys=True)
        f.write("\n")
    return nieuw

def schone_links(dist):
    """Interne links zonder .html: Cloudflare Pages stuurt /x.html met een 308 door naar /x.
    Zo volgt Google geen omleidingen meer ("Page with redirect" in Search Console)."""
    pat = re.compile(r'href=(["\'])(?![a-z]+:|//|#)([^"\'#?]*?)\.html((?:[?#][^"\']*)?)\1')
    def vervang(m):
        q, pad, rest = m.group(1), m.group(2), m.group(3)
        if pad == "index" or pad.endswith("/index"):
            pad = pad[:-5] or "./"
        return f'href={q}{pad}{rest}{q}'
    for root, _, files in os.walk(dist):
        for fn in files:
            if fn.endswith(".html"):
                p = os.path.join(root, fn)
                t = open(p, encoding="utf-8").read()
                n = pat.sub(vervang, t)
                if n != t:
                    open(p, "w", encoding="utf-8").write(n)


if __name__ == "__main__":
    build()
