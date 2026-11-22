"""Nieuwe pagina's (18-11-2026): prijzen, over ons, pakketkiezer, bedankt, vergelijkpagina's en artikelen.
Alleen feiten die al op de site staan (prijzen, doorlooptijden, werkwijze, eigen apps). Marktbedragen met bron."""
import datetime

NOINDEX = '<meta name="robots" content="noindex, follow">'


def bouw(page, e, faq_html, faq_ld, DIENSTEN, PAKKETTEN, VANDAAG, CONFIG):
    pages, items = [], []
    art = lambda kop: {"@type": "Article", "headline": kop, "dateModified": "@@BIJGEWERKT_ISO@@", "datePublished": "@@GEPUBLICEERD_ISO@@", "inLanguage": "nl", "author": {"@id": "#org"}, "publisher": {"@id": "#org"}}
    cta = lambda txt="Vraag je gratis concept aan": f'<p style="margin-top:24px"><a class="knop geel" href="index.html#contact">{txt}</a></p>'
    d = {x["slug"]: x for x in DIENSTEN}
    prijs = lambda p: "€" + f"{p:,}".replace(",", ".")

    # ---------- PRIJZEN ----------
    rijen = ""
    for slug in ("website-laten-maken", "game-laten-maken", "ai-automatisering"):
        x = d[slug]
        for n, p, t, it in x["pakketten"]:
            rijen += f'<tr><td><a href="{slug}.html">{e(n)}</a><small>{e(" · ".join(it[:3]))}</small></td><td>{e(x["kort"])}</td><td>{e(t)}</td><td>vanaf {prijs(p)}</td></tr>'
        for n, p, s in x["extra"]:
            rijen += f'<tr><td>{e(n)}<small>{e(s)}</small></td><td>{e(x["kort"])}</td><td></td><td>{e(p)}</td></tr>'
    app_rijen = ('<tr><td><a href="app-laten-maken-kosten.html">Basis / MVP-app</a><small>Tot 5 schermen, publicatieklaar voor iOS of Android</small></td><td>Apps</td><td>3–5 weken</td><td>vanaf €3.150</td></tr>'
                 '<tr><td><a href="app-laten-maken-kosten.html">Standaard-app</a><small>5 tot 12 schermen, accounts, database, pushmeldingen</small></td><td>Apps</td><td>6–10 weken</td><td>vanaf €6.750</td></tr>'
                 '<tr><td><a href="app-laten-maken-kosten.html">Maatwerk / Pro-app</a><small>12+ schermen, backend, betalingen, rollen</small></td><td>Apps</td><td>10–16+ weken</td><td>vanaf €13.050</td></tr>'
                 '<tr><td>Ontwikkeling per uur<small>Uitbreidingen en losse opdrachten</small></td><td>Apps</td><td></td><td>€67,50 per uur</td></tr>'
                 '<tr><td>Onderhoud Basis<small>Monitoring, kritieke bugfixes, kleine updates</small></td><td>Apps</td><td></td><td>€85,50 per maand</td></tr>'
                 '<tr><td>Onderhoud Groei &amp; Support<small>Alles uit Basis, tot 4 uur aanpassingen, voorrang bij storingen</small></td><td>Apps</td><td></td><td>€265,50 per maand</td></tr>')
    faq_p = [("Staat de btw erbij?", "Nee. Alle prijzen zijn eindprijzen: er komt geen btw bij."),
             ("Wat betekent 'vanaf'?", "Bij 'vanaf' hoort het pakket zoals beschreven. Wijkt jouw project daarvan af, dan krijg je vooraf een vaste prijs op maat. Meerwerk doen we alleen na jouw akkoord."),
             ("Welke kosten komen er buiten jullie prijs bij?", "Externe kosten betaal je rechtstreeks aan de partij: een domeinnaam (meestal €10 tot €25 per jaar), Apple Developer Account ($99 per jaar), Google Play ($25 eenmalig) en eventuele hosting. Ze staan vooraf in de offerte."),
             ("Hoe betaal ik?", "Bij apps in drie delen: 40% bij akkoord, 40% bij een goedgekeurde testversie en 20% bij oplevering. De betaling voor andere diensten staat vooraf in je offerte."),
             ("Is er echt een gratis concept?", "Ja. Je krijgt binnen 48 uur een gratis concept, zonder verplichtingen.")]
    pages.append(page("prijzen.html", "Prijzen website, app, game en AI | Collens Group",
        "Alle prijzen op een rij: website vanaf €495, webshop vanaf €1.950, app vanaf €3.150, game vanaf €1.950 en AI vanaf €395. Eindprijzen, geen btw erbij.",
        f'''<article class="tekst breed"><h1>Prijzen: website, app, game en AI laten maken</h1>
<p class="lead2">Alle prijzen op één plek. Het zijn eindprijzen: er komt geen btw bij. Je krijgt vooraf een vaste prijs en binnen 48 uur een gratis concept.</p>
<div class="scroll"><table class="tabel vergelijk"><tr><th>Pakket</th><th>Soort</th><th>Klaar in</th><th>Prijs</th></tr>{rijen}{app_rijen}</table></div>
<p class="noot">Bij &ldquo;vanaf&rdquo; hoort het pakket zoals beschreven. Wijkt jouw project daarvan af, dan krijg je vooraf een vaste prijs op maat.</p>
{cta()}
<h2>Niet zeker welk pakket past?</h2><p>Beantwoord drie korte vragen in de <a href="pakketkiezer.html">pakketkiezer</a> en zie direct wat bij je past, of vraag het de online adviseur rechtsonder.</p>
<h2>Waarom zijn onze prijzen lager?</h2><p>We bouwen met moderne tools en veel automatisering en geven dat voordeel door. Een eenvoudige website kost in Nederland volgens <a href="https://trustoo.nl/kosten/webdesign-kosten/" rel="nofollow noopener">Trustoo</a> gemiddeld €500 tot €2.000 en een geavanceerde website €2.000 tot €5.000. Voor een eenvoudige app noemen kostengidsen €5.000 tot €25.000 (<a href="https://searchlab.nl/kosten/wat-kost-een-app-laten-maken" rel="nofollow noopener">Searchlab, 2026</a>).</p>
<h2>Veelgestelde vragen over prijzen</h2>{faq_html(faq_p)}{cta("Vraag een vaste prijs aan")}
<p class="bron" style="margin-top:22px">Zie ook: <a href="website-laten-maken.html">Website laten maken</a> · <a href="app-laten-maken-kosten.html">Wat kost een app?</a> · <a href="game-laten-maken.html">Game laten maken</a> · <a href="ai-automatisering.html">AI en automatisering</a></p></article>''',
        crumbs=[("Home", "index.html"), ("Prijzen", "prijzen.html")], extra_ld=[faq_ld(faq_p)]))

    # ---------- OVER ONS ----------
    pages.append(page("over-ons.html", "Over ons: werkwijze en eigen projecten | Collens Group",
        "Collens Group maakt websites, apps, games en AI met een vaste prijs. Bekijk onze werkwijze en eigen projecten: LubbyC, Koffer Vol! en Eiland Express.",
        f'''<article class="tekst breed"><h1>Over Collens Group</h1>
<p class="lead2">We maken websites, apps, games en AI-oplossingen voor ondernemers in Nederland, België en de rest van de wereld, met een vaste prijs vooraf en een gratis concept voordat je iets betaalt.</p>
<h2>Wat we doen</h2><p>Collens Group is een klein, onafhankelijk digitaal bedrijf. We bouwen <a href="website-laten-maken.html">websites en webshops</a>, <a href="app-laten-maken-kosten.html">apps voor iPhone en Android</a>, <a href="game-laten-maken.html">games</a> en <a href="ai-automatisering.html">AI-automatisering en chatbots</a>. We werken volledig online, zodat je niet hoeft te reizen en wij onze prijzen laag kunnen houden.</p>
<h2>Wie zit erachter?</h2><p>Collens Group is opgericht door Jeffrey Collens. Hij bouwt met moderne AI-tools en controleert elk concept, elke tekst en elke oplevering zelf voordat het naar een klant gaat. Je mailt dus rechtstreeks met de maker, niet met een accountmanager.</p>
<h2>Waar we werken</h2><p>Overal. We werken volledig online, per mail en video, met ondernemers in Nederland en België en daarbuiten, bijvoorbeeld in het Verenigd Koninkrijk, Ierland, de Verenigde Staten, Canada, Australië en Nieuw-Zeeland. Je kunt met ons in het Nederlands of het Engels werken. De prijzen zijn overal dezelfde eindprijzen in euro.</p>
<h2>Zo werken we</h2><ul>
<li><strong>Vaste prijs vooraf.</strong> Je weet wat je betaalt voordat we beginnen. Meerwerk doen we alleen na jouw akkoord.</li>
<li><strong>Eerst een gratis concept.</strong> Binnen 48 uur zie je hoe het eruit kan zien, zonder verplichtingen.</li>
<li><strong>Eindprijzen.</strong> Er komt geen btw bij.</li>
<li><strong>Jij blijft eigenaar.</strong> De site, het domein en de inhoud staan op jouw naam; apps staan in je eigen Apple- en Google-account en de broncode is na de laatste betaling van jou.</li>
<li><strong>Eerlijk over wat we niet doen.</strong> We bouwen geen grote 3D-games of online multiplayer, en we werken niet op locatie.</li></ul>
<h2>Wat we zelf bouwden</h2><p>Wat we voor onszelf maken, maken we ook voor jou. Zo testen we onze werkwijze eerst op onszelf:</p>
<ul><li><a href="app-lubbyc.html"><strong>LubbyC</strong></a>, een reisapp om reizigers in de buurt te ontmoeten en samen iets te plannen.</li>
<li><a href="app-koffer-vol.html"><strong>Koffer Vol!</strong></a>, een inpakpuzzel met 100 levels in 10 landen.</li>
<li><a href="app-eiland-express.html"><strong>Eiland Express</strong></a>, een 3D-rijgame met een songthaew op een tropisch eiland.</li>
<li><a href="app-manu-en-khanun.html"><strong>Manu en Khanun</strong></a>, een animatieserie voor kinderen.</li></ul>
<p>Op de <a href="apps.html">projectenpagina</a> zie je hoe ze eruitzien en in welke fase ze zijn.</p>
<h2>Contact</h2><p>Mail ons op <a href="mailto:{CONFIG["email"]}">{CONFIG["email"]}</a> of gebruik het <a href="index.html#contact">aanvraagformulier</a>. Je krijgt binnen 48 uur een reactie.</p>
{cta()}</article>''',
        crumbs=[("Home", "index.html"), ("Over ons", "over-ons.html")],
        extra_ld=[{"@type": "AboutPage", "name": "Over Collens Group", "about": {"@id": "#org"}}, {"@type": "Person", "name": "Jeffrey Collens", "jobTitle": "Oprichter", "worksFor": {"@id": "#org"}}]))

    # ---------- BEDANKT (niet indexeren) ----------
    pages.append(page("bedankt.html", "Bedankt voor je aanvraag | Collens Group",
        "Je aanvraag bij Collens Group is ontvangen. Dit is wat er nu gebeurt en wanneer je van ons hoort.",
        '''<article class="tekst"><h1 id="bedankt-kop">Bedankt, je aanvraag is ontvangen</h1>
<p class="lead2">Binnen 48 uur krijg je een reactie op het e-mailadres dat je hebt ingevuld.</p>
<h2>Wat gebeurt er nu?</h2><ol><li>We lezen je aanvraag en sturen je een paar korte vragen als er iets onduidelijk is.</li><li>Je krijgt een gratis concept, zonder verplichtingen.</li><li>Bevalt het, dan krijg je een vaste prijs en planning. Pas na jouw akkoord beginnen we.</li></ol>
<p>Zie je niets binnen 48 uur? Kijk dan in je ongewenste e-mail of mail ons rechtstreeks via <a href="mailto:''' + CONFIG["email"] + '''">''' + CONFIG["email"] + '''</a>.</p>
<p style="margin-top:24px"><a class="knop" href="index.html">Terug naar de startpagina</a> <a class="knop" href="apps.html" style="margin-left:8px">Bekijk onze eigen apps</a></p></article>
<script>try{const n=new URLSearchParams(location.search).get("n");if(n)document.getElementById("bedankt-kop").textContent="Bedankt "+n+", je aanvraag is ontvangen"}catch(_){}</script>''',
        extra_head=NOINDEX, crumbs=[("Home", "index.html")]))

    # ---------- PAKKETKIEZER ----------
    pages.append(page("pakketkiezer.html", "Pakketkiezer: welk pakket past bij mij? | Collens Group",
        "Beantwoord drie korte vragen en zie welk pakket bij je past, met prijs en doorlooptijd. Eindprijzen vanaf €395, geen btw erbij.",
        '''<article class="tekst breed"><h1>Welk pakket past bij mij?</h1>
<p class="lead2">Drie korte vragen. Je ziet direct welk pakket het beste past, met richtprijs en doorlooptijd. Het advies is een richting; je krijgt altijd eerst een gratis concept en een vaste prijs op maat.</p>
<form id="kiezer" class="kiezer" onsubmit="return false">
<fieldset><legend>1. Wat wil je laten maken?</legend>
<label><input type="radio" name="soort" value="website" checked> Een website</label>
<label><input type="radio" name="soort" value="webshop"> Een webshop</label>
<label><input type="radio" name="soort" value="app"> Een app voor iPhone en Android</label>
<label><input type="radio" name="soort" value="game"> Een game</label>
<label><input type="radio" name="soort" value="ai"> AI of automatisering</label></fieldset>
<fieldset id="v2"><legend>2. Hoe groot is het ongeveer?</legend><div id="v2opties"></div></fieldset>
<fieldset><legend>3. Hoe snel wil je live?</legend>
<label><input type="radio" name="tempo" value="snel" checked> Zo snel mogelijk</label>
<label><input type="radio" name="tempo" value="gewoon"> Binnen een paar weken is prima</label>
<label><input type="radio" name="tempo" value="rustig"> Geen haast</label></fieldset></form>
<section id="advies" class="kiezer-advies" aria-live="polite"></section>
<script>
const SOORTEN={
 website:{v:["Alles op één pagina","Een paar pagina's (tot 6)"],r:[{n:"One-page website",p:495,t:"3–5 dagen",u:"website-laten-maken"},{n:"Bedrijfswebsite",p:995,t:"2–3 weken",u:"website-laten-maken"}]},
 webshop:{v:["Tot ongeveer 50 producten","Meer dan 50 producten of speciale wensen"],r:[{n:"Webshop",p:1950,t:"3–5 weken",u:"webshop-laten-maken"},{n:"Webshop op maat (prijs na intake)",p:1950,t:"in overleg",u:"webshop-laten-maken"}]},
 app:{v:["Een eenvoudig idee testen (tot 5 schermen)","Een complete app met accounts en database","Een groot platform met betalingen en beheer"],r:[{n:"Basis / MVP-app",p:3150,t:"3–5 weken",u:"app-laten-maken-kosten"},{n:"Standaard-app",p:6750,t:"6–10 weken",u:"app-laten-maken-kosten"},{n:"Maatwerk / Pro-app",p:13050,t:"10–16+ weken",u:"app-laten-maken-kosten"}]},
 game:{v:["Een kleine game voor een merk of actie","Een casual game","Een 2D-game met levels"],r:[{n:"Merkgame",p:1950,t:"in overleg",u:"game-laten-maken"},{n:"Casual game",p:4950,t:"in overleg",u:"game-laten-maken"},{n:"2D-game met levels",p:9950,t:"in overleg",u:"game-laten-maken"}]},
 ai:{v:["Een taak automatiseren","Een chatbot op mijn website","Een assistent met meerdere koppelingen"],r:[{n:"Automatisering",p:395,t:"2–5 dagen",u:"ai-automatisering"},{n:"AI-chatbot",p:995,t:"ongeveer 1 week",u:"chatbot-laten-maken"},{n:"AI-assistent",p:1950,t:"in overleg",u:"ai-automatisering"}]}};
const f=document.getElementById("kiezer"),o=document.getElementById("v2opties"),a=document.getElementById("advies");
const eur=n=>"€"+n.toLocaleString("nl-NL");
function opties(){const s=f.soort.value;o.innerHTML=SOORTEN[s].v.map((t,i)=>`<label><input type="radio" name="groot" value="${i}" ${i===0?"checked":""}> ${t}</label>`).join("")}
function toon(){const s=f.soort.value,i=+(f.groot&&f.groot.value||0),r=SOORTEN[s].r[Math.min(i,SOORTEN[s].r.length-1)];
 const idee=encodeURIComponent("Ik heb interesse in: "+r.n+" ("+eur(r.p)+"). Mijn wens: "),pk=({website:"Website",webshop:"Webshop",app:"App",game:"Game",ai:"AI of automatisering"})[s];
 const tempo=f.tempo.value==="snel"?" Je wilt snel live; vertel in je aanvraag je gewenste datum.":"";
 a.innerHTML=`<h2>Ons advies: ${r.n}</h2><p class="kiezer-prijs">vanaf ${eur(r.p)} <small>eindprijs, geen btw erbij</small></p><p>Klaar in ${r.t}.${tempo}</p><p><a class="knop geel" href="index.html?pakket=${encodeURIComponent(pk)}&idee=${idee}#contact">Vraag je gratis concept aan</a> <a class="knop" href="${r.u}.html" style="margin-left:8px">Lees meer over dit pakket</a></p><p class="noot">Dit is een richting. Je krijgt altijd eerst een gratis concept en een vaste prijs op maat.</p>`}
f.addEventListener("change",e=>{if(e.target.name==="soort")opties();toon()});opties();toon();
</script></article>''',
        crumbs=[("Home", "index.html"), ("Pakketkiezer", "pakketkiezer.html")]))

    # ---------- KOSTENCALCULATOR ----------
    pages.append(page("kostencalculator.html", "Kostencalculator website en webshop | Collens Group",
        "Reken zelf uit wat je website of webshop kost: kies het type, extra pagina's en onderhoud. Eindprijzen, geen btw erbij.",
        '''<article class="tekst breed"><h1>Kostencalculator website en webshop</h1>
<p class="lead2">Stel je website samen en zie direct wat het kost. Alle bedragen zijn eindprijzen: er komt geen btw bij. Je krijgt altijd eerst een gratis concept en een vaste prijs op maat.</p>
<form id="calc" class="kiezer" onsubmit="return false">
<fieldset><legend>1. Wat heb je nodig?</legend>
<label><input type="radio" name="type" value="495|3–5 dagen|One-page website" checked> One-page website (alles op één pagina)</label>
<label><input type="radio" name="type" value="995|2–3 weken|Bedrijfswebsite (tot 6 pagina's)"> Bedrijfswebsite (tot 6 pagina's)</label>
<label><input type="radio" name="type" value="1950|3–5 weken|Webshop (tot 50 producten)"> Webshop (tot 50 producten)</label></fieldset>
<fieldset><legend>2. Extra pagina's</legend>
<label>Aantal extra pagina's: <input type="number" id="extra" min="0" max="30" value="0" style="width:80px"> <small>(€95 per pagina)</small></label></fieldset>
<fieldset><legend>3. Onderhoud</legend>
<label><input type="radio" name="zorg" value="0" checked> Geen onderhoud, ik regel het zelf</label>
<label><input type="radio" name="zorg" value="29"> Wij houden de website bij (€29 per maand)</label></fieldset></form>
<section id="uitkomst" class="kiezer-advies" aria-live="polite"></section>
<script>
const c=document.getElementById("calc"),u=document.getElementById("uitkomst"),x=document.getElementById("extra");
const eur=n=>"€"+n.toLocaleString("nl-NL");
function reken(){const [p,t,n]=c.type.value.split("|"),ex=Math.max(0,Math.min(30,+x.value||0)),m=+c.zorg.value,tot=+p+ex*95;
 const idee=encodeURIComponent("Ik heb interesse in: "+n+(ex?" met "+ex+" extra pagina's":"")+(m?" en onderhoud":"")+" (richtprijs "+eur(tot)+"). Mijn wens: ");
 u.innerHTML=`<h2>Jouw richtprijs</h2><p class="kiezer-prijs">${eur(tot)} <small>eenmalig, eindprijs, geen btw erbij</small></p>${m?`<p>Plus ${eur(m)} per maand voor onderhoud.</p>`:""}<p>${n}${ex?` + ${ex} extra pagina's`:""}. Klaar in ongeveer ${t}.</p><p><a class="knop geel" href="index.html?pakket=Website&idee=${idee}#contact">Vraag je gratis concept aan</a> <a class="knop" href="prijzen.html" style="margin-left:8px">Alle prijzen</a></p><p class="noot">Dit is een richtprijs. Externe kosten zoals een domeinnaam staan altijd apart in je offerte. Niet zeker wat past? Probeer de <a href="pakketkiezer.html">pakketkiezer</a>.</p>`}
c.addEventListener("input",reken);reken();
</script></article>''',
        crumbs=[("Home", "index.html"), ("Kostencalculator", "kostencalculator.html")]))

    # ---------- VERGELIJK: APP OF WEBSITE ----------
    faq_aw = [("Wat is goedkoper: een app of een website?", "Een website. Bij ons begint een website bij €495 en een app bij €3.150, allemaal eindprijzen zonder btw erbij."),
              ("Kan een website ook op een telefoon werken?", "Ja. Elke website die wij bouwen is mobielvriendelijk. Bezoekers hoeven niets te installeren."),
              ("Wanneer heb ik toch een app nodig?", "Als gebruikers dagelijks terugkomen, een account nodig hebben, meldingen moeten krijgen of functies van de telefoon gebruiken, zoals de camera of locatie."),
              ("Kan ik eerst met een website beginnen?", "Ja. Veel ondernemers testen hun idee eerst met een website of een kleine app (MVP) en breiden later uit.")]
    pages.append(page("app-of-website.html", "App of website: wat past bij jou? | Collens Group",
        "App of website laten maken? Zo kies je: kosten, doorlooptijd en wanneer een app echt nodig is. Website vanaf €495, app vanaf €3.150, eindprijzen.",
        f'''<article class="tekst breed"><h1>App of website: wat past bij jou?</h1>
<p class="lead2">Kort antwoord: begin met een website, tenzij je gebruikers dagelijks terugkomen, meldingen nodig hebben of functies van de telefoon gebruiken. Dan loont een app.</p>
<p class="bijgewerkt">Bijgewerkt op @@BIJGEWERKT_NL@@</p>
<h2>De verschillen op een rij</h2>
<div class="scroll"><table class="tabel vergelijk"><tr><th></th><th>Website</th><th>App</th></tr>
<tr><td>Kosten bij ons</td><td>vanaf €495</td><td>vanaf €3.150</td></tr>
<tr><td>Doorlooptijd</td><td>3–5 dagen tot 3–5 weken</td><td>3–5 weken tot 16+ weken</td></tr>
<tr><td>Gevonden via Google</td><td>Ja, dat is de kracht</td><td>Beperkt: mensen zoeken in de App Store of Google Play</td></tr>
<tr><td>Installeren</td><td>Niet nodig</td><td>Ja, via de store</td></tr>
<tr><td>Meldingen en telefoonfuncties</td><td>Beperkt</td><td>Ja, zoals pushmeldingen, camera en locatie</td></tr>
<tr><td>Doorlopende kosten</td><td>Domein en eventueel onderhoud vanaf €29 per maand</td><td>Apple $99 per jaar, Google $25 eenmalig, onderhoud vanaf €85,50 per maand</td></tr></table></div>
<h2>Kies een website als…</h2><ul><li>je gevonden wilt worden door mensen die iets zoeken in Google;</li><li>je je bedrijf, aanbod en prijzen wilt tonen en aanvragen wilt ontvangen;</li><li>je snel en goedkoop wilt starten;</li><li>je een <a href="webshop-laten-maken.html">webshop</a> wilt zonder dat klanten iets installeren.</li></ul>
<h2>Kies een app als…</h2><ul><li>gebruikers vaak terugkomen en een eigen account hebben;</li><li>je pushmeldingen, de camera of locatie nodig hebt;</li><li>de app zelf het product is, zoals onze reisapp <a href="app-lubbyc.html">LubbyC</a>.</li></ul>
<h2>Twijfel je? Begin klein</h2><p>Test je idee eerst met een website of een <a href="mvp-app-laten-maken.html">MVP-app</a>, het kleinste product waarmee echte gebruikers je idee kunnen proberen. Pas als daar vraag naar is, bouw je uit. Wil je weten wat jouw idee kost, doe dan de <a href="pakketkiezer.html">pakketkiezer</a> of lees <a href="app-laten-maken-kosten.html">wat een app kost</a>.</p>
<h2>Veelgestelde vragen</h2>{faq_html(faq_aw)}{cta()}
<p class="bron" style="margin-top:22px">Zie ook: <a href="website-laten-maken.html">Website laten maken</a> · <a href="app-laten-maken-kosten.html">App laten maken</a> · <a href="prijzen.html">Alle prijzen</a></p></article>''',
        crumbs=[("Home", "index.html"), ("App of website", "app-of-website.html")], extra_ld=[art("App of website: wat past bij jou?"), faq_ld(faq_aw)]))
    items.append(("app-of-website.html", "App of website: wat past bij jou?", "Kosten, doorlooptijd en wanneer een app echt nodig is, naast elkaar gezet."))

    # ---------- VERGELIJK: WIX OF LATEN MAKEN ----------
    faq_wx = [("Is een zelfbouw-website goedkoper?", "Aan de start vaak wel, zeker als je je tijd niet meetelt. Reken ook de maandelijkse abonnementskosten van de bouwer mee en hoeveel uren je zelf kwijt bent aan ontwerp, teksten en techniek."),
              ("Kan ik mijn site later meenemen naar een andere partij?", "Dat hangt af van de bouwer. Controleer vooraf of je je site en domein kunt meenemen. Bij ons staan site, domein en inhoud op jouw naam."),
              ("Wat kost een website laten maken bij Collens Group?", "Een one-page website begint bij €495, een bedrijfswebsite bij €995 en een webshop bij €1.950, allemaal eindprijzen zonder btw erbij."),
              ("Kan ik beginnen met zelf bouwen en later laten maken?", "Ja, dat kan. Houd je teksten en foto's bij, dan hoef je ze later niet opnieuw te maken.")]
    pages.append(page("zelf-website-bouwen-of-laten-maken.html", "Zelf een website bouwen of laten maken? | Collens Group",
        "Zelf een website bouwen (Wix, WordPress, Squarespace) of laten maken? Kosten, tijd, eigendom en vindbaarheid vergeleken. Website laten maken vanaf €495.",
        f'''<article class="tekst breed"><h1>Zelf een website bouwen of laten maken?</h1>
<p class="lead2">Een websitebouwer als Wix, Squarespace of WordPress is een prima keuze als je tijd hebt en zin om het te leren. Laten maken loont als je snel en professioneel online wilt zonder er zelf uren aan kwijt te zijn.</p>
<p class="bijgewerkt">Bijgewerkt op @@BIJGEWERKT_NL@@</p>
<h2>De afwegingen</h2>
<div class="scroll"><table class="tabel vergelijk"><tr><th></th><th>Zelf bouwen</th><th>Laten maken</th></tr>
<tr><td>Startkosten</td><td>Laag, vaak een abonnement per maand</td><td>Eenmalig, bij ons vanaf €495</td></tr>
<tr><td>Jouw tijd</td><td>Veel: ontwerp, teksten, techniek en zoekmachine-instellingen</td><td>Weinig: jij levert de inhoud, wij bouwen</td></tr>
<tr><td>Resultaat</td><td>Hangt af van je ervaring en de gekozen template</td><td>Afgestemd op jouw bedrijf en op Google</td></tr>
<tr><td>Eigendom en meenemen</td><td>Controleer de voorwaarden van de bouwer</td><td>Site, domein en inhoud staan op jouw naam</td></tr>
<tr><td>Hulp bij problemen</td><td>Zelf uitzoeken of via de helpdesk van de bouwer</td><td>Onderhoud optioneel vanaf €29 per maand</td></tr></table></div>
<p>Marktprijzen: volgens Trustoo kost een eenvoudige website in Nederland gemiddeld €500 tot €2.000 (<a href="https://trustoo.nl/kosten/webdesign-kosten/" rel="nofollow noopener">Trustoo, november 2026</a>). Een website laten maken bij ons begint bij €495.</p>
<h2>Zelf bouwen past als…</h2><ul><li>je plezier hebt in het uitzoeken en de tijd er voor neemt;</li><li>je site eenvoudig blijft en niet de basis is van je omzet;</li><li>je prima leeft met een standaardontwerp.</li></ul>
<h2>Laten maken past als…</h2><ul><li>je snel een professionele site wilt, bijvoorbeeld een one-page website in 3–5 dagen;</li><li>je gevonden wilt worden in Google en de technische basis goed wilt hebben;</li><li>je je tijd liever aan je bedrijf besteedt.</li></ul>
<h2>Waar je op moet letten, wat je kiest</h2><ul><li><strong>Eigendom:</strong> wie is eigenaar van het domein en de site?</li><li><strong>Totale kosten:</strong> abonnement, domein, extra functies en je eigen uren.</li><li><strong>Meenemen:</strong> kun je de site later verhuizen?</li><li><strong>Wat zit er niet in de prijs:</strong> vraag het vooraf.</li></ul>
<p>Meer hierover lees je in <a href="website-laten-maken-afspraken.html">acht dingen die je vooraf afspreekt met je websitebouwer</a>.</p>
<h2>Veelgestelde vragen</h2>{faq_html(faq_wx)}{cta()}</article>''',
        crumbs=[("Home", "index.html"), ("Zelf bouwen of laten maken", "zelf-website-bouwen-of-laten-maken.html")], extra_ld=[art("Zelf een website bouwen of laten maken?"), faq_ld(faq_wx)]))
    items.append(("zelf-website-bouwen-of-laten-maken.html", "Zelf een website bouwen of laten maken?", "Wix, Squarespace of WordPress tegenover laten maken: kosten, tijd, eigendom en vindbaarheid."))

    # ---------- ARTIKEL: 8 AFSPRAKEN ----------
    faq_af = [("Wat moet er in een offerte voor een website staan?", "De prijs en of daar btw bij komt, wat wel en niet inbegrepen is, de levertijd, wie eigenaar is van site en domein, en de kosten na oplevering zoals hosting en onderhoud."),
              ("Moet ik een voorschot betalen?", "Dat is gebruikelijk bij grotere opdrachten, maar spreek vooraf af wanneer je betaalt en wat je dan gezien hebt. Bij ons zie je eerst een gratis concept.")]
    pages.append(page("website-laten-maken-afspraken.html", "Website laten maken: 8 afspraken vooraf | Collens Group",
        "Acht dingen die je vooraf afspreekt als je een website laat maken: prijs, btw, eigendom, levertijd, hosting, onderhoud, teksten en vindbaarheid.",
        f'''<article class="tekst breed"><h1>Website laten maken: 8 afspraken die je vooraf vastlegt</h1>
<p class="lead2">De meeste teleurstellingen bij een nieuwe website zijn geen kwestie van ontwerp, maar van afspraken die niemand vooraf maakte. Dit zijn de acht dingen waar je naar vraagt voordat je tekent.</p>
<p class="bijgewerkt">Bijgewerkt op @@BIJGEWERKT_NL@@</p>
<h2>1. Wat kost het, en staat de btw erbij?</h2><p>Vraag om één eindbedrag. Prijzen zonder btw lijken lager dan ze zijn. Bij Collens Group zijn alle prijzen eindprijzen: er komt geen btw bij.</p>
<h2>2. Wat zit er wel en niet in de prijs?</h2><p>Aantal pagina's, teksten, foto's, formulieren, koppelingen en aanpassingsrondes. Wat niet genoemd wordt, kost meestal extra. Laat het opschrijven.</p>
<h2>3. Wie is eigenaar van de website en het domein?</h2><p>De site, het domein en de inhoud horen op jouw naam te staan. Zo zit je niet vast aan één partij en kun je later verhuizen.</p>
<h2>4. Hoe lang duurt het?</h2><p>Vraag naar een datum, en wat jij moet aanleveren om die te halen. Bij ons is een one-page website meestal in 3–5 dagen klaar, een bedrijfswebsite in 2–3 weken en een webshop in 3–5 weken, afhankelijk van hoe snel teksten en foto's binnenkomen.</p>
<h2>5. Wat kost het na oplevering?</h2><p>Een domeinnaam kost meestal €10 tot €25 per jaar. Hosting kan voor kleine sites gratis zijn. Onderhoud is optioneel, bij ons vanaf €29 per maand. Vraag altijd naar de jaarlijkse kosten.</p>
<h2>6. Wie levert teksten en foto's?</h2><p>Meestal levert de ondernemer de kern en maakt de bouwer er goede websiteteksten van. Spreek af wie wat doet, en dat je alleen foto's gebruikt waarvoor je de rechten hebt.</p>
<h2>7. Wordt de site goed gevonden?</h2><p>Een goede bouwer levert een snelle, mobielvriendelijke site met de technische basis die Google verwacht. Een toppositie kan niemand garanderen. Wees wantrouwig bij beloftes daarover.</p>
<h2>8. Wat gebeurt er als je niet tevreden bent?</h2><p>Vraag naar aanpassingsrondes en naar wat er gebeurt als het resultaat niet bevalt. Bij ons zie je eerst een gratis concept, zodat je geen risico loopt voordat je kiest.</p>
<h2>Veelgestelde vragen</h2>{faq_html(faq_af)}
<p>Meer weten over prijzen? Bekijk <a href="prijzen.html">alle prijzen</a> of lees <a href="zelf-website-bouwen-of-laten-maken.html">zelf bouwen of laten maken</a>.</p>{cta()}</article>''',
        crumbs=[("Home", "index.html"), ("8 afspraken", "website-laten-maken-afspraken.html")], extra_ld=[art("Website laten maken: 8 afspraken die je vooraf vastlegt"), faq_ld(faq_af)]))
    items.append(("website-laten-maken-afspraken.html", "Website laten maken: 8 afspraken vooraf", "Prijs, btw, eigendom, levertijd, hosting, onderhoud, teksten en vindbaarheid: waar je vooraf naar vraagt."))

    # ---------- ARTIKEL: WAT KOST EEN WEBSITE ----------
    faq_k = [("Wat kost een website laten maken gemiddeld?", "Volgens Trustoo kost een eenvoudige website in Nederland gemiddeld €500 tot €2.000. Bij ons begint een one-page website bij €495 en een bedrijfswebsite bij €995, eindprijzen zonder btw erbij."),
             ("Wat kost een website per jaar?", "Naast de bouw betaal je een domeinnaam (meestal €10 tot €25 per jaar). Hosting kan voor kleine sites gratis. Onderhoud is optioneel, bij ons vanaf €29 per maand."),
             ("Wat kost een website in België?", "Volgens Lunidev (2026) kost een professionele bedrijfswebsite in België €2.000 tot €6.000. Lees meer op onze pagina over een website laten maken in België.")]
    pages.append(page("wat-kost-een-website.html", "Wat kost een website laten maken in 2026? | Collens Group",
        "Wat kost een website laten maken in 2026? Marktprijzen voor freelancers en bureaus, bijkomende kosten per jaar en onze vaste prijzen vanaf €495.",
        f'''<article class="tekst breed"><h1>Wat kost een website laten maken in 2026?</h1>
<p class="lead2">Kort antwoord: een eenvoudige zakelijke website kost bij Nederlandse freelancers meestal €800 tot €3.000 en bij bureaus €2.500 tot €12.000. Bij Collens Group begint een one-page website bij €495 en een bedrijfswebsite bij €995, allemaal eindprijzen.</p>
<p class="bijgewerkt">Bijgewerkt op @@BIJGEWERKT_NL@@</p>
<h2>Wat kost het op de markt?</h2>
<div class="scroll"><table class="tabel vergelijk"><tr><th>Soort</th><th>Marktprijs</th><th>Bron</th></tr>
<tr><td>Eenvoudige website</td><td>€500 tot €2.000</td><td><a href="https://trustoo.nl/kosten/webdesign-kosten/" rel="nofollow noopener">Trustoo (nov. 2026)</a></td></tr>
<tr><td>Geavanceerde website</td><td>€2.000 tot €5.000</td><td><a href="https://trustoo.nl/kosten/webdesign-kosten/" rel="nofollow noopener">Trustoo (nov. 2026)</a></td></tr>
<tr><td>Eenvoudige website, gemiddelde in Nederland</td><td>€500 tot €2.000</td><td><a href="https://trustoo.nl/kosten/webdesign-kosten/" rel="nofollow noopener">Trustoo (nov. 2026)</a></td></tr>
<tr><td>Bedrijfswebsite in België</td><td>€2.000 tot €6.000</td><td><a href="https://lunidev.com/nl/blog/website-kosten-2026-complete-prijsgids-belgie" rel="nofollow noopener">Lunidev (2026)</a></td></tr></table></div>
<h2>Onze prijzen</h2><div class="scroll"><table class="tabel vergelijk"><tr><th>Pakket</th><th>Klaar in</th><th>Vanaf</th></tr>
<tr><td>One-page website</td><td>3–5 dagen</td><td>€495</td></tr><tr><td>Bedrijfswebsite (tot 6 pagina's)</td><td>2–3 weken</td><td>€995</td></tr><tr><td>Webshop (tot 50 producten)</td><td>3–5 weken</td><td>€1.950</td></tr></table></div>
<p>Alle prijzen zijn eindprijzen: er komt geen btw bij. Bekijk <a href="prijzen.html">alle prijzen</a>.</p>
<h2>Welke kosten komen er na de bouw?</h2><ul><li><strong>Domeinnaam:</strong> meestal €10 tot €25 per jaar.</li><li><strong>Hosting:</strong> voor de meeste kleine sites gratis.</li><li><strong>Onderhoud (optioneel):</strong> bij ons vanaf €29 per maand, inclusief kleine wijzigingen tot 30 minuten.</li><li><strong>Extra pagina:</strong> €95, inclusief SEO-tekst.</li></ul>
<h2>Wat bepaalt de prijs?</h2><ul><li>Het aantal pagina's en de functies, zoals formulieren of een webshop.</li><li>Of je teksten en foto's zelf aanlevert.</li><li>Koppelingen, bijvoorbeeld met een agenda of betaalprovider.</li><li>Meertaligheid.</li></ul>
<p>Lees ook <a href="website-laten-maken-afspraken.html">8 afspraken die je vooraf vastlegt</a> en <a href="zelf-website-bouwen-of-laten-maken.html">zelf bouwen of laten maken</a>.</p>
<h2>Veelgestelde vragen</h2>{faq_html(faq_k)}{cta("Vraag een vaste prijs aan")}</article>''',
        crumbs=[("Home", "index.html"), ("Wat kost een website?", "wat-kost-een-website.html")], extra_ld=[art("Wat kost een website laten maken in 2026?"), faq_ld(faq_k)]))
    items.append(("wat-kost-een-website.html", "Wat kost een website laten maken in 2026?", "Marktprijzen, bijkomende kosten per jaar en onze vaste prijzen vanaf €495."))

    # ---------- ARTIKEL: WAT KOST EEN WEBSHOP ----------
    faq_w = [("Wat kost een webshop laten maken?", "Volgens Searchlab (2026) betaal je bij een freelancer meestal €2.000 tot €8.000 en bij een bureau voor het mkb €5.000 tot €15.000. Bij ons begint een webshop bij €1.950 (geen btw erbij), met tot 50 producten ingericht."),
             ("Welke kosten komen er bij een webshop bij?", "Denk aan een domeinnaam, de kosten van je betaalprovider per transactie en eventuele abonnementskosten van het platform. Die staan vooraf in de offerte."),
             ("Kan ik zelf producten toevoegen?", "Ja. Je beheert zelf je producten.")]
    pages.append(page("wat-kost-een-webshop.html", "Wat kost een webshop laten maken? | Collens Group",
        "Wat kost een webshop laten maken? Marktprijzen voor freelancers en bureaus, bijkomende kosten en onze vaste prijs vanaf €1.950. Eindprijzen, geen btw erbij.",
        f'''<article class="tekst breed"><h1>Wat kost een webshop laten maken?</h1>
<p class="lead2">Kort antwoord: een webshop kost bij een freelancer meestal €2.000 tot €8.000 en bij een bureau voor het mkb €5.000 tot €15.000. Bij Collens Group begint een webshop bij €1.950, een eindprijs zonder btw erbij.</p>
<p class="bijgewerkt">Bijgewerkt op @@BIJGEWERKT_NL@@</p>
<h2>Marktprijzen</h2><div class="scroll"><table class="tabel vergelijk"><tr><th>Wie bouwt</th><th>Prijs</th></tr><tr><td>Freelancer</td><td>€2.000 tot €8.000</td></tr><tr><td>Bureau, voor het mkb</td><td>€5.000 tot €15.000</td></tr><tr><td>Collens Group</td><td>vanaf €1.950</td></tr></table></div>
<p class="bron">Bron marktbedragen: <a href="https://searchlab.nl/kosten/wat-kost-een-webshop-laten-maken" rel="nofollow noopener">Searchlab, Wat kost een webshop laten maken (2026)</a>.</p>
<h2>Wat zit er in onze webshop?</h2><ul><li>Tot 50 producten ingericht</li><li>iDEAL en andere betaalmethoden</li><li>Verzending en btw ingesteld</li><li>Je beheert zelf je producten</li></ul><p>Klaar in 3–5 weken. Bekijk de <a href="webshop-laten-maken.html">webshoppagina</a>, of zie een voorbeeld: <a href="concept/suismuis/index.html">Suismuis Home</a>, een conceptwebshop voor woonaccessoires, nog niet gelanceerd.</p>
<h2>Welke kosten komen erbij?</h2><ul><li><strong>Domeinnaam:</strong> meestal €10 tot €25 per jaar.</li><li><strong>Betaalprovider:</strong> een kleine vergoeding per transactie; die staat vooraf in de offerte.</li><li><strong>Onderhoud (optioneel):</strong> vanaf €29 per maand.</li></ul>
<h2>Waar let je op?</h2><p>Zorg dat je webshop de wettelijke basis heeft: algemene voorwaarden, privacyverklaring, retour- en herroepingsinformatie en duidelijke contactgegevens. Laat bij twijfel je boekhouder of een jurist meekijken; dit is praktische informatie, geen juridisch advies.</p>
<p>Lees ook <a href="prijzen.html">alle prijzen</a> en <a href="website-laten-maken-afspraken.html">8 afspraken die je vooraf vastlegt</a>.</p>
<h2>Veelgestelde vragen</h2>{faq_html(faq_w)}{cta("Vraag een vaste prijs aan")}</article>''',
        crumbs=[("Home", "index.html"), ("Wat kost een webshop?", "wat-kost-een-webshop.html")], extra_ld=[art("Wat kost een webshop laten maken?"), faq_ld(faq_w)]))
    items.append(("wat-kost-een-webshop.html", "Wat kost een webshop laten maken?", "Marktprijzen, bijkomende kosten en onze vaste prijs vanaf €1.950."))

    return pages, items
