/* Suismuis Home – klantaccount en interieuradviseur (server-functie "suismuis-klant"). Gebouwd door Collens Group. */
(function () {
  "use strict";
  var API = "https://eyrfizayagcwaxbxyeuh.supabase.co/functions/v1/suismuis-klant";
  var $ = function (s, r) { return (r || document).querySelector(s); };
  var esc = function (s) { return String(s == null ? "" : s).replace(/[&<>"']/g, function (c) { return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]; }); };
  var euro = function (x) { return "€ " + Number(x).toFixed(2).replace(".", ","); };
  var basis = function () { return location.origin + location.pathname.replace(/\/[^\/]*$/, ""); };
  var opslag = function (k, v) { try { if (v === undefined) return localStorage.getItem(k); if (v === null) localStorage.removeItem(k); else localStorage.setItem(k, v); } catch (e) { return null; } };
  function api(data) {
    return fetch(API, { method: "POST", headers: { "Content-Type": "application/json" }, body: JSON.stringify(data) })
      .then(function (r) { return r.json().catch(function () { return {}; }).then(function (j) { if (!r.ok && !j.fout) j.fout = "Er ging iets mis. Probeer het opnieuw."; j._status = r.status; return j; }); })
      .catch(function () { return { fout: "Geen verbinding. Controleer je internet en probeer het opnieuw." }; });
  }
  var sessie = function () { return opslag("suis-ksessie") || ""; };
  var pag = document.body.dataset.pagina;

  /* ---------- accountpagina ---------- */
  if (pag === "account") {
    var melding = $("#acc-melding"), url = new URLSearchParams(location.search);
    var meld = function (t) { melding.textContent = t; melding.hidden = !t; };
    var toon = function (id) { ["acc-uit", "acc-reset", "acc-in"].forEach(function (x) { $("#" + x).hidden = x !== id; }); };
    var fout = function (f, t) { $(".fout", f).textContent = t || ""; };
    var leeg = function (f) { var x = Array.prototype.filter.call(f.querySelectorAll("[required]"), function (i) { return i.type === "checkbox" ? !i.checked : (!i.value.trim() || !i.checkValidity()); })[0]; if (x) x.focus(); return x; };
    var bezig = function (f, aan) { var k = $("button[type=submit]", f); if (!k.dataset.t) k.dataset.t = k.textContent; k.disabled = aan; k.textContent = aan ? "Bezig…" : k.dataset.t; };
    var STAP = { betaald: "Betaald", besteld: "In behandeling", verzonden: "Verzonden", geleverd: "Bezorgd" };
    var orderHtml = function (o) {
      return '<div class="orderkaart"><span class="klein">Bestelling ' + esc(o.nr) + ' · ' + new Date(o.created_at).toLocaleDateString("nl-NL", { day: "numeric", month: "long", year: "numeric" }) + '</span><h2 style="font-size:30px">' + esc(o.status_tekst || STAP[o.status] || o.status) + '</h2>' +
        (o.track_trace ? '<p><b>Track-and-trace:</b> ' + esc(o.vervoerder || "") + ' ' + (/^https?:\/\//.test(o.track_trace) ? '<a class="link" href="' + esc(o.track_trace) + '" rel="noopener" target="_blank">volg je pakket</a>' : esc(o.track_trace)) + '</p>' : "") +
        (o.iban ? '<p>Maak <b>' + euro(o.totaal) + '</b> over naar <b>' + esc(o.iban) + '</b> t.n.v. Suismuis Home, onder vermelding van <b>' + esc(o.nr) + '</b>.</p>' : "") +
        '<div class="samenvatting">' + (o.regels || []).map(function (r) { return '<div class="rij"><span>' + r.aantal + " × " + esc(r.naam) + (r.uitvoering ? " <small>(" + esc(r.uitvoering) + ")</small>" : "") + "</span><span>" + euro(r.prijs * r.aantal) + "</span></div>"; }).join("") +
        '<div class="rij totaal"><span>Totaal</span><span>' + euro(o.totaal) + "</span></div></div></div>";
    };
    var laad = function () {
      if (!sessie()) { toon("acc-uit"); return; }
      api({ actie: "account_ik", ksessie: sessie() }).then(function (j) {
        if (j.fout) { if (j.uitgelogd) opslag("suis-ksessie", null); toon("acc-uit"); if (!j.uitgelogd) meld(j.fout); return; }
        var k = j.klant, a = k.adres || {}, f = $("#f-gegevens");
        $("#acc-titel").textContent = "Welkom" + (k.naam ? ", " + k.naam.split(" ")[0] : "");
        $("#acc-intro").textContent = "Hier zie je je bestellingen en beheer je je gegevens.";
        $("#acc-email").textContent = "Ingelogd als " + k.email;
        f.elements.naam.value = k.naam || ""; f.elements.tel.value = k.tel || ""; f.elements.postcode.value = a.postcode || ""; f.elements.huisnummer.value = a.huisnummer || "";
        f.elements.straat.value = a.straat || ""; f.elements.plaats.value = a.plaats || ""; if (a.land) f.elements.land.value = a.land; f.elements.nieuwsbrief.checked = !!k.nieuwsbrief;
        $("#acc-orders").innerHTML = j.orders.length ? j.orders.map(orderHtml).join("") : '<p>Je hebt nog geen bestellingen met dit account.</p><a class="knop" href="shop.html">Naar de shop</a>';
        toon("acc-in");
      });
    };
    var ingelogd = function (s) { opslag("suis-ksessie", s); meld(""); history.replaceState(null, "", location.pathname); laad(); window.scrollTo(0, 0); };

    $("#f-in").addEventListener("submit", function (e) {
      e.preventDefault(); var f = this; if (leeg(f)) { fout(f, "Vul je e-mailadres en wachtwoord in."); return; }
      bezig(f, true); fout(f, "");
      api({ actie: "account_login", email: f.elements.email.value.trim(), wachtwoord: f.elements.wachtwoord.value }).then(function (j) { bezig(f, false); if (j.fout) { fout(f, j.fout); return; } ingelogd(j.sessie); });
    });
    $("#f-nieuw").addEventListener("submit", function (e) {
      e.preventDefault(); var f = this, x = leeg(f);
      if (x) { fout(f, x.type === "checkbox" ? "Vink aan dat je de privacyverklaring hebt gelezen." : x.name === "wachtwoord" ? "Kies een wachtwoord van minstens 8 tekens." : "Vul je naam en een geldig e-mailadres in."); return; }
      bezig(f, true); fout(f, "");
      api({ actie: "account_registreer", site: basis(), naam: f.elements.naam.value.trim(), email: f.elements.email.value.trim(), wachtwoord: f.elements.wachtwoord.value, nieuwsbrief: f.elements.nieuwsbrief.checked, akkoord: f.elements.akkoord.checked })
        .then(function (j) { bezig(f, false); if (j.fout) { fout(f, j.fout); return; } ingelogd(j.sessie); });
    });
    $("#naar-vergeten").addEventListener("click", function () { $("#f-in").hidden = true; $("#f-vergeten").hidden = false; $("#f-vergeten").elements.email.value = $("#f-in").elements.email.value; $("#f-vergeten").elements.email.focus(); });
    $("#terug-in").addEventListener("click", function () { $("#f-vergeten").hidden = true; $("#f-in").hidden = false; });
    $("#f-vergeten").addEventListener("submit", function (e) {
      e.preventDefault(); var f = this; if (leeg(f)) { fout(f, "Vul een geldig e-mailadres in."); return; }
      bezig(f, true);
      api({ actie: "account_vergeten", site: basis(), email: f.elements.email.value.trim() }).then(function (j) {
        bezig(f, false); if (j.fout) { fout(f, j.fout); return; }
        fout(f, ""); meld("Als er een account is met dit e-mailadres, krijg je binnen een paar minuten een mail. Kijk ook in je spam.");
      });
    });
    $("#f-reset").addEventListener("submit", function (e) {
      e.preventDefault(); var f = this; if (leeg(f)) { fout(f, "Kies een wachtwoord van minstens 8 tekens."); return; }
      bezig(f, true);
      api({ actie: "account_reset", token: url.get("reset"), wachtwoord: f.elements.wachtwoord.value }).then(function (j) { bezig(f, false); if (j.fout) { fout(f, j.fout); return; } ingelogd(j.sessie); meld("Je nieuwe wachtwoord is opgeslagen."); });
    });
    $("#f-gegevens").addEventListener("submit", function (e) {
      e.preventDefault(); var f = this, v = function (n) { return f.elements[n].value.trim(); };
      bezig(f, true);
      api({ actie: "account_opslaan", ksessie: sessie(), naam: v("naam"), tel: v("tel"), nieuwsbrief: f.elements.nieuwsbrief.checked, adres: { straat: v("straat"), huisnummer: v("huisnummer"), postcode: v("postcode"), plaats: v("plaats"), land: f.elements.land.value } })
        .then(function (j) { bezig(f, false); fout(f, j.fout || ""); if (!j.fout) meld("Je gegevens zijn opgeslagen."); });
    });
    $("#f-pw").addEventListener("submit", function (e) {
      e.preventDefault(); var f = this; if (leeg(f)) { fout(f, "Vul je huidige wachtwoord en een nieuw wachtwoord van minstens 8 tekens in."); return; }
      bezig(f, true);
      api({ actie: "account_wachtwoord", ksessie: sessie(), wachtwoord: f.elements.wachtwoord.value, nieuw: f.elements.nieuw.value }).then(function (j) { bezig(f, false); if (j.fout) { fout(f, j.fout); return; } opslag("suis-ksessie", j.sessie); f.reset(); fout(f, ""); meld("Je wachtwoord is gewijzigd."); });
    });
    $("#f-weg").addEventListener("submit", function (e) {
      e.preventDefault(); var f = this; if (leeg(f)) { fout(f, "Vul je wachtwoord in ter bevestiging."); return; }
      bezig(f, true);
      api({ actie: "account_verwijder", ksessie: sessie(), wachtwoord: f.elements.wachtwoord.value }).then(function (j) { bezig(f, false); if (j.fout) { fout(f, j.fout); return; } opslag("suis-ksessie", null); toon("acc-uit"); meld("Je account is verwijderd."); window.scrollTo(0, 0); });
    });
    $("#uitloggen").addEventListener("click", function () { api({ actie: "account_uit", ksessie: sessie() }); opslag("suis-ksessie", null); $("#acc-titel").textContent = "Mijn account"; toon("acc-uit"); meld("Je bent uitgelogd."); window.scrollTo(0, 0); });

    if (url.get("reset")) toon("acc-reset"); else laad();
  }

  /* ---------- afrekenen: gegevens invullen en de bestelling aan het account koppelen ---------- */
  if (pag === "afrekenen" && $("#bestel")) {
    var f = $("#bestel"), fo = $("#fout");
    var bewaar = document.createElement("label"); bewaar.className = "check"; bewaar.hidden = true;
    bewaar.innerHTML = '<input name="bewaar_adres" type="checkbox" checked><span>Bewaar deze gegevens in mijn account</span>';
    var hint = document.createElement("p"); hint.className = "noot";
    hint.innerHTML = 'Heb je een account? <a class="link" href="account.html">Log in</a> en je gegevens staan meteen klaar.';
    if (fo) { fo.parentNode.insertBefore(bewaar, fo); fo.parentNode.insertBefore(hint, fo); }
    if (sessie()) {
      api({ actie: "account_ik", ksessie: sessie() }).then(function (j) {
        if (j.fout) { if (j.uitgelogd) opslag("suis-ksessie", null); return; }
        var k = j.klant, a = k.adres || {}, n = (k.naam || "").split(" ");
        var zet = function (naam, w) { var el = f.elements[naam]; if (el && !el.value && w) el.value = w; };
        zet("voornaam", n[0]); zet("achternaam", n.slice(1).join(" ")); zet("email", k.email); zet("tel", k.tel);
        zet("postcode", a.postcode); zet("huisnummer", a.huisnummer); zet("straat", a.straat); zet("plaats", a.plaats);
        if (a.land && f.elements.land) f.elements.land.value = a.land;
        bewaar.hidden = false; hint.innerHTML = "Ingelogd als " + esc(k.email) + ". Je bestelling komt in je account te staan.";
      });
    }
    window.suisNaStart = function (order) {
      if (!sessie() || !order || !order.nr) return;
      api({ actie: "account_koppel", ksessie: sessie(), nr: order.nr, token: order.token, bewaar_adres: !bewaar.hidden && f.elements.bewaar_adres.checked });
    };
  }

  /* kop: het persoonsicoon gaat naar Mijn account */
  Array.prototype.forEach.call(document.querySelectorAll('.iconen a[href="bestelling.html"]'), function (a) { a.href = "account.html"; a.setAttribute("aria-label", "Mijn account"); });

  /* ---------- interieuradviseur ---------- */
  /* AI via Make (scenario 8815970); zet op false om de adviseur te verbergen */
  var CHAT_AAN = true;
  if (pag === "beheer" || !(CHAT_AAN || /[?&]advies=1/.test(location.search))) return;
  var bezoeker = opslag("suis-bezoeker");
  if (!bezoeker) { bezoeker = "b-" + Date.now().toString(36) + "-" + Math.random().toString(36).slice(2, 10); opslag("suis-bezoeker", bezoeker); }
  var gesprek = [];
  try { gesprek = JSON.parse(sessionStorage.getItem("suis-chat") || "[]"); } catch (e) { gesprek = []; }
  var bewaarGesprek = function () { try { sessionStorage.setItem("suis-chat", JSON.stringify(gesprek.slice(-20))); } catch (e) { /* geen opslag */ } };
  var knopC = document.createElement("button");
  knopC.type = "button"; knopC.className = "advies-knop"; knopC.setAttribute("aria-haspopup", "dialog"); knopC.setAttribute("aria-expanded", "false");
  knopC.innerHTML = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 5h16v11H9l-5 4z"/></svg><span>Interieuradvies</span>';
  var paneel = document.createElement("section");
  paneel.className = "advies"; paneel.hidden = true; paneel.setAttribute("role", "dialog"); paneel.setAttribute("aria-label", "Interieuradvies");
  paneel.innerHTML = '<div class="advies-kop"><div><b>Interieuradvies</b><small>Onze AI-adviseur kiest mee uit de collectie</small></div><button type="button" class="advies-sluit" aria-label="Sluiten">×</button></div>' +
    '<div class="advies-lijst" aria-live="polite"></div>' +
    '<form class="advies-form"><label class="sr" for="advies-in">Je vraag</label><input id="advies-in" name="v" autocomplete="off" maxlength="1000" placeholder="Bijv. iets voor mijn salontafel in beige"><button type="submit" class="knop">Stuur</button></form>' +
    '<p class="advies-noot">Advies door AI, op basis van onze collectie. Vragen over een bestelling? <a href="klantenservice.html#contact">Klantenservice</a></p>';
  document.body.appendChild(knopC); document.body.appendChild(paneel);
  var lijst = $(".advies-lijst", paneel), vorm = $(".advies-form", paneel), inv = $("#advies-in", paneel);
  var bel = function (rol, t, prods) {
    var d = document.createElement("div"); d.className = "advies-bel " + rol;
    d.innerHTML = esc(t).replace(/\n/g, "<br>") + (prods && prods.length ? '<div class="advies-prods">' + prods.map(function (p) {
      return '<a href="product.html?p=' + encodeURIComponent(p.id) + '">' + (p.img ? '<img src="' + esc(p.img) + '" alt="" loading="lazy">' : "") + '<span>' + esc(p.n) + '<b>' + euro(p.p) + '</b></span></a>';
    }).join("") + "</div>" : "");
    lijst.appendChild(d); lijst.scrollTop = lijst.scrollHeight;
  };
  var welkom = "Hoi! Waar ben je naar op zoek? Vertel me welke ruimte je inricht, welke kleuren je mooi vindt of wat je budget is, dan zoek ik passende stukken uit onze collectie.";
  var open = function (aan) {
    paneel.hidden = !aan; knopC.setAttribute("aria-expanded", String(aan)); knopC.hidden = aan;
    if (aan) { if (!lijst.children.length) { bel("bot", welkom); gesprek.forEach(function (m) { bel(m.rol === "klant" ? "klant" : "bot", m.t, m.p); }); } inv.focus(); } else knopC.focus();
  };
  knopC.addEventListener("click", function () { open(true); });
  $(".advies-sluit", paneel).addEventListener("click", function () { open(false); });
  paneel.addEventListener("keydown", function (e) { if (e.key === "Escape") open(false); });
  vorm.addEventListener("submit", function (e) {
    e.preventDefault(); var v = inv.value.trim(); if (!v) return;
    inv.value = ""; bel("klant", v);
    var wacht = document.createElement("div"); wacht.className = "advies-bel bot wacht"; wacht.textContent = "Even kijken…"; lijst.appendChild(wacht); lijst.scrollTop = lijst.scrollHeight;
    var knopS = $("button", vorm); knopS.disabled = true;
    var prod = pag === "product" ? new URLSearchParams(location.search).get("p") : "";
    api({ actie: "chat", bezoeker: bezoeker, bericht: v, product: prod || "", geschiedenis: gesprek.map(function (m) { return { rol: m.rol, t: m.t }; }) }).then(function (j) {
      wacht.remove(); knopS.disabled = false; inv.focus();
      if (j.fout) { bel("bot advies-fout", j.fout); return; }
      gesprek.push({ rol: "klant", t: v }); gesprek.push({ rol: "bot", t: j.antwoord, p: j.producten });
      bewaarGesprek(); bel("bot", j.antwoord, j.producten);
    });
  });

})();
