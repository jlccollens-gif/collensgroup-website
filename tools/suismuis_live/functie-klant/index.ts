// Suismuis Home: klantaccounts (eigen klantenbestand, los van Supabase Auth) en de interieuradviseur (chat).
// Geheimen alleen in Supabase-secrets: ANTHROPIC_API_KEY (chat), BREVO_API_KEY + SUISMUIS_AFZENDER (mail, optioneel).
// Instelbaar: SUISMUIS_CHAT_MODEL, SUISMUIS_CHAT_DAGLIMIET. Gebouwd door Collens Group.
import { createClient } from "npm:@supabase/supabase-js@2";

const env = (k: string, d = "") => Deno.env.get(k) || d;
const sb = createClient(env("SUPABASE_URL"), env("SUPABASE_SERVICE_ROLE_KEY"), { auth: { persistSession: false } });
const KIM = env("SUISMUIS_KIM_EMAIL", "suisterkim@gmail.com");
const AFZENDER = env("SUISMUIS_AFZENDER", "info@collensgroup.com");
const IBAN = env("SUISMUIS_IBAN", "NL22 BUNQ 2207 4744 53");
const CATALOGUS_URL = "https://suismuishome.com/assets/catalogus.json";

const enc = new TextEncoder();
const hex = (b: ArrayBuffer) => [...new Uint8Array(b)].map((x) => x.toString(16).padStart(2, "0")).join("");
const sha = async (s: string) => hex(await crypto.subtle.digest("SHA-256", enc.encode(s)));
const willekeurig = (n = 24) => hex(crypto.getRandomValues(new Uint8Array(n)).buffer);
async function pbkdf2(pw: string, salt: string) {
  const k = await crypto.subtle.importKey("raw", enc.encode(pw), "PBKDF2", false, ["deriveBits"]);
  return hex(await crypto.subtle.deriveBits({ name: "PBKDF2", hash: "SHA-256", salt: enc.encode(salt), iterations: 120000 }, k, 256));
}
function gelijk(a: string, b: string) { if (!a || !b || a.length !== b.length) return false; let r = 0; for (let i = 0; i < a.length; i++) r |= a.charCodeAt(i) ^ b.charCodeAt(i); return r === 0; }
const tekst = (v: unknown, max = 120) => (typeof v === "string" ? v.replace(/[\u0000-\u001f]/g, " ").trim().slice(0, max) : "");
const esc = (s: unknown) => String(s ?? "").replace(/[&<>"']/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]!));
const geldigMail = (s: string) => /^[^\s@<>]+@[^\s@<>]+\.[^\s@<>]{2,}$/.test(s);
function antwoord(data: unknown, status = 200) {
  return new Response(JSON.stringify(data), { status, headers: {
    "Content-Type": "application/json", "Access-Control-Allow-Origin": "*",
    "Access-Control-Allow-Headers": "content-type", "Access-Control-Allow-Methods": "POST, OPTIONS", "Cache-Control": "no-store",
  } });
}
const STAPPEN: Record<string, string> = { open: "Nog niet betaald", wacht_op_betaling: "Wacht op je overschrijving", betaald: "Betaald", besteld: "In behandeling", verzonden: "Verzonden", geleverd: "Geleverd", geannuleerd: "Geannuleerd", terugbetaald: "Terugbetaald" };
function publiek(o: any) {
  return { nr: o.nr, created_at: o.created_at, status: o.status, status_tekst: STAPPEN[o.status], regels: o.regels, subtotaal: o.subtotaal, verzending: o.verzending, cadeau: o.cadeau, totaal: o.totaal,
    betaalmethode: o.betaalmethode, vervoerder: o.vervoerder, track_trace: o.track_trace, iban: o.status === "wacht_op_betaling" ? IBAN : undefined };
}
function omlijst(titel: string, inhoud: string) {
  return `<!doctype html><html lang="nl"><body style="margin:0;background:#F3EEE7;font-family:Georgia,serif;color:#3E3229">
<div style="max-width:600px;margin:0 auto;padding:28px 16px"><div style="background:#7A6553;color:#F7F1E8;text-align:center;padding:22px 16px;letter-spacing:.32em;font-size:20px">SUISMUIS<span style="display:block;font-size:11px;letter-spacing:.5em;margin-top:4px">HOME</span></div>
<div style="background:#fff;padding:30px 26px;font-family:Arial,Helvetica,sans-serif;font-size:15px;line-height:1.6"><h1 style="font-family:Georgia,serif;font-weight:400;font-size:26px;margin:0 0 14px">${titel}</h1>${inhoud}</div>
<p style="font-family:Arial,sans-serif;font-size:12px;color:#7A6553;text-align:center;margin:16px 0">Suismuis Home · Warme, tijdloze woonaccessoires</p></div></body></html>`;
}
const knop = (href: string, t: string) => `<p style="margin:22px 0"><a href="${esc(href)}" style="background:#7A6553;color:#fff;text-decoration:none;padding:12px 22px;display:inline-block">${t}</a></p>`;
async function mail(naar: string, onderwerp: string, html: string) {
  const sleutel = env("BREVO_API_KEY");
  if (!sleutel) return "geen-mailsleutel";
  const r = await fetch("https://api.brevo.com/v3/smtp/email", { method: "POST",
    headers: { "api-key": sleutel, "content-type": "application/json", accept: "application/json" },
    body: JSON.stringify({ sender: { name: "Suismuis Home", email: AFZENDER }, to: [{ email: naar }], replyTo: { email: KIM, name: "Suismuis Home" }, subject: onderwerp, htmlContent: html }) });
  return r.ok ? "verstuurd" : "fout " + r.status;
}
let cache: { t: number; d: any } | null = null;
async function catalogus() {
  if (cache && Date.now() - cache.t < 600e3) return cache.d;
  const r = await fetch(CATALOGUS_URL + "?t=" + Math.floor(Date.now() / 600e3));
  const d = await r.json();
  cache = { t: Date.now(), d };
  return d;
}
async function uitverkocht(): Promise<number[]> {
  const { data } = await sb.from("suismuis_voorraad").select("nr").eq("status", "uitverkocht");
  return (data || []).map((r: any) => Number(r.nr));
}

// ---------- klantaccounts ----------
const SITES = /^https:\/\/((www\.)?suismuishome\.com|collensgroup\.com\/concept\/suismuis)$/;
const eigenSite = (v: unknown) => { const u = tekst(v, 200).replace(/\/$/, ""); return SITES.test(u) ? u : "https://suismuishome.com"; };
async function teVaak(soort: string, sleutel: string, max: number, minuten: number) {
  const { count } = await sb.from("suismuis_pogingen").select("id", { count: "exact", head: true }).eq("soort", soort).eq("sleutel", sleutel).gte("created_at", new Date(Date.now() - minuten * 60e3).toISOString());
  await sb.from("suismuis_pogingen").insert({ soort, sleutel });
  return (count ?? 0) >= max;
}
const ipVan = async (req: Request) => (await sha("suis:" + ((req.headers.get("x-forwarded-for") || "").split(",")[0].trim() || "?"))).slice(0, 32);
async function nieuweKlantSessie(id: string) {
  const s = willekeurig(24);
  await sb.from("suismuis_klant_sessies").delete().lt("verloopt", new Date().toISOString());
  await sb.from("suismuis_klant_sessies").insert({ token_hash: await sha(s), klant_id: id, verloopt: new Date(Date.now() + 60 * 864e5).toISOString() });
  return s;
}
async function klantVan(token: unknown) {
  if (typeof token !== "string" || token.length < 20) return null;
  const { data } = await sb.from("suismuis_klant_sessies").select("klant_id,verloopt").eq("token_hash", await sha(token)).maybeSingle();
  if (!data || new Date(data.verloopt) < new Date()) return null;
  const { data: k } = await sb.from("suismuis_klanten").select("id,email,naam,tel,adres,nieuwsbrief,created_at").eq("id", data.klant_id).maybeSingle();
  return k;
}
const pwHash = async (pw: string) => { const salt = willekeurig(12); return salt + ":" + await pbkdf2(pw, salt); };
const pwOk = async (pw: unknown, opgeslagen: string) => { const [salt, h] = (opgeslagen || ":").split(":"); return gelijk(h, await pbkdf2(typeof pw === "string" ? pw : "", salt)); };
function schoonAdres(a: any) {
  a = a || {};
  return { straat: tekst(a.straat), huisnummer: tekst(a.huisnummer, 20), postcode: tekst(a.postcode, 12).toUpperCase(), plaats: tekst(a.plaats, 80), land: ["Nederland", "België"].includes(a.land) ? a.land : "Nederland" };
}

// ---------- interieuradvies (chat) ----------
let assort: { t: number; lijst: any[] } | null = null;
async function assortiment() {
  if (assort && Date.now() - assort.t < 600e3) return assort.lijst;
  const r = await fetch("https://suismuishome.com/assets/scouting.js?t=" + Math.floor(Date.now() / 600e3));
  const t = await r.text();
  const alle = JSON.parse(t.slice(t.indexOf("["), t.lastIndexOf("]") + 1)) as any[];
  const cat = await catalogus();
  const weg = new Set(await uitverkocht());
  const lijst = alle.filter((p) => cat.producten[p.id] && !weg.has(Number(p.nr))).map((p) => ({ id: p.id, n: p.n, s: p.s, p: p.p, m: p.m || "", d: p.d || "", v: (p.var || []).map((v: any) => v.n).join(", "), t: p.t || "", lt: p.lt || "", img: p.u?.[0] || (p.img ? "img/" + String(p.img).replace(/^img\//, "") + ".jpg" : "") }));
  // producten die Kim zelf in haar bestelbalie toevoegde
  const { data: eigen } = await sb.from("suismuis_producten").select("nr,data").eq("actief", true);
  for (const r of eigen || []) { const p = r.data || {}; if (p.id && !weg.has(Number(r.nr))) lijst.push({ id: p.id, n: p.n, s: p.s, p: p.p, m: p.m || "", d: p.d || "", v: (p.var || []).map((v: any) => v.n).join(", "), t: p.t || "", lt: p.lt || "", img: p.u?.[0] || "" }); }
  assort = { t: Date.now(), lijst };
  return lijst;
}
async function chatAntwoord(vraag: string, geschiedenis: { rol: string; t: string }[], product: string) {
  const key = env("ANTHROPIC_API_KEY");
  if (!key) return null;
  const lijst = await assortiment();
  const regels = lijst.map((p) => `${p.id} | ${p.n} | ${p.s} | € ${Number(p.p).toFixed(2).replace(".", ",")} | ${p.m.slice(0, 110)} | ${p.d.slice(0, 110)}${p.v ? " | uitvoeringen: " + p.v.slice(0, 120) : ""} | levertijd ${p.lt}`).join("\n");
  const huidig = product ? lijst.find((p) => p.id === product) : null;
  const system = `Je bent de interieuradviseur van Suismuis Home, een Nederlandse webshop voor warme, tijdloze woonaccessoires en meubels in de stijl "Organic Luxury" (rustig, naturel, crème, zand, taupe, mokka, linnen, keramiek, rotan, travertin, hout). Je helpt bezoekers hun huis in te richten en het juiste product te kiezen.
Regels:
- Schrijf in het Nederlands (of in de taal van de klant), warm, kort en concreet: maximaal 5 zinnen of een kort lijstje. Geen opsmuk, geen emoji's.
- Je bent een AI-assistent; zeg dat eerlijk als iemand ernaar vraagt.
- Raad ALLEEN producten aan uit de lijst hieronder. Verzin nooit producten, prijzen, maten, materialen, kortingen, voorraad of levertijden. Staat iets niet in de lijst, zeg dat eerlijk.
- Geef bij een advies 1 tot 3 passende producten en zeg in één zin waarom ze passen (kleur, materiaal, ruimte, maat). Stel één vervolgvraag als dat helpt (bijv. welke ruimte, welke kleuren, welk budget).
- Algemeen stijladvies (kleuren combineren, styling, verhoudingen, licht) mag je ook geven.
- Vaste informatie: gratis verzending vanaf € 75, anders € 5,95. 14 dagen bedenktijd. Betalen met PayPal, creditcard of bankoverschrijving. Voor vragen over een bestelling, retour of klacht: verwijs naar de pagina Klantenservice (contactformulier) of "Bestelling volgen"; je kunt zelf geen bestellingen inzien of wijzigen.
- Vraag nooit om persoonsgegevens, wachtwoorden of betaalgegevens.
${huidig ? `\nDe klant bekijkt nu dit product: ${huidig.id} | ${huidig.n} | € ${huidig.p} | ${huidig.m} | ${huidig.d} | ${huidig.t.slice(0, 300)}\n` : ""}
Assortiment (id | naam | subcategorie | prijs | materiaal | afmetingen | uitvoeringen | levertijd):
${regels}

Antwoord ALLEEN met JSON: {"antwoord": "...", "producten": ["id", ...]} met maximaal 3 ids uit de lijst (of []).`;
  const msgs: { role: string; content: string }[] = [];
  for (const m of geschiedenis.slice(-10)) {
    const role = m.rol === "klant" ? "user" : "assistant";
    const t = tekst(m.t, 1500); if (!t) continue;
    const last = msgs[msgs.length - 1];
    if (last && last.role === role) last.content += "\n" + t; else msgs.push({ role, content: role === "assistant" ? JSON.stringify({ antwoord: t, producten: [] }) : t });
  }
  while (msgs.length && msgs[0].role !== "user") msgs.shift();
  if (msgs.length && msgs[msgs.length - 1].role === "user") msgs[msgs.length - 1].content += "\n" + vraag; else msgs.push({ role: "user", content: vraag });
  const r = await fetch("https://api.anthropic.com/v1/messages", { method: "POST",
    headers: { "x-api-key": key, "anthropic-version": "2023-06-01", "content-type": "application/json" },
    body: JSON.stringify({ model: env("SUISMUIS_CHAT_MODEL", "claude-haiku-4-5-20251001"), max_tokens: 700, system: [{ type: "text", text: system, cache_control: { type: "ephemeral" } }], messages: [...msgs, { role: "assistant", content: "{" }] }) });
  if (!r.ok) { console.log("chat", r.status, (await r.text()).slice(0, 300)); return null; }
  const j = await r.json();
  const raw = "{" + (j?.content?.[0]?.text ?? "");
  let uit: any = null;
  try { uit = JSON.parse(raw.match(/\{[\s\S]*\}/)?.[0] || ""); } catch { uit = null; }
  if (!uit || typeof uit.antwoord !== "string") { const m = raw.match(/"antwoord"\s*:\s*"((?:[^"\\]|\\.)*)"/); if (!m) return null; try { uit = { antwoord: JSON.parse('"' + m[1] + '"'), producten: [] }; } catch { return null; } }
  const ids = (Array.isArray(uit.producten) ? uit.producten : []).map(String).slice(0, 3);
  const prods = ids.map((id: string) => lijst.find((p) => p.id === id)).filter(Boolean).map((p: any) => ({ id: p.id, n: p.n, p: p.p, img: p.img }));
  return { antwoord: uit.antwoord.trim().slice(0, 2000), producten: prods };
}


Deno.serve(async (req) => {
  if (req.method === "OPTIONS") return antwoord({});
  if (req.method !== "POST") return antwoord({ fout: "Alleen POST" }, 405);
  let b: any; try { b = await req.json(); } catch { return antwoord({ fout: "Ongeldige aanvraag" }, 400); }
  const actie = b?.actie;
  // ---------- klantaccount ----------
  if (actie === "account_registreer") {
    const email = tekst(b.email, 160).toLowerCase(), pw = typeof b.wachtwoord === "string" ? b.wachtwoord : "", naam = tekst(b.naam, 100);
    if (!geldigMail(email)) return antwoord({ fout: "Vul een geldig e-mailadres in." }, 400);
    if (pw.length < 8 || pw.length > 200) return antwoord({ fout: "Kies een wachtwoord van minstens 8 tekens." }, 400);
    if (!b.akkoord) return antwoord({ fout: "Ga akkoord met de privacyverklaring om een account aan te maken." }, 400);
    if (await teVaak("registreer", await ipVan(req), 8, 60)) return antwoord({ fout: "Te veel pogingen. Probeer het over een uur opnieuw." }, 429);
    const { data: bestaat } = await sb.from("suismuis_klanten").select("id").eq("email", email).maybeSingle();
    if (bestaat) return antwoord({ fout: "Er bestaat al een account met dit e-mailadres. Log in of kies \"Wachtwoord vergeten\"." }, 409);
    const { data: k, error } = await sb.from("suismuis_klanten").insert({ email, naam, wachtwoord_hash: await pwHash(pw), nieuwsbrief: !!b.nieuwsbrief, laatst_ingelogd: new Date().toISOString() }).select("id").single();
    if (error || !k) return antwoord({ fout: "Je account kon niet worden aangemaakt. Probeer het opnieuw." }, 500);
    await mail(email, "Welkom bij Suismuis Home", omlijst("Welkom bij Suismuis Home", `<p>Hoi ${esc(naam.split(" ")[0] || "")},</p><p>Je account is aangemaakt. Je kunt nu sneller afrekenen en je bestellingen terugzien.</p>${knop(eigenSite(b.site) + "/account.html", "Naar mijn account")}<p style="font-size:13px;color:#7A6553">Heb jij dit account niet aangemaakt? Beantwoord dan deze mail.</p>`));
    return antwoord({ sessie: await nieuweKlantSessie(k.id) });
  }
  if (actie === "account_login") {
    const email = tekst(b.email, 160).toLowerCase();
    if (await teVaak("login", email, 10, 15)) return antwoord({ fout: "Te veel pogingen. Probeer het over 15 minuten opnieuw." }, 429);
    const { data: k } = await sb.from("suismuis_klanten").select("id,wachtwoord_hash").eq("email", email).maybeSingle();
    await new Promise((r) => setTimeout(r, 300));
    if (!k || !(await pwOk(b.wachtwoord, k.wachtwoord_hash))) return antwoord({ fout: "Onjuist e-mailadres of wachtwoord." }, 403);
    await sb.from("suismuis_klanten").update({ laatst_ingelogd: new Date().toISOString() }).eq("id", k.id);
    return antwoord({ sessie: await nieuweKlantSessie(k.id) });
  }
  if (actie === "account_vergeten") {
    const email = tekst(b.email, 160).toLowerCase();
    if (!geldigMail(email)) return antwoord({ fout: "Vul een geldig e-mailadres in." }, 400);
    if (await teVaak("vergeten", email, 3, 60)) return antwoord({ ok: true });
    const { data: k } = await sb.from("suismuis_klanten").select("id,naam").eq("email", email).maybeSingle();
    if (k) {
      const tok = willekeurig(24);
      await sb.from("suismuis_klant_reset").delete().eq("klant_id", k.id);
      await sb.from("suismuis_klant_reset").insert({ token_hash: await sha(tok), klant_id: k.id, verloopt: new Date(Date.now() + 3600e3).toISOString() });
      await mail(email, "Nieuw wachtwoord voor je Suismuis-account", omlijst("Kies een nieuw wachtwoord", `<p>Hoi ${esc(String(k.naam || "").split(" ")[0])},</p><p>Je vroeg een nieuw wachtwoord aan. Deze link werkt één uur.</p>${knop(eigenSite(b.site) + "/account.html?reset=" + tok, "Nieuw wachtwoord kiezen")}<p style="font-size:13px;color:#7A6553">Heb je dit niet gevraagd? Dan kun je deze mail negeren.</p>`));
    }
    return antwoord({ ok: true });
  }
  if (actie === "account_reset") {
    const pw = typeof b.wachtwoord === "string" ? b.wachtwoord : "";
    if (pw.length < 8 || pw.length > 200) return antwoord({ fout: "Kies een wachtwoord van minstens 8 tekens." }, 400);
    const { data: r } = await sb.from("suismuis_klant_reset").select("klant_id,verloopt").eq("token_hash", await sha(tekst(b.token, 80))).maybeSingle();
    if (!r || new Date(r.verloopt) < new Date()) return antwoord({ fout: "Deze link is verlopen of al gebruikt. Vraag een nieuwe aan." }, 403);
    await sb.from("suismuis_klanten").update({ wachtwoord_hash: await pwHash(pw) }).eq("id", r.klant_id);
    await sb.from("suismuis_klant_reset").delete().eq("klant_id", r.klant_id);
    await sb.from("suismuis_klant_sessies").delete().eq("klant_id", r.klant_id);
    return antwoord({ sessie: await nieuweKlantSessie(r.klant_id) });
  }
  if (["account_ik", "account_opslaan", "account_uit", "account_verwijder", "account_wachtwoord"].includes(actie)) {
    const k = await klantVan(b.ksessie);
    if (!k) return antwoord({ fout: "Log opnieuw in.", uitgelogd: true }, 401);
    if (actie === "account_uit") { await sb.from("suismuis_klant_sessies").delete().eq("token_hash", await sha(b.ksessie)); return antwoord({ ok: true }); }
    if (actie === "account_ik") {
      const { data: orders } = await sb.from("suismuis_orders").select("*").eq("klant_id", k.id).neq("status", "open").order("created_at", { ascending: false }).limit(50);
      return antwoord({ klant: { email: k.email, naam: k.naam, tel: k.tel, adres: k.adres, nieuwsbrief: k.nieuwsbrief }, orders: (orders || []).map(publiek) });
    }
    if (actie === "account_opslaan") {
      await sb.from("suismuis_klanten").update({ naam: tekst(b.naam, 100), tel: tekst(b.tel, 40), adres: schoonAdres(b.adres), nieuwsbrief: !!b.nieuwsbrief }).eq("id", k.id);
      return antwoord({ ok: true });
    }
    const { data: kk } = await sb.from("suismuis_klanten").select("wachtwoord_hash").eq("id", k.id).single();
    if (!(await pwOk(b.wachtwoord, kk?.wachtwoord_hash || ""))) return antwoord({ fout: "Je huidige wachtwoord klopt niet." }, 403);
    if (actie === "account_wachtwoord") {
      const nw = typeof b.nieuw === "string" ? b.nieuw : "";
      if (nw.length < 8 || nw.length > 200) return antwoord({ fout: "Kies een nieuw wachtwoord van minstens 8 tekens." }, 400);
      await sb.from("suismuis_klanten").update({ wachtwoord_hash: await pwHash(nw) }).eq("id", k.id);
      await sb.from("suismuis_klant_sessies").delete().eq("klant_id", k.id);
      return antwoord({ sessie: await nieuweKlantSessie(k.id) });
    }
    // account_verwijder: account en inloggegevens weg; bestellingen blijven (bewaarplicht), zonder koppeling
    await sb.from("suismuis_orders").update({ klant_id: null }).eq("klant_id", k.id);
    await sb.from("suismuis_klanten").delete().eq("id", k.id);
    return antwoord({ ok: true });
  }

  // ---------- interieuradvies ----------
  if (actie === "chat") {
    const vraag = tekst(b.bericht, 1000);
    const bezoeker = tekst(b.bezoeker, 64).replace(/[^a-z0-9-]/gi, "");
    if (!vraag) return antwoord({ fout: "Typ je vraag." }, 400);
    if (bezoeker.length < 8) return antwoord({ fout: "Ververs de pagina en probeer het opnieuw." }, 400);
    const ip = await ipVan(req);
    const dag = new Date(Date.now() - 864e5).toISOString();
    const { count: perBezoeker } = await sb.from("suismuis_chat").select("id", { count: "exact", head: true }).eq("bezoeker", bezoeker).gte("created_at", dag);
    if ((perBezoeker ?? 0) >= 30) return antwoord({ fout: "Je hebt vandaag veel vragen gesteld. Morgen helpen we je graag verder, of stuur ons een bericht via Klantenservice." }, 429);
    if (await teVaak("chat", ip, 60, 1440)) return antwoord({ fout: "Je hebt vandaag veel vragen gesteld. Stuur ons gerust een bericht via Klantenservice." }, 429);
    const { count: totaal } = await sb.from("suismuis_chat").select("id", { count: "exact", head: true }).gte("created_at", dag);
    if ((totaal ?? 0) >= Number(env("SUISMUIS_CHAT_DAGLIMIET", "1500"))) return antwoord({ fout: "De adviseur is even niet beschikbaar. Stuur ons een bericht via Klantenservice." }, 503);
    let uit = null;
    try { uit = await chatAntwoord(vraag, Array.isArray(b.geschiedenis) ? b.geschiedenis : [], tekst(b.product, 80)); } catch (e) { console.log("chat fout", String(e)); }
    if (!uit) return antwoord({ fout: "De adviseur is even niet beschikbaar. Probeer het zo opnieuw." }, 503);
    await sb.from("suismuis_chat").insert({ bezoeker, vraag, antwoord: uit.antwoord, producten: uit.producten.map((p: any) => p.id) });
    return antwoord(uit);
  }


  // bestelling achteraf aan het account koppelen (de klant heeft het ordernummer + de geheime ordertoken)
  if (actie === "account_koppel") {
    const k = await klantVan(b.ksessie);
    if (!k) return antwoord({ fout: "Log opnieuw in." }, 401);
    const { data: o } = await sb.from("suismuis_orders").select("nr,status_token_hash,klant_id,klant_naam,klant_tel,adres").eq("nr", tekst(b.nr, 24)).maybeSingle();
    if (!o || !gelijk(o.status_token_hash, await sha(tekst(b.token, 64)))) return antwoord({ fout: "Bestelling niet gevonden." }, 404);
    if (!o.klant_id) await sb.from("suismuis_orders").update({ klant_id: k.id }).eq("nr", o.nr);
    if (b.bewaar_adres) await sb.from("suismuis_klanten").update({ naam: o.klant_naam, tel: o.klant_tel, adres: o.adres }).eq("id", k.id);
    return antwoord({ ok: true });
  }
  return antwoord({ fout: "Onbekende actie" }, 400);
});
