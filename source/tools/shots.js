// Phone-size screenshots of each feature, for the front page of the repository (README.md, docs/features/).
//   serve a build first:  (python3 test/cors_server.py dist/web 8766 &)
//   node tools/shots.js [http://localhost:8766/index.html] [out folder, default research/shots]
// Run it again after a change that alters how a screen looks, look at every picture, then copy them to docs/features/ in the clone.
// Each picture starts from a new, empty browser, so nothing a reader would not see on a first visit leaks from one into the next.
// The "you are here" point is a made-up spot on a public street in Cohoes, New York: nobody's home or start place.
const { chromium, devices } = require('playwright');
const U = process.argv[2] || 'http://localhost:8766/index.html', OUT = process.argv[3] || 'research/shots', ONLY = process.argv[4] || '';      // a fourth word takes only the pictures whose name holds it
require('fs').mkdirSync(OUT, { recursive: true });
const HERE = { latitude: 42.7742, longitude: -73.7005, accuracy: 10 };
(async () => {
  const opt = process.env.HTTPS_PROXY ? { proxy: { server: process.env.HTTPS_PROXY, bypass: 'localhost,127.0.0.1' } } : {};
  const browser = await chromium.launch(opt); let bad = 0;
  const shot = async (name, hash, f) => {
    if (ONLY && !name.includes(ONLY)) return;
    const ctx = await browser.newContext({ ...devices['Pixel 7'], deviceScaleFactor: 1.5, ignoreHTTPSErrors: true, permissions: ['geolocation'], geolocation: HERE });
    const page = await ctx.newPage(); const errs = []; page.on('pageerror', e => errs.push(e.message));
    try {
      await page.goto(U + (hash || '')); await page.waitForTimeout(4000);
      await f(page);
      await page.screenshot({ path: OUT + '/' + name + '.jpg', type: 'jpeg', quality: 78 });
      console.log((errs.length ? 'PAGE ERROR ' : 'ok   ') + name + (errs.length ? '  ' + errs[0].slice(0, 120) : '')); if (errs.length) bad++;
    } catch (e) { console.log('FAIL ' + name + '  ' + String(e).slice(0, 160)); bad++; }
    await ctx.close();
  };
  const tap = (page, sel) => page.evaluate(s => document.querySelector(s).click(), sel);       // a bar button may be scrolled out of sight
  const view = (page, lat, lon, z) => page.evaluate(([a, b, c]) => window.__atlasMap.setView([a, b], c, { animate: false }), [lat, lon, z]);
  // The first picture shows both ways the map can stand in for a crowd of pins (the owner, November 25, 2026: the numbered bubbles
  // "show off just how many places there actually are", the heat map is the other choice): one map, the heat map on one side of a
  // slanted line and the bubbles on the other. The heat map is photographed first and laid over its half of the bubbles.
  await shot('01-map', '', async p => {
    await p.waitForTimeout(3000);
    const r = await p.evaluate(() => { const b = document.querySelector('#map').getBoundingClientRect(); return { x: b.left, y: b.top, width: b.width, height: b.height }; });
    await p.evaluate(() => window.__atlasSet('heat', true)); await p.waitForTimeout(3000);
    const heat = (await p.screenshot({ clip: r, type: 'png' })).toString('base64');
    await p.evaluate(() => window.__atlasSet('heat', false)); await p.waitForTimeout(3000);
    await p.evaluate(([png, r, cut]) => {
      const pill = 'position:fixed;z-index:100000;font:600 12px/1 system-ui,sans-serif;color:#fff;background:rgba(20,24,22,.82);padding:5px 9px;border-radius:11px;pointer-events:none';
      const d = document.createElement('div');
      d.style.cssText = `position:fixed;left:${r.x}px;top:${r.y}px;width:${r.width}px;height:${r.height}px;z-index:99999;pointer-events:none;background:url(data:image/png;base64,${png}) 0 0/${r.width}px ${r.height}px no-repeat;clip-path:polygon(0 0,${cut[0]}% 0,${cut[1]}% 100%,0 100%)`;
      const l = document.createElement('div');
      l.style.cssText = `position:fixed;left:${r.x}px;top:${r.y}px;width:${r.width}px;height:${r.height}px;z-index:99999;pointer-events:none;background:#fff;clip-path:polygon(${cut[0] - 0.5}% 0,${cut[0] + 0.5}% 0,${cut[1] + 0.5}% 100%,${cut[1] - 0.5}% 100%)`;
      const a = document.createElement('div'); a.textContent = 'Heat map'; a.style.cssText = pill + `;left:${r.x + 8}px;top:${r.y + 8}px`;
      const b = document.createElement('div'); b.textContent = 'Numbered bubbles'; b.style.cssText = pill + `;right:${innerWidth - r.x - r.width + 8}px;top:${r.y + 8}px`;
      document.body.append(d, l, a, b);
    }, [heat, r, [58, 42]]);
    await p.waitForTimeout(300);
  });
  await shot('02-place', '#kinzua-bridge', async p => { await p.waitForTimeout(4000); });
  // the same place twice: 02 with the old map laid over it (as a place opens), 03 with it switched off, so the two can be compared (the owner, November 22, 2026)
  await shot('03-access', '#kinzua-bridge', async p => { await p.evaluate(() => { const c = document.querySelector('#d-hist'); if (c && c.checked) c.click(); }); await p.waitForTimeout(2500); await p.evaluate(() => { const h = [...document.querySelectorAll('#v-detail h3, #v-detail dt')].find(x => /Getting there/.test(x.textContent)); h.scrollIntoView(); let e = h.parentElement; while (e && e.scrollHeight <= e.clientHeight + 5) e = e.parentElement; if (e) e.scrollTop -= 14; }); await p.waitForTimeout(1500); });
  await shot('04-filters', '', async p => { await p.click('#filt-btn'); await p.waitForTimeout(800); });
  await shot('05-compare', '#crown-point-forts', async p => { await p.click('#v-detail button:has-text("Swipe aerial")'); await p.waitForTimeout(10000); });
  await shot('06-lines', '', async p => { await p.click('#lb-big'); await view(p, 42.79, -73.69, 13); for (const b of ['#lb-rails', '#lb-canal', '#lb-leads']) await tap(p, b); await p.waitForTimeout(9000); });
  await shot('07-oldtowns', '', async p => { await p.click('#lb-big'); await view(p, 40.05, -76.6, 9); await tap(p, '#lb-pock'); await p.waitForTimeout(9000); });
  await shot('08-near', '', async p => { await p.click('#tab-near'); await p.click('#v-near button:has-text("Find me")'); await p.waitForTimeout(7000); });
  await shot('09-trip', '', async p => {
    for (const id of ['harmony-mills-cohoes', 'lock-23', 'burden-iron-works-office-troy']) { await p.goto(U + '#' + id); await p.waitForTimeout(2500); await p.click('#v-detail button:has-text("Add to trip")'); await p.waitForTimeout(400); }
    await p.click('#tab-trip'); await p.waitForTimeout(800);
    // the trip starts from where you are by itself (November 21, 2026: the "Use my location" button went). Leave at half past nine, so the
    // arrival times in the picture are a day out, not whatever hour the picture happened to be taken at
    await p.evaluate(() => { const t = document.querySelector('#trip-t0'); if (t) { t.value = '09:30'; t.dispatchEvent(new Event('change', { bubbles: true })); } }); await p.waitForTimeout(4000); });
  await shot('10-log', '', async p => { await view(p, HERE.latitude, HERE.longitude, 16); await p.click('#tab-log'); await p.click('#v-log button:has-text("Start a field log")'); await p.waitForTimeout(6000); });
  await shot('11-options', '', async p => { await p.click('#lb-opt'); await p.waitForTimeout(900); });
  await shot('12-dark', '#harmony-mills-cohoes', async p => {
    await p.click('#lb-opt'); await p.waitForTimeout(400); await p.click('#sheet-set'); await p.waitForTimeout(600);
    await p.selectOption('#sheet select >> nth=0', { label: 'Always dark' }); await p.waitForTimeout(400); await p.click('#sheet button:has-text("Done")'); await p.waitForTimeout(5000); });
  await browser.close(); console.log(bad ? bad + ' picture(s) failed' : 'all pictures taken: ' + OUT); process.exit(bad ? 1 : 0);
})();
