// Collens Group: één Cloudflare Pages-project, meerdere sites.
// - collensgroup.com en *.pages.dev: gewone site.
// - collensgroup.com/live-suismuis/...: voorvertoning van de live webshop van Suismuis (noindex).
// - elk ander domein dat aan dit project is gekoppeld (Kims eigen domein): de webshop van Suismuis Home,
//   zonder conceptwatermerk, met canonical, robots.txt en sitemap op dat domein.
const EIGEN = /(^|\.)collensgroup\.com$|\.pages\.dev$|^localhost$|^127\.0\.0\.1$/;
const BRON = "/concept/suismuis";
const VOORVERTONING = "/live-suismuis";
const PAGINAS = ["index.html", "shop.html", "over.html", "journal.html", "klantenservice.html", "winkelmand.html", "favorieten.html", "bestelling.html"];

class Weg { element(e) { e.remove(); } }
class Titel { text(t) { if (t.text.includes(" (concept)")) t.replace(t.text.replace(" (concept)", "")); } }
class Inhoud { constructor(van, naar) { this.van = van; this.naar = naar; } element(e) { const c = e.getAttribute("content"); if (c && c.includes(this.van)) e.setAttribute("content", c.replace(this.van, this.naar)); } }
class Kop { constructor(html) { this.html = html; } element(e) { e.append(this.html, { html: true }); } }

export async function onRequest(ctx) {
  const { request, env, next } = ctx;
  const url = new URL(request.url);
  const eigen = EIGEN.test(url.hostname);
  let basis;
  if (eigen) {
    if (url.pathname !== VOORVERTONING && !url.pathname.startsWith(VOORVERTONING + "/")) return next();
    basis = VOORVERTONING;
  } else {
    if (url.hostname.startsWith("www.")) { url.hostname = url.hostname.slice(4); return Response.redirect(url.toString(), 301); }
    basis = "";
  }
  const live = !eigen;
  let rest = url.pathname.slice(basis.length);
  if (rest === "") return Response.redirect(url.origin + basis + "/" + url.search, 301);
  if (rest.startsWith("/api/") || rest.startsWith("/concept/") || rest.startsWith("/functions/")) return new Response("Niet gevonden", { status: 404 });

  if (live && rest === "/robots.txt")
    return new Response(`User-agent: *\nAllow: /\nDisallow: /beheer.html\nDisallow: /afrekenen.html\nDisallow: /winkelmand.html\nDisallow: /bestelling.html\nSitemap: ${url.origin}/sitemap.xml\n`, { headers: { "content-type": "text/plain; charset=utf-8" } });
  if (live && rest === "/sitemap.xml") {
    const c = await env.ASSETS.fetch(new Request(new URL(BRON + "/assets/catalogus.json", url)));
    const ids = c.ok ? Object.keys((await c.json()).producten || {}) : [];
    const locs = ["/", ...PAGINAS.slice(1, 5).map((p) => "/" + p), ...ids.map((id) => "/product.html?p=" + encodeURIComponent(id))];
    const xml = `<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n${locs.map((l) => `<url><loc>${url.origin}${l.replace(/&/g, "&amp;")}</loc></url>`).join("\n")}\n</urlset>\n`;
    return new Response(xml, { headers: { "content-type": "application/xml; charset=utf-8", "cache-control": "public, max-age=3600" } });
  }

  let doel = BRON + rest;
  if (doel.endsWith("/index.html")) doel = doel.slice(0, -10);
  else if (doel.endsWith(".html")) doel = doel.slice(0, -5);
  const res = await env.ASSETS.fetch(new Request(new URL(doel + url.search, url), { method: request.method === "HEAD" ? "HEAD" : "GET", headers: request.headers }));

  if (res.status >= 300 && res.status < 400) {
    const loc = res.headers.get("location");
    if (loc) {
      const l = new URL(loc, url);
      if (l.pathname.startsWith(BRON)) l.pathname = basis + l.pathname.slice(BRON.length);
      return new Response(null, { status: res.status, headers: { location: l.pathname + l.search } });
    }
    return res;
  }

  const h = new Headers(res.headers);
  if (live) {
    h.delete("x-robots-tag");
    if (/^\/(img|assets)\//.test(rest)) h.set("cache-control", url.search.includes("v=") || rest.startsWith("/img/") ? "public, max-age=604800" : "public, max-age=300");
    if (rest === "/beheer.html" || rest === "/afrekenen.html" || rest === "/bestelling.html") h.set("x-robots-tag", "noindex");
  } else h.set("x-robots-tag", "noindex, nofollow");
  const uit = new Response(res.body, { status: res.status, statusText: res.statusText, headers: h });
  if (!(h.get("content-type") || "").includes("text/html")) return uit;

  let pad = rest === "/" ? "/" : rest;
  if (pad === "/index.html") pad = "/";
  const p = url.searchParams.get("p");
  const canon = url.origin + basis + pad + (pad === "/product.html" && p ? "?p=" + encodeURIComponent(p) : "");
  let rw = new HTMLRewriter()
    .on(".alleen-concept", new Weg())
    .on('meta[name="generator"]', new Weg())
    .on("title", new Titel())
    .on('meta[property="og:title"]', new Inhoud(" (concept)", ""))
    .on('meta[property="og:image"]', new Inhoud("https://collensgroup.com" + BRON, url.origin + basis))
    .on("head", new Kop(`<link rel="canonical" href="${canon.replace(/"/g, "&quot;")}"><meta property="og:url" content="${canon.replace(/"/g, "&quot;")}">`));
  if (live) rw = rw.on('meta[name="robots"]', new Weg());
  return rw.transform(uit);
}
