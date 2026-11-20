// Phone-size smoke test of the hosted build. Serve dist/ first:
//   (cd $ATLAS/dist && python3 -m http.server 8766) &   then   node tools/smoke.js http://localhost:8766/web/ [place-id]
const { chromium, devices } = require('playwright');
const B = process.argv[2] || 'http://localhost:8766/web/';
(async () => {
  const opt = process.env.HTTPS_PROXY ? { proxy: { server: process.env.HTTPS_PROXY, bypass: 'localhost,127.0.0.1' } } : {};
  const browser = await chromium.launch(opt), errs = [];
  const ctx = await browser.newContext({ ...devices['Pixel 7'], ignoreHTTPSErrors: true, permissions: ['geolocation'], geolocation: { latitude: 42.8533, longitude: -73.8946, accuracy: 10 } });
  const page = await ctx.newPage(); page.on('pageerror', e => errs.push(e.message));
  await page.goto(B + '#luna-park'); await page.waitForTimeout(3000);
  await page.evaluate(() => document.getElementById('lb-rails').click()); await page.waitForTimeout(3500);      /* old rail lines are off until asked for (November 2026): a tap on the bar must bring them */
  const r = await page.evaluate(() => { let lines = 0; window.__atlasMap.eachLayer(l => { if (l.options && l.options.pane === 'lines' && l.getLatLngs) lines++; });
    const i = document.querySelector('.leaflet-hist-pane img');
    return { places: JSON.parse(document.getElementById('d-sites').textContent).sites.length, title: document.querySelector('#v-detail h2').textContent, lineShapes: lines, oldMap: i ? i.naturalWidth : 0, barButtons: document.querySelectorAll('.lb').length, tabs: [...document.querySelectorAll('.tabs button')].map(b => b.textContent.trim()).join(',') }; });
  await page.click('#lb-opt'); await page.waitForTimeout(300); r.sheetOpens = await page.isVisible('#sheet'); await page.click('#sheet-x'); r.sheetCloses = !(await page.isVisible('#sheet'));
  await page.click('#lb-loc'); await page.waitForTimeout(2000); r.locate = await page.locator('#banner').textContent();
  // optional: node smoke.js <url> <place-id> also checks that leaf-off and LiDAR tiles load at that place (use it for a new state)
  const pid = process.argv[3];
  if (pid) {
    await page.click('#lb-loc'); await page.goto(B + '#' + pid); await page.reload(); await page.waitForTimeout(3500);
    r.place = await page.evaluate(() => (document.querySelector('#v-detail h2') || {}).textContent || null);
    const tiles = async key => { await page.click('#lb-' + key); await page.evaluate(() => { const m = window.__atlasMap; m.setZoom(16, { animate: false }); }); await page.waitForTimeout(9000);
      return page.evaluate(() => { const t = [...document.querySelectorAll('.leaflet-tile-pane .leaflet-tile')]; return t.filter(i => i.classList.contains('leaflet-tile-loaded')).length + ' of ' + t.length + ' tiles'; }); };
    r.leafOff = await tiles('leaf'); r.lidar = await tiles('lidar');
    await page.screenshot({ path: 'smoke-' + pid + '.png' });
    r.placeOk = !!r.place && !/^0 of/.test(r.leafOff) && !/^0 of/.test(r.lidar);
  }
  console.log(JSON.stringify(r, null, 1)); console.log(errs.length ? 'PAGE ERRORS:\n' + errs.join('\n') : 'no page errors');
  const ok = (r.placeOk !== false) && r.places > 300 && r.lineShapes > 3 && r.oldMap > 0 && r.sheetOpens && r.sheetCloses && !errs.length;
  await browser.close(); process.exit(ok ? 0 : 1);
})();
