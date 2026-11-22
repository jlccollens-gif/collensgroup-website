"""IndexNow: meldt gewijzigde, indexeerbare pagina's direct aan Bing, Yandex, Seznam, Naver e.a.
(Bing-index voedt ook Copilot en ChatGPT-zoeken). Google doet niet mee aan IndexNow; daarvoor sitemap + Search Console.
Gebruik (GitHub Actions, na livecheck): python3 tools/seo/indexnow.py <oude-sha> <nieuwe-sha>
Sleutelbestand staat op https://collensgroup.com/<KEY>.txt (openbaar, zo hoort IndexNow te werken)."""
import json, os, re, subprocess, sys, urllib.request

KEY = "aceaa1aae33f492c9fc3bb575567f4a2"
HOST = "collensgroup.com"
BASIS = f"https://{HOST}/"

def url_voor(pad):
    p = pad[len("dist/"):]
    if p == "index.html": return BASIS
    if p.endswith("/index.html"): return BASIS + p[:-len("index.html")]
    return BASIS + p[:-len(".html")]

def main(oud, nieuw):
    if not oud.strip("0") or not nieuw:
        nieuw = subprocess.run(["git", "log", "-1", "--format=%H", "--", "dist"], capture_output=True, text=True).stdout.strip()
        oud = nieuw + "~1"
    try:
        uit = subprocess.run(["git", "diff", "--name-only", "--diff-filter=AM", oud, nieuw, "--", "dist"], capture_output=True, text=True, check=True).stdout
    except subprocess.CalledProcessError:
        uit = ""
    sitemap = open("dist/sitemap.xml", encoding="utf-8").read()
    in_map = set(re.findall(r"<loc>([^<]+)</loc>", sitemap))
    urls = []
    for p in uit.split():
        if not p.endswith(".html") or not os.path.exists(p): continue
        html = open(p, encoding="utf-8").read(40000)
        if re.search(r'name="robots"[^>]*noindex', html): continue
        u = url_voor(p)
        if u in in_map: urls.append(u)
    if not urls:
        print("IndexNow: geen gewijzigde indexeerbare pagina's"); return 0
    body = json.dumps({"host": HOST, "key": KEY, "keyLocation": f"{BASIS}{KEY}.txt", "urlList": urls[:10000]}).encode()
    req = urllib.request.Request("https://api.indexnow.org/indexnow", data=body, headers={"Content-Type": "application/json; charset=utf-8"})
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            print(f"IndexNow: {len(urls)} URL's gemeld, status {r.status}")
    except urllib.error.HTTPError as e:
        print(f"::warning::IndexNow status {e.code}: {e.read()[:200]!r}")
    for u in urls: print(" ", u)
    return 0

if __name__ == "__main__":
    sys.exit(main(sys.argv[1] if len(sys.argv) > 1 else "", sys.argv[2] if len(sys.argv) > 2 else ""))
