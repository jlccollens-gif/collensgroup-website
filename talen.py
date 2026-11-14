# Extra talen voor buitenlandse klanten: één volledige startpagina per taal (diensten, prijzen, werkwijze, FAQ, contact).
# Prijzen in euro, dezelfde als op de NL/EN-site. Alleen feiten die ook op de rest van de site staan.

TALEN = {
 "de": {
  "naam": "Deutsch", "trust": ['Festpreis im Voraus', 'Zuerst ein kostenloses Konzept', 'Code und Design gehören Ihnen'], "og": "de_DE", "skip": "Zum Inhalt", "menu": "Schnellmenü", "hoofdmenu": "Hauptmenü",
  "title": "Websites, Apps, Games und KI zu fairen Festpreisen | Collens Group",
  "desc": "Websites ab 495 €, Apps ab 3.150 €, Games ab 1.950 € und KI-Automatisierung ab 395 €. Festpreis und kostenloses Konzept.",
  "nav": [("#leistungen", "Leistungen"), ("#preise", "Preise"), ("en-projects.html", "Projekte")],
  "cta": ("Angebot anfordern", "Angebot"),
  "h1": "Ihre Idee. Blitzschnell live.",
  "lead": "Kostenloses Konzept in 48 Stunden. Websites ab 495 €, dazu Apps, Games und KI. Festpreis.",
  "cta1": "Kostenloses Angebot", "cta2": "Unsere Leistungen",
  "s_kop": "Was wir bauen", "s_intro": "Alles Digitale aus einer Hand, zu Festpreisen.",
  "diensten": [("Websites", "One-Page-Website", "ab 495 €"), ("Apps", "iPhone und Android", "ab 3.150 €"), ("Games", "Casual-2D-Games", "ab 1.950 €"), ("KI & Automatisierung", "Chatbots und Workflows", "ab 395 €")],
  "feiten": [("Festpreis", "Sie kennen den Preis, bevor wir starten. Mehraufwand nur mit Ihrer Zustimmung."), ("Alles gehört Ihnen", "Keine Bindung an eine Plattform. Nach der Zahlung gehört der Code Ihnen."), ("Kostenloses Konzept", "Sehen Sie ein klickbares Konzept, bevor Sie entscheiden."), ("Weltweit, online", "Wir arbeiten per E-Mail und Video, auf Englisch oder Niederländisch.")],
  "p_kop": "Preise", "p_intro": "Startpreise in Euro. Nach einem kurzen Intake per E-Mail erhalten Sie ein Festpreisangebot.", "klaar": "Fertig in",
  "prijzen": [("Websites", [("One-Page-Website", "495 €", "3–5 Tage"), ("Unternehmenswebsite (bis 6 Seiten)", "995 €", "2–3 Wochen"), ("Onlineshop (bis 50 Produkte)", "1.950 €", "3–5 Wochen")]),
              ("Apps (iOS und Android)", [("Basis / MVP-App (bis 5 Screens)", "3.150 €", "3–5 Wochen"), ("Standard-App (Konten, Datenbank, Push)", "6.750 €", "6–10 Wochen"), ("Individuelle App (Zahlungen, Admin, Rollen)", "13.050 €", "10–16+ Wochen")]),
              ("Games (Casual 2D)", [("Marken-Minispiel (Web)", "1.950 €", "2–3 Wochen"), ("Casual Game", "4.950 €", "4–6 Wochen"), ("2D-Game mit Levels", "9.950 €", "8–12 Wochen")]),
              ("KI & Automatisierung", [("Automatisierung (1 Workflow)", "395 €", "2–5 Tage"), ("KI-Chatbot mit Ihren Inhalten", "995 €", "1 Woche"), ("KI-Assistent (mehrere Workflows)", "1.950 €", "2–4 Wochen")])],
  "vanaf": "ab",
  "p_noot": "Wartung ab 29 € pro Monat (Websites) oder 85,50 € pro Monat (Apps und Games). Externe Kosten wie Domain, Hosting und Store-Konten werden immer separat ausgewiesen.",
  "w_kop": "So läuft es ab", "w_intro": "Jeder Schritt endet mit Ihrer Freigabe.",
  "stappen": [("Intake per E-Mail", "Beantworten Sie ein paar kurze Fragen zu Idee, Nutzern und Budget."), ("Kostenloses Konzept", "Ein klickbares Konzept mit 1–3 Screens."), ("Festpreisangebot", "Preis, Zeitplan und genau, was enthalten ist."), ("Bauen und testen", "Jede Woche eine neue Testversion."), ("Launch", "Wir helfen bei der Veröffentlichung im Web, App Store oder Google Play.")],
  "o_kop": "Eigene Projekte", "o_tekst": "Wir bauen auch für uns selbst: eine Reise-App, zwei Games und eine Animationsserie.", "o_link": "Projekte ansehen",
  "f_kop": "Häufige Fragen",
  "faq": [("Arbeiten Sie mit Kunden außerhalb der Niederlande?", "Ja. Wir arbeiten vollständig online mit Kunden weltweit, auf Englisch oder Niederländisch. Die Preise sind in Euro."),
          ("Warum sind Ihre Preise niedriger als bei den meisten Agenturen?", "Wir bauen eine App für iPhone und Android gleichzeitig, nutzen bewährte Bausteine und automatisieren viel. Das spart Stunden, und diese Ersparnis sehen Sie im Preis."),
          ("Gehört mir das Ergebnis?", "Ja. Nach der letzten Zahlung gehören Code, Design und Inhalte Ihnen. Apps werden in Ihren eigenen Apple- und Google-Konten veröffentlicht."),
          ("Wie bezahle ich?", "In drei Teilen: 40 % zum Start, 40 % bei Freigabe der Testversion und 20 % bei Lieferung."),
          ("Kann ich etwas sehen, bevor ich bezahle?", "Ja. Nach einem kurzen Intake per E-Mail erstellen wir ein kostenloses klickbares Konzept mit 1–3 Screens.")],
  "contact": {"kop": "Erzählen Sie uns von Ihrem Projekt", "tekst": "Beschreiben Sie, was Sie bauen möchten. Sie erhalten schnell eine Antwort mit ein paar kurzen Fragen und danach einen Festpreis. Alles per E-Mail, kostenlos und unverbindlich.",
              "naam": "Name", "email": "E-Mail", "bedrijf": "Firma (optional)", "wat": "Was brauchen Sie?", "opts": ["Noch unklar", "App", "Website oder Onlineshop", "Game", "KI oder Automatisierung"],
              "idee": "Ihre Idee", "ph": "Was soll es können, und für wen?", "knop": "Anfrage senden", "mail": "Lieber per E-Mail? ", "fout": "Bitte geben Sie Ihren Namen, eine gültige E-Mail-Adresse und Ihre Idee ein.",
              "klaar": "Ihre Anfrage ist bereit. Wählen Sie, wie Sie sie senden:", "viamail": "Per E-Mail", "kopie": "Anfrage kopieren", "gekopieerd": "Kopiert", "selecteer": "Text oben markieren und kopieren"},
  "footer": "Websites, Apps, Games und KI · weltweit",
 },
 "fr": {
  "naam": "Français", "trust": ["Prix fixe à l'avance", "D'abord un concept gratuit", 'Le code et le design sont à vous'], "og": "fr_FR", "skip": "Aller au contenu", "menu": "Menu rapide", "hoofdmenu": "Menu principal",
  "title": "Sites web, applis, jeux et IA à prix fixes justes | Collens Group",
  "desc": "Sites web dès 495 €, applis dès 3 150 €, jeux dès 1 950 € et automatisation IA dès 395 €. Prix fixe et concept gratuit.",
  "nav": [("#services", "Services"), ("#tarifs", "Tarifs"), ("en-projects.html", "Projets")],
  "cta": ("Demander un devis", "Devis"),
  "h1": "Votre idée. En ligne en un éclair.",
  "lead": "Concept gratuit en 48 heures. Sites web dès 495 €, plus applis, jeux et IA. Prix fixe.",
  "cta1": "Devis gratuit", "cta2": "Nos services",
  "s_kop": "Ce que nous créons", "s_intro": "Tout le numérique sous un même toit, à prix fixes.",
  "diensten": [("Sites web", "Site d'une page", "dès 495 €"), ("Applis", "iPhone et Android", "dès 3 150 €"), ("Jeux", "Jeux 2D casual", "dès 1 950 €"), ("IA & automatisation", "Chatbots et workflows", "dès 395 €")],
  "feiten": [("Prix fixe", "Vous connaissez le prix avant que nous commencions. Travail supplémentaire uniquement avec votre accord."), ("Tout vous appartient", "Aucune dépendance à une plateforme. Après paiement, le code est à vous."), ("Concept gratuit", "Découvrez un concept cliquable avant de décider."), ("Partout, en ligne", "Nous travaillons par e-mail et visio, en anglais ou en néerlandais.")],
  "p_kop": "Tarifs", "p_intro": "Prix de départ en euros. Après un court échange par e-mail, vous recevez un devis à prix fixe.", "klaar": "Prêt en",
  "prijzen": [("Sites web", [("Site d'une page", "495 €", "3–5 jours"), ("Site d'entreprise (jusqu'à 6 pages)", "995 €", "2–3 semaines"), ("Boutique en ligne (jusqu'à 50 produits)", "1 950 €", "3–5 semaines")]),
              ("Applis (iOS et Android)", [("Appli Basique / MVP (jusqu'à 5 écrans)", "3 150 €", "3–5 semaines"), ("Appli Standard (comptes, base de données, notifications)", "6 750 €", "6–10 semaines"), ("Appli sur mesure (paiements, admin, rôles)", "13 050 €", "10–16+ semaines")]),
              ("Jeux (2D casual)", [("Mini-jeu de marque (web)", "1 950 €", "2–3 semaines"), ("Jeu casual", "4 950 €", "4–6 semaines"), ("Jeu 2D avec niveaux", "9 950 €", "8–12 semaines")]),
              ("IA & automatisation", [("Automatisation (1 workflow)", "395 €", "2–5 jours"), ("Chatbot IA formé sur vos contenus", "995 €", "1 semaine"), ("Assistant IA (plusieurs workflows)", "1 950 €", "2–4 semaines")])],
  "vanaf": "dès",
  "p_noot": "Maintenance dès 29 € par mois (sites web) ou 85,50 € par mois (applis et jeux). Les frais externes comme le domaine, l'hébergement et les comptes des stores sont toujours indiqués séparément.",
  "w_kop": "Comment ça marche", "w_intro": "Chaque étape se termine par votre validation.",
  "stappen": [("Échange par e-mail", "Répondez à quelques questions sur votre idée, vos utilisateurs et votre budget."), ("Concept gratuit", "Un concept cliquable de 1 à 3 écrans."), ("Devis à prix fixe", "Prix, planning et ce qui est inclus, précisément."), ("Développement et tests", "Une nouvelle version de test chaque semaine."), ("Lancement", "Nous vous aidons à publier sur le web, l'App Store ou Google Play.")],
  "o_kop": "Nos propres projets", "o_tekst": "Nous créons aussi pour nous-mêmes : une appli de voyage, deux jeux et une série animée.", "o_link": "Voir nos projets",
  "f_kop": "Questions fréquentes",
  "faq": [("Travaillez-vous avec des clients hors des Pays-Bas ?", "Oui. Nous travaillons entièrement en ligne avec des clients du monde entier, en anglais ou en néerlandais. Les prix sont en euros."),
          ("Pourquoi vos prix sont-ils plus bas que ceux de la plupart des agences ?", "Nous créons une seule appli pour iPhone et Android à la fois, utilisons des briques éprouvées et automatisons beaucoup de travail. Cela fait gagner des heures, et vous le voyez dans le prix."),
          ("Le résultat m'appartient-il ?", "Oui. Après le dernier paiement, le code, le design et les contenus sont à vous. Les applis sont publiées sur vos propres comptes Apple et Google."),
          ("Comment se passe le paiement ?", "En trois fois : 40 % au démarrage, 40 % à la validation de la version de test et 20 % à la livraison."),
          ("Puis-je voir quelque chose avant de payer ?", "Oui. Après un court échange par e-mail, nous réalisons un concept cliquable gratuit de 1 à 3 écrans.")],
  "contact": {"kop": "Parlez-nous de votre projet", "tekst": "Décrivez ce que vous voulez créer. Vous recevez rapidement une réponse avec quelques questions, puis un prix fixe. Tout par e-mail, gratuit et sans engagement.",
              "naam": "Nom", "email": "E-mail", "bedrijf": "Entreprise (facultatif)", "wat": "De quoi avez-vous besoin ?", "opts": ["Je ne sais pas encore", "Appli", "Site web ou boutique", "Jeu", "IA ou automatisation"],
              "idee": "Votre idée", "ph": "Que doit-il faire, et pour qui ?", "knop": "Envoyer la demande", "mail": "Plutôt par e-mail ? ", "fout": "Veuillez indiquer votre nom, une adresse e-mail valide et votre idée.",
              "klaar": "Votre demande est prête. Choisissez comment l'envoyer :", "viamail": "Par e-mail", "kopie": "Copier la demande", "gekopieerd": "Copié", "selecteer": "Sélectionnez le texte ci-dessus et copiez-le"},
  "footer": "Sites web, applis, jeux et IA · dans le monde entier",
 },
 "es": {
  "naam": "Español", "trust": ['Precio fijo por adelantado', 'Primero un concepto gratis', 'El código y el diseño son tuyos'], "og": "es_ES", "skip": "Ir al contenido", "menu": "Menú rápido", "hoofdmenu": "Menú principal",
  "title": "Webs, apps, juegos e IA a precios fijos justos | Collens Group",
  "desc": "Webs desde 495 €, apps desde 3.150 €, juegos desde 1.950 € y automatización con IA desde 395 €. Precio fijo y concepto gratis.",
  "nav": [("#servicios", "Servicios"), ("#precios", "Precios"), ("en-projects.html", "Proyectos")],
  "cta": ("Pedir presupuesto", "Contacto"),
  "h1": "Tu idea. Online en tiempo récord.",
  "lead": "Concepto gratis en 48 horas. Webs desde 495 €, además de apps, juegos e IA. Precio fijo.",
  "cta1": "Presupuesto gratis", "cta2": "Nuestros servicios",
  "s_kop": "Qué creamos", "s_intro": "Todo lo digital bajo un mismo techo, a precios fijos.",
  "diensten": [("Webs", "Web de una página", "desde 495 €"), ("Apps", "iPhone y Android", "desde 3.150 €"), ("Juegos", "Juegos 2D casuales", "desde 1.950 €"), ("IA y automatización", "Chatbots y flujos de trabajo", "desde 395 €")],
  "feiten": [("Precio fijo", "Conoces el precio antes de empezar. Trabajo extra solo con tu aprobación."), ("Todo es tuyo", "Sin ataduras a ninguna plataforma. Tras el pago, el código es tuyo."), ("Concepto gratis", "Ve un concepto interactivo antes de decidir."), ("En todo el mundo, online", "Trabajamos por correo y videollamada, en inglés o neerlandés.")],
  "p_kop": "Precios", "p_intro": "Precios de partida en euros. Tras una breve conversación por correo recibes un presupuesto cerrado.", "klaar": "Listo en",
  "prijzen": [("Webs", [("Web de una página", "495 €", "3–5 días"), ("Web de empresa (hasta 6 páginas)", "995 €", "2–3 semanas"), ("Tienda online (hasta 50 productos)", "1.950 €", "3–5 semanas")]),
              ("Apps (iOS y Android)", [("App Básica / MVP (hasta 5 pantallas)", "3.150 €", "3–5 semanas"), ("App Estándar (cuentas, base de datos, notificaciones)", "6.750 €", "6–10 semanas"), ("App a medida (pagos, panel de administración, roles)", "13.050 €", "10–16+ semanas")]),
              ("Juegos (2D casual)", [("Minijuego de marca (web)", "1.950 €", "2–3 semanas"), ("Juego casual", "4.950 €", "4–6 semanas"), ("Juego 2D con niveles", "9.950 €", "8–12 semanas")]),
              ("IA y automatización", [("Automatización (1 flujo)", "395 €", "2–5 días"), ("Chatbot con IA entrenado con tu contenido", "995 €", "1 semana"), ("Asistente con IA (varios flujos)", "1.950 €", "2–4 semanas")])],
  "vanaf": "desde",
  "p_noot": "Mantenimiento desde 29 € al mes (webs) o 85,50 € al mes (apps y juegos). Los costes externos como dominio, alojamiento y cuentas de las tiendas siempre se indican por separado.",
  "w_kop": "Cómo trabajamos", "w_intro": "Cada paso termina con tu aprobación.",
  "stappen": [("Conversación por correo", "Responde unas preguntas breves sobre tu idea, tus usuarios y tu presupuesto."), ("Concepto gratis", "Un concepto interactivo de 1 a 3 pantallas."), ("Presupuesto cerrado", "Precio, plazos y exactamente qué incluye."), ("Desarrollo y pruebas", "Una nueva versión de prueba cada semana."), ("Lanzamiento", "Te ayudamos a publicar en la web, App Store o Google Play.")],
  "o_kop": "Proyectos propios", "o_tekst": "También creamos para nosotros: una app de viajes, dos juegos y una serie de animación.", "o_link": "Ver proyectos",
  "f_kop": "Preguntas frecuentes",
  "faq": [("¿Trabajáis con clientes fuera de los Países Bajos?", "Sí. Trabajamos totalmente online con clientes de todo el mundo, en inglés o neerlandés. Los precios están en euros."),
          ("¿Por qué vuestros precios son más bajos que los de la mayoría de agencias?", "Creamos una sola app para iPhone y Android a la vez, usamos componentes probados y automatizamos mucho trabajo. Eso ahorra horas, y se nota en el precio."),
          ("¿El resultado es mío?", "Sí. Tras el último pago, el código, el diseño y el contenido son tuyos. Las apps se publican en tus propias cuentas de Apple y Google."),
          ("¿Cómo se paga?", "En tres partes: 40 % al empezar, 40 % al aprobar la versión de prueba y 20 % a la entrega."),
          ("¿Puedo ver algo antes de pagar?", "Sí. Tras una breve conversación por correo hacemos un concepto interactivo gratis de 1 a 3 pantallas.")],
  "contact": {"kop": "Cuéntanos tu proyecto", "tekst": "Describe lo que quieres crear. Recibirás pronto una respuesta con unas preguntas breves y después un precio fijo. Todo por correo, gratis y sin compromiso.",
              "naam": "Nombre", "email": "Correo electrónico", "bedrijf": "Empresa (opcional)", "wat": "¿Qué necesitas?", "opts": ["Aún no lo sé", "App", "Web o tienda online", "Juego", "IA o automatización"],
              "idee": "Tu idea", "ph": "¿Qué debe hacer y para quién?", "knop": "Enviar solicitud", "mail": "¿Prefieres el correo? ", "fout": "Indica tu nombre, un correo válido y tu idea.",
              "klaar": "Tu solicitud está lista. Elige cómo enviarla:", "viamail": "Por correo", "kopie": "Copiar solicitud", "gekopieerd": "Copiado", "selecteer": "Selecciona el texto de arriba y cópialo"},
  "footer": "Webs, apps, juegos e IA · en todo el mundo",
 },
}

exec(open(__import__("os").path.join(__import__("os").path.dirname(__file__), "talen_azie.py"), encoding="utf-8").read())
TALEN["th"] = TH
TALEN["my"] = MY


def contact_lang(contact_section, T):
    c = T["contact"]
    h = contact_section()
    nl_opts = ["Weet ik nog niet", "App", "Website of webshop", "Game", "AI of automatisering"]
    pairs = [("Vertel over je app-idee", c["kop"]),
             ("Beschrijf kort wat je wilt bouwen. Je krijgt snel een reactie met een paar korte vragen, en daarna een vaste prijs. Alles per mail, gratis en zonder verplichtingen.", c["tekst"]),
             (">Naam<", ">" + c["naam"] + "<"), (">E-mail<", ">" + c["email"] + "<"), ("Bedrijf (optioneel)", c["bedrijf"]),
             ("Wat wil je laten maken?", c["wat"]),
             (">Je idee<", ">" + c["idee"] + "<"), ("Wat moet de app doen, en voor wie?", c["ph"]),
             ("Verstuur aanvraag", c["knop"]), ('"Liever direct mailen? "', '"' + c["mail"] + '"'),
             ("Vul je naam, een geldig e-mailadres en je idee in.", c["fout"]),
             ("Je aanvraag staat klaar. Kies hoe je hem verstuurt:", c["klaar"]),
             ('"Via e-mail"', '"' + c["viamail"] + '"'), ('"Kopieer aanvraag"', '"' + c["kopie"] + '"'), ('"Gekopieerd"', '"' + c["gekopieerd"] + '"'),
             ('"Selecteer de tekst hierboven en kopieer"', '"' + c["selecteer"] + '"')]
    for a, b in zip(nl_opts, c["opts"]):
        pairs.append((f"<option>{a}</option>", f"<option>{b}</option>"))
    for a, b in pairs:
        h = h.replace(a, b)
    return h


VINK='<svg viewBox="0 0 20 20" width="18" height="18" aria-hidden="true"><circle cx="10" cy="10" r="10" fill="#E3EBFA"/><path d="M6 10.3l2.6 2.6L14.2 7.4" fill="none" stroke="#2457D6" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg>'

def taal_paginas(page, e, faq_html, faq_ld, contact_section, pages, icoon=lambda n: ''):
    for code, T in TALEN.items():
        ids = [h.lstrip("#") for h, _ in T["nav"][:2]]
        diensten = '<div class="diensten">' + "".join(
            f'<a class="dienst" href="#{ids[1]}" style="--k:{k}">{icoon(sleutel)}<span class="dienst-naam">{e(n)}</span><span class="dienst-sub">{e(s)}</span><span class="dienst-prijs">{e(p)}</span></a>'
            for (n, s, p), k, sleutel in zip(T["diensten"], ["#2457D6", "#14213D", "#7A3BD1", "#0E7C86"], ["Websites", "Apps", "Games", "AI"])) + '</div>'
        feiten = "".join(f'<div><h3>{e(a)}</h3><p>{e(b)}</p></div>' for a, b in T["feiten"])
        prijzen = "".join(f'<div class="prijsblok"><h3>{e(cat)}</h3><table class="lijst">' +
                          "".join(f'<tr><td>{e(n)}<small>{e(T["klaar"])} {e(t)}</small></td><td>{e((T["vanaf"] + " " + p + " " + T.get("vanaf_na", "")).strip())}</td></tr>' for n, p, t in rows) + '</table></div>'
                          for cat, rows in T["prijzen"])
        stappen = "".join(f'<li><h3>{e(a)}</h3><p>{e(b)}</p></li>' for a, b in T["stappen"])
        offers = [{"@type": "Offer", "name": n, "price": int(p.replace("€", "").replace(".", "").replace(",", "").replace(" ", "").replace(" ", "")), "priceCurrency": "EUR"} for _, rows in T["prijzen"] for n, p, _ in rows]
        body = f'''<section class="hero" aria-labelledby="kop"><div class="wrap"><div>
<h1 id="kop">{e(T["h1"])}</h1>
<p class="lead">{e(T["lead"])}</p>
<div class="acties"><a class="knop geel" href="#contact">{e(T["cta1"])}</a><a class="zacht" href="#{ids[0]}">{e(T["cta2"])}</a></div><ul class="vertrouwen">{"".join(f'<li>{VINK}{e(x)}</li>' for x in T["trust"])}</ul></div>
<div class="etalage"><figure class="tel-links"><img src="img/koffer-spel.jpg" alt="Koffer Vol!" width="240" height="480"></figure><figure class="tel-midden"><img src="img/lubbyc-kaart.jpg" alt="LubbyC" width="240" height="480" fetchpriority="high"></figure><figure class="tel-rechts"><img src="img/eiland-rood.jpg" alt="Island Express" width="240" height="480"></figure></div></div></section>
<section id="{ids[0]}" class="wit" aria-labelledby="s-kop"><div class="wrap">
<div class="intro"><h2 id="s-kop">{e(T["s_kop"])}</h2><p>{e(T["s_intro"])}</p></div>
{diensten}
<div class="feiten" style="margin-top:48px">{feiten}</div></div></section>
<section id="{ids[1]}" aria-labelledby="p-kop"><div class="wrap">
<div class="intro"><h2 id="p-kop">{e(T["p_kop"])}</h2><p>{e(T["p_intro"])}</p></div>
<div class="prijsgrid">{prijzen}</div>
<p class="noot">{e(T["p_noot"])}</p></div></section>
<section class="donker" aria-labelledby="w-kop"><div class="wrap">
<div class="intro"><h2 id="w-kop">{e(T["w_kop"])}</h2><p>{e(T["w_intro"])}</p></div>
<ol class="stappen">{stappen}</ol></div></section>
<section class="wit" aria-labelledby="o-kop"><div class="wrap">
<div class="intro"><h2 id="o-kop">{e(T["o_kop"])}</h2><p>{e(T["o_tekst"])} <a href="en-projects.html">{e(T["o_link"])}</a>.</p></div></div></section>
<section aria-labelledby="f-kop"><div class="wrap" style="max-width:820px">
<h2 id="f-kop">{e(T["f_kop"])}</h2>{faq_html(T["faq"])}</div></section>
{contact_lang(contact_section, T)}'''
        pages.append(page(f"{code}.html", T["title"], T["desc"], body, crumbs=[("Home", f"{code}.html")],
                          extra_ld=[faq_ld(T["faq"]), {"@type": "Service", "name": T["s_kop"], "provider": {"@id": "#org"}, "areaServed": "Worldwide", "offers": offers}],
                          lang=code))
