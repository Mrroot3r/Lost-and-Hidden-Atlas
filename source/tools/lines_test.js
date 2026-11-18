// The old rail and canal lines on the hosted copy: fetched a state at a time, and kept on the phone.
//   node tools/lines_test.js http://localhost:8766/index.html      (serve the built site first, as for smoke.js)
// Run it after changing how the lines are fetched or kept (LX, lineStatesIn(), lineFetch(), lineWideFetch(), lineForget(),
// linesWarm() in app.js; the lines store in sw.js) or how they are cut up (tools/lines_split.py, "s" in tools/lines.py).
// What it holds the app to:
//   1. a view of one town fetches that state's lines and no other state's, and never the one big file the Android app reads;
//   2. a wide view is drawn from the thinned picture of every state; a tap there on a line whose state is not on the phone
//      says so and offers to zoom in, and after zooming in the same tap opens the line's own box;
//   3. moving the map into another state fetches that state; the whole country in view, or a wide view of ground with no
//      lines, fetches nothing;
//   4. a place page fetches its own state's lines even with every line switch off, and lists the old lines passing the place;
//   5. the offline worker keeps the state files in their own store, drops the copy a new one replaces, and with no signal
//      the lines of a state already fetched are still drawn.
const { chromium } = require('playwright');
(async()=>{
  const fails=[]; const ok=(name,cond,extra)=>{ console.log((cond?'ok   ':'FAIL ')+name+(extra!==undefined?'  ['+extra+']':'')); if(!cond) fails.push(name); };
  const url=process.argv[2]||'http://localhost:8766/index.html', base=url.replace(/[^/]*$/,'');
  const b=await chromium.launch(); const errs=[];
  const open=async(state,hash,sw)=>{ const c=await b.newContext({viewport:{width:390,height:844},deviceScaleFactor:2,isMobile:true,hasTouch:true,serviceWorkers:sw?'allow':'block'}); const p=await c.newPage();
    const asked=[]; c.on('request',r=>{ const u=r.url(); if(u.indexOf('/data/lines')>=0) asked.push(u.replace(/^.*\/data\//,'').replace(/\?.*$/,'')); }); p.on('pageerror',e=>errs.push(e.message));
    await c.route(u=>!/^http:\/\/localhost/.test(u.href),r=>r.fulfill({status:204,body:''}));
    await p.addInitScript(s=>{ try{ if(!localStorage.getItem('lost-hidden-atlas-v1')) localStorage.setItem('lost-hidden-atlas-v1',JSON.stringify(s)); }catch(e){} },state);
    await p.goto(url+(hash||'')); await p.waitForFunction(()=>window.__atlasMap&&window.__atlasLines); return {c,p,asked}; };
  const ON={v:1,home:{id:'alb',by:1},ui:{base:'streets',view:[42.6526,-73.7562,13],hist:false,lines:{oldrail:true,canal:true,rail:true}}};
  // wait until nothing is on its way
  const settle=async p=>{ for(let i=0;i<60;i++){ const s=await p.evaluate(()=>window.__atlasLines()); if(!Object.values(s.got).some(v=>v===1)&&s.wideWait!==1){ await p.waitForTimeout(250); return s; } await p.waitForTimeout(150); } return p.evaluate(()=>window.__atlasLines()); };
  const go=async(p,la,lo,z)=>{ await p.evaluate(a=>{ window.__atlasMap.setView([a[0],a[1]],a[2],{animate:false}); },[la,lo,z]); await p.waitForTimeout(200); return settle(p); };
  const drawn=p=>p.evaluate(()=>{ let n=0; window.__atlasMap.eachLayer(l=>{ if(l.options&&l.options.casing) n++; }); return n; });
  // tap the first old line (not a railroad in use) that has a point in view; returns the text of the box that opens
  // (with `near`, the line point closest to that spot instead)
  const tap=(p,near)=>p.evaluate(near=>{ const m=window.__atlasMap, b=m.getBounds().pad(-0.1); m.closePopup(); let hit=null, bd=1e9; m.eachLayer(l=>{ if((hit&&!near)||!(l.options&&l.options.casing)||l.options.color==='#2b3136') return; const g=l.getLatLngs();
      (Array.isArray(g[0])?g:[g]).forEach(q=>q.forEach(pt=>{ if(near){ const d=Math.abs(pt.lat-near[0])+Math.abs(pt.lng-near[1]); if(d<bd){ bd=d; hit=[l,pt]; } } else if(!hit&&b.contains(pt)) hit=[l,pt]; })); });
    if(!hit) return 'no line in view'; window.__tapAt=[hit[1].lat,hit[1].lng]; hit[0].fire('click',{latlng:hit[1]}); const e=m._popup&&m._popup.isOpen()&&m._popup.getElement();      /* the map's own box: one that is closing can still be in the page */
    return e?e.querySelector('.leaflet-popup-content').textContent.slice(0,300):'no box'; },near||null);

  // 1. one town, one state
  let {c,p,asked}=await open(ON); let s=await settle(p);
  ok('the hosted copy fetches the lines a state at a time',s.split===true);
  ok('Albany at zoom 13: New York\'s lines are fetched',asked.indexOf('lines/ny.json')>=0&&s.got.ny===2,asked.join(' '));
  ok('Albany at zoom 13: no other state is fetched, nor the one big file',asked.every(a=>a==='lines/ny.json'||a==='lines/wide.json')&&asked.indexOf('lines.json')<0,asked.join(' '));
  let n=await drawn(p), t=await tap(p);
  ok('Albany at zoom 13: lines are drawn and a tap opens the line\'s box',n>0&&/Google Maps/.test(t),n+' layers; '+t);
  // 2. the wide picture
  s=await go(p,45.25,-69.1,7); n=await drawn(p);
  ok('zoom 7 over Maine: drawn from the thinned picture of every state, with no state fetched for it',s.wide===true&&asked.indexOf('lines/wide.json')>=0&&!s.got.me&&n>0,n+' layers; '+asked.join(' '));
  t=await tap(p);
  ok('zoom 7 over Maine: a tap on a line whose state is not here says to zoom in',/Zoom in here/.test(t)&&!/Google Maps/.test(t),t);
  await p.evaluate(()=>window.__atlasMap._popup.getElement().querySelector('button').click()); await p.waitForTimeout(400); s=await settle(p);
  const z=await p.evaluate(()=>window.__atlasMap.getZoom()); t=await tap(p);
  ok('"Zoom in here" goes to zoom 11, fetches Maine, and the tap now opens the line\'s own box',z===11&&s.got.me===2&&/Google Maps/.test(t),'zoom '+z+'; '+t);
  const at=await p.evaluate(()=>window.__tapAt); await go(p,at[0],at[1],7); t=await tap(p,at);
  ok('back at zoom 7: with Maine on the phone the tap opens the line\'s own box',/Google Maps/.test(t),t);
  // 3. another state by moving the map
  s=await go(p,41.41,-75.66,10); n=await drawn(p);
  ok('the map moved to Scranton: Pennsylvania is fetched and drawn',s.got.pa===2&&asked.indexOf('lines/pa.json')>=0&&n>0,n+' layers');
  s=await go(p,41.8,-71.42,12); ok('the map moved to Providence: Rhode Island is fetched',s.got.ri===2,Object.keys(s.got).join(' '));
  ok('each file was asked for once',asked.length===new Set(asked).size,asked.join(' '));
  await c.close();

  // 3b. views that need no lines fetch none
  { const FAR=JSON.parse(JSON.stringify(ON)); FAR.ui.view=[39,-96,4]; ({c,p,asked}=await open(FAR)); await p.waitForTimeout(800); s=await settle(p); n=await drawn(p);
    ok('the whole country in view (zoom 4): no lines are drawn and none are fetched',n===0&&asked.length===0,n+' layers; '+(asked.join(' ')||'nothing asked'));
    s=await go(p,39.1,-94.58,7); ok('zoom 7 over Kansas City, where the Atlas has no lines: nothing is fetched',asked.length===0,asked.join(' ')||'nothing asked');
    s=await go(p,40.6,-79.5,6); n=await drawn(p); ok('zoom 6 over western Pennsylvania: the thinned picture is fetched and drawn',asked.join()==='lines/wide.json'&&n>0,n+' layers; '+asked.join(' '));
    s=await go(p,41.41,-75.66,11); ok('zoom 11 at Scranton, 60 km from New York: Pennsylvania alone is fetched',s.got.pa===2&&!s.got.ny&&asked.join()==='lines/wide.json,lines/pa.json',asked.join(' '));
    await c.close(); }
  // 4. a place page, every line switch off. The place: one outside New York within 150 m of an old line, found here from the built files.
  const D=JSON.parse(/<script type="application\/json" id="d-sites">([\s\S]*?)<\/script>/.exec(await (await fetch(url)).text())[1]);
  const regOf={}; D.states.forEach(st=>st.regions.forEach(r=>{ regOf[r[0]]=st.k; }));
  let pick=null;
  for(const k of Object.keys(D.lx.s)){ if(k==='ny'||pick) continue; const L=await (await fetch(base+'data/lines/'+k+'.json')).json();
    for(const site of D.sites){ if(regOf[site.reg]!==k||pick) continue; const kx=Math.cos(site.lat*Math.PI/180)*111320;
      for(const f of L){ if(f.k==='rr'||f.k==='cn'||pick) continue; for(const part of f.c){ if(pick) break; for(const q of part){ const dx=(q[1]-site.lon)*kx, dy=(q[0]-site.lat)*110540; if(dx*dx+dy*dy<150*150){ pick={id:site.id,st:k,name:site.name}; break; } } } } } }
  ok('there is a place outside New York beside an old line to try',!!pick,pick?pick.id+' ('+pick.st+')':'none');
  if(pick){ const OFF=JSON.parse(JSON.stringify(ON)); OFF.ui.lines={oldrail:false,canal:false,rail:false}; delete OFF.ui.view;
    ({c,p,asked}=await open(OFF,'#'+pick.id)); await p.waitForTimeout(600); s=await settle(p);
    const head=await p.evaluate(()=>[...document.querySelectorAll('#v-detail h3')].some(h=>h.textContent==='Old lines passing here'));
    ok('a place page with every line switch off fetches its state\'s lines',s.got[pick.st]===2&&asked.indexOf('lines/wide.json')<0,pick.id+': '+asked.join(' '));
    ok('and lists the old lines passing the place',head,pick.name);
    ok('and draws none of them, the switches being off',(await drawn(p))===0);
    await c.close(); }

  // 5. the offline worker
  ({c,p,asked}=await open(ON,'',true)); await settle(p);
  await p.evaluate(()=>navigator.serviceWorker.ready); await p.reload(); await p.waitForFunction(()=>window.__atlasMap&&window.__atlasLines&&navigator.serviceWorker.controller); await settle(p);
  const keys=()=>p.evaluate(async()=>{ const out={}; for(const k of await caches.keys()){ out[k.replace(/-\d+$/,'')]=(await (await caches.open(k)).keys()).map(r=>r.url.replace(/^.*?\/\/[^/]+\//,'')); } return out; });
  let k=await keys();
  ok('the offline worker keeps a fetched state in the lines store',(k['atlas-lines']||[]).some(u=>/^data\/lines\/ny\.json\?v=/.test(u)),JSON.stringify(k['atlas-lines']));
  ok('and the one big file is not kept for the hosted copy',!Object.keys(k).some(c2=>k[c2].some(u=>/^data\/lines\.json/.test(u))));
  await p.evaluate(()=>fetch('data/lines/ny.json?v=newstamp').then(r=>r.text())); await p.waitForTimeout(300); k=await keys();
  ok('a state fetched under a new stamp replaces the copy it had',(k['atlas-lines']||[]).filter(u=>/^data\/lines\/ny\.json/.test(u)).join()==='data/lines/ny.json?v=newstamp',JSON.stringify(k['atlas-lines']));
  await p.evaluate(()=>caches.open('atlas-lines').then(c2=>c2.delete('data/lines/ny.json?v=newstamp'))); await p.reload(); await p.waitForFunction(()=>window.__atlasMap&&window.__atlasLines); await settle(p);
  await c.setOffline(true); await p.reload(); await p.waitForFunction(()=>window.__atlasMap&&window.__atlasLines,null,{timeout:20000}).catch(()=>{}); s=await settle(p).catch(()=>({got:{}})); n=await drawn(p).catch(()=>0);
  ok('with no signal the page opens and New York\'s lines are drawn from the phone',s.got.ny===2&&n>0,n+' layers');
  s=await go(p,41.41,-75.66,10).catch(()=>({got:{}})); const ban=await p.evaluate(()=>(document.querySelector('#banner')||{}).textContent||'');
  ok('with no signal a state never fetched says the lines could not load',!(s.got.pa===2)&&/could not load/.test(ban),ban.slice(0,70));
  await c.close();
  ok('no script errors',errs.length===0,errs.join(' | ').slice(0,200));
  await b.close(); console.log(fails.length?('\n'+fails.length+' FAILED'):'\nlines test passed'); process.exit(fails.length?1:0);
})();
