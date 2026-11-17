# Concepten voor prospects
1. Voeg een prospect toe aan `concepten_data.py` (lijst C + EXTRA): alleen feiten van hun eigen site.
2. `python3 tools/concepten/maak_concepten.py` → `src/concept/<slug>/index.html` (3 stijlen, watermerk, herkenningscode `cgc-<slug>-<hash>`).
3. `python3 build.py && python3 qa.py`, commit bron + dist samen, push.
4. `concepten_register.json` = herkenningscodes + kernzinnen voor de wekelijkse diefstalcontrole.

## Contactsheet (vóór "getest")
`node tools/concepten/contactsheet.js /pad/uit.png slug1 slug2 ...` na `python3 build.py`: elk concept in Klassiek, Modern en Minimal op 390 px in één PNG (6 kolommen). Zelf bekijken vóór push.
