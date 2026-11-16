#!/usr/bin/env node
/* Builds www/, the copy of the Atlas that goes inside the Android app, from a built site.
     node scripts/make-www.js [site-folder]        default: the repository root (..)
   It copies the page, the app script, the map library, the lines, the leads and the historic pockets, and changes two things in the page:
   the app starts through boot.js (which picks the newest place data on the phone before starting app.js), and the
   viewport no longer asks to draw under the system bars. Old survey maps are not copied: the app fetches each one
   from the Atlas address the first time it is needed and keeps it. */
const fs = require('fs'), path = require('path');
const site = path.resolve(process.argv[2] || path.join(__dirname, '..', '..'));
const out = path.join(__dirname, '..', 'www');
const need = ['index.html', 'app.js', 'leaflet.js', 'boot.js', 'data/lines.json', 'data/leads.json'];
for (const f of need) if (!fs.existsSync(path.join(site, f))) { console.error('Missing ' + f + ' in ' + site + '. Build the site first.'); process.exit(1); }
fs.rmSync(out, { recursive: true, force: true });
fs.mkdirSync(path.join(out, 'data'), { recursive: true });
for (const f of need.slice(1)) fs.copyFileSync(path.join(site, f), path.join(out, f));
for (const f of ['data/pockets.json']) if (fs.existsSync(path.join(site, f))) fs.copyFileSync(path.join(site, f), path.join(out, f));   // optional layers
let html = fs.readFileSync(path.join(site, 'index.html'), 'utf8');
const swap = (re, to, what) => { if (!re.test(html)) { console.error('Could not find ' + what + ' in index.html; the page layout has changed.'); process.exit(1); } html = html.replace(re, to); };
swap(/<script src="app\.js\?v=[^"]*"><\/script>/, '<script src="boot.js"></script>', 'the app script tag');
swap(/<script src="leaflet\.js\?v=[^"]*"><\/script>/, '<script src="leaflet.js"></script>', 'the map library tag');
swap(/,viewport-fit=cover/, '', 'the viewport setting');
fs.writeFileSync(path.join(out, 'index.html'), html);
const v = (/"v":"(\d+)"/.exec(html) || [])[1];
const size = fs.readdirSync(out, { recursive: true }).reduce((n, f) => { const s = fs.statSync(path.join(out, f)); return n + (s.isFile() ? s.size : 0); }, 0);
console.log('www ready: place data build ' + v + ', ' + Math.round(size / 1024) + ' KB');
