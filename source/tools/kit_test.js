// Phone-size check of the episode kit (app.js, "episode kit"): stops, chapters, the kit file and the route map picture.
//   node tools/kit_test.js http://localhost:8766/index.html      (serve the built site first, as for smoke.js)
// It makes up a walk past two neighbouring Atlas places, with two videos, two photos and two notes, and opens its kit.
// The picture is saved to /tmp/kit_route.png and screenshots to /tmp/kit_*.png. It needs the USGS base map to be reachable.
const { chromium, devices } = require('playwright'); const fs = require('fs');
(async()=>{
  const fails=[]; const ok=(name,cond,extra)=>{ console.log((cond?'ok   ':'FAIL ')+name+(extra!==undefined?'  ['+extra+']':'')); if(!cond) fails.push(name); };
  const b=await chromium.launch({proxy:{server:process.env.HTTPS_PROXY||'http://x',bypass:'localhost,127.0.0.1'}});
  const c=await b.newContext(Object.assign({},devices['Pixel 7'],{acceptDownloads:true})); const p=await c.newPage(); const errs=[];
  p.on('pageerror',e=>errs.push(e.message));
  const url=process.argv[2]||'http://localhost:8766/index.html';
  await p.goto(url); await p.waitForFunction(()=>window.__atlasMap); await p.waitForTimeout(800);
  const made=await p.evaluate(()=>{ const D=JSON.parse(document.getElementById('d-sites').textContent), S=D.sites, R=6371000, rad=x=>x*Math.PI/180;
    const dist=(a,b)=>{ const dl=rad(b.lat-a.lat), dn=rad(b.lon-a.lon), h=Math.sin(dl/2)**2+Math.cos(rad(a.lat))*Math.cos(rad(b.lat))*Math.sin(dn/2)**2; return 2*R*Math.asin(Math.sqrt(h)); };
    const good=S.filter(s=>s.prec!=='area'&&Array.isArray(s.links)&&s.links.length&&s.lat>42&&s.lat<43.2&&s.lon>-74.6&&s.lon<-73.3); let A=null,B=null;
    for(const x of good){ for(const y of good){ if(x===y) continue; const d=dist(x,y); if(d>700&&d<1500&&!S.some(o=>o!==x&&o!==y&&(dist(o,x)<420||dist(o,y)<420))){ A=x; B=y; break; } } if(A) break; }
    if(!A) return null;
    const t0=Math.round(Date.now()/1000)-7200, pts=[], step=2.8; let t=t0;   // 2 s a point at 1.4 m/s
    const leg=(a,b)=>{ const n=Math.max(1,Math.round(dist(a,b)/step)); for(let i=0;i<=n;i++){ pts.push([+(a.lat+(b.lat-a.lat)*i/n).toFixed(6),+(a.lon+(b.lon-a.lon)*i/n).toFixed(6),t]); t+=2; } };
    const stay=(a,sec)=>{ for(let i=0;i<sec/2;i++){ pts.push([+(a.lat+Math.sin(i/7)*0.00008).toFixed(6),+(a.lon+Math.cos(i/5)*0.0001).toFixed(6),t]); t+=2; } };
    const south={lat:A.lat-400/111320,lon:A.lon}, north={lat:B.lat+200/111320,lon:B.lon};
    leg(south,A); const atA=t; stay(A,240); leg(A,B); const atB=t; stay(B,300); leg(B,north);
    const log={id:'logkit1',name:'Two old places · Nov 16',site:A.id,t0:t0,t1:t,pts:pts,mscan:1,
      notes:[{t:atA+120,x:'cellar hole',la:A.lat,lo:A.lon},{t:atB+60,x:'wheel pit',la:B.lat,lo:B.lon}],
      media:[{k:'v',id:1,n:'VID_0001.mp4',t:t0+60,d:(atA-t0)+140,la:south.lat,lo:south.lon},{k:'i',id:2,n:'IMG_0002.jpg',t:atA+100,la:A.lat,lo:A.lon,nt:atA+120},{k:'v',id:3,n:'VID_0003.mp4',t:atB+30,d:200,la:B.lat,lo:B.lon},{k:'i',id:4,n:'IMG_0004.jpg',t:atB+90,la:B.lat,lo:B.lon,nt:atB+60}]};
    return {log:log,A:A.name,B:B.name,aid:A.id,link:A.links[0][1],pts:pts.length,gap:Math.round(dist(A,B))}; });
  ok('made up a walk past two neighbouring places',!!made,made&&(made.A+' -> '+made.B+', '+made.gap+' m apart, '+made.pts+' points'));
  if(!made){ await b.close(); process.exit(1); }
  // the page saves its own data as it closes, so new data goes in just before the next load, once
  const inject=(key,part)=>c.addInitScript(([key,part])=>{ if(location.protocol==='about:'||sessionStorage.getItem('inj'+key)) return; sessionStorage.setItem('inj'+key,'1'); const U=JSON.parse(localStorage.getItem('lost-hidden-atlas-v1')||'{}'); Object.assign(U,part); localStorage.setItem('lost-hidden-atlas-v1',JSON.stringify(U)); },[key,part]);
  await inject(1,{logs:[made.log]});
  await p.goto('about:blank'); await p.goto(url); await p.waitForFunction(()=>window.__atlasMap); await p.waitForTimeout(800);
  await p.click('#tab-log'); await p.waitForTimeout(400);
  await p.getByRole('button',{name:'Episode kit'}).click(); await p.waitForTimeout(500);
  const stops=await p.evaluate(()=>[...document.querySelectorAll('.kitstops li')].map(n=>n.querySelector('b').textContent+' | '+n.querySelector('small').textContent));
  ok('two stops, in the order walked, each with its clip, photo and note',stops.length===2&&stops[0].startsWith(made.A)&&stops[1].startsWith(made.B)&&stops.every(s=>/1 clip · 1 photo · 1 note/.test(s)),stops.join(' // '));
  const ch=(await p.innerText('.kitpre')).trim().split('\n');
  const sec=x=>x.split(' ')[0].split(':').reduce((a,v)=>a*60+ +v,0);
  ok('three chapters: setting out, then each place',ch.length===3&&ch[0]==='0:00 Setting out'&&ch[1].endsWith(' '+made.A)&&ch[2].endsWith(' '+made.B)&&sec(ch[1])>60&&sec(ch[2])-sec(ch[1])>=10,ch.join(' / '));
  await p.screenshot({path:'/tmp/kit_1.png',fullPage:false});
  const [dl]=await Promise.all([p.waitForEvent('download'),p.getByRole('button',{name:'Save the whole kit'}).click()]); const kit=fs.readFileSync(await dl.path(),'utf8');
  ok('the kit file groups clips, photos and notes by place',kit.includes('1. '+made.A.toUpperCase())&&kit.includes('2. '+made.B.toUpperCase())&&/VIDEO 1 {2}VID_0001\.mp4/.test(kit)&&/PHOTOS {2}IMG_0002\.jpg/.test(kit)&&/NOTE {2}[\d:]+ {2}cellar hole {3}\(video 1 at /.test(kit));
  ok('it carries the chapters and a description with the sources',kit.includes('YOUTUBE CHAPTERS (DRAFT)\n0:00 Setting out')&&kit.includes('Sources and further reading')&&kit.includes(made.link)&&kit.includes('Before you go')&&kit.includes('#'+made.aid)&&/On foot: [\d.]+ mi in \d+ min\./.test(kit));
  fs.writeFileSync('/tmp/kit_text.txt',kit);
  await p.getByRole('button',{name:'Draw the route map'}).click(); await p.waitForSelector('.kitpic img',{timeout:60000}); await p.waitForTimeout(500);
  const pic=await p.evaluate(()=>{ const im=document.querySelector('.kitpic img'); return [im.naturalWidth,im.naturalHeight,document.querySelector('.kitpic .snote').textContent]; });
  ok('the route map is 1920 x 1080 and every base-map tile loaded',pic[0]===1920&&pic[1]===1080&&!/did not load/.test(pic[2]),pic.join(' '));
  const [d2]=await Promise.all([p.waitForEvent('download'),p.getByRole('button',{name:'Save the picture'}).click()]); fs.copyFileSync(await d2.path(),'/tmp/kit_route.png');
  ok('the picture saves as a PNG',fs.statSync('/tmp/kit_route.png').size>200000&&d2.suggestedFilename()==='two-old-places-nov-16-route-map.png',fs.statSync('/tmp/kit_route.png').size+' bytes '+d2.suggestedFilename());
  await p.evaluate(()=>{ document.querySelector('.kitpic').scrollIntoView(); }); await p.screenshot({path:'/tmp/kit_2.png'});
  // trimming the ends: with 500 m cut from each end the picture and distance use the shorter walk
  await p.click('#lb-opt'); await p.click('#sheet-set'); await p.selectOption('#set-trim','500'); await p.click('#sheet-x'); await p.waitForTimeout(300);
  const [d3]=await Promise.all([p.waitForEvent('download'),p.getByRole('button',{name:'Save the whole kit'}).click()]); const kit2=fs.readFileSync(await d3.path(),'utf8');
  const mi=x=>+(/On foot: ([\d.]+) mi/.exec(x)||[0,0])[1]; ok('"Trim the ends" shortens the published distance',mi(kit2)<mi(kit)-0.5,mi(kit)+' -> '+mi(kit2)+' mi');
  // a walk nowhere near a place still gets a kit
  { const t0=made.log.t0, pts=[]; for(let i=0;i<200;i++) pts.push([+(44.9+i*0.00002).toFixed(6),-74.9,t0+i*2]); await inject(2,{logs:[{id:'logkit2',name:'Nowhere · Nov 16',site:null,t0:t0,t1:t0+400,pts:pts,notes:[],media:[]}],set:{trim:0}}); }
  await p.goto('about:blank'); await p.goto(url); await p.waitForFunction(()=>window.__atlasMap); await p.click('#tab-log'); await p.getByRole('button',{name:'Episode kit'}).click(); await p.waitForTimeout(400);
  ok('a walk past no place still opens, and says so',/did not come within reach/.test(await p.innerText('.kit'))&&(await p.locator('.kitstops li').count())===0);
  ok('no script errors',errs.length===0,errs.join(' | ').slice(0,300));
  await b.close(); console.log(fails.length?fails.length+' FAILED':'kit test passed'); process.exit(fails.length?1:0);
})().catch(e=>{ console.error(e); process.exit(1); });
