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
  // ---- sending a report or a place to the Atlas
  await p.click('#sheet-x'); await p.goto(url+'#joliet-iron-works'); await p.waitForFunction(()=>window.__atlasMap); await p.waitForTimeout(800);
  await p.click('.visit-item .visit-send'); await p.waitForTimeout(200);
  const sh=await p.evaluate(()=>{ const b=document.querySelector('.visit-item .sharebox'); if(!b) return null; const g=b.querySelector('a.share-gh'); return {gh:g?g.href:'',form:!!b.querySelector('a.share-form'),copy:[...b.querySelectorAll('button')].some(n=>/Copy as text/.test(n.textContent)),note:b.textContent}; });
  ok('"Send to the public Atlas" on a report opens a box with a GitHub link and a copy button',!!sh&&/issues\/new\?/.test(sh.gh)&&sh.copy,sh&&sh.gh.slice(0,90));
  const q=sh?new URL(sh.gh).searchParams:new URLSearchParams();
  ok('the link opens the visit form already filled in: place and id, date, what was found',q.get('template')==='visit.yml'&&/Joliet Iron Works/.test(q.get('place')||'')&&/\(joliet-iron-works\)/.test(q.get('place')||'')&&/^\d{4}-\d\d-\d\d$/.test(q.get('when')||'')&&q.get('found')==='Nothing there',[q.get('place'),q.get('when'),q.get('found')].join(' | '));
  ok('the box says nothing is sent until Submit, and that it is public',!!sh&&/nothing is sent until you press Submit/i.test(sh.note)&&/public/.test(sh.note));
  ok('the no-account button is offered and opens the owner\'s form with the report filled in',!!sh&&sh.form&&await p.evaluate(()=>{ const a=document.querySelector('.visit-item .sharebox a.share-form'), u=new URL(a.href); return /docs\.google\.com\/forms/.test(a.href)&&u.searchParams.get('usp')==='pp_url'&&[...u.searchParams.values()].some(v=>v==='A visit report')&&[...u.searchParams.values()].some(v=>/Joliet Iron Works/.test(v)); }));
  ok('with no form set up, the no-account link is left out',await p.evaluate(()=>window.__atlasShare({form:'',ent:{}},'visit',{place:'x'}).form===''));
  ok('with a form set up, the no-account link carries the report',await p.evaluate(()=>{ const L=window.__atlasShare({form:'https://docs.google.com/forms/d/e/TEST/viewform',ent:{kind:'entry.1',place:'entry.2',where:'entry.3',text:'entry.4'}},'visit',{place:'Old mill',id:'old-mill',when:'2026-11-15',found:'Found it',text:'Two walls',spot:'42.1, -73.9'}); const u=new URL(L.form); return u.searchParams.get('usp')==='pp_url'&&u.searchParams.get('entry.1')==='A visit report'&&/Old mill \(old-mill\)/.test(u.searchParams.get('entry.2'))&&/2026-11-15/.test(u.searchParams.get('entry.3'))&&/Found it\. Two walls/.test(u.searchParams.get('entry.4')); }));
  ok('a spot on the map can be sent with its coordinates filled in',await p.evaluate(()=>{ const m=window.__atlasMap; m.fire('contextmenu',{latlng:L.latLng(42.61234,-73.98765),containerPoint:L.point(200,200),layerPoint:L.point(200,200),originalEvent:{preventDefault(){}}}); const a=document.querySelector('.leaflet-popup a.spot-send, .ctxflat a.spot-send'); if(!a) return false; const u=new URL(a.href); m.closePopup(); return /forms/.test(a.href)&&[...u.searchParams.values()].some(v=>v==='42.61234, -73.98765'); }));
  // ---- "Report a problem with this place" (the owner, November 24, 2026): a place that is not what the Atlas is for, is gone, has its
  // pin or a fact wrong. Not a visit report: nobody has to have been there.
  ok('problem: the kind travels to the form, with the place, its id and the reason',await p.evaluate(()=>{ const L=window.__atlasShare({form:'https://docs.google.com/forms/d/e/TEST/viewform',ent:{kind:'entry.1',place:'entry.2',where:'entry.3',text:'entry.4'}},'problem',{place:'Old mill, Troy',id:'old-mill',reason:'Not what the Atlas is for',text:'A 1960s concrete block'}); const u=new URL(L.form), g=new URL(L.gh);
    return u.searchParams.get('entry.1')==='A problem with a place'&&/Old mill, Troy \(old-mill\)/.test(u.searchParams.get('entry.2'))&&/^Problem: Not what the Atlas is for\. A 1960s concrete block/.test(u.searchParams.get('entry.4'))&&g.searchParams.get('template')==='problem.yml'&&/^Problem: Old mill/.test(g.searchParams.get('title'))&&g.searchParams.get('problem')==='Not what the Atlas is for'&&/old-mill/.test(g.searchParams.get('place')); }));
  { const pr=await p.evaluate(()=>{ const d=document.querySelector('#prob'); if(!d) return null; return {open:d.open,sum:d.querySelector('summary').textContent.trim(),links:d.querySelectorAll('a').length,reasons:[...d.querySelectorAll('input[name=prob-why]')].map(i=>i.value)}; });
    ok('problem: every place page offers it, folded away, with five reasons and nothing to send until one is chosen',!!pr&&!pr.open&&/Report a problem with this place/.test(pr.sum)&&pr.reasons.length===5&&pr.reasons[0]==='Not what the Atlas is for'&&pr.links===0,JSON.stringify(pr));
    await p.click('#prob summary'); await p.waitForTimeout(150); await p.check('#prob input[value="The pin is in the wrong spot"]'); await p.fill('#prob-note','It is across the road'); await p.waitForTimeout(250);
    const sent=await p.evaluate(()=>{ const a=document.querySelector('#prob a.share-gh'), f=document.querySelector('#prob a.share-form'); if(!a) return null; const g=new URL(a.href); return {tpl:g.searchParams.get('template'),why:g.searchParams.get('problem'),more:g.searchParams.get('more'),place:g.searchParams.get('place'),form:f?new URL(f.href).search:''}; });
    ok('problem: choosing a reason and writing a line makes the links, with this place and its id filled in',!!sent&&sent.tpl==='problem.yml'&&sent.why==='The pin is in the wrong spot'&&sent.more==='It is across the road'&&/\(joliet-iron-works\)/.test(sent.place)&&/across/.test(decodeURIComponent(sent.form)),JSON.stringify(sent).slice(0,200)); }
  await p.click('#tab-guide'); await p.waitForTimeout(300);
  ok('the Guide offers a way to send a place without a pin',await p.evaluate(()=>{ const a=document.querySelector('#share-blank a.share-gh'); return !!a&&/template=lead\.yml/.test(a.href); }));
  await p.goto(url+'#joliet-iron-works'); await p.reload(); await p.waitForFunction(()=>window.__atlasMap); await p.waitForTimeout(800);
  p.once('dialog',d=>d.accept()); await p.click('.visit-item .visit-del'); await p.waitForTimeout(1300);
  u=await U(); ok('a report can be deleted',!(u.visits||{})['joliet-iron-works']||u.visits['joliet-iron-works'].length===0);
  // ---- a long press on the map: the two buttons say which is which
  await p.evaluate(()=>{ const m=window.__atlasMap; m.fire('contextmenu',{latlng:m.getCenter(),containerPoint:m.latLngToContainerPoint(m.getCenter()),originalEvent:{preventDefault(){}}}); }); await p.waitForTimeout(300);
  const pop=await p.evaluate(()=>{ const c=document.querySelector('.leaflet-popup-content, .ctxflat'); return c?c.textContent:''; });
  const tips=await p.evaluate(()=>[...document.querySelectorAll('.leaflet-popup-content a,.leaflet-popup-content button, .ctxflat a, .ctxflat button')].map(b=>b.textContent.trim()+'='+(b.title||'')).join(' ; '));
  ok('long press: "+ My places" and "Send to Atlas"; which is which is in each button\'s own hint, not a paragraph',/\+ My places/.test(pop)&&/Send to Atlas/.test(pop)&&!/My places stay on this device/.test(pop)&&/\+ My places=[^;]*this device/.test(tips)&&/Send to Atlas=.*checked before/.test(tips),tips.slice(0,260));
  await p.evaluate(()=>window.__atlasMap.closePopup());
  ok('no script errors',errs.length===0,errs.slice(0,2).join(' | '));
  await b.close(); console.log(fails.length?fails.length+' FAILED':'visit test passed'); process.exit(fails.length?1:0);
})();
