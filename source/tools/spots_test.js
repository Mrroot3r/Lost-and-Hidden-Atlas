// Placing a pin by hand, and Spots: many bare marks dropped quickly for somebody to research (app.js, "placing by hand" and "spots").
//   node tools/spots_test.js http://localhost:8766/index.html      (serve the built site first, as for smoke.js)
// Run it after changing the + Add bar, the crosshair, the form's movable pin, spot mode, the Spots card or how spots are exported,
// and after changing how tools/visits.py reads spots. A phone first (a tap must not drop a spot there), then a desktop.
const { chromium, devices } = require('playwright'); const fs=require('fs'), path=require('path'), cp=require('child_process');
(async()=>{
  const fails=[]; const ok=(name,cond,extra)=>{ console.log((cond?'ok   ':'FAIL ')+name+(extra!==undefined?'  ['+String(extra).slice(0,170)+']':'')); if(!cond) fails.push(name); };
  const url=(process.argv[2]||'http://localhost:8766/index.html'), ME=[42.7742,-73.7005];
  const b=await chromium.launch({proxy:{server:process.env.HTTPS_PROXY||'http://x',bypass:'localhost,127.0.0.1'}});
  const U=p=>p.evaluate(()=>JSON.parse(localStorage.getItem('lost-hidden-atlas-v1')||'{}'));
  const centre=p=>p.evaluate(()=>{ const c=window.__atlasMap.getCenter(); return [c.lat,c.lng]; });
  const near=(a,b,m)=>Math.hypot((a[0]-b[0])*111320,(a[1]-b[1])*111320*Math.cos(a[0]*Math.PI/180))<=m;
  const vis=(p,sel)=>p.evaluate(s=>{ const n=document.querySelector(s); return !!n&&!n.hidden&&n.getClientRects().length>0; },sel);

  /* ---------- a phone ---------- */
  const c=await b.newContext(Object.assign({},devices['Pixel 7'],{geolocation:{latitude:ME[0],longitude:ME[1],accuracy:5},permissions:['geolocation','clipboard-read','clipboard-write']}));
  const p=await c.newPage(); const errs=[]; p.on('pageerror',e=>errs.push(e.message));
  await p.goto(url); await p.waitForFunction(()=>window.__atlasMap); await p.waitForTimeout(900);
  await p.evaluate(()=>window.__atlasMap.setView([42.6526,-73.7573],17,{animate:false})); await p.waitForTimeout(400);
  ok('no crosshair until you ask to add something',!(await vis(p,'#aim')));
  await p.click('#add-place'); await p.waitForTimeout(250);
  ok('+ Add shows a crosshair',await vis(p,'#aim'));
  const mid=await p.evaluate(()=>{ const a=document.querySelector('#aim').getBoundingClientRect(), m=document.querySelector('#map').getBoundingClientRect(); return [Math.round(a.left+a.width/2-(m.left+m.width/2)),Math.round(a.top+a.height/2-(m.top+m.height/2))]; });
  ok('and the crosshair is at the middle of the map',Math.abs(mid[0])<=1&&Math.abs(mid[1])<=1,mid);
  ok('with a "Place here" button',await vis(p,'#add-centre'));
  const c0=await centre(p); await p.click('#add-centre'); await p.waitForTimeout(400);
  const at=await p.evaluate(()=>{ const t=document.querySelector('#f-at'); return t?t.textContent:''; });
  const got=(at.match(/-?\d+\.\d+/g)||[]).map(Number);
  ok('"Place here" opens the quick card at the middle of the map',/What is it/.test(await p.innerText('#v-detail'))&&got.length===2&&near(got,c0,2),at);
  // the quick card: one row of four taps, nothing to type (the owner, November 21, 2026: the full form was too much to look at while filming)
  const qa=await p.evaluate(()=>{ const b=[...document.querySelectorAll('#qa-what button')], r=b.map(x=>x.getBoundingClientRect()); return {t:b.map(x=>x.textContent.trim()),oneRow:r.length>0&&r.every(x=>Math.abs(x.top-r[0].top)<2),fits:r.every(x=>x.right<=innerWidth+1&&x.width>=44),inputs:document.querySelectorAll('#v-detail input, #v-detail select, #v-detail textarea').length,more:!!document.querySelector('#qa-more')}; });
  ok('it is one row of four choices, with nothing to type and a way to the full form',qa.t.join('|')==='Standing|Ruin|Trace|Odd find'&&qa.oneRow&&qa.fits&&qa.inputs===0&&qa.more,JSON.stringify(qa));
  const pv=await p.evaluate(()=>{ const f=document.querySelector('.formpin').getBoundingClientRect(), m=document.querySelector('#map').getBoundingClientRect(); return {dx:Math.round(f.left+f.width/2-(m.left+m.width/2)),dy:Math.round(f.top+f.height/2-(m.top+m.height/2)),h:Math.round(m.height)}; });
  ok('the pin is in the middle of the map that is still showing',Math.abs(pv.dx)<=20&&Math.abs(pv.dy)<=20&&pv.h>120,JSON.stringify(pv));
  ok('the crosshair goes away and a pin you can still drag stands on the spot',!(await vis(p,'#aim'))&&(await p.locator('.formpin').count())===1);
  await p.click('#v-detail button:has-text("Cancel")'); await p.waitForTimeout(250);
  ok('Cancel takes that pin off again',(await p.locator('.formpin').count())===0);
  // one tap saves
  await p.click('#add-place'); await p.waitForTimeout(250); const c1=await centre(p); await p.click('#add-centre'); await p.waitForTimeout(400);
  await p.click('#qa-what button[data-w="ruins"]'); await p.waitForTimeout(500);
  let cu1=((await U(p)).custom||[]).slice(-1)[0]||{};
  ok('a tap on Ruin saves the place there and then: a ruin, named so it can be told apart, no pin left over',cu1.st==='ruins'&&/^Unnamed ruin/.test(cu1.name||'')&&near([cu1.lat,cu1.lon],c1,2)&&(await p.locator('.formpin').count())===0&&!(await vis(p,'#qa-what')),JSON.stringify([cu1.name,cu1.st,cu1.cat]));
  await p.click('#add-place'); await p.waitForTimeout(250); await p.click('#add-centre'); await p.waitForTimeout(400);
  await p.click('#qa-what button[data-w="curio"]'); await p.waitForTimeout(500); cu1=((await U(p)).custom||[]).slice(-1)[0]||{};
  ok('Odd find saves it under the kind for curiosities and relics',cu1.cat==='curio'&&/^Odd find/.test(cu1.name||''),JSON.stringify([cu1.name,cu1.st,cu1.cat]));
  await p.evaluate(id=>{ location.hash='#'+id; },cu1.id); await p.waitForTimeout(500);
  ok('and its page names that kind',/Curiosities & relics/.test(await p.innerText('#v-detail')));
  await p.click('#tab-list'); await p.waitForTimeout(200); await p.click('#add-place'); await p.waitForTimeout(250); await p.click('#add-centre'); await p.waitForTimeout(400);
  await p.click('#qa-more'); await p.waitForTimeout(300);
  ok('"More details" opens the full form at the same spot, pin still there',await vis(p,'#f-name')&&(await p.locator('.formpin').count())===1&&/Add a place/.test(await p.innerText('#v-detail')));
  await p.click('#v-detail button:has-text("Cancel")'); await p.waitForTimeout(250);
  // the setting: the quick card can ask the kind, the year and the name as well
  await p.evaluate(()=>window.__atlasNM.setPref('addMore',true)); await p.click('#add-place'); await p.waitForTimeout(250); await p.click('#add-centre'); await p.waitForTimeout(400);
  const qm=await p.evaluate(()=>({kinds:[...document.querySelectorAll('#qa-kind button')].map(x=>x.textContent.trim()),year:!!document.querySelector('#qa-year'),yearPad:(document.querySelector('#qa-year')||{}).inputMode,name:!!document.querySelector('#qa-name')}));
  ok('with the setting on it also offers kinds to tap, a year on a number pad and a name',qm.kinds.length>=5&&qm.kinds.indexOf('Church')>=0&&qm.year&&qm.yearPad==='numeric'&&qm.name,JSON.stringify(qm));
  await p.click('#qa-kind button:has-text("Church")'); await p.fill('#qa-year','1890'); await p.click('#qa-what button[data-w="standing"]'); await p.waitForTimeout(500); cu1=((await U(p)).custom||[]).slice(-1)[0]||{};
  ok('Church, 1890, Standing: saved as a standing place of worship of 1890, named Unnamed church',cu1.cat==='worship'&&cu1.st==='standing'&&cu1.years==='1890'&&/^Unnamed church/.test(cu1.name||''),JSON.stringify([cu1.name,cu1.st,cu1.cat,cu1.years]));
  await p.evaluate(()=>window.__atlasNM.setPref('addMore',false));

  /* spots */
  await p.click('#add-place'); await p.waitForTimeout(200);
  ok('the bar offers "Spot many"',await vis(p,'#add-many'));
  await p.click('#add-many'); await p.waitForTimeout(250);
  ok('spot mode keeps the crosshair and counts from nothing',(await vis(p,'#aim'))&&/\b0 spots\b/.test(await p.innerText('#addbar')),await p.innerText('#addbar'));
  const s1=await centre(p); await p.click('#add-centre'); await p.waitForTimeout(200);
  await p.evaluate(()=>window.__atlasMap.panBy([120,-90],{animate:false})); await p.waitForTimeout(300);
  const s2=await centre(p); await p.click('#add-centre'); await p.waitForTimeout(200);
  let u=await U(p), sp=u.spots||[];
  ok('each press of Drop keeps a spot where the cross was, with no form',sp.length===2&&near([sp[0].lat,sp[0].lon],s1,2)&&near([sp[1].lat,sp[1].lon],s2,2)&&!(await vis(p,'#f-name')),JSON.stringify(sp).slice(0,120));
  ok('the bar counts them and the map shows them numbered',/\b2 spots\b/.test(await p.innerText('#addbar'))&&(await p.locator('.spotpin').count())===2&&(await p.locator('.spotpin').nth(1).innerText())==='2');
  const box=await p.locator('#map').boundingBox(); await p.touchscreen.tap(box.x+box.width*0.25,box.y+box.height*0.3); await p.waitForTimeout(300);
  ok('on a phone a tap on the map drops nothing: a slip of the thumb is not a spot',((await U(p)).spots||[]).length===2);
  await p.click('#spot-undo'); await p.waitForTimeout(200);
  ok('Undo takes the last one back',((await U(p)).spots||[]).length===1&&(await p.locator('.spotpin').count())===1);
  await p.click('#lb-loc'); await p.waitForFunction(()=>{ const n=document.querySelector('#add-here'); return n&&!n.hidden; },null,{timeout:9000}).catch(()=>{});
  await p.click('#add-here'); await p.waitForTimeout(300); u=await U(p); sp=u.spots||[];
  ok('"Where I am" drops one at the phone\'s position',sp.length===2&&near([sp[1].lat,sp[1].lon],ME,15),JSON.stringify(sp[1]||{}));
  await p.click('#add-cancel'); await p.waitForTimeout(300);
  ok('Done leaves spot mode and keeps the spots',!(await vis(p,'#aim'))&&!(await vis(p,'#addbar'))&&((await U(p)).spots||[]).length===2);
  await p.click('#tab-list'); await p.waitForTimeout(300);
  const card=await p.innerText('#spotcard').catch(()=>'');
  ok('the Places tab says how many spots wait and offers to copy or clear them',/2 spots/.test(card)&&(await vis(p,'#spots-copy'))&&(await vis(p,'#spots-clear')),card.replace(/\n/g,' / '));
  await p.evaluate(()=>window.__spotOpen(0)); await p.waitForTimeout(250);
  await p.fill('#spot-note','brick warehouse, arched windows'); await p.click('#spot-save'); await p.waitForTimeout(200);
  ok('a spot can be given a few words, and does not need them',((await U(p)).spots||[])[0].note==='brick warehouse, arched windows'&&!((await U(p)).spots||[])[1].note);
  // spots can go to the public Atlas through the form, like a place, so anybody can send them (the owner, November 21, 2026)
  const send=await p.evaluate(()=>[...document.querySelectorAll('#spotcard a.spots-send')].map(x=>x.href));
  const sq=send.length?new URL(send[0]).searchParams:null, body=sq?[...sq.values()].find(v=>/^1\. -?\d+\.\d+, -?\d+\.\d+/.test(v))||'':'';
  ok('the card has one link that sends both spots through the form, a numbered line each with its note',send.length===1&&/docs\.google\.com\/forms/.test(send[0])&&body.split('\n').length===2&&/brick warehouse, arched windows/.test(body)&&[...sq.values()].some(v=>/^Spots: 2/.test(v)),body.replace(/\n/g,' / ').slice(0,140));
  await p.click('#spots-copy'); await p.waitForTimeout(300);
  const clip=await p.evaluate(()=>navigator.clipboard.readText()).catch(()=>'');
  let J=null; try{ J=JSON.parse(clip); }catch(e){}
  ok('"Copy for Claude" puts the spots on the clipboard as data',!!J&&Array.isArray(J.spots)&&J.spots.length===2&&typeof J.spots[0].lat==='number'&&J.spots[0].note==='brick warehouse, arched windows',clip.slice(0,120));
  if(J){ const f=path.join(require('os').tmpdir(),'spots_'+Date.now()+'.json'); fs.writeFileSync(f,JSON.stringify(J));
    const r=cp.spawnSync('python3',[path.join(__dirname,'visits.py'),f],{encoding:'utf8'}); const out=(r.stdout||'')+(r.stderr||'');
    ok('tools/visits.py reads them and prints each as a lead to research first, as a LEADS.md row',/SPOTS/.test(out)&&(out.match(/^\| Spot /gm)||[]).length===2&&/brick warehouse/.test(out)&&/42\.\d+, -73\.\d+/.test(out),out.slice(0,300).replace(/\n/g,' / ')); }
  await p.reload(); await p.waitForFunction(()=>window.__atlasMap); await p.waitForTimeout(900);
  ok('the spots are still there, and on the map, after the page is opened again',((await U(p)).spots||[]).length===2&&(await p.locator('.spotpin').count())>=1);
  await p.click('#tab-list'); await p.waitForTimeout(200); await p.click('#spots-clear'); await p.waitForTimeout(150); await p.click('#spots-clear'); await p.waitForTimeout(300);
  ok('Clear asks twice, then empties them and takes the card away',((await U(p)).spots||[]).length===0&&(await p.locator('.spotpin').count())===0&&!(await vis(p,'#spotcard')));
  // ---- a long press on the map: a short box that fits the map on a phone, the other maps folded away (the owner, November 21, 2026)
  await p.click('#tab-list'); await p.waitForTimeout(200);
  await p.evaluate(()=>{ const m=window.__atlasMap; m.closePopup(); m.fire('contextmenu',{latlng:m.getCenter()}); }); await p.waitForTimeout(500);
  const cx2=await p.evaluate(()=>{ const pop=document.querySelector('.leaflet-popup'), m=document.querySelector('#map').getBoundingClientRect(), r=pop.getBoundingClientRect(), d=pop.querySelector('details');
    const vis=t=>[...pop.querySelectorAll('a,button')].some(b=>b.textContent.trim()===t&&b.offsetParent!==null&&b.getBoundingClientRect().height>0&&!(d&&d.contains(b)&&!d.open));
    return {fits:r.top>=m.top-1&&r.bottom<=m.bottom+1,h:Math.round(r.height),mh:Math.round(m.height),add:vis('+ Add to my places'),send:vis('Send this spot to the public Atlas'),gm:vis('Google Maps'),folded:!!d&&!d.open&&[...d.querySelectorAll('a')].some(a=>a.textContent.trim()==='Google Maps')}; });
  ok('a long press opens a box that fits inside the map, with Add and Send showing and the other maps folded away',cx2.fits&&cx2.add&&cx2.send&&!cx2.gm&&cx2.folded,JSON.stringify(cx2));
  await p.evaluate(()=>window.__atlasMap.closePopup());
  // ---- a place of your own: the button that sends it to the public Atlas is at the top of its page
  const mineId=await p.evaluate(()=>{ const u=JSON.parse(localStorage.getItem('lost-hidden-atlas-v1')); return (u.custom||[]).slice(-1)[0].id; });
  await p.evaluate(id=>{ location.hash='#'+id; },mineId); await p.waitForTimeout(500);
  const ls=await p.evaluate(()=>{ const b=document.querySelector('#lead-send'), v=document.querySelector('#v-detail'), n=document.querySelectorAll('#lead-send').length; if(!b) return null; return {top:Math.round(b.getBoundingClientRect().top-v.getBoundingClientRect().top+v.scrollTop),n:n,t:b.textContent.trim()}; });
  ok('its page has one "Send to the public Atlas" button, near the top',!!ls&&ls.n===1&&ls.top<260&&/Send to the public Atlas/.test(ls.t),JSON.stringify(ls));
  await p.click('#lead-send'); await p.waitForTimeout(300);
  ok('which opens the three ways to send it',(await p.locator('.sharebox .share-form').count())===1);
  // ---- no two pins for one place: once the public Atlas has a reader's place, the reader's own copy of it steps aside
  const tw=await p.evaluate(()=>{ const N=window.__atlasNM, t=N.sites().find(x=>x.tip&&!x.mine); if(!t) return null;
    N.addMine({id:'my-twin1',mine:true,name:'My copy of it',name2:'',town:'',years:'',reg:'',cat:'landmark',st:'standing',prec:'exact',acc:'view',eff:'walk',conf:'lead',lat:t.lat+0.0002,lon:t.lon,tags:[],story:'',look:'',hook:'',accn:'',links:[],now:false}); return {id:t.id,lat:t.lat,lon:t.lon}; });
  ok('the Atlas has a place sent in by a reader to try this on',!!tw);
  if(tw){ await p.waitForTimeout(500);
    let t2=await p.evaluate(()=>({listed:window.__atlasNM.sites().some(x=>x.id==='my-twin1'),kept:window.__atlasNM.custom().some(x=>x.id==='my-twin1')}));
    ok('my own copy, 22 m from it, is no longer on the map or in the list, but is still kept',!t2.listed&&t2.kept,JSON.stringify(t2));
    await p.evaluate(id=>{ location.hash='#'+id; },tw.id); await p.waitForTimeout(500);
    ok('the public place says so and offers to show my copy again',/My copy of it/.test(await p.innerText('#twin-note'))&&(await p.locator('#twin-show').count())===1,(await p.locator('#twin-note').count())?(await p.innerText('#twin-note')).slice(0,140):'no note');
    await p.click('#twin-show'); await p.waitForTimeout(400); t2=await p.evaluate(()=>window.__atlasNM.sites().some(x=>x.id==='my-twin1'));
    ok('"Show my copy" brings it back',t2===true); }
  ok('no script errors on the phone',errs.length===0,errs.join(' | '));
  await c.close();

  /* ---------- a desktop: a click places, and the pin can be dragged before saving ---------- */
  const d=await b.newContext({viewport:{width:1280,height:800}}); const q=await d.newPage(); const errs2=[]; q.on('pageerror',e=>errs2.push(e.message));
  await q.goto(url); await q.waitForFunction(()=>window.__atlasMap); await q.waitForTimeout(900);
  await q.evaluate(()=>window.__atlasMap.setView([42.6526,-73.7573],17,{animate:false})); await q.waitForTimeout(500);
  await q.click('#add-place'); await q.waitForTimeout(200); await q.click('#add-many'); await q.waitForTimeout(200);
  const mb=await q.locator('#map').boundingBox(); const cx=mb.x+mb.width*0.3, cy=mb.y+mb.height*0.4;
  const want=await q.evaluate(([x,y])=>{ const m=window.__atlasMap, r=m.getContainer().getBoundingClientRect(), ll=m.containerPointToLatLng([x-r.left,y-r.top]); return [ll.lat,ll.lng]; },[cx,cy]);
  await q.mouse.click(cx,cy); await q.waitForTimeout(300);
  let s=((await U(q)).spots||[]);
  ok('on a desktop a click on the map drops a spot where you clicked',s.length===1&&near([s[0].lat,s[0].lon],want,3),JSON.stringify(s));
  await q.click('#add-cancel'); await q.waitForTimeout(200);
  await q.click('#add-place'); await q.waitForTimeout(200); await q.mouse.click(mb.x+mb.width*0.6,mb.y+mb.height*0.5); await q.waitForTimeout(400);
  const before=await q.evaluate(()=>document.querySelector('#f-at').textContent);
  const pin=await q.locator('.formpin').boundingBox();
  await q.mouse.move(pin.x+pin.width/2,pin.y+pin.height/2); await q.mouse.down(); await q.mouse.move(pin.x+pin.width/2+40,pin.y+pin.height/2+30,{steps:6}); await q.mouse.up(); await q.waitForTimeout(400);
  const after=await q.evaluate(()=>document.querySelector('#f-at').textContent);
  ok('a click places a single pin too, and dragging that pin changes where the place will be saved',/\d/.test(before)&&before!==after,before+' -> '+after);
  await q.click('#qa-more'); await q.waitForTimeout(300); await q.fill('#f-name','Test place'); await q.click('#v-detail button[type=submit]'); await q.waitForTimeout(400);
  const cu=((await U(q)).custom||[]).slice(-1)[0]||{}, av=(after.match(/-?\d+\.\d+/g)||[]).map(Number);
  ok('the place is saved where the pin was dragged to, and the loose pin is gone',av.length===2&&near([cu.lat,cu.lon],av,2)&&(await q.locator('.formpin').count())===0,JSON.stringify([cu.lat,cu.lon])+' '+after);
  ok('no script errors on the desktop',errs2.length===0,errs2.join(' | '));
  await b.close();
  console.log(fails.length?fails.length+' FAILED':'spots test passed'); process.exit(fails.length?1:0);
})();
