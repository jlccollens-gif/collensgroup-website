"""Extra branchepagina's en de Belgiepagina (zelfde structuur als LANDINGS in landings.py).
Alleen feiten die ook elders op de site staan: prijzen, levertijden, onderhoud, eindprijzen.
Marktbedragen komen uit bronnen die al op de site worden aangehaald (Trustoo, Lunidev, Searchlab)."""

PRIJS_TABEL = ("<div class='scroll'><table class='tabel vergelijk'><tr><th>Pakket</th><th>Geschikt voor</th><th>Vanaf</th></tr>"
               "<tr><td>One-page website</td><td>{een}</td><td>€495</td></tr>"
               "<tr><td>Bedrijfswebsite</td><td>{twee}</td><td>€995</td></tr>"
               "<tr><td>Extra pagina</td><td>Bijvoorbeeld {extra}</td><td>€95</td></tr></table></div>"
               "<p>Alle prijzen zijn eindprijzen, er komt geen btw bij, vast en vooraf afgesproken. Een domeinnaam kost meestal €10 tot €25 per jaar en hosting kan voor de meeste kleine sites gratis. "
               "Onderhoud is optioneel vanaf €29 per maand, bijvoorbeeld voor kleine wijzigingen tot 30 minuten per maand. Ter vergelijking: een eenvoudige website kost in Nederland gemiddeld €500 tot €2.000 "
               "(<a href='https://trustoo.nl/kosten/webdesign-kosten/' rel='nofollow noopener'>Trustoo, november 2026</a>).</p>")

STAPPEN = ("<ol><li>Stuur je aanvraag: een paar zinnen over je bedrijf is genoeg.</li>"
           "<li>Binnen 48 uur krijg je een gratis concept van je homepage, zonder verplichtingen.</li>"
           "<li>Je keurt ontwerp en vaste prijs goed.</li>"
           "<li>Wij bouwen, jij test, daarna gaat de site live op jouw eigen domein.</li></ol>")

ZOEK = ("<p>Klanten zoeken meestal op {term} met hun plaats of regio erbij. We bouwen elke site snel, mobielvriendelijk en met de technische basis die Google verwacht, "
        "met een duidelijke titel, beschrijving en koppen per pagina. Een toppositie kan niemand garanderen; we zorgen wel dat je site goed leesbaar is voor mensen en voor zoekmachines, "
        "en dat je bedrijfsnaam, werkgebied en contactgegevens op elke pagina kloppen.</p>")


def _maak(slug, kort, titel, desc, h1, lead, wat_kop, wat, tabel, uniek_kop, uniek, term, _leeg, faq_extra, rel_extra=None):
    return {"slug": slug, "lang": "nl", "kort": kort, "titel": titel, "desc": desc, "h1": h1, "lead": lead,
            "secties": [(wat_kop, wat), (f"Wat kost een website voor {tabel['voor']}?", PRIJS_TABEL.format(**tabel["rijen"])),
                        (uniek_kop, uniek), ("Gevonden worden", ZOEK.format(term=term)), ("Zo werkt het", STAPPEN)],
            "faq": faq_extra + [("Ben ik eigenaar van de website?", "Ja. De site, het domein en de inhoud staan op jouw naam. Je zit niet vast aan een websitebouwer."),
                                ("Staat de btw erbij?", "Nee. Alle prijzen zijn eindprijzen: er komt geen btw bij."),
                                ("Hoe snel is mijn website klaar?", "Een one-page website meestal in 3–5 dagen en een bedrijfswebsite in 2–3 weken. Hoe snel je teksten en foto's aanlevert, bepaalt mee hoe snel het gaat.")],
            "offers": [("One-page website", 495), ("Bedrijfswebsite", 995)],
            "rel": [("website-laten-maken.html", "Website laten maken"), ("prijzen.html", "Alle prijzen"), ("pakketkiezer.html", "Pakketkiezer")] + (rel_extra or [])}


NIEUW = [
 _maak("website-laten-maken-fotograaf", "Website fotograaf",
  "Website voor fotograaf vanaf €495 | Collens Group",
  "Website laten maken voor fotografen: snelle portfolio, pakketten en prijzen, boekformulier. Vaste prijs vanaf €495, gratis concept binnen 48 uur.",
  "Website laten maken voor fotografen",
  "Een snelle portfoliowebsite voor fotografen en videografen waarop je werk groot en scherp staat en klanten zonder omwegen een shoot aanvragen. Vanaf €495, geen btw erbij, met een gratis concept binnen 48 uur.",
  "Wat moet er op de website van een fotograaf?",
  "<p>Een bezoeker beslist in seconden of jouw stijl past. Daarom draait een fotografiesite om je beste werk, snel in beeld, en om een duidelijke volgende stap.</p><ul><li><strong>Een sterk portfolio</strong>: een selectie per genre (bruiloft, portret, bedrijf), niet alles wat je ooit maakte</li><li><strong>Foto's die snel laden</strong>: we verkleinen beelden en gebruiken moderne formaten, zodat de site ook op een telefoon vlot blijft</li><li><strong>Pakketten en prijzen</strong>, of in elk geval een richtprijs, zodat mensen weten of je binnen hun budget valt</li><li><strong>Een boek- of offerteformulier</strong> met datum en soort shoot</li><li><strong>Echte ervaringen</strong> van klanten, alleen met hun toestemming</li><li>Een link naar je <strong>Instagram</strong> en je contactgegevens</li></ul>",
  {"voor": "een fotograaf", "rijen": {"een": "Portfolio op één pagina: selectie van je werk, pakketten, over jou en contactformulier. Klaar in 3–5 dagen.", "twee": "Aparte pagina's per genre (bruiloft, portret, zakelijk), prijzen, over mij en contact. Tot 6 pagina's, klaar in 2–3 weken.", "extra": "een aparte pagina voor een nieuw genre of een fotoserie"}},
  "Foto's, rechten en eigendom",
  "<p>Op je site staan alleen foto's waarvoor jij de rechten hebt. Bij foto's van klanten vraag je vooraf toestemming; wij helpen je met een korte tekst daarvoor. Je levert de foto's aan of wijst aan welke uit je bestaande portfolio horen; wij zorgen dat ze goed worden verkleind en geplaatst.</p><p>De site, het domein en de inhoud staan op jouw naam. Wil je later andere foto's tonen, dan kun je dat als kleine wijziging bij ons laten doen (onderhoud vanaf €29 per maand, inclusief kleine wijzigingen tot 30 minuten).</p>",
  "fotograaf of trouwfotograaf",
  {}, [("Kan ik zelf foto's wisselen?", "Kleine wijzigingen, zoals een nieuwe serie, laat je door ons doen via het onderhoud (vanaf €29 per maand, kleine wijzigingen tot 30 minuten per maand). Een extra pagina kost €95.")]),
 _maak("website-laten-maken-aannemer", "Website aannemer",
  "Website aannemer of installateur vanaf €495 | Collens Group",
  "Website laten maken voor aannemers, installateurs en klusbedrijven: offerteformulier, werkgebied en projecten. Vaste prijs vanaf €495, gratis concept in 48 uur.",
  "Website laten maken voor aannemers, installateurs en klusbedrijven",
  "Een duidelijke website voor je bouw-, klus- of installatiebedrijf waarop klanten in je werkgebied meteen zien wat je doet en hoe ze een offerte aanvragen. Vanaf €495, geen btw erbij, met een gratis concept binnen 48 uur.",
  "Wat moet er op de website van een aannemer of installateur?",
  "<p>Mensen zoeken vaak met haast of met een concreet klusje in hun hoofd. De site moet in een paar seconden beantwoorden: doen jullie dit, werken jullie bij mij in de buurt, en hoe vraag ik een prijs aan?</p><ul><li><strong>Wat je doet</strong>, per dienst op een eigen plek (bijvoorbeeld dakkapel, badkamer, cv-onderhoud)</li><li><strong>Werkgebied</strong>: de plaatsen of regio waar je werkt</li><li><strong>Een offerteformulier</strong> met een paar vragen die jou al veel werk besparen</li><li><strong>Foto's van eigen projecten</strong>, liefst voor en na</li><li><strong>Contactgegevens</strong> met een belknop op mobiel, en bij spoed duidelijk wanneer je bereikbaar bent</li><li><strong>Keurmerken en verzekeringen</strong>, maar alleen als je ze echt hebt</li></ul>",
  {"voor": "een aannemer of installateur", "rijen": {"een": "Alle diensten, werkgebied, foto's en offerteformulier op één pagina. Klaar in 3–5 dagen.", "twee": "Een pagina per dienst, projecten, over ons en contact. Tot 6 pagina's, klaar in 2–3 weken.", "extra": "een aparte pagina voor een extra dienst of een regio"}},
  "Offertes en aanvragen die bruikbaar zijn",
  "<p>Een offerteformulier dat om de juiste dingen vraagt (soort klus, plaats, globale omvang, foto's), scheelt je telefoontjes. We bouwen het formulier zo dat aanvragen netjes in je mail aankomen. Wil je later koppelen met je offertesysteem of agenda, dan bespreken we dat als aparte stap en staat de prijs vooraf op papier, zoals bij onze AI- en automatiseringsdiensten vanaf €395.</p>",
  "aannemer, loodgieter of schilder",
  {}, [("Kan ik mijn werkgebied noemen?", "Ja. We zetten je werkgebied duidelijk op de site, zodat klanten en Google zien waar je werkt. Per extra regio kan een aparte pagina (€95) zinvol zijn.")]),
 _maak("website-laten-maken-coach-zzp", "Website coach en zzp",
  "Website voor coach en zzp'er vanaf €495 | Collens Group",
  "Website laten maken voor coaches, trainers en zzp'ers: duidelijk aanbod, over jou, kennismaking boeken. Vaste prijs vanaf €495, gratis concept in 48 uur.",
  "Website laten maken voor coaches, trainers en zzp'ers",
  "Een persoonlijke website voor coaches, trainers, adviseurs en andere zzp'ers waarop bezoekers snel snappen wat je aanbiedt en een kennismaking plannen. Vanaf €495, geen btw erbij, met een gratis concept binnen 48 uur.",
  "Wat moet er op de website van een zzp'er?",
  "<p>Bij een persoonlijk bedrijf kopen mensen vooral jou. De website moet daarom twee dingen goed doen: helder zijn over wat je aanbiedt en voor wie, en vertrouwen geven.</p><ul><li><strong>Een duidelijke belofte</strong> bovenaan: voor wie ben je er en wat verandert er voor hen</li><li><strong>Je aanbod</strong> in een paar duidelijke blokken, met een richtprijs of tenminste hoe een traject verloopt</li><li><strong>Over jou</strong>, met een echte foto en je werkwijze</li><li><strong>Een kennismaking plannen</strong>, met één knop</li><li><strong>Ervaringen van echte klanten</strong>, met hun toestemming</li><li>Je contactgegevens en eventueel je <strong>LinkedIn</strong></li></ul>",
  {"voor": "een coach of zzp'er", "rijen": {"een": "Aanbod, over jou, ervaringen en kennismakingsknop op één pagina. Klaar in 3–5 dagen.", "twee": "Aparte pagina's voor elk aanbod, over mij, werkwijze en contact. Tot 6 pagina's, klaar in 2–3 weken.", "extra": "een aparte pagina voor een nieuw aanbod of een blog-artikel"}},
  "Een afspraak plannen zonder gedoe",
  "<p>De drempel om contact op te nemen moet laag zijn. Meestal plaatsen we op je site een knop naar jouw eigen agenda-tool of een eenvoudig contactformulier; welke koppeling mogelijk is hangt af van het systeem dat je al gebruikt en dat zoeken we uit vóór de offerte. Heb je nog niets, dan werkt een formulier dat naar je mail gaat prima om mee te beginnen.</p><p>Echte ervaringen zijn waardevol, maar we plaatsen alleen reviews die je werkelijk van klanten hebt gekregen en mogen tonen. We verzinnen of kopen nooit reviews.</p>",
  "coach, trainer of adviseur",
  {}, [("Moet ik zelf teksten schrijven?", "Jij levert de kern aan: wat je doet, voor wie en je werkwijze. Wij zetten het om in heldere websiteteksten die Google ook kan lezen, en jij keurt ze goed.")]),
 _maak("website-laten-maken-vakantiehuis", "Website vakantiehuis",
  "Website voor vakantiehuis en B&B vanaf €495 | Collens Group",
  "Website laten maken voor je vakantiehuis, B&B of campingstek: foto's, beschikbaarheid en aanvragen rechtstreeks. Vanaf €495, gratis concept binnen 48 uur.",
  "Website laten maken voor je vakantiehuis of B&B",
  "Een eigen website voor je vakantiehuis, B&B of kleine camping waarop gasten je accommodatie zien, prijzen vinden en rechtstreeks een aanvraag doen. Vanaf €495, geen btw erbij, met een gratis concept binnen 48 uur.",
  "Wat moet er op de website van een vakantiehuis staan?",
  "<p>Gasten vergelijken snel. Een eigen website werkt naast boekingsplatforms: jij bepaalt de presentatie en gasten kunnen rechtstreeks contact opnemen.</p><ul><li><strong>Foto's die kloppen</strong> met wat gasten krijgen, groot en snel geladen</li><li><strong>Een duidelijke beschrijving</strong>: slaapplekken, voorzieningen, omgeving en huisregels</li><li><strong>Prijzen en seizoenen</strong>, en wat er bij de prijs hoort</li><li><strong>Beschikbaarheid en aanvragen</strong>: een link naar je boekingskalender of een aanvraagformulier</li><li><strong>Waar je zit</strong> en wat er in de buurt te doen is</li><li><strong>Contact</strong> en bereikbaarheid</li></ul>",
  {"voor": "een vakantiehuis of B&B", "rijen": {"een": "Foto's, beschrijving, prijzen, omgeving en aanvraagformulier op één pagina. Klaar in 3–5 dagen.", "twee": "Aparte pagina's voor accommodatie, prijzen, omgeving, huisregels en contact. Tot 6 pagina's, klaar in 2–3 weken.", "extra": "een pagina per accommodatie of een pagina over de omgeving"}},
  "Rechtstreekse aanvragen en je boekingskalender",
  "<p>Veel verhuurders gebruiken al een boekingskalender of een platform. Dat hoef je niet te vervangen. We kunnen een link of widget van je bestaande systeem op je site plaatsen, of een aanvraagformulier dat in je mail aankomt. Welke koppeling kan, hangt af van je systeem; dat zoeken we uit vóór de offerte. Heb je gasten uit meerdere landen, dan bespreken we in de offerte welke taalversies zinvol zijn en wat die kosten.</p>",
  "vakantiehuis, B&B of vakantiewoning",
  {}, [("Kan ik mijn boekingskalender koppelen?", "Vaak wel: een link of widget van je bestaande kalender of platform kan op de site. Welke koppeling mogelijk is hangt af van je systeem en dat zoeken we vooraf uit.")]),
]

# Belgiepagina (nl-BE)
BELGIE = {"slug": "website-laten-maken-belgie", "lang": "nl", "kort": "Website België",
  "titel": "Website laten maken in België vanaf €495 | Collens Group",
  "desc": "Website of webshop laten maken in België: wat het kost, waar je op moet letten en hoe wij werken. Vaste eindprijs vanaf €495, gratis concept binnen 48 uur.",
  "h1": "Website laten maken in België",
  "lead": "We bouwen websites en webshops voor ondernemers in Vlaanderen, Brussel en Wallonië, volledig online en in het Nederlands. Een vaste eindprijs vooraf, vanaf €495 voor een one-page website, geen btw erbij.",
  "secties": [
   ("Wat kost een website laten maken in België?", "<div class='scroll'><table class='tabel vergelijk'><tr><th>Soort</th><th>Markt in België</th><th>Collens Group</th></tr><tr><td>Professionele bedrijfswebsite</td><td>€2.000 tot €6.000</td><td>vanaf €995</td></tr><tr><td>Webshop</td><td>€4.000 tot €15.000 of meer</td><td>vanaf €1.950</td></tr><tr><td>One-page website</td><td>niet apart genoemd</td><td>vanaf €495</td></tr></table></div><p class='bron'>Bron marktbedragen: <a href='https://lunidev.com/nl/blog/website-kosten-2026-complete-prijsgids-belgie' rel='nofollow noopener'>Lunidev, prijsgids websites (2026)</a>. Onze prijzen zijn eindprijzen: er komt geen btw bij.</p>"),
   ("Waar moet je op letten bij een website in België?", "<ul><li><strong>Bedrijfsgegevens</strong>: in België hoort een webshop of zakelijke site gegevens als je ondernemingsnummer en, als je btw-plichtig bent, je btw-nummer te tonen. Wij zetten die netjes in de footer, maar jij levert de gegevens aan en blijft verantwoordelijk voor de juistheid.</li><li><strong>Betaalmethoden</strong>: in een Belgische webshop horen vaak Bancontact en kaartbetalingen thuis. Welke methoden mogelijk zijn hangt af van je betaalprovider; dat regelen we vooraf in de offerte.</li><li><strong>Privacy en cookies</strong>: een privacyverklaring hoort op je site, en bij het gebruik van tracking gelden de cookieregels.</li><li><strong>Taal</strong>: we schrijven in het Nederlands. Een Franstalige of Engelstalige versie bespreken we in de offerte.</li></ul><p>Dit is praktische informatie en geen juridisch advies. Laat bij twijfel je boekhouder of een jurist meekijken.</p>"),
   ("Hoe werken we samen op afstand?", "<p>We werken volledig online. Je stuurt je aanvraag, krijgt binnen 48 uur een gratis concept van je homepage en keurt het ontwerp en de vaste prijs goed. Daarna bouwen wij, test jij tussentijds en gaat de site live op jouw eigen domein. Je hoeft nergens naartoe te reizen en alles staat vooraf op papier: wat wel en niet in de prijs zit, hoe lang het duurt en wat eventuele externe kosten zijn, zoals een domeinnaam (meestal €10 tot €25 per jaar).</p>"),
   ("Welk pakket past bij jou?", "<ul><li><a href='website-laten-maken.html'>One-page website</a> (€495): alles op één pagina, klaar in 3–5 dagen. Voor wie snel online wil.</li><li><a href='website-laten-maken.html'>Bedrijfswebsite</a> (€995): tot 6 pagina's, klaar in 2–3 weken.</li><li><a href='webshop-laten-maken.html'>Webshop</a> (€1.950): tot 50 producten ingericht, klaar in 3–5 weken.</li></ul><p>Twijfel je? Doe de <a href='pakketkiezer.html'>pakketkiezer</a> of vraag het onze online adviseur.</p>")],
  "faq": [("Werken jullie ook voor Belgische bedrijven?", "Ja. We werken voor klanten in Nederland, België en wereldwijd, volledig online."),
          ("Wat kost een website in België?", "Volgens Lunidev (2026) kost een professionele bedrijfswebsite in België €2.000 tot €6.000 en een webshop €4.000 tot €15.000 of meer. Bij ons begint een bedrijfswebsite bij €995 en een webshop bij €1.950, eindprijzen zonder btw erbij."),
          ("Staat de btw erbij?", "Nee. Alle prijzen zijn eindprijzen: er komt geen btw bij."),
          ("Ben ik eigenaar van de website?", "Ja. De site, het domein en de inhoud staan op jouw naam.")],
  "offers": [("One-page website", 495), ("Bedrijfswebsite", 995), ("Webshop", 1950)],
  "rel": [("website-laten-maken.html", "Website laten maken"), ("webshop-laten-maken.html", "Webshop laten maken"), ("prijzen.html", "Alle prijzen")]}
NIEUW.append(BELGIE)
