"""Bouwt het volledige verbeterconcept van collensgroup.com in src/concept/collensgroup-v3/.
Opdracht eigenaar 22-11-2026: complete website incl. info, links en artikelen, met grafische ontwerpen,
volgens zijn wensen (luxer, strak, professioneel, duidelijke grafieken, subpagina's, watermerk).
Alle prijzen en marktcijfers komen van de live site (met dezelfde bronnen).
Gebruik: python3 tools/concepten/collensgroup_v3.py
"""
import html, os

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
UIT = os.path.join(ROOT, "src", "concept", "collensgroup-v3")
LIVE = "../../"  # live site, voor artikelen en talen
e = lambda s: html.escape(s, quote=True)
FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
         '<link href="https://fonts.googleapis.com/css2?family=Geist:wght@400;500;600;700&display=swap" rel="stylesheet">')
LOGO = ('<svg width="30" height="30" viewBox="0 0 30 30" aria-hidden="true"><rect width="30" height="30" rx="8" fill="#14213D"/>'
        '<rect x="13.5" y="4" width="3" height="5" rx="1" fill="#F2B705"/><rect x="13.5" y="12" width="3" height="5" rx="1" fill="#F2B705"/>'
        '<rect x="13.5" y="20" width="3" height="6" rx="1" fill="#F2B705"/></svg>')

# ---------- showcase-scènes: echte schermen in apparaatframes ----------
IMG = "../../img/"
SC = {
 "ombre":  {"bg": "ombre", "br": ("beeld/ombre-d.jpg", "atelier-ombre.com"), "ph": ["beeld/ombre-m.jpg"],
            "alt": "Atelier Ombre, kunstwebshop op desktop en telefoon"},
 "suis":   {"bg": "zand", "br": ("beeld/suis-d.jpg", "suismuis.nl"), "ph": ["beeld/suis-m.jpg"],
            "alt": "Suismuis Home, webshop op desktop en telefoon"},
 "lubbyc": {"bg": "zee", "ph": [IMG + "lubbyc-kaart.jpg", IMG + "lubbyc-evenementen.jpg", IMG + "lubbyc-noodhulp.jpg"],
            "alt": "LubbyC reisapp: kaart, evenementen en noodhulp"},
 "games":  {"bg": "groen", "ph": [IMG + "koffer-spel.jpg", IMG + "eiland-weg.jpg"],
            "alt": "Koffer Vol! en Eiland Express op de telefoon"},
 "koffer": {"bg": "groen", "ph": [IMG + "koffer-spel.jpg", IMG + "koffer-gewonnen.jpg"],
            "alt": "Koffer Vol!: inpakken in Kyoto en level gehaald"},
 "eiland": {"bg": "lucht", "ph": [IMG + "eiland-weg.jpg", IMG + "eiland-rood.jpg"],
            "alt": "Eiland Express: rijden over het eiland"},
 "hero":   {"bg": "hero", "br": ("beeld/ombre-d.jpg", "atelier-ombre.com"), "ph": [IMG + "lubbyc-evenementen.jpg"],
            "alt": "Een website en een app van Collens Group: Atelier Ombre en LubbyC"},
 "ai":     {"bg": "nacht", "chat": "beeld/chat.jpg", "alt": "AI-adviseur op de website van Collens Group"},
 "manu":   {"bg": "nacht", "film": IMG + "manu-lantaarnfeest.jpg", "alt": "Manu en Khanun: het lantaarnfeest"},
}
def scene(key, chips=(), cls="", eager=False):
    c = SC[key]; lz = "" if eager else ' loading="lazy"'; s = ""
    if "br" in c:
        s += (f'<div class="sc-br"><div class="bk"><i></i><i></i><i></i><span>{e(c["br"][1])}</span></div>'
              f'<img src="{c["br"][0]}" alt="{e(c["alt"])}"{lz}></div>')
        s += f'<div class="sc-ph sc-p1"><img src="{c["ph"][0]}" alt=""{lz}></div>'
    elif "chat" in c:
        s += f'<div class="sc-chat"><img src="{c["chat"]}" alt="{e(c["alt"])}"{lz}></div>'
    elif "film" in c:
        s += f'<div class="sc-film"><img src="{c["film"]}" alt="{e(c["alt"])}"{lz}></div>'
    else:
        n = len(c["ph"])
        for i, src in enumerate(c["ph"]):
            alt = e(c["alt"]) if i == 0 else ""
            s += f'<div class="sc-ph sc-n{n} sc-i{i+1}"><img src="{src}" alt="{alt}"{lz}></div>'
    for i, (txt, sub, kleur) in enumerate(chips):
        s += f'<div class="chip ch{i+1}"><i class="{kleur}"></i><span>{e(txt)}<small>{e(sub)}</small></span></div>'
    return f'<div class="scene bg-{c["bg"]} {cls}">{s}</div>'

DSCENE = {"websites": ("ombre", [("Snel en mobiel", "Core Web Vitals in orde", "gr")]),
          "webshops": ("suis", [("Bestelling ontvangen", "iDEAL · verzending ingesteld", "go")]),
          "apps": ("lubbyc", [("iPhone en Android", "één app, twee stores", "gr")]),
          "games": ("games", [("Level 12 gehaald", "scorebord en sterren", "go")]),
          "ai": ("ai", [("Vraag beantwoord", "uit jouw eigen teksten", "gr"), ("Twijfelgeval", "doorgestuurd naar jou", "go")])}
DTHUMB = {"websites": "beeld/ombre-d.jpg", "webshops": "beeld/suis-d.jpg", "apps": IMG + "lubbyc-kaart.jpg", "games": IMG + "koffer-spel.jpg", "ai": "beeld/chat.jpg"}

# ---------- gegevens (van de live site) ----------
DIENSTEN = [
 {"slug": "websites", "naam": "Websites", "kort": "One-page tot bedrijfswebsite", "vanaf": 495,
  "kop": "Websites die werken voor je bedrijf.", "lead": "Snel, vindbaar in Google en sterk op de telefoon. Een one-page site vanaf €495, een bedrijfswebsite tot zes pagina's vanaf €995.",
  "pakketten": [("One-page", 495, "3–5 dagen", ["Alle info op één pagina", "Contactformulier", "Mobielvriendelijk en snel", "Basis-SEO en Google-koppeling"]),
                ("Bedrijfswebsite", 995, "2–3 weken", ["Tot 6 pagina's", "Teksten op Google afgestemd", "Contact- en offerteformulier", "Snelheid en Core Web Vitals in orde"]),
                ("Webshop", 1950, "3–5 weken", ["Tot 50 producten ingericht", "iDEAL en andere betaalmethoden", "Verzending ingesteld", "Je beheert zelf je producten"])],
  "markt": [("Eenvoudige website", "markt", 500, 2000), ("Geavanceerde website", "markt", 2000, 5000), ("One-page", "wij", 495, 495), ("Bedrijfswebsite", "wij", 995, 995)],
  "max": 5000, "bron": ("Trustoo, Wat kost een website laten maken? (nov. 2026)", "https://trustoo.nl/kosten/webdesign-kosten/"),
  "faq": [("Ben ik eigenaar van de website?", "Ja. De site, het domein en de inhoud staan op jouw naam. Je zit niet vast aan een websitebouwer."),
          ("Word ik gevonden in Google?", "Elke site bouwen we snel, mobielvriendelijk en met de technische basis die Google verwacht. Een toppositie kan niemand garanderen; wel helpen we je op weg met de juiste zoekwoorden."),
          ("Wat kost een website per maand?", "Hosting kan voor de meeste kleine sites gratis. Een domeinnaam kost meestal €10 tot €25 per jaar. Onderhoud is optioneel vanaf €29 per maand."),
          ("Kan ik later uitbreiden?", "Ja. Een extra pagina kost €95, inclusief SEO-tekst.")],
  "artikelen": ["wat-kost-een-website", "zelf-website-bouwen-of-laten-maken", "website-laten-maken-afspraken"]},
 {"slug": "webshops", "naam": "Webshops", "kort": "Verkopen, betalen, verzenden", "vanaf": 1950,
  "kop": "Een webshop die verkoopt, niet alleen bestaat.", "lead": "Snel, overzichtelijk op de telefoon en jij beheert zelf je producten. Vanaf €1.950 met tot vijftig producten al voor je ingericht.",
  "pakketten": [("Webshop", 1950, "3–5 weken", ["Tot 50 producten ingericht", "iDEAL en andere betaalmethoden", "Verzendkosten ingesteld", "Jij beheert producten, voorraad en bestellingen"]),
                ("Extra pagina", 95, "per pagina", ["Bijvoorbeeld merkverhaal of klantenservice", "Inclusief SEO-tekst"]),
                ("Onderhoud", 29, "per maand", ["Updates en back-ups", "Kleine wijzigingen tot 30 minuten per maand"])],
  "markt": [("Freelancer", "markt", 2000, 8000), ("Bureau (mkb)", "markt", 5000, 15000), ("Collens Group", "wij", 1950, 1950)],
  "max": 15000, "bron": ("Searchlab, Wat kost een webshop laten maken (2026)", "https://searchlab.nl/kosten/wat-kost-een-webshop-laten-maken"),
  "faq": [("Kan ik later meer producten toevoegen?", "Ja, dat doe je zelf in het beheer. Er zit geen limiet op wat je later toevoegt."),
          ("Ben ik eigenaar van de webshop?", "Ja. De shop, het domein en de inhoud staan op jouw naam."),
          ("Welke kosten komen erbij?", "Een domeinnaam (meestal €10 tot €25 per jaar). Het webshopplatform en de betaalprovider rekenen eigen tarieven; die staan vooraf in de offerte.")],
  "artikelen": ["wat-kost-een-webshop", "webshop-laten-maken", "website-laten-maken-belgie"]},
 {"slug": "apps", "naam": "Apps", "kort": "iPhone en Android tegelijk", "vanaf": 3150,
  "kop": "Eén app. iPhone en Android tegelijk.", "lead": "Van een eerste versie om je idee te testen tot een compleet platform met accounts en betalingen. Vaste prijs, vooraf.",
  "pakketten": [("Basis / MVP", 3150, "3–5 weken", ["Tot 5 schermen", "Eenvoudige navigatie en inhoud", "Publicatieklaar voor iOS of Android"]),
                ("Standaard", 6750, "6–10 weken", ["5 tot 12 schermen", "Accounts en inloggen", "Database en pushmeldingen", "In App Store en Google Play"]),
                ("Maatwerk / Pro", 13050, "10–16+ weken", ["12+ schermen en beheerdashboard", "Betalingen en abonnementen", "Meerdere gebruikersrollen", "Extra beveiliging"])],
  "markt": [("Eenvoudige app (markt)", "markt", 5000, 25000), ("Basis / MVP", "wij", 3150, 3150), ("Standaard", "wij", 6750, 6750), ("Maatwerk / Pro", "wij", 13050, 13050)],
  "max": 25000, "bron": ("Searchlab, Wat kost een app laten maken (2026)", "https://searchlab.nl/kosten/wat-kost-een-app-laten-maken"),
  "faq": [("Ben ik eigenaar van mijn app?", "Ja. Na de laatste betaling is de broncode van jou. De app staat op jouw eigen Apple- en Google-account."),
          ("Wat kost een app na de lancering?", "Apple rekent $99 per jaar, Google $25 eenmalig. Hosting is voor kleine apps vaak €0 tot €25 per maand. Ons onderhoud is optioneel, vanaf €85,50 per maand."),
          ("Hoe betaal ik?", "In drie delen: 40% bij akkoord, 40% bij een goedgekeurde testversie en 20% bij oplevering.")],
  "artikelen": ["app-laten-maken-kosten", "mvp-app-laten-maken", "app-of-website"]},
 {"slug": "games", "naam": "Games", "kort": "Merkgame tot 2D-game", "vanaf": 1950,
  "kop": "Games die mensen echt spelen.", "lead": "Casual 2D-games voor de browser, iPhone en Android. Voor je merk, je klanten of als eigen product.",
  "pakketten": [("Merkgame", 1950, "2–3 weken", ["Webgame in jouw huisstijl", "1 spelprincipe, bijv. quiz of reactiespel", "Scorebord en deelknop"]),
                ("Casual game", 4950, "4–6 weken", ["1 uitgewerkt spelprincipe", "Geluid en animaties", "Voor iOS, Android of browser"]),
                ("2D-game met levels", 9950, "8–12 weken", ["Meerdere levels en voortgang", "Eigen personages en wereld", "Live in App Store en Google Play"])],
  "markt": [("Eenvoudige mobiele game (markt)", "markt", 10000, 10000), ("Merkgame", "wij", 1950, 1950), ("Casual game", "wij", 4950, 4950), ("2D-game met levels", "wij", 9950, 9950)],
  "max": 12000, "bron": ("Juego Studios, Cost of Game Development in the Netherlands (2026): vanaf ±€10.000", "https://www.juegostudio.com/blog/cost-of-game-development-netherlands"),
  "faq": [("Welke games maken jullie?", "Casual 2D-games: puzzels, quizzen, reactie- en arcadespellen. Grote 3D-games of online multiplayer doen we niet."),
          ("Kan ik geld verdienen met mijn game?", "Ja, we kunnen advertenties of aankopen in de game inbouwen volgens de regels van Apple en Google."),
          ("Moeten spelers een app downloaden?", "Niet bij een merkgame: die draait in de browser via een link of QR-code.")],
  "artikelen": ["game-laten-maken", "merkgame-laten-maken-kerst", "apps"]},
 {"slug": "ai", "naam": "AI en automatisering", "kort": "Workflows en chatbots", "vanaf": 395,
  "kop": "Werk dat vanzelf gaat.", "lead": "Mails, offertes, planning en klantvragen: AI-tools die je bestaande apps aan elkaar koppelen, met jou in controle.",
  "pakketten": [("Automatisering", 395, "2–5 dagen", ["1 workflow, bijv. formulier → CRM → mail", "Koppelt je bestaande apps", "Getest en gedocumenteerd"]),
                ("AI-chatbot", 995, "1 week", ["Beantwoordt vragen op je website", "Getraind op je eigen teksten", "Stuurt twijfelgevallen door naar jou"]),
                ("AI-assistent", 1950, "2–4 weken", ["Meerdere workflows en koppelingen", "Mail, agenda, documenten en CRM", "Jij houdt de eindcontrole"])],
  "markt": [("AI-agent (markt)", "markt", 2000, 8000), ("Automatisering", "wij", 395, 395), ("AI-chatbot", "wij", 995, 995), ("AI-assistent", "wij", 1950, 1950)],
  "max": 8000, "bron": ("Searchlab, Wat kost een AI-agent laten bouwen (2026)", "https://searchlab.nl/kosten/wat-kost-een-ai-agent-laten-bouwen"),
  "faq": [("Heb je mijn wachtwoorden nodig?", "Nee. We gebruiken officiële koppelingen en jij houdt de regie over je accounts."),
          ("Kan de chatbot foute antwoorden geven?", "Dat is het grootste risico van AI. Daarom beperken we hem tot jouw eigen informatie en laat hij twijfelvragen aan jou over."),
          ("Wat kost het per maand?", "Het AI-gebruik zelf, voor een klein bedrijf meestal een paar euro tot enkele tientjes. Beheer door ons is optioneel, €49 per maand.")],
  "artikelen": ["chatbot-laten-maken", "ai-automatisering", "en-ai-chatbot"]},
]
ARTIKELEN = {
 "wat-kost-een-website": ("Kosten", "Wat kost een website laten maken in 2026?", "Marktprijzen, bijkomende kosten per jaar en onze vaste prijzen vanaf €495."),
 "wat-kost-een-webshop": ("Kosten", "Wat kost een webshop laten maken?", "Marktprijzen, bijkomende kosten en onze vaste prijs vanaf €1.950."),
 "app-laten-maken-kosten": ("Kosten", "Wat kost een app laten maken?", "Prijzen, doorlooptijd en vaste kosten van een app, en hoe je bespaart."),
 "mvp-app-laten-maken": ("Keuzehulp", "MVP-app laten maken", "Test je app-idee eerst met een kleine versie: wat erin zit en wat het kost."),
 "app-of-website": ("Keuzehulp", "App of website: wat past bij jou?", "Kosten, doorlooptijd en wanneer een app echt nodig is, naast elkaar."),
 "zelf-website-bouwen-of-laten-maken": ("Keuzehulp", "Zelf een website bouwen of laten maken?", "Wix, Squarespace of WordPress tegenover laten maken: kosten, tijd en eigendom."),
 "website-laten-maken-afspraken": ("Keuzehulp", "Website laten maken: 8 afspraken vooraf", "Prijs, eigendom, levertijd, hosting en onderhoud: waar je vooraf naar vraagt."),
 "goedkope-website-laten-maken": ("Kosten", "Goedkope website laten maken", "Wanneer goedkoop prima is, en waar je op moet letten."),
 "webshop-laten-maken": ("Diensten", "Webshop laten maken vanaf €1.950", "Tot 50 producten ingericht, iDEAL en verzending geregeld."),
 "chatbot-laten-maken": ("Diensten", "AI-chatbot laten maken", "Een chatbot die vragen beantwoordt vanuit jouw eigen teksten."),
 "ai-automatisering": ("Diensten", "AI en automatisering", "Welk pakket past bij jouw terugkerende werk."),
 "game-laten-maken": ("Diensten", "Game laten maken", "Merkgame, casual game of 2D-game met levels."),
 "merkgame-laten-maken-kerst": ("Diensten", "Merkgame voor kerst", "Een eigen kerstgame voor je merk, klanten of personeel."),
 "apps": ("Eigen werk", "Onze apps en games", "LubbyC, Koffer Vol!, Eiland Express en Manu en Khanun."),
 "en-ai-chatbot": ("English", "AI chatbot for small business", "What an AI chatbot does for your business and what it costs."),
 "website-laten-maken-horeca": ("Per branche", "Website voor horeca", "Menukaart, openingstijden, reserveren en route op je telefoon."),
 "app-laten-maken-horeca": ("Per branche", "App voor horeca", "Spaarkaart, vooraf bestellen, reserveren en pushberichten."),
 "website-laten-maken-kapper": ("Per branche", "Website voor kapper", "Prijslijst, online afspraak maken en foto's van je werk."),
 "website-laten-maken-schoonheidssalon": ("Per branche", "Website voor salon of nagelstudio", "Behandelingen met prijs, online boeken en cadeaubonnen."),
 "website-laten-maken-fotograaf": ("Per branche", "Website voor fotograaf", "Snelle portfolio, pakketten en een boekformulier."),
 "website-laten-maken-aannemer": ("Per branche", "Website voor aannemer of installateur", "Offerteformulier, werkgebied en projecten."),
 "website-laten-maken-coach-zzp": ("Per branche", "Website voor coach en zzp'er", "Duidelijk aanbod, over jou en kennismaking boeken."),
 "website-laten-maken-vakantiehuis": ("Per branche", "Website voor vakantiehuis en B&B", "Foto's, beschikbaarheid en aanvragen rechtstreeks."),
 "website-laten-maken-belgie": ("Per branche", "Website laten maken in België", "Wat het kost, waar je op let en hoe wij werken."),
}
eur = lambda p: "€" + f"{p:,}".replace(",", ".")

# ---------- onderdelen ----------
def header(actief, dark=False):
    paneel = "".join(f'<a href="{d["slug"]}.html"><img class="th" src="{DTHUMB[d["slug"]]}" alt="" loading="lazy"><div><b>{e(d["naam"])}</b><span>{e(d["kort"])} · vanaf {eur(d["vanaf"])}</span></div></a>' for d in DIENSTEN)
    def m(href, naam):
        return f'<a href="{href}"{" aria-current=\"page\"" if actief == href else ""}>{naam}</a>'
    return (f'<div class="balk"><b>Verbeterconcept</b> voor collensgroup.com · alle pagina\'s klikbaar · niet live</div>'
            f'<header class="top{" dark-h" if dark else ""}"><div class="wrap"><a class="merk" href="index.html">{LOGO}Collens Group</a>'
            f'<nav class="menu" id="menu" aria-label="Hoofdmenu"><div class="drop"><button type="button" aria-haspopup="true">Diensten</button><div class="paneel">{paneel}</div></div>'
            f'{m("prijzen.html","Prijzen")}{m("werk.html","Werk")}{m("artikelen.html","Artikelen")}{m("over-ons.html","Over ons")}{m("contact.html","Contact")}</nav>'
            f'<div class="acties"><a class="taal" href="{LIVE}en">EN</a><a class="knop{" goud" if dark else ""}" href="contact.html">Gratis concept</a>'
            f'<button class="hamburger" aria-label="Menu" aria-expanded="false" onclick="var m=document.getElementById(\'menu\');var o=m.classList.toggle(\'open\');this.setAttribute(\'aria-expanded\',o)">'
            f'<svg viewBox="0 0 24 24" width="24" height="24" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M4 8h16M4 16h16"/></svg></button></div></div></header>')

def footer():
    kol = [("Diensten", [(f'{d["slug"]}.html', d["naam"]) for d in DIENSTEN]),
           ("Bedrijf", [("over-ons.html", "Over ons"), ("werk.html", "Eigen werk"), ("prijzen.html", "Prijzen"), ("contact.html", "Contact")]),
           ("Kennis", [("artikelen.html", "Alle artikelen"), (LIVE + "wat-kost-een-website", "Wat kost een website?"), (LIVE + "app-of-website", "App of website?"), (LIVE + "kostencalculator", "Kostencalculator")]),
           ("Talen", [(LIVE, "Nederlands"), (LIVE + "en", "English"), (LIVE + "de", "Deutsch"), (LIVE + "fr", "Français"), (LIVE + "es", "Español"), (LIVE + "th", "ไทย"), (LIVE + "my", "မြန်မာ")])]
    k = "".join(f'<div><h4>{e(t)}</h4>' + "".join(f'<a href="{h}">{e(n)}</a>' for h, n in items) + "</div>" for t, items in kol)
    return (f'<footer class="voet"><div class="wrap"><div class="kol"><div><a class="merk" href="index.html" style="color:#fff">{LOGO}Collens Group</a>'
            f'<p style="margin-top:18px;max-width:30ch">Websites, webshops, apps, games en AI. Persoonlijk ontworpen, vaste prijs, wereldwijd online.</p>'
            f'<p style="margin-top:14px"><a href="mailto:info@collensgroup.com" style="display:inline;color:#fff">info@collensgroup.com</a></p></div>{k}</div>'
            f'<div class="slot"><span>© 2026 Collens Group · Alle prijzen zijn eindprijzen: er komt geen btw bij.</span><span><a href="{LIVE}privacy" style="display:inline">Privacy</a></span></div></div></footer>'
            '<div class="watermerk">Concept · Collens Group</div>')

import hashlib
CSSV = hashlib.md5(open(os.path.join(UIT, 'stijl.css'), 'rb').read()).hexdigest()[:8]
def pagina(naam, titel, desc, body, actief="", dark=False, script=""):
    doc = (f'<!DOCTYPE html><html lang="nl"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">'
           f'<meta name="robots" content="noindex, nofollow"><title>{e(titel)}</title><meta name="description" content="{e(desc)}">{FONTS}'
           f'<link rel="stylesheet" href="stijl.css?v={CSSV}"><link rel="icon" href="../../img/favicon-48.png"></head><body>'
           f'{header(actief, dark)}<main id="inhoud">{body}</main>{footer()}{script}</body></html>')
    with open(os.path.join(UIT, naam), "w", encoding="utf-8") as f:
        f.write(doc)

def grafiek(d, dark=False):
    mx = d["max"]
    rijen = ""
    for naam, soort, lo, hi in d["markt"]:
        links = lo / mx * 100
        breed = max((hi - lo) / mx * 100, 1.6)
        lab = eur(lo) if lo == hi else f"{eur(lo)} – {eur(hi)}"
        if soort == "markt" and lo == hi: lab = "vanaf " + eur(lo)
        rijen += (f'<div class="gr-rij"><div class="lb">{e(naam)}<small>{"marktprijs" if soort == "markt" else "Collens Group, eindprijs"}</small></div>'
                  f'<div class="balkje"><div class="as"></div><div class="bar{" wij" if soort == "wij" else ""}{" lv" if links + breed > 62 else ""}" style="left:{links:.2f}%;width:{breed:.2f}%"><span>{lab}</span></div></div></div>')
    stap = mx / 4
    schaal = "".join(f"<span>{eur(int(stap * i))}</span>" for i in range(5))
    return (f'<div class="grafiek"><h3>{e(d["naam"])}: wat je betaalt</h3><div style="margin-top:18px">{rijen}</div>'
            f'<div class="schaal"><span></span><div>{schaal}</div></div>'
            f'<p class="bron">Bron marktprijzen: <a href="{d["bron"][1]}" rel="nofollow noopener">{e(d["bron"][0])}</a>. Onze prijzen: vanaf-prijzen, eindprijs.</p></div>')

def artikelkaarten(slugs):
    return '<div class="artikelen">' + "".join(
        f'<a class="ar" href="{LIVE}{s}"><small>{e(ARTIKELEN[s][0])}</small><b>{e(ARTIKELEN[s][1])}</b><p>{e(ARTIKELEN[s][2])}</p><span class="lees">Lees het artikel →</span></a>'
        for s in slugs) + "</div>"

def faq(items):
    return "".join(f"<details><summary>{e(q)}</summary><p>{e(a)}</p></details>" for q, a in items)

def band():
    return (f'<section style="padding-top:0"><div class="wrap"><div class="band"><svg class="deco" viewBox="0 0 200 200" fill="none" aria-hidden="true"><circle cx="100" cy="100" r="98" stroke="#d4a017" stroke-width=".6"/><circle cx="100" cy="100" r="70" stroke="#d4a017" stroke-width=".6"/><circle cx="100" cy="100" r="42" stroke="#d4a017" stroke-width=".6"/></svg>'
            f'<div><h2>Benieuwd hoe jouw site eruit kan zien?</h2><p>Je krijgt binnen 48 uur een gratis concept, ontworpen voor jouw bedrijf. Pas als het je bevalt, praten we over een vaste prijs.</p></div>'
            f'<a class="knop goud" href="contact.html">Vraag je gratis concept aan</a></div></div></section>')

def stappen(dark=True):
    st = [("Je aanvraag", "Een paar zinnen over je bedrijf en wat je wilt bereiken.", "vandaag"),
          ("Je concept", "Onderzocht en ontworpen voor jouw bedrijf, niet voor een branche.", "binnen 48 uur"),
          ("Vaste prijs", "Wat erin zit, wat het kost en wanneer het klaar is.", "na jouw reactie"),
          ("Bouwen", "Tussentijdse versies die je zelf test en goedkeurt.", "per project"),
          ("Live", "Op je eigen domein of in je eigen store-account.", "opgeleverd")]
    return '<div class="stappen">' + "".join(f'<div class="stap{" uit" if i == 1 else ""}"><span class="n">{i+1}</span><h3>{e(h)}</h3><p>{e(p)}</p><small>{e(t)}</small></div>' for i, (h, p, t) in enumerate(st)) + "</div>"

WERK = [("LubbyC", "Reisapp · binnenkort in Google Play", "Reizigers in de buurt ontmoeten en samen plannen.", "lubbyc-evenementen.jpg", LIVE + "app-lubbyc"),
        ("Koffer Vol!", "Puzzelgame", "Inpakpuzzel met honderd levels in tien landen.", "koffer-spel.jpg", LIVE + "app-koffer-vol"),
        ("Eiland Express", "3D-rijgame · in ontwikkeling", "Met een songthaew over een tropisch eiland.", "eiland-weg.jpg", LIVE + "app-eiland-express"),
        ("Manu en Khanun", "Animatieserie · in productie", "Een Nederlandse jongen en een babyolifant in Noord-Thailand.", "manu-personages.jpg", LIVE + "app-manu-en-khanun")]
def _oud_werkkaarten(items, cls="werk"):
    return f'<div class="{cls}">' + "".join(f'<a class="wk" href="{h}"><img src="../../img/{img}" alt="{e(n)}: {e(p)}" loading="lazy"><div><small>{e(s)}</small><b>{e(n)}</b><p>{e(p)}</p></div></a>' for n, s, p, img, h in items) + "</div>"

FORM = ('<form class="form" onsubmit="event.preventDefault();this.querySelector(\'.onder small\').textContent=\'Dit is het concept. Op de echte site gaat je aanvraag nu naar ons en hoor je binnen 48 uur van ons.\'">'
        '<div class="rij"><div><label for="f1">Naam</label><input id="f1" autocomplete="name" required></div>'
        '<div><label for="f2">E-mail</label><input id="f2" type="email" autocomplete="email" required></div>'
        '<div><label for="f3">Bedrijf en huidige website</label><input id="f3"></div>'
        '<div><label for="f4">Wat wil je laten maken?</label><select id="f4"><option>Website</option><option>Webshop</option><option>App</option><option>Game</option><option>AI en automatisering</option><option>Weet ik nog niet</option></select></div>'
        '<div class="vol"><label for="f5">Wat moet het voor je klanten doen?</label><textarea id="f5" rows="3"></textarea></div></div>'
        '<div class="onder"><button class="knop" type="submit">Verstuur aanvraag</button><small>Reactie binnen 48 uur. We gebruiken je gegevens alleen voor je aanvraag.</small></div></form>')

PROBEER_JS = """<script>(function(){var V={
bakker:{kop:"Vers van de plaat, elke ochtend vanaf zeven uur.",sub:"Bestel vandaag, haal morgen op. Taarten op maat voor elk feest.",knop:"Bestel voor morgen",menu:["Assortiment","Bestellen","Contact"],r:[["Dagvers","brood en gebak"],["Op maat","taarten voor feesten"],["Open","ma–za 7–18 uur"]],k:"#7a3e1d",z:"#f7efe7"},
bouw:{kop:"Vakwerk dat je ziet, een prijs die vooraf vaststaat.",sub:"Offerte binnen een dag, met projecten uit jouw buurt.",knop:"Vraag een offerte",menu:["Projecten","Werkwijze","Contact"],r:[["Projecten","in de regio"],["Werkgebied","postcodecheck"],["Spoed","direct bellen"]],k:"#1e3a52",z:"#eaf0f5"},
zorg:{kop:"Een afspraak maken kost je nu tien seconden.",sub:"Kies je behandeling en een tijd die past. Herinnering vooraf.",knop:"Plan een afspraak",menu:["Behandelingen","Prijzen","Team"],r:[["Behandelingen","met prijzen"],["Online plannen","dag en nacht"],["Ons team","maak kennis"]],k:"#2d5a4c",z:"#e8f1ed"},
winkel:{kop:"Vandaag besteld, morgen in huis.",sub:"Snel verzonden, makkelijk retour. Ontdek de nieuwe collectie.",knop:"Bekijk de collectie",menu:["Nieuw","Collectie","Service"],r:[["Nieuw binnen","deze week"],["Bestsellers","meest gekocht"],["Service","verzenden en retour"]],k:"#3b2a50",z:"#f0ebf5"},
advies:{kop:"Helder advies, zonder kleine lettertjes.",sub:"Plan een kennismaking. Daarna weet je precies wat het kost.",knop:"Plan een kennismaking",menu:["Diensten","Werkwijze","Kennis"],r:[["Diensten","wat we doen"],["Werkwijze","in drie stappen"],["Kennisbank","artikelen"]],k:"#14213d",z:"#ebeef4"}};
var vak="bakker",$=function(i){return document.getElementById(i)};
function slug(n){return(n.toLowerCase().normalize("NFD").replace(/[\\u0300-\\u036f]/g,"").replace(/[^a-z0-9]+/g,"")||"jouwbedrijf")+".nl"}
function naam(){var n=$("naam").value.trim()||"Jouw bedrijf";$("s-naam").textContent=n;$("url").textContent=slug(n)}
function zet(){var v=V[vak],t=$("s-tekst");t.classList.add("uit");setTimeout(function(){$("s-kop").textContent=v.kop;$("s-sub").textContent=v.sub;$("s-knop").textContent=v.knop;
$("s-menu").innerHTML=v.menu.map(function(m){return"<span>"+m+"</span>"}).join("");["r1","r2","r3"].forEach(function(id,i){$(id).innerHTML=v.r[i][0]+"<small>"+v.r[i][1]+"</small>"});t.classList.remove("uit")},220);
$("ms").style.setProperty("--k",v.k);$("ms").style.setProperty("--z",v.z)}
$("naam").addEventListener("input",naam);document.querySelectorAll(".chips button").forEach(function(b){b.addEventListener("click",function(){
document.querySelectorAll(".chips button").forEach(function(x){x.setAttribute("aria-pressed","false")});b.setAttribute("aria-pressed","true");vak=b.dataset.v;zet()})});naam()})();</script>"""

# ---------- pagina's ----------
def home():
    diensten = "".join(
        f'<a class="dk{" breed" if i < 2 else ""}" href="{d["slug"]}.html">{scene(DSCENE[d["slug"]][0], DSCENE[d["slug"]][1], "klein")}<div class="dk-t"><h3>{e(d["naam"])}</h3><p>{e(d["kort"])}</p>'
        f'<div class="pr"><span>vanaf</span><b>{eur(d["vanaf"])}</b></div></div></a>' for i, d in enumerate(DIENSTEN))
    alle = {"naam": "Alles op een rij", "max": 25000, "markt": [
        ("Website (markt)", "markt", 500, 2000), ("Website bij ons", "wij", 495, 995),
        ("Webshop, freelancer (markt)", "markt", 2000, 8000), ("Webshop bij ons", "wij", 1950, 1950),
        ("Eenvoudige app (markt)", "markt", 5000, 25000), ("App bij ons", "wij", 3150, 13050),
        ("AI-agent (markt)", "markt", 2000, 8000), ("AI bij ons", "wij", 395, 1950)],
        "bron": ("Trustoo (website), Searchlab (webshop, app, AI-agent), 2026", "https://searchlab.nl/kosten/wat-kost-een-app-laten-maken")}
    body = f'''
<section class="hero"><div class="wrap"><div>
 <h1>Jouw idee.<br>Razendsnel live.</h1>
 <p class="lead">Websites, webshops, apps, games en AI, persoonlijk ontworpen voor jouw bedrijf. Binnen 48 uur zie je je eigen concept. Pas als je het goed vindt, maken we een vaste prijs.</p>
 <div class="rij"><a class="knop goud" href="contact.html">Vraag je gratis concept aan</a><a class="knop licht" href="werk.html">Bekijk ons werk</a></div>
 <div class="feit"><div><b>48 uur</b>tot je eigen concept</div><div><b>€495</b>websites vanaf, eindprijs</div><div><b>7 talen</b>wereldwijd online</div></div>
</div><div class="hero-sc">{scene("hero", [("Nieuwe aanvraag", "vandaag binnen", "go"), ("Concept klaar", "binnen 48 uur", "gr"), ("Live", "op je eigen domein", "gr")], "groot", True)}</div></div></section>

<section><div class="wrap probeer">
 <div><p class="oog">Probeer het zelf</p><h2 style="font-size:clamp(32px,3.6vw,48px)">Zie hoe snel een site van jou wordt.</h2>
  <p class="zacht" style="margin:20px 0 28px;font-size:18px;max-width:40ch">Typ je bedrijfsnaam en kies je vak. Een echt concept gaat veel verder: jouw diensten, kleuren, foto's en de manier waarop jouw klanten kopen.</p>
  <div class="veld"><input id="naam" value="Bakkerij De Vries" maxlength="30" autocomplete="organization" aria-label="Bedrijfsnaam"></div>
  <div class="chips" role="group" aria-label="Vak"><button type="button" data-v="bakker" aria-pressed="true">Horeca</button><button type="button" data-v="bouw" aria-pressed="false">Bouw</button><button type="button" data-v="zorg" aria-pressed="false">Salon of praktijk</button><button type="button" data-v="winkel" aria-pressed="false">Winkel</button><button type="button" data-v="advies" aria-pressed="false">Advies</button></div>
 </div>
 <div class="browser" aria-live="polite"><div class="bk"><i></i><i></i><i></i><span id="url">bakkerijdevries.nl</span></div>
  <div class="ms" id="ms"><div class="n"><b id="s-naam">Bakkerij De Vries</b><em id="s-menu"><span>Assortiment</span><span>Bestellen</span><span>Contact</span></em></div>
  <div class="h"><svg viewBox="0 0 200 200" fill="none"><circle cx="100" cy="100" r="90" stroke="#fff"/><circle cx="100" cy="100" r="60" stroke="#fff"/></svg><div class="fade" id="s-tekst"><h4 id="s-kop">Vers van de plaat, elke ochtend vanaf zeven uur.</h4><p id="s-sub">Bestel vandaag, haal morgen op. Taarten op maat voor elk feest.</p><a href="contact.html" id="s-knop">Bestel voor morgen</a></div></div>
  <div class="g"><div id="r1">Dagvers<small>brood en gebak</small></div><div id="r2">Op maat<small>taarten voor feesten</small></div><div id="r3">Open<small>ma–za 7–18 uur</small></div></div></div></div>
</div></section>

<section style="padding-top:0"><div class="wrap">
 <div class="kop2"><div><p class="oog">Diensten</p><h2>Alles digitaal onder één dak.</h2></div><p class="zacht">Kies wat je nodig hebt. Elke dienst heeft een eigen pagina met pakketten, levertijden, een prijsvergelijking en veelgestelde vragen.</p></div>
 <div class="diensten">{diensten}</div>
</div></section>

<section class="dark"><div class="wrap">
 <div class="kop2"><div><p class="oog">Eerlijk vergeleken</p><h2>Wat je bij ons betaalt, naast de markt.</h2></div><p class="zacht">Marktprijzen uit onafhankelijke kostengidsen, onze prijzen als vaste eindprijs. Geen btw erbij, geen verrassingen achteraf.</p></div>
 {grafiek(alle, True)}
 <div style="margin-top:96px"><p class="oog">Werkwijze</p><h2 style="font-size:clamp(32px,3.6vw,48px);max-width:14ch;margin-bottom:64px">Je ziet het eerst. Je beslist daarna.</h2>{stappen()}</div>
</div></section>

<section><div class="wrap">
 <div class="kop2"><div><p class="oog">Eigen werk</p><h2>Wat we voor onszelf maken.</h2></div><p class="zacht">Echte schermen uit onze eigen apps en games. Zo testen we elke werkwijze eerst op onszelf. <a href="werk.html">Bekijk al ons werk →</a></p></div>
 {werkmini()}
</div></section>

<section style="padding-top:0"><div class="wrap">
 <div class="kop2"><div><p class="oog">Kennis</p><h2>Artikelen en gidsen.</h2></div><p class="zacht">Eerlijke antwoorden op wat ondernemers ons het vaakst vragen. <a href="artikelen.html">Alle artikelen →</a></p></div>
 {artikelkaarten(["wat-kost-een-website", "app-of-website", "zelf-website-bouwen-of-laten-maken"])}
</div></section>
{band()}'''
    pagina("index.html", "Collens Group – websites, apps, games en AI, persoonlijk ontworpen", "Websites, webshops, apps, games en AI, persoonlijk ontworpen. Gratis concept binnen 48 uur, vaste eindprijs.", body, "index.html", dark=True, script=PROBEER_JS)

def dienst(d):
    pk = "".join(f'<div class="pk{" top" if i == 1 and len(d["pakketten"]) == 3 else ""}"><h3>{e(n)}</h3><div class="prijs"><small>vanaf</small>{eur(p)}</div><p class="duur">{e(t)}</p><ul>' + "".join(f"<li>{e(x)}</li>" for x in items) + "</ul></div>" for i, (n, p, t, items) in enumerate(d["pakketten"]))
    andere = "".join(f'<a class="ar" href="{x["slug"]}.html"><small>Ook bij ons</small><b>{e(x["naam"])}</b><p>{e(x["kort"])} · vanaf {eur(x["vanaf"])}</p><span class="lees">Bekijk →</span></a>' for x in DIENSTEN if x["slug"] != d["slug"])
    body = f'''
<div class="pkop"><div class="wrap"><div><p class="kruimel"><a href="index.html">Home</a> / Diensten / {e(d["naam"])}</p><h1>{e(d["kop"])}</h1><p>{e(d["lead"])}</p>
 <div style="display:flex;gap:12px;flex-wrap:wrap;margin-top:32px"><a class="knop" href="contact.html">Vraag je gratis concept aan</a><a class="knop licht" href="prijzen.html">Alle prijzen</a></div></div>
 {scene(DSCENE[d["slug"]][0], DSCENE[d["slug"]][1], "kop", True)}</div></div>
<section><div class="wrap"><div class="kop2"><div><p class="oog">Pakketten</p><h2>Vaste prijs, vooraf.</h2></div><p class="zacht">Bij "vanaf" hoort het pakket zoals beschreven. Wijkt jouw project af, dan krijg je eerst een vaste prijs op maat. Alle prijzen zijn eindprijzen: er komt geen btw bij.</p></div><div class="pakketten">{pk}</div></div></section>
<section style="padding-top:0"><div class="wrap">{grafiek(d)}</div></section>
<section class="dark"><div class="wrap"><p class="oog">Zo werken we</p><h2 style="font-size:clamp(32px,3.6vw,48px);max-width:14ch;margin-bottom:64px">Je ziet het eerst. Je beslist daarna.</h2>{stappen()}</div></section>
<section><div class="wrap twee"><div><p class="oog">Veelgestelde vragen</p><h2 style="font-size:clamp(30px,3.4vw,44px)">Wat ondernemers ons vragen.</h2></div><div>{faq(d["faq"])}</div></div></section>
<section style="padding-top:0"><div class="wrap"><div class="kop2"><div><p class="oog">Lees verder</p><h2>Gidsen over {e(d["naam"].lower())}.</h2></div><p class="zacht"></p></div>{artikelkaarten(d["artikelen"])}</div></section>
<section style="padding-top:0"><div class="wrap"><div class="kop2"><div><p class="oog">Meer diensten</p><h2>Ook bij ons.</h2></div><p class="zacht"></p></div><div class="artikelen vier">{andere}</div></div></section>
{band()}'''
    pagina(f'{d["slug"]}.html', f'{d["naam"]} laten maken vanaf {eur(d["vanaf"])} | Collens Group', d["lead"], body)

def prijzen():
    groepen = ""
    for d in DIENSTEN:
        groepen += f'<h2 class="groep">{e(d["naam"])}</h2><div class="regels">' + "".join(
            f'<div class="regel"><b>{e(n)}</b><span class="s">{e(" · ".join(items))}</span><span class="t">{e(t)}</span><span class="p">{"vanaf " if t not in ("per maand", "per pagina") else ""}{eur(p)}</span></div>' for n, p, t, items in d["pakketten"]) + "</div>"
    groepen += ('<h2 class="groep">Onderhoud en extra\'s</h2><div class="regels">'
                '<div class="regel"><b>Website-onderhoud</b><span class="s">Updates, back-ups, kleine wijzigingen tot 30 min per maand</span><span class="t">per maand</span><span class="p">€29</span></div>'
                '<div class="regel"><b>App- of game-onderhoud</b><span class="s">Monitoring, kritieke bugfixes, updates voor nieuwe iOS- en Android-versies</span><span class="t">per maand</span><span class="p">€85,50</span></div>'
                '<div class="regel"><b>Groei &amp; Support</b><span class="s">Alles uit Basis, tot 4 uur aanpassingen, voorrang bij storingen</span><span class="t">per maand</span><span class="p">€265,50</span></div>'
                '<div class="regel"><b>Beheer AI</b><span class="s">Monitoring en kleine aanpassingen</span><span class="t">per maand</span><span class="p">€49</span></div>'
                '<div class="regel"><b>Ontwikkeling per uur</b><span class="s">Uitbreidingen en losse opdrachten</span><span class="t">per uur</span><span class="p">€67,50</span></div></div>')
    body = f'''<div class="pkop"><div class="wrap"><div><p class="kruimel"><a href="index.html">Home</a> / Prijzen</p><h1>Alle prijzen op één plek.</h1><p>Vaste eindprijzen, geen btw erbij. Je krijgt eerst een gratis concept en daarna een vaste prijs, nooit een open rekening.</p></div>{scene("suis", [("Vaste eindprijs", "geen btw erbij", "go")], "kop", True)}</div></div>
<section><div class="wrap">{groepen}<p class="zacht" style="margin-top:40px;font-size:15px">Externe kosten, zoals een domeinnaam (meestal €10 tot €25 per jaar), platformkosten of store-accounts (Apple $99 per jaar, Google $25 eenmalig), staan vooraf in de offerte. Betalen in drie delen: 40% bij akkoord, 40% bij een goedgekeurde testversie, 20% bij oplevering.</p></div></section>{band()}'''
    pagina("prijzen.html", "Prijzen website, webshop, app, game en AI | Collens Group", "Alle prijzen van Collens Group op één plek: vaste eindprijzen, geen btw erbij.", body, "prijzen.html")

CASES = [
 {"key": "ombre", "naam": "Atelier Ombre", "soort": "Kunstwebshop", "voor": "Eigen merk", "status": "Concept", "platform": ["Website", "Webshop", "Mobiel"],
  "tekst": "Een kunstboutique met twee gezichten: een premium galerie voor abstracte schilderijen en beelden, en een betaalbare afdeling voor vondsten. Donker, rustig en volledig gericht op het werk zelf.",
  "punten": ["Galerie en betaalbare afdeling in één shop", "Kunstenaarspagina's en certificaat van echtheid", "Verlanglijst, zoeken en winkelmand", "Ontworpen voor desktop én telefoon"],
  "link": ("../atelier-ombre/", "Bekijk het concept"),
  "chips": [("Galerie", "premium collectie", "go")]},
 {"key": "suis", "naam": "Suismuis Home", "soort": "Webshop woonaccessoires", "voor": "Klant", "status": "Concept", "platform": ["Webshop", "Mobiel"],
  "tekst": "Een complete webshop voor woonaccessoires, gebouwd naar het eigen ontwerp van de klant: organic luxury, met rust, warmte en elegantie als uitgangspunt.",
  "punten": ["Producten per categorie, met filters", "Winkelmand en afrekenen", "Beheer voor producten en voorraad", "Journal en klantenservicepagina's"],
  "link": ("../suismuis/", "Bekijk het concept"),
  "chips": [("Bestelling ontvangen", "iDEAL en verzending", "gr")]},
 {"key": "lubbyc", "naam": "LubbyC", "soort": "Reisapp", "voor": "Eigen app", "status": "Binnenkort in Google Play", "platform": ["Android", "iPhone", "12 talen"],
  "tekst": "Reizigers die op dezelfde plek zijn en hetzelfde willen doen, vinden elkaar via de kaart. Je ziet wat mensen in de buurt van plan zijn en sluit aan, of maakt zelf een plan.",
  "punten": ["Plannen in de buurt op de kaart", "Groepschat zodra je bent geaccepteerd", "Feesten en evenementen in het gebied", "Noodhulp met één tik"],
  "link": (LIVE + "app-lubbyc", "Over LubbyC"),
  "chips": [("Ik ga", "aangemeld voor een plan", "gr")]},
 {"key": "koffer", "naam": "Koffer Vol!", "soort": "Puzzelgame", "voor": "Eigen game", "status": "Binnenkort in Google Play", "platform": ["Android", "iPhone", "12 talen"],
  "tekst": "Een vrolijke inpakpuzzel: pak voor elke reis precies de juiste spullen in en laat alles passen. Honderd levels, verspreid over tien landen.",
  "punten": ["100 levels in 10 landen", "Sterren, munten en een ansichtkaart per bestemming", "Uitleg bij foute keuzes", "Avatars vrijspelen in de winkel"],
  "link": (LIVE + "app-koffer-vol", "Over Koffer Vol!"),
  "chips": [("3 sterren", "level 12, Kyoto", "go")]},
 {"key": "eiland", "naam": "Eiland Express", "soort": "3D-rijgame", "voor": "Eigen game", "status": "In ontwikkeling", "platform": ["Android", "iPhone"],
  "tekst": "Rij je songthaew, de open taxi-pick-up uit Thailand, over kronkelende wegen langs het strand en door de heuvels, en breng passagiers heelhuids naar hun halte.",
  "punten": ["3D-rijden over een tropisch eiland", "Passagiers ophalen en afzetten", "Munten verdienen", "Eigen kleur voor je songthaew"],
  "link": (LIVE + "app-eiland-express", "Over Eiland Express"),
  "chips": []},
 {"key": "manu", "naam": "Manu en Khanun", "soort": "Animatieserie voor kinderen", "voor": "Eigen productie", "status": "In productie", "platform": ["Video", "Nederlands"],
  "tekst": "Manu verhuist naar een dorp tussen de rijstvelden in Noord-Thailand en ontmoet in het bamboebos Khanun, een babyolifant uit het klooster. Gemaakt met AI-beeld, -stem en -muziek.",
  "punten": ["Personages en wereld ontworpen", "AI-animatie, -stem en -muziek", "Over vriendschap en een nieuwe cultuur"],
  "link": (LIVE + "app-manu-en-khanun", "Over de serie"),
  "chips": []},
]
def case(c, i):
    tags = "".join(f"<li>{e(t)}</li>" for t in c["platform"])
    punten = "".join(f"<li>{e(x)}</li>" for x in c["punten"])
    return (f'<article class="case{" om" if i % 2 else ""}"><div class="case-t">'
            f'<dl class="meta"><div><dt>Voor</dt><dd>{e(c["voor"])}</dd></div><div><dt>Status</dt><dd>{e(c["status"])}</dd></div></dl>'
            f'<h2>{e(c["naam"])}</h2><p class="soort">{e(c["soort"])}</p><p class="ct">{e(c["tekst"])}</p>'
            f'<h3>Wat we bouwden</h3><ul class="punten">{punten}</ul><ul class="tags">{tags}</ul>'
            f'<a class="knop licht" href="{c["link"][0]}">{e(c["link"][1])}</a></div>'
            f'{scene(c["key"], c["chips"], "case-sc")}</article>')

def werkmini():
    return '<div class="werk3">' + "".join(
        f'<a class="wm" href="werk.html">{scene(c["key"], [], "klein")}<div><b>{e(c["naam"])}</b><span>{e(c["soort"])}</span></div></a>'
        for c in (CASES[0], CASES[2], CASES[3])) + "</div>"

def werk():
    inhoud = "".join(f'<li><a href="#{c["key"]}">{e(c["naam"])}</a><span>{e(c["soort"])}</span></li>' for c in CASES)
    rijen = "".join(case(c, i).replace('<article class="case', f'<article id="{c["key"]}" class="case', 1) for i, c in enumerate(CASES))
    body = f'''<div class="pkop werkkop"><div class="wrap"><div><p class="kruimel"><a href="index.html">Home</a> / Werk</p><h1>Ons werk.</h1><p>Websites, webshops, apps, games en een animatieserie. Wat we voor onszelf en onze klanten maken, met echte schermen en eerlijk over de status.</p></div>
<ol class="inhoud">{inhoud}</ol></div></div>
<section class="cases"><div class="wrap">{rijen}</div></section>{band()}'''
    pagina("werk.html", "Ons werk: websites, webshops, apps en games | Collens Group", "Projecten van Collens Group met echte schermen: Atelier Ombre, Suismuis Home, LubbyC, Koffer Vol!, Eiland Express en Manu en Khanun.", body, "werk.html")

def artikelen():
    cats = {}
    for s, (c, t, p) in ARTIKELEN.items(): cats.setdefault(c, []).append(s)
    volgorde = ["Kosten", "Keuzehulp", "Per branche", "Diensten", "Eigen werk", "English"]
    blok = "".join(f'<h2 class="groep">{e(c)}</h2>{artikelkaarten(cats[c])}' for c in volgorde if c in cats)
    body = f'''<div class="pkop"><div class="wrap"><div><p class="kruimel"><a href="index.html">Home</a> / Artikelen</p><h1>Artikelen en gidsen.</h1><p>Eerlijke antwoorden op wat ondernemers ons het vaakst vragen: wat het kost, wat je kiest en wat je vooraf afspreekt. Met bronnen.</p></div>{scene("ombre", [("Met bronnen", "kosten en keuzehulp", "go")], "kop", True)}</div></div>
<section style="padding-top:40px"><div class="wrap">{blok}</div></section>{band()}'''
    pagina("artikelen.html", "Artikelen en gidsen | Collens Group", "Gidsen over wat een website, webshop, app of chatbot kost en wat je kiest.", body, "artikelen.html")

def over():
    body = f'''<div class="pkop"><div class="wrap"><div><p class="kruimel"><a href="index.html">Home</a> / Over ons</p><h1>Je spreekt de maker.</h1><p>Collens Group is een klein, onafhankelijk digitaal bedrijf. We maken websites, webshops, apps, games en AI, persoonlijk ontworpen en met een vaste prijs.</p></div>{scene("manu", [("Eigen animatieserie", "gemaakt met AI-beeld en -stem", "go")], "kop", True)}</div></div>
<section><div class="wrap twee"><div><p class="oog">Wie zit erachter</p><h2 style="font-size:clamp(30px,3.4vw,44px)">Jeffrey Collens, oprichter.</h2></div><div class="tekst"><p>Jeffrey bouwt met moderne AI-tools en controleert elk concept, elke tekst en elke oplevering zelf voordat het naar een klant gaat. Er zit geen accountmanager tussen: je mailt rechtstreeks met de maker.</p><p>Wat we voor onszelf maken, maken we ook voor jou. Daarom bouwen we eigen apps en games, zoals LubbyC, Koffer Vol! en Eiland Express. Zo testen we elke werkwijze eerst op onszelf.</p></div></div></section>
<section class="dark"><div class="wrap twee"><div><p class="oog">Waar we werken</p><h2 style="font-size:clamp(30px,3.4vw,44px)">Overal.</h2></div><div class="tekst"><p class="zacht">Volledig online, per mail en video, met ondernemers in Nederland, België en ver daarbuiten, bijvoorbeeld in het Verenigd Koninkrijk, Ierland, de Verenigde Staten, Canada, Australië en Nieuw-Zeeland. Je werkt met ons in het Nederlands of het Engels, en de prijzen zijn overal dezelfde eindprijzen in euro.</p></div></div></section>
<section><div class="wrap"><div class="kop2"><div><p class="oog">Zo werken we</p><h2>Onze afspraken met jou.</h2></div><p class="zacht"></p></div>
<div class="regels"><div class="regel"><b>Vaste prijs vooraf</b><span class="s">Je weet wat je betaalt voordat we beginnen. Meerwerk alleen na jouw akkoord.</span><span class="t"></span><span class="p"></span></div>
<div class="regel"><b>Eerst een gratis concept</b><span class="s">Binnen 48 uur zie je hoe het eruit kan zien, ontworpen voor jouw bedrijf, zonder verplichtingen.</span><span class="t"></span><span class="p"></span></div>
<div class="regel"><b>Eindprijzen</b><span class="s">Er komt geen btw bij.</span><span class="t"></span><span class="p"></span></div>
<div class="regel"><b>Jij bent eigenaar</b><span class="s">Site, domein en inhoud op jouw naam; apps in je eigen Apple- en Google-account; broncode na de laatste betaling van jou.</span><span class="t"></span><span class="p"></span></div>
<div class="regel"><b>Eerlijk over wat we niet doen</b><span class="s">Geen grote 3D-games of online multiplayer, en we werken niet op locatie.</span><span class="t"></span><span class="p"></span></div></div></div></section>{band()}'''
    pagina("over-ons.html", "Over Collens Group | Collens Group", "Collens Group: opgericht door Jeffrey Collens, online en wereldwijd, vaste prijzen.", body, "over-ons.html")

def contact():
    body = f'''<div class="pkop"><div class="wrap"><div><p class="kruimel"><a href="index.html">Home</a> / Contact</p><h1>Vraag je gratis concept aan.</h1><p>Vertel in een paar zinnen wie je bent en wat je wilt bereiken. Binnen 48 uur krijg je een reactie, en daarna een concept dat alleen bij jou past.</p></div>{scene("ombre", [("Concept klaar", "binnen 48 uur", "go")], "kop", True)}</div></div>
<section><div class="wrap">{FORM}
<div class="twee" style="margin-top:96px"><div><p class="oog">Liever mailen?</p><h2 style="font-size:clamp(28px,3vw,40px)">info@collensgroup.com</h2><p class="zacht" style="margin-top:16px">Je krijgt binnen 48 uur antwoord, in het Nederlands of het Engels.</p></div>
<div>{faq([("Wat kost een concept?", "Niets. Het concept is gratis en zonder verplichtingen."), ("Hoe snel kunnen jullie beginnen?", "Na je akkoord op het concept en de vaste prijs, meestal direct."), ("Werken jullie ook voor bedrijven buiten Nederland?", "Ja. We werken volledig online met ondernemers wereldwijd, in het Nederlands of het Engels."), ("Hoe betaal ik?", "In drie delen: 40% bij akkoord, 40% bij een goedgekeurde testversie en 20% bij oplevering.")])}</div></div></div></section>'''
    pagina("contact.html", "Contact en gratis concept | Collens Group", "Vraag je gratis concept aan. Reactie binnen 48 uur.", body, "contact.html")

if __name__ == "__main__":
    os.makedirs(UIT, exist_ok=True)
    home(); prijzen(); werk(); artikelen(); over(); contact()
    for d in DIENSTEN: dienst(d)
    print("klaar:", sorted(f for f in os.listdir(UIT)))
