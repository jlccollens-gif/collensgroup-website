"""Beginnersgids Claude AI van Jeffrey (akkoord 22-11-2026: subtiele vermelding op Over ons en de AI-pagina's).
Zet hier de verkooplink (Gumroad). Leeg = niets tonen op de site."""
BOEK_URL = ""
BOEK_TITEL = "Claude AI Beginnersgids"

def boek_alinea():
    if not BOEK_URL:
        return ""
    return (f'<p>Jeffrey schreef ook de <a href="{BOEK_URL}" rel="noopener" target="_blank">{BOEK_TITEL}</a>: '
            'een praktische werkgids voor ondernemers die AI voor zich willen laten werken, zonder technische kennis.</p>')

def boek_rel():
    return [(BOEK_URL, f"{BOEK_TITEL} (boek van Jeffrey)")] if BOEK_URL else []
