/* Checks how the Android app's page loads the historic pockets through boot.js, in a desktop browser at phone size.
   The website loads them with a plain fetch (source/tools/smoke.js and a look at the layer cover that); the app has
   three more cases, and none of them can be tried on a phone from here:
     1. built-in data: the index, then one state's detail file when the map is zoomed in there
     2. a state whose detail is NOT built into the app (added to the site after the app was built): fetched from the
        Atlas address, and kept on the phone
     3. an update: only the states whose detail changed are downloaded again
   Run it after any change to boot.js, to pockLoad/pockFetch in app.js, or to the shape of data/pockets.json:
     cd android-app && node scripts/make-www.js && cd ..
     node source/tools/app_pockets.js            (from the repository root; it starts its own three little servers)
   Needs Playwright (npm install playwright; npx playwright install chromium). Exits 1 on any failure. */
const { chromium, devices } = require('playwright');
const http = require('http'), fs = require('fs'), path = require('path'), os = require('os');
const REPO = path.resolve(process.argv[2] || '.');
const TYPES = { '.html': 'text/html', '.js': 'text/javascript', '.json': 'application/json', '.css': 'text/css', '.webp': 'image/webp' };
function serve(dir) { return new Promise(res => { const s = http.createServer((q, r) => {
  let p = decodeURIComponent(q.url.split('?')[0]); if (p.endsWith('/')) p += 'index.html';
  const f = path.join(dir, p); if (!f.startsWith(dir) || !fs.existsSync(f) || fs.statSync(f).isDirectory()) { r.writeHead(404, { 'Access-Control-Allow-Origin': '*' }); r.end('not found'); return; }
  r.writeHead(200, { 'Content-Type': TYPES[path.extname(f)] || 'application/octet-stream', 'Access-Control-Allow-Origin': '*', 'Cache-Control': 'no-store' }); fs.createReadStream(f).pipe(r);
}); s.listen(0, '127.0.0.1', () => res({ url: 'http://localhost:' + s.address().port + '/', close: () => s.close() })); }); }
/* a copy of the site that looks one version newer, in which only the first state's detail stamp changed */
function newer(site) { const out = fs.mkdtempSync(path.join(os.tmpdir(), 'atlas-newer-'));
  fs.mkdirSync(path.join(out, 'data', 'pock'), { recursive: true });
  const v = JSON.parse(fs.readFileSync(path.join(site, 'version.json'), 'utf8')).v, nv = String(+v + 1);
  for (const f of ['version.json', 'index.html']) fs.writeFileSync(path.join(out, f), fs.readFileSync(path.join(site, f), 'utf8').split(v).join(nv));
  for (const f of ['data/lines.json', 'data/leads.json']) fs.copyFileSync(path.join(site, f), path.join(out, f));
  const j = JSON.parse(fs.readFileSync(path.join(site, 'data/pockets.json'), 'utf8')), first = Object.keys(j.s)[0]; j.s[first].h = 'changed1';
  fs.writeFileSync(path.join(out, 'data/pockets.json'), JSON.stringify(j));
  for (const k of Object.keys(j.s)) fs.copyFileSync(path.join(site, 'data/pock', k + '.json'), path.join(out, 'data/pock', k + '.json'));
  return { dir: out, changed: first }; }
const fails = []; const ok = (name, cond, detail) => { console.log((cond ? 'ok   ' : 'FAIL ') + name + (detail !== undefined ? '  [' + detail + ']' : '')); if (!cond) fails.push(name); };
(async () => {
  const www = path.join(REPO, 'android-app', 'www');
  if (!fs.existsSync(path.join(www, 'index.html'))) { console.error('No android-app/www. Run: cd android-app && node scripts/make-www.js'); process.exit(1); }
  const idx = JSON.parse(fs.readFileSync(path.join(REPO, 'data/pockets.json'), 'utf8')), states = Object.keys(idx.s);
  if (states.length < 2) { console.error('This check needs pockets for at least two states.'); process.exit(1); }
  /* a town centre in each of the first two states to zoom in on */
  const spot = k => { const r = idx.k.find(x => x[8] === k && x[10] === 'c'); return [r[0], r[1]]; }, A1 = states[0], A2 = states[1];
  const nw = newer(REPO), app = await serve(www), site = await serve(REPO), site2 = await serve(nw.dir);
  const proxy = process.env.HTTPS_PROXY ? { proxy: { server: process.env.HTTPS_PROXY, bypass: 'localhost,127.0.0.1' } } : {};
  const browser = await chromium.launch(proxy);
  async function open(base, block) {
    const c = await browser.newContext({ ...devices['Pixel 7'] }), p = await c.newPage(), errs = [], reqs = [];
    p.on('pageerror', e => errs.push(e.message)); p.on('request', r => { const u = r.url(); if (u.indexOf('/data/pock') >= 0) reqs.push((u.indexOf(app.url) === 0 ? 'app:' : u.indexOf(base) === 0 ? 'atlas:' : '?:') + u.replace(/^.*\/data\//, '').split('?')[0]); });
    await c.addInitScript(b => { try { localStorage.setItem('atlas-base', b); } catch (e) {} }, base);
    if (block) await p.route(app.url + 'data/pock/' + block + '.json', r => r.fulfill({ status: 404, body: 'not built in' }));
    await p.goto(app.url); await p.waitForFunction(() => window.__atlasMap, null, { timeout: 30000 }); await p.waitForTimeout(1500);
    const go = async (ll, z) => { await p.evaluate(([ll, z]) => { window.__atlasMap.setView(ll, z, { animate: false }); }, [ll, z]); await p.waitForTimeout(2500); };
    const shapes = () => p.evaluate(() => { let n = 0; window.__atlasMap.eachLayer(l => { if (l.options && l.options.pane === 'lines' && l.options.fillColor && l.options.fillOpacity === 1) n++; }); return n; });
    const kept = () => p.evaluate(async () => { const c = await caches.open('atlas-data'); return (await c.keys()).map(r => r.url.replace(/^https?:\/\/[^/]+\//, '')).sort(); });
    const layerOn = async () => { await p.click('#lb-opt'); await p.waitForSelector('#pock-on'); await p.check('#pock-on'); await p.waitForTimeout(2500); };
    return { c, p, errs, reqs, go, shapes, kept, layerOn };
  }
  // ---- 1 and 2
  let t = await open(site.url, A2);
  ok('nothing about pockets is fetched before the layer is on', t.reqs.length === 0, t.reqs.join(' '));
  await t.layerOn();
  ok('the index comes from the copy built into the app', t.reqs.join(' ') === 'app:pockets.json', t.reqs.join(' '));
  ok('the list of old town centres is filled', (await t.p.$$('.pocklist .btn')).length > 0);
  await t.p.click('#sheet-x'); await t.go(spot(A1), 16);
  ok('zoomed in (' + A1 + '): that state\'s detail from the built-in copy', t.reqs.indexOf('app:pock/' + A1 + '.json') >= 0 && t.reqs.indexOf('atlas:pock/' + A1 + '.json') < 0, t.reqs.join(' '));
  const n1 = await t.shapes(); ok('single markers and listings are drawn', n1 > 3, n1);
  await t.go(spot(A2), 16);
  ok('zoomed in (' + A2 + '): its detail is not built in, so it comes from the Atlas address', t.reqs.indexOf('atlas:pock/' + A2 + '.json') >= 0, t.reqs.join(' '));
  const n2 = await t.shapes(); ok('and its markers and listings are drawn', n2 > 3, n2);
  const k1 = await t.kept(); ok('and it is kept on the phone', k1.indexOf('data/pock/' + A2 + '.json') >= 0, k1.join(' '));
  ok('no page errors', t.errs.length === 0, t.errs.join(' | ')); await t.c.close();
  // ---- 3: the Atlas address now holds a newer version in which only one state's detail changed
  t = await open(site2.url);
  await t.p.waitForFunction(() => { const x = document.getElementById('banner'); return x && !x.hidden && /New places downloaded/.test(x.textContent); }, null, { timeout: 30000 }).catch(() => {});
  const k2 = await t.kept(), got = k2.filter(x => x.indexOf('data/pock/') === 0);
  ok('an update was downloaded', k2.indexOf('data/pockets.json') >= 0 && k2.indexOf('atlas-sites.json') >= 0, k2.join(' '));
  ok('with it, only the state whose detail changed (' + nw.changed + ')', got.join() === 'data/pock/' + nw.changed + '.json', got.join(' '));
  await t.p.reload(); await t.p.waitForFunction(() => window.__atlasMap, null, { timeout: 30000 }); await t.p.waitForTimeout(1500);
  await t.layerOn(); await t.p.click('#sheet-x'); t.reqs.length = 0; await t.go(spot(nw.changed), 16);
  const n3 = await t.shapes(); ok('after the update the kept detail is used, with no new download', n3 > 3 && !t.reqs.some(x => x.indexOf('atlas:') === 0), n3 + ' shapes; ' + t.reqs.join(' '));
  ok('no page errors after the update', t.errs.length === 0, t.errs.join(' | ')); await t.c.close();
  await browser.close(); app.close(); site.close(); site2.close(); fs.rmSync(nw.dir, { recursive: true, force: true });
  console.log(fails.length ? fails.length + ' FAILED' : 'app pockets test passed'); process.exit(fails.length ? 1 : 0);
})().catch(e => { console.error(e); process.exit(1); });
