// Contactsheet: elk concept in 3 stijlen op 390 px, eerste scherm, in één PNG.
// Gebruik: node tools/concepten/contactsheet.js uit.png slug1 slug2 ...  (na python3 build.py)
const {chromium} = require('playwright'); const path = require('path');
(async () => {
  const [uit, ...slugs] = process.argv.slice(2);
  if (!uit || !slugs.length) { console.error('Gebruik: node tools/concepten/contactsheet.js uit.png slug ...'); process.exit(1); }
  const W = 390, H = 760, S = 0.5, b = await chromium.launch();
  const p = await b.newPage({viewport: {width: W, height: H}});
  const tegels = [];
  for (const s of slugs) {
    await p.goto('file://' + path.resolve('dist/concept/' + s + '/index.html'));
    for (const st of ['s1', 's2', 's3']) {
      await p.click(`.kies button[data-s="${st}"]`); await p.waitForTimeout(400);
      tegels.push((await p.screenshot()).toString('base64'));
    }
  }
  const kol = 6, rij = Math.ceil(tegels.length / kol);
  const html = `<body style="margin:0;display:grid;grid-template-columns:repeat(${kol},${W*S}px);background:#fff">` +
    tegels.map(t => `<img src="data:image/png;base64,${t}" style="width:${W*S}px;height:${H*S}px">`).join('') + '</body>';
  await p.setViewportSize({width: kol * W * S, height: rij * H * S});
  await p.setContent(html); await p.waitForTimeout(300);
  await p.screenshot({path: uit}); await b.close();
  console.log(`Contactsheet: ${slugs.length} concepten x 3 stijlen -> ${uit}`);
})();
