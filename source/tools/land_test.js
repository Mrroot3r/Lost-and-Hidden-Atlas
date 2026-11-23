// A phone turned on its side: the menu on the left, the map on the right, nothing that scrolls along the bottom edge
// (Android takes a swipe there as "go home" or "switch app").
//   node tools/land_test.js http://localhost:8766/index.html      (serve the built site first, as for smoke.js)
// Run it after changing the page layout in app.css (the grid, the layer bar, the Map options sheet), the Full button,
// or the head of a place page (.dhead, which stays put while the page scrolls).
// Screenshots go to /tmp/land_*.png.
const { chromium } = require('playwright');
(async()=>{
  const fails=[]; const ok=(name,cond,extra)=>{ console.log((cond?'ok   ':'FAIL ')+name+(extra!==undefined?'  ['+extra+']':'')); if(!cond) fails.push(name); };
  const b=await chromium.launch({proxy:{server:process.env.HTTPS_PROXY||'http://x',bypass:'localhost,127.0.0.1'}});
  const c=await b.newContext({viewport:{width:390,height:844},deviceScaleFactor:2,hasTouch:true,isMobile:true,userAgent:'Mozilla/5.0 (Linux; Android 14; Pixel 7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0 Mobile Safari/537.36'});
  const p=await c.newPage(); const errs=[]; p.on('pageerror',e=>errs.push(e.message));
  await p.goto(process.argv[2]||'http://localhost:8766/index.html'); await p.waitForFunction(()=>window.__atlasMap); await p.waitForTimeout(600);
  const R=sel=>p.evaluate(sel=>{ const n=document.querySelector(sel); if(!n||n.offsetParent===null&&getComputedStyle(n).position!=='fixed') return null; const r=n.getBoundingClientRect(); return {l:r.left,t:r.top,r:r.right,b:r.bottom,w:r.width,h:r.height}; },sel);
  const mapSize=()=>p.evaluate(()=>{ const s=window.__atlasMap.getSize(); return [s.x,s.y]; });
  // ---- upright: as it was
  let side=await R('#side'), stage=await R('#stage');
  ok('upright: the map is above the menu',stage.b<=side.t+1&&stage.w>380,[stage.b,side.t].join(' '));
  // The compare divider pushed to the right edge: its right-hand label used to stick out past the screen, which made the page itself
  // wider than the phone. In the Android app the whole page could then be dragged about by the layer bar, with blank beside and below it.
  await p.evaluate(()=>{ document.getElementById('lb-cmp').click(); }); await p.waitForTimeout(500);
  { const g=await p.$('#swipe .grip'), r=await g.boundingBox(); await p.mouse.move(r.x+18,r.y+18); await p.mouse.down(); await p.mouse.move(388,r.y+18,{steps:5}); await p.mouse.up(); await p.waitForTimeout(300); }
  const wide=await p.evaluate(()=>{ window.scrollTo(200,200); const s=document.scrollingElement; return {w:s.scrollWidth,h:s.scrollHeight,iw:innerWidth,ih:innerHeight,x:scrollX,y:scrollY,grip:document.querySelector('#swipe .grip').getBoundingClientRect().left}; });
  ok('upright, compare divider at the right edge: the page is still exactly the size of the screen and cannot be scrolled',wide.grip>300&&wide.iw===390&&wide.ih===844&&wide.w<=390&&wide.h<=844&&wide.x===0&&wide.y===0,JSON.stringify(wide));
  await p.evaluate(()=>{ window.scrollTo(0,0); document.getElementById('lb-cmp').click(); }); await p.waitForTimeout(300);
  // ---- upright: the layer bar is the edge between map and list, and drags up and down (the owner, November 23, 2026: "I always want
  // to be able to see a little bit of the bottom": more map, with the first entry of the list still showing)
  const geom=()=>p.evaluate(()=>{ const r=q=>document.querySelector(q).getBoundingClientRect(), st=r('#stage'), sd=r('#side'), v=r('.view:not([hidden])'), ms=window.__atlasMap.getSize(); return {stage:Math.round(st.height),sideTop:Math.round(sd.top),view:Math.round(v.height),map:ms.y,ih:innerHeight}; });
  const dragBar=async(dx,dy)=>{ const bb=await (await p.$('#lb-opt')).boundingBox(); const x=bb.x+bb.width/2, y=bb.y+bb.height/2; dy=Math.max(3-y,Math.min(841-y,dy)); await p.mouse.move(x,y); await p.mouse.down(); await p.mouse.move(x+dx/2,y+dy/2,{steps:4}); await p.mouse.move(x+dx,y+dy,{steps:4}); await p.mouse.up(); await p.waitForTimeout(350); };
  const g0=await geom();
  await dragBar(0,150); const g1=await geom();
  ok('upright: dragging the layer bar down gives the map that much more room',Math.abs(g1.stage-g0.stage-150)<=3&&Math.abs(g1.sideTop-g0.sideTop-150)<=3,[g0.stage,g1.stage].join(' -> '));
  ok('upright: the map itself is redrawn at the new size',Math.abs(g1.map-g0.map-150)<=3,[g0.map,g1.map].join(' -> '));
  ok('upright: letting go on a button after a drag does not press it',await p.evaluate(()=>document.querySelector('#sheet').hidden));
  await dragBar(0,900); const g2=await geom();
  ok('upright: dragged to the bottom, the tabs and the first entry of the list still show',g2.view>=150&&g2.view<=200&&g2.stage>g1.stage,JSON.stringify(g2));
  await dragBar(0,-900); const g3=await geom();
  ok('upright: dragged to the top, the map keeps a usable strip',g3.stage>=220&&g3.stage<=240,JSON.stringify(g3));
  await dragBar(-120,6); const g4=await geom();
  ok('upright: a sideways drag (scrolling the bar) changes nothing',g4.stage===g3.stage,[g3.stage,g4.stage].join(' '));
  await dragBar(0,200); const g5=await geom(); await p.waitForTimeout(400);
  await p.reload(); await p.waitForFunction(()=>window.__atlasMap); await p.waitForTimeout(600); const g6=await geom();
  ok('upright: the map opens at the size it was left at',Math.abs(g6.stage-g5.stage)<=2,[g5.stage,g6.stage].join(' '));
  await p.evaluate(()=>document.getElementById('lb-opt').click()); await p.waitForTimeout(400);
  ok('upright: a plain tap on the bar still works',await p.evaluate(()=>!!document.querySelector('#lb-opt')&&[...document.querySelectorAll('button')].some(b=>b.textContent.trim()==='Done'&&b.offsetParent!==null)));
  await p.evaluate(()=>{ const d=[...document.querySelectorAll('button')].find(b=>b.textContent.trim()==='Done'&&b.offsetParent!==null); d&&d.click(); }); await p.waitForTimeout(300);
  // ---- turned on its side, at the two sizes phones come in (under and over the old 820-point switch)
  for(const [W,H,name] of [[780,360,'narrow phone'],[915,412,'wide phone']]){
    await p.setViewportSize({width:W,height:H}); await p.waitForTimeout(500);
    side=await R('#side'); stage=await R('#stage'); const view=await R('.view:not([hidden])'), bar=await R('#lbar'), ls=await R('#lscroll'), ms=await mapSize();
    ok(name+': the menu is on the left and the map on the right',side&&stage&&side.l<1&&side.r<=stage.l+1&&Math.abs(stage.r-W)<1,side&&stage?[side.r,stage.l].join(' '):'missing');
    ok(name+': both run the full height',side.h>=H-1&&stage.h>=H-1,[side.h,stage.h].join(' '));
    ok(name+': the map has more than half the width and nearly all the height',ms[0]>=W*0.5&&ms[1]>=H-70,ms.join('x'));
    ok(name+': the list is tall enough to scroll with a thumb',view&&view.h>=H-80,view&&view.h);
    ok(name+': the layer bar is at the top of the map, not along the bottom edge',bar&&bar.b<=H-120&&ls.b<=H-120&&bar.l>=stage.l-1,bar&&[bar.t,bar.b].join(' '));
    ok(name+': the Full button is there',(await R('#lb-big'))!==null);
    ok(name+': tabs fit in the column',await p.evaluate(()=>{ const t=document.querySelector('.tabs'); return t.scrollWidth<=t.clientWidth+1; }));
    // a finger drag on the map moves the map
    const c0=await p.evaluate(()=>{ const c=window.__atlasMap.getCenter(); return [c.lat,c.lng]; });
    const mx=stage.l+stage.w/2, my=H/2; await p.mouse.move(mx,my); await p.mouse.down(); await p.mouse.move(mx-80,my+40,{steps:6}); await p.mouse.up(); await p.waitForTimeout(400);
    const c1=await p.evaluate(()=>{ const c=window.__atlasMap.getCenter(); return [c.lat,c.lng]; });
    ok(name+': dragging the map moves it',Math.abs(c0[1]-c1[1])>1e-4);
    // the list scrolls
    const sc=await p.evaluate(()=>{ const v=document.querySelector('.view:not([hidden])'); v.scrollTop=200; return v.scrollTop; });
    ok(name+': the list scrolls',sc>100,sc);
    // Map options opens over the menu and leaves the map in sight
    await p.click('#lb-opt'); await p.waitForTimeout(350); const sh=await R('#sheet');
    ok(name+': Map options opens on the left, full height, with the map still showing',sh&&sh.l<1&&sh.r<=stage.l+2&&sh.h>=H-1,sh&&[sh.l,sh.r,sh.h].join(' '));
    ok(name+': its Done button can be reached',await p.evaluate(()=>{ const r=document.querySelector('#sheet-x').getBoundingClientRect(); return r.top>=0&&r.bottom<=innerHeight&&r.width>40; }));
    await p.screenshot({path:'/tmp/land_'+W+'_options.png'});
    await p.click('#sheet-x'); await p.waitForTimeout(250);
    // Full: the map takes everything; again brings the menu back
    await p.click('#lb-big'); await p.waitForTimeout(350); stage=await R('#stage');
    ok(name+': Full gives the map the whole screen',stage.l<1&&Math.abs(stage.w-W)<1&&(await R('#side'))===null,stage.w);
    ok(name+': the map knows its new size',Math.abs((await mapSize())[0]-W)<2,(await mapSize()).join('x'));
    await p.click('#lb-big'); await p.waitForTimeout(350);
    ok(name+': Full again brings the menu back',(await R('#side'))!==null&&(await R('#stage')).l>200);
    await p.screenshot({path:'/tmp/land_'+W+'.png'});
  }
  // ---- a place page and the field log bar, on the narrow one
  await p.setViewportSize({width:780,height:360}); await p.waitForTimeout(400);
  await p.evaluate(()=>{ const v=document.querySelector('#v-list'); v.scrollTop=v.scrollHeight; }); await p.waitForTimeout(200);
  await p.evaluate(()=>{ const li=[...document.querySelectorAll('#list li')].find(n=>!n.classList.contains('empty')); (li.querySelector('button,a,[role=button]')||li).click(); }); await p.waitForTimeout(600);
  await p.screenshot({path:'/tmp/land_780_place.png'});
  ok('a place page opens in the left column',await p.evaluate(()=>{ const v=document.querySelector('#v-detail'); const r=v.getBoundingClientRect(); return !v.hidden&&r.height>=innerHeight-80&&r.right<=document.querySelector('#stage').getBoundingClientRect().left+1; }));
  const hd=await p.evaluate(()=>{ const h=document.querySelector('#v-detail .dhead'), v=document.querySelector('#v-detail'), bs=[...h.querySelectorAll('.dtop .btn')].map(b=>b.getBoundingClientRect());
    return {h:h.getBoundingClientRect().height,view:v.getBoundingClientRect().height,rows:new Set(bs.map(r=>Math.round(r.top))).size,n:bs.length,right:Math.max(...bs.map(r=>r.right)),edge:v.getBoundingClientRect().right,inside:!!h.querySelector('.dphoto,.dmeta,.sub2')}; });
  ok('the place page\'s fixed head is one row of buttons and the name, under a third of the column',hd.rows===1&&hd.right<=hd.edge&&hd.h<=hd.view/3&&!hd.inside,JSON.stringify(hd));
  await p.evaluate(()=>{ document.querySelector('#v-detail').scrollTop=400; }); await p.waitForTimeout(150);
  const sc=await p.evaluate(()=>{ const v=document.querySelector('#v-detail'), h=v.querySelector('.dhead'); return Math.round(v.getBoundingClientRect().bottom-h.getBoundingClientRect().bottom); });
  ok('scrolled, three quarters of the column is left to read',sc>=hd.view*0.75,sc+' px under the head of '+Math.round(hd.view));
  await p.screenshot({path:'/tmp/land_780_place_scrolled.png'});
  { const long=await p.evaluate(()=>{ const S=window.__atlasNM.sites().slice().sort((x,y)=>y.name.length-x.name.length)[0]; location.hash='#'+S.id; return S.name; }); await p.waitForTimeout(700);
    const fn=await p.evaluate(()=>{ const v=document.querySelector('#v-detail'), h=v.querySelector('.dhead h2'), f=v.querySelector('.dintro .fullname'); return {cut:h.scrollHeight>h.clientHeight+2,full:f?f.textContent:null,head:Math.round(v.querySelector('.dhead').getBoundingClientRect().height)}; });
    ok('a name too long for two lines is cut in the head and given in full just under it',fn.cut&&fn.full===long&&fn.head<=110,JSON.stringify(fn).slice(0,160));
    await p.screenshot({path:'/tmp/land_780_longname.png'});
    await p.setViewportSize({width:390,height:844}); await p.waitForTimeout(500);
    ok('upright, where the name is not cut, it is not written twice',await p.evaluate(()=>{ const v=document.querySelector('#v-detail'), h=v.querySelector('.dhead h2'); return h.scrollHeight<=h.clientHeight+2&&!v.querySelector('.dintro .fullname'); }));
    await p.setViewportSize({width:780,height:360}); await p.waitForTimeout(500);
    ok('and turned back on its side, the full name returns',await p.evaluate(()=>!!document.querySelector('#v-detail .dintro .fullname'))); }
  // the bars that float on the map sit under the layer bar, not on it
  await p.evaluate(()=>{ for(const id of ['addbar','recbar']) document.getElementById(id).hidden=false; }); await p.waitForTimeout(200);
  const bb=await R('#lbar'), ab=await R('#addbar'), rb=await R('#recbar');
  ok('the add-a-place and field-log bars sit below the layer bar and clear of each other',ab.t>=bb.b&&rb.t>=ab.b-1&&rb.b<=360,[bb.b,ab.t,ab.b,rb.t].join(' '));
  await p.screenshot({path:'/tmp/land_780_bars.png'});
  await p.evaluate(()=>{ for(const id of ['addbar','recbar']) document.getElementById(id).hidden=true; });
  // ---- upright again, and upright with the keyboard up (a short, wide-ish window must not flip the layout)
  await p.setViewportSize({width:390,height:844}); await p.waitForTimeout(400); side=await R('#side'); stage=await R('#stage');
  ok('upright again: the map is back above the menu',stage.b<=side.t+1&&stage.w>380&&(await mapSize())[0]>380);
  await p.setViewportSize({width:412,height:380}); await p.waitForTimeout(400); side=await R('#side'); stage=await R('#stage');
  ok('upright with the keyboard up: still map above menu',stage.b<=side.t+1&&stage.w>400,[stage.w,stage.b,side.t].join(' '));
  ok('no script errors',errs.length===0,errs.slice(0,2).join(' | '));
  await b.close(); console.log(fails.length?fails.length+' FAILED':'landscape test passed'); process.exit(fails.length?1:0);
})();
