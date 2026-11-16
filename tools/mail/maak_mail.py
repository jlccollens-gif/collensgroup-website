"""Collens Group prospectmail v2 (luxe, met concept-preview in 3 stijlen).
Gebruik: python3 -I maak_mail.py concept.json > uit.json
concept.json: {"taal":"nl|en","kicker":"Website-check","aanhef":"Goedendag team X,","kop":"...","alineas":["..."],
               "concept_url":"https://collensgroup.com/concept/<slug>/","prijs":"€995"}
Inline bijlagen in deze volgorde: att0 = banner-v2 (Drive 1QvhwGOfSiIr_kMRuGfzV_yCjLHnbtSzA), att1 = icon-v2 (Drive 1XVrhYr-fQ98PZASt1LHyZAFlM1jgoLxJ); NOOIT de oude met drie gele streepjes, att2 = preview (tools/mail/preview.py)."""
import json, sys, html
NAVY, GOLD, INK, MUTED, LINE = "#0f1726", "#f2b705", "#1a2233", "#5b6676", "#e6e8ec"

def maak(c):
    nl = c.get("taal", "nl") == "nl"; e = html.escape; u = c["concept_url"]
    stijlen = ("Klassiek", "Modern", "Minimal") if nl else ("Classic", "Modern", "Minimal")
    knop = "Bekijk uw nieuwe homepage" if nl else "View your new homepage"
    kies = "Kies uw stijl:" if nl else "Pick your style:"
    usps = (["Binnen een week live", f"Vaste prijs vanaf {c.get('prijs','€995')}", "Eerst zien, dan beslissen"] if nl
            else ["Live within a week", f"Fixed price from {c.get('prijs','€995')}", "See first, then decide"])
    afmeld = ("Geen interesse? Laat het weten, dan mail ik niet meer." if nl else "Not interested? Just let me know and I won't email again.")
    groet = "Met vriendelijke groet," if nl else "Kind regards,"
    P = f'style="margin:0 0 16px;font-size:15.5px;line-height:1.65;color:{INK}"'
    alineas = "".join(f"<p {P}>{e(a)}</p>" for a in c["alineas"])
    stijl_links = " &nbsp;·&nbsp; ".join(f'<a href="{e(u)}?stijl={i}" style="color:{INK};text-decoration:none;border-bottom:1px solid {GOLD};padding-bottom:1px">{s}</a>' for i, s in enumerate(stijlen, 1))
    usp_cells = "".join(f'<td align="center" style="padding:14px 8px;font-size:13px;color:{MUTED};border-right:1px solid {LINE}">{e(x)}</td>' for x in usps[:-1]) + \
                f'<td align="center" style="padding:14px 8px;font-size:13px;color:{MUTED}">{e(usps[-1])}</td>'
    h = f'''<!DOCTYPE html><html><body style="margin:0;padding:0;background:#f1f2f5">
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="background:#f1f2f5;padding:28px 0"><tr><td align="center">
<table role="presentation" width="640" cellpadding="0" cellspacing="0" style="width:640px;max-width:100%;background:#ffffff;font-family:Inter,'Segoe UI',Helvetica,Arial,sans-serif">
<tr><td style="background:{NAVY}"><img src="cid:att0" width="640" alt="Collens Group" style="display:block;width:100%;max-width:640px;height:auto;border:0"></td></tr>
<tr><td style="padding:44px 48px 6px">
<p style="margin:0 0 18px;font-size:11.5px;font-weight:600;letter-spacing:3px;color:#a07c00;text-transform:uppercase">{e(c["kicker"])}</p>
<h1 style="margin:0 0 22px;font-family:Georgia,'Times New Roman',serif;font-weight:normal;font-size:30px;line-height:1.2;color:{NAVY}">{e(c["kop"])}</h1>
<p {P}>{e(c["aanhef"])}</p>{alineas}
</td></tr>
<tr><td style="padding:10px 48px 0"><a href="{e(u)}" style="text-decoration:none"><img src="cid:att2" width="544" alt="{e(knop)}" style="display:block;width:100%;max-width:544px;height:auto;border:0;border-radius:8px"></a></td></tr>
<tr><td style="padding:18px 48px 0;font-size:14.5px;color:{MUTED}">{kies} &nbsp;{stijl_links}</td></tr>
<tr><td style="padding:26px 48px 8px"><table role="presentation" cellpadding="0" cellspacing="0"><tr><td style="background:{NAVY}">
<a href="{e(u)}" style="display:inline-block;padding:16px 30px;font-size:15px;font-weight:600;letter-spacing:.3px;color:#ffffff;text-decoration:none">{e(knop)} &rarr;</a></td></tr></table></td></tr>
<tr><td style="padding:26px 48px 0"><table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="border-top:1px solid {LINE};border-bottom:1px solid {LINE}"><tr>{usp_cells}</tr></table></td></tr>
<tr><td style="padding:30px 48px 8px"><p style="margin:0 0 14px;font-size:15px;color:{INK}">{groet}</p>
<table role="presentation" cellpadding="0" cellspacing="0"><tr>
<td style="padding-right:14px;vertical-align:middle"><img src="cid:att1" width="46" height="46" alt="Collens Group" style="display:block;border:0;border-radius:50%"></td>
<td style="vertical-align:middle;font-size:14px;line-height:1.5;color:{INK}"><strong style="font-size:15px">Jeffrey Collens</strong><br><span style="color:{MUTED}">Collens Group · {"websites, apps, games en AI" if nl else "websites, apps, games and AI"}</span><br>
<a href="https://collensgroup.com" style="color:{INK};text-decoration:none">collensgroup.com</a> <span style="color:{LINE}">|</span> <a href="mailto:info@collensgroup.com" style="color:{INK};text-decoration:none">info@collensgroup.com</a></td></tr></table></td></tr>
<tr><td style="padding:30px 48px 0"></td></tr>
<tr><td style="background:{NAVY};padding:16px 48px;font-size:12px;line-height:1.5;color:#9fb0c6">{e(afmeld)}</td></tr>
</table></td></tr></table></body></html>'''
    tekst = "\n\n".join([c["kop"], c["aanhef"], *c["alineas"], f"{knop}: {u}",
                         (kies + " " + ", ".join(f"{s} ({u}?stijl={i})" for i, s in enumerate(stijlen, 1))), " · ".join(usps), afmeld,
                         f"{groet}\nJeffrey Collens, Collens Group\ncollensgroup.com · info@collensgroup.com"])
    return {"htmlBody": h, "body": tekst}

if __name__ == "__main__":
    print(json.dumps(maak(json.load(open(sys.argv[1]))), ensure_ascii=False))
