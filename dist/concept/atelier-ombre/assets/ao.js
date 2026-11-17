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

  /* Huis & Beeld: echte producten van ontwerpmerken. p = verkoopprijs */
  var H = [
    { id: "ptmd-vrouw", n: "Beeld Vrouw, zwart", merk: "PTMD", c: "beelden", p: 69, b: 25, h: 90, d: "H 90 × B 25 × D 27 cm", mat: "Cement, diepzwart", kleur: "#2A2A2C", r: "p" },
    { id: "pt-imagine", n: "Figuur Imagine, zwart", merk: "Present Time", c: "beelden", p: 24.95, b: 12.5, h: 23.5, d: "H 23,5 × B 12,5 cm", mat: "Polyresin", kleur: "#26272A", r: "g" },
    { id: "ptmd-darina", n: "Wandpaneel Darina, grote golf brons", merk: "PTMD", c: "wand", p: 159, b: 120, h: 120, d: "120 × 120 cm", mat: "Wandpaneel met golfmotief, bronskleur", kleur: "#8C6A45", r: "p" },
    { id: "ptmd-salima", n: "Wandpaneel Salima, gesneden bloem", merk: "PTMD", c: "wand", p: 135, b: 90, h: 90, d: "90 × 90 cm", mat: "Wandpaneel, gesneden bloemmotief", kleur: "#CFC6B6", r: "p" },
    { id: "canvas-warme-tinten", n: "Canvas Abstracte vormen, warme tinten", merk: "De Wanddecoratie", c: "wand", p: 84.95, b: 80, h: 120, d: "80 × 120 cm", mat: "Canvas op frame van FSC/PEFC-hout, 1,8 cm", kleur: "#C98E5E", r: "w" }
  ];
  var TINT = {"ptmd-vrouw": "zwart", "pt-imagine": "zwart", "ptmd-darina": "messing", "ptmd-salima": "naturel", "canvas-warme-tinten": "aarde"};
  var MERKSLUG = { "PTMD": "ptmd", "Present Time": "present-time", "De Wanddecoratie": "de-wanddecoratie" };
  H.forEach(function (x) { x.huis = 1; x.ms = MERKSLUG[x.merk]; x.tint = TINT[x.id]; });
  var ROUTE = { p: "Droppery (dropshipping)", g: "Groothandel, navragen", w: "Rechtstreeks, navragen" };
  var API = "https://eyrfizayagcwaxbxyeuh.supabase.co/functions/v1/ombre-order";
  function api(data) {
    return fetch(API, { method: "POST", headers: { "Content-Type": "application/json" }, body: JSON.stringify(data) })
      .then(function (r) { return r.json().catch(function () { return {}; }).then(function (j) { if (!r.ok) { var e = new Error(j.fout || "Er ging iets mis. Probeer het opnieuw."); e.code = r.status; throw e; } return j; }); },
        function () { throw new Error("Geen verbinding. Controleer je internet en probeer het opnieuw."); });
  }
  var DATUM = function (t) { try { return new Date(t).toLocaleString("nl-NL", { day: "numeric", month: "long", hour: "2-digit", minute: "2-digit" }); } catch (e) { return ""; } };
  var VOLG = ["betaald", "besteld", "verzonden", "geleverd"];
  var VOLGNAAM = { betaald: "Betaald", besteld: "Besteld bij de maker", verzonden: "Verzonden", geleverd: "Geleverd", geannuleerd: "Geannuleerd" };
  var GRATIS = 250, VERZEND = 14.95, BETAAL = 0.29, COMMISSIE = 0.4;
  var MUUR = { b: 2000, h: 2933, cm: 2000 / 184, onder: 1660, midden: 1100 }; /* bank op de foto is ca. 184 cm breed */
  var mb = function (b) { return 'src="img/' + b + '-m.jpg" srcset="img/' + b + '-m.jpg 1080w, img/' + b + '.jpg 1800w" sizes="(max-width:700px) 50vw, 25vw"'; };
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
      '<div class="wand' + (x.wand ? "" : " object") + '"><img ' + mb(x.img) + ' alt="' + esc(x.n + ", " + x.mat.toLowerCase()) + '" loading="lazy" width="1400" height="1750"></div>' +
      '<div class="bordje"><a class="dekker" href="werk.html?w=' + x.id + '"><span class="wie">' + MAKERS[x.m] + '</span><br><span class="wat">' + esc(x.n) + "</span>, " + x.j + "</a>" +
      '<div class="mat">' + esc(x.mat) + "<br>" + maat(x) + '</div><div class="prijs"><span>' + prijsKort(x.p) + "</span></div></div>" +
      '<button class="koop" type="button" data-koop="' + x.id + '"' + (bezet ? " disabled>In je winkelmand" : ">In winkelmand") + "</button></article>";
  }

  function schaal(x, groot) {
    var wand = x.c === "wand", max = wand ? 130 : 110, f = wand ? 62 : 84, hv = Math.min(x.h / max * f, f), bv = Math.min(x.b / max * f, f);
    return '<div class="schaal' + (groot ? " groot" : "") + (wand ? " is-wand" : "") + '" style="--kleur:' + x.kleur + '"><span class="maatlabel">' + (x.c === "wand" ? x.b + " × " + x.h + " cm" : "H " + String(x.h).replace(".", ",") + " cm") + '</span>' +
      '<span class="ref" style="height:' + (30 / max * f) + '%;width:' + (21 / max * f) + '%" title="A4, 30 cm"></span>' +
      '<span class="vorm ' + (x.c === "wand" ? "paneel" : "beeld") + '" style="height:' + hv + '%;width:' + bv + '%"></span></div>';
  }
  function huisKaart(x) {
    return '<article class="ding">' + schaal(x) + '<div class="bordje"><span class="wie">' + x.merk + '</span><br><span class="wat">' + esc(x.n) + '</span>' +
      '<div class="mat">' + esc(x.mat) + "<br>" + x.d + '</div><div class="prijs"><span>' + prijsMooi(x.p) + '</span></div></div>' +
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

  (function () { var k = $(".kopbalk"); if (!k) return; var t = function () { k.classList.toggle("gescrold", scrollY > 8); }; addEventListener("scroll", t, { passive: true }); t(); })();

  var pag = document.body.dataset.pagina, url = new URLSearchParams(location.search);

  if (pag === "home") {
    $("#strook").innerHTML = ["beweging", "danser", "wit-ii", "rustende-beer", "zomer-in-rood", "nacht", "koraalschaal", "relief-i"].map(function (id) {
      var x = vind(id);
      return '<a class="strook-item' + (x.wand ? "" : " object") + '" href="werk.html?w=' + x.id + '"><div class="lijst"><img ' + mb(x.img) + ' alt="' + esc(x.n + " van " + MAKERS[x.m]) + '" loading="lazy" width="1400" height="1750"></div><p><b>' + esc(x.n) + "</b>" + MAKERS[x.m] + " · " + prijsKort(x.p) + "</p></a>";
    }).join("");
    (function () {
      var n = $("#nacht"); if (!n) return;
      var stil = window.matchMedia && matchMedia("(prefers-reduced-motion: reduce)").matches;
      var aanraak = window.matchMedia && matchMedia("(hover: none)").matches;
      var tx = 62, ty = 42, cx = 62, cy = 42, laatst = -1e9, zicht = true, tour = 0, tourT = 0;
      var zet = function (x, y) { n.style.setProperty("--x", x.toFixed(2) + "%"); n.style.setProperty("--y", y.toFixed(2) + "%"); };
      var naar = function (e) { var r = n.getBoundingClientRect(); tx = (e.clientX - r.left) / r.width * 100; ty = (e.clientY - r.top) / r.height * 100; laatst = performance.now(); n.classList.add("actief"); };
      var punten = function () {
        var r = n.getBoundingClientRect();
        return $$(".nw", n).map(function (w) { var b = w.getBoundingClientRect(); return [(b.left + b.width / 2 - r.left) / r.width * 100, (b.top + b.height / 2 - r.top) / r.height * 100]; })
          .filter(function (p) { return p[0] > 0 && p[0] < 100 && p[1] > 0 && p[1] < 100; });
      };
      n.addEventListener("pointermove", function (e) { if (e.pointerType === "mouse" || e.pointerType === "pen") naar(e); });
      n.addEventListener("pointerdown", function (e) { if (e.pointerType !== "mouse" && !e.target.closest("a,button")) naar(e); });
      if ("IntersectionObserver" in window) new IntersectionObserver(function (es) { zicht = es[0].isIntersecting; }).observe(n);
      if (stil) { var p0 = punten()[0] || [62, 42]; zet(p0[0], p0[1]); return; }
      zet(cx, cy);
      (function stap(t) {
        if (zicht) {
          if (t - laatst > (aanraak ? 4500 : 2600)) {
            var ps = punten();
            if (ps.length) { if (t - tourT > 2300) { tour = (tour + 1) % ps.length; tourT = t; } tx = ps[tour][0]; ty = ps[tour][1]; }
          }
          var k = t - laatst < 400 ? 0.16 : 0.045;
          cx += (tx - cx) * k; cy += (ty - cy) * k; zet(cx, cy);
        }
        requestAnimationFrame(stap);
      })(performance.now());
    })();
    $("#nieuw-grid").innerHTML = ["relief-i", "danser", "zomer-in-rood", "rustende-beer"].map(function (id) { return kaart(vind(id)); }).join("");
    $("#advies-grid").innerHTML = ["terra", "kalk", "koraalschaal", "nacht"].map(function (id) { return kaart(vind(id)); }).join("");
  }


  /* ===== overzichten met filters (Galerie, Huis & Beeld, subpagina's) ===== */
  var getal = function (t) { return (String(t).match(/\d+([.,]\d+)?/g) || ["0"]).map(function (v) { return parseFloat(v.replace(",", ".")); }); };
  var maatVan = function (x) { return x.huis ? Math.max(x.b, x.h) : x.wand ? Math.max(x.w, x.h) : Math.max.apply(null, getal(x.d)); };
  var techVan = function (x) {
    var m = x.mat.toLowerCase();
    if (/olieverf/.test(m)) return "olie"; if (/giclée|print/.test(m)) return "print"; if (/acryl/.test(m)) return "acryl";
    if (/gips|kalk|structuur|marmerpoeder/.test(m)) return "relief"; if (/brons/.test(m)) return "brons";
    if (/porselein|keramiek|steengoed/.test(m)) return "keramiek"; if (/steen|travertin/.test(m)) return "steen"; return "overig";
  };
  var FMT = { klein: "Klein (tot 40 cm)", middel: "Middel (40–90 cm)", groot: "Groot (vanaf 90 cm)" };
  var fmtVan = function (x) { var m = maatVan(x); return m < 40 ? "klein" : m < 90 ? "middel" : "groot"; };
  var MERKNAAM = {}; Object.keys(MERKSLUG).forEach(function (k) { MERKNAAM[MERKSLUG[k]] = k; });
  var MAKERSEL = {}; Object.keys(MAKERS).forEach(function (k) { if (k !== "onbekend") MAKERSEL[k] = MAKERS[k]; });
  var CONF = {
    W: { items: W, kaart: kaart, filters: [
      { k: "c", naam: "Wereld", chips: true, opts: CATS, v: function (x) { return x.c; } },
      { k: "m", naam: "Kunstenaar", opts: MAKERSEL, v: function (x) { return x.m; } },
      { k: "tech", naam: "Techniek", opts: { acryl: "Acryl", olie: "Olieverf", relief: "Reliëf, gips en kalk", print: "Print op papier", brons: "Brons", keramiek: "Keramiek en porselein", steen: "Steen" }, v: techVan },
      { k: "ed", naam: "Editie", opts: { Unicum: "Unicum", Oplage: "Oplage", Vondst: "Vondst" }, v: function (x) { return /^Oplage/.test(x.l) ? "Oplage" : x.l; } },
      { k: "fmt", naam: "Formaat", opts: FMT, v: fmtVan },
      { k: "prijs", naam: "Prijs", opts: { "1": "Tot € 350", "2": "€ 350 – 1.500", "3": "Vanaf € 1.500" }, v: function (x) { return x.p < 350 ? "1" : x.p < 1500 ? "2" : "3"; } }] },
    H: { items: H, kaart: huisKaart, filters: [
      { k: "c", naam: "Soort", chips: true, opts: { beelden: "Beelden", wand: "Wandobjecten" }, v: function (x) { return x.c; } },
      { k: "merk", naam: "Merk", opts: MERKNAAM, v: function (x) { return x.ms; } },
      { k: "tint", naam: "Kleur", opts: { zilver: "Zilver", goud: "Goud", messing: "Messing en brons", zwart: "Zwart", wit: "Wit", naturel: "Naturel", aarde: "Aardetinten" }, v: function (x) { return x.tint; } },
      { k: "fmt", naam: "Formaat", opts: FMT, v: fmtVan },
      { k: "prijs", naam: "Prijs", opts: { "1": "Tot € 50", "2": "€ 50 – 150", "3": "Vanaf € 150" }, v: function (x) { return x.p < 50 ? "1" : x.p < 150 ? "2" : "3"; } }] }
  };
  var OUDE = { cat: "c", maker: "m" };
  $$(".lijst[data-bron]").forEach(function (L) {
    var cf = CONF[L.getAttribute("data-bron")], vast = {}; try { vast = JSON.parse(L.getAttribute("data-vast") || "{}"); } catch (e) {}
    var sel = {}, sort = url.get("sort") || "standaard";
    cf.filters.forEach(function (f) { var w = url.get(f.k) || url.get(Object.keys(OUDE).filter(function (o) { return OUDE[o] === f.k; })[0] || "-"); if (w && f.opts[w] && !vast[f.k]) sel[f.k] = w; });
    var basis = cf.items.filter(function (x) { return cf.filters.every(function (f) { return !vast[f.k] || f.v(x) === vast[f.k]; }); });
    var zicht = cf.filters.filter(function (f) { if (vast[f.k]) return false; var vals = {}; basis.forEach(function (x) { vals[f.v(x)] = 1; }); return Object.keys(f.opts).filter(function (o) { return vals[o]; }).length > 1; });
    var balk = L.querySelector(".filterbalk"), grid = L.querySelector("[data-grid]"), leeg = L.querySelector(".lijst-leeg"), act = L.querySelector(".actief");
    var opties = function (f) { var vals = {}; basis.forEach(function (x) { vals[f.v(x)] = 1; }); return Object.keys(f.opts).filter(function (o) { return vals[o]; }); };
    balk.innerHTML = zicht.map(function (f) {
      if (f.chips) return '<div class="chips" role="group" aria-label="' + f.naam + '"><button class="chip" type="button" data-f="' + f.k + '" data-w="" aria-pressed="' + !sel[f.k] + '">Alles</button>' + opties(f).map(function (o) { return '<button class="chip" type="button" data-f="' + f.k + '" data-w="' + o + '" aria-pressed="' + (sel[f.k] === o) + '">' + f.opts[o] + "</button>"; }).join("") + "</div>";
      return '<label class="fveld"><span>' + f.naam + '</span><select data-f="' + f.k + '"><option value="">Alle</option>' + opties(f).map(function (o) { return '<option value="' + o + '"' + (sel[f.k] === o ? " selected" : "") + ">" + f.opts[o] + "</option>"; }).join("") + "</select></label>";
    }).join("") + '<label class="fveld"><span>Sorteren</span><select data-sort><option value="standaard">Uitgelicht</option><option value="laag">Prijs laag – hoog</option><option value="hoog">Prijs hoog – laag</option><option value="groot">Formaat groot – klein</option></select></label>';
    balk.querySelector("[data-sort]").value = sort;
    var kn = document.createElement("button"); kn.type = "button"; kn.className = "filterknop"; kn.setAttribute("aria-expanded", "false");
    balk.parentNode.insertBefore(kn, balk);
    kn.addEventListener("click", function () { var o = balk.classList.toggle("open"); kn.setAttribute("aria-expanded", o); });
    var teken = function () {
      var l = basis.filter(function (x) { return zicht.every(function (f) { return !sel[f.k] || f.v(x) === sel[f.k]; }); });
      if (sort === "laag") l.sort(function (a, b) { return a.p - b.p; });
      if (sort === "hoog") l.sort(function (a, b) { return b.p - a.p; });
      if (sort === "groot") l.sort(function (a, b) { return maatVan(b) - maatVan(a); });
      grid.innerHTML = l.map(cf.kaart).join(""); leeg.hidden = l.length > 0;
      var pills = zicht.filter(function (f) { return sel[f.k]; }).map(function (f) { return '<button class="pill" type="button" data-weg-f="' + f.k + '" aria-label="Filter ' + f.naam + ' verwijderen">' + f.opts[sel[f.k]] + " <span aria-hidden=\"true\">×</span></button>"; });
      act.innerHTML = '<span class="aantal-res">' + l.length + (l.length === 1 ? (cf === CONF.W ? " werk" : " product") : (cf === CONF.W ? " werken" : " producten")) + "</span>" + pills.join("") + (pills.length > 1 ? '<button class="link" type="button" data-wis>Alles wissen</button>' : "");
      $$("[data-f]", balk).forEach(function (el) { if (el.tagName === "BUTTON") el.setAttribute("aria-pressed", (sel[el.getAttribute("data-f")] || "") === el.getAttribute("data-w")); else el.value = sel[el.getAttribute("data-f")] || ""; });
      var nf = zicht.filter(function (f) { return sel[f.k] && !f.chips; }).length; kn.textContent = "Filters en sorteren" + (nf ? " (" + nf + ")" : "");
      var q = Object.keys(sel).map(function (k) { return k + "=" + encodeURIComponent(sel[k]); }); if (sort !== "standaard") q.push("sort=" + sort);
      try { history.replaceState(null, "", location.pathname + (q.length ? "?" + q.join("&") : "") + location.hash); } catch (e) {}
    };
    L.addEventListener("click", function (e) {
      var c = e.target.closest("button[data-f]"); if (c) { var k = c.getAttribute("data-f"), w = c.getAttribute("data-w"); if (w) sel[k] = w; else delete sel[k]; teken(); return; }
      var w2 = e.target.closest("[data-weg-f]"); if (w2) { delete sel[w2.getAttribute("data-weg-f")]; teken(); return; }
      if (e.target.closest("[data-wis]")) { sel = {}; teken(); }
    });
    L.addEventListener("change", function (e) {
      var s2 = e.target.closest("select[data-f]"); if (s2) { if (s2.value) sel[s2.getAttribute("data-f")] = s2.value; else delete sel[s2.getAttribute("data-f")]; teken(); }
      if (e.target.matches("[data-sort]")) { sort = e.target.value; teken(); }
    });
    teken();
  });

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
      '<div class="info"><p class="wie"><a href="' + (x.m === "onbekend" ? "vondsten.html" : "kunstenaar-" + x.m + ".html") + '">' + MAKERS[x.m] + "</a></p><h1>" + esc(x.n) + "</h1>" +
      '<dl class="feiten"><dt>Jaar</dt><dd>' + x.j + "</dd><dt>Techniek</dt><dd>" + esc(x.mat) + "</dd><dt>Afmetingen</dt><dd>" + maat(x) + "</dd><dt>Editie</dt><dd>" + x.l + "</dd><dt>Certificaat</dt><dd>" + (x.c === "vondsten" ? "Beschrijving van herkomst en staat" : "Gesigneerd door de kunstenaar") + "</dd></dl>" +
      '<p class="grootprijs">' + prijsMooi(x.p) + '</p><p class="klein">Inclusief btw' + (x.p >= GRATIS ? ", verzekerde verzending gratis" : "") + (x.p >= 1000 ? ". Of 3 × " + euro(x.p / 3) + " zonder rente" : "") + ".</p>" +
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
        return '<div class="regel"><a class="mini" href="werk.html?w=' + x.id + '"><img src="img/' + x.img + '-m.jpg" alt=""></a><div><h3>' + esc(x.n) + '</h3><p class="klein">' + MAKERS[x.m] + " · " + maat(x) + " · " + x.l + "</p>" +
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
      var v = function (n) { var el = f.querySelector('[name="' + n + '"]'); return el ? el.value.trim() : ""; };
      var knop = f.querySelector('button[type=submit]'); knop.disabled = true; knop.textContent = "Bezig met plaatsen…"; $("#fout").textContent = "";
      api({ actie: "plaats", klant: { naam: v("voornaam") + " " + v("achternaam"), email: v("email"), tel: v("tel"), straat: v("straat"), huisnummer: v("huisnummer"), postcode: v("postcode"), plaats: v("plaats"), land: v("land") },
        regels: mand().map(function (r) { return { id: r.id, aantal: r.a }; }), betaalmethode: (f.querySelector('[name=betaal]:checked') || {}).value }).then(function (d) {
        var mijn = lees("bestellingen", []); mijn.unshift({ nr: d.nr, t: d.token }); bewaar("bestellingen", mijn.slice(0, 10));
        zetMand([]); location.href = "bestelling.html?nr=" + encodeURIComponent(d.nr) + "&t=" + encodeURIComponent(d.token) + "&nieuw=1";
      }).catch(function (err) { knop.disabled = false; knop.textContent = "Doorgaan naar veilig betalen"; $("#fout").textContent = err.message; });
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
      return "<tr><td>" + esc(x.n) + '<br><span class="klein">' + x.d + "</span></td><td>" + x.merk + "</td><td>" + prijsMooi(x.p) + "</td><td>" + ROUTE[x.r] + "</td></tr>";
    }).join("");
    balie();
  }

  /* volgpagina */
  function tijdlijn(o) {
    var log = {}; (o.log || []).forEach(function (l) { log[l.status] = l.tijd; });
    if (o.status === "geannuleerd") return '<p class="melding-ombre">Deze bestelling is geannuleerd. Het bedrag wordt teruggestort.</p>';
    var hier = VOLG.indexOf(o.status);
    return '<ol class="tijdlijn">' + VOLG.map(function (st, i) {
      return '<li class="' + (i <= hier ? "klaar" : "") + (i === hier ? " nu" : "") + '"><b>' + VOLGNAAM[st] + "</b>" + (log[st] ? '<span class="klein">' + DATUM(log[st]) + "</span>" : "") +
        (st === "verzonden" && o.track_trace && i <= hier ? '<span class="klein">' + esc(o.vervoerder || "Vervoerder") + ": " + esc(o.track_trace) + "</span>" : "") + "</li>";
    }).join("") + "</ol>";
  }
  if (pag === "bestelling") {
    var nr = url.get("nr"), tk = url.get("t");
    if (!nr || !tk) { var m0 = lees("bestellingen", [])[0]; if (m0) { nr = m0.nr; tk = m0.t; } }
    if (!nr) $("#volg").innerHTML = '<p>Er is nog geen bestelling op dit apparaat. Je vindt de volglink ook in je bevestigingsmail.</p><a class="knop" href="collectie.html">Naar de collectie</a>';
    else api({ actie: "status", nr: nr, token: tk }).then(function (o) {
      $("#volg").innerHTML = (url.get("nieuw") ? '<h2>Dank je wel voor je bestelling</h2><p>We hebben je bestelling en betaling ontvangen. De maker verzendt hem rechtstreeks naar je toe; zodra hij onderweg is, zie je hier de track-and-trace. Bewaar deze pagina: hij laat altijd de actuele status zien.</p>' : "<h2>Status van je bestelling</h2>") +
        '<p class="klein">Bestelnummer <b>' + esc(o.nr) + "</b> · geplaatst op " + DATUM(o.created_at) + "</p>" + tijdlijn(o) +
        '<div class="samenvatting" style="position:static;margin-top:28px">' + o.regels.map(function (r) { return '<div class="rij"><span>' + (r.aantal > 1 ? r.aantal + " × " : "") + "<i>" + esc(r.naam) + "</i>, " + esc(r.maker) + "</span><span>" + euro(r.prijs * r.aantal) + "</span></div>"; }).join("") +
        '<div class="rij"><span>Verzekerde verzending</span><span>' + (+o.verzending ? euro(+o.verzending) : "Gratis") + '</span></div><div class="rij totaal"><span>Totaal</span><span>' + euro(+o.totaal) + "</span></div></div>" +
        (o.test ? '<p class="noot">Testbestelling vanuit het concept: er is niet betaald en er wordt niets verzonden.</p>' : "") +
        '<p style="margin-top:24px"><a class="link" href="service.html#contact">Vraag over je bestelling?</a></p>';
    }).catch(function (e) { $("#volg").innerHTML = "<p>" + esc(e.message) + '</p><a class="link" href="service.html#contact">Neem contact op</a>'; });
  }

  /* bestelbalie (beheer) */
  function balie() {
    var el = $("#balie"); if (!el) return;
    var code = url.get("setup"), sessie = lees("sessie", "");
    if (code) {
      el.innerHTML = '<form class="form balie-vak" id="setup"><h3>Beheer instellen</h3><p class="klein">Kies je eigen wachtwoord voor de bestelbalie. Alleen jij kent het; het wordt versleuteld opgeslagen.</p><label>Nieuw wachtwoord (minstens 10 tekens)<input type="password" name="pw" autocomplete="new-password" required minlength="10"></label><label>Herhaal wachtwoord<input type="password" name="pw2" autocomplete="new-password" required></label><p class="fout" role="status"></p><button class="knop" type="submit">Wachtwoord instellen</button></form>';
      $("#setup").addEventListener("submit", function (e) {
        e.preventDefault(); var f = this, fo = f.querySelector(".fout");
        if (f.pw.value.length < 10) { fo.textContent = "Kies minstens 10 tekens."; return; }
        if (f.pw.value !== f.pw2.value) { fo.textContent = "De wachtwoorden zijn niet gelijk."; return; }
        api({ actie: "setup", code: code, wachtwoord: f.pw.value }).then(function () { history.replaceState(null, "", "beheer.html#bestellingen"); url = new URLSearchParams(""); el.innerHTML = '<p class="bevestig">Je wachtwoord is ingesteld. Log hieronder in.</p>'; setTimeout(balie, 900); }).catch(function (er) { fo.textContent = er.message; });
      });
      return;
    }
    if (!sessie) {
      el.innerHTML = '<form class="form balie-vak" id="login"><h3>Inloggen op de bestelbalie</h3><label>Wachtwoord<input type="password" name="pw" autocomplete="current-password" required></label><p class="fout" role="status"></p><button class="knop" type="submit">Inloggen</button></form>';
      $("#login").addEventListener("submit", function (e) {
        e.preventDefault(); var f = this, fo = f.querySelector(".fout"); fo.textContent = "";
        api({ actie: "login", wachtwoord: f.pw.value }).then(function (d) { bewaar("sessie", d.sessie); balie(); }).catch(function (er) { fo.textContent = er.message; });
      });
      return;
    }
    el.innerHTML = '<p class="leeg">Bestellingen laden…</p>';
    api({ actie: "lijst", sessie: sessie }).then(function (d) {
      var o = d.orders, open = o.filter(function (x) { return x.status === "betaald"; }).length;
      el.innerHTML = '<div class="balie-kop"><span><b>' + o.length + "</b> bestellingen · <b>" + open + '</b> wachten op inkoop</span><span><button class="link" type="button" id="ververs">Vernieuwen</button> · <button class="link" type="button" id="uitlog">Uitloggen</button></span></div>' +
        (o.length ? o.map(orderKaart).join("") : '<p class="leeg">Nog geen bestellingen.</p>');
      $("#ververs").addEventListener("click", balie);
      $("#uitlog").addEventListener("click", function () { bewaar("sessie", ""); balie(); });
    }).catch(function (er) { if (er.code === 401) { bewaar("sessie", ""); balie(); } else el.innerHTML = '<p class="fout">' + esc(er.message) + "</p>"; });
  }
  function orderKaart(o) {
    var a = o.adres || {}, adres = o.klant_naam + "\n" + a.straat + " " + a.huisnummer + "\n" + a.postcode + " " + a.plaats + "\n" + a.land;
    var regels = o.regels.map(function (r) {
      return '<li><span><b>' + (r.aantal > 1 ? r.aantal + " × " : "") + esc(r.naam) + "</b> · " + esc(r.leverancier) + "</span><span>" + euro(r.prijs * r.aantal) +
        (r.bron ? '<br><a class="link" href="' + esc(r.bron) + '" target="_blank" rel="noopener">Bestel bij verkoper</a>' : '<br><span class="klein">Eigen route</span>') + "</span></li>";
    }).join("");
    var vv = ["PostNL", "DHL", "DPD", "GLS", "UPS", "Kunstkoerier", "Anders"];
    return '<article class="balie-order st-' + o.status + '" data-nr="' + esc(o.nr) + '"><header><b>' + esc(o.nr) + "</b>" + (o.test ? '<span class="tag">Test</span>' : "") + '<span class="pil">' + VOLGNAAM[o.status] + '</span><span class="klein">' + DATUM(o.created_at) + " · " + esc(o.betaalmethode || "") + "</span><b class=\"tot\">" + euro(+o.totaal) + "</b></header>" +
      '<div class="balie-raster"><div><h4>Afleveradres (adres van de klant)</h4><pre>' + esc(adres) + '</pre><button class="chip" type="button" data-kopieer="' + esc(adres) + '">Kopieer adres</button><p class="klein" style="margin-top:10px">' + esc(o.klant_email) + (o.klant_tel ? " · " + esc(o.klant_tel) : "") + "</p></div>" +
      "<div><h4>Inkopen</h4><ul class=\"balie-regels\">" + regels + "</ul></div>" +
      '<div><h4>Verkoper en verzending</h4><form class="form balie-form"><label>Ordernummer bij verkoper<input name="leverancier_ordernr" value="' + esc(o.leverancier_ordernr || "") + '"></label>' +
      '<div class="twee"><label>Vervoerder<select name="vervoerder"><option value="">Kies</option>' + vv.map(function (x) { return "<option" + (x === o.vervoerder ? " selected" : "") + ">" + x + "</option>"; }).join("") + '</select></label><label>Track-and-trace<input name="track_trace" value="' + esc(o.track_trace || "") + '"></label></div>' +
      '<label>Notitie<input name="notitie" value="' + esc(o.notitie || "") + '"></label><div class="balie-knoppen">' +
      (o.status === "betaald" ? '<button class="knop" type="button" data-zet="besteld">Besteld bij verkoper</button>' : "") +
      (o.status === "besteld" ? '<button class="knop" type="button" data-zet="verzonden">Markeer als verzonden</button>' : "") +
      (o.status === "verzonden" ? '<button class="knop" type="button" data-zet="geleverd">Markeer als geleverd</button>' : "") +
      '<button class="knop licht" type="button" data-zet="">Opslaan</button>' + (o.status !== "geannuleerd" && o.status !== "geleverd" ? '<button class="link" type="button" data-zet="geannuleerd">Annuleren</button>' : "") + '</div><p class="fout" role="status"></p></form></div></div></article>';
  }
  document.addEventListener("click", function (e) {
    var k = e.target.closest("[data-kopieer]");
    if (k) { var t = k.getAttribute("data-kopieer"); (navigator.clipboard ? navigator.clipboard.writeText(t) : Promise.reject()).then(function () { toast("Adres gekopieerd"); }, function () { toast("Kopiëren lukte niet; selecteer het adres handmatig"); }); return; }
    var z = e.target.closest("[data-zet]"); if (!z) return;
    var kaart = z.closest(".balie-order"), f = kaart.querySelector("form"), fo = f.querySelector(".fout"), st = z.getAttribute("data-zet");
    if (st === "verzonden" && !f.track_trace.value.trim()) { fo.textContent = "Vul eerst de track-and-trace in."; f.track_trace.focus(); return; }
    if (st === "geannuleerd" && !confirm("Deze bestelling annuleren? Vergeet niet het bedrag terug te betalen.")) return;
    var data = { actie: "update", sessie: lees("sessie", ""), nr: kaart.getAttribute("data-nr"), leverancier_ordernr: f.leverancier_ordernr.value, vervoerder: f.vervoerder.value, track_trace: f.track_trace.value, notitie: f.notitie.value };
    if (st) data.status = st;
    z.disabled = true;
    api(data).then(function () { toast(st ? "Status bijgewerkt: " + VOLGNAAM[st] : "Opgeslagen"); balie(); }).catch(function (er) { z.disabled = false; fo.textContent = er.message; });
  });

  tellers();
})();
