// The Places tab's header: one row (search, Filters, Add), the filter panel, and the single drive time on a place.
//   node tools/places_test.js http://localhost:8766/index.html      (serve the built site first, as for smoke.js)
// Run it after changing the Places header in app.body.html, buildFilters(), the chips' styles, or "Getting there" in renderDetail().
// What it holds the app to: the list starts high on a phone; a filter that is switched on looks different from one that is
// off, in dark and light; the Filters button shows how many are on; the start place is chosen under the gear only.
const { chromium } = require('playwright');
(async()=>{
  const fails=[]; const ok=(name,cond,extra)=>{ console.log((cond?'ok   ':'FAIL ')+name+(extra!==undefined?'  ['+extra+']':'')); if(!cond) fails.push(name); };
  const b=await chromium.launch(); const url=process.argv[2]||'http://localhost:8766/index.html';
  for(const [name,vp,dpr,mobile,scheme] of [['phone, dark',{width:390,height:844},2,true,'dark'],['desktop, dark',{width:1400,height:900},1,false,'dark'],['desktop, light',{width:1400,height:900},1,false,'light']]){
    const c=await b.newContext({viewport:vp,deviceScaleFactor:dpr,isMobile:mobile,hasTouch:mobile,colorScheme:scheme}); const p=await c.newPage(); const errs=[]; p.on('pageerror',e=>errs.push(e.message));
    await c.route(u=>!/^http:\/\/localhost/.test(u.href),r=>r.fulfill({status:204,body:''}));
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
    ok(name+': no script errors',errs.length===0,errs.join(' | ').slice(0,200)); await c.close(); }
  await b.close(); console.log(fails.length?('\n'+fails.length+' FAILED'):'\nplaces header test passed'); process.exit(fails.length?1:0);
})();
