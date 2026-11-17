// Phone-size check of visit reports (app.js, "visit reports") and of tools/visits.py, which reads what the app exports.
//   node tools/visit_test.js http://localhost:8766/index.html      (serve the built site first, as for smoke.js)
// It opens a LiDAR lead, files a report from 35 m away from the pin, edits it, exports it and runs the worklist tool.
const { chromium, devices } = require('playwright'); const fs=require('fs'), path=require('path'), cp=require('child_process');
(async()=>{
  const fails=[]; const ok=(name,cond,extra)=>{ console.log((cond?'ok   ':'FAIL ')+name+(extra!==undefined?'  ['+extra+']':'')); if(!cond) fails.push(name); };
  const ID='lidar-high-knob-walled-yard', PIN=[42.427596,-74.318405], ME=[PIN[0]+0.00030,PIN[1]+0.00010];      // about 34 m north-north-east of the pin
  const b=await chromium.launch({proxy:{server:process.env.HTTPS_PROXY||'http://x',bypass:'localhost,127.0.0.1'}});
  const c=await b.newContext(Object.assign({},devices['Pixel 7'],{geolocation:{latitude:ME[0],longitude:ME[1],accuracy:5},permissions:['geolocation','clipboard-read','clipboard-write']})); const p=await c.newPage(); const errs=[]; p.on('pageerror',e=>errs.push(e.message));
  const url=(process.argv[2]||'http://localhost:8766/index.html');
  await p.goto(url+'#'+ID); await p.waitForFunction(()=>window.__atlasMap); await p.waitForTimeout(900);
  const U=()=>p.evaluate(()=>JSON.parse(localStorage.getItem('lost-hidden-atlas-v1')||'{}'));
  ok('the place page opens',/Walled yard/.test(await p.innerText('#v-detail h2')));
  ok('it has a "I was here" button and no reports yet',(await p.locator('#visit-add').count())===1&&(await p.locator('.visit-item').count())===0);
  await p.click('#visit-add'); await p.waitForTimeout(200);
  await p.click('#visit-save'); await p.waitForTimeout(200);
  ok('a report needs an answer to "what did you find"',(await p.locator('.visit-item').count())===0&&/Choose/.test(await p.innerText('#visit-msg')));
  await p.click('.visit-v[data-v="found"]'); await p.fill('#visit-x','Laid-stone cellar about 5 m square, a well 10 m east of it.'); await p.fill('#visit-a','Parked at the gate; the forest road is walkable.');
  ok('without a position fix "where I am standing" cannot be chosen yet',await p.evaluate(()=>document.querySelector('#visit-at-me').disabled));
  await p.click('#lb-loc'); await p.waitForFunction(()=>!document.querySelector('#visit-at-me').disabled,null,{timeout:8000}).catch(()=>{});
  await p.check('#visit-at-me'); await p.waitForTimeout(200);
  const far=await p.innerText('#visit-far'); ok('it says how far that is from the pin',/3\d m|1\d\d ft/.test(far),far);
  await p.click('#visit-save'); await p.waitForTimeout(1300);
  let u=await U(), r=(u.visits||{})[ID]||[];
  ok('the report is saved with what was found, the access and the true spot',r.length===1&&r[0].v==='found'&&/Laid-stone/.test(r[0].x)&&/gate/.test(r[0].a)&&Array.isArray(r[0].at)&&Math.abs(r[0].at[0]-ME[0])<1e-4&&/^\d{4}-\d\d-\d\d$/.test(r[0].t),JSON.stringify(r[0]||{}).slice(0,160));
  ok('progress becomes Visited',u.status&&u.status[ID]==='visited');
  ok('the pin moves to the true spot',u.moved&&u.moved[ID]&&Math.abs(u.moved[ID][0]-ME[0])<1e-4,JSON.stringify((u.moved||{})[ID]));
  ok('the page lists the report',(await p.locator('.visit-item').count())===1&&/Found it/.test(await p.innerText('.visit-item'))&&/Laid-stone/.test(await p.innerText('.visit-item')));
  await p.click('.visit-item .visit-edit'); await p.waitForTimeout(200); await p.click('.visit-v[data-v="else"]'); await p.fill('#visit-x','A barn foundation, not a house.'); await p.click('#visit-save'); await p.waitForTimeout(1300);
  u=await U(); r=u.visits[ID]; ok('a report can be edited',r.length===1&&r[0].v==='else'&&/barn/.test(r[0].x));
  // a second place gets a "nothing there" report, with the pin left alone
  await p.goto(url+'#joliet-iron-works'); await p.waitForFunction(()=>window.__atlasMap); await p.waitForTimeout(900);
  await p.click('#visit-add'); await p.click('.visit-v[data-v="nothing"]'); await p.fill('#visit-x','Graded flat for a parking area.'); await p.click('#visit-save'); await p.waitForTimeout(1300);
  u=await U(); ok('a second place: "nothing there", pin not moved',u.visits['joliet-iron-works'][0].v==='nothing'&&!u.visits['joliet-iron-works'][0].at&&!(u.moved||{})['joliet-iron-works']);
  // the export, and the tool that reads it
  await p.click('#lb-opt'); await p.click('#sheet-set'); await p.waitForTimeout(250);
  await p.evaluate(()=>{ const d=[...document.querySelectorAll('#sheet-b details')].find(n=>/Your data/.test(n.textContent)); d.open=true; }); await p.getByRole('button',{name:'Copy my additions for Claude'}).click(); await p.waitForTimeout(300);
  const out=await p.inputValue('#bk-out'); let j=null; try{ j=JSON.parse(out); }catch(e){}
  ok('"Copy my additions for Claude" carries the visit reports, with each place\'s name and Atlas pin',!!j&&Array.isArray(j.visits)&&j.visits.length===2&&j.visits.some(v=>v.id===ID&&/Walled yard/.test(v.name)&&Math.abs(v.pin[0]-PIN[0])<1e-6&&v.reports.length===1),out.slice(0,120));
  if(j){ const f='/tmp/visit_export.json'; fs.writeFileSync(f,out); const tool=path.join(__dirname,'visits.py');
    const res=cp.spawnSync('python3',[tool,f],{encoding:'utf8'}); const t=res.stdout||'';
    ok('tools/visits.py turns the export into a worklist',res.status===0&&/lidar-high-knob-walled-yard/.test(t)&&/move the pin/i.test(t)&&/3\d m/.test(t)&&/joliet-iron-works/.test(t)&&/nothing there/i.test(t),(t||res.stderr||'').split('\n').slice(0,3).join(' / ').slice(0,200)); }
  await p.click('#sheet-x'); await p.goto(url+'#joliet-iron-works'); await p.waitForFunction(()=>window.__atlasMap); await p.waitForTimeout(800);
  p.once('dialog',d=>d.accept()); await p.click('.visit-item .visit-del'); await p.waitForTimeout(1300);
  u=await U(); ok('a report can be deleted',!(u.visits||{})['joliet-iron-works']||u.visits['joliet-iron-works'].length===0);
  ok('no script errors',errs.length===0,errs.slice(0,2).join(' | '));
  await b.close(); console.log(fails.length?fails.length+' FAILED':'visit test passed'); process.exit(fails.length?1:0);
})();
