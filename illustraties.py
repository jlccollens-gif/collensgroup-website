"""Illustraties per dienst voor de kop van binnenpagina's.

Alles is inline SVG of echte schermen van eigen werk; geen stockbeelden.
"""
import re, os

N, G, B, T, L, Z = "#14213D", "#F2B705", "#2457D6", "#0E7C86", "#F3F6FA", "#C9D3E1"

TXT = {
    "nl": {"scherm": "Werkt op elk scherm", "url": "jouwbedrijf.nl", "kassa": "Afrekenen", "ideal": "Betaal met iDEAL",
           "vraag": "Wat kost een website?", "antw": "Een one-page website begint bij €495.", "chat": "Stel je vraag",
           "flow": ["Formulier", "Mail", "Agenda"], "uit": ["CRM", "Offerte", "Planning"], "ai": "AI",
           "alt_web": "Voorbeeld van een website op laptop en telefoon", "alt_shop": "Voorbeeld van een webshop met afrekenscherm",
           "alt_ai": "Schema: aanvragen gaan automatisch via AI naar CRM, offerte en planning", "alt_chat": "Voorbeeld van een AI-chatbot op een website",
           "alt_app1": "Ontdekscherm van onze reisapp LubbyC", "alt_app2": "Kaartscherm van onze reisapp LubbyC",
           "alt_g1": "Onze puzzelgame Koffer Vol!", "alt_g2": "Onze rijgame Eiland Express", "bijschrift_app": "Echte schermen van onze eigen app LubbyC",
           "bijschrift_game": "Echte schermen van onze eigen games"},
    "en": {"scherm": "Works on every screen", "url": "yourbusiness.com", "kassa": "Checkout", "ideal": "Pay now",
           "vraag": "How much is a website?", "antw": "A one-page website starts at €495.", "chat": "Ask a question",
           "flow": ["Form", "Email", "Calendar"], "uit": ["CRM", "Quote", "Planning"], "ai": "AI",
           "alt_web": "Example of a website on laptop and phone", "alt_shop": "Example of an online shop with checkout",
           "alt_ai": "Diagram: requests flow automatically through AI to CRM, quote and planning", "alt_chat": "Example of an AI chatbot on a website",
           "alt_app1": "Discover screen of our travel app LubbyC", "alt_app2": "Map screen of our travel app LubbyC",
           "alt_g1": "Our puzzle game Koffer Vol!", "alt_g2": "Our driving game Island Express", "bijschrift_app": "Real screens from our own app LubbyC",
           "bijschrift_game": "Real screens from our own games"},
}

SCHADUW = '<defs><filter id="sch" x="-20%" y="-20%" width="140%" height="170%"><feDropShadow dx="0" dy="16" stdDeviation="16" flood-color="#0E1830" flood-opacity=".16"/></filter></defs>'


def _browser(t, inhoud):
    return f'''<g filter="url(#sch)"><rect x="10" y="22" width="372" height="272" rx="16" fill="#fff"/></g>
<path d="M10 38a16 16 0 0 1 16-16h340a16 16 0 0 1 16 16v20H10z" fill="{L}"/>
<circle cx="32" cy="40" r="4.5" fill="{Z}"/><circle cx="47" cy="40" r="4.5" fill="{Z}"/><circle cx="62" cy="40" r="4.5" fill="{Z}"/>
<rect x="92" y="30" width="196" height="20" rx="10" fill="#fff" stroke="#E1E7F0"/>
<path d="M104 42v-3a3 3 0 0 1 6 0v3" fill="none" stroke="#5A6782" stroke-width="1.4"/><rect x="102.5" y="41" width="9" height="6.5" rx="1.5" fill="#5A6782"/>
<text x="118" y="44.5" font-size="11" fill="#5A6782" font-family="Inter,system-ui,sans-serif">{t["url"]}</text>
<rect x="30" y="72" width="18" height="18" rx="5" fill="{B}"/><rect x="56" y="77.5" width="62" height="7" rx="3.5" fill="{N}"/>
<rect x="206" y="78.5" width="24" height="5" rx="2.5" fill="{Z}"/><rect x="238" y="78.5" width="24" height="5" rx="2.5" fill="{Z}"/><rect x="270" y="78.5" width="24" height="5" rx="2.5" fill="{Z}"/>
<rect x="306" y="72" width="56" height="18" rx="9" fill="{N}"/>{inhoud}'''


def _telefoon(inhoud):
    return f'''<g filter="url(#sch)"><rect x="328" y="104" width="122" height="228" rx="24" fill="#0E1830"/></g>
<rect x="335" y="111" width="108" height="214" rx="18" fill="#fff"/><rect x="371" y="116" width="36" height="7" rx="3.5" fill="#0E1830"/>{inhoud}'''


def _pil(t, x=26, y=300):
    return f'''<g filter="url(#sch)"><rect x="{x}" y="{y}" width="168" height="34" rx="17" fill="#fff"/></g>
<circle cx="{x+18}" cy="{y+17}" r="9" fill="#1E9E6A"/><path d="M{x+13.5} {y+17.5}l3 3 5.5-6" fill="none" stroke="#fff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
<text x="{x+34}" y="{y+21.5}" font-size="12.5" font-weight="700" fill="{N}" font-family="Inter,system-ui,sans-serif">{t["scherm"]}</text>'''


def svg_web(t):
    held = f'''<rect x="30" y="104" width="332" height="98" rx="12" fill="{N}"/>
<rect x="50" y="124" width="160" height="12" rx="4" fill="#fff"/><rect x="50" y="142" width="116" height="12" rx="4" fill="#fff"/>
<rect x="50" y="164" width="136" height="6" rx="3" fill="#8FA0BF"/><rect x="50" y="178" width="66" height="14" rx="7" fill="{G}"/>
<rect x="238" y="118" width="106" height="70" rx="10" fill="{B}"/><circle cx="318" cy="136" r="8" fill="{G}"/>
<path d="M238 176l26-26 20 18 14-12 46 32v2a10 10 0 0 1-10 10h-86a10 10 0 0 1-10-10z" fill="#5B83E8"/>
<rect x="30" y="216" width="102" height="60" rx="10" fill="{L}"/><rect x="145" y="216" width="102" height="60" rx="10" fill="{L}"/><rect x="260" y="216" width="102" height="60" rx="10" fill="{L}"/>
<circle cx="48" cy="234" r="8" fill="{B}"/><circle cx="163" cy="234" r="8" fill="{G}"/><circle cx="278" cy="234" r="8" fill="{T}"/>
<rect x="40" y="250" width="70" height="6" rx="3" fill="{Z}"/><rect x="40" y="262" width="50" height="6" rx="3" fill="{Z}"/>
<rect x="155" y="250" width="70" height="6" rx="3" fill="{Z}"/><rect x="155" y="262" width="50" height="6" rx="3" fill="{Z}"/>
<rect x="270" y="250" width="54" height="6" rx="3" fill="{Z}"/><rect x="270" y="262" width="40" height="6" rx="3" fill="{Z}"/>'''
    tel = f'''<rect x="344" y="134" width="90" height="74" rx="9" fill="{N}"/><rect x="353" y="148" width="58" height="8" rx="3" fill="#fff"/>
<rect x="353" y="161" width="42" height="8" rx="3" fill="#fff"/><rect x="353" y="184" width="38" height="12" rx="6" fill="{G}"/>
<rect x="344" y="218" width="90" height="28" rx="7" fill="{L}"/><rect x="344" y="252" width="90" height="28" rx="7" fill="{L}"/><rect x="344" y="286" width="90" height="28" rx="7" fill="{L}"/>
<circle cx="357" cy="232" r="6" fill="{B}"/><circle cx="357" cy="266" r="6" fill="{G}"/><circle cx="357" cy="300" r="6" fill="{T}"/>'''
    return _browser(t, held) + _telefoon(tel) + _pil(t)


def svg_shop(t):
    kleuren = [B, G, T, "#E4572E", N, "#7A3BD1"]
    prod = ""
    for i in range(6):
        x, y = 30 + (i % 3) * 112, 104 + (i // 3) * 90
        prod += (f'<rect x="{x}" y="{y}" width="102" height="80" rx="10" fill="{L}"/>'
                 f'<rect x="{x+10}" y="{y+8}" width="82" height="40" rx="7" fill="{kleuren[i]}" opacity=".9"/>'
                 f'<rect x="{x+10}" y="{y+56}" width="50" height="6" rx="3" fill="{Z}"/><rect x="{x+10}" y="{y+67}" width="30" height="6" rx="3" fill="{N}"/>')
    tel = f'''<text x="346" y="146" font-size="12" font-weight="800" fill="{N}" font-family="Inter,system-ui,sans-serif">{t["kassa"]}</text>
<rect x="344" y="156" width="90" height="34" rx="7" fill="{L}"/><rect x="350" y="162" width="22" height="22" rx="5" fill="{B}"/><rect x="378" y="166" width="46" height="5" rx="2.5" fill="{Z}"/><rect x="378" y="176" width="28" height="5" rx="2.5" fill="{N}"/>
<rect x="344" y="196" width="90" height="34" rx="7" fill="{L}"/><rect x="350" y="202" width="22" height="22" rx="5" fill="{G}"/><rect x="378" y="206" width="46" height="5" rx="2.5" fill="{Z}"/><rect x="378" y="216" width="28" height="5" rx="2.5" fill="{N}"/>
<line x1="344" y1="244" x2="434" y2="244" stroke="#E1E7F0"/><rect x="344" y="254" width="40" height="7" rx="3.5" fill="{Z}"/><rect x="404" y="254" width="30" height="7" rx="3.5" fill="{N}"/>
<rect x="344" y="282" width="90" height="26" rx="13" fill="#CC0066"/><text x="389" y="299" text-anchor="middle" font-size="10.5" font-weight="700" fill="#fff" font-family="Inter,system-ui,sans-serif">{t["ideal"]}</text>'''
    return _browser(t, prod) + _telefoon(tel) + _pil(t)


def svg_ai(t):
    links = "".join(
        f'''<g filter="url(#sch)"><rect x="14" y="{40+i*96}" width="118" height="56" rx="14" fill="#fff"/></g>
<rect x="28" y="{54+i*96}" width="28" height="28" rx="8" fill="{c}"/><text x="66" y="{73+i*96}" font-size="13.5" font-weight="700" fill="{N}" font-family="Inter,system-ui,sans-serif">{n}</text>'''
        for i, (n, c) in enumerate(zip(t["flow"], [B, G, T])))
    rechts = "".join(
        f'''<g filter="url(#sch)"><rect x="318" y="{40+i*96}" width="128" height="56" rx="14" fill="#fff"/></g>
<circle cx="342" cy="{68+i*96}" r="11" fill="#1E9E6A"/><path d="M337 {68.5+i*96}l3.5 3.5 6-6.5" fill="none" stroke="#fff" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/>
<text x="362" y="{73+i*96}" font-size="13.5" font-weight="700" fill="{N}" font-family="Inter,system-ui,sans-serif">{n}</text>'''
        for i, n in enumerate(t["uit"]))
    lijnen = "".join(f'<path class="stroom" d="M132 {68+i*96}C185 {68+i*96} 180 166 202 166" fill="none" stroke="{Z}" stroke-width="2.5"/>' for i in range(3))
    lijnen += "".join(f'<path class="stroom" d="M258 166C280 166 275 {68+i*96} 318 {68+i*96}" fill="none" stroke="{G}" stroke-width="2.5"/>' for i in range(3))
    kern = f'''<g filter="url(#sch)"><circle cx="230" cy="166" r="42" fill="{N}"/></g>
<path d="M230 140l5.5 14 14 4.5-14 4.8L230 178l-5.5-14.7-14-4.8 14-4.5z" fill="{G}"/><path d="M246 170l2.4 5.6 5.6 2.4-5.6 2.4-2.4 5.6-2.4-5.6-5.6-2.4 5.6-2.4z" fill="#fff"/>'''
    return lijnen + links + rechts + kern


def svg_chat(t):
    held = f'''<rect x="30" y="104" width="200" height="12" rx="4" fill="{N}"/><rect x="30" y="122" width="150" height="12" rx="4" fill="{N}"/>
<rect x="30" y="146" width="180" height="6" rx="3" fill="{Z}"/><rect x="30" y="158" width="160" height="6" rx="3" fill="{Z}"/><rect x="30" y="170" width="120" height="6" rx="3" fill="{Z}"/>
<rect x="30" y="190" width="72" height="16" rx="8" fill="{G}"/>
<rect x="30" y="222" width="160" height="56" rx="10" fill="{L}"/>'''
    venster = f'''<g filter="url(#sch)"><rect x="214" y="96" width="232" height="232" rx="18" fill="#fff"/></g>
<path d="M214 114a18 18 0 0 1 18-18h196a18 18 0 0 1 18 18v26H214z" fill="{N}"/>
<circle cx="238" cy="118" r="10" fill="{G}"/><path d="M238 112l1.8 4.4 4.4 1.6-4.4 1.6-1.8 4.4-1.8-4.4-4.4-1.6 4.4-1.6z" fill="{N}"/>
<rect x="256" y="113" width="70" height="9" rx="4.5" fill="#fff" opacity=".9"/>
<rect x="292" y="154" width="140" height="30" rx="12" fill="{B}"/><text x="362" y="173.5" text-anchor="middle" font-size="11" fill="#fff" font-family="Inter,system-ui,sans-serif">{t["vraag"]}</text>
<rect x="228" y="194" width="196" height="30" rx="12" fill="{L}"/><text x="238" y="213.5" font-size="11" fill="{N}" font-family="Inter,system-ui,sans-serif">{t["antw"]}</text>
<rect x="228" y="234" width="58" height="22" rx="11" fill="#fff" stroke="{Z}"/><circle cx="246" cy="245" r="2.5" fill="#8FA0BF"/><circle cx="257" cy="245" r="2.5" fill="#8FA0BF"/><circle cx="268" cy="245" r="2.5" fill="#8FA0BF"/>
<rect x="228" y="288" width="204" height="28" rx="14" fill="{L}"/><text x="244" y="306" font-size="11" fill="#5A6782" font-family="Inter,system-ui,sans-serif">{t["chat"]}</text>
<circle cx="418" cy="302" r="10" fill="{G}"/><path d="M414 302h8m-3-3.5l3.5 3.5-3.5 3.5" fill="none" stroke="{N}" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/>'''
    return _browser(t, held) + venster


def tels(beelden, bijschrift):
    a, b = beelden
    return (f'<div class="illu-tels"><figure class="a"><img src="{a[0]}" alt="{a[1]}" width="240" height="480"></figure>'
            f'<figure class="b"><img src="{b[0]}" alt="{b[1]}" width="240" height="480"></figure></div>'
            f'<figcaption>{bijschrift}</figcaption>')


ECHT = {  # echte schermen van eigen ontwerpwerk: (laptop, telefoon, alt)
    ("web", "nl"): ("img/toon-suismuis-lap.jpg", "img/toon-suismuis-tel.jpg", "Webshop-ontwerp van Collens Group voor Suismuis Home op laptop en telefoon"),
    ("web", "en"): ("img/toon-suismuis-lap.jpg", "img/toon-suismuis-tel.jpg", "Web shop design by Collens Group for Suismuis Home on laptop and phone"),
    ("chat", "nl"): ("img/voorbeeld-chat.jpg", "img/voorbeeld-chat-m.jpg", "Jeff, de AI-adviseur van Collens Group, op laptop en telefoon"),
    ("shop", "nl"): ("img/voorbeeld-webshop.jpg", "img/toon-suismuis-tel.jpg", "Webshop-ontwerp van Collens Group voor Suismuis Home op laptop en telefoon"),
}


def echt(soort, lang):
    a, b, alt = ECHT[(soort, lang)]
    return (f'<div class="illu-scherm"><div class="lap"><div class="balk"><i></i><i></i><i></i></div><img src="{a}" alt="{alt}" width="640" height="400" loading="eager"></div>'
            f'<div class="tel"><img src="{b}" alt="" width="120" height="213" loading="eager"></div></div>')


def illustratie(soort, lang):
    if (soort, "en" if lang == "en" else "nl") in ECHT:
        return echt(soort, "en" if lang == "en" else "nl")
    t = TXT["en" if lang == "en" else "nl"]
    if soort == "app":
        return tels([("img/lubbyc-ontdekken.jpg", t["alt_app1"]), ("img/lubbyc-kaart.jpg", t["alt_app2"])], t["bijschrift_app"])
    if soort == "game":
        return tels([("img/koffer-spel.jpg", t["alt_g1"]), ("img/eiland-rood.jpg", t["alt_g2"])], t["bijschrift_game"])
    teken = {"web": svg_web, "shop": svg_shop, "ai": svg_ai, "chat": svg_chat}[soort]
    return f'<svg viewBox="0 0 460 346" role="img" aria-label="{t["alt_" + soort]}">{SCHADUW}{teken(t)}</svg>'


KAART = {
    "website-laten-maken": ("web", "nl"), "goedkope-website-laten-maken": ("web", "nl"), "en-website-design": ("web", "en"),
    "webshop-laten-maken": ("shop", "nl"),
    "game-laten-maken": ("game", "nl"),
    "ai-automatisering": ("ai", "nl"), "chatbot-laten-maken": ("chat", "nl"),
    "app-laten-maken-kosten": ("app", "nl"), "mvp-app-laten-maken": ("app", "nl"), "en-app-development": ("app", "en"),
    **{f"website-laten-maken-{b}": ("web", "nl") for b in ("kapper", "horeca", "schoonheidssalon", "fotograaf", "aannemer", "coach-zzp", "vakantiehuis", "belgie", "afspraken")},
    "wat-kost-een-website": ("web", "nl"), "zelf-website-bouwen-of-laten-maken": ("web", "nl"), "wat-kost-een-webshop": ("shop", "nl"),
    "app-laten-maken-horeca": ("app", "nl"), "app-of-website": ("app", "nl"), "merkgame-laten-maken-kerst": ("game", "nl"),
}

PATROON = re.compile(r'(<h1>.*?</h1>)\s*(<p class="lead2">.*?</p>)', re.S)


def verrijk(dist):
    """Zet de illustratie naast de kop van elke dienstpagina."""
    for slug, (soort, lang) in KAART.items():
        pad = os.path.join(dist, slug + ".html")
        if not os.path.exists(pad):
            continue
        html = open(pad, encoding="utf-8").read()
        if 'class="kopblok"' in html:
            continue
        nieuw, n = PATROON.subn(lambda m: f'<div class="kopblok soort-{soort}"><div class="kop-tekst">{m.group(1)}{m.group(2)}</div>'
                                f'<figure class="illu">{illustratie(soort, lang)}</figure></div>', html, count=1)
        if n:
            open(pad, "w", encoding="utf-8").write(nieuw)
