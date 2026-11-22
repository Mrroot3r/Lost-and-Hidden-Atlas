// What is on the map, and what is not: pins, lead dots, pocket discs and old lines are kept on the map only in or near the
// view, because Leaflet works out every layer's position again at each zoom step, on screen or not.
//   node tools/overlay_test.js http://localhost:8766/index.html      (serve the built site first, as for smoke.js)
// Run it after changing syncMarkers(), the pinch picture (pinchBegin(), pinDraw()), pockLabels(), viewDots()/viewSync(), drawLeads(), drawXL(), pockZoom() or the line levels (LLEV,
// syncLines()) in app.js. What it holds the app to:
//   1. every place in view has its pin, and most places out of view have none; panning brings in the pins for the new ground;
//   2. the chosen place keeps its pin wherever the map goes;
//   3. grouped pins are not made again when the map is nudged;
//   4. lead dots and pocket discs: all of those in view, few of those that are not; town centres are drawn over plain pockets
//      after the map moves as well as before;
//   5. the old lines are a handful of layers when zoomed out, and a tap on one still opens its box, zoomed out and zoomed in;
//   6. with everything switched on the map holds hundreds of layers, not thousands.
//   7. for the length of a pinch one picture stands in for the pins, drawn again when it has stretched far, and they are back after it;
//   8. the old town centres are drawn over the heat map, with their names from zoom 8.
const { chromium } = require('playwright');
(async()=>{
  const fails=[]; const ok=(name,cond,extra)=>{ console.log((cond?'ok   ':'FAIL ')+name+(extra!==undefined?'  ['+extra+']':'')); if(!cond) fails.push(name); };
  const b=await chromium.launch(); const url=process.argv[2]||'http://localhost:8766/index.html';
  const c=await b.newContext({viewport:{width:390,height:844},deviceScaleFactor:2,isMobile:true,hasTouch:true}); await c.addInitScript(()=>{ try{ if(!localStorage.getItem('lost-hidden-atlas-v1')) localStorage.setItem('lost-hidden-atlas-v1',JSON.stringify({set:{heat:false}})); }catch(e){} });      /* these checks are of the numbered discs, the backup since the heat map became what a first visit shows */ const p=await c.newPage(); const errs=[]; p.on('pageerror',e=>errs.push(e.message));
  await c.route(u=>!/^http:\/\/localhost/.test(u.href),r=>r.fulfill({status:204,body:''}));
  await p.addInitScript(()=>{ try{ localStorage.setItem('lost-hidden-atlas-v1',JSON.stringify({v:1,set:{heat:false},ui:{base:'streets',view:[42.6526,-73.7562,13],hist:false,lines:{oldrail:true,canal:true,rail:true},leads:true,xl:{vanished:true,mines:true},pockets:true}})); }catch(e){} });
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
  // ---- leads cover the whole continent since November 2026, so a view of half a country draws none of them (LEADZ)
  await go(29.5,-98.5,9); s=await snap(); ok('lead dots: Texas has them, and those in view are drawn',s.leadsDataIn>5&&s.leadsIn===s.leadsDataIn,s.leadsIn+' of '+s.leadsDataIn+' round San Antonio');
  await go(39.5,-98,4); s=await snap(); ok('lead dots: a view of the whole country draws none',s.leads===0&&s.leadsDataIn>1000,s.leads+' on the map, '+s.leadsDataIn+' in view');
  await go(39.5,-98,5); s=await snap(); ok('lead dots: none at zoom 5 either',s.leads===0&&s.leadsDataIn>300,s.leads+' on the map, '+s.leadsDataIn+' in view');
  await go(41.5,-75,6); s=await snap(); ok('lead dots: back at zoom 6, and no more than the Northeast held before',s.leadsIn===s.leadsDataIn&&s.leadsIn>500&&s.leads<3000,s.leadsIn+' of '+s.leadsDataIn+' in view, '+s.leads+' on the map');
  await go(42.75,-73.9,12);
  // ---- historic pockets (the owner's notes, November 19, 2026): no outlines round districts; the discs start at the
  //      20-mile scale (zoom 8); zoomed in, listed buildings (white dots) show and plain markers (purple dots) only when asked for
  { const c4=await b.newContext({viewport:{width:390,height:844},deviceScaleFactor:2,isMobile:true,hasTouch:true}); const q=await c4.newPage(); q.on('pageerror',e=>errs.push(e.message));
    await c4.route(u=>!/^http:\/\/localhost/.test(u.href),r=>r.fulfill({status:204,body:''}));
    await q.addInitScript(()=>{ try{ if(!localStorage.getItem('lost-hidden-atlas-v1')) localStorage.setItem('lost-hidden-atlas-v1',JSON.stringify({v:1,home:{id:'alb',by:1},ui:{base:'streets',view:[42.6526,-73.7562,16],hist:false,pockets:true,lines:{oldrail:false,canal:false,rail:false}}})); }catch(e){} });
    await q.goto(url); await q.waitForFunction(()=>window.__atlasMap); await q.waitForTimeout(3500);
    const pk=()=>q.evaluate(()=>{ let boxes=0, white=0, purple=0, discs=0; window.__atlasMap.eachLayer(l=>{ const o=l.options||{}; if(o.pane!=='lines') return;
      if(!l.getRadius){ if(l.getLatLngs&&o.dashArray==='5 5') boxes++; return; }
      if(o.fillColor==='#ffffff'&&o.fillOpacity===1) white++; else if(o.fillColor==='#5b3fd6'&&o.fillOpacity===1) purple++; else if(o.fillOpacity<=0.3) discs++; }); return {boxes,white,purple,discs,z:window.__atlasMap.getZoom()}; });
    let k=await pk();
    ok('pockets, downtown Albany at street level: the listed buildings are there as white dots',k.white>10,JSON.stringify(k));
    ok('no dashed outline is drawn round a district',k.boxes===0,k.boxes+' outlines');
    ok('the plain markers (purple dots) are not shown until asked for',k.purple===0,k.purple+' purple dots');
    await q.click('#lb-opt'); await q.waitForTimeout(300);
    const sw=await q.evaluate(()=>{ const m=document.querySelector('#pock-m'), r=document.querySelector('#pock-r'); return m&&r?{m:m.checked,r:r.checked}:null; });
    ok('Map options has a switch for each kind of dot: listed buildings on, markers off',!!sw&&sw.r===true&&sw.m===false,JSON.stringify(sw));
    if(sw) await q.evaluate(()=>document.querySelector('#pock-m').click()); await q.waitForTimeout(700); k=await pk();
    ok('markers switched on: the purple dots come',k.purple>10&&k.white>10,JSON.stringify(k));
    if(sw) await q.evaluate(()=>{ document.querySelector('#pock-m').click(); document.querySelector('#pock-r').click(); }); await q.waitForTimeout(700); k=await pk();
    ok('both switched off: no dots, and the discs stay',k.purple===0&&k.white===0&&k.discs>0,JSON.stringify(k));
    await q.click('#sheet-x').catch(()=>{});
    // other pockets (dashed rings) are off until asked for; a tap inside a big disc but away from its middle does nothing; the box is small
    const rings=()=>q.evaluate(()=>{ let d=0,c=0; window.__atlasMap.eachLayer(l=>{ const o=l.options||{}; if(o.pane==='lines'&&l.getRadius&&o.fillOpacity<=0.3){ if(o.dashArray==='3 4') d++; else c++; } }); return {dashed:d,centres:c}; });
    await q.evaluate(()=>{ window.__atlasMap.setView([42.6526,-73.7562],14,{animate:false}); }); await q.waitForTimeout(900); let rg=await rings();
    ok('other pockets (the dashed rings) are not drawn until asked for; the town centre is',rg.dashed===0&&rg.centres>0,JSON.stringify(rg));
    await q.click('#lb-opt'); await q.waitForTimeout(300); const po=await q.evaluate(()=>{ const n=document.querySelector('#pock-o'); return n?n.checked:null; });
    if(po!==null) await q.evaluate(()=>document.querySelector('#pock-o').click()); await q.waitForTimeout(700); rg=await rings();
    ok('"Also show other pockets" is off to begin with and brings them when ticked',po===false&&rg.dashed>2,po+' '+JSON.stringify(rg));
    if(po!==null) await q.evaluate(()=>document.querySelector('#pock-o').click()); await q.click('#sheet-x').catch(()=>{}); await q.waitForTimeout(400);
    const tapDisc=(frac)=>q.evaluate(f=>{ const m=window.__atlasMap; m.closePopup(); let disc=null; m.eachLayer(l=>{ const o=l.options||{}; if(!disc&&o.pane==='lines'&&l.getRadius&&o.fillOpacity<=0.3&&o.dashArray!=='3 4'&&l.getRadius()>60) disc=l; }); if(!disc) return {none:true};
      const c=disc.getLatLng(), cp=m.latLngToContainerPoint(c), pt=L.point(cp.x+disc.getRadius()*f,cp.y), ll=m.containerPointToLatLng(pt); disc.fire('click',{latlng:ll,containerPoint:pt,layerPoint:m.containerPointToLayerPoint(pt)});
      const e=m._popup&&m._popup.isOpen()&&m._popup.getElement(); return {r:Math.round(disc.getRadius()),open:!!e,text:e?e.querySelector('.leaflet-popup-content').textContent:'',h:e?Math.round(e.getBoundingClientRect().height):0}; },frac);
    let td=await tapDisc(0.7); ok('a tap inside a big town-centre disc, away from its middle, opens nothing',!td.none&&td.r>60&&!td.open,JSON.stringify(td).slice(0,120));
    td=await tapDisc(0.05); ok('a tap on its middle opens its box',td.open&&/score/i.test(td.text),JSON.stringify(td).slice(0,160));
    ok('the box is small: the name, the score, the counts and one button',td.open&&td.h<170&&td.text.length<170&&!/Ranked by|mostly speak/.test(td.text),td.h+' px, '+td.text.length+' characters');
    await q.evaluate(()=>window.__atlasMap.closePopup());
    // a weak town centre close to a stronger one is left off the map (it is still in the list in Map options)
    const thin=await q.evaluate(async()=>{ const ix=await fetch('data/pock/index.json').then(r=>r.json()), k=(await fetch('data/pock/ny-k-'+ix.s.ny.kh+'.json').then(r=>r.json())).k.filter(r=>r[10]==='c');
      const km=(a,b)=>Math.hypot((a[0]-b[0])*111,(a[1]-b[1])*111*Math.cos(a[0]*Math.PI/180)); const w=k.find(r=>r[11]<15&&k.some(o=>o!==r&&o[11]>r[11]&&km(r,o)<3)), lone=k.find(r=>r[11]<15&&r[11]>=8&&!k.some(o=>o!==r&&km(r,o)<6)); if(!w||!lone) return null;
      const at=async r=>{ const m=window.__atlasMap; m.setView([r[0],r[1]],13,{animate:false}); await new Promise(z=>setTimeout(z,900)); let n=0; m.eachLayer(l=>{ const o=l.options||{}; if(o.pane==='lines'&&l.getRadius&&o.fillOpacity<=0.3){ const c=l.getLatLng(); if(Math.abs(c.lat-r[0])<1e-5&&Math.abs(c.lng-r[1])<1e-5) n++; } }); return n; };
      return {weak:w[7],weakOn:await at(w),lone:lone[7],loneOn:await at(lone)}; });
    ok('a weak town centre beside a stronger one is left off the map; a lone weak one stays',!!thin&&thin.weakOn===0&&thin.loneOn===1,JSON.stringify(thin));
    await q.evaluate(()=>{ window.__atlasMap.setView([42.65,-73.75],7,{animate:false}); }); await q.waitForTimeout(700); k=await pk();
    ok('at the 50-mile scale (zoom 7) no pocket disc is drawn',k.discs===0,JSON.stringify(k));
    await q.evaluate(()=>{ window.__atlasMap.setZoom(8,{animate:false}); }); await q.waitForTimeout(700); k=await pk();
    ok('at the 20-mile scale (zoom 8) the best town centres show',k.discs>0&&k.discs<200,JSON.stringify(k));
    // over the heat map, with their names (the owner, November 22, 2026): under it the discs were tinted and looked odd, and a town's name is what finds the right town when the street map's own names are too small to read
    const ov=await q.evaluate(()=>{ const m=window.__atlasMap, zi=n=>{ const e=m.getPane(n); return e?+getComputedStyle(e).zIndex:null; }, lab=[...document.querySelectorAll('.leaflet-marker-pane .pocklab span')].map(e=>e.textContent);
      return {heat:document.querySelectorAll('.leaflet-pane img.heatimg').length,zHeat:zi('heat'),zLines:zi('lines'),names:lab.length,blank:lab.filter(t=>!t.trim()).length,first:lab.slice(0,3)}; });
    ok('at zoom 8 the heat map is showing, and the town centres are drawn over it, not under',ov.heat===1&&ov.zHeat!==null&&ov.zLines!==null&&ov.zHeat<ov.zLines,JSON.stringify(ov));
    ok('at zoom 8 the best town centres in view have their names written by them',ov.names>=5&&ov.names<=20&&ov.blank===0,JSON.stringify(ov));
    await q.evaluate(()=>{ window.__atlasMap.setZoom(7,{animate:false}); }); await q.waitForTimeout(700);
    ok('at zoom 7, where no disc is drawn, no name is either',(await q.evaluate(()=>document.querySelectorAll('.leaflet-marker-pane .pocklab').length))===0);
    await c4.close(); }
  // ---- the old town centres travel one state at a time: an index, then a state's discs when the map looks at it or
  //      the reader stands in it. Nobody looking at Albany downloads Ohio.
  { const c6=await b.newContext({viewport:{width:390,height:844},deviceScaleFactor:2,isMobile:true,hasTouch:true}); const q=await c6.newPage(); const got=[]; q.on('pageerror',e=>errs.push(e.message));
    await c6.route(u=>!/^http:\/\/localhost/.test(u.href),r=>r.fulfill({status:204,body:''}));
    q.on('request',r=>{ const m=/\/data\/(pockets\.json|pock\/index\.json|pock\/([a-z]{2})-k-[0-9a-f]{8}\.json)/.exec(r.url()); if(m) got.push(m[2]?'k:'+m[2]:m[1]); });
    await q.addInitScript(()=>{ try{ localStorage.setItem('lost-hidden-atlas-v1',JSON.stringify({v:1,home:{id:'alb',by:1},ui:{base:'streets',view:[42.6526,-73.7562,13],hist:false,pockets:true,lines:{oldrail:false,canal:false,rail:false},nm:{r:3,al:0,k:{p:0,l:0,v:0,m:0,c:1}}}})); }catch(e){} });
    await q.goto(url); await q.waitForFunction(()=>window.__atlasMap); await q.waitForTimeout(3000);
    const discs=()=>q.evaluate(()=>{ let n=0; window.__atlasMap.eachLayer(l=>{ const o=l.options||{}; if(o.pane==='lines'&&l.getRadius&&o.fillOpacity<=0.3) n++; }); return n; });
    ok('town centres over Albany: the index and New York\'s discs are fetched',got.indexOf('pock/index.json')>=0&&got.indexOf('k:ny')>=0,got.join(' '));
    ok('and not the old whole file, nor a far state',got.indexOf('pockets.json')<0&&!got.some(x=>/^k:(va|oh|md|me|pa)$/.test(x)),got.join(' '));
    ok('New York\'s discs are drawn',await discs()>0,await discs()+' discs');      /* round Albany that is the city's own centre: the other pockets are off by default */
    const ix=await q.evaluate(()=>fetch('data/pock/index.json').then(r=>r.json()));
    ok('the index lists every state with its stamps and its box, and no discs itself',Object.keys(ix.s||{}).length>=15&&Object.values(ix.s).every(o=>/^[0-9a-f]{8}$/.test(o.kh||'')&&o.h&&Array.isArray(o.b)&&o.b.length===4&&o.n>0)&&!(ix.k&&ix.k.length),Object.keys(ix.s||{}).length+' states');
    await q.evaluate(()=>{ window.__atlasMap.setView([37.54,-77.44],12,{animate:false}); }); await q.waitForTimeout(2200);
    ok('the map moved to Richmond: Virginia\'s discs come then, and are drawn',got.indexOf('k:va')>=0&&await discs()>3,got.join(' ')+'; '+await discs()+' discs');
    const before=got.length; await q.evaluate(()=>{ window.__atlasMap.setView([37.56,-77.40],12,{animate:false}); }); await q.waitForTimeout(900);
    ok('a state that has come is not fetched again',got.length===before,got.slice(before).join(' '));
    await q.click('#lb-opt'); await q.waitForTimeout(1500);
    ok('Map options lists the town centres near the middle of the map or the start place',await q.locator('#sheet-b .pocklist button').count()>0,await q.locator('#sheet-b .pocklist button').count()+' listed');
    await q.click('#sheet-x').catch(()=>{});
    await q.evaluate(()=>{ window.__atlasNM.nmCollect([40.44,-79.99],3); }); await q.waitForTimeout(2000);
    const nc=await q.evaluate(()=>window.__atlasNM.nmCollect([40.44,-79.99],3).filter(t=>t.k==='c').length);
    ok('Near: standing in Pittsburgh with town centres among the kinds wanted brings Pennsylvania\'s',got.indexOf('k:pa')>=0&&nc>0,nc+' centres within 3 miles; '+got.join(' '));
    const old=await q.evaluate(()=>fetch('data/pockets.json').then(r=>r.json()).then(j=>({st:Object.keys(j.s||{}).length,k:j.k.length,stray:j.k.filter(k=>!(j.s||{})[k[8]]).length})));
    ok('the old whole file is still there for older copies of the Android app, and has stopped growing',old.st>0&&old.st<=15&&old.k>1000&&old.stray===0,JSON.stringify(old));
    await c6.close(); }
  // ---- grouped pins are coloured by how many places they stand for, cool to hot, and the biggest are a little larger
  { await go(42.9,-75.5,6); await p.waitForTimeout(400);
    const cl=await p.evaluate(()=>[...document.querySelectorAll('.leaflet-marker-pane .clus')].map(e=>({n:+e.textContent,c:(/\bc(\d)\b/.exec(e.className)||[])[1],bg:getComputedStyle(e).backgroundColor,w:e.offsetWidth})).sort((a,b)=>a.n-b.n));
    const lo=cl[0], hi=cl[cl.length-1], step=n=>n<10?0:n<30?1:n<100?2:n<300?3:4;
    ok('grouped pins: each disc carries the step its count belongs to',cl.length>3&&cl.every(x=>+x.c===step(x.n)),cl.map(x=>x.n+':c'+x.c).join(' '));
    ok('grouped pins: the smallest and the biggest are different colours, and the biggest is larger',!!lo&&!!hi&&hi.n>=300&&lo.bg!==hi.bg&&hi.w>lo.w,lo&&hi?lo.n+' '+lo.bg+' '+lo.w+'px; '+hi.n+' '+hi.bg+' '+hi.w+'px':'');
    const cols=new Set(cl.map(x=>x.bg)); ok('grouped pins: as many colours as steps in view',cols.size===new Set(cl.map(x=>x.c)).size&&cols.size>=3,[...cols].join(' | '));
    await go(42.75,-73.9,12); }
  // ---- Native American sites and leads on reservation land are their own category: a second file that nobody is sent
  //      until they switch it on under the gear (Settings, "nativeLeads"). Off, nothing of it is fetched, drawn or listed.
  { const c3=await b.newContext({viewport:{width:390,height:844},deviceScaleFactor:2,isMobile:true,hasTouch:true}); const q=await c3.newPage(); const got=[]; q.on('pageerror',e=>errs.push(e.message));
    await c3.route(u=>!/^http:\/\/localhost/.test(u.href),r=>r.fulfill({status:204,body:''}));
    q.on('request',r=>{ if(/\/data\/leads\//.test(r.url())) got.push(r.url().replace(/^.*\/data\//,'').replace(/\?.*$/,'')); });
    const MV=[37.18,-108.49];      /* Mesa Verde: hundreds of mapped sites, and no ordinary lead for miles */
    await q.addInitScript(a=>{ try{ if(!localStorage.getItem('lost-hidden-atlas-v1')) localStorage.setItem('lost-hidden-atlas-v1',JSON.stringify({v:1,home:{id:'alb',by:1},ui:{base:'streets',view:[a[0],a[1],12],hist:false,leads:true}})); }catch(e){} },MV);
    await q.goto(url); await q.waitForFunction(()=>window.__atlasMap); await q.waitForTimeout(2600);
    const NAMES=/^(Archaeological site|Native American site|Probably a Native American site|.+ on reservation land)$/;
    const LJ=await q.evaluate(()=>fetch('data/leads.json').then(r=>r.json()));
    const x=LJ.x&&LJ.x.native;
    ok('the leads file holds none of that category, and says where the rest is',!LJ.t.some(n=>/native|reservation/i.test(n))&&!!x&&x.n>1500&&/^[0-9a-f]{8}$/.test(x.h||''),JSON.stringify(x||null)+' '+LJ.t.filter(n=>/native|reservation/i.test(n)).join(','));
    const NJ=x?await q.evaluate(h=>fetch('data/leads/native-'+h+'.json').then(r=>r.ok?r.json():null).catch(()=>null),x.h):null;
    ok('the second file holds only that category, as many rows as the leads file says',!!NJ&&NJ.p.length===x.n&&NJ.t.length>0&&NJ.t.every(n=>NAMES.test(n))&&NJ.p.every(r=>r.length===4&&r[2]<NJ.t.length),NJ?NJ.p.length+' rows; '+NJ.t.join(', '):'no file');
    const inMV=NJ?NJ.p.filter(r=>Math.abs(r[0]-MV[0])<0.03&&Math.abs(r[1]-MV[1])<0.03).length:0;
    const teal=()=>q.evaluate(()=>{ let n=0; window.__atlasMap.eachLayer(l=>{ if(l.options&&l.getRadius&&l.options.fillColor==='#3cc8b4') n++; }); return n; });
    const yellow=()=>q.evaluate(()=>{ let n=0; window.__atlasMap.eachLayer(l=>{ if(l.options&&l.getRadius&&l.options.fillColor==='#ffd500') n++; }); return n; });
    const near=()=>q.evaluate(a=>window.__atlasNM.nmCollect(a,3).filter(t=>t.k==='l').length,MV);
    got.length=0; await q.evaluate(a=>window.__atlasMap.setView([a[0],a[1]+0.01],12,{animate:false}),MV); await q.waitForTimeout(900);
    ok('switched off (as it is to begin with): Mesa Verde shows none of its dots and the file is not fetched',inMV>20&&await teal()===0&&got.length===0,inMV+' in the file there, '+await teal()+' drawn, fetched: '+got.join(' '));
    ok('and the Near tab does not list them',await near()===0,await near()+' leads within 3 miles');
    await q.click('#lb-opt'); await q.click('#sheet-set'); await q.waitForTimeout(300);
    const box=await q.evaluate(()=>{ const n=document.querySelector('#set-nativeLeads'); return n?{checked:n.checked,text:n.closest('label').textContent}:null; });
    ok('the switch is under the gear, off, and says what it is',!!box&&box.checked===false&&/Native American/.test(box.text)&&/sacred|closed/.test(box.text),box?box.text.slice(0,90):'no switch');
    if(box) await q.evaluate(()=>document.querySelector('#set-nativeLeads').click()); await q.waitForTimeout(1500); await q.click('#sheet-x').catch(()=>{}); await q.waitForTimeout(300);
    ok('switched on: the second file is fetched once',got.length===1&&/^leads\/native-[0-9a-f]{8}\.json$/.test(got[0]),got.join(' '));
    const t1=await teal();
    ok('its dots are drawn in their own colour, and the ordinary leads are not recoloured',t1>20&&t1<=inMV*4,t1+' turquoise, '+await yellow()+' yellow');
    const pop=await q.evaluate(()=>{ const m=window.__atlasMap, b=m.getBounds(); let hit=null; m.eachLayer(l=>{ if(!hit&&l.options&&l.getRadius&&l.options.fillColor==='#3cc8b4'&&b.contains(l.getLatLng())) hit=l; }); if(!hit) return ''; hit.fire('click',{latlng:hit.getLatLng()}); const e=m._popup&&m._popup.getElement(); return e?e.textContent:''; });
    ok('a tap on one says what it is and to go only where visitors are invited',/Archaeological site|Native American site/.test(pop)&&/invites visitors/.test(pop),pop.slice(0,140));
    ok('the Near tab lists them now',await near()>0,await near()+' leads within 3 miles');
    await q.reload(); await q.waitForFunction(()=>window.__atlasMap); await q.waitForTimeout(2800);
    ok('the choice is remembered: after a reload the dots are back',await teal()>20,await teal()+' turquoise');
    await q.evaluate(()=>window.__atlasNM.setPref('nativeLeads',false)); await q.waitForTimeout(600);
    ok('switched off again: the dots go and Near forgets them',await teal()===0&&await near()===0,await teal()+' drawn, '+await near()+' near');
    await c3.close(); }
  // ---- vanished places and old mines come one state at a time: an index, then a state's own file when the map is zoomed in
  //      over it or the reader stands in it. Nobody looking at Albany downloads Missouri.
  { const c2=await b.newContext({viewport:{width:390,height:844},deviceScaleFactor:2,isMobile:true,hasTouch:true}); const q=await c2.newPage(); const got=[]; q.on('pageerror',e=>errs.push(e.message));
    await c2.route(u=>!/^http:\/\/localhost/.test(u.href),r=>r.fulfill({status:204,body:''}));
    q.on('request',r=>{ const m=/\/data\/(vanished|mines)(?:\/([a-z]+)-[0-9a-f]+\.json|\/(index)\.json|(\.json))/.exec(r.url()); if(m) got.push(m[1]+':'+(m[2]||m[3]||'WHOLE')); });
    await q.addInitScript(()=>{ try{ localStorage.setItem('lost-hidden-atlas-v1',JSON.stringify({v:1,home:{id:'alb',by:1},ui:{base:'streets',view:[42.6526,-73.7562,13],hist:false,xl:{vanished:true,mines:true}}})); }catch(e){} });
    await q.goto(url); await q.waitForFunction(()=>window.__atlasMap); await q.waitForTimeout(2600);
    const st=()=>q.evaluate(()=>{ const X=window.__atlasNM.XL, n=k=>Object.values(X[k].idx||{}).reduce((a,v)=>a+v.length,0), by=k=>{ const o={}; Object.values(X[k].idx||{}).forEach(v=>v.forEach(x=>{ const s=x[x.length-1]; o[s]=(o[s]||0)+1; })); return o; };
      return {v:n('vanished'),m:n('mines'),vs:by('vanished'),idx:X.vanished.data&&X.vanished.data.s?Object.keys(X.vanished.data.s).length:0,nyN:X.vanished.data&&X.vanished.data.s&&X.vanished.data.s.ny?X.vanished.data.s.ny.n:0,p:Array.isArray(X.vanished.data&&X.vanished.data.p)}; });
    let s2=await st();
    ok('over Albany: the index and New York\'s own file are fetched, for both layers',got.indexOf('vanished:index')>=0&&got.indexOf('vanished:ny')>=0&&got.indexOf('mines:index')>=0&&got.indexOf('mines:ny')>=0,got.join(' '));
    ok('and no far state\'s file, nor the old whole-layer file',!got.some(x=>/:(mo|ks|pa|me|WHOLE)$/.test(x)),got.join(' '));
    ok('the index lists every state with its count, and carries no points itself',s2.idx>=11&&!s2.p&&s2.nyN>1000,s2.idx+' states; New York '+s2.nyN);
    ok('New York\'s points are all there and nothing else',s2.vs.ny===s2.nyN&&Object.keys(s2.vs).every(k=>k==='ny'||k==='ma'||k==='vt'),JSON.stringify(s2.vs));
    const dots=()=>q.evaluate(()=>{ let n=0; window.__atlasMap.eachLayer(l=>{ if(l.options&&l.options.pane==='lines'&&l.getRadius&&l.options.fillColor==='#ff8a3d') n++; }); return n; });
    ok('its orange dots are on the map',await dots()>0,await dots()+' dots');
    await q.evaluate(()=>window.__atlasMap.setView([39.10,-94.58],12,{animate:false})); await q.waitForTimeout(2200); s2=await st();
    ok('the map moved to Kansas City: Missouri and Kansas come then',got.indexOf('vanished:mo')>=0&&got.indexOf('vanished:ks')>=0&&s2.vs.mo>1000&&s2.vs.ks>100,JSON.stringify(s2.vs));
    ok('and their dots are drawn',await dots()>0,await dots()+' dots');
    const before=got.length; await q.evaluate(()=>window.__atlasMap.setView([39.12,-94.50],12,{animate:false})); await q.waitForTimeout(900);
    ok('a state that has come is not fetched again',got.length===before,got.slice(before).join(' '));
    // Near: standing in Pennsylvania with the map elsewhere brings Pennsylvania's file
    const near=await q.evaluate(async()=>{ const NM=window.__atlasNM; const c=[40.44,-79.99]; NM.nmCollect(c,2); for(let i=0;i<40;i++){ await new Promise(r=>setTimeout(r,150)); if(NM.XL.vanished.got&&NM.XL.vanished.got.pa===true) break; } const S=(JSON.parse(localStorage.getItem('lost-hidden-atlas-v1')||'{}').ui||{}).nm; return {pa:NM.XL.vanished.got.pa===true,list:NM.nmCollect(c,2).filter(x=>x.k==='v').length,kinds:S&&S.k}; });
    ok('Near: standing in Pittsburgh with vanished places among the kinds wanted brings Pennsylvania\'s file',near.pa||!(near.kinds&&near.kinds.v),JSON.stringify(near).slice(0,160));
    const whole=await q.evaluate(()=>Promise.all(['vanished','mines'].map(k=>fetch('data/'+k+'.json').then(r=>r.json()).then(j=>({n:j.p.length,st:Object.keys(j.s).length,t:j.t.length})))));
    ok('the old whole-layer files are still there for older copies of the Android app, holding the eleven states they held',whole.every(w=>w.n>10000&&w.st===11&&w.t>0),JSON.stringify(whole));
    await c2.close(); }
  /* 7. Two fingers on the map (the owner, November 22, 2026). Leaflet moves every pin separately at every frame of a pinch,
        and round Albany that is hundreds of pins: the map crawled while two fingers were down. So for the length of a pinch
        the pins are swapped for one picture of themselves, stretched with the map like the heat map, and swapped back when
        the fingers lift: tried on his phone as a trial and kept ("completely fixed how it feels"). It is on unless switched
        off under the gear. The picture is drawn again whenever it has been stretched or shrunk a good deal, at the size the
        pins have then, so a long pinch stays sharp and a pinch far out still has pins to its edges. The frames here are the
        ones Leaflet's own pinch handler makes. This checks that the swap is right, not that it is fast: the test browser's
        frame times did not predict a phone (GUIDE.md section 9, "Pinch lag"). */
  { const run=async set=>{ const c3=await b.newContext({viewport:{width:390,height:844},deviceScaleFactor:2,isMobile:true,hasTouch:true});
      await c3.addInitScript(set=>{ try{ localStorage.setItem('lost-hidden-atlas-v1',JSON.stringify({v:1,set:set,ui:{base:'streets',view:[42.7,-73.8,10],hist:false,leads:false}})); }catch(e){} },set);
      await c3.route(u=>!/^http:\/\/localhost/.test(u.href),r=>r.fulfill({status:204,body:''}));
      const q=await c3.newPage(); q.on('pageerror',e=>errs.push('pinch: '+e.message)); await q.goto(url); await q.waitForFunction(()=>window.__atlasMap); await q.waitForTimeout(2500);
      const r=await q.evaluate(async()=>{ const m=window.__atlasMap, box=m.getContainer().getBoundingClientRect(), c=m.getCenter(), z0=m.getZoom(), frame=()=>new Promise(r=>requestAnimationFrame(r));
        const pins=()=>[...document.querySelectorAll('.leaflet-marker-pane .pinwrap')], shown=()=>pins().filter(e=>getComputedStyle(e).display!=='none').length, cvs=()=>[...m.getContainer().querySelectorAll('canvas.pinstand')];
        const fits=()=>{ const st=window.__atlasPinch&&window.__atlasPinch(), cv=cvs()[0]; if(!st||!cv) return null; const r=cv.getBoundingClientRect(), w=m.latLngToContainerPoint(st.nw), k=m.getZoomScale(m.getZoom(),st.z0);
          return {dx:Math.round(Math.abs(r.left-box.left-w.x)*10)/10,dy:Math.round(Math.abs(r.top-box.top-w.y)*10)/10,dw:Math.round(Math.abs(r.width-st.w*k)*10)/10,stretch:Math.round(k*100)/100,mag:Math.round((st.mag||1)*100)/100,
            covers:r.left<=box.left+1&&r.top<=box.top+1&&r.right>=box.right-1&&r.bottom>=box.bottom-1}; };
        const inked=()=>{ const st=window.__atlasPinch(), cv=cvs()[0], g=cv.getContext('2d'), k=cv.width/st.w, o=m.latLngToContainerPoint(st.nw), s=m.getZoomScale(m.getZoom(),st.z0); let n=0, hit=0; m.eachLayer(l=>{ if(!(l instanceof L.Marker)||!l._icon||!l._icon.classList.contains('pinwrap')||!m.getBounds().contains(l.getLatLng())) return; n++; const q=m.latLngToContainerPoint(l.getLatLng()); if(g.getImageData(Math.round((q.x-o.x)/s*k),Math.round((q.y-o.y)/s*k),1,1).data[3]>200) hit++; }); return {n,hit}; };
        const before={pins:pins().length,shown:shown(),cv:cvs().length};
        m._stop(); m._moveStart(true,false); m._move(c,z0+0.02,{pinch:true,round:false}); await frame();
        const one={shown:shown(),cv:cvs().length,fit:fits(),ink:cvs().length?inked():null};
        m._move(c,z0+0.3,{pinch:true,round:false}); await frame(); const inn={shown:shown(),cv:cvs().length,fit:fits()};
        for(const d of [0.6,0.9,1.2,1.5]){ m._move(c,z0+d,{pinch:true,round:false}); await frame(); } const deep={cv:cvs().length,fit:fits(),ink:cvs().length?inked():null};
        for(const d of [1.0,0.5,0,-0.5,-1.0,-1.4]){ m._move(L.latLng(c.lat+0.02,c.lng-0.03),z0+d,{pinch:true,round:false}); await frame(); } const out={shown:shown(),cv:cvs().length,fit:fits(),ink:cvs().length?inked():null};
        m._move(c,z0+0.2,{pinch:true,round:false}); await frame();      /* back to the pins' zoom before the fingers lift: let go at zoom 9 and the heat map takes over */
        m._animateZoom(c,Math.round(m.getZoom()),true,true); await new Promise(r=>setTimeout(r,700));
        let right=0, tot=0; m.eachLayer(l=>{ if(l instanceof L.Marker&&l._icon&&l._icon.classList.contains('pinwrap')){ tot++; const w=m.latLngToLayerPoint(l.getLatLng()).round(), g=L.DomUtil.getPosition(l._icon); if(Math.abs(w.x-g.x)<=1&&Math.abs(w.y-g.y)<=1) right++; } });
        return {before,one,inn,deep,out,end:{shown:shown(),pins:pins().length,cv:cvs().length,right,tot,st:window.__atlasPinch?window.__atlasPinch():'none'}}; });
      await q.click('#lb-opt'); await q.click('#sheet-set'); await q.waitForTimeout(250); r.sw=await q.evaluate(()=>{ const x=document.querySelector('#set-pinchStand'); return x?{on:x.checked,label:x.closest('label').textContent}:null; });
      await c3.close(); return r; };
    const off=await run({pinchStand:false}), on=await run({}), near=f=>!!f&&f.dx<=1.5&&f.dy<=1.5&&f.dw<=1.5;
    ok('pinch: Settings has the switch, on unless it is switched off, and it is no longer called a trial',!!on.sw&&on.sw.on===true&&!!off.sw&&off.sw.on===false&&!/trial/i.test(on.sw.label),JSON.stringify([on.sw,off.sw&&off.sw.on]).slice(0,200));
    ok('pinch switched off: a pinch leaves every pin on the page and puts no picture there',off.before.shown>400&&off.one.shown===off.before.shown&&off.one.cv===0&&off.out.cv===0,JSON.stringify([off.before,off.one]));
    ok('pinch: before it the pins are on the page and there is no picture',on.before.shown>400&&on.before.cv===0,JSON.stringify(on.before));
    ok('pinch: at the first frame the pins are hidden and one picture stands in for them',on.one.shown===0&&on.one.cv===1,JSON.stringify(on.one));
    ok('pinch: the picture has a pin drawn where each pin in view was',!!on.one.ink&&on.one.ink.n>100&&on.one.ink.hit>=on.one.ink.n*0.98,JSON.stringify(on.one.ink));
    ok('pinch: the picture sits where the map is, at the first frame and pinched in a little',near(on.one.fit)&&near(on.inn.fit)&&on.inn.cv===1,JSON.stringify([on.one.fit,on.inn.fit]));
    ok('pinch: pinched in a long way, the picture has been drawn again, sharp: it is stretched little, and its pins are drawn as large as they had grown',on.deep.cv===1&&near(on.deep.fit)&&on.deep.fit.stretch<=1.45&&on.deep.fit.mag>1.5&&on.deep.fit.stretch*on.deep.fit.mag>2.6&&on.deep.fit.stretch*on.deep.fit.mag<3,JSON.stringify(on.deep.fit));
    ok('pinch: and there is still a pin drawn where each pin in view is',!!on.deep.ink&&on.deep.ink.n>20&&on.deep.ink.hit>=on.deep.ink.n*0.98,JSON.stringify(on.deep.ink));
    ok('pinch: pinched out a long way and aside, the picture still covers the whole map, with a pin drawn for each pin in view',on.out.cv===1&&on.out.shown===0&&near(on.out.fit)&&on.out.fit.covers===true&&!!on.out.ink&&on.out.ink.hit>=on.out.ink.n*0.9,JSON.stringify([on.out.fit,on.out.ink]));
    ok('pinch: when the fingers lift the picture is gone and every pin is back, where it belongs',on.end.cv===0&&on.end.shown===on.end.pins&&on.end.pins>400&&on.end.right===on.end.tot&&on.end.st===null,JSON.stringify(on.end)); }
  ok('no script errors',errs.length===0,errs.join(' | ').slice(0,200));
  await b.close(); console.log(fails.length?('\n'+fails.length+' FAILED'):'\noverlay test passed'); process.exit(fails.length?1:0);
})();
