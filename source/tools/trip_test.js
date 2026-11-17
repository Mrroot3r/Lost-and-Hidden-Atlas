// Phone-size check of the Trip tab's clock (arrival times, sunset) and of "Save this map view for offline".
//   node tools/trip_test.js http://localhost:8766/index.html      (serve the built site first, as for smoke.js)
const { chromium, devices } = require('playwright');
(async()=>{
  const fails=[]; const ok=(name,cond,extra)=>{ console.log((cond?'ok   ':'FAIL ')+name+(extra!==undefined?'  ['+extra+']':'')); if(!cond) fails.push(name); };
  const b=await chromium.launch({proxy:{server:process.env.HTTPS_PROXY||'http://x',bypass:'localhost,127.0.0.1'}});
  const c=await b.newContext(Object.assign({},devices['Pixel 7'],{timezoneId:'America/New_York',locale:'en-US'})); const p=await c.newPage(); const errs=[]; p.on('pageerror',e=>errs.push(e.message));
  const TRIP=['lidar-high-knob-walled-yard','lidar-rossman-hill-road-house-site','lidar-ccc-road-pits'];
  await c.addInitScript(t=>{ if(location.protocol!=='about:'&&!localStorage.getItem('lost-hidden-atlas-v1')) localStorage.setItem('lost-hidden-atlas-v1',JSON.stringify({trip:t})); },TRIP);
  await p.goto(process.argv[2]||'http://localhost:8766/index.html'); await p.waitForFunction(()=>window.__atlasMap); await p.waitForTimeout(600);
  const U=()=>p.evaluate(()=>JSON.parse(localStorage.getItem('lost-hidden-atlas-v1')||'{}'));
  const mins=s=>{ const m=/(\d{1,2}):(\d\d)\s*(AM|PM)/i.exec(s||''); if(!m) return null; return (+m[1]%12+(/pm/i.test(m[3])?12:0))*60+ +m[2]; };
  await p.click('#tab-trip'); await p.waitForTimeout(300);
  // ---- the clock
  await p.fill('#trip-day','2026-12-21'); await p.fill('#trip-t0','09:00'); await p.selectOption('#trip-stop','45'); await p.waitForTimeout(400);
  let at=await p.evaluate(()=>[...document.querySelectorAll('.stops .stop-at')].map(n=>n.textContent));
  ok('each stop shows when you would get there',at.length===3&&at.every(x=>mins(x)!==null),at.join(' | '));
  const a=at.map(mins); ok('later stops come later, by at least the time spent at each',a[1]-a[0]>=45&&a[2]-a[1]>=45&&a[0]>9*60,a.join(','));
  let sum=await p.innerText('#trip-clock');
  const ss=mins((/Sunset[^\d]*(\d{1,2}:\d\d\s*[AP]M)/i.exec(sum)||[])[1]);
  ok('sunset for the shortest day near Middleburgh is about 4:25 PM',ss!==null&&ss>=16*60+15&&ss<=16*60+38,sum.replace(/\n/g,' ').slice(0,160));
  ok('an early start finishes in daylight: no warning',(await p.locator('.trip-warn').count())===0);
  await p.fill('#trip-t0','14:30'); await p.waitForTimeout(400);
  ok('a late start warns that it runs past sunset',(await p.locator('.trip-warn').count())===1&&/sunset|dark/i.test(await p.innerText('.trip-warn')),(await p.locator('.trip-warn').count())?(await p.innerText('.trip-warn')).slice(0,120):'no warning');
  await p.fill('#trip-day','2026-06-21'); await p.waitForTimeout(400); sum=await p.innerText('#trip-clock');
  const s2=mins((/Sunset[^\d]*(\d{1,2}:\d\d\s*[AP]M)/i.exec(sum)||[])[1]); ok('and for the longest day about 8:35 PM',s2!==null&&s2>=20*60+25&&s2<=20*60+45,String(s2));
  await p.selectOption('#trip-stop','90'); await p.waitForTimeout(1200);
  ok('the time at each stop is remembered as a setting',((await U()).set||{}).tripStop===90);
  // ---- save the map view for offline
  await p.evaluate(()=>{ window.__atlasMap.setView([42.4276,-74.3184],9,{animate:false}); }); await p.waitForTimeout(400);
  await p.click('#lb-opt'); await p.waitForTimeout(250); await p.click('#view-off'); await p.waitForTimeout(300);
  ok('a view too wide to save says so and offers no button',/zoom in/i.test(await p.innerText('#view-box'))&&(await p.locator('#view-save').count())===0,(await p.innerText('#view-box')).slice(0,100));
  await p.click('#sheet-x'); await p.evaluate(()=>{ window.__atlasMap.setView([42.4276,-74.3184],17,{animate:false}); }); await p.waitForTimeout(500);
  await p.click('#lb-opt'); await p.waitForTimeout(250); if(!(await p.locator('#view-box').count())) await p.click('#view-off'); await p.waitForTimeout(300);
  const est=await p.innerText('#view-box'); ok('zoomed in, it says how many tiles and megabytes',/\d+ tiles/.test(est)&&/MB/.test(est),est.replace(/\n/g,' ').slice(0,140));
  await p.selectOption('#view-detail','16'); await p.waitForTimeout(250); const est2=await p.innerText('#view-box');
  const n1=+(/(\d+) tiles/.exec(est)||[0,0])[1], n2=+(/(\d+) tiles/.exec(est2)||[0,0])[1]; ok('less detail means fewer tiles',n2>0&&n2<n1,n1+' -> '+n2);
  await p.click('#view-save'); await p.waitForFunction(()=>{ const U=JSON.parse(localStorage.getItem('lost-hidden-atlas-v1')||'{}'); return Object.keys(U.saved||{}).some(k=>k.indexOf('view:')===0); },null,{timeout:90000}).catch(()=>{});
  const sv=(await U()).saved||{}, k=Object.keys(sv).find(x=>x.indexOf('view:')===0);
  ok('the view is saved and listed with a name',!!k&&/Map view/.test(sv[k].label)&&sv[k].n+sv[k].miss>0,k?JSON.stringify(sv[k]).slice(0,150):'nothing saved');
  ok('no script errors',errs.length===0,errs.slice(0,2).join(' | '));
  await b.close(); console.log(fails.length?fails.length+' FAILED':'trip and offline test passed'); process.exit(fails.length?1:0);
})();
