#!/usr/bin/env python3
"""Klantensite-blik: vaste controle voor websites die wij voor klanten (of onszelf) maken.
Gebruik:  python3 sitecheck.py https://voorbeeld.nl      (crawlt zelf, max 40 pagina's, alleen leesverkeer)
          python3 sitecheck.py ./dist                     (map met .html-bestanden)
Alleen standaardbibliotheek. Rapport in markdown; afsluitcode 1 bij 🔴.
🔴 = moet opgelost vóór oplevering/publicatie, 🟡 = verbeteren, 🔵 = handmatig verifiëren (kan niet automatisch bewezen worden)."""
import sys, os, re, json, collections, urllib.request, urllib.parse
from html.parser import HTMLParser

MAXP = 40
LEK = re.compile(r"""(?:["']?\b(ink|inkoop\w*|inkoopprijs|cost_price|marge)["']?\s*:\s*["']?\d)|(?:["']?\b(api[_-]?key|secret|sk_live\w*|service_role|password|wachtwoord)["']?\s*[:=]\s*["'][^"'\s]{8,})""", re.I)
PLACEHOLDER = re.compile(r"lorem ipsum|\[[^\]]{3,60}(volgen|invullen|adres|naam|todo)[^\]]*\]|tekst ter illustratie|jouwbedrijf|example\.(com|nl)|(?-i:\bTODO\b)|volgen bij lancering|kies een titel", re.I)
RISICO = re.compile(r"bestseller|meest verkocht|nr\.? ?1|beste van|gegarandeerd|100 ?%|top ?kwaliteit|handgemaakt|handgeschilderd|duurzaam|biologisch|gratis|nog maar \d+|laatste kans|alleen vandaag|⭐|★|reviews?", re.I)

class P(HTMLParser):
    def __init__(s):
        super().__init__(); s.t=""; s._t=False; s.m={}; s.h1=0; s.links=[]; s.imgs=[]; s.ld=[]; s.txt=[]; s.scripts=[]; s._skip=0; s._ld=False; s.canon=None
    def handle_starttag(s, tag, a):
        a=dict(a)
        if tag=="title": s._t=True
        if tag=="meta" and (a.get("name") or a.get("property")): s.m[a.get("name") or a.get("property")]=a.get("content","")
        if tag=="link" and a.get("rel")=="canonical": s.canon=a.get("href")
        if tag=="h1": s.h1+=1
        if tag=="a" and a.get("href"): s.links.append(a["href"])
        if tag=="img": s.imgs.append(a)
        if tag=="script":
            if a.get("src"): s.scripts.append(a["src"])
            if a.get("type")=="application/ld+json": s._ld=True
            s._skip+=1
        if tag=="style": s._skip+=1
    def handle_endtag(s, tag):
        if tag=="title": s._t=False
        if tag in ("script","style"): s._skip=max(0,s._skip-1); s._ld=False
    def handle_data(s, d):
        if s._t: s.t+=d
        elif s._ld: s.ld.append(d)
        elif not s._skip: s.txt.append(d)

def haal(url):
    r=urllib.request.Request(url, headers={"User-Agent":"sitecheck/1.0 (leesverkeer)"})
    with urllib.request.urlopen(r, timeout=20) as f: return f.read().decode("utf-8","replace")

def laad(doel):
    """geeft {naam: (html, [scripttekst])}"""
    pag, assets = {}, {}
    if os.path.isdir(doel):
        for dp,_,fs in os.walk(doel):
            for f in fs:
                p=os.path.join(dp,f); rel=os.path.relpath(p,doel)
                if f.endswith(".html"): pag[rel]=open(p,encoding="utf-8",errors="replace").read()
                elif f.endswith((".js",".json")) and os.path.getsize(p)<3_000_000: assets[rel]=open(p,encoding="utf-8",errors="replace").read()
        return pag, assets
    host=urllib.parse.urlparse(doel).netloc; todo=[doel]; seen=set()
    while todo and len(pag)<MAXP:
        u=todo.pop(0).split("#")[0]
        if u in seen: continue
        seen.add(u)
        try: h=haal(u)
        except Exception as e: pag[u]=""; continue
        pag[u]=h; p=P(); p.feed(h)
        for l in p.links:
            x=urllib.parse.urljoin(u,l).split("#")[0]
            if urllib.parse.urlparse(x).netloc==host and not re.search(r"(\.(jpg|png|webp|pdf|mp4|svg|js|css)$|cdn-cgi)",x) and x not in seen: todo.append(x)
        for sc in p.scripts:
            x=urllib.parse.urljoin(u,sc)
            if urllib.parse.urlparse(x).netloc==host and x not in assets:
                try: assets[x]=haal(x)[:3_000_000]
                except Exception: pass
    return pag, assets

def main(doel):
    pag, assets = laad(doel)
    rood, geel, blauw, ok = [], [], [], []
    tekst_alle = ""; titels=collections.Counter(); descs=collections.Counter(); btw_excl=btw_geen=0; lt=set(); shop=False; trust=collections.Counter()
    for n,h in pag.items():
        p=P(); p.feed(h); tekst=re.sub(r"\s+"," "," ".join(p.txt)); tl=tekst.lower(); tekst_alle+=" "+tl
        w=len(tekst.split()); idx="noindex" in p.m.get("robots","")
        titels[p.t.strip()]+=1; descs[p.m.get("description","")]+=1
        if not h: rood.append(f"{n}: pagina niet op te halen"); continue
        if p.h1!=1 and not os.path.basename(n).startswith("404"): geel.append(f"{n}: {p.h1} h1-koppen (moet 1 zijn; bij JS-pagina's controleren of de h1 na laden bestaat)")
        if not p.t.strip() or len(p.t)>65: geel.append(f"{n}: titel {len(p.t)} tekens ('{p.t[:40]}')")
        d=p.m.get("description","")
        if not d: geel.append(f"{n}: geen meta description")
        elif not 70<=len(d)<=165: geel.append(f"{n}: meta description {len(d)} tekens (richt 70–160)")
        if not idx and not p.canon: geel.append(f"{n}: geen canonical")
        if w<300 and not re.search(r"(winkelmand|afrekenen|account|favorieten|404|privacy|voorwaarden)",n,re.I): geel.append(f"{n}: dun ({w} woorden); commerciële pagina's liefst 600+ met proces, prijs en FAQ")
        leeg=[i for i in p.imgs if i.get("alt") is None or (i.get("alt")=="" and int(re.sub(r'\D','0',i.get("width","0")) or 0)>=200)]
        if leeg: geel.append(f"{n}: {len(leeg)} afbeeldingen zonder alt-tekst")
        if idx: blauw.append(f"{n}: staat op noindex (bedoeld? zo ja, niet vindbaar in Google)")
        for m in PLACEHOLDER.finditer(h): rood.append(f"{n}: placeholdertekst zichtbaar: '{m.group(0)[:60]}'"); break
        btw_excl+=len(re.findall(r"excl\.? ?btw|exclusief btw|zonder btw|ex\.? btw",tl)); btw_geen+=len(re.findall(r"geen btw|incl\.? ?btw|inclusief btw",tl))
        lt.update(re.findall(r"\d+\s?[–-]\s?\d+ werkdagen",tl))
        if re.search(r"winkelmand|afrekenen|in winkelwagen",tl): shop=True
        for k,rx in {"contact":r"mailto:|tel:|contactformulier|neem contact","over":r"over ons|over mij|about","voorwaarden":r"algemene voorwaarden","privacy":r"privacy","retour":r"retour|herroep|bedenktijd","kvk":r"kvk","reviews":r"beoordeling|review|ervaringen|testimonial","adres":r"\d{4} ?[a-z]{2}\b|straat \d|\bnl-\d{4}"}.items():
            if re.search(rx,tl+" ".join(p.links).lower()): trust[k]+=1
        if "$" in tekst and p.m.get("og:locale","nl_NL").startswith("nl") and "€" in tekst: blauw.append(f"{n}: dollar- en eurobedragen door elkaar (bedoeld? zet er een eurobedrag bij)")
        risico=sorted(set(m.group(0).lower() for m in RISICO.finditer(tekst)))
        if risico: blauw.append(f"{n}: claims om te verifiëren vóór publicatie: {', '.join(risico[:8])}")
        if not [x for x in p.ld if x.strip()] and not idx: geel.append(f"{n}: geen structured data (Organization/Product/FAQPage/Article waar passend)")
    for t,c in titels.items():
        if c>2 and t: geel.append(f"{c} pagina's hebben dezelfde titel: '{t[:50]}'")
    for t,c in descs.items():
        if c>2 and t: geel.append(f"{c} pagina's hebben dezelfde meta description")
    for naam,tk in assets.items():
        lt.update(re.findall(r"\d+\s?[–-]\s?\d+ werkdagen",tk.lower()))
        if re.search(r"bestseller|meest verkocht",tk,re.I) and shop: blauw.append(f"{naam}: labels als 'Bestseller' in productdata; alleen tonen als het aantoonbaar klopt (nieuwe webshop heeft nog niets verkocht)")
    if btw_excl and btw_geen and min(btw_excl,btw_geen)<2: geel.append(f"btw-tekst: {btw_excl}x 'excl./zonder btw' tegenover {btw_geen}x 'geen/incl. btw'; controleer of dit een bewuste uitzondering is (bijv. tarief van een derde)")
    elif btw_excl and btw_geen: rood.append(f"btw-tekst tegenstrijdig: {btw_excl}x 'excl./zonder btw' en {btw_geen}x 'geen/incl. btw'. Kies één formulering die klopt voor de ondernemer.")
    if len(lt)>1: rood.append(f"verschillende levertijden op de site: {sorted(lt)}. Eén waarheid; bij dropshipping de langste levertijd tonen.")
    for naam,tk in assets.items():
        m=LEK.search(tk)
        if m: rood.append(f"{naam}: mogelijk gevoelige gegevens publiek leesbaar (sleutel '{(m.group(1) or m.group(2))}'); inkoopprijzen/marges/sleutels horen nooit in bestanden die iedereen kan downloaden")
    if shop:
        for k,txt in {"voorwaarden":"algemene voorwaarden","privacy":"privacyverklaring","retour":"retour-/herroepingsinformatie","contact":"contactgegevens","adres":"adres of vestigingsplaats van de verkoper (wettelijk verplicht voor webshops; invullen door de ondernemer)"}.items():
            if not trust[k]: rood.append(f"webshop mist {txt}")
    else:
        for k,txt in {"contact":"contactmogelijkheid","over":"'over ons'-pagina","reviews":"klantbewijs (reviews/cases)","privacy":"privacyverklaring"}.items():
            if not trust[k]: geel.append(f"site mist {txt}")
    if not trust["reviews"]: blauw.append("geen reviews/cases zichtbaar: alleen echte tonen, nooit verzinnen of kopen")
    blauw.append("handmatig: eigendom (wie is eigenaar van site/domein?), hosting/domeinkosten, levertijd, wat zit er niet in de prijs, foto's met rechten/licentie, productclaims vs leverancier")
    print(f"# Klantensite-blik: {doel}\n{len(pag)} pagina's, {len(assets)} scripts/data\n")
    for kop,lijst in (("🔴 Moet opgelost",rood),("🟡 Verbeteren",geel),("🔵 Handmatig verifiëren",blauw)):
        print(f"## {kop} ({len(lijst)})"); [print("- "+x) for x in lijst[:60]]; print()
    return 1 if rood else 0

if __name__=="__main__":
    if len(sys.argv)<2: sys.exit(__doc__)
    sys.exit(main(sys.argv[1]))
