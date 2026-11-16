"""Bouwt de concept-webshop Atelier Ombre (kunstboutique) in src/concept/atelier-ombre/."""
import os

DOEL = os.path.join(os.path.dirname(__file__), "..", "..", "src", "concept", "atelier-ombre")
CATS = [("schilderijen", "Schilderijen", "w-relief-i", "Originele werken op doek en papier, van verstild wit tot uitgesproken kleur."),
        ("beelden", "Beelden & objecten", "w-danser", "Brons, steen en porselein. Kleine oplages en unica voor kast, sokkel of tafel."),
        ("vondsten", "Vondsten", "w-beer", "Gevonden schatten met een verhaal: studiokeramiek en beelden uit privécollecties.")]
MAKERS = [("ines-vaerman", "Ines Vaerman", "w-wit-ii", "Gent, 1988", "Werkt met gips, kalk en structuurpasta. Haar witte reliëfs veranderen met het licht van de dag: 's ochtends zacht, 's avonds diep en grafisch."),
          ("teo-brakel", "Teo Brakel", "w-beweging", "Rotterdam, 1979", "Schildert in zwart en wit, met grote, snelle gebaren. Elk doek is één beweging, vastgelegd in acryl en houtskool."),
          ("noor-ilhan", "Noor Ilhan", "w-kleur", "Utrecht, 1991", "Kleur als onderwerp. Werkt met dikke lagen olieverf en paletmes, en maakt daarnaast kleine oplages giclée-prints."),
          ("atelier-ruys", "Atelier Ruys", "w-danser", "Antwerpen", "Klein atelier voor brons en steen. Gietwerk in oplages van maximaal acht, elk exemplaar genummerd en gesigneerd.")]
SVG = {
    "zoek": '<svg viewBox="0 0 24 24"><circle cx="11" cy="11" r="7"/><path d="M20 20l-4-4"/></svg>',
    "account": '<svg viewBox="0 0 24 24"><circle cx="12" cy="8" r="4"/><path d="M4 21c1.5-4 4.5-6 8-6s6.5 2 8 6"/></svg>',
    "hart": '<svg viewBox="0 0 24 24"><path d="M12 20s-7.5-4.6-7.5-10A4.3 4.3 0 0 1 12 7.4 4.3 4.3 0 0 1 19.5 10c0 5.4-7.5 10-7.5 10z"/></svg>',
    "mand": '<svg viewBox="0 0 24 24"><path d="M5 8h14l-1 13H6z"/><path d="M9 8V6a3 3 0 0 1 6 0v2"/></svg>',
    "menu": '<svg viewBox="0 0 24 24"><path d="M3 7h18M3 12h18M3 17h18"/></svg>',
}


def kop(actief):
    nav = [("collectie.html", "Galerie", "collectie"), ("huis.html", "Huis &amp; Beeld", "huis"), ("kunstenaars.html", "Kunstenaars", "kunstenaars"), ("over.html", "Over", "over"), ("service.html", "Service", "service")]
    links = "".join(f'<a href="{h}"{" aria-current=\"page\"" if k == actief else ""}>{t}</a>' for h, t, k in nav)
    lade_cats = "".join(f'<a href="collectie.html?cat={c}">{n}</a>' for c, n, _, _ in CATS)
    return f'''<div class="wm" aria-hidden="true"></div>
<a class="sr" href="#inhoud">Naar de inhoud</a>
<div class="balk">Verzekerd verzonden met certificaat van echtheid<span class="balk-extra"> &nbsp;·&nbsp; 14 dagen bedenktijd</span></div>
<header class="kopbalk"><div class="wrap kop">
 <nav aria-label="Hoofdmenu">{links}</nav>
 <button class="ico menuknop" type="button" data-open="lade" aria-label="Menu openen">{SVG["menu"]}</button>
 <a class="logo" href="index.html" aria-label="Atelier Ombre, naar de homepage">Atelier <i>Ombre</i></a>
 <div class="iconen">
  <button class="ico" type="button" data-open="zoek" aria-label="Zoeken">{SVG["zoek"]}</button>
  <a class="ico" href="favorieten.html" aria-label="Favorieten">{SVG["hart"]}<span class="teller" data-teller="favs"></span></a>
  <a class="ico" href="winkelmand.html" aria-label="Winkelmand">{SVG["mand"]}<span class="teller" data-teller="mand"></span></a>
 </div>
</div></header>
<div class="lade" id="lade" role="dialog" aria-modal="true" aria-label="Menu"><div class="doek" data-sluit></div><div class="paneel">
 <button class="sluit" type="button" data-sluit aria-label="Menu sluiten">×</button>
 <a href="index.html">Home</a><a href="collectie.html">Galerie</a><div class="sub">{lade_cats}</div><a href="huis.html">Huis &amp; Beeld</a>
 <a href="kunstenaars.html">Kunstenaars</a><a href="over.html">Over</a><a href="service.html">Service</a><a href="favorieten.html">Favorieten</a>
</div></div>
<div class="zoek" id="zoek" role="dialog" aria-modal="true" aria-label="Zoeken"><div class="wrap">
 <div style="display:flex;justify-content:space-between;align-items:center"><span class="klein">Zoek in de collectie</span><button class="sluit" type="button" data-sluit aria-label="Zoeken sluiten">×</button></div>
 <label class="sr" for="zoekveld">Zoek een werk of kunstenaar</label><input id="zoekveld" type="search" placeholder="Kunstenaar, titel of materiaal" autocomplete="off">
 <p class="leeg" id="zoekleeg">Probeer bijvoorbeeld brons, wit, Vaerman of keramiek.</p><div class="werken" id="zoekres"></div>
</div></div>'''


def voet():
    cats = "".join(f'<li><a href="collectie.html?cat={c}">{n}</a></li>' for c, n, _, _ in CATS)
    return f'''<footer><div class="wrap">
 <div class="voet">
  <div><span class="logo">Atelier <i>Ombre</i></span><p style="margin-top:14px;max-width:320px">Abstracte kunst, beelden en gevonden schatten. Zorgvuldig gekozen, eerlijk geprijsd.</p><div class="betaalmerken" aria-label="Betaalmethoden"><span>Visa</span><span>Mastercard</span><span>Amex</span><span>Apple Pay</span><span>Google Pay</span><span>iDEAL</span></div></div>
  <div><h4>Collectie</h4><ul>{cats}<li><a href="huis.html">Huis &amp; Beeld</a></li><li><a href="kunstenaars.html">Kunstenaars</a></li></ul></div>
  <div><h4>Service</h4><ul><li><a href="service.html#verzending">Verzending en ophangen</a></li><li><a href="service.html#echtheid">Certificaat van echtheid</a></li><li><a href="service.html#herroepen">Bestelling herroepen</a></li><li><a href="service.html#advies">Kunstadvies</a></li><li><a href="service.html#contact">Contact</a></li></ul></div>
  <div><h4>Atelier Ombre</h4><ul><li><a href="over.html">Over ons</a></li><li><a href="over.html#aanmelden">Kunstenaar aanmelden</a></li><li><a href="index.html#brief">Nieuwsbrief</a></li><li><a href="beheer.html">Beheer</a></li></ul></div>
 </div>
 <div class="onder"><span>© 2026 Atelier Ombre</span><span><a href="service.html#voorwaarden">Algemene voorwaarden</a> · <a href="service.html#privacy">Privacy</a></span></div>
</div></footer>
<div class="concept">Concept door <a href="https://collensgroup.com">Collens Group</a> · voorbeeldwerken en -kunstenaars</div>
<div class="toast" id="toast" role="status" aria-live="polite"></div>'''


def pagina(bestand, titel, sleutel, actief, inhoud, beschrijving="Abstracte schilderijen, beelden en gevonden schatten, van betaalbaar tot verzamelwaardig."):
    html = f'''<!DOCTYPE html>
<html lang="nl">
<head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{titel}</title>
<link rel="icon" href="assets/favicon.svg" type="image/svg+xml">
<meta property="og:title" content="{titel}"><meta property="og:description" content="{beschrijving}"><meta property="og:image" content="https://collensgroup.com/concept/atelier-ombre/img/og.jpg"><meta property="og:type" content="website"><meta name="twitter:card" content="summary_large_image">
<meta name="robots" content="noindex,nofollow,noarchive"><meta name="description" content="{beschrijving}">
<meta name="generator" content="Collens Group concept cgc-atelierombre"><meta name="copyright" content="Collens Group">
<meta name="theme-color" content="#F2F1ED">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Bodoni+Moda:ital,opsz,wght@0,6..96,400;1,6..96,400&family=Instrument+Sans:wght@400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/ao.css">
</head>
<body data-pagina="{sleutel}">
{kop(actief)}
<main id="inhoud">
{inhoud}
</main>
{voet()}
<script src="assets/ao.js" defer></script>
</body>
</html>
'''
    with open(os.path.join(DOEL, bestand), "w", encoding="utf-8") as f:
        f.write(html)


def paginakop(titel, tekst, kruimel):
    k = '<a href="index.html">Home</a><span>/</span>' + "<span>/</span>".join(kruimel)
    return f'<div class="paginakop"><div class="wrap"><nav class="kruimel" aria-label="Kruimelpad">{k}</nav><h1>{titel}</h1>{f"<p>{tekst}</p>" if tekst else ""}</div></div>'


BELOFTE = '''<div class="belofte"><div class="wrap"><ul>
 <li><b>Certificaat van echtheid</b>Bij elk origineel en elke oplage, gesigneerd door kunstenaar of taxateur.</li>
 <li><b>Verzekerd thuisbezorgd</b>In museumverpakking. Grote werken met een kunstkoerier.</li>
 <li><b>Eerst aan je muur zien</b>Bekijk elk schilderij op ware grootte boven een bank.</li>
 <li><b>14 dagen bedenktijd</b>Past het toch niet? Retour aanmelden kan met één knop.</li>
</ul></div></div>'''


def bouw():
    os.makedirs(DOEL, exist_ok=True)
    werelden = "".join(f'<a class="wereld" href="collectie.html?cat={c}"><div class="beeld"><img src="img/{img}.jpg" alt="" loading="lazy" width="1400" height="1750"></div><h3>{n}</h3><p>{t}</p></a>' for c, n, img, t in CATS)

    # ---------- home ----------
    pagina("index.html", "Atelier Ombre – abstracte kunst, beelden en vondsten (concept)", "home", "home", f'''
<section class="nacht" id="nacht" aria-label="Atelier Ombre">
 <div class="nacht-werken" aria-hidden="true">
  <img class="nw nw1" src="img/w-beweging.jpg" alt="" width="1600" height="1600" fetchpriority="high">
  <img class="nw nw2" src="img/w-danser.jpg" alt="" width="1400" height="1750">
  <img class="nw nw3" src="img/w-relief-i.jpg" alt="" width="1400" height="1750">
  <img class="nw nw4" src="img/w-kleur.jpg" alt="" width="1600" height="1200">
  <img class="nw nw5" src="img/w-beer.jpg" alt="" width="1400" height="1750">
 </div>
 <div class="nacht-licht" aria-hidden="true"></div>
 <div class="nacht-tekst wrap">
  <p class="nacht-boven">Kunst, beelden en vondsten</p>
  <h1>Atelier<span>Ombre</span></h1>
  <p class="nacht-onder">Alles begint in de schaduw. Beweeg het licht en ontdek wat er hangt.</p>
  <div class="knoppen"><a class="knop wit" href="collectie.html">Naar de galerie</a><a class="knop lijn" href="huis.html">Huis &amp; Beeld</a></div>
 </div>
 <p class="nacht-hint" aria-hidden="true">Beweeg je muis of vinger over de zaal</p>
</section>
<section class="strook" aria-label="Uitgelicht in de galerie">
 <div class="wrap strook-kop"><h2>Uitgelicht</h2><p>Schuif door de zaal</p></div>
 <div class="strook-baan" id="strook" tabindex="0" aria-label="Uitgelichte werken, horizontaal scrollbaar"></div>
</section>
<section><div class="wrap">
 <div class="sectiekop"><div><h2>Twee afdelingen</h2><p>Originele kunst om te verzamelen, en design-beelden om meteen mee te leven.</p></div></div>
 <div class="afdelingen">
  <a class="afdeling" href="collectie.html"><div class="beeld"><img src="img/s-galerie.jpg" alt="Galeriezaal met keramiek en een groot doek" loading="lazy" width="2000" height="1333"></div><div><h3>Galerie</h3><p>Originele schilderijen, beelden in kleine oplage en vondsten. Altijd met certificaat.</p><span class="link">Originelen vanaf € 165</span></div></a>
  <a class="afdeling" href="huis.html"><div class="beeld"><img src="img/s-interieur.jpg" alt="Abstracte wandobjecten aan een grijze stucmuur" loading="lazy" width="1400" height="1750"></div><div><h3>Huis &amp; Beeld</h3><p>Design-beelden en wandobjecten van Nederlandse ontwerpmerken, direct uit hun magazijn.</p><span class="link">Vanaf € 24,95</span></div></a>
 </div>
</div></section>
<section><div class="wrap">
 <div class="sectiekop"><div><h2>De galerie in drie werelden</h2><p>Van verstilde reliëfs tot beelden en vondsten met een verleden.</p></div><a class="link" href="collectie.html">Naar de galerie</a></div>
 <div class="werelden">{werelden}</div>
</div></section>
<section style="background:var(--wit)"><div class="wrap">
 <div class="sectiekop"><div><h2>Nieuw in de collectie</h2><p>Deze maand toegevoegd. Unica gaan maar één keer weg.</p></div><a class="link" href="collectie.html">Alle werken</a></div>
 <div class="werken" id="nieuw-grid"></div>
</div></section>
{BELOFTE}
<section id="prijs"><div class="wrap">
 <div class="sectiekop"><div><h2>Kunst voor elk budget</h2><p>Goede kunst hoeft niet onbereikbaar te zijn. Begin met een oplage of vondst, of kies een origineel om te houden.</p></div></div>
 <div class="prijsband">
  <a href="collectie.html?prijs=1"><b>Tot € 350</b><span>Oplages, porselein en kleine vondsten</span></a>
  <a href="collectie.html?prijs=2"><b>€ 350 – 1.500</b><span>Originelen en beelden in kleine oplage</span></a>
  <a href="collectie.html?prijs=3"><b>Vanaf € 1.500</b><span>Grote doeken en verzamelstukken</span></a>
 </div>
</div></section>
<section class="statement"><div class="wrap">
 <img src="img/s-atelier.jpg" alt="Beeldhouwer aan het werk in een licht atelier met witte reliëfs aan de muur" loading="lazy" width="2000" height="1333">
 <div><h2>Rechtstreeks uit het atelier</h2>
  <p>We werken met een kleine kring kunstenaars en ateliers, en zoeken daarnaast zelf naar vondsten op veilingen en in privécollecties. Wat we niet zelf zouden ophangen, nemen we niet op.</p>
  <a class="knop" href="kunstenaars.html">Ontmoet de kunstenaars</a></div>
</div></section>
<section><div class="wrap">
 <div class="sectiekop"><div><h2>Twijfel je over formaat of plek?</h2><p>Stuur een foto van je muur en we adviseren gratis welke werken passen, inclusief formaat en lijst.</p></div><a class="link" href="service.html#advies">Vraag kunstadvies</a></div>
 <div class="werken" id="advies-grid"></div>
</div></section>
<section class="brief" id="brief" style="padding:0">
 <img src="img/s-interieur.jpg" alt="Twee abstracte werken in zwart en wit aan een grijze stucmuur" loading="lazy" width="1400" height="1750">
 <div class="brief-tekst"><h2>Als eerste de nieuwe werken zien</h2>
  <p style="margin-top:14px">Eén keer per maand: nieuwe werken, een kunstenaar uitgelicht en een vondst vooraf. Afmelden kan altijd.</p>
  <form class="inline" data-bevestig="Dank je wel. Je ontvangt de eerstvolgende nieuwsbrief." novalidate><label for="mail" class="sr">E-mailadres</label><input id="mail" type="email" required placeholder="Je e-mailadres" autocomplete="email"><button type="submit">Inschrijven</button></form>
 </div>
</section>''')

    # ---------- collectie ----------
    pagina("collectie.html", "Collectie | Atelier Ombre (concept)", "collectie", "collectie",
           '''<div class="paginakop"><div class="wrap"><nav class="kruimel" aria-label="Kruimelpad"><a href="index.html">Home</a><span>/</span><a href="collectie.html">Collectie</a><span>/</span><span id="kruimel-cat">Alle werken</span></nav>
<h1 id="col-titel">Alle werken</h1><p id="col-tekst">Schilderijen, beelden en vondsten. Filter op wereld, prijs of kunstenaar.</p></div></div>
<section style="padding-top:44px"><div class="wrap">
 <div class="shopbalk"><div class="chips" id="chips" role="group" aria-label="Filter op wereld"></div>
  <div class="filters"><span class="aantal-res" id="aantal" aria-live="polite"></span>
   <label class="sr" for="prijsfilter">Prijs</label><select id="prijsfilter"><option value="0">Alle prijzen</option><option value="1">Tot € 350</option><option value="2">€ 350 – 1.500</option><option value="3">Vanaf € 1.500</option></select>
   <label class="sr" for="makerfilter">Kunstenaar</label><select id="makerfilter"><option value="">Alle kunstenaars</option></select>
   <label class="sr" for="sorteer">Sorteren</label><select id="sorteer"><option value="standaard">Uitgelicht</option><option value="laag">Prijs laag – hoog</option><option value="hoog">Prijs hoog – laag</option><option value="groot">Formaat groot – klein</option></select></div></div>
 <div class="werken" id="col-grid"></div>
 <div id="col-leeg" hidden><p class="leeg">Geen werken met deze combinatie. Probeer een andere prijs of kunstenaar.</p><button class="knop licht" type="button" id="wis">Filters wissen</button></div>
 <p class="noot">Voorbeeldwerken, voorbeeldkunstenaars en voorbeeldprijzen. Bij lancering komen hier de echte werken.</p>
</div></section>''' + BELOFTE)

    # ---------- werk ----------
    pagina("werk.html", "Werk | Atelier Ombre (concept)", "werk", "collectie",
           '''<div class="wrap"><nav class="kruimel" aria-label="Kruimelpad" style="margin-top:28px"><a href="index.html">Home</a><span>/</span><a href="collectie.html">Collectie</a><span>/</span><span id="kruimel-werk"></span></nav><div class="detail" id="detail"></div></div>
<section style="background:var(--wit)"><div class="wrap"><div class="sectiekop"><h2>Past hier ook bij</h2><a class="link" href="collectie.html">Alle werken</a></div><div class="werken" id="gerelateerd"></div></div></section>''')

    # ---------- kunstenaars ----------
    makers = "".join(f'''<article class="maker" id="{s}"><div class="beeld"><img src="img/{img}.jpg" alt="" loading="lazy" width="1400" height="1750"></div>
<div><h2>{n}</h2><p class="klein">{plaats}</p><p>{bio}</p><p class="klein" data-telling="{s}"></p><a class="link" href="collectie.html?maker={s}">Bekijk de werken</a></div></article>''' for s, n, img, plaats, bio in MAKERS)
    pagina("kunstenaars.html", "Kunstenaars | Atelier Ombre (concept)", "kunstenaars", "kunstenaars",
           paginakop("Kunstenaars", "Een kleine kring makers die we persoonlijk kennen. Elk werk komt rechtstreeks uit hun atelier.", ["<span>Kunstenaars</span>"]) +
           f'<section style="padding-top:48px"><div class="wrap"><div class="makers">{makers}</div><p class="noot">Voorbeeldkunstenaars ter illustratie. Bij lancering stellen we de echte kunstenaars voor, met hun eigen tekst en portret.</p></div></section>')

    # ---------- over ----------
    pagina("over.html", "Over | Atelier Ombre (concept)", "over", "over",
           paginakop("Over Atelier Ombre", "Kunst kopen moet even vanzelfsprekend voelen als een goed boek uitkiezen. Zonder drempel, wel met kennis.", ["<span>Over</span>"]) + '''
<div class="wrap twee-kol">
 <img src="img/s-galerie.jpg" alt="Lange galeriezaal met open kasten vol keramiek en een groot doek aan de achterwand" loading="lazy" width="2000" height="1333" style="aspect-ratio:3/2">
 <div><h2 style="margin-bottom:18px">Van ontdekking tot verzamelstuk</h2>
  <p>Atelier Ombre brengt drie werelden samen: abstracte schilderijen van levende kunstenaars, beelden in kleine oplages en vondsten die we zelf opsporen op veilingen, in ateliers en bij verzamelaars.</p>
  <p>We kiezen met een strenge blik en prijzen eerlijk. Bij elk werk vertellen we wie het maakte, waarvan het gemaakt is en waarom we het mooi vinden.</p>
  <p class="noot">Tekst ter illustratie: bij lancering schrijven we het echte verhaal.</p></div>
</div>
<section style="padding-top:24px"><div class="wrap">
 <h2 style="margin-bottom:32px">Zo werkt het</h2>
 <ol class="stappen-route">
  <li><b>Je kiest een werk</b>Bekijk het eerst op ware grootte aan de muur.</li>
  <li><b>Je betaalt veilig</b>Met creditcard, Apple Pay, Google Pay of iDEAL.</li>
  <li><b>Het atelier pakt in</b>In museumverpakking, met certificaat.</li>
  <li><b>Verzekerd onderweg</b>Met track-and-trace of kunstkoerier.</li>
  <li><b>Aan je muur</b>Met ophangsysteem en 14 dagen bedenktijd.</li>
 </ol>
</div></section>
<section style="background:var(--wit)" id="aanmelden"><div class="wrap"><div class="tekst" style="padding:0">
 <h2>Kunstenaar aanmelden</h2>
 <p>Maak je abstract werk, beelden of keramiek en zoek je een plek? Stuur een korte introductie en een link naar je werk. We reageren binnen twee weken.</p>
 <form class="form" data-bevestig="Dank je wel. We bekijken je werk en reageren binnen twee weken." novalidate>
  <div class="twee"><label>Naam *<input required autocomplete="name"></label><label>E-mailadres *<input type="email" required autocomplete="email"></label></div>
  <div class="twee"><label>Discipline<select><option>Schilderkunst</option><option>Beeldhouwkunst</option><option>Keramiek</option><option>Werk op papier</option><option>Anders</option></select></label><label>Website of Instagram *<input required></label></div>
  <label>Over je werk<textarea></textarea></label>
  <button class="knop" type="submit">Aanmelding versturen</button>
 </form>
</div></div></section>''')

    # ---------- service ----------
    faq = [("Hoe weet ik of een werk echt is?", "Bij elk werk krijg je een certificaat van echtheid met titel, maker, jaar, materiaal en formaat, gesigneerd door de kunstenaar. Vondsten krijgen een beschrijving van herkomst en staat."),
           ("Hoe groot moet een werk boven mijn bank zijn?", "Een vuistregel: ongeveer twee derde van de breedte van de bank, met 20 tot 25 cm ruimte erboven. Gebruik de knop Aan de muur bij elk schilderij om het op ware grootte te zien."),
           ("Kan ik een werk reserveren?", "Ja, je kunt een werk 48 uur kosteloos reserveren via de knop op de werkpagina. Zo kun je rustig meten of overleggen."),
           ("Kan ik in termijnen betalen?", "Voor werken vanaf € 1.000 kun je in drie termijnen betalen zonder rente. Het werk wordt verzonden na de laatste termijn."),
           ("Leveren jullie ook buiten Nederland en België?", "Binnen de EU leveren we op aanvraag. Neem contact op voor een prijs voor verzekerd transport.")]
    faq_html = "".join(f"<details><summary>{v}</summary><p>{a}</p></details>" for v, a in faq)
    pagina("service.html", "Service | Atelier Ombre (concept)", "service", "service",
           paginakop("Service", "Alles over verzending, echtheid, retourneren en advies.", ["<span>Service</span>"]) + f'''
<div class="wrap"><div class="tekst">
 <h2 id="verzending">Verzending en ophangen</h2><ul><li>Kleine werken en objecten: verzekerd verzonden binnen 3–5 werkdagen, met track-and-trace.</li><li>Grote doeken en beelden: bezorgd door een kunstkoerier, op afspraak.</li><li>Gratis verzekerde verzending vanaf € 250, daaronder € 14,95.</li><li>Schilderijen worden geleverd met ophangsysteem.</li></ul>
 <h2 id="echtheid">Certificaat van echtheid</h2><p>Elk origineel en elke oplage wordt geleverd met een certificaat van echtheid. Oplages zijn genummerd en gesigneerd. Bij vondsten beschrijven we herkomst, periode en staat zo nauwkeurig mogelijk.</p>
 <h2 id="herroepen">Bestelling herroepen</h2><p>Je hebt 14 dagen bedenktijd na ontvangst, zonder opgaaf van reden. Vul je gegevens in en druk op de knop; je krijgt direct een ontvangstbevestiging per e-mail met de retourinstructies. Het aankoopbedrag krijg je binnen 14 dagen terug.</p>
 <form class="form" data-bevestig="Je herroeping is ontvangen. Je krijgt een bevestiging per e-mail met de retourinstructies." novalidate>
  <div class="twee"><label>Naam *<input required autocomplete="name"></label><label>E-mailadres *<input type="email" required autocomplete="email"></label></div>
  <div class="twee"><label>Ordernummer *<input required></label><label>Datum van ontvangst *<input type="date" required></label></div>
  <label>Welk werk herroep je? (optioneel)<input></label>
  <button class="knop" type="submit">Bestelling herroepen</button>
 </form>
 <details style="margin-top:22px"><summary>Modelformulier voor herroeping</summary><p>Liever per post of e-mail? Gebruik dan dit modelformulier. Aan: Atelier Ombre, [adres en e-mailadres volgen bij lancering]. Ik deel u hierbij mede dat ik onze overeenkomst betreffende de verkoop van de volgende goederen herroep: [werk]. Besteld op / ontvangen op: [datum]. Naam en adres: [gegevens]. Datum: [datum].</p></details>
 <h2 id="advies">Kunstadvies</h2><p>Stuur een foto van je muur of ruimte, met de breedte erbij. We stellen binnen twee werkdagen een kleine selectie voor, met formaat en lijstadvies. Gratis en vrijblijvend.</p>
 <form class="form" data-bevestig="Dank je wel. Je ontvangt binnen twee werkdagen ons advies." novalidate>
  <div class="twee"><label>Naam *<input required autocomplete="name"></label><label>E-mailadres *<input type="email" required autocomplete="email"></label></div>
  <div class="twee"><label>Breedte van de muur (cm)<input inputmode="numeric"></label><label>Budget<select><option>Tot € 350</option><option>€ 350 – 1.500</option><option>Vanaf € 1.500</option><option>Weet ik nog niet</option></select></label></div>
  <label>Foto van je muur<input type="file" accept="image/*"></label>
  <label>Wat zoek je?<textarea placeholder="Bijvoorbeeld: iets rustigs boven de bank, veel wit en zand in huis."></textarea></label>
  <button class="knop" type="submit">Advies aanvragen</button>
 </form>
 <h2 id="faq">Veelgestelde vragen</h2>{faq_html}
 <h2 id="contact">Contact</h2><p>Stel je vraag via het formulier. We reageren binnen één werkdag.</p>
 <form class="form" data-bevestig="Dank je wel. We reageren binnen één werkdag." novalidate>
  <div class="twee"><label>Naam *<input required autocomplete="name"></label><label>E-mailadres *<input type="email" required autocomplete="email"></label></div>
  <label>Onderwerp<select><option>Vraag over een werk</option><option>Mijn bestelling</option><option>Retour aanmelden</option><option>Iets anders</option></select></label>
  <label>Bericht *<textarea required></textarea></label>
  <button class="knop" type="submit">Verstuur bericht</button>
 </form>
 <h2 id="voorwaarden">Algemene voorwaarden</h2><p>De algemene voorwaarden stellen we bij de lancering op, afgestemd op de Nederlandse regels voor online verkoop, waaronder 14 dagen bedenktijd.</p>
 <h2 id="privacy">Privacy</h2><p>Atelier Ombre gebruikt je gegevens alleen om je bestelling te verwerken en, als je dat wilt, om je de nieuwsbrief te sturen. De volledige privacyverklaring volgt bij de lancering.</p>
</div></div>''')

    # ---------- winkelmand ----------
    pagina("winkelmand.html", "Winkelmand | Atelier Ombre (concept)", "mand", "",
           paginakop("Winkelmand", "", ["<span>Winkelmand</span>"]) + '''
<div class="wrap"><div class="mand" id="mand">
 <div><div id="mand-regels"></div><a class="link" href="collectie.html" style="display:inline-block;margin-top:22px">Verder kijken</a></div>
 <aside class="samenvatting" aria-label="Overzicht">
  <h2 style="font-size:30px;margin-bottom:12px">Overzicht</h2>
  <div class="rij"><span>Subtotaal</span><span id="sub"></span></div>
  <div class="rij"><span>Verzekerde verzending</span><span id="verz"></span></div>
  <div class="rij totaal"><span>Totaal</span><span id="tot"></span></div>
  <p class="klein" id="termijn" hidden style="margin:8px 0 0">Of in 3 termijnen zonder rente.</p>
  <a class="knop breed" href="afrekenen.html" style="margin-top:18px">Veilig afrekenen</a>
  <p class="klein" style="margin:14px 0 0;text-align:center">Creditcard · Apple Pay · Google Pay · iDEAL</p>
 </aside>
</div></div>''')

    # ---------- afrekenen ----------
    pagina("afrekenen.html", "Afrekenen | Atelier Ombre (concept)", "afrekenen", "",
           paginakop("Afrekenen", "", ['<a href="winkelmand.html">Winkelmand</a>', "<span>Afrekenen</span>"]) + '''
<div class="wrap"><div class="mand" id="afreken">
 <form class="form" id="bestel" novalidate>
  <div class="stappen"><b>1. Gegevens</b><span>2. Betalen</span><span>3. Bevestiging</span></div>
  <div class="twee"><label>Voornaam *<input name="voornaam" required autocomplete="given-name"></label><label>Achternaam *<input name="achternaam" required autocomplete="family-name"></label></div>
  <div class="twee"><label>E-mailadres *<input name="email" type="email" required autocomplete="email"></label><label>Telefoon (voor de bezorger) *<input name="tel" type="tel" required autocomplete="tel"></label></div>
  <div class="twee"><label>Postcode *<input name="postcode" required autocomplete="postal-code"></label><label>Huisnummer *<input name="huisnummer" required></label></div>
  <div class="twee"><label>Straat *<input name="straat" required autocomplete="address-line1"></label><label>Plaats *<input name="plaats" required autocomplete="address-level2"></label></div>
  <label>Land<select name="land" autocomplete="country"><option>Nederland</option><option>België</option></select></label>
  <h2 style="font-size:30px;margin-top:16px">Betaalmethode</h2>
  <div class="betaal" role="radiogroup" aria-label="Betaalmethode">
   <label><input type="radio" name="betaal" value="Creditcard" checked><span><b>Creditcard</b><small>Visa, Mastercard, American Express</small></span></label>
   <label><input type="radio" name="betaal" value="Apple Pay of Google Pay"><span><b>Apple Pay of Google Pay</b><small>Betalen met je telefoon</small></span></label>
   <label><input type="radio" name="betaal" value="iDEAL"><span><b>iDEAL</b><small>Via je eigen bank</small></span></label>
  </div>
  <p class="veilig"><svg viewBox="0 0 24 24" aria-hidden="true"><rect x="5" y="11" width="14" height="10" rx="2"/><path d="M8 11V8a4 4 0 0 1 8 0v3"/></svg>Je rondt de betaling af op de beveiligde betaalpagina van Stripe, met 3D Secure. Wij zien en bewaren je kaartgegevens nooit.</p>
  <label class="check"><input type="checkbox" required><span>Ik ga akkoord met de <a class="link" href="service.html#voorwaarden">algemene voorwaarden</a> *</span></label>
  <p id="fout" role="status" style="color:var(--ossenbloed);margin:0"></p>
  <button class="knop" type="submit">Doorgaan naar veilig betalen</button>
  <p class="klein">Concept: dit is een testbestelling. Er wordt niet betaald en er wordt niets verzonden.</p>
 </form>
 <aside class="samenvatting" aria-label="Je bestelling"><h2 style="font-size:30px;margin-bottom:12px">Je bestelling</h2><div id="overzicht"></div></aside>
</div></div>''')

    # ---------- favorieten ----------
    pagina("favorieten.html", "Favorieten | Atelier Ombre (concept)", "favorieten", "",
           paginakop("Favorieten", "Bewaar werken die je raken en kom later terug.", ["<span>Favorieten</span>"]) + '''
<section style="padding-top:48px"><div class="wrap"><div id="fav-leeg"><p>Je hebt nog geen favorieten. Tik op het hartje bij een werk om het te bewaren.</p><a class="knop" href="collectie.html">Naar de collectie</a></div>
<div class="werken" id="fav-grid"></div></div></section>''')

    # ---------- huis & beeld ----------
    pagina("huis.html", "Huis & Beeld | Atelier Ombre (concept)", "huis", "huis",
           paginakop("Huis &amp; Beeld", "Design-beelden en wandobjecten van Nederlandse ontwerpmerken. Goede kwaliteit voor een normale prijs, rechtstreeks uit het magazijn van de maker.", ["<span>Huis &amp; Beeld</span>"]) + '''
<section style="padding-top:44px"><div class="wrap">
 <div class="shopbalk"><div class="chips" id="h-chips" role="group" aria-label="Filter">
  <button class="chip" type="button" data-hcat="" aria-pressed="true">Alles</button><button class="chip" type="button" data-hcat="beelden" aria-pressed="false">Beelden</button><button class="chip" type="button" data-hcat="wand" aria-pressed="false">Wandobjecten</button></div>
  <div class="filters"><span class="aantal-res" id="h-aantal" aria-live="polite"></span><label class="sr" for="h-sorteer">Sorteren</label><select id="h-sorteer"><option value="standaard">Uitgelicht</option><option value="laag">Prijs laag – hoog</option><option value="hoog">Prijs hoog – laag</option><option value="groot">Formaat groot – klein</option></select></div></div>
 <p class="schaaluitleg"><span class="a4" aria-hidden="true"></span>Elk product staat op schaal naast een A4-vel (30 cm), zodat je direct ziet hoe groot het is.</p>
 <div class="dingen" id="h-grid"></div>
 <p class="noot">Echte producten van Richmond Interiors, PTMD, Present Time en De Wanddecoratie. Prijzen zijn een voorstel; de definitieve prijs volgt zodra de inkoopprijs bekend is. Productfoto's van de merken komen erbij na aansluiting als verkooppunt.</p>
</div></section>
<section class="belofte-huis"><div class="wrap"><ul>
 <li><b>Ontwerpmerken uit Nederland</b>Eigen ontwerpen, geen namaak.</li>
 <li><b>Snel in huis</b>Rechtstreeks uit het magazijn van de maker.</li>
 <li><b>14 dagen bedenktijd</b>Retour aanmelden met één knop.</li>
</ul></div></section>''')

    # ---------- bestelling (volgpagina) ----------
    pagina("bestelling.html", "Je bestelling | Atelier Ombre (concept)", "bestelling", "",
           paginakop("Je bestelling", "", ["<span>Bestelling</span>"]) + '''
<div class="wrap"><div class="tekst" id="volg" aria-live="polite"><p class="leeg">Bestelling laden…</p></div></div>''')

    # ---------- beheer ----------
    pagina("beheer.html", "Beheer | Atelier Ombre (concept)", "beheer", "",
           paginakop("Beheer", "Zo werkt Atelier Ombre achter de schermen: drie inkoopmodellen, één webshop.", ["<span>Beheer</span>"]) + '''
<section style="padding-top:48px"><div class="wrap">
 <h2 style="margin-bottom:22px">Drie manieren van inkopen</h2>
 <div class="modellen">
  <div><h3>Consignatie</h3><p>De kunstenaar levert het werk in commissie. Bij verkoop houdt Atelier Ombre een commissie in (voorbeeld 40 %), de kunstenaar krijgt de rest. Geen voorraadrisico.</p></div>
  <div><h3>Print op bestelling</h3><p>Genummerde giclée-prints worden pas gedrukt na een bestelling en rechtstreeks door de drukker verzonden. Jij betaalt alleen druk en verzending.</p></div>
  <div><h3>Eigen inkoop</h3><p>Vondsten koop je zelf in op veilingen en bij verzamelaars. Hogere marge, wel eigen voorraad en opslag.</p></div>
 </div>
</div></section>
<section style="background:var(--wit)"><div class="wrap">
 <div class="sectiekop"><div><h2>Werken en marge</h2><p>Pas een verkoopprijs aan en zie direct de opbrengst per verkoop. Commissies, inkoop- en verzendprijzen zijn voorbeelden.</p></div></div>
 <div class="kpi"><div><b id="k-werken"></b><span>Werken in de collectie</span></div><div><b id="k-waarde"></b><span>Totale verkoopwaarde</span></div><div><b id="k-marge"></b><span>Gemiddelde marge</span></div><div><b id="k-risico"></b><span>Eigen voorraad (ingekocht)</span></div></div>
 <div class="tabelwrap"><table class="marge" id="marge-tabel"><thead><tr><th>Werk</th><th>Model</th><th>Kosten</th><th>Verzending</th><th>Verkoopprijs</th><th>Opbrengst</th><th>Marge</th></tr></thead><tbody></tbody></table></div>
 <p class="noot">Let op bij de echte start: btw-regeling voor kunst (margeregeling), volgrecht bij doorverkoop van werk van levende kunstenaars en verzekering van voorraad. Dit stemmen we af met een boekhouder.</p>
</div></section>
<section><div class="wrap">
 <div class="sectiekop"><div><h2>Huis &amp; Beeld: leveranciers</h2><p>Waar elk product vandaan komt en hoe we het inkopen. Alleen merken met eigen ontwerpen.</p></div></div>
 <div class="modellen">
  <div><h3>PTMD</h3><p>Nederlands merk met eigen ontwerpstudio. Levert via Droppery rechtstreeks aan de klant van de webshop. Droppery begint bij circa $ 46 per maand.</p></div>
  <div><h3>Richmond Interiors</h3><p>Groothandel uit Heerhugowaard met eigen collectie. Verkoopt alleen via dealers: dealeraccount aanvragen en vragen of zij of Droppery rechtstreeks leveren.</p></div>
  <div><h3>Present Time en De Wanddecoratie</h3><p>Present Time: design-objecten, groothandel navragen. De Wanddecoratie: Nederlandse maker van canvas met FSC/PEFC-hout, samenwerking navragen.</p></div>
 </div>
 <div class="tabelwrap" style="margin-top:28px"><table class="marge" id="huis-tabel"><thead><tr><th>Product</th><th>Merk</th><th>Onze prijs</th><th>Inkoop via</th></tr></thead><tbody></tbody></table></div>
 <p class="noot">Inkoopprijzen krijg je pas met een account bij de leverancier. Daarom staat de marge hier nog niet; die rekenen we uit zodra de prijslijsten binnen zijn.</p>
</div></section>
<section id="bestellingen"><div class="wrap">
 <div class="sectiekop"><div><h2>Bestellingen</h2><p>De bestelbalie: elke bestelling met alles wat je nodig hebt om hem bij de verkoper te plaatsen, met het adres van de klant als afleveradres.</p></div></div>
 <ol class="stappen-route" style="margin-bottom:40px">
  <li><b>Klant bestelt</b>Op Atelier Ombre, tegen jouw prijs met marge.</li>
  <li><b>Klant betaalt aan Ombre</b>Creditcard, Apple Pay, Google Pay of iDEAL via Stripe.</li>
  <li><b>Ombre bestelt bij de verkoper</b>Met het adres van de klant als afleveradres.</li>
  <li><b>Klant krijgt bevestiging</b>Met een volglink naar de status van de bestelling.</li>
  <li><b>Verkoper verzendt</b>Rechtstreeks naar de klant; jij zet de track-and-trace erbij.</li>
 </ol>
 <div id="balie" aria-live="polite"></div>
 <p class="noot">Fase nu: testbestellingen vanuit dit concept. Zodra de KvK er is, koppelen we echte betalingen (Stripe) en bevestigingsmails.</p>
</div></div></section>''')


if __name__ == "__main__":
    bouw()
    print("Atelier Ombre gebouwd in", os.path.abspath(DOEL))
