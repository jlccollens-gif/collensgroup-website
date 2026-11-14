// Spraakbericht naar tekst voor de chat-adviseur (Cloudflare Pages Function: /api/spraak).
// Verstaat 90+ talen. Het geluid wordt alleen omgezet en niet bewaard.
// Geheim (een van beide is genoeg), in Cloudflare Pages → Settings → Variables and Secrets:
//   ELEVENLABS_API_KEY  (Scribe)  of  OPENAI_API_KEY (gpt-4o-mini-transcribe)
const MAX_BYTES = 3 * 1024 * 1024; // ruim 1 minuut spraak
const TOEGESTAAN = [/^https:\/\/(www\.)?collensgroup\.com$/, /^https:\/\/[a-z0-9-]+\.collensgroup-website\.pages\.dev$/, /^https:\/\/collensgroup-website\.pages\.dev$/];

const json = (data, status = 200) => new Response(JSON.stringify(data), {
  status, headers: { "content-type": "application/json; charset=utf-8", "cache-control": "no-store" },
});

export async function onRequestGet({ env }) {
  return json({ actief: Boolean(env.ANTHROPIC_API_KEY && (env.ELEVENLABS_API_KEY || env.OPENAI_API_KEY)) });
}

export async function onRequestPost({ request, env }) {
  const o = request.headers.get("origin");
  if (!o || !TOEGESTAAN.some(r => r.test(o))) return json({ fout: "niet-toegestaan" }, 403);
  if (!env.ELEVENLABS_API_KEY && !env.OPENAI_API_KEY) return json({ fout: "niet-actief" }, 503);
  const type = (request.headers.get("content-type") || "audio/webm").split(";")[0];
  if (!/^audio\//.test(type)) return json({ fout: "ongeldig" }, 400);
  const buf = await request.arrayBuffer();
  if (!buf.byteLength || buf.byteLength > MAX_BYTES) return json({ fout: "te-lang" }, 413);
  const ext = type.includes("mp4") || type.includes("m4a") ? "m4a" : type.includes("ogg") ? "ogg" : "webm";
  const bestand = new Blob([buf], { type });

  try {
    let tekst = "";
    if (env.ELEVENLABS_API_KEY) {
      const fd = new FormData();
      fd.append("model_id", env.STT_MODEL || "scribe_v2");
      fd.append("file", bestand, `bericht.${ext}`);
      const r = await fetch("https://api.elevenlabs.io/v1/speech-to-text", { method: "POST", headers: { "xi-api-key": env.ELEVENLABS_API_KEY }, body: fd });
      if (!r.ok) throw new Error("ElevenLabs " + r.status + " " + (await r.text()).slice(0, 200));
      tekst = String((await r.json()).text || "");
    } else {
      const fd = new FormData();
      fd.append("model", env.STT_MODEL || "gpt-4o-mini-transcribe");
      fd.append("file", bestand, `bericht.${ext}`);
      fd.append("prompt", "Question to a web, app and game agency: website, webshop, app, game, AI chatbot, price, Collens Group.");
      const r = await fetch("https://api.openai.com/v1/audio/transcriptions", { method: "POST", headers: { Authorization: `Bearer ${env.OPENAI_API_KEY}` }, body: fd });
      if (!r.ok) throw new Error("OpenAI " + r.status + " " + (await r.text()).slice(0, 200));
      tekst = String((await r.json()).text || "");
    }
    tekst = tekst.replace(/\s*\([^)]*\)\s*/g, " ").trim(); // geluidslabels zoals (gelach) weghalen
    return tekst ? json({ tekst: tekst.slice(0, 2000) }) : json({ fout: "leeg" }, 422);
  } catch (err) {
    console.log("spraakfout", String(err).slice(0, 400));
    return json({ fout: "storing" }, 502);
  }
}
