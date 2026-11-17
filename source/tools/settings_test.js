// Phone-size check of the two sheets behind the "More" button: Map options (kept short) and Settings (the gear).
//   node tools/settings_test.js http://localhost:8766/index.html      (serve the built site first, as for smoke.js)
// Run it after changing buildSheet(), buildSettings() or anything they show. Screenshots go to /tmp/set_*.png.
const { chromium, devices } = require('playwright');
(async()=>{
  const fails=[]; const ok=(name,cond,extra)=>{ console.log((cond?'ok   ':'FAIL ')+name+(extra!==undefined?'  ['+extra+']':'')); if(!cond) fails.push(name); };
  const b=await chromium.launch({proxy:{server:process.env.HTTPS_PROXY||'http://x',bypass:'localhost,127.0.0.1'}});
  const c=await b.newContext(Object.assign({},devices['Pixel 7'])); const p=await c.newPage(); const errs=[]; p.on('pageerror',e=>errs.push(e.message));
  // a trip of two places, put in before the page first loads
  await c.addInitScript(()=>{ if(location.protocol!=='about:'&&!localStorage.getItem('lost-hidden-atlas-v1')) localStorage.setItem('lost-hidden-atlas-v1',JSON.stringify({trip:['joliet-iron-works','lidar-high-knob-walled-yard']})); });
  await p.goto(process.argv[2]||'http://localhost:8766/index.html'); await p.waitForFunction(()=>window.__atlasMap); await p.waitForTimeout(600);
  const U=()=>p.evaluate(()=>JSON.parse(localStorage.getItem('lost-hidden-atlas-v1')||'{}'));
  const shown=sel=>p.evaluate(sel=>[...document.querySelectorAll(sel)].filter(n=>n.offsetParent!==null&&n.getClientRects().length).length,sel);
  // ---- Map options: every switch in sight, explanations only when asked for
  await p.click('#lb-opt'); await p.waitForTimeout(300);
  const h0=await p.evaluate(()=>document.querySelector('#sheet-b').scrollHeight), vh=await p.evaluate(()=>innerHeight);
  ok('Map options: short by default',h0<vh*1.6,h0+' px tall on a '+vh+' px screen');
  ok('Map options: explanations hidden by default',(await shown('#sheet-b .lopt small'))===0&&(await shown('#sheet-b .snote'))===0);
  ok('Map options: the switches are all there',(await shown('#sheet-b #hist-on'))===1&&(await shown('#sheet-b #leads-on'))===1&&(await shown('#sheet-b #xl-mines'))===1&&(await shown('#sheet-b #pock-on'))===1&&(await shown('#sheet-b #land-on'))===1);
  await p.screenshot({path:'/tmp/set_1_options.png'});
  await p.click('#sheet-tips'); await p.waitForTimeout(250);
  ok('Map options: "What do these do?" shows the explanations',(await shown('#sheet-b .lopt small'))>5&&(await shown('#sheet-b .snote'))>1);
  await p.waitForTimeout(900); ok('Map options: the choice is remembered',(await U()).ui.tips===true);
  await p.click('#sheet-tips'); await p.waitForTimeout(250);
  ok('Map options: and hides them again',(await shown('#sheet-b .lopt small'))===0);
  const keys=()=>shown('#sheet-b .lkeys');
  const k0=await keys(); await p.evaluate(()=>{ const n=document.querySelector('#land-on'); if(!n.checked) n.click(); }); await p.waitForTimeout(300);
  ok('Map options: a legend shows only for a layer that is on',(await keys())===k0+1,k0+' -> '+(await keys()));
  await p.evaluate(()=>document.querySelector('#land-on').click()); await p.waitForTimeout(200);
  // ---- Settings
  await p.click('#sheet-set'); await p.waitForTimeout(300);
  const txt=await p.innerText('#sheet-b');
  ok('Settings: no stray "null" on the page',!/\bnull\b/.test(txt),(txt.match(/.{0,25}null.{0,10}/)||[''])[0]);
  const heads=await p.evaluate(()=>[...document.querySelectorAll('#sheet-b h3')].map(n=>n.textContent));
  ok('Settings: Near me and Episode kit have their own sections',heads.includes('Near me')&&heads.includes('Episode kit'),heads.join(' | '));
  await p.selectOption('#set-nm-al','200'); await p.selectOption('#set-nm-r','5'); await p.waitForTimeout(1200);   // saving waits a moment for more changes
  let u=await U(); ok('Settings: the Near me choices are saved',u.ui.nm&&u.ui.nm.al===200&&u.ui.nm.r===5,JSON.stringify(u.ui.nm));
  await p.fill('#set-kitSign','Subscribe: example.org/channel'); await p.selectOption('#set-kitBase','air'); await p.click('#sheet-t'); await p.waitForTimeout(250);
  u=await U(); ok('Settings: the kit choices are saved',u.set&&u.set.kitSign==='Subscribe: example.org/channel'&&u.set.kitBase==='air',JSON.stringify(u.set));
  await p.screenshot({path:'/tmp/set_2_settings.png'});
  await p.click('#sheet-x'); await p.click('#tab-near'); await p.waitForTimeout(500);
  ok('Near tab shows what Settings chose',(await p.inputValue('#near-al'))==='200'&&(await p.inputValue('#near-r'))==='5');
  await p.selectOption('#near-al','50'); await p.waitForTimeout(200); await p.click('#near-set'); await p.waitForTimeout(350);
  ok('Near tab: its Settings link opens the gear at Near me',(await p.innerText('#sheet-t')).trim().toLowerCase()==='settings'&&(await p.inputValue('#set-nm-al'))==='50');
  await p.click('#sheet-x');
  // ---- Trip: the round-trip tick is remembered
  await p.click('#tab-trip'); await p.waitForTimeout(250);
  await p.evaluate(()=>{ const n=document.querySelector('#trip-round'); if(n.checked) n.click(); }); await p.waitForTimeout(1200);
  ok('Trip: "round trip" off is remembered',(await U()).ui.round===false);
  await p.reload(); await p.waitForFunction(()=>window.__atlasMap); await p.click('#tab-trip'); await p.waitForTimeout(250);
  ok('Trip: and still off after a reload',(await p.evaluate(()=>document.querySelector('#trip-round').checked))===false);
  ok('no script errors',errs.length===0,errs.slice(0,2).join(' | '));
  await b.close(); console.log(fails.length?fails.length+' FAILED':'settings test passed'); process.exit(fails.length?1:0);
})();
