// The Places tab's header: one row (search, Filters, Add), the filter panel, and the single drive time on a place.
//   node tools/places_test.js http://localhost:8766/index.html      (serve the built site first, as for smoke.js)
// Run it after changing the Places header in app.body.html, buildFilters(), the chips' styles, or "Getting there" in renderDetail().
// What it holds the app to: the list starts high on a phone; a filter that is switched on looks different from one that is
// off, in dark and light; the Filters button shows how many are on; the start place is chosen under the gear only.
// And the first visit: the map opens on the whole country, nothing is measured from a city the reader never chose, and a card
// asks where they start from (their location, a place they choose, or not now).
const { chromium } = require('playwright');
(async()=>{
  const fails=[]; const ok=(name,cond,extra)=>{ console.log((cond?'ok   ':'FAIL ')+name+(extra!==undefined?'  ['+extra+']':'')); if(!cond) fails.push(name); };
  const b=await chromium.launch(); const url=process.argv[2]||'http://localhost:8766/index.html';
  for(const [name,vp,dpr,mobile,scheme] of [['phone, dark',{width:390,height:844},2,true,'dark'],['desktop, dark',{width:1400,height:900},1,false,'dark'],['desktop, light',{width:1400,height:900},1,false,'light']]){
    const c=await b.newContext({viewport:vp,deviceScaleFactor:dpr,isMobile:mobile,hasTouch:mobile,colorScheme:scheme}); const p=await c.newPage(); const errs=[]; p.on('pageerror',e=>errs.push(e.message));
    await c.route(u=>!/^http:\/\/localhost/.test(u.href),r=>r.fulfill({status:204,body:''}));
    await p.addInitScript(()=>{ try{ if(!localStorage.getItem('lost-hidden-atlas-v1')) localStorage.setItem('lost-hidden-atlas-v1',JSON.stringify({v:1,home:{id:'alb',by:1}})); }catch(e){} });      // a reader with a start place; the first visit is tested further down
    await p.goto(url); await p.waitForFunction(()=>window.__atlasMap); await p.waitForTimeout(700);
    const vis=sel=>p.evaluate(sel=>{ const n=document.querySelector(sel); return !!n&&n.offsetParent!==null; },sel);
    const total=await p.evaluate(()=>+document.querySelector('#count').textContent.split(' ')[0]);
    if(mobile){ const g=await p.evaluate(()=>{ const t=document.querySelector('.tabs').getBoundingClientRect(), l=document.querySelector('#list li').getBoundingClientRect(); return Math.round(l.top-t.bottom); });
      ok(name+': the first place starts within 130 points of the tabs',g>0&&g<=130,g); }
    ok(name+': search, Filters and Add share one row',await p.evaluate(()=>{ const r=['#q','#filt-btn','#add-place'].map(s=>document.querySelector(s).getBoundingClientRect()); return Math.abs(r[0].top-r[1].top)<8&&Math.abs(r[1].top-r[2].top)<4&&r[0].right<=r[1].left+1&&r[1].right<=r[2].left+1&&r[2].right<=innerWidth; }));
    ok(name+': no start-city box and no shortcut chips above the list',!(await vis('#home'))&&!(await vis('#presets')));
    ok(name+': the filter panel is shut to begin with',!(await vis('#fbody')));
    await p.click('#filt-btn'); ok(name+': Filters opens the panel',await vis('#fbody')&&await p.evaluate(()=>document.querySelector('#filt-btn').getAttribute('aria-expanded')==='true'));
    ok(name+': the shortcuts are inside it',await vis('#presets')&&await p.evaluate(()=>document.querySelectorAll('#presets .chip').length>=4));
    const look=sel=>p.evaluate(sel=>{ const n=document.querySelector(sel), s=getComputedStyle(n); return s.backgroundColor+'|'+s.color+'|'+s.fontWeight; },sel);
    const chip='#fbody .fgrp:nth-child(2) .chip:nth-child(1)', off=await look(chip); await p.click(chip); await p.waitForTimeout(250); const on=await look(chip);
    const lum=c=>{ const m=c.match(/\d+(\.\d+)?/g).map(Number).slice(0,3).map(v=>{ v/=255; return v<=0.03928?v/12.92:Math.pow((v+0.055)/1.055,2.4); }); return 0.2126*m[0]+0.7152*m[1]+0.0722*m[2]; };
    const cr=(a,b)=>{ const x=lum(a),y=lum(b); return (Math.max(x,y)+0.05)/(Math.min(x,y)+0.05); };
    ok(name+': a switched-on filter is plainly different from one that is off',cr(on.split('|')[0],off.split('|')[0])>=3,'fill contrast '+cr(on.split('|')[0],off.split('|')[0]).toFixed(1));
    ok(name+': its label still reads on the new fill',cr(on.split('|')[0],on.split('|')[1])>=4.5,'text contrast '+cr(on.split('|')[0],on.split('|')[1]).toFixed(1));
    ok(name+': it carries a tick as well as the colour',await p.evaluate(sel=>getComputedStyle(document.querySelector(sel),'::before').content.length>2,chip));
    const n1=await p.evaluate(()=>+document.querySelector('#count').textContent.split(' ')[0]);
    ok(name+': the list is filtered and the button counts the filter',n1>0&&n1<total&&await p.evaluate(()=>document.querySelector('#fcount').textContent==='1'&&document.querySelector('#filt-btn').classList.contains('on')),n1+' of '+total);
    ok(name+': "Show N places" names the same number',await p.evaluate(n=>document.querySelector('#f-done').textContent==='Show '+n+' places',n1));
    await p.click('#f-done'); await p.waitForTimeout(200);
    ok(name+': it shuts the panel; the filter stays on and the button still says so',!(await vis('#fbody'))&&await p.evaluate(()=>document.querySelector('#filt-btn').classList.contains('on')));
    await p.fill('#q','mill'); await p.waitForTimeout(400); ok(name+': typing in the search box narrows the list and is not counted as a filter',await p.evaluate(n=>+document.querySelector('#count').textContent.split(' ')[0]<n&&document.querySelector('#fcount').textContent==='1',n1));
    await p.fill('#q',''); await p.waitForTimeout(400); await p.click('#filt-btn'); await p.click('#fbody .fdone .btn.sm'); await p.waitForTimeout(250);
    ok(name+': "Clear all filters" brings every place back',await p.evaluate(n=>+document.querySelector('#count').textContent.split(' ')[0]===n&&document.querySelector('#fcount').textContent===''&&!document.querySelector('#filt-btn').classList.contains('on'),total));
    await p.click('#filt-btn'); await p.click('#list li button'); await p.waitForTimeout(400);
    ok(name+': a place shows one drive time, from the start place',await p.evaluate(()=>document.querySelectorAll('.times .time').length===1&&/from /.test(document.querySelector('.times .time').textContent)));
    await p.click('#dt-change'); await p.waitForTimeout(350);
    ok(name+': "Change start place" opens Settings at the start place',await vis('#set-home'));
    await p.selectOption('#set-home','bost'); await p.waitForTimeout(400);
    ok(name+': choosing a start city there changes the drive time',await p.evaluate(()=>/from Boston/.test(document.querySelector('.times .time').textContent)));
    // the age filter: "Standing, from before 1800" lists standing places whose years begin before 1800, and no others
    { await p.evaluate(()=>{ const f=document.querySelector('#filters'); if(f&&!f.open) document.querySelector('#filt-btn').click(); }); await p.waitForTimeout(200);
      await p.evaluate(()=>{ [...document.querySelectorAll('#presets .chip')].find(b=>b.textContent==='Standing, from before 1800').click(); }); await p.waitForTimeout(300);
      const r=await p.evaluate(()=>{ const D=JSON.parse(document.getElementById('d-sites').textContent), by={}; D.sites.forEach(x=>{ by[x.id]=x; });
        const rows=[...document.querySelectorAll('#list li button[data-id]')].map(b=>by[b.dataset.id]); const yr=x=>{ const t=String(x.years), c=/(\d\d)(st|nd|rd|th) century/i.exec(t); return Math.min(...(t.match(/(1[5-9]\d\d)(?!\d)/g)||['9999']).map(Number),c?(+c[1]-1)*100:9999); };      /* "18th century" is 1700, as yearOf() reads it */
        return {n:+document.querySelector('#count').textContent.split(' ')[0],rows:rows.length,bad:rows.filter(x=>x.st!=='standing'||yr(x)>=1800).map(x=>x.id+' '+x.years),sel:document.querySelector('#f-before').value,
          razed:D.sites.filter(x=>/^razed/.test(x.years||'')).length}; });
      ok(name+': "Standing, from before 1800" lists standing places from before 1800 and no others',r.n>20&&r.rows>0&&r.bad.length===0&&r.sel==='1800',r.n+' listed; wrong: '+(r.bad.slice(0,3).join(', ')||'none')); }
    // the Red brick shortcut: only places marked yes or some, and the place page says so
    { const want=await p.evaluate(()=>JSON.parse(document.getElementById('d-sites').textContent).sites.filter(x=>x.bk==='y'||x.bk==='s').length);
      await p.evaluate(()=>{ const f=document.querySelector('#filters'); if(f&&!f.open) document.querySelector('#filt-btn').click(); }); await p.waitForTimeout(200);
      await p.evaluate(()=>{ [...document.querySelectorAll('#presets .chip')].find(b=>b.textContent==='Red brick').click(); }); await p.waitForTimeout(300);
      const got=await p.evaluate(()=>+document.querySelector('#count').textContent.split(' ')[0]);
      ok(name+': the Red brick shortcut lists the places marked as having it, and only those',want>20&&got===want,got+' listed, '+want+' marked');
      await p.evaluate(()=>{ const f=document.querySelector('#filters'); if(f&&f.open) document.querySelector('#filt-btn').click(); document.querySelector('#list li button').click(); }); await p.waitForTimeout(500);
      const sub=await p.evaluate(()=>(document.querySelector('#v-detail .sub2')||{}).textContent||'');
      ok(name+': a place page says Red brick or Some red brick',/red brick/i.test(sub),sub.slice(0,80)); }
    ok(name+': no script errors',errs.length===0,errs.join(' | ').slice(0,200)); await c.close(); }
  // ---- the first visit: nothing saved, no start place
  { const mk=async(geo,seed)=>{ const c=await b.newContext(Object.assign({viewport:{width:390,height:844},deviceScaleFactor:2,isMobile:true,hasTouch:true},geo?{geolocation:geo,permissions:['geolocation']}:{})); const p=await c.newPage(); const errs=[]; p.on('pageerror',e=>errs.push(e.message));
      await c.route(u=>!/^http:\/\/localhost/.test(u.href),r=>r.fulfill({status:204,body:''}));
      if(seed) await p.addInitScript(x=>{ try{ if(!localStorage.getItem('lost-hidden-atlas-v1')) localStorage.setItem('lost-hidden-atlas-v1',JSON.stringify(x)); }catch(e){} },seed);
      await p.goto(url); await p.waitForFunction(()=>window.__atlasMap); await p.waitForTimeout(800); return {c,p,errs}; };
    const state=p=>p.evaluate(()=>{ const m=window.__atlasMap, b=m.getBounds(), card=document.querySelector('#startcard'), li=document.querySelector('#list li');
      return {card:!!card&&card.offsetParent!==null,btns:card?[...card.querySelectorAll('button')].map(x=>x.textContent):[],mins:document.querySelectorAll('#list .mins').length,rows:document.querySelectorAll('#list .item').length,
        label:document.querySelector('#sort').options[0].textContent,zoom:m.getZoom(),coast:b.contains([47.6,-122.3])&&b.contains([25.8,-80.2])&&b.contains([44.6,-68.0]),home:document.querySelectorAll('.homepin').length,
        gap:Math.round(li.getBoundingClientRect().top-document.querySelector('.tabs').getBoundingClientRect().bottom),U:JSON.parse(localStorage.getItem('lost-hidden-atlas-v1')||'{}')}; });
    let A=await mk(), s=await state(A.p);
    ok('first visit: the map opens on the whole country, Seattle to Miami to Maine',s.coast&&s.zoom<=5,'zoom '+s.zoom);
    ok('first visit: a card asks where you start from, with three answers',s.card&&s.btns.join('|')==='Use my location|Choose a place|Not now',s.btns.join('|'));
    ok('first visit: no drive time is shown from a city nobody chose, and no start pin',s.rows>0&&s.mins===0&&s.home===0&&s.label==='Nearest first',s.mins+' times on '+s.rows+' rows; "'+s.label+'"');
    ok('first visit: with the card, the first place still starts within 250 points of the tabs',s.gap>0&&s.gap<=250,s.gap);
    await A.p.click('#list .item'); await A.p.waitForTimeout(400);
    ok('first visit: a place page shows no time from anywhere, and offers to set a start place',await A.p.evaluate(()=>document.querySelectorAll('.times .time').length===0&&/Set a start place/.test(document.querySelector('#dt-change').textContent)));
    ok('first visit: directions do not start from a city nobody chose',await A.p.evaluate(()=>{ const a=[...document.querySelectorAll('#v-detail a')].find(x=>/Directions/.test(x.textContent)); return !!a&&!/origin=/.test(a.href); }));
    await A.p.click('#tab-list'); await A.p.waitForTimeout(250); await A.p.click('#sc-pick'); await A.p.waitForTimeout(400);
    ok('"Choose a place" opens Settings at the start place, which reads "Not chosen yet"',await A.p.evaluate(()=>{ const n=document.querySelector('#set-home'); return !!n&&n.offsetParent!==null&&n.options[n.selectedIndex].textContent==='Not chosen yet'; }));
    await A.p.selectOption('#set-home','bost'); await A.p.waitForTimeout(500); await A.p.click('#sheet-x').catch(()=>{}); await A.p.waitForTimeout(250); s=await state(A.p);
    ok('choosing Boston: the card goes, times count from Boston, and the map goes there',!s.card&&s.mins>0&&s.label==='Nearest to Boston'&&s.home===1&&s.zoom>=9&&s.U.home.id==='bost'&&s.U.home.by===1,'"'+s.label+'", zoom '+s.zoom+', '+s.mins+' times');
    ok('first visit, a place chosen: no script errors',A.errs.length===0,A.errs.join(' | ').slice(0,200)); await A.c.close();
    A=await mk(); await A.p.click('#sc-no'); await A.p.waitForTimeout(300); s=await state(A.p);
    ok('"Not now": the card goes and still nothing is measured from anywhere',!s.card&&s.mins===0&&s.label==='Nearest first'&&s.gap<=130,'gap '+s.gap);
    await A.p.reload(); await A.p.waitForFunction(()=>window.__atlasMap); await A.p.waitForTimeout(600); s=await state(A.p);
    ok('"Not now" is remembered on the next visit',!s.card&&s.mins===0);
    ok('"Not now": no script errors',A.errs.length===0,A.errs.join(' | ').slice(0,200)); await A.c.close();
    A=await mk(null,{v:1,trip:['joliet-iron-works'],ui:{noStart:1}}); await A.p.click('#tab-trip'); await A.p.waitForTimeout(300);
    ok('a trip with no start place asks for one and does not plan from a city nobody chose',await A.p.evaluate(()=>{ const v=document.querySelector('#v-trip'); return !!v.querySelector('#startcard')&&!v.querySelector('#sc-no')&&!v.querySelector('#trip-day')&&!/Albany/.test(v.textContent); }));
    ok('a trip with no start place: no script errors',A.errs.length===0,A.errs.join(' | ').slice(0,200)); await A.c.close();
    A=await mk({latitude:39.0997,longitude:-94.5786,accuracy:15}); await A.p.click('#sc-me'); await A.p.waitForFunction(()=>document.querySelector('#sort').options[0].textContent==='Nearest to you',null,{timeout:9000}).catch(()=>{}); await A.p.waitForTimeout(400); s=await state(A.p);
    ok('"Use my location" (in Kansas City): the card goes and the list counts from where you are',!s.card&&s.mins>0&&s.label==='Nearest to you','"'+s.label+'", '+s.mins+' times');
    ok('and the nearest start city becomes the start place, with the map at town scale, not street scale',s.U.home.id==='kc'&&s.U.home.by===2&&s.zoom===10,(s.U.home.id||'')+' by '+s.U.home.by+', zoom '+s.zoom);
    await A.p.click('#lb-loc'); await A.p.waitForTimeout(500); s=await state(A.p);
    ok('location off again: the list counts from Kansas City, and no card',!s.card&&s.label==='Nearest to Kansas City'&&s.mins>0,'"'+s.label+'"');
    ok('"Use my location": no script errors',A.errs.length===0,A.errs.join(' | ').slice(0,200)); await A.c.close();
    /* somebody who was near Albany all along: the device says so, and Albany then counts as chosen */
    A=await mk({latitude:42.66,longitude:-73.78,accuracy:15}); await A.p.click('#sc-me'); await A.p.waitForFunction(()=>document.querySelector('#sort').options[0].textContent==='Nearest to you',null,{timeout:9000}).catch(()=>{}); await A.p.waitForTimeout(400); await A.p.click('#lb-loc'); await A.p.waitForTimeout(500); s=await state(A.p);
    ok('a reader whose device is near Albany: Albany becomes the start place by position, not by default',!s.card&&s.label==='Nearest to Albany'&&s.U.home.id==='alb'&&s.U.home.by===2&&s.home===1,'"'+s.label+'" by '+s.U.home.by);
    await A.c.close(); }
  // ---- "Nearest first" counts from where the reader is while location is on, otherwise from the start place
  { const c=await b.newContext({viewport:{width:390,height:844},deviceScaleFactor:2,isMobile:true,hasTouch:true,geolocation:{latitude:42.8864,longitude:-78.8784,accuracy:12},permissions:['geolocation']}); const p=await c.newPage(); const errs=[]; p.on('pageerror',e=>errs.push(e.message));
    await c.route(u=>!/^http:\/\/localhost/.test(u.href),r=>r.fulfill({status:204,body:''}));
    await p.addInitScript(()=>{ try{ localStorage.setItem('lost-hidden-atlas-v1',JSON.stringify({v:1,home:{id:'bost',by:1}})); }catch(e){} });
    await p.goto(url); await p.waitForFunction(()=>window.__atlasMap); await p.waitForTimeout(700);
    const top=()=>p.evaluate(()=>{ const li=document.querySelector('#list li'); return {label:document.querySelector('#sort').options[0].textContent,town:li.querySelector('small').textContent,mins:li.querySelector('.mins').textContent}; });
    let t=await top(); ok('location off: the list counts from the start place and says so',t.label==='Nearest to Boston'&&/Boston|Cambridge|Charlestown|Roxbury/.test(t.town),t.label+' | '+t.town);
    await p.click('#lb-loc'); await p.waitForFunction(()=>document.querySelector('#sort').options[0].textContent==='Nearest to you',null,{timeout:8000}).catch(()=>{});
    t=await top(); ok('location on (in Buffalo): the list counts from where you are',t.label==='Nearest to you'&&/Buffalo/.test(t.town)&&/^~/.test(t.mins),t.label+' | '+t.town+' | '+t.mins);
    await p.click('#list li button'); await p.waitForTimeout(400);
    ok('location on: a place shows the time from where you are first, then from the start place',await p.evaluate(()=>{ const n=[...document.querySelectorAll('.times .time')].map(x=>x.textContent); return n.length===2&&/from where you are/.test(n[0])&&/from Boston/.test(n[1]); }));
    ok('location on: directions start from the phone, not the start place',await p.evaluate(()=>{ const a=[...document.querySelectorAll('#v-detail a')].find(x=>/Directions/.test(x.textContent)); return !!a&&!/origin=/.test(a.href); }));
    await p.click('#lb-loc'); await p.waitForTimeout(500); await p.click('#tab-list'); await p.waitForTimeout(300);
    t=await top(); ok('location switched off again: back to the start place',t.label==='Nearest to Boston'&&!/Buffalo/.test(t.town),t.label+' | '+t.town);
    ok('location: no script errors',errs.length===0,errs.join(' | ').slice(0,200)); await c.close(); }
  await b.close(); console.log(fails.length?('\n'+fails.length+' FAILED'):'\nplaces header test passed'); process.exit(fails.length?1:0);
})();
