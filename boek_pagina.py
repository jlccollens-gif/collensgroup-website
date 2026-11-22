"""Boekpagina 'Claude voor beginners' (deel 1). Opdracht Jeffrey 22-11-2026: "Maak een boekpagina".
Alle feiten komen van de Gumroad-productpagina (collens3.gumroad.com/l/claude-voor-beginners, gecontroleerd 22-11-2026):
titel, prijs €29,99, 82 pagina's, PDF + EPUB, 8 stations, Sanne de kapster, 19 schema's, 7-dagenplan, werkblad, 50 vragen."""
from boek import BOEK_URL

GUMROAD = BOEK_URL

BOEK_PAGINAS = [
 {"slug": "boek-claude-voor-beginners", "lang": "nl", "kort": "Boek: Claude voor beginners",
  "titel": "Boek: Claude voor beginners (€29,99) | Collens Group",
  "desc": "Claude voor beginners: in gewoon Nederlands van je eerste vraag tot je eigen AI-assistent. 82 pagina's, PDF en EPUB, €29,99. Geen techniek nodig.",
  "h1": "Claude voor beginners",
  "lead": "Van je eerste vraag tot je eigen AI-assistent. Een praktische gids in gewoon Nederlands, voor iedereen die AI wil gebruiken zonder technische kennis. 82 pagina's, als PDF en EPUB, €29,99.",
  "knop": ("Koop het boek op Gumroad", GUMROAD),
  "secties": [
   ("Voor wie is dit boek?",
    "<p>Voor iedereen die wel eens over AI hoort, maar niet goed weet waar te beginnen. Ondernemers, zzp'ers, mensen in loondienst en iedereen die nieuwsgierig is. Je hebt geen technische kennis nodig: alles wordt stap voor stap uitgelegd, knop voor knop.</p>"
    "<p>Je loopt de hele 'Claude-reis' mee in 8 stations, samen met Sanne, een kapster zonder technische kennis. Zo zie je niet alleen wát Claude kan, maar ook hoe iemand het echt in haar werk gebruikt.</p>"),
   ("Wat leer je?",
    "<ul><li>Het scherm uitgelegd en je eerste gesprek, knop voor knop</li>"
    "<li>Goede vragen stellen met één eenvoudige formule</li>"
    "<li>Je eigen assistent met Projecten en geheugen</li>"
    "<li>Documenten, tabellen en presentaties laten maken</li>"
    "<li>Je mail en agenda veilig koppelen</li>"
    "<li>Werk automatiseren met geplande taken</li>"
    "<li>Veilig blijven en oplichting herkennen</li>"
    "<li>Eerlijk over geld verdienen met AI</li></ul>"),
   ("Wat zit erin?",
    "<div class='scroll'><table class='tabel vergelijk'><tr><th>Onderdeel</th><th>Inhoud</th></tr>"
    "<tr><td>Omvang</td><td>82 pagina's</td></tr>"
    "<tr><td>Formaat</td><td>PDF en EPUB (voor e-readers), direct te downloaden</td></tr>"
    "<tr><td>Extra's</td><td>19 schema's, een 7-dagenplan, een werkblad en 50 vragen om te kopiëren</td></tr>"
    "<tr><td>Per hoofdstuk</td><td>Een samenvatting en een checklist</td></tr>"
    "<tr><td>Prijs</td><td>€29,99, persoonlijk exemplaar</td></tr></table></div>"
    "<p>Dit is een onafhankelijke gids, niet verbonden aan Anthropic, het bedrijf achter Claude.</p>"),
   ("Wie schreef het?",
    "<p>Jeffrey Collens, oprichter van Collens Group. Hij bouwt websites, apps en AI-automatiseringen en gebruikt Claude daar elke dag voor. Wat in het boek staat, past hij zelf toe in zijn bedrijf. Meer over hem lees je op <a href='over-ons.html'>Over ons</a>.</p>"
    "<p>Wil je AI liever laten inrichten dan het zelf te leren? Kijk dan bij <a href='ai-automatisering.html'>AI en automatisering</a> of <a href='chatbot-laten-maken.html'>een AI-chatbot laten maken</a>.</p>")],
  "faq": [
   ("Heb ik technische kennis nodig?", "Nee. Het boek is geschreven voor beginners en legt alles in gewoon Nederlands uit, knop voor knop. Je volgt Sanne, een kapster zonder technische kennis, die Claude stap voor stap in haar werk gaat gebruiken."),
   ("In welk formaat krijg ik het boek?", "Je krijgt het boek als PDF en als EPUB. De PDF lees je op je computer, tablet of telefoon; de EPUB is voor e-readers. Na het afrekenen download je beide bestanden direct via Gumroad."),
   ("Hoe betaal ik?", "Je koopt het boek via Gumroad, een bekend platform voor digitale producten. Daar reken je veilig af en download je het boek meteen. De prijs is €29,99."),
   ("Heb ik een betaald Claude-abonnement nodig?", "Je kunt beginnen met de gratis versie van Claude. Sommige functies die in het boek aan bod komen, zoals bepaalde koppelingen of geplande taken, vragen om een betaald abonnement of extra instellingen. Het boek legt uit wat je waarvoor nodig hebt, zodat je zelf kunt kiezen."),
   ("Is het boek van Anthropic?", "Nee. Dit is een onafhankelijke gids, geschreven door Jeffrey Collens. Hij is niet verbonden aan Anthropic, het bedrijf achter Claude.")],
  "offers": [("Claude voor beginners (PDF + EPUB)", 29.99)],
  "ld": {"@type": "Book", "name": "Claude voor beginners", "inLanguage": "nl", "bookFormat": "https://schema.org/EBook",
         "numberOfPages": 82, "author": {"@type": "Person", "name": "Jeffrey Collens"}, "publisher": {"@id": "#org"},
         "offers": {"@type": "Offer", "price": "29.99", "priceCurrency": "EUR", "url": GUMROAD, "availability": "https://schema.org/InStock"}},
  "rel": [("over-ons.html", "Over ons"), ("ai-automatisering.html", "AI en automatisering"), ("chatbot-laten-maken.html", "AI-chatbot laten maken")]},
]
