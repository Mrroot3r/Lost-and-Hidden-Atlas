// Start-up and interaction timings at phone size with the CPU slowed four times, about a mid-range phone (GUIDE.md section 9).
//   node tools/perf.js http://localhost:8766/index.html      serve the built site first, as for smoke.js
// Measure before and after any change meant to make the app faster. tools/drag.js measures a finger drag and zoom steps.
const {chromium,devices}=require('playwright');
(async()=>{ const b=await chromium.launch(); const c=await b.newContext(Object.assign({},devices['Pixel 7'])); const p=await c.newPage();
  const cdp=await c.newCDPSession(p); await cdp.send('Emulation.setCPUThrottlingRate',{rate:4});
  await p.addInitScript(()=>{ window.__lt=[]; try{ new PerformanceObserver(l=>l.getEntries().forEach(e=>window.__lt.push([Math.round(e.startTime),Math.round(e.duration)]))).observe({entryTypes:['longtask']}); }catch(e){} });
  const url=process.argv[2]||'http://localhost:8766/index.html'; const t0=Date.now();
  await p.goto(url,{waitUntil:'commit'}); await p.waitForFunction(()=>window.__atlasMap,null,{timeout:60000}); const tMap=Date.now()-t0;
  await p.waitForFunction(()=>document.querySelectorAll('#list li').length>0); const tList=Date.now()-t0;
  await p.waitForTimeout(3500);
  const r=await p.evaluate(()=>({lt:window.__lt,nav:Math.round(performance.getEntriesByType('navigation')[0].domContentLoadedEventEnd),markers:document.querySelectorAll('.leaflet-marker-icon').length,items:document.querySelectorAll('#list li').length,dom:document.querySelectorAll('*').length,
    res:performance.getEntriesByType('resource').filter(e=>/\.(js|json)/.test(e.name)).map(e=>[e.name.split('/').pop().split('?')[0],Math.round(e.startTime),Math.round(e.duration),Math.round((e.transferSize||e.encodedBodySize)/1024)])}));
  console.log('map ready',tMap,'ms; list',tList,'ms; DOMContentLoaded',r.nav,'ms; markers',r.markers,'list items',r.items,'DOM nodes',r.dom);
  console.log('long tasks (start,dur):',JSON.stringify(r.lt),'total',r.lt.reduce((a,x)=>a+x[1],0),'ms');
  console.log('resources:',JSON.stringify(r.res));
  // typing in the search box
  const ty=await p.evaluate(async()=>{ const q=document.querySelector('#q'), out=[]; for(const w of ['m','mi','mil','mill','mill ','mill r']){ const t=performance.now(); q.value=w; q.dispatchEvent(new Event('input',{bubbles:true})); await new Promise(r=>setTimeout(r,450)); out.push(Math.round(performance.now()-t-450)); } return out; });
  console.log('typing "mill r" (ms over the wait, per key):',JSON.stringify(ty), 'results:',await p.evaluate(()=>document.querySelector('#count').textContent));
  await p.evaluate(()=>{ const q=document.querySelector('#q'); q.value=''; q.dispatchEvent(new Event('input',{bubbles:true})); }); await p.waitForTimeout(600);
  // panning the map with every pin showing
  const pan=await p.evaluate(async()=>{ const m=window.__atlasMap; m.setView([42.9,-74.6],7,{animate:false}); await new Promise(r=>setTimeout(r,800)); const t=performance.now(); let n=0; for(let i=0;i<12;i++){ m.panBy([40,0],{animate:false}); await new Promise(r=>requestAnimationFrame(r)); n++; } return Math.round((performance.now()-t)/n); });
  console.log('pan at zoom 7: ms per frame',pan,'; markers',await p.evaluate(()=>document.querySelectorAll('.leaflet-marker-icon').length));
  await b.close(); })();
