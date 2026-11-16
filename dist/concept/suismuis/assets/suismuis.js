/* Suismuis Home – concept-webshop (Collens Group). Werkt volledig in de browser; er wordt niets echt besteld of betaald. */
(function () {
  "use strict";
  var CATS = {
    decoratie: "Decoratie", kaarsen: "Kaarsen & windlichten", kussens: "Kussens",
    verlichting: "Verlichting", textiel: "Plaids & textiel", accessoires: "Accessoires"
  };
  var P = [
    { id: "vaas-olea", ink: 9.5, lv: 2.95, n: "Vaas Olea", c: "decoratie", p: 24.95, img: "p-vaas-olea", l: "Nieuw", m: "Steengoed, mat geglazuurd", d: "H 14 × Ø 7 cm", t: "Een klein, rank vaasje met een zachte, zandkleurige glazuur. Mooi met een enkele droogbloem of als groepje van drie." },
    { id: "vaas-orbit", ink: 19.9, lv: 3.95, n: "Vaas Orbit", c: "decoratie", p: 49.95, img: "p-vaas-orbit", m: "Keramiek, mat crème", d: "H 25 × B 24 cm", t: "Een sculpturale ringvaas die ook zonder bloemen een statement is. Met een smalle opening voor een paar takjes." },
    { id: "droogbloemen-champagne", ink: 12.4, lv: 3.95, n: "Droogbloemen Champagne", c: "decoratie", p: 34.95, img: "p-droogbloemen", m: "Gedroogde bloemen en pampas", d: "Lengte ca. 60 cm", t: "Een luchtige bundel in champagne- en zandtinten die maandenlang mooi blijft. Zonder vaas geleverd." },
    { id: "vazenset-blanc", ink: 28.0, lv: 4.95, n: "Vazenset Blanc", c: "decoratie", p: 69.95, img: "p-vazenset", l: "Set van 3", m: "Keramiek, mat wit", d: "H 12, 22 en 30 cm", t: "Drie vazen in verschillende hoogtes die samen een rustige, gelaagde compositie vormen." },
    { id: "kandelaar-antique", ink: 31.5, lv: 4.95, n: "Kandelaar Antique", c: "kaarsen", p: 79.00, img: "p-kandelaar", l: "Bestseller", m: "Messing, handgemaakt", d: "H 38 × B 30 cm", t: "Een klassieke driearmige kandelaar met een warme, licht verweerde messing afwerking. Voor dinerkaarsen tot Ø 2,2 cm." },
    { id: "windlichtjes-clair", ink: 12.9, lv: 3.95, n: "Windlichtjes Clair", c: "kaarsen", p: 34.95, img: "p-windlichtjes", l: "Set van 4", m: "Helder glas", d: "H 7 × Ø 6 cm", t: "Vier kleine windlichtjes voor theelichtjes. Prachtig in een rij op de eettafel of vensterbank." },
    { id: "geurkaarsen-marmer", ink: 23.0, lv: 4.95, n: "Geurkaarsen op marmer", c: "kaarsen", p: 59.95, img: "p-kaarsen-dienblad", m: "Sojawas, marmeren dienblad", d: "Dienblad 30 × 15 cm", t: "Drie geurkaarsen met een zachte geur van vijg en ceder, geleverd op een marmeren dienblad." },
    { id: "kussenhoes-linnen", ink: 14.8, lv: 2.95, n: "Kussenhoes Linnen", c: "kussens", p: 39.95, img: "p-kussens-linnen", m: "100 % stonewashed linnen", d: "50 × 50 cm, zonder binnenkussen", t: "Een zachte linnen kussenhoes in warme aardetinten met een verborgen rits. Wasbaar op 30 °C." },
    { id: "tafellamp-lune", ink: 54.0, lv: 6.95, n: "Tafellamp Lune", c: "verlichting", p: 129.00, img: "p-tafellamp", m: "Metalen voet, linnen kap", d: "H 52 × Ø 35 cm", t: "Een elegante tafellamp met een linnen kap die het licht warm en zacht verspreidt. Fitting E27, lamp niet inbegrepen." },
    { id: "hanglamp-sol", ink: 58.0, lv: 6.95, n: "Hanglamp Sol", c: "verlichting", p: 149.00, img: "p-hanglamp", m: "Handgevlochten riet", d: "Ø 45 cm", t: "Een gevlochten kap die een mooi schaduwspel op muur en plafond geeft. Inclusief textielsnoer van 1,5 m." },
    { id: "plaid-cosy", ink: 34.5, lv: 4.95, n: "Plaid Cosy", c: "textiel", p: 89.95, img: "p-plaid-cosy", l: "Nieuw", m: "Wolmix, grof gebreid", d: "130 × 170 cm", t: "Een grof gebreide plaid in warme naturel tinten, heerlijk voor koude avonden op de bank." },
    { id: "plaid-teddy", ink: 27.9, lv: 4.95, n: "Plaid Teddy", c: "textiel", p: 74.95, img: "p-plaid-teddy", m: "Zachte teddystof", d: "150 × 200 cm", t: "Een royale, wollig zachte plaid in crème die je bank direct een warme uitstraling geeft." },
    { id: "beddengoed-linnen", ink: 66.0, lv: 5.95, n: "Linnen beddengoed", c: "textiel", p: 159.00, img: "p-beddengoed", m: "100 % stonewashed linnen", d: "Dekbedovertrek 240 × 220 cm + 2 slopen", t: "Zacht gewassen linnen dat met elke wasbeurt mooier wordt. Ademend in de zomer, warm in de winter." },
    { id: "schaal-terra", ink: 10.9, lv: 2.95, n: "Schaal Terra", c: "accessoires", p: 29.95, img: "p-schaal", m: "Steengoed, handgevormd", d: "Ø 16 × H 8 cm", t: "Een handgevormde schaal met een zachte, organische rand. Voor sieraden, sleutels of gewoon als object." },
    { id: "objet-pierre", ink: 16.5, lv: 3.95, n: "Objet Pierre", c: "accessoires", p: 44.95, img: "p-objet", m: "Travertin-look steen", d: "10 × 10 × 10 cm", t: "Een ruw gehouwen blok dat rust en textuur geeft aan een kast of salontafel. Mooi naast een vaas." },
    { id: "kruk-tronc", ink: 52.0, lv: 9.95, n: "Kruk Tronc", c: "accessoires", p: 129.00, img: "p-kruk", m: "Massief walnotenhout", d: "H 60 × Ø 30 cm", t: "Een slanke houten kruk die ook dienstdoet als bijzettafel of plantentafel." }
  ];
  var GRATIS = 75, VERZEND = 5.95, CADEAU = 3.95;
  var euro = function (x) { return "€ " + x.toFixed(2).replace(".", ","); };
  var vind = function (id) { for (var i = 0; i < P.length; i++) if (P[i].id === id) return P[i]; return null; };
  var mb = function (b) { return 'src="img/' + b + '-m.jpg" srcset="img/' + b + '-m.jpg 1080w, img/' + b + '.jpg 1800w" sizes="(max-width:700px) 50vw, 25vw"'; };
  var $ = function (s, r) { return (r || document).querySelector(s); };
  var $$ = function (s, r) { return Array.prototype.slice.call((r || document).querySelectorAll(s)); };
  var esc = function (s) { return String(s).replace(/[&<>"']/g, function (c) { return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]; }); };

  /* opslag met vangnet (privémodus) */
  var geheugen = {};
  function lees(k, d) { try { var v = localStorage.getItem("suismuis-" + k); return v ? JSON.parse(v) : d; } catch (e) { return geheugen[k] || d; } }
  function bewaar(k, v) { geheugen[k] = v; try { localStorage.setItem("suismuis-" + k, JSON.stringify(v)); } catch (e) {} }

  /* winkelmand */
  function mand() { return lees("mand", []); }
  function zetMand(m) { bewaar("mand", m); tellers(); }
  function voegToe(id, aantal) {
    var m = mand(), r = null;
    for (var i = 0; i < m.length; i++) if (m[i].id === id) r = m[i];
    if (r) r.a = Math.min(r.a + aantal, 20); else m.push({ id: id, a: aantal });
    zetMand(m);
    var p = vind(id);
    toast(esc(p.n) + " is toegevoegd aan je winkelmand", '<a href="winkelmand.html">Bekijk winkelmand</a>');
  }
  function subtotaal() { return mand().reduce(function (s, r) { var p = vind(r.id); return s + (p ? p.p * r.a : 0); }, 0); }

  /* favorieten */
  function favs() { return lees("favs", []); }
  function wisselFav(id, knop) {
    var f = favs(), i = f.indexOf(id);
    if (i > -1) f.splice(i, 1); else f.push(id);
    bewaar("favs", f); tellers();
    $$('[data-fav="' + id + '"]').forEach(function (b) { b.setAttribute("aria-pressed", f.indexOf(id) > -1); });
    toast(i > -1 ? "Verwijderd uit je favorieten" : "Bewaard in je favorieten", i > -1 ? "" : '<a href="favorieten.html">Bekijk favorieten</a>');
    if (document.body.dataset.pagina === "favorieten") toonFavorieten();
  }

  function tellers() {
    var a = mand().reduce(function (s, r) { return s + r.a; }, 0);
    $$("[data-teller=mand]").forEach(function (t) { t.textContent = a || ""; });
    var f = favs().length;
    $$("[data-teller=favs]").forEach(function (t) { t.textContent = f || ""; });
  }

  var toastTimer;
  function toast(tekst, actie) {
    var t = $(".toast");
    if (!t) { t = document.createElement("div"); t.className = "toast"; t.setAttribute("role", "status"); document.body.appendChild(t); }
    t.innerHTML = "<span>" + tekst + "</span>" + (actie || "");
    t.classList.add("aan"); clearTimeout(toastTimer);
    toastTimer = setTimeout(function () { t.classList.remove("aan"); }, 3800);
  }

  /* productkaart */
  var HART = '<svg viewBox="0 0 24 24"><path d="M12 20s-7.5-4.6-7.5-10A4.3 4.3 0 0 1 12 7.4 4.3 4.3 0 0 1 19.5 10c0 5.4-7.5 10-7.5 10z"/></svg>';
  function kaart(p) {
    var fav = favs().indexOf(p.id) > -1;
    return '<article class="product">' +
      '<a class="beeld" href="product.html?p=' + p.id + '">' + (p.l ? '<span class="label">' + esc(p.l) + "</span>" : "") +
      '<img ' + mb(p.img) + ' alt="' + esc(p.n) + '" loading="lazy" width="1200" height="1500"></a>' +
      '<button class="hart" type="button" data-fav="' + p.id + '" aria-pressed="' + fav + '" aria-label="' + esc(p.n) + ' bewaren als favoriet">' + HART + "</button>" +
      '<div class="snel"><button class="knop" type="button" data-koop="' + p.id + '">In winkelmand</button></div>' +
      '<a href="product.html?p=' + p.id + '"><h3>' + esc(p.n) + '</h3><span class="prijs">' + euro(p.p) + "</span></a></article>";
  }

  /* klikken overal: koop / fav / lade / zoeken / stippen */
  document.addEventListener("click", function (e) {
    var k = e.target.closest("[data-koop]"); if (k) { e.preventDefault(); voegToe(k.getAttribute("data-koop"), 1); return; }
    var f = e.target.closest("[data-fav]"); if (f) { e.preventDefault(); wisselFav(f.getAttribute("data-fav"), f); return; }
    var o = e.target.closest("[data-open]"); if (o) { e.preventDefault(); openPaneel(o.getAttribute("data-open")); return; }
    if (e.target.closest("[data-sluit]")) { e.preventDefault(); sluitPanelen(); return; }
    var s = e.target.closest(".stip");
    $$(".stip-kaart").forEach(function (x) { if (!s || x.id !== s.getAttribute("aria-controls")) x.classList.remove("open"); });
    if (s) { var kk = document.getElementById(s.getAttribute("aria-controls")); var open = kk.classList.toggle("open"); s.setAttribute("aria-expanded", open); }
  });
  document.addEventListener("keydown", function (e) { if (e.key === "Escape") sluitPanelen(); });
  var vorigeFocus;
  function openPaneel(naam) {
    var el = document.getElementById(naam); if (!el) return;
    vorigeFocus = document.activeElement; el.classList.add("open"); el.removeAttribute("hidden");
    document.body.style.overflow = "hidden";
    var veld = el.querySelector("input,a,button"); if (veld) setTimeout(function () { veld.focus(); }, 30);
  }
  function sluitPanelen() {
    $$(".lade.open,.zoek.open").forEach(function (el) { el.classList.remove("open"); });
    document.body.style.overflow = ""; if (vorigeFocus) vorigeFocus.focus();
  }

  /* zoeken */
  var zv = $("#zoekveld");
  if (zv) zv.addEventListener("input", function () {
    var q = zv.value.trim().toLowerCase(), r = $("#zoekres"), leeg = $("#zoekleeg");
    if (!q) { r.innerHTML = ""; leeg.textContent = "Zoek op bijvoorbeeld vaas, kaars, linnen of lamp."; return; }
    var hits = P.filter(function (p) { return (p.n + " " + CATS[p.c] + " " + p.m + " " + p.t).toLowerCase().indexOf(q) > -1; });
    r.innerHTML = hits.map(kaart).join("");
    leeg.textContent = hits.length ? hits.length + (hits.length === 1 ? " product gevonden" : " producten gevonden") : "Geen producten gevonden voor “" + zv.value + "”. Probeer een ander woord.";
  });

  /* nieuwsbrief + formulieren (concept: niets wordt verstuurd) */
  $$("form[data-bevestig]").forEach(function (f) {
    f.addEventListener("submit", function (e) {
      e.preventDefault();
      var leegVeld = $$("[required]", f).filter(function (i) { return !i.value.trim() || (i.type === "email" && !i.checkValidity()); })[0];
      var m = $(".bevestig", f) || f.appendChild(Object.assign(document.createElement("p"), { className: "bevestig" }));
      m.setAttribute("role", "status");
      if (leegVeld) { m.textContent = "Vul alle verplichte velden correct in."; leegVeld.focus(); return; }
      m.textContent = f.getAttribute("data-bevestig"); f.reset();
    });
  });

  /* tabs (account) */
  $$("[role=tab]").forEach(function (t) {
    t.addEventListener("click", function () {
      $$("[role=tab]", t.parentNode).forEach(function (x) { x.setAttribute("aria-selected", x === t); document.getElementById(x.getAttribute("aria-controls")).hidden = x !== t; });
    });
  });

  /* pagina's */
  var pag = document.body.dataset.pagina;
  var url = new URLSearchParams(location.search);

  if (pag === "home") {
    $("#nieuw-grid").innerHTML = ["vaas-orbit", "tafellamp-lune", "plaid-cosy", "kandelaar-antique"].map(function (id) { return kaart(vind(id)); }).join("");
  }

  if (pag === "shop") {
    var cat = url.get("cat"); if (cat && !CATS[cat]) cat = null;
    var sort = "standaard";
    var chips = '<button class="chip" type="button" data-cat="" aria-pressed="' + !cat + '">Alles</button>' +
      Object.keys(CATS).map(function (k) { return '<button class="chip" type="button" data-cat="' + k + '" aria-pressed="' + (cat === k) + '">' + CATS[k] + "</button>"; }).join("");
    $("#chips").innerHTML = chips;
    var teken = function () {
      var lijst = P.filter(function (p) { return !cat || p.c === cat; });
      if (sort === "laag") lijst.sort(function (a, b) { return a.p - b.p; });
      if (sort === "hoog") lijst.sort(function (a, b) { return b.p - a.p; });
      if (sort === "naam") lijst.sort(function (a, b) { return a.n.localeCompare(b.n); });
      $("#shop-grid").innerHTML = lijst.map(kaart).join("");
      $("#aantal").textContent = lijst.length + " producten";
      $("#shop-titel").textContent = cat ? CATS[cat] : "Alle producten";
      $("#kruimel-cat").textContent = cat ? CATS[cat] : "Alle producten";
      document.title = (cat ? CATS[cat] : "Shop") + " | Suismuis Home (concept)";
    };
    $("#chips").addEventListener("click", function (e) {
      var b = e.target.closest("[data-cat]"); if (!b) return;
      cat = b.getAttribute("data-cat") || null;
      $$("#chips .chip").forEach(function (x) { x.setAttribute("aria-pressed", x === b); });
      history.replaceState(null, "", cat ? "?cat=" + cat : location.pathname); teken();
    });
    $("#sorteer").addEventListener("change", function () { sort = this.value; teken(); });
    teken();
  }

  if (pag === "product") {
    var p = vind(url.get("p")) || P[0];
    document.title = p.n + " | Suismuis Home (concept)";
    var extra = P.filter(function (x) { return x.c === p.c && x.id !== p.id; }).concat(P.filter(function (x) { return x.c !== p.c; })).slice(0, 4);
    var beelden = [p.img].concat(extra.slice(0, 2).map(function (x) { return x.img; }));
    $("#pdp").innerHTML =
      '<div class="galerij"><div class="hoofd"><img id="hoofdbeeld" src="img/' + p.img + '.jpg" alt="' + esc(p.n) + '" width="1200" height="1500"></div>' +
      '<div class="duim">' + beelden.map(function (b, i) { return '<button type="button" data-beeld="' + b + '" aria-current="' + (i === 0) + '" aria-label="Toon afbeelding ' + (i + 1) + '"><img src="img/' + b + '.jpg" alt=""></button>'; }).join("") + "</div>" +
      '<p class="noot" style="margin-top:6px">Voorbeeldbeelden; bij lancering komen hier je eigen productfoto’s.</p></div>' +
      '<div class="pdp-info"><nav class="kruimel" aria-label="Kruimelpad"><a href="index.html">Home</a><span>/</span><a href="shop.html">Shop</a><span>/</span><a href="shop.html?cat=' + p.c + '">' + CATS[p.c] + '</a></nav>' +
      '<span class="klein">' + CATS[p.c] + '</span><h1>' + esc(p.n) + '</h1><div class="prijs">' + euro(p.p) + '</div>' +
      '<p>' + esc(p.t) + '</p><p class="voorraad">Op voorraad · in 2–4 werkdagen in huis</p>' +
      '<div class="koop"><div class="stapper"><button type="button" data-stap="-1" aria-label="Minder">−</button><input id="aantal-p" type="number" min="1" max="20" value="1" aria-label="Aantal"><button type="button" data-stap="1" aria-label="Meer">+</button></div>' +
      '<button class="knop" type="button" id="koop-p">In winkelmand</button></div>' +
      '<button class="knop licht breed" type="button" data-fav="' + p.id + '" aria-pressed="' + (favs().indexOf(p.id) > -1) + '">Bewaar als favoriet</button>' +
      '<ul class="usp"><li>Gratis verzending vanaf € 75</li><li>14 dagen bedenktijd, eenvoudig retourneren</li><li>Veilig betalen met creditcard, Apple Pay of iDEAL</li><li>Cadeauverpakking mogelijk bij het afrekenen</li></ul>' +
      '<details open><summary>Materiaal en afmetingen</summary><p>' + esc(p.m) + "<br>" + esc(p.d) + '</p></details>' +
      '<details><summary>Onderhoud</summary><p>Afnemen met een droge of licht vochtige doek. Natuurlijke materialen kunnen kleine kleurverschillen hebben; dat maakt elk stuk uniek.</p></details>' +
      '<details><summary>Verzenden en retourneren</summary><p>Je bestelling is in 2–4 werkdagen in huis, in Nederland en België. Niet tevreden? Je hebt 14 dagen bedenktijd. Lees meer bij <a class="link" href="klantenservice.html#retour">retourneren</a>.</p></details></div>';
    $("#gerelateerd").innerHTML = extra.map(kaart).join("");
    $("#pdp").addEventListener("click", function (e) {
      var b = e.target.closest("[data-beeld]");
      if (b) { $("#hoofdbeeld").src = "img/" + b.getAttribute("data-beeld") + ".jpg"; $$("[data-beeld]").forEach(function (x) { x.setAttribute("aria-current", x === b); }); }
      var s = e.target.closest("[data-stap]");
      if (s) { var i = $("#aantal-p"); i.value = Math.max(1, Math.min(20, (+i.value || 1) + (+s.getAttribute("data-stap")))); }
      if (e.target.closest("#koop-p")) voegToe(p.id, Math.max(1, Math.min(20, +$("#aantal-p").value || 1)));
    });
  }

  function toonMand() {
    var m = mand(), doel = $("#mand-regels");
    if (!m.length) {
      $("#mand").innerHTML = '<div class="leegmand"><h2 style="font-size:36px;margin-bottom:12px">Je winkelmand is nog leeg</h2><p>Laat je inspireren door onze collectie.</p><a class="knop" href="shop.html">Naar de shop</a></div>';
      return;
    }
    doel.innerHTML = m.map(function (r) {
      var p = vind(r.id); if (!p) return "";
      return '<div class="regel"><a href="product.html?p=' + p.id + '"><img src="img/' + p.img + '-m.jpg" alt=""' + esc(p.n) + '"></a>' +
        '<div><a href="product.html?p=' + p.id + '"><h3>' + esc(p.n) + '</h3></a><div style="font-size:14px;color:var(--mokka)">' + euro(p.p) + '</div>' +
        '<div class="stapper"><button type="button" data-mstap="-1" data-id="' + p.id + '" aria-label="Minder">−</button><input value="' + r.a + '" readonly aria-label="Aantal"><button type="button" data-mstap="1" data-id="' + p.id + '" aria-label="Meer">+</button></div>' +
        '<button class="weg" type="button" data-weg="' + p.id + '">Verwijderen</button></div><div class="rprijs">' + euro(p.p * r.a) + "</div></div>";
    }).join("");
    var sub = subtotaal(), cadeau = $("#cadeau") && $("#cadeau").checked ? CADEAU : 0;
    var verz = sub >= GRATIS ? 0 : VERZEND;
    $("#sub").textContent = euro(sub);
    $("#verz").textContent = verz ? euro(verz) : "Gratis";
    $("#cad-rij").hidden = !cadeau; $("#cad").textContent = euro(cadeau);
    $("#tot").textContent = euro(sub + verz + cadeau);
    var rest = GRATIS - sub;
    $("#vg-tekst").textContent = rest > 0 ? "Nog " + euro(rest) + " tot gratis verzending" : "Je bestelling wordt gratis verzonden";
    $("#vg-vul").style.width = Math.min(100, sub / GRATIS * 100) + "%";
    bewaar("cadeau", !!cadeau);
  }
  if (pag === "mand") {
    $("#cadeau").checked = lees("cadeau", false);
    $("#mand").addEventListener("click", function (e) {
      var s = e.target.closest("[data-mstap]"), w = e.target.closest("[data-weg]"), m = mand();
      if (s) { m.forEach(function (r) { if (r.id === s.getAttribute("data-id")) r.a = Math.max(1, Math.min(20, r.a + (+s.getAttribute("data-mstap")))); }); zetMand(m); toonMand(); }
      if (w) { zetMand(m.filter(function (r) { return r.id !== w.getAttribute("data-weg"); })); toonMand(); }
    });
    $("#cadeau").addEventListener("change", toonMand);
    toonMand();
  }

  if (pag === "afrekenen") {
    var m2 = mand();
    if (!m2.length) { $("#afreken").innerHTML = '<div class="leegmand"><h2 style="font-size:36px;margin-bottom:12px">Je winkelmand is leeg</h2><a class="knop" href="shop.html">Naar de shop</a></div>'; }
    else {
      var sub2 = subtotaal(), cad2 = lees("cadeau", false) ? CADEAU : 0, vz2 = sub2 >= GRATIS ? 0 : VERZEND;
      $("#overzicht").innerHTML = m2.map(function (r) { var p = vind(r.id); return '<div class="rij"><span>' + r.a + " × " + esc(p.n) + "</span><span>" + euro(p.p * r.a) + "</span></div>"; }).join("") +
        '<div class="rij"><span>Verzending</span><span>' + (vz2 ? euro(vz2) : "Gratis") + "</span></div>" +
        (cad2 ? '<div class="rij"><span>Cadeauverpakking</span><span>' + euro(cad2) + "</span></div>" : "") +
        '<div class="rij totaal"><span>Totaal</span><span>' + euro(sub2 + vz2 + cad2) + "</span></div>";
      $("#bestel").addEventListener("submit", function (e) {
        e.preventDefault();
        var f = this, fout = $$("[required]", f).filter(function (i) { return !i.value.trim() || !i.checkValidity(); })[0];
        if (fout) { $("#fout").textContent = "Vul alle verplichte velden correct in."; fout.focus(); return; }
        zetMand([]); bewaar("cadeau", false);
        $("#afreken").innerHTML = '<div class="leegmand" style="max-width:640px"><span class="klein">Dank je wel</span><h2 style="font-size:44px;margin:10px 0 16px">Je bestelling is geplaatst</h2>' +
          '<p>Je ontvangt zo een bevestiging per e-mail met je ordernummer en de verwachte bezorgdatum.</p>' +
          '<div class="melding">Dit is een concept: er is niets echt besteld of betaald. In de echte webshop ga je hier naar de beveiligde betaalpagina van Stripe (creditcard, Apple Pay, Google Pay of iDEAL).</div>' +
          '<a class="knop" href="index.html">Terug naar de homepage</a></div>';
        window.scrollTo(0, 0);
      });
    }
  }

  function toonFavorieten() {
    var f = favs().map(vind).filter(Boolean);
    $("#fav-grid").innerHTML = f.map(kaart).join("");
    $("#fav-leeg").hidden = !!f.length;
  }
  if (pag === "favorieten") toonFavorieten();

  /* beheer (concept): marge per product en route van betaling naar levering */
  if (pag === "beheer") {
    var FEE = 0.29;
    var rij = function (p) {
      return '<tr data-id="' + p.id + '"><td><img src="img/' + p.img + '-m.jpg" alt=""><span>' + esc(p.n) + '<small>' + CATS[p.c] + '</small></span></td>' +
        '<td>' + euro(p.ink) + '</td><td>' + euro(p.lv) + '</td>' +
        '<td><input type="number" step="0.05" min="0" value="' + p.p.toFixed(2) + '" aria-label="Verkoopprijs ' + esc(p.n) + '"></td>' +
        '<td class="winst"></td><td class="marge"></td></tr>';
    };
    var tb = $("#marge-tabel tbody"); tb.innerHTML = P.map(rij).join("");
    var reken = function () {
      var som = 0, n = 0;
      $$("tr[data-id]", tb).forEach(function (tr) {
        var p = vind(tr.getAttribute("data-id")), vk = +$("input", tr).value || 0;
        var w = vk - p.ink - p.lv - FEE, m = vk ? w / vk * 100 : 0;
        $(".winst", tr).textContent = euro(w); $(".marge", tr).textContent = Math.round(m) + " %";
        $(".winst", tr).style.color = w < 0 ? "#8A3B2E" : ""; som += m; n++;
      });
      $("#gem-marge").textContent = Math.round(som / n) + " %";
    };
    tb.addEventListener("input", reken); reken();
    var stappen = ["Betaald", "Doorgestuurd naar leverancier", "Verzonden", "Bezorgd"];
    var orders = [["SM-1043", "vazenset-blanc", 3], ["SM-1042", "plaid-cosy", 2], ["SM-1041", "kandelaar-antique", 1], ["SM-1040", "schaal-terra", 0]];
    $("#orders").innerHTML = orders.map(function (o) {
      var p = vind(o[1]);
      return '<div class="order"><div><b>' + o[0] + '</b><span>' + esc(p.n) + ' · ' + euro(p.p) + '</span></div><ol class="statusbalk">' +
        stappen.map(function (s, i) { return '<li class="' + (i <= o[2] ? "klaar" : "") + '">' + s + "</li>"; }).join("") + "</ol>" +
        '<div class="ordwinst">Jouw winst <b>' + euro(p.p - p.ink - p.lv - FEE) + "</b></div></div>";
    }).join("");
  }

  tellers();
})();
