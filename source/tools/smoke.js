// Phone-size smoke test of the hosted build. Serve dist/ first:
//   (cd $ATLAS/dist && python3 -m http.server 8766) &   then   node tools/smoke.js http://localhost:8766/web/
const { chromium, devices } = require('playwright');
const B = process.argv[2] || 'http://localhost:8766/web/';
(async () => {
  const opt = process.env.HTTPS_PROXY ? { proxy: { server: process.env.HTTPS_PROXY, bypass: 'localhost,127.0.0.1' } } : {};
  const browser = await chromium.launch(opt), errs = [];
  const ctx = await browser.newContext({ ...devices['Pixel 7'], ignoreHTTPSErrors: true, permissions: ['geolocation'], geolocation: { latitude: 42.8533, longitude: -73.8946, accuracy: 10 } });
  const page = await ctx.newPage(); page.on('pageerror', e => errs.push(e.message));
  await page.goto(B + '#luna-park'); await page.waitForTimeout(5000);
  const r = await page.evaluate(() => { let lines = 0; window.__atlasMap.eachLayer(l => { if (l.options && l.options.pane === 'lines' && l.getLatLngs) lines++; });
    const i = document.querySelector('.leaflet-hist-pane img');
    return { places: JSON.parse(document.getElementById('d-sites').textContent).sites.length, title: document.querySelector('#v-detail h2').textContent, lineShapes: lines, oldMap: i ? i.naturalWidth : 0, barButtons: document.querySelectorAll('.lb').length, tabs: [...document.querySelectorAll('.tabs button')].map(b => b.textContent.trim()).join(',') }; });
  await page.click('#lb-opt'); await page.waitForTimeout(300); r.sheetOpens = await page.isVisible('#sheet'); await page.click('#sheet-x'); r.sheetCloses = !(await page.isVisible('#sheet'));
  await page.click('#lb-loc'); await page.waitForTimeout(2000); r.locate = await page.locator('#banner').textContent();
  console.log(JSON.stringify(r, null, 1)); console.log(errs.length ? 'PAGE ERRORS:\n' + errs.join('\n') : 'no page errors');
  const ok = r.places > 300 && r.lineShapes > 1000 && r.oldMap > 0 && r.sheetOpens && r.sheetCloses && !errs.length;
  await browser.close(); process.exit(ok ? 0 : 1);
})();
