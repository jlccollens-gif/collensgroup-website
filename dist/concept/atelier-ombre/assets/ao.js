/* Atelier Ombre – concept-webshop (Collens Group). Werkt volledig in de browser; er wordt niets echt besteld of betaald. */
(function () {
  "use strict";
  var CATS = { schilderijen: "Schilderijen", beelden: "Beelden & objecten", vondsten: "Vondsten" };
  var CAT_TEKST = {
    schilderijen: "Originele werken op doek en papier, van verstild wit tot uitgesproken kleur.",
    beelden: "Brons, steen en porselein. Kleine oplages en unica voor kast, sokkel of tafel.",
    vondsten: "Gevonden schatten met een verhaal: studiokeramiek en beelden uit privécollecties."
  };
  var MAKERS = { "ines-vaerman": "Ines Vaerman", "teo-brakel": "Teo Brakel", "noor-ilhan": "Noor Ilhan", "atelier-ruys": "Atelier Ruys", "onbekend": "Maker onbekend" };
  /* model: c = consignatie (commissie), p = print op bestelling, i = eigen inkoop. kost = inkoop (p/i), lv = verzendkosten voor de winkel */
  var W = [
    { id: "relief-i", n: "Relief I", m: "ines-vaerman", j: "2025", c: "schilderijen", p: 1450, mat: "Gips en acryl op doek", w: 80, h: 100, img: "w-relief-i", wand: 1, l: "Unicum", model: "c", lv: 35, t: "Een wit reliëf vol horizontale lagen, als zand na eb. In strijklicht verschijnen diepe schaduwen; bij daglicht wordt het werk bijna stil." },
    { id: "golf", n: "Golf", m: "ines-vaerman", j: "2025", c: "schilderijen", p: 890, mat: "Structuurpasta op doek", w: 60, h: 80, img: "w-golf", wand: 1, l: "Unicum", model: "c", lv: 25, t: "Zachte bogen in één kleur. Een werk dat je niet ziet maar voelt, ideaal voor slaapkamer of werkplek." },
    { id: "wit-ii", n: "Wit II", m: "ines-vaerman", j: "2024", c: "schilderijen", p: 2650, mat: "Kalk en marmerpoeder op doek", w: 100, h: 100, img: "w-wit-ii", wand: 1, l: "Unicum", model: "c", lv: 85, t: "Het grootste werk uit de reeks Wit. Grof gezet met het paletmes, met een matte, minerale huid." },
    { id: "kalk", n: "Kalk", m: "ines-vaerman", j: "2024", c: "schilderijen", p: 620, mat: "Kalkverf op linnen", w: 50, h: 75, img: "w-kalk", wand: 1, l: "Unicum", model: "c", lv: 25, t: "Lagen kalkverf in grijs en zand, als een oude muur in het zuiden. Klein genoeg voor een gang of nis." },
    { id: "beweging", n: "Beweging", m: "teo-brakel", j: "2025", c: "schilderijen", p: 3800, mat: "Acryl en houtskool op doek", w: 120, h: 120, img: "w-beweging", wand: 1, l: "Unicum", model: "c", lv: 95, t: "Brede zwarte banen die over en onder elkaar lijken te schuiven. Een statement boven een lange bank of in een hal met hoogte." },
    { id: "nacht", n: "Nacht", m: "teo-brakel", j: "2023", c: "schilderijen", p: 480, mat: "Acryl op papier, ingelijst", w: 54, h: 72, img: "w-nacht", wand: 1, l: "Unicum", model: "c", lv: 25, t: "Een werk op papier met een zware zwarte horizon. Geleverd in een zwarte houten lijst met museumglas." },
    { id: "zomer-in-rood", n: "Zomer in rood", m: "noor-ilhan", j: "2025", c: "schilderijen", p: 1150, mat: "Olieverf op doek", w: 100, h: 75, img: "w-kleur", wand: 1, l: "Unicum", model: "c", lv: 45, t: "Rood, oker en kobalt in dikke lagen. Het meest uitgesproken werk in de collectie en een directe energiebron in een rustig interieur." },
    { id: "terra", n: "Terra", m: "noor-ilhan", j: "2025", c: "schilderijen", p: 245, mat: "Giclée-print op Hahnemühle-papier", w: 60, h: 45, img: "w-terra", wand: 1, l: "Oplage 30", model: "p", kost: 58, lv: 12, t: "Zachte vormen in terracotta en zand. Genummerd en gesigneerd, gedrukt met pigmentinkt op museumpapier." },
    { id: "danser", n: "Danser", m: "atelier-ruys", j: "2025", c: "beelden", p: 1290, mat: "Brons op marmeren sokkel", d: "H 46 × B 22 × D 12 cm", img: "w-danser", l: "Oplage 8", model: "c", lv: 30, t: "Een figuur in één doorgaande lijn, gegoten in zwart gepatineerd brons. Elk exemplaar is genummerd en gesigneerd." },
    { id: "koraalschaal", n: "Koraalschaal", m: "atelier-ruys", j: "2025", c: "beelden", p: 165, mat: "Porselein, handgevormd", d: "H 14 × Ø 22 cm", img: "w-koraal", l: "Oplage 20", model: "c", lv: 12, t: "Een porseleinen schaal met een rand als koraal. Mooi leeg, of met een paar gedroogde takjes." },
    { id: "rustende-beer", n: "Rustende beer", m: "onbekend", j: "ca. 1980", c: "vondsten", p: 690, mat: "Serpentijnsteen op natuursteen", d: "H 20 × B 38 × D 14 cm", img: "w-beer", l: "Vondst", model: "i", kost: 260, lv: 25, t: "Een gepolijste beer uit één stuk steen, gevonden in een privécollectie. Lichte gebruikssporen op de sokkel passen bij de leeftijd." },
    { id: "torsovaas", n: "Torsovaas", m: "onbekend", j: "ca. 1975", c: "vondsten", p: 285, mat: "Studiokeramiek, geglazuurd steengoed", d: "H 24 × B 15 cm", img: "w-brons", l: "Vondst", model: "i", kost: 85, lv: 15, t: "Een sculpturale vaas met de vorm van een torso. Ongesigneerd, waarschijnlijk Nederlands atelierwerk uit de jaren zeventig." },
    { id: "drie-objecten", n: "Drie objecten", m: "onbekend", j: "ca. 1985", c: "vondsten", p: 195, mat: "Travertin en steengoed, set van drie", d: "H 9 tot 26 cm", img: "w-stilleven", l: "Vondst", model: "i", kost: 60, lv: 15, t: "Een blok travertin met twee flessen in roze en ivoor. Samen een stilleven, los mooi op een plank." }
  ];

  /* Huis & Beeld: echte producten van ontwerpmerken. p = voorstel verkoopprijs; ref + bron = prijs elders; maker = productpagina bij het merk */
  var H = [
    { id: "beer-mozaiek-klein", n: "Beer zilver mozaïek, klein", merk: "Richmond Interiors", c: "beelden", p: 329, b: 32.5, h: 70, d: "H 70 × B 32,5 × D 25,5 cm", mat: "Polyresin met handgesneden mozaïekglas", kleur: "#B7BBC0", ref: "£ 282 bij Olivia's (VK)", bron: "https://olivias.com/products/richmond-interiors-decorative-bear-small", maker: "https://richmondinteriors.nl/en/producten/decoratief-object-bear-silver-small/", r: "r" },
    { id: "beer-mozaiek-groot", n: "Beer zilver mozaïek, groot", merk: "Richmond Interiors", c: "beelden", p: 649, b: 46, h: 101, d: "H 101 × B 46 × D 34 cm", mat: "Polyresin met handgesneden mozaïekglas", kleur: "#B7BBC0", ref: "£ 407 in de aanbieding (normaal £ 679) bij Olivia's (VK)", bron: "https://olivias.com/products/richmond-interiors-decorative-bear-large", maker: "https://richmondinteriors.nl/en/producten/decoratief-object-bear-silver-large/", r: "r" },
    { id: "aap-goud", n: "Aap goud", merk: "Richmond Interiors", c: "beelden", p: 89, b: 21.5, h: 25, d: "H 25 × B 21,5 × D 17 cm", mat: "Polyresin, goud afgewerkt", kleur: "#C9A24A", ref: "£ 71 bij Olivia's (VK)", bron: "https://olivias.com/products/richmond-monkey-gold-ornament", maker: "https://richmondinteriors.nl/en/producten/decoratief-object-monkey-gold/", r: "r" },
    { id: "beer-berlyn", n: "Beer Berlyn, parelmoerwit", merk: "Richmond Interiors", c: "beelden", p: 39, b: 11, h: 19, d: "H 19 × B 11 × D 9 cm", mat: "Glanzend wit met regenboogglans", kleur: "#EEEBE4", ref: "£ 31 bij Belgica Furniture (VK)", bron: "https://www.belgicafurniture.com/berlyn-decorative-object-white/p55638", maker: "https://richmondinteriors.nl/en/producten/decoratief-object-berlyn-white/", r: "r" },
    { id: "beer-ave", n: "Beer Ave, wit en goud", merk: "Richmond Interiors", c: "beelden", p: 49, b: 14, h: 29, d: "H 29 × B 14 × D 9 cm", mat: "Polyresin, glanzend wit met gouden accenten", kleur: "#F3F1EC", ref: "$ 155 bij Oroa (VS); £ 41 bij Belgica Furniture (VK)", bron: "https://oroa.com/products/white-bear-decorative-object-richmond-interiors-ave", maker: "", r: "r" },
    { id: "swirl-messing", n: "Swirl, antiek messing", merk: "Richmond Interiors", c: "beelden", p: 119, b: 27, h: 46, d: "H 46 × B 27 × D 10 cm", mat: "Afwerking antiek messing", kleur: "#A88A52", ref: "vanaf £ 95 bij Olivia's (VK)", bron: "https://olivias.com/products/swirl-decorative-object-antique-brass", maker: "https://richmondinteriors.nl/en/producten/decoratief-object-swirl-brass-antique/", r: "r" },
    { id: "ptmd-vrouw", n: "Beeld Vrouw, zwart", merk: "PTMD", c: "beelden", p: 69, b: 25, h: 90, d: "H 90 × B 25 × D 27 cm", mat: "Cement, diepzwart", kleur: "#2A2A2C", ref: "€ 64 bij Yellow Webshop", bron: "https://www.yellowwebshop.com/en/go/product/159626762", maker: "", r: "p" },
    { id: "pt-imagine", n: "Figuur Imagine, zwart", merk: "Present Time", c: "beelden", p: 24.95, b: 12.5, h: 23.5, d: "H 23,5 × B 12,5 cm", mat: "Polyresin", kleur: "#26272A", ref: "€ 20,90 adviesprijs bij Galaxus", bron: "https://www.galaxus.nl/en/s14/product/present-time-imagine-decorative-figurines-and-sculptures-43106319", maker: "", r: "g" },
    { id: "ptmd-darina", n: "Wandpaneel Darina, grote golf brons", merk: "PTMD", c: "wand", p: 159, b: 120, h: 120, d: "120 × 120 cm", mat: "Wandpaneel met golfmotief, bronskleur", kleur: "#8C6A45", ref: "€ 149 in de aanbieding (normaal € 299) bij Otto (DE)", bron: "https://www.otto.de/dekoration/?marke=ptmd", maker: "", r: "p" },
    { id: "ptmd-salima", n: "Wandpaneel Salima, gesneden bloem", merk: "PTMD", c: "wand", p: 135, b: 90, h: 90, d: "90 × 90 cm", mat: "Wandpaneel, gesneden bloemmotief", kleur: "#CFC6B6", ref: "€ 129 in de aanbieding (normaal € 219) bij Otto (DE)", bron: "https://www.otto.de/dekoration/?marke=ptmd", maker: "", r: "p" },
    { id: "canvas-warme-tinten", n: "Canvas Abstracte vormen, warme tinten", merk: "De Wanddecoratie", c: "wand", p: 84.95, b: 80, h: 120, d: "80 × 120 cm", mat: "Canvas op frame van FSC/PEFC-hout, 1,8 cm", kleur: "#C98E5E", ref: "adviesprijs € 89,95 bij bol", bron: "https://www.bol.com/be/nl/p/abstracte-vormen-met-warme-tinten-abstract-wanddecoratie-muurkunst-vormen-abstracte-kunst-muurdecoratie-kinderkamer-decoratie-woonkamer-canvas-80x120-cm/9300000231539889/", maker: "", r: "w" }
  ];
  H.forEach(function (x) { x.huis = 1; });
  var ROUTE = { p: "Droppery (dropshipping)", r: "Dealeraccount Richmond", g: "Groothandel, navragen", w: "Rechtstreeks, navragen" };
  var GRATIS = 250, VERZEND = 14.95, BETAAL = 0.29, COMMISSIE = 0.4;
  var MUUR = { b: 2000, h: 2933, cm: 2000 / 184, onder: 1660, midden: 1100 }; /* bank op de foto is ca. 184 cm breed */
  var $ = function (s, r) { return (r || document).querySelector(s); };
  var $$ = function (s, r) { return Array.prototype.slice.call((r || document).querySelectorAll(s)); };
  var esc = function (s) { return String(s).replace(/[&<>"']/g, function (c) { return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]; }); };
  var euro = function (x) { var r = Math.round(x * 100) / 100, heel = Math.floor(r), cent = Math.round((r - heel) * 100); return "€ " + heel.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ".") + "," + (cent < 10 ? "0" : "") + cent; };
  var prijsKort = function (x) { return "€ " + x.toString().replace(/\B(?=(\d{3})+(?!\d))/g, "."); };
  var vind = function (id) { var alle = W.concat(H); for (var i = 0; i < alle.length; i++) if (alle[i].id === id) return alle[i]; return null; };
  var prijsMooi = function (x) { return x % 1 ? euro(x) : prijsKort(x); };
  var maat = function (x) { return x.wand ? x.w + " × " + x.h + " cm" : x.d; };
  var uniek = function (x) { return x.l === "Unicum" || x.l === "Vondst"; };

  var geheugen = {};
  function lees(k, d) { try { var v = localStorage.getItem("atelierombre-" + k); return v ? JSON.parse(v) : d; } catch (e) { return geheugen[k] || d; } }
  function bewaar(k, v) { geheugen[k] = v; try { localStorage.setItem("atelierombre-" + k, JSON.stringify(v)); } catch (e) {} }

  var toastTimer;
  function toast(tekst, actie) {
    var t = $("#toast"); if (!t) return;
    t.innerHTML = "<span>" + tekst + "</span>" + (actie || "");
    t.classList.add("aan"); clearTimeout(toastTimer);
    toastTimer = setTimeout(function () { t.classList.remove("aan"); }, 3800);
  }

  function mand() { return lees("mand", []); }
  function inMand(id) { return mand().some(function (r) { return r.id === id; }); }
  function zetMand(m) { bewaar("mand", m); tellers(); }
  function voegToe(id) {
    var x = vind(id), m = mand(), r = null;
    for (var i = 0; i < m.length; i++) if (m[i].id === id) r = m[i];
    if (r && uniek(x)) { toast("Dit is een uniek werk en staat al in je winkelmand", '<a href="winkelmand.html">Bekijk winkelmand</a>'); return; }
    if (r) r.a = Math.min(r.a + 1, 5); else m.push({ id: id, a: 1 });
    zetMand(m);
    toast("<i>" + esc(x.n) + "</i> staat in je winkelmand", '<a href="winkelmand.html">Bekijk winkelmand</a>');
    $$('[data-koop="' + id + '"]').forEach(function (b) { if (uniek(x)) { b.disabled = true; b.textContent = "In je winkelmand"; } });
  }
  function subtotaal() { return mand().reduce(function (s, r) { var x = vind(r.id); return s + (x ? x.p * r.a : 0); }, 0); }
  function favs() { return lees("favs", []); }
  function wisselFav(id) {
    var f = favs(), i = f.indexOf(id);
    if (i > -1) f.splice(i, 1); else f.push(id);
    bewaar("favs", f); tellers();
    $$('[data-fav="' + id + '"]').forEach(function (b) { b.setAttribute("aria-pressed", f.indexOf(id) > -1); });
    toast(i > -1 ? "Verwijderd uit je favorieten" : "Bewaard in je favorieten", i > -1 ? "" : '<a href="favorieten.html">Bekijk favorieten</a>');
    if (document.body.dataset.pagina === "favorieten") toonFavorieten();
  }
  function tellers() {
    var a = mand().reduce(function (s, r) { return s + r.a; }, 0), f = favs().length;
    $$("[data-teller=mand]").forEach(function (t) { t.textContent = a || ""; });
    $$("[data-teller=favs]").forEach(function (t) { t.textContent = f || ""; });
  }

  var HART = '<svg viewBox="0 0 24 24"><path d="M12 20s-7.5-4.6-7.5-10A4.3 4.3 0 0 1 12 7.4 4.3 4.3 0 0 1 19.5 10c0 5.4-7.5 10-7.5 10z"/></svg>';
  function kaart(x) {
    var fav = favs().indexOf(x.id) > -1, bezet = uniek(x) && inMand(x.id);
    return '<article class="werk">' +
      (x.l ? '<span class="label' + (x.l === "Unicum" ? " uniek" : "") + '">' + x.l + "</span>" : "") +
      '<button class="hartje" type="button" data-fav="' + x.id + '" aria-pressed="' + fav + '" aria-label="Bewaar ' + esc(x.n) + ' als favoriet">' + HART + "</button>" +
      '<div class="wand' + (x.wand ? "" : " object") + '"><img src="img/' + x.img + '.jpg" alt="' + esc(x.n + ", " + x.mat.toLowerCase()) + '" loading="lazy" width="1400" height="1750"></div>' +
      '<div class="bordje"><a class="dekker" href="werk.html?w=' + x.id + '"><span class="wie">' + MAKERS[x.m] + '</span><br><span class="wat">' + esc(x.n) + "</span>, " + x.j + "</a>" +
      '<div class="mat">' + esc(x.mat) + "<br>" + maat(x) + '</div><div class="prijs"><span>' + prijsKort(x.p) + "</span></div></div>" +
      '<button class="koop" type="button" data-koop="' + x.id + '"' + (bezet ? " disabled>In je winkelmand" : ">In winkelmand") + "</button></article>";
  }

  function schaal(x, groot) {
    var max = x.c === "wand" ? 130 : 110, hv = Math.min(x.h / max * 84, 84), bv = Math.min(x.b / max * 84, 84);
    return '<div class="schaal' + (groot ? " groot" : "") + '" style="--kleur:' + x.kleur + '"><span class="maatlabel">' + (x.c === "wand" ? x.b + " × " + x.h + " cm" : "H " + String(x.h).replace(".", ",") + " cm") + '</span>' +
      '<span class="ref" style="height:' + (30 / max * 84) + '%;width:' + (21 / max * 84) + '%" title="A4, 30 cm"></span>' +
      '<span class="vorm ' + (x.c === "wand" ? "paneel" : "beeld") + '" style="height:' + hv + '%;width:' + bv + '%"></span></div>';
  }
  function huisKaart(x) {
    return '<article class="ding">' + schaal(x) + '<div class="bordje"><span class="wie">' + x.merk + '</span><br><span class="wat">' + esc(x.n) + '</span>' +
      '<div class="mat">' + esc(x.mat) + "<br>" + x.d + '</div><div class="prijs"><span>' + prijsMooi(x.p) + '</span><a class="concept-bron" href="' + (x.maker || x.bron) + '" target="_blank" rel="noopener">Bron</a></div></div>' +
      '<button class="koop" type="button" data-koop="' + x.id + '">In winkelmand</button></article>';
  }

  /* klikken */
  document.addEventListener("click", function (e) {
    var k = e.target.closest("[data-koop]"); if (k) { e.preventDefault(); voegToe(k.getAttribute("data-koop")); return; }
    var f = e.target.closest("[data-fav]"); if (f) { e.preventDefault(); wisselFav(f.getAttribute("data-fav")); return; }
    var o = e.target.closest("[data-open]"); if (o) { e.preventDefault(); openPaneel(o.getAttribute("data-open")); return; }
    if (e.target.closest("[data-sluit]")) { e.preventDefault(); sluitPanelen(); return; }
    if (e.target.closest(".paneel a")) sluitPanelen();
  });
  document.addEventListener("keydown", function (e) { if (e.key === "Escape") sluitPanelen(); });
  var laatsteFocus;
  function openPaneel(naam) {
    var el = document.getElementById(naam); if (!el) return;
    laatsteFocus = document.activeElement; el.classList.add("open"); document.body.style.overflow = "hidden";
    var veld = el.querySelector("input") || el.querySelector("button,a"); if (veld) setTimeout(function () { veld.focus(); }, 30);
  }
  function sluitPanelen() {
    var open = $$(".lade.open,.zoek.open"); if (!open.length) return;
    open.forEach(function (el) { el.classList.remove("open"); });
    document.body.style.overflow = ""; if (laatsteFocus) laatsteFocus.focus();
  }

  /* zoeken */
  var zv = $("#zoekveld");
  if (zv) zv.addEventListener("input", function () {
    var q = this.value.trim().toLowerCase(), res = $("#zoekres"), leeg = $("#zoekleeg");
    if (q.length < 2) { res.innerHTML = ""; leeg.textContent = "Probeer bijvoorbeeld brons, wit, Vaerman of keramiek."; return; }
    var hits = W.filter(function (x) { return (x.n + " " + MAKERS[x.m] + " " + x.mat + " " + CATS[x.c] + " " + x.t).toLowerCase().indexOf(q) > -1; });
    res.innerHTML = hits.slice(0, 8).map(kaart).join("");
    leeg.textContent = hits.length ? hits.length + (hits.length === 1 ? " werk gevonden" : " werken gevonden") : "Geen werken gevonden voor “" + this.value + "”.";
  });

  /* formulieren met bevestiging */
  $$("form[data-bevestig]").forEach(function (f) {
    f.addEventListener("submit", function (e) {
      e.preventDefault();
      var leegVeld = $$("[required]", f).filter(function (i) { return !i.value.trim() || (i.type === "email" && !i.checkValidity()); })[0];
      var oud = f.querySelector(".bevestig"); if (oud) oud.remove();
      var p = document.createElement("p"); p.className = "bevestig"; p.setAttribute("role", "status");
      if (leegVeld) { p.textContent = "Vul de verplichte velden in (met *)."; leegVeld.focus(); }
      else { p.textContent = f.getAttribute("data-bevestig"); f.reset(); }
      f.appendChild(p);
    });
  });
  $$("[role=tab]").forEach(function (t) {
    t.addEventListener("click", function () {
      $$("[role=tab]", t.parentNode).forEach(function (x) { x.setAttribute("aria-selected", x === t); document.getElementById(x.getAttribute("aria-controls")).hidden = x !== t; });
    });
  });

  var pag = document.body.dataset.pagina, url = new URLSearchParams(location.search);

  if (pag === "home") {
    $("#strook").innerHTML = ["beweging", "danser", "wit-ii", "rustende-beer", "zomer-in-rood", "nacht", "koraalschaal", "relief-i"].map(function (id) {
      var x = vind(id);
      return '<a class="strook-item' + (x.wand ? "" : " object") + '" href="werk.html?w=' + x.id + '"><div class="lijst"><img src="img/' + x.img + '.jpg" alt="' + esc(x.n + " van " + MAKERS[x.m]) + '" loading="lazy" width="1400" height="1750"></div><p><b>' + esc(x.n) + "</b>" + MAKERS[x.m] + " · " + prijsKort(x.p) + "</p></a>";
    }).join("");
    (function () {
      var n = $("#nacht"); if (!n) return;
      var stil = window.matchMedia && matchMedia("(prefers-reduced-motion: reduce)").matches, laatst = -1e9, t0 = performance.now(), zicht = true;
      var zet = function (x, y) { n.style.setProperty("--x", x + "%"); n.style.setProperty("--y", y + "%"); };
      n.addEventListener("pointermove", function (e) { var r = n.getBoundingClientRect(); laatst = performance.now(); zet((e.clientX - r.left) / r.width * 100, (e.clientY - r.top) / r.height * 100); n.classList.add("actief"); });
      if ("IntersectionObserver" in window) new IntersectionObserver(function (es) { zicht = es[0].isIntersecting; }).observe(n);
      if (stil) { zet(66, 42); return; }
      (function stap(t) {
        if (zicht && t - laatst > 2500) { var s2 = (t - t0) / 1000; zet(62 + Math.sin(s2 * 0.45) * 24, 42 + Math.sin(s2 * 0.8 + 1) * 20); }
        requestAnimationFrame(stap);
      })(t0);
    })();
    $("#nieuw-grid").innerHTML = ["relief-i", "danser", "zomer-in-rood", "rustende-beer"].map(function (id) { return kaart(vind(id)); }).join("");
    $("#advies-grid").innerHTML = ["terra", "kalk", "koraalschaal", "nacht"].map(function (id) { return kaart(vind(id)); }).join("");
  }

  /* collectie */
  if (pag === "collectie") {
    var cat = CATS[url.get("cat")] ? url.get("cat") : "", band = +(url.get("prijs") || 0), maker = MAKERS[url.get("maker")] ? url.get("maker") : "", sort = "standaard";
    if (band < 0 || band > 3) band = 0;
    $("#chips").innerHTML = '<button class="chip" type="button" data-cat="" aria-pressed="' + !cat + '">Alle werken</button>' +
      Object.keys(CATS).map(function (k) { return '<button class="chip" type="button" data-cat="' + k + '" aria-pressed="' + (cat === k) + '">' + CATS[k] + "</button>"; }).join("");
    $("#makerfilter").innerHTML = '<option value="">Alle kunstenaars</option>' + Object.keys(MAKERS).map(function (k) { return '<option value="' + k + '">' + MAKERS[k] + "</option>"; }).join("");
    $("#prijsfilter").value = String(band); $("#makerfilter").value = maker;
    var inBand = function (x) { return !band || (band === 1 && x.p < 350) || (band === 2 && x.p >= 350 && x.p < 1500) || (band === 3 && x.p >= 1500); };
    var opp = function (x) { if (x.wand) return x.w * x.h; var n = (x.d.match(/\d+/g) || [0]).map(Number); return n[0] * (n[1] || n[0]); };
    var teken = function () {
      var lijst = W.filter(function (x) { return (!cat || x.c === cat) && inBand(x) && (!maker || x.m === maker); });
      if (sort === "laag") lijst.sort(function (a, b) { return a.p - b.p; });
      if (sort === "hoog") lijst.sort(function (a, b) { return b.p - a.p; });
      if (sort === "groot") lijst.sort(function (a, b) { return opp(b) - opp(a); });
      $("#col-grid").innerHTML = lijst.map(kaart).join("");
      $("#col-leeg").hidden = lijst.length > 0;
      $("#aantal").textContent = lijst.length + (lijst.length === 1 ? " werk" : " werken");
      var titel = maker ? MAKERS[maker] : cat ? CATS[cat] : "Alle werken";
      $("#col-titel").textContent = titel; $("#kruimel-cat").textContent = titel;
      $("#col-tekst").textContent = cat ? CAT_TEKST[cat] : "Schilderijen, beelden en vondsten. Filter op wereld, prijs of kunstenaar.";
      document.title = titel + " | Atelier Ombre (concept)";
      var q = []; if (cat) q.push("cat=" + cat); if (band) q.push("prijs=" + band); if (maker) q.push("maker=" + maker);
      try { history.replaceState(null, "", "collectie.html" + (q.length ? "?" + q.join("&") : "")); } catch (e) {}
    };
    teken();
    $("#chips").addEventListener("click", function (e) {
      var b = e.target.closest("[data-cat]"); if (!b) return;
      cat = b.getAttribute("data-cat");
      $$("#chips .chip").forEach(function (x) { x.setAttribute("aria-pressed", x === b); });
      teken();
    });
    $("#prijsfilter").addEventListener("change", function () { band = +this.value; teken(); });
    $("#makerfilter").addEventListener("change", function () { maker = this.value; teken(); });
    $("#sorteer").addEventListener("change", function () { sort = this.value; teken(); });
    $("#wis").addEventListener("click", function () {
      cat = ""; band = 0; maker = ""; $("#prijsfilter").value = "0"; $("#makerfilter").value = "";
      $$("#chips .chip").forEach(function (x) { x.setAttribute("aria-pressed", x.getAttribute("data-cat") === ""); }); teken();
    });
  }

  /* werkpagina */
  function plaatsAanMuur(x, img) {
    var bw = x.w * MUUR.cm, bh = x.h * MUUR.cm;
    img.style.width = (bw / MUUR.b * 100) + "%";
    img.style.height = (bh / MUUR.h * 100) + "%";
    img.style.left = ((MUUR.midden - bw / 2) / MUUR.b * 100) + "%";
    img.style.top = ((MUUR.onder - bh) / MUUR.h * 100) + "%";
    img.style.objectFit = "cover";
  }
  if (pag === "werk") {
    var x = vind(url.get("w")) || W[0], gereserveerd = lees("reserv", []).indexOf(x.id) > -1, bezet = uniek(x) && inMand(x.id);
    document.title = x.n + " – " + MAKERS[x.m] + " | Atelier Ombre (concept)";
    $("#kruimel-werk").textContent = x.n;
    var podium = x.wand ?
      '<div class="podium" id="podium"><img src="img/' + x.img + '.jpg" alt="' + esc(x.n + " van " + MAKERS[x.m]) + '" width="1400" height="1750"></div>' +
      '<div class="kamer" id="kamer" hidden><img class="aan-muur" id="muurwerk" src="img/' + x.img + '.jpg" alt="' + esc(x.n) + ' op ware grootte boven een bank"><span class="maat">Werk ' + x.w + " × " + x.h + " cm · bank 184 cm breed</span></div>" +
      '<div class="weergave" role="group" aria-label="Weergave"><button type="button" data-weergave="werk" aria-pressed="true">Het werk</button><button type="button" data-weergave="muur" aria-pressed="false">Aan de muur, op ware grootte</button></div>' +
      '<div class="lijsten" id="lijsten" hidden><span class="klein">Lijst:</span><button class="chip" type="button" data-lijst="" aria-pressed="true">Zonder</button><button class="chip" type="button" data-lijst="lijst-zwart" aria-pressed="false">Zwart</button><button class="chip" type="button" data-lijst="lijst-eik" aria-pressed="false">Eiken</button></div>'
      : '<div class="podium object"><img src="img/' + x.img + '.jpg" alt="' + esc(x.n + ", " + x.mat.toLowerCase()) + '" width="1400" height="1750"></div>';
    $("#detail").innerHTML = "<div>" + podium + "</div>" +
      '<div class="info"><p class="wie"><a href="' + (x.m === "onbekend" ? "collectie.html?cat=vondsten" : "kunstenaars.html#" + x.m) + '">' + MAKERS[x.m] + "</a></p><h1>" + esc(x.n) + "</h1>" +
      '<dl class="feiten"><dt>Jaar</dt><dd>' + x.j + "</dd><dt>Techniek</dt><dd>" + esc(x.mat) + "</dd><dt>Afmetingen</dt><dd>" + maat(x) + "</dd><dt>Editie</dt><dd>" + x.l + "</dd><dt>Certificaat</dt><dd>" + (x.c === "vondsten" ? "Beschrijving van herkomst en staat" : "Gesigneerd door de kunstenaar") + "</dd></dl>" +
      '<p class="grootprijs">' + euro(x.p) + '</p><p class="klein">Inclusief btw' + (x.p >= GRATIS ? ", verzekerde verzending gratis" : "") + (x.p >= 1000 ? ". Of 3 × " + euro(x.p / 3) + " zonder rente" : "") + ".</p>" +
      '<div class="acties"><button class="knop" type="button" data-koop="' + x.id + '"' + (bezet ? " disabled>In je winkelmand" : ">In winkelmand") + '</button><button class="ico" type="button" data-fav="' + x.id + '" aria-pressed="' + (favs().indexOf(x.id) > -1) + '" aria-label="Bewaar als favoriet">' + HART + "</button></div>" +
      (uniek(x) ? '<button class="knop licht breed" type="button" id="reserveer"' + (gereserveerd ? " disabled>Gereserveerd tot overmorgen" : ">48 uur gratis reserveren") + "</button>" : "") +
      '<ul class="zekerheden"><li>Certificaat van echtheid</li><li>' + (x.p >= GRATIS ? "Gratis verzekerd verzonden" : "Verzekerd verzonden voor € 14,95") + (x.lv >= 80 ? ", met kunstkoerier op afspraak" : ", 3–5 werkdagen") + "</li><li>14 dagen bedenktijd</li></ul>" +
      '<details open><summary>Over dit werk</summary><p>' + esc(x.t) + "</p></details>" +
      "<details><summary>Verzending en ophangen</summary><p>" + (x.wand ? "Geleverd met ophangsysteem. Tip: hang het midden van het werk op ooghoogte, ongeveer 150 cm vanaf de vloer, of 20 tot 25 cm boven een bank." : "Geleverd in museumverpakking met zuurvrij papier. Zet beelden op een stabiele, vlakke ondergrond buiten direct zonlicht.") + "</p></details>" +
      '<details><summary>Vraag over dit werk?</summary><p>We sturen graag extra foto\'s of een detailopname. <a class="link" href="service.html#contact">Stel je vraag</a>.</p></details></div>';
    if (x.wand) {
      plaatsAanMuur(x, $("#muurwerk"));
      $$("[data-weergave]").forEach(function (b) {
        b.addEventListener("click", function () {
          var muur = b.getAttribute("data-weergave") === "muur";
          $$("[data-weergave]").forEach(function (y) { y.setAttribute("aria-pressed", y === b); });
          $("#podium").hidden = muur; $("#kamer").hidden = !muur; $("#lijsten").hidden = !muur;
        });
      });
      $("#lijsten").addEventListener("click", function (e) {
        var b = e.target.closest("[data-lijst]"); if (!b) return;
        $$("#lijsten .chip").forEach(function (y) { y.setAttribute("aria-pressed", y === b); });
        $("#muurwerk").className = "aan-muur " + b.getAttribute("data-lijst");
      });
    }
    var rk = $("#reserveer");
    if (rk) rk.addEventListener("click", function () {
      var r = lees("reserv", []); if (r.indexOf(x.id) < 0) r.push(x.id); bewaar("reserv", r);
      rk.disabled = true; rk.textContent = "Gereserveerd tot overmorgen";
      toast("<i>" + esc(x.n) + "</i> is 48 uur voor je gereserveerd (concept)");
    });
    var verwant = W.filter(function (y) { return y.id !== x.id && (y.m === x.m || y.c === x.c); }).concat(W.filter(function (y) { return y.c !== x.c; }));
    var gezien = {}; verwant = verwant.filter(function (y) { if (gezien[y.id] || y.id === x.id) return false; gezien[y.id] = 1; return true; }).slice(0, 4);
    $("#gerelateerd").innerHTML = verwant.map(kaart).join("");
  }

  /* huis & beeld */
  if (pag === "huis") {
    var hcat = "", hsort = "standaard";
    var hteken = function () {
      var l = H.filter(function (x) { return !hcat || x.c === hcat; });
      if (hsort === "laag") l.sort(function (a, b) { return a.p - b.p; });
      if (hsort === "hoog") l.sort(function (a, b) { return b.p - a.p; });
      if (hsort === "groot") l.sort(function (a, b) { return b.h * b.b - a.h * a.b; });
      $("#h-grid").innerHTML = l.map(huisKaart).join("");
      $("#h-aantal").textContent = l.length + " producten";
    };
    hteken();
    $("#h-chips").addEventListener("click", function (e) {
      var b = e.target.closest("[data-hcat]"); if (!b) return; hcat = b.getAttribute("data-hcat");
      $$("#h-chips .chip").forEach(function (y) { y.setAttribute("aria-pressed", y === b); }); hteken();
    });
    $("#h-sorteer").addEventListener("change", function () { hsort = this.value; hteken(); });
  }

  /* kunstenaars */
  if (pag === "kunstenaars") {
    $$("[data-telling]").forEach(function (p) {
      var n = W.filter(function (x) { return x.m === p.getAttribute("data-telling"); }).length;
      p.textContent = n + (n === 1 ? " werk in de collectie" : " werken in de collectie");
    });
  }

  /* winkelmand */
  function verzending(sub) { return sub === 0 || sub >= GRATIS ? 0 : VERZEND; }
  function toonMand() {
    var m = mand(), doel = $("#mand-regels"), sub = subtotaal(), v = verzending(sub);
    if (!m.length) {
      doel.innerHTML = '<p class="leeg" style="padding:20px 0">Je winkelmand is leeg.</p><a class="knop" href="collectie.html">Bekijk de collectie</a>';
    } else {
      doel.innerHTML = m.map(function (r) {
        var x = vind(r.id); if (!x) return "";
        if (x.huis) return '<div class="regel"><div class="mini mini-huis" style="--kleur:' + x.kleur + '"><span></span></div><div><h3>' + esc(x.n) + '</h3><p class="klein">' + x.merk + " · " + x.d + '</p><p class="klein">Aantal: <button class="weg" type="button" data-mstap="-1" data-id="' + x.id + '" aria-label="Eén minder">−</button> ' + r.a + ' <button class="weg" type="button" data-mstap="1" data-id="' + x.id + '" aria-label="Eén meer">+</button></p><button class="weg" type="button" data-weg="' + x.id + '">Verwijderen</button></div><span class="rprijs">' + euro(x.p * r.a) + "</span></div>";
        return '<div class="regel"><a class="mini" href="werk.html?w=' + x.id + '"><img src="img/' + x.img + '.jpg" alt=""></a><div><h3>' + esc(x.n) + '</h3><p class="klein">' + MAKERS[x.m] + " · " + maat(x) + " · " + x.l + "</p>" +
          (uniek(x) ? "" : '<p class="klein">Aantal: <button class="weg" type="button" data-mstap="-1" data-id="' + x.id + '" aria-label="Eén minder">−</button> ' + r.a + ' <button class="weg" type="button" data-mstap="1" data-id="' + x.id + '" aria-label="Eén meer">+</button></p>') +
          '<button class="weg" type="button" data-weg="' + x.id + '">Verwijderen</button></div><span class="rprijs">' + euro(x.p * r.a) + "</span></div>";
      }).join("");
    }
    $("#sub").textContent = euro(sub); $("#verz").textContent = v ? euro(v) : "Gratis";
    $("#tot").textContent = euro(sub + v); $("#termijn").hidden = sub + v < 1000;
    var knop = $("#mand .knop.breed"); if (knop) knop.style.display = m.length ? "" : "none";
  }
  if (pag === "mand") {
    toonMand();
    $("#mand").addEventListener("click", function (e) {
      var m = mand(), s = e.target.closest("[data-mstap]"), w = e.target.closest("[data-weg]");
      if (s) { m.forEach(function (r) { if (r.id === s.getAttribute("data-id")) r.a = Math.max(1, Math.min(5, r.a + (+s.getAttribute("data-mstap")))); }); zetMand(m); toonMand(); }
      if (w) { zetMand(m.filter(function (r) { return r.id !== w.getAttribute("data-weg"); })); toonMand(); }
    });
  }
  if (pag === "afrekenen") {
    var m2 = mand(), sub2 = subtotaal(), v2 = verzending(sub2);
    $("#overzicht").innerHTML = m2.length ? m2.map(function (r) { var x = vind(r.id); return x ? '<div class="rij"><span>' + (r.a > 1 ? r.a + " × " : "") + "<i>" + esc(x.n) + "</i></span><span>" + euro(x.p * r.a) + "</span></div>" : ""; }).join("") +
      '<div class="rij"><span>Verzekerde verzending</span><span>' + (v2 ? euro(v2) : "Gratis") + '</span></div><div class="rij totaal"><span>Totaal</span><span>' + euro(sub2 + v2) + "</span></div>"
      : '<p class="leeg">Je winkelmand is leeg.</p><a class="link" href="collectie.html">Naar de collectie</a>';
    $("#bestel").addEventListener("submit", function (e) {
      e.preventDefault();
      var f = this, fout = $$("[required]", f).filter(function (i) { return i.type === "checkbox" ? !i.checked : (!i.value.trim() || !i.checkValidity()); })[0];
      if (!mand().length) { $("#fout").textContent = "Je winkelmand is leeg. Kies eerst een werk."; return; }
      if (fout) { $("#fout").textContent = "Vul de verplichte velden in (met *)."; fout.focus(); return; }
      var nr = "AO-" + (1000 + Math.floor(Math.random() * 9000));
      zetMand([]);
      $("#afreken").innerHTML = '<div class="tekst" style="padding:0"><div class="stappen"><span>1. Gegevens</span><span>2. Betalen</span><b>3. Bevestiging</b></div><h2>Dank je wel voor je bestelling</h2><p>Je bestelnummer is <b>' + nr + "</b>. Het atelier pakt je werk zorgvuldig in; je ontvangt de track-and-trace en het certificaat per e-mail.</p><p class=\"klein\">Concept: er is niets echt besteld of betaald.</p><a class=\"knop\" href=\"collectie.html\">Verder kijken</a></div>";
      window.scrollTo(0, 0);
    });
  }

  /* favorieten */
  function toonFavorieten() {
    var lijst = favs().map(vind).filter(Boolean);
    $("#fav-leeg").hidden = lijst.length > 0;
    $("#fav-grid").innerHTML = lijst.map(kaart).join("");
  }
  if (pag === "favorieten") toonFavorieten();

  /* beheer */
  if (pag === "beheer") {
    var MODEL = { c: "Consignatie", p: "Print op bestelling", i: "Eigen inkoop" };
    var prijzen = {};
    W.forEach(function (x) { prijzen[x.id] = x.p; });
    var kosten = function (x, p) { return x.model === "c" ? p * (1 - COMMISSIE) : x.kost; };
    var reken = function () {
      var tot = 0, waarde = 0, risico = 0;
      W.forEach(function (x) {
        var p = prijzen[x.id], k = kosten(x, p), op = p - k - x.lv - BETAAL, mg = p ? op / p : 0;
        tot += mg; waarde += p; if (x.model === "i") risico += x.kost;
        var rij = $('[data-rij="' + x.id + '"]');
        rij.querySelector(".k").textContent = euro(k) + (x.model === "c" ? " (60 % naar kunstenaar)" : "");
        rij.querySelector(".op").textContent = euro(op); rij.querySelector(".op").className = "op " + (op >= 0 ? "pos" : "neg");
        rij.querySelector(".mg").textContent = Math.round(mg * 100) + " %";
      });
      $("#k-werken").textContent = W.length; $("#k-waarde").textContent = prijsKort(Math.round(waarde));
      $("#k-marge").textContent = Math.round(tot / W.length * 100) + " %"; $("#k-risico").textContent = prijsKort(Math.round(risico));
    };
    $("#marge-tabel tbody").innerHTML = W.map(function (x) {
      return '<tr data-rij="' + x.id + '"><td><i>' + esc(x.n) + "</i><br><span class=\"klein\">" + MAKERS[x.m] + '</span></td><td><span class="model">' + MODEL[x.model] + '</span></td><td class="k"></td><td>' + euro(x.lv) +
        '</td><td><label class="sr" for="p-' + x.id + '">Verkoopprijs ' + esc(x.n) + '</label><input id="p-' + x.id + '" type="number" min="0" step="5" value="' + x.p + '"></td><td class="op"></td><td class="mg"></td></tr>';
    }).join("");
    $("#marge-tabel").addEventListener("input", function (e) {
      if (e.target.id && e.target.id.indexOf("p-") === 0) { prijzen[e.target.id.slice(2)] = Math.max(0, +e.target.value || 0); reken(); }
    });
    reken();
    $("#huis-tabel tbody").innerHTML = H.map(function (x) {
      return "<tr><td>" + esc(x.n) + '<br><span class="klein">' + x.d + "</span></td><td>" + x.merk + '</td><td><a class="link" href="' + x.bron + '" target="_blank" rel="noopener">' + esc(x.ref) + "</a></td><td>" + prijsMooi(x.p) + "</td><td>" + ROUTE[x.r] + "</td><td>" + (x.maker ? '<a class="link" href="' + x.maker + '" target="_blank" rel="noopener">Productpagina</a>' : '<span class="klein">via bron</span>') + "</td></tr>";
    }).join("");
    var STAP = ["Betaald", "Doorgestuurd", "Onderweg", "Geleverd"];
    var orders = [["AO-2481", "rustende-beer", 4, "Eigen voorraad, verzonden met PostNL verzekerd"], ["AO-2479", "terra", 3, "Drukker print en verzendt rechtstreeks"], ["AO-2476", "wit-ii", 2, "Kunstkoerier haalt op bij het atelier van Ines Vaerman"], ["AO-2475", "danser", 1, "Atelier Ruys ontvangt de bestelling"]];
    $("#orders").innerHTML = orders.map(function (o) {
      var x = vind(o[1]);
      return '<div class="order"><b>' + o[0] + "</b><div><i>" + esc(x.n) + "</i> · " + euro(x.p) + '<br><span class="klein">' + o[3] + '</span></div><div><div class="status" aria-label="Status: ' + STAP[o[2] - 1] + '">' + STAP.map(function (s, i) { return '<i class="' + (i < o[2] ? "ja" : "") + '"></i>'; }).join("") + '</div><span class="klein">' + STAP[o[2] - 1] + "</span></div></div>";
    }).join("");
  }

  tellers();
})();
