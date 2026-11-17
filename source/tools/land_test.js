// A phone turned on its side: the menu on the left, the map on the right, nothing that scrolls along the bottom edge
// (Android takes a swipe there as "go home" or "switch app").
//   node tools/land_test.js http://localhost:8766/index.html      (serve the built site first, as for smoke.js)
// Run it after changing the page layout in app.css (the grid, the layer bar, the Map options sheet) or the Full button.
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
