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
    # Datum-plaatshouders moeten door build.py (datums_vastzetten) ingevuld zijn (19-11)
    for ph in sorted(set(re.findall(r"@@[A-Z_]+@@", src))): fouten.append(f"{f}: datum-plaatshouder {ph} niet ingevuld")
    # Verboden slogan van de eigenaar (16-11): eigendom alleen feitelijk in een FAQ
    for slogan in ("alles is van jou","helemaal van jou","volledig van jou","own everything","you own it","blijft eigenaar van wat"):
        if slogan in src.lower(): fouten.append(f"{f}: verboden slogan '{slogan}'")
    # Anderstalige pagina's: geen Nederlandse formulier- of contactteksten (regressie 18-11: nieuwe NL-tekst, vertaling paste niet meer)
    lm=re.search(r'<html[^>]*lang="([a-z]+)',src)
    if lm and lm.group(1)!="nl":
        zicht=re.sub(r'<(script|style)[^>]*>.*?</\1>','',src,flags=re.S)
        for nl in ("Vertel wat je wilt laten maken","Vertel over je app-idee","Een paar zinnen zijn genoeg","Verstuur aanvraag","Foto's kiezen","Voorbeelden van je smaak","Weet ik nog niet","Vaste prijs vooraf","Wat wil je laten maken","Bedrijf (optioneel)",">Je idee<"):
            if nl in zicht: fouten.append(f"{f}: Nederlandse tekst op {lm.group(1)}-pagina: '{nl}'")
# Generiek (19-11): elke zichtbare tekst uit het NL-contactformulier die letterlijk op een anderstalig formulier staat = vergeten vertaling.
# Vangt ook NIEUWE NL-teksten die in geen enkele vervanglijst staan. Toegestaan: woorden die in die taal hetzelfde zijn en technische waarden.
from html.parser import HTMLParser as _HP
class _TX(_HP):
    def __init__(s): super().__init__(); s.t=set(); s.skip=0
    def handle_starttag(s,t,a):
        if t in("script","style"): s.skip+=1
        for k,v in a:
            if k in("placeholder","aria-label","title","alt") and v and v.strip(): s.t.add(" ".join(v.split()))
    def handle_endtag(s,t):
        if t in("script","style"): s.skip-=1
    def handle_data(s,d):
        if not s.skip and d.strip(): s.t.add(" ".join(d.split()))
def _form_teksten(src):
    m=re.search(r'<section id="contact".*?</section>',src,re.S)
    if not m: return None
    p=_TX(); p.feed(m.group(0)); out=set(p.t)
    for j in re.findall(r'<script[^>]*>(.*?)</script>',src,re.S):
        if 'getElementById("aanvraag")' not in j: continue
        j=re.sub(r'/\*.*?\*/','',j,flags=re.S)
        for q in ('"',"'","`"):
            for x in re.findall(q+r'([^'+q+r'\\\n;{}=<>]{6,})'+q,j):
                if re.search(r'[A-Za-zÀ-ÿ]{3,} [A-Za-zÀ-ÿ]{2,}',x) or x.rstrip().endswith((".",":","…","?")): out.add(x.strip())
    return out
_ZELFDE={"App","Apps","Game","Games","Website","Websites","E-mail","Email","Niet invullen","knop geel","mailto:","melding aan","Collens Group"}
_nl_src=os.path.join(D,"index.html")
_nl=_form_teksten(open(_nl_src,encoding="utf-8").read()) if os.path.exists(_nl_src) else None
if not _nl: fouten.append("index.html: NL-contactformulier niet gevonden (formuliercheck kan niet draaien)")
else:
    for f in sorted(pages):
        src=open(os.path.join(D,f),encoding="utf-8").read()
        lm=re.search(r'<html[^>]*lang="([a-z]+)',src)
        if not lm or lm.group(1)=="nl": continue
        t=_form_teksten(src)
        if t is None: continue
        for x in sorted((t&_nl)-_ZELFDE): fouten.append(f"{f}: formuliertekst niet vertaald ({lm.group(1)}): '{x[:60]}'")
for x in waarsch: print("LET OP:",x)
for x in fouten: print("FOUT:",x)
print(f"{len(pages)} pagina's gecontroleerd, {len(fouten)} fouten, {len(waarsch)} aandachtspunten")
sys.exit(1 if fouten else 0)
