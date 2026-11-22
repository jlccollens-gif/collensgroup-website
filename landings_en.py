"""Engelse pagina's die de Nederlandse aanvullen (zelfde structuur als LANDINGS in landings.py).
Alleen feiten die ook op de Nederlandse pagina's staan: pakketten, prijzen, levertijden, onderhoud.
Opdracht eigenaar 22-11-2026: "Pas mijn website ook aan voor buitenlandse bezoekers. Net zo goed als de Nederlandse."
"""

FINAL = "All prices are final prices in euros: no VAT is added."

EN_EXTRA = [
 {"slug": "en-pricing", "lang": "en", "kort": "Pricing",
  "titel": "Prices for websites, apps, games and AI | Collens Group",
  "desc": "All our prices in one place: websites from €495, web shops from €1,950, games from €1,950, AI automation from €395, apps from €3,150. Fixed up front.",
  "h1": "Pricing: websites, apps, games and AI",
  "lead": "Every price in one place. You get a fixed price before we start and a free concept within 48 hours. " + FINAL,
  "secties": [
   ("Websites and web shops", "<div class='scroll'><table class='tabel vergelijk'><tr><th>Package</th><th>Includes</th><th>Ready in</th><th>From</th></tr>"
    "<tr><td>One-page website</td><td>All key information on one page, contact form, fast and mobile-friendly</td><td>3–5 days</td><td>€495</td></tr>"
    "<tr><td>Business website</td><td>Up to 6 pages, copy written for Google, contact and quote form</td><td>2–3 weeks</td><td>€995</td></tr>"
    "<tr><td>Web shop</td><td>Up to 50 products set up, online payments, shipping</td><td>3–5 weeks</td><td>€1,950</td></tr>"
    "<tr><td>Extra page</td><td>Per page, including SEO copy</td><td>–</td><td>€95</td></tr>"
    "<tr><td>Website maintenance</td><td>Updates, backups, small changes up to 30 minutes a month</td><td>–</td><td>€29 / month</td></tr></table></div>"),
   ("Games", "<div class='scroll'><table class='tabel vergelijk'><tr><th>Package</th><th>Includes</th><th>Ready in</th><th>From</th></tr>"
    "<tr><td>Branded game</td><td>Browser game in your brand style, 1 game mechanic (for example a quiz or reaction game), leaderboard and share button</td><td>2–3 weeks</td><td>€1,950</td></tr>"
    "<tr><td>Casual game</td><td>1 fully developed game mechanic, sound and animation, for iOS, Android or browser</td><td>4–6 weeks</td><td>€4,950</td></tr>"
    "<tr><td>2D game with levels</td><td>Several levels and progress, your own characters and world, live in the App Store and Google Play</td><td>8–12 weeks</td><td>€9,950</td></tr>"
    "<tr><td>Extra level or game mode</td><td>After the first version</td><td>–</td><td>€395</td></tr>"
    "<tr><td>Game maintenance</td><td>Updates for new iOS and Android versions</td><td>–</td><td>€85.50 / month</td></tr></table></div>"),
   ("AI and automation", "<div class='scroll'><table class='tabel vergelijk'><tr><th>Package</th><th>Includes</th><th>Ready in</th><th>From</th></tr>"
    "<tr><td>Automation</td><td>1 workflow that connects your existing apps, tested and documented</td><td>2–5 days</td><td>€395</td></tr>"
    "<tr><td>AI chatbot</td><td>Answers questions on your website, trained on your own content, passes doubtful questions to you</td><td>1 week</td><td>€995</td></tr>"
    "<tr><td>AI assistant</td><td>Several workflows and integrations: email, calendar, documents and CRM, you keep the final say</td><td>2–4 weeks</td><td>€1,950</td></tr>"
    "<tr><td>Extra workflow</td><td>Per additional automation</td><td>–</td><td>€195</td></tr>"
    "<tr><td>Management</td><td>Monitoring and small changes</td><td>–</td><td>€49 / month</td></tr></table></div>"),
   ("Apps for iPhone and Android", "<div class='scroll'><table class='tabel vergelijk'><tr><th>Package</th><th>Includes</th><th>Ready in</th><th>From</th></tr>"
    "<tr><td>Basic / MVP app</td><td>Up to 5 screens, ready to publish on iOS or Android</td><td>3–5 weeks</td><td>€3,150</td></tr>"
    "<tr><td>Standard app</td><td>5 to 12 screens, accounts, database, push notifications</td><td>6–10 weeks</td><td>€6,750</td></tr>"
    "<tr><td>Custom / Pro app</td><td>12+ screens, backend, payments, user roles</td><td>10–16+ weeks</td><td>€13,050</td></tr>"
    "<tr><td>Development by the hour</td><td>Extensions and smaller jobs</td><td>–</td><td>€67.50 / hour</td></tr>"
    "<tr><td>Basic maintenance</td><td>Monitoring, critical bug fixes, small updates</td><td>–</td><td>€85.50 / month</td></tr>"
    "<tr><td>Growth &amp; Support</td><td>Everything in Basic, up to 4 hours of changes, priority support</td><td>–</td><td>€265.50 / month</td></tr></table></div>"),
   ("What \"from\" means", "<p>\"From\" is the price of the package as described above. If your project needs more, you get a fixed price for it before we start, never an open-ended bill. External costs, such as a domain name (usually about €10 to €25 a year), platform fees or Apple and Google developer accounts, are listed in your quote. " + FINAL + "</p>")],
  "faq": [("Do your prices include VAT?", "Our prices are final prices in euros: no VAT is added. What you see in the quote is what you pay for our work. External costs, such as a domain name, store accounts or payment provider fees, are paid directly to those parties and are listed in the quote up front."),
          ("How do I pay?", "For apps, in three parts: 40% when you approve the quote, 40% when you approve the test version and 20% on delivery. That way you never pay everything up front and always see results first. For smaller jobs, such as a website or automation, the payment terms are stated in the quote. All prices are final prices in euros."),
          ("Can I see something before I pay?", "Yes. You get a free concept within 48 hours, designed specifically for your business, with no obligation. Only if you like it do we make a fixed price. If it is not for you, you have paid nothing and are not committed to anything."),
          ("Do you work with clients outside the Netherlands?", "Yes. We work fully online, by email and video, with clients worldwide, in English or Dutch. Prices are the same final prices in euros everywhere, with no VAT added. Time zones are rarely a problem: most of the work is done in writing, and calls are planned at a time that suits you.")],
  "offers": [("One-page website", 495), ("Business website", 995), ("Web shop", 1950), ("Branded game", 1950), ("Automation", 395), ("AI chatbot", 995), ("Basic / MVP app", 3150)],
  "rel": [("en.html", "Home"), ("en-website-design.html", "Website design"), ("en-app-development.html", "App development"), ("en-about.html", "About us")]},

 {"slug": "en-web-shop", "lang": "en", "kort": "Web shop",
  "titel": "Web shop design from €1,950, fixed price | Collens Group",
  "desc": "A fast, mobile-friendly web shop where you manage your own products. From €1,950 with up to 50 products set up, ready in 3–5 weeks. Free concept first.",
  "h1": "Web shop design for small businesses",
  "lead": "A web shop that loads fast, works well on a phone and lets you manage your own products, stock and orders. From €1,950 with up to 50 products already set up for you, ready in 3–5 weeks.",
  "secties": [
   ("What's included", "<ul><li>Up to 50 products set up, with the photos and texts you supply</li><li>Online payments with the payment methods your customers use</li><li>Shipping costs set up</li><li>Fast and mobile-friendly</li><li>You manage your own products, stock and orders</li></ul>"),
   ("Running costs", "<p>A domain name usually costs about €10 to €25 a year. The shop platform and the payment provider charge their own fees; we list them in your quote so there are no surprises. Maintenance is optional from €29 a month.</p>"),
   ("How it works", "<ol><li>Tell us by email what you sell and to whom.</li><li>You get a free concept of the homepage and a product page, designed for your shop.</li><li>After you approve, we build the shop and set up payments and shipping.</li><li>You test everything yourself, then the shop goes live.</li></ol>"),
   ("What a shop can look like", "<p>An example of a complete web shop with basket, checkout and management is <a href='concept/suismuis/'>Suismuis Home</a>, a shop for home accessories. It is a concept version and has not launched yet. Our own apps and games are on the <a href='en-projects.html'>projects page</a>.</p>")],
  "faq": [("Can I add more products later?", "Yes, you do that yourself in the admin, without technical knowledge. There is no limit on what you add later. At delivery we show you how to change products, photos, prices and stock. With the package we already set up your first 50 products, so your shop is ready to sell from day one."),
          ("Do I own the web shop?", "Yes. The shop, the domain and the content are registered in your name, as are your customer and order data. You are not tied to us: if you later want to work with someone else, you take everything with you."),
          ("What does \"from €1,950\" mean?", "It is the price of the package described here: a shop with up to 50 products, payments and shipping. If you need more, for example a special integration, you get a fixed price up front. " + FINAL),
          ("Do you build shops for businesses outside the Netherlands?", "Yes. We work fully online with clients worldwide, in English or Dutch, and set up the payment methods and shipping options that fit your country. Prices are the same final prices in euros everywhere. The payment provider's transaction fees are listed in the quote up front.")],
  "offers": [("Web shop", 1950)],
  "rel": [("en-website-design.html", "Website design"), ("en-pricing.html", "All prices"), ("en-ai-chatbot.html", "AI chatbot")]},

 {"slug": "en-game-development", "lang": "en", "kort": "Game development",
  "titel": "Game development from €1,950 | Collens Group",
  "desc": "Casual 2D games for browser, iPhone and Android: branded game from €1,950, casual game from €4,950, 2D game with levels from €9,950. Fixed price.",
  "h1": "Game development: branded and casual 2D games",
  "lead": "Casual 2D games for the browser, iPhone and Android, for your brand, your customers or as a product of your own. At a fixed price, below the market average.",
  "secties": [
   ("Compared with the market", "<p>A simple mobile game typically starts at around €10,000 when you hire a studio in the Netherlands (<a href='https://www.juegostudio.com/blog/cost-of-game-development-netherlands' rel='nofollow noopener'>Juego Studios, 2026</a>). With us, a branded browser game starts at €1,950, a casual game at €4,950 and a 2D game with levels at €9,950. " + FINAL + "</p>"),
   ("Our game packages", "<div class='scroll'><table class='tabel vergelijk'><tr><th>Package</th><th>Includes</th><th>Ready in</th><th>From</th></tr>"
    "<tr><td>Branded game</td><td>Browser game in your brand style, 1 game mechanic (quiz or reaction game), leaderboard and share button. Ideal for campaigns and trade fairs.</td><td>2–3 weeks</td><td>€1,950</td></tr>"
    "<tr><td>Casual game</td><td>1 fully developed game mechanic, sound and animation, for iOS, Android or browser, ads or in-app purchases possible</td><td>4–6 weeks</td><td>€4,950</td></tr>"
    "<tr><td>2D game with levels</td><td>Several levels and progress, your own characters and world, live in the App Store and Google Play, leaderboards and rewards</td><td>8–12 weeks</td><td>€9,950</td></tr></table></div>"),
   ("Games we made ourselves", "<p>We build and publish our own games too, so you can see what we make before you pay: <a href='app-koffer-vol.html'>Koffer Vol!</a>, a packing puzzle with 100 levels in 10 countries, and <a href='app-eiland-express.html'>Eiland Express</a>, a 3D driving game on a tropical island. More on the <a href='en-projects.html'>projects page</a>.</p>"),
   ("How it works", "<ol><li>Send us your logo, colours and the goal by email: a greeting, a contest or something for your team.</li><li>Within 48 hours you get a free concept of the game.</li><li>After you approve the design and the fixed price, we build it.</li><li>You test it on your own phone, then share the link or QR code.</li></ol>")],
  "faq": [("Which games do you make?", "Casual 2D games: puzzles, quizzes, reaction and arcade games. That can be a branded browser game for a campaign or trade show, a casual game for iPhone and Android, or a 2D game with levels and its own characters. Our own example is the puzzle game Koffer Vol!. We do not build large 3D games or online multiplayer."),
          ("Can I earn money with my game?", "Yes. We can add ads or in-app purchases, such as extra levels, coins or removing ads, following Apple's and Google's rules; they keep a share of in-app purchase revenue. What works best depends on your players and your goal. In the concept we show how the revenue model fits the game without spoiling the fun."),
          ("Do players need to download an app?", "Not for a branded game: it runs in the browser. Players open a link or scan a QR code, for example on a poster, packaging or in a newsletter, and play straight away, without installing anything or creating an account. If you do want an app in the stores, the casual game or the 2D game with levels is the right package."),
          ("Can the game be in my language?", "Yes. The game can be in English, Dutch or another language, or in several languages at once. Our own game Koffer Vol! is available in 12 languages, for example. Tell us in your request which languages you need and we include them in the fixed price."),
          ("What does it cost after launch?", "An extra level or game mode is from €395. Game maintenance with updates for new iOS and Android versions is €85.50 a month.")],
  "offers": [("Branded game", 1950), ("Casual game", 4950), ("2D game with levels", 9950)],
  "rel": [("en-projects.html", "Our work"), ("en-pricing.html", "All prices"), ("en-app-development.html", "App development")]},

 {"slug": "en-ai-automation", "lang": "en", "kort": "AI automation",
  "titel": "AI automation for small business from €395 | Collens Group",
  "desc": "Let repetitive work run by itself: emails, quotes, planning and customer questions. Automation from €395, AI chatbot from €995, AI assistant from €1,950.",
  "h1": "AI automation for small business",
  "lead": "Let repetitive work run by itself: emails, quotes, planning, social media and customer questions. With AI tools that connect the apps you already use, at a fixed price.",
  "secties": [
   ("Compared with the market", "<p>An AI agent built with no-code tools such as Zapier or Make costs a one-off €2,000 to €8,000 in the Netherlands (<a href='https://searchlab.nl/kosten/wat-kost-een-ai-agent-laten-bouwen' rel='nofollow noopener'>Searchlab, 2026</a>). With us, a single automation starts at €395. " + FINAL + "</p>"),
   ("Our packages", "<div class='scroll'><table class='tabel vergelijk'><tr><th>Package</th><th>Includes</th><th>Ready in</th><th>From</th></tr>"
    "<tr><td>Automation</td><td>1 workflow, for example form → CRM → email; connects your existing apps; tested and documented</td><td>2–5 days</td><td>€395</td></tr>"
    "<tr><td>AI chatbot</td><td>Answers questions on your website, trained on your own content, passes doubtful questions to you</td><td>1 week</td><td>€995</td></tr>"
    "<tr><td>AI assistant</td><td>Several workflows and integrations with email, calendar, documents and CRM; you keep the final say</td><td>2–4 weeks</td><td>€1,950</td></tr></table></div>"
    "<p>Extra workflow from €195. Monitoring and small changes €49 a month.</p>"),
   ("Which package fits you?", "<ul><li><strong>Automation (from €395):</strong> you keep handling the same form, email or overview and want it to happen by itself.</li><li><strong>AI chatbot (from €995):</strong> customers keep asking the same questions about opening hours, prices or delivery times. Read more about the <a href='en-ai-chatbot.html'>AI chatbot</a>.</li><li><strong>AI assistant (from €1,950):</strong> several workflows across email, calendar, documents and CRM, with you in control.</li></ul><p>Not sure? Describe what you do again every week, and we will tell you honestly which package fits, or that you can solve it without us.</p>"),
   ("How it works", "<ol><li>Tell us by email which work keeps coming back.</li><li>You get a free concept and a fixed price.</li><li>After you approve, we build it and test it with you.</li><li>Then it goes live.</li></ol>")],
  "faq": [("Do you need my passwords?", "No. We use official integrations and you stay in control of your accounts. Where a tool needs access, you grant it yourself through that tool's own permission screen, and you can revoke it at any time. We only set up the access an automation actually needs, nothing more."),
          ("Which tools do you work with?", "Tools such as Make and Zapier and the apps you already use, like your email, calendar, spreadsheets and CRM. We prefer to build on what you already have, so you do not need new subscriptions unless they really add something. Before the quote we check your setup and tell you whether any tool costs extra."),
          ("What if something breaks?", "Every automation is tested with real examples and documented, so you know what it does and where. If an app you use changes, a connection can occasionally stop working. With management (€49 a month) we monitor your automations, get notified when something fails and fix small issues. Without management, we fix it as a separate job at our hourly rate."),
          ("Do you work with businesses outside the Netherlands?", "Yes. We work fully online, by email and video, with clients worldwide, in English or Dutch. Prices are the same final prices in euros everywhere, with no VAT added. Time zones are rarely a problem: most of the work is done in writing, and calls are planned at a time that suits you.")],
  "offers": [("Automation", 395), ("AI chatbot", 995), ("AI assistant", 1950)],
  "rel": [("en-ai-chatbot.html", "AI chatbot"), ("en-pricing.html", "All prices"), ("en-website-design.html", "Website design")]},

 {"slug": "en-about", "lang": "en", "kort": "About us",
  "titel": "About Collens Group: websites, apps, games and AI | Collens Group",
  "desc": "Collens Group builds websites, apps, games and AI at a fixed price, with a free concept first. Founded by Jeffrey Collens. Working online, worldwide.",
  "h1": "About Collens Group",
  "lead": "We build websites, apps, games and AI solutions for businesses in the Netherlands, Belgium and the rest of the world, with a fixed price up front and a free concept before you pay anything.",
  "secties": [
   ("What we do", "<p>Collens Group is a small, independent digital company. We build <a href='en-website-design.html'>websites</a> and <a href='en-web-shop.html'>web shops</a>, <a href='en-app-development.html'>apps for iPhone and Android</a>, <a href='en-game-development.html'>games</a> and <a href='en-ai-automation.html'>AI automation and chatbots</a>.</p>"),
   ("Who is behind it?", "<p>Collens Group was founded by Jeffrey Collens. He builds with modern AI tools and checks every concept, every text and every delivery himself before it goes to a client. So you email directly with the maker, not with an account manager.</p>"),
   ("Where we work", "<p>Anywhere. We work fully online, by email and video, with businesses in the Netherlands and Belgium and beyond, for example in the United Kingdom, Ireland, the United States, Canada, Australia and New Zealand. You can work with us in English or Dutch. Prices are the same final prices in euros everywhere.</p>"),
   ("How we work", "<ul><li><strong>Fixed price up front.</strong> You know what you pay before we start. Extra work only after your approval.</li><li><strong>A free concept first.</strong> Within 48 hours you see what it can look like, made for your business, with no obligation.</li><li><strong>Final prices.</strong> No VAT is added.</li><li><strong>You stay the owner.</strong> The site, the domain and the content are in your name; apps are published on your own Apple and Google accounts and the source code is yours after the final payment.</li><li><strong>Honest about what we don't do.</strong> We don't build large 3D games or online multiplayer, and we don't work on location.</li></ul>"),
   ("What we built ourselves", "<p>What we make for ourselves, we make for you. <a href='app-lubbyc.html'>LubbyC</a> is a travel app, <a href='app-koffer-vol.html'>Koffer Vol!</a> a packing puzzle with 100 levels in 10 countries, <a href='app-eiland-express.html'>Eiland Express</a> a 3D driving game and <a href='app-manu-en-khanun.html'>Manu en Khanun</a> an animated series for children. See them on the <a href='en-projects.html'>projects page</a>.</p>")],
  "faq": [("How do I contact you?", "Use the contact form on our home page or email info@collensgroup.com. You get a reply within 48 hours, in English or Dutch. Tell us briefly what your business does and what you would like to have built; that is enough for us to start on your free concept. We work fully online, by email and video, so it does not matter where you are."),
          ("Do you work with clients in my country?", "Most likely yes. We work fully online, by email and video, with clients worldwide, in English or Dutch, for example in the United Kingdom, Ireland, the United States, Canada, Australia and New Zealand. Prices are the same final prices in euros everywhere. We set up payment methods and texts that fit your country and your customers."),
          ("Who owns what you build?", "You do. After the final payment everything we built for you is yours: the code, the design and the content. Websites and domains are registered in your name, and apps are published on your own Apple and Google developer accounts. If you later want to work with someone else, you take everything with you.")],
  "offers": [("Business website", 995), ("AI chatbot", 995), ("Basic / MVP app", 3150)],
  "rel": [("en-projects.html", "Our work"), ("en-pricing.html", "All prices"), ("en.html", "Home")]},
]
