"""Maakt de prijslijst die de betaalserver (Supabase-functie 'suismuis') gebruikt.
Bron: scouting.js (producten) en de WEG-lijst in suismuis.js. De server rekent ALTIJD met deze prijzen, nooit met wat de browser stuurt."""
import json, os, re

def maak(map_assets):
    s = open(os.path.join(map_assets, "scouting.js"), encoding="utf-8").read()
    d = json.loads(s[s.index("["):s.rindex("]") + 1])
    js = open(os.path.join(map_assets, "suismuis.js"), encoding="utf-8").read()
    m = re.search(r"var WEG = \[([0-9,\s]*)\]", js)
    weg = {int(x) for x in m.group(1).split(",") if x.strip()} if m else set()
    k = re.search(r"var GRATIS = ([0-9.]+), VERZEND = ([0-9.]+), CADEAU = ([0-9.]+);", js)
    cat = {}
    for p in d:
        if p.get("nr") in weg:
            continue
        cat[p["id"]] = {"n": p["n"], "p": round(float(p["p"]), 2), "nr": p.get("nr"),
                        "maten": [m + " cm" for m in p.get("maten", [])],
                        "var": [v["n"] for v in p.get("var", [])], "lt": p.get("lt", "")}
    uit = {"versie": 1, "gratis": float(k.group(1)), "verzend": float(k.group(2)), "cadeau": float(k.group(3)), "producten": cat}
    with open(os.path.join(map_assets, "catalogus.json"), "w", encoding="utf-8") as f:
        json.dump(uit, f, ensure_ascii=False, separators=(",", ":"))
    return len(cat)

if __name__ == "__main__":
    import sys
    print(maak(sys.argv[1]))
