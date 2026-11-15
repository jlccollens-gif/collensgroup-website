// Mobiele kwaliteitscheck (360 px) voor alle pagina's in dist/, incl. /concept/.
// Gebruik: node tools/mobiel_check.js   (exitcode 1 bij fouten)
// Controleert: horizontaal scrollen, afgesneden tekst (scrollWidth > clientWidth),
// interne links naar bestaande bestanden, en Nederlandse afbeeldingen op anderstalige
// pagina's (er bestaat een -en-versie die niet gebruikt wordt).
const {chromium} = require('playwright');
const fs = require('fs'), path = require('path');
const D = path.join(__dirname, '..', 'dist');
const files = fs.readdirSync(D).filter(f => f.endsWith('.html'));
if (fs.existsSync(path.join(D, 'concept')))
  for (const d of fs.readdirSync(path.join(D, 'concept')))
    if (fs.existsSync(path.join(D, 'concept', d, 'index.html'))) files.push(`concept/${d}/index.html`);
const bestaat = t => { const fp = path.join(D, t); return fs.existsSync(fp) && fs.statSync(fp).isFile()
  || fs.existsSync(fp + '.html') || fs.existsSync(path.join(fp, 'index.html')); };
(async () => {
  const b = await chromium.launch();
  const p = await b.newPage({viewport: {width: 360, height: 800}});
  let fouten = 0;
  for (const f of files) {
    await p.goto('file://' + path.join(D, f)); await p.waitForTimeout(100);
    const r = await p.evaluate(() => ({
      sw: document.documentElement.scrollWidth, lang: document.documentElement.lang,
      clip: [...document.querySelectorAll('h1,h2,h3,h4,p,li,button,.knop')]
        .filter(e => e.clientWidth > 0 && e.scrollWidth > e.clientWidth + 1).map(e => e.tagName + ': ' + e.innerText.slice(0, 30)),
      imgs: [...document.querySelectorAll('img[src],source[srcset]')].map(i => i.getAttribute('src') || i.getAttribute('srcset')),
      links: [...document.querySelectorAll('a[href]')].map(a => a.getAttribute('href')),
    }));
    const bad = [];
    if (r.sw > 360) bad.push(`horizontaal scrollen (${r.sw}px)`);
    for (const c of r.clip.slice(0, 3)) bad.push('afgesneden ' + c);
    const dir = path.dirname(f);
    for (const l of r.links) {
      if (/^(https?:|mailto:|tel:|#|javascript:|sms:|whatsapp:)/.test(l)) continue;
      const t = l.split('#')[0].split('?')[0]; if (!t) continue;
      if (!bestaat(t.startsWith('/') ? t.slice(1) : path.join(dir, t))) bad.push('kapotte link ' + l);
    }
    if (r.lang && r.lang !== 'nl') for (const s of r.imgs) {
      const src = s.split(/[\s,]/)[0]; const m = src.match(/^(.*?)(\.(jpe?g|png|webp))$/i);
      if (m && !/-en$/.test(m[1]) && fs.existsSync(path.join(D, dir, m[1] + '-en' + m[2]))) bad.push('NL-afbeelding ' + src);
    }
    const uniek = [...new Set(bad)];
    if (uniek.length) { fouten += uniek.length; console.log(`FOUT ${f} [${r.lang}]: ${uniek.join(' | ')}`); }
  }
  console.log(`${files.length} pagina's op 360 px gecontroleerd, ${fouten} fouten`);
  await b.close(); process.exit(fouten ? 1 : 0);
})();
