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
  ok('"Place here" opens the form at the middle of the map',/Add a place/.test(await p.innerText('#v-detail'))&&got.length===2&&near(got,c0,2),at);
  ok('the crosshair goes away and a pin you can still drag stands on the spot',!(await vis(p,'#aim'))&&(await p.locator('.formpin').count())===1);
  await p.click('#v-detail button:has-text("Cancel")'); await p.waitForTimeout(250);
  ok('Cancel takes that pin off again',(await p.locator('.formpin').count())===0);

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
  await q.fill('#f-name','Test place'); await q.click('#v-detail button[type=submit]'); await q.waitForTimeout(400);
  const cu=((await U(q)).custom||[]).slice(-1)[0]||{}, av=(after.match(/-?\d+\.\d+/g)||[]).map(Number);
  ok('the place is saved where the pin was dragged to, and the loose pin is gone',av.length===2&&near([cu.lat,cu.lon],av,2)&&(await q.locator('.formpin').count())===0,JSON.stringify([cu.lat,cu.lon])+' '+after);
  ok('no script errors on the desktop',errs2.length===0,errs2.join(' | '));
  await b.close();
  console.log(fails.length?fails.length+' FAILED':'spots test passed'); process.exit(fails.length?1:0);
})();
