"""Kwaliteitscontrole: draai na elke build. Faalt bij fouten."""
import os, re, sys, html
from html.parser import HTMLParser
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), "dist")
fouten, waarsch = [], []
class P(HTMLParser):
    def __init__(s): super().__init__(); s.links=[]; s.imgs=[]; s.h1=0; s.title=""; s.desc=None; s._t=False; s.ids=[]
    def handle_starttag(s, t, a):
        a=dict(a)
        if t=="a" and "href" in a: s.links.append(a["href"])
        if t in ("img","video"): s.imgs.append(a)
        if t=="h1": s.h1+=1
        if t=="title": s._t=True
        if t=="meta" and a.get("name")=="description": s.desc=a.get("content","")
        if "id" in a: s.ids.append(a["id"])
    def handle_endtag(s,t):
        if t=="title": s._t=False
    def handle_data(s,d):
        if s._t: s.title+=d
pages=[f for f in os.listdir(D) if f.endswith(".html")]
for f in sorted(pages):
    src=open(os.path.join(D,f),encoding="utf-8").read(); p=P(); p.feed(src)
    if f!="404.html" and p.h1!=1: fouten.append(f"{f}: {p.h1} h1-koppen (moet 1 zijn)")
    if not (10<=len(p.title)<=70): waarsch.append(f"{f}: titel {len(p.title)} tekens")
    if p.desc is None or not (50<=len(p.desc)<=170): waarsch.append(f"{f}: meta description {0 if p.desc is None else len(p.desc)} tekens")
    for i in p.imgs:
        if i.get("src") and not os.path.exists(os.path.join(D,i["src"].split("?")[0])): fouten.append(f"{f}: ontbrekend beeld {i['src']}")
        if "alt" not in i and i.get("src","").endswith((".jpg",".png")): fouten.append(f"{f}: img zonder alt {i.get('src')}")
    for h in p.links:
        if h.startswith(("http","mailto:","tel:")) or h=="#": continue
        path,_,frag=h.partition("#")
        tgt=path or f
        # schone URL's (zonder .html) zoals Cloudflare Pages ze serveert
        if os.path.isdir(os.path.join(D,tgt)): tgt=os.path.join(tgt,"index.html")
        elif not os.path.exists(os.path.join(D,tgt)) and os.path.exists(os.path.join(D,tgt+".html")): tgt=tgt+".html"
        if not os.path.exists(os.path.join(D,tgt)): fouten.append(f"{f}: kapotte link {h}")
        elif frag:
            t=open(os.path.join(D,tgt),encoding="utf-8").read()
            if f'id="{frag}"' not in t: fouten.append(f"{f}: anker #{frag} bestaat niet in {tgt}")
    m=re.search(r'<nav class="snel-paneel".*?</nav>',src,re.S)
    if m:
        hrefs=re.findall(r'href="([^"]+)"',m.group(0)); txt=re.findall(r'>([^<]+)</a>',m.group(0))
        if len(set(hrefs))!=len(hrefs): fouten.append(f"{f}: dubbele link in snelmenu")
        for t in txt:
            if t.strip() in ("English","Nederlands","Deutsch","Français","Español"): fouten.append(f"{f}: taal in snelmenu ({t}) – hoort in taalknop")
    m=re.search(r'<header.*?</header>',src,re.S)
    if m:
        if m.group(0).count('class="taalkeuze"')!=1: fouten.append(f"{f}: taalknop ontbreekt of dubbel")
    if len(set(p.ids))!=len(p.ids): fouten.append(f"{f}: dubbele id's")
    # Verboden slogan van de eigenaar (16-11): eigendom alleen feitelijk in een FAQ
    for slogan in ("alles is van jou","helemaal van jou","volledig van jou","own everything","you own it"):
        if slogan in src.lower(): fouten.append(f"{f}: verboden slogan '{slogan}'")
for x in waarsch: print("LET OP:",x)
for x in fouten: print("FOUT:",x)
print(f"{len(pages)} pagina's gecontroleerd, {len(fouten)} fouten, {len(waarsch)} aandachtspunten")
sys.exit(1 if fouten else 0)
