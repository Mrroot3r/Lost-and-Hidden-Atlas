// How smooth a drag of the map is, and how long a zoom step takes, with the CPU slowed four times (GUIDE.md section 9).
//   node tools/drag.js http://localhost:8766/index.html      serve the built site first, as for smoke.js
const {chromium,devices}=require('playwright');
(async()=>{ const b=await chromium.launch(); const c=await b.newContext(Object.assign({},devices['Pixel 7'],{hasTouch:false,isMobile:false})); const p=await c.newPage();
  const cdp=await c.newCDPSession(p); await cdp.send('Emulation.setCPUThrottlingRate',{rate:4});
  await p.goto(process.argv[2]||'http://localhost:8766/index.html'); await p.waitForFunction(()=>window.__atlasMap); await p.waitForTimeout(3500);
  const run=async(z,label)=>{ await p.evaluate(z=>{ window.__atlasMap.setView([42.9,-74.6],z,{animate:false}); },z); await p.waitForTimeout(1500);
    const box=await p.evaluate(()=>{ const r=document.querySelector('#map').getBoundingClientRect(); return [r.left+r.width/2,r.top+r.height/2]; });
    await p.evaluate(()=>{ window.__ft=[]; let last=performance.now(); window.__raf=function f(t){ window.__ft.push(t-last); last=t; window.__rid=requestAnimationFrame(f); }; window.__rid=requestAnimationFrame(window.__raf); });
    await p.mouse.move(box[0],box[1]); await p.mouse.down(); for(let i=1;i<=40;i++){ await p.mouse.move(box[0]-i*6,box[1]+i*2); } await p.mouse.up(); await p.waitForTimeout(700);
    const ft=await p.evaluate(()=>{ cancelAnimationFrame(window.__rid); return window.__ft.slice(2); }); ft.sort((a,b)=>a-b);
    console.log(label,'z'+z,'frames',ft.length,'median',Math.round(ft[ft.length>>1]),'ms  p90',Math.round(ft[Math.floor(ft.length*0.9)]),'ms  worst',Math.round(ft[ft.length-1]),'ms; DOM pins',await p.evaluate(()=>document.querySelectorAll('.leaflet-marker-icon').length)); };
  await run(7,'drag'); await run(9,'drag'); await run(12,'drag');
  const z=await p.evaluate(async()=>{ const m=window.__atlasMap, out=[]; for(const k of [8,7,9]){ const t=performance.now(); m.setZoom(k,{animate:false}); await new Promise(r=>requestAnimationFrame(()=>requestAnimationFrame(r))); out.push(Math.round(performance.now()-t)); } return out; });
  console.log('zoom steps (ms):',JSON.stringify(z));
  await b.close(); })();
