"""Bouwt de concept-webshop Suismuis Home in src/concept/suismuis/ (alle pagina's delen kop, voet en watermerk)."""
import os

DOEL = os.path.join(os.path.dirname(__file__), "..", "..", "src", "concept", "suismuis")
CATS = [("decoratie", "Decoratie", "c-decoratie"), ("kaarsen", "Kaarsen & windlichten", "c-kaarsen"), ("kussens", "Kussens", "c-kussens"),
        ("verlichting", "Verlichting", "c-verlichting"), ("textiel", "Plaids & textiel", "c-textiel"), ("accessoires", "Accessoires", "c-accessoires")]
SVG = {
    "zoek": '<svg viewBox="0 0 24 24"><circle cx="11" cy="11" r="7"/><path d="M20 20l-4-4"/></svg>',
    "account": '<svg viewBox="0 0 24 24"><circle cx="12" cy="8" r="4"/><path d="M4 21c1.5-4 4.5-6 8-6s6.5 2 8 6"/></svg>',
    "hart": '<svg viewBox="0 0 24 24"><path d="M12 20s-7.5-4.6-7.5-10A4.3 4.3 0 0 1 12 7.4 4.3 4.3 0 0 1 19.5 10c0 5.4-7.5 10-7.5 10z"/></svg>',
    "mand": '<svg viewBox="0 0 24 24"><path d="M5 8h14l-1 13H6z"/><path d="M9 8V6a3 3 0 0 1 6 0v2"/></svg>',
    "menu": '<svg viewBox="0 0 24 24"><path d="M3 7h18M3 12h18M3 17h18"/></svg>',
}


def kop(actief):
    nav = [("index.html", "Home", "home"), ("shop.html", "Shop", "shop"), ("over.html", "Over ons", "over"), ("journal.html", "Journal", "journal"), ("klantenservice.html", "Klantenservice", "service")]
    links = "".join(f'<a href="{h}"{" aria-current=\"page\"" if k == actief else ""}>{t}</a>' for h, t, k in nav)
    lade_cats = "".join(f'<a href="shop.html?cat={c}">{n}</a>' for c, n, _ in CATS)
    return f'''<div class="wm" aria-hidden="true"></div>
<a class="sr" href="#inhoud">Naar de inhoud</a>
<div class="balk">Gratis verzending vanaf € 75<span class="balk-extra"> &nbsp;·&nbsp; 14 dagen bedenktijd</span></div>
<header class="kopbalk"><div class="wrap kop">
 <nav aria-label="Hoofdmenu">{links}</nav>
 <button class="ico menuknop" type="button" data-open="lade" aria-label="Menu openen">{SVG["menu"]}</button>
 <a class="logo" href="index.html" aria-label="Suismuis Home, naar de homepage"><b>Suismuis</b><span>HOME</span></a>
 <div class="iconen">
  <button class="ico" type="button" data-open="zoek" aria-label="Zoeken">{SVG["zoek"]}</button>
  <a class="ico verberg" href="account.html" aria-label="Mijn account">{SVG["account"]}</a>
  <a class="ico" href="favorieten.html" aria-label="Favorieten">{SVG["hart"]}<span class="teller" data-teller="favs"></span></a>
  <a class="ico" href="winkelmand.html" aria-label="Winkelmand">{SVG["mand"]}<span class="teller" data-teller="mand"></span></a>
 </div>
</div></header>
<div class="lade" id="lade" role="dialog" aria-modal="true" aria-label="Menu"><div class="doek" data-sluit></div><div class="paneel">
 <button class="sluit" type="button" data-sluit aria-label="Menu sluiten">×</button>
 <a href="index.html">Home</a><a href="shop.html">Shop</a><div class="sub">{lade_cats}</div>
 <a href="over.html">Over ons</a><a href="journal.html">Journal</a><a href="klantenservice.html">Klantenservice</a><a href="account.html">Mijn account</a><a href="favorieten.html">Favorieten</a>
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
  <div><b>Suismuis</b><p>Warme, tijdloze woonaccessoires voor een thuis vol rust.</p><div class="betaalmerken" aria-label="Betaalmethoden"><span>iDEAL</span><span>Bancontact</span><span>Visa</span><span>Mastercard</span><span>PayPal</span></div></div>
  <div><h4>Shop</h4><ul>{cats}</ul></div>
  <div><h4>Klantenservice</h4><ul><li><a href="klantenservice.html#verzenden">Verzenden</a></li><li><a href="klantenservice.html#retour">Retourneren</a></li><li><a href="klantenservice.html#herroepen">Bestelling herroepen</a></li><li><a href="klantenservice.html#faq">Veelgestelde vragen</a></li><li><a href="klantenservice.html#contact">Contact</a></li></ul></div>
  <div><h4>Suismuis</h4><ul><li><a href="over.html">Over ons</a></li><li><a href="journal.html">Journal</a></li><li><a href="account.html">Mijn account</a></li><li><a href="index.html#brief">Nieuwsbrief</a></li><li><a href="beheer.html">Beheer (voor Kim)</a></li></ul></div>
 </div>
 <div class="onder"><span>© 2026 Suismuis Home</span><span><a href="klantenservice.html#voorwaarden">Algemene voorwaarden</a> · <a href="klantenservice.html#privacy">Privacy</a></span></div>
</div></footer>
<div class="concept">Concept door <a href="https://collensgroup.com">Collens Group</a></div>'''


def pagina(bestand, titel, sleutel, actief, inhoud, beschrijving="Warme, tijdloze woonaccessoires: vazen, kaarsen, kussens, verlichting en linnen."):
    html = f'''<!DOCTYPE html>
<html lang="nl">
<head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{titel}</title>
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
<script src="assets/suismuis.js" defer></script>
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
 <li><svg viewBox="0 0 32 32" aria-hidden="true"><rect x="7" y="14" width="18" height="13" rx="2"/><path d="M11 14v-4a5 5 0 0 1 10 0v4"/><circle cx="16" cy="20.5" r="1.6"/></svg>Veilig betalen met iDEAL</li>
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
    stippen = [("s1", 13, 50, "droogbloemen-champagne", "p-droogbloemen", "Droogbloemen Champagne", "€ 34,95"),
               ("s2", 82, 62, "plaid-teddy", "p-plaid-teddy", "Plaid Teddy", "€ 74,95"),
               ("s3", 93, 50, "kussenhoes-linnen", "p-kussens-linnen", "Kussenhoes Linnen", "€ 39,95")]
    stip_html = "".join(f'<button class="stip" type="button" style="left:{x}%;top:{y}%" aria-controls="{i}" aria-expanded="false" aria-label="Bekijk {n}"></button>'
                        f'<a class="stip-kaart" id="{i}" href="product.html?p={pid}" style="left:{x}%;top:{y}%"><img src="img/{img}.jpg" alt=""><span><b>{n}</b>{pr} · Bekijk</span></a>'
                        for i, x, y, pid, img, n, pr in stippen)
    pagina("index.html", "Suismuis Home – warm, stijlvol, tijdloos wonen (concept)", "home", "home", f'''
<div class="held">
 <div class="held-tekst">
  <span class="klein">Live beautiful. Live Suismuis.</span>
  <h1>Jouw huis,<br><em>onze passie</em></h1>
  <p>Tijdloze woonaccessoires met een vleugje elegantie. Natuurlijke materialen, zachte tinten.</p>
  <div class="knoppen"><a class="knop" href="#look">Shop de look <span aria-hidden="true">→</span></a><a class="knop licht" href="over.html">Ons verhaal</a></div>
 </div>
 <figure id="look"><img src="img/s-held.jpg" alt="Rustige woonkamer in warme tinten met pampas, een crèmekleurige bank en zacht daglicht" width="2000" height="1333" fetchpriority="high">{stip_html}</figure>
</div>
<section><div class="wrap">
 <div class="sectiekop"><div><h2>Shop per categorie</h2></div><a class="link" href="shop.html">Bekijk alles</a></div>
 <div class="cats">{cat_tegels}</div>
</div></section>
<section class="nieuw"><div class="wrap">
 <div class="sectiekop"><div><h2>Nieuw binnen</h2><p>Zorgvuldig gekozen stukken die je interieur rust en warmte geven.</p></div><a class="link" href="shop.html">Alle producten</a></div>
 <div class="producten" id="nieuw-grid"></div>
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
<section class="brief" id="brief">
 <img src="img/s-brief.jpg" alt="Lichte woonkamer met een lage bank, droogbloemen en een rieten poef" loading="lazy" width="1800" height="1200">
 <div class="brief-tekst"><span class="klein">Blijf geïnspireerd</span><h2>Als eerste de nieuwe collectie zien</h2>
  <p>Schrijf je in voor de nieuwsbrief en ontvang stylingtips en nieuwe items. Afmelden kan altijd.</p>
  <form data-bevestig="Dank je wel! Je inschrijving is ontvangen." novalidate><label for="mail" class="sr">E-mailadres</label><input id="mail" type="email" required placeholder="Je e-mailadres" autocomplete="email"><button type="submit">Inschrijven</button></form>
 </div>
</section>''')

    # ---------- shop ----------
    pagina("shop.html", "Shop | Suismuis Home (concept)", "shop", "shop",
           f'''<div class="paginakop"><div class="wrap"><nav class="kruimel" aria-label="Kruimelpad"><a href="index.html">Home</a><span>/</span><a href="shop.html">Shop</a><span>/</span><span id="kruimel-cat">Alle producten</span></nav>
<h1 id="shop-titel">Alle producten</h1><p>Vazen, kaarsen, kussens, verlichting en linnen in warme, natuurlijke tinten.</p></div></div>
<section style="padding-top:44px"><div class="wrap">
 <div class="shopbalk"><div class="chips" id="chips" role="group" aria-label="Filter op categorie"></div>
  <div style="display:flex;gap:16px;align-items:center"><span class="aantal-res" id="aantal" aria-live="polite"></span><label class="sr" for="sorteer">Sorteren</label>
  <select id="sorteer"><option value="standaard">Aanbevolen</option><option value="laag">Prijs laag – hoog</option><option value="hoog">Prijs hoog – laag</option><option value="naam">Naam A – Z</option></select></div></div>
 <div class="producten" id="shop-grid"></div>
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
  <p style="font-size:13px;margin:14px 0 0;text-align:center">iDEAL · Bancontact · Visa · Mastercard · PayPal</p>
 </aside>
</div></div>''')

    # ---------- afrekenen ----------
    pagina("afrekenen.html", "Afrekenen | Suismuis Home (concept)", "afrekenen", "",
           paginakop("Afrekenen", "", ['<a href="winkelmand.html">Winkelmand</a>', "<span>Afrekenen</span>"]) + '''
<div class="wrap"><div class="mand" id="afreken">
 <form class="form" id="bestel" novalidate>
  <div class="stappen"><b>1. Gegevens</b><span>2. Betalen</span><span>3. Bevestiging</span></div>
  <div class="twee"><label>Voornaam *<input required autocomplete="given-name"></label><label>Achternaam *<input required autocomplete="family-name"></label></div>
  <label>E-mailadres *<input type="email" required autocomplete="email"></label>
  <div class="twee"><label>Postcode *<input required autocomplete="postal-code"></label><label>Huisnummer *<input required></label></div>
  <div class="twee"><label>Straat *<input required autocomplete="address-line1"></label><label>Plaats *<input required autocomplete="address-level2"></label></div>
  <label>Land<select autocomplete="country"><option>Nederland</option><option>België</option></select></label>
  <h2 style="font-size:30px;margin-top:16px">Betaalmethode</h2>
  <div class="betaal" role="radiogroup" aria-label="Betaalmethode">
   <label><input type="radio" name="betaal" checked> iDEAL</label><label><input type="radio" name="betaal"> Bancontact</label><label><input type="radio" name="betaal"> Creditcard</label><label><input type="radio" name="betaal"> PayPal</label>
  </div>
  <label class="check"><input type="checkbox" required> Ik ga akkoord met de <a class="link" href="klantenservice.html#voorwaarden">algemene voorwaarden</a> *</label>
  <p id="fout" role="status" style="color:#8A3B2E;margin:0"></p>
  <button class="knop" type="submit">Bestelling plaatsen</button>
  <p style="font-size:13px;color:var(--mokka)">Concept: er wordt niets echt besteld of betaald.</p>
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
  <p class="noot">Tekst ter illustratie: bij lancering schrijven we samen jouw eigen verhaal.</p>
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
    faq = [("Wanneer is mijn bestelling in huis?", "Binnen 2–4 werkdagen, in Nederland en België. Zodra je pakket onderweg is, krijg je een track-and-tracecode per e-mail."),
           ("Wat kost verzending?", "Verzending kost € 5,95. Vanaf € 75 verzenden we gratis binnen Nederland en België."),
           ("Kan ik mijn bestelling retourneren?", "Ja, je hebt 14 dagen bedenktijd na ontvangst. Gebruik de knop Bestelling herroepen hierboven; je krijgt het aankoopbedrag binnen 14 dagen terug."),
           ("Kan ik een product als cadeau laten inpakken?", "Ja, bij het afrekenen kies je voor cadeauverpakking met een handgeschreven kaartje (+ € 3,95)."),
           ("Hoe kan ik betalen?", "Met iDEAL, Bancontact, Visa, Mastercard en PayPal. Betalen gaat via een beveiligde verbinding."),
           ("Zijn de producten handgemaakt?", "Veel stukken zijn van natuurlijke materialen en deels met de hand gemaakt. Kleine verschillen in kleur en structuur maken elk stuk uniek.")]
    faq_html = "".join(f"<details><summary>{v}</summary><p>{a}</p></details>" for v, a in faq)
    pagina("klantenservice.html", "Klantenservice | Suismuis Home (concept)", "service", "service",
           paginakop("Klantenservice", "We helpen je graag. Hier vind je alles over bestellen, verzenden en retourneren.", ["<span>Klantenservice</span>"]) + f'''
<div class="wrap"><div class="tekst">
 <h2 id="verzenden">Verzenden</h2><ul><li>Je bestelling is binnen 2–4 werkdagen in huis.</li><li>We leveren in Nederland en België.</li><li>Verzendkosten € 5,95, gratis vanaf € 75.</li><li>Je ontvangt een track-and-tracecode per e-mail.</li></ul>
 <h2 id="retour">Retourneren</h2><p>Niet helemaal blij? Je hebt 14 dagen bedenktijd na ontvangst. Stuur het product ongebruikt en in de originele verpakking terug. Meld je retour aan met de knop <a class="link" href="#herroepen">Bestelling herroepen</a>; binnen 14 dagen na ontvangst van je retour storten we het bedrag terug.</p>
 <h2 id="herroepen">Bestelling herroepen</h2><p>Je kunt je bestelling binnen 14 dagen na ontvangst zonder opgaaf van reden herroepen. Vul je gegevens in en druk op de knop; je krijgt direct een ontvangstbevestiging per e-mail.</p>
 <form class="form" data-bevestig="Je herroeping is ontvangen. Je krijgt een bevestiging per e-mail met de retourinstructies." novalidate>
  <div class="twee"><label>Naam *<input required autocomplete="name"></label><label>E-mailadres *<input type="email" required autocomplete="email"></label></div>
  <div class="twee"><label>Ordernummer *<input required></label><label>Datum van ontvangst *<input type="date" required></label></div>
  <label>Welke producten herroep je? (optioneel)<input></label>
  <button class="knop" type="submit">Bestelling herroepen</button>
 </form>
 <details style="margin-top:22px"><summary>Modelformulier voor herroeping</summary><p>Liever per post of e-mail? Gebruik dan dit modelformulier. Aan: Suismuis Home, [adres en e-mailadres volgen bij lancering]. Ik deel u hierbij mede dat ik onze overeenkomst betreffende de verkoop van de volgende goederen herroep: [producten]. Besteld op / ontvangen op: [datum]. Naam en adres: [gegevens]. Datum: [datum].</p></details>
 <h2 id="faq">Veelgestelde vragen</h2>{faq_html}
 <h2 id="contact">Contact</h2><p>Stel je vraag via het formulier. We reageren binnen één werkdag.</p>
 <form class="form" data-bevestig="Dank je wel! We reageren binnen één werkdag." novalidate>
  <div class="twee"><label>Naam *<input required autocomplete="name"></label><label>E-mailadres *<input type="email" required autocomplete="email"></label></div>
  <label>Ordernummer (optioneel)<input></label>
  <label>Onderwerp<select><option>Vraag over een product</option><option>Mijn bestelling</option><option>Retour aanmelden</option><option>Iets anders</option></select></label>
  <label>Bericht *<textarea required></textarea></label>
  <button class="knop" type="submit">Verstuur bericht</button>
 </form>
 <h2 id="voorwaarden">Algemene voorwaarden</h2><p>De algemene voorwaarden stellen we bij de lancering op, afgestemd op Suismuis Home en de Nederlandse regels voor online verkoop (o.a. 14 dagen bedenktijd).</p>
 <h2 id="privacy">Privacy</h2><p>Suismuis Home gebruikt je gegevens alleen om je bestelling te verwerken en, als je dat wilt, om je de nieuwsbrief te sturen. De volledige privacyverklaring volgt bij de lancering.</p>
</div></div>''')

    # ---------- account ----------
    pagina("account.html", "Mijn account | Suismuis Home (concept)", "account", "",
           paginakop("Mijn account", "Bekijk je bestellingen en bewaar je adres voor sneller afrekenen.", ["<span>Mijn account</span>"]) + '''
<div class="wrap"><div class="tekst" style="max-width:520px">
 <div class="tabs" role="tablist"><button role="tab" aria-selected="true" aria-controls="t-in" type="button">Inloggen</button><button role="tab" aria-selected="false" aria-controls="t-nieuw" type="button">Account aanmaken</button></div>
 <form class="form" id="t-in" role="tabpanel" data-bevestig="Concept: inloggen werkt in de echte webshop." novalidate><label>E-mailadres *<input type="email" required autocomplete="email"></label><label>Wachtwoord *<input type="password" required autocomplete="current-password"></label><button class="knop" type="submit">Inloggen</button><a class="link" href="klantenservice.html#contact" style="justify-self:start">Wachtwoord vergeten?</a></form>
 <form class="form" id="t-nieuw" role="tabpanel" hidden data-bevestig="Concept: account aanmaken werkt in de echte webshop." novalidate><label>Naam *<input required autocomplete="name"></label><label>E-mailadres *<input type="email" required autocomplete="email"></label><label>Wachtwoord *<input type="password" required autocomplete="new-password"></label><button class="knop" type="submit">Account aanmaken</button><p style="font-size:14px;color:var(--mokka)">Je kunt ook bestellen zonder account.</p></form>
</div></div>''')

    # ---------- beheer (concept voor Kim) ----------
    pagina("beheer.html", "Beheer | Suismuis Home (concept)", "beheer", "",
           paginakop("Jouw beheeromgeving", "Zo werkt je webshop achter de schermen: jij kiest de producten en je marge, de leverancier verzendt.", ["<span>Beheer</span>"]) + '''
<section style="padding-top:48px"><div class="wrap">
 <h2 style="font-size:40px;margin-bottom:22px">Van betaling tot levering</h2>
 <ol class="route">
  <li><b>Klant bestelt</b>Op jouw webshop, in jouw stijl.</li>
  <li><b>Klant betaalt</b>Het geld komt op jouw rekening, via je betaalprovider.</li>
  <li><b>Automatisch doorgestuurd</b>De bestelling gaat direct naar de leverancier, tegen jouw inkoopprijs.</li>
  <li><b>Leverancier verzendt</b>Rechtstreeks naar je klant, met track-and-trace.</li>
  <li><b>Klant ontvangt</b>Jij houdt het verschil: dat is je marge.</li>
 </ol>
 <p class="noot">De klant ziet alleen Suismuis Home. Jij beheert producten, prijzen en klantcontact; de leverancier doet voorraad en verzending.</p>
</div></section>
<section class="nieuw"><div class="wrap">
 <div class="sectiekop"><div><h2>Producten en marge</h2><p>Pas een verkoopprijs aan en zie direct je winst per verkoop. Inkoop- en verzendprijzen zijn voorbeelden.</p></div></div>
 <div class="kpi"><div><b id="gem-marge"></b><span>Gemiddelde marge</span></div><div><b>16</b><span>Producten in de shop</span></div><div><b>€ 0,29</b><span>Betaalkosten per bestelling (voorbeeld)</span></div></div>
 <div class="tabelwrap"><table class="marge" id="marge-tabel"><thead><tr><th>Product</th><th>Inkoop</th><th>Verzending leverancier</th><th>Verkoopprijs</th><th>Winst per stuk</th><th>Marge</th></tr></thead><tbody></tbody></table></div>
</div></section>
<section><div class="wrap">
 <div class="sectiekop"><div><h2>Laatste bestellingen</h2><p>Elke bestelling volgt automatisch deze stappen. Jij hoeft alleen in te grijpen als er iets afwijkt.</p></div></div>
 <div id="orders"></div>
 <p class="noot">Voorbeeldbestellingen ter illustratie.</p>
</div></section>''')


if __name__ == "__main__":
    bouw()
    print("Suismuis gebouwd in", os.path.abspath(DOEL))
