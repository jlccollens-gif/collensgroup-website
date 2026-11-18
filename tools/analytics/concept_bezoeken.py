"""Dagelijks (05:17 UTC) overzicht: welke concept-pagina's (/concept/<slug>/) zijn bekeken.
Bron: Cloudflare Web Analytics (GraphQL, dataset rumPageloadEventsAdaptiveGroups).
Token alleen via omgeving (CF_ANALYTICS_TOKEN, recht Account Analytics: Read).
Schrijft rapporten/concept-bezoeken.json en .md in de huidige map."""
import json, os, sys, urllib.request, urllib.error, datetime as dt

ACCOUNT = os.environ.get("CF_ACCOUNT_ID", "5c0e89673825539df27c9e1c99219e8b")
TOKEN = os.environ.get("CF_ANALYTICS_TOKEN", "")
DAGEN = int(os.environ.get("DAGEN", "7"))

Q = """query($acc: String!, $since: Time!, $until: Time!) {
  viewer { accounts(filter: {accountTag: $acc}) {
    rumPageloadEventsAdaptiveGroups(limit: 5000, filter: {datetime_geq: $since, datetime_lt: $until, requestPath_like: "/concept/%"}, orderBy: [date_ASC]) {
      count
      sum { visits }
      dimensions { date requestHost requestPath countryName deviceType refererHost }
    }
  } } }"""


def iso(t):
    return t.isoformat().replace("+00:00", "Z")


def main():
    nu = dt.datetime.now(dt.timezone.utc).replace(microsecond=0)
    van = nu - dt.timedelta(days=DAGEN)
    uit = {"gemaakt": iso(nu), "van": iso(van), "tot": iso(nu), "fout": None, "per_concept": {}}
    if not TOKEN:
        uit["fout"] = "CF_ANALYTICS_TOKEN ontbreekt"
    else:
        body = json.dumps({"query": Q, "variables": {"acc": ACCOUNT, "since": iso(van), "until": iso(nu)}}).encode()
        req = urllib.request.Request("https://api.cloudflare.com/client/v4/graphql", data=body,
                                     headers={"Authorization": "Bearer " + TOKEN, "Content-Type": "application/json"})
        try:
            data = json.load(urllib.request.urlopen(req, timeout=60))
        except urllib.error.HTTPError as e:
            tekst = e.read().decode("utf-8", "replace")
            try:
                data = json.loads(tekst)
                if not data.get("errors"):
                    data = {"errors": [{"message": f"HTTP {e.code}: {tekst[:400]}"}]}
            except ValueError:
                data = {"errors": [{"message": f"HTTP {e.code}: {tekst[:400]}"}]}
        except Exception as e:  # netwerk
            data = {"errors": [{"message": f"{type(e).__name__}: {e}"}]}
        if data.get("errors"):
            uit["fout"] = "; ".join(x.get("message", "?") for x in data["errors"])[:500]
        else:
            rijen = data["data"]["viewer"]["accounts"][0]["rumPageloadEventsAdaptiveGroups"]
            for r in rijen:
                d = r["dimensions"]
                if "collensgroup.com" not in (d.get("requestHost") or ""):
                    continue
                delen = [p for p in d["requestPath"].split("/") if p]
                if len(delen) < 2:
                    continue
                slug = delen[1]
                c = uit["per_concept"].setdefault(slug, {"weergaven": 0, "bezoeken": 0, "dagen": {}, "landen": {}, "apparaten": {}, "verwijzers": {}})
                c["weergaven"] += r["count"]
                c["bezoeken"] += (r.get("sum") or {}).get("visits", 0)
                for k, v in (("dagen", d.get("date")), ("landen", d.get("countryName")),
                             ("apparaten", d.get("deviceType")), ("verwijzers", d.get("refererHost"))):
                    if v:
                        c[k][v] = c[k].get(v, 0) + r["count"]
    os.makedirs("rapporten", exist_ok=True)
    with open("rapporten/concept-bezoeken.json", "w") as f:
        json.dump(uit, f, ensure_ascii=False, indent=1, sort_keys=True)
    regels = [f"# Concept-bezoeken (laatste {DAGEN} dagen)", f"Gemaakt: {uit['gemaakt']} (UTC)", ""]
    if uit["fout"]:
        regels.append(f"**Fout:** {uit['fout']}")
    elif not uit["per_concept"]:
        regels.append("Geen bezoeken aan /concept/-pagina's in deze periode.")
    else:
        regels += ["| Concept | Weergaven | Bezoeken | Laatste dag | Landen |", "|---|---|---|---|---|"]
        for slug, c in sorted(uit["per_concept"].items(), key=lambda x: -x[1]["weergaven"]):
            laatste = max(c["dagen"]) if c["dagen"] else "-"
            regels.append(f"| {slug} | {c['weergaven']} | {c['bezoeken']} | {laatste} | {', '.join(sorted(c['landen']))} |")
    with open("rapporten/concept-bezoeken.md", "w") as f:
        f.write("\n".join(regels) + "\n")
    print("\n".join(regels))
    return 1 if uit["fout"] else 0


if __name__ == "__main__":
    sys.exit(main())
