// What is on the map, and what is not: pins, lead dots, pocket discs and old lines are kept on the map only in or near the
// view, because Leaflet works out every layer's position again at each zoom step, on screen or not.
//   node tools/overlay_test.js http://localhost:8766/index.html      (serve the built site first, as for smoke.js)
// Run it after changing syncMarkers(), viewDots()/viewSync(), drawLeads(), drawXL(), pockZoom() or the line levels (LLEV,
// syncLines()) in app.js. What it holds the app to:
//   1. every place in view has its pin, and most places out of view have none; panning brings in the pins for the new ground;
//   2. the chosen place keeps its pin wherever the map goes;
//   3. grouped pins are not made again when the map is nudged;
//   4. lead dots and pocket discs: all of those in view, few of those that are not; town centres are drawn over plain pockets
//      after the map moves as well as before;
//   5. the old lines are a handful of layers when zoomed out, and a tap on one still opens its box, zoomed out and zoomed in;
//   6. with everything switched on the map holds hundreds of layers, not thousands.
const { chromium } = require('playwright');
(async()=>{
  const fails=[]; const ok=(name,cond,extra)=>{ console.log((cond?'ok   ':'FAIL ')+name+(extra!==undefined?'  ['+extra+']':'')); if(!cond) fails.push(name); };
  const b=await chromium.launch(); const url=process.argv[2]||'http://localhost:8766/index.html';
  const c=await b.newContext({viewport:{width:390,height:844},deviceScaleFactor:2,isMobile:true,hasTouch:true}); const p=await c.newPage(); const errs=[]; p.on('pageerror',e=>errs.push(e.message));
  await c.route(u=>!/^http:\/\/localhost/.test(u.href),r=>r.fulfill({status:204,body:''}));
  await p.addInitScript(()=>{ try{ localStorage.setItem('lost-hidden-atlas-v1',JSON.stringify({v:1,ui:{base:'streets',view:[42.6526,-73.7562,13],hist:false,lines:{oldrail:true,canal:true,rail:true},leads:true,xl:{vanished:true,mines:true},pockets:true}})); }catch(e){} });
  await p.goto(url); await p.waitForFunction(()=>window.__atlasMap); await p.waitForTimeout(2500);
  const snap=()=>p.evaluate(async()=>{ const m=window.__atlasMap, b=m.getBounds(), D=JSON.parse(document.getElementById('d-sites').textContent), S=D.sites||D;
    const LD=window.__ld||(window.__ld=await fetch('data/leads.json').then(r=>r.json()).catch(()=>({p:[]})));
    let layers=0, pins=0, pinsIn=0, leads=0, leadsIn=0, discs=0, lines=0, xl=0; const xlIds=[];
    m.eachLayer(l=>{ layers++; const o=l.options||{};
      if(l.getLatLng&&o.riseOnHover){ pins++; if(b.contains(l.getLatLng())) pinsIn++; }
      if(o.pane!=='lines') return;
      if(o.casing) lines++;
      if(!l.getRadius) return;
      if(o.fillColor==='#ffd500'){ leads++; if(b.contains(l.getLatLng())) leadsIn++; }
      else if(o.fillColor==='#ff8a3d'||o.fillColor==='#aeb7c2'){ xl++; xlIds.push(l._leaflet_id); }
      else if(o.fillOpacity<=0.3) discs++; });
    /* drawing order of the discs: no plain pocket (dashed ring) may come after a town centre */
    let order=true, seenCentre=false, any=null; m.eachLayer(l=>{ if(!any&&l._renderer&&l.options.pane==='lines') any=l; });
    if(any){ for(let n=any._renderer._drawFirst;n;n=n.next){ const o=n.layer.options; if(!n.layer.getRadius||!(o.fillOpacity<=0.3)) continue; if(o.dashArray==='3 4'){ if(seenCentre) order=false; } else seenCentre=true; } }
    return {z:m.getZoom(),layers,pins,pinsIn,placesIn:S.filter(s=>b.contains([s.lat,s.lon])).length,places:S.length,leads,leadsIn,leadsData:LD.p.length,leadsDataIn:LD.p.filter(q=>b.contains([q[0],q[1]])).length,discs,order,lines,xl,xlIds,
      clus:document.querySelectorAll('.leaflet-marker-pane .clus').length,selPin:document.querySelectorAll('.leaflet-marker-pane .pin.sel').length}; });
  /* the old lines are fetched a state at a time (tools/lines_test.js is their own test): wait for what a view asked for */
  const lined=async()=>{ for(let i=0;i<40;i++){ const s=await p.evaluate(()=>window.__atlasLines?window.__atlasLines():{got:{}}); if(!Object.values(s.got).some(v=>v===1)&&s.wideWait!==1) return; await p.waitForTimeout(100); } };
  const go=async(la,lo,z)=>{ await p.evaluate(a=>{ window.__atlasMap.setView([a[0],a[1]],a[2],{animate:false}); },[la,lo,z]); await p.waitForTimeout(350); await lined(); };
  const pan=async(x,y)=>{ await p.evaluate(a=>{ window.__atlasMap.panBy(a,{animate:false}); },[x,y]); await p.waitForTimeout(350); };
  // 1. pins
  await lined(); let s=await snap();
  ok('zoom 13: every place in view has its pin',s.placesIn>0&&s.pinsIn===s.placesIn,s.pinsIn+' pins for '+s.placesIn+' places in view');
  ok('zoom 13: most places out of view have no pin on the map',s.pins<s.places/2,s.pins+' pins on the map of '+s.places+' places');
  await pan(380,-610); s=await snap(); ok('after a pan of a screen and more toward Troy: the pins for the new ground are there',s.placesIn>0&&s.pinsIn===s.placesIn,s.pinsIn+' of '+s.placesIn);
  await go(42.26,-71.80,14); s=await snap(); ok('after a jump to Worcester: its pins are there',s.placesIn>0&&s.pinsIn===s.placesIn,s.pinsIn+' of '+s.placesIn);
  // 2. the chosen place
  await go(42.6526,-73.7562,14); await p.evaluate(()=>{ let done=false; window.__atlasMap.eachLayer(l=>{ if(!done&&l.getLatLng&&l.options.riseOnHover&&window.__atlasMap.getBounds().contains(l.getLatLng())){ done=true; l.fire('click'); } }); }); await p.waitForTimeout(500);
  s=await snap(); const had=s.selPin; await go(42.8864,-78.8784,14); s=await snap();
  ok('the chosen place keeps its pin when the map goes 400 km away',had===1&&s.selPin===1,had+' then '+s.selPin);
  // 3. grouped pins
  await go(42.9,-75.5,8); s=await snap(); const mark=await p.evaluate(()=>{ const e=document.querySelector('.leaflet-marker-pane .clus'); if(e) e.setAttribute('data-keep','1'); return !!e; });
  await pan(30,20); const kept=await p.evaluate(()=>!!document.querySelector('.leaflet-marker-pane .clus[data-keep]'));
  ok('zoom 8: places are grouped, and a nudge does not make the groups again',s.clus>0&&mark&&kept,s.clus+' groups');
  // 4. leads and pockets
  await go(42.6526,-73.7562,13); s=await snap();
  ok('lead dots: all of those in view are drawn',s.leadsDataIn>0&&s.leadsIn===s.leadsDataIn,s.leadsIn+' of '+s.leadsDataIn+' in view');
  ok('lead dots: few of the rest are on the map',s.leads<s.leadsData/3,s.leads+' on the map of '+s.leadsData);
  ok('pocket discs: some in view, not the whole set',s.discs>0&&s.discs<600,s.discs+' discs');
  ok('pocket discs: town centres are drawn over plain pockets',s.order);
  const x0=s.xlIds; await pan(60,40); s=await snap();
  ok('pocket discs: still in the right order after the map moves',s.order&&s.discs>0,s.discs+' discs');
  ok('vanished places and mines: a dot that stays in view is kept, not made again',x0.length>0&&x0.filter(i=>s.xlIds.indexOf(i)>=0).length>=Math.min(x0.length,s.xlIds.length)*0.5,x0.length+' before, '+s.xlIds.length+' after, '+x0.filter(i=>s.xlIds.indexOf(i)>=0).length+' the same');
  ok('everything switched on at zoom 13: hundreds of layers, not thousands',s.layers<900,s.layers+' layers');
  // 5. lines
  const tap=()=>p.evaluate(()=>{ const m=window.__atlasMap, b=m.getBounds(); m.closePopup(); let hit=null; m.eachLayer(l=>{ if(hit||!(l.options&&l.options.casing)) return; const g=l.getLatLngs(); (Array.isArray(g[0])?g:[g]).forEach(q=>q.forEach(pt=>{ if(!hit&&b.contains(pt)) hit=[l,pt]; })); });
    if(!hit) return 'no line in view'; hit[0].fire('click',{latlng:hit[1]}); const e=m._popup&&m._popup.isOpen()&&m._popup.getElement();      /* the map's own box: one that is closing can still be in the page */
    return e?e.querySelector('.leaflet-popup-content').textContent.slice(0,60):'no box'; });
  let t=await tap(); ok('zoom 13: a tap on a line opens its box',t.length>5&&!/^no /.test(t),t);
  for(const z of [11,9,8,6]){ await go(42.75,-73.9,z); s=await snap(); t=await tap();
    ok('zoom '+z+': the lines are a handful of layers and a tap still opens a box',s.lines>0&&s.lines<90&&t.length>5&&!/^no /.test(t),s.lines+' layers; '+t); }
  await go(42.75,-73.9,12); s=await snap(); ok('everything switched on at zoom 12: hundreds of layers, not thousands',s.layers<900,s.layers+' layers');
  ok('no script errors',errs.length===0,errs.join(' | ').slice(0,200));
  await b.close(); console.log(fails.length?('\n'+fails.length+' FAILED'):'\noverlay test passed'); process.exit(fails.length?1:0);
})();
