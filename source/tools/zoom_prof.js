// How long a zoom step holds up the page with the overlays on. Map tiles are stubbed out, so only the Atlas's own drawing
// is timed, and the CPU is slowed to stand in for a mid-range phone (GUIDE.md section 9, "Speed").
//   node tools/zoom_prof.js [slowdown=4] [alb|bos|syr|kc] [all|none|lines|leads|xl|pockets]      (serve the built site first)
// It zooms through 16 steps once (the first pass makes layers) and three times more, and prints the median of the later
// passes for each zoom and the number of layers on the map. Run it before and after a change to what is put on the map.
//   SITE=<address>   time another copy, such as the published one served from the clone's root
//   NOPINS=1         hide every pin first, to see what the pins cost
//   PROF=25          also print the 25 functions that took the most time
//   NOSTROKE=1, NODASH=1, VAR=c|n   switch off canvas strokes, dashes, round line ends (c) or the white casing (n), to see
//                    how much of a step is the browser drawing lines. A headless browser draws in software, so that part is
//                    larger here than on a phone.
const { chromium, devices } = require('playwright');
(async()=>{
  const thr=+process.argv[2]||4, view=process.argv[3]||'alb', ov=process.argv[4]||'all';
  const V={alb:[42.6526,-73.7562],bos:[42.36,-71.06],syr:[43.05,-76.15],kc:[39.1,-94.58]}[view]||[42.6526,-73.7562];
  const b=await chromium.launch(); const c=await b.newContext({...devices['Pixel 7']}); const p=await c.newPage();
  const JPG=Buffer.from('/9j/4AAQSkZJRgABAQEASABIAAD/2wBDAAMCAgICAgMCAgIDAwMDBAYEBAQEBAgGBgUGCQgKCgkICQkKDA8MCgsOCwkJDRENDg8QEBEQCgwSExIQEw8QEBD/yQALCAABAAEBAREA/8wABgAQEAX/2gAIAQEAAD8A0s8g/9k=','base64');
  await c.route(u=>!/^http:\/\/localhost/.test(u.href),r=>{ const u=r.request().url(); if(/\/(export|exportImage|tile)[\/?]|\.png|\.jpg/.test(u)) return r.fulfill({status:200,contentType:'image/jpeg',headers:{'access-control-allow-origin':'*'},body:JPG}); return r.fulfill({status:204,body:''}); });
  const on=k=>ov==='all'||ov===k;
  await p.addInitScript(a=>{ try{ localStorage.setItem('lost-hidden-atlas-v1',JSON.stringify({v:1,ui:{base:'streets',view:[a.V[0],a.V[1],12],hist:false,lines:{oldrail:a.lines,canal:a.lines,rail:a.lines},leads:a.leads,xl:a.xl?{vanished:true,mines:true}:{},pockets:a.pockets,walls:false}})); }catch(e){} },{V,lines:on('lines'),leads:on('leads'),xl:on('xl'),pockets:on('pockets')});
  if(process.env.VAR) await p.addInitScript(v=>{ const st=CanvasRenderingContext2D.prototype.stroke; CanvasRenderingContext2D.prototype.stroke=function(){ if(v.indexOf('a')>=0) this.globalAlpha=1; if(v.indexOf('c')>=0){ this.lineCap='butt'; this.lineJoin='bevel'; } if(v.indexOf('m')>=0){ this.lineCap='butt'; this.lineJoin='miter'; } if(v.indexOf('n')>=0&&this.strokeStyle==='#ffffff') return; return st.apply(this,arguments); }; },process.env.VAR);
  if(process.env.NODASH) await p.addInitScript(()=>{ CanvasRenderingContext2D.prototype.setLineDash=function(){}; });
  if(process.env.NOSTROKE) await p.addInitScript(()=>{ CanvasRenderingContext2D.prototype.stroke=function(){}; });
  const errs=[]; p.on('pageerror',e=>errs.push(e.message));
  await p.goto(process.env.SITE||'http://localhost:8766/index.html'); await p.waitForFunction(()=>window.__atlasMap); await p.waitForTimeout(2500);
  if(process.env.NOPINS){ await p.fill('#q','qqqqzz'); await p.waitForTimeout(600); }
  const cdp=await c.newCDPSession(p); await cdp.send('Emulation.setCPUThrottlingRate',{rate:thr});
  await p.evaluate(()=>{ window.__lt=[]; try{ new PerformanceObserver(l=>l.getEntries().forEach(e=>window.__lt.push(Math.round(e.duration)))).observe({entryTypes:['longtask']}); }catch(e){} });
  const step=async z=>p.evaluate(z=>new Promise(res=>{ const m=window.__atlasMap, t0=performance.now(); m.setZoom(z,{animate:false}); const t1=performance.now();
    requestAnimationFrame(()=>requestAnimationFrame(()=>{ const t2=performance.now(); setTimeout(()=>res({z:z,sync:Math.round(t1-t0),frames:Math.round(t2-t1),layers:Object.keys(m._layers).length}),350); })); }),z);
  const PROF=!!process.env.PROF; if(PROF){ await cdp.send('Profiler.enable'); await cdp.send('Profiler.setSamplingInterval',{interval:500}); await cdp.send('Profiler.start'); }
  const SEQ=[13,14,15,16,15,14,13,12,11,10,9,8,9,10,11,12], first=[]; for(const z of SEQ) first.push(await step(z));
  const out=[]; for(let k=0;k<(+process.env.REPS||3);k++) for(const z of SEQ) out.push(await step(z));
  const f1=first.map(r=>r.sync+r.frames).sort((a,b)=>a-b);
  const pan=await p.evaluate(()=>new Promise(res=>{ const m=window.__atlasMap, t0=performance.now(); m.panBy([200,150],{animate:false}); const t1=performance.now(); requestAnimationFrame(()=>requestAnimationFrame(()=>res(Math.round(performance.now()-t0)))); }));
  if(PROF){ const {profile}=await cdp.send('Profiler.stop'); const self=new Map(), byId=new Map(); profile.nodes.forEach(n=>byId.set(n.id,n));
    const dt=profile.timeDeltas, tot={}; profile.samples.forEach((id,i)=>{ const n=byId.get(id), f=n.callFrame, k=(f.functionName||'(anon)')+' '+(f.url.split('/').pop()||'')+':'+f.lineNumber; self.set(k,(self.get(k)||0)+(dt[i]||0)); });
    // inclusive time by walking parents
    const parent=new Map(); profile.nodes.forEach(n=>(n.children||[]).forEach(c=>parent.set(c,n.id))); const incl=new Map();
    profile.samples.forEach((id,i)=>{ const seen=new Set(); let cur=id; while(cur!==undefined){ const f=byId.get(cur).callFrame, k=(f.functionName||'(anon)')+' '+(f.url.split('/').pop()||'')+':'+f.lineNumber; if(!seen.has(k)){ seen.add(k); incl.set(k,(incl.get(k)||0)+(dt[i]||0)); } cur=parent.get(cur); } });
    const top=m=>[...m.entries()].sort((a,b)=>b[1]-a[1]).slice(0,+process.env.PROF||28).map(([k,v])=>(v/1000).toFixed(0).padStart(6)+' ms  '+k).join('\n');
    console.log('--- self time\n'+top(self)+'\n--- inclusive time\n'+top(incl)); }
  const lt=await p.evaluate(()=>window.__lt);
  const tot=out.map(r=>r.sync+r.frames); tot.sort((a,b)=>a-b);
  const byz={}; out.forEach(r=>{ (byz[r.z]=byz[r.z]||[]).push(r.sync+r.frames); }); const med=a=>{ a=a.slice().sort((x,y)=>x-y); return a[a.length>>1]; };
  console.log('x'+thr+' '+view+' '+ov.padEnd(8)+' first pass: median '+f1[f1.length>>1]+' worst '+f1[f1.length-1]+' | later passes by zoom '+Object.keys(byz).map(z=>z+':'+med(byz[z])).join(' ')+' | layers at 12: '+out[out.length-1].layers);
  console.log('   later passes: median '+tot[tot.length>>1]+' ms, worst '+tot[tot.length-1]+' ms, mean '+Math.round(tot.reduce((a,b)=>a+b,0)/tot.length)+' ms; one pan '+pan+' ms'+(errs.length?' ERRORS '+errs.join(';').slice(0,200):''));
  await b.close();
})();
