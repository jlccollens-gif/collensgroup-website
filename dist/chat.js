/* Chat-adviseur van Collens Group. Verschijnt alleen als /api/chat meldt dat hij actief is. */
(() => {
  const TAAL = (document.documentElement.lang || "nl").slice(0, 2);
  const T = {
    nl: { knop: "Twijfel je? Vraag de adviseur", kort: "Advies", titel: "Online adviseur", sub: "Collens Group · 24/7 online", sluit: "Sluiten", plek: "Typ je vraag…", stuur: "Versturen",
          hallo: "Hoi! Ik help je graag kiezen. Weet je nog niet precies wat je nodig hebt? Vertel wat je wilt bereiken, dan denk ik met je mee en adviseer ik welke oplossing en welk pakket passen.",
          snel: ["Ik weet nog niet wat ik nodig heb", "Wat kost een website?", "Ik heb een idee voor een app"], denkt: "Adviseur typt…", fout: "Sorry, dat lukte even niet. Probeer het nog eens, of mail naar info@collensgroup.com.",
          noot: "Je praat met een AI-adviseur (Claude). Deel geen gevoelige gegevens.", privacy: "Privacy", opnieuw: "Nieuw gesprek", klaar: "Doorgestuurd: we mailen je zo snel mogelijk." },
    en: { knop: "Not sure? Ask our advisor", kort: "Advice", titel: "Online advisor", sub: "Collens Group · online 24/7", sluit: "Close", plek: "Type your question…", stuur: "Send",
          hallo: "Hi! I'm happy to help you choose. Not sure exactly what you need? Tell me what you want to achieve and I'll think along and recommend the solution and package that fit.",
          snel: ["I'm not sure what I need", "How much is a website?", "I have an idea for an app"], denkt: "Advisor is typing…", fout: "Sorry, something went wrong. Please try again, or email info@collensgroup.com.",
          noot: "You're chatting with an AI advisor (Claude). Don't share sensitive information.", privacy: "Privacy", opnieuw: "New chat", klaar: "Sent: we'll email you as soon as possible." },
    de: { knop: "Unsicher? Fragen Sie den Berater", kort: "Beratung", titel: "Online-Berater", sub: "Collens Group · 24/7 online", sluit: "Schließen", plek: "Ihre Frage…", stuur: "Senden",
          hallo: "Hallo! Ich helfe Ihnen gern bei der Wahl. Sie wissen noch nicht genau, was Sie brauchen? Erzählen Sie, was Sie erreichen möchten, dann denke ich mit und empfehle die passende Lösung.",
          snel: ["Ich weiß noch nicht, was ich brauche", "Was kostet eine Website?", "Ich habe eine App-Idee"], denkt: "Berater schreibt…", fout: "Entschuldigung, das hat nicht geklappt. Bitte erneut versuchen oder an info@collensgroup.com schreiben.",
          noot: "Sie chatten mit einem KI-Berater (Claude). Teilen Sie keine sensiblen Daten.", privacy: "Datenschutz", opnieuw: "Neues Gespräch", klaar: "Weitergeleitet: Wir melden uns so schnell wie möglich per E-Mail." },
    fr: { knop: "Un doute ? Demandez au conseiller", kort: "Conseil", titel: "Conseiller en ligne", sub: "Collens Group · en ligne 24h/24", sluit: "Fermer", plek: "Votre question…", stuur: "Envoyer",
          hallo: "Bonjour ! Je vous aide volontiers à choisir. Vous ne savez pas encore ce qu'il vous faut ? Dites-moi ce que vous voulez accomplir, je réfléchis avec vous et vous recommande la bonne solution.",
          snel: ["Je ne sais pas ce qu'il me faut", "Combien coûte un site web ?", "J'ai une idée d'application"], denkt: "Le conseiller écrit…", fout: "Désolé, une erreur s'est produite. Réessayez ou écrivez à info@collensgroup.com.",
          noot: "Vous discutez avec un conseiller IA (Claude). Ne partagez pas d'informations sensibles.", privacy: "Confidentialité", opnieuw: "Nouvelle discussion", klaar: "Envoyé : nous vous écrirons au plus vite." },
    es: { knop: "¿Dudas? Pregunta al asesor", kort: "Asesor", titel: "Asesor en línea", sub: "Collens Group · en línea 24/7", sluit: "Cerrar", plek: "Escribe tu pregunta…", stuur: "Enviar",
          hallo: "¡Hola! Te ayudo a elegir. ¿Aún no sabes exactamente lo que necesitas? Cuéntame qué quieres conseguir y pienso contigo qué solución y paquete te encajan.",
          snel: ["No sé qué necesito", "¿Cuánto cuesta una web?", "Tengo una idea para una app"], denkt: "El asesor escribe…", fout: "Lo siento, algo falló. Inténtalo de nuevo o escribe a info@collensgroup.com.",
          noot: "Hablas con un asesor de IA (Claude). No compartas datos sensibles.", privacy: "Privacidad", opnieuw: "Nueva conversación", klaar: "Enviado: te escribiremos lo antes posible." },
  }[TAAL] || null;
  if (!T) return;
  const SLEUTEL = "cg-chat-v1";

  const css = `
.cg-fab[hidden],.cg-paneel[hidden],.chat-blok[hidden]{display:none!important}
.cg-fab{position:fixed;right:18px;bottom:18px;z-index:50;display:flex;align-items:center;gap:10px;background:#14213D;color:#fff;border:0;border-radius:999px;padding:12px 18px 12px 14px;font:700 16px/1.2 "Atkinson Hyperlegible",system-ui,sans-serif;box-shadow:0 10px 30px rgba(14,24,48,.28);cursor:pointer}
.cg-fab:hover{background:#2457D6}.cg-fab .cg-stip{width:9px;height:9px;border-radius:50%;background:#22C55E;box-shadow:0 0 0 3px rgba(34,197,94,.25)}
.cg-fab .cg-kort{display:none}@media (max-width:520px){.cg-fab .cg-lang{display:none}.cg-fab .cg-kort{display:inline}}
.cg-paneel{position:fixed;right:18px;bottom:18px;z-index:60;width:min(400px,calc(100vw - 24px));height:min(620px,calc(100vh - 36px));display:flex;flex-direction:column;background:#fff;border-radius:22px;box-shadow:0 24px 60px rgba(14,24,48,.32);overflow:hidden;font-family:"Atkinson Hyperlegible",system-ui,sans-serif}
@media (max-width:520px){.cg-paneel{right:0;bottom:0;width:100vw;height:100dvh;border-radius:0}}
.cg-kop{display:flex;align-items:center;gap:12px;background:#14213D;color:#fff;padding:14px 14px 14px 18px}
.cg-kop img{width:34px;height:34px;border-radius:50%;background:#fff}.cg-kop b{display:block;font-size:17px}.cg-kop small{color:#AEBBD2;font-size:13px}
.cg-kop .cg-acties{margin-left:auto;display:flex;gap:4px}.cg-kop button{white-space:nowrap;background:transparent;border:0;color:#fff;cursor:pointer;border-radius:10px;padding:6px 10px;font:inherit;font-size:20px;line-height:1}
.cg-kop button:hover{background:rgba(255,255,255,.12)}
.cg-log{flex:1;overflow-y:auto;padding:16px;display:flex;flex-direction:column;gap:10px;background:#F3F6FA}
.cg-b{max-width:86%;padding:10px 14px;border-radius:16px;font-size:16px;line-height:1.5;white-space:pre-wrap;overflow-wrap:anywhere}
.cg-b.bot{background:#fff;color:#22304D;border:1px solid #E1E7F0;border-bottom-left-radius:6px;align-self:flex-start}
.cg-b.jij{background:#2457D6;color:#fff;border-bottom-right-radius:6px;align-self:flex-end}
.cg-b a{color:#2457D6;font-weight:700}.cg-b ul{margin:4px 0;padding-left:20px;white-space:normal}
.cg-b.denkt{color:#5A6782;font-style:italic}.cg-b.ok{background:#E8F7EE;border-color:#BFE6CD;color:#14532D}
.cg-snel{display:flex;flex-wrap:wrap;gap:8px}.cg-snel button{background:#fff;border:1.5px solid #2457D6;color:#2457D6;border-radius:999px;padding:7px 12px;font:600 14px "Atkinson Hyperlegible",system-ui,sans-serif;cursor:pointer}
.cg-snel button:hover{background:#2457D6;color:#fff}
.cg-form{display:flex;gap:8px;padding:12px;border-top:1px solid #E1E7F0;background:#fff}
.cg-form textarea{flex:1;resize:none;border:1.5px solid #C9D3E1!important;border-radius:14px;padding:10px 12px;font:16px/1.4 "Atkinson Hyperlegible",system-ui,sans-serif;height:46px;min-height:46px!important;max-height:120px;margin:0!important;background:#fff!important;color:#22304D!important;width:auto!important;box-sizing:border-box}
.cg-form textarea::placeholder{color:#7A869E}
.cg-form textarea:focus{outline:none;border-color:#2457D6}
.cg-form button{align-self:flex-end;height:46px;background:#F2B705;color:#14213D;border:0;border-radius:14px;padding:0 16px;font-weight:700;cursor:pointer}
.cg-form button:disabled{opacity:.5;cursor:default}
.cg-noot{margin:0;padding:0 14px 10px;background:#fff;color:#5A6782;font-size:12px}.cg-noot a{color:#5A6782}
.chat-blok{background:#14213D;color:#fff;padding:44px 0}.chat-blok h2{color:#fff;font-size:clamp(26px,3.2vw,36px)}
.chat-blok-in{display:grid;grid-template-columns:auto 1fr auto;gap:24px;align-items:center}
.chat-blok-ico{width:58px;height:58px;border-radius:18px;background:#F2B705;color:#14213D;display:grid;place-items:center}.chat-blok-ico svg{width:30px;height:30px}
.chat-blok p{color:#C9D3E1;margin:10px 0 0;max-width:640px}
.chat-blok-actie{display:flex;flex-direction:column;align-items:flex-start;gap:8px}.chat-blok-actie small{color:#AEBBD2;font-size:14px}
.chat-blok-actie small::before{content:"";display:inline-block;width:8px;height:8px;border-radius:50%;background:#22C55E;margin-right:7px;vertical-align:middle}
@media (max-width:820px){.chat-blok-in{grid-template-columns:1fr;gap:16px}}`;

  let berichten = [], klaar = false;
  try { const s = JSON.parse(sessionStorage.getItem(SLEUTEL) || "null"); if (s && Array.isArray(s.b)) { berichten = s.b; klaar = !!s.k; } } catch (_) {}
  const bewaar = () => { try { sessionStorage.setItem(SLEUTEL, JSON.stringify({ b: berichten.slice(-40), k: klaar })); } catch (_) {} };

  const esc = s => s.replace(/[&<>"']/g, c => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]));
  function opmaak(t) {
    let h = esc(t);
    h = h.replace(/\*\*([^*\n]+)\*\*/g, "<strong>$1</strong>");
    h = h.replace(/\[([^\]\n]+)\]\(([^)\s]+)\)/g, (m, tekst, url) => {
      const ok = /^(?:[a-z0-9-]+\.html(?:#[\w-]+)?|#[\w-]+|https:\/\/(?:www\.)?collensgroup\.com\/[^\s]*|mailto:info@collensgroup\.com)$/i.test(url);
      return ok ? `<a href="${url}">${tekst}</a>` : tekst;
    });
    h = h.replace(/(^|\s)(info@collensgroup\.com)/g, '$1<a href="mailto:$2">$2</a>');
    h = h.replace(/(?:^|\n)((?:[-•] .+(?:\n|$))+)/g, (m, blok) => "\n<ul>" + blok.trim().split("\n").map(r => "<li>" + r.replace(/^[-•] /, "") + "</li>").join("") + "</ul>");
    return h.replace(/<\/ul>\n+/g, "</ul>").replace(/\n+<ul>/g, "<ul>").trim();
  }

  let paneel, log, veld, knop, fab, bezig = false;

  function bel(rol, tekst, extra) {
    const d = document.createElement("div");
    d.className = "cg-b " + rol + (extra ? " " + extra : "");
    if (rol === "bot") d.innerHTML = opmaak(tekst); else d.textContent = tekst;
    log.appendChild(d); log.scrollTop = log.scrollHeight; return d;
  }

  function snelknoppen() {
    const w = document.createElement("div"); w.className = "cg-snel";
    T.snel.forEach(s => { const b = document.createElement("button"); b.type = "button"; b.textContent = s; b.onclick = () => { w.remove(); verstuur(s); }; w.appendChild(b); });
    log.appendChild(w);
  }

  function teken() {
    log.innerHTML = "";
    bel("bot", T.hallo);
    berichten.forEach(b => bel(b.role === "user" ? "jij" : "bot", b.content));
    if (klaar) bel("bot", T.klaar, "ok");
    if (!berichten.length) snelknoppen();
  }

  async function verstuur(tekst) {
    tekst = (tekst || "").trim();
    if (!tekst || bezig) return;
    bezig = true; knop.disabled = true;
    log.querySelectorAll(".cg-snel").forEach(x => x.remove());
    berichten.push({ role: "user", content: tekst.slice(0, 2000) }); bewaar();
    bel("jij", tekst);
    const wacht = bel("bot", T.denkt, "denkt");
    try {
      const r = await fetch("/api/chat", { method: "POST", headers: { "content-type": "application/json" },
        body: JSON.stringify({ berichten, taal: TAAL, pagina: location.pathname }) });
      const d = await r.json().catch(() => ({}));
      wacht.remove();
      if (!r.ok || !d.antwoord) throw new Error(d.fout || r.status);
      berichten.push({ role: "assistant", content: d.antwoord });
      bel("bot", d.antwoord);
      if (d.doorgestuurd && !klaar) { klaar = true; bel("bot", T.klaar, "ok"); if (window.goatcounter && goatcounter.count) goatcounter.count({ path: "chat-aanvraag", event: true }); }
      bewaar();
    } catch (_) {
      wacht.remove();
      berichten.pop(); bewaar();
      bel("bot", T.fout);
      veld.value = tekst;
    } finally { bezig = false; knop.disabled = false; veld.focus(); }
  }

  function bouw() {
    const st = document.createElement("style"); st.textContent = css; document.head.appendChild(st);
    fab = document.createElement("button");
    fab.type = "button"; fab.className = "cg-fab"; fab.setAttribute("aria-haspopup", "dialog");
    fab.innerHTML = `<span class="cg-stip" aria-hidden="true"></span><span class="cg-lang">${esc(T.knop)}</span><span class="cg-kort">${esc(T.kort)}</span>`;
    fab.onclick = open;
    document.body.appendChild(fab);

    paneel = document.createElement("div");
    paneel.className = "cg-paneel"; paneel.hidden = true;
    paneel.setAttribute("role", "dialog"); paneel.setAttribute("aria-label", T.titel);
    paneel.innerHTML = `<div class="cg-kop"><img src="img/logo-icon-96.png" alt=""><div><b>${esc(T.titel)}</b><small>${esc(T.sub)}</small></div>
<div class="cg-acties"><button type="button" data-nieuw title="${esc(T.opnieuw)}" aria-label="${esc(T.opnieuw)}">↺</button><button type="button" data-sluit aria-label="${esc(T.sluit)}">✕</button></div></div>
<div class="cg-log" role="log" aria-live="polite"></div>
<form class="cg-form"><textarea rows="1" maxlength="2000" aria-label="${esc(T.plek)}" placeholder="${esc(T.plek)}"></textarea><button type="submit">${esc(T.stuur)}</button></form>
<p class="cg-noot">${esc(T.noot)} <a href="${TAAL === "nl" ? "privacy.html" : "privacy.html"}">${esc(T.privacy)}</a></p>`;
    document.body.appendChild(paneel);
    log = paneel.querySelector(".cg-log"); veld = paneel.querySelector("textarea"); knop = paneel.querySelector(".cg-form button");
    paneel.querySelector("[data-sluit]").onclick = sluit;
    paneel.querySelector("[data-nieuw]").onclick = () => { berichten = []; klaar = false; bewaar(); teken(); veld.focus(); };
    paneel.querySelector("form").onsubmit = ev => { ev.preventDefault(); const t = veld.value; veld.value = ""; veld.style.height = ""; verstuur(t); };
    veld.addEventListener("keydown", ev => { if (ev.key === "Enter" && !ev.shiftKey) { ev.preventDefault(); paneel.querySelector("form").requestSubmit(); } });
    veld.addEventListener("input", () => { veld.style.height = "auto"; veld.style.height = Math.min(veld.scrollHeight, 120) + "px"; });
    paneel.addEventListener("keydown", ev => { if (ev.key === "Escape") sluit(); });
    teken();

    document.querySelectorAll("[data-chat-blok]").forEach(el => { el.hidden = false; });
    document.querySelectorAll("[data-chat-open]").forEach(el => el.addEventListener("click", ev => { ev.preventDefault(); open(); }));
  }

  function open() { paneel.hidden = false; fab.hidden = true; log.scrollTop = log.scrollHeight; veld.focus(); if (window.goatcounter && goatcounter.count) goatcounter.count({ path: "chat-geopend", event: true }); }
  function sluit() { paneel.hidden = true; fab.hidden = false; fab.focus(); }

  fetch("/api/chat", { headers: { accept: "application/json" } })
    .then(r => (r.ok ? r.json() : null))
    .then(d => { if (d && d.actief) bouw(); })
    .catch(() => {});
})();
