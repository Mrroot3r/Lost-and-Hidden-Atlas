// How the slow map layers (leaf-off aerial, LiDAR) load: stand-in tile servers, so nothing here depends on the real ones.
//   node tools/tiles_test.js http://localhost:8766/index.html      (serve the built site first, as for smoke.js)
// Run it after changing how tiles are fetched, cached or drawn in app.js (TQ, tileBlob, CacheMixin, FnLayer, leafUrl, lidarUrl).
// What it holds the app to:
//   1. a request the server never answers is given up on and asked again, so the tile still arrives;
//   2. zooming through many levels does not fetch the levels passed through;
//   3. zoomed far out the leaf-off layer still shows a map (it used to go black below zoom 9);
//   4. while a slow tile is on its way, the same ground shows at once from a tile already held;
//   5. a wide screen asks in 512-pixel tiles, a phone in its own sharp 256-point tiles, and "save for offline" keeps
//      exactly the addresses the map will ask for;
//   6. ground already looked at shows again when the servers cannot be reached.
//   7. the world's ready-cut tile is laid beneath a state tile that is slow, has holes (a PNG) or failed;
//   8. each state's own server is asked, at the zoom it starts from, and Canada stays on the world hillshade;
//   9. the credit line names the states in view.
const { chromium } = require('playwright');
const PNG=Buffer.from('iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mNkYPhfDwAChwGA60e6kgAAAABJRU5ErkJggg==','base64');   // one see-through pixel
const JPG=Buffer.from('/9j/4AAQSkZJRgABAQEASABIAAD/2wBDAAMCAgICAgMCAgIDAwMDBAYEBAQEBAgGBgUGCQgKCgkICQkKDA8MCgsOCwkJDRENDg8QEBEQCgwSExIQEw8QEBD/yQALCAABAAEBAREA/8wABgAQEAX/2gAIAQEAAD8A0s8g/9k=','base64');
(async()=>{
  const fails=[]; const ok=(name,cond,extra)=>{ console.log((cond?'ok   ':'FAIL ')+name+(extra!==undefined?'  ['+extra+']':'')); if(!cond) fails.push(name); };
  const b=await chromium.launch();
  const url=process.argv[2]||'http://localhost:8766/index.html';
  async function open(vp,dpr,view,mobile){
    const c=await b.newContext({viewport:vp,deviceScaleFactor:dpr,isMobile:!!mobile,hasTouch:!!mobile});
    const p=await c.newPage(); const S={n:0,nb:0,hang:0,delay:120,hangEvery:0,log:[],sizes:new Set(),esri:0};
    await c.route(u=>!/^http:\/\/localhost/.test(u.href),async r=>{ const u=r.request().url();
      if(!/\/(export|exportImage|tile)[\/?]/.test(u)) return r.fulfill({status:204,body:''});
      if(S.block) return r.abort();
      S.n++; S.log.push(u); const m=/size=(\d+)/.exec(u); if(m) S.sizes.add(+m[1]); if(/arcgisonline/.test(u)) S.esri++;
      const cut=/bbox=/.test(u); if(cut) S.nb++;                                                  // cut to order by a state server; the rest are ready-cut tiles
      if(cut&&S.hangEvery&&S.nb%S.hangEvery===0){ S.hang++; return; }                            // never answered
      await new Promise(z=>setTimeout(z,cut?S.delay:15));
      if(cut&&S.fail) return r.fulfill({status:500,headers:{'access-control-allow-origin':'*'},body:'no'}).catch(()=>{});
      if(cut&&S.png) return r.fulfill({status:200,contentType:'image/png',headers:{'access-control-allow-origin':'*'},body:PNG}).catch(()=>{});
      r.fulfill({status:200,contentType:'image/jpeg',headers:{'access-control-allow-origin':'*'},body:JPG}).catch(()=>{}); });
    await p.addInitScript(v=>{ try{ localStorage.setItem('lost-hidden-atlas-v1',JSON.stringify({v:1,ui:{base:'leaf',view:v}})); }catch(e){} },view);
    const errs=[]; p.on('pageerror',e=>errs.push(e.message));
    await p.goto(url); await p.waitForFunction(()=>window.__atlasMap);
    const st=()=>p.evaluate(()=>{ const m=window.__atlasMap; let tot=0,real=0,ghost=0,shown=0,under=0; m.eachLayer(l=>{ if(l._tiles&&l.options.fn&&l.options.ghost){ for(const k in l._tiles){ const t=l._tiles[k]; if(!t.current) continue; tot++;
        const r=t.el._real||(t.el.tagName==='IMG'&&t.loaded); if(r) real++; else if(t.el._ghost) ghost++; if(t.loaded) shown++; if(t.el._under) under++; } } });
      const q=window.__atlasTiles; return {z:m.getZoom(),tot:tot,real:real,ghost:ghost,shown:shown,under:under,dropped:q.dropped,retried:q.retried,sz:(()=>{ let s=0; m.eachLayer(l=>{ if(l.options.fn&&l.options.ghost) s=l.getTileSize().x; }); return s; })()}; });
    const until=async(f,ms)=>{ const t=Date.now(); let s; for(;;){ s=await st(); if(f(s)||Date.now()-t>ms) return Object.assign(s,{ms:Date.now()-t}); await p.waitForTimeout(100); } };
    const zoom=z=>p.evaluate(z=>{ window.__atlasMap.setZoom(z,{animate:false}); },z);
    return {c,p,S,st,until,zoom,errs}; }

  // ---- a wide screen
  let A=await open({width:1920,height:1000},1,[42.549,-74.19,16]);
  let s=await A.until(s=>s.tot>0&&s.real>=s.tot,8000);
  ok('wide screen: the first view fills',s.tot>0&&s.real===s.tot,s.real+'/'+s.tot+' in '+s.ms+' ms');
  ok('wide screen: 512-pixel tiles, asked for at 512',s.sz===512&&A.S.sizes.has(512)&&!A.S.sizes.has(256),'tile '+s.sz+', sizes '+[...A.S.sizes].join(' '));
  ok('wide screen: a view takes a quarter of the requests it used to',A.S.n<=20,A.S.n+' requests');
  // 1. hung requests
  A.S.hangEvery=4; A.S.n=0; A.S.nb=0; await A.p.evaluate(()=>{ window.__atlasMap.panBy([3000,0],{animate:false}); });
  s=await A.until(s=>s.tot>0&&s.real>=s.tot,14000);
  ok('one request in four never answered: every tile still arrives',s.real===s.tot&&A.S.hang>0&&s.retried>0,s.real+'/'+s.tot+', '+A.S.hang+' hung, '+s.retried+' asked again, '+s.ms+' ms');
  A.S.hangEvery=0;
  // 2. zooming through levels
  A.S.delay=700; A.S.n=0; const d0=(await A.st()).dropped; for(const z of [15,14,13,12,13,14,15,16,17]){ await A.zoom(z); await A.p.waitForTimeout(120); }
  s=await A.until(s=>s.tot>0&&s.real>=s.tot,12000);
  ok('nine quick zoom steps: tiles for the levels passed through are not fetched',s.dropped-d0>=30&&A.S.n<=70,(s.dropped-d0)+' dropped, '+A.S.n+' fetched');
  ok('nine quick zoom steps: the level you stop on fills',s.real===s.tot&&s.tot>0,s.real+'/'+s.tot+' in '+s.ms+' ms');
  // 4. stand-ins
  A.S.delay=2500; await A.zoom(18); s=await A.until(s=>s.tot>0&&s.shown>=s.tot,1500);
  ok('zooming in past a level already held: the ground shows at once, stretched',s.shown===s.tot&&s.ghost>0&&s.real<s.tot,s.ghost+' stand-ins of '+s.tot+' in '+s.ms+' ms');
  s=await A.until(s=>s.real>=s.tot,9000); ok('then the sharp tiles replace them',s.real===s.tot&&s.ghost<=s.tot,s.real+'/'+s.tot);
  await A.zoom(17); s=await A.until(s=>s.tot>0&&s.shown>=s.tot,1500);
  ok('zooming back out: shows at once from tiles already held',s.shown===s.tot,s.shown+'/'+s.tot+' in '+s.ms+' ms');
  // 3. far out
  A.S.delay=120; A.S.esri=0; await A.zoom(7); s=await A.until(s=>s.tot>0&&s.real>=s.tot,8000);
  ok('zoom 7 on leaf-off: a map, not black',s.tot>0&&s.real===s.tot&&A.S.esri>0,s.real+'/'+s.tot+', '+A.S.esri+' ready-cut tiles');
  // 7. the world's ready-cut tile beneath a slow, holed or failed state tile
  const go=(la,lo,z,base)=>A.p.evaluate(a=>{ const m=window.__atlasMap; m.setView([a[0],a[1]],a[2],{animate:false}); if(a[3]){ const b=document.getElementById('lb-'+a[3]); if(b&&b.getAttribute('aria-pressed')!=='true') b.click(); } },[la,lo,z,base]);
  const asked=re=>A.S.log.filter(u=>re.test(u)).length;
  A.S.delay=4000; A.S.log.length=0; await go(42.70,-74.60,16); s=await A.until(s=>s.tot>0&&s.under>=s.tot,4000);
  ok('a slow tile with nothing held to stand in: the world tile shows beneath within two seconds',s.tot>0&&s.under===s.tot&&s.shown===s.tot&&s.real===0&&s.ms<2500,s.under+' of '+s.tot+' in '+s.ms+' ms');
  s=await A.until(s=>s.real>=s.tot,9000); ok('and the state tile takes its place when it comes',s.real===s.tot&&s.under===0,s.real+'/'+s.tot+', '+s.under+' still beneath');
  A.S.delay=120; A.S.png=true; await go(42.90,-74.90,16); s=await A.until(s=>s.tot>0&&s.real>=s.tot&&s.under>=s.tot,6000);
  ok('a state tile that comes back with holes keeps the world tile beneath it',s.tot>0&&s.real===s.tot&&s.under===s.tot,s.real+' real, '+s.under+' beneath, of '+s.tot); A.S.png=false;
  A.S.fail=true; await go(43.10,-75.20,16); s=await A.until(s=>s.tot>0&&s.under>=s.tot,9000);
  ok('a state server that answers with an error: the world tile is shown instead',s.tot>0&&s.under===s.tot&&s.shown===s.tot,s.under+' beneath, '+s.shown+' shown, of '+s.tot); A.S.fail=false;
  // 8. which server is asked, by state
  const route=async(name,la,lo,z,base,re,not)=>{ A.S.log.length=0; await go(la,lo,z,base); await A.until(s=>s.tot>0&&s.shown>=s.tot,5000); const n=asked(re), x=not?asked(not):0; ok(name,n>0&&x===0,n+' asked'+(not?', '+x+' of the wrong kind':'')); };
  await route('leaf-off in New Jersey asks the state\'s tiles',40.636,-74.913,16,'leaf',/maps\.nj\.gov\/.*Orthos_Natural_2020/,/bbox=/);
  await route('leaf-off in Connecticut asks the state\'s tiles',41.60,-72.70,16,'leaf',/cteco\.uconn\.edu\/.*Ortho_2023_tiled/,/bbox=/);
  await route('leaf-off in New Hampshire asks the state\'s tiles',43.249,-71.117,16,'leaf',/nhgeodata\.unh\.edu\/.*6in_tiled/,/bbox=/);
  await route('leaf-off in Pennsylvania asks the state for the picture layer alone',40.652,-77.753,16,'leaf',/imagery\.pasda\.psu\.edu\/.*layers=show:3/);
  await route('leaf-off in Pennsylvania zoomed out to 13 asks only ready-cut tiles',40.652,-77.753,13,'leaf',/World_Imagery/,/bbox=/);
  await route('leaf-off in Maine asks the state for a JPEG or a holed PNG',44.566,-68.803,16,'leaf',/gis\.maine\.gov\/.*format=jpgpng.*bandIds=0,1,2/);
  await route('leaf-off in Kansas asks the state',38.764,-95.131,16,'leaf',/services\.kgs\.ku\.edu\/.*NG911_Imagery_2024/);
  await route('LiDAR in Pennsylvania at zoom 16 asks the national elevation service',40.652,-77.753,16,'lidar',/elevation\.nationalmap\.gov\/.*Hillshade/);
  await route('LiDAR in Pennsylvania at zoom 15 asks only ready-cut tiles',40.652,-77.753,15,'lidar',/World_Hillshade/,/bbox=/);
  await route('LiDAR in Connecticut asks the state',41.60,-72.70,16,'lidar',/cteco\.uconn\.edu\/.*elevation\/Hillshade/);
  await route('LiDAR in New Hampshire asks the state, with the light direction',43.249,-71.117,16,'lidar',/nhgeodata\.unh\.edu\/.*LiDAR_Bare_Earth_DEM.*Hillshade/);
  await route('LiDAR in Maine asks the state',44.566,-68.803,16,'lidar',/gis\.maine\.gov\/.*Maine_Elevation_DEM_Statewide/);
  await route('LiDAR in Ontario stays on the world hillshade',43.654,-79.384,17,'lidar',/World_Hillshade/,/bbox=/);
  // 9. the credit line names the states in view, and stays one short line
  const credit=()=>A.p.evaluate(()=>{ const e=document.querySelector('.leaflet-control-attribution'); return e?e.textContent:''; });
  await go(40.636,-74.913,16,'leaf'); await A.p.waitForTimeout(150); let cr=await credit();
  ok('credit on leaf-off in New Jersey names New Jersey, not every state',/NJ Office of GIS/.test(cr)&&/Esri/.test(cr)&&!/MassGIS|Maine|Kansas/.test(cr),cr.slice(0,90));
  await go(40.652,-77.753,16,'lidar'); await A.p.waitForTimeout(150); cr=await credit();
  ok('credit on LiDAR in Pennsylvania names the national elevation service',/USGS 3DEP/.test(cr)&&!/NJ Office|PEMA/.test(cr),cr.slice(0,90));
  await go(43.654,-79.384,16,'lidar'); await A.p.waitForTimeout(150); cr=await credit();
  ok('credit on LiDAR in Ontario does not',!/USGS 3DEP/.test(cr)&&/Esri/.test(cr),cr.slice(0,90));
  ok('wide screen: still no script errors',A.errs.length===0,A.errs.join(' | ').slice(0,200));
  await go(42.549,-74.19,16,'leaf'); await A.until(s=>s.tot>0&&s.real>=s.tot,8000);                 // back where the saving checks expect to be
  // 5. saving
  await A.zoom(16); await A.until(s=>s.tot>0&&s.real>=s.tot,8000);
  const sv=await A.p.evaluate(()=>{ const m=window.__atlasMap; let shown=[],lyr=null; m.eachLayer(l=>{ if(l.options.fn&&l.options.ghost) lyr=l; });
    for(const k in lyr._tiles){ const t=lyr._tiles[k]; if(t.current) shown.push(lyr.getTileUrl(t.coords)); }
    const keep=new Set(); const n=Math.pow(2,16), bb=m.getBounds().pad(0.3), tx=lo=>Math.floor((lo+180)/360*n), ty=la=>{ const r=la*Math.PI/180; return Math.floor((1-Math.log(Math.tan(r)+1/Math.cos(r))/Math.PI)/2*n); };
    for(let x=tx(bb.getWest());x<=tx(bb.getEast());x++) for(let y=ty(bb.getNorth());y<=ty(bb.getSouth());y++) keep.add(lyr.saveUrl(x,y,16));
    return {shown:shown.length,miss:shown.filter(u=>!keep.has(u)).length}; });
  ok('wide screen: "save for offline" keeps the very addresses the map asks for',sv.shown>0&&sv.miss===0,sv.shown+' shown, '+sv.miss+' not kept');
  // tiles already seen still show when the servers cannot be reached
  await A.p.waitForTimeout(600); A.S.block=true; await A.p.reload(); await A.p.waitForFunction(()=>window.__atlasMap); s=await A.until(s=>s.tot>0&&s.real>=s.tot,8000);
  ok('wide screen: ground already looked at shows again with the servers unreachable',s.tot>0&&s.real===s.tot,s.real+'/'+s.tot);
  ok('wide screen: no script errors',A.errs.length===0,A.errs.join(' | ').slice(0,200)); await A.c.close();

  // ---- a phone
  let P=await open({width:390,height:844},2.6,[42.549,-74.19,16],true);
  s=await P.until(s=>s.tot>0&&s.real>=s.tot,8000);
  ok('phone: the first view fills',s.tot>0&&s.real===s.tot,s.real+'/'+s.tot+' in '+s.ms+' ms');
  ok('phone: ordinary tiles, asked for sharp',s.sz===256&&P.S.sizes.has(512)&&P.S.sizes.size===1,'tile '+s.sz+', sizes '+[...P.S.sizes].join(' '));
  P.S.hangEvery=3; P.S.n=0; P.S.nb=0; await P.p.evaluate(()=>{ window.__atlasMap.panBy([0,2500],{animate:false}); }); s=await P.until(s=>s.tot>0&&s.real>=s.tot,26000);
  ok('phone: hung requests are asked again',s.real===s.tot&&s.retried>0,s.real+'/'+s.tot+', '+s.retried+' asked again');
  P.S.hangEvery=0; await P.zoom(8); s=await P.until(s=>s.tot>0&&s.real>=s.tot,8000);
  ok('phone: zoom 8 on leaf-off shows a map',s.tot>0&&s.real===s.tot,s.real+'/'+s.tot);
  ok('phone: no script errors',P.errs.length===0,P.errs.join(' | ').slice(0,200)); await P.c.close();
  await b.close();
  console.log(fails.length?('\n'+fails.length+' FAILED'):'\ntile loading test passed'); process.exit(fails.length?1:0);
})();
