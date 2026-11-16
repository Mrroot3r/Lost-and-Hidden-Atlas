// Phone-size check of the Near tab (app.js, "near me"): the list, the big arrow, the compass, and the alert as you walk up to a place.
//   node tools/near_test.js http://localhost:8766/index.html      (serve the built site first, as for smoke.js)
// It stands 400 m south of a LiDAR lead near Berne, New York, and walks in. Screenshots go to /tmp/near_*.png.
const { chromium, devices } = require('playwright');
(async()=>{
  const fails=[]; const ok=(name,cond,extra)=>{ console.log((cond?'ok   ':'FAIL ')+name+(extra!==undefined?'  ['+extra+']':'')); if(!cond) fails.push(name); };
  const b=await chromium.launch({proxy:{server:process.env.HTTPS_PROXY||'http://x',bypass:'localhost,127.0.0.1'}});
  const c=await b.newContext(Object.assign({},devices['Pixel 7'],{permissions:['geolocation']})); const p=await c.newPage(); const errs=[];
  p.on('pageerror',e=>errs.push(e.message));
  await p.addInitScript(()=>{ window.__buzz=[]; navigator.vibrate=x=>{ window.__buzz.push(x); return true; }; });
  await p.goto(process.argv[2]||'http://localhost:8766/index.html'); await p.waitForFunction(()=>window.__atlasMap); await p.waitForTimeout(1200);
  // stand 400 m south of a LiDAR lead in the Helderbergs
  const T=await p.evaluate(()=>{ const D=JSON.parse(document.getElementById('d-sites').textContent); const s=(D.sites||D.s||[]).find(x=>x.id==='lidar-cole-hill-farmstead'); return s?[s.lat,s.lon,s.name]:null; });
  ok('the test place exists',!!T,T&&T[2]);
  const at=async(m)=>{ await c.setGeolocation({latitude:T[0]-m/111320,longitude:T[1],accuracy:6}); await p.waitForTimeout(2600); };
  await c.setGeolocation({latitude:T[0]-400/111320,longitude:T[1],accuracy:6});
  const tabs=await p.evaluate(()=>[...document.querySelectorAll('.tabs button')].map(n=>{ const r=n.getBoundingClientRect(); return [n.textContent.trim(),Math.round(r.width),n.scrollWidth>n.clientWidth+1]; }));
  ok('five tabs fit across the phone',tabs.length===5&&tabs.every(t=>!t[2]),JSON.stringify(tabs));
  await p.click('#tab-near'); await p.waitForTimeout(500);
  ok('before any fix it asks to find you',/needs to know where you are/.test(await p.innerText('#near-st')));
  await p.screenshot({path:'/tmp/near_0.png'});
  await p.getByRole('button',{name:'Find me'}).click(); await p.waitForTimeout(4500);
  const rows=async()=>p.evaluate(()=>[...document.querySelectorAll('#near-list .nmitem')].map(n=>[n.querySelector('b').textContent,n.querySelector('.mins').textContent,n.getAttribute('data-id'),n.querySelector('.nmarrow').style.transform]));
  let r=await rows(); const mine=()=>r.find(x=>x[2]==='p:lidar-cole-hill-farmstead')||['','','',''];
  const far=r.map(x=>{ const m=/^([\d.,]+) (ft|mi)/.exec(x[1]); return m?(+m[1].replace(',',''))*(m[2]==='mi'?5280:1):-1; });
  ok('the list fills in, nearest first',r.length>3&&far.every((v,i)=>v>0&&(!i||v>=far[i-1])),r.slice(0,4).map(x=>x[0]+' '+x[1]).join(' | '));
  ok('the place 400 m to the north reads 0.25 mi N, arrow straight up',/^0\.25 miN$/.test(mine()[1])&&mine()[3]==='rotate(0deg)',mine()[1]+' '+mine()[3]);
  ok('status says where it measures from',/From where you are, good to 6 m/.test(await p.innerText('#near-st')),(await p.innerText('#near-st')).replace(/\s+/g,' ').slice(0,90));
  const chips=await p.evaluate(()=>[...document.querySelectorAll('#near-k .chip')].map(n=>n.textContent.trim()+':'+n.getAttribute('aria-pressed')));
  ok('five kinds, all on, with counts',chips.length===5&&chips.every(x=>/ \d+:true$/.test(x)),chips.join(' '));
  ok('no stray text in the status row',!/null|undefined/.test(await p.innerText('#v-near')));
  await p.screenshot({path:'/tmp/near_1.png'});
  const kinds=await p.evaluate(()=>{ const o={}; document.querySelectorAll('#near-list .nmitem').forEach(n=>{ const k=n.getAttribute('data-id')[0]; o[k]=(o[k]||0)+1; }); return o; });
  console.log('     kinds within 3 mi:',JSON.stringify(kinds));
  // wider circle
  const n3=r.length; await p.selectOption('#near-r','10'); await p.waitForTimeout(700); r=await rows(); ok('a wider circle lists more',r.length>n3,n3+' -> '+r.length);
  await p.selectOption('#near-r','3'); await p.waitForTimeout(500);
  // a kind switched off
  await p.locator('#near-k .chip').nth(2).click(); await p.waitForTimeout(500); r=await rows(); ok('switching Vanished off removes them',!r.some(x=>x[2][0]==='v'));
  await p.locator('#near-k .chip').nth(2).click(); await p.waitForTimeout(500);
  // point me there
  await p.locator('#near-list .nmitem[data-id="p:lidar-cole-hill-farmstead"]').click(); await p.waitForTimeout(900);
  const goal=(await p.innerText('#near-goal')).replace(/\s+/g,' ');
  ok('tapping a row gives one big arrow and distance',/0\.25 mi N/.test(goal)&&goal.includes(T[2])&&/Details/.test(goal)&&/Stop/.test(goal),goal.slice(0,110));
  ok('and a dashed line on the map',await p.evaluate(()=>{ let n=0; window.__atlasMap.eachLayer(l=>{ if(l.options&&l.options.dashArray==='7 7') n++; }); return n===1; }));
  await p.screenshot({path:'/tmp/near_2.png'});
  // compass: the phone lying flat with its top pointing west (alpha 90) turns a north arrow to the right
  await p.evaluate(()=>{ const e=new Event('deviceorientationabsolute'); e.absolute=true; e.alpha=90; e.beta=0; e.gamma=0; window.dispatchEvent(e); }); await p.waitForTimeout(500);
  r=await rows(); ok('compass: phone pointing west, the north arrow turns to point right',mine()[3]==='rotate(90deg)'&&/Compass on/.test(await p.innerText('#near-note')),mine()[3]);
  // held upright facing east (beta 90, alpha 270): north is to the left
  await p.evaluate(()=>{ for(let i=0;i<12;i++){ const e=new Event('deviceorientationabsolute'); e.absolute=true; e.alpha=270; e.beta=88; e.gamma=0; window.dispatchEvent(e); } }); await p.waitForTimeout(600);
  r=await rows(); const deg=((+(/rotate\((-?[\d.]+)deg\)/.exec(mine()[3])||[0,NaN])[1])%360+360)%360; ok('compass: phone upright facing east, the north arrow points left',Math.abs(deg-270)<=4,mine()[3]);
  // turning slowly through north: the arrow must follow, never swing the long way round the dial
  const steps=await p.evaluate(async()=>{ const out=[], fire=h=>{ const e=new Event('deviceorientationabsolute'); e.absolute=true; e.alpha=(360-h)%360; e.beta=0; e.gamma=0; window.dispatchEvent(e); };
    const read=()=>{ const n=document.querySelector('#near-list .nmitem[data-id="p:lidar-cole-hill-farmstead"] .nmarrow'); return +(/rotate\((-?[\d.]+)deg\)/.exec(n.style.transform)||[0,NaN])[1]; };
    const frame=()=>new Promise(r=>requestAnimationFrame(()=>requestAnimationFrame(r)));
    for(let i=0;i<14;i++) fire(330); await frame();
    for(let h=330;h<=390;h+=4){ fire(h%360); fire(h%360); await frame(); out.push(read()); } return out; });
  const jump=Math.max(...steps.slice(1).map((v,i)=>Math.abs(v-steps[i])));
  ok('turning slowly through north, the arrow never swings the long way round',jump<45&&steps.every(v=>!isNaN(v)),steps.join(' '));
  // walk towards it: nothing at 250 m, a buzz inside 100 m, and no second buzz while still there
  await at(250); ok('no alert at 250 m',(await p.evaluate(()=>window.__buzz.length))===0);
  await at(80); const ban=await p.innerText('#banner').catch(()=>'');
  ok('inside 100 m: a buzz and a notice',(await p.evaluate(()=>window.__buzz.length))===1&&/Close by: /.test(ban)&&ban.includes(T[2]),ban.slice(0,120));
  await p.screenshot({path:'/tmp/near_3.png'});
  await at(60); ok('still there: no second buzz',(await p.evaluate(()=>window.__buzz.length))===1);
  await at(400); await at(70); ok('walk away and come back: it buzzes again',(await p.evaluate(()=>window.__buzz.length))===2);
  // alert off
  await p.selectOption('#near-al','0'); await at(400); await at(70); ok('alert off: silent',(await p.evaluate(()=>window.__buzz.length))===2&&!/Buzzes/.test(await p.innerText('#near-note')));
  // stop pointing
  await p.getByRole('button',{name:'Stop',exact:true}).click(); await p.waitForTimeout(400);
  ok('Stop removes the big arrow and the line',await p.evaluate(()=>{ let n=0; window.__atlasMap.eachLayer(l=>{ if(l.options&&l.options.dashArray==='7 7') n++; }); return n===0&&document.getElementById('near-goal').hidden; }));
  // the middle of the map
  await p.getByRole('button',{name:'Use map centre'}).click(); await p.evaluate(()=>{ window.__atlasMap.setView([42.6526,-73.7562],13,{animate:false}); }); await p.waitForTimeout(2200);
  r=await rows(); ok('middle of the map: the list follows the map to Albany',/From the middle of the map/.test(await p.innerText('#near-st'))&&r.length>10&&r[0][0]!==T[2],r.slice(0,3).map(x=>x[0]+' '+x[1]).join(' | '));
  await p.screenshot({path:'/tmp/near_4.png'});
  // a place row leads to its page through Details
  await p.locator('#near-list .nmitem[data-id^="p:"]').first().click(); await p.waitForTimeout(600); await p.getByRole('button',{name:'Details'}).click(); await p.waitForTimeout(700);
  ok('Details opens the place page',await p.evaluate(()=>!document.getElementById('v-detail').hidden));
  // kilometres
  await p.click('#tab-near'); await p.click('#lb-opt'); await p.click('#sheet-set'); await p.selectOption('#set-units','km'); await p.click('#sheet-x'); await p.waitForTimeout(600);
  r=await rows(); ok('kilometres: distances and choices switch',/ (m|km)[A-Z]/.test(r[0][1].replace(/^[\d.,]+/,' '))&&/5 km/.test(await p.innerText('#near-r')),r[0][1]+' / '+(await p.innerText('#near-r')).replace(/\s+/g,' '));
  ok('no script errors',errs.length===0,errs.join(' | ').slice(0,300));
  await b.close(); console.log(fails.length?fails.length+' FAILED':'near test passed'); process.exit(fails.length?1:0);
})().catch(e=>{ console.error(e); process.exit(1); });
