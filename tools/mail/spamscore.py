"""Spamscore van een prospectmail VOOR versturen (gratis, lokaal, geen account).
Gebruikt Apache SpamAssassin met de standaardregels in lokale modus (-L: geen DNS-/blacklisttests,
dus de echte score bij de ontvanger kan hoger zijn). Doel: v2-HTML en platte tekst vergelijken
en een mail tegenhouden die te veel regels raakt.

Installeren (1x per sessie): sudo apt-get update -qq && sudo apt-get install -y -qq spamassassin
Gebruik:
  python3 -I spamscore.py mail.json [banner.jpg icoon.jpg preview.jpg]
  mail.json = uitvoer van maak_mail.py ({"htmlBody":..., "body":...}) of {"body": "..."} voor platte tekst.
  Optioneel "onderwerp" en "aan" in mail.json. Met plaatjes: multipart/related zoals Gmail v2 verstuurt.
Uitvoer: score, geraakte regels en een oordeel. Drempel ons: < 2,0 = groen, 2,0-4,9 = oranje, >= 5 = rood (SA-standaard spam).
"""
import json, subprocess, sys
from email.message import EmailMessage
from email.utils import formatdate, make_msgid

def bouw(m, plaatjes):
    msg = EmailMessage()
    msg["Received"] = "from mail-sor-f41.google.com (mail-sor-f41.google.com. [209.85.220.41]) by mx.example.co.uk with SMTPS; " + formatdate()
    msg["From"] = "Jeffrey Collens <jlccollens@gmail.com>"
    msg["To"] = m.get("aan", "info@example.co.uk")
    msg["Subject"] = m.get("onderwerp", "Een nieuwe homepage, al voor u gemaakt")
    msg["Date"] = formatdate(localtime=False)
    msg["Message-ID"] = make_msgid(domain="mail.gmail.com")
    msg.set_content(m["body"])
    if m.get("htmlBody"):
        msg.add_alternative(m["htmlBody"], subtype="html")
        html_deel = msg.get_payload()[1]
        for i, p in enumerate(plaatjes):
            html_deel.add_related(open(p, "rb").read(), "image", "jpeg", cid=f"<att{i}>", filename=f"att{i}.jpg")
    return msg.as_bytes()

# Regels die alleen ontstaan doordat de test niet echt via Gmail loopt (tellen niet mee):
ARTEFACT = {"FORGED_GMAIL_RCVD", "NO_RECEIVED", "NO_RELAYS", "RCVD_IN_DNSWL_NONE", "DKIM_ADSP_CUSTOM_MED", "NML_ADSP_CUSTOM_MED"}

def score(raw):
    r = subprocess.run(["spamassassin", "-L", "-t", "--siteconfigpath=/etc/spamassassin", "-C", "/usr/share/spamassassin"], input=raw, capture_output=True)
    uit = r.stdout.decode("utf8", "replace")
    kop = next((l for l in uit.splitlines() if l.startswith("X-Spam-Status:")), "")
    regels, deel = [], uit.split("Content analysis details:")[-1]
    for l in deel.splitlines():
        p = l.split(None, 2)
        if len(p) >= 2 and p[0].replace(".", "").replace("-", "").isdigit():
            regels.append((float(p[0]), p[1], p[2].strip() if len(p) > 2 else ""))
    regels = [r for r in regels if r[1] not in ARTEFACT]
    s = round(sum(r[0] for r in regels), 1) if kop else None
    return s, regels

if __name__ == "__main__":
    m = json.load(open(sys.argv[1]))
    s, regels = score(bouw(m, sys.argv[2:]))
    oordeel = "GROEN" if s is not None and s < 2 else ("ORANJE" if s is not None and s < 5 else "ROOD")
    print(f"SCORE {s} -> {oordeel}")
    for pt, naam, uitleg in sorted(regels, reverse=True):
        print(f"  {pt:+.1f} {naam}: {uitleg}")
    sys.exit(0 if oordeel != "ROOD" else 1)
