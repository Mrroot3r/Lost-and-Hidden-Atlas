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
const { chromium } = require('playwright');
const JPG=Buffer.from('/9j/4AAQSkZJRgABAQEASABIAAD/2wBDAAMCAgICAgMCAgIDAwMDBAYEBAQEBAgGBgUGCQgKCgkICQkKDA8MCgsOCwkJDRENDg8QEBEQCgwSExIQEw8QEBD/yQALCAABAAEBAREA/8wABgAQEAX/2gAIAQEAAD8A0s8g/9k=','base64');
(async()=>{
  const fails=[]; const ok=(name,cond,extra)=>{ console.log((cond?'ok   ':'FAIL ')+name+(extra!==undefined?'  ['+extra+']':'')); if(!cond) fails.push(name); };
  const b=await chromium.launch();
  const url=process.argv[2]||'http://localhost:8766/index.html';
  async function open(vp,dpr,view,mobile){
    const c=await b.newContext({viewport:vp,deviceScaleFactor:dpr,isMobile:!!mobile,hasTouch:!!mobile});
    const p=await c.newPage(); const S={n:0,hang:0,delay:120,hangEvery:0,log:[],sizes:new Set(),esri:0};
    await c.route(u=>!/^http:\/\/localhost/.test(u.href),async r=>{ const u=r.request().url();
      if(!/\/(export|exportImage|tile)[\/?]/.test(u)) return r.fulfill({status:204,body:''});
      if(S.block) return r.abort();
      S.n++; S.log.push(u); const m=/size=(\d+)/.exec(u); if(m) S.sizes.add(+m[1]); if(/arcgisonline/.test(u)) S.esri++;
      if(/bbox=/.test(u)&&S.hangEvery&&S.n%S.hangEvery===0){ S.hang++; return; }                 // never answered
      await new Promise(z=>setTimeout(z,/bbox=/.test(u)?S.delay:15));
      r.fulfill({status:200,contentType:'image/jpeg',headers:{'access-control-allow-origin':'*'},body:JPG}).catch(()=>{}); });
    await p.addInitScript(v=>{ try{ localStorage.setItem('lost-hidden-atlas-v1',JSON.stringify({v:1,ui:{base:'leaf',view:v}})); }catch(e){} },view);
    const errs=[]; p.on('pageerror',e=>errs.push(e.message));
    await p.goto(url); await p.waitForFunction(()=>window.__atlasMap);
    const st=()=>p.evaluate(()=>{ const m=window.__atlasMap; let tot=0,real=0,ghost=0,shown=0; m.eachLayer(l=>{ if(l._tiles&&l.options.fn&&l.options.ghost){ for(const k in l._tiles){ const t=l._tiles[k]; if(!t.current) continue; tot++;
        const r=t.el._real||(t.el.tagName==='IMG'&&t.loaded); if(r) real++; else if(t.el._ghost) ghost++; if(t.loaded) shown++; } } });
      const q=window.__atlasTiles; return {z:m.getZoom(),tot:tot,real:real,ghost:ghost,shown:shown,dropped:q.dropped,retried:q.retried,sz:(()=>{ let s=0; m.eachLayer(l=>{ if(l.options.fn&&l.options.ghost) s=l.getTileSize().x; }); return s; })()}; });
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
  A.S.hangEvery=4; A.S.n=0; await A.p.evaluate(()=>{ window.__atlasMap.panBy([3000,0],{animate:false}); });
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
  P.S.hangEvery=3; P.S.n=0; await P.p.evaluate(()=>{ window.__atlasMap.panBy([0,2500],{animate:false}); }); s=await P.until(s=>s.tot>0&&s.real>=s.tot,26000);
  ok('phone: hung requests are asked again',s.real===s.tot&&s.retried>0,s.real+'/'+s.tot+', '+s.retried+' asked again');
  P.S.hangEvery=0; await P.zoom(8); s=await P.until(s=>s.tot>0&&s.real>=s.tot,8000);
  ok('phone: zoom 8 on leaf-off shows a map',s.tot>0&&s.real===s.tot,s.real+'/'+s.tot);
  ok('phone: no script errors',P.errs.length===0,P.errs.join(' | ').slice(0,200)); await P.c.close();
  await b.close();
  console.log(fails.length?('\n'+fails.length+' FAILED'):'\ntile loading test passed'); process.exit(fails.length?1:0);
})();
