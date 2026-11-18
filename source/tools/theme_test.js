// The colour schemes (Settings, "Colours"): each one can be chosen, and its text can be read.
//   node tools/theme_test.js http://localhost:8766/index.html      (serve the built site first, as for smoke.js)
// Run it after adding or changing a scheme in app.css or THEMES in app.js. For every scheme it checks, by the WCAG
// contrast formula on the colours the page actually computed: body text on the panel and on the page (7 to 1), quiet
// text, accent text and a chip's text (4.5 to 1), and the text on an accent-filled button (4.5 to 1). It also checks
// that "Follow the phone" gives Brick and paper by day and Tomorrow by night, and that a setting saved by an older
// build ("light", "dark") still means those two.
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
  ok('Follow the phone, by day: Brick and paper',r.theme===null&&r.accent==='#a33a24',r.accent); await A.c.close();
  A=await open('dark',{v:1,home:{id:'alb',by:1}}); r=await read(A.p);
  ok('Follow the phone, by night: Tomorrow',r.theme===null&&r.accent==='#81a2be'&&r.bg==='#1d1f21',r.accent+' on '+r.bg); await A.c.close();
  A=await open('dark',{v:1,home:{id:'alb',by:1},set:{theme:'light'}}); r=await read(A.p); ok('a saved "light" on a phone in dark mode is still Brick and paper',r.accent==='#a33a24',r.accent); await A.c.close();
  A=await open('light',{v:1,home:{id:'alb',by:1},set:{theme:'dark'}}); r=await read(A.p); ok('a saved "dark" on a phone in light mode is still Tomorrow',r.accent==='#81a2be',r.accent); await A.c.close();
  A=await open('light',{v:1,home:{id:'alb',by:1},set:{theme:'no-such-scheme'}}); r=await read(A.p); ok('a scheme this build does not know falls back to following the phone',r.theme===null&&r.accent==='#a33a24',r.accent);
  // every scheme, chosen in Settings
  await A.p.click('#lb-opt'); await A.p.waitForTimeout(250); await A.p.evaluate(()=>{ const g=[...document.querySelectorAll('#sheet button')].find(x=>/settings/i.test(x.getAttribute('aria-label')||x.textContent)); if(g) g.click(); }); await A.p.waitForTimeout(300);
  const opts=await A.p.evaluate(()=>{ const s=document.querySelector('#set-theme'); return s?[...s.options].map(o=>[o.value,o.textContent]):[]; });
  ok('Settings has a Colours list with seven choices',opts.length===7,opts.map(o=>o[1]).join(' | '));
  for(const [val,label] of opts){ if(val==='auto') continue;
    await A.p.selectOption('#set-theme',val); await A.p.waitForTimeout(150); r=await read(A.p);
    const low=[['body text on the panel',r.ink_panel,7],['body text on the page',r.ink_bg,7],['quiet text',r.mute_panel,4.5],['accent text',r.accent_panel,4.5],['chip text',r.ink_chip,4.5],['text on an accent button',r.on_accent,4.5],['warning text',r.warn_panel,4.5]].filter(x=>x[1]<x[2]);
    ok(label+': chosen, and every text colour can be read',r.theme===val&&low.length===0&&r.meta.toLowerCase()===r.accent.toLowerCase(),low.length?low.map(x=>x[0]+' '+x[1]+' (needs '+x[2]+')').join('; '):'lowest: quiet '+r.mute_panel+', accent '+r.accent_panel+', on accent '+r.on_accent); }
  await A.c.close();
  ok('no script errors',errs.length===0,errs.join(' | ').slice(0,200));
  await b.close(); console.log(fails.length?('\n'+fails.length+' FAILED'):'\ntheme test passed'); process.exit(fails.length?1:0);
})();
