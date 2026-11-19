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
    else if(MODE!=='nocredit') m.Artist={value:'<a href="//commons.wikimedia.org/wiki/User:Example">Ann Example</a>'};
    if(MODE!=='nocredit') m.LicenseShortName={value:'CC BY-SA 4.0'};
    return {query:{pages:{'-1':{ns:6,title:'File:Some_building_1.jpg',imageinfo:[{url:'https://upload.wikimedia.org/x.jpg',descriptionurl:'https://commons.wikimedia.org/wiki/File:Some_building_1.jpg',extmetadata:m}]}}}}; };
  const open=async set=>{ const c=await b.newContext({viewport:{width:390,height:844},isMobile:true,hasTouch:true}); const p=await c.newPage(); p.on('pageerror',e=>errs.push(e.message));
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
    return {wiki:wiki.filter(s=>s.town&&!s.name.toLowerCase().includes(s.town.split(',')[0].toLowerCase())).map(s=>s.id).slice(0,12),none:(none[0]||{}).id,list:(list[0]||{}).id,nwiki:wiki.length,all:S.length}; });
  ok('there are places with a Wikipedia link to try',pick.wiki.length>=12&&pick.none,JSON.stringify({nwiki:pick.nwiki,all:pick.all,list:pick.list}));
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
  await c.close(); await b.close();
  ok('no page errors',!errs.length,errs.slice(0,3).join(' | '));
  console.log(fails.length?fails.length+' FAILED':'photo_test passed'); process.exit(fails.length?1:0);
})();
