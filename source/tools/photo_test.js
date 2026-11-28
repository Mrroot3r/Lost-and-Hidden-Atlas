// The photo at the top of a place page, from the place's Wikipedia article, with the photographer's credit.
//   node tools/photo_test.js http://localhost:8766/index.html      (serve the built site first, as for smoke.js)
// Run it after changing wikiTitle(), photoBy(), placePhoto(), photoBox(), the .dphoto styles or the wikiPhotos setting.
// Wikipedia and Wikimedia Commons are never reached (the app asks only Wikipedia; Commons is checked to stay unasked): every request to them is answered here, and counted. What it holds
// the app to:
//   1. a place whose Wikipedia article has coordinates and a free photo shows that photo, credited (photographer, licence,
//      a link to the file on Commons);
//   2. a Commons credit that is a whole banner of HTML gives way to the photographer's name;
//   3. no photo when the article has no coordinates (a person, a list), when they are far from the pin, when the article
//      is the one on the town, when the picture is an .svg drawing or a map,
//      or when Commons gives no photographer or licence;
//   4. a place with no Wikipedia link, or a link to a list, asks nothing;
//   5. with the setting off nothing is asked and nothing shown; the setting is under the gear;
//   6. a failed request shows nothing and breaks nothing.
const { chromium } = require('playwright');
(async()=>{
  const fails=[]; const ok=(name,cond,extra)=>{ console.log((cond?'ok   ':'FAIL ')+name+(extra!==undefined?'  ['+extra+']':'')); if(!cond) fails.push(name); };
  const url=process.argv[2]||'http://localhost:8766/index.html'; const b=await chromium.launch(); const errs=[];
  const PNG=Buffer.from('iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mNk+M9QDwADhgGAWjR9awAAAABJRU5ErkJggg==','base64');
  let MODE='good', asked={wiki:0,commons:0,img:0}, CUR={};
  const wikiAnswer=title=>{ const pg={pageid:1,ns:0,title:MODE==='town'?CUR.town:CUR.name};
    if(MODE!=='nocoord') pg.coordinates=[{lat:CUR.lat+(MODE==='far'?0.05:0.001),lon:CUR.lon,primary:'',globe:'earth'}];
    const f=MODE==='svg'?'Some_building.svg':MODE==='map'?'Some_building_location_map.png':'Some_building_1.jpg';
    pg.thumbnail={source:'https://upload.wikimedia.org/test/'+f+'.png',width:900,height:550}; pg.pageimage=f;
    return {batchcomplete:'',query:{pages:{'1':pg}}}; };
  const commonsAnswer=()=>{ const m={};
    if(MODE==='banner') m.Artist={value:'<table><tr><td><img src="https://upload.wikimedia.org/test/banner.png"><big>This image was taken by <b><a href="//commons.wikimedia.org/wiki/User:Example" title="User:Example">Ann Example</a></b>. To see her whole portfolio, <a href="//commons.wikimedia.org/wiki/Category:Images">click here</a>. More words to make this long.</big></td></tr></table>'};
    else if(MODE==='longcredit') m.Artist={value:'The Example County Historical Society and Museum of Local Industry, Photograph Collection, Box 14, Folder 3'};
    else if(MODE==='emptycredit') m.Artist={value:'<span></span>'};
    else if(MODE==='mailcredit') m.Artist={value:'Ann Example (ann.example'+AT_+'example.org)'};
    else if(MODE==='onlymail') m.Artist={value:'<a href="mailto:ann'+AT_+'example.org">ann'+AT_+'example.org</a>'};
    else if(MODE!=='nocredit') m.Artist={value:'<a href="//commons.wikimedia.org/wiki/User:Example">Ann Example</a>'};
    if(MODE!=='nocredit') m.LicenseShortName={value:'CC BY-SA 4.0'};
    return {query:{pages:{'-1':{ns:6,title:'File:Some_building_1.jpg',imageinfo:[{url:'https://upload.wikimedia.org/x.jpg',descriptionurl:'https://commons.wikimedia.org/wiki/File:Some_building_1.jpg',extmetadata:m}]}}}}; };
  const AT_=String.fromCharCode(64);      // the at sign, put together here so that no address is written in this file (check.py looks for them)
  let STORED={};      // what data/photos.json holds for this page: nothing, unless a test says otherwise
  const open=async set=>{ const c=await b.newContext({viewport:{width:390,height:844},isMobile:true,hasTouch:true}); const p=await c.newPage(); p.on('pageerror',e=>errs.push(e.message));
    await c.route(u=>/\/data\/photos\.json/.test(u.pathname),r=>r.fulfill({status:200,contentType:'application/json',body:JSON.stringify({asof:'2026-11-19',p:STORED})}));
    await c.route(u=>!/^http:\/\/localhost/.test(u.href),r=>{ const u=new URL(r.request().url());
      if(u.host==='en.wikipedia.org'&&u.pathname==='/w/api.php'&&u.searchParams.get('prop')==='imageinfo'){ asked.commons++; return r.fulfill({status:200,contentType:'application/json',headers:{'access-control-allow-origin':'*'},body:JSON.stringify(commonsAnswer())}); }
      if(u.host==='en.wikipedia.org'&&u.pathname==='/w/api.php'){ asked.wiki++; if(MODE==='fail') return r.fulfill({status:500,body:''}); return r.fulfill({status:200,contentType:'application/json',headers:{'access-control-allow-origin':'*'},body:JSON.stringify(wikiAnswer(u.searchParams.get('titles')))}); }
      if(u.host==='commons.wikimedia.org'){ asked.other=(asked.other||0)+1; return r.fulfill({status:500,body:''}); }
      if(u.host==='upload.wikimedia.org'){ asked.img++; return r.fulfill({status:200,contentType:'image/png',body:PNG}); }
      return r.fulfill({status:204,body:''}); });
    await p.addInitScript(s=>{ try{ localStorage.setItem('lost-hidden-atlas-v1',JSON.stringify({v:1,home:{id:'alb',by:1},set:s})); }catch(e){} },set||{});
    await p.goto(url); await p.waitForFunction(()=>window.__atlasNM); await p.waitForTimeout(300); return {c,p}; };
  const show=async(p,id)=>{ asked={wiki:0,commons:0,img:0}; CUR=await p.evaluate(id=>{ const s=window.__atlasNM.sites().find(x=>x.id===id); return {lat:s.lat,lon:s.lon,name:s.name,town:(s.town||'').split(',')[0]}; },id); await p.evaluate(id=>{ location.hash='#'+id; },id); await p.waitForTimeout(700);
    return p.evaluate(()=>{ const f=document.querySelector('#v-detail .dphoto'); return {box:!!f,shown:!!f&&!f.hidden,img:f&&f.querySelector('img')?f.querySelector('img').getAttribute('src'):null,cap:f&&f.querySelector('figcaption')?f.querySelector('figcaption').textContent:'',link:f&&f.querySelector('figcaption a')?f.querySelector('figcaption a').href:''}; }); };
  let {c,p}=await open();
  const pick=await p.evaluate(()=>{ const S=window.__atlasNM.sites(), w=s=>(s.links||[]).map(l=>l[1]||'').filter(u=>/en\.wikipedia\.org\/wiki\//.test(u));
    const wiki=S.filter(s=>w(s).some(u=>!/\/wiki\/(List_of|Lists_of|National_Register_of_Historic_Places_listings)/i.test(u)&&!/\/wiki\/[^\/]*:/.test(decodeURIComponent(u.split('/wiki/')[1]||''))));
    const none=S.filter(s=>!w(s).length&&!s.mine), list=S.filter(s=>w(s).length&&w(s).every(u=>/\/wiki\/List_of/i.test(u)));
    return {wiki:wiki.filter(s=>s.town&&!s.name.toLowerCase().includes(s.town.split(',')[0].toLowerCase())).map(s=>s.id).slice(0,14),none:(none[0]||{}).id,list:(list[0]||{}).id,nwiki:wiki.length,all:S.length}; });
  ok('there are places with a Wikipedia link to try',pick.wiki.length>=14&&pick.none,JSON.stringify({nwiki:pick.nwiki,all:pick.all,list:pick.list}));
  // 1
  MODE='good'; let r=await show(p,pick.wiki[0]);
  ok('a place whose article has coordinates and a free photo shows it',r.shown&&/Some_building_1\.jpg/.test(r.img||''),JSON.stringify(r));
  ok('credited with the photographer, the licence and a link to the file on Commons',/Ann Example/.test(r.cap)&&/CC BY-SA 4\.0/.test(r.cap)&&/commons\.wikimedia\.org\/wiki\/File:Some_building_1\.jpg/.test(r.link),r.cap);
  ok('two questions, both to Wikipedia (the article, then the file\'s credit), none to Commons',asked.wiki===1&&asked.commons===1&&!asked.other,JSON.stringify(asked));
  // 2
  MODE='banner'; r=await show(p,pick.wiki[1]);
  ok('a credit that is a whole banner gives way to the photographer\'s name',r.shown&&/Photo: Ann Example · CC BY-SA 4\.0/.test(r.cap)&&/^From Wikipedia's article on /.test(r.cap)&&!/portfolio/.test(r.cap),r.cap);
  ok('the banner\'s own images are not fetched',asked.img<=1,JSON.stringify(asked));
  MODE='longcredit'; r=await show(p,pick.wiki[9]);
  ok('a long plain credit is cut short, not dropped',r.shown&&/Photo: The Example County Historical Society.{10,50}… · CC BY-SA 4\.0/.test(r.cap),r.cap);
  const dim=await p.evaluate(()=>{ const i=document.querySelector('#v-detail .dphoto img'); return i?[i.getAttribute('width'),i.getAttribute('height')]:null; });
  ok('the picture carries its size, so its box is the right height before it arrives',dim&&dim[0]==='900'&&dim[1]==='550',JSON.stringify(dim));
  // 3
  MODE='emptycredit'; r=await show(p,pick.wiki[8]); ok('no photo when the credit is empty markup',!r.shown);
  MODE='mailcredit'; r=await show(p,pick.wiki[12]); ok('a credit that carries an e-mail address is shown without it',r.shown&&/Photo: Ann Example · /.test(r.cap)&&!/@/.test(r.cap),r.cap.slice(-70));
  MODE='onlymail'; r=await show(p,pick.wiki[13]); ok('no photo when the credit is nothing but an e-mail address',!r.shown);
  MODE='nocoord'; r=await show(p,pick.wiki[2]); ok('no photo when the article has no coordinates',!r.shown&&asked.commons===0,JSON.stringify(asked));
  MODE='svg'; r=await show(p,pick.wiki[3]); ok('no photo when the picture is an .svg drawing',!r.shown&&asked.commons===0);
  MODE='map'; r=await show(p,pick.wiki[4]); ok('no photo when the picture is a location map',!r.shown&&asked.commons===0);
  MODE='far'; r=await show(p,pick.wiki[7]); ok('no photo when the article\'s coordinates are 5 km from the pin',!r.shown&&asked.commons===0);
  MODE='town'; r=await show(p,pick.wiki[10]); ok('no photo when the article is the one on the town',!r.shown&&asked.commons===0,CUR.town);
  MODE='nocredit'; r=await show(p,pick.wiki[5]); ok('no photo when Commons gives no photographer or licence',!r.shown&&asked.commons===1);
  // 4
  MODE='good'; r=await show(p,pick.none); ok('a place with no Wikipedia link asks nothing',!r.box&&asked.wiki===0,JSON.stringify(asked));
  if(pick.list){ r=await show(p,pick.list); ok('a link only to a list article asks nothing',!r.box&&asked.wiki===0,pick.list); }
  // 6
  MODE='fail'; r=await show(p,pick.wiki[6]||pick.wiki[0]); ok('a failed request shows nothing',!r.shown);
  // back to the first place: kept, not asked again
  MODE='good'; r=await show(p,pick.wiki[0]); ok('a photo once found is not asked for again',r.shown&&asked.wiki===0,JSON.stringify(asked));
  await c.close();
  // 5
  ({c,p}=await open({wikiPhotos:false})); MODE='good'; r=await show(p,pick.wiki[0]);
  ok('setting off: nothing asked, nothing shown',!r.box&&asked.wiki===0,JSON.stringify(asked));
  await p.click('#lb-opt'); await p.waitForTimeout(250);
  await p.evaluate(()=>{ const g=[...document.querySelectorAll('#sheet button')].find(x=>/settings/i.test(x.getAttribute('aria-label')||x.textContent)); if(g) g.click(); }); await p.waitForTimeout(300);
  const st=await p.evaluate(()=>/Photos from Wikipedia on place pages/.test(document.querySelector('#sheet').textContent));
  ok('the setting is under the gear',st);
  // photo details stored ahead of time (tools/photos.py): shown at once, with their room kept, and Wikipedia is asked nothing
  await c.close();
  STORED={}; STORED[pick.wiki[0]]=['https://upload.wikimedia.org/stored/900px-Stored.jpg',900,600,'Sam Stored','CC BY 4.0','https://commons.wikimedia.org/wiki/File:Stored.jpg','Stored Article']; STORED[pick.wiki[1]]=0; STORED[pick.none]=['https://upload.wikimedia.org/found/900px-Found.jpg',900,600,'Fay Found','CC BY-SA 4.0','https://commons.wikimedia.org/wiki/File:Found.jpg',''];      /* found on Wikimedia Commons near the pin (tools/photo_find.py): no article */
  ({c,p}=await open()); MODE='good';
  await p.waitForFunction(()=>true); await p.waitForTimeout(3200);          // the file is fetched a moment after the page opens
  r=await show(p,pick.wiki[0]);
  ok('a place whose photo details are stored shows the picture with its credit',r.shown&&r.img==='https://upload.wikimedia.org/stored/900px-Stored.jpg'&&/Stored Article/.test(r.cap)&&/Sam Stored · CC BY 4\.0/.test(r.cap)&&/commons\.wikimedia\.org\/wiki\/File:Stored\.jpg/.test(r.link),r.cap.slice(0,90));
  ok('and Wikipedia is asked nothing for it',asked.wiki===0&&asked.commons===0,JSON.stringify(asked));
  ok('its room is kept from the first frame: the picture carries its size',await p.evaluate(()=>{ const i=document.querySelector('#v-detail .dphoto img'); return !!i&&i.getAttribute('width')==='900'&&i.getAttribute('height')==='600'; }));
  { const sync=await p.evaluate(id=>{ location.hash='#'; location.hash='#'+id; return new Promise(res=>{ const t0=performance.now(); const tick=()=>{ const f=document.querySelector('#v-detail .dphoto'); if(f&&!f.hidden&&f.querySelector('img')) return res(true); if(performance.now()-t0>600) return res(false); requestAnimationFrame(tick); }; setTimeout(tick,0); }); },pick.wiki[0]);
    ok('opened again, the picture is there as the page is drawn',sync); }
  r=await show(p,pick.wiki[1]);
  ok('a place stored as "nothing usable" shows no picture and asks nothing',!r.shown&&asked.wiki===0,JSON.stringify(asked));
  r=await show(p,pick.wiki[2]);
  ok('a place the stored file does not hold is still looked up as before',r.shown&&asked.wiki===1&&asked.commons===1,JSON.stringify(asked));
  // ---- a picture found on Wikimedia Commons near the pin, for a place with no Wikipedia article at all
  { const f=await show(p,pick.none);
    ok('a place with no Wikipedia article shows the picture that was found for it on Wikimedia Commons',f.shown&&f.img==='https://upload.wikimedia.org/found/900px-Found.jpg',JSON.stringify(f).slice(0,120));
    ok('its credit names the photographer, the licence and Wikimedia Commons, and no article',/Fay Found · CC BY-SA 4\.0/.test(f.cap)&&/Wikimedia Commons/.test(f.cap)&&!/article/i.test(f.cap)&&/commons\.wikimedia\.org\/wiki\/File:Found\.jpg/.test(f.link),f.cap); }
  // ---- a tap on the picture shows it large, with its credit; another tap puts it away. And a button looks for more photos elsewhere.
  { await show(p,pick.wiki[0]);      /* the place whose photo is stored */
    const tap=()=>p.evaluate(()=>{ const i=document.querySelector('#v-detail .dphoto img'); if(i) i.click(); });
    const big=()=>p.evaluate(()=>{ const n=document.querySelector('#photobig'); if(!n||n.hidden) return null; const i=n.querySelector('img'), r=i.getBoundingClientRect(); return {src:i.getAttribute('src'),w:Math.round(r.width),cap:n.textContent,vw:innerWidth}; });
    await tap(); await p.waitForTimeout(400); const g=await big();
    ok('a tap on the picture opens it large over the page, asking for a bigger copy',!!g&&/\/1280px-Stored\.jpg$/.test(g.src),g?g.src:'no large view');
    ok('the large view carries the credit',!!g&&/Sam Stored/.test(g.cap)&&/CC BY 4\.0/.test(g.cap),g?g.cap.slice(0,80):'');
    await p.touchscreen.tap(200,700); await p.waitForTimeout(500);
    ok('a tap on it puts it away again',(await big())===null);
    // ---- the large picture can be pinched bigger (the owner, November 25, 2026), dragged about, and put away with its own button
    { const cdp=await p.context().newCDPSession(p); const tp=pts=>pts.map((q,i)=>({x:q[0],y:q[1],id:i}));
      const touch=async(type,pts)=>{ await cdp.send('Input.dispatchTouchEvent',{type,touchPoints:tp(pts)}); await p.waitForTimeout(40); };
      const st=()=>p.evaluate(()=>{ const n=document.querySelector('#photobig'); if(!n||n.hidden) return null; const i=n.querySelector('img'), m=new DOMMatrix(getComputedStyle(i).transform); return {w:m.a,l:m.e,page:visualViewport.scale,x:!!n.querySelector('button.pbx'),cap:n.querySelector('p').textContent}; });
      await tap(); await p.waitForTimeout(400); await p.evaluate(()=>{ const i=document.querySelector('#photobig img'); i.style.width=i.style.height='300px'; });   /* the test's picture is a dot: give it a size */
      const s0=await st();
      ok('pinch: the large view says it can be pinched and has a button to close it',!!s0&&s0.x&&/pinch/i.test(s0.cap),JSON.stringify(s0));
      await touch('touchStart',[[170,400],[220,400]]); await touch('touchMove',[[140,400],[250,400]]); await touch('touchMove',[[95,400],[295,400]]); await touch('touchEnd',[]); await p.waitForTimeout(200); const s1=await st();
      ok('pinch: two fingers spread apart make the picture bigger, not the page',!!s1&&s1.w>s0.w*2.5&&s1.page===1,JSON.stringify([s0&&s0.w,s1]));
      await touch('touchStart',[[200,400]]); await touch('touchMove',[[160,400]]); await touch('touchMove',[[120,400]]); await touch('touchEnd',[]); await p.waitForTimeout(200); const s2=await st();
      ok('pinch: one finger then slides the bigger picture about',!!s2&&s2.l<s1.l-50&&Math.abs(s2.w-s1.w)<.02,JSON.stringify([s1&&s1.l,s2&&s2.l]));
      await touch('touchStart',[[200,300]]); await touch('touchEnd',[]); await p.waitForTimeout(450);
      ok('pinch: a tap does not put a zoomed picture away',(await st())!==null);
      await touch('touchStart',[[200,300]]); await touch('touchEnd',[]); await touch('touchStart',[[200,300]]); await touch('touchEnd',[]); await p.waitForTimeout(450); const s3=await st();
      ok('pinch: a double tap takes it back to its first size',!!s3&&Math.abs(s3.w-1)<.02&&Math.abs(s3.l)<2,JSON.stringify([s0,s3]));
      await touch('touchStart',[[200,300]]); await touch('touchEnd',[]); await touch('touchStart',[[200,300]]); await touch('touchEnd',[]); await p.waitForTimeout(450); const s4=await st();
      ok('pinch: and a double tap on a picture at its first size makes it bigger',!!s4&&s4.w>s0.w*1.8,JSON.stringify(s4));
      await p.evaluate(()=>{ const x=document.querySelector('#photobig button.pbx'); x&&x.click(); }); await p.waitForTimeout(200);
      ok('pinch: the close button puts it away, zoomed or not',(await st())===null);
      await tap(); await p.waitForTimeout(400); const s5=await st();
      ok('pinch: opened again it is back at its first size',!!s5&&Math.abs(s5.w-1)<.02,JSON.stringify(s5));
      await touch('touchStart',[[200,700]]); await touch('touchEnd',[]); await p.waitForTimeout(450);
      ok('pinch: a single tap still puts an unzoomed picture away',(await st())===null); await cdp.detach();
      await tap(); await p.waitForTimeout(400); const bk=await p.evaluate(()=>window.atlasBack()); await p.waitForTimeout(150);
      ok('the phone\'s Back button puts the large picture away and leaves the place page open',bk===true&&(await st())===null&&await p.evaluate(()=>!!document.querySelector('#v-detail .dphoto img'))); }
    const more=await p.evaluate(()=>{ const a=document.querySelector('#v-detail #d-morephotos'); return a?{href:a.getAttribute('href'),t:a.textContent,target:a.getAttribute('target')}:null; });
    const nm=await p.evaluate(()=>{ const h=document.querySelector('#v-detail h2'); return h.dataset.full||h.textContent; });
    ok('the place page has a "More photos" link that searches for pictures of it by name, outside the Atlas',!!more&&/^https:\/\/www\.google\.com\/search\?/.test(more.href)&&/udm=2|tbm=isch/.test(more.href)&&decodeURIComponent(more.href.replace(/\+/g,' ')).indexOf(nm)>=0&&more.target==='_blank',more?more.href.slice(0,120):'no link'); }
  await c.close(); await b.close();
  ok('no page errors',!errs.length,errs.slice(0,3).join(' | '));
  console.log(fails.length?fails.length+' FAILED':'photo_test passed'); process.exit(fails.length?1:0);
})();
