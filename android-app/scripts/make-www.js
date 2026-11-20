#!/usr/bin/env node
/* Builds www/, the copy of the Atlas that goes inside the Android app, from a built site.
     node scripts/make-www.js [site-folder]        default: the repository root (..)
   It copies the page, the app script, the map library, the lines, the leads and the historic pockets (the index and each
   state's detail file), and changes two things in the page:
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
// (data/pockets.json, the whole pockets layer in one file, is no longer carried: the app reads data/pock/index.json)
// vanished places and old mines: an index and one file per state, each named with a stamp of its content (data/vanished/, data/mines/).
// Every state is 15 MB, so only the index and the Northeast's states are built in and work with no signal from the first day;
// any other state is fetched by boot.js the first time the map is zoomed in there, and kept on the phone after that.
const XL_BUILT_IN = ['ny', 'ma', 'vt', 'ct', 'nh', 'nj', 'pa', 'ri', 'me'];
for (const d of ['vanished', 'mines']) { const src = path.join(site, 'data', d);
  if (fs.existsSync(src)) { fs.mkdirSync(path.join(out, 'data', d), { recursive: true });
    for (const f of fs.readdirSync(src)) if (f === 'index.json' || XL_BUILT_IN.indexOf(f.split('-')[0]) >= 0) fs.copyFileSync(path.join(src, f), path.join(out, 'data', d, f)); } }
// the historic pockets: the index, and for the nine states in XL_BUILT_IN their discs (<state>-k-<stamp>.json) and their detail (<state>.json); any other state is fetched by boot.js when the map looks at it, and kept
const pock = path.join(site, 'data', 'pock');
if (fs.existsSync(pock)) { fs.mkdirSync(path.join(out, 'data', 'pock'), { recursive: true }); for (const f of fs.readdirSync(pock)) if (f === 'index.json' || (f.endsWith('.json') && XL_BUILT_IN.indexOf(f.slice(0, 2)) >= 0)) fs.copyFileSync(path.join(pock, f), path.join(out, 'data', 'pock', f)); }
let html = fs.readFileSync(path.join(site, 'index.html'), 'utf8');
const swap = (re, to, what) => { if (!re.test(html)) { console.error('Could not find ' + what + ' in index.html; the page layout has changed.'); process.exit(1); } html = html.replace(re, to); };
swap(/<script src="app\.js\?v=[^"]*"><\/script>/, '<script src="boot.js"></script>', 'the app script tag');
swap(/<script src="leaflet\.js\?v=[^"]*"><\/script>/, '<script src="leaflet.js"></script>', 'the map library tag');
swap(/,viewport-fit=cover/, '', 'the viewport setting');
fs.writeFileSync(path.join(out, 'index.html'), html);
const v = (/"v":"(\d+)"/.exec(html) || [])[1];
const size = fs.readdirSync(out, { recursive: true }).reduce((n, f) => { const s = fs.statSync(path.join(out, f)); return n + (s.isFile() ? s.size : 0); }, 0);
console.log('www ready: place data build ' + v + ', ' + Math.round(size / 1024) + ' KB');
