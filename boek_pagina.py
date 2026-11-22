"""Boekenpagina's (reeks Claude AI Compleet).
- boeken.html: overzicht met omslagen, korte omschrijving (bewust weinig inhoud prijsgegeven) en links naar de webshop.
- boek-claude-voor-beginners.html: deel 1, herziene editie november 2026.
Feiten deel 1 (Gumroad, bijgewerkt 22-11-2026): €29,99, 106 pagina's, PDF + EPUB, 18 hoofdstukken, 17 figuren, 40 vragen, 7-dagenplan.
Deel 2 en 3 zijn gepubliceerd op Gumroad (22-11-2026).
"""
from boek import BOEK_URL

GUMROAD = BOEK_URL
WINKEL = "https://collens3.gumroad.com"
BOEK2_URL = "https://collens3.gumroad.com/l/programmeren-met-claude-ai"
BOEK3_URL = "https://collens3.gumroad.com/l/ondernemen-met-claude-ai"


def _kaart(img, deel, titel, sub, tekst, prijs, knoppen):
    kn = "".join(f'<a class="knop {cls}" href="{h}"{" rel=noopener target=_blank" if h.startswith("http") else ""}>{t}</a>' for t, h, cls in knoppen)
    return (f'<div class="boek-kaart"><img src="img/{img}" alt="Omslag van {titel}" width="240" height="360" loading="lazy">'
            f'<div class="boek-info"><p class="boek-deel">{deel}</p><h3>{titel}</h3><p class="boek-sub">{sub}</p><p>{tekst}</p>'
            f'<p class="boek-prijs">{prijs}</p><p class="knoppen">{kn}</p></div></div>')


_d2 = ([("Koop op Gumroad", BOEK2_URL, "geel")] if BOEK2_URL else [("Bekijk de webshop", WINKEL, "knop-rand")])
_d3 = ([("Koop op Gumroad", BOEK3_URL, "geel")] if BOEK3_URL else [("Bekijk de webshop", WINKEL, "knop-rand")])

BOEKEN_HTML = ('<div class="boeken-lijst">'
 + _kaart("boek-deel1.jpg", "Deel 1", "Claude voor beginners", "Van je eerste vraag tot je eigen AI-assistent",
          "Voor iedereen die AI wil gebruiken zonder technische kennis. In gewoon Nederlands leer je Claude zo inwerken dat het je werk, je bedrijf en je toon kent, en elke dag tijd voor je bespaart.",
          "€29,99 · PDF en EPUB", [("Lees meer", "boek-claude-voor-beginners.html", "knop-rand"), ("Koop op Gumroad", GUMROAD, "geel")])
 + _kaart("boek-deel2.jpg", "Deel 2", "Programmeren met Claude AI", "Van je eerste regel code tot meester in masterprompts",
          "Leer zelf websites en apps bouwen met AI als partner, en schrijf de instructies waarmee AI voorspelbaar en controleerbaar voor je werkt. Geen ervaring nodig.",
          "€39,99 · 92 pagina's · PDF en EPUB" + ("" if BOEK2_URL else " · verschijnt binnenkort"), _d2)
 + _kaart("boek-deel3.jpg", "Deel 3", "Ondernemen met Claude AI", "Bouw je eigen AI-team dat elke dag voor je bedrijf werkt",
          "Het praktijkboek voor ondernemers: hoe je marketing, klanten, vindbaarheid en administratie laat voorbereiden door een klein AI-team, terwijl jij goedkeurt en beslist. Met 30 masterprompts, 20 werkinstructies en 12 sjablonen.",
          "€44,99 · 139 pagina's · PDF en EPUB" + ("" if BOEK3_URL else " · verschijnt binnenkort"), _d3)
 + '</div>')

_DETAIL = [
 (1, "Claude voor beginners", "Je begint met AI en wilt het goed leren gebruiken.", "Goede vragen stellen, Projecten, geheugen, koppelingen en veilig werken.", "17 figuren, 40 vragen om te kopiëren, oefeningen", "106 pagina's · PDF en EPUB", "€29,99", GUMROAD),
 (2, "Programmeren met Claude AI", "Je wilt zelf websites en apps bouwen, zonder ervaring.", "HTML, CSS en JavaScript, een eigen website en app, masterprompts en werkinstructies.", "Echte code, 12 masterprompts, 14 werkinstructies", "92 pagina's · PDF en EPUB", "€39,99", BOEK2_URL or WINKEL),
 (3, "Ondernemen met Claude AI", "Je onderneemt en wilt meer uit handen geven aan AI.", "Een AI-team met geheugen, grenzen en rapporten voor marketing, verkoop, SEO en administratie.", "12 figuren en grafieken, 30 masterprompts, 20 werkinstructies, 12 sjablonen", "139 pagina's · PDF en EPUB", "€44,99", BOEK3_URL or WINKEL),
]

def _detail(n, titel, wie, leer, extra, omvang, prijs, url):
    return (f'<article class="boek-detail"><img src="img/boek-binnen-deel{n}.jpg" alt="Omslag en twee binnenpagina\'s van {titel}" width="960" height="600" loading="lazy">'
            f'<div><p class="boek-deel">Deel {n}</p><h3>{titel}</h3><dl>'
            f'<dt>Voor wie</dt><dd>{wie}</dd><dt>Je leert</dt><dd>{leer}</dd><dt>Extra</dt><dd>{extra}</dd><dt>Omvang</dt><dd>{omvang}</dd></dl>'
            f'<p class="knoppen"><a class="knop geel" href="{url}" rel="noopener" target="_blank">Koop voor {prijs}</a>' + ('<a class="knop knop-rand" href="boek-claude-voor-beginners.html">Lees meer</a>' if n == 1 else '') + '</p></div></article>')

DETAIL_HTML = '<div class="boek-details">' + "".join(_detail(*d) for d in _DETAIL) + '</div>'

BOEK_PAGINAS = [
 {"slug": "boeken", "lang": "nl", "kort": "Boeken",
  "titel": "Boeken over Claude AI van Jeffrey Collens | Collens Group",
  "desc": "De reeks Claude AI Compleet van Jeffrey Collens: praktische boeken in gewoon Nederlands over AI gebruiken, bouwen en ondernemen. Los verkrijgbaar via Gumroad.",
  "h1": "Leer het jezelf: boeken over Claude AI",
  "lead": "Praktische boeken in gewoon Nederlands, geschreven vanuit de dagelijkse praktijk van Collens Group. Elk deel is los verkrijgbaar en direct te downloaden.",
  "knop": ("Naar de webshop", WINKEL),
  "secties": [
   ("De boeken: welk deel past bij jou?", "<p>Elk boek heeft een eigen opmaak met figuren, grafieken en kaders met oefeningen en praktijkvoorbeelden. Hieronder per deel de omslag en twee echte binnenpagina's.</p>" + DETAIL_HTML),
   ("Waarom deze reeks?",
    "<p>Alles wat in deze boeken staat, gebruiken we zelf: voor onze eigen website, onze apps en het dagelijkse werk van ons bedrijf. Ook wat misging staat erin, met de regels die het voortaan voorkomen. De boeken bouwen op elkaar voort: deel 1 leert je AI gebruiken, deel 2 leert je ermee bouwen en deel 3 leert je er je bedrijf mee runnen.</p>"),
   ("Hoe koop je een boek?",
    "<p>Je koopt de boeken via <a href='https://collens3.gumroad.com' rel='noopener' target='_blank'>onze webshop op Gumroad</a>, een bekend platform voor digitale producten. Na het afrekenen download je het boek meteen. In de webshop vind je ook printbare producten, zoals planners en spellen voor het hele gezin.</p>")],
  "faq": [
   ("Moet ik de boeken op volgorde lezen?", "Nee, elk boek is los te lezen en je koopt alleen het deel dat je nodig hebt. Ben je nieuw met AI, begin dan bij deel 1: daar leer je goede vragen stellen en een eigen assistent inrichten. Wil je zelf websites, apps of kleine programma's laten bouwen, dan is deel 2 de volgende stap; je hoeft daarvoor niet te kunnen programmeren. Deel 3 is voor ondernemers die Claude al gebruiken en werk structureel uit handen willen geven, met 30 masterprompts, 20 werkinstructies en 12 sjablonen."),
   ("Hoe betaal ik en hoe krijg ik het boek?", "Je koopt elk boek apart via onze webshop op Gumroad, een internationaal platform voor digitale producten. Je betaalt daar veilig, bijvoorbeeld met je creditcard of PayPal, en je hoeft geen account aan te maken. Direct na het afrekenen download je het boek. Je krijgt ook een mail met de downloadlink en je betaalbewijs, zodat je het later opnieuw kunt downloaden."),
   ("Mag ik de masterprompts en sjablonen gebruiken?", "Ja. Daar zijn ze voor gemaakt. Je mag de masterprompts, werkinstructies en sjablonen kopiëren, aanpassen aan je eigen bedrijf en gebruiken voor je eigen klanten en projecten, ook commercieel. Wat niet mag: het boek of de bestanden zelf doorsturen, delen in een groep of doorverkopen. Elk exemplaar is een persoonlijke licentie. Werk je met een team, dan koopt ieder teamlid een eigen exemplaar."),
   ("In welk formaat krijg ik de boeken?", "Elk deel krijg je als PDF én als EPUB, zonder extra kosten. De PDF heeft de volledige opmaak met figuren en grafieken en leest prettig op een computer, tablet of telefoon. De EPUB past zich aan je scherm aan en is bedoeld voor e-readers zoals Kobo, of voor apps als Apple Boeken. Na het afrekenen download je de bestanden direct. Je krijgt ook een mail met de downloadlink, zodat je ze later opnieuw kunt downloaden. Er is geen gedrukte versie."),
   ("Heb ik een betaald Claude-abonnement nodig?", "Voor deel 1 kun je beginnen met de gratis versie van Claude. Sommige onderdelen, zoals koppelingen met je mail en agenda of geplande taken, vragen om een betaald abonnement. Voor deel 2 en deel 3 werk je het prettigst met een betaald abonnement, omdat je daar langere opdrachten en projecten laat uitvoeren. In elk boek staat per onderdeel wat je nodig hebt, zodat je niet voor niets betaalt."),
   ("Zijn de boeken van Anthropic?", "Nee. De boeken zijn geschreven door Jeffrey Collens, oprichter van Collens Group, en zijn niet verbonden aan Anthropic, het bedrijf dat Claude maakt. Ze zijn gebaseerd op wat hij dagelijks met Claude doet in zijn eigen bedrijf. Daardoor lees je hoe het in de praktijk werkt, inclusief wat misging, en niet alleen wat de handleiding belooft. Claude verandert snel; schermen en namen van knoppen kunnen dus afwijken van wat je in het boek ziet.")],
  "offers": [("Claude voor beginners", 29.99), ("Programmeren met Claude AI", 39.99), ("Ondernemen met Claude AI", 44.99)],
  "ld": {"@type": "CollectionPage", "name": "Boeken: de reeks Claude AI Compleet", "inLanguage": "nl", "publisher": {"@id": "#org"}},
  "rel": [("boek-claude-voor-beginners.html", "Claude voor beginners"), ("over-ons.html", "Over ons"), ("ai-automatisering.html", "AI en automatisering")]},

 {"slug": "boek-claude-voor-beginners", "lang": "nl", "kort": "Boek: Claude voor beginners",
  "titel": "Boek: Claude voor beginners (€29,99) | Collens Group",
  "desc": "Claude voor beginners: in gewoon Nederlands van je eerste vraag tot je eigen AI-assistent. Herziene editie, 106 pagina's, PDF en EPUB, €29,99. Geen techniek nodig.",
  "h1": "Claude voor beginners",
  "lead": "Van je eerste vraag tot je eigen AI-assistent. Een praktische gids in gewoon Nederlands, voor iedereen die AI wil gebruiken zonder technische kennis. Herziene editie november 2026: 106 pagina's, als PDF en EPUB, €29,99.",
  "knop": ("Koop het boek op Gumroad", GUMROAD),
  "secties": [
   ("Voor wie is dit boek?",
    "<p><img src='img/boek-deel1.jpg' alt='Omslag van Claude voor beginners' width='200' height='300' loading='lazy' style='float:right;margin:0 0 16px 20px;border-radius:8px;box-shadow:0 10px 30px rgba(0,0,0,.18)'>Voor iedereen die wel eens over AI hoort, maar niet goed weet waar te beginnen. Ondernemers, zzp'ers, mensen in loondienst en iedereen die nieuwsgierig is. Je hebt geen technische kennis nodig: alles wordt stap voor stap uitgelegd, knop voor knop.</p>"
    "<p>Je loopt de Claude-reis van acht stations mee met Sanne, eigenaar van een kleine kapsalon. Zo zie je niet alleen wat Claude kan, maar ook hoe iemand het echt in haar werk gebruikt.</p>"),
   ("Wat leer je?",
    "<ul><li>Je eerste gesprek en goede vragen stellen met één eenvoudige formule</li>"
    "<li>Je eigen assistent die je bedrijf, je prijzen en je toon kent</li>"
    "<li>Documenten laten maken en onderzoek met bronnen die je zelf controleert</li>"
    "<li>Je mail en agenda veilig koppelen en werk laten draaien met geplande taken</li>"
    "<li>Veilig blijven, oplichting herkennen en eerlijk kijken naar verdienen met AI</li></ul>"),
   ("Wat zit erin?",
    "<div class='scroll'><table class='tabel vergelijk'><tr><th>Onderdeel</th><th>Inhoud</th></tr>"
    "<tr><td>Omvang</td><td>18 hoofdstukken, 106 pagina's (herziene editie, november 2026)</td></tr>"
    "<tr><td>Formaat</td><td>PDF en EPUB (voor e-readers), direct te downloaden</td></tr>"
    "<tr><td>Extra's</td><td>17 figuren, een 7-dagenplan, een werkblad en 40 vragen om te kopiëren</td></tr>"
    "<tr><td>Per hoofdstuk</td><td>Een oefening, een samenvatting en een afvinklijst</td></tr>"
    "<tr><td>Prijs</td><td>€29,99, persoonlijk exemplaar</td></tr></table></div>"
    "<p>Dit is een onafhankelijke gids, niet verbonden aan Anthropic, het bedrijf achter Claude.</p>"),
   ("Wie schreef het?",
    "<p>Jeffrey Collens, oprichter van Collens Group. Hij bouwt websites, apps en AI-automatiseringen en gebruikt Claude daar elke dag voor. Wat in het boek staat, past hij zelf toe in zijn bedrijf. Meer over hem lees je op <a href='over-ons.html'>Over ons</a>.</p>"
    "<p>Dit boek is deel 1 van de reeks Claude AI Compleet. <a href='boeken.html'>Bekijk alle boeken</a>. Wil je AI liever laten inrichten dan het zelf te leren? Kijk dan bij <a href='ai-automatisering.html'>AI en automatisering</a>.</p>")],
  "faq": [
   ("Heb ik technische kennis nodig?", "Nee. Het boek is geschreven voor mensen die nog nooit met AI hebben gewerkt. Elke stap staat in gewoon Nederlands uitgelegd, met schermvoorbeelden en figuren. Je leert eerst een goede vraag stellen en bouwt daarna stap voor stap verder, tot je een eigen assistent hebt die je bedrijf kent. Kun je mailen en een website bezoeken, dan kun je dit boek volgen. Vaktermen worden uitgelegd zodra ze voorkomen."),
   ("In welk formaat krijg ik het boek?", "Je krijgt het boek als PDF en als EPUB. De PDF lees je op je computer, tablet of telefoon; de EPUB is voor e-readers. Na het afrekenen download je beide bestanden direct via Gumroad."),
   ("Hoe betaal ik?", "Je koopt het boek via Gumroad, een internationaal platform voor digitale producten. Je betaalt daar veilig, bijvoorbeeld met je creditcard of PayPal. Je hoeft geen account aan te maken. Direct na het afrekenen download je het boek, en je krijgt een mail met de downloadlink en je betaalbewijs. De prijs is €29,99."),
   ("Heb ik een betaald Claude-abonnement nodig?", "Je kunt beginnen met de gratis versie van Claude. Sommige functies die in het boek aan bod komen, zoals bepaalde koppelingen of geplande taken, vragen om een betaald abonnement. Het boek legt uit wat je waarvoor nodig hebt."),
   ("Is het boek van Anthropic?", "Nee. Dit is een onafhankelijke gids van Jeffrey Collens, oprichter van Collens Group. Het boek is niet verbonden aan Anthropic, het bedrijf dat Claude maakt. Alles wat erin staat, gebruikt hij zelf in zijn bedrijf. Claude krijgt regelmatig nieuwe functies; namen van knoppen en schermen kunnen daardoor wat afwijken van de voorbeelden, maar de werkwijze blijft hetzelfde.")],
  "offers": [("Claude voor beginners (PDF + EPUB)", 29.99)],
  "ld": {"@type": "Book", "name": "Claude voor beginners", "inLanguage": "nl", "bookFormat": "https://schema.org/EBook", "bookEdition": "Herziene editie, november 2026",
         "numberOfPages": 106, "author": {"@type": "Person", "name": "Jeffrey Collens"}, "publisher": {"@id": "#org"},
         "isPartOf": {"@type": "BookSeries", "name": "Claude AI Compleet"},
         "offers": {"@type": "Offer", "price": "29.99", "priceCurrency": "EUR", "url": GUMROAD, "availability": "https://schema.org/InStock"}},
  "rel": [("boeken.html", "Alle boeken"), ("over-ons.html", "Over ons"), ("ai-automatisering.html", "AI en automatisering")]},
]
