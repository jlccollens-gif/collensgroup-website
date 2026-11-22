"""Bouwt de concept-webshop Suismuis Home in src/concept/suismuis/ (alle pagina's delen kop, voet en watermerk)."""
import os

# Winkelgegevens (wettelijk verplicht op een webshop). ADRES invullen door Kim voor de livegang.
WINKEL = {"naam": "Suismuis Home", "eigenaar": "Kim Suister", "adres": "", "email": "suisterkim@gmail.com"}
ADRES = WINKEL["adres"] or "[adres volgt]"
WINKEL_TXT = f'{WINKEL["naam"]} ({WINKEL["eigenaar"]}), {ADRES}, {WINKEL["email"]}'
VOORWAARDEN = f'''<p class="noot">Versie 1, november 2026.</p>
<h3>1. Wie zijn wij</h3><p>Suismuis Home is een webshop van {WINKEL["eigenaar"]}, {ADRES}. E-mail: <a class="link" href="mailto:{WINKEL["email"]}">{WINKEL["email"]}</a>. Deze voorwaarden gelden voor elke bestelling via deze webshop.</p>
<h3>2. Aanbod en prijzen</h3><p>We beschrijven elk product zo nauwkeurig mogelijk, met foto's, materialen en maten. Kleine verschillen in kleur en structuur zijn bij natuurlijke en handgemaakte materialen mogelijk. Alle prijzen zijn eindprijzen in euro; verzendkosten zie je vóór het afrekenen. Kennelijke vergissingen in prijzen of beschrijvingen binden ons niet.</p>
<h3>3. De overeenkomst</h3><p>De overeenkomst komt tot stand zodra je betaling is gelukt. Je ontvangt direct een bevestiging per e-mail met je ordernummer. Kunnen we een product toch niet leveren, dan laten we dat zo snel mogelijk weten en betalen we het volledige bedrag binnen 14 dagen terug.</p>
<h3>4. Betalen</h3><p>Je betaalt vooraf met je creditcard (Visa, Mastercard of American Express) via een beveiligde betaalverwerker met 3D Secure. Wij zien en bewaren je kaartgegevens nooit.</p>
<h3>5. Levering</h3><p>We leveren in Nederland en België, meestal binnen 8 tot 15 werkdagen. Zodra je pakket onderweg is, krijg je een track-and-tracecode. Is je bestelling na 30 dagen nog niet geleverd, dan mag je de overeenkomst kosteloos ontbinden en betalen we je binnen 14 dagen terug. Het risico van verlies of beschadiging gaat pas op jou over als je het pakket hebt ontvangen.</p>
<h3>6. Herroepingsrecht (14 dagen bedenktijd)</h3><p>Je mag je aankoop binnen 14 dagen na ontvangst zonder opgaaf van reden herroepen, met de knop <a class="link" href="#herroepen">Bestelling herroepen</a>, met het modelformulier of per e-mail. Daarna heb je opnieuw 14 dagen om het product terug te sturen. Ga zorgvuldig met het product om; je mag het alleen bekijken zoals je dat in een winkel zou doen. De kosten van het terugsturen zijn voor jou. We betalen het aankoopbedrag inclusief de standaard verzendkosten binnen 14 dagen na je herroeping terug, op dezelfde manier als je hebt betaald; we mogen wachten tot we het product terug hebben of je verzendbewijs hebben gezien. Is het product door jouw toedoen beschadigd of gebruikt, dan kunnen we de waardevermindering verrekenen.</p>
<h3>7. Garantie en klachten</h3><p>Je hebt altijd recht op een product dat doet wat je ervan mag verwachten (wettelijke garantie). Is er iets mis, mail ons dan binnen twee maanden nadat je het gebrek hebt ontdekt, het liefst met een foto. We reageren binnen één werkdag en zoeken samen naar een oplossing: herstel, vervanging of terugbetaling.</p>
<h3>8. Privacy</h3><p>We gebruiken je gegevens alleen zoals beschreven in onze <a class="link" href="#privacy">privacyverklaring</a>.</p>
<h3>9. Geschillen</h3><p>Op deze voorwaarden is Nederlands recht van toepassing. Kom je er met ons niet uit, dan kun je je wenden tot de bevoegde rechter. Als consument behoud je de bescherming van de dwingende regels van het land waar je woont.</p>'''
PRIVACY = f'''<p class="noot">Versie 1, november 2026.</p>
<p>{WINKEL["eigenaar"]} (Suismuis Home, {ADRES}) is verantwoordelijk voor je gegevens. Vragen of een verzoek? Mail naar <a class="link" href="mailto:{WINKEL["email"]}">{WINKEL["email"]}</a>.</p>
<h3>Welke gegevens en waarom</h3><ul><li><b>Bestellen:</b> naam, adres, e-mailadres, eventueel telefoonnummer en wat je bestelt, om je bestelling te leveren en je op de hoogte te houden (uitvoering van de overeenkomst).</li><li><b>Betalen:</b> de betaalverwerker verwerkt je kaartgegevens; wij ontvangen alleen of de betaling is gelukt.</li><li><b>Contact en herroeping:</b> wat je ons stuurt, om je vraag te beantwoorden.</li><li><b>Nieuwsbrief:</b> alleen je e-mailadres en alleen als je je aanmeldt (toestemming). Afmelden kan altijd.</li></ul>
<h3>Wie helpt ons daarbij</h3><p>We werken met zorgvuldig gekozen dienstverleners die je gegevens alleen voor ons verwerken: hosting van de website (Cloudflare), opslag van bestellingen (Supabase), betaalverwerking (PayPal, ook voor creditcards), het versturen van e-mails (Brevo) en de leverancier en vervoerder die je bestelling bezorgen. Een deel van deze partijen zit buiten de EU; zij werken dan met de standaardcontractbepalingen van de Europese Commissie.</p>
<h3>Hoe lang</h3><p>Bestelgegevens bewaren we 7 jaar, omdat de belastingwet dat verplicht. Berichten bewaren we tot een jaar nadat je vraag is afgehandeld. Je nieuwsbriefaanmelding tot je je afmeldt.</p>
<h3>Je rechten</h3><p>Je mag je gegevens inzien, laten corrigeren of laten verwijderen, bezwaar maken en je toestemming intrekken. Mail ons; we reageren binnen een maand. Ben je het niet met ons eens, dan kun je een klacht indienen bij de Autoriteit Persoonsgegevens.</p>
<h3>Cookies</h3><p>We gebruiken geen tracking- of advertentiecookies. Je winkelmand en favorieten bewaren we alleen in je eigen browser.</p>'''
DOEL = os.path.join(os.path.dirname(__file__), "..", "..", "src", "concept", "suismuis")
TAX = [
    ("wonen", "Wonen & decoratie", "p-schilderij-1", [("schilderijen", "Schilderijen"), ("spiegels", "Spiegels"), ("beeldjes", "Beeldjes & objecten"), ("bloempotten", "Bloempotten"), ("droogbloemen", "Droogbloemen")]),
    ("vazen", "Vazen", "c-decoratie", [("glazen-vazen", "Glazen vazen"), ("stenen-vazen", "Stenen vazen"), ("rotan-vazen", "Rotan vazen")]),
    ("verlichting", "Verlichting & kaarsen", "c-verlichting", [("lampen", "Lampen"), ("lampenkappen", "Lampenkappen"), ("kaarsen", "Kaarsen & windlichten")]),
    ("textiel", "Textiel", "c-textiel", [("kussenhoezen", "Kussenhoezen"), ("plaids", "Plaids"), ("vloerkleden", "Vloerkleden"), ("beddengoed", "Beddengoed"), ("gordijnen", "Gordijnen & vitrage"), ("vloerkussens", "Vloerkussens")]),
    ("tafel", "Servies & tafel", "c-accessoires", [("servies", "Servies"), ("schalen", "Schalen & dienbladen"), ("tafellinnen", "Servetten & placemats")]),
    ("meubels", "Meubels", "p-kruk", [("bijzettafels", "Bijzettafels"), ("salontafels", "Salontafels"), ("eettafels", "Eettafels"), ("eetkamerstoelen", "Eetkamerstoelen"), ("stoelen", "Stoelen"), ("fauteuils", "Fauteuils"), ("bankjes", "Bankjes"), ("krukken", "Barkrukken"), ("kasten", "Kasten & nachtkastjes")]),
]
CATS = [(c, n, img) for c, n, img, _ in TAX]
SVG = {
    "zoek": '<svg viewBox="0 0 24 24"><circle cx="11" cy="11" r="7"/><path d="M20 20l-4-4"/></svg>',
    "account": '<svg viewBox="0 0 24 24"><circle cx="12" cy="8" r="4"/><path d="M4 21c1.5-4 4.5-6 8-6s6.5 2 8 6"/></svg>',
    "hart": '<svg viewBox="0 0 24 24"><path d="M12 20s-7.5-4.6-7.5-10A4.3 4.3 0 0 1 12 7.4 4.3 4.3 0 0 1 19.5 10c0 5.4-7.5 10-7.5 10z"/></svg>',
    "mand": '<svg viewBox="0 0 24 24"><path d="M5 8h14l-1 13H6z"/><path d="M9 8V6a3 3 0 0 1 6 0v2"/></svg>',
    "menu": '<svg viewBox="0 0 24 24"><path d="M3 7h18M3 12h18M3 17h18"/></svg>',
}


def kop(actief):
    nav = [("index.html", "Home", "home"), ("shop.html", "Shop", "shop"), ("over.html", "Over ons", "over"), ("journal.html", "Journal", "journal"), ("klantenservice.html", "Klantenservice", "service")]
    def navlink(h, t, k):
        cur = ' aria-current="page"' if k == actief else ""
        if k != "shop":
            return f'<a href="{h}"{cur}>{t}</a>'
        kol = "".join(f'<div class="mega-kol"><a class="mega-kop" href="shop.html?cat={c}">{n}</a><ul>' + "".join(f'<li><a href="shop.html?cat={c}&amp;sub={sk}">{sn}</a></li>' for sk, sn in subs) + '</ul></div>' for c, n, _, subs in TAX)
        return (f'<div class="mega-wrap"><a href="{h}"{cur} class="mega-knop" aria-haspopup="true" aria-expanded="false">{t}</a>'
                f'<div class="mega" role="region" aria-label="Shop per categorie"><div class="wrap mega-grid">{kol}'
                f'<a class="mega-alles" href="shop.html">Bekijk alle producten</a></div></div></div>')
    links = "".join(navlink(h, t, k) for h, t, k in nav)
    lade_cats = "".join(f'<details><summary>{n}</summary><a href="shop.html?cat={c}">Alles in {n.lower()}</a>' + "".join(f'<a href="shop.html?cat={c}&amp;sub={sk}">{sn}</a>' for sk, sn in subs) + '</details>' for c, n, _, subs in TAX)
    return f'''<div class="wm alleen-concept" aria-hidden="true"></div>
<a class="sr" href="#inhoud">Naar de inhoud</a>
<div class="balk">Gratis verzending vanaf € 75<span class="balk-extra"> &nbsp;·&nbsp; 14 dagen bedenktijd</span></div>
<header class="kopbalk"><div class="wrap kop">
 <nav aria-label="Hoofdmenu">{links}</nav>
 <button class="ico menuknop" type="button" data-open="lade" aria-label="Menu openen">{SVG["menu"]}</button>
 <a class="logo" href="index.html" aria-label="Suismuis Home, naar de homepage"><img src="img/logo-mono.png" alt="" width="64" height="64"><span class="woord"><b>SUISMUIS</b><span>HOME</span></span></a>
 <div class="iconen">
  <button class="ico" type="button" data-open="zoek" aria-label="Zoeken">{SVG["zoek"]}</button>
  <a class="ico verberg" href="bestelling.html" aria-label="Bestelling volgen">{SVG["account"]}</a>
  <a class="ico" href="favorieten.html" aria-label="Favorieten">{SVG["hart"]}<span class="teller" data-teller="favs"></span></a>
  <a class="ico" href="winkelmand.html" aria-label="Winkelmand">{SVG["mand"]}<span class="teller" data-teller="mand"></span></a>
 </div>
</div></header>
<div class="lade" id="lade" role="dialog" aria-modal="true" aria-label="Menu"><div class="doek" data-sluit></div><div class="paneel">
 <button class="sluit" type="button" data-sluit aria-label="Menu sluiten">×</button>
 <a href="index.html">Home</a><a href="shop.html">Shop</a><div class="sub">{lade_cats}</div>
 <a href="over.html">Over ons</a><a href="journal.html">Journal</a><a href="klantenservice.html">Klantenservice</a><a href="bestelling.html">Bestelling volgen</a><a href="favorieten.html">Favorieten</a>
</div></div>
<div class="zoek" id="zoek" role="dialog" aria-modal="true" aria-label="Zoeken"><div class="wrap">
 <div style="display:flex;justify-content:space-between;align-items:center"><span class="klein">Zoeken</span><button class="sluit" type="button" data-sluit aria-label="Zoeken sluiten">×</button></div>
 <label class="sr" for="zoekveld">Zoek een product</label><input id="zoekveld" type="search" placeholder="Waar ben je naar op zoek?" autocomplete="off">
 <p class="leeg" id="zoekleeg">Zoek op bijvoorbeeld vaas, kaars, linnen of lamp.</p><div class="resultaten producten" id="zoekres"></div>
</div></div>'''


def voet():
    cats = "".join(f'<li><a href="shop.html?cat={c}">{n}</a></li>' for c, n, _ in CATS)
    return f'''<footer><div class="wrap">
 <div class="voet">
  <div><b>Suismuis</b><p>Warme, tijdloze woonaccessoires voor een thuis vol rust.</p><div class="betaalmerken" aria-label="Betaalmethoden"><span>Visa</span><span>Mastercard</span><span>American Express</span><span>3D Secure</span></div></div>
  <div><h4>Shop</h4><ul>{cats}</ul></div>
  <div><h4>Klantenservice</h4><ul><li><a href="klantenservice.html#verzenden">Verzenden</a></li><li><a href="klantenservice.html#retour">Retourneren</a></li><li><a href="klantenservice.html#herroepen">Bestelling herroepen</a></li><li><a href="klantenservice.html#faq">Veelgestelde vragen</a></li><li><a href="klantenservice.html#contact">Contact</a></li></ul></div>
  <div><h4>Suismuis</h4><ul><li><a href="over.html">Over ons</a></li><li><a href="journal.html">Journal</a></li><li><a href="bestelling.html">Bestelling volgen</a></li><li><a href="index.html#brief">Nieuwsbrief</a></li><li class="alleen-concept"><a href="beheer.html">Beheer (voor Kim)</a></li></ul></div>
 </div>
 <div class="onder"><span>© 2026 Suismuis Home</span><span><a href="klantenservice.html#voorwaarden">Algemene voorwaarden</a> · <a href="klantenservice.html#privacy">Privacy</a></span></div>
</div></footer>
<div class="concept alleen-concept">Concept door <a href="https://collensgroup.com">Collens Group</a></div>'''


def pagina(bestand, titel, sleutel, actief, inhoud, beschrijving="Warme, tijdloze woonaccessoires: vazen, kaarsen, kussens, verlichting en linnen."):
    html = f'''<!DOCTYPE html>
<html lang="nl">
<head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{titel}</title>
<link rel="icon" href="assets/favicon.svg" type="image/svg+xml">
<meta property="og:title" content="{titel}"><meta property="og:description" content="{beschrijving}"><meta property="og:image" content="https://collensgroup.com/concept/suismuis/img/og.jpg"><meta property="og:type" content="website"><meta name="twitter:card" content="summary_large_image">
<meta name="robots" content="noindex,nofollow,noarchive"><meta name="description" content="{beschrijving}">
<meta name="generator" content="Collens Group concept cgc-suismuis"><meta name="copyright" content="Collens Group">
<meta name="theme-color" content="#E5D8C8">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,500;1,400&family=Jost:wght@300;400&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/suismuis.css">
</head>
<body data-pagina="{sleutel}">
{kop(actief)}
<main id="inhoud">
{inhoud}
</main>
{voet()}
<script src="assets/scouting.js" defer></script><script src="assets/suismuis.js" defer></script>
</body>
</html>
'''
    with open(os.path.join(DOEL, bestand), "w", encoding="utf-8") as f:
        f.write(html)


def paginakop(titel, tekst, kruimel):
    k = '<a href="index.html">Home</a><span>/</span>' + "<span>/</span>".join(kruimel)
    return f'<div class="paginakop"><div class="wrap"><nav class="kruimel" aria-label="Kruimelpad">{k}</nav><h1>{titel}</h1>{f"<p>{tekst}</p>" if tekst else ""}</div></div>'


ZEKER = '''<div class="zeker"><div class="wrap"><ul>
 <li><svg viewBox="0 0 32 32" aria-hidden="true"><path d="M3 9h17v13H3zM20 13h5l4 4v5h-9z"/><circle cx="9" cy="24" r="2.5"/><circle cx="24" cy="24" r="2.5"/></svg>Gratis verzending vanaf € 75</li>
 <li><svg viewBox="0 0 32 32" aria-hidden="true"><path d="M16 27S4 19.5 4 11.5A6 6 0 0 1 16 9a6 6 0 0 1 12 2.5C28 19.5 16 27 16 27z"/></svg>Met liefde uitgekozen</li>
 <li><svg viewBox="0 0 32 32" aria-hidden="true"><path d="M6 12a10 10 0 0 1 18-3M26 20a10 10 0 0 1-18 3"/><path d="M24 4v5h-5M8 28v-5h5"/></svg>14 dagen bedenktijd</li>
 <li><svg viewBox="0 0 32 32" aria-hidden="true"><rect x="7" y="14" width="18" height="13" rx="2"/><path d="M11 14v-4a5 5 0 0 1 10 0v4"/><circle cx="16" cy="20.5" r="1.6"/></svg>Veilig betalen met creditcard</li>
</ul></div></div>'''

ARTIKELEN = [
    ("rust", "j-rust", "Rust in huis in vijf stappen", "Minder spullen, meer ruimte: zo creëer je een interieur dat tot rust brengt.",
     ["Begin met opruimen: laat per ruimte alleen staan wat je echt gebruikt of mooi vindt.", "Kies een palet van drie tot vier zachte tinten, zoals crème, zand en taupe, en houd die overal aan.", "Werk met natuurlijke materialen: linnen, hout, keramiek en steen geven warmte zonder drukte.", "Zorg voor zacht licht op meerdere hoogtes: een tafellamp, een kaars en een hanglamp in plaats van één felle plafondlamp.", "Groepeer decoratie in oneven aantallen, bijvoorbeeld een vaas, een schaal en een kaars bij elkaar."]),
    ("kaarsen", "j-kaarsen", "Sfeer met kaarslicht", "Zo zet je kaarsen veilig en stijlvol neer, van eettafel tot badkamer.",
     ["Combineer verschillende hoogtes: een lage kaarsschaal naast twee kandelaars geeft direct diepte.", "Kies windlichten voor plekken waar het tocht of waar kinderen en huisdieren komen.", "Laat een stompkaars de eerste keer lang genoeg branden, tot de hele bovenkant gesmolten is. Zo brandt hij gelijkmatig af.", "Laat kaarsen nooit onbeheerd branden en houd ze uit de buurt van gordijnen en droogbloemen."]),
    ("linnen", "j-linnen", "Waarom wij van linnen houden", "Linnen wordt met elke wasbeurt zachter. Zo verzorg je het goed.",
     ["Was linnen op 30 of 40 °C met een mild wasmiddel, zonder wasverzachter.", "Droog het bij voorkeur aan de lijn; in de droger op een lage stand blijft het extra zacht.", "Kreukels horen erbij en geven de ontspannen, natuurlijke look. Strijken hoeft niet.", "Linnen is ademend: koel in de zomer en warm in de winter."]),
]


def bouw():
    os.makedirs(DOEL, exist_ok=True)
    cat_tegels = "".join(f'<a class="cat" href="shop.html?cat={c}"><div class="beeld"><img src="img/{img}.jpg" alt="" loading="lazy" width="1200" height="1200"></div><span>{n.split(" &")[0]}</span></a>' for c, n, img in CATS)
    journal = "".join(f'<a class="artikel" href="journal.html#{s}"><div class="beeld"><img src="img/{img}.jpg" alt="" loading="lazy" width="1500" height="1000"></div><h3>{t}</h3><p>{k}</p><span class="link">Lees verder</span></a>' for s, img, t, k, _ in ARTIKELEN)

    # ---------- home ----------
    stippen = [("s1", 77, 24, "droogbloemen-champagne", "p-droogbloemen", "Droogbloemen Champagne", "€ 34,95"),
               ("s2", 82, 62, "plaid-teddy", "p-plaid-teddy", "Plaid Teddy", "€ 74,95"),
               ("s3", 93, 50, "kussenhoes-linnen", "p-kussens-linnen", "Kussenhoes Linnen", "€ 39,95")]
    stip_html = "".join(f'<button class="stip" type="button" style="left:{x}%;top:{y}%" aria-controls="{i}" aria-expanded="false" aria-label="Bekijk {n}"></button>'
                        f'<a class="stip-kaart" id="{i}" href="product.html?p={pid}" style="left:{x}%;top:{y}%"><img src="img/{img}.jpg" alt=""><span><b>{n}</b>{pr} · Bekijk</span></a>'
                        for i, x, y, pid, img, n, pr in stippen)
    pillen = [(77, 24, "shop.html?cat=wonen", "Wonen & decoratie", "Bekijk"), (82, 62, "shop.html?cat=textiel&sub=plaids", "Plaids", "Bekijk"), (93, 50, "shop.html?cat=textiel&sub=kussenhoezen", "Kussenhoezen", "Bekijk")]
    stip_html = "".join(f'<a class="pil{" links" if x > 70 else ""}" href="{h}" style="left:{x}%;top:{y}%"><i aria-hidden="true"></i><span><b>{n}</b>{pr}</span></a>'
                        for x, y, h, n, pr in pillen)
    tak = '<svg class="tak" viewBox="0 0 220 420" aria-hidden="true"><g fill="none" stroke="currentColor" stroke-width="1.4" stroke-linecap="round"><path d="M120 418C116 330 104 250 70 170 52 128 40 80 44 14"/><path d="M98 300c-26-8-46-26-56-52M92 262c22-16 46-22 74-18M80 214c-24-6-40-22-50-44M72 176c18-18 40-28 66-28M60 132c-20-8-32-24-38-44M54 100c14-16 32-24 54-24M48 60c-12-10-18-24-18-38"/></g><g fill="currentColor" opacity=".55"><ellipse cx="40" cy="246" rx="9" ry="4" transform="rotate(-50 40 246)"/><ellipse cx="168" cy="244" rx="9" ry="4" transform="rotate(10 168 244)"/><ellipse cx="28" cy="168" rx="8" ry="4" transform="rotate(-60 28 168)"/><ellipse cx="140" cy="148" rx="8" ry="4"/><ellipse cx="20" cy="88" rx="7" ry="3.5" transform="rotate(-70 20 88)"/><ellipse cx="110" cy="76" rx="7" ry="3.5"/><ellipse cx="30" cy="20" rx="6" ry="3" transform="rotate(-80 30 20)"/></g></svg>'
    pagina("index.html", "Suismuis Home – warm, stijlvol, tijdloos wonen (concept)", "home", "home", f'''
<div class="voorpagina" id="look">
 <img src="img/s-held.jpg" alt="Rustige woonkamer in warme tinten met pampas, een crèmekleurige bank en zacht daglicht" width="2000" height="1333" fetchpriority="high">
 {stip_html}
 <div class="wrap voorpagina-tekst">
  <span class="klein">Live beautiful. Live Suismuis.</span>
  <h1>Jouw huis,<br>onze passie</h1>
  <p>Ontdek tijdloze woonaccessoires met een vleugje elegantie.</p>
  <div class="knoppen"><a class="knop" href="shop.html">Shop de look <span aria-hidden="true">→</span></a></div>
 </div>
</div>
<section class="cat-band" aria-label="Shop per categorie"><div class="cats">{cat_tegels}</div></section>
<section class="nieuw"><div class="wrap">
 <div class="sectiekop midden"><h2>Nieuw binnen</h2><p>Zorgvuldig gekozen stukken die je interieur rust en warmte geven.</p></div>
 <div class="producten studio" id="nieuw-grid"></div>
 <div class="midden-knop"><a class="knop licht" href="shop.html">Bekijk de hele collectie</a></div>
</div></section>
<section class="verhaal">
 <img src="img/s-verhaal.jpg" alt="Bank met zachte kussens, een houten bijzettafel en een vaas met bloemen" loading="lazy" width="1800" height="1350">
 <div class="verhaal-tekst"><span class="klein">Het Suismuis-gevoel</span><h2>Warm. Stijlvol. Tijdloos.</h2>
  <p>Bij Suismuis Home geloven we in de schoonheid van eenvoud. Onze collectie brengt warmte, stijl en rust in elk huis: linnen, hout, keramiek en zacht licht.</p>
  <div><a class="knop" href="over.html">Over Suismuis <span aria-hidden="true">→</span></a></div></div>
</section>
{ZEKER}
<section><div class="wrap">
 <div class="sectiekop"><div><h2>Journal</h2><p>Stylingtips en inspiratie voor een thuis vol rust.</p></div><a class="link" href="journal.html">Alle verhalen</a></div>
 <div class="journal-rij">{journal}</div>
</div></section>
<section class="brief-vol" id="brief">
 <img src="img/s-brief.jpg" alt="" loading="lazy" width="1800" height="1200">
 <div class="wrap"><div class="brief-tekst"><span class="klein">Blijf geïnspireerd</span><h2>Als eerste de nieuwe collectie zien</h2>
  <p>Schrijf je in voor de nieuwsbrief en ontvang stylingtips en nieuwe items. Afmelden kan altijd.</p>
  <form data-soort="nieuwsbrief" data-bevestig="Dank je wel! Je inschrijving is ontvangen." novalidate><label for="mail" class="sr">E-mailadres</label><input id="mail" name="email" type="email" required placeholder="Je e-mailadres" autocomplete="email"><button type="submit">Inschrijven</button></form>
 </div></div>
</section>''')

    # ---------- shop ----------
    pagina("shop.html", "Shop | Suismuis Home (concept)", "shop", "shop",
           f'''<div class="paginakop"><div class="wrap"><nav class="kruimel" aria-label="Kruimelpad"><a href="index.html">Home</a><span>/</span><a href="shop.html">Shop</a><span>/</span><span id="kruimel-cat">Alle producten</span></nav>
<h1 id="shop-titel">Alle producten</h1><p id="shop-intro">Wonen, vazen, verlichting, textiel, servies en meubels in warme, natuurlijke tinten.</p></div></div>
<section style="padding-top:44px"><div class="wrap">
 <div class="shopbalk"><nav class="subnav" id="subnav" aria-label="Subcategorieën"></nav>
  <div style="display:flex;gap:16px;align-items:center"><span class="aantal-res" id="aantal" aria-live="polite"></span><label class="sr" for="sorteer">Sorteren</label>
  <select id="sorteer"><option value="standaard">Aanbevolen</option><option value="laag">Prijs laag – hoog</option><option value="hoog">Prijs hoog – laag</option><option value="naam">Naam A – Z</option></select></div></div>
 <div class="producten" id="shop-grid"></div>
 <div class="binnenkort" id="binnenkort" hidden><h2>Deze collectie wordt nu samengesteld</h2><p>De eerste stukken staan hier binnenkort. Laat je e-mailadres achter, dan hoor je het als eerste.</p>
  <form data-soort="nieuwsbrief" data-bevestig="Dank je wel! We laten het je weten zodra deze collectie online staat." novalidate><label for="bk-mail" class="sr">E-mailadres</label><input id="bk-mail" name="email" type="email" required placeholder="Je e-mailadres" autocomplete="email"><button type="submit">Houd me op de hoogte</button></form>
  <a class="link" id="bk-terug" href="shop.html">Bekijk de hele collectie</a></div>
 <p class="noot">Voorbeeldproducten en voorbeeldprijzen: bij lancering komen hier jouw eigen producten, foto's en prijzen.</p>
</div></section>
{ZEKER}''')

    # ---------- product ----------
    pagina("product.html", "Product | Suismuis Home (concept)", "product", "shop",
           '''<div class="wrap"><div class="pdp" id="pdp"></div></div>
<section class="nieuw"><div class="wrap"><div class="sectiekop"><h2>Mooi in combinatie met</h2><a class="link" href="shop.html">Alle producten</a></div><div class="producten" id="gerelateerd"></div></div></section>''')

    # ---------- winkelmand ----------
    pagina("winkelmand.html", "Winkelmand | Suismuis Home (concept)", "mand", "",
           paginakop("Winkelmand", "", ["<span>Winkelmand</span>"]) + '''
<div class="wrap"><div class="mand" id="mand">
 <div><div id="mand-regels"></div><a class="link" href="shop.html" style="display:inline-block;margin-top:22px">Verder winkelen</a></div>
 <aside class="samenvatting" aria-label="Overzicht">
  <h2 style="font-size:30px;margin-bottom:12px">Overzicht</h2>
  <div class="voortgang"><span id="vg-tekst"></span><div class="baan"><div class="vul" id="vg-vul"></div></div></div>
  <div class="rij"><span>Subtotaal</span><span id="sub"></span></div>
  <div class="rij"><span>Verzending</span><span id="verz"></span></div>
  <div class="rij" id="cad-rij" hidden><span>Cadeauverpakking</span><span id="cad"></span></div>
  <label class="check"><input type="checkbox" id="cadeau"> Inpakken als cadeau met handgeschreven kaartje (+ € 3,95)</label>
  <div class="rij totaal"><span>Totaal</span><span id="tot"></span></div>
  <p style="font-size:13px;color:var(--mokka);margin:6px 0 18px">Prijzen inclusief btw.</p>
  <a class="knop breed" href="afrekenen.html">Veilig afrekenen</a>
  <p style="font-size:13px;margin:14px 0 0;text-align:center">Veilig betalen met creditcard: Visa, Mastercard en American Express</p>
 </aside>
</div></div>''')

    # ---------- afrekenen ----------
    pagina("afrekenen.html", "Afrekenen | Suismuis Home (concept)", "afrekenen", "",
           paginakop("Afrekenen", "", ['<a href="winkelmand.html">Winkelmand</a>', "<span>Afrekenen</span>"]) + '''
<div class="wrap"><div class="mand" id="afreken">
 <form class="form" id="bestel" novalidate>
  <ol class="stappen" aria-label="Stappen"><li aria-current="step" data-stap="1">Gegevens</li><li data-stap="2">Betalen</li><li data-stap="3">Bevestiging</li></ol>
  <fieldset id="gegevens">
  <legend class="sr">Je gegevens</legend>
  <div class="twee"><label>Voornaam *<input name="voornaam" required autocomplete="given-name"></label><label>Achternaam *<input name="achternaam" required autocomplete="family-name"></label></div>
  <div class="twee"><label>E-mailadres *<input name="email" type="email" required autocomplete="email"></label><label>Telefoon (optioneel)<input name="tel" type="tel" autocomplete="tel"></label></div>
  <div class="twee"><label>Postcode *<input name="postcode" required autocomplete="postal-code"></label><label>Huisnummer *<input name="huisnummer" required></label></div>
  <div class="twee"><label>Straat *<input name="straat" required autocomplete="address-line1"></label><label>Plaats *<input name="plaats" required autocomplete="address-level2"></label></div>
  <label>Land<select name="land" autocomplete="country-name"><option>Nederland</option><option>België</option></select></label>
  <label class="check"><input name="akkoord" type="checkbox" required><span>Ik ga akkoord met de <a class="link" href="klantenservice.html#voorwaarden" target="_blank">algemene voorwaarden</a> en heb de <a class="link" href="klantenservice.html#privacy" target="_blank">privacyverklaring</a> gelezen *</span></label>
  <p id="fout" role="alert" class="fout"></p>
  <button class="knop" type="submit" id="naar-betalen">Verder naar betalen</button>
  </fieldset>
  <section id="betalen" class="kaartbetaal" hidden aria-labelledby="betalen-kop">
   <div class="kaart-kop"><h2 id="betalen-kop">Betalen met creditcard</h2><span class="merken" aria-label="Wij accepteren Visa, Mastercard en American Express"><i class="m-visa">VISA</i><i class="m-mc"><b></b><b></b></i><i class="m-amex">AMEX</i></span></div>
   <p class="kaart-voor" id="kaart-voor"></p>
   <div id="kaartvelden" class="kaartvelden">
    <div id="cf-naam" class="cf"></div>
    <div id="cf-nummer" class="cf"></div>
    <div class="twee"><div id="cf-datum" class="cf"></div><div id="cf-cvv" class="cf"></div></div>
   </div>
   <div id="kaartknop"></div>
   <p id="betaalfout" role="alert" class="fout"></p>
   <button class="knop breed" type="button" id="betaal">Betaal veilig</button>
   <ul class="bz"><li><svg viewBox="0 0 24 24" aria-hidden="true"><rect x="5" y="11" width="14" height="10" rx="2"/><path d="M8 11V8a4 4 0 0 1 8 0v3"/></svg><span><b>Versleutelde betaling met 3D Secure</b>Je kaartgegevens gaan rechtstreeks naar de betaalverwerker. Wij zien en bewaren ze nooit.</span></li>
   <li><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 12a8 8 0 1 0 3-6.2"/><path d="M4 4v5h5"/></svg><span><b>14 dagen bedenktijd</b>Niet helemaal blij? Je krijgt je geld terug.</span></li>
   <li><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 6h16v12H4z"/><path d="M4 7l8 6 8-6"/></svg><span><b>Direct een bevestiging</b>Met je ordernummer en een link om je bestelling te volgen.</span></li></ul>
   <button type="button" class="link terug" id="wijzig">Gegevens wijzigen</button>
  </section>
 </form>
 <aside class="samenvatting" aria-label="Je bestelling"><h2 style="font-size:30px;margin-bottom:12px">Je bestelling</h2><div id="overzicht"></div></aside>
</div></div>''')

    # ---------- favorieten ----------
    pagina("favorieten.html", "Favorieten | Suismuis Home (concept)", "favorieten", "",
           paginakop("Favorieten", "Bewaar wat je mooi vindt en bestel wanneer het jou uitkomt.", ["<span>Favorieten</span>"]) + '''
<section style="padding-top:48px"><div class="wrap"><div id="fav-leeg"><p>Je hebt nog geen favorieten. Tik op het hartje bij een product om het te bewaren.</p><a class="knop" href="shop.html">Naar de shop</a></div>
<div class="producten" id="fav-grid"></div></div></section>''')

    # ---------- over ----------
    pagina("over.html", "Over ons | Suismuis Home (concept)", "over", "over",
           paginakop("Over Suismuis", "Een thuis dat rust geeft, warm aanvoelt en nooit uit de mode raakt.", ["<span>Over ons</span>"]) + '''
<div class="wrap twee-kol">
 <img src="img/s-over.jpg" alt="Woonkamer met een zachte crèmekleurige bank en warm licht" loading="lazy" width="1400" height="1750">
 <div><span class="klein">Ons verhaal</span><h2 style="font-size:44px;margin:12px 0 18px">De schoonheid van eenvoud</h2>
  <p>Suismuis Home is ontstaan uit liefde voor interieurs die tot rust brengen. Geen drukte, geen trends die na een seizoen weer verdwijnen, maar stukken die je jarenlang blijft waarderen.</p>
  <p>We kiezen elk product met zorg: natuurlijke materialen zoals linnen, hout, keramiek en steen, in zachte tinten van crème tot espresso. Zo past alles bij elkaar en bouw je stap voor stap een thuis dat helemaal van jou is.</p>
  <a class="knop" href="shop.html">Ontdek de collectie</a></div>
</div>''' + ZEKER)

    # ---------- journal ----------
    stukken = "".join(f'''<article id="{s}" style="padding:56px 0;border-bottom:1px solid var(--lijn)"><div class="twee-kol" style="padding:0">
<img src="img/{img}.jpg" alt="" loading="lazy" width="1500" height="1000" style="aspect-ratio:3/2;object-fit:cover">
<div><span class="klein">Journal</span><h2 style="font-size:40px;margin:12px 0 14px">{t}</h2><p>{k}</p><ol style="padding-left:20px">{"".join(f"<li style='margin-bottom:8px'>{x}</li>" for x in punten)}</ol></div></div></article>'''
                      for s, img, t, k, punten in ARTIKELEN)
    pagina("journal.html", "Journal | Suismuis Home (concept)", "journal", "journal",
           paginakop("Journal", "Stylingtips, onderhoud en inspiratie voor een thuis vol rust.", ["<span>Journal</span>"]) + f'<div class="wrap">{stukken}</div>')

    # ---------- klantenservice ----------
    faq = [("Wanneer is mijn bestelling in huis?", "Binnen 8–15 werkdagen, in Nederland en België. Zodra je pakket onderweg is, krijg je een track-and-tracecode per e-mail."),
           ("Wat kost verzending?", "Verzending kost € 5,95. Vanaf € 75 verzenden we gratis binnen Nederland en België."),
           ("Kan ik mijn bestelling retourneren?", "Ja, je hebt 14 dagen bedenktijd na ontvangst. Gebruik de knop Bestelling herroepen hierboven; je krijgt het aankoopbedrag binnen 14 dagen terug."),
           ("Kan ik een product als cadeau laten inpakken?", "Ja, bij het afrekenen kies je voor cadeauverpakking met een handgeschreven kaartje (+ € 3,95)."),
           ("Hoe kan ik betalen?", "Met je creditcard: Visa, Mastercard of American Express. Je vult je kaart in op een beveiligde betaalpagina met 3D Secure; je kaartgegevens gaan versleuteld rechtstreeks naar de betaalverwerker en worden nooit door ons gezien of bewaard."),
           ("Is betalen bij Suismuis Home veilig?", "Ja. De site is volledig versleuteld (https) en betalingen lopen via een erkende betaalverwerker met 3D Secure. Je bank vraagt je meestal om de betaling in je bank-app te bevestigen. Direct na je betaling krijg je een bevestiging met je ordernummer."),
           ("Kan ik mijn bestelling volgen?", "Ja. In je bevestigingsmail staat een link naar je bestelling. Je kunt ook op <a class='link' href='bestelling.html'>Bestelling volgen</a> je ordernummer en e-mailadres invullen."),
           ("Zijn de producten handgemaakt?", "Veel stukken zijn van natuurlijke materialen en deels met de hand gemaakt. Kleine verschillen in kleur en structuur maken elk stuk uniek.")]
    faq_html = "".join(f"<details><summary>{v}</summary><p>{a}</p></details>" for v, a in faq)
    pagina("klantenservice.html", "Klantenservice | Suismuis Home (concept)", "service", "service",
           paginakop("Klantenservice", "We helpen je graag. Hier vind je alles over bestellen, verzenden en retourneren.", ["<span>Klantenservice</span>"]) + f'''
<div class="wrap"><div class="tekst">
 <h2 id="verzenden">Verzenden</h2><ul><li>Je bestelling is binnen 8–15 werkdagen in huis.</li><li>We leveren in Nederland en België.</li><li>Verzendkosten € 5,95, gratis vanaf € 75.</li><li>Je ontvangt een track-and-tracecode per e-mail.</li></ul>
 <h2 id="retour">Retourneren</h2><p>Niet helemaal blij? Je hebt 14 dagen bedenktijd na ontvangst. Stuur het product ongebruikt en in de originele verpakking terug. Meld je retour aan met de knop <a class="link" href="#herroepen">Bestelling herroepen</a>; binnen 14 dagen na ontvangst van je retour storten we het bedrag terug.</p>
 <h2 id="herroepen">Bestelling herroepen</h2><p>Je kunt je bestelling binnen 14 dagen na ontvangst zonder opgaaf van reden herroepen. Vul je gegevens in en druk op de knop; je krijgt direct een ontvangstbevestiging per e-mail.</p>
 <form class="form" data-soort="herroeping" data-bevestig="Je herroeping is ontvangen. Je krijgt een bevestiging per e-mail; binnen twee werkdagen sturen we je het retouradres." novalidate>
  <div class="twee"><label>Naam *<input name="naam" required autocomplete="name"></label><label>E-mailadres *<input name="email" type="email" required autocomplete="email"></label></div>
  <div class="twee"><label>Ordernummer *<input name="Ordernummer" required></label><label>Datum van ontvangst *<input name="Datum van ontvangst" type="date" required></label></div>
  <label>Welke producten herroep je? (optioneel)<input name="Producten"></label><input class="hp" name="website" tabindex="-1" autocomplete="off" aria-hidden="true">
  <button class="knop" type="submit">Bestelling herroepen</button>
 </form>
 <details style="margin-top:22px"><summary>Modelformulier voor herroeping</summary><p>Liever per post of e-mail? Gebruik dan dit modelformulier. Aan: {WINKEL_TXT}. Ik deel u hierbij mede dat ik onze overeenkomst betreffende de verkoop van de volgende goederen herroep: [producten]. Besteld op / ontvangen op: [datum]. Naam en adres: [gegevens]. Datum: [datum].</p></details>
 <h2 id="faq">Veelgestelde vragen</h2>{faq_html}
 <h2 id="contact">Contact</h2><p>Stel je vraag via het formulier of mail naar <a class="link" href="mailto:{WINKEL["email"]}">{WINKEL["email"]}</a>. We reageren binnen één werkdag.</p>
 <form class="form" data-soort="contact" data-bevestig="Dank je wel! We reageren binnen één werkdag." novalidate>
  <div class="twee"><label>Naam *<input name="naam" required autocomplete="name"></label><label>E-mailadres *<input name="email" type="email" required autocomplete="email"></label></div>
  <label>Ordernummer (optioneel)<input name="Ordernummer"></label><input class="hp" name="website" tabindex="-1" autocomplete="off" aria-hidden="true">
  <label>Onderwerp<select name="Onderwerp"><option>Vraag over een product</option><option>Mijn bestelling</option><option>Retour aanmelden</option><option>Iets anders</option></select></label>
  <label>Bericht *<textarea name="Bericht" required></textarea></label>
  <button class="knop" type="submit">Verstuur bericht</button>
 </form>
 <h2 id="voorwaarden">Algemene voorwaarden</h2>{VOORWAARDEN}
 <h2 id="privacy">Privacyverklaring</h2>{PRIVACY}
</div></div>''')

    # ---------- bestelling volgen (ook als account.html, voor oude links) ----------
    volg = paginakop("Bestelling volgen", "Bekijk de status van je bestelling met je ordernummer en e-mailadres.", ["<span>Bestelling volgen</span>"]) + '''
<div class="wrap"><div class="tekst" style="max-width:640px">
 <div id="volg-uitslag" aria-live="polite"></div>
 <form class="form" id="volg" novalidate>
  <label>Ordernummer *<input name="nr" required placeholder="Bijvoorbeeld SH261122-AB12" autocomplete="off"></label>
  <label>E-mailadres *<input name="email" type="email" required autocomplete="email"></label>
  <p class="fout" role="alert" id="volg-fout"></p>
  <button class="knop" type="submit">Bekijk mijn bestelling</button>
  <p class="noot">Je ordernummer staat in de bevestigingsmail. Vragen? <a class="link" href="klantenservice.html#contact">Neem contact op</a>.</p>
 </form>
</div></div>'''
    pagina("bestelling.html", "Bestelling volgen | Suismuis Home (concept)", "bestelling", "", volg)
    pagina("account.html", "Bestelling volgen | Suismuis Home (concept)", "bestelling", "", volg)

    # ---------- beheer: bestelbalie voor Kim (inloggen met eigen wachtwoord) ----------
    pagina("beheer.html", "Bestelbalie | Suismuis Home", "beheer", "",
           paginakop("Bestelbalie", "Je bestellingen en berichten op één plek.", ["<span>Bestelbalie</span>"]) + '''
<div class="wrap" id="beheer">
 <form class="form smal" id="bh-setup" hidden novalidate><h2>Kies je wachtwoord</h2><p>Kies een wachtwoord van minstens 10 tekens. Alleen jij kent het; bewaar het in je wachtwoordkluis.</p>
  <label>Nieuw wachtwoord *<input name="pw" type="password" required minlength="10" autocomplete="new-password"></label><label>Herhaal wachtwoord *<input name="pw2" type="password" required minlength="10" autocomplete="new-password"></label>
  <p class="fout" role="alert"></p><button class="knop" type="submit">Wachtwoord opslaan</button></form>
 <form class="form smal" id="bh-login" hidden novalidate><h2>Inloggen</h2>
  <label>Wachtwoord *<input name="pw" type="password" required autocomplete="current-password"></label>
  <p class="fout" role="alert"></p><button class="knop" type="submit">Inloggen</button></form>
 <div id="bh-app" hidden>
  <div class="bh-balk"><div class="bh-tabs" role="tablist"><button type="button" role="tab" aria-selected="true" data-tab="orders">Bestellingen</button><button type="button" role="tab" aria-selected="false" data-tab="berichten">Berichten</button></div><span id="bh-pp" class="klein"></span><button type="button" class="link" id="bh-uit">Uitloggen</button></div>
  <div class="kpi" id="bh-kpi"></div>
  <div id="bh-orders"></div><div id="bh-berichten" hidden></div>
 </div>
</div>''')

if __name__ == "__main__":
    bouw()
    print("Suismuis gebouwd in", os.path.abspath(DOEL))
