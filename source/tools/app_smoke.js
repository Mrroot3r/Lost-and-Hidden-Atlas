/* Checks the Android app's page logic in a desktop browser, with a stand-in for the phone's background recorder.
   It cannot test the real recorder (that is Java, in android-app/android); it tests that the page drives it correctly:
   start, a refused permission, points collected after the page was away, a restart after Android killed the recorder,
   stop, share, delete, and the Back button.
     cd android-app && node scripts/make-www.js && python3 -m http.server -d www 8772 &
     node source/tools/app_smoke.js http://localhost:8772/
   Needs Playwright (npm install playwright; npx playwright install chromium). Exits 1 on any failure. */
const { chromium, devices } = require('playwright');
const URL0 = process.argv[2] || 'http://localhost:8772/';
(async () => {
  const proxy = process.env.HTTPS_PROXY ? { proxy: { server: process.env.HTTPS_PROXY, bypass: 'localhost,127.0.0.1' } } : {};
  const browser = await chromium.launch(proxy); const errs = [], fails = [];
  const ok = (name, cond, detail) => { console.log((cond ? 'ok   ' : 'FAIL ') + name + (detail !== undefined ? '  [' + detail + ']' : '')); if (!cond) fails.push(name); };
  const ctx = await browser.newContext({ ...devices['Pixel 7'], permissions: ['geolocation'], geolocation: { latitude: 42.8533, longitude: -73.8946, accuracy: 8 } });
  // the stand-in phone: once started it "records" a point every 400 ms, 5 m further north, whether or not the page is open
  await ctx.addInitScript(base => {
    try { localStorage.setItem('atlas-base', base); } catch (e) {}
    const K = 'mock-phone', get = () => JSON.parse(localStorage.getItem(K) || '{"rec":false,"running":false,"logId":"","t0":0,"base":[],"frozen":{},"calls":[]}'), put = s => localStorage.setItem(K, JSON.stringify(s));
    const pts = (s, id) => { if (s.frozen[id]) return s.frozen[id]; if (s.logId !== id) return []; const a = (s.base || []).slice(); if (!s.t0) return a; const n = Math.floor((Date.now() - s.t0) / 400); for (let i = 0; i < n; i++) a.push([+(42.8533 + a.length * 5 / 111320).toFixed(5), -73.8946, Math.round(s.t0 / 1000 + i * 0.4)]); return a; };
    window.__phonePoints = id => pts(get(), id);
    window.Capacitor = { isNativePlatform: () => true, nativePromise: (plugin, m, o) => new Promise((res, rej) => {
      const s = get(); s.calls.push(m);
      const st = () => ({ recording: s.rec, running: s.running, logId: s.logId, started: s.t0, count: pts(s, s.logId).length, fine: true, background: false, gps: true, battery: false, version: 'test', android: 36, phone: 'Stand-in', fixes: 0, kept: 0, lastAccuracy: 8, lastFixAgo: 1, error: '' });
      if (plugin !== 'FieldLog') { rej(new Error('no such plugin')); return; }
      if (m === 'status') res(st());
      else if (m === 'start') { if (window.__denyStart) { put(s); rej(new Error('Precise location was not allowed.')); return; }
        s.base = (s.rec && s.logId === o.logId) ? pts(s, o.logId) : []; s.t0 = Date.now(); s.rec = true; s.running = true; s.logId = o.logId; put(s); res(st()); return; }
      else if (m === 'stop') { s.frozen[s.logId] = pts(s, s.logId); s.rec = false; s.running = false; res(st()); }
      else if (m === 'points') res({ points: pts(s, o.logId).slice(o.from || 0) });
      else if (m === 'remove') { delete s.frozen[o.logId]; res({}); }
      else if (m === 'media') res({ access: 'all', items: [   // one photo and one 5-second video inside the asked-for time range, and a screenshot that must be ignored
        { kind: 'image', id: 1, name: 'P1.jpg', taken: (o.from + 62) * 1000, modified: o.from + 62, bucket: 'Camera' },
        { kind: 'image', id: 2, name: 'shot.png', taken: (o.from + 63) * 1000, modified: o.from + 63, bucket: 'Screenshots' },
        { kind: 'video', id: 3, name: 'V1.mp4', taken: (o.from + 70) * 1000, modified: o.from + 70, duration: 5000, bucket: 'Camera' }] })
      else if (m === 'share') { s.lastShare = { name: o.name, mime: o.mime, b64: (o.base64 || '').length, text: (o.text || '').length }; res({}); }
      else if (m === 'targets') { s.targets = { r: o.r, n: (o.list || []).length, first: (o.list || [])[0] }; res({}); }   // Near me: what the recorder should buzz near
      else if (m === 'marks') res({ marks: (s.marks || []).slice(o.from || 0) })
      else if (m === 'saveBackup') res({ where: 'Download/Lost Hidden Atlas/' + o.name, bytes: o.text.length })
      else if (m === 'thumb') res({ data: 'data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7' })
      else res({});
      put(s); }) };
  }, URL0);
  const page = await ctx.newPage(); page.on('pageerror', e => errs.push(e.message));
  const phone = () => page.evaluate(() => JSON.parse(localStorage.getItem('mock-phone') || '{}'));
  const log = () => page.evaluate(() => { const U = JSON.parse(localStorage.getItem('lost-hidden-atlas-v1') || '{}'); const l = (U.logs || [])[0]; return l ? { id: l.id, pts: l.pts.length, notes: l.notes.length, rec: U.rec === l.id, t1: l.t1, media: (l.media || []).map(m => m.k + ':' + m.n).join() } : null; });
  const reopen = async () => { await page.goto('about:blank'); await page.goto(URL0); await page.waitForTimeout(4500); };
  await page.goto(URL0); await page.waitForTimeout(3000);
  ok('page starts through boot.js in app mode', await page.evaluate(() => !!(window.ATLAS && ATLAS.native)));
  ok('places are listed', await page.locator('#list .item').count() > 50);
  await page.click('#tab-log'); await page.waitForTimeout(600);
  ok('Log tab explains background recording', /screen off/.test(await page.locator('#v-log').innerText()));
  ok('battery button offered when Android may pause the app', await page.getByRole('button', { name: 'Stop Android pausing it' }).count() === 1);
  await page.evaluate(() => { window.__denyStart = true; }); await page.getByRole('button', { name: 'Start a field log', exact: true }).click(); await page.waitForTimeout(800);
  ok('refused permission: clear message and no empty log left behind', /could not start/i.test(await page.locator('#banner').textContent()) && (await log()) === null && !(await page.isVisible('#recbar')));
  await page.evaluate(() => { window.__denyStart = false; }); await page.getByRole('button', { name: 'Start a field log', exact: true }).click(); await page.waitForTimeout(5000);
  await page.click('#rec-note'); await page.fill('#rec-text', 'cellar hole'); await page.keyboard.press('Enter'); await page.waitForTimeout(500);   // adding a note also saves the log
  let l = await log(); ok('recording: points arrive from the phone', l && l.rec && l.pts >= 6, l && l.pts);
  const tg = (await phone()).targets || {}; ok('Near me: the recorder is handed the places and leads to buzz near', tg.r === 100 && tg.n > 20 && Array.isArray(tg.first) && tg.first.length === 4 && typeof tg.first[2] === 'string', JSON.stringify(tg).slice(0, 120));
  await page.evaluate(() => { const s = JSON.parse(localStorage.getItem('mock-phone')); s.marks = [[null, null, Math.round(Date.now() / 1000)]]; localStorage.setItem('mock-phone', JSON.stringify(s)); }); await page.waitForTimeout(3200);   // "Mark here" tapped on the notification
  ok('a mark from the notification becomes a note with a position', await page.evaluate(() => { const l = JSON.parse(localStorage.getItem('lost-hidden-atlas-v1')).logs[0]; const n = l.notes.find(x => x.mk); return !!(n && n.x === 'Mark 1' && n.la != null); }));
  const before = (await log()).pts; await page.goto('about:blank'); await page.waitForTimeout(4000); await page.goto(URL0); await page.waitForTimeout(4500);
  l = await log(); ok('page away 4 s: the points recorded meanwhile are collected', l.rec && l.pts >= before + 8, before + ' -> ' + l.pts);
  // Android killed the recorder: it still wants to record but is not running
  await page.evaluate(() => { const s = JSON.parse(localStorage.getItem('mock-phone')); s.base = window.__phonePoints(s.logId); s.t0 = 0; s.running = false; localStorage.setItem('mock-phone', JSON.stringify(s)); });
  const atKill = (await phone()).base.length; await reopen();
  l = await log(); ok('after a kill: recorder restarted in the same log, nothing lost', (await phone()).running && l.rec && l.pts >= atKill, atKill + ' -> ' + l.pts);
  await page.click('#rec-stop'); await page.waitForTimeout(200); await page.click('#rec-stop'); await page.waitForTimeout(1500);
  l = await log(); const ph = await phone(); const saved = (ph.frozen[l.id] || []).length;
  ok('stop: every point the phone saved is in the log', !l.rec && !!l.t1 && l.pts === saved, l.pts + ' of ' + saved);
  ok('the note and the mark were kept', l.notes === 2);
  ok('a backup file is written when a log ends', (await phone()).calls.includes('saveBackup'));
  ok('photos and video from the walk are matched when it ends; screenshots are left out', l.media === 'i:P1.jpg,v:V1.mp4', l.media);
  ok('the log lists them', /1 photo · 1 video/.test(await page.locator('.logitem').first().innerText()));
  await page.getByRole('button', { name: 'Share route (GPX)' }).click(); await page.waitForTimeout(400);
  ok('GPX goes to the Android share sheet', (await phone()).calls.includes('share'));
  await page.getByRole('button', { name: 'Episode kit' }).click(); await page.waitForTimeout(400);
  ok('Episode kit opens on a finished log', /Episode kit/.test(await page.locator('.kit').innerText()) && await page.getByRole('button', { name: 'Share the whole kit' }).count() === 1);
  await page.getByRole('button', { name: 'Share the whole kit' }).click(); await page.waitForTimeout(500);
  let sh = (await phone()).lastShare || {}; ok('the kit text goes to the share sheet', /-episode-kit\.txt$/.test(sh.name || '') && sh.text > 300 && sh.mime === 'text/plain', JSON.stringify(sh));
  await page.getByRole('button', { name: 'Draw the route map' }).click(); await page.waitForSelector('.kitpic img', { timeout: 60000 }); await page.getByRole('button', { name: 'Share the picture' }).click(); await page.waitForTimeout(1500);
  sh = (await phone()).lastShare || {}; ok('the route map picture goes to the share sheet as a PNG', /-route-map\.png$/.test(sh.name || '') && sh.b64 > 20000 && sh.mime === 'image/png' && sh.text === 0, JSON.stringify(sh));
  await page.getByRole('button', { name: 'Delete' }).click(); await page.getByRole('button', { name: 'Really delete?' }).click(); await page.waitForTimeout(400);
  ok('deleting a log removes the phone file too', (await phone()).calls.includes('remove') && (await log()) === null);
  await page.click('#tab-list'); await page.locator('#list .item').first().click(); await page.waitForTimeout(600); await page.click('#lb-opt'); await page.waitForTimeout(300);
  const seq = []; for (let i = 0; i < 3; i++) { seq.push(await page.evaluate(() => window.atlasBack())); await page.waitForTimeout(150); }
  ok('Back closes the sheet, then the place, then leaves the app', seq.join() === 'true,true,false', seq.join());
  await page.click('#lb-opt'); await page.waitForTimeout(300); await page.click('#sheet-set'); await page.waitForTimeout(400);
  ok('Settings open from the gear and hold the data-source section', (await page.locator('#sheet-t').textContent()) === 'Settings' && await page.locator('#at-base').count() === 1);
  await page.selectOption('#set-units', 'km'); await page.waitForTimeout(300);
  ok('settings reach the recorder', (await phone()).calls.includes('configure'));
  await page.click('#sheet-x'); await page.click('#tab-near'); await page.waitForTimeout(2500);   // opening Near switches location on
  ok('Near tab lists what is close, nearest first', await page.locator('#near-list .nmitem').count() > 3 && /From where you are/.test(await page.locator('#near-st').innerText()), (await page.locator('#near-list .nmitem').count()) + ' rows; ' + (await page.locator('#near-st').innerText()).replace(/\s+/g, ' ').slice(0, 60) + '; ' + (await page.locator('#near-list .nmitem').first().innerText()).replace(/\s+/g, ' ').slice(0, 60));
  await page.selectOption('#near-al', '0'); await page.waitForTimeout(600);
  ok('Near me: switching the alert off reaches the recorder', ((await phone()).targets || {}).r === 0);
  await page.click('#lb-opt'); await page.waitForTimeout(300);
  await page.click('#sheet-x'); await page.click('#tab-log'); await page.waitForTimeout(300);
  // the photo details (data/photos.json) are not built into the app: they must come from the Atlas address, or pictures found on
  // Wikimedia Commons never show in the app and every other place asks Wikipedia each time (found November 25, 2026)
  { const ph = await page.evaluate(async () => { const b0 = window.ATLAS.base; window.ATLAS.setBase('http://localhost:8766/');
      try { const r = await window.ATLAS.fetch('data/photos.json'); const j = await r.json(); return { ok: r.ok, n: Object.keys(j.p || {}).length }; } catch (e) { return { err: String(e).slice(0, 80) }; } finally { window.ATLAS.setBase(b0); } });
    ok('the app gets the photo details from the Atlas address', ph.ok === true && ph.n > 100, JSON.stringify(ph)); }
  ok('no script errors', errs.length === 0, errs.join(' | ').slice(0, 300));
  await browser.close(); console.log(fails.length ? fails.length + ' FAILED' : 'app smoke test passed'); process.exit(fails.length ? 1 : 0);
})().catch(e => { console.error(e); process.exit(1); });
