"""Live-check na elke push: wacht tot Cloudflare Pages de gewijzigde pagina's toont.
Vergelijkt per gewijzigde dist/*.html de <title> van de lokale versie met de live versie.
Gebruik (in GitHub Actions): python3 tools/livecheck/livecheck.py <oude-sha> <nieuwe-sha>"""
import re, subprocess, sys, time, urllib.request

BASIS = "https://collensgroup.com/"

def titel(html):
    m = re.search(r"<title>(.*?)</title>", html, re.S)
    return m.group(1).strip() if m else ""

def url_voor(pad):
    p = pad[len("dist/"):]
    if p == "index.html": return BASIS
    if p.endswith("/index.html"): return BASIS + p[:-len("index.html")]
    return BASIS + p[:-len(".html")]

def main(oud, nieuw):
    if not oud.strip("0") or not nieuw:  # handmatig gestart of eerste push: laatste commit die dist/ wijzigde
        nieuw = subprocess.run(["git", "log", "-1", "--format=%H", "--", "dist"], capture_output=True, text=True).stdout.strip()
        oud = nieuw + "~1"
    try:
        uit = subprocess.run(["git", "diff", "--name-only", oud, nieuw, "--", "dist"], capture_output=True, text=True, check=True).stdout
    except subprocess.CalledProcessError:
        uit = "dist/index.html\n"
    paden = [p for p in uit.split() if p.endswith(".html")][:15] or ["dist/index.html"]
    open_ = {p: titel(open(p, encoding="utf-8").read()) for p in paden if __import__("os").path.exists(p)}
    for poging in range(12):
        fout = []
        for p, t in open_.items():
            u = url_voor(p)
            try:
                req = urllib.request.Request(u, headers={"User-Agent": "collens-livecheck", "Cache-Control": "no-cache"})
                with urllib.request.urlopen(req, timeout=20) as r:
                    live = r.read().decode("utf-8", "replace")
                    if r.status != 200 or titel(live) != t:
                        fout.append(f"{u}: titel live '{titel(live)[:60]}' ≠ '{t[:60]}'")
            except Exception as e:
                fout.append(f"{u}: {e}")
        if not fout:
            print(f"LIVE OK: {len(open_)} pagina's ({', '.join(url_voor(p) for p in open_)})")
            return 0
        print(f"poging {poging+1}: nog {len(fout)} niet live; wacht 30 s"); time.sleep(30)
    print("NIET LIVE na 6 minuten:\n" + "\n".join(fout)); return 1

if __name__ == "__main__":
    sys.exit(main(*(sys.argv[1:3] + ["", ""])[:2]))
