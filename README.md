# collensgroup.com

Statische website van Collens Group.

- Bron: `build.py` (+ `talen.py`, `landings.py`), stijl en afbeeldingen in `src/`.
- Bouwen: `python3 build.py` → resultaat in `dist/`.
- Hosting: Cloudflare Pages, publiceert de map `dist/` bij elke push naar `main`.

## Chat-adviseur (24/7)

- Backend: `functions/api/chat.js` (Cloudflare Pages Function op `/api/chat`), gebruikt Claude.
- Kennis (diensten, prijzen, FAQ): wordt bij elke build automatisch gemaakt in `chatbot/kennis.js` uit dezelfde gegevens als de site. Niet met de hand bewerken.
- Widget: `src/chat.js`, op elke pagina; op de startpagina's staat een sectie "Weet je nog niet precies wat je nodig hebt?".
- Widget en sectie blijven verborgen tot de sleutel is ingesteld.
- Geheimen in Cloudflare Pages → collensgroup-website → Settings → Variables and Secrets (Production):
  - `ANTHROPIC_API_KEY` (verplicht)
  - `BREVO_API_KEY` (om aanvragen uit de chat naar info@ te mailen)
  - optioneel `LEAD_EMAIL`, `CHAT_MODEL`
  Na het toevoegen een nieuwe deployment starten (Deployments → laatste → Retry deployment).
