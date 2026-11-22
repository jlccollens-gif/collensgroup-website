"""Grafieken en beeld op de binnenpagina's.

Alle bedragen komen uit bronnen die al op de pagina staan (zelfde bron, zelfde cijfers).
Rijtypen: ("bereik", label, laag, hoog) | ("vanaf", label, laag) open naar rechts | ("punt", label, waarde)
"""
import os
import re


def eur(n):
    return "€" + f"{n:,}".replace(",", ".")


def _bar(rij, maxi):
    soort = rij[0]
    if soort == "bereik":
        _, label, lo, hi = rij
        stijl, waarde, cls = f"left:{lo / maxi * 100:.1f}%;width:{(hi - lo) / maxi * 100:.1f}%", f"{eur(lo)} – {eur(hi)}", "g-bar"
    elif soort == "vanaf":
        _, label, lo = rij
        stijl, waarde, cls = f"left:{lo / maxi * 100:.1f}%;right:0", f"vanaf {eur(lo)}", "g-bar g-open"
    else:
        _, label, v = rij
        stijl, waarde, cls = f"left:0;width:{v / maxi * 100:.1f}%", eur(v), "g-bar"
    return label, stijl, waarde, cls


def prijsgrafiek(titel, markt, ons, maxi, bron_tekst, bron_url):
    stappen = next((s for s in (5, 4, 3, 6) if maxi % s == 0 and (maxi // s) % 500 == 0), 4)
    ticks = "".join(f'<span style="left:{i / stappen * 100:.0f}%">{eur(round(maxi * i / stappen))}</span>' for i in range(stappen + 1))
    rijen = ""
    for groep, cls_rij in ((markt, ""), (ons, " ons")):
        for rij in groep:
            label, stijl, waarde, cls = _bar(rij, maxi)
            rijen += (f'<div class="g-rij{cls_rij}"><span class="g-label">{label}</span>'
                      f'<span class="g-baan"><span class="{cls}" style="{stijl}"></span></span>'
                      f'<span class="g-waarde">{waarde}</span></div>')
    return (f'<figure class="grafiek"><figcaption class="g-titel">{titel}</figcaption>{rijen}'
            f'<div class="g-as" aria-hidden="true">{ticks}</div>'
            f'<p class="g-bron">Bron marktprijzen: <a href="{bron_url}" rel="nofollow noopener">{bron_tekst}</a>. '
            f'Onze prijzen zijn eindprijzen: er komt geen btw bij.</p></figure>')


def tijdgrafiek(titel, rijen, maxi, eenheid="weken", noot=""):
    """rijen: (label, laag, hoog, tekst, ons:bool) in weken."""
    ticks = "".join(f'<span style="left:{w / maxi * 100:.0f}%">{w}</span>' for w in range(0, maxi + 1, 4 if maxi > 12 else 2))
    html = ""
    for label, lo, hi, tekst, ons in rijen:
        html += (f'<div class="g-rij{" ons" if ons else ""}"><span class="g-label">{label}</span>'
                 f'<span class="g-baan"><span class="g-bar" style="left:{lo / maxi * 100:.1f}%;width:{max(hi - lo, .35) / maxi * 100:.1f}%"></span></span>'
                 f'<span class="g-waarde">{tekst}</span></div>')
    return (f'<figure class="grafiek tijd"><figcaption class="g-titel">{titel}</figcaption>{html}'
            f'<div class="g-as" aria-hidden="true">{ticks}</div><p class="g-bron">Doorlooptijd in {eenheid}. {noot}</p></figure>')


def galerij(beelden):
    return '<div class="galerij tel">' + "".join(
        f'<figure><img src="{src}" alt="{alt}" loading="lazy" width="240" height="480"><figcaption>{alt}</figcaption></figure>'
        for src, alt in beelden) + '</div>'


SL_APP = ("Searchlab, Wat kost een app laten maken (2026)", "https://searchlab.nl/kosten/wat-kost-een-app-laten-maken")
SL_AI = ("Searchlab, Wat kost een AI-agent laten bouwen (2026)", "https://searchlab.nl/kosten/wat-kost-een-ai-agent-laten-bouwen")

APP_PRIJS = prijsgrafiek("Wat kost een eenvoudige app?",
                         [("bereik", "Freelancer of bureau", 5000, 25000)],
                         [("punt", "Collens Group Basis", 3150), ("punt", "Collens Group Standaard", 6750)], 25000, *SL_APP)
APP_TIJD = tijdgrafiek("Hoe snel is je app klaar?",
                       [("Markt, eenvoudige app", 8.7, 13, "2–3 maanden", False),
                        ("Collens Group Basis", 3, 5, "3–5 weken", True),
                        ("Collens Group Standaard", 6, 10, "6–10 weken", True)], 16,
                       noot="Marktcijfer: Searchlab (2026).")

GAME_BEELD = galerij([("img/koffer-spel.jpg", "Koffer Vol!: inpakken"), ("img/koffer-gewonnen.jpg", "Koffer Vol!: gewonnen"),
                      ("img/eiland-rood.jpg", "Eiland Express: rijden"), ("img/eiland-menu.jpg", "Eiland Express: menu")])
APP_BEELD = galerij([("img/lubbyc-ontdekken.jpg", "LubbyC: ontdekken"), ("img/lubbyc-kaart.jpg", "LubbyC: kaart"),
                     ("img/lubbyc-evenementen.jpg", "LubbyC: evenementen"), ("img/lubbyc-noodhulp.jpg", "LubbyC: hulp")])

# slug -> lijst van (regex van de kop waarna ingevoegd wordt, html, "na_p" = na eerste alinea | "voor" = vóór de kop)
PLAN = {
    "website-laten-maken": [
        (r"Vergeleken met de markt", "na_p", prijsgrafiek("Website: wat je betaalt",
            [("bereik", "Geavanceerde website", 2000, 5000), ("bereik", "Eenvoudige website", 500, 2000)],
            [("punt", "Collens Group one-page", 495), ("punt", "Collens Group bedrijfssite", 995)], 5000,
            "Trustoo, Wat kost een website laten maken? (aangepast 03-11-2026)", "https://trustoo.nl/kosten/webdesign-kosten/")),
        (r"Extra", "voor", tijdgrafiek("Hoe snel ben je live?",
            [("One-page", .6, 1, "3–5 dagen", True), ("Bedrijfswebsite", 2, 3, "2–3 weken", True), ("Webshop", 3, 5, "3–5 weken", True)], 6)),
    ],
    "webshop-laten-maken": [
        (r"Wat zit erin\?", "voor", prijsgrafiek("Webshop: wat je betaalt",
            [("bereik", "Bureau (mkb)", 5000, 15000), ("bereik", "Freelancer", 2000, 8000)],
            [("punt", "Collens Group", 1950)], 15000, "Searchlab (2026)", "https://searchlab.nl/kosten/wat-kost-een-webshop-laten-maken")),
    ],
    "game-laten-maken": [
        (r"Vergeleken met de markt", "na_p", prijsgrafiek("Mobiele game: wat je betaalt",
            [("vanaf", "Markt, eenvoudige game", 10000)],
            [("punt", "Collens Group casual game", 4950), ("punt", "Collens Group 2D met levels", 9950)], 16000,
            "Juego Studios, Cost of Game Development in the Netherlands (2026)", "https://www.juegostudio.com/blog/cost-of-game-development-netherlands")),
        (r"Extra", "voor", tijdgrafiek("Hoe snel is je game klaar?",
            [("Merkgame", 2, 3, "2–3 weken", True), ("Casual game", 4, 6, "4–6 weken", True), ("2D-game met levels", 8, 12, "8–12 weken", True)], 12)
            + '<h2>Zo zien onze eigen games eruit</h2>' + GAME_BEELD),
    ],
    "ai-automatisering": [
        (r"Vergeleken met de markt", "na_p", prijsgrafiek("AI-oplossing: wat je betaalt",
            [("bereik", "AI-agent (markt)", 2000, 8000)],
            [("punt", "Collens Group automatisering", 395), ("punt", "Collens Group AI-chatbot", 995), ("punt", "Collens Group AI-assistent", 1950)], 8000, *SL_AI)),
        (r"Extra", "voor", tijdgrafiek("Hoe snel werkt het?",
            [("Automatisering", .4, 1, "2–5 dagen", True), ("AI-chatbot", .8, 1.2, "1 week", True), ("AI-assistent", 2, 4, "2–4 weken", True)], 4)),
    ],
    "chatbot-laten-maken": [
        (r"Voor wie is het handig\?", "voor", prijsgrafiek("AI-chatbot: wat je betaalt",
            [("bereik", "AI-agent (markt)", 2000, 8000)], [("punt", "Collens Group AI-chatbot", 995)], 8000, *SL_AI)),
    ],
    "app-laten-maken-kosten": [
        (r"Marktprijzen in Nederland", "na_tabel", APP_PRIJS + APP_TIJD),
        (r"Veelgestelde vragen over app-kosten", "voor", '<h2>Zo ziet een app van ons eruit</h2>' + APP_BEELD),
    ],
    "mvp-app-laten-maken": [
        (r"Wat zit er in ons Basis / MVP-pakket\?", "voor", '<h2>Prijs en tijd vergeleken</h2>' + APP_PRIJS + APP_TIJD),
    ],
}


def verrijk_grafieken(dist):
    for slug, stappen in PLAN.items():
        pad = os.path.join(dist, slug + ".html")
        if not os.path.exists(pad):
            continue
        html = open(pad, encoding="utf-8").read()
        if 'class="grafiek' in html:
            continue
        for kop, waar, blok in stappen:
            m = re.search(r'<h2[^>]*>' + kop + r'</h2>', html)
            if not m:
                print("grafieken: kop niet gevonden", slug, kop)
                continue
            if waar == "voor":
                pos = m.start()
            elif waar == "na_tabel":
                t = html.find("</table>", m.end())
                b = html.find("</p>", t)  # bronregel onder de tabel
                pos = b + 4
            else:
                pos = html.find("</p>", m.end()) + 4
            html = html[:pos] + blok + html[pos:]
        open(pad, "w", encoding="utf-8").write(html)
