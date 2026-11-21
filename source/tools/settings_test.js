// Phone-size check of the two sheets behind the "More" button: Map options (kept short) and Settings (the gear).
//   node tools/settings_test.js http://localhost:8766/index.html      (serve the built site first, as for smoke.js)
// Run it after changing buildSheet(), buildSettings() or anything they show. Screenshots go to /tmp/set_*.png.
const { chromium, devices } = require('playwright');
(async()=>{
  const fails=[]; const ok=(name,cond,extra)=>{ console.log((cond?'ok   ':'FAIL ')+name+(extra!==undefined?'  ['+extra+']':'')); if(!cond) fails.push(name); };
  const b=await chromium.launch({proxy:{server:process.env.HTTPS_PROXY||'http://x',bypass:'localhost,127.0.0.1'}});
  const c=await b.newContext(Object.assign({},devices['Pixel 7'])); const p=await c.newPage(); const errs=[]; p.on('pageerror',e=>errs.push(e.message));
  // a trip of two places, put in before the page first loads
  await c.addInitScript(()=>{ if(location.protocol!=='about:'&&!localStorage.getItem('lost-hidden-atlas-v1')) localStorage.setItem('lost-hidden-atlas-v1',JSON.stringify({home:{id:'alb',by:1},trip:['joliet-iron-works','lidar-high-knob-walled-yard']})); });
  await p.goto(process.argv[2]||'http://localhost:8766/index.html'); await p.waitForFunction(()=>window.__atlasMap); await p.waitForTimeout(600);
  const U=()=>p.evaluate(()=>JSON.parse(localStorage.getItem('lost-hidden-atlas-v1')||'{}'));
  const shown=sel=>p.evaluate(sel=>[...document.querySelectorAll(sel)].filter(n=>n.offsetParent!==null&&n.getClientRects().length).length,sel);
  // ---- Map options: every switch in sight, explanations only when asked for
  await p.click('#lb-opt'); await p.waitForTimeout(300);
  const h0=await p.evaluate(()=>document.querySelector('#sheet-b').scrollHeight), vh=await p.evaluate(()=>innerHeight);
  ok('Map options: short by default',h0<vh*1.6,h0+' px tall on a '+vh+' px screen');
  ok('Map options: explanations hidden by default',(await shown('#sheet-b .lopt small'))===0&&(await shown('#sheet-b .snote'))===0);
  ok('Map options: the switches are all there',(await shown('#sheet-b #hist-on'))===1&&(await shown('#sheet-b #leads-on'))===1&&(await shown('#sheet-b #xl-mines'))===1&&(await shown('#sheet-b #pock-on'))===1&&(await shown('#sheet-b #land-on'))===1);
  await p.screenshot({path:'/tmp/set_1_options.png'});
  ok('Map options: no small legend of pin shapes (the Legend button has the whole one)',(await p.locator('#sheet-b .pinkey').count())===0);
  const tips=await p.evaluate(()=>[...document.querySelectorAll('#sheet-b .lopt')].map(l=>({id:l.getAttribute('for'),small:(l.querySelector('small')||{}).textContent||'',title:l.getAttribute('title')||''})));
  ok('Map options: every switch that has an explanation gives it as a tooltip too',tips.filter(t=>t.small).length>6&&tips.filter(t=>t.small).every(t=>t.title===t.small),tips.filter(t=>t.small&&t.title!==t.small).map(t=>t.id).join(' ')||tips.filter(t=>t.small).length+' switches');
  ok('Map options: the three lead switches say what they turn on',['leads-on','xl-vanished','xl-mines'].every(id=>((tips.find(t=>t.id===id)||{}).title||'').length>60));
  const tb=await p.evaluate(()=>{ const a=document.querySelector('#sheet-tips'), o=document.querySelector('#sheet-b .btn.sm:not(#sheet-tips)')||document.querySelector('.btn.sm:not(#sheet-tips)'); return {a:getComputedStyle(a).backgroundColor,o:o?getComputedStyle(o).backgroundColor:'',top:a.getBoundingClientRect().top<innerHeight}; });
  ok('Map options: "What do these do?" stands out from the plain buttons',tb.top&&tb.a!==tb.o&&tb.a!=='rgba(0, 0, 0, 0)',JSON.stringify(tb));
  { const pb=await p.evaluate(()=>{ const n=document.querySelector('#lb-pock'); return n?{t:n.getAttribute('title')||'',on:n.getAttribute('aria-pressed')}:null; });
    ok('the bar has a button for the old town centres, off to begin with',!!pb&&pb.on==='false'&&/town centres/i.test(pb.t),JSON.stringify(pb));
    await p.click('#sheet-x'); if(pb) await p.evaluate(()=>document.querySelector('#lb-pock').click()); await p.waitForTimeout(500);
    const on=await p.evaluate(()=>({u:JSON.parse(localStorage.getItem('lost-hidden-atlas-v1')||'{}'),a:(document.querySelector('#lb-pock')||{getAttribute(){}}).getAttribute('aria-pressed')}));
    if(pb) await p.evaluate(()=>document.querySelector('#lb-pock').click()); await p.waitForTimeout(1200);
    const off=await p.evaluate(()=>({p:JSON.parse(localStorage.getItem('lost-hidden-atlas-v1')||'{}').ui.pockets,a:(document.querySelector('#lb-pock')||{getAttribute(){}}).getAttribute('aria-pressed')}));
    ok('a tap switches the town centres on and the button shows it; another tap switches them off',on.a==='true'&&off.a==='false'&&!off.p,JSON.stringify([on.a,off]));
    await p.click('#lb-opt'); await p.waitForTimeout(300); }
  ok('the Leads button on the bar says what it shows when the pointer rests on it',/nobody has checked/i.test(await p.getAttribute('#lb-leads','title')),await p.getAttribute('#lb-leads','title'));
  await p.click('#sheet-tips'); await p.waitForTimeout(250);
  ok('Map options: "What do these do?" shows the explanations',(await shown('#sheet-b .lopt small'))>5&&(await shown('#sheet-b .snote'))>1);
  await p.waitForTimeout(900); ok('Map options: the choice is remembered',(await U()).ui.tips===true);
  await p.click('#sheet-tips'); await p.waitForTimeout(250);
  ok('Map options: and hides them again',(await shown('#sheet-b .lopt small'))===0);
  const keys=()=>shown('#sheet-b .lkeys');
  const k0=await keys(); await p.evaluate(()=>{ const n=document.querySelector('#land-on'); if(!n.checked) n.click(); }); await p.waitForTimeout(300);
  ok('Map options: a legend shows only for a layer that is on',(await keys())===k0+1,k0+' -> '+(await keys()));
  await p.evaluate(()=>document.querySelector('#land-on').click()); await p.waitForTimeout(200);
  // ---- Settings
  await p.click('#sheet-set'); await p.waitForTimeout(300);
  const txt=await p.innerText('#sheet-b');
  ok('Settings: no stray "null" on the page',!/\bnull\b/.test(txt),(txt.match(/.{0,25}null.{0,10}/)||[''])[0]);
  const heads=await p.evaluate(()=>[...document.querySelectorAll('#sheet-b h3')].map(n=>n.textContent));
  ok('Settings: Near me and Episode kit have their own sections',heads.includes('Near me')&&heads.includes('Episode kit'),heads.join(' | '));
  await p.selectOption('#set-nm-al','200'); await p.selectOption('#set-nm-r','5'); await p.waitForTimeout(1200);   // saving waits a moment for more changes
  let u=await U(); ok('Settings: the Near me choices are saved',u.ui.nm&&u.ui.nm.al===200&&u.ui.nm.r===5,JSON.stringify(u.ui.nm));
  await p.fill('#set-kitSign','Subscribe: example.org/channel'); await p.selectOption('#set-kitBase','air'); await p.click('#sheet-t'); await p.waitForTimeout(250);
  u=await U(); ok('Settings: the kit choices are saved',u.set&&u.set.kitSign==='Subscribe: example.org/channel'&&u.set.kitBase==='air',JSON.stringify(u.set));
  await p.screenshot({path:'/tmp/set_2_settings.png'});
  const swatches=await p.evaluate(()=>[...document.querySelectorAll('.swatches [role=radio]')].map(b=>b.getAttribute('aria-label')));
  await p.click('#sheet-x'); await p.click('#tab-near'); await p.waitForTimeout(500);
  ok('Near tab shows what Settings chose',(await p.inputValue('#near-al'))==='200'&&(await p.inputValue('#near-r'))==='5');
  await p.selectOption('#near-al','50'); await p.waitForTimeout(200); await p.click('#near-set'); await p.waitForTimeout(350);
  ok('Near tab: its Settings link opens the gear at Near me',(await p.innerText('#sheet-t')).trim().toLowerCase()==='settings'&&(await p.inputValue('#set-nm-al'))==='50');
  await p.click('#sheet-x');
  // ---- the search box: names first, accents and capitals ignored, a long list shown in two steps
  await p.click('#tab-list'); await p.waitForTimeout(200);
  const rowsN=()=>p.evaluate(()=>document.querySelectorAll('#list .item').length), total=await p.evaluate(()=>JSON.parse(document.getElementById('d-sites').textContent).sites.length);
  ok('a long list shows its first part and offers the rest',(await rowsN())<=150&&(await shown('#list-more'))===1,(await rowsN())+' of '+total+' rows');
  await p.click('#list-more'); await p.waitForTimeout(250); ok('"Show the rest" lists every place',(await rowsN())>=total,(await rowsN())+' rows');
  const type=async w=>{ await p.fill('#q',w); await p.waitForTimeout(450); return p.evaluate(()=>[...document.querySelectorAll('#list .item b')].map(n=>n.textContent)); };
  let names=await type('joliet'); ok('a place is found by its name',names.length>0&&/joliet/i.test(names[0]),names.slice(0,2).join(' | '));
  names=await type('JOLIÉT iron'); ok('capitals and accents do not matter',names.length>0&&/joliet iron/i.test(names[0]),names.slice(0,2).join(' | '));
  names=await type('mill'); if(await shown('#list-more')){ await p.click('#list-more'); await p.waitForTimeout(250); names=await p.evaluate(()=>[...document.querySelectorAll('#list .item b')].map(n=>n.textContent)); }
  const firstText=names.findIndex(n=>!/mill/i.test(n)), lastName=names.map(n=>/mill/i.test(n)).lastIndexOf(true);
  ok('places with the word in their name come before those that only mention it',names.length>20&&firstText>0&&lastName<firstText,names.length+' found; first without it in the name is row '+(firstText+1)+', last with it is row '+(lastName+1));
  names=await type('walled yard schoharie'); ok('words can match across the name, the town, the region and the text',names.length>=1&&names.length<12,names.slice(0,3).join(' | '));
  await type('');
  // ---- pins that crowd together are grouped when zoomed out (Settings > Map)
  const pins=()=>p.evaluate(()=>[document.querySelectorAll('.leaflet-marker-pane .pin').length,document.querySelectorAll('.leaflet-marker-pane .clus').length]);
  await p.evaluate(()=>{ window.__atlasMap.setView([42.75,-73.9],7,{animate:false}); }); await p.waitForTimeout(700);
  let pc=await pins(); ok('zoomed out: crowded pins are grouped',pc[1]>=3&&pc[0]<300,pc[0]+' pins, '+pc[1]+' groups');
  const sum=await p.evaluate(()=>[...document.querySelectorAll('.leaflet-marker-pane .clus')].reduce((a,n)=>a+(+n.textContent||0),0));
  ok('every place is either a pin or counted in a group',sum+pc[0]>=540,sum+' in groups + '+pc[0]+' pins');
  const z0=await p.evaluate(()=>window.__atlasMap.getZoom());
  await p.evaluate(()=>{ const n=[...document.querySelectorAll('.leaflet-marker-pane .clus')].sort((a,b)=>(+b.textContent)-(+a.textContent))[0]; n.click(); }); await p.waitForTimeout(900);
  ok('tapping a group zooms in to it',(await p.evaluate(()=>window.__atlasMap.getZoom()))>z0);
  await p.evaluate(()=>{ window.__atlasMap.setView([42.75,-73.9],12,{animate:false}); }); await p.waitForTimeout(600);
  pc=await pins(); const inView=await p.evaluate(()=>{ const b=window.__atlasMap.getBounds(), D=JSON.parse(document.getElementById('d-sites').textContent); return (D.sites||D).filter(s=>b.contains([s.lat,s.lon])).length; });
  ok('zoomed in: no groups, and every place in view is a pin of its own (pins far out of view are not on the map)',pc[1]===0&&inView>0&&pc[0]>=inView&&pc[0]>20,pc[0]+' pins for '+inView+' places in view, '+pc[1]+' groups');
  await p.evaluate(()=>{ window.__atlasMap.setView([42.75,-73.9],7,{animate:false}); }); await p.waitForTimeout(500);
  await p.click('#lb-opt'); await p.click('#sheet-set'); await p.waitForTimeout(250); await p.evaluate(()=>document.querySelector('#set-cluster').click()); await p.waitForTimeout(500); await p.click('#sheet-x');
  pc=await pins(); ok('with grouping switched off in Settings every pin shows',pc[1]===0&&pc[0]>400,pc[0]+' pins, '+pc[1]+' groups');
  // ---- stone walls found on LiDAR: shaded squares zoomed out, the walls themselves zoomed in
  const wl=()=>p.evaluate(()=>{ let boxes=0, cells=0, parts=0; window.__atlasMap.eachLayer(l=>{ if(l.options&&l.options.wallBox) boxes++; if(l.options&&l.options.wallCell){ cells++; parts+=l.getLatLngs().length; } }); return [boxes,cells,parts]; });
  const idx=await p.evaluate(()=>fetch('data/walls.json').then(r=>r.ok?r.json():null).catch(()=>null));
  if(!idx||!idx.n){ ok('stone walls: the build has a walls layer to test',false,'data/walls.json is missing or empty'); }
  else {
    const at=await p.evaluate(()=>fetch('data/walls.json').then(r=>r.json()).then(j=>{ const b=j.d.slice().sort((x,y)=>y[2]-x[2])[0]; return [b[0]*0.005+0.0025,b[1]*0.005+0.0025]; }));
    await p.evaluate(at=>{ window.__atlasMap.setView(at,12,{animate:false}); },at); await p.waitForTimeout(400);
    let w=await wl(); ok('stone walls: nothing is drawn until the layer is switched on',w[0]===0&&w[1]===0,w.join(','));
    await p.click('#lb-opt'); await p.waitForTimeout(250); await p.evaluate(()=>document.querySelector('#walls-on').click()); await p.waitForTimeout(900); await p.click('#sheet-x');
    w=await wl(); ok('stone walls, zoomed out: squares are shaded where the walls are',w[0]>5&&w[1]===0,w[0]+' squares');
    await p.evaluate(at=>{ window.__atlasMap.setView(at,15,{animate:false}); },at); await p.waitForTimeout(1500);
    w=await wl(); ok('stone walls, zoomed in: the walls themselves are drawn',w[0]===0&&w[1]>=1&&w[2]>20,w[1]+' cells, '+w[2]+' pieces');
    await p.screenshot({path:'/tmp/set_3_walls.png'});
    await p.evaluate(()=>{ window.__atlasMap.setView([40.0,-80.0],15,{animate:false}); }); await p.waitForTimeout(500);
    w=await wl(); ok('stone walls: cells out of view are taken off the map',w[1]===0,w.join(','));
    ok('stone walls: the switch is remembered',(await U()).ui.walls===true);
  }
  // ---- the track colour: no pink anywhere, and the Near tab's "point me there" ring and line follow it
  const tk=await p.evaluate(()=>{ const N=window.__atlasNM, s=N.sites().find(x=>x.st==='standing'), m=window.__atlasMap;
        N.nmGoal({k:'p',id:'p:'+s.id,o:s,la:s.lat,lo:s.lon},false); const col=()=>{ const e=document.querySelector('.leaflet-marker-pane .nmring'); if(!e) return []; const g=getComputedStyle(e); return [g.borderTopColor,/255, 255, 255/.test(g.boxShadow)?'white casing':'no casing']; };      /* the ring is a marker (near_test.js says why): its border is the colour, its shadow the white casing */
    const before=col(); N.setPref('trk','#7c3aed'); const after=col(); N.nmGoal(null); N.setPref('trk','#2563eb');
    return {before,after,css:getComputedStyle(document.documentElement).getPropertyValue('--trk').trim()}; });
  ok('track colours offered: no pink',swatches.length>=4&&!swatches.some(x=>/pink/i.test(x)),swatches.join(','));
  ok('the "point me there" ring takes the track colour, over a white casing, and follows a change',tk.before.join()==='rgb(37, 99, 235),white casing'&&tk.after.join()==='rgb(124, 58, 237),white casing',JSON.stringify(tk));
  const src=await p.evaluate(()=>[...document.styleSheets].map(ss=>{ try{ return [...ss.cssRules].map(r=>r.cssText).join(''); }catch(e){ return ''; } }).join(''));
  ok('no pink left in the styles',!/e11d74|225,\s*29,\s*116/i.test(src));
  // ---- a new reader: no old rail lines or canals drawn until asked for (they are a tool for hunting leads, not the first thing to see)
  { const c5=await b.newContext(Object.assign({},devices['Pixel 7'])); const p5=await c5.newPage(); p5.on('pageerror',e=>errs.push(e.message)); const got=[];
    p5.on('request',r=>{ if(/\/data\/lines/.test(r.url())) got.push(r.url().replace(/^.*\/data\//,'')); });
    await p5.goto(process.argv[2]||'http://localhost:8766/index.html'); await p5.waitForFunction(()=>window.__atlasMap); await p5.evaluate(()=>{ window.__atlasMap.setView([42.6526,-73.7562],13,{animate:false}); }); await p5.waitForTimeout(2500);
    const d=await p5.evaluate(()=>{ let n=0; window.__atlasMap.eachLayer(l=>{ if(l.options&&l.options.casing) n++; }); const u=JSON.parse(localStorage.getItem('lost-hidden-atlas-v1')||'{}'); return {n:n,ui:(u.ui||{})}; });
    await p5.click('#lb-opt'); await p5.waitForTimeout(300);
    const ck5=await p5.evaluate(()=>['ln-oldrail','ln-canal','ln-rail','leads-on','xl-vanished','xl-mines','pock-on'].map(i=>{ const n=document.querySelector('#'+i); return n?n.checked:null; }));
    ok('a new reader: old rails, canals, leads, vanished places, mines and pockets all start switched off',ck5.every(v=>v===false),JSON.stringify(ck5));
    ok('a new reader: no line is drawn and no line file is fetched',d.n===0&&got.length===0,d.n+' line layers; fetched '+got.join(' '));
    await c5.close(); }
  const c2=await b.newContext(Object.assign({},devices['Pixel 7'])); const p2=await c2.newPage();
  await p2.addInitScript(()=>{ localStorage.setItem('lost-hidden-atlas-v1',JSON.stringify({home:{id:'alb',by:1},set:{trk:'#e11d74'}})); });
  await p2.goto(process.argv[2]||'http://localhost:8766/index.html'); await p2.waitForFunction(()=>window.__atlasMap); await p2.waitForTimeout(300);
  const mig=await p2.evaluate(()=>getComputedStyle(document.documentElement).getPropertyValue('--trk').trim()); await c2.close();
  ok('a track colour saved as the old pink comes back as the blue default',mig==='#2563eb',mig);
  // ---- a double tap: three steps in on open map (as many as Settings says), street level on a pin, and at least three steps toward a numbered disc
  { const c4=await b.newContext(Object.assign({},devices['Pixel 7'])); const p4=await c4.newPage(); p4.on('pageerror',e=>errs.push(e.message));
    await p4.addInitScript(()=>{ localStorage.setItem('lost-hidden-atlas-v1',JSON.stringify({home:{id:'alb',by:1}})); });
    await p4.goto(process.argv[2]||'http://localhost:8766/index.html'); await p4.waitForFunction(()=>window.__atlasNM); await p4.waitForTimeout(300);
    const dbl=(opt)=>p4.evaluate(async opt=>{ const m=window.__atlasMap; m.setView([42.9,-75.2],opt.z,{animate:false}); await new Promise(r=>setTimeout(r,150));
      const pt=m.latLngToContainerPoint(m.getCenter()); m.fire('dblclick',{latlng:m.getCenter(),containerPoint:pt,layerPoint:m.containerPointToLayerPoint(pt),originalEvent:{shiftKey:!!opt.shift}}); await new Promise(r=>setTimeout(r,900)); return m.getZoom(); },opt);
    ok('a double tap on open map goes in three steps',(await dbl({z:8}))===11);
    ok('Shift and a double click goes out three',(await dbl({z:12,shift:true}))===9);
    ok('and it stops at the closest zoom the map has',(await dbl({z:19}))===20);
    ok('Leaflet\'s own one-step double tap is switched off',await p4.evaluate(()=>!window.__atlasMap.doubleClickZoom.enabled()));
    await p4.evaluate(()=>window.__atlasNM.setPref('dbl',1)); ok('set to one step in Settings, it goes one step',(await dbl({z:8}))===9);
    await p4.evaluate(()=>window.__atlasNM.setPref('dbl',3));
    const pin=await p4.evaluate(async()=>{ const N=window.__atlasNM, m=window.__atlasMap, s=N.sites().find(x=>x.st==='standing'&&!x.mine); m.setView([s.lat,s.lon],13,{animate:false}); N.syncMarkers(); await new Promise(r=>setTimeout(r,200));
      let mk=null; m.eachLayer(l=>{ if(l.getLatLng&&l.options.riseOnHover&&l.getLatLng().distanceTo([s.lat,s.lon])<2) mk=l; }); if(!mk) return null; mk.fire('click',{latlng:mk.getLatLng()}); await new Promise(r=>setTimeout(r,120)); mk.fire('dblclick',{latlng:mk.getLatLng()}); await new Promise(r=>setTimeout(r,1200));
      return {z:m.getZoom(),off:Math.round(m.getCenter().distanceTo([s.lat,s.lon])),open:(document.querySelector('#v-detail h2')||{}).textContent===s.name}; });
    ok('a double tap on a pin opens its page and goes to street level, on the pin',!!pin&&pin.z===17&&pin.off<30&&pin.open,JSON.stringify(pin));
    const grp=await p4.evaluate(async()=>{ const N=window.__atlasNM, m=window.__atlasMap; m.setView([42.652,-73.755],9,{animate:false}); N.syncMarkers(); await new Promise(r=>setTimeout(r,300));      /* Albany from far enough out to be one tight disc */
      const discs=[]; m.eachLayer(l=>{ if(l.options&&l.options.icon&&/^clus\b/.test(l.options.icon.options.className||'')) discs.push(l); }); if(!discs.length) return null;
      const d=discs.sort((x,y)=>x.getLatLng().distanceTo([42.652,-73.755])-y.getLatLng().distanceTo([42.652,-73.755]))[0], n=+d.options.icon.options.html; d.fire('click',{latlng:d.getLatLng()}); await new Promise(r=>setTimeout(r,120)); d.fire('dblclick',{latlng:d.getLatLng()}); await new Promise(r=>setTimeout(r,1100)); return {n,z:m.getZoom()}; });      /* as a real double tap arrives: a tap, then the double tap */
    ok('a double tap on a numbered disc goes three steps in from where the map stood, toward the disc (a single tap goes two)',!!grp&&grp.z===12,JSON.stringify(grp));
    await p4.click('#lb-opt'); await p4.waitForTimeout(250); await p4.evaluate(()=>{ const g=[...document.querySelectorAll('#sheet button')].find(x=>/settings/i.test(x.getAttribute('aria-label')||x.textContent)); if(g) g.click(); }); await p4.waitForTimeout(300);
    ok('the choice is under the gear',await p4.evaluate(()=>{ const n=document.querySelector('#set-dbl'); return !!n&&n.value==='3'&&n.options.length===4; }));
    await c4.close(); }
  // ---- Compare: the button steps off -> the way used last -> the other way -> off, says which is showing, and all of it is kept
  { const c=await b.newContext({viewport:{width:390,height:844},deviceScaleFactor:2,isMobile:true,hasTouch:true}); const p=await c.newPage(); const errs=[]; p.on('pageerror',e=>errs.push(e.message));
    await c.route(u=>!/^http:\/\/localhost/.test(u.href),r=>r.fulfill({status:204,body:''}));
    await p.addInitScript(()=>{ try{ if(!localStorage.getItem('lost-hidden-atlas-v1')) localStorage.setItem('lost-hidden-atlas-v1',JSON.stringify({v:1,home:{id:'alb',by:1}})); }catch(e){} });
    await p.goto(process.argv[2]||'http://localhost:8766/index.html'); await p.waitForFunction(()=>window.__atlasMap); await p.waitForTimeout(600);
    const st=()=>p.evaluate(()=>{ const m=window.__atlasMap, pane=m.getPane('cmp'), sw=document.querySelector('#swipe'), fd=document.querySelector('#fade'), bt=document.querySelector('#lb-cmp');
      const u=JSON.parse(localStorage.getItem('lost-hidden-atlas-v1')||'{}'); let lay=0; m.eachLayer(l=>{ if(l.options&&l.options.pane==='cmp') lay++; });
      return {label:bt.querySelector('.lt').textContent,pressed:bt.getAttribute('aria-pressed'),swipe:!sw.hidden,fade:!fd.hidden,op:pane.style.opacity,clip:!!pane.style.clip,lay:lay,kept:(u.ui||{}).cmp||null,fl:fd.textContent,slider:document.querySelector('#fade-op').value}; });
    const tap=async wait=>{ await p.evaluate(()=>document.querySelector('#lb-cmp').click()); await p.waitForTimeout(wait||1700); };
    let s=await st(); ok('compare: off to begin with, and the button says Compare',s.label==='Compare'&&s.pressed==='false'&&!s.swipe&&!s.fade&&s.lay===0,JSON.stringify(s).slice(0,120));
    await tap(); s=await st(); ok('first tap: Swipe, with the divider, and the button says so',s.label==='Swipe'&&s.pressed==='true'&&s.swipe&&!s.fade&&s.clip&&s.lay===1,s.label);
    await tap(); s=await st(); ok('second tap: Overlay, the second layer see-through over the map, with a slider on the map',s.label==='Overlay'&&s.pressed==='true'&&!s.swipe&&s.fade&&!s.clip&&Math.abs(+s.op-0.6)<0.01&&s.lay===1&&s.fl.trim().length>3,s.label+' '+s.op+' "'+s.fl+'"');
    ok('the slider sits on the map and inside the screen',await p.evaluate(()=>{ const r=document.querySelector('#fade').getBoundingClientRect(), m=document.querySelector('#map').getBoundingClientRect(); return r.left>=0&&r.right<=innerWidth&&r.top>=m.top&&r.bottom<=m.bottom&&r.height>20; }));
    await p.evaluate(()=>{ const i=document.querySelector('#fade-op'); i.value='0.35'; i.dispatchEvent(new Event('input',{bubbles:true})); }); await p.waitForTimeout(500); s=await st();
    ok('sliding it fades the layer on top',Math.abs(+s.op-0.35)<0.01,s.op);
    ok('what was chosen is kept: on, Overlay, the layer and the strength',!!s.kept&&s.kept.on===true&&s.kept.mode==='fade'&&Math.abs(s.kept.op-0.35)<0.01&&!!s.kept.key,JSON.stringify(s.kept));
    await p.reload(); await p.waitForFunction(()=>window.__atlasMap); await p.waitForTimeout(900); s=await st();
    ok('opened again, it is still Overlay at that strength',s.label==='Overlay'&&s.fade&&!s.swipe&&Math.abs(+s.op-0.35)<0.01&&s.slider==='0.35'&&s.lay===1,s.label+' '+s.op);
    await tap(250); s=await st(); ok('a tap from Overlay goes to Swipe',s.label==='Swipe'&&s.swipe&&!s.fade,s.label);
    await tap(300); s=await st(); ok('and the next, made at once, switches compare off',s.label==='Compare'&&!s.swipe&&!s.fade&&s.lay===0&&s.pressed==='false',s.label);
    ok('passing through Swipe on the way to off did not make it the way to remember',!!s.kept&&s.kept.on===false&&s.kept.mode==='fade',JSON.stringify(s.kept));
    await tap(); s=await st(); ok('switched on again it comes back as Overlay',s.label==='Overlay'&&s.fade,s.label);
    await tap(); await tap(); s=await st(); ok('staying on Swipe a while and then switching off makes Swipe the way to remember',s.label==='Compare'&&s.kept.mode==='swipe'&&s.kept.on===false,JSON.stringify(s.kept));
    await p.evaluate(()=>document.querySelector('#lb-opt').click()); await p.waitForTimeout(400);
    ok('Map options offers the same two ways by the same names',await p.evaluate(()=>{ const on=document.querySelector('#cmp-on'); if(on&&!on.checked) on.click(); const m=document.querySelector('#cmp-mode'); return !!m&&[...m.options].map(o=>o.textContent).join()==='Swipe,Overlay'; }));
    ok('compare: no script errors',errs.length===0,errs.join(' | ').slice(0,200)); await c.close(); }
  // ---- Black as the track colour in a dark scheme: on the panels the text colour stands in, or the Near arrow and the recording dot could not be seen
  const c3=await b.newContext(Object.assign({},devices['Pixel 7'])); const p3=await c3.newPage();
  await p3.addInitScript(()=>{ localStorage.setItem('lost-hidden-atlas-v1',JSON.stringify({home:{id:'alb',by:1},set:{trk:'#111827',theme:'dark',themeD:'tomorrow'}})); });
  await p3.goto(process.argv[2]||'http://localhost:8766/index.html'); await p3.waitForFunction(()=>window.__atlasMap); await p3.waitForTimeout(300);
  const dk=await p3.evaluate(()=>{ const cs=getComputedStyle(document.documentElement), d=document.createElement('span'); d.className='nmarrow big'; document.body.append(d); const arrow=getComputedStyle(d).color; d.remove();
    const rgb=h=>{ h=h.trim().replace('#',''); if(h.length===3) h=h.replace(/./g,'$&$&'); return 'rgb('+[0,2,4].map(i=>parseInt(h.substr(i,2),16)).join(', ')+')'; };
    const ink=rgb(cs.getPropertyValue('--ink'));      /* read now: the style object is live and the scheme is about to change */
    window.__atlasNM.setPref('theme','light'); const d2=document.createElement('span'); d2.className='nmarrow big'; document.body.append(d2); const light=getComputedStyle(d2).color; d2.remove();
    return {arrow,ink,trk:cs.getPropertyValue('--trk').trim(),light}; }); await c3.close();
  ok('Black track colour in a dark scheme: the Near arrow takes the text colour, the track itself stays black',dk.arrow===dk.ink&&dk.trk==='#111827',JSON.stringify(dk));
  ok('and in a light scheme the arrow is black again',dk.light==='rgb(17, 24, 39)',dk.light);
  ok('no script errors',errs.length===0,errs.slice(0,2).join(' | '));
  await b.close(); console.log(fails.length?fails.length+' FAILED':'settings test passed'); process.exit(fails.length?1:0);
})();
