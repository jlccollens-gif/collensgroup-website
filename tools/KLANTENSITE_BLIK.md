# Klantensite-blik (vaste controle voor elke site die wij voor klanten maken of nakijken)
Gebruik dit in elk project vóór oplevering, bij elke nieuwe klantsite en bij elke nacontrole. Eerst `python3 tools/sitecheck.py <url of map>` draaien, daarna de handmatige punten.

## Werkwijze
1. Alleen lezen en rapporteren. Niets wijzigen of publiceren zonder opdracht van de eigenaar.
2. Rapport in 🔴 moet opgelost vóór publicatie / 🟡 verbeteren / 🔵 handmatig verifiëren. Per punt: wat, waar (pagina), waarom, voorstel.
3. Alleen feiten uit de site zelf of de klant. Nooit reviews, cijfers, certificeringen, voorraad of levertijden verzinnen. Echt bewijs ontbreekt = zeggen en vragen, niet opvullen.

## Checklist
**A. Vertrouwen en eerlijkheid (altijd eerst)**
- Geen placeholdertekst ("tekst ter illustratie", "[adres volgt]", lorem, voorbeeldnamen).
- Eén btw-formulering die klopt ("incl. btw" of "geen btw erbij"; "excl. btw" betekent dat er btw bijkomt). Nooit door elkaar.
- Eén levertijd. Bij leverancier-/dropshipping de langste realistische levertijd; geen "2–4 werkdagen" naast "8–15 werkdagen".
- Claims die bewezen moeten zijn: bestseller, meest verkocht, handgemaakt, duurzaam, gratis, nr. 1, reviews/sterren, "nog maar X op voorraad". Geen nep-schaarste.
- Bedrijfsgegevens: de ondernemer beslist wat getoond wordt. Webshops: voorwaarden, privacy, retour/herroeping (14 dagen), contact en verkoperadres zijn verplicht. Wij tonen geen KvK-nummer als de eigenaar dat niet wil (besluit Jeffrey voor Collens Group).
- Foto's: rechten of licentie (leveranciersfoto's alleen met toestemming).
- Eigendom: site, domein en inhoud staan op naam van de klant; uitleg in een FAQ (niet als slogan).

**B. Vertrouwelijke gegevens**
- Geen inkoopprijzen, marges, sleutels, wachtwoorden of beheerdata in bestanden die iedereen kan downloaden (JS, JSON, HTML). Statische sites: alleen publieke gegevens meesturen.
- Beheerpagina's staan achter echte inlog of niet online.

**C. Inhoud en conversie**
- Per pagina één duidelijke belofte (H1), prijs of prijsrange, wat erin zit en wat niet, hoe het werkt (stappen), veelgestelde vragen, één duidelijke volgende stap (CTA) die bovenaan én halverwege terugkomt.
- Bewijs: echte projecten, echte reviews, echte voorbeelden (conceptsites duidelijk als voorbeeld labelen).
- Geen dunne pagina's voor commerciële zoektermen (richt 600+ woorden met proces en FAQ).

**D. Vindbaarheid (SEO)**
- Eén h1, unieke titel (≤60 tekens) en unieke meta description (70–160) per pagina; canonical; alt-tekst bij betekenisvolle beelden.
- Structured data waar passend (Organization, Product, FAQPage, Article). Webshops: elk product een eigen URL met eigen titel/beschrijving en Product-schema.
- Interne links tussen verwante pagina's; geen twee pagina's voor dezelfde zoekterm zonder duidelijk onderscheid.
- noindex alleen bewust (concepten/beheer).

**E. Techniek en gebruik**
- Mobiel (360 px) zonder horizontaal scrollen of afgesneden tekst; snel; geen kapotte links.
- Formulieren werken en sturen naar een bestaand adres; bedanktpagina of bevestiging.
- Meting aanwezig (cookieloos zoals GoatCounter of Search Console), anders weten we niet wat het oplevert.

## Wat de code wel en niet doet
`tools/sitecheck.py` vindt automatisch: placeholders, btw-tegenstrijdigheid, meerdere levertijden, vertrouwelijke sleutels in scripts, ontbrekende voorwaarden/privacy/retour/contact bij webshops, titel/meta/h1/alt/canonical/structured-data-problemen, dunne pagina's, claims om te verifiëren. Niet automatisch: of een claim waar is, of foto's rechten hebben, of de tekst goed is, of het ontwerp klopt. Dat blijft handmatig.
