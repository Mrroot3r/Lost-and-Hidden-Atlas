// "Nothing to see": places marked Nothing visible or Marker only, and vanished places (the orange dots).
//   node tools/nothing_test.js http://localhost:8766/index.html      (serve the built site first, as for smoke.js)
// Run it after changing nothingToSee(), nmBuzzes(), the hideGone test in match() or nmCollect(), or the three settings
// (quietGone, hideGone, buzzVanished). What it holds the app to:
//   1. by default a place with nothing to see is listed but does not buzz, a standing place buzzes, and a vanished place
//      is listed in the Near tab but does not buzz; the list handed to the Android app's recorder follows the same rule;
//   2. "No buzz for places with nothing to see" off: such a place buzzes again; "Buzz for vanished places too" on: they buzz;
//   3. "Hide places with nothing to see" takes them off the Places list, the map and the Near tab, leaves drowned places,
//      and choosing "Nothing visible" in Filters still shows those;
//   4. the three settings are under the gear.
const { chromium } = require('playwright');
(async()=>{
  const fails=[]; const ok=(name,cond,extra)=>{ console.log((cond?'ok   ':'FAIL ')+name+(extra!==undefined?'  ['+extra+']':'')); if(!cond) fails.push(name); };
  const url=process.argv[2]||'http://localhost:8766/index.html'; const b=await chromium.launch(); const errs=[];
  const open=async set=>{ const c=await b.newContext({viewport:{width:390,height:844},isMobile:true,hasTouch:true}); const p=await c.newPage(); p.on('pageerror',e=>errs.push(e.message));
    await c.route(u=>!/^http:\/\/localhost/.test(u.href),r=>r.fulfill({status:204,body:''}));
    await p.addInitScript(s=>{ window.__buzz=[]; navigator.vibrate=x=>{ window.__buzz.push(x); return true; }; try{ localStorage.setItem('lost-hidden-atlas-v1',JSON.stringify({v:1,home:{id:'alb',by:1},set:s,ui:{nm:{r:3,al:100,k:{p:1,l:0,v:1,m:0,c:0}}}})); }catch(e){} },set||{});
    await p.goto(url); await p.waitForFunction(()=>window.__atlasMap); await p.waitForTimeout(400); return {c,p}; };
  // stand on a place and ask whether it buzzes (the alert code itself, nmFix, with the position handed in)
  const buzzAt=(p,id)=>p.evaluate(id=>{ const {sites,nmFix,nmCollect,nmBuzzes,NM,XL,xlLoad,syncMarkers}=window.__atlasNM; const s=sites().find(x=>x.id===id); NM.in.clear(); NM.cand=null; window.__buzz=[]; nmFix([s.lat+0.0001,s.lon],5); return window.__buzz.length>0; },id);
  let {c,p}=await open();
  const pick=await p.evaluate(()=>{ const {sites}=window.__atlasNM; const S=sites(), f=st=>S.filter(s=>s.st===st&&!S.some(o=>o!==s&&o.st!==st&&Math.abs(o.lat-s.lat)<0.004&&Math.abs(o.lon-s.lon)<0.006));
    return {gone:(f('gone')[0]||{}).id,marker:(f('marker')[0]||{}).id,standing:(f('standing')[0]||{}).id,water:(S.find(s=>s.st==='water')||{}).id,
      n:{gone:S.filter(s=>s.st==='gone').length,marker:S.filter(s=>s.st==='marker').length,water:S.filter(s=>s.st==='water').length,all:S.length}}; });
  ok('there are places of each kind to try',pick.gone&&pick.marker&&pick.standing&&pick.water,JSON.stringify(pick.n));
  // 1. defaults
  ok('by default a place with nothing visible does not buzz',!(await buzzAt(p,pick.gone)),pick.gone);
  ok('by default a marker-only place does not buzz',!(await buzzAt(p,pick.marker)),pick.marker);
  ok('a standing place still buzzes',await buzzAt(p,pick.standing),pick.standing);
  const near=await p.evaluate(id=>{ const {sites,nmFix,nmCollect,nmBuzzes,NM,XL,xlLoad,syncMarkers}=window.__atlasNM; const s=sites().find(x=>x.id===id); return nmCollect([s.lat,s.lon],1).some(x=>x.id==='p:'+id); },pick.gone);
  ok('by default a place with nothing to see is still listed in the Near tab',near);
  const vz=await p.evaluate(async()=>{ const {nmCollect,nmBuzzes,XL,xlLoad}=window.__atlasNM; xlLoad('vanished',true); for(let i=0;i<60&&!(XL.vanished&&XL.vanished.data);i++) await new Promise(r=>setTimeout(r,150)); window.__atlasNM.xlNeed('vanished',42,-75,43.5,-73); for(let i=0;i<60&&!Object.keys((XL.vanished&&XL.vanished.idx)||{}).length;i++) await new Promise(r=>setTimeout(r,150));      /* the index, then New York's own file */
    const X=XL.vanished; if(!X||!X.idx) return null; let list=[], t=null;
    for(const k of Object.keys(X.idx).slice(0,400)){ const x=X.idx[k][0]; list=nmCollect([x[0],x[1]],0.3); t=list.find(y=>y.k==='v'); if(t) break; }      /* some kinds (old schools) are hidden by default */ return {listed:!!t,buzz:t?nmBuzzes(t):null,pushed:list.filter(nmBuzzes).some(y=>y.k==='v')}; });
  ok('a vanished place is listed in the Near tab but does not buzz, nor go to the phone\'s recorder',vz&&vz.listed&&vz.buzz===false&&!vz.pushed,JSON.stringify(vz));
  const rec=await p.evaluate(id=>{ const {sites,nmFix,nmCollect,nmBuzzes,NM,XL,xlLoad,syncMarkers}=window.__atlasNM; const s=sites().find(x=>x.id===id); return nmCollect([s.lat,s.lon],1).filter(nmBuzzes).some(x=>x.id==='p:'+id); },pick.gone);
  ok('the list for the Android app\'s recorder leaves out the place with nothing to see',!rec);
  // 1b. one place can be silenced for good: it stays in the Near list and stops buzzing, here and on the phone's recorder
  { const s=await p.evaluate(id=>{ const x=window.__atlasNM.sites().find(x=>x.id===id); return [x.lat,x.lon,x.name]; },pick.standing);
    await p.evaluate(a=>{ window.__atlasMap.setView([a[0],a[1]],15,{animate:false}); },s); await p.click('#tab-near'); await p.waitForTimeout(500);
    await p.evaluate(()=>{ const b=[...document.querySelectorAll('#v-near button')].find(b=>/Use map centre/i.test(b.textContent)); if(b) b.click(); }); await p.waitForTimeout(700);
    const row=p.locator('#near-list .nmitem[data-id="p:'+pick.standing+'"]'); const has=await row.count();
    if(has) await row.click(); await p.waitForTimeout(500);
    const mb=p.locator('#near-goal #near-mute');
    ok('the card for a chosen place has a button to silence it',has===1&&(await mb.count())===1&&/silence|never buzz/i.test(await mb.innerText().catch(()=>'')),has+' row; '+(await mb.innerText().catch(()=>'no button')));
    if(await mb.count()) await mb.click(); await p.waitForTimeout(400);
    ok('silenced: standing right on it no longer buzzes',!(await buzzAt(p,pick.standing)));
    const st=await p.evaluate(id=>{ const {sites,nmCollect,nmBuzzes}=window.__atlasNM; const x=sites().find(x=>x.id===id), l=nmCollect([x.lat,x.lon],1); return {listed:l.some(t=>t.id==='p:'+id),pushed:l.filter(nmBuzzes).some(t=>t.id==='p:'+id),row:(document.querySelector('#near-list .nmitem[data-id="p:'+id+'"]')||{}).textContent||''}; },pick.standing);
    ok('it is still listed in the Near tab, marked as silenced, and left out of the list for the phone\'s recorder',st.listed&&!st.pushed&&/silenced/i.test(st.row),JSON.stringify(st).slice(0,160));
    await p.waitForTimeout(300);
    ok('the choice is kept with the reader\'s other data',await p.evaluate(id=>(JSON.parse(localStorage.getItem('lost-hidden-atlas-v1')).mute||[]).indexOf('p:'+id)>=0,pick.standing));
    await p.click('#lb-opt'); await p.click('#sheet-set'); await p.waitForTimeout(300);
    const un=p.locator('#set-unmute'); ok('Settings says how many are silenced and offers to undo it',(await un.count())===1&&/1 /.test(await p.locator('#set-muted').innerText().catch(()=>'')),await p.locator('#set-muted').innerText().catch(()=>'no line'));
    if(await un.count()) await un.click(); await p.waitForTimeout(300); await p.click('#sheet-x').catch(()=>{});
    ok('undone: it buzzes again',await buzzAt(p,pick.standing)); }
  await c.close();
  // 2. switched the other way
  ({c,p}=await open({quietGone:false,buzzVanished:true}));
  ok('"No buzz for places with nothing to see" off: it buzzes again',await buzzAt(p,pick.gone));
  const v2=await p.evaluate(async()=>{ const {nmCollect,nmBuzzes,XL,xlLoad}=window.__atlasNM; xlLoad('vanished',true); for(let i=0;i<60&&!(XL.vanished&&XL.vanished.data);i++) await new Promise(r=>setTimeout(r,150)); window.__atlasNM.xlNeed('vanished',42,-75,43.5,-73); for(let i=0;i<60&&!Object.keys((XL.vanished&&XL.vanished.idx)||{}).length;i++) await new Promise(r=>setTimeout(r,150));      /* the index, then New York's own file */
    const X=XL.vanished; let t=null; for(const k of Object.keys(X.idx).slice(0,400)){ const x=X.idx[k][0]; t=nmCollect([x[0],x[1]],0.3).find(y=>y.k==='v'); if(t) break; } return t?nmBuzzes(t):null; });
  ok('"Buzz for vanished places too" on: they buzz',v2===true);
  await c.close();
  // 3. hidden
  ({c,p}=await open({hideGone:true}));
  const h=await p.evaluate(()=>({n:+document.querySelector('#count').textContent.split(' ')[0],bad:window.__atlasNM.visible().filter(s=>s.st==='gone'||s.st==='marker').length,water:window.__atlasNM.visible().filter(s=>s.st==='water').length}));
  ok('"Hide places with nothing to see": none of them in the Places list, drowned places kept',h.bad===0&&h.water===pick.n.water&&h.n===pick.n.all-pick.n.gone-pick.n.marker,JSON.stringify(h));
  const pinned=await p.evaluate(id=>{ const {sites,nmFix,nmCollect,nmBuzzes,NM,XL,xlLoad,syncMarkers}=window.__atlasNM; const s=sites().find(x=>x.id===id); window.__atlasMap.setView([s.lat,s.lon],16,{animate:false}); syncMarkers(); let n=0; window.__atlasMap.eachLayer(l=>{ if(l.getLatLng&&l.options.riseOnHover&&l.getLatLng().distanceTo([s.lat,s.lon])<2) n++; }); return n; },pick.gone);
  ok('and no pin for them on the map',pinned===0,pinned+' pins');
  const nl=await p.evaluate(id=>{ const {sites,nmFix,nmCollect,nmBuzzes,NM,XL,xlLoad,syncMarkers}=window.__atlasNM; const s=sites().find(x=>x.id===id); return nmCollect([s.lat,s.lon],1).some(x=>x.id==='p:'+id); },pick.gone);
  ok('and none in the Near tab',!nl);
  await p.evaluate(()=>{ document.querySelector('#filt-btn').click(); }); await p.waitForTimeout(200);
  await p.evaluate(()=>{ [...document.querySelectorAll('#filters .chip')].find(b=>b.textContent.trim()==='Nothing visible').click(); }); await p.waitForTimeout(300);
  const ch=await p.evaluate(()=>({n:+document.querySelector('#count').textContent.split(' ')[0],gone:window.__atlasNM.visible().filter(s=>s.st==='gone').length}));
  ok('choosing "Nothing visible" in Filters still shows them',ch.gone===pick.n.gone&&ch.n===pick.n.gone,JSON.stringify(ch));
  // 3b. the list says how many it is hiding, a search for a hidden place says so, and a stop on the trip is not hidden
  await p.evaluate(()=>{ [...document.querySelectorAll('#filters .chip')].find(b=>b.textContent.trim()==='Nothing visible').click(); }); await p.waitForTimeout(300);      /* the chip off again */
  await p.evaluate(()=>{ const f=document.querySelector('#filters'); if(f&&f.open) document.querySelector('#filt-btn').click(); });
  const gname=await p.evaluate(id=>window.__atlasNM.sites().find(x=>x.id===id).name,pick.gone);
  await p.fill('#q',gname); await p.waitForTimeout(450);
  const srch=await p.evaluate(id=>({row:!!document.querySelector('#list li button[data-id="'+id+'"]'),note:(document.querySelector('#list .hidnote')||{}).textContent||''}),pick.gone);
  ok('searching for a hidden place by name: it is not listed, and the list says a place is hidden',!srch.row&&/with nothing to see (is|are) hidden/.test(srch.note),srch.note);
  await p.fill('#q',''); await p.waitForTimeout(450);
  await p.evaluate(()=>{ const m=document.querySelector('#list-more'); if(m) m.click(); }); await p.waitForTimeout(400);
  const note=await p.evaluate(()=>(document.querySelector('#list .hidnote')||{}).textContent||'');
  ok('the whole list ends by saying how many are hidden',note.indexOf((pick.n.gone+pick.n.marker)+' places with nothing to see are hidden')===0,note);
  ({c,p}=await (async()=>{ await c.close(); const c2=await b.newContext({viewport:{width:390,height:844},isMobile:true,hasTouch:true}); const p2=await c2.newPage(); p2.on('pageerror',e=>errs.push(e.message));
    await c2.route(u=>!/^http:\/\/localhost/.test(u.href),r=>r.fulfill({status:204,body:''}));
    await p2.addInitScript(id=>{ localStorage.setItem('lost-hidden-atlas-v1',JSON.stringify({v:1,home:{id:'alb',by:1},set:{hideGone:true},trip:[id]})); },pick.gone);
    await p2.goto(url); await p2.waitForFunction(()=>window.__atlasMap); await p2.waitForTimeout(400); return {c:c2,p:p2}; })());
  const tr=await p.evaluate(id=>{ const v=window.__atlasNM.visible(); return {in:v.some(s=>s.id===id),others:v.filter(s=>(s.st==='gone'||s.st==='marker')&&s.id!==id).length}; },pick.gone);
  ok('a stop on the trip stays on the map and in the list though it has nothing to see',tr.in&&tr.others===0,JSON.stringify(tr));
  await p.evaluate(()=>{ const m=document.querySelector('#list-more'); if(m) m.click(); }); await p.waitForTimeout(400);
  await p.click('#hid-show'); await p.waitForTimeout(400);
  const shown=await p.evaluate(()=>({n:window.__atlasNM.visible().filter(s=>s.st==='gone'||s.st==='marker').length,set:JSON.parse(localStorage.getItem('lost-hidden-atlas-v1')).set.hideGone,note:!!document.querySelector('#list .hidnote')}));
  ok('"Show them" switches the setting off and brings them back',shown.n===pick.n.gone+pick.n.marker&&shown.set===false&&!shown.note,JSON.stringify(shown));
  await p.evaluate(()=>window.__atlasNM.setPref('hideGone',true)); await p.waitForTimeout(300);
  // 4. settings
  await p.evaluate(()=>{ const f=document.querySelector('#filters'); if(f&&f.open) document.querySelector('#filt-btn').click(); }); await p.click('#lb-opt'); await p.waitForTimeout(250);
  await p.evaluate(()=>{ const g=[...document.querySelectorAll('#sheet button')].find(x=>/settings/i.test(x.getAttribute('aria-label')||x.textContent)); if(g) g.click(); }); await p.waitForTimeout(300);
  const rows=await p.evaluate(()=>['hideGone','quietGone','buzzVanished'].map(k=>{ const n=document.querySelector('#set-'+k); return n?k+'='+n.checked:k+' missing'; }));
  ok('the three settings are under the gear, as saved',rows.join()==='hideGone=true,quietGone=true,buzzVanished=false',rows.join(', '));
  await p.click('#set-hideGone'); await p.waitForTimeout(300);
  const back=await p.evaluate(()=>window.__atlasNM.visible().filter(s=>s.st==='gone'||s.st==='marker').length);
  ok('switching "Hide" off puts them back at once',back>0,back);
  await c.close();
  ok('no script errors',errs.length===0,errs.join(' | ').slice(0,200));
  await b.close(); console.log(fails.length?('\n'+fails.length+' FAILED'):'\nnothing-to-see test passed'); process.exit(fails.length?1:0);
})();
