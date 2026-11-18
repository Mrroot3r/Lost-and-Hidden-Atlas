// The colour schemes (Settings, "Colours"): each one can be chosen, and its text can be read.
//   node tools/theme_test.js http://localhost:8766/index.html      (serve the built site first, as for smoke.js)
// Run it after adding or changing a scheme in app.css or THEMES in app.js. For every scheme it checks, by the WCAG
// contrast formula on the colours the page actually computed: body text on the panel and on the page (7 to 1), quiet
// text, accent text and a chip's text (4.5 to 1), and the text on an accent-filled button (4.5 to 1). It also checks
// that the reader's light scheme and dark scheme are each used when they should be (the phone deciding, or always one),
// that the page follows the phone into night mode without a reload, and that a setting saved by an older build still works.
const { chromium } = require('playwright');
(async()=>{
  const fails=[]; const ok=(name,cond,extra)=>{ console.log((cond?'ok   ':'FAIL ')+name+(extra!==undefined?'  ['+extra+']':'')); if(!cond) fails.push(name); };
  const url=process.argv[2]||'http://localhost:8766/index.html'; const b=await chromium.launch(); const errs=[];
  const read=p=>p.evaluate(()=>{ const cs=getComputedStyle(document.documentElement), v=k=>cs.getPropertyValue(k).trim();
    const lum=h=>{ const n=parseInt(h.slice(1),16), c=[n>>16&255,n>>8&255,n&255].map(x=>{ x/=255; return x<=0.03928?x/12.92:Math.pow((x+0.055)/1.055,2.4); }); return 0.2126*c[0]+0.7152*c[1]+0.0722*c[2]; };
    const cr=(a,b)=>{ const x=lum(v(a)), y=lum(v(b)); return +((Math.max(x,y)+0.05)/(Math.min(x,y)+0.05)).toFixed(2); };
    return {theme:document.documentElement.getAttribute('data-theme'),accent:v('--accent'),bg:v('--bg'),ink_panel:cr('--ink','--panel'),ink_bg:cr('--ink','--bg'),mute_panel:cr('--mute','--panel'),accent_panel:cr('--accent','--panel'),ink_chip:cr('--ink','--chip'),on_accent:cr('--accent-ink','--accent'),warn_panel:cr('--warn','--panel'),
      meta:(document.querySelector('meta[name="theme-color"]')||{}).content||''}; });
  const open=async(scheme,state)=>{ const c=await b.newContext({viewport:{width:390,height:844},isMobile:true,hasTouch:true,colorScheme:scheme}); const p=await c.newPage(); p.on('pageerror',e=>errs.push(e.message));
    await c.route(u=>!/^http:\/\/localhost/.test(u.href),r=>r.fulfill({status:204,body:''}));
    await p.addInitScript(s=>{ try{ localStorage.setItem('lost-hidden-atlas-v1',JSON.stringify(s)); }catch(e){} },state);
    await p.goto(url); await p.waitForFunction(()=>window.__atlasMap); await p.waitForTimeout(300); return {c,p}; };
  let A=await open('light',{v:1,home:{id:'alb',by:1}}); let r=await read(A.p);
  ok('Follow the phone, by day: Brick and paper',r.theme==='brick'&&r.accent==='#a33a24',r.theme+' '+r.accent);
  await A.p.emulateMedia({colorScheme:'dark'}); await A.p.waitForTimeout(200); r=await read(A.p);
  ok('the phone goes to night mode while the page is open: Tomorrow, without a reload',r.theme==='tomorrow'&&r.accent==='#81a2be',r.theme); await A.c.close();
  A=await open('dark',{v:1,home:{id:'alb',by:1}}); r=await read(A.p);
  ok('Follow the phone, by night: Tomorrow',r.theme==='tomorrow'&&r.bg==='#1d1f21',r.theme+' on '+r.bg); await A.c.close();
  A=await open('dark',{v:1,home:{id:'alb',by:1},set:{theme:'light'}}); r=await read(A.p); ok('"Always light" on a phone in night mode: Brick and paper',r.theme==='brick',r.theme); await A.c.close();
  A=await open('light',{v:1,home:{id:'alb',by:1},set:{theme:'dark'}}); r=await read(A.p); ok('"Always dark" on a phone in day mode: Tomorrow',r.theme==='tomorrow',r.theme); await A.c.close();
  // settings saved by the build of the evening of November 17, which kept one name for mode and scheme
  A=await open('light',{v:1,home:{id:'alb',by:1},set:{theme:'blueprint'}}); r=await read(A.p); let st=await A.p.evaluate(()=>JSON.parse(localStorage.getItem('lost-hidden-atlas-v1')||'{}').set||{});
  ok('an older saved "blueprint" becomes Always dark with Blueprint night',r.theme==='blueprint',r.theme); await A.c.close();
  A=await open('dark',{v:1,home:{id:'alb',by:1},set:{theme:'slate'}}); r=await read(A.p); ok('an older saved "slate" becomes Always light with Slate and copper',r.theme==='slate',r.theme); await A.c.close();
  A=await open('light',{v:1,home:{id:'alb',by:1},set:{theme:'auto',themeL:'no-such',themeD:'brick'}}); r=await read(A.p); ok('a scheme this build does not know, or one of the wrong kind, falls back to the default',r.theme==='brick',r.theme); await A.c.close();
  // the reader's own pair: one light, one dark, and the phone decides between them
  A=await open('light',{v:1,home:{id:'alb',by:1},set:{theme:'auto',themeL:'survey',themeD:'morning'}}); r=await read(A.p); const day=r.theme;
  await A.p.emulateMedia({colorScheme:'dark'}); await A.p.waitForTimeout(200); r=await read(A.p);
  ok('a chosen pair: Survey green by day and Tomorrow morning by night',day==='survey'&&r.theme==='morning',day+' then '+r.theme); await A.c.close();
  // every scheme, chosen in Settings
  A=await open('light',{v:1,home:{id:'alb',by:1}});
  await A.p.click('#lb-opt'); await A.p.waitForTimeout(250); await A.p.evaluate(()=>{ const g=[...document.querySelectorAll('#sheet button')].find(x=>/settings/i.test(x.getAttribute('aria-label')||x.textContent)); if(g) g.click(); }); await A.p.waitForTimeout(300);
  const opts=k=>A.p.evaluate(k=>{ const s=document.querySelector('#set-'+k); return s?[...s.options].map(o=>[o.value,o.textContent]):[]; },k);
  const mode=await opts('theme'), L=await opts('themeL'), Dk=await opts('themeD');
  ok('Settings has Colours (3 choices), Light colours and Dark colours',mode.length===3&&L.length>=4&&Dk.length>=4,mode.length+' / '+L.map(o=>o[1]).join(', ')+' / '+Dk.map(o=>o[1]).join(', '));
  for(const [kind,list] of [['light',L],['dark',Dk]]){ await A.p.selectOption('#set-theme',kind); await A.p.waitForTimeout(250);
    for(const [val,label] of list){ await A.p.selectOption(kind==='light'?'#set-themeL':'#set-themeD',val); await A.p.waitForTimeout(250); r=await read(A.p);
      const low=[['body text on the panel',r.ink_panel,7],['body text on the page',r.ink_bg,7],['quiet text',r.mute_panel,4.5],['accent text',r.accent_panel,4.5],['chip text',r.ink_chip,4.5],['text on an accent button',r.on_accent,4.5],['warning text',r.warn_panel,4.5]].filter(x=>x[1]<x[2]);
      const isDark=await A.p.evaluate(()=>getComputedStyle(document.documentElement).colorScheme);
      ok(label+' ('+kind+'): chosen, and every text colour can be read',r.theme===val&&low.length===0&&r.meta.toLowerCase()===r.accent.toLowerCase()&&isDark===kind,low.length?low.map(x=>x[0]+' '+x[1]+' (needs '+x[2]+')').join('; '):'lowest: quiet '+r.mute_panel+', accent '+r.accent_panel+', on accent '+r.on_accent); } }
  await A.c.close();
  ok('no script errors',errs.length===0,errs.join(' | ').slice(0,200));
  await b.close(); console.log(fails.length?('\n'+fails.length+' FAILED'):'\ntheme test passed'); process.exit(fails.length?1:0);
})();
