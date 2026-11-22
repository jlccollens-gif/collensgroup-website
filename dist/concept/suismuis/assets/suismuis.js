/* Suismuis Home – webshop (Collens Group). Bestellen, betalen (creditcard) en beheer via de server-functie "suismuis". */
  var API = "https://eyrfizayagcwaxbxyeuh.supabase.co/functions/v1/suismuis";
function suisStart() {
  "use strict";
  var TAX = [
    ["wonen", "Wonen & decoratie", [["schilderijen", "Schilderijen"], ["spiegels", "Spiegels"], ["beeldjes", "Beeldjes & objecten"], ["bloempotten", "Bloempotten"], ["droogbloemen", "Droogbloemen"]]],
    ["vazen", "Vazen", [["glazen-vazen", "Glazen vazen"], ["stenen-vazen", "Stenen vazen"], ["rotan-vazen", "Rotan vazen"]]],
    ["verlichting", "Verlichting & kaarsen", [["lampen", "Lampen"], ["lampenkappen", "Lampenkappen"], ["kaarsen", "Kaarsen & windlichten"]]],
    ["textiel", "Textiel", [["kussenhoezen", "Kussenhoezen"], ["plaids", "Plaids"], ["vloerkleden", "Vloerkleden"], ["beddengoed", "Beddengoed"], ["gordijnen", "Gordijnen & vitrage"], ["vloerkussens", "Vloerkussens"]]],
    ["tafel", "Servies & tafel", [["servies", "Servies"], ["schalen", "Schalen & dienbladen"], ["tafellinnen", "Servetten & placemats"]]],
    ["meubels", "Meubels", [["bijzettafels", "Bijzettafels"], ["salontafels", "Salontafels"], ["eettafels", "Eettafels"], ["eetkamerstoelen", "Eetkamerstoelen"], ["stoelen", "Stoelen"], ["fauteuils", "Fauteuils"], ["bankjes", "Bankjes"], ["krukken", "Barkrukken"], ["kasten", "Kasten & nachtkastjes"]]]
  ];
  var CATS = {}, SUBS = {}, SUBCAT = {};
  TAX.forEach(function (t) { CATS[t[0]] = t[1]; SUBS[t[0]] = t[2]; t[2].forEach(function (s) { SUBCAT[s[0]] = [t[0], s[1]]; }); });
  var OUD = { decoratie: "wonen", kaarsen: "verlichting", kussens: "textiel", accessoires: "wonen" };
  var P = [
    { id: "vaas-olea", n: "Vaas Olea", c: "vazen", s: "stenen-vazen", p: 24.95, img: "p-vaas-olea", l: "Nieuw", m: "Steengoed, mat geglazuurd", d: "H 14 × Ø 7 cm", t: "Een klein, rank vaasje met een zachte, zandkleurige glazuur. Mooi met een enkele droogbloem of als groepje van drie." },
    { id: "vaas-orbit", n: "Vaas Orbit", c: "vazen", s: "stenen-vazen", p: 49.95, img: "p-vaas-orbit", m: "Keramiek, mat crème", d: "H 25 × B 24 cm", t: "Een sculpturale ringvaas die ook zonder bloemen een statement is. Met een smalle opening voor een paar takjes." },
    { id: "droogbloemen-champagne", n: "Droogbloemen Champagne", c: "wonen", s: "droogbloemen", p: 34.95, img: "p-droogbloemen", m: "Gedroogde bloemen en pampas", d: "Lengte ca. 60 cm", t: "Een luchtige bundel in champagne- en zandtinten die maandenlang mooi blijft. Zonder vaas geleverd." },
    { id: "vazenset-blanc", n: "Vazenset Blanc", c: "vazen", s: "stenen-vazen", p: 69.95, img: "p-vazenset", l: "Set van 3", m: "Keramiek, mat wit", d: "H 12, 22 en 30 cm", t: "Drie vazen in verschillende hoogtes die samen een rustige, gelaagde compositie vormen." },
    { id: "kandelaar-antique", n: "Kandelaar Antique", c: "verlichting", s: "kaarsen", p: 79.00, img: "p-kandelaar", m: "Messing, handgemaakt", d: "H 38 × B 30 cm", t: "Een klassieke driearmige kandelaar met een warme, licht verweerde messing afwerking. Voor dinerkaarsen tot Ø 2,2 cm." },
    { id: "windlichtjes-clair", n: "Windlichtjes Clair", c: "verlichting", s: "kaarsen", p: 34.95, img: "p-windlichtjes", l: "Set van 4", m: "Helder glas", d: "H 7 × Ø 6 cm", t: "Vier kleine windlichtjes voor theelichtjes. Prachtig in een rij op de eettafel of vensterbank." },
    { id: "geurkaarsen-marmer", n: "Geurkaarsen op marmer", c: "verlichting", s: "kaarsen", p: 59.95, img: "p-kaarsen-dienblad", m: "Sojawas, marmeren dienblad", d: "Dienblad 30 × 15 cm", t: "Drie geurkaarsen met een zachte geur van vijg en ceder, geleverd op een marmeren dienblad." },
    { id: "kussenhoes-linnen", n: "Kussenhoes Linnen", c: "textiel", s: "kussenhoezen", p: 39.95, img: "p-kussens-linnen", m: "100 % stonewashed linnen", d: "50 × 50 cm, zonder binnenkussen", t: "Een zachte linnen kussenhoes in warme aardetinten met een verborgen rits. Wasbaar op 30 °C." },
    { id: "tafellamp-lune", n: "Tafellamp Lune", c: "verlichting", s: "lampen", p: 129.00, img: "p-tafellamp", m: "Metalen voet, linnen kap", d: "H 52 × Ø 35 cm", t: "Een elegante tafellamp met een linnen kap die het licht warm en zacht verspreidt. Fitting E27, lamp niet inbegrepen." },
    { id: "hanglamp-sol", n: "Hanglamp Sol", c: "verlichting", s: "lampen", p: 149.00, img: "p-hanglamp", m: "Handgevlochten riet", d: "Ø 45 cm", t: "Een gevlochten kap die een mooi schaduwspel op muur en plafond geeft. Inclusief textielsnoer van 1,5 m." },
    { id: "plaid-cosy", n: "Plaid Cosy", c: "textiel", s: "plaids", p: 89.95, img: "p-plaid-cosy", l: "Nieuw", m: "Wolmix, grof gebreid", d: "130 × 170 cm", t: "Een grof gebreide plaid in warme naturel tinten, heerlijk voor koude avonden op de bank." },
    { id: "plaid-teddy", n: "Plaid Teddy", c: "textiel", s: "plaids", p: 74.95, img: "p-plaid-teddy", m: "Zachte teddystof", d: "150 × 200 cm", t: "Een royale, wollig zachte plaid in crème die je bank direct een warme uitstraling geeft." },
    { id: "beddengoed-linnen", n: "Linnen beddengoed", c: "textiel", s: "beddengoed", p: 159.00, img: "p-beddengoed", m: "100 % stonewashed linnen", d: "Dekbedovertrek 240 × 220 cm + 2 slopen", t: "Zacht gewassen linnen dat met elke wasbeurt mooier wordt. Ademend in de zomer, warm in de winter." },
    { id: "schaal-terra", n: "Schaal Terra", c: "tafel", s: "servies", p: 29.95, img: "p-schaal", m: "Steengoed, handgevormd", d: "Ø 16 × H 8 cm", t: "Een handgevormde schaal met een zachte, organische rand. Voor sieraden, sleutels of gewoon als object." },
    { id: "objet-pierre", n: "Objet Pierre", c: "wonen", s: "beeldjes", p: 44.95, img: "p-objet", m: "Travertin-look steen", d: "10 × 10 × 10 cm", t: "Een ruw gehouwen blok dat rust en textuur geeft aan een kast of salontafel. Mooi naast een vaas." },
    { id: "schilderij-duin", n: "Schilderij Duin", c: "wonen", s: "schilderijen", p: 149.00, img: "p-schilderij-1", l: "Nieuw", m: "Canvas in eiken lijst", d: "60 × 80 cm", t: "Zachte, overlappende vormen in zand, taupe en mokka. Rustig genoeg voor boven de bank, met genoeg diepte om naar te blijven kijken." },
    { id: "schilderij-horizon", n: "Schilderij Horizon", c: "wonen", s: "schilderijen", p: 179.00, img: "p-schilderij-2", m: "Canvas in eiken lijst", d: "70 × 90 cm", t: "Brede banen in warme aardetinten met een lichte zon. Een kalm, horizontaal ritme dat elke wand meer ruimte geeft." },
    { id: "schilderij-boog", n: "Schilderij Boog", c: "wonen", s: "schilderijen", p: 129.00, img: "p-schilderij-3", m: "Canvas in eiken lijst", d: "50 × 70 cm", t: "Een zachte boog en een ronde vorm in crème en taupe. Mooi in een hal, slaapkamer of als paar naast elkaar." },
    { id: "kruk-tronc", n: "Kruk Tronc", c: "meubels", s: "bijzettafels", p: 129.00, img: "p-kruk", m: "Massief walnotenhout", d: "H 60 × Ø 30 cm", t: "Een slanke houten kruk die ook dienstdoet als bijzettafel of plantentafel." }
  ];
  /* Kim 18-11: voorbeeldproducten en de producten van haar schermfoto's eruit */
  var WEG = [110, 113, 117, 118, 125, 134, 149, 151, 153, 155, 157]; /* 149: Kim 22-11 */
  P = (window.SUIS_EXTRA || []).filter(function (p) { return WEG.indexOf(p.nr) < 0; });
  var GRATIS = 75, VERZEND = 5.95, CADEAU = 3.95;
  var euro = function (x) { return "€ " + x.toFixed(2).replace(".", ","); };
  var foto = function (p, groot) { if (p.u) return p.u[0]; if (p.f) return "img/" + p.img + ".jpg"; return "img/" + p.img + (groot ? "" : "-m") + ".jpg"; };
  var vind = function (id) { for (var i = 0; i < P.length; i++) if (P[i].id === id) return P[i]; return null; };
  var mb = function (b) { return 'src="img/' + b + '-m.jpg" srcset="img/' + b + '-m.jpg 1080w, img/' + b + '.jpg 1800w" sizes="(max-width:700px) 50vw, 25vw"'; };
  var $ = function (s, r) { return (r || document).querySelector(s); };
  var $$ = function (s, r) { return Array.prototype.slice.call((r || document).querySelectorAll(s)); };
  function api(data) {
    return fetch(API, { method: "POST", headers: { "Content-Type": "application/json" }, body: JSON.stringify(data) })
      .then(function (r) { return r.json().catch(function () { return {}; }).then(function (j) { if (!r.ok && !j.fout) j.fout = "Er ging iets mis. Probeer het opnieuw."; j._status = r.status; return j; }); })
      .catch(function () { return { fout: "Geen verbinding. Controleer je internet en probeer het opnieuw." }; });
  }
  var basis = function () { return location.origin + location.pathname.replace(/\/[^\/]*$/, ""); };
  var esc = function (s) { return String(s).replace(/[&<>"']/g, function (c) { return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]; }); };

  /* uitklapmenu onder Shop: hover/focus via CSS, tik en Escape via JS */
  $$(".mega-wrap").forEach(function (w) {
    var k = $(".mega-knop", w);
    var zet = function (open) { w.classList.toggle("open", open); k.setAttribute("aria-expanded", open); };
    w.addEventListener("mouseenter", function () { zet(true); });
    w.addEventListener("mouseleave", function () { zet(false); });
    w.addEventListener("focusin", function () { zet(true); });
    w.addEventListener("focusout", function (e) { if (!w.contains(e.relatedTarget)) zet(false); });
    w.addEventListener("keydown", function (e) { if (e.key === "Escape") { zet(false); k.focus(); } });
  });

  /* opslag met vangnet (privémodus) */
  var geheugen = {};
  function lees(k, d) { try { var v = localStorage.getItem("suismuis-" + k); return v ? JSON.parse(v) : d; } catch (e) { return geheugen[k] || d; } }
  function bewaar(k, v) { geheugen[k] = v; try { localStorage.setItem("suismuis-" + k, JSON.stringify(v)); } catch (e) {} }

  /* winkelmand */
  function mand() { return lees("mand", []); }
  function zetMand(m) { bewaar("mand", m); tellers(); }
  function voegToe(id, aantal, uitvoering) {
    var m = mand(), r = null;
    for (var i = 0; i < m.length; i++) if (m[i].id === id && (m[i].u || "") === (uitvoering || "")) r = m[i];
    if (r) r.a = Math.min(r.a + aantal, 20); else m.push({ id: id, a: aantal, u: uitvoering || "" });
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
      '<img ' + (p.u || p.f ? 'src="' + foto(p) + '"' : mb(p.img)) + ' alt=""' + esc(p.n) + '" loading="lazy" width="1200" height="1500"></a>' +
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
      var soort = f.getAttribute("data-soort");
      if (!soort) { m.textContent = f.getAttribute("data-bevestig"); f.reset(); return; }
      var velden = {}, email = "", naam = "", hp = "";
      $$("input[name],select[name],textarea[name]", f).forEach(function (i) {
        if (i.name === "email") email = i.value; else if (i.name === "naam") naam = i.value; else if (i.name === "website") hp = i.value; else if (i.value) velden[i.name] = i.value;
      });
      var knop = $("button[type=submit]", f); knop.disabled = true; m.textContent = "Bezig met versturen…";
      api({ actie: "bericht", soort: soort, email: email, naam: naam, velden: velden, website: hp }).then(function (j) {
        knop.disabled = false;
        if (j.fout) { m.textContent = j.fout; return; }
        m.textContent = f.getAttribute("data-bevestig"); f.reset();
      });
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

  var MAT = { linnen: [/linnen/, "Linnen"], keramiek: [/keramiek|steengoed|porselein|aardewerk|terracotta/, "Keramiek"], hout: [/hout|eiken|teak|mango|rotan|riet|jute|bamboe|acacia|walnoot/, "Hout & riet"], glas: [/glas/, "Glas"], metaal: [/messing|metaal|ijzer|staal|brons/, "Messing & metaal"], zacht: [/wol|katoen|teddy|boucl|fluweel/, "Wol & katoen"] };
  function vanMat(p, k) { return MAT[k][0].test(((p.m || "") + " " + p.n).toLowerCase()); }
  function telling(n) { return n === 1 ? "1 stuk" : n + " stukken"; }
  if (pag === "home") {
    $("#nieuw-grid").innerHTML = [184, 121, 141, 102].map(function (nr) { return P.filter(function (p) { return p.nr === nr; })[0]; }).filter(Boolean).map(kaart).join("");
  }

  if (pag === "shop") {
    var cat = url.get("cat"), sub = url.get("sub"), mat = url.get("mat");
    if (mat && !MAT[mat]) mat = null;
    if (cat && OUD[cat]) cat = OUD[cat];
    if (sub && SUBCAT[sub]) cat = SUBCAT[sub][0]; else sub = null;
    if (cat && !CATS[cat]) cat = null;
    var sort = "standaard";
    var subnav = $("#subnav");
    if (cat) {
      subnav.innerHTML = '<a href="shop.html?cat=' + cat + '"' + (!sub ? ' aria-current="page"' : "") + '>Alles</a>' +
        SUBS[cat].map(function (x) { return '<a href="shop.html?cat=' + cat + '&amp;sub=' + x[0] + '"' + (sub === x[0] ? ' aria-current="page"' : "") + ">" + x[1] + "</a>"; }).join("");
    } else {
      subnav.innerHTML = TAX.map(function (t) { return '<a href="shop.html?cat=' + t[0] + '">' + t[1] + "</a>"; }).join("");
    }
    var titel = sub ? SUBCAT[sub][1] : (cat ? CATS[cat] : (mat ? MAT[mat][1] : "Alle producten"));
    var kr = $("#kruimel-cat");
    if (sub) kr.outerHTML = '<a href="shop.html?cat=' + cat + '">' + CATS[cat] + '</a><span>/</span><span id="kruimel-cat">' + titel + "</span>"; else kr.textContent = titel;
    $("#shop-titel").textContent = titel;
    if (mat && !cat) { $("#shop-intro").textContent = "Alles van " + MAT[mat][1].toLowerCase() + " uit de collectie."; subnav.innerHTML = Object.keys(MAT).map(function (k) { return '<a href="shop.html?mat=' + k + '"' + (k === mat ? ' aria-current="page"' : "") + ">" + MAT[k][1] + "</a>"; }).join(""); }
    if (cat) $("#shop-intro").textContent = sub ? "Uit de collectie " + CATS[cat].toLowerCase() + ", in warme, natuurlijke tinten." : "Alles uit " + CATS[cat].toLowerCase() + ", in warme, natuurlijke tinten.";
    document.title = titel + " | Suismuis Home (concept)";
    var teken = function () {
      var lijst = P.filter(function (p) { return (!cat || p.c === cat) && (!sub || p.s === sub) && (!mat || vanMat(p, mat)); });
      if (sort === "standaard") lijst.sort(function (a, b) { return (a.s === b.s ? 0 : (a.s < b.s ? -1 : 1)) || ((a.o || 0) - (b.o || 0)); });
      if (sort === "laag") lijst.sort(function (a, b) { return a.p - b.p; });
      if (sort === "hoog") lijst.sort(function (a, b) { return b.p - a.p; });
      if (sort === "naam") lijst.sort(function (a, b) { return a.n.localeCompare(b.n); });
      $("#shop-grid").innerHTML = lijst.map(kaart).join("");
      $("#aantal").textContent = lijst.length === 1 ? "1 product" : lijst.length + " producten";
      var leeg = lijst.length === 0;
      $("#binnenkort").hidden = !leeg; $("#shop-grid").hidden = leeg;
      $("#sorteer").parentNode.style.visibility = leeg ? "hidden" : "";
      if (leeg && cat) $("#bk-terug").setAttribute("href", "shop.html?cat=" + cat), $("#bk-terug").textContent = "Bekijk alles in " + CATS[cat].toLowerCase();
    };
    $("#sorteer").addEventListener("change", function () { sort = this.value; teken(); });
    teken();
  }

  if (pag === "product") {
    var p = vind(url.get("p")) || P[0];
    document.title = p.n + " | Suismuis Home (concept)";
    var extra = P.filter(function (x) { return x.c === p.c && x.id !== p.id; }).concat(P.filter(function (x) { return x.c !== p.c; })).slice(0, 4);
    var beelden = p.u ? p.u.slice() : [foto(p, true)].concat(p.f ? [] : extra.slice(0, 2).map(function (x) { return foto(x, true); }));
    var lever = p.lt ? "Levertijd " + p.lt : "Levertijd 8–15 werkdagen";
    $("#pdp").innerHTML =
      '<div class="galerij"><div class="hoofd"><img id="hoofdbeeld" src="' + beelden[0] + '" alt=""' + esc(p.n) + '" width="1200" height="1500"></div>' +
      (beelden.length > 1 ? '<div class="duim">' + beelden.map(function (b, i) { return '<button type="button" data-beeld="' + b + '" aria-current="' + (i === 0) + '" aria-label="Toon afbeelding ' + (i + 1) + '"><img src="' + b + '" alt=""></button>'; }).join("") + "</div>" : "") +
      (p.ok ? '<p class="noot" style="margin-top:6px">Eerste foto: het werk vrijstaand. Daarna alle foto’s van de maker, ook sfeer- en detailfoto’s.</p>' : '<p class="noot" style="margin-top:6px">' + "Voorbeeldbeelden; bij lancering komen hier je eigen productfoto’s." + '</p>') + '</div>' +
      '<div class="pdp-info"><nav class="kruimel" aria-label="Kruimelpad"><a href="index.html">Home</a><span>/</span><a href="shop.html">Shop</a><span>/</span><a href="shop.html?cat=' + p.c + '">' + CATS[p.c] + '</a>' + (p.s ? '<span>/</span><a href="shop.html?cat=' + p.c + '&amp;sub=' + p.s + '">' + SUBCAT[p.s][1] + '</a>' : '') + '</nav>' +
      '<span class="klein">' + (p.s ? SUBCAT[p.s][1] : CATS[p.c]) + '</span><h1>' + esc(p.n) + '</h1><div class="prijs">' + (p.maten && p.maten.length > 1 ? '<span class="vanaf">vanaf</span> ' : '') + euro(p.p) + '</div>' +
      (p.var && p.var.length > 1 ? '<div class="opties"><p class="optie-kop">Uitvoering: <b id="var-naam">' + esc(p.var[0].n) + '</b></p><div class="stalen">' + p.var.map(function (v, i) { return '<button type="button" class="staal" data-var="' + i + '" aria-pressed="' + (i === 0) + '" aria-label="Uitvoering ' + esc(v.n) + '"><img src="' + v.b + '" alt=""></button>'; }).join("") + '</div></div>' : '') +
      (p.maten && p.maten.length ? '<div class="opties"><label class="optie-kop" for="maat">Maat (cm)</label><select id="maat">' + p.maten.map(function (m) { return "<option>" + m + " cm</option>"; }).join("") + '</select>' + (p.maten.length > 1 ? '<p class="optie-noot" id="maat-noot">De prijs geldt voor de maat ' + esc(p.maten[0]) + ' cm. Wil je een andere maat? Dan vragen we de prijs voor je op.</p>' : '') + '</div>' : '') +
      '<p>' + esc(p.t) + '</p><p class="voorraad">' + lever + '</p>' +
      '<div class="koop"><div class="stapper"><button type="button" data-stap="-1" aria-label="Minder">−</button><input id="aantal-p" type="number" min="1" max="20" value="1" aria-label="Aantal"><button type="button" data-stap="1" aria-label="Meer">+</button></div>' +
      '<button class="knop" type="button" id="koop-p">In winkelmand</button></div>' +
      '<button class="knop licht breed" type="button" data-fav="' + p.id + '" aria-pressed="' + (favs().indexOf(p.id) > -1) + '">Bewaar als favoriet</button>' +
      '<ul class="usp"><li>Gratis verzending vanaf € 75</li><li>14 dagen bedenktijd, eenvoudig retourneren</li><li>Veilig betalen met creditcard (3D Secure)</li><li>Cadeauverpakking mogelijk bij het afrekenen</li></ul>' +
      '<details open><summary>Materiaal en afmetingen</summary>' + (p.spec ? '<dl class="spec">' + p.spec.map(function (r) { return "<dt>" + esc(r[0]) + "</dt><dd>" + esc(r[1]) + "</dd>"; }).join("") + '</dl><p class="spec-maten">' + esc(p.d) + '</p>' : '<p>' + esc(p.m) + "<br>" + esc(p.d) + '</p>') + '</details>' +
      '<details><summary>Onderhoud</summary><p>Afnemen met een droge of licht vochtige doek. Natuurlijke materialen kunnen kleine kleurverschillen hebben; dat maakt elk stuk uniek.</p></details>' +
      '<details><summary>Verzenden en retourneren</summary><p>' + (p.lt ? "Levertijd " + p.lt + ", in Nederland en België." : "Je bestelling is in 8–15 werkdagen in huis, in Nederland en België.") + ' Niet tevreden? Je hebt 14 dagen bedenktijd. Lees meer bij <a class="link" href="klantenservice.html#retour">retourneren</a>.</p></details></div>';
    $("#gerelateerd").innerHTML = extra.map(kaart).join("");
    var msel = $("#maat");
    if (msel && p.maten.length > 1) msel.addEventListener("change", function () {
      var k = $("#koop-p"), pr = $(".pdp-info .prijs");
      k.textContent = msel.selectedIndex > 0 ? "Vraag de prijs aan" : "In winkelmand";
      pr.innerHTML = msel.selectedIndex > 0 ? '<span class="vanaf">prijs op aanvraag</span>' : euro(p.p);
    });
    $("#pdp").addEventListener("click", function (e) {
      var b = e.target.closest("[data-beeld]");
      if (b) { $("#hoofdbeeld").src = b.getAttribute("data-beeld"); $$("[data-beeld]").forEach(function (x) { x.setAttribute("aria-current", x === b); }); }
      var v = e.target.closest("[data-var]");
      if (v) { var vv = p.var[+v.getAttribute("data-var")]; $("#hoofdbeeld").src = vv.b; $("#var-naam").textContent = vv.n; $$("[data-var]").forEach(function (x) { x.setAttribute("aria-pressed", x === v); }); }
      var s = e.target.closest("[data-stap]");
      if (s) { var i = $("#aantal-p"); i.value = Math.max(1, Math.min(20, (+i.value || 1) + (+s.getAttribute("data-stap")))); }
      if (e.target.closest("#koop-p")) {
        var ms = $("#maat");
        if (ms && ms.selectedIndex > 0) { vraagMaat(p, ms.value); return; }
        var vn = $("#var-naam");
        voegToe(p.id, Math.max(1, Math.min(20, +$("#aantal-p").value || 1)), p.var && p.var.length > 1 && vn ? vn.textContent : "");
      }
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
      return '<div class="regel"><a href="product.html?p=' + p.id + '"><img src="' + foto(p) + '" alt="' + esc(p.n) + '"></a>' +
        '<div><a href="product.html?p=' + p.id + '"><h3>' + esc(p.n) + '</h3></a><div style="font-size:14px;color:var(--mokka)">' + euro(p.p) + (p.maten && p.maten.length ? ' · ' + esc(p.maten[0]) + ' cm' : '') + (r.u ? ' · uitvoering ' + esc(r.u) : '') + '</div>' +
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
    var m2 = mand().filter(function (r) { return vind(r.id); });
    if (!m2.length) { $("#afreken").innerHTML = '<div class="leegmand"><h2 style="font-size:36px;margin-bottom:12px">Je winkelmand is leeg</h2><a class="knop" href="shop.html">Naar de shop</a></div>'; }
    else {
      var cad2 = lees("cadeau", false), order = null, cfg = null, kaart = null;
      var regelsHtml = function (o) {
        return o.regels.map(function (r) { return '<div class="rij"><span>' + r.aantal + " × " + esc(r.naam) + (r.maat ? '<small>' + esc(r.maat) + '</small>' : '') + (r.uitvoering ? '<small>Uitvoering ' + esc(r.uitvoering) + '</small>' : '') + "</span><span>" + euro(r.prijs * r.aantal) + "</span></div>"; }).join("") +
          '<div class="rij"><span>Verzending</span><span>' + (o.verzending ? euro(o.verzending) : "Gratis") + "</span></div>" +
          (o.cadeau ? '<div class="rij"><span>Cadeauverpakking</span><span>' + euro(o.cadeau) + "</span></div>" : "") +
          '<div class="rij totaal"><span>Totaal</span><span>' + euro(o.totaal) + "</span></div>";
      };
      var sub2 = subtotaal(), vz2 = sub2 >= GRATIS ? 0 : VERZEND;
      $("#overzicht").innerHTML = regelsHtml({ regels: m2.map(function (r) { var p = vind(r.id); return { naam: p.n, aantal: r.a, prijs: p.p, maat: p.maten && p.maten.length ? p.maten[0] + " cm" : "", uitvoering: r.u }; }), verzending: vz2, cadeau: cad2 ? CADEAU : 0, totaal: sub2 + vz2 + (cad2 ? CADEAU : 0) });
      var stap = function (n) { $$(".stappen li").forEach(function (li) { if (+li.getAttribute("data-stap") === n) li.setAttribute("aria-current", "step"); else li.removeAttribute("aria-current"); }); };
      var f = $("#bestel"), bf = $("#betaalfout"), bk = $("#betaal");
      var bezig = function (aan, t) { bk.disabled = aan; bk.textContent = aan ? (t || "Bezig…") : "Betaal " + euro(order.totaal) + " veilig"; };
      api({ actie: "config" }).then(function (j) { cfg = j || {}; });
      var bedankt = function (o) {
        zetMand([]); bewaar("cadeau", false); stap(3);
        $("#afreken").innerHTML = '<div class="leegmand bedankt" style="max-width:660px"><span class="klein">Dank je wel</span><h2 style="font-size:44px;margin:10px 0 16px">Je betaling is gelukt</h2>' +
          '<p>Je ordernummer is <b>' + esc(o.nr) + '</b>. Je krijgt zo een bevestiging per e-mail. Zodra je bestelling onderweg is, sturen we je de track-and-tracecode.</p>' +
          '<div class="samenvatting">' + regelsHtml(o) + '</div>' +
          '<a class="knop" href="shop.html">Verder winkelen</a></div>';
        window.scrollTo(0, 0);
      };
      var laadSdk = function (cb) {
        if (window.paypal) return cb();
        var sc = document.createElement("script");
        sc.src = "https://www.paypal.com/sdk/js?client-id=" + encodeURIComponent(cfg.paypal.clientId) + "&components=card-fields,buttons&currency=EUR&intent=capture&locale=nl_NL&disable-funding=paylater,venmo,sepa,ideal,bancontact,blik,eps,mybank,p24,giropay,sofort";
        sc.onload = cb; sc.onerror = function () { bf.textContent = "De betaalpagina kon niet worden geladen. Ververs de pagina en probeer het opnieuw."; };
        document.head.appendChild(sc);
      };
      var maak = function () { return api({ actie: "pp_maak", nr: order.nr, token: order.token, methode: "Creditcard" }).then(function (j) { if (j.fout) throw new Error(j.fout); return j.id; }); };
      var klaar = function (data) {
        bezig(true, "Betaling controleren…");
        return api({ actie: "pp_vang", nr: order.nr, token: order.token, id: data.orderID }).then(function (j) {
          if (j.fout) { bezig(false); bf.textContent = j.fout; return; }
          bedankt(j.order);
        });
      };
      var fout = function (e) { bezig(false); bf.textContent = (e && e.message && !/^[A-Z_]+$/.test(e.message) && e.message.length < 200 ? e.message : "De betaling is niet gelukt. Controleer je kaartgegevens of probeer een andere kaart."); };
      var toonKaart = function () {
        if (!cfg) { setTimeout(toonKaart, 200); return; }
        if (!cfg.paypal) { $("#kaartvelden").hidden = true; bk.hidden = true; bf.textContent = "Betalen met creditcard wordt op dit moment geactiveerd. Probeer het later nog eens of neem contact met ons op."; return; }
        laadSdk(function () {
          var stijl = { input: { "font-size": "16px", "font-family": "Jost, system-ui, sans-serif", color: "#3A2D25", padding: "12px" }, ".invalid": { color: "#8A3B2E" } };
          kaart = window.paypal.CardFields({ createOrder: maak, onApprove: klaar, onError: fout, style: stijl });
          if (kaart.isEligible()) {
            kaart.NameField({ placeholder: "Naam op de kaart" }).render("#cf-naam");
            kaart.NumberField({ placeholder: "Kaartnummer" }).render("#cf-nummer");
            kaart.ExpiryField({ placeholder: "MM / JJ" }).render("#cf-datum");
            kaart.CVVField({ placeholder: "CVC" }).render("#cf-cvv");
            bezig(false);
          } else {
            $("#kaartvelden").hidden = true; bk.hidden = true;
            window.paypal.Buttons({ fundingSource: window.paypal.FUNDING.CARD, style: { color: "black", label: "pay", shape: "rect" }, createOrder: maak, onApprove: klaar, onError: fout }).render("#kaartknop");
          }
        });
      };
      bk.addEventListener("click", function () {
        if (!kaart) return; bf.textContent = ""; bezig(true, "Bezig met betalen…");
        kaart.getState().then(function (st) {
          var ok = st && st.fields && Object.keys(st.fields).every(function (k) { return st.fields[k].isValid; });
          if (!ok) { bezig(false); bf.textContent = "Controleer je kaartgegevens: niet alle velden zijn goed ingevuld."; return; }
          return kaart.submit().catch(fout);
        }).catch(fout);
      });
      f.addEventListener("submit", function (e) {
        e.preventDefault();
        var leeg = $$("[required]", f).filter(function (i) { return i.type === "checkbox" ? !i.checked : (!i.value.trim() || !i.checkValidity()); })[0];
        if (leeg) { $("#fout").textContent = leeg.type === "checkbox" ? "Ga akkoord met de algemene voorwaarden om verder te gaan." : "Vul alle verplichte velden correct in."; leeg.focus(); return; }
        var v = function (n) { return f.elements[n].value.trim(); }, knop = $("#naar-betalen");
        knop.disabled = true; knop.textContent = "Bezig…"; $("#fout").textContent = "";
        api({ actie: "start", site: basis(), akkoord: f.elements.akkoord.checked, cadeau: !!cad2,
          klant: { naam: v("voornaam") + " " + v("achternaam"), email: v("email"), tel: v("tel"), postcode: v("postcode"), huisnummer: v("huisnummer"), straat: v("straat"), plaats: v("plaats"), land: f.elements.land.value },
          regels: m2.map(function (r) { var p = vind(r.id); return { id: r.id, a: r.a, uitvoering: r.u || "", maat: p.maten && p.maten.length ? p.maten[0] + " cm" : "" }; })
        }).then(function (j) {
          knop.disabled = false; knop.textContent = "Verder naar betalen";
          if (j.fout) { $("#fout").textContent = j.fout; return; }
          order = j; $("#overzicht").innerHTML = regelsHtml(j);
          $("#gegevens").hidden = true; $("#betalen").hidden = false; stap(2);
          $("#kaart-voor").textContent = "Totaal " + euro(j.totaal) + " · ordernummer " + j.nr;
          bk.textContent = "Betaal " + euro(j.totaal) + " veilig"; bk.disabled = true;
          if (!kaart) toonKaart(); else bezig(false);
          $("#betalen").scrollIntoView({ behavior: "smooth", block: "start" });
        });
      });
      $("#wijzig").addEventListener("click", function () { $("#betalen").hidden = true; $("#gegevens").hidden = false; stap(1); });
    }
  }

  /* bestelling volgen */
  var STATUS = ["betaald", "besteld", "verzonden", "geleverd"], STATUSNAAM = { betaald: "Betaald", besteld: "In behandeling", verzonden: "Verzonden", geleverd: "Bezorgd" };
  function toonOrder(o) {
    var i = STATUS.indexOf(o.status);
    return '<div class="orderkaart"><span class="klein">Bestelling ' + esc(o.nr) + '</span><h2>' + esc(o.status_tekst) + '</h2>' +
      (i > -1 ? '<ol class="statusbalk">' + STATUS.map(function (s, k) { return '<li class="' + (k <= i ? "klaar" : "") + '">' + STATUSNAAM[s] + "</li>"; }).join("") + "</ol>" : "") +
      (o.track_trace ? '<p><b>Track-and-trace:</b> ' + esc(o.vervoerder || "") + ' ' + (/^https?:\/\//.test(o.track_trace) ? '<a class="link" href="' + esc(o.track_trace) + '" rel="noopener" target="_blank">volg je pakket</a>' : esc(o.track_trace)) + '</p>' : "") +
      '<div class="samenvatting">' + o.regels.map(function (r) { return '<div class="rij"><span>' + r.aantal + " × " + esc(r.naam) + "</span><span>" + euro(r.prijs * r.aantal) + "</span></div>"; }).join("") +
      '<div class="rij totaal"><span>Totaal</span><span>' + euro(+o.totaal) + "</span></div></div>" +
      '<p class="noot">Besteld op ' + new Date(o.created_at).toLocaleDateString("nl-NL", { day: "numeric", month: "long", year: "numeric" }) + (o.betaalmethode ? ' · betaald met ' + esc(o.betaalmethode) : '') + '</p></div>';
  }
  if (pag === "bestelling") {
    var vf = $("#volg"), uit = $("#volg-uitslag");
    if (url.get("nr") && url.get("t")) api({ actie: "status", nr: url.get("nr"), token: url.get("t") }).then(function (j) { if (j.order) { uit.innerHTML = toonOrder(j.order); vf.hidden = true; } });
    vf.addEventListener("submit", function (e) {
      e.preventDefault(); var fo = $("#volg-fout");
      if (!vf.elements.nr.value.trim() || !vf.elements.email.checkValidity() || !vf.elements.email.value) { fo.textContent = "Vul je ordernummer en e-mailadres in."; return; }
      fo.textContent = "Bezig met zoeken…";
      api({ actie: "status", nr: vf.elements.nr.value.trim(), email: vf.elements.email.value.trim() }).then(function (j) {
        if (j.fout) { fo.textContent = j.fout; return; } fo.textContent = ""; uit.innerHTML = toonOrder(j.order);
      });
    });
  }

  /* vraag de prijs voor een andere maat */
  function vraagMaat(p, maat) {
    var d = document.createElement("dialog"); d.className = "maatdlg";
    d.innerHTML = '<form method="dialog" class="form" novalidate><h2 style="font-size:30px">Prijs aanvragen</h2><p>' + esc(p.n) + ', maat <b>' + esc(maat) + '</b>. We mailen je de prijs en levertijd, meestal binnen één werkdag.</p>' +
      '<label>Naam *<input name="naam" required autocomplete="name"></label><label>E-mailadres *<input name="email" type="email" required autocomplete="email"></label><p class="fout" role="alert"></p>' +
      '<div style="display:flex;gap:12px;flex-wrap:wrap"><button class="knop" value="ok">Vraag de prijs aan</button><button class="knop licht" value="nee" formnovalidate>Annuleren</button></div></form>';
    document.body.appendChild(d); d.showModal();
    var fm = $("form", d);
    fm.addEventListener("submit", function (e) {
      if (e.submitter && e.submitter.value === "nee") return;
      e.preventDefault();
      if (!fm.elements.naam.value.trim() || !fm.elements.email.value || !fm.elements.email.checkValidity()) { $(".fout", fm).textContent = "Vul je naam en e-mailadres in."; return; }
      $(".fout", fm).textContent = "Bezig…";
      api({ actie: "bericht", soort: "maatprijs", naam: fm.elements.naam.value, email: fm.elements.email.value, velden: { Product: p.n + " (nr. " + p.nr + ")", Maat: maat, Link: location.href } }).then(function (j) {
        if (j.fout) { $(".fout", fm).textContent = j.fout; return; }
        fm.innerHTML = '<h2 style="font-size:30px">Aanvraag ontvangen</h2><p>Dank je wel. Je krijgt de prijs voor maat ' + esc(maat) + ' per e-mail.</p><button class="knop" value="nee">Sluiten</button>';
      });
    });
    d.addEventListener("close", function () { d.remove(); });
  }

  function toonFavorieten() {
    var f = favs().map(vind).filter(Boolean);
    $("#fav-grid").innerHTML = f.map(kaart).join("");
    $("#fav-leeg").hidden = !!f.length;
  }
  if (pag === "favorieten") toonFavorieten();

  /* bestelbalie voor Kim */
  if (pag === "beheer") {
    var sessie = lees("beheer-sessie", ""), data = null;
    var toon = function (id) { ["bh-setup", "bh-login", "bh-app"].forEach(function (x) { $("#" + x).hidden = x !== id; }); };
    var code = url.get("setup");
    if (code) toon("bh-setup"); else if (sessie) laad(); else toon("bh-login");
    $("#bh-setup").addEventListener("submit", function (e) {
      e.preventDefault(); var f = this, fo = $(".fout", f);
      if (f.elements.pw.value.length < 10) { fo.textContent = "Kies minstens 10 tekens."; return; }
      if (f.elements.pw.value !== f.elements.pw2.value) { fo.textContent = "De wachtwoorden zijn niet gelijk."; return; }
      fo.textContent = "Bezig…";
      api({ actie: "setup", code: code, wachtwoord: f.elements.pw.value }).then(function (j) {
        if (j.fout) { fo.textContent = j.fout; return; }
        history.replaceState(null, "", location.pathname); toon("bh-login"); $(".fout", $("#bh-login")).textContent = "Je wachtwoord is opgeslagen. Log nu in.";
      });
    });
    $("#bh-login").addEventListener("submit", function (e) {
      e.preventDefault(); var f = this, fo = $(".fout", f); fo.textContent = "Bezig…";
      api({ actie: "login", wachtwoord: f.elements.pw.value }).then(function (j) {
        if (j.fout) { fo.textContent = j.fout; return; }
        sessie = j.sessie; bewaar("beheer-sessie", sessie); f.reset(); fo.textContent = ""; laad();
      });
    });
    $("#bh-uit").addEventListener("click", function () { api({ actie: "uitloggen", sessie: sessie }); sessie = ""; bewaar("beheer-sessie", ""); toon("bh-login"); });
    $$(".bh-tabs button").forEach(function (t) { t.addEventListener("click", function () {
      $$(".bh-tabs button").forEach(function (x) { x.setAttribute("aria-selected", x === t); });
      var tb = t.getAttribute("data-tab"); $("#bh-orders").hidden = tb !== "orders"; $("#bh-berichten").hidden = tb !== "berichten"; $("#bh-producten").hidden = tb !== "producten"; $("#bh-kpi").hidden = tb === "producten"; if (tb === "producten") laadProducten();
    }); });
    function laad() {
      api({ actie: "lijst", sessie: sessie }).then(function (j) {
        if (j.fout) { sessie = ""; bewaar("beheer-sessie", ""); toon("bh-login"); if (j._status !== 401) $(".fout", $("#bh-login")).textContent = j.fout; return; }
        data = j; toon("bh-app"); teken();
      });
    }
    function teken() {
      var o = data.orders, echt = o.filter(function (x) { return !x.test; });
      var omzet = echt.filter(function (x) { return ["betaald", "besteld", "verzonden", "geleverd"].indexOf(x.status) > -1; }).reduce(function (s, x) { return s + (+x.totaal); }, 0);
      var open = o.filter(function (x) { return x.status === "betaald" || x.status === "besteld"; }).length;
      $("#bh-pp").textContent = data.paypal === "live" ? "Creditcardbetalingen: live" : data.paypal === "test" ? "Creditcardbetalingen: testmodus" : "Creditcardbetalingen: nog niet gekoppeld";
      $("#bh-kpi").innerHTML = '<div><b>' + open + '</b><span>Te versturen</span></div><div><b>' + echt.length + '</b><span>Bestellingen</span></div><div><b>' + euro(omzet) + '</b><span>Omzet (betaald)</span></div><div><b>' + data.berichten.filter(function (x) { return !x.afgehandeld; }).length + '</b><span>Open berichten</span></div>';
      var opties = Object.keys(data.stappen).filter(function (k) { return k !== "open"; });
      $("#bh-orders").innerHTML = o.length ? o.map(function (x) {
        return '<details class="bh-order"' + (x.status === "betaald" ? " open" : "") + '><summary><b>' + esc(x.nr) + '</b><span>' + new Date(x.created_at).toLocaleString("nl-NL", { dateStyle: "medium", timeStyle: "short" }) + '</span><span>' + esc(x.klant_naam) + '</span><span>' + euro(+x.totaal) + '</span><span class="bh-status s-' + x.status + '">' + esc(data.stappen[x.status]) + (x.test ? " · test" : "") + '</span></summary>' +
          '<div class="bh-grid"><div><h3>Producten</h3>' + x.regels.map(function (r) { var lv = (data.leveranciers || {})[r.nr]; return '<p>' + r.aantal + ' × ' + esc(r.naam) + (r.nr ? ' <small>(nr. ' + r.nr + ')</small>' : '') + (r.maat ? '<br><small>Maat ' + esc(r.maat) + '</small>' : '') + (r.uitvoering ? '<br><small>Uitvoering ' + esc(r.uitvoering) + '</small>' : '') + (lv ? '<br><a class="bh-lev" href="' + esc(lv) + '" target="_blank" rel="noopener">Bestel bij leverancier ↗</a>' : '<br><small>Nog geen leverancierslink (voeg toe onder Producten)</small>') + '</p>'; }).join("") +
          '<p><small>Verzending ' + (+x.verzending ? euro(+x.verzending) : "gratis") + (+x.cadeau ? ' · cadeauverpakking' : '') + ' · ' + esc(x.betaalmethode || "") + '</small></p></div>' +
          '<div><h3>Klant</h3><p>' + esc(x.klant_naam) + '<br>' + esc(x.adres.straat) + ' ' + esc(x.adres.huisnummer) + '<br>' + esc(x.adres.postcode) + ' ' + esc(x.adres.plaats) + '<br>' + esc(x.adres.land) + '</p><p><a class="link" href="mailto:' + esc(x.klant_email) + '?subject=' + encodeURIComponent("Je bestelling " + x.nr) + '">' + esc(x.klant_email) + '</a>' + (x.klant_tel ? '<br>' + esc(x.klant_tel) : '') + '</p><p><button type="button" class="bh-kopie" data-kopie="' + esc(x.klant_naam + "\n" + x.adres.straat + " " + x.adres.huisnummer + "\n" + x.adres.postcode + " " + x.adres.plaats + "\n" + (x.adres.land === "België" ? "Belgium" : "Netherlands") + (x.klant_tel ? "\nTel: " + x.klant_tel : "")) + '">Kopieer adres voor leverancier</button> <button type="button" class="bh-kopie" data-kopie="' + esc(data.notitie || "") + '">Kopieer notitie voor verkoper</button></p></div>' +
          '<form class="form bh-upd" data-nr="' + esc(x.nr) + '"><h3>Afhandelen</h3><label>Status<select name="status">' + opties.map(function (k) { return '<option value="' + k + '"' + (k === x.status ? " selected" : "") + '>' + esc(data.stappen[k]) + '</option>'; }).join("") + '</select></label>' +
          '<label>Ordernummer bij leverancier<input name="leverancier_ordernr" value="' + esc(x.leverancier_ordernr || "") + '"></label><div class="twee"><label>Vervoerder<input name="vervoerder" value="' + esc(x.vervoerder || "") + '" placeholder="PostNL"></label><label>Track-and-trace (code of link)<input name="track_trace" value="' + esc(x.track_trace || "") + '"></label></div>' +
          '<label>Notitie (alleen voor jou)<textarea name="notitie">' + esc(x.notitie || "") + '</textarea></label><label class="check"><input type="checkbox" name="mail_klant" checked><span>Mail de klant bij een nieuwe status</span></label><button class="knop" type="submit">Opslaan</button><p class="bevestig" role="status"></p></form></div></details>';
      }).join("") : '<p class="leeg-bh">Nog geen bestellingen. Zodra er iemand betaalt, staat de bestelling hier en krijg je een mail.</p>';
      $("#bh-berichten").innerHTML = data.berichten.length ? data.berichten.map(function (b) {
        var nm = { contact: "Bericht", herroeping: "Herroeping", nieuwsbrief: "Nieuwsbrief", maatprijs: "Prijsaanvraag maat" }[b.soort];
        return '<div class="bh-bericht' + (b.afgehandeld ? " af" : "") + '"><div><b>' + nm + '</b> · ' + new Date(b.created_at).toLocaleString("nl-NL", { dateStyle: "medium", timeStyle: "short" }) + '<br>' + esc(b.naam || "") + ' <a class="link" href="mailto:' + esc(b.email) + '">' + esc(b.email) + '</a></div>' +
          Object.keys(b.velden || {}).map(function (k) { return '<p><small>' + esc(k) + '</small><br>' + esc(b.velden[k]) + '</p>'; }).join("") +
          '<label class="check"><input type="checkbox" data-af="' + b.id + '"' + (b.afgehandeld ? " checked" : "") + '><span>Afgehandeld</span></label></div>';
      }).join("") : '<p class="leeg-bh">Nog geen berichten.</p>';
    }
    $("#bh-orders").addEventListener("submit", function (e) {
      var f = e.target.closest(".bh-upd"); if (!f) return; e.preventDefault();
      var bv = $(".bevestig", f); bv.textContent = "Bezig met opslaan…";
      api({ actie: "update", sessie: sessie, nr: f.getAttribute("data-nr"), status: f.elements.status.value, leverancier_ordernr: f.elements.leverancier_ordernr.value, vervoerder: f.elements.vervoerder.value, track_trace: f.elements.track_trace.value, notitie: f.elements.notitie.value, mail_klant: f.elements.mail_klant.checked })
        .then(function (j) { if (j.fout) { bv.textContent = j.fout; return; } bv.textContent = "Opgeslagen."; setTimeout(laad, 600); });
    });
    document.addEventListener("click", function (e) {
      var k = e.target.closest(".bh-kopie"); if (!k) return;
      var t = k.getAttribute("data-kopie"), oud = k.textContent;
      (navigator.clipboard ? navigator.clipboard.writeText(t) : Promise.reject()).then(function () { k.textContent = "Gekopieerd ✓"; }, function () { window.prompt("Kopieer deze tekst:", t); }).then(function () { setTimeout(function () { k.textContent = oud; }, 1600); });
    });
    var pdata = null, fotos = [];
    var SUBS = { wonen: [["schilderijen", "Schilderijen"], ["spiegels", "Spiegels"], ["beeldjes", "Beeldjes & objecten"], ["bloempotten", "Bloempotten"], ["droogbloemen", "Droogbloemen"]], vazen: [["glazen-vazen", "Glazen vazen"], ["stenen-vazen", "Stenen vazen"], ["rotan-vazen", "Rotan vazen"]], verlichting: [["lampen", "Lampen"], ["lampenkappen", "Lampenkappen"], ["kaarsen", "Kaarsen & windlichten"]], textiel: [["kussenhoezen", "Kussenhoezen"], ["plaids", "Plaids"], ["vloerkleden", "Vloerkleden"], ["beddengoed", "Beddengoed"], ["gordijnen", "Gordijnen & vitrage"], ["vloerkussens", "Vloerkussens"]], tafel: [["servies", "Servies"], ["schalen", "Schalen & dienbladen"], ["tafellinnen", "Servetten & placemats"]], meubels: [["bijzettafels", "Bijzettafels"], ["salontafels", "Salontafels"], ["eettafels", "Eettafels"], ["eetkamerstoelen", "Eetkamerstoelen"], ["stoelen", "Stoelen"], ["fauteuils", "Fauteuils"], ["bankjes", "Bankjes"], ["krukken", "Barkrukken"], ["kasten", "Kasten & nachtkastjes"]] };
    var CATN = { wonen: "Wonen & decoratie", vazen: "Vazen", verlichting: "Verlichting & kaarsen", textiel: "Textiel", tafel: "Servies & tafel", meubels: "Meubels" };
    function laadProducten() {
      $("#bh-producten").innerHTML = '<p class="leeg-bh">Bezig met laden…</p>';
      api({ actie: "producten_beheer", sessie: sessie }).then(function (j) { if (j.fout) { $("#bh-producten").innerHTML = '<p class="fout">' + esc(j.fout) + '</p>'; return; } pdata = j; tekenProducten(); });
    }
    function prodForm(p, lev) {
      p = p || {}; fotos = (p.u || []).slice();
      var cat = p.c || "wonen";
      return '<form class="form bh-pform" novalidate><h3>' + (p.nr ? "Product " + p.nr + " bewerken" : "Nieuw product toevoegen") + '</h3><input type="hidden" name="nr" value="' + (p.nr || "") + '">' +
        '<label>Naam<input name="n" required maxlength="120" value="' + esc(p.n || "") + '"></label>' +
        '<div class="twee"><label>Prijs (€, incl. btw)<input name="p" required inputmode="decimal" value="' + (p.p ? String(p.p).replace(".", ",") : "") + '"></label><label>Levertijd<input name="lt" value="' + esc(p.lt || "8–15 werkdagen") + '"></label></div>' +
        '<div class="twee"><label>Categorie<select name="c">' + Object.keys(CATN).map(function (k) { return '<option value="' + k + '"' + (k === cat ? " selected" : "") + '>' + CATN[k] + '</option>'; }).join("") + '</select></label><label>Subcategorie<select name="s">' + SUBS[cat].map(function (x) { return '<option value="' + x[0] + '"' + (x[0] === p.s ? " selected" : "") + '>' + x[1] + '</option>'; }).join("") + '</select></label></div>' +
        '<label>Materiaal<input name="m" maxlength="300" value="' + esc(p.m || "") + '" placeholder="Bijv. Handgemaakt keramiek."></label>' +
        '<label>Afmetingen<input name="d" maxlength="300" value="' + esc(p.d || "") + '" placeholder="Bijv. Ca. 20 × 30 cm (Ø × h)."></label>' +
        '<label>Maten om uit te kiezen (optioneel, gescheiden door komma’s; de eerste maat hoort bij de prijs)<input name="maten" value="' + esc((p.maten || []).join(", ")) + '" placeholder="Bijv. 40 × 60, 50 × 80"></label>' +
        '<label>Korte omschrijving<textarea name="t" maxlength="600">' + esc(p.t || "") + '</textarea></label>' +
        '<label>Link naar de leverancier (alleen voor jou zichtbaar)<input name="lev" value="' + esc(lev || "") + '" placeholder="https://www.aliexpress.com/item/…"></label>' +
        '<div class="bh-fotos"></div><label class="bh-upload">Foto’s toevoegen vanaf je computer of telefoon (de eerste foto is de hoofdfoto)<input type="file" name="foto" accept="image/jpeg,image/png,image/webp" multiple></label>' +
        '<label>Of plak fotolinks (één per regel), bijvoorbeeld van de leverancier<textarea name="fotolinks" rows="3" placeholder="https://…jpg"></textarea></label><p><button type="button" class="bh-kopie" data-flinks>Foto’s van deze links toevoegen</button></p>' +
        '<label class="check"><input type="checkbox" name="actief"' + (p.nr && pdata && pdata.producten.some(function (r) { return r.nr === p.nr && !r.actief; }) ? "" : " checked") + '><span>Zichtbaar in de winkel</span></label>' +
        '<button class="knop" type="submit">Opslaan</button> <button class="link" type="button" data-pannuleer>Annuleren</button><p class="bevestig" role="status"></p></form>';
    }
    function tekenFotos(f) {
      $(".bh-fotos", f).innerHTML = fotos.map(function (u, i) { return '<figure><img src="' + esc(u) + '" alt=""><button type="button" data-fweg="' + i + '" aria-label="Foto verwijderen">×</button>' + (i ? '<button type="button" data-feerst="' + i + '">Hoofdfoto</button>' : '<small>Hoofdfoto</small>') + '</figure>'; }).join("");
    }
    function tekenProducten() {
      var eigen = pdata.producten, lv = {}; (pdata.leveranciers || []).forEach(function (r) { lv[r.nr] = r.url; });
      var vast = P.filter(function (p) { return p.nr && p.nr < 1000; }).sort(function (a, b) { return a.nr - b.nr; });
      $("#bh-producten").innerHTML = '<p><button class="knop" type="button" data-pnieuw>Nieuw product toevoegen</button></p><div id="bh-pedit"></div>' +
        '<h3>Jouw toegevoegde producten</h3>' + (eigen.length ? eigen.map(function (r) { var p = r.data; return '<div class="bh-prod"><img src="' + esc((p.u || [])[0] || "") + '" alt=""><div><b>' + esc(p.n) + '</b><br><small>nr. ' + r.nr + ' · ' + euro(+p.p) + ' · ' + (r.actief ? "zichtbaar" : "verborgen") + (r.leverancier ? ' · <a class="link" href="' + esc(r.leverancier) + '" target="_blank" rel="noopener">leverancier ↗</a>' : ' · geen leverancierslink') + '</small></div><button type="button" class="link" data-pbewerk="' + r.nr + '">Bewerken</button></div>'; }).join("") : '<p class="leeg-bh">Nog geen eigen producten. Voeg er hierboven een toe.</p>') +
        '<h3>Leverancierslinks van de bestaande producten</h3><p><small>Klopt een link niet meer of wil je een andere leverancier? Pas hem hier aan; hij verschijnt dan bij nieuwe bestellingen.</small></p>' +
        vast.map(function (p) { return '<form class="bh-levrij" data-nr="' + p.nr + '"><span><b>' + p.nr + '</b> ' + esc(p.n) + '</span><input name="url" value="' + esc(lv[p.nr] || "") + '" placeholder="https://…" aria-label="Leverancierslink voor ' + esc(p.n) + '"><button type="submit">Opslaan</button><small role="status"></small></form>'; }).join("");
    }
    $("#bh-producten").addEventListener("click", function (e) {
      var t = e.target;
      if (t.closest("[data-pnieuw]")) { $("#bh-pedit").innerHTML = prodForm(null, ""); tekenFotos($(".bh-pform")); $("#bh-pedit").scrollIntoView({ behavior: "smooth" }); }
      var b = t.closest("[data-pbewerk]"); if (b) { var r = pdata.producten.filter(function (x) { return x.nr === +b.getAttribute("data-pbewerk"); })[0]; $("#bh-pedit").innerHTML = prodForm(r.data, r.leverancier || ""); tekenFotos($(".bh-pform")); $("#bh-pedit").scrollIntoView({ behavior: "smooth" }); }
      if (t.closest("[data-pannuleer]")) $("#bh-pedit").innerHTML = "";
      if (t.closest("[data-flinks]")) {
        var pf = $(".bh-pform"), bv0 = $(".bevestig", pf), links = pf.elements.fotolinks.value.split(/\s+/).filter(function (x) { return /^https:\/\//.test(x); });
        var stap = function () { var u = links.shift(); if (!u) { bv0.textContent = "Foto’s staan klaar. Vergeet niet op te slaan."; pf.elements.fotolinks.value = ""; return; } bv0.textContent = "Foto ophalen… (" + (links.length + 1) + " te gaan)"; api({ actie: "product_foto", sessie: sessie, url: u }).then(function (j) { if (j.fout) bv0.textContent = j.fout; else { fotos.push(j.url); tekenFotos(pf); } stap(); }); };
        stap();
      }
      var w = t.closest("[data-fweg]"); if (w) { fotos.splice(+w.getAttribute("data-fweg"), 1); tekenFotos($(".bh-pform")); }
      var h = t.closest("[data-feerst]"); if (h) { var i = +h.getAttribute("data-feerst"); fotos.unshift(fotos.splice(i, 1)[0]); tekenFotos($(".bh-pform")); }
    });
    $("#bh-producten").addEventListener("change", function (e) {
      var f = e.target.closest(".bh-pform"); if (!f) return;
      if (e.target.name === "c") f.elements.s.innerHTML = SUBS[e.target.value].map(function (x) { return '<option value="' + x[0] + '">' + x[1] + '</option>'; }).join("");
      if (e.target.name === "foto") {
        var bv = $(".bevestig", f), lijst = Array.prototype.slice.call(e.target.files); e.target.value = "";
        var volgende = function () {
          var file = lijst.shift(); if (!file) { bv.textContent = "Foto’s staan klaar. Vergeet niet op te slaan."; return; }
          bv.textContent = "Foto uploaden… (" + (lijst.length + 1) + " te gaan)";
          verklein(file, function (data) { api({ actie: "product_foto", sessie: sessie, data: data }).then(function (j) { if (j.fout) { bv.textContent = j.fout; return; } fotos.push(j.url); tekenFotos(f); volgende(); }); });
        };
        volgende();
      }
    });
    function verklein(file, klaar) {
      var img = new Image(), rd = new FileReader();
      rd.onload = function () { img.onload = function () { var m = 2000, s = Math.min(1, m / Math.max(img.width, img.height)), c = document.createElement("canvas"); c.width = Math.round(img.width * s); c.height = Math.round(img.height * s); c.getContext("2d").drawImage(img, 0, 0, c.width, c.height); klaar(c.toDataURL("image/jpeg", 0.88)); }; img.src = rd.result; };
      rd.readAsDataURL(file);
    }
    $("#bh-producten").addEventListener("submit", function (e) {
      var f = e.target.closest(".bh-pform"), r = e.target.closest(".bh-levrij"); e.preventDefault();
      if (r) { var st = $("small", r); st.textContent = "…"; api({ actie: "leverancier", sessie: sessie, nr: +r.getAttribute("data-nr"), url: r.elements.url.value.trim() }).then(function (j) { st.textContent = j.fout || "Opgeslagen"; }); return; }
      if (!f) return;
      var el = f.elements, bv = $(".bevestig", f);
      var prod = { nr: +el.nr.value || 0, n: el.n.value, p: el.p.value, lt: el.lt.value, c: el.c.value, s: el.s.value, m: el.m.value, d: el.d.value, maten: el.maten.value, t: el.t.value, u: fotos, actief: el.actief.checked };
      bv.textContent = "Bezig met opslaan…";
      api({ actie: "product_opslaan", sessie: sessie, product: prod, leverancier: el.lev.value.trim() }).then(function (j) {
        if (j.fout) { bv.textContent = j.fout; return; }
        try { sessionStorage.removeItem("suis-eigen"); } catch (x) {}
        bv.textContent = "Opgeslagen. Het product staat binnen een paar minuten in je winkel.";
        setTimeout(laadProducten, 900);
      });
    });
    $("#bh-berichten").addEventListener("change", function (e) {
      var c = e.target.closest("[data-af]"); if (!c) return;
      api({ actie: "bericht_af", sessie: sessie, id: +c.getAttribute("data-af"), af: c.checked }).then(function () { c.closest(".bh-bericht").classList.toggle("af", c.checked); });
    });
  }

  tellers();
}
/* eigen producten van Kim (toegevoegd via de bestelbalie) eerst ophalen, dan de winkel tonen */
(function () {
  var klaar = false, voeg = function (lijst) {
    var x = window.SUIS_EXTRA = window.SUIS_EXTRA || [], ids = {};
    x.forEach(function (p) { ids[p.id] = 1; });
    (lijst || []).forEach(function (p) { if (p && p.id && !ids[p.id]) { x.push(p); ids[p.id] = 1; } });
  };
  var start = function () { if (klaar) return; klaar = true; suisStart(); };
  var cache = null; try { cache = JSON.parse(sessionStorage.getItem("suis-eigen") || "null"); } catch (e) {}
  if (cache && Date.now() - cache.t < 300000) { voeg(cache.p); start(); return; }
  if (!API) { start(); return; }
  setTimeout(start, 2500);
  fetch(API, { method: "POST", headers: { "Content-Type": "application/json" }, body: '{"actie":"producten"}' })
    .then(function (r) { return r.json(); })
    .then(function (j) { var l = j.producten || []; try { sessionStorage.setItem("suis-eigen", JSON.stringify({ t: Date.now(), p: l })); } catch (e) {} if (!klaar) voeg(l); start(); })
    .catch(start);
})();
