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
 (1, "Claude voor beginners", "Werk slimmer met AI. Vanaf vandaag.",
  "Voor wie net begint. In gewoon Nederlands leer je stap voor stap hoe je Claude inzet in je werk, tot je een assistent hebt die jouw bedrijf kent.",
  ["Goede vragen stellen met één eenvoudige formule", "Een eigen assistent die je bedrijf, prijzen en toon kent", "Mail en agenda veilig koppelen"],
  ["106 pagina's", "17 figuren", "40 vragen om te kopiëren"], "€29,99", GUMROAD),
 (2, "Programmeren met Claude AI", "Bouw je eigen website of app. Ook zonder ervaring.",
  "Voor wie zelf wil bouwen. Je leert de basis van HTML, CSS en JavaScript en laat Claude het zware werk doen, terwijl jij begrijpt wat er gebeurt.",
  ["Je eigen website, stap voor stap gebouwd", "Een eigen app maken met Claude als partner", "Masterprompts waarmee AI voorspelbaar werkt"],
  ["92 pagina's", "12 masterprompts", "14 werkinstructies"], "€39,99", BOEK2_URL or WINKEL),
 (3, "Ondernemen met Claude AI", "Laat AI het werk doen. Jij houdt de regie.",
  "Voor ondernemers die Claude al gebruiken. Bouw een klein AI-team dat marketing, klanten, vindbaarheid en administratie voorbereidt, terwijl jij goedkeurt en beslist.",
  ["Een AI-team met geheugen, grenzen en dagrapporten", "Marketing, verkoop en SEO laten voorbereiden", "Heldere regels: wat AI zelf mag en wat nooit"],
  ["139 pagina's", "30 masterprompts", "20 werkinstructies", "12 sjablonen"], "€44,99", BOEK3_URL or WINKEL),
]


_INHOUD = {
 1: ("Claude voor beginners is de gids die je wilde hebben toen je voor het eerst een AI-chat opende. Je loopt de reis mee met Sanne, eigenaar van een kleine kapsalon, en ziet stap voor stap hoe AI van een handig hulpje uitgroeit tot een assistent die haar bedrijf kent. Geen vakjargon, wel concrete voorbeelden, oefeningen en een afvinklijst per hoofdstuk.",
     [("Deel 1 · De basis", ["Wat Claude is, en wat niet", "Aan de slag in tien minuten", "Goed vragen stellen", "Dagelijks werk: tien vragen die tijd besparen"]),
      ("Deel 2 · Je eigen assistent", ["Projecten en vaste instructies", "Geheugen: Claude onthoudt wat belangrijk is", "Bestanden en kant-en-klare documenten", "Onderzoek en bronnen"]),
      ("Deel 3 · Verder gaan", ["Koppelingen en toestemmingen", "Langere taken, browser en computer", "Automatisering en geplande taken", "MCP en API's in gewone taal", "Skills, plugins en agents", "Claude steeds beter maken", "Zelfstandig laten werken, met grenzen"]),
      ("Deel 4 · Verdienen en veilig", ["Onderzoek, ondernemen en inkomsten", "Veiligheid, privacy en oplichting", "Van gebruiker naar maker"])]),
 2: ("Programmeren met Claude AI laat je zelf bouwen, ook als je nog nooit een regel code schreef. Je leert genoeg van HTML, CSS, JavaScript en Python om te begrijpen wat er gebeurt, en laat Claude het zware werk doen. Je bouwt een echte website en een app, en leert daarna de masterprompts en werkinstructies schrijven waarmee AI voorspelbaar en controleerbaar voor je werkt.",
     [("De basis", ["Wat programmeren is en wat AI eraan verandert", "Je werkplek klaarzetten", "De basis: HTML, CSS en JavaScript", "Python voor beginners", "Claude als programmeerpartner"]),
      ("Bouwen", ["Project 1: je eigen website bouwen en online zetten", "Project 2: een app voor iPhone en Android", "Data, database en API's", "Testen, fouten zoeken en versiebeheer", "Veilig werken en publiceren"]),
      ("Meesterniveau", ["Masterprompts leren bouwen: de anatomie", "Masterprompts testen, meten en verbeteren", "Werkinstructies leren bouwen", "AI zelfstandig laten bouwen, met controle"])]),
 3: ("Ondernemen met Claude AI is het praktijkboek voor ondernemers die meer willen dan losse prompts. Je bouwt een klein AI-team met geheugen, duidelijke grenzen en dagrapporten. Het team bereidt marketing, verkoop, vindbaarheid en administratie voor; jij keurt goed en beslist. Inclusief 30 masterprompts, 20 werkinstructies en 12 sjablonen die je direct kunt gebruiken.",
     [("Deel 1 · Het fundament", ["Waarom een AI-team en geen losse prompts", "Het organigram van je AI-team", "Het bedrijfsgeheugen", "Grenzen, bevoegdheden en goedkeuring"]),
      ("Deel 2 · Marketing en merk", ["Je merk en positionering scherp", "De contentmachine die menselijk klinkt", "Social media met een vaste planning", "Beeld, video en ontwerp", "Eerlijke marketing die toch overtuigt"]),
      ("Deel 3 · Klanten en verkoop", ["Leads die bestaan", "Persoonlijke voorstellen die wél gelezen worden", "Koude mail met fatsoen", "Offertes en opvolging", "Klantenservice die altijd antwoordt"]),
      ("Deel 4 · Vindbaarheid en eigen producten", ["SEO met een AI-team", "Gevonden worden door AI-zoekmachines", "Digitale producten die verkopen", "Je webshop draaiend houden"]),
      ("Deel 5 · Operatie en geld", ["Mail en administratie op orde", "Geplande taken: je team werkt ook als jij slaapt", "Dagrapport en weekrapport", "Wat kost het en wat levert het op"]),
      ("Deel 6 · Groeien", ["Je werkwijzen als dienst voor anderen", "Het 90-dagenplan"])]),
}

def _dialoog(n, titel, prijs, url, stats):
    besch, delen = _INHOUD[n]
    k = 0; blokken = ""
    for d, hs in delen:
        li = ""
        for h in hs:
            if h.startswith("…"):
                li += f"<li class='meer'>{h}</li>"
            else:
                k += 1; li += f"<li><span>{k}</span>{h}</li>"
        blokken += f"<div class='inh-deel'><h4>{d}</h4><ol>{li}</ol></div>"
    st = "".join(f"<li>{x}</li>" for x in stats)
    return (f'<dialog class="boek-dlg boek-p{n}" id="inhoud-{n}" aria-labelledby="dlg-t{n}"><div class="dlg-in">'
            f'<button class="dlg-x" type="button" aria-label="Sluiten" data-sluit>×</button>'
            f'<div class="dlg-kop"><img src="img/omslag-{n}.jpg" alt="Omslag van {titel}" width="400" height="600" loading="lazy">'
            f'<div><p class="boek-deel">Deel {n}</p><h3 id="dlg-t{n}">{titel}</h3><p>{besch}</p><ul class="boek-stats">{st}</ul>'
            f'<div class="boek-koop"><div class="boek-prijs">{prijs}<small>PDF + EPUB · direct downloaden</small></div><p class="knoppen"><a class="knop geel" href="{url}" rel="noopener" target="_blank">Koop deel {n}</a></p></div></div></div>'
            f'<h4 class="dlg-sub">Wat er in staat</h4><div class="inh-grid">{blokken}</div>'
            f'<h4 class="dlg-sub">Een kijkje binnen</h4><div class="inkijk"><img src="img/inkijk-{n}a.jpg" alt="Binnenpagina uit {titel}" width="347" height="520" loading="lazy"><img src="img/inkijk-{n}b.jpg" alt="Tweede binnenpagina uit {titel}" width="347" height="520" loading="lazy"></div>'
            f'</div></dialog>')

_DLG_JS = ("<script>document.addEventListener('click',function(e){var o=e.target.closest('[data-open]');if(o){e.preventDefault();var d=document.getElementById(o.getAttribute('data-open'));if(d&&d.showModal){d.showModal();}return;}"
           "var s=e.target.closest('[data-sluit]');if(s){s.closest('dialog').close();return;}if(e.target.tagName==='DIALOG'){e.target.close();}});</script>")

_VINK = '<svg viewBox="0 0 20 20" width="20" height="20" aria-hidden="true"><circle cx="10" cy="10" r="10" fill="currentColor" opacity=".18"/><path d="M6 10.3l2.6 2.6L14.2 7.4" fill="none" stroke="currentColor" stroke-width="2.3" stroke-linecap="round" stroke-linejoin="round"/></svg>'

def _detail(n, titel, kop, pitch, punten, stats, prijs, url):
    li = "".join(f"<li>{_VINK}<span>{p}</span></li>" for p in punten)
    st = "".join(f"<li>{x}</li>" for x in stats)
    meer = f'<a class="knop boek-knop-rand" href="#inhoud-{n}" data-open="inhoud-{n}">Bekijk de inhoud</a>'
    return (f'<article class="boek-paneel boek-p{n}" id="deel-{n}"><div class="boek-tekst">'
            f'<p class="boek-deel">Deel {n} · {titel}</p><h3>{kop}</h3><p class="boek-pitch">{pitch}</p>'
            f'<ul class="boek-punten">{li}</ul><ul class="boek-stats">{st}</ul>'
            f'<div class="boek-koop"><div class="boek-prijs">{prijs}<small>PDF + EPUB · direct downloaden</small></div>'
            f'<p class="knoppen"><a class="knop geel" href="{url}" rel="noopener" target="_blank">Koop deel {n}</a>{meer}</p></div></div>'
            f'<a class="boek-beeld" href="#inhoud-{n}" data-open="inhoud-{n}" aria-label="Bekijk de inhoud van {titel}"><img src="img/boek-visual-deel{n}.png" alt="Omslag en binnenpagina\'s van {titel}" width="960" height="900" loading="lazy"><span class="beeld-hint">Bekijk de inhoud</span></a></article>' + _dialoog(n, titel, prijs, url, stats))


_BUNDELS = [
 ("claude-compleet", "Claude AI Compleet", "Alle 3 delen: beginnen, bouwen en ondernemen met AI. De beste deal als je het hele pad wilt lopen.", "€84,95", "€114,97", "Bespaar €30", "https://collens3.gumroad.com/l/claude-ai-compleet", True),
 ("ai-starter", "AI Starter", "Claude voor beginners plus 100 slimme AI-vragen voor zzp'ers. Direct aan de slag in je eigen werk.", "€32,95", "€39,94", "Bespaar €6,99", "https://collens3.gumroad.com/l/ai-starter", False),
]

def _bundel(slug, naam, txt, prijs, oud, bespaar, url, top):
    return (f'<article class="bundel{" bundel-top" if top else ""}"><img src="img/bundel-{slug}.jpg" alt="Bundel {naam}" width="960" height="540" loading="lazy">'
            f'<div class="bundel-tekst">{"<p class=\'bundel-tag\'>Meest gekozen</p>" if False else ""}<h3>{naam}</h3><p>{txt}</p>'
            f'<div class="bundel-prijs"><strong>{prijs}</strong><s>{oud}</s><span>{bespaar}</span></div>'
            f'<a class="knop geel" href="{url}" rel="noopener" target="_blank">Koop de bundel</a></div></article>')

BUNDEL_HTML = '<div class="bundels">' + "".join(_bundel(*b) for b in _BUNDELS) + '</div>'

DETAIL_HTML = '<div class="boek-details">' + "".join(_detail(*d) for d in _DETAIL) + '</div>' + _DLG_JS

BOEK_PAGINAS = [
 {"slug": "boeken", "lang": "nl", "kort": "Boeken",
  "titel": "Boeken over Claude AI van Jeffrey Collens | Collens Group",
  "desc": "De reeks Claude AI Compleet van Jeffrey Collens: praktische boeken in gewoon Nederlands over AI gebruiken, bouwen en ondernemen. Los verkrijgbaar via Gumroad.",
  "h1": "Leer het jezelf: boeken over Claude AI",
  "lead": "Praktische boeken in gewoon Nederlands, geschreven vanuit de dagelijkse praktijk van Collens Group. Elk deel is los verkrijgbaar en direct te downloaden.",
  "knop": ("Naar de webshop", WINKEL),
  "secties": [
   ("De boeken: welk deel past bij jou?", "<p>Drie boeken, drie stappen. Begin waar jij nu staat en koop alleen wat je nodig hebt. Elk deel staat vol figuren, praktijkvoorbeelden en opdrachten die je direct kunt toepassen.</p>" + DETAIL_HTML),
   ("Voordeliger in een bundel", "<p>Wil je meer dan één deel? Met een bundel betaal je minder dan los. Je krijgt dezelfde bestanden, als PDF en EPUB, direct na aankoop.</p>" + BUNDEL_HTML),
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
