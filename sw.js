/* Keeps the Atlas on the phone so it opens with no signal. The page itself is always fetched fresh when there is a connection.
   Three stores: the page and its scripts (thrown away at each new build), old survey maps, and the old rail and canal lines.
   The lines come one state to a file (data/lines/), each address carrying a stamp of the file's content, so a state is
   fetched again only when its lines change, not at every build; the copy it replaces is dropped then. */
const V='2611210854', SHELL='atlas-shell-'+V, KEEP='atlas-topo', LINES='atlas-lines';
self.addEventListener('install',e=>{ self.skipWaiting();
  e.waitUntil(caches.open(SHELL).then(c=>c.addAll(['./','app.js?v='+V,'leaflet.js?v=1.9.4'])).catch(()=>{})); });
self.addEventListener('activate',e=>{ e.waitUntil(caches.keys().then(ks=>Promise.all(ks.filter(k=>k!==SHELL&&k!==KEEP&&k!==LINES).map(k=>caches.delete(k)))).then(()=>self.clients.claim())); });
self.addEventListener('fetch',e=>{ const r=e.request; if(r.method!=='GET') return; const u=new URL(r.url); if(u.origin!==self.location.origin) return;
  const topo=u.pathname.indexOf('/topo/')>=0, lines=u.pathname.indexOf('/data/lines/')>=0, fixed=topo||lines||u.search.indexOf('v=')>=0;
  e.respondWith((async()=>{ const c=await caches.open(topo?KEEP:lines?LINES:SHELL);
    if(fixed){ const hit=await c.match(r); if(hit) return hit; const net=await fetch(r);
      if(net.ok){ if(lines) await c.delete(r,{ignoreSearch:true}).catch(()=>{}); c.put(r,net.clone()); } return net; }
    const cached=await c.match(r,{ignoreSearch:true});
    try{ const net=await Promise.race([fetch(r),new Promise((_,no)=>setTimeout(()=>no(new Error('slow')),cached?4000:30000))]); if(net.ok) c.put(r,net.clone()); return net; }
    catch(err){ if(cached) return cached; throw err; } })()); });
