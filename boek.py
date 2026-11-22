"""Boek van Jeffrey (akkoord 22-11-2026: boekpagina + subtiele vermelding op Over ons en de AI-pagina's).
Deel 1 staat op Gumroad (winkel collens3). Leeg BOEK_URL = niets tonen op de site."""
BOEK_URL = "https://collens3.gumroad.com/l/claude-voor-beginners"
BOEK_TITEL = "Claude voor beginners"
BOEK_PAGINA = "boek-claude-voor-beginners.html"

def boek_alinea():
    if not BOEK_URL:
        return ""
    return (f'<p>Jeffrey schreef ook het boek <a href="{BOEK_PAGINA}">{BOEK_TITEL}</a>: '
            'een praktische gids in gewoon Nederlands, van je eerste vraag aan Claude tot je eigen AI-assistent, zonder technische kennis.</p>')

def boek_rel():
    return [(BOEK_PAGINA, f"Boek: {BOEK_TITEL}")] if BOEK_URL else []
