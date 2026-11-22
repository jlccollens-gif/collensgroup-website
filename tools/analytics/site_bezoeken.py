"""Dagelijks overzicht van ALLE bezoeken aan collensgroup.com (cookieloos, Cloudflare Web Analytics).
Bron: Cloudflare GraphQL, dataset rumPageloadEventsAdaptiveGroups. Token alleen via omgeving (CF_ANALYTICS_TOKEN).
Schrijft rapporten/site-bezoeken.json en .md. Conceptpagina's (/concept/) en testerpagina's tellen apart.
Zoekmachine-verkeer = verwijzer is een zoekmachine (Google, Bing, DuckDuckGo, Yahoo, Ecosia, Yandex, Baidu)."""
import json, os, sys, urllib.request, urllib.error, datetime as dt

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from concept_bezoeken import ACCOUNT, TOKEN, iso  # zelfde token en account

DAGEN = int(os.environ.get("DAGEN", "28"))
HOST = "collensgroup.com"
ZOEK = ("google.", "bing.", "duckduckgo.", "yahoo.", "ecosia.", "yandex.", "baidu.", "startpage.", "qwant.")
AI = ("chatgpt.", "openai.", "perplexity.", "claude.ai", "gemini.google", "copilot.microsoft")

Q = """query($acc: String!, $since: Time!, $until: Time!, $host: String!) {
  viewer { accounts(filter: {accountTag: $acc}) {
    rumPageloadEventsAdaptiveGroups(limit: 10000, filter: {datetime_geq: $since, datetime_lt: $until, requestHost: $host}, orderBy: [date_ASC]) {
      count
      sum { visits }
      dimensions { date requestPath countryName deviceType refererHost }
    }
  } } }"""


def soort(pad):
    if pad.startswith("/concept/"):
        return "concept"
    if pad.startswith("/tester"):
        return "tester"
    return "site"


def bron(ref):
    r = (ref or "").lower()
    if not r or r == HOST or r.endswith("." + HOST):
        return "direct/intern"
    if any(z in r for z in ZOEK):
        return "zoekmachine"
    if any(a in r for a in AI):
        return "AI-assistent"
    return "andere site"


def tel(d, k, n):
    d[k] = d.get(k, 0) + n


def main():
    nu = dt.datetime.now(dt.timezone.utc).replace(microsecond=0)
    van = nu - dt.timedelta(days=DAGEN)
    uit = {"gemaakt": iso(nu), "van": iso(van), "tot": iso(nu), "dagen_periode": DAGEN, "fout": None}
    if not TOKEN:
        uit["fout"] = "CF_ANALYTICS_TOKEN ontbreekt"
    else:
        body = json.dumps({"query": Q, "variables": {"acc": ACCOUNT, "since": iso(van), "until": iso(nu), "host": HOST}}).encode()
        req = urllib.request.Request("https://api.cloudflare.com/client/v4/graphql", data=body,
                                     headers={"Authorization": "Bearer " + TOKEN, "Content-Type": "application/json"})
        try:
            data = json.load(urllib.request.urlopen(req, timeout=60))
        except urllib.error.HTTPError as e:
            data = {"errors": [{"message": f"HTTP {e.code}: {e.read().decode('utf-8', 'replace')[:300]}"}]}
        except Exception as e:
            data = {"errors": [{"message": f"{type(e).__name__}: {e}"}]}
        if data.get("errors"):
            uit["fout"] = "; ".join(x.get("message", "?") for x in data["errors"])[:500]
        else:
            rijen = data["data"]["viewer"]["accounts"][0]["rumPageloadEventsAdaptiveGroups"]
            uit["rijen"] = len(rijen)
            per = {s: {"weergaven": 0, "bezoeken": 0} for s in ("site", "concept", "tester")}
            dagen, paginas, landen, apparaten, bronnen, zoekmachines, verwijzers = {}, {}, {}, {}, {}, {}, {}
            for r in rijen:
                d, n, v = r["dimensions"], r["count"], (r.get("sum") or {}).get("visits", 0)
                pad = d.get("requestPath") or "/"
                s = soort(pad)
                per[s]["weergaven"] += n; per[s]["bezoeken"] += v
                if s != "site":
                    continue
                dag = dagen.setdefault(d["date"], {"weergaven": 0, "bezoeken": 0, "zoekmachine": 0})
                dag["weergaven"] += n; dag["bezoeken"] += v
                b = bron(d.get("refererHost"))
                if b == "zoekmachine":
                    dag["zoekmachine"] += v
                    tel(zoekmachines, d.get("refererHost"), v)
                tel(paginas, pad, n); tel(landen, d.get("countryName") or "?", v)
                tel(apparaten, d.get("deviceType") or "?", v); tel(bronnen, b, v)
                if b in ("andere site", "AI-assistent"):
                    tel(verwijzers, d.get("refererHost"), v)
            srt = lambda x: dict(sorted(x.items(), key=lambda kv: -kv[1]))
            uit.update({"per_soort": per, "per_dag": dict(sorted(dagen.items())), "paginas": srt(paginas),
                        "landen": srt(landen), "apparaten": srt(apparaten), "bronnen": srt(bronnen),
                        "zoekmachines": srt(zoekmachines), "verwijzers": srt(verwijzers)})
    os.makedirs("rapporten", exist_ok=True)
    with open("rapporten/site-bezoeken.json", "w") as f:
        json.dump(uit, f, ensure_ascii=False, indent=1)
    r = [f"# Bezoeken collensgroup.com (laatste {DAGEN} dagen)", f"Gemaakt: {uit['gemaakt']} (UTC). Bron: Cloudflare Web Analytics (cookieloos, zonder bots).", ""]
    if uit["fout"]:
        r.append(f"**Fout:** {uit['fout']}")
    else:
        p = uit["per_soort"]
        r += [f"- Site: **{p['site']['bezoeken']} bezoeken**, {p['site']['weergaven']} paginaweergaven",
              f"- Conceptpagina's (klanten): {p['concept']['bezoeken']} bezoeken · testerpagina's: {p['tester']['bezoeken']} bezoeken", "",
              "## Waar komen bezoekers vandaan", *[f"- {k}: {v}" for k, v in uit["bronnen"].items()], "",
              "## Zoekmachines", *([f"- {k}: {v}" for k, v in uit["zoekmachines"].items()] or ["- nog geen"]), "",
              "## Top 15 pagina's (weergaven)", *[f"- {k}: {v}" for k, v in list(uit["paginas"].items())[:15]], "",
              "## Landen", *[f"- {k}: {v}" for k, v in list(uit["landen"].items())[:10]], "",
              "## Per dag (bezoeken / via zoekmachine)", *[f"- {k}: {v['bezoeken']} / {v['zoekmachine']}" for k, v in uit["per_dag"].items()]]
    with open("rapporten/site-bezoeken.md", "w") as f:
        f.write("\n".join(r) + "\n")
    print("\n".join(r))
    return 1 if uit["fout"] else 0


if __name__ == "__main__":
    sys.exit(main())
