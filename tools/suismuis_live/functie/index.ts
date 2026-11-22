// Suismuis Home: bestellingen, betalingen (PayPal-omgeving: creditcard en PayPal) en beheer. Gebouwd door Collens Group.
// Geheimen staan alleen in de Supabase-secrets: SUISMUIS_PAYPAL_CLIENT_ID, SUISMUIS_PAYPAL_SECRET, SUISMUIS_PAYPAL_ENV (live|sandbox),
// SUISMUIS_SITE, SUISMUIS_KIM_EMAIL, SUISMUIS_SETUPCODE; optioneel BREVO_API_KEY, SUISMUIS_AFZENDER.
import { createClient } from "npm:@supabase/supabase-js@2";

const env = (k: string, d = "") => Deno.env.get(k) || d;
const sb = createClient(env("SUPABASE_URL"), env("SUPABASE_SERVICE_ROLE_KEY"), { auth: { persistSession: false } });
const CATALOGUS_URL = env("SUISMUIS_CATALOGUS", "https://collensgroup.com/concept/suismuis/assets/catalogus.json");
const IBAN = env("SUISMUIS_IBAN", "NL22 BUNQ 2207 4744 53");
const KIM = env("SUISMUIS_KIM_EMAIL", "suisterkim@gmail.com");
const AFZENDER = env("SUISMUIS_AFZENDER", "info@collensgroup.com");
const PP_LIVE = env("SUISMUIS_PAYPAL_ENV", "sandbox") === "live";
const PP_API = PP_LIVE ? "https://api-m.paypal.com" : "https://api-m.sandbox.paypal.com";
const PP_ID = env("SUISMUIS_PAYPAL_CLIENT_ID"), PP_GEHEIM = env("SUISMUIS_PAYPAL_SECRET");
const ppAan = () => !!(PP_ID && PP_GEHEIM);

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
const rond = (x: number) => Math.round(x * 100) / 100;
const bedrag = (x: number) => rond(x).toFixed(2);
const euro = (x: number) => "€ " + rond(x).toFixed(2).replace(".", ",");
const esc = (s: unknown) => String(s ?? "").replace(/[&<>"']/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]!));
const geldigMail = (s: string) => /^[^\s@<>]+@[^\s@<>]+\.[^\s@<>]{2,}$/.test(s);

function antwoord(data: unknown, status = 200) {
  return new Response(JSON.stringify(data), { status, headers: {
    "Content-Type": "application/json", "Access-Control-Allow-Origin": "*",
    "Access-Control-Allow-Headers": "content-type", "Access-Control-Allow-Methods": "POST, OPTIONS", "Cache-Control": "no-store",
  } });
}

// ---------- catalogus (prijzen komen altijd van de server) ----------
let cache: { t: number; d: any } | null = null;
async function catalogus() {
  if (cache && Date.now() - cache.t < 300e3) return cache.d;
  const r = await fetch(CATALOGUS_URL + "?t=" + Math.floor(Date.now() / 300e3), { headers: { accept: "application/json" } });
  if (!r.ok) { if (cache) return cache.d; throw new Error("catalogus " + r.status); }
  const t = await r.text();
  cache = { t: Date.now(), d: CATALOGUS_URL.split("?")[0].endsWith(".js") ? vanScouting(t) : JSON.parse(t) };
  return cache.d;
}
// leest producten en verzendkosten rechtstreeks uit assets/scouting.js van de eigen website (één bron voor prijzen)
function vanScouting(t: string) {
  const lijst = JSON.parse(t.slice(t.indexOf("["), t.lastIndexOf("]") + 1)) as any[];
  const k = t.match(/SUIS_KOSTEN\s*=\s*(\{[^}]*\})/);
  const kosten = k ? JSON.parse(k[1]) : { gratis: 75, verzend: 5.95, cadeau: 3.95 };
  const producten: Record<string, any> = {};
  for (const p of lijst) producten[p.id] = { n: p.n, p: Math.round(Number(p.p) * 100) / 100, nr: p.nr, maten: (p.maten || []).map((m: string) => m + " cm"), var: (p.var || []).map((v: any) => v.n), lt: p.lt || "" };
  return { gratis: Number(kosten.gratis), verzend: Number(kosten.verzend), cadeau: Number(kosten.cadeau), producten };
}

// ---------- PayPal ----------
let ppToken: { t: number; v: string } | null = null;
async function pp(pad: string, init: RequestInit = {}) {
  if (!ppToken || Date.now() > ppToken.t) {
    const r = await fetch(PP_API + "/v1/oauth2/token", { method: "POST", body: "grant_type=client_credentials",
      headers: { Authorization: "Basic " + btoa(PP_ID + ":" + PP_GEHEIM), "Content-Type": "application/x-www-form-urlencoded" } });
    const j = await r.json();
    if (!r.ok) throw new Error("PayPal-token " + r.status + " " + (j.error_description || ""));
    ppToken = { v: j.access_token, t: Date.now() + (Number(j.expires_in || 3000) - 120) * 1000 };
  }
  const r = await fetch(PP_API + pad, { ...init, headers: { Authorization: "Bearer " + ppToken.v, "Content-Type": "application/json", Prefer: "return=representation", ...(init.headers || {}) } });
  const j = await r.json().catch(() => ({}));
  return { ok: r.ok, status: r.status, j };
}

// ---------- mail (Brevo) ----------
const STAPPEN: Record<string, string> = { open: "Nog niet betaald", wacht_op_betaling: "Wacht op je overschrijving", betaald: "Betaald", besteld: "In behandeling", verzonden: "Verzonden", geleverd: "Geleverd", geannuleerd: "Geannuleerd", terugbetaald: "Terugbetaald" };
function omlijst(titel: string, inhoud: string) {
  return `<!doctype html><html lang="nl"><body style="margin:0;background:#F3EEE7;font-family:Georgia,serif;color:#3E3229">
<div style="max-width:600px;margin:0 auto;padding:28px 16px"><div style="background:#7A6553;color:#F7F1E8;text-align:center;padding:22px 16px;letter-spacing:.32em;font-size:20px">SUISMUIS<span style="display:block;font-size:11px;letter-spacing:.5em;margin-top:4px">HOME</span></div>
<div style="background:#fff;padding:30px 26px;font-family:Arial,Helvetica,sans-serif;font-size:15px;line-height:1.6"><h1 style="font-family:Georgia,serif;font-weight:400;font-size:26px;margin:0 0 14px">${titel}</h1>${inhoud}</div>
<p style="font-family:Arial,sans-serif;font-size:12px;color:#7A6553;text-align:center;margin:16px 0">Suismuis Home · Warme, tijdloze woonaccessoires</p></div></body></html>`;
}
function tabel(o: any) {
  const r = (a: string, b: string, vet = false) => `<tr><td style="padding:6px 0;border-bottom:1px solid #EFE7DC${vet ? ";font-weight:bold" : ""}">${a}</td><td style="padding:6px 0;border-bottom:1px solid #EFE7DC;text-align:right${vet ? ";font-weight:bold" : ""}">${b}</td></tr>`;
  return `<table style="width:100%;border-collapse:collapse;margin:14px 0">${(o.regels as any[]).map((x) => r(`${x.aantal} × ${esc(x.naam)}${x.maat ? `<br><small style="color:#7A6553">Maat ${esc(x.maat)}</small>` : ""}${x.uitvoering ? `<br><small style="color:#7A6553">Uitvoering ${esc(x.uitvoering)}</small>` : ""}`, euro(x.prijs * x.aantal))).join("")}
${r("Verzending", Number(o.verzending) ? euro(Number(o.verzending)) : "Gratis")}${Number(o.cadeau) ? r("Cadeauverpakking", euro(Number(o.cadeau))) : ""}${r("Totaal", euro(Number(o.totaal)), true)}</table>`;
}
const adresHtml = (o: any) => `${esc(o.klant_naam)}<br>${esc(o.adres.straat)} ${esc(o.adres.huisnummer)}<br>${esc(o.adres.postcode)} ${esc(o.adres.plaats)}<br>${esc(o.adres.land)}`;
const knop = (href: string, t: string) => `<p style="margin:22px 0"><a href="${esc(href)}" style="background:#7A6553;color:#fff;text-decoration:none;padding:12px 22px;display:inline-block">${t}</a></p>`;

async function mail(naar: string, onderwerp: string, html: string, antwoordAan?: string) {
  const sleutel = env("BREVO_API_KEY");
  if (!sleutel) return "geen-mailsleutel";
  const r = await fetch("https://api.brevo.com/v3/smtp/email", { method: "POST",
    headers: { "api-key": sleutel, "content-type": "application/json", accept: "application/json" },
    body: JSON.stringify({ sender: { name: "Suismuis Home", email: AFZENDER }, to: [{ email: naar }], replyTo: { email: antwoordAan || KIM, name: "Suismuis Home" }, subject: onderwerp, htmlContent: html }) });
  return r.ok ? "verstuurd" : "fout " + r.status;
}
async function logMail(nr: string, soort: string, uitkomst: string) {
  const { data } = await sb.from("suismuis_orders").select("mails").eq("nr", nr).maybeSingle();
  await sb.from("suismuis_orders").update({ mails: [...((data?.mails as any[]) || []), { soort, uitkomst, tijd: new Date().toISOString() }] }).eq("nr", nr);
}
async function mailsBijBestelling(o: any, token: string) {
  const link = `${o.site || "https://collensgroup.com/concept/suismuis"}/bestelling.html?nr=${encodeURIComponent(o.nr)}&t=${token}`;
  const bank = o.status === "wacht_op_betaling";
  const klant = omlijst(bank ? "Bedankt, je bestelling staat klaar" : "Bedankt voor je bestelling",
    `<p>Hoi ${esc(o.klant_naam.split(" ")[0])},</p>` +
    (bank ? `<p>We hebben je bestelling <b>${esc(o.nr)}</b> ontvangen. Maak <b>${euro(Number(o.totaal))}</b> over naar <b>${esc(IBAN)}</b> t.n.v. Suismuis Home, onder vermelding van <b>${esc(o.nr)}</b>. Zodra je betaling binnen is, gaan we voor je aan de slag.</p>`
          : `<p>Je betaling is gelukt. We gaan je bestelling <b>${esc(o.nr)}</b> nu voor je klaarmaken. Zodra hij onderweg is, krijg je een mail met de track-and-tracecode.</p>`) +
    tabel(o) + `<p><b>Bezorgadres</b><br>${adresHtml(o)}</p>` + knop(link, "Bekijk je bestelling") +
    `<p style="font-size:13px;color:#7A6553">Je hebt 14 dagen bedenktijd na ontvangst. Vragen? Beantwoord gewoon deze mail.</p>`);
  await logMail(o.nr, "klant-bevestiging", await mail(o.klant_email, `Je bestelling ${o.nr} bij Suismuis Home`, klant));
  const kim = omlijst("Nieuwe bestelling " + esc(o.nr),
    `<p><b>${bank ? "Wacht op overschrijving" : "Betaald via " + esc(o.betaalmethode)}</b> · ${euro(Number(o.totaal))}</p>` + tabel(o) +
    `<p><b>Klant</b><br>${adresHtml(o)}<br>${esc(o.klant_email)}${o.klant_tel ? "<br>" + esc(o.klant_tel) : ""}</p>` +
    knop(`${o.site || "https://collensgroup.com/concept/suismuis"}/beheer.html`, "Open je bestelbalie"));
  await logMail(o.nr, "kim-melding", await mail(KIM, `Nieuwe bestelling ${o.nr} (${euro(Number(o.totaal))})`, kim, o.klant_email));
}

// ---------- orders ----------
async function orderMetToken(nr: unknown, token: unknown) {
  const { data } = await sb.from("suismuis_orders").select("*").eq("nr", tekst(nr, 24)).maybeSingle();
  if (!data || !gelijk(data.status_token_hash, await sha(tekst(token, 64)))) return null;
  return data;
}
function publiek(o: any) {
  return { nr: o.nr, created_at: o.created_at, status: o.status, status_tekst: STAPPEN[o.status], regels: o.regels, subtotaal: o.subtotaal, verzending: o.verzending, cadeau: o.cadeau, totaal: o.totaal,
    betaalmethode: o.betaalmethode, vervoerder: o.vervoerder, track_trace: o.track_trace, iban: o.status === "wacht_op_betaling" ? IBAN : undefined };
}
async function markeerBetaald(o: any, captureId: string, methode: string) {
  if (["betaald", "besteld", "verzonden", "geleverd"].includes(o.status)) return o;
  const nu = new Date().toISOString();
  const upd = { status: "betaald", paypal_capture_id: captureId, betaald_op: nu, betaalmethode: methode, log: [...(o.log as any[]), { status: "betaald", tijd: nu, door: "PayPal" }] };
  const { data } = await sb.from("suismuis_orders").update(upd).eq("nr", o.nr).neq("status", "betaald").select("*").maybeSingle();
  return data;
}
// controleert een PayPal-order bij PayPal zelf en verwerkt hem (gebruikt door de klant én de webhook)
async function verwerkPayPal(o: any) {
  let g = await pp(`/v2/checkout/orders/${o.paypal_order_id}`);
  if (!g.ok) return { fout: "Betaling niet gevonden bij PayPal." };
  if (g.j.status === "APPROVED") {
    g = await pp(`/v2/checkout/orders/${o.paypal_order_id}/capture`, { method: "POST", headers: { "PayPal-Request-Id": "cap-" + o.nr } });
    if (!g.ok) {
      const reden = g.j?.details?.[0]?.issue || "";
      if (reden === "INSTRUMENT_DECLINED") return { fout: "Je betaling is geweigerd door je bank. Controleer je kaartgegevens of probeer een andere kaart.", opnieuw: true };
      if (reden !== "ORDER_ALREADY_CAPTURED") return { fout: "De betaling kon niet worden afgerond. Er is niets afgeschreven." };
      g = await pp(`/v2/checkout/orders/${o.paypal_order_id}`);
    }
  }
  if (g.j.status !== "COMPLETED") return { fout: "De betaling is nog niet afgerond.", wacht: true };
  const pu = g.j.purchase_units?.[0], cap = pu?.payments?.captures?.[0];
  if (!cap || pu.custom_id !== o.nr || cap.amount?.currency_code !== "EUR" || cap.amount?.value !== bedrag(Number(o.totaal)))
    return { fout: "Het betaalde bedrag klopt niet. Neem contact met ons op." };
  if (cap.status !== "COMPLETED" && cap.status !== "PENDING") return { fout: "De betaling is niet gelukt." };
  const bron = g.j.payment_source ? Object.keys(g.j.payment_source)[0] : "paypal";
  const methode = ({ paypal: "PayPal", card: "Creditcard", ideal: "iDEAL", bancontact: "Bancontact", apple_pay: "Apple Pay", google_pay: "Google Pay" } as any)[bron] || bron;
  const voor = o.status;
  const n = await markeerBetaald(o, cap.id, methode);
  if (n && voor !== "betaald") { const tok = willekeurig(16); await sb.from("suismuis_orders").update({ status_token_hash: await sha(tok) }).eq("nr", o.nr); await mailsBijBestelling(n, tok); return { ok: true, order: n, token: tok }; }
  return { ok: true, order: n || o };
}

async function sessieOk(token: unknown) {
  if (typeof token !== "string" || token.length < 20) return false;
  const { data } = await sb.from("suismuis_sessies").select("verloopt").eq("token_hash", await sha(token)).maybeSingle();
  return !!data && new Date(data.verloopt) > new Date();
}

Deno.serve(async (req) => {
  if (req.method === "OPTIONS") return antwoord({});
  const url = new URL(req.url);
  if (req.method !== "POST") return antwoord({ fout: "Alleen POST" }, 405);

  // PayPal-webhook: de inhoud wordt niet vertrouwd; we halen de order zelf op bij PayPal.
  if (url.searchParams.get("bron") === "paypal") {
    if (!ppAan()) return antwoord({ ok: true });
    const ev = await req.json().catch(() => ({}));
    const id = ev?.resource?.supplementary_data?.related_ids?.order_id || (ev?.resource_type === "checkout-order" ? ev?.resource?.id : "");
    if (typeof id === "string" && /^[A-Z0-9]{8,40}$/.test(id)) {
      const { data: o } = await sb.from("suismuis_orders").select("*").eq("paypal_order_id", id).maybeSingle();
      if (o && o.status === "open") await verwerkPayPal(o);
    }
    return antwoord({ ok: true });
  }

  let b: any; try { b = await req.json(); } catch { return antwoord({ fout: "Ongeldige aanvraag" }, 400); }
  const actie = b?.actie;

  if (actie === "config") return antwoord({ paypal: ppAan() ? { clientId: PP_ID, live: PP_LIVE } : null, iban: IBAN });

  if (actie === "start") {
    const k = b.klant || {};
    const naam = tekst(k.naam, 100), email = tekst(k.email, 160).toLowerCase(), tel = tekst(k.tel, 40);
    const adres = { straat: tekst(k.straat), huisnummer: tekst(k.huisnummer, 20), postcode: tekst(k.postcode, 12).toUpperCase(), plaats: tekst(k.plaats, 80), land: ["Nederland", "België"].includes(k.land) ? k.land : "Nederland" };
    if (!naam || !geldigMail(email) || !adres.straat || !adres.huisnummer || !adres.postcode || !adres.plaats) return antwoord({ fout: "Vul alle verplichte velden correct in." }, 400);
    if (!b.akkoord) return antwoord({ fout: "Ga akkoord met de algemene voorwaarden om te bestellen." }, 400);
    if (!Array.isArray(b.regels) || !b.regels.length || b.regels.length > 30) return antwoord({ fout: "Je winkelmand is leeg." }, 400);
    let cat; try { cat = await catalogus(); } catch { return antwoord({ fout: "De webshop is even niet bereikbaar. Probeer het over een paar minuten opnieuw." }, 503); }
    const regels = [];
    for (const r of b.regels) {
      const x = cat.producten[r?.id]; if (!x) return antwoord({ fout: "Een product in je winkelmand is niet meer beschikbaar. Verwijder het en probeer opnieuw." }, 400);
      const maat = x.maten.length ? x.maten[0] : "";
      if (r.maat && r.maat !== maat) return antwoord({ fout: `Voor ${x.n} in maat ${tekst(r.maat, 30)} vragen we de prijs voor je op. Kies de kleinste maat of vraag de prijs aan op de productpagina.` }, 400);
      const uitvoering = x.var.length > 1 ? (x.var.includes(r.uitvoering) ? r.uitvoering : x.var[0]) : "";
      regels.push({ id: r.id, nr: x.nr, naam: x.n, maat, uitvoering, aantal: Math.max(1, Math.min(20, Math.floor(Number(r.a ?? r.aantal) || 1))), prijs: x.p });
    }
    const { count } = await sb.from("suismuis_orders").select("id", { count: "exact", head: true }).gte("created_at", new Date(Date.now() - 3600e3).toISOString());
    if ((count ?? 0) > 80) return antwoord({ fout: "Het is even erg druk. Probeer het over een paar minuten opnieuw." }, 429);
    const sub = rond(regels.reduce((s, r) => s + r.prijs * r.aantal, 0)), verz = sub >= cat.gratis ? 0 : cat.verzend, cad = b.cadeau ? cat.cadeau : 0;
    const token = willekeurig(16), d = new Date();
    const nr = "SH" + String(d.getUTCFullYear()).slice(2) + String(d.getUTCMonth() + 1).padStart(2, "0") + String(d.getUTCDate()).padStart(2, "0") + "-" + willekeurig(2).toUpperCase();
    const herkomst = tekst(b.site, 200);
    const site = /^https:\/\/[a-z0-9.-]+(\/[a-z0-9\/_-]*)?$/i.test(herkomst) ? herkomst.replace(/\/$/, "") : null;
    const rij = { nr, test: !PP_LIVE || !!b.test, klant_naam: naam, klant_email: email, klant_tel: tel, adres, regels, subtotaal: sub, verzending: verz, cadeau: cad, totaal: rond(sub + verz + cad), status_token_hash: await sha(token), site, log: [{ status: "open", tijd: d.toISOString(), door: "klant" }] };
    const { error } = await sb.from("suismuis_orders").insert(rij);
    if (error) return antwoord({ fout: "Je bestelling kon niet worden opgeslagen. Probeer het opnieuw." }, 500);
    return antwoord({ nr, token, totaal: rij.totaal, regels, subtotaal: sub, verzending: verz, cadeau: cad });
  }

  if (actie === "pp_maak") {
    if (!ppAan()) return antwoord({ fout: "Betalen met creditcard is nog niet actief. Probeer het later opnieuw." }, 503);
    const o = await orderMetToken(b.nr, b.token); if (!o) return antwoord({ fout: "Bestelling niet gevonden." }, 404);
    if (o.status !== "open") return antwoord({ fout: "Deze bestelling is al afgerond." }, 409);
    const items = (o.regels as any[]).map((r) => ({ name: (r.naam + (r.maat ? " (" + r.maat + ")" : "")).slice(0, 127), quantity: String(r.aantal), unit_amount: { currency_code: "EUR", value: bedrag(r.prijs) }, category: "PHYSICAL_GOODS", sku: String(r.nr || r.id).slice(0, 127) }));
    if (Number(o.cadeau)) items.push({ name: "Cadeauverpakking met kaartje", quantity: "1", unit_amount: { currency_code: "EUR", value: bedrag(Number(o.cadeau)) }, category: "PHYSICAL_GOODS", sku: "cadeau" });
    const itemTotaal = rond(Number(o.subtotaal) + Number(o.cadeau));
    const pu: any = { reference_id: o.nr, custom_id: o.nr, invoice_id: o.nr + (o.test ? "-T" + willekeurig(2) : ""), description: "Suismuis Home bestelling " + o.nr,
      amount: { currency_code: "EUR", value: bedrag(Number(o.totaal)), breakdown: { item_total: { currency_code: "EUR", value: bedrag(itemTotaal) }, shipping: { currency_code: "EUR", value: bedrag(Number(o.verzending)) } } },
      items, shipping: { type: "SHIPPING", name: { full_name: o.klant_naam }, address: { address_line_1: (o.adres.straat + " " + o.adres.huisnummer).slice(0, 300), admin_area_2: o.adres.plaats, postal_code: o.adres.postcode, country_code: o.adres.land === "België" ? "BE" : "NL" } } };
    if (env("SUISMUIS_PAYPAL_PAYEE")) pu.payee = { email_address: env("SUISMUIS_PAYPAL_PAYEE") };
    const terug = (o.site || "https://collensgroup.com/concept/suismuis") + "/afrekenen.html?nr=" + encodeURIComponent(o.nr);
    const r = await pp("/v2/checkout/orders", { method: "POST", headers: { "PayPal-Request-Id": "maak-" + o.nr + "-" + willekeurig(3) }, body: JSON.stringify({ intent: "CAPTURE", purchase_units: [pu],
      application_context: { brand_name: "Suismuis Home", locale: "nl-NL", shipping_preference: "SET_PROVIDED_ADDRESS", user_action: "PAY_NOW", return_url: terug, cancel_url: terug } }) });
    if (!r.ok) { console.log("pp_maak", r.status, JSON.stringify(r.j).slice(0, 600)); return antwoord({ fout: "Betalen lukt nu even niet. Probeer het over een paar minuten opnieuw." }, 502); }
    await sb.from("suismuis_orders").update({ paypal_order_id: r.j.id, betaalmethode: tekst(b.methode, 30) || "Creditcard" }).eq("nr", o.nr);
    return antwoord({ id: r.j.id });
  }

  if (actie === "pp_vang") {
    const o = await orderMetToken(b.nr, b.token); if (!o) return antwoord({ fout: "Bestelling niet gevonden." }, 404);
    if (!o.paypal_order_id || (b.id && b.id !== o.paypal_order_id)) return antwoord({ fout: "Betaling hoort niet bij deze bestelling." }, 400);
    if (o.status !== "open") return antwoord({ ok: true, order: publiek(o) });
    const u: any = await verwerkPayPal(o);
    if (u.fout) return antwoord(u, 402);
    return antwoord({ ok: true, order: publiek(u.order), token: u.token });
  }

  if (actie === "bank") {
    const o = await orderMetToken(b.nr, b.token); if (!o) return antwoord({ fout: "Bestelling niet gevonden." }, 404);
    if (o.status !== "open") return antwoord({ ok: true, order: publiek(o) });
    const nu = new Date().toISOString();
    const { data: n } = await sb.from("suismuis_orders").update({ status: "wacht_op_betaling", betaalmethode: "Bankoverschrijving", log: [...(o.log as any[]), { status: "wacht_op_betaling", tijd: nu, door: "klant" }] }).eq("nr", o.nr).eq("status", "open").select("*").maybeSingle();
    if (n) await mailsBijBestelling(n, tekst(b.token, 64));
    return antwoord({ ok: true, order: publiek(n || o) });
  }

  if (actie === "status") {
    let o: any = null;
    if (b.token) o = await orderMetToken(b.nr, b.token);
    else if (b.email) { const { data } = await sb.from("suismuis_orders").select("*").eq("nr", tekst(b.nr, 24).toUpperCase()).maybeSingle(); await new Promise((r) => setTimeout(r, 300)); if (data && data.klant_email === tekst(b.email, 160).toLowerCase()) o = data; }
    if (!o || o.status === "open") return antwoord({ fout: "We vinden geen bestelling met deze gegevens." }, 404);
    return antwoord({ order: publiek(o) });
  }

  if (actie === "bericht") {
    const soort = ["contact", "herroeping", "nieuwsbrief", "maatprijs"].includes(b.soort) ? b.soort : "";
    const email = tekst(b.email, 160).toLowerCase();
    if (!soort || !geldigMail(email)) return antwoord({ fout: "Vul een geldig e-mailadres in." }, 400);
    if (tekst(b.website, 50)) return antwoord({ ok: true }); // honeypot
    const { count } = await sb.from("suismuis_berichten").select("id", { count: "exact", head: true }).gte("created_at", new Date(Date.now() - 3600e3).toISOString());
    if ((count ?? 0) > 60) return antwoord({ fout: "Het is even erg druk. Probeer het later opnieuw." }, 429);
    const velden: Record<string, string> = {};
    for (const [k2, v] of Object.entries(b.velden || {})) if (Object.keys(velden).length < 12) velden[tekst(k2, 40)] = tekst(v, 3000);
    const naam = tekst(b.naam, 100);
    await sb.from("suismuis_berichten").insert({ soort, naam, email, velden });
    const titels: any = { contact: "Nieuw bericht via de webshop", herroeping: "Herroeping van een bestelling", nieuwsbrief: "Nieuwe aanmelding nieuwsbrief", maatprijs: "Prijsaanvraag voor een maat" };
    const rijen = Object.entries(velden).map(([k2, v]) => `<p><b>${esc(k2)}</b><br>${esc(v).replace(/\n/g, "<br>")}</p>`).join("");
    if (soort !== "nieuwsbrief") await mail(KIM, `${titels[soort]}${naam ? " van " + naam : ""}`, omlijst(titels[soort], `<p>${esc(naam)} &lt;${esc(email)}&gt;</p>${rijen}<p style="font-size:13px;color:#7A6553">Beantwoord deze mail om direct te reageren.</p>`), email);
    if (soort === "herroeping") await mail(email, "Ontvangstbevestiging van je herroeping", omlijst("We hebben je herroeping ontvangen", `<p>Hoi ${esc(naam.split(" ")[0])},</p><p>Je herroeping voor bestelling <b>${esc(velden["Ordernummer"] || "")}</b> is ontvangen op ${new Date().toLocaleDateString("nl-NL", { timeZone: "Europe/Amsterdam" })}. We mailen je binnen twee werkdagen het retouradres en de instructies. Na ontvangst van de retour storten we het bedrag binnen 14 dagen terug.</p>`));
    return antwoord({ ok: true });
  }

  // ---------- beheer (Kim) ----------
  if (actie === "setup") {
    const pw = typeof b.wachtwoord === "string" ? b.wachtwoord : "";
    if (pw.length < 10) return antwoord({ fout: "Kies een wachtwoord van minstens 10 tekens." }, 400);
    const { data } = await sb.from("suismuis_beheer").select("*").eq("id", 1).maybeSingle();
    const code = tekst(b.code, 80), eigenCode = env("SUISMUIS_SETUPCODE");
    const viaCode = !data?.wachtwoord_hash && eigenCode.length >= 12 && gelijk(eigenCode, code); // eerste keer: zelfgekozen code uit de Supabase-secrets
    const viaLink = !!data?.setup_token_hash && !!data.setup_verloopt && new Date(data.setup_verloopt) > new Date() && gelijk(data.setup_token_hash, await sha(code));
    if (!viaCode && !viaLink) return antwoord({ fout: "Deze link is verlopen of al gebruikt." }, 403);
    const salt = willekeurig(12);
    await sb.from("suismuis_beheer").update({ wachtwoord_hash: salt + ":" + await pbkdf2(pw, salt), setup_token_hash: null, setup_verloopt: null }).eq("id", 1);
    await sb.from("suismuis_sessies").delete().neq("token_hash", "");
    return antwoord({ ok: true });
  }
  if (actie === "login") {
    const { data } = await sb.from("suismuis_beheer").select("wachtwoord_hash").eq("id", 1).maybeSingle();
    await new Promise((r) => setTimeout(r, 500));
    if (!data?.wachtwoord_hash) return antwoord({ fout: "Je bestelbalie is nog niet ingesteld. Gebruik eerst je instellink." }, 403);
    const [salt, h] = data.wachtwoord_hash.split(":");
    if (!gelijk(h, await pbkdf2(typeof b.wachtwoord === "string" ? b.wachtwoord : "", salt))) return antwoord({ fout: "Onjuist wachtwoord." }, 403);
    const sessie = willekeurig(24);
    await sb.from("suismuis_sessies").delete().lt("verloopt", new Date().toISOString());
    await sb.from("suismuis_sessies").insert({ token_hash: await sha(sessie), verloopt: new Date(Date.now() + 30 * 864e5).toISOString() });
    return antwoord({ sessie });
  }
  if (["lijst", "update", "bericht_af", "uitloggen"].includes(actie)) {
    if (!(await sessieOk(b.sessie))) return antwoord({ fout: "Log opnieuw in." }, 401);
    if (actie === "uitloggen") { await sb.from("suismuis_sessies").delete().eq("token_hash", await sha(b.sessie)); return antwoord({ ok: true }); }
    if (actie === "lijst") {
      const { data: orders } = await sb.from("suismuis_orders").select("nr,created_at,status,test,klant_naam,klant_email,klant_tel,adres,regels,subtotaal,verzending,cadeau,totaal,betaalmethode,paypal_capture_id,betaald_op,leverancier_ordernr,vervoerder,track_trace,notitie,log,mails").neq("status", "open").order("created_at", { ascending: false }).limit(200);
      const { data: berichten } = await sb.from("suismuis_berichten").select("*").order("created_at", { ascending: false }).limit(200);
      return antwoord({ orders: orders ?? [], berichten: berichten ?? [], stappen: STAPPEN, paypal: ppAan() ? (PP_LIVE ? "live" : "test") : "uit" });
    }
    if (actie === "bericht_af") { await sb.from("suismuis_berichten").update({ afgehandeld: !!b.af }).eq("id", Number(b.id)); return antwoord({ ok: true }); }
    const nr = tekst(b.nr, 24);
    const { data: o } = await sb.from("suismuis_orders").select("*").eq("nr", nr).maybeSingle();
    if (!o) return antwoord({ fout: "Bestelling niet gevonden." }, 404);
    const upd: Record<string, unknown> = {};
    for (const v of ["leverancier_ordernr", "vervoerder", "track_trace", "notitie"]) if (typeof b[v] === "string") upd[v] = tekst(b[v], v === "notitie" ? 1000 : 200);
    const nieuw = b.status && STAPPEN[b.status] && b.status !== o.status && b.status !== "open" ? b.status : "";
    if (nieuw) { upd.status = nieuw; upd.log = [...(o.log as any[]), { status: nieuw, tijd: new Date().toISOString(), door: "Kim" }]; if (nieuw === "betaald" && !o.betaald_op) upd.betaald_op = new Date().toISOString(); }
    await sb.from("suismuis_orders").update(upd).eq("nr", nr);
    const n = { ...o, ...upd };
    if (nieuw && b.mail_klant !== false && ["betaald", "verzonden", "geannuleerd", "terugbetaald"].includes(nieuw)) {
      const tok = willekeurig(16); await sb.from("suismuis_orders").update({ status_token_hash: await sha(tok) }).eq("nr", nr);
      const link = `${o.site || "https://collensgroup.com/concept/suismuis"}/bestelling.html?nr=${encodeURIComponent(nr)}&t=${tok}`;
      const teksten: any = {
        betaald: ["We hebben je betaling ontvangen", `<p>Je overschrijving voor bestelling <b>${esc(nr)}</b> is binnen. We gaan je bestelling nu voor je klaarmaken.</p>`],
        verzonden: ["Je bestelling is onderweg", `<p>Goed nieuws: bestelling <b>${esc(nr)}</b> is verzonden.</p>${n.track_trace ? `<p><b>Track-and-trace</b><br>${esc(n.vervoerder || "")} ${/^https?:\/\//.test(String(n.track_trace)) ? `<a href="${esc(n.track_trace)}">${esc(n.track_trace)}</a>` : esc(n.track_trace)}</p>` : ""}`],
        geannuleerd: ["Je bestelling is geannuleerd", `<p>Bestelling <b>${esc(nr)}</b> is geannuleerd. Heb je al betaald, dan krijg je het volledige bedrag binnen 14 dagen terug.</p>`],
        terugbetaald: ["We hebben je geld teruggestort", `<p>Het bedrag voor bestelling <b>${esc(nr)}</b> is teruggestort. Afhankelijk van je bank of PayPal staat het binnen enkele werkdagen op je rekening.</p>`],
      };
      const [t, inh] = teksten[nieuw];
      await logMail(nr, "klant-" + nieuw, await mail(o.klant_email, `${t} (${nr})`, omlijst(t, `<p>Hoi ${esc(o.klant_naam.split(" ")[0])},</p>${inh}${knop(link, "Bekijk je bestelling")}`)));
    }
    return antwoord({ ok: true });
  }
  return antwoord({ fout: "Onbekende actie" }, 400);
});
