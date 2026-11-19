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
    // standing places are stars on the map and in the list; the layer bar ends in an arrow, not a cut-off button
    { const r=await p.evaluate(()=>{ const D=JSON.parse(document.getElementById('d-sites').textContent).sites, by={}; D.forEach(x=>{ by[x.id]=x; });
        const pins=[...document.querySelectorAll('.leaflet-marker-pane .pin')], st=pins.filter(n=>n.classList.contains('sq')), bad=st.filter(n=>n.tagName.toLowerCase()!=='svg').length;
        const rows=[...document.querySelectorAll('#list li button[data-id]')].slice(0,40), wrong=rows.filter(b=>(by[b.dataset.id]||{}).st==='standing'&&!b.querySelector('.dot.star')).length;
        const mo=document.querySelector('#lbar .lmore'), sc=document.querySelector('#lscroll');
        return {stars:st.length,bad,wrong,arrow:!!mo&&!mo.hidden,more:sc.scrollWidth>sc.clientWidth+4}; });
      ok(name+': standing places are stars on the map and in the list',r.bad===0&&r.wrong===0,r.stars+' stars on the map');
      if(r.more) ok(name+': the layer bar shows an arrow where more layers are off the edge',r.arrow);
      if(r.more){ await p.evaluate(()=>{ const sc=document.querySelector('#lscroll'); sc.scrollLeft=sc.scrollWidth; }); await p.waitForTimeout(250);
        ok(name+': and the arrow goes once the bar is scrolled to its end',await p.evaluate(()=>document.querySelector('#lbar .lmore').hidden));
        await p.evaluate(()=>{ document.querySelector('#lscroll').scrollLeft=0; }); } }
    // the arrow is worked out again when the window changes size (a phone turned on its side, a desktop window dragged wider)
    { const vp=p.viewportSize(); await p.evaluate(()=>{ document.querySelector('#lscroll').scrollLeft=0; }); await p.setViewportSize({width:1500,height:800}); await p.waitForTimeout(500);
      const w=await p.evaluate(()=>{ const mo=document.querySelector('#lbar .lmore'), sc=document.querySelector('#lscroll'); return {hidden:mo.hidden,more:sc.scrollWidth>sc.clientWidth+4}; });
      ok(name+': widened until every layer fits, the arrow goes',w.more||w.hidden,JSON.stringify(w));
      await p.setViewportSize(vp); await p.waitForTimeout(500);
      const n=await p.evaluate(()=>{ const mo=document.querySelector('#lbar .lmore'), sc=document.querySelector('#lscroll'); return {hidden:mo.hidden,more:sc.scrollWidth>sc.clientWidth+4}; });
      ok(name+': narrowed again, it is back',!n.more||!n.hidden,JSON.stringify(n)); }
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
  // ---- places that began as a reader's tip: a filter, a badge with the day, a word in the list, and no name anywhere
  { const c=await b.newContext({viewport:{width:390,height:844},isMobile:true,hasTouch:true}); const p=await c.newPage(); const errs=[]; p.on('pageerror',e=>errs.push(e.message));
    await p.addInitScript(()=>{ localStorage.setItem('lost-hidden-atlas-v1',JSON.stringify({v:1,home:{id:'alb',by:1}})); });
    await p.goto(url); await p.waitForFunction(()=>window.__atlasNM); await p.waitForTimeout(400);
    const tips=await p.evaluate(()=>JSON.parse(document.getElementById('d-sites').textContent).sites.filter(x=>x.tip).map(x=>[x.id,x.tip]));
    ok('some places carry the day a reader sent them in',tips.length>=2&&tips.every(t=>/^20\d\d-\d\d-\d\d$/.test(t[1])),tips.length+' places');
    await p.evaluate(()=>{ const f=document.querySelector('#filters'); if(f&&!f.open) document.querySelector('#filt-btn').click(); }); await p.waitForTimeout(200);
    await p.evaluate(()=>{ [...document.querySelectorAll('#filters .chip')].find(x=>x.textContent.trim()==='Sent in by readers').click(); }); await p.waitForTimeout(350);
    const r=await p.evaluate(()=>({n:+document.querySelector('#count').textContent.split(' ')[0],vis:window.__atlasNM.visible().map(s=>s.id).sort().join(),fc:(document.querySelector('#fcount')||{}).textContent||''}));
    ok('"Sent in by readers" in Filters lists those places and no others, and counts as one filter',r.n===tips.length&&r.vis===tips.map(t=>t[0]).sort().join()&&/1/.test(r.fc),r.n+' listed; filters on: '+r.fc);
    await p.evaluate(()=>{ const f=document.querySelector('#filters'); if(f&&f.open) document.querySelector('#filt-btn').click(); }); await p.waitForTimeout(200);
    ok('the list says "from a reader" on each',await p.evaluate(()=>[...document.querySelectorAll('#list li button[data-id]')].every(x=>/from a reader/.test(x.textContent))));
    await p.evaluate(id=>{ location.hash='#'+id; },tips[0][0]); await p.waitForTimeout(600);
    const bd=await p.evaluate(()=>{ const t=document.querySelector('#v-detail .tag.tipd'); return t?{text:t.textContent,title:t.getAttribute('title')}:null; });
    ok('its page carries the badge "Sent in by a reader", with the day in words',!!bd&&bd.text==='Sent in by a reader'&&/ on [A-Z][a-z]+ \d{1,2}, 20\d\d\./.test(bd.title),bd&&bd.title.slice(0,70));
    const other=await p.evaluate(()=>{ const s=window.__atlasNM.sites().find(x=>!x.tip&&!x.mine); location.hash='#'+s.id; return s.id; }); await p.waitForTimeout(600);
    ok('a place a session found has no such badge',await p.evaluate(()=>!document.querySelector('#v-detail .tag.tipd')),other);
    ok('reader tips: no script errors',errs.length===0,errs.join(' | ').slice(0,200)); await c.close(); }
  // ---- Favourites: the reader's own short list. A favourite is marked on its page, wears a ring on the map, is listed by one
  //      filter, is kept when the page is opened again, and is never folded into a grey group disc however far out the map is.
  { const c=await b.newContext({viewport:{width:390,height:844},isMobile:true,hasTouch:true}); const p=await c.newPage(); const errs=[]; p.on('pageerror',e=>errs.push(e.message));
    await c.route(u=>!/^http:\/\/localhost/.test(u.href),r=>r.fulfill({status:204,body:''}));
    await p.addInitScript(()=>{ try{ if(!localStorage.getItem('lost-hidden-atlas-v1')) localStorage.setItem('lost-hidden-atlas-v1',JSON.stringify({v:1,home:{id:'alb',by:1}})); }catch(e){} });
    await p.goto(url); await p.waitForFunction(()=>window.__atlasNM); await p.waitForTimeout(500);
    // two places in the thick of Albany, where pins are grouped when the map is zoomed out
    const two=await p.evaluate(()=>window.__atlasNM.sites().filter(s=>!s.mine&&s.st==='standing'&&Math.abs(s.lat-42.652)<0.012&&Math.abs(s.lon+73.755)<0.012).slice(0,2).map(s=>({id:s.id,lat:s.lat,lon:s.lon})));
    ok('two places in downtown Albany to try',two.length===2,two.map(x=>x.id).join());
    const seen=async()=>{ await p.waitForTimeout(700); return p.evaluate(ids=>{ const NM=window.__atlasNM, m=window.__atlasMap, on=[]; m.eachLayer(l=>{ if(l.getLatLng&&l.options&&l.options.icon&&l._icon){ const n=l._icon.querySelector('.pin'); if(n) on.push({fav:n.classList.contains('fav'),la:l.getLatLng().lat,lo:l.getLatLng().lng}); } });
        const hit=x=>on.find(o=>Math.abs(o.la-x.lat)<1e-5&&Math.abs(o.lo-x.lon)<1e-5); return {a:hit(ids[0])||null,b:hit(ids[1])||null,discs:document.querySelectorAll('.clus').length,favs:on.filter(o=>o.fav).length,zoom:m.getZoom()}; },two); };
    await p.evaluate(x=>window.__atlasMap.setView([x.lat,x.lon],9,{animate:false}),two[0]); let v=await seen();
    ok('zoomed out, neither has a pin of its own: both are inside a group disc',!v.a&&!v.b&&v.discs>0,JSON.stringify(v));
    await p.evaluate(id=>{ location.hash='#'+id; },two[0].id); await p.waitForTimeout(600);
    const btn=()=>p.evaluate(()=>{ const n=document.querySelector('#d-fav'); return n?{t:n.textContent,p:n.getAttribute('aria-pressed'),l:n.getAttribute('aria-label'),row:Math.abs(n.getBoundingClientRect().top-document.querySelector('.dtop .btn').getBoundingClientRect().top)<6,fits:n.getBoundingClientRect().right<=innerWidth&&document.querySelector('.dtop').scrollWidth<=document.querySelector('.dtop').clientWidth+1}:null; });
    let bt=await btn(); ok('a place page has a favourite button in its top row, empty heart, and the row still fits a phone',!!bt&&bt.t==='♡'&&bt.p==='false'&&bt.l==='Add to my favourites'&&bt.row&&bt.fits,JSON.stringify(bt));
    await p.click('#d-fav'); await p.waitForTimeout(500); bt=await btn();
    ok('tapped, it is a full heart and says how to undo it',!!bt&&bt.t==='♥'&&bt.p==='true'&&bt.l==='Remove from my favourites',JSON.stringify(bt));
    await p.click('.dtop .btn'); await p.waitForTimeout(400);     // Back
    await p.evaluate(x=>window.__atlasMap.setView([x.lat,x.lon],9,{animate:false}),two[0]); v=await seen();
    ok('zoomed out again, the favourite has its own pin, ringed; its neighbour is still in the disc',!!v.a&&v.a.fav&&!v.b&&v.discs>0&&v.favs===1,JSON.stringify(v));
    await p.evaluate(x=>window.__atlasMap.setView([x.lat,x.lon],5,{animate:false}),two[0]); v=await seen();
    ok('and at the scale of half a continent it is still there',!!v.a&&v.a.fav,'zoom '+v.zoom);
    await p.evaluate(()=>{ const f=document.querySelector('#filters'); if(f&&!f.open) document.querySelector('#filt-btn').click(); }); await p.waitForTimeout(250);
    ok('Filters has "My favourites" among the shortcuts and under Only show',await p.evaluate(()=>[...document.querySelectorAll('#presets .chip')].some(x=>x.textContent.trim()==='My favourites')&&[...document.querySelectorAll('#fbody .fgrp .chip')].some(x=>x.textContent.trim()==='My favourites')));
    await p.evaluate(()=>{ [...document.querySelectorAll('#fbody .fgrp .chip')].find(x=>x.textContent.trim()==='My favourites').click(); }); await p.waitForTimeout(400);
    let r=await p.evaluate(()=>({ids:window.__atlasNM.visible().map(s=>s.id).join(),fc:(document.querySelector('#fcount')||{}).textContent||'',row:(document.querySelector('#list li')||{}).textContent||''}));
    ok('it lists the favourite and nothing else, counts as one filter, and the row says so',r.ids===two[0].id&&r.fc==='1'&&/favourite/.test(r.row),r.ids+' | '+r.fc);
    await p.evaluate(()=>{ [...document.querySelectorAll('#fbody .fgrp .chip')].find(x=>x.textContent.trim()==='My favourites').click(); const f=document.querySelector('#filters'); if(f&&f.open) document.querySelector('#filt-btn').click(); }); await p.waitForTimeout(300);
    await p.reload(); await p.waitForFunction(()=>window.__atlasNM); await p.waitForTimeout(600);
    await p.evaluate(x=>window.__atlasMap.setView([x.lat,x.lon],9,{animate:false}),two[0]); v=await seen();
    ok('the page opened again: it is still a favourite, still on the map zoomed out',!!v.a&&v.a.fav&&await p.evaluate(id=>JSON.parse(localStorage.getItem('lost-hidden-atlas-v1')).fav.join()===id,two[0].id));
    await p.evaluate(id=>{ location.hash='#'+id; },two[0].id); await p.waitForTimeout(600); await p.click('#d-fav'); await p.waitForTimeout(500); await p.click('.dtop .btn'); await p.waitForTimeout(300);
    await p.evaluate(x=>window.__atlasMap.setView([x.lat,x.lon],9,{animate:false}),two[0]); v=await seen();
    ok('taken off the list, it goes back into the disc',(!v.a||!v.a.fav)&&v.favs===0&&await p.evaluate(()=>JSON.parse(localStorage.getItem('lost-hidden-atlas-v1')).fav.length===0),JSON.stringify(v));
    ok('favourites: no script errors',errs.length===0,errs.join(' | ').slice(0,200)); await c.close(); }
  // ---- Access "Open to visitors", and the Hours row under it (November 2026): a museum, an inn or a church that opens is not
  //      "Public land or street"; the page says the hours research read and how old they are, and links to today's.
  { const c=await b.newContext({viewport:{width:390,height:844},isMobile:true,hasTouch:true}); const p=await c.newPage(); const errs=[]; p.on('pageerror',e=>errs.push(e.message));
    await c.route(u=>!/^http:\/\/localhost/.test(u.href),r=>r.fulfill({status:204,body:''}));
    await p.addInitScript(()=>{ localStorage.setItem('lost-hidden-atlas-v1',JSON.stringify({v:1,home:{id:'alb',by:1}})); });
    await p.goto(url); await p.waitForFunction(()=>window.__atlasNM); await p.waitForTimeout(400);
    const S=await p.evaluate(()=>JSON.parse(document.getElementById('d-sites').textContent).sites.map(x=>({id:x.id,name:x.name,acc:x.acc,cat:x.cat,st:x.st,hrs:x.hrs||'',nw:x.new||''})));
    const open=S.filter(x=>x.acc==='open');
    ok('several hundred places are "Open to visitors"',open.length>=300,open.length);
    ok('the old landmark pins that are museums or theatres are among them',['lm-schuyler-mansion','lm-proctors','lm-olana'].every(i=>!S.find(x=>x.id===i)||S.find(x=>x.id===i).acc==='open'));
    await p.evaluate(()=>{ const f=document.querySelector('#filters'); if(f&&!f.open) document.querySelector('#filt-btn').click(); }); await p.waitForTimeout(200);
    const chips=await p.evaluate(()=>{ const g=[...document.querySelectorAll('#fbody .fgrp')].find(x=>/^Access/.test(x.textContent.trim())); return g?[...g.querySelectorAll('.chip')].map(x=>x.textContent.trim()):[]; });
    ok('Filters, Access: "Open to visitors" comes second, after public land',chips[0]==='Public land or street'&&chips[1]==='Open to visitors, check hours'&&chips.length===6,chips.join(' | '));
    await p.evaluate(()=>{ [...document.querySelectorAll('#fbody .chip')].find(x=>x.textContent.trim()==='Open to visitors, check hours').click(); }); await p.waitForTimeout(350);
    const v=await p.evaluate(()=>window.__atlasNM.visible().map(s=>s.acc));
    ok('that filter lists the open-to-visitors places and no others',v.length>=open.length-8&&v.length<=open.length&&v.every(a=>a==='open'),v.length+' of '+open.length);
    await p.evaluate(()=>{ [...document.querySelectorAll('#fbody .chip')].find(x=>x.textContent.trim()==='Open to visitors, check hours').click(); const f=document.querySelector('#filters'); if(f&&f.open) document.querySelector('#filt-btn').click(); }); await p.waitForTimeout(250);
    const row=async id=>{ await p.evaluate(id=>{ location.hash='#'+id; },id); await p.waitForTimeout(550);
      return p.evaluate(()=>{ const kv=document.querySelector('#v-detail dl.kv'), dts=[...kv.querySelectorAll('dt')], g=t=>{ const d=dts.find(x=>x.textContent===t); return d?d.nextElementSibling:null; }, h=g('Hours'), a=h&&h.querySelector('a');
        return {acc:(g('Access')||{}).textContent,order:dts.map(x=>x.textContent).join(),has:!!h,txt:h?((h.querySelector('span')||{}).textContent||''):'',when:h?((h.querySelector('small')||{}).textContent||''):'',link:a?a.textContent:'',href:a?a.href:'',target:a?a.target:'',fits:h?h.getBoundingClientRect().right<=innerWidth:true}; }); };
    const noh=open.find(x=>!x.hrs&&x.st==='standing'); let r=await row(noh.id);
    ok('an open-to-visitors place says so beside Access',r.acc==='Open to visitors, check hours',noh.id+': '+r.acc);
    ok('Hours comes straight after Access',/^Access,Hours,/.test(r.order),r.order);
    ok('with no hours on record it offers a look-up of today’s by the place’s name, in a new tab',r.has&&r.txt===''&&r.link==='Today’s hours in Google Maps'&&r.href.indexOf('https://www.google.com/maps/search/?api=1&query='+encodeURIComponent(noh.name))===0&&r.target==='_blank',r.link+' | '+r.href.slice(0,110));
    const wh=S.find(x=>x.hrs&&x.nw);
    if(!wh) ok('some place has its hours on record',false);
    else { r=await row(wh.id);
      ok('a place with hours on record shows them, word for word',r.has&&r.txt===wh.hrs,wh.id+': '+r.txt.slice(0,80));
      ok('and says which month they were read, since hours change',/^As read [A-Z][a-z]+ 20\d\d\.$/.test(r.when),r.when);
      ok('and still links to today’s',r.link==='Today’s hours in Google Maps'&&r.fits,r.link); }
    { const lk=await p.evaluate(()=>{ const s=JSON.parse(document.getElementById('d-sites').textContent).sites.find(x=>x.hrs&&x.hrd&&x.hru); return s?{id:s.id,hrd:s.hrd,hru:s.hru}:null; });
      if(lk){ await p.evaluate(id=>{ location.hash='#'+id; },lk.id); await p.waitForTimeout(550);
        const g=await p.evaluate(()=>{ const h=[...document.querySelectorAll('#v-detail dl.kv dt')].find(x=>x.textContent==='Hours').nextElementSibling, a=h.querySelector('a.hsrc'); return {when:h.querySelector('small').textContent,src:a?a.href:'',txt:a?a.textContent:''}; });
        const mon=new Date(+lk.hrd.slice(0,4),+lk.hrd.slice(5,7)-1,1).toLocaleDateString('en-US',{month:'long',year:'numeric'});
        ok('hours looked up later carry their own month and a link to the page they were read on',g.when==='As read '+mon+', '&&g.src.replace(/\/$/,'')===lk.hru.replace(/\/$/,'')&&g.txt==='on this page',lk.id+': '+g.when+g.txt); } }
    ok('recorded hours are short enough to be a row, not a paragraph',S.every(x=>x.hrs.length<=180),S.filter(x=>x.hrs.length>180).map(x=>x.id).join());
    const pv=S.find(x=>x.acc==='view'&&x.cat==='landmark'&&x.st==='standing'&&!x.hrs); r=await row(pv.id);
    ok('a private house seen from the street has no Hours row',!r.has&&/^Access,Effort/.test(r.order),pv.id+': '+r.order);
    const ch=S.find(x=>x.acc==='view'&&x.cat==='worship'&&x.st==='standing'&&!x.hrs); r=await row(ch.id);
    ok('a standing church seen from the street still gets the look-up: services are when it is open',r.has&&r.txt===''&&r.link==='Today’s hours in Google Maps',ch.id);
    const ru=S.find(x=>x.acc==='public'&&x.st==='ruins'&&!x.hrs); r=await row(ru.id);
    ok('a ruin on public land has no Hours row',!r.has,ru.id);
    ok('open to visitors and hours: no script errors',errs.length===0,errs.join(' | ').slice(0,200)); await c.close(); }
  // ---- the kinds of place: one list in the app, every place's kind is on it, and "Places of worship" has its own chip, shortcut and colour
  { const c=await b.newContext({viewport:{width:390,height:844},isMobile:true,hasTouch:true}); const p=await c.newPage(); const errs=[]; p.on('pageerror',e=>errs.push(e.message));
    await p.addInitScript(()=>{ localStorage.setItem('lost-hidden-atlas-v1',JSON.stringify({v:1,home:{id:'alb',by:1}})); });
    await p.goto(url); await p.waitForFunction(()=>window.__atlasNM); await p.waitForTimeout(400);
    await p.evaluate(()=>{ const f=document.querySelector('#filters'); if(f&&!f.open) document.querySelector('#filt-btn').click(); }); await p.waitForTimeout(200);
    const k=await p.evaluate(()=>{ const D=JSON.parse(document.getElementById('d-sites').textContent).sites, grp=[...document.querySelectorAll('#filters .fgrp')].find(g=>/Kind of place/.test(g.textContent)), chips=[...grp.querySelectorAll('.chip')];
      const names=chips.map(x=>x.textContent.trim()), cols=chips.map(x=>x.querySelector('.dot').style.getPropertyValue('--c'));
      return {names,dupCol:cols.length-new Set(cols).size,kinds:[...new Set(D.map(x=>x.cat))].length,worship:D.filter(x=>x.cat==='worship').length,churchElsewhere:D.filter(x=>x.cat==='civic'&&/\b(church|meeting ?house|synagogue)\b/i.test(x.name)).map(x=>x.name)}; });
    ok('Filters lists every kind of place, each in a colour of its own',k.names.length===k.kinds&&k.dupCol===0&&k.names.indexOf('Places of worship')>=0&&k.names.indexOf('Downtown losses')<0,k.names.join(' | '));
    ok('churches and meeting houses are filed under Places of worship, not under civic buildings',k.worship>150&&k.churchElsewhere.length<=Math.max(8,k.worship*0.05),k.worship+' places of worship; '+k.churchElsewhere.length+' with church in the name are civic (a church park, a civic centre in an old church): '+k.churchElsewhere.slice(0,3).join('; '));      /* a few are right to stay; many would mean sessions are not using the kind */
    await p.evaluate(()=>{ [...document.querySelectorAll('#presets .chip')].find(x=>x.textContent==='Places of worship').click(); }); await p.waitForTimeout(350);
    const w=await p.evaluate(()=>{ const v=window.__atlasNM.visible(); return {n:v.length,other:v.filter(s=>s.cat!=='worship').length}; });
    ok('the "Places of worship" shortcut lists them and nothing else',w.n===k.worship&&w.other===0,w.n+' listed');
    ok('kinds of place: no script errors',errs.length===0,errs.join(' | ').slice(0,200)); await c.close(); }
  // ---- an older thin pin that a full entry replaced (was=): the pin is gone, a reader's notes moved, and an old link opens the new entry
  { const c=await b.newContext({viewport:{width:390,height:844},isMobile:true,hasTouch:true}); const p=await c.newPage(); const errs=[]; p.on('pageerror',e=>errs.push(e.message));
    await p.goto(url); await p.waitForFunction(()=>window.__atlasNM);
    const al=await p.evaluate(()=>{ const D=JSON.parse(document.getElementById('d-sites').textContent); const o=Object.keys(D.alias||{})[0]; return o?{o,n:D.alias[o],oldThere:D.sites.some(x=>x.id===o),newThere:D.sites.some(x=>x.id===D.alias[o])}:null; });
    if(!al) ok('(no entry has replaced another yet: nothing to test)',true);
    else { ok('a replaced pin is no longer on the map and its replacement is',!al.oldThere&&al.newThere,al.o+' -> '+al.n);
      /* a reader who saved things against the old id, in a context of their own: the page writes its own state when it is left, so it cannot be planted from inside */
      const c2=await b.newContext({viewport:{width:390,height:844},isMobile:true,hasTouch:true}); const p2=await c2.newPage(); p2.on('pageerror',e=>errs.push(e.message));
      await p2.addInitScript(a=>{ if(!localStorage.getItem('lost-hidden-atlas-v1')) localStorage.setItem('lost-hidden-atlas-v1',JSON.stringify({v:1,home:{id:'alb',by:1},status:{[a.o]:'visited'},notes:{[a.o]:'my note on the old pin'},trip:[a.o],visits:{[a.o]:[{t:'2026-11-01',v:'found',x:'x'}]}})); },al);
      await p2.goto(url+'#'+al.o); await p2.waitForFunction(()=>window.__atlasNM); await p2.waitForTimeout(1200);
      const r=await p2.evaluate(a=>{ const U=JSON.parse(localStorage.getItem('lost-hidden-atlas-v1')); return {status:U.status[a.n],note:U.notes[a.n],trip:U.trip.join(),visits:(U.visits[a.n]||[]).length,old:(a.o in U.status)||(a.o in U.notes)||(a.o in U.visits),open:(document.querySelector('#v-detail h2')||{}).textContent||'',hash:location.hash}; },al);
      ok('what the reader saved against the old pin moved to the new entry',r.status==='visited'&&r.note==='my note on the old pin'&&r.trip===al.n&&r.visits===1&&!r.old,JSON.stringify(r).slice(0,160));
      ok('a link to the old pin opens the entry that replaced it',r.open.length>0&&r.hash==='#'+al.n,r.hash+' | '+r.open.slice(0,40)); await c2.close(); }
    ok('replaced pins: no script errors',errs.length===0,errs.join(' | ').slice(0,200)); await c.close(); }
  // ---- a place of the reader's own is a diamond even when it is standing; a standing place that is changing now still pulses
  { const c=await b.newContext({viewport:{width:390,height:844},isMobile:true,hasTouch:true}); const p=await c.newPage(); const errs=[]; p.on('pageerror',e=>errs.push(e.message));
    await p.addInitScript(()=>{ localStorage.setItem('lost-hidden-atlas-v1',JSON.stringify({v:1,home:{id:'alb',by:1},custom:[{id:'my-test-1',mine:true,name:'Zz my own standing place',lat:42.6526,lon:-73.7562,cat:'landmark',st:'standing',prec:'exact',acc:'public',eff:'drive',town:'Albany',story:'x',links:[]}]})); });
    await p.goto(url); await p.waitForFunction(()=>window.__atlasNM); await p.waitForTimeout(400);
    const r=await p.evaluate(()=>{ const N=window.__atlasNM, m=window.__atlasMap, at=(la,lo)=>{ m.setView([la,lo],17,{animate:false}); N.syncMarkers(); let e=null; m.eachLayer(l=>{ if(l.getLatLng&&l.options.riseOnHover&&l.getLatLng().distanceTo([la,lo])<2) e=l.getElement().firstElementChild; }); return e; };
      const mine=at(42.6526,-73.7562), o={mine:mine?mine.tagName.toLowerCase()+'.'+mine.getAttribute('class').split(' ').join('.'):null};
      const now=N.sites().find(s=>s.now&&s.st==='standing'&&!s.mine); if(now){ const e=at(now.lat,now.lon); o.now=now.id; o.pulse=!!(e&&e.querySelector('path.p'))&&getComputedStyle(e.querySelector('path.p')).animationName; }
      const calm=N.sites().find(s=>!s.now&&s.st==='standing'&&!s.mine), e2=at(calm.lat,calm.lon); o.calm=e2?e2.querySelectorAll('path').length:null; return o; });
    ok('a place of your own that is standing is a diamond on the map, not a tilted star',r.mine==='span.pin.mine',r.mine);
    await p.fill('#q','Zz my own'); await p.waitForTimeout(450);
    ok('and a diamond in the list',await p.evaluate(()=>{ const d=document.querySelector('#list li button[data-id="my-test-1"] .dot'); return !!d&&d.classList.contains('mine')&&!d.classList.contains('star'); }));
    if(r.now) ok('a standing place that is changing now is a star that pulses',r.pulse==='starpulse',r.now+': '+r.pulse);
    ok('a standing place that is not changing has no pulse',r.calm===2,r.calm+' paths');
    ok('own place and pulse: no script errors',errs.length===0,errs.join(' | ').slice(0,200)); await c.close(); }
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
