(function(){
'use strict';
/* ---------- data ---------- */
const D=JSON.parse(document.getElementById('d-sites').textContent);
const BASE=D.sites, HUBS=D.hubs;
let TOPO=null;
/* AT is set by boot.js when this runs inside the Android app; NATIVE means the phone's recorder is available too */
const AT=window.ATLAS||null, NATIVE=!!(AT&&AT.native);
const HOSTED=!document.getElementById('d-topo');   /* hosted copy: old maps, lines and leads are separate files fetched when needed */
const VQ=D.v?'?v='+D.v:'';
const topoImg=s=>{ if(!s||!s.tm) return null; if(HOSTED) return 'topo/'+s.id+'.webp'+(s.tm.v?'?'+s.tm.v:''); if(!TOPO){ try{TOPO=JSON.parse(document.getElementById('d-topo').textContent);}catch(e){TOPO={};} } return TOPO[s.id]?'data:image/webp;base64,'+TOPO[s.id]:null; };
/* the address of a place's old map; in the app it is fetched once and then kept on the phone, so this is a promise */
function topoSrc(s){ if(!s||!s.tm) return Promise.resolve(null); if(AT) return AT.topo(s.id,s.tm.v).catch(()=>null); return Promise.resolve(topoImg(s)); }
function topoWarm(list){ if(!HOSTED) return; list.forEach(x=>{ if(AT){ topoSrc(x); return; } const u=topoImg(x); if(u) fetch(u).catch(()=>{}); }); }

/* The kinds of place. This line is the one list: tools/check.py and tools/export.py read the codes, names and colours from it.
   What belongs in each kind is set out for research sessions in GUIDE.md section 4. */
const CAT={amuse:['Amusement & trolley parks','#d6338a'],hotel:['Hotels & resorts','#c8322b'],canal:['Canal works','#2f8fd0'],rail:['Railroads & trolleys','#4b4f54'],industry:['Mills, iron, brick & ice','#b4691f'],worship:['Places of worship','#9b1b45'],burial:['Burial grounds','#6b4fa0'],town:['Ghost, drowned & historic towns','#2e9e4a'],civic:['Civic & downtown buildings','#5c6bc0'],fort:['Forts & depots','#7a6a1e'],water:['Water works & buried creeks','#19a3b3'],inst:['Estates, institutions & parks','#1f4e79'],light:['Lighthouses','#f08a24'],landmark:['Houses, bridges & landmarks','#f2b705'],curio:['Curiosities & relics','#8db600'],lidar:['LiDAR finds, unverified','#00a88f']};
const ST={ruins:'Ruins you can see',traces:'Traces: grades, piers, earthworks',standing:'Still standing',marker:'Marker only',gone:'Nothing visible',water:'Under water'};
const STS={ruins:'Ruins',traces:'Traces',standing:'Standing',marker:'Marker only',gone:'Nothing visible',water:'Under water'};
const STRANK={ruins:0,standing:1,traces:2,marker:3,gone:4,water:5};
const PREC={exact:['Pin on the spot','On the structure or marker itself, within about 30 m.',30],site:['Pin within the site','Inside the documented footprint, within about 150 m.',150],area:['Pin approximate','Right vicinity, but the exact spot is not established. Scout it with the old map and LiDAR first.',500]};
/* How you get to see it. 'open' is a place you go into, at set times: a museum, a house shown by tour, a working inn or shop, a church that opens.
   tools/check.py and tools/export.py read this list from here. */
const ACC={public:'Public land or street',open:'Open to visitors, check hours',view:'View from the public way',ask:'Ask permission first',permit:'Permit required',boat:'On the water'};
const EFF={drive:'Drive-up',walk:'Short walk',hike:'Hike',boat:'Boat or shore view'};
const MY={'':'Not started',todo:'Want to scout',scouted:'Scouted online',asked:'Asked the owner',ok:'Have permission',visited:'Visited',filmed:'Filmed',skip:'Skip'};
/* states, their regions and start cities come from tools/states.py, so a new area needs no change here */
const STATES=D.states||[], REG={}, REG_STATE={}, STATE={other:'this area'};
STATES.forEach(st=>{ STATE[st.k]=st.name; st.regions.forEach(r=>{ REG[r[0]]=r[1]; REG_STATE[r[0]]=st.k; }); });
const HOLLOW={gone:1,marker:1,water:1};
const LOCAL=location.protocol==='file:';

/* ---------- helpers ---------- */
const $=(s,r)=>(r||document).querySelector(s);
function el(tag,a){
  const n=document.createElement(tag); let i=1;
  if(a&&typeof a==='object'&&!(a instanceof Node)&&!Array.isArray(a)){
    for(const k in a){ const v=a[k]; if(v==null||v===false) continue;
      if(k==='class') n.className=v; else if(k==='text') n.textContent=v;
      else if(k.slice(0,2)==='on') n.addEventListener(k.slice(2),v);
      else if(k==='style') n.style.cssText=v;
      else if(typeof v!=='string'&&k in n) n[k]=v;
      else n.setAttribute(k,v===true?'':v); }
    i=2; }
  for(;i<arguments.length;i++){ const c=arguments[i]; if(c==null||c===false) continue;
    if(Array.isArray(c)) c.forEach(x=>{ if(x!=null&&x!==false) n.append(x); }); else n.append(c); }
  return n;
}
/* a link out of the Atlas. Only a web address is ever made into one: an address from a place list, a reader's own place or a
   backup file that begins any other way (javascript:, data:) becomes a link that goes nowhere */
const webUrl=u=>/^https?:\/\//i.test(String(u||'').trim())?String(u).trim():'#';
const ext=(href,text,cls)=>el('a',{href:webUrl(href),target:'_blank',rel:'noopener noreferrer',class:cls||'',text:text});
const rad=x=>x*Math.PI/180;
function hav(a,b,c,d){ const R=3958.8,dl=rad(c-a),dn=rad(d-b),h=Math.sin(dl/2)**2+Math.cos(rad(a))*Math.cos(rad(c))*Math.sin(dn/2)**2; return 2*R*Math.asin(Math.sqrt(h)); }
const fmtMin=m=> m<60? m+' min' : Math.floor(m/60)+' h '+String(m%60).padStart(2,'0');
const ll=(p,n)=>p.lat.toFixed(n||5)+', '+p.lon.toFixed(n||5);
function copy(text,btn){ const done=()=>{ if(btn){ const t=btn.textContent; btn.textContent='Copied'; setTimeout(()=>btn.textContent=t,1200);} };
  try{ navigator.clipboard.writeText(text).then(done,()=>fallbackCopy(text,done)); }catch(e){ fallbackCopy(text,done); } }
function fallbackCopy(text,done){ const t=el('textarea',{style:'position:fixed;left:-999px;top:0'}); t.value=text; document.body.append(t); t.select(); try{document.execCommand('copy');done();}catch(e){} t.remove(); }
const debounce=(f,ms)=>{ let t; return function(){ const a=arguments; clearTimeout(t); t=setTimeout(()=>f.apply(null,a),ms); }; };

/* ---------- your saved data (this browser only) ---------- */
const LS='lost-hidden-atlas-v1';
const U0=()=>({v:1,home:{id:'alb'},status:{},notes:{},moved:{},custom:[],trip:[],fav:[],mute:[],visits:{},saved:{},dtc:null,me:{},logs:[],last:null,ui:{base:'streets',year:'Latest',light:'nw',hist:true,histOp:0.8,sort:'time',land:false,lots:false,leads:false,lines:{oldrail:false,canal:false,rail:false},split:0}});
let U=U0(), storeOK=true;
try{ const raw=localStorage.getItem(LS); if(raw){ const j=JSON.parse(raw); U=Object.assign(U0(),j); U.ui=Object.assign(U0().ui,j.ui||{}); U.ui.lines=Object.assign(U0().ui.lines,(j.ui||{}).lines||{}); if(U.ui.base==='lidar1') U.ui.base='lidar'; if(!U.me||typeof U.me!=='object') U.me={}; } }catch(e){ storeOK=false; }
/* ---- settings (the gear in the map options sheet). Stored in U.set; anything missing falls back to SET0. ---- */
const SET0={heat:true,pinchStand:true,addMore:false,dbl:3,wikiPhotos:true,quietGone:true,hideGone:false,nativeLeads:false,buzzVanished:false,theme:'auto',themeL:'brick',themeD:'tomorrow',units:'mi',clock:'auto',trk:'#2563eb',open:'last',start:'last',follow:true,autoPhotos:true,near:25,detail:'normal',buzz:true,trim:0,previews:true,autoBackup:true,kitBase:'topo',kitSign:'',cluster:true,tripStop:45};
const pref=k=>(U.set&&k in U.set)?U.set[k]:SET0[k];
const H12=()=>pref('clock')==='24'?false:pref('clock')==='12'?true:undefined;   /* undefined lets the phone's own setting decide */
const KM=()=>pref('units')==='km';
const fmtMi=(mi,dg)=>KM()?(mi*1.609344).toFixed(dg)+' km':(+mi).toFixed(dg)+' mi';            /* a distance measured in miles, shown in the chosen unit */
const miTxt=mi=>KM()?Math.round(mi*1.609344)+' km':mi+' mi';
const STEP=()=>({fine:2,normal:4,coarse:10})[pref('detail')]||4;                                 /* metres between saved track points */
/* Colour schemes: app.css has one block of colours for each. The reader chooses one light scheme and one dark scheme
   (themeL, themeD) and when each is used (theme: 'auto' lets the phone decide, 'light', 'dark'). To add a scheme: its
   block in app.css and a line here saying which kind it is; the two lists in Settings are made from this. */
const THEMES=[['brick','Brick and paper','l'],['slate','Slate and copper','l'],['survey','Survey green','l'],['daylight','Daylight, high contrast','l'],
  ['tomorrow','Tomorrow','d'],['oled','Tomorrow, true black (OLED)','d'],['morning','Tomorrow morning','d'],['blueprint','Blueprint night','d'],['black','Black and yellow, high contrast','d']];
const themeKind=k=>{ const t=THEMES.find(x=>x[0]===k); return t?t[2]:''; };
const DARKQ=window.matchMedia?window.matchMedia('(prefers-color-scheme: dark)'):null;
/* a build before November 18, 2026 kept one name in "theme" for mode and scheme together: split it once */
function themeMigrate(){ if(!U.set) return; if(U.set.trk==='#e11d74') delete U.set.trk;   /* the old pink is gone (November 18, 2026): back to the default */ const t=U.set.theme, k=themeKind(t); if(k==='l'){ U.set.themeL=t; U.set.theme='light'; } else if(k==='d'){ U.set.themeD=t; U.set.theme='dark'; } }
function themeNow(){ const m=pref('theme'), dark=m==='dark'||(m!=='light'&&!!(DARKQ&&DARKQ.matches));
  let k=dark?pref('themeD'):pref('themeL'); if(themeKind(k)!==(dark?'d':'l')) k=dark?'tomorrow':'brick'; return k; }
function applyTheme(){ themeMigrate(); const r=document.documentElement; r.setAttribute('data-theme',themeNow());
  try{ const m=document.querySelector('meta[name="theme-color"]'); if(m) m.setAttribute('content',getComputedStyle(r).getPropertyValue('--accent').trim()||'#a33a24'); }catch(e){} r.style.setProperty('--trk',pref('trk')); r.style.setProperty('--trk-ui',trkUI(r)); }
/* The track colour is also used on the panels (the Near arrow, the recording dot). Where it would not show against the
   panel, such as Black in a dark scheme, the text colour stands in. On the map the track keeps the colour chosen. */
function relLum(c){ let m=/^#([0-9a-f]{3}|[0-9a-f]{6})$/i.exec(String(c||'').trim()); if(!m) return null; let h=m[1]; if(h.length===3) h=h.replace(/./g,'$&$&');
  const v=[0,2,4].map(i=>parseInt(h.substr(i,2),16)/255).map(x=>x<=0.03928?x/12.92:Math.pow((x+0.055)/1.055,2.4)); return 0.2126*v[0]+0.7152*v[1]+0.0722*v[2]; }
function trkUI(r){ try{ const cs=getComputedStyle(r), t=pref('trk'), a=relLum(t), b=relLum(cs.getPropertyValue('--panel')); if(a==null||b==null) return t;
    return (Math.max(a,b)+0.05)/(Math.min(a,b)+0.05)<2?(cs.getPropertyValue('--ink').trim()||t):t; }catch(e){ return pref('trk'); } }
applyTheme();
if(DARKQ&&DARKQ.addEventListener) DARKQ.addEventListener('change',applyTheme);      /* the phone went to night mode, or back */
const save=debounce(()=>{ try{ localStorage.setItem(LS,JSON.stringify(U)); }catch(e){ storeOK=false; } },250);

/* No two pins for one place (the owner, November 21, 2026). A reader adds a place of their own, sends it in, and in time the
   public Atlas has it: their own copy would then sit on top of the public pin. So a place of the reader's own steps aside,
   kept but not shown, when a public place stands on the same spot: within 80 m of one marked "sent in by a reader", or within
   40 m of any public place once the reader has pressed Send for it (U.sent). "Show my copy" on the public place's page
   (U.keep) brings it back. The answer is worked out once and kept until the reader's places change. */
let twinKey=null, twinMap=new Map();
function twins(){ const C=U.custom||[], key=C.map(x=>x.id+':'+x.lat+','+x.lon).join('|')+'#'+Object.keys(U.sent||{}).join()+'#'+Object.keys(U.keep||{}).join();
  if(key===twinKey) return twinMap; twinKey=key; twinMap=new Map();
  C.forEach(m=>{ if((U.keep||{})[m.id]) return; const sent=!!(U.sent||{})[m.id], k=Math.cos(m.lat*Math.PI/180); let best=null, bd=1e9;
    for(const b of BASE){ const dy=(b.lat-m.lat)*111320; if(dy>80||dy<-80) continue; const dx=(b.lon-m.lon)*111320*k; if(dx>80||dx<-80) continue; const d=Math.hypot(dx,dy);
      if(d<bd&&((b.tip&&d<=80)||(sent&&d<=40))){ bd=d; best=b; } }
    if(best) twinMap.set(m.id,best.id); });
  return twinMap; }
const twinsOf=id=>{ const out=[]; twins().forEach((b,m)=>{ if(b===id) out.push(m); }); return out.map(m=>(U.custom||[]).find(x=>x.id===m)).filter(Boolean); };
const sites=()=>{ const T=twins(); return T.size?BASE.concat(U.custom.filter(x=>!T.has(x.id))):BASE.concat(U.custom); };
/* Ids that gave way to a fuller entry for the same place: {old id: new id} (was= in a place list). What a reader had saved
   against the old id (status, notes, a moved pin, visit reports, a trip stop, a field-log note's place) moves to the new one. */
const ALIAS=D.alias||{};
function aliasMigrate(){ let ch=false; Object.keys(ALIAS).forEach(o=>{ const n=ALIAS[o];
    ['status','notes','moved','visits'].forEach(k=>{ const m=U[k]; if(m&&Object.prototype.hasOwnProperty.call(m,o)){ if(!Object.prototype.hasOwnProperty.call(m,n)) m[n]=m[o]; delete m[o]; ch=true; } });
    ['trip','fav'].forEach(k=>{ if(Array.isArray(U[k])){ const i=U[k].indexOf(o); if(i>=0){ if(U[k].indexOf(n)<0) U[k][i]=n; else U[k].splice(i,1); ch=true; } } });
    (U.logs||[]).forEach(l=>(l.notes||[]).forEach(x=>{ if(x.pl===o){ x.pl=n; ch=true; } })); });
  if(ch) save(); }
aliasMigrate();
/* "Nothing to see": a place marked Nothing visible or Marker only. Under water is not counted: something can show at low water.
   Settings: quietGone (default on) keeps them from buzzing; hideGone (default off) takes them off the map, the lists and Near. */
const nothingToSee=s=>!!s&&(s.st==='gone'||s.st==='marker');
const byId=id=>sites().find(s=>s.id===id);
const pos=s=>{ const m=U.moved[s.id]; return m?{lat:m[0],lon:m[1]}:{lat:s.lat,lon:s.lon}; };
const dest=s=>s.th?{lat:s.th[0],lon:s.th[1]}:pos(s);
/* Nothing is measured from anywhere until the reader has a start place: one they chose (by 1), or the nearest start city to
   where their device said they were (by 2). The Atlas is used all over the map, so it does not open on one city's ground
   or count drive times from it for somebody who never asked. homeObj() still answers with the first start city then,
   for code that needs a point; nothing on the page shows it. */
const homePicked=()=>!!(U.home.by||U.home.id!=='alb');       /* 'alb' with no mark is only the value a fresh copy starts with; any other was chosen, by hand or by position */
const fromOK=()=>homePicked()||!!nearAt;                 /* a start place, or the reader's position while it is on */
function homeObj(){ if(U.home.id==='custom') return {id:'custom',name:U.home.name||'My spot',lat:U.home.lat,lon:U.home.lon}; return HUBS.find(h=>h.id===U.home.id)||HUBS[0]; }
const MAXB=[[17.5,-170.0],[72.0,-50.0]];
const inMap=(la,lo)=>la>=MAXB[0][0]&&la<=MAXB[1][0]&&lo>=MAXB[0][1]&&lo<=MAXB[1][1];
/* Until a start place is chosen by hand, it follows the nearest start city to where the reader is (or last was). */
function nearHome(ll,say){ if(!ll||U.home.by===1||U.home.id==='custom') return false; let b=null,bd=1e9; HUBS.forEach(h=>{ const d=hav(ll[0],ll[1],h.lat,h.lon); if(d<bd){ bd=d; b=h; } });
  if(!b||bd>300) return false;
  if(b.id===U.home.id){ if(!U.home.by){ U.home.by=2; save(); if(say){ buildHome(); drawHome(); refresh(); } } return false; }      /* already the nearest: it now counts as chosen */
  U.home={id:b.id,by:2}; save();
  if(say){ buildHome(); drawHome(); refresh(); banner('Drive times now count from '+b.name+', the nearest start city. Change it under the gear in Map options.',false,7000); } return true; }
const USBOX=[[24.5,-125],[49.5,-66.5]];                  /* the first view for somebody new: the whole country, pins grouped */
function startView(){ const v=U.ui.view, H=homeObj();
  if(pref('start')!=='home'&&v&&inMap(v[0],v[1])) return {c:[v[0],v[1]],z:Math.max(3,Math.min(20,v[2]||9))};
  if(!homePicked()) return {b:USBOX};
  return {c:[H.lat,H.lon],z:H.id==='custom'?11:10}; }
function setSpot(la,lo,name){ U.home={id:'custom',lat:+(+la).toFixed(5),lon:+(+lo).toFixed(5),by:1}; if(name) U.home.name=String(name).slice(0,60); save(); buildHome(); drawHome(); refresh(); banner('Working out drive times from '+(name||'your spot')+'…',false);
  fetchDT().then(ok=>{ banner(ok?'Drive times updated from '+(name||'your spot')+'.':'Could not reach the routing service, so times are rough estimates (marked ~).',!ok,5000); refresh(); }); }
/* A typed start place: "lat, lon" is read directly, anything else is looked up with OpenStreetMap's Nominatim. */
async function findSpot(q){ q=String(q||'').trim(); if(!q) return {err:'Type a town, an address, a ZIP code, or coordinates.'};
  const m=q.match(/^\s*(-?\d{1,2}(?:\.\d+)?)\s*[, ]\s*(-?\d{1,3}(?:\.\d+)?)\s*$/); let la,lo,name='';
  if(m){ la=+m[1]; lo=+m[2]; if(lo>0) lo=-lo; }
  else { try{ const r=await fetch('https://nominatim.openstreetmap.org/search?format=jsonv2&limit=1&countrycodes=us,ca&q='+encodeURIComponent(q)); const j=await r.json(); if(!j.length) return {err:'Nothing found for "'+q+'". Try a town and state, or coordinates like 39.10, -94.58.'}; la=+j[0].lat; lo=+j[0].lon; name=String(j[0].display_name||q).split(',').slice(0,2).join(',').trim(); }
    catch(e){ return {err:'Could not look that up (no connection?). Type coordinates like 39.10, -94.58, or choose "Pick a spot on the map".'}; } }
  if(!isFinite(la)||!isFinite(lo)||!inMap(la,lo)) return {err:'That is outside the area the Atlas covers.'};
  return {lat:la,lon:lo,name:name}; }
const homeKey=()=>{ const H=homeObj(); return H.lat.toFixed(4)+','+H.lon.toFixed(4); };
function roughMin(mi){ const road=mi*1.3, mph=road<8?26:road<35?40:50; return {min:Math.max(1,Math.round(road/mph*60)),mi:Math.round(road*10)/10}; }
/* Routed drive times from a start city come in a file of their own, data/dt/<city>-<stamp>.json, fetched the first time that city
   is the start place (they were a fifth of the page; tools/make.py). Until it arrives, and when it cannot be had, the time is the
   straight-line estimate, marked ~. A place that still carries its own table (the single-file copy, or older place data in the
   Android app) is read as before. */
const DTT={}, DTW={};
function dtLoad(h){ const x=(D.dtx||{})[h]; if(!x||DTT[h]||DTW[h]===true||(DTW[h]&&Date.now()-DTW[h]<60000)) return; DTW[h]=true; const p='data/dt/'+h+'-'+x+'.json';
  (AT?AT.fetch(p):fetch(p+'?v='+x)).then(r=>{ if(!r.ok) throw new Error('http '+r.status); return r.json(); })
    .then(j=>{ DTT[h]=j; DTW[h]=0; if(U.home.id===h){ refresh(); if(sel&&view==='detail') renderDetail(sel); } })
    .catch(()=>{ DTW[h]=Date.now(); }); }
try{ window.__atlasDT=h=>DTT[h]?Object.keys(DTT[h]).length:0; }catch(e){}
function dt(s){
  const h=U.home.id;
  if(h!=='custom'&&!U.moved[s.id]){ const T=DTT[h]; if(T&&T[s.id]) return {min:T[s.id][0],mi:T[s.id][1],est:false}; if(s.dt&&s.dt[h]) return {min:s.dt[h][0],mi:s.dt[h][1],est:false}; if(!T&&homePicked()) dtLoad(h); }      /* nobody who has not chosen a start place downloads a table */
  if(U.dtc&&U.dtc.key===homeKey()&&U.dtc.t[s.id]) return {min:U.dtc.t[s.id][0],mi:U.dtc.t[s.id][1],est:false};
  const H=homeObj(),d=dest(s),r=roughMin(hav(H.lat,H.lon,d.lat,d.lon)); return {min:r.min,mi:r.mi,est:true};
}
/* What "nearest" is measured from in the Places list: where the reader is, while their position is being followed (the
   location button), otherwise their start place. The position used is a snapshot, renewed only after a quarter of a mile,
   so the list does not reshuffle under a thumb. From a live position the time is a rough estimate, marked ~. */
let nearAt=null, listFrom=null;
function nearFrom(){ const g=(typeof geo==='object'&&geo)?geo.ll:null; if(g){ if(!nearAt||hav(nearAt[0],nearAt[1],g[0],g[1])>0.25) nearAt=[g[0],g[1]]; } else nearAt=null; return nearAt; }
function dtl(s){ if(!nearAt) return dt(s); const d=dest(s), r=roughMin(hav(nearAt[0],nearAt[1],d.lat,d.lon)); return {min:r.min,mi:r.mi,est:true,live:true}; }
/* called when the position moves or is switched off: redo the list if its origin has changed */
/* A place page that is open is left alone (it may hold a half-written visit report); it shows the new origin when next opened. */
function nearMoved(){ const was=nearAt, now=nearFrom(); if(was===now) return; if(view==='trip'){ trip.real=null; renderTrip(); }      /* the estimate starts where the reader is */
  if(F.max&&view!=='detail') refresh(); else if(view==='list') renderList(); }
async function fetchDT(){
  const H=homeObj(),key=homeKey(),all=sites(),t={};
  try{
    for(let k=0;k<all.length;k+=80){
      const ch=all.slice(k,k+80);
      const coords=[H].concat(ch.map(dest)).map(p=>p.lon.toFixed(5)+','+p.lat.toFixed(5)).join(';');
      const r=await fetch('https://router.project-osrm.org/table/v1/driving/'+coords+'?sources=0&annotations=duration,distance');
      const j=await r.json(); if(j.code!=='Ok') throw new Error('route');
      ch.forEach((s,i)=>{ const du=j.durations[0][i+1], di=j.distances[0][i+1]; if(du!=null&&di!=null) t[s.id]=[Math.round(du/60),Math.round(di/160.934)/10]; });   /* no road (an island): leave it to the rough estimate */
    }
    U.dtc={key:key,t:t}; save(); return true;
  }catch(e){ return false; }
}

/* ---------- filters ---------- */
/* Favourites: the reader's own short list of the places they care most about (U.fav, ids in the order added; kept in this
   browser like the trip). A favourite's pin wears a white ring, is never folded into a grey group disc however far out the
   map is, and is never hidden as "nothing to see". Filters has "My favourites" to list them. */
const isFav=id=>Array.isArray(U.fav)&&U.fav.indexOf(id)>=0;
function favToggle(s){ if(!Array.isArray(U.fav)) U.fav=[]; const i=U.fav.indexOf(s.id); if(i>=0) U.fav.splice(i,1); else U.fav.push(s.id); save(); refresh(); return i<0; }
const F={fav:false,line:null,q:'',cat:new Set(),st:new Set(),reg:'',acc:new Set(),eff:new Set(),max:0,tag:'',now:false,lead:false,oldmap:false,pub:false,brick:false,tip:false,before:0,fresh:'',my:'any',hideDone:false};
/* Searching. Each place's words are gathered once, lower-cased and with accents removed: its names, its town, and the
   rest (years, kind, what is left, region, the texts, the access note, series tags). Every word typed must be found
   somewhere. In the list, places with all the words in their name come first, then name or town, then the rest. */
const HAY=new Map(), fold=x=>String(x||'').toLowerCase().normalize('NFD').replace(/[\u0300-\u036f]/g,'');
function hay(s){ let h=HAY.get(s.id); if(!h||h.s!==s){ h={s:s,n:fold(s.name+' '+(s.name2||'')),t:fold(s.town),
  x:fold([s.years,(CAT[s.cat]||[])[0],STS[s.st],REG[s.reg],s.hook,s.story,s.look,s.accn,s.hrs,Array.isArray(s.tags)?s.tags.join(' '):s.tags,s.bk==='y'?'red brick':s.bk==='s'?'some red brick':'',s.tip?'sent in by a reader':''].filter(Boolean).join(' '))}; HAY.set(s.id,h); } return h; }
let qMemo=['',[]];
function qWords(){ if(qMemo[0]!==F.q) qMemo=[F.q,fold(F.q).split(/\s+/).filter(Boolean)]; return qMemo[1]; }
function qTier(s){ const h=hay(s), w=qWords(); return w.every(x=>h.n.indexOf(x)>=0)?0:w.every(x=>h.n.indexOf(x)>=0||h.t.indexOf(x)>=0)?1:2; }
/* hidden by "Hide places with nothing to see"? Not when its chip is chosen in Filters, not the place that is open, and not a stop on the trip */
const goneHid=s=>pref('hideGone')&&nothingToSee(s)&&!F.st.has(s.st)&&!(sel&&sel.id===s.id)&&U.trip.indexOf(s.id)<0&&!isFav(s.id);
function match(s){ return !goneHid(s)&&match0(s); }
function match0(s){
  if(F.line&&!F.line.ids.has(s.id)) return false;
  if(F.q){ const h=hay(s); if(!qWords().every(w=>h.n.indexOf(w)>=0||h.t.indexOf(w)>=0||h.x.indexOf(w)>=0)) return false; }
  if(F.cat.size&&!F.cat.has(s.cat)) return false;
  if(F.st.size&&!F.st.has(s.st)) return false;
  if(F.reg&&s.reg!==F.reg) return false;
  if(F.acc.size&&!F.acc.has(s.acc)) return false;
  if(F.eff.size&&!F.eff.has(s.eff)) return false;
  if(F.max&&fromOK()&&dtl(s).min>F.max) return false;
  if(F.now&&!s.now) return false;
  if(F.lead&&!(s.conf==='lead'||s.conf==='mixed'||s.prec==='area')) return false;
  if(F.oldmap&&!s.tm) return false;
  if(F.before){ const y=yearOf(s); if(!y||y>=F.before) return false; }      /* a place with no year it dates from is left out, not guessed */
  if(F.fav&&!isFav(s.id)) return false;
  if(F.tip&&!s.tip) return false;      /* a place that began as a reader's tip carries the day it was sent */
  if(F.brick&&s.bk!=='y'&&s.bk!=='s') return false;      /* red brick: bk is y (mostly), s (some), n (none); absent when nobody has looked */
  if(F.pub&&!(s.pl&&s.pl[2]==='OA')) return false;
  if(F.fresh&&s.new!==F.fresh) return false;
  const my=U.status[s.id]||'';
  if(F.my==='mine'){ if(!s.mine) return false; } else if(F.my!=='any'&&my!==F.my) return false;
  if(F.hideDone&&(my==='filmed'||my==='skip')) return false;
  return true;
}
/* The year a place dates from: the earliest year in its "years" text ("1764", "c. 1750–1924", "1840s", "18th century").
   Text that opens with what ended it ("razed 1962", "flooded 1950s") gives none: that year is not when it was built. */
const YEAR=new Map();
function yearOf(s){ if(YEAR.has(s.id)) return YEAR.get(s.id); const t=String(s.years||''); let y=0;
  if(!/^\s*(razed|burned|flooded|filled|piped|closed|demolished|drowned|lost|gone|removed)/i.test(t)){
    (t.match(/(1[5-9]\d\d|20[0-2]\d)(?!\d)/g)||[]).forEach(m=>{ if(!y||+m<y) y=+m; });
    const c=/(\d\d)(st|nd|rd|th) century/i.exec(t); if(c){ const v=(+c[1]-1)*100; if(!y||v<y) y=v; } }
  YEAR.set(s.id,y); return y; }
function activeCount(){ return (F.line?1:0)+(F.q?1:0)+F.cat.size+F.st.size+(F.reg?1:0)+F.acc.size+F.eff.size+(F.max?1:0)+(F.now?1:0)+(F.lead?1:0)+(F.oldmap?1:0)+(F.pub?1:0)+(F.brick?1:0)+(F.tip?1:0)+(F.fav?1:0)+(F.before?1:0)+(F.fresh?1:0)+(F.my!=='any'?1:0)+(F.hideDone?1:0); }
function syncFcount(){ const n=activeCount()-(F.q?1:0), b=$('#filt-btn'); $('#fcount').textContent=n?String(n):''; b.classList.toggle('on',n>0); b.setAttribute('aria-expanded',String($('#filters').open)); b.setAttribute('aria-label',n?'Filters, '+n+' on':'Filters'); }
function clearF(){ setLine(null,true); F.q='';F.cat.clear();F.st.clear();F.reg='';F.acc.clear();F.eff.clear();F.max=0;F.now=false;F.lead=false;F.oldmap=false;F.pub=false;F.brick=false;F.tip=false;F.fav=false;F.before=0;F.fresh='';F.my='any';F.hideDone=false; }
/* batches of places, oldest first; each data file names its own, so a new state needs no change here */
const BATCHES=D.batches||[];
const PRESETS=(BATCHES.length?[['Newest: '+BATCHES[BATCHES.length-1].label,()=>{ F.fresh=BATCHES[BATCHES.length-1].key; }]]:[]).concat([
  ['My favourites',()=>{ F.fav=true; }],
  ['Ruins you can walk to',()=>{ F.st.add('ruins');F.st.add('traces');F.acc.add('public'); }],
  ['Standing, from before 1800',()=>{ F.st.add('standing'); F.before=1800; }],
  ['Red brick',()=>{ F.brick=true; }],
  /* with no start place there is nothing to count 30 minutes from: it used to switch on, show "Filters 1" and leave every place in the list */
  ['Within 30 min',()=>{ if(!fromOK()){ banner('Say where you start first: "Use my location" or "Choose a place" on the Places tab. Drive times count from there.',true,8000); return; } F.max=30; }],
  ['Changing now',()=>{ F.now=true; }],
  ['Places of worship',()=>{ F.cat.add('worship'); }],
  ['Houses, bridges & landmarks',()=>{ F.cat.add('landmark'); }],
  ['Pins to confirm',()=>{ F.lead=true; }]
]);
function chipGroup(label,map,set,colors){
  const g=el('div',{class:'fgrp'},el('span',{class:'lbl',text:label}));
  const box=el('div',{class:'chips'});
  Object.keys(map).forEach(k=>{
    const name=Array.isArray(map[k])?map[k][0]:map[k];
    const b=el('button',{class:'chip',type:'button','aria-pressed':set.has(k)?'true':'false',onclick:()=>{ set.has(k)?set.delete(k):set.add(k); refresh(); }},
      colors?el('span',{class:'dot',style:'--c:'+map[k][1]}):null,name);
    box.append(b);
  });
  g.append(box); return g;
}
function buildFilters(){
  const fb=$('#fbody'); fb.textContent='';
  /* shortcuts: each clears the filters and sets one common combination */
  fb.append(el('div',{class:'fgrp'},el('span',{class:'lbl',text:'Shortcuts'}),el('div',{class:'chips',id:'presets'},PRESETS.map(p=>el('button',{class:'chip',type:'button',onclick:()=>{clearF();$('#q').value='';p[1]();refresh();}},p[0])))));
  fb.append(chipGroup("What's left to see",STS,F.st));
  fb.append(chipGroup('Kind of place',CAT,F.cat,true));
  const reg=el('select',{id:'f-reg',onchange:e=>{F.reg=e.target.value;refresh();}},el('option',{value:'',text:'All regions'}),STATES.map(st=>{ const used=st.regions.filter(r=>BASE.some(x=>x.reg===r[0])); return used.length?el('optgroup',{label:st.name},used.map(r=>el('option',{value:r[0],text:r[1]}))):null; }));
  reg.value=F.reg;
  const max=el('select',{id:'f-max',onchange:e=>{F.max=+e.target.value;refresh();}},[[0,'Any drive'],[15,'15 min or less'],[30,'30 min or less'],[45,'45 min or less'],[60,'1 hour or less'],[90,'1½ hours or less'],[120,'2 hours or less']].map(o=>el('option',{value:String(o[0]),text:o[1]})));
  max.value=String(F.max);
  fb.append(el('div',{class:'row'},el('label',{class:'field'},el('span',{text:'Region'}),reg),el('label',{class:'field'},el('span',{text:'Drive time'}),max)));
  fb.append(chipGroup('Access',ACC,F.acc));
  fb.append(chipGroup('Effort',EFF,F.eff));
  const my=el('select',{id:'f-my',onchange:e=>{F.my=e.target.value;refresh();}},el('option',{value:'any',text:'Any'}),Object.keys(MY).map(k=>el('option',{value:k,text:MY[k]})),el('option',{value:'mine',text:'Places I added'}));
  my.value=F.my;
  const bef=el('select',{id:'f-before',onchange:e=>{F.before=+e.target.value;refresh();}},[[0,'Any age'],[1700,'Before 1700'],[1750,'Before 1750'],[1800,'Before 1800'],[1850,'Before 1850'],[1900,'Before 1900']].map(o=>el('option',{value:String(o[0]),text:o[1]})));
  bef.value=String(F.before);
  fb.append(el('div',{class:'row'},el('label',{class:'field'},el('span',{text:'My progress'}),my)));
  fb.append(el('label',{class:'field'},el('span',{text:'Dates from'}),bef));
  if(BATCHES.length){ const bs=el('select',{id:'f-batch',onchange:e=>{F.fresh=e.target.value;refresh();}},el('option',{value:'',text:'Any time'}),BATCHES.slice().reverse().map(b=>el('option',{value:b.key,text:b.label+' ('+b.n+')'}))); bs.value=F.fresh; fb.append(el('label',{class:'field'},el('span',{text:'Added in'}),bs)); }
  const tog=(label,key)=>el('button',{class:'chip',type:'button','aria-pressed':F[key]?'true':'false',onclick:()=>{F[key]=!F[key];refresh();}},label);
  fb.append(el('div',{class:'fgrp'},el('span',{class:'lbl',text:'Only show'}),el('div',{class:'chips'},tog('My favourites','fav'),tog('Changing right now','now'),tog('Leads and rough pins','lead'),tog('Has an old map overlay','oldmap'),tog('Red brick to see','brick'),tog('Sent in by readers','tip'),tog('On open public land','pub'),tog('Hide filmed and skipped','hideDone'))));
  /* the way out of a long panel: close it and go to the list */
  fb.append(el('div',{class:'row fdone'},el('button',{class:'btn pri',type:'button',id:'f-done',onclick:()=>{ $('#filters').open=false; syncFcount(); const t=$('#v-list'); if(t&&t.scrollIntoView) t.scrollIntoView({block:'start'}); }},'Show '+visible.length+(visible.length===1?' place':' places')),
    el('button',{class:'btn sm',type:'button',onclick:()=>{clearF();$('#q').value='';refresh();}},'Clear all filters')));
}

/* ---------- list ---------- */
let visible=[], listAll=false, listKey=''; const LISTCAP=120;
function sortSites(a){
  const ok=fromOK(), k=!ok&&U.ui.sort==='time'?'reg':U.ui.sort;      /* nowhere to count from yet: by region, then name */
  const t=new Map(a.map(s=>[s.id,ok?dtl(s).min:0]));
  if(F.line){ a.sort((x,y)=>F.line.ord.get(x.id)-F.line.ord.get(y.id)); return a; }
  if(k==='name') a.sort((x,y)=>x.name.localeCompare(y.name));
  else if(k==='reg') a.sort((x,y)=>(REG[x.reg]||'').localeCompare(REG[y.reg]||'')||x.name.localeCompare(y.name));
  else if(k==='left') a.sort((x,y)=>STRANK[x.st]-STRANK[y.st]||t.get(x.id)-t.get(y.id)||x.name.localeCompare(y.name));
  else a.sort((x,y)=>t.get(x.id)-t.get(y.id));
  if(F.q){ const tier=new Map(a.map(s=>[s.id,qTier(s)])); a.sort((x,y)=>tier.get(x.id)-tier.get(y.id)); }      /* the sort keeps the chosen order inside each tier */
  return a;
}
/* Shown at the head of the list, and in the trip builder, until there is a start place. */
function startCard(must){ const pick=()=>{ openSettings(); setTimeout(()=>{ const n=$('#set-home'); if(n){ n.scrollIntoView({block:'center'}); n.focus(); } },80); };
  return el('div',{class:'startcard',id:'startcard'},
    el('b',{text:'Where are you starting from?'}),
    el('p',{text:'Drive times and "nearest first" count from there.'}),
    el('div',{class:'row'},
      el('button',{class:'btn sm',type:'button',id:'sc-me',onclick:()=>{ if(!map){ banner('Your location needs the map, and the map has not loaded. Choose a place instead.',true,7000); return; } if(geo.id===null){ geo.wide=true; locate(); } }},'Use my location'),
      el('button',{class:'btn sm',type:'button',id:'sc-pick',onclick:pick},'Choose a place'),
      must?null:el('button',{class:'later',type:'button',id:'sc-no',onclick:()=>{ U.ui.noStart=1; save(); renderList(); }},'Not now'))); }
/* the little shape beside a name, the same as the pin: a star for standing, a ring for nothing left, a diamond for a place of the reader's own */
function dot(s){ return el('span',{class:'dot'+(HOLLOW[s.st]?' hollow':'')+(s.mine?' mine':s.st==='standing'?' star':''),style:'--c:'+((CAT[s.cat]||CAT.landmark)[1])}); }
function renderList(){
  listFrom=nearFrom();
  { const o=$('#sort').options[0], n=homeObj().name||'your start'; o.textContent=nearAt?'Nearest to you':!homePicked()?'Nearest first':'Nearest to '+(n.length>20?n.slice(0,19)+'…':n); }
  { const slot=$('#startslot'); if(slot){ slot.textContent=''; if(!fromOK()&&!U.ui.noStart) slot.append(startCard()); } }
  visible=sortSites(sites().filter(match));
  const ul=$('#list'); ul.textContent='';
  syncFcount();
  $('#count').textContent=visible.length+' of '+sites().length+' places';
  { const fd=$('#f-done'); if(fd) fd.textContent='Show '+visible.length+(visible.length===1?' place':' places'); }
  const lc=$('#linechip'); lc.textContent=''; lc.hidden=!F.line; if(F.line){ lc.append(el('span',{class:'chip','aria-pressed':'true'},el('span',{class:'sw',style:'--c:'+LK[F.line.k][1]}),'Along '+F.line.label,el('button',{type:'button',class:'x','aria-label':'Stop following this line',onclick:()=>{setLine(null);refresh();}},'✕'))); }
  /* places that fit the search and the filters but are kept off by the setting: say so, or a search for one looks like a gap in the Atlas */
  const hid=pref('hideGone')?sites().filter(s=>goneHid(s)&&match0(s)).length:0;
  const hidRow=()=>el('li',{class:'pad hidnote'},el('span',{text:hid+(hid===1?' place':' places')+' with nothing to see '+(hid===1?'is':'are')+' hidden by your setting.'}),el('button',{class:'btn sm',type:'button',id:'hid-show',onclick:()=>{ setPref('hideGone',false); banner('Showing them again. Settings has the switch.',false,5000); }},'Show them'));
  if(!visible.length){ ul.append(el('li',{class:'empty pad'},hid?'Nothing else matches.':'Nothing matches. Clear a filter or two.')); if(hid) ul.append(hidRow()); return; }
  /* a long list is shown in two steps: the first 120 rows now, the rest when asked for. The map shows every pin either way. */
  const key=visible.length+'|'+(visible[0]?visible[0].id:'')+'|'+F.q; if(key!==listKey){ listKey=key; listAll=false; }
  const frag=document.createDocumentFragment(), rows=listAll?visible:visible.slice(0,LISTCAP);
  if(sel&&!listAll&&rows.indexOf(sel)<0&&visible.indexOf(sel)>=0) rows.push(sel);
  rows.forEach(s=>{
    const d=dtl(s), my=U.status[s.id], far=fromOK();
    frag.append(el('li',null,el('button',{class:'item pad'+(sel&&sel.id===s.id?' cur':''),type:'button','data-id':s.id,onclick:()=>select(s,true)},
      dot(s),
      el('span',null,el('b',{text:s.name}),el('small',{text:[s.town,s.years].filter(Boolean).join(' · ')}),
        el('small',null,STS[s.st],s.now?' · changing now':'',s.prec==='area'?' · rough pin':'',s.tip?' · from a reader':'',isFav(s.id)?' · \u2665 favourite':'',my?' · '+MY[my]:'',U.trip.indexOf(s.id)>=0?' · in trip':'')),
      far?el('span',{class:'mins'},(d.est?'~':'')+fmtMin(d.min),el('i',{text:miTxt(d.mi)})):null)));
  });
  ul.append(frag);
  if(rows.length<visible.length) ul.append(el('li',{class:'pad'},el('button',{class:'btn',type:'button',id:'list-more',onclick:()=>{ listAll=true; renderList(); }},'Show the other '+(visible.length-rows.length)+' places')));
  else if(hid) ul.append(hidRow());
}

/* ---------- map ---------- */
let clusLayer=null;
let map=null, sel=null, markers=new Map(), baseLayer=null, cmpLayer=null, histLayer=null, selShapes=[], homeMarker=null, schematic=false, adding=false, pickingHome=false;
const stage=$('#stage');
const W=20037508.342789244;
let FnLayer=null;
const YEARS=['Latest','2025','2024','2023','2022','2021','2020','2018','2017','2016','2015','2014','2013','2012','2011','2010','2009','2008','2007','2006','2005','2004','2003','2002','2001','2000','napp'];
const LIGHT={nw:['Sun from northwest',315,40,2],ne:['Sun from northeast',45,40,2],low:['Low evening sun',300,18,3],s:['Sun from south',180,35,2]};
/* which state a map tile is in: New York's eastern border as [latitude, longitude] steps */
/* which state a point is in: point-in-polygon on simplified Census outlines (they include coastal water, so harbor islands count) */
const OUTL=D.outlines||{}, regMemo=new Map();
function inRing(r,x,y){ let ins=false; for(let i=0,n=r.length/2,j=n-1;i<n;j=i++){ const xi=r[2*i],yi=r[2*i+1],xj=r[2*j],yj=r[2*j+1]; if((yi>y)!==(yj>y)&&x<(xj-xi)*(y-yi)/(yj-yi)+xi) ins=!ins; } return ins; }
function regionOf(lat,lon){
  const key=lat.toFixed(3)+','+lon.toFixed(3); let v=regMemo.get(key); if(v) return v;
  v='other'; for(const k in OUTL){ if(OUTL[k].some(r=>inRing(r,lon,lat))){ v=k; break; } }
  if(v==='other'){ /* just off the edge of an outline: take the nearest state within about 3 km */
    let best=0.0009; for(const k in OUTL) OUTL[k].forEach(r=>{ for(let i=0;i<r.length;i+=2){ const dx=(r[i]-lon)*0.74, dy=r[i+1]-lat, d=dx*dx+dy*dy; if(d<best){ best=d; v=k; } } }); }
  if(regMemo.size>4000) regMemo.clear(); regMemo.set(key,v); return v; }
function tileCenter(c){ const n=Math.pow(2,c.z); return [Math.atan(Math.sinh(Math.PI*(1-2*(c.y+0.5)/n)))*180/Math.PI,(c.x+0.5)/n*360-180]; }
let PXM=1;   /* 2 while a big tile's address is being built (FnLayer, below) */
/* fmt 'jpgpng' (image services only): a JPEG where the service has the whole square, a see-through PNG where it has holes */
function exportUrl(base,c,extra,fmt){ const n=Math.pow(2,c.z),r=2*W/n,x0=-W+c.x*r,y1=W-c.y*r,px=PXQ()*PXM;
  return base+'?bbox='+[x0,y1-r,x0+r,y1].map(v=>v.toFixed(2)).join(',')+'&bboxSR=3857&imageSR=3857&size='+px+','+px+'&format='+(fmt||'jpg')+'&f=image'+(extra||''); }
function xyz(tpl,c,maxN){ let z=c.z,x=c.x,y=c.y,dz=0; if(z>maxN){ dz=z-maxN; x=x>>dz; y=y>>dz; z=maxN; }
  const u=tpl.replace('{z}',z).replace('{y}',y).replace('{x}',x); return dz?{url:u,dz:dz,ox:c.x-(x<<dz),oy:c.y-(y<<dz)}:u; }
const RIG='https://maps.edc.uri.edu/rigis/rest/services/', RILEAF=RIG+'IMG/RI_202603_RGB_3in_web/ImageServer/exportImage', RIDEM=RIG+'TOPO/Elevation_2022_Lidar_web/ImageServer/exportImage';
const hsRule=g=>'&interpolation=RSP_BilinearInterpolation&renderingRule='+encodeURIComponent(JSON.stringify({rasterFunction:'Hillshade',rasterFunctionArguments:{Azimuth:g[1],Altitude:g[2],ZFactor:g[3]},variableName:'DEM'}));
const NYHS='https://elevation.its.ny.gov/arcgis/rest/services/NYS_Statewide_Hillshade/MapServer/export', NYDEM='https://elevation.its.ny.gov/arcgis/rest/services/Latest_DEM/ImageServer/exportImage';
const WORLDIMG='https://services.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}';
/* State flights beyond the first four. Ready-cut tiles: New Jersey 2020, Connecticut spring 2023, New Hampshire spring 2021-22.
   Cut to order: Kansas 2024 (about a second a tile), Maine's statewide mosaic (one to two seconds, and it has holes in the
   north woods), Pennsylvania 2021-23 (three to nine seconds a tile: the slowest server here). */
const NJLEAF='https://maps.nj.gov/arcgis/rest/services/Basemap/Orthos_Natural_2020_NJ_WM/MapServer/tile/{z}/{y}/{x}',
  CTLEAF='https://cteco.uconn.edu/ctraster/rest/services/images/Ortho_2023_tiled/ImageServer/tile/{z}/{y}/{x}',
  NHLEAF='https://nhgeodata.unh.edu/image/rest/services/ImageServices/NH_2021_2022_6in_tiled/ImageServer/tile/{z}/{y}/{x}',
  KSLEAF='https://services.kgs.ku.edu/arcgis7/rest/services/IMAGERY_STATEWIDE/NG911_Imagery_2024/ImageServer/exportImage',
  MELEAF='https://gis.maine.gov/image/rest/services/Misc/MaineOrthoimageryAggregate/ImageServer/exportImage',
  PALEAF='https://imagery.pasda.psu.edu/arcgis/rest/services/pasda/PEMAImagery2021_2023/MapServer/export';
function leafUrl(c){
  /* zoomed far out, a state flight and the world imagery look the same; the world imagery is ready-cut tiles that arrive at
     once and has no white blocks beyond a state's edge. An older flight, picked by year, is kept from zoom 9. */
  const z=c.gz||c.z;                                   /* the map's zoom: one more than a big tile's own (FnLayer._req) */
  if(z<(U.ui.year==='Latest'?11:9)) return xyz(WORLDIMG,c,19);
  const p=tileCenter(c), r=regionOf(p[0],p[1]);
  if(r==='ny') return exportUrl('https://orthos.its.ny.gov/arcgis/rest/services/wms/'+U.ui.year+'/MapServer/export',c);
  if(r==='ma') return xyz('https://tiles.arcgis.com/tiles/hGdibHYSPO59RG1h/arcgis/rest/services/orthos2023/MapServer/tile/{z}/{y}/{x}',c,20);
  if(r==='vt') return xyz('https://maps.vcgi.vermont.gov/arcgis/rest/services/EGC_services/IMG_VCGI_CLR_WM_CACHE/ImageServer/tile/{z}/{y}/{x}',c,19);
  if(r==='ri'&&z>=12) return exportUrl(RILEAF,c);
  if(z>=12){ if(r==='nj') return xyz(NJLEAF,c,20); if(r==='ct') return xyz(CTLEAF,c,20); if(r==='nh') return xyz(NHLEAF,c,20); }
  if(z>=14){ if(r==='ks') return exportUrl(KSLEAF,c,'','jpgpng'); if(r==='pa') return exportUrl(PALEAF,c,'&layers=show:3'); }     /* layer 3 is the picture alone: layer 0 draws the tiles' outlines over it */
  if(r==='me'&&z>=15) return exportUrl(MELEAF,c,'&bandIds=0,1,2','jpgpng');
  return xyz(WORLDIMG,c,19); }
const WORLDHS='https://services.arcgisonline.com/arcgis/rest/services/Elevation/World_Hillshade/MapServer/tile/{z}/{y}/{x}';
const CTHS='https://cteco.uconn.edu/ctraster/rest/services/elevation/Hillshade/ImageServer/exportImage',
  NHDEM='https://nhgeodata.unh.edu/image/rest/services/ImageServices/LiDAR_Bare_Earth_DEM_NH_2022/ImageServer/exportImage',
  MEDEM='https://gis.maine.gov/image/rest/services/DEM/Maine_Elevation_DEM_Statewide/ImageServer/exportImage',
  USDEM='https://elevation.nationalmap.gov/arcgis/rest/services/3DEPElevation/ImageServer/exportImage',
  CANADA={on:1,qc:1,nb:1,ns:1,pe:1,nl:1,mb:1,sk:1,ab:1,bc:1};
function lidarUrl(c){ const z=c.gz||c.z; if(z<9) return xyz(WORLDHS,c,15);
  const p=tileCenter(c), r=regionOf(p[0],p[1]);
  if(r==='ny'){ if(z<14) return exportUrl(NYHS,c); const g=LIGHT[U.ui.light]||LIGHT.nw;
    return exportUrl(NYDEM,c,hsRule(g)); }
  if(r==='ri'&&z>=11) return exportUrl(RIDEM,c,hsRule(LIGHT[U.ui.light]||LIGHT.nw));
  if(r==='ma') return xyz('https://tiles.arcgis.com/tiles/hGdibHYSPO59RG1h/arcgis/rest/services/LiDAR_ShadedRelief/MapServer/tile/{z}/{y}/{x}',c,18);
  if(r==='vt') return xyz('https://maps.vcgi.vermont.gov/arcgis/rest/services/EGC_services/IMG_VCGI_LIDARHILLSHD_WM_CACHE_v1/ImageServer/tile/{z}/{y}/{x}',c,19);
  if(z>=14){ const g=LIGHT[U.ui.light]||LIGHT.nw;
    if(r==='ct') return exportUrl(CTHS,c,'','jpgpng');                       /* drawn by the state with the sun in the northwest: the light setting does not move it */
    if(r==='nh') return exportUrl(NHDEM,c,hsRule(g),'jpgpng');
    if(r==='me') return exportUrl(MEDEM,c,hsRule(g),'jpgpng');
    /* every other state: the national elevation service has 1-metre LiDAR for most of the country. It takes three to ten
       seconds a tile, so it starts only where the world hillshade's ready-cut tiles run out of detail. */
    if(z>=16&&r!=='other'&&!CANADA[r]) return exportUrl(USDEM,c,hsRule(g),'jpgpng'); }
  return xyz(WORLDHS,c,15); }
/* Who to credit depends on the ground in view: one short line for the states on screen, not every state's office at once. */
const CREDIT={leaf:{ny:'NYS ITS',ma:'MassGIS',vt:'VCGI',ri:'RIGIS',nj:'NJ Office of GIS',ct:'CT ECO',nh:'NH GRANIT',pa:'PEMA, PASDA',me:'Maine GeoLibrary',ks:'Kansas NG911, DASC'},
  lidar:{ny:'NYS ITS',ma:'MassGIS',vt:'VCGI',ri:'RIGIS',ct:'CT ECO',nh:'NH GRANIT',me:'Maine GeoLibrary'}};
function creditFor(kind){ return m=>{ const b=m.getBounds(), c=m.getCenter(), out=[];
  [[c.lat,c.lng],[b.getNorth(),b.getWest()],[b.getNorth(),b.getEast()],[b.getSouth(),b.getWest()],[b.getSouth(),b.getEast()]].forEach(p=>{ const r=regionOf(p[0],p[1]);
    const t=CREDIT[kind][r]||(kind==='lidar'&&r!=='other'&&!CANADA[r]?'USGS 3DEP':''); if(t&&out.indexOf(t)<0) out.push(t); });
  out.push('Esri'); return out.join(', '); }; }
const LD={
  streets:{n:'Streets',d:'Roads and place names',mk:p=>L.tileLayer('https://services.arcgisonline.com/ArcGIS/rest/services/World_Street_Map/MapServer/tile/{z}/{y}/{x}',{pane:p,maxZoom:20,maxNativeZoom:19,attribution:'Esri, HERE, Garmin, USGS'})},
  leaf:{n:'Leaf-off aerial',d:'State spring flights. The ground shows through bare trees',mk:p=>new FnLayer('',bigOpt({pane:p,maxZoom:20,ghost:true,fn:leafUrl,fast:c=>xyz(WORLDIMG,c,19),credit:creditFor('leaf')}))},
  lidar:{n:'LiDAR terrain',d:'Bare ground with the trees stripped off. Sharpens to 1 m as you zoom in',mk:p=>new FnLayer('',bigOpt({pane:p,maxZoom:20,ghost:true,fn:lidarUrl,fast:c=>xyz(WORLDHS,c,15),credit:creditFor('lidar')}))},
  sat:{n:'Satellite',d:'World imagery, usually leaves on',mk:p=>L.tileLayer('https://services.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}',{pane:p,maxZoom:20,maxNativeZoom:19,attribution:'Esri, Maxar, Earthstar Geographics'})},
  topo:{n:'USGS topo, current',d:'Contours, streams and trails',mk:p=>new CachedXYZ('https://basemap.nationalmap.gov/arcgis/rest/services/USGSTopo/MapServer/tile/{z}/{y}/{x}',{pane:p,maxZoom:20,maxNativeZoom:16,attribution:'USGS The National Map'})},
  oldtopo:{n:'USGS topo, 1940s–80s',d:'Scanned paper quads. Purple marks later photo-revisions',mk:p=>L.tileLayer('https://services.arcgisonline.com/ArcGIS/rest/services/USA_Topo_Maps/MapServer/tile/{z}/{y}/{x}',{pane:p,maxZoom:20,maxNativeZoom:15,attribution:'USGS, National Geographic, i-cubed'})}
};
/* Compare: a second layer over the map, either behind a divider you drag ('swipe') or lying over it, see-through ('fade',
   called Overlay on the page). What was chosen is kept (U.ui.cmp): on or off, which way, which layer, how strong. */
let cmp=Object.assign({on:false,key:'lidar',mode:'swipe',x:0.5,op:0.6},(U.ui&&U.ui.cmp)||{}); cmp.x=0.5; if(cmp.mode!=='fade') cmp.mode='swipe'; cmp.op=Math.min(1,Math.max(0.1,+cmp.op||0.6));
function cmpSave(){ U.ui.cmp={on:!!cmp.on,key:cmp.key,mode:cmp.mode,op:cmp.op}; save(); }

/* tile cache: keeps every slow state-server tile in this browser */
const TTL=30*864e5, AUTOMAX=150*1048576;
const TC={db:null,mem:new Map(),memMax:250,pending:new Map(),size:0,pinSize:0,pinN:0,fetchOk:0,fetchFail:0,directOk:0,off:false};
function tcOpen(){ if(TC.db) return TC.db; TC.db=new Promise(res=>{ try{ const r=indexedDB.open('lost-hidden-atlas-tiles',1);
  r.onupgradeneeded=()=>{ const st=r.result.createObjectStore('t',{keyPath:'k'}); st.createIndex('t','t'); };
  r.onsuccess=()=>res(r.result); r.onerror=()=>res(null); r.onblocked=()=>res(null); }catch(e){ res(null); } }); return TC.db; }
function memPut(k,b){ TC.mem.delete(k); TC.mem.set(k,b); if(TC.mem.size>TC.memMax) TC.mem.delete(TC.mem.keys().next().value); }
async function tcGet(k,needPin){
  if(!needPin){ const m=TC.mem.get(k); if(m){ memPut(k,m); return m; } }
  const db=await tcOpen(); if(!db) return null;
  return new Promise(res=>{ try{ const q=db.transaction('t').objectStore('t').get(k);
    q.onsuccess=()=>{ const v=q.result; if(v&&(v.p||Date.now()-v.t<TTL)){ memPut(k,v.b); if(needPin&&!v.p) tcPut(k,v.b,true,v.s); res(v.b); } else res(null); };
    q.onerror=()=>res(null); }catch(e){ res(null); } }); }
async function tcPut(k,b,pin,wasSize){
  memPut(k,b); const db=await tcOpen(); if(!db) return;
  try{ const tx=db.transaction('t','readwrite'), st=tx.objectStore('t');
    if(pin){ st.put({k:k,b:b,t:Date.now(),s:b.size,p:1}); TC.pinSize+=b.size; TC.pinN++; if(wasSize) TC.size-=wasSize; }
    else { const g=st.get(k); g.onsuccess=()=>{ const o=g.result; st.put({k:k,b:b,t:Date.now(),s:b.size,p:o&&o.p?1:0}); if(!(o&&o.p)) TC.size+=b.size; }; }
  }catch(e){}
  if(TC.size>AUTOMAX) tcTrim(); }
let trimming=false;
async function tcTrim(){ if(trimming) return; trimming=true; const db=await tcOpen(); if(!db){ trimming=false; return; }
  try{ const tx=db.transaction('t','readwrite'), cur=tx.objectStore('t').index('t').openCursor();
    cur.onsuccess=()=>{ const c=cur.result; if(!c||TC.size<AUTOMAX*0.7) return; if(!c.value.p){ TC.size-=c.value.s; c.delete(); } c.continue(); };
    tx.oncomplete=tx.onabort=()=>{ trimming=false; }; }catch(e){ trimming=false; } }
async function tcScan(){ const db=await tcOpen(); if(!db) return; TC.size=0; TC.pinSize=0; TC.pinN=0;
  return new Promise(res=>{ try{ const cur=db.transaction('t').objectStore('t').openCursor();
    cur.onsuccess=()=>{ const c=cur.result; if(!c){ res(); return; } const v=c.value; if(v.p){ TC.pinSize+=v.s; TC.pinN++; } else TC.size+=v.s; c.continue(); };
    cur.onerror=()=>res(); }catch(e){ res(); } }); }
async function tcClear(){ TC.mem.clear(); const db=await tcOpen(); if(!db) return; await new Promise(res=>{ try{ const tx=db.transaction('t','readwrite'); tx.objectStore('t').clear(); tx.oncomplete=tx.onerror=()=>res(); }catch(e){ res(); } }); TC.size=TC.pinSize=TC.pinN=0; }
/* Fetching tiles. The state servers are slow, and about one request in thirty simply hangs for 15 seconds. So:
   - a request that has not answered in a few seconds is dropped and asked again (three tries, each allowed longer);
   - only a few run at a time for each server, the newest first, so what the map shows NOW is fetched before what it showed
     a moment ago;
   - a tile the map no longer wants (you zoomed on) is never asked for at all. */
const TQ={q:[],run:new Map(),max:8,avg:900,hav:new Map(),retried:0,dropped:0};
const tqHost=u=>{ const m=/^https?:\/\/([^/]+)/.exec(u); return m?m[1]:''; };
/* How long a tile usually takes is kept for each server: the national elevation service and Pennsylvania's aerials take
   several seconds a tile, and must be given that long without making the wait on a quick server longer. */
const SLOWHOST={'elevation.nationalmap.gov':3000,'imagery.pasda.psu.edu':3500};
const tqAvg=h=>TQ.hav.has(h)?TQ.hav.get(h):(SLOWHOST[h]||TQ.avg);
async function fetchTile(url){ let err=null; const h=tqHost(url);
  for(let k=0;k<3;k++){ const ac=typeof AbortController==='function'?new AbortController():null, lim=Math.min(20000,Math.max(5000,tqAvg(h)*5)*(k+1)), t0=Date.now(), tm=ac?setTimeout(()=>ac.abort(),lim):0;
    if(k) TQ.retried++;
    try{ const r=await fetch(url,{mode:'cors',credentials:'omit',signal:ac?ac.signal:undefined});
      if(!r.ok){ err=new Error('http '+r.status); if(r.status<500&&r.status!==429) break; continue; }
      const ct=r.headers.get('content-type')||''; if(ct.indexOf('image')<0&&ct.indexOf('octet-stream')<0){ err=new Error('not an image'); break; }
      const b=await r.blob(); TQ.hav.set(h,tqAvg(h)*0.9+(Date.now()-t0)*0.1); return b; }
    catch(e){ err=e; if(navigator.onLine===false) break;
      if(e.name==='AbortError') TQ.hav.set(h,Math.max(tqAvg(h),lim/3));                        /* on a slow connection, wait longer next time and do not ask twice */
      else if(k>=1) break; }                                                          /* a hang is tried three times; any other failure twice */
    finally{ clearTimeout(tm); } }
  throw err||new Error('tile failed'); }
function tqPump(){
  for(let i=TQ.q.length-1;i>=0;i--){ const j=TQ.q[i];
    if(!j.keep&&j.wants.length&&!j.wants.some(w=>w())){ TQ.q.splice(i,1); TQ.dropped++; j.rej(new Error('dropped')); continue; }
    const h=tqHost(j.url), n=TQ.run.get(h)||0; if(n>=TQ.max) continue;
    TQ.q.splice(i,1); TQ.run.set(h,n+1);
    fetchTile(j.url).then(j.res,j.rej).then(()=>{ TQ.run.set(h,Math.max(0,(TQ.run.get(h)||1)-1)); tqPump(); }); } }
/* want: a function that says whether the map still shows this tile. Leave it out for a tile that must be fetched whatever
   happens (saving an area for offline). */
async function tileBlob(url,pin,want){
  const hit=await tcGet(url,pin); if(hit) return hit;
  let j=TC.pending.get(url);
  if(j){ if(want) j.wants.push(want); else j.keep=true; const b=await j.pr; if(b&&pin) tcPut(url,b,true,b.size); return b; }
  j={url:url,wants:want?[want]:[],keep:!want}; j.pr=new Promise((res,rej)=>{ j.res=res; j.rej=rej; }); TC.pending.set(url,j); TQ.q.push(j); tqPump();
  try{ const b=await j.pr; TC.fetchOk++; tcPut(url,b,!!pin); return b; }
  catch(e){ if(e.message!=='dropped') TC.fetchFail++; throw e; }
  finally{ TC.pending.delete(url); } }
const CacheMixin={ createTile:function(c,done){
  const img=document.createElement('img'); img.alt=''; img.setAttribute('role','presentation'); const url=this.getTileUrl(c);
  const direct=()=>{ img.onload=()=>{ TC.directOk++; if(TC.fetchOk===0&&TC.fetchFail>=4&&TC.directOk>=4) TC.off=true; done(null,img); }; img.onerror=e=>done(e,img); img.src=url; };
  if(TC.off){ direct(); return img; }
  tileBlob(url,false,()=>img.isConnected!==false).then(b=>{ img._gap=b.type==='image/png'; const u=URL.createObjectURL(b); img.onload=()=>{ URL.revokeObjectURL(u); done(null,img); }; img.onerror=()=>{ URL.revokeObjectURL(u); done(new Error('bad tile'),img); }; img.src=u; },
    e=>{ if(e&&e.message==='dropped') return;                                       /* the map moved on before its turn came */
      if(navigator.onLine===false){ done(new Error('offline'),img); } else direct(); });
  return img; } };
/* A wide screen at ordinary sharpness needs sixty or more 256-pixel tiles for one view. There the slow layers are asked for
   in 512-pixel tiles, a quarter as many requests for the same picture. Decided once from the screen, not the window, so
   an area saved for offline matches what is shown later. */
const BIGT=(()=>{ try{ return (window.devicePixelRatio||1)<=1.4&&Math.max(screen.width||0,screen.height||0)>=1200; }catch(e){ return false; } })();
const bigOpt=o=>BIGT?Object.assign(o,{big:true,tileSize:512,zoomOffset:-1}):o;
let CachedXYZ=null, cspBlocked=false;
document.addEventListener('securitypolicyviolation',e=>{ const d=(e.effectiveDirective||e.violatedDirective||''); if(/img-src|default-src/.test(d)) cspBlocked=true; });
const PXQ=()=>(window.devicePixelRatio||1)>1.4?512:256;

/* save an area for offline */
const OFF=[['leaf',14,18],['lidar',15,18],['topo',13,16]], OFFR=500;
let saving=null;
function tilesAround(p,z,rm){ const n=Math.pow(2,z), dy=rm/111320, dx=rm/(111320*Math.cos(rad(p.lat)));
  const tx=lon=>Math.floor((lon+180)/360*n), ty=la=>{ const r=rad(la); return Math.floor((1-Math.log(Math.tan(r)+1/Math.cos(r))/Math.PI)/2*n); };
  const out=[]; for(let x=tx(p.lon-dx);x<=tx(p.lon+dx);x++) for(let y=ty(p.lat+dy);y<=ty(p.lat-dy);y++) out.push([x,y]); return out; }
function offlineUrls(pts){ const set=new Set();
  OFF.forEach(o=>{ const lyr=LD[o[0]].mk('tilePane'); for(let z=o[1];z<=o[2];z++){ lyr._tileZoom=z; pts.forEach(p=>tilesAround(p,z,OFFR).forEach(t=>set.add(lyr.saveUrl?lyr.saveUrl(t[0],t[1],z):lyr.getTileUrl({x:t[0],y:t[1],z:z})))); } });
  return Array.from(set); }
async function saveArea(id,urls){
  const tok={id:id,cancel:false,done:0,n:urls.length,bytes:0,fail:0,render:null}; saving=tok; let i=0;
  try{ if(navigator.storage&&navigator.storage.persist) navigator.storage.persist(); }catch(e){}
  const upd=()=>{ if(tok.render) tok.render(); };
  const worker=async()=>{ while(i<urls.length&&!tok.cancel){ const u=urls[i++]; try{ const b=await tileBlob(u,true); tok.bytes+=b.size; }catch(e){ tok.fail++; } tok.done++; upd(); } };
  await Promise.all([worker(),worker(),worker(),worker()]); saving=null; tok.finished=true; upd(); return tok; }
const mb=b=>(b/1048576).toFixed(b<10485760?1:0)+' MB';
/* "Save this map view": every leaf-off, LiDAR and USGS topo tile inside what the map shows, down to a chosen zoom */
const VIEWMAX=4500; let viewOpen=false, viewCap=17;
function viewUrls(b,cap){ const set=new Set(), rr=x=>rad(x);
  OFF.forEach(o=>{ const lyr=LD[o[0]].mk('tilePane'); for(let z=o[1];z<=Math.min(o[2],cap);z++){ lyr._tileZoom=z; const n=Math.pow(2,z), tx=lon=>Math.floor((lon+180)/360*n), ty=la=>{ const r=rr(la); return Math.floor((1-Math.log(Math.tan(r)+1/Math.cos(r))/Math.PI)/2*n); };
      if((tx(b.getEast())-tx(b.getWest())+1)*(ty(b.getSouth())-ty(b.getNorth())+1)>VIEWMAX*2){ set.add('too-many-'+o[0]+z); for(let i=0;i<VIEWMAX*2;i++) set.add('x'+o[0]+z+'_'+i); return; }
      for(let x=tx(b.getWest());x<=tx(b.getEast());x++) for(let y=ty(b.getNorth());y<=ty(b.getSouth());y++) set.add(lyr.saveUrl?lyr.saveUrl(x,y,z):lyr.getTileUrl({x:x,y:y,z:z})); } });
  return Array.from(set); }
function viewBox(){ const box=el('div',{id:'view-box'}); if(!map||schematic) return box;
  const b=map.getBounds(), urls=viewUrls(b,viewCap), est=urls.length*(PXQ()>256?62000:21000), msg=el('p',{class:'offmsg'}), bar=el('div',{class:'bar',hidden:true},el('span'));
  const sel2=el('select',{id:'view-detail','aria-label':'How much detail to save',onchange:e=>{ viewCap=+e.target.value; buildSheet(); }},[[16,'Fields and tracks (zoom 16)'],[17,'Walls and cellars (zoom 17)'],[18,'Everything (zoom 18)']].map(o=>el('option',{value:String(o[0]),text:o[1]}))); sel2.value=String(viewCap);
  box.append(el('div',{class:'lsub'},sel2));
  if(urls.length>VIEWMAX){ box.append(el('p',{class:'offmsg',text:'This view is too wide to save in one go'+(viewCap>16?' at that detail':'')+'. Zoom in until the map shows only the ground you will walk'+(viewCap>16?', or choose less detail':'')+'.'})); return box; }
  const id='view:'+b.getCenter().lat.toFixed(4)+','+b.getCenter().lng.toFixed(4)+':'+viewCap, btn=el('button',{class:'btn sm',type:'button',id:'view-save'});
  const show=()=>{ const t=saving&&saving.id===id?saving:null;
    if(t){ btn.textContent='Stop'; bar.hidden=false; bar.firstChild.style.width=Math.round(t.done/t.n*100)+'%'; msg.textContent='Saving '+t.done+' of '+t.n+' tiles · '+mb(t.bytes)+(t.fail?' · '+t.fail+' failed':'')+'. Keep the Atlas open.'; return; }
    bar.hidden=true; const s2=U.saved[id]; btn.textContent=s2?'Save again':'Save '+urls.length+' tiles, about '+mb(est);
    msg.textContent=s2?('Saved '+new Date(s2.at).toLocaleDateString()+': '+s2.mb+(s2.miss?', '+s2.miss+' tiles missing':'')+'. Works with no signal on this device.'):'Leaf-off aerial, LiDAR and the USGS topo map are saved. The street map and satellite are not: their owners do not allow copies to be kept.'; };
  btn.addEventListener('click',async()=>{
    if(saving){ if(saving.id===id) saving.cancel=true; else banner('Another area is still saving. Wait for it or stop it first.',true,5000); return; }
    const c=b.getCenter(), near=sites().map(s=>[hav(c.lat,c.lng,pos(s).lat,pos(s).lon),s]).sort((x,y)=>x[0]-y[0])[0], label='Map view '+(near&&near[0]<3?'near '+near[1].name:'at '+c.lat.toFixed(3)+', '+c.lng.toFixed(3));
    const t=saveArea(id,urls); saving.render=show; show(); const r=await t;
    if(!r.cancel||r.done>0){ U.saved[id]={at:Date.now(),label:label,mb:mb(r.bytes),n:r.done-r.fail,miss:r.fail+(r.n-r.done),y:U.ui.year,pts:[[+c.lat.toFixed(5),+c.lng.toFixed(5)]]}; saveNow(); }
    show(); if(r.cancel) msg.textContent='Stopped. '+(r.done-r.fail)+' tiles kept.'; else if(r.fail) msg.textContent+=' Some tiles failed; try Save again on better wifi.'; });
  box.append(el('div',{class:'row'},btn),bar,msg); show(); return box; }
function offlineBox(id,pts,label){
  const info=U.saved[id], urls=offlineUrls(pts), est=urls.length*(PXQ()>256?62000:21000);
  const msg=el('p',{class:'offmsg'}), btn=el('button',{class:'btn sm',type:'button'});
  const bar=el('div',{class:'bar',hidden:true},el('span'));
  const show=()=>{ const t=saving&&saving.id===id?saving:null;
    if(t){ btn.textContent='Stop'; bar.hidden=false; bar.firstChild.style.width=Math.round(t.done/t.n*100)+'%'; msg.textContent='Saving '+t.done+' of '+t.n+' tiles · '+mb(t.bytes)+(t.fail?' · '+t.fail+' failed':'')+'. Keep this page open.'; return; }
    bar.hidden=true; const s2=U.saved[id];
    btn.textContent=s2?'Save again':'Save for offline ('+urls.length+' tiles, about '+mb(est)+')';
    msg.textContent=s2?('Saved '+new Date(s2.at).toLocaleDateString()+': '+s2.mb+(s2.miss?', '+s2.miss+' tiles missing':'')+'. Works with no signal on this device.'):''; };
  btn.addEventListener('click',async()=>{
    if(saving){ if(saving.id===id) saving.cancel=true; else banner('Another area is still saving. Wait for it or stop it first.',true,5000); return; }
    topoWarm((id.indexOf('trip:')===0?id.slice(5).split(','):[id]).map(byId).filter(Boolean)); linesWarm(pts);
    const t=saveArea(id,urls); saving.render=show; show(); const r=await t;
    if(!r.cancel||r.done>0){ U.saved[id]={at:Date.now(),label:label,mb:mb(r.bytes),n:r.done-r.fail,miss:r.fail+(r.n-r.done),y:U.ui.year,pts:pts.map(p=>[+p.lat.toFixed(5),+p.lon.toFixed(5)])}; save(); }
    show(); if(r.cancel) msg.textContent='Stopped. '+(r.done-r.fail)+' tiles kept.'; else if(r.fail) msg.textContent+=' Some tiles failed; try Save again on better wifi.'; });
  if(saving&&saving.id===id) saving.render=show;
  show();
  return el('div',{class:'offl'},el('p',{style:'font-size:12.5px;color:var(--mute);margin:0 0 6px',text:'Downloads the leaf-off aerial ('+(U.ui.year==='Latest'?'latest flight':U.ui.year==='napp'?'1990s infrared':U.ui.year+' flight')+'), sharp LiDAR ('+(LIGHT[U.ui.light]||LIGHT.nw)[0].toLowerCase()+') and USGS topo for about 500 m around '+(pts.length>1?'each stop':'the pin')+', so you can scout with no signal. Use wifi. Streets and satellite are not saved.'}),btn,bar,msg); }

function banner(msg,warn,ms){ const b=$('#banner'); if(!msg){ b.hidden=true; return; } b.textContent=msg; b.className='float'+(warn?' warn':''); b.hidden=false; b.title='Click to dismiss'; b.onclick=()=>{b.hidden=true;}; clearTimeout(banner.t); if(ms) banner.t=setTimeout(()=>b.hidden=true,ms); }

function initMap(){
  /* A tile layer whose addresses come from a function (which state's service, which zoom).
     c  = the tile as Leaflet numbers it; rc = the same square in ordinary 256-pixel tile numbering (they differ for big tiles).
     An "export" address (bbox=...) is cut to order by a slow state server; anything else is a ready-cut tile. */
  const isExp=t=>typeof t==='string'&&t.indexOf('bbox=')>0;
  const abs=(n,x,y,w,h)=>{ n.style.cssText='position:absolute;max-width:none;left:'+x+'px;top:'+y+'px;width:'+w+'px;height:'+h+'px'; return n; };
  FnLayer=L.TileLayer.extend({ options:{updateWhenZooming:false,keepBuffer:4},
    onAdd:function(m){ L.TileLayer.prototype.onAdd.call(this,m); if(!this.options.credit) return;
      this._crFn=()=>{ const ac=this._map&&this._map.attributionControl; if(!ac) return; const t=this.options.credit(this._map); if(t===this._crText) return;
        if(this._crText) ac.removeAttribution(this._crText); this._crText=t; if(t) ac.addAttribution(t); };
      m.on('moveend',this._crFn); this._crFn(); },
    onRemove:function(m){ if(this._crFn){ m.off('moveend',this._crFn); if(this._crText&&m.attributionControl) m.attributionControl.removeAttribution(this._crText); this._crText=null; this._crFn=null; }
      L.TileLayer.prototype.onRemove.call(this,m); },
    _rc:function(c){ return this.options.big?{x:c.x,y:c.y,z:c.z-1}:c; },
    /* A big tile covers the ground of four ordinary ones, so its own z is one less than the map's. Which server to ask is
       decided by the map's zoom (gz), or a wide screen would cross every threshold a level late and ask a slow server
       for four small pictures where one big one will do. */
    _req:function(rc,small){ const big=this.options.big&&!small; PXM=big?2:1; try{ return this.options.fn(big&&rc.gz===undefined?{x:rc.x,y:rc.y,z:rc.z,gz:rc.z+1}:rc); } finally{ PXM=1; } },
    getTileUrl:function(c){ const t=this._req(this._rc(c)); return typeof t==='string'?t:t.url; },
    /* the address that will be fetched for the ground under ordinary tile x,y,z: what "save for offline" must keep */
    saveUrl:function(x,y,z){ const t=this._req({x:x,y:y,z:z},true);
      if(this.options.big&&isExp(t)&&z>0){ const b=this._req({x:x>>1,y:y>>1,z:z-1}); if(isExp(b)) return b; }
      return typeof t==='string'?t:t.url; },
    /* one ordinary tile drawn into a square of the given size; cb(error) when it has loaded or failed */
    _piece:function(rc,size,cb,t){ t=t||this._req(rc,true);
      /* an image with no picture yet is kept hidden: Chrome draws a grey outline round one */
      if(typeof t==='string'){ const im=CacheMixin.createTile.call({getTileUrl:()=>t},rc,e=>{ if(!e) im.style.visibility=''; cb(e); }); abs(im,0,0,size,size); im.style.visibility='hidden'; return im; }
      const bx=document.createElement('div'); bx.style.overflow='hidden'; const k=1<<t.dz, im=CacheMixin.createTile.call({getTileUrl:()=>t.url},rc,e=>{ if(!e) im.style.visibility=''; cb(e); });
      abs(im,-t.ox*size,-t.oy*size,size*k,size*k); im.style.visibility='hidden'; bx.appendChild(im); return abs(bx,0,0,size,size); },
    /* four ordinary tiles making up one big one */
    _quad:function(rc,sz,cb){ const g=document.createElement('div'); let left=4, good=0;
      for(let i=0;i<4;i++){ const dx=i&1, dy=i>>1, pc=this._piece({x:rc.x*2+dx,y:rc.y*2+dy,z:rc.z+1},sz/2,e=>{ if(!e) good++; if(--left===0) cb(good?null:new Error('no tile')); });
        pc.style.left=dx*sz/2+'px'; pc.style.top=dy*sz/2+'px'; g.appendChild(pc); }
      return abs(g,0,0,sz,sz); },
    /* While a slow tile is on its way, show the same ground from a tile this browser already holds: a wider one stretched,
       or the four finer ones shrunk. It is blurry or patchy for a second instead of blank. */
    _ghost:async function(rc,sz){
      const have=async(u,deep)=>TC.mem.get(u)||(deep?await tcGet(u):null), pic=b=>{ const im=document.createElement('img'), u=URL.createObjectURL(b); im.alt=''; im.onload=im.onerror=()=>URL.revokeObjectURL(u); im.src=u; return im; };
      for(let d=1;d<=5&&rc.z-d>=3;d++){ const a={x:rc.x>>d,y:rc.y>>d,z:rc.z-d}, u=this._req(a); if(typeof u!=='string') continue;
        const b=await have(u,d<=3); if(b){ const k=1<<d; return abs(pic(b),-(rc.x-(a.x<<d))*sz,-(rc.y-(a.y<<d))*sz,sz*k,sz*k); } }
      const g=document.createElement('div'); let n=0;
      for(let i=0;i<4;i++){ const u=this._req({x:rc.x*2+(i&1),y:rc.y*2+(i>>1),z:rc.z+1}); if(typeof u!=='string') continue;
        const b=await have(u,true); if(b){ n++; g.appendChild(abs(pic(b),(i&1)*sz/2,(i>>1)*sz/2,sz/2,sz/2)); } }
      return n?abs(g,0,0,sz,sz):null; },
    createTile:function(c,done){ const rc=this._rc(c), t=this._req(rc), sz=this.getTileSize().x, big=this.options.big;
      const box=document.createElement('div'); box.style.overflow='hidden';
      if(!isExp(t)){                                                   /* ready-cut tiles: quick, and never stretched */
        if(big) box.appendChild(this._quad(rc,sz,e=>{ box._real=!e; done(e,box); })); else if(typeof t==='string') return CacheMixin.createTile.call(this,c,done); else box.appendChild(this._piece(rc,sz,e=>{ box._real=!e; done(e,box); }));
        return box; }
      let told=false, fin=false, ghost=null, under=null; const tell=e=>{ if(!told){ told=true; done(e,box); } }, fastFn=this.options.fast;
      /* The world's ready-cut tile for the same ground, laid beneath. It is fetched when a slow state tile has not come and
         nothing held can stand in for it, and it stays when the state's picture has holes in it or never comes. */
      const lay=cb=>{ if(under||!fastFn){ if(cb) cb(under?null:new Error('no world tile')); return; }
        const u=this._piece(rc,sz,e=>{ if(under===u){ if(e){ u.remove(); under=null; } else box._under=true; } if(cb) cb(e); },fastFn(rc)); under=u; box.insertBefore(u,box.firstChild); };
      const unlay=()=>{ if(under){ under.remove(); under=null; box._under=false; } };
      const img=CacheMixin.createTile.call({getTileUrl:()=>t},c,e=>{ fin=true;
        if(!e){ box._real=true; img.style.visibility=''; if(ghost){ ghost.remove(); ghost=null; }
          if(img._gap) lay(); else unlay();
          tell(null); return; }
        if(ghost){ tell(null); return; }                               /* the real tile failed: the stand-in stays */
        if(fastFn&&navigator.onLine!==false){ img.remove(); lay(e2=>tell(e2?e:null)); return; }   /* or the world's tile takes its place */
        if(big&&navigator.onLine===false){ img.remove(); box.appendChild(this._quad(rc,sz,e2=>tell(e2))); return; }   /* no signal: ordinary tiles kept from before may cover it */
        tell(e); });
      box.appendChild(abs(img,0,0,sz+1,sz+1)); img.style.visibility='hidden'; Promise.resolve().then(()=>{ box.style.width=box.style.height=(sz+1)+'px'; });    /* one pixel over its neighbours: no hairline between tiles while a level is stretched */
      /* only when the real tile is not here within a moment: a tile this browser holds arrives sooner than a stand-in could be made */
      if(this.options.ghost&&!TC.mem.has(t)) setTimeout(()=>{ if(fin||box.isConnected===false) return;
        this._ghost(rc,sz).then(g=>{ if(g&&!fin&&box.isConnected!==false){ ghost=g; box._ghost=true; box.insertBefore(g,img); tell(null); } },()=>{}); },70);
      if(fastFn&&!TC.mem.has(t)) setTimeout(()=>{ if(fin||ghost||box.isConnected===false) return;
        lay(e=>{ if(!e&&!fin&&box.isConnected!==false){ box._ghost=true; tell(null); } }); },1200);
      return box; } });
  CachedXYZ=L.TileLayer.extend(Object.assign({options:{keepBuffer:4}},CacheMixin));
  setTimeout(tcScan,4000);
  window.addEventListener('offline',()=>banner('No signal. Leaf-off, LiDAR and Topo still show for areas you saved or looked at recently.',true,9000));
  window.addEventListener('online',()=>{ banner('Back online.',false,2500); linesRetry(); drawLines(); });
  map=L.map('map',{zoomControl:false,maxZoom:20,minZoom:3,zoomSnap:1,worldCopyJump:false,maxBounds:MAXB,maxBoundsViscosity:0.6}); if(U.last&&U.last.ll) nearHome(U.last.ll,false); { const sv=startView(); if(sv.b) map.fitBounds(sv.b,{animate:false}); else map.setView(sv.c,sv.z); }
  L.control.zoom({position:'bottomright'}).addTo(map);
  drawScale();
  map.attributionControl.setPrefix(false);
  map.createPane('cmp').style.zIndex=250;
  map.createPane('hist').style.zIndex=350;
  map.on('moveend',()=>{ if(U.ui.land) drawLand(); if(view==='near'&&NM.org==='map') nmDraw(); const c=map.getCenter(); U.ui.view=[+c.lat.toFixed(5),+c.lng.toFixed(5),map.getZoom()]; save(); });
  if(!LD[U.ui.base]) U.ui.base='streets';
  setBase(U.ui.base,true); if(cmp.on){ cmp.lap=0; setCmp(); }      /* a comparison left on is on again, the way it was */
  map.on('zoom',pinchFrame); map.on('zoomanim',pinchAnim); map.on('zoomend moveend',pinchEnd); map.on('zoomend',onZoom); onZoom(); map.on('moveend',syncMarkers);        /* a zoom ends with a moveend too */
  map.on('move zoom zoomend moveend resize viewreset',clipCmp);
  map.on('click',onMapClick); drawSpots();
  /* A double tap. Leaflet's own goes in one step, which is slow work with one thumb, most of all with the map full screen:
     on open map it goes in as many steps as Settings says (three unless changed; Shift and a double click goes out); on a
     pin it goes to street level; on a numbered disc it goes at least that many steps toward the disc (dblPin, dblGroup below). */
  map.doubleClickZoom.disable();
  map.on('dblclick',e=>{ if(adding||pickingHome) return; const n=Math.max(1,Math.min(4,+pref('dbl')||3)), out=!!(e.originalEvent&&e.originalEvent.shiftKey);
    map.setZoomAround(e.containerPoint,Math.max(map.getMinZoom(),Math.min(map.getMaxZoom(),map.getZoom()+(out?-n:n)))); });
  map.on('contextmenu',onContext);
  map.on('mousemove',e=>{ const r=$('#readout'); r.hidden=false; r.textContent=e.latlng.lat.toFixed(5)+', '+e.latlng.lng.toFixed(5)+' · z'+map.getZoom(); });
  window.addEventListener('resize',debounce(()=>map.invalidateSize(),150));
  setupSwipe(); setupSplit(); drawLines(); drawLand(); drawLots(); drawLeads(); drawPockets(); Object.keys(XL).forEach(drawXL); drawWalls(); try{ window.__atlasMap=map; window.__atlasTiles=TQ; window.__atlasNM={sites:sites,custom:()=>U.custom,addMine:o=>{ U.custom.push(o); save(); refresh(); },nmGoal:nmGoal,setPref:setPref,nmFix:nmFix,nmCollect:nmCollect,nmBuzzes:nmBuzzes,NM:NM,XL:XL,xlLoad:xlLoad,xlNeed:xlNeed,syncMarkers:syncMarkers,visible:()=>visible}; window.__atlasLines=()=>({split:!!LX,got:Object.assign({},lineGot),wide:!!lineWide,wideWait:lineWideWait,n:(LINES||[]).length}); window.__atlasShare=(cfg,kind,f)=>{ const o=Object.assign({},SHARE); Object.assign(SHARE,cfg); try{ return shareLinks(kind,f); } finally{ Object.assign(SHARE,o); } }; }catch(e){}
  syncMarkers(); drawHome();
  map.on('dragstart',()=>{ dragging=true; }); map.on('dragend',()=>{ dragging=false; });
  if(U.last&&U.last.ll) placeDot(U.last.ll,false);
}
function onZoom(){ map.getContainer().classList.toggle('zfar',map.getZoom()<12); }
function setBase(key,first){
  if(schematic) return;
  if(baseLayer) map.removeLayer(baseLayer);
  U.ui.base=key; save();
  baseLayer=LD[key].mk('tilePane').addTo(map);
  if(first&&navigator.onLine===false){ banner('No signal. Switch to Leaf-off, LiDAR or Topo on the bar to see areas you saved.',true,12000); first=false; }
  if(first){ let ok=0,bad=0,told=false; const lyr=baseLayer;
    const judge=()=>{ if(ok) return; if(cspBlocked){ goSchematic(); return; }
      if(bad>=3&&!told){ told=true; banner('Map tiles are not loading. Weak signal? Leaf-off, LiDAR and Topo still show for areas you saved.',true,12000); } };
    lyr.on('tileload',()=>{ok++;}); lyr.on('tileerror',()=>{ bad++; setTimeout(judge,50); });
    setTimeout(judge,7000); }
  onZoom(); syncBar();
}
function setCmp(){
  if(cmpLayer){ map.removeLayer(cmpLayer); cmpLayer=null; }
  const sw=$('#swipe'), fd=$('#fade'); const pane=map.getPane('cmp');
  if(!cmp.on||schematic){ sw.hidden=true; fd.hidden=true; pane.style.clip=''; pane.style.opacity=''; return; }
  if(!LD[cmp.key]||cmp.key===U.ui.base) cmp.key=U.ui.base==='lidar'?'leaf':'lidar';      /* a layer is not compared with itself */
  cmpLayer=LD[cmp.key].mk('cmp').addTo(map);
  if(cmp.mode==='swipe'){ fd.hidden=true; pane.style.opacity=''; sw.hidden=false; $('#swipe-l').textContent=LD[U.ui.base].n; $('#swipe-r').textContent=LD[cmp.key].n; placeSwipe(); }
  else { sw.hidden=true; pane.style.clip=''; pane.style.opacity=cmp.op; fd.hidden=false; $('#fade-l').textContent=LD[cmp.key].n; $('#fade-op').value=String(cmp.op); }
  onZoom();
}
function clipCmp(){ if(!map) return; const pane=map.getPane('cmp'); if(!cmp.on||cmp.mode!=='swipe'){ return; }
  const sz=map.getSize(),nw=map.containerPointToLayerPoint([0,0]); const x=nw.x+sz.x*cmp.x;
  pane.style.clip='rect('+nw.y+'px,'+(nw.x+sz.x)+'px,'+(nw.y+sz.y)+'px,'+x+'px)'; }
function placeSwipe(){ $('#swipe').style.left=(cmp.x*100)+'%'; clipCmp(); }
/* Upright phone: the layer bar is the edge between the map and the list, and can be dragged up and down to share the screen
   differently (U.ui.split: the map's share of the height; 0 is the layout's own 44%). The map never gets less than its 220-pixel
   strip, and the list always keeps its tabs and about one entry. Sideways the bar still scrolls its buttons. */
const SPLITMAP=220, SPLITLIST=230;      /* 230: the tabs, the search row, the count and the first entry */
function splitClamp(f,H){ const lo=SPLITMAP/H, hi=1-SPLITLIST/H; return Math.min(Math.max(f,lo),Math.max(lo,hi)); }
function splitApply(){ const a=$('#app'); if(U.ui.split>0) a.style.setProperty('--split',(U.ui.split*100).toFixed(2)+'%'); else a.style.removeProperty('--split'); }
function setupSplit(){
  splitApply(); const bar=$('#lbar'), app=$('#app'); let st=null, quiet=0;
  const stacked=()=>stage.getBoundingClientRect().bottom<=$('#side').getBoundingClientRect().top+1;      /* not side by side, as a wide window and a phone on its side are */
  bar.addEventListener('pointerdown',e=>{ if((e.pointerType==='mouse'&&e.button!==0)||app.classList.contains('mapbig')||!stacked()) return; st={id:e.pointerId,x:e.clientX,y:e.clientY,on:false,h0:stage.getBoundingClientRect().height,raf:0}; });
  /* moves and the lift are heard on the window: a finger stays with the bar it touched, but a mouse that leaves the bar would be lost */
  window.addEventListener('pointermove',e=>{ if(!st||e.pointerId!==st.id) return; const dx=e.clientX-st.x, dy=e.clientY-st.y;
    if(!st.on){ if(Math.abs(dy)<10||Math.abs(dy)<Math.abs(dx)*1.5) return; st.on=true; try{bar.setPointerCapture(e.pointerId);}catch(x){} bar.classList.add('dragging'); }
    const H=app.getBoundingClientRect().height; U.ui.split=splitClamp((st.h0+dy)/H,H); splitApply(); e.preventDefault();
    if(!st.raf){ const s0=st; s0.raf=requestAnimationFrame(()=>{ s0.raf=0; if(map) map.invalidateSize({pan:false}); }); } });
  const end=e=>{ if(!st||e.pointerId!==st.id) return; const was=st.on; st=null; bar.classList.remove('dragging'); if(!was) return;
    quiet=Date.now()+400; save(); if(map) map.invalidateSize({pan:false}); };
  window.addEventListener('pointerup',end); window.addEventListener('pointercancel',end);
  bar.addEventListener('click',e=>{ if(Date.now()<quiet){ e.stopPropagation(); e.preventDefault(); } },true);      /* letting go over a button after a drag is not a tap on it */
}
function setupSwipe(){
  const g=$('#swipe .grip'); let drag=false;
  g.addEventListener('pointerdown',e=>{ drag=true; try{g.setPointerCapture(e.pointerId);}catch(x){} e.preventDefault(); });
  g.addEventListener('pointermove',e=>{ if(!drag) return; const r=stage.getBoundingClientRect(); cmp.x=Math.min(0.97,Math.max(0.03,(e.clientX-r.left)/r.width)); placeSwipe(); });
  const up=()=>{drag=false;}; g.addEventListener('pointerup',up); g.addEventListener('pointercancel',up);
  g.addEventListener('keydown',e=>{ if(e.key==='ArrowLeft'){cmp.x=Math.max(0.03,cmp.x-0.03);placeSwipe();} if(e.key==='ArrowRight'){cmp.x=Math.min(0.97,cmp.x+0.03);placeSwipe();} });
  /* Overlay's own slider, on the map, so the strength is set without opening Map options */
  $('#fade-op').addEventListener('input',e=>{ cmp.op=Math.min(1,Math.max(0.1,+e.target.value||0.6)); if(map&&cmp.on&&cmp.mode==='fade') map.getPane('cmp').style.opacity=cmp.op; cmpSave(); const o=document.getElementById('cmp-op'); if(o) o.value=String(cmp.op); });
}
/* layer bar: one row of icon buttons, plus an options sheet with a Done button that is always in reach */
const ICON={
  streets:'<path d="M9 3 6 21M15 3l3 18M12 5v3M12 11v3M12 17v3"/>',
  leaf:'<path d="M12 21v-9M12 12 8 8M12 12l4-4M12 16l-3-2M12 16l3-2M8 8V4M8 8H4M16 8V4M16 8h4"/>',
  lidar:'<path d="M2 19 9 7l4 7 3-4 6 9zM9 7l1.5 6M16 10l.5 5"/>',
  sat:'<circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3c3.5 3 3.5 15 0 18M12 3c-3.5 3-3.5 15 0 18"/>',
  topo:'<path d="M4 12c0-5 3.5-8 8-8s8 3 8 8-3.500 8-8 8-8-3-8-8z"/><path d="M8 12c0-2.500 1.700-4 4-4s4 1.500 4 4-1.700 4-4 4-4-1.500-4-4z"/>',
  oldtopo:'<path d="M3 6l6-2 6 2 6-2v14l-6 2-6-2-6 2zM9 4v14M15 6v14"/>',
  rails:'<path d="M7 3v18M17 3v18M7 7h10M7 12h10M7 17h10"/>',
  canal:'<path d="M3 8c2-2 4-2 6 0s4 2 6 0 4-2 6 0M3 14c2-2 4-2 6 0s4 2 6 0 4-2 6 0M3 20c2-2 4-2 6 0s4 2 6 0 4-2 6 0"/>',
  hist:'<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3.500 2"/>',
  land:'<path d="M12 3l5 7h-3l4 6H6l4-6H7zM12 16v5"/>',
  lots:'<path d="M4 4h16v16H4zM4 11h16M11 4v7M15 11v9"/>',
  leads:'<path d="M12 21s-6-5.500-6-10a6 6 0 1 1 12 0c0 4.500-6 10-6 10z"/><path d="M12 8v3.500M12 14h.01"/>',
  pock:'<circle cx="12" cy="12" r="8.500"/><path d="M8.500 15.500v-5l3.500-2.500 3.500 2.500v5zM11 15.500v-2.500h2v2.500"/>',
  cmp:'<path d="M12 3v18M4 6h5v12H4zM15 6h5v12h-5z"/>',
  who:'<circle cx="9" cy="8" r="3.500"/><path d="M3 20c0-3.500 2.500-6 6-6 1.500 0 2.800.400 3.800 1.200M17 13v.01M17 16v5M14.500 9.500a2.500 2.500 0 1 1 3.500 2.300"/>',
  opt:'<path d="M4 7h9M17 7h3M4 17h3M11 17h9"/><circle cx="15" cy="7" r="2"/><circle cx="9" cy="17" r="2"/>',
  loc:'<circle cx="12" cy="12" r="4"/><path d="M12 2v4M12 18v4M2 12h4M18 12h4"/>',
  big:'<path d="M4 9V4h5M20 9V4h-5M4 15v5h5M20 15v5h-5"/>',
  list:'<path d="M4 6h16M4 12h16M4 18h16"/>'
};
function ico(k){ const s=document.createElement('span'); s.className='ic'; s.innerHTML='<svg viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">'+ICON[k]+'</svg>'; return s; }
const BAR=[['streets','Streets','Street map'],['leaf','Leaf-off','Leaf-off aerial: spring flights with bare trees'],['lidar','LiDAR','LiDAR terrain: bare ground with the trees stripped off'],['sat','Satellite','Satellite imagery'],['topo','Topo','Current USGS topo map'],['oldtopo','Old topo','USGS paper maps, 1940s to 1980s'],
  ['rails','Old rails','Old railroad and trolley lines'],['canal','Canals','Canals, old and current'],['hist','Old map','Lay the old survey sheet over the selected place'],['land','Public land','Shade public and protected land by access'],['lots','Lot lines','Property lines (New York and Massachusetts, zoom in close)'],['leads','Leads','Yellow dots: ruins and old sites mapped on OpenStreetMap that nobody has checked for the Atlas. Vanished places and old mines are separate switches under More'],['pock','Old towns','Purple discs: old town centres and other pockets of listed buildings and historical markers. Zoom in to street level for the single buildings'],
  ['cmp','Compare','Compare two layers: tap for a divider to drag, again to lay one over the other, again to stop'],['who','Owner?','Tap the map to see whose land it is']];
let asking=false, lotLayer=null, spotting=false;
function barState(k){
  if(LD[k]) return !schematic&&U.ui.base===k;
  if(k==='rails') return !!U.ui.lines.oldrail; if(k==='canal') return !!U.ui.lines.canal;
  if(k==='hist') return !!U.ui.hist; if(k==='land') return !!U.ui.land; if(k==='lots') return !!U.ui.lots; if(k==='leads') return !!U.ui.leads; if(k==='pock') return !!U.ui.pockets;
  if(k==='cmp') return cmp.on; if(k==='who') return asking; return false; }
function barTap(k){
  if(!map) return;
  if(LD[k]){ setBase(k); if(cmp.on) setCmp(); }
  else if(k==='rails'){ U.ui.lines.oldrail=!U.ui.lines.oldrail; save(); drawLines(); }
  else if(k==='canal'){ U.ui.lines.canal=!U.ui.lines.canal; save(); drawLines(); }
  else if(k==='hist'){ U.ui.hist=!U.ui.hist; save(); showHist();
    if(U.ui.hist&&!sel) banner('Old map is on. Pick a place to see its old survey sheet laid over the map.',false,6000);
    else if(U.ui.hist&&!sel.tm) banner('No old survey sheet is stored for this place.',false,5000);
    if(sel&&view==='detail'){ const c=document.getElementById('d-hist'); if(c) c.checked=!!U.ui.hist; } }
  else if(k==='land'){ U.ui.land=!U.ui.land; save(); drawLand(); if(U.ui.land) banner(map.getZoom()<11?'Public land is on. Zoom in to see it.':'Green is open to the public, amber is restricted, red is closed. Purple has no access on record.',false,7000); }
  else if(k==='lots'){ U.ui.lots=!U.ui.lots; save(); drawLots(); if(U.ui.lots) banner(map.getZoom()<15?'Lot lines are on. Zoom in close to see them. New York and Massachusetts.':'Orange lines are property lines. Tap Owner? and then a lot to see who owns it.',false,7000); }
  else if(k==='leads'){ U.ui.leads=!U.ui.leads; save(); drawLeads(); if(U.ui.leads) banner(map.getZoom()<LEADZ?'Leads are on. Zoom in to see them: yellow dots, unchecked ruins and old sites from OpenStreetMap.':'Yellow dots are unchecked ruins, mines, kilns and quarries from OpenStreetMap. Tap one.',false,7000); }
  else if(k==='pock'){ U.ui.pockets=!U.ui.pockets; save(); drawPockets(); if(U.ui.pockets) banner(map.getZoom()<POCKZ?'Old town centres are on. Zoom in to see them: purple discs, from about the 20-mile scale.':'Purple discs are old town centres and other pockets of listed buildings. Tap one, or zoom in to street level.',false,7000); }
  else if(k==='cmp'){ cmpTap(); }
  else if(k==='who'){ setAsking(!asking); }
  syncBar(); }
/* The Compare button goes round three stops: off, the way used last time, the other way, off. Passing through the second way
   on the way to off (a tap within a second and a half) does not make it the way to remember. */
function cmpTap(){ const other=m=>m==='swipe'?'fade':'swipe', now=Date.now();
  if(!cmp.on){ cmp.on=true; cmp.lap=0; cmp.x=0.5; }
  else if(!cmp.lap){ cmp.lap=1; cmp.home=cmp.mode; cmp.mode=other(cmp.mode); cmp.since=now; }
  else { cmp.on=false; cmp.lap=0; if(now-(cmp.since||0)<1500&&cmp.home) cmp.mode=cmp.home; }
  setCmp(); cmpSave();
  if(cmp.on&&cmp.mode==='swipe'&&!cmp.lap) banner('Swipe: drag the divider. Tap again to lay '+LD[cmp.key].n+' over the map instead.',false,4500); else banner(''); }      /* nothing is said over Overlay: its slider sits where the words would */
function setAsking(on){ asking=on; adding=false; spotting=false; pickingHome=false; addBar(); $('#add-here').hidden=true; stage.classList.toggle('adding',on); $('#addbar').hidden=!on; if(on) $('#addbar span').textContent='Tap the map to see whose land it is.'; syncBar(); }
function buildBar(){
  const sc=$('#lscroll'), fx=$('#lfix'); sc.textContent=''; fx.textContent='';
  BAR.forEach((b,i)=>{ if(schematic&&(LD[b[0]]||b[0]==='cmp'||b[0]==='lots'||b[0]==='land'||b[0]==='who')) return;
    if((i===6||i===12)&&sc.childNodes.length) sc.append(el('span',{class:'lsep'}));
    sc.append(el('button',{class:'lb',type:'button',id:'lb-'+b[0],title:b[2],'aria-label':b[2],'aria-pressed':'false',onclick:()=>barTap(b[0])},ico(b[0]),el('span',{class:'lt',text:b[1]}))); });
  fx.append(el('button',{class:'lb',type:'button',id:'lb-opt',title:'Flight year, light direction, compare and line options','aria-label':'More map options',onclick:openSheet},ico('opt'),el('span',{class:'lt',text:'More'})));
  fx.append(el('button',{class:'lb',type:'button',id:'lb-loc',title:'Show where I am','aria-label':'Show where I am','aria-pressed':String(geo.id!==null),onclick:()=>{ if(map) locate(); }},ico('loc'),el('span',{class:'lt',text:'Me'})));
  const big=$('#app').classList.contains('mapbig');
  fx.append(el('button',{class:'lb',type:'button',id:'lb-big',title:'Make the map fill the screen','aria-label':big?'Show the list':'Bigger map',onclick:()=>{ $('#app').classList.toggle('mapbig'); buildBar(); if(map) setTimeout(()=>map.invalidateSize(),60); }},ico(big?'list':'big'),el('span',{class:'lt',text:big?'List':'Full'})));
  const mo=el('button',{class:'lmore',type:'button','aria-label':'More layers',title:'More layers',onclick:()=>sc.scrollBy({left:sc.clientWidth*0.7,behavior:'smooth'})},'›');
  const old=$('#lbar .lmore'); if(old) old.remove(); $('#lbar').append(mo);
  const fit=()=>{ mo.style.right=fx.offsetWidth+'px'; mo.hidden=sc.scrollLeft+sc.clientWidth>=sc.scrollWidth-4; };
  sc.onscroll=fit; buildBar.fit=fit; if(!buildBar.rs){ buildBar.rs=true; window.addEventListener('resize',debounce(()=>{ if(buildBar.fit) buildBar.fit(); },120)); } requestAnimationFrame(fit); setTimeout(fit,400);
  syncBar(); }
function syncBar(){ BAR.forEach(b=>{ const n=document.getElementById('lb-'+b[0]); if(n) n.setAttribute('aria-pressed',String(barState(b[0]))); });
  { const n=document.querySelector('#lb-cmp .lt'); if(n) n.textContent=!cmp.on?'Compare':cmp.mode==='swipe'?'Swipe':'Overlay'; }      /* the button says which way is showing */ if(!$('#sheet').hidden) buildSheet(); }
let sheetMode='map';
function drawScale(){ if(!map) return; if(drawScale.c) map.removeControl(drawScale.c); drawScale.c=L.control.scale({position:'bottomleft',imperial:!KM(),metric:KM()}).addTo(map); }
/* send the recorder's settings to the phone; it reads them when a recording starts and when a mark is dropped */
function pushPrefs(){ if(NATIVE) AT.call('configure',{units:pref('units'),step:STEP(),every:({fine:1000,normal:2000,coarse:5000})[pref('detail')]||2000,buzz:!!pref('buzz')}).catch(()=>{}); }
function setPref(k,v){ if(!U.set) U.set={}; U.set[k]=v; saveNow(); applyTheme(); drawScale(); pushPrefs();
  if(k==='cluster'||k==='heat') syncMarkers();
  if(k==='nativeLeads'){ if(v&&LEADS) leadsMore(); drawLeads(); NM.ver++; NM.cand=null; NM.in.clear(); nmPush(true); if(view==='near') nmDraw(true); }
  if(k==='hideGone'||k==='quietGone'||k==='buzzVanished'){ NM.ver++; NM.cand=null; NM.in.clear(); nmPush(true); if(k==='hideGone') refresh(); if(view==='near') nmDraw(true); }
  if(k==='trk'){ if(rec) drawRec(); if(NM.ring&&NM.ring._icon) NM.ring._icon.style.setProperty('--trk',v); if(NM.line) NM.line.setStyle({color:v}); const sl=shownLog&&logById(shownLog); if(sl) showLog(sl,false); }
  if(k==='units'){ const nv=$('#v-near'); if(nv) nv.textContent=''; if(view==='near') renderNear(); nmPush(true); }
  if(k==='units'||k==='clock'){ renderList(); if(sel&&view==='detail') renderDetail(sel); if(view==='log') renderLog(); if(view==='trip') renderTrip(); syncRec(); } }
function showSettings(on){ sheetMode=on?'set':'map'; $('#sheet-t').textContent=on?'Settings':'Map options'; const g=$('#sheet-set'); g.setAttribute('aria-label',on?'Back to map options':'Settings'); g.classList.toggle('back',!!on);
  if(on) buildSettings(); else buildSheet(); $('#sheet-b').scrollTop=0; }
function openSettings(head){ openSheet(); showSettings(true); if(head){ const h=[...$('#sheet-b').querySelectorAll('h3')].find(n=>n.textContent===head); if(h) h.scrollIntoView({block:'start'}); } }
function buildSettings(){ const lb=$('#sheet-b'); lb.textContent=''; lb.classList.add('guide');
  const H=t=>el('h3',{text:t});
  const pick=(key,label,choices,sub)=>{ const id='set-'+key, x=el('select',{id:id},choices.map(c=>el('option',{value:String(c[0]),text:c[1]}))); x.value=String(pref(key));
    x.addEventListener('change',()=>{ const c=choices.find(c=>String(c[0])===x.value); setPref(key,c?c[0]:x.value); }); return el('label',{class:'field setrow',for:id},el('span',{text:label}),x,sub?el('small',{class:'snote',text:sub}):null); };
  const tog=(key,label,sub)=>{ const id='set-'+key; return el('label',{class:'lopt',for:id},el('input',{type:'checkbox',id:id,checked:!!pref(key),onchange:e=>setPref(key,e.target.checked)}),el('span',null,label,sub?el('small',null,sub):null)); };
  const sw=el('div',{class:'swatches',role:'radiogroup','aria-label':'Track colour'}); [['#2563eb','Blue'],['#dc2626','Red'],['#7c3aed','Purple'],['#0f766e','Teal'],['#111827','Black']].forEach(c=>{ const b=el('button',{type:'button',role:'radio','aria-checked':String(pref('trk')===c[0]),'aria-label':c[1],title:c[1],style:'--c:'+c[0]}); b.addEventListener('click',()=>{ setPref('trk',c[0]); buildSettings(); }); sw.append(b); });
  const hs=el('select',{id:'set-home'}); [...$('#home').children].forEach(n=>hs.append(n.cloneNode(true))); hs.value=homePicked()?U.home.id:''; hs.addEventListener('change',()=>{ const h=$('#home'); h.value=hs.value; if(hs.value==='pick') closeSheet(); const ev=new Event('change'); ev.go=true; h.dispatchEvent(ev); });
  const fq=el('input',{type:'text',id:'set-find',placeholder:'Town, address, ZIP or 39.10, -94.58',autocomplete:'off',enterkeyhint:'search'}), fb=el('button',{type:'button',class:'btn',text:'Set'}), fm=el('small',{class:'snote',text:'Use this when the device cannot find you, such as a desktop with location turned off. Names are looked up with OpenStreetMap; coordinates are not sent anywhere.'});
  const go=async()=>{ fb.disabled=true; fm.textContent='Looking…'; const r=await findSpot(fq.value); fb.disabled=false; if(r.err){ fm.textContent=r.err; return; } setSpot(r.lat,r.lon,r.name); if(map) map.setView([r.lat,r.lon],11); buildSettings(); };
  fb.addEventListener('click',go); fq.addEventListener('keydown',e=>{ if(e.key==='Enter'){ e.preventDefault(); go(); } });
  const nmPick=(k,label,list,sub)=>{ const id='set-nm-'+k, x=el('select',{id:id},list.map(c=>el('option',{value:String(c[0]),text:c[0]?(KM()?c[2]:c[1]):'Off'}))); x.value=String(nmSet()[k]);
    x.addEventListener('change',()=>{ const o={}; o[k]=+x.value; nmSave(o); const n=$('#near-'+k); if(n) n.value=x.value; }); return el('label',{class:'field setrow',for:id},el('span',{text:label}),x,sub?el('small',{class:'snote',text:sub}):null); };
  const ks=el('textarea',{id:'set-kitSign',rows:'2',placeholder:'More walks: youtube.com/@yourchannel'}); ks.value=pref('kitSign'); ['change','blur'].forEach(ev=>ks.addEventListener(ev,()=>{ if(ks.value.trim()!==pref('kitSign')) setPref('kitSign',ks.value.trim()); }));
  const add=(...a)=>a.forEach(x=>{ if(x) lb.append(x); });      /* Element.append(null) would print the word "null" */
  add(H('Look and units'),
    pick('theme','Colours',[['auto','Follow the phone'],['light','Always light'],['dark','Always dark']]),
    pick('themeL','Light colours',THEMES.filter(t=>t[2]==='l')),
    pick('themeD','Dark colours',THEMES.filter(t=>t[2]==='d')),
    tog('addMore','Adding a place also asks its kind, year and name','Off: one tap on Standing, Ruin, Trace or Odd find saves the place. "More details" on that card always opens the full form.'),
    tog('wikiPhotos','Photos from Wikipedia on place pages','Fetched from the place\'s Wikipedia article when you open it, with the photographer\'s credit. Off saves data on a weak signal.'),
    pick('units','Distances',[['mi','Miles and feet'],['km','Kilometres and metres']]),
    pick('clock','Clock',[['auto','Follow the phone'],['12','12-hour (2:30 PM)'],['24','24-hour (14:30)']]),
    el('div',{class:'field setrow'},el('span',{text:'Track colour'}),sw),
    H('Map'),
    pick('open','The map opens showing',[['last','Whatever was last showing']].concat(['streets','leaf','lidar','sat','topo'].filter(k=>LD[k]).map(k=>[k,LD[k].n]))),
    tog('cluster','Zoomed out, stand in for the pins','The heat map below, or numbered discs, in place of hundreds of pins. Off: every pin at every zoom, which is slow where places are thick.'),
    tog('heat','Zoomed out, show a heat map','Colour shows where places are thick: blue for a few, red for many. Tap it for a count, double-tap to zoom in. Off: numbered discs instead, each standing for the pins under it.'),
    tog('pinchStand','Smooth pinching','While two fingers are down the pins are shown as one picture that stretches with the map, and they come back when you let go. Off: every pin is moved on its own, which is slow where places are thick.'),
    pick('dbl','A double tap on the map zooms in',[[1,'One step'],[2,'Two steps'],[3,'Three steps'],[4,'Four steps']],'A double tap on a pin goes straight to street level.'),
    tog('hideGone','Hide places with nothing to see','Takes places marked "Nothing visible" or "Marker only" off the map, the Places list and the Near tab. Choosing either one in Filters still shows them. Drowned places stay: something can show at low water.'),
    tog('nativeLeads','Show Native American sites among the leads','Mounds, pueblos, rock art, heiau and other sites mapped on OpenStreetMap, and old sites on reservation land: turquoise dots when Unchecked leads is on, and rows in the Near tab. Off unless you switch it on here. Many are sacred, protected by law or closed: go only where whoever looks after the place invites visitors.'),
    tog('follow','Keep the map on me as I move','When your dot walks off the edge of the map, the map moves with it.'),
    pick('start','The map opens at',[['last','Where I left it'],['home','My start place']]),
    el('label',{class:'field setrow',for:'set-home'},el('span',{text:'Start place'}),hs,el('small',{class:'snote',text:'Drive times count from here, and the Places list puts the nearest first. While your location is switched on, the list counts from where you are instead. Until you choose a start place, the Atlas uses the start city nearest to where you are or last were.'})),
    el('div',{class:'field setrow'},el('label',{for:'set-find',text:'Or type your start place'}),el('div',{class:'findrow'},fq,fb),fm),
    H('Trip'),
    pick('tripStop','Time at each stop',[20,30,45,60,90,120].map(m=>[m,fmtMin(m)]),'Used for the arrival times and the sunset warning in the Trip tab.'),
    H('Near me'),
    nmPick('r','List what is within',NMR),
    nmPick('al','Buzz when I walk within',NMA,NATIVE?'While a field log is recording the phone buzzes with the screen off too. Old town centres are listed but never buzz.':'Works while the Atlas is open and showing where you are. Old town centres are listed but never buzz.'),
    tog('quietGone','No buzz for places with nothing to see','Places marked "Nothing visible" or "Marker only" are still listed in the Near tab, but do not buzz.'),
    tog('buzzVanished','Buzz for vanished places too','The orange dots: places the federal names file marks as gone. Off, they are listed in the Near tab but never buzz. Turn it on when you want to go and see whether anything is left.'),
    el('small',{class:'snote',text:'Which kinds count (places, leads, vanished places, mines, town centres) is chosen with the chips at the top of the Near tab.'}),
    el('div',{class:'field setrow'},el('span',{id:'set-muted',text:(U.mute&&U.mute.length?U.mute.length+(U.mute.length===1?' place is':' places are')+' silenced: listed in the Near tab, never buzzing.':'No single place is silenced. To silence one (the one by your house, say), tap it in the Near tab, then "Never buzz here".')}),U.mute&&U.mute.length?el('button',{class:'btn sm',id:'set-unmute',type:'button',onclick:()=>{ U.mute=[]; saveNow(); NM.ver++; NM.in.clear(); nmPush(true); showSettings(true); }},'Let them all buzz again'):null),
    H('Field log'),
    pick('detail','Track detail',[['fine','Fine: a point every 2 m'],['normal','Normal: every 4 m'],['coarse','Coarse: every 10 m']],NATIVE?'Coarse also checks GPS less often, which saves some battery on long days. Takes effect on the next recording.':'Takes effect on the next recording.'),
    NATIVE?tog('buzz','Vibrate on "Mark here"','A short buzz so you know the pin was dropped without looking.'):null,
    NATIVE?tog('autoPhotos','Find photos and video when a log ends'):null,
    NATIVE?pick('near','A photo joins a note within',[[10,'10 m'],[25,'25 m'],[50,'50 m']],'After changing this, use "Look again for photos" on a log. Photos you placed by hand stay put.'):null,
    H('Episode kit'),
    pick('kitBase','Draw the route map picture on',Object.keys(KITMAP).map(k=>[k,KITMAP[k][0]])),
    el('label',{class:'field setrow',for:'set-kitSign'},el('span',{text:'Lines to end every description'}),ks,el('small',{class:'snote',text:'Your channel link, credits or a standing thank-you. The kit adds them to each description it writes, above the Atlas credit.'})),
    H('Sharing and privacy'),
    pick('trim','Trim the ends of a shared walk',[[0,'Do not trim'],[100,'First and last 100 m'],[200,'First and last 200 m'],[500,'First and last 500 m']],'Applies to "Share this walk" and the GPX file, so a shared walk does not show where you parked or live. Your own copy is not changed.'),
    tog('previews','Include photo previews in a shared walk'),
    H('Your data'),
    NATIVE?tog('autoBackup','Save a backup file when a log ends','Download / Lost Hidden Atlas / atlas-backup.json on the phone.'):null);
  dataSections(lb); }
function openSheet(){ sheetMode='map'; $('#sheet-t').textContent='Map options'; $('#sheet-set').classList.remove('back'); $('#sheet-set').setAttribute('aria-label','Settings'); buildSheet(); $('#sheet').hidden=false; $('#scrim').hidden=false; try{ $('#sheet-x').focus({preventScroll:true}); }catch(e){} }
function closeSheet(){ $('#sheet').hidden=true; $('#scrim').hidden=true; }
function buildSheet(){
  if(sheetMode==='set') return;
  const lb=$('#sheet-b'), keep=lb.scrollTop; lb.textContent=''; lb.classList.remove('guide'); lb.classList.toggle('tips',!!U.ui.tips);
  /* the sheet lists every switch and nothing else; the small print under each shows only when asked for */
  lb.append(el('button',{class:'btn sm '+(U.ui.tips?'on':'pri'),id:'sheet-tips',type:'button','aria-pressed':String(!!U.ui.tips),onclick:()=>{ U.ui.tips=!U.ui.tips; save(); buildSheet(); }},U.ui.tips?'Hide the explanations':'What do these do?'));
  const H=t=>el('h3',{text:t}), note=t=>el('small',{class:'snote',text:t});
  const ck=(id,on,label,sub,fn)=>el('label',Object.assign({class:'lopt',for:id},sub?{title:sub}:{}),el('input',{type:'checkbox',id:id,checked:!!on,onchange:e=>fn(e.target.checked)}),el('span',null,label,sub?el('small',null,sub):null));
  if(schematic){ lb.append(el('p',{style:'margin:8px 0 0',text:LOCAL?'Live imagery could not load, so the map is showing a built-in outline. Old-map overlays and every scouting link still work. Reload when you are back online.':'This online copy cannot load live imagery, so the map is a built-in outline. Old-map overlays and every scouting link still work. Open the Atlas file, or host it, for satellite, leaf-off, LiDAR, public land and owner lookups.'})); }
  else {
    lb.append(H('Leaf-off aerial'));
    const y=el('select',{id:'leaf-year','aria-label':'Flight year',onchange:e=>{ U.ui.year=e.target.value; save(); if(U.ui.base==='leaf') setBase('leaf'); if(cmp.on&&cmp.key==='leaf') setCmp(); }},YEARS.map(v=>el('option',{value:v,text:v==='napp'?'1990s infrared':v==='Latest'?'Latest flight':v})));
    y.value=U.ui.year; lb.append(el('div',{class:'lsub'},el('span',{text:'Flight year'}),y),note('The year applies to New York. Blank? That year skipped this county. Massachusetts, Vermont, New Jersey, Connecticut and New Hampshire show their own latest state flight (the Vermont one is not always leaf-off). Rhode Island, Kansas, Pennsylvania and Maine show theirs once you zoom in past town level. Pennsylvania\'s server is slow: the satellite picture shows first and the bare-tree flight takes its place after a few seconds. Everywhere else is satellite, usually with leaves on.'));
    lb.append(H('LiDAR light'));
    const s=el('select',{id:'lidar-light','aria-label':'Light direction',onchange:e=>{ U.ui.light=e.target.value; save(); if(U.ui.base==='lidar') setBase('lidar'); if(cmp.on&&cmp.key==='lidar') setCmp(); }},Object.keys(LIGHT).map(v=>el('option',{value:v,text:LIGHT[v][0]})));
    s.value=U.ui.light; lb.append(el('div',{class:'lsub'},s),note('Changing the light makes faint walls and grades pop. It applies once you zoom in close, everywhere except Massachusetts, Vermont and Connecticut, which draw their LiDAR with a fixed light. Outside New York and New England the 1-metre LiDAR comes from the USGS at the last few zoom levels and takes a few seconds a tile; a coarser picture shows first.'));
    lb.append(H('Compare two layers'));
    lb.append(ck('cmp-on',cmp.on,'Show a second layer over the map','Drag a divider (Swipe), or lay one over the other (Overlay). The Compare button on the bar steps through both',v=>{ cmp.on=v; cmp.lap=0; setCmp(); cmpSave(); syncBar(); }));
    if(cmp.on){
      const ks=el('select',{id:'cmp-key','aria-label':'Second layer',onchange:e=>{cmp.key=e.target.value;setCmp();cmpSave();}},Object.keys(LD).map(k=>el('option',{value:k,text:LD[k].n}))); ks.value=cmp.key;
      const ms=el('select',{id:'cmp-mode','aria-label':'Compare mode',onchange:e=>{cmp.mode=e.target.value;cmp.lap=0;setCmp();cmpSave();syncBar();}},el('option',{value:'swipe',text:'Swipe'}),el('option',{value:'fade',text:'Overlay'})); ms.value=cmp.mode;
      lb.append(el('div',{class:'lsub'},ks,ms));
      if(cmp.mode==='fade') lb.append(el('div',{class:'lsub'},el('input',{type:'range',id:'cmp-op',min:'0.1',max:'1',step:'0.05',value:String(cmp.op),'aria-label':'Second layer strength',oninput:e=>{cmp.op=Math.min(1,Math.max(0.1,+e.target.value||0.6));map.getPane('cmp').style.opacity=cmp.op;$('#fade-op').value=String(cmp.op);cmpSave();}})));
    }
  }
  lb.append(H('Old survey map'));
  lb.append(ck('hist-on',U.ui.hist,'Lay it over the selected place','1890s–1930s USGS sheets, where one exists',v=>{ U.ui.hist=v; save(); showHist(); syncBar(); if(sel&&view==='detail') renderDetail(sel); }));
  lb.append(el('div',{class:'lsub'},el('span',{text:'Strength'}),el('input',{type:'range',id:'hist-op',min:'0.1',max:'1',step:'0.05',value:String(U.ui.histOp),'aria-label':'Old map strength',oninput:e=>{U.ui.histOp=+e.target.value;save();if(histLayer)histLayer.setOpacity(U.ui.histOp);}})));
  lb.append(H('Lines'));
  Object.keys(LGRP).forEach(g=>{ lb.append(ck('ln-'+g,U.ui.lines[g],LGRP[g][0],null,v=>{ U.ui.lines[g]=v; save(); drawLines(); syncBar(); }));
    if(U.ui.lines[g]||U.ui.tips) lb.append(el('div',{class:'lkeys'},LGRP[g][1].map(k=>el('span',{class:'lkey'},el('span',{class:'sw'+(LK[k][2]?' dash':''),style:'--c:'+LK[k][1]}),LK[k][0])))); });
  lb.append(note('Tap any line for its name and the Atlas places along it.'));
  if(!schematic){
    lb.append(H('Land and owners'));
    lb.append(ck('land-on',U.ui.land,'Public and protected land','From the national protected-areas database. Zoom in to town level',v=>{ U.ui.land=v; save(); drawLand(); syncBar(); }));
    if(U.ui.land||U.ui.tips) lb.append(el('div',{class:'lkeys'},Object.keys(PADC).map(k=>el('span',{class:'lkey'},el('span',{class:'sw',style:'--c:'+PADC[k][1]}),PADC[k][0]))));
    lb.append(ck('lots-on',U.ui.lots,'Lot lines','New York and Massachusetts property lines. Zoom in close',v=>{ U.ui.lots=v; save(); drawLots(); syncBar(); }));
    lb.append(note('Tap Owner? on the bar, then tap the map, to see the public-land unit and the parcel owner at that spot. Long-press the map for the same thing. Massachusetts is covered statewide; in New York not every county shares owner names.'));
  }
  lb.append(H('Leads'));
  lb.append(ck('leads-on',U.ui.leads,'Unchecked leads','Yellow dots: ruins, abandoned buildings, kilns, quarries and old farms that OpenStreetMap volunteers have mapped. Nobody has checked them for the Atlas, so one may be a fine ruin or nothing at all. Every state and province',v=>{ U.ui.leads=v; save(); drawLeads(); syncBar(); if(v&&map&&map.getZoom()<LEADZ) banner('Zoom in to see them: they show from about state level.',false,5000); }));
  lb.append(ck('xl-vanished',xlOn('vanished'),'Vanished places','Hamlets, churches, forts, airfields, hospitals and post offices the federal names file marks as gone: usually nothing is left, sometimes a cellar hole or a cemetery. Orange dots, from town level in. Every state; nobody has checked them',v=>{ xlSet('vanished',v); buildSheet(); }));
  if(xlOn('vanished')) lb.append(ck('xl-schools',U.ui.xl&&U.ui.xl.schools,'Old school sites too','Mostly one-room schoolhouses. There are thousands, so they are off unless you ask',v=>xlSet('schools',v)));
  lb.append(ck('xl-mines',xlOn('mines'),'Old mines and quarries','Iron mines, quarries, clay pits and prospects from U.S. Geological Survey records, most long closed. Grey dots, from town level in. Positions are rough and nobody has checked them; a separate kind of hunting from old buildings',v=>xlSet('mines',v)));
  lb.append(H('Found on LiDAR'));
  lb.append(ck('walls-on',U.ui.walls,'Stone walls','Low straight ridges a program picked out of the LiDAR ground model: field walls, yard walls, walled lanes. Zoom in to street level to see each one; zoomed out, shaded squares show where they are thick, which is where the old farms were. Only pieces that line up into a run, a corner or a yard are drawn; stray short pieces are left out, and so is everything on ground too rough to trust. Unchecked: some are ditch banks or old road edges, and many walls are missed. Only on the public land that has been swept so far'+(WALLS?' ('+WALLS.units.length+' forests and parks, '+WALLS.km+' km of wall)':''),v=>{ U.ui.walls=v; save(); drawWalls(); buildSheet(); }));
  if(U.ui.walls||U.ui.tips) lb.append(el('div',{class:'lkeys'},el('span',{class:'lkey'},el('span',{class:'sw',style:'--c:#ff7a1a'}),'A wall found on LiDAR'),el('span',{class:'lkey'},el('span',{class:'sw',style:'--c:#c2410c;opacity:.5;height:9px'}),'Ground with many walls')));
  lb.append(H('Places with history'));
  lb.append(ck('pock-on',U.ui.pockets,'Historic pockets','Purple discs: old town centres, and other places where historical markers and National Register listings bunch together. They show from the 20-mile scale in; zoom in to street level for the single buildings',v=>{ U.ui.pockets=v; save(); drawPockets(); buildSheet(); syncBar(); }));
  if(U.ui.pockets&&POCK){ const all=pockNear(pockList.mode), other=pockList.mode==='other';
    lb.append(ck('pock-r',U.ui.pockR!==false,'Listed buildings','White dots at street level: buildings and sites on the National Register of Historic Places. Tap one for its name',v=>{ U.ui.pockR=v; save(); pockDetail(); }));
    lb.append(ck('pock-m',U.ui.pockM,'Historical markers','Purple dots at street level: roadside plaques from HMdb.org. Many mark something that is gone, so they are off unless you ask',v=>{ U.ui.pockM=v; save(); pockDetail(); }));
    lb.append(ck('pock-o',U.ui.pockO,'Also show other pockets','Dashed rings: estates, mill sites, battlefields, campuses and city neighbourhoods away from the centre. Off unless you ask, because a city has many',v=>{ U.ui.pockO=v; save(); pockReset(); }));
    const seg=el('div',{class:'pockseg'}); [['rich','Richest'],['near','Nearest'],['other','Other pockets']].forEach(m=>seg.append(el('button',{class:'btn sm'+(pockList.mode===m[0]?' on':''),type:'button','aria-pressed':String(pockList.mode===m[0]),onclick:()=>{ pockList={mode:m[0],n:8}; buildSheet(); }},m[1])));
    const from=homePicked()?'your start place':'the middle of the map';
    lb.append(note(other?'Estates, mill sites, battlefields and other pockets within 40 miles of '+from+'.':'Old town centres within 40 miles of '+from+'. Tap one to go there.'),seg);
    if(all.length){ const ul=el('div',{class:'pocklist'}); all.slice(0,pockList.n).forEach(o=>ul.append(el('button',{class:'btn sm',type:'button',onclick:()=>{ closeSheet(); map.setView([o.k[0],o.k[1]],15); }},el('b',{text:o.k[7]}),el('small',{text:' '+pockLine(o)})))); lb.append(ul);
      if(all.length>pockList.n) lb.append(el('button',{class:'btn sm',type:'button',id:'pock-more',onclick:()=>{ pockList.n+=8; buildSheet(); }},'Show more ('+(all.length-pockList.n)+')')); }
    else lb.append(note('None are mapped within 40 miles of '+from+' yet. The layer covers '+(Object.keys(POCK.s||{}).length>12?Object.keys(POCK.s).length+' states':Object.keys(POCK.s||{}).map(x=>STATE[x]||x).join(', '))+' so far.')); }
  if(map&&!schematic){ lb.append(H('Offline'));
    lb.append(el('button',{class:'btn sm',type:'button',id:'view-off','aria-expanded':String(viewOpen),onclick:()=>{ viewOpen=!viewOpen; buildSheet(); }},viewOpen?'Close':'Save this map view for offline…'));
    if(viewOpen) lb.append(viewBox()); }
  lb.scrollTop=keep;
}
function goSchematic(){
  if(schematic) return; schematic=true;
  if(baseLayer){ map.removeLayer(baseLayer); baseLayer=null; } if(cmpLayer){ map.removeLayer(cmpLayer); cmpLayer=null; } $('#swipe').hidden=true;
  let g; try{ g=JSON.parse(document.getElementById('d-base').textContent); }catch(e){ g=null; }
  if(g){ const cv=L.canvas({padding:0.3}); const css=getComputedStyle(document.documentElement); const v=n=>css.getPropertyValue(n).trim();
    const flip=c=>c.map(p=>[p[1],p[0]]);
    g.counties.forEach(c=>L.polyline(flip(c),{renderer:cv,color:v('--line'),weight:1,interactive:false}).addTo(map));
    g.lakes.forEach(c=>L.polygon(flip(c),{renderer:cv,color:v('--water'),weight:1,fillColor:v('--water'),fillOpacity:0.35,interactive:false}).addTo(map));
    g.rivers.forEach(c=>L.polyline(flip(c),{renderer:cv,color:v('--water'),weight:2,interactive:false}).addTo(map));
    g.roads.forEach(r=>L.polyline(flip(r.c),{renderer:cv,color:v('--brown'),weight:r.t?1.6:0.8,opacity:r.t?0.8:0.5,interactive:false}).addTo(map));
    g.towns.forEach(t=>L.marker([t[1],t[2]],{interactive:false,keyboard:false,icon:L.divIcon({className:'townlbl'+(t[3]?' big':''),html:'',iconSize:[0,0]})}).addTo(map).getElement().textContent=t[0]);
  }
  banner(LOCAL?'Live map imagery could not load, so you are seeing a built-in outline. Check your connection and reload.':'This online copy cannot load live map imagery. Pins, old maps, drive times and links all work here; open the Atlas file on a computer for satellite, leaf-off and LiDAR.',true,14000);
  buildBar(); showHist(); if(sel&&view==='detail') renderDetail(sel);
}

/* rail and canal lines */
const LK={ab:['Abandoned railroad','#ff5a1f','8 6'],tr:['Old trolley line','#e83fd0','2 6'],tl:['Rail trail on an old line','#12a150','8 6'],di:['Disused track, rails still down','#ffab1f',null],rr:['Railroad in use','#2b3136',null],co:['Old canal','#00b3ff','7 5'],cn:['Canal in use','#1464d2',null]};
const LGRP={oldrail:['Old rail and trolley lines',['ab','tr','tl','di']],canal:['Canals, old and current',['co','cn']],rail:['Railroads in use',['rr']]};
let LINES=null, lineLayer={}, lineHi=null, lineCanvas=null;
function prepLines(a){ a.forEach(f=>{ let x=90,b=-90,c=180,d=-180; f.c.forEach(p=>p.forEach(q=>{ if(q[0]<x)x=q[0]; if(q[0]>b)b=q[0]; if(q[1]<c)c=q[1]; if(q[1]>d)d=q[1]; })); f.bb=[x,c,b,d]; }); return a; }
function lineChunks(f){ if(f.c.length<2) return [f.c]; const m={}, o=[]; f.c.forEach(p=>{ const k=Math.floor(p[0][0]*2)+','+Math.floor(p[0][1]*2); if(!m[k]){ m[k]=[]; o.push(m[k]); } m[k].push(p); }); return o; }
let linesWait=null, linesTold=false;
/* ---- where the lines come from ----
   The Android app and the single-file copies hold every line in one file (data/lines.json, or the page itself).
   The hosted copy fetches them a state at a time, because all of them together are several megabytes and a reader looks
   at one or two states. The page data lists what there is (D.lx, written by tools/lines_split.py):
     data/lines/wide.json     every state's lines thinned for a wide view: what zoom 8 and wider are drawn from
     data/lines/<state>.json  one state at full detail: fetched from zoom 9 for each state with lines in or near the view,
                              and for the state a place page is in
   LINES is then whatever has arrived so far, so the code below never assumes a line is there. Each address carries a
   stamp of its content, and the offline worker keeps these files across builds (sw.js). */
const LX=HOSTED&&!AT&&D.lx&&D.lx.s?D.lx:null, LWIDE=2;         /* LWIDE: how many levels of LLEV are drawn from wide.json */
let lineWide=null, lineWideWait=0, lineGot={}, lineCells=null;   /* lineGot: state -> 1 asked for, 2 here, or the time it failed */
function linesData(){ if(LINES) return LINES; if(LX) return LINES=[]; const n=document.getElementById('d-lines'); if(!n){ loadLines(); return []; }
  try{ LINES=JSON.parse(n.textContent); }catch(e){ LINES=[]; } return prepLines(LINES); }
function linesArrived(full){ drawLines();
  if(full&&sel&&view==='detail'&&!/^(INPUT|TEXTAREA|SELECT)$/.test((document.activeElement||{}).tagName||'')){ const v=$('#v-detail'), y=v.scrollTop; renderDetail(sel); v.scrollTop=y; } }
function linesFailed(){ if(!linesTold){ linesTold=true; banner('Old rail and canal lines could not load. They will try again when you are back online.',true,7000); } }
function loadLines(){ if(linesWait||LINES) return;
  linesWait=(AT?AT.fetch('data/lines.json'):fetch('data/lines.json'+VQ)).then(r=>{ if(!r.ok) throw new Error('http '+r.status); return r.json(); }).then(a=>{ LINES=prepLines(a); linesArrived(true); })
    .catch(()=>{ linesWait=null; linesFailed(); }); }
/* the states with lines in a box, from the quarter-degree squares each state's lines touch (LSQ squares to a degree, as
   SQ in tools/lines_split.py) */
const LSQ=4;
let lineBox=null;                                              /* the box round every line there is */
function lineStatesIn(s,w,n,e){ const out=new Set(); if(!LX) return out;
  if(!lineCells){ lineCells=new Map(); let a0=1e9,b0=1e9,a1=-1e9,b1=-1e9; Object.keys(LX.s).forEach(k=>{ const c=LX.s[k].c||[]; for(let i=0;i<c.length;i+=2){ const q=c[i]+','+c[i+1], a=lineCells.get(q); if(a) a.push(k); else lineCells.set(q,[k]);
      if(c[i]<a0)a0=c[i]; if(c[i]>a1)a1=c[i]; if(c[i+1]<b0)b0=c[i+1]; if(c[i+1]>b1)b1=c[i+1]; } }); lineBox=a1>=a0?L.latLngBounds([a0/LSQ,b0/LSQ],[(a1+1)/LSQ,(b1+1)/LSQ]):null; }
  if(n===undefined) return out;                                /* called only to work out lineBox */
  const i0=Math.floor(s*LSQ), i1=Math.floor(n*LSQ), j0=Math.floor(w*LSQ), j1=Math.floor(e*LSQ); if((i1-i0+1)*(j1-j0+1)>12000) return out;
  for(let i=i0;i<=i1;i++) for(let j=j0;j<=j1;j++){ const a=lineCells.get(i+','+j); if(a) a.forEach(k=>out.add(k)); }
  return out; }
function lineFetch(k){ const g=lineGot[k]; if(g===1||g===2||(g&&Date.now()-g<30000)) return; lineGot[k]=1;
  fetch('data/lines/'+k+'.json?v='+LX.s[k].h).then(r=>{ if(!r.ok) throw new Error('http '+r.status); return r.json(); })
    .then(a=>{ lineGot[k]=2; LINES=(LINES||[]).concat(prepLines(a)); lineForget(LWIDE,LLEV.length+1); linesArrived(true);
      /* the wide picture too, a little later, so that zooming out works with no signal; not when no line is switched on (a place page asked) or the phone is saving data */
      if(!lineWide&&Object.keys(LGRP).some(g=>U.ui.lines[g])&&!(navigator.connection&&navigator.connection.saveData)) setTimeout(lineWideFetch,6000); })
    .catch(()=>{ lineGot[k]=Date.now(); linesFailed(); }); }
function lineWideFetch(){ if(lineWide||lineWideWait===1||Date.now()-lineWideWait<30000) return; lineWideWait=1;
  fetch('data/lines/wide.json?v='+LX.w).then(r=>{ if(!r.ok) throw new Error('http '+r.status); return r.json(); })
    .then(j=>{ lineWide=j; lineWideWait=0; lineForget(0,LWIDE); linesArrived(false); })
    .catch(()=>{ lineWideWait=Date.now(); const z=map?map.getZoom():0; if(z>=LMINZ&&lineLevel(z)>=0&&lineLevel(z)<LWIDE) linesFailed(); }); }
/* new lines have arrived: take what was drawn from the old set off the map and forget it (levels a to b-1 of LLEV; the
   close-up pieces too when b is past the last level). The next syncLines() builds it again, for the view only. */
function lineForget(a,b){ for(let i=a;i<b&&i<LLEV.length;i++){ const m=lineIdx[i]; if(m){ m.forEach(t=>{ if(t.on) map.removeLayer(t.pl); }); lineIdx[i]=null; } }
  if(b>LLEV.length&&lineSet){ Object.keys(lineSet).forEach(g=>lineSet[g].forEach(c=>{ if(c.on) map.removeLayer(c.pl); })); lineSet=null; } }
function linesRetry(){ linesTold=false; if(lineWideWait>1) lineWideWait=0; Object.keys(lineGot).forEach(k=>{ if(lineGot[k]>2) delete lineGot[k]; }); }
/* the state files for some spots (a place page, an area being saved for offline) */
function linesWarm(pts){ if(LX) pts.forEach(p=>lineStatesIn(p.lat-0.01,p.lon-0.01,p.lat+0.01,p.lon+0.01).forEach(lineFetch)); }
function distToPart(lat,lon,part){ const kx=Math.cos(rad(lat))*111320, ky=110540; let best=1e12;
  for(let i=1;i<part.length;i++){ const ax=(part[i-1][1]-lon)*kx, ay=(part[i-1][0]-lat)*ky, bx=(part[i][1]-lon)*kx, by=(part[i][0]-lat)*ky, dx=bx-ax, dy=by-ay, L=dx*dx+dy*dy; let t=L?-(ax*dx+ay*dy)/L:0; t=t<0?0:t>1?1:t; const x=ax+t*dx, y=ay+t*dy, d2=x*x+y*y; if(d2<best) best=d2; }
  return Math.sqrt(best); }
function distToFeat(p,f,parts){ const m=0.006; if(!parts&&(p.lat<f.bb[0]-m||p.lat>f.bb[2]+m||p.lon<f.bb[1]-m||p.lon>f.bb[3]+m)) return 1e9; let best=1e9; (parts||f.c).forEach(pt=>{ const d=distToPart(p.lat,p.lon,pt); if(d<best) best=d; }); return best; }
const LGOF={ab:'r',tr:'r',tl:'r',di:'r',co:'c',cn:'x',rr:'x'};
function corridor(f,part){
  const grp=LGOF[f.k]; let base=[];
  if(f.n&&!part) linesData().forEach(g=>{ if(g.n===f.n&&LGOF[g.k]===grp) base=base.concat(g.c); }); else base=[part||f.c[0]];
  if(grp==='x') return base;
  let a=90,b=-90,c=180,d=-180; base.forEach(p=>p.forEach(q=>{ if(q[0]<a)a=q[0]; if(q[0]>b)b=q[0]; if(q[1]<c)c=q[1]; if(q[1]>d)d=q[1]; })); const m=0.002;
  const near=q=>{ if(q[0]<a-m||q[0]>b+m||q[1]<c-m||q[1]>d+m) return false; for(let i=0;i<base.length;i++){ if(distToPart(q[0],q[1],base[i])<=80) return true; } return false; };
  const out=base.slice(), have=new Set(base);
  linesData().forEach(g=>{ if(LGOF[g.k]!==grp) return; g.c.forEach(pt=>{ if(have.has(pt)) return; if(near(pt[0])||near(pt[pt.length-1])) out.push(pt); }); });
  return out;
}
function lineLabel(f){ return f.n||('an unnamed '+LK[f.k][0].toLowerCase()); }
function setLine(sel2,quiet){
  if(lineHi&&map){ map.removeLayer(lineHi); lineHi=null; }
  if(!sel2){ F.line=null; return; }
  const f=sel2.f, parts=corridor(f,sel2.parts?sel2.parts[0]:null), ids=new Set(), ord=new Map();
  let a=90,b=-90,c=180,d=-180; parts.forEach(p=>p.forEach(q=>{ if(q[0]<a)a=q[0]; if(q[0]>b)b=q[0]; if(q[1]<c)c=q[1]; if(q[1]>d)d=q[1]; }));
  const byLat=(b-a)*111>(d-c)*82;
  sites().forEach(s=>{ const p=pos(s); if(distToFeat(p,f,parts)<=450){ ids.add(s.id); ord.set(s.id,byLat?-p.lat:p.lon); } });
  F.line={k:f.k,label:lineLabel(f)+' and the segments it joins',ids:ids,ord:ord};
  if(map){ lineHi=L.polyline(parts,{pane:'lines',renderer:lineCanvas,color:'#ffe600',weight:9,opacity:0.55,interactive:false}).addTo(map); lineHi.bringToBack(); }
  if(!quiet){ showView('list'); sel=null; drawSel(); showHist(); refresh(); if(map){ try{ map.fitBounds(L.latLngBounds(parts.reduce((x,p)=>x.concat(p),[])).pad(0.1)); }catch(e){} } }
}
function lineWidePopup(k,latlng){
  const box=el('div',{class:'ctx'},el('b',{text:LK[k][0]}),el('span',{style:'color:#5b6660',text:'Zoom in for its name and the Atlas places along it.'}),
    el('button',{class:'btn sm',type:'button',onclick:()=>{ map.closePopup(); map.setView(latlng,11); }},'Zoom in here'));
  L.popup({maxWidth:270}).setLatLng(latlng).setContent(box).openOn(map); }
function linePopup(f,part,latlng){
  const whole={f:f}, one={f:f,parts:[part]}; const tgt=f.n?whole:one;
  const cp=corridor(f,f.n?null:part); const n=sites().filter(s=>distToFeat(pos(s),f,cp)<=450).length;
  const box=el('div',{class:'ctx'},el('b',{text:f.n||'Unnamed line'}),el('span',{style:'color:#5b6660',text:LK[f.k][0]+(f.y?' · '+f.y:'')}),
    f.k==='tl'?el('span',{style:'color:#5b6660',text:'Mapped as a path or trail today. Check the trail name for access.'}):null,
    el('button',{class:'btn sm',type:'button',disabled:!n,onclick:()=>{ map.closePopup(); setLine(tgt); }},n?('Show the '+n+' Atlas place'+(n>1?'s':'')+' along it'):'No Atlas places within 450 m'),
    ext('https://www.google.com/maps/search/?api=1&query='+latlng.lat.toFixed(5)+','+latlng.lng.toFixed(5),'This spot in Google Maps','btn sm'));
  L.popup({maxWidth:270}).setLatLng(latlng).setContent(box).openOn(map);
}
/* ---- drawing the lines fast ----
   The lines are 108,000 points in 16,000 pieces. Leaflet works out every point of every layer on the map again at each
   zoom step, in view or not, and each layer costs something on top of its points. So what is on the map depends on the zoom:
   - zoom 13 and closer: one layer for each piece of each line, at full detail, only where its half-degree cell is in or
     near the view. A tap picks the line directly.
   - wider than that (LLEV): one layer for each kind of line in each square of the map, thinned to what a pixel can show at
     that zoom, and only the squares in or near the view. The squares grow as the map zooms out. Measured round Albany:
     zoom 8 had 21,000 points on the map and has 13,500; zoom 9 had 337 layers and has 35.
   - one layer draws both the white casing and the colour, where there used to be two. */
const CasedLine=L.Polyline.extend({ _updatePath:function(){ const r=this._renderer, o=this.options; if(!r||!r._updatePoly) return;
  const c=o.color, w=o.weight, d=o._dashArray, op=o.opacity;
  o.color='#ffffff'; o.weight=o.casing; o._dashArray=null; o.opacity=0.75; r._updatePoly(this);
  o.color=c; o.weight=w; o._dashArray=d; o.opacity=op; r._updatePoly(this); } });
function thinPart(part,tol){ const n=part.length; if(n<3) return part;      /* Douglas-Peucker, in degrees */
  const keep=new Uint8Array(n); keep[0]=keep[n-1]=1; const st=[0,n-1], kx=Math.cos(rad(part[0][0])), t2=tol*tol;
  while(st.length){ const b=st.pop(), a=st.pop(), ax=part[a][1]*kx, ay=part[a][0], dx=part[b][1]*kx-ax, dy=part[b][0]-ay, l2=dx*dx+dy*dy; let md=0, mi=-1;
    for(let i=a+1;i<b;i++){ const px=part[i][1]*kx-ax, py=part[i][0]-ay; let t=l2?(px*dx+py*dy)/l2:0; t=t<0?0:t>1?1:t; const ex=px-t*dx, ey=py-t*dy, e=ex*ex+ey*ey; if(e>md){ md=e; mi=i; } }
    if(md>t2){ keep[mi]=1; st.push(a,mi,mi,b); } }
  const out=[]; for(let i=0;i<n;i++) if(keep[i]) out.push(part[i]); return out; }
let lineSet=null;
const LKG={}; Object.keys(LGRP).forEach(g=>LGRP[g][1].forEach(k=>{ LKG[k]=g; }));              /* kind of line -> its switch */
function lineSets(){ if(lineSet) return lineSet; const data=linesData(); if(!data.length) return null; lineSet={};
  Object.keys(LGRP).forEach(g=>{ lineSet[g]=[]; });
  data.forEach(f=>{ const g=LKG[f.k]; if(!lineSet[g]) return; lineChunks(f).forEach(ch=>{ let a=90,b=-90,c=180,d=-180; ch.forEach(p=>p.forEach(q=>{ if(q[0]<a)a=q[0]; if(q[0]>b)b=q[0]; if(q[1]<c)c=q[1]; if(q[1]>d)d=q[1]; }));
    lineSet[g].push({f:f,ch:ch,b:L.latLngBounds([a,c],[b,d]),pl:null,on:false}); }); });
  return lineSet; }
/* wide: square ends and plain corners. Rounding every end and corner of thousands of short pieces was a third of the cost
   of drawing a wide view, and cannot be seen on a line under 3 pixels thick. */
const lineStyle=(k,wide)=>{ const st=LK[k], o={pane:'lines',renderer:lineCanvas,color:st[1],weight:k==='rr'?1.5:2.6,casing:k==='rr'?3.5:5,opacity:1,dashArray:st[2],bubblingMouseEvents:false};
  if(wide){ o.lineCap='butt'; o.lineJoin='bevel'; } return o; };
function lineMake(c){ const f=c.f, pl=new CasedLine(c.ch,lineStyle(f.k));
  pl.on('click',e=>{ if(adding||pickingHome||asking){ onMapClick(e); return; } let part=c.ch[0], bd=1e12; if(c.ch.length>1) c.ch.forEach(q=>{ const d=distToPart(e.latlng.lat,e.latlng.lng,q); if(d<bd){ bd=d; part=q; } }); linePopup(f,part,e.latlng); });
  return pl; }
/* The wider levels. z: the closest zoom the level serves; cell: the side of its squares in degrees; tol: how
   far a thinned line may stray, in degrees of latitude, about one pixel at that zoom. */
const LLEV=[{z:6,cell:8,tol:0.016},{z:8,cell:2,tol:0.004},{z:10,cell:1,tol:0.0009},{z:12,cell:0.5,tol:0.00018}];
const lineLevel=z=>{ for(let i=0;i<LLEV.length;i++) if(z<=LLEV[i].z) return i; return -1; };
const LMINZ=5;      /* wider than this (the whole country on a phone) the lines are a smudge on one corner: none are drawn, and the hosted copy fetches none */
let lineIdx=[];
function lineTiles(li){ if(lineIdx[li]) return lineIdx[li]; const wide=!!LX&&li<LWIDE; if(wide&&!lineWide) return null;
  const S=LLEV[li].cell, m=new Map();
  const put=(k,p)=>{ const key=k+'|'+Math.floor(p[0][0]/S)+','+Math.floor(p[0][1]/S); let t=m.get(key); if(!t){ t={k:k,raw:[],a:90,b:-90,c:180,d:-180,pl:null,on:false}; m.set(key,t); }
    t.raw.push(p); p.forEach(q=>{ if(q[0]<t.a)t.a=q[0]; if(q[0]>t.b)t.b=q[0]; if(q[1]<t.c)t.c=q[1]; if(q[1]>t.d)t.d=q[1]; }); };
  if(wide) Object.keys(lineWide).forEach(k=>{ if(LKG[k]) lineWide[k].forEach(p=>put(k,p)); });
  else linesData().forEach(f=>{ if(LKG[f.k]) f.c.forEach(p=>put(f.k,p)); });
  m.forEach(t=>{ t.bb=L.latLngBounds([t.a,t.c],[t.b,t.d]); });
  return lineIdx[li]=m; }
function lineTileMake(t,li){ const tol=LLEV[li].tol, min=tol*1.3, geo=[], k=t.k;
  t.raw.forEach(p=>{ const q=thinPart(p,tol); if(q.length>2||Math.abs(q[0][0]-q[q.length-1][0])+Math.abs(q[0][1]-q[q.length-1][1])>min) geo.push(q); });      /* a piece shorter than a pixel is left out */
  if(!geo.length) return false;
  const pl=new CasedLine(geo,lineStyle(k,true));
  pl.on('click',e=>{ if(adding||pickingHome||asking){ onMapClick(e); return; } const la=e.latlng.lat, lo=e.latlng.lng; let bf=null, bp=null, bd=1e12;
    linesData().forEach(f=>{ if(f.k!==k||la<f.bb[0]-0.1||la>f.bb[2]+0.1||lo<f.bb[1]-0.1||lo>f.bb[3]+0.1) return; f.c.forEach(q=>{ const d=distToPart(la,lo,q); if(d<bd){ bd=d; bf=f; bp=q; } }); });
    /* the hosted copy, wide view: the line under the finger may be in a state not fetched yet, and the nearest line that
       has been fetched is then some other one. 12 pixels and the thinning are as far as the real line can be from a tap. */
    if(LX&&li<LWIDE&&bd>12*40075016*Math.cos(rad(la))/(256*Math.pow(2,map.getZoom()))+tol*111000){ lineWidePopup(k,e.latlng); return; }
    if(bf) linePopup(bf,bp,e.latlng); });
  return pl; }
function syncLines(){ if(!map||(!LX&&!lineSets())) return; const z=map.getZoom(), li=z<LMINZ?-2:lineLevel(z), vb=map.getBounds().pad(0.35);      /* li: a level of LLEV, -1 close up, -2 too wide to draw any */
  if(LX&&li>-2&&Object.keys(LGRP).some(g=>U.ui.lines[g])){     /* the hosted copy: ask for what this view is drawn from */
    if(li<0||li>=LWIDE) lineStatesIn(vb.getSouth(),vb.getWest(),vb.getNorth(),vb.getEast()).forEach(lineFetch);
    else { lineStatesIn(); if(lineBox&&vb.intersects(lineBox)) lineWideFetch(); } }      /* a wide view of ground with no lines at all fetches nothing */
  LLEV.forEach((_,i)=>{ if(i!==li&&!lineIdx[i]) return;                        /* a level never looked at has nothing on the map */
    const T=lineTiles(i); if(!T) return;                                       /* the wide picture has not arrived yet */
    T.forEach(t=>{ const want=i===li&&!!U.ui.lines[LKG[t.k]]&&vb.intersects(t.bb);
      if(want){ if(t.pl===null) t.pl=lineTileMake(t,i); if(t.pl&&!t.on){ t.pl.addTo(map); t.on=true; } }
      else if(t.on){ map.removeLayer(t.pl); t.on=false; } }); });
  const S=lineSets();
  if(S) Object.keys(LGRP).forEach(g=>{ const on=li===-1&&!!U.ui.lines[g];
    S[g].forEach(c=>{ const want=on&&vb.intersects(c.b); if(c.on===want) return;
      if(want){ if(!c.pl) c.pl=lineMake(c); c.pl.addTo(map); } else map.removeLayer(c.pl);
      c.on=want; }); });
  if(lineHi) lineHi.bringToBack(); }
function drawLines(){
  if(!map) return; if(!lineCanvas){ map.createPane('lines').style.zIndex=380; lineCanvas=L.canvas({pane:'lines',tolerance:7}); }
  if(!LINES){ linesData(); if(!LINES) return; }
  if(!map._lnOn){ map._lnOn=true; map.on('moveend',syncLines); }
  syncLines();
}
function nearLines(p){ linesWarm([p]); const out=[], seen=new Set(); linesData().forEach(f=>{ if(f.k==='rr'||f.k==='cn') return; if(f.n){ const d=distToFeat(p,f); if(d<=350&&!seen.has(f.k+f.n)){ seen.add(f.k+f.n); out.push({f:f,d:d}); } }
    else f.c.forEach(part=>{ const d=distToFeat(p,f,[part]); if(d<=350) out.push({f:f,parts:[part],d:d}); }); });
  return out.sort((a,b)=>a.d-b.d).slice(0,6); }

/* public land, lot lines, leads, and "whose land is it" */
const PADC={OA:['Open to the public','#1a9641'],RA:['Restricted: permit, fee or season','#e08a00'],XA:['Closed to the public','#d7191c'],UK:['Access not recorded','#7b6fb5']};
const PADRANK={OA:0,RA:1,UK:2,XA:3};
const PADU='https://services.arcgis.com/v01gqwM5QqNysAAi/arcgis/rest/services/PADUS_Public_Access/FeatureServer/0/query';
const PARU='https://services6.arcgis.com/EbVsqZ18sv1kVJ3k/arcgis/rest/services/NYS_Tax_Parcels_Public/FeatureServer/1/query';
const CNTU='https://services6.arcgis.com/EbVsqZ18sv1kVJ3k/arcgis/rest/services/NYS_Civil_Boundaries/FeatureServer/2/query';
const PCLASS={1:'Agricultural',2:'Residential',3:'Vacant land',4:'Commercial',5:'Recreation and entertainment',6:'Community services',7:'Industrial',8:'Public services',9:'Wild, forest, conservation land or public park'};
const MAPU='https://services1.arcgis.com/hGdibHYSPO59RG1h/arcgis/rest/services/Massachusetts_Property_Tax_Parcels/FeatureServer/0/query';
const MAUSE={0:'Mixed use',1:'Residential',2:'Open space',3:'Commercial',4:'Industrial',5:'Personal property',6:'Forest land (Chapter 61)',7:'Farm land (Chapter 61A)',8:'Recreation land (Chapter 61B)',9:'Tax-exempt: public, charitable or religious'};
const PCX={695:'Cemetery',931:'State Forest Preserve',932:'State reforestation land',961:'State park',963:'Municipal park'};
const land={grp:null,cv:null,cells:new Map(),seen:new Set(),told:false};
function drawLand(){
  if(!map) return;
  if(!U.ui.land||schematic){ if(land.grp) map.removeLayer(land.grp); return; }
  if(!land.grp){ const pn=map.createPane('land'); pn.style.zIndex=330; pn.style.pointerEvents='none'; land.cv=L.canvas({pane:'land',padding:0.3}); land.grp=L.layerGroup(); }
  land.grp.addTo(map);
  if(map.getZoom()<11) return;
  const b=map.getBounds(), CW=0.25, CH=0.2; let n=0;
  for(let x=Math.floor(b.getWest()/CW);x<=Math.floor(b.getEast()/CW);x++) for(let y=Math.floor(b.getSouth()/CH);y<=Math.floor(b.getNorth()/CH);y++){
    const k=x+','+y; if(land.cells.has(k)||n>=12) continue; n++; land.cells.set(k,1); loadLand(x*CW,y*CH,CW,CH,k); } }
async function loadLand(w,s,cw,ch,k){
  try{ const u=PADU+'?where=1%3D1&geometry='+[w,s,w+cw,s+ch].map(v=>v.toFixed(3)).join(',')+'&geometryType=esriGeometryEnvelope&inSR=4326&spatialRel=esriSpatialRelIntersects&outFields=OBJECTID,Unit_Nm,Pub_Access&outSR=4326&maxAllowableOffset=0.0004&geometryPrecision=5&f=geojson';
    const j=await (await fetch(u)).json(); if(!j||!j.features) throw new Error('no data');
    j.features.forEach(f=>{ const id=f.properties.OBJECTID; if(land.seen.has(id)||!f.geometry) return; land.seen.add(id); const c=(PADC[f.properties.Pub_Access]||PADC.UK)[1];
      L.geoJSON(f,{pane:'land',renderer:land.cv,interactive:false,style:{color:c,weight:1.2,opacity:0.9,fillColor:c,fillOpacity:0.2}}).addTo(land.grp); });
  }catch(e){ land.cells.delete(k); if(!land.told){ land.told=true; banner(navigator.onLine===false?'Public land needs a signal to load.':'Public land could not load here. It works when the Atlas is opened as a file or from your own web address.',true,9000); } } }
function drawLots(){
  if(!map) return;
  if(!U.ui.lots||schematic){ if(lotLayer) map.removeLayer(lotLayer); return; }
  if(!lotLayer){ const pn=map.createPane('lots'); pn.style.zIndex=340; pn.style.pointerEvents='none';
    lotLayer=new FnLayer('',{pane:'lots',minZoom:15,maxZoom:20,attribution:'NYS DEC, MassGIS parcels',fn:c=>{ const p=tileCenter(c);
      if(regionOf(p[0],p[1])==='ma') return xyz('https://tiles.arcgis.com/tiles/hGdibHYSPO59RG1h/arcgis/rest/services/MassGIS_Level3_Parcels/MapServer/tile/{z}/{y}/{x}',c,20);
      return exportUrl('https://gisservices.dec.ny.gov/arcgis/rest/services/parcel_boundaries/MapServer/export',c,'&transparent=true').replace('format=jpg','format=png32'); }}); }
  lotLayer.addTo(map); }
/* Dots that are on the map only while they are in or near the view. Leaflet works out the position of every layer on the
   map again at each zoom step, on screen or not, so a few thousand dots a long way off made every zoom step slow.
   V = viewDots(); viewSync(V, the items wanted now, make(item) -> layer) returns how many were added. */
function viewDots(){ return {grp:L.layerGroup(),on:new Set(),mk:new Map()}; }
function viewSync(V,want,make){ const w=new Set(want); let added=0;
  V.on.forEach(x=>{ if(!w.has(x)){ V.grp.removeLayer(V.mk.get(x)); V.on.delete(x); } });
  want.forEach(x=>{ if(V.on.has(x)) return; let m=V.mk.get(x); if(!m){ m=make(x); V.mk.set(x,m); } V.grp.addLayer(m); V.on.add(x); added++; });
  return added; }
let LEADS=null, leadGrp=null;
/* Lead dots show from zoom LEADZ in. Since November 2026 the leads cover the whole continent (7,400 of them): a view of
   half a country held thousands of dots and each zoom step took over half a second on a phone. At LEADZ and closer the
   most a view holds is about what the Northeast alone held before. */
const LEADZ=6;
/* Native American sites and leads on reservation land are their own category, kept in a second file (tools/leads.py), which
   data/leads.json names in x.native. The Atlas asks for it only when a reader has switched "nativeLeads" on under the gear
   and leads are in use; its rows carry a fifth value, 1, and are drawn (turquoise), listed in Near and tapped like any lead
   while the switch is on. Switched off, which is how it starts, none of it is fetched, drawn or listed. */
function leadRows(){ return LEADS.xp&&pref('nativeLeads')?(LEADS.all||(LEADS.all=LEADS.p.concat(LEADS.xp))):LEADS.p; }
function leadsMore(){ const x=LEADS&&LEADS.x&&LEADS.x.native; if(!x||!pref('nativeLeads')||LEADS.xp||leadsMore.wait||Date.now()-(leadsMore.fail||0)<30000) return;
  const p='data/leads/native-'+x.h+'.json';
  leadsMore.wait=(AT?AT.fetch(p):fetch(p+'?v='+x.h)).then(r=>{ if(!r.ok) throw new Error('http '+r.status); return r.json(); })
    .then(j=>{ const ix=j.t.map(n=>{ let i=LEADS.t.indexOf(n); if(i<0) i=LEADS.t.push(n)-1; return i; }); LEADS.xp=j.p.map(q=>[q[0],q[1],ix[q[2]],q[3],1]); leadsMore.wait=null; drawLeads(); nmLoaded(); })
    .catch(()=>{ leadsMore.wait=null; leadsMore.fail=Date.now(); if(!leadsMore.said){ leadsMore.said=true; banner('The Native American sites could not load. Check your signal.',true,6000); } }); }
function drawLeads(){
  if(!map) return;
  if(!U.ui.leads){ if(leadGrp) map.removeLayer(leadGrp.grp); return; }
  if(!LEADS){ leadsLoad(); if(!LEADS) return; }
  if(!leadGrp){ leadGrp=viewDots(); map.on('moveend',()=>{ if(U.ui.leads&&LEADS) leadSync(); }); }
  leadsMore(); leadSync(); leadGrp.grp.addTo(map); }
function leadSync(){ const b=map.getBounds().pad(0.25), s=b.getSouth(), n=b.getNorth(), w=b.getWest(), e=b.getEast();
  viewSync(leadGrp,map.getZoom()<LEADZ?[]:leadRows().filter(p=>p[0]>=s&&p[0]<=n&&p[1]>=w&&p[1]<=e),p=>{
    const m=L.circleMarker([p[0],p[1]],{pane:'lines',renderer:lineCanvas,radius:5.5,color:p[4]?'#0d3b36':'#3a2f00',weight:1.3,fillColor:p[4]?'#3cc8b4':'#ffd500',fillOpacity:0.95,bubblingMouseEvents:false});
    m.on('click',e=>{ if(adding||pickingHome||asking){ onMapClick(e); return; } leadPopup(p); }); return m; }); }
/* ---------- two more lead layers, drawn only where the map is looking ----------
   data/vanished.json (tools/vanished.py): places the federal names file of 2021 marks "(historical)".
       p = [lat,lon,type,name,GNIS id,state]
   data/mines.json (tools/mines.py): past producers and prospects from the USGS Mineral Resources Data System.
       p = [lat,lon,type,name,MRDS id,commodity,'P' past producer|'S' prospect,last year worked or 0,state]
   Both are fetched only when switched on. There are thousands of points, so they are indexed on a grid and only the
   ones in view are drawn, from zoom XL[k].z. */
const XL={
  vanished:{file:'data/vanished/index.json',z:10,fill:'#ff8a3d',ring:'#5a2600',what:'vanished place',
    src:'From the U.S. Board on Geographic Names file of 2021, which marks it "historical": it no longer exists or no longer serves that purpose. Something may still stand. The position can be 100 m or more out.',
    seed:x=>'Lead from the federal place-names file (GNIS '+x[4]+'), which marks it historical. Not checked yet.'},
  mines:{file:'data/mines/index.json',z:9,fill:'#aeb7c2',ring:'#1f2a36',what:'old mine or quarry',
    src:'From the USGS Mineral Resources Data System, last updated in 2011. The position is often only good to a few hundred metres. Old workings can be flooded, fenced or on private land: do not enter shafts or adits.',
    seed:x=>'Lead from the USGS Mineral Resources Data System (record '+x[4]+'). Not checked yet.'} };
Object.keys(XL).forEach(k=>{ XL[k].k=k; XL[k].data=null; XL[k].idx=null; XL[k].got={}; XL[k].layer=null; XL[k].wait=null; });
const xlOn=k=>!!(U.ui.xl&&U.ui.xl[k]);
const xlShow=(k,x)=>k!=='vanished'||x[2]!==1||!!(U.ui.xl&&U.ui.xl.schools);     /* old school sites are two thirds of the file: off unless asked for */
/* ---------- stone walls found on LiDAR (tools/lidar_walls.py finds them, tools/walls.py builds the layer) ----------
   data/walls.json says which 0.05-degree cells hold walls and how many metres of wall each 0.005-degree box has.
   Zoom 9 to 13: the boxes are shaded, darker for more wall, which shows where the old farms were.
   Zoom 14 and in: the walls themselves, one file for each cell in view, fetched when first needed. */
let WALLS=null, wallsWait=null, wallBoxes=null; const wallCells=new Map();
function wallsLoad(){ if(WALLS||wallsWait) return;
  wallsWait=(AT?AT.fetch('data/walls.json'):fetch('data/walls.json'+VQ)).then(r=>{ if(!r.ok) throw new Error('http '+r.status); return r.json(); }).then(j=>{ WALLS=j; drawWalls(); if(!$('#sheet').hidden) buildSheet(); })
    .catch(()=>{ wallsWait=null; if(U.ui.walls) banner('The stone walls could not load. Check your signal and switch them on again.',true,6000); }); }
function drawWalls(){ if(!map) return;
  if(!lineCanvas){ map.createPane('lines').style.zIndex=380; lineCanvas=L.canvas({pane:'lines',tolerance:7}); }
  const on=!!U.ui.walls; if(on&&!WALLS){ wallsLoad(); return; } if(!WALLS) return;
  if(!map._wlOn){ map._wlOn=true; map.on('moveend',drawWalls); }
  const z=map.getZoom(), fine=on&&z>=14, coarse=on&&z>=9&&z<14;
  if(coarse&&!wallBoxes){ wallBoxes=L.layerGroup(); WALLS.d.forEach(b=>{ const la=b[0]*0.005, lo=b[1]*0.005;
      L.rectangle([[la,lo],[la+0.005,lo+0.005]],{pane:'lines',renderer:lineCanvas,stroke:false,fillColor:'#c2410c',fillOpacity:Math.min(0.6,0.14+b[2]/2200),interactive:false,wallBox:true}).addTo(wallBoxes); }); }
  if(wallBoxes){ if(coarse&&!map.hasLayer(wallBoxes)) wallBoxes.addTo(map); else if(!coarse&&map.hasLayer(wallBoxes)) map.removeLayer(wallBoxes); }
  const want=new Set();
  if(fine){ const b=map.getBounds().pad(0.2); for(let i=Math.floor(b.getSouth()/0.05);i<=Math.floor(b.getNorth()/0.05);i++) for(let j=Math.floor(b.getWest()/0.05);j<=Math.floor(b.getEast()/0.05);j++){ const k=i+'_'+j; if(WALLS.c[k]) want.add(k); } }
  wallCells.forEach((c,k)=>{ if(c.layer&&!want.has(k)&&map.hasLayer(c.layer)) map.removeLayer(c.layer); });
  want.forEach(k=>{ let c=wallCells.get(k);
    if(!c){ c={layer:null}; wallCells.set(k,c); const p='data/walls/'+k+'.json';
      (AT?AT.fetch(p):fetch(p+VQ)).then(r=>{ if(!r.ok) throw new Error('http '+r.status); return r.json(); })
        .then(j=>{ const o=j.o; c.layer=L.polyline(j.w.map(w=>[[(o[0]+w[0])/1e5,(o[1]+w[1])/1e5],[(o[0]+w[2])/1e5,(o[1]+w[3])/1e5]]),{pane:'lines',renderer:lineCanvas,color:'#ff7a1a',weight:2.2,opacity:0.95,interactive:false,wallCell:k}); drawWalls(); })
        .catch(()=>{ wallCells.delete(k); });
      return; }
    if(c.layer&&!map.hasLayer(c.layer)) c.layer.addTo(map); }); }
/* These two layers hold tens of thousands of points, so they come in pieces: a small index (the kinds of point, and for each
   state how many, a stamp of its file and the box it lies in), then one file per state, fetched the first time the map is
   zoomed in over that state or the reader stands in it (xlNeed). A state's file is named with its stamp, so a copy kept on
   the phone is never a stale one. X.idx sorts the points that have arrived into squares a twentieth of a degree across. */
function xlLoad(k,quiet){ const X=XL[k]; if(X.data||X.wait) return;
  X.wait=(AT?AT.fetch(X.file):fetch(X.file+VQ)).then(r=>{ if(!r.ok) throw new Error('http '+r.status); return r.json(); })
    .then(j=>{ X.data=j; X.idx={}; X.got={}; if(Array.isArray(j.p)) xlAdd(X,j.p); drawXL(k); if(!$('#sheet').hidden&&sheetMode==='map') buildSheet(); nmLoaded(); })
    .catch(()=>{ X.wait=null; if(!quiet||xlOn(k)) banner('That layer could not load. Check your signal and switch it on again.',true,6000); }); }
function xlAdd(X,rows){ rows.forEach(x=>{ const g=Math.floor(x[0]*20)+','+Math.floor(x[1]*20); (X.idx[g]=X.idx[g]||[]).push(x); }); }
/* fetch every state whose box touches this one (south, west, north, east) and has not come yet; a failure is tried again after half a minute */
function xlNeed(k,S,W,N,E){ const X=XL[k], st=X.data&&X.data.s; if(!st) return;
  Object.keys(st).forEach(key=>{ const o=st[key], b=o&&o.b, g=X.got[key]; if(!b||!o.h||g===true||g==='wait'||(g&&Date.now()-g.t<30000)) return;
    if(b[0]>N||b[2]<S||b[1]>E||b[3]<W) return;
    X.got[key]='wait'; const p='data/'+k+'/'+key+'-'+o.h+'.json';
    (AT?AT.fetch(p):fetch(p+'?v='+o.h)).then(r=>{ if(!r.ok) throw new Error('http '+r.status); return r.json(); })
      .then(j=>{ X.got[key]=true; xlAdd(X,j.p||[]); drawXL(k); nmLoaded(); })
      .catch(()=>{ X.got[key]={t:Date.now()}; if(xlOn(k)) banner('Part of that layer could not load here. Check your signal.',true,5000); }); }); }
function xlInView(k,b){ const X=XL[k], out=[]; if(!X.idx) return out;
  for(let i=Math.floor(b.getSouth()*20);i<=Math.floor(b.getNorth()*20);i++) for(let j=Math.floor(b.getWest()*20);j<=Math.floor(b.getEast()*20);j++) (X.idx[i+','+j]||[]).forEach(x=>{ if(xlShow(k,x)&&b.contains([x[0],x[1]])) out.push(x); });
  return out; }
function drawXL(k){ const X=XL[k]; if(!map) return;
  const off=()=>{ if(X.layer){ map.removeLayer(X.layer.grp); X.layer=null; } };
  if(!xlOn(k)){ off(); return; }
  if(!X.data){ off(); xlLoad(k); return; }
  if(!map._xlOn){ map._xlOn=true; map.on('moveend',()=>Object.keys(XL).forEach(drawXL)); }
  if(map.getZoom()<X.z){ off(); return; }
  { const b=map.getBounds().pad(0.1); xlNeed(k,b.getSouth(),b.getWest(),b.getNorth(),b.getEast()); }      /* the states in view, if they have not come yet */
  if(!lineCanvas){ map.createPane('lines').style.zIndex=380; lineCanvas=L.canvas({pane:'lines',tolerance:7}); }
  if(!X.layer){ X.layer=viewDots(); X.layer.grp.addTo(map); }                /* a dot already drawn stays; only what came into view is made */
  viewSync(X.layer,xlInView(k,map.getBounds().pad(0.1)).slice(0,1500),x=>{
    const m=L.circleMarker([x[0],x[1]],{pane:'lines',renderer:lineCanvas,radius:5,color:X.ring,weight:1.3,fillColor:X.fill,fillOpacity:0.95,bubblingMouseEvents:false});
    m.on('click',e=>{ if(adding||pickingHome||asking){ onMapClick(e); return; } xlPopup(k,x); }); return m; }); }
function xlLine(k,x){ const t=XL[k].data.t[x[2]];
  return k==='mines'?t+(x[5]?' · '+x[5].toLowerCase():'')+' · '+(x[6]==='S'?'prospect':'past producer')+(x[7]?', last worked '+x[7]:''):t; }
function xlPopup(k,x){ const X=XL[k], pt={lat:x[0],lon:x[1]}, name=x[3]||X.data.t[x[2]];
  const box=el('div',{class:'ctx'},el('b',{text:name}),el('span',{style:'color:#5b6660',text:xlLine(k,x)+' · unchecked lead'}),el('span',{style:'color:#5b6660',text:X.src}));
  if(k==='mines') box.append(ext('https://mrdata.usgs.gov/mrds/show-mrds.php?dep_id='+x[4],'USGS record','btn sm'));
  box.append(el('button',{class:'btn sm',type:'button',onclick:()=>{ map.closePopup(); openForm({lat:x[0],lon:x[1],name:name,story:X.seed(x)}); }},'+ Add to my places'));
  box.append(el('button',{class:'btn sm',type:'button',onclick:()=>whoPopup(pt)},'Whose land is it?'));
  scoutLinks(pt).slice(0,2).forEach(l=>box.append(ext(l[1],l[0],'btn sm')));
  L.popup({maxWidth:270}).setLatLng([x[0],x[1]]).setContent(box).openOn(map); }
function xlSet(k,v){ U.ui.xl=U.ui.xl||{}; U.ui.xl[k]=v; save(); if(k==='schools') drawXL('vanished'); else { drawXL(k); if(v&&map.getZoom()<XL[k].z) banner('Zoom in to see them: they show from about town level.',false,5000); } }
/* ---------- historic pockets: old town centres, and other places where markers and Register listings bunch together ----------
   data/pockets.json (tools/pockets.py) holds every state's pockets and is small:
     k = [lat,lon,radius m,markers,listed places,districts,contributing buildings,name,state,marker spots,type,score,era,settlement kind]
         type 'c' = old town centre, named after its settlement; 'p' = any other pocket. Rows come sorted: centres first, best score first.
     s = per state: counts, and h, a stamp of that state's detail file
   data/pock/<state>.json holds one state's single things and is fetched only when the map is zoomed in there:
     m = markers [lat,lon,HMdb number,title], r = listings [lat,lon,NRIS ref,name,kind,contributing buildings (-1 unknown),year],
     d = district outlines [ref,[[lat,lon]...]]
   A pocket is drawn as one disc; the single markers and listings appear only from zoom 15, and only those in view. */
let POCK=null, pockGrp=null, pockItems=null, pockLab=null, pockMid=null, pockWait=null, pockIdx={}, pockDet={}, pockList={mode:'rich',n:8};
const PKK={b:'building',d:'historic district',s:'site',t:'structure',o:'object'}, PKS={C:'city',t:'town',v:'village',h:'hamlet'};
const pockC=k=>k[10]==='c';
const pockColor=k=>{ const s=k[11]; return !pockC(k)?'#8d86ad':s>=40?'#3b1a9e':s>=25?'#5b3fd6':s>=14?'#7a62e8':'#9d8bf2'; };
function pockPx(k,z){ const real=k[2]/(156543.03392*Math.cos(rad(k[0]))/Math.pow(2,z)); return Math.max(real,pockC(k)?5+Math.min(8,k[11]/6):3.5+Math.min(4,k[11]/9)); }
/* Zoomed out, only the richest show, or a state full of old villages is one purple smear: each disc has a zoom it appears from. */
const POCKZ=8;      /* no disc wider than the 20-mile scale: out there the grouped pins already say where the places are */
const pockFrom=k=>{ const s=k[11]; return pockC(k)?(s>=30?0:s>=22?8:s>=14?9:s>=8?10:11):(s>=25?9:s>=15?10:11); };
/* The discs on the map are only those in or near the view, from the zoom each appears at (viewDots, above, says why: there
   are some four thousand). Plain pockets lie underneath and the richest town centres on top: the rows come best first, so
   they are gone through backwards, and the order is put right whenever a disc joins ones already drawn.
   Close in, a disc would tint the whole screen: its fill fades and the ring stays. */
function pockZoom(){ if(!U.ui.pockets||!pockGrp||!POCK) return; const z=map.getZoom(), f=z>=16?0.03:z>=14?0.12:0.3;
  const b=map.getBounds().pad(0.3), S=b.getSouth(), N=b.getNorth(), W=b.getWest(), E=b.getEast(), only=!U.ui.pockO, want=[];
  if(z>=POCKZ) pockNeed(S,W,N,E);
  for(let i=POCK.k.length-1;i>=0;i--){ const k=POCK.k[i], r=k[2]/70000;                      /* its radius in degrees, generously */
    if(z<POCKZ||k.thin||z<pockFrom(k)||k[0]+r<S||k[0]-r>N||k[1]+r<W||k[1]-r>E||(only&&!pockC(k))) continue; want.push(k); }
  const had=pockGrp.on.size, added=viewSync(pockGrp,want,k=>{ const tc=pockC(k), c=pockColor(k); k.px=k.f=null;
    const m=L.circleMarker([k[0],k[1]],{pane:'lines',renderer:lineCanvas,radius:pockPx(k,z),color:tc?c:'#6d6790',weight:tc?2:1.2,dashArray:tc?null:'3 4',opacity:0.95,fillColor:c,fillOpacity:tc?0.3:0.12,bubblingMouseEvents:false});
    m.on('click',e=>{ if(adding||pickingHome||asking){ onMapClick(e); return; }
      /* a big disc covers half the screen: only a tap near its middle (the dot) opens its box, so a tap on the park lake inside it does not */
      const px=pockPx(k,map.getZoom()); if(px>32&&e.latlng&&map.latLngToContainerPoint([k[0],k[1]]).distanceTo(map.latLngToContainerPoint(e.latlng))>Math.max(26,px*0.3)) return;
      pockPopup(k,L.latLng(k[0],k[1])); }); return m; });
  /* a dot at the middle of each big disc: what to tap */
  if(pockMid){ map.removeLayer(pockMid); pockMid=null; }
  { const g=L.layerGroup(); want.forEach(k=>{ if(pockPx(k,z)<=32) return; const d=L.circleMarker([k[0],k[1]],{pane:'lines',renderer:lineCanvas,radius:5,color:'#ffffff',weight:1.5,fillColor:pockColor(k),fillOpacity:0.99,bubblingMouseEvents:false});
      d.on('click',e=>{ if(adding||pickingHome||asking){ onMapClick(e); return; } pockPopup(k,L.latLng(k[0],k[1])); }); d.addTo(g); }); if(g.getLayers().length) pockMid=g.addTo(map); }
  if(added&&had) want.forEach(k=>pockGrp.mk.get(k).bringToFront());
  want.forEach(k=>{ const c=pockGrp.mk.get(k), px=Math.round(pockPx(k,z)*2)/2; if(k.px!==px){ k.px=px; c.setRadius(px); } const ff=pockC(k)?f:f*0.4; if(k.f!==ff){ k.f=ff; c.setStyle({fillOpacity:ff}); } }); }
function pockLoad(quiet){ if(POCK||pockWait) return;
  pockWait=(AT?AT.fetch('data/pock/index.json'):fetch('data/pock/index.json'+VQ)).then(r=>{ if(!r.ok) throw new Error('http '+r.status); return r.json(); })
    .then(j=>{ POCK={s:j.s||{},k:[],got:{}}; drawPockets(); if(!$('#sheet').hidden&&sheetMode==='map') buildSheet(); nmLoaded(); })
    .catch(()=>{ pockWait=null; if(!quiet||U.ui.pockets) banner('Historic pockets could not load. Check your signal and turn them on again.',true,6000); }); }
/* The discs come one state at a time (tools/make.py): POCK.s lists each state with the box b its pockets lie in and the
   stamp kh of its file. pockNeed fetches the states a box touches that have not come yet; POCK.k holds what has come,
   town centres first and best score first, as the drawing and the labels expect. Nobody looking at Albany fetches Ohio. */
function pockNeed(S,W,N,E){ if(!POCK) return;
  Object.keys(POCK.s).forEach(key=>{ const o=POCK.s[key], b=o&&o.b, g=POCK.got[key]; if(!b||!o.kh||g===true||g==='wait'||(g&&Date.now()-g.t<30000)) return;
    if(b[0]>N||b[2]<S||b[1]>E||b[3]<W) return;
    POCK.got[key]='wait'; const p='data/pock/'+key+'-k-'+o.kh+'.json';
    (AT?AT.fetch(p):fetch(p+'?v='+o.kh)).then(r=>{ if(!r.ok) throw new Error('http '+r.status); return r.json(); })
      .then(j=>{ POCK.got[key]=true; POCK.k=POCK.k.concat(j.k||[]).sort((x,y)=>(pockC(y)-pockC(x))||(y[11]-x[11])); pockThin(); pockZoom(); pockDetail(); if(!$('#sheet').hidden&&sheetMode==='map') buildSheet(); nmLoaded(); })
      .catch(()=>{ POCK.got[key]={t:Date.now()}; if(U.ui.pockets) banner('Some town centres could not load here. Check your signal.',true,5000); }); }); }
/* In and round a city the small centres crowd the strong one. A town centre scoring under 15 that has a stronger one within
   3 km is left off the map (k.thin); a weak one with nothing near it stays. The list in Map options and the Near tab keep all. */
function pockThin(){ const g={}, C=POCK.k.filter(pockC); C.forEach(k=>{ const c=Math.floor(k[0]*20)+','+Math.floor(k[1]*20); (g[c]=g[c]||[]).push(k); });
  C.forEach(k=>{ k.thin=false; if(k[11]>=15) return; const a=Math.floor(k[0]*20), b=Math.floor(k[1]*20);
    for(let i=a-1;i<=a+1&&!k.thin;i++) for(let j=b-2;j<=b+2&&!k.thin;j++) (g[i+','+j]||[]).forEach(o=>{ if(o!==k&&o[11]>k[11]&&hav(k[0],k[1],o[0],o[1])<1.864) k.thin=true; }); }); }
/* after "also show other pockets" is switched: draw the discs afresh */
function pockReset(){ if(pockGrp){ map.removeLayer(pockGrp.grp); pockGrp=null; } if(POCK) POCK.k.forEach(k=>{ k.f=null; k.px=null; }); drawPockets(); }
function drawPockets(){
  if(!map) return;
  if(!U.ui.pockets){ if(pockGrp) map.removeLayer(pockGrp.grp); [pockItems,pockLab,pockMid].forEach(g=>{ if(g) map.removeLayer(g); }); pockItems=pockLab=pockMid=null; return; }
  if(!POCK){ pockLoad(); return; }
  if(!lineCanvas){ map.createPane('lines').style.zIndex=380; lineCanvas=L.canvas({pane:'lines',tolerance:7}); }
  if(!pockGrp){ pockGrp=viewDots(); if(!map._pockOn){ map._pockOn=true; map.on('moveend',()=>{ pockZoom(); pockDetail(); }); } }
  pockGrp.grp.addTo(map); pockZoom(); pockDetail(); }
/* names on the best town centres in view, so a disc can be told without tapping it. Best score first; a name that
   would sit on top of one already placed is left out. */
function pockLabels(){
  if(pockLab){ map.removeLayer(pockLab); pockLab=null; }
  const z=map.getZoom(); if(!U.ui.pockets||!POCK||z<POCKZ) return;      /* from the zoom the discs start at (it was zoom 10): zoomed out the street map's own town names are too small to read, and a name is how the right town is found (the owner, November 22, 2026) */
  const b=map.getBounds(), cap=z>=13?22:z>=10?14:18, g=L.layerGroup(), put=[]; let n=0;
  for(const k of POCK.k){ if(!pockC(k)||n>=cap) break; if(k.thin||z<pockFrom(k)||!b.contains([k[0],k[1]])) continue;
    const pt=map.latLngToContainerPoint([k[0],k[1]]), r=Math.round(pockPx(k,z)+2), w=k[7].length*6.6+8, box=[pt.x-w/2,pt.y-r-15,pt.x+w/2,pt.y-r];
    if(put.some(q=>box[0]<q[2]&&box[2]>q[0]&&box[1]<q[3]&&box[3]>q[1])) continue; put.push(box); n++;
    L.marker([k[0],k[1]],{interactive:false,keyboard:false,icon:L.divIcon({className:'pocklab',iconSize:[0,0],html:el('span',{style:'transform:translate(-50%,calc(-100% - '+r+'px))',text:k[7]})})}).addTo(g); }
  pockLab=g.addTo(map); }
/* one state's markers, listings and district outlines: fetched the first time the map is zoomed in there */
function pockFetch(key){ const d=pockDet[key]; if(d&&(d==='wait'||d.m||Date.now()-d.t<30000)) return; pockDet[key]='wait';
  const p='data/pock/'+key+'.json', h=((POCK.s||{})[key]||{}).h;
  (AT?AT.fetch(p):fetch(p+(h?'?v='+h:VQ))).then(r=>{ if(!r.ok) throw new Error('http '+r.status); return r.json(); })
    .then(j=>{ pockDet[key]=j; const put=(a,t)=>(a||[]).forEach(x=>{ const g=Math.floor(x[0]*50)+','+Math.floor(x[1]*50); (pockIdx[g]=pockIdx[g]||[]).push([t,x]); });
      put(j.m,'m'); put(j.r,'r'); put((j.d||[]).map(d=>[d[1][0][0],d[1][0][1],d]),'d'); pockDetail(); })
    .catch(()=>{ pockDet[key]={t:Date.now()}; banner('The single markers and listings here could not load. Check your signal.',true,5000); }); }
/* the single markers and listings: only when zoomed in, only what is in view */
function pockDetail(){
  pockLabels();
  if(pockItems){ map.removeLayer(pockItems); pockItems=null; }
  if(!U.ui.pockets||!POCK||map.getZoom()<15||(!U.ui.pockM&&U.ui.pockR===false)) return;
  const c=map.getCenter(), need={}; POCK.k.forEach(k=>{ if(!need[k[8]]&&Math.abs(k[0]-c.lat)<0.25&&Math.abs(k[1]-c.lng)<0.35) need[k[8]]=1; }); Object.keys(need).forEach(pockFetch);
  const b=map.getBounds().pad(0.15), g=L.layerGroup(); let n=0;
  for(let i=Math.floor(b.getSouth()*50);i<=Math.floor(b.getNorth()*50);i++) for(let j=Math.floor(b.getWest()*50);j<=Math.floor(b.getEast()*50);j++) (pockIdx[i+','+j]||[]).forEach(q=>{ const x=q[1];
    if(q[0]==='d'||(q[0]==='m'?!U.ui.pockM:U.ui.pockR===false)) return;      /* district outlines are no longer drawn: a box round half a city told nobody anything */
    if(n>700||!b.contains([x[0],x[1]])) return; n++;
    const mk=q[0]==='m'?L.circleMarker([x[0],x[1]],{pane:'lines',renderer:lineCanvas,radius:4.5,color:'#ffffff',weight:1.5,fillColor:'#5b3fd6',fillOpacity:1,bubblingMouseEvents:false})
                       :L.circleMarker([x[0],x[1]],{pane:'lines',renderer:lineCanvas,radius:5.5,color:'#3b1a9e',weight:2,fillColor:'#ffffff',fillOpacity:1,bubblingMouseEvents:false});
    mk.on('click',e=>{ if(adding||pickingHome||asking){ onMapClick(e); return; } pockItemPopup(q[0],x); }); mk.addTo(g); });
  pockItems=g.addTo(map); }
function pockCounts(k){ const a=[]; if(k[3]) a.push(k[3]+' historical marker'+(k[3]>1?'s':'')+(k[9]&&k[9]*1.5<k[3]?' at '+k[9]+' spot'+(k[9]>1?'s':''):'')); if(k[4]) a.push(k[4]+' listed place'+(k[4]>1?'s':'')); if(k[5]) a.push(k[5]+' historic district'+(k[5]>1?'s':'')+(k[6]?' ('+k[6]+' buildings)':'')); return a.join(' · '); }
function pockPopup(k,latlng){
  const tc=pockC(k);
  /* a small box: the name, what it is and its score, the counts, one button (it used to fill a phone's screen) */
  const box=el('div',{class:'ctx'},el('b',{text:k[7]}),
    el('span',{style:'color:#5b6660',text:(tc?'Old town centre'+(PKS[k[13]]?' ('+PKS[k[13]]+')':''):'Pocket of markers and listings')+' · score '+Math.round(k[11])}),
    el('span',{style:'color:#5b6660',text:pockCounts(k)}),
    el('button',{class:'btn sm',type:'button',onclick:()=>{ map.closePopup(); map.setView([k[0],k[1]],Math.max(map.getZoom(),16)); }},'Zoom in'));
  L.popup({maxWidth:250}).setLatLng(latlng||[k[0],k[1]]).setContent(box).openOn(map); }
function pockItemPopup(t,x){
  const pt={lat:x[0],lon:x[1]}, name=x[3]||'Unnamed';
  const box=el('div',{class:'ctx'},el('b',{text:name}));
  if(t==='m'){ box.append(el('span',{style:'color:#5b6660',text:'Historical marker · HMdb.org'}), ext('https://www.hmdb.org/m.asp?m='+x[2],'Read the marker on HMdb.org','btn sm')); }
  else { box.append(el('span',{style:'color:#5b6660',text:'National Register of Historic Places: '+(PKK[x[4]]||'listing')+(x[6]?', listed '+x[6]:'')+(x[5]>1?', '+x[5]+' contributing buildings':'')+'. Position approximate; it may be gone.'}), ext('https://npgallery.nps.gov/AssetDetail/NRIS/'+x[2],'National Park Service record','btn sm')); }
  box.append(el('button',{class:'btn sm',type:'button',onclick:()=>{ map.closePopup(); openForm({lat:x[0],lon:x[1],name:name,story:(t==='m'?'From a historical marker listed on HMdb.org (marker '+x[2]+').':'From a National Register listing (reference '+x[2]+').')+' Not checked yet.'}); }},'+ Add to my places'));
  box.append(el('button',{class:'btn sm',type:'button',onclick:()=>whoPopup(pt)},'Whose land is it?'));
  L.popup({maxWidth:270}).setLatLng([x[0],x[1]]).setContent(box).openOn(map); }
/* for the map options sheet: old town centres within reach of the start place, richest or nearest first, or the other pockets.
   "Nearest" leaves out the thinnest centres when there are plenty, so the list is not all crossroads with one plaque. */
function pockNear(mode){ if(!POCK) return []; let H=homeObj(); if(!homePicked()&&map){ const c=map.getCenter(); H={lat:c.lat,lon:c.lng}; }
  pockNeed(H.lat-0.6,H.lon-0.85,H.lat+0.6,H.lon+0.85);      /* the states within 40 miles; the sheet is built again when one comes */
  let a=POCK.k.filter(k=>(mode==='other')!==pockC(k)).map(k=>({k:k,mi:hav(H.lat,H.lon,k[0],k[1])})).filter(o=>o.mi<=40);
  if(mode==='near'){ const solid=a.filter(o=>o.k[11]>=10); if(solid.length>=8) a=solid; return a.sort((x,y)=>x.mi-y.mi); }
  return a.sort((x,y)=>y.k[11]-x.k[11]); }
function pockLine(o){ const k=o.k, a=[Math.round(o.mi)+' mi'], reg=k[4]+k[6]; if(reg) a.push(reg+' on the Register'); else if(k[5]) a.push('historic district'); if(k[9]) a.push(k[9]+' plaque spot'+(k[9]>1?'s':'')); if(k[12]) a.push(k[12]); return a.join(' · '); }
function leadPopup(p){
  const pt={lat:p[0],lon:p[1]}, kind=LEADS.t[p[2]];
  const box=el('div',{class:'ctx'},el('b',{text:p[3]||kind}),el('span',{style:'color:#5b6660',text:(p[3]?kind+' · ':'')+'unchecked lead from OpenStreetMap'}));
  if(p[4]) box.append(el('span',{style:'color:#5b6660',text:'From the category you switched on in Settings: Native American sites and reservation land. Many such places are sacred, protected by law or closed. Go only where whoever looks after it invites visitors, and leave everything as it lies.'}));
  box.append(el('button',{class:'btn sm',type:'button',onclick:()=>{ map.closePopup(); openForm({lat:p[0],lon:p[1],name:p[3]||'',story:'Lead from OpenStreetMap ('+kind.toLowerCase()+'). Not checked yet.'}); }},'+ Add to my places'));
  box.append(el('button',{class:'btn sm',type:'button',onclick:()=>whoPopup(pt)},'Whose land is it?'));
  scoutLinks(pt).slice(0,2).forEach(l=>box.append(ext(l[1],l[0],'btn sm')));
  L.popup({maxWidth:260}).setLatLng([p[0],p[1]]).setContent(box).openOn(map); }
const ptq=(u,p,fields)=>fetch(u+'?geometry='+p.lon.toFixed(6)+','+p.lat.toFixed(6)+'&geometryType=esriGeometryPoint&inSR=4326&spatialRel=esriSpatialRelIntersects&outFields='+fields+'&returnGeometry=false&f=json').then(r=>r.json());
async function lookup(p,box){
  box.textContent=''; box.append(el('p',{class:'who-wait',text:'Looking up land records…'}));
  const reg=regionOf(p.lat,p.lon); let failed=0;
  const res=await Promise.all([
    ptq(PADU,p,'Unit_Nm,MngNm_Desc,Pub_Access,DesTp_Desc').catch(()=>{ failed++; return null; }),
    reg==='ny'?ptq(PARU,p,'COUNTY_NAME,MUNI_NAME,PARCEL_ADDR,PRINT_KEY,PROP_CLASS,ACRES,PRIMARY_OWNER,NYS_NAME').catch(()=>{ failed++; return null; }):
    reg==='ma'?ptq(MAPU,p,'OWNER1,SITE_ADDR,CITY,USE_CODE,USE_DESC,LOT_SIZE,LOT_UNITS,PROP_ID,FY').catch(()=>{ failed++; return null; }):Promise.resolve(null)]);
  const pad=res[0], par=res[1]; box.textContent='';
  if(failed&&!pad&&!par){ box.append(el('p',{class:'who-wait',text:navigator.onLine===false?'No signal, so the records could not be reached.':'The records service could not be reached from here. The lookup works when the Atlas is opened as a file or from your own web address.'})); return; }
  if(pad&&pad.features&&pad.features.length){
    pad.features.map(f=>f.attributes).sort((a,b)=>(PADRANK[a.Pub_Access]||0)-(PADRANK[b.Pub_Access]||0)).slice(0,2).forEach(a=>{ const c=PADC[a.Pub_Access]||PADC.UK;
      box.append(el('div',{class:'who-row'},el('span',{class:'sw',style:'--c:'+c[1]}),el('div',null,el('b',{text:a.Unit_Nm||'Protected land'}),el('small',{text:[a.MngNm_Desc,a.DesTp_Desc].filter(Boolean).join(' · ')}),el('small',{text:c[0]})))); });
  } else if(pad&&pad.features) box.append(el('p',{class:'who-none',text:'Not on mapped public or protected land. Treat it as private until you know otherwise.'}));
  if(reg==='ma'&&par&&par.features&&par.features.length){ const a=par.features[0].attributes, uc=String(a.USE_CODE||''), more=par.features.length-1;
    const use=a.USE_DESC||MAUSE[parseInt(uc.charAt(0),10)]||'';
    box.append(el('dl',{class:'kv who-kv'},
      el('dt',{text:'Owner'}),el('dd',{text:(a.OWNER1||'Not given')+(more>0?' (and '+more+' more record'+(more>1?'s':'')+' on this lot)':'')}),
      el('dt',{text:'Parcel'}),el('dd',{text:[a.SITE_ADDR,a.CITY].filter(Boolean).join(', ')||'No address'}),
      use?el('dt',{text:'Use'}):null,use?el('dd',{text:use+(uc?' ('+uc+')':'')}):null,
      a.LOT_SIZE?el('dt',{text:'Size'}):null,a.LOT_SIZE?el('dd',{text:(+a.LOT_SIZE).toLocaleString([],{hour12:H12()})+(a.LOT_UNITS==='S'?' sq ft':' acres')}):null,
      a.PROP_ID?el('dt',{text:'Parcel ID'}):null,a.PROP_ID?el('dd',{class:'mono',text:a.PROP_ID}):null));
    box.append(ext('https://www.google.com/search?q='+encodeURIComponent((a.CITY||'')+' MA assessor property record '+(a.SITE_ADDR||a.PROP_ID||'')),'Find the assessor record','btn sm'));
    box.append(el('small',{class:'snote',text:'From the MassGIS parcel file'+(a.FY?', fiscal year '+a.FY:'')+', which can lag a sale. The town assessor has the mailing address for a permission letter.'}));
  } else if(reg==='ma'&&par&&par.features){ box.append(el('p',{class:'who-none',text:'No parcel record at this spot. It may be a road, water, or a gap in the state file; ask the town assessor.'}));
  } else if(par&&par.features&&par.features.length){ const a=par.features[0].attributes, pc=parseInt(a.PROP_CLASS,10)||0;
    const use=PCX[pc]||PCLASS[Math.floor(pc/100)]||'';
    box.append(el('dl',{class:'kv who-kv'},
      el('dt',{text:'Owner'}),el('dd',{text:a.NYS_NAME||a.PRIMARY_OWNER||'Not given'}),
      el('dt',{text:'Parcel'}),el('dd',{text:[a.PARCEL_ADDR,a.MUNI_NAME].filter(Boolean).join(', ')||'No address'}),
      use?el('dt',{text:'Use'}):null,use?el('dd',{text:use+(a.PROP_CLASS?' ('+a.PROP_CLASS+')':'')}):null,
      a.ACRES?el('dt',{text:'Size'}):null,a.ACRES?el('dd',{text:(+a.ACRES).toFixed(a.ACRES<10?1:0)+' acres'}):null,
      a.PRINT_KEY?el('dt',{text:'Tax ID'}):null,a.PRINT_KEY?el('dd',{class:'mono',text:a.PRINT_KEY}):null));
    box.append(ext('https://www.google.com/search?q='+encodeURIComponent((a.COUNTY_NAME||'')+' County NY real property parcel search '+(a.PRINT_KEY||'')),'Find the county record','btn sm'));
    box.append(el('small',{class:'snote',text:'From the state parcel file, which can lag a sale. The county record has the mailing address for a permission letter.'}));
  } else if(par&&par.features){
    let cn=''; try{ const c=await ptq(CNTU,p,'NAME'); cn=c.features&&c.features[0]?c.features[0].attributes.NAME:''; }catch(e){}
    box.append(el('p',{class:'who-none',text:(cn?cn+' County does':'This county does')+' not share parcel owners in the state file. Use the county\'s own parcel viewer or the town assessor.'}));
    if(cn) box.append(ext('https://www.google.com/search?q='+encodeURIComponent(cn+' County NY parcel viewer real property'),'Find '+cn+' County\'s parcel viewer','btn sm'));
  } else if(reg!=='ny'&&reg!=='ma') box.append(el('p',{class:'who-none',text:'Owner lookup covers New York and Massachusetts. For '+STATE[reg]+', ask the town assessor or use the state parcel viewer.'}));
  else if(failed) box.append(el('p',{class:'who-none',text:'The parcel service did not answer. Try again in a moment.'}));
}
function whoPopup(p){ const box=el('div',{class:'ctx who'}); const pop=L.popup({maxWidth:280,minWidth:220}).setLatLng([p.lat,p.lon]).setContent(box).openOn(map);
  lookup(p,box).then(()=>{ try{ pop.update(); }catch(e){} }); }
/* permission letter, after the sample in the field manual */
function letterText(s){ const me=U.me||{}, f=(k,d)=>(me[k]&&me[k].trim())||d;
  return 'Dear [owner\'s name],\n\nMy name is '+f('name','[your name]')+'. I produce '+f('chan','[channel name]')+', a history-focused YouTube channel ('+f('link','[channel link]')+') documenting lost buildings and old industries. I am researching '+s.name+(s.town?' in '+s.town:'')+', which I understand you own. I would like permission for a one-time daytime visit of about two hours with one partner to photograph and film what remains.\n\n'+
    'We will: not disclose the address or how to reach it; not move, take or alter anything; stay out of any areas you specify; carry signed proof of permission; and sign a release holding you harmless. I am happy to share all photos for your use, credit you or keep you anonymous, and let you review the video before release.\n\n'+
    'I can be reached at '+f('contact','[phone or email]')+'. Thank you for considering it.\n\n'+f('name','[your name]'); }
function letterBox(s){
  if(!U.me) U.me={};
  const out=el('textarea',{id:'letter-out',style:'min-height:230px;margin-top:8px','aria-label':'Permission request'}); out.value=letterText(s);
  const inp=(k,label,ph)=>{ const i=el('input',{type:'text',placeholder:ph}); i.value=U.me[k]||''; i.addEventListener('input',()=>{ U.me[k]=i.value; save(); out.value=letterText(s); }); return el('label',{class:'field',style:'margin-top:6px'},el('span',{text:label}),i); };
  const cp=el('button',{class:'btn sm',type:'button'},'Copy letter'); cp.addEventListener('click',()=>copy(out.value,cp));
  return el('details',{class:'letter'},el('summary',{text:'Write a permission request'}),
    el('p',{class:'snote',text:'Your details are saved in this browser and reused on every place. Edit the letter freely before copying.'}),
    inp('name','Your name','Name'),inp('chan','Channel name','Channel'),inp('link','Channel link','https://youtube.com/@…'),inp('contact','Phone or email','How the owner can reach you'),out,
    el('div',{class:'row',style:'margin-top:8px'},cp,el('button',{class:'btn sm',type:'button',onclick:()=>{ U.status[s.id]='asked'; save(); syncMarkers(); const m=document.getElementById('my-status'); if(m) m.value='asked'; banner('Marked as "Asked the owner".',false,3000); }},'Mark as asked')),
    el('p',{class:'snote',text:'Rural owners often do not use email: post it, then follow up once by mail and once by phone. Carry the signed reply and the owner\'s number on site. From your field manual; not legal advice.'})); }

/* where am I: fixes are filtered so the dot glides instead of jumping, and it stays put (grey) when tracking is off */
let geo={id:null,dot:null,ll:null,first:true,f:null,anim:0,shown:null,live:false}, dragging=false;
const saveNow=()=>{ try{ localStorage.setItem(LS,JSON.stringify(U)); }catch(e){ storeOK=false; } };
let lastSlow=0; const saveSlow=()=>{ if(Date.now()-lastSlow>8000){ lastSlow=Date.now(); saveNow(); } };
function dotIcon(live){ return L.divIcon({className:'gpsdot'+(live?'':' stale'),html:'',iconSize:[18,18],iconAnchor:[9,9]}); }
function placeDot(p,live){ if(!map) return;
  if(!geo.dot){ geo.dot=L.marker(p,{icon:dotIcon(live),interactive:false,keyboard:false,zIndexOffset:900}).addTo(map); geo.shown=p.slice(); geo.live=live; return; }
  if(geo.live!==live){ geo.dot.setIcon(dotIcon(live)); geo.live=live; }
  cancelAnimationFrame(geo.anim); const from=geo.shown||p, t0=performance.now();
  if(document.hidden||hav(from[0],from[1],p[0],p[1])>0.25){ geo.shown=p.slice(); geo.dot.setLatLng(p); return; }
  const step=now=>{ const k=Math.min(1,(now-t0)/700), e=k*(2-k), q=[from[0]+(p[0]-from[0])*e,from[1]+(p[1]-from[1])*e]; geo.shown=q; geo.dot.setLatLng(q); if(k<1) geo.anim=requestAnimationFrame(step); };
  geo.anim=requestAnimationFrame(step); }
/* one-number Kalman filter: trusts a fix by its stated accuracy, and loosens up when you are really moving */
function gpsFilter(c,t){
  const acc=Math.max(3,c.accuracy||50), f=geo.f;
  if(!f){ geo.f={lat:c.latitude,lon:c.longitude,v:acc*acc,t:t,bad:0}; return [c.latitude,c.longitude]; }
  const dts=Math.max(0,Math.min(60,(t-f.t)/1000));
  if(acc>80&&f.bad<4&&dts<20){ f.bad++; return null; }
  f.bad=0;
  const innov=hav(f.lat,f.lon,c.latitude,c.longitude)*1609.34;
  let q=(c.speed!=null&&c.speed>=0)?c.speed:0; if(innov>2.5*acc) q=Math.max(q,innov/Math.max(1,dts)); q=Math.max(1.5,Math.min(45,q));
  f.v+=dts*q*q; f.t=t;
  const k=f.v/(f.v+acc*acc);
  f.lat+=k*(c.latitude-f.lat); f.lon+=k*(c.longitude-f.lon); f.v=(1-k)*f.v;
  return [f.lat,f.lon]; }
function locate(){
  const mark=on=>{ const b=$('#lb-loc'); if(b) b.setAttribute('aria-pressed',String(on)); if(!on) geo.acc=null; setTimeout(()=>nmDraw(true),0); };
  if(geo.id!==null){
    if(rec){ if(geo.ll){ geo.fol=true; geo.auto=true; map.setView(geo.ll,Math.max(map.getZoom(),16)); } banner('Location stays on while a field log is recording.',false,4000); return; }
    /* the map had let go of the dot (you moved it away): this tap takes hold again. A tap while it is holding switches location off. */
    if(geo.fol===false&&geo.ll){ geo.fol=true; geo.auto=true; map.panTo(geo.ll,{animate:true,duration:0.5}); banner('Back on your dot, and following it. Tap Me once more to switch location off.',false,5000); return; }
    navigator.geolocation.clearWatch(geo.id); geo.id=null; geo.f=null; geo.ll=null; mark(false); nearMoved();
    if(U.last){ placeDot(U.last.ll,false); saveNow(); banner('Location off. The grey dot marks where you last were.',false,4000); }
    return; }
  const fail=msg=>{ if(geo.id!==null){ try{ navigator.geolocation.clearWatch(geo.id); }catch(e){} } geo.id=null; geo.f=null; geo.ll=null; mark(false); nearMoved(); if(geo.dot&&U.last) placeDot(U.last.ll,false); banner(msg,true,12000); if(rec&&!NATIVE) stopLog(); };
  if(!navigator.geolocation){ fail('This browser has no location service.'); return; }
  geo.first=true; geo.f=null; mark(true); banner('Finding you…',false,6000);
  if(!map._folOn){ map._folOn=true; map.on('moveend',()=>{ if(geo.id!==null&&geo.ll&&geo.fol&&!geo.auto&&!map.getBounds().pad(-0.12).contains(geo.ll)) geo.fol=false; geo.auto=false; }); }
  try{ geo.id=navigator.geolocation.watchPosition(g=>{ const c=g.coords, t=g.timestamp||Date.now(), p=gpsFilter(c,t); if(!p) return;
      const was=geo.ll; geo.ll=p; U.last={ll:[+p[0].toFixed(6),+p[1].toFixed(6)],t:Date.now()}; saveSlow(); placeDot(p,true); nearMoved(); recPoint(p,c.accuracy||50,t); geo.acc=c.accuracy||50; nmFix(p,geo.acc);
      /* follow: while the map has hold of the dot (geo.fol) and the dot walks off the screen, bring the map along. The map
         lets go the moment you move it so that the dot is at the edge or off it, by a drag or by tapping a place, and stays
         let go until you tap Me: before November 20, 2026 the next fix dragged the map back while you were looking elsewhere. */
      if(pref('follow')&&geo.fol&&!geo.first&&was&&!dragging){ if(!map.getBounds().pad(-0.12).contains(p)){ geo.auto=true; map.panTo(p,{animate:true,duration:0.6}); } }
      if(geo.first){ geo.first=false; geo.fol=true; geo.auto=true; nearHome(p,true); banner('You are the blue dot, good to about '+accFmt(c.accuracy)+'. Tap Me again to stop.',false,6000); map.setView(p,geo.wide?10:Math.max(map.getZoom(),16)); geo.wide=false; }
    },e=>{ if(e&&e.code===1){ fail(LOCAL||HOSTED?'Location was refused. Allow it for this page in your browser settings, then tap again.':'This online copy is not allowed to use your location. It works when the Atlas is opened as a file or from your own web address.'); return; }
      if(geo.f) return;   /* a passing timeout after we already had a fix: keep listening */
      fail('Could not get a GPS fix. Step into the open and try again.'); },
    {enableHighAccuracy:true,maximumAge:2000,timeout:25000}); }catch(e){ fail('Location is not available here.'); }
}

/* ---------- near me ----------
   The Near tab: everything within a few miles of where you stand, nearest first, each with an arrow and a distance,
   and an alert (a buzz on a phone) when you walk close to one. It reads the places, the OpenStreetMap leads, the
   vanished places, the old mines and quarries, and the old town centres (listed, never buzzed).
   Settings live in U.ui.nm: r = list radius in miles, al = alert distance in metres (0 = off), k = which kinds are in.
   A target is {id,k,la,lo,n,t,o}: id is stable ('p:'+place id, 'l:'+position, 'v:'+GNIS id, 'm:'+USGS id, 'c:'+position).
   In the Android app the page cannot run with the screen off, so while a field log records the list of targets is handed
   to the recorder (FieldLog.targets -> TrackService), which does the buzzing itself. */
const NMK={p:['Places','#d6338a'],l:['Leads','#c9a700'],v:['Vanished','#ff8a3d'],m:['Mines','#8c97a3'],c:['Towns','#6d5bd0']};
const NMR=[[1,'1 mi','1.5 km'],[3,'3 mi','5 km'],[5,'5 mi','8 km'],[10,'10 mi','16 km']], NMA=[[0,'Off','Off'],[50,'160 ft','50 m'],[100,'330 ft','100 m'],[200,'660 ft','200 m']];
const nmLab=(T,v)=>{ const c=T.find(c=>c[0]===v); return c?(KM()?c[2]:c[1]):(T===NMA?v+' m':v+' mi'); };
const NM={org:'me',ver:0,cand:null,in:new Set(),goal:null,hd:null,drawn:0,dt:0,touch:0,push:null,line:null,ring:null,more:false,cmp:false};
function nmSet(){ const o=U.ui.nm||{}; return {r:+o.r||3,al:o.al!=null?+o.al:100,k:Object.assign({p:1,l:1,v:1,m:1,c:1},o.k||{})}; }
function nmSave(ch){ const S=nmSet(); Object.assign(S,ch); U.ui.nm=S; save(); NM.ver++; NM.cand=null; NM.more=false; nmEnsure(true); nmPush(true); nmDraw(true); }
const brg=(a,b,c,d)=>{ const y=Math.sin(rad(d-b))*Math.cos(rad(c)), x=Math.cos(rad(a))*Math.sin(rad(c))-Math.sin(rad(a))*Math.cos(rad(c))*Math.cos(rad(d-b)); return (Math.atan2(y,x)*180/Math.PI+360)%360; };
const dirTxt=b=>['N','NE','E','SE','S','SW','W','NW'][Math.round(b/45)%8];
/* how good a fix is, in the reader's own units (it said metres to a reader who had chosen miles and feet) */
const accFmt=m=>KM()?Math.round(m)+' m':Math.max(5,Math.round(m*3.28084/5)*5)+' ft';
const nmDist=mi=>{ if(KM()){ const m=mi*1609.344; return m<950?Math.max(10,Math.round(m/10)*10)+' m':(m/1000).toFixed(m<20000?1:0)+' km'; } const f=mi*5280; return f<1000?Math.max(10,Math.round(f/10)*10)+' ft':mi.toFixed(mi<1?2:mi<10?1:0)+' mi'; };
/* fetch whichever lead files the chosen kinds need; each tells nmLoaded() when it arrives */
function leadsLoad(quiet){ if(LEADS) return; const n=document.getElementById('d-leads');
  if(n){ try{ LEADS=JSON.parse(n.textContent); }catch(e){ LEADS={t:[],p:[]}; } leadsMore(); return; }
  if(!leadsLoad.wait) leadsLoad.wait=(AT?AT.fetch('data/leads.json'):fetch('data/leads.json'+VQ)).then(r=>r.json()).then(j=>{ LEADS=j; leadsMore(); drawLeads(); nmLoaded(); }).catch(()=>{ leadsLoad.wait=null; if(!quiet||U.ui.leads) banner('Leads could not load. Check your signal and tap Leads again.',true,6000); }); }
function nmEnsure(force){ const t=Date.now(); if(!force&&t-(NM.ens||0)<60000) return; NM.ens=t; const S=nmSet(); if(S.k.l) leadsLoad(true); if(S.k.v) xlLoad('vanished',true); if(S.k.m) xlLoad('mines',true); if(S.k.c) pockLoad(true); }
function nmLoaded(){ NM.ver++; NM.cand=null; clearTimeout(NM.lt); NM.lt=setTimeout(()=>nmPush(false),1200); nmDraw(true); }
/* every target of the chosen kinds within rmi miles of c */
function nmCollect(c,rmi){ const S=nmSet(), out=[], add=(id,k,la,lo,n,t,o)=>{ if(hav(c[0],c[1],la,lo)<=rmi) out.push({id:id,k:k,la:la,lo:lo,n:n,t:t,o:o}); };
  if(S.k.p) sites().forEach(s=>{ if(pref('hideGone')&&nothingToSee(s)) return; const q=pos(s), my=U.status[s.id]; add('p:'+s.id,'p',q.lat,q.lon,s.name,[s.cat==='lidar'?'LiDAR find, not verified':STS[s.st],s.town,my?MY[my]:''].filter(Boolean).join(' · '),s); });
  if(S.k.l&&LEADS) leadRows().forEach(p=>add('l:'+p[0]+','+p[1],'l',p[0],p[1],p[3]||LEADS.t[p[2]],(p[3]?LEADS.t[p[2]]+' · ':'')+'unchecked lead',p));
  [['v','vanished'],['m','mines']].forEach(q=>{ const X=XL[q[1]]; if(!S.k[q[0]]||!X.idx) return; const dla=rmi/69+0.002, dlo=rmi/(69*Math.cos(rad(c[0])))+0.002;
    xlNeed(q[1],c[0]-dla,c[1]-dlo,c[0]+dla,c[1]+dlo);      /* the state the reader stands in, and a neighbour within reach; when it comes, nmLoaded() counts again */
    for(let i=Math.floor((c[0]-dla)*20);i<=Math.floor((c[0]+dla)*20);i++) for(let j=Math.floor((c[1]-dlo)*20);j<=Math.floor((c[1]+dlo)*20);j++) (X.idx[i+','+j]||[]).forEach(x=>{ if(xlShow(q[1],x)) add(q[0]+':'+x[4],q[0],x[0],x[1],x[3]||X.data.t[x[2]],xlLine(q[1],x)+' · unchecked lead',x); }); });
  if(S.k.c&&POCK){ const dla=rmi/69+0.02, dlo=rmi/(69*Math.cos(rad(c[0])))+0.02; pockNeed(c[0]-dla,c[1]-dlo,c[0]+dla,c[1]+dlo); }
  if(S.k.c&&POCK) POCK.k.forEach(k=>{ if(pockC(k)) add('c:'+k[0]+','+k[1],'c',k[0],k[1],k[7],'Old town centre'+(k[12]?' · '+k[12]:''),k); });
  return out; }
/* the candidates round p, kept until you have moved a quarter of a mile or something changed */
function nmCands(p){ const S=nmSet(), c=NM.cand; if(c&&c.v===NM.ver&&c.r===S.r&&hav(p[0],p[1],c.c[0],c.c[1])<0.25) return c.a;
  NM.cand={v:NM.ver,r:S.r,c:p.slice(),a:nmCollect(p,S.r+0.3)}; return NM.cand.a; }
/* where the list is measured from: you, the place you last were, or the middle of the map */
function nmOrigin(){ if(NM.org==='map'&&map){ const c=map.getCenter(); return {p:[c.lat,c.lng],how:'map'}; }
  if(geo.ll) return {p:geo.ll,how:'live'}; if(U.last&&U.last.ll) return {p:U.last.ll,how:'last'}; return null; }
function nmOpen(t){ if(!map) return; const z=Math.max(map.getZoom(),15);
  if(t.k==='p'){ select(t.o,true); return; }
  map.setView([t.la,t.lo],z); if(t.k==='l') leadPopup(t.o); else if(t.k==='c') pockPopup(t.o,L.latLng(t.la,t.lo)); else xlPopup(t.k==='v'?'vanished':'mines',t.o); }
/* "point me there": a big arrow and distance for one target, and a dashed line to it on the map */
function nmGoal(t,fit){ NM.goal=t||null; nmGoalDraw();
  if(t&&fit&&map){ const o=nmOrigin(); if(o&&hav(o.p[0],o.p[1],t.la,t.lo)<60) map.fitBounds(L.latLngBounds([o.p,[t.la,t.lo]]).pad(0.25),{maxZoom:17}); else map.setView([t.la,t.lo],Math.max(map.getZoom(),15)); }
  nmDraw(true); }
function nmGoalDraw(){ if(!map) return; const t=NM.goal, o=t&&nmOrigin();
  const drop=k=>{ if(NM[k]){ map.removeLayer(NM[k]); NM[k]=null; } };
  if(!t){ ['line','lineBg','ring'].forEach(drop); return; }
  /* each is drawn twice, white underneath, as the field-log track is: one colour alone is lost on some aerial or other */
  /* the ring is a marker like the pins, not a shape in the drawing layer: a shape there is stretched with the map while two
     fingers zoom, so from far out the 13-pixel ring grew into a huge blue circle that slid about the screen (the owner, November 21, 2026) */
  if(!NM.ring) NM.ring=L.marker([t.la,t.lo],{interactive:false,keyboard:false,zIndexOffset:-50,icon:L.divIcon({className:'nmring',html:'',iconSize:[26,26],iconAnchor:[13,13]})}).addTo(map);
  else NM.ring.setLatLng([t.la,t.lo]);
  if(NM.ring._icon) NM.ring._icon.style.setProperty('--trk',pref('trk'));
  if(o&&o.how!=='map'){ const ll=[o.p,[t.la,t.lo]];
    if(!NM.line){ NM.lineBg=L.polyline(ll,{color:'#fff',opacity:0.7,weight:5.5,interactive:false}).addTo(map); NM.line=L.polyline(ll,{color:pref('trk'),weight:2.5,dashArray:'7 7',interactive:false}).addTo(map); }
    else { NM.lineBg.setLatLngs(ll); NM.line.setLatLngs(ll); } }
  else { drop('line'); drop('lineBg'); } }
const nmArrow=(b,big)=>{ const s=el('span',{class:'nmarrow'+(big?' big':''),'data-b':String(Math.round(b)),'aria-hidden':'true'}); s.innerHTML='<svg viewBox="0 0 24 24" width="'+(big?54:22)+'" height="'+(big?54:22)+'"><path d="M12 2.5 18.5 20 12 16.2 5.5 20z" fill="currentColor"/></svg>'; nmRot(s); return s; };
const nmTurn=b=>Math.round(NM.hd==null?b:(b-NM.hd+360)%360);
/* Turn one arrow to where it should point. The angle is kept running on (361, 362 ... not 1, 2) and each change goes the short way round:
   a jump from 3 to 359 degrees would otherwise be animated as a spin through nearly a whole turn. */
function nmRot(n){ const t=nmTurn(+n.getAttribute('data-b')), was=n.hasAttribute('data-r')?+n.getAttribute('data-r'):null; let r=t;
  if(was!=null&&isFinite(was)){ let d=(t-was)%360; if(d>180) d-=360; if(d<-180) d+=360; r=was+d; }
  n.setAttribute('data-r',String(r)); n.style.transform='rotate('+r+'deg)'; }
function nmSpin(){ document.querySelectorAll('#v-near .nmarrow').forEach(nmRot); }
/* the phone's compass, while the Near tab is showing: arrows then point from the way the phone is held */
function nmHeading(e){ let h=null;
  if(typeof e.webkitCompassHeading==='number') h=e.webkitCompassHeading;
  else if(e.absolute&&e.alpha!=null){ const x=rad(e.beta||0), y=rad(e.gamma||0), z=rad(e.alpha);
    /* east and north parts of two arrows fixed to the phone: out of its top edge (right when it lies flattish), and out of its back (right when it is held upright) */
    const te=-Math.sin(z)*Math.cos(x), tn=Math.cos(z)*Math.cos(x), be=-Math.cos(z)*Math.sin(y)-Math.sin(z)*Math.sin(x)*Math.cos(y), bn=-Math.sin(z)*Math.sin(y)+Math.cos(z)*Math.sin(x)*Math.cos(y);
    const top=te*te+tn*tn>=be*be+bn*bn; h=Math.atan2(top?te:be,top?tn:bn)*180/Math.PI; if(!isFinite(h)) return; }
  if(h==null) return; h=(h+((screen.orientation&&screen.orientation.angle)||0)+360)%360;
  const was=NM.hd; if(was!=null){ let d=h-was; if(d>180) d-=360; if(d<-180) d+=360; if(Math.abs(d)<2) return; h=(was+d*0.5+360)%360; }
  NM.hd=h; if(was==null) nmDraw(true); else if(!nmHeading.raf) nmHeading.raf=requestAnimationFrame(()=>{ nmHeading.raf=0; nmSpin(); }); }
function nmCompass(on){ if(on===NM.cmp) return; NM.cmp=on; const f=on?'addEventListener':'removeEventListener';
  window[f]('deviceorientationabsolute',nmHeading); window[f]('deviceorientation',nmHeading); if(!on) NM.hd=null; }
function nmAgo(t){ const m=Math.round((Date.now()-t)/60000); return m<2?'just now':m<90?m+' min ago':m<2880?Math.round(m/60)+' h ago':Math.round(m/1440)+' days ago'; }
function renderNear(){ const v=$('#v-near'); if(!v) return;
  if(!v.firstChild){   /* the controls are built once; nmDraw() fills in what changes */
    const S=nmSet(), rs=el('select',{id:'near-r','aria-label':'How far to look'},NMR.map(c=>el('option',{value:String(c[0]),text:'Within '+(KM()?c[2]:c[1])}))), as=el('select',{id:'near-al','aria-label':'Alert me when this close'},NMA.map(c=>el('option',{value:String(c[0]),text:c[0]?'Alert at '+(KM()?c[2]:c[1]):'No alert'})));
    rs.value=String(S.r); as.value=String(S.al); rs.addEventListener('change',()=>nmSave({r:+rs.value})); as.addEventListener('change',()=>nmSave({al:+as.value}));
    v.append(el('div',{class:'pad nmtop'},el('div',{id:'near-st'}),el('div',{class:'nmrow'},rs,as,el('button',{class:'btn sm',id:'near-set',type:'button','aria-label':'Near me settings',title:'Near me settings',onclick:()=>openSettings('Near me')},$('#sheet-set svg')?$('#sheet-set svg').cloneNode(true):'Settings')),el('div',{class:'presets',id:'near-k'}),el('p',{class:'nmnote',id:'near-note'})),el('div',{id:'near-goal',hidden:''}),el('ul',{id:'near-list'}));
    ['pointerdown','touchstart'].forEach(k=>v.addEventListener(k,()=>{ NM.touch=Date.now(); },{passive:true})); }
  nmDraw(true); }
function nmDraw(now){ if(view!=='near') return; const v=$('#v-near'); if(!v||!v.firstChild) return; const t=Date.now();
  if(!now&&(t-NM.drawn<1500||t-NM.touch<700)){ clearTimeout(NM.dt); NM.dt=setTimeout(nmDraw,800); return; }
  NM.drawn=t; const S=nmSet(), o=nmOrigin(), st=$('#near-st'), ul=$('#near-list'), top=v.scrollTop; NM.how=o?o.how:null; st.textContent=''; ul.textContent='';
  const btn=(txt,fn,cls)=>el('button',{class:'btn sm'+(cls?' '+cls:''),type:'button',onclick:fn},txt);
  const useMap=btn(NM.org==='map'?'Use where I am':'Use map centre',()=>{ NM.org=NM.org==='map'?'me':'map'; NM.cand=null; if(NM.org==='me'&&geo.id===null&&map) locate(); nmDraw(true); });
  const find=()=>btn('Find me',()=>{ if(map) locate(); nmDraw(true); },'pri');
  if(!o) st.append(...[el('b',{text:geo.id!==null?'Finding you…':'Near me needs to know where you are.'}),geo.id!==null?null:find(),useMap].filter(Boolean));
  else st.append(...[el('b',{text:o.how==='live'?'From where you are'+(geo.acc?', good to '+accFmt(geo.acc):''):o.how==='map'?'From the middle of the map':geo.id!==null?'Finding you… Showing where you last were':'From where you last were, '+nmAgo(U.last.t)}),o.how==='last'&&geo.id===null?find():null,useMap].filter(Boolean));
  const kb=$('#near-k'); kb.textContent=''; let all=[];
  if(o){ all=nmCands(o.p).map(x=>{ x.mi=hav(o.p[0],o.p[1],x.la,x.lo); x.b=brg(o.p[0],o.p[1],x.la,x.lo); return x; }).filter(x=>x.mi<=S.r).sort((a,b)=>a.mi-b.mi); }
  const wait={l:!LEADS,v:!XL.vanished.data,m:!XL.mines.data,c:!POCK};
  Object.keys(NMK).forEach(k=>{ const n=all.filter(x=>x.k===k).length; kb.append(el('button',{class:'chip',type:'button','aria-pressed':String(!!S.k[k]),title:k==='c'?'Old town centres are listed but never set off the alert':k==='v'?'Old school sites are left out unless they are switched on under More, Vanished places':'',onclick:()=>{ const kk=Object.assign({},nmSet().k); kk[k]=kk[k]?0:1; nmSave({k:kk}); }},el('span',{class:'sw',style:'--c:'+NMK[k][1]}),NMK[k][0]+(S.k[k]&&o?(wait[k]?' …':' '+n):''))); });
  $('#near-note').textContent=(NM.hd!=null?'Compass on: arrows point the way to walk. ':'Arrows: up is north. ')+(S.al?(navigator.vibrate?'Buzzes':'A notice shows')+' within '+nmLab(NMA,S.al)+' of a place or lead'+(NATIVE?' (screen off: only while a log records).':'.'):'');
  const g=$('#near-goal'), G=NM.goal; g.textContent=''; g.hidden=!G;
  if(G){ const far=o?hav(o.p[0],o.p[1],G.la,G.lo):null, b=o?brg(o.p[0],o.p[1],G.la,G.lo):0;
    g.append(...[o?nmArrow(b,true):null,el('div',null,el('b',{class:'nmbig',text:o?nmDist(far)+' '+dirTxt(b):'Waiting for your position'}),el('span',{text:G.n}),el('small',{text:G.t})),
      el('div',{class:'nmgo'},btn('Details',()=>nmOpen(G)),G.k==='c'?null:el('button',{class:'btn sm'+(nmMuted(G.id)?' on':''),id:'near-mute',type:'button','aria-pressed':String(nmMuted(G.id)),title:'A silenced place stays in this list but never sets off the alert. For the one beside your own house.',onclick:()=>{ const on=!nmMuted(G.id); nmMute(G.id,on); banner(on?'Silenced: '+G.n+' will not buzz again. Undo it here or in Settings.':G.n+' can buzz again.',false,5000); }},nmMuted(G.id)?'Silenced: undo':'Never buzz here'),btn('Stop',()=>nmGoal(null)))].filter(Boolean)); nmGoalDraw(); }
  if(o&&!all.length) ul.append(el('li',{class:'empty pad',text:Object.keys(wait).some(k=>S.k[k]&&wait[k])?'Loading the lead lists…':'Nothing on file within '+nmLab(NMR,S.r)+'. Try a wider circle, or switch on more kinds above.'}));
  const cap=NM.more?400:60, frag=document.createDocumentFragment();
  all.slice(0,cap).forEach(x=>frag.append(el('li',null,el('button',{class:'item pad nmitem'+(G&&G.id===x.id?' cur':''),type:'button','data-id':x.id,onclick:()=>nmGoal(x,true)},
    nmArrow(x.b),el('span',null,el('b',{text:x.n}),el('small',null,el('span',{class:'sw',style:'--c:'+NMK[x.k][1]}),x.t+(nmMuted(x.id)?' · silenced':''))),el('span',{class:'mins'},nmDist(x.mi),el('i',{text:dirTxt(x.b)}))))));
  ul.append(frag); if(all.length>cap) ul.append(el('li',{class:'pad',style:'padding-block:10px'},btn('Show all '+all.length,()=>{ NM.more=true; nmDraw(true); })));
  v.scrollTop=top; }
/* every GPS fix comes through here: refresh the list, and alert when something has come within range */
/* may this target buzz? Town centres never; places with nothing to see and vanished places only when Settings say so */
/* one target silenced for good (the place beside your own house): U.mute holds its Near id. It stays in the list. */
const nmMuted=id=>Array.isArray(U.mute)&&U.mute.indexOf(id)>=0;
function nmMute(id,on){ U.mute=(Array.isArray(U.mute)?U.mute:[]).filter(x=>x!==id); if(on) U.mute.push(id); saveNow(); NM.ver++; NM.in.delete(id); nmPush(true); if(view==='near') nmDraw(true); }
const nmBuzzes=x=>!nmMuted(x.id)&&x.k!=='c'&&!(x.k==='p'&&pref('quietGone')&&nothingToSee(x.o))&&!(x.k==='v'&&!pref('buzzVanished'));
function nmFix(p,acc){ nmDraw(NM.org==='me'&&NM.how!=='live'); if(NM.goal) nmGoalDraw(); const S=nmSet(); if(!S.al) return; nmEnsure(); if(NATIVE&&rec) nmPush(false); if(acc>35) return;
  let hit=null, more=0; nmCands(p).forEach(x=>{ if(!nmBuzzes(x)) return; const m=hav(p[0],p[1],x.la,x.lo)*1609.344;
    if(m<=S.al){ if(!NM.in.has(x.id)){ NM.in.add(x.id); if(!hit||m<hit.m){ if(hit) more++; hit={x:x,m:m}; } else more++; } } else if(m>S.al*2+30) NM.in.delete(x.id); });
  if(!hit) return; const x=hit.x;
  if(!(NATIVE&&rec)){ try{ if(navigator.vibrate) navigator.vibrate([260,140,260]); }catch(e){} }   /* while a log records in the app, the recorder buzzes */
  banner('Close by: '+x.n+', about '+nmDist(hit.m/1609.344)+' '+dirTxt(brg(p[0],p[1],x.la,x.lo))+(more?', and '+more+' more':'')+'. Tap to point me there.',false,20000);
  $('#banner').onclick=()=>{ $('#banner').hidden=true; showView('near'); nmGoal(x,true); }; }
/* in the Android app: hand the recorder everything within 25 miles, so it can buzz with the screen off */
function nmPush(force){ if(!NATIVE) return; const S=nmSet(), p=geo.ll||(U.last&&U.last.ll);
  if(!S.al||!p){ if(force||NM.push){ NM.push=null; AT.call('targets',{r:0,list:[]}).catch(()=>{}); } return; }
  if(!force&&NM.push&&NM.push.v===NM.ver&&hav(p[0],p[1],NM.push.c[0],NM.push.c[1])<8) return;
  const list=nmCollect(p,25).filter(nmBuzzes).map(x=>{ x.mi=hav(p[0],p[1],x.la,x.lo); return x; }).sort((a,b)=>a.mi-b.mi).slice(0,4000).map(x=>[+(+x.la).toFixed(5),+(+x.lo).toFixed(5),x.id,String(x.n||'').slice(0,60)]);
  NM.push={c:p.slice(),v:NM.ver,n:list.length}; AT.call('targets',{r:S.al,list:list}).catch(()=>{}); }

/* field log: a GPS track with timed notes, kept in this browser */
let rec=null, recLine=null, recMarks=[], shownLog=null, shownLayers=[], wake=null, recTick=0;

const logById=id=>(U.logs||[]).find(l=>l.id===id);
const trackMi=pts=>{ let m=0; for(let i=1;i<pts.length;i++) m+=hav(pts[i-1][0],pts[i-1][1],pts[i][0],pts[i][1]); return m; };
const hms=s=>{ s=Math.max(0,Math.round(s)); const h=Math.floor(s/3600),m=Math.floor(s%3600/60),x=s%60; return (h?h+':'+String(m).padStart(2,'0'):String(m))+':'+String(x).padStart(2,'0'); };
const logSummary=l=>fmtMi(trackMi(l.pts),2)+' · '+hms((l.t1||Math.round(Date.now()/1000))-l.t0)+' · '+l.notes.length+(l.notes.length===1?' note':' notes');
async function keepAwake(){ try{ if(navigator.wakeLock&&!document.hidden) wake=await navigator.wakeLock.request('screen'); }catch(e){ wake=null; } }
function dropAwake(){ try{ if(wake) wake.release(); }catch(e){} wake=null; }
document.addEventListener('visibilitychange',()=>{ if(document.hidden) saveNow(); else if(rec){ if(NATIVE) natSync().then(()=>syncRec()); else keepAwake(); } });
window.addEventListener('pagehide',saveNow);
/* In the Android app the phone records the track itself, screen off or not, and saves points to a file.
   This page only reads them: natSync() collects any points it has not seen yet. */
let natBusy=null, natTick=0;
function natSync(){ if(!NATIVE||!rec) return Promise.resolve(0); if(natBusy) return natBusy; const l=rec;
  natBusy=AT.call('points',{logId:l.id,from:l.nat||0}).then(r=>{ const a=(r&&r.points)||[];
      a.forEach(p=>{ l.pts.push([p[0],p[1],p[2]]); if(recLine&&rec===l) recLine.addLatLng([p[0],p[1]]); });
      if(a.length){ l.nat=(l.nat||0)+a.length; saveSlow(); } return a.length; })
    .then(n=>AT.call('marks',{logId:l.id,from:l.nmk||0}).then(r=>{ const a=(r&&r.marks)||[];   /* pins dropped with the notification's "Mark here" button */
      a.forEach(k=>{ const q=k[0]!=null?[k[0],k[1]]:trackPos(l,k[2]), nn={t:k[2],x:'Mark '+(l.notes.filter(x=>x.mk).length+1),mk:1}; if(q){ nn.la=+(+q[0]).toFixed(5); nn.lo=+(+q[1]).toFixed(5); } l.notes.push(nn); });
      if(a.length){ l.nmk=(l.nmk||0)+a.length; l.notes.sort((x,y)=>x.t-y.t); saveNow(); if(rec===l){ drawRec(); syncRec(); } if(view==='log') renderLog(); } return n; },()=>n))
    .catch(()=>0).then(n=>{ natBusy=null; return n; });
  return natBusy; }
function natWatch(){ clearInterval(natTick); natTick=setInterval(()=>{ if(!rec){ clearInterval(natTick); return; } if(!document.hidden) natSync(); },2500); }
function startLog(s){
  if(rec) return;
  if(!map||(!NATIVE&&!navigator.geolocation)){ banner('A field log needs the map and your location, which are not available here.',true,8000); return; }
  if(!Array.isArray(U.logs)) U.logs=[];
  const log={id:'log'+Date.now().toString(36),name:(s?s.name:'Field log')+' · '+new Date().toLocaleDateString(undefined,{month:'short',day:'numeric'}),site:s?s.id:null,t0:Math.round(Date.now()/1000),t1:null,pts:[],notes:[]};
  U.logs.unshift(log); U.rec=log.id; rec=log; saveNow(); hideLog();
  if(NATIVE){ log.nat=0; drawRec(); syncRec(); if(view==='log') renderLog();
    AT.call('start',{logId:log.id,title:log.name}).then(st=>{ if(rec!==log) return; natWatch(); nmEnsure(true); nmPush(true);
        banner(st&&st.gps===false?'Location is switched off on this phone. Turn it on and the log will start filling in.':'Recording. It keeps going in the background. To drop a pin without leaving the camera, pull down the notifications and tap Mark here.',!!(st&&st.gps===false),8000);
        if(geo.id===null) locate(); if(view==='log') renderLog(); },
      e=>{ if(rec===log){ rec=null; delete U.rec; clearRec(); syncRec(); } U.logs=U.logs.filter(x=>x!==log); saveNow(); if(view==='log') renderLog();
        banner('Recording could not start. '+((e&&e.message)||'Permission was refused.'),true,12000); });
    return; }
  if(geo.id===null) locate(); else banner('Recording. Keep this page open and the screen on.',false,6000);
  keepAwake(); drawRec(); syncRec(); if(view==='log') renderLog(); }
function recPoint(p,acc,t){ if(!rec||NATIVE||acc>35) return; const pts=rec.pts,last=pts[pts.length-1];
  if(last&&hav(last[0],last[1],p[0],p[1])*1609.34<STEP()) return;
  pts.push([+p[0].toFixed(5),+p[1].toFixed(5),Math.round(t/1000)]); if(recLine) recLine.addLatLng([p[0],p[1]]); saveSlow(); }
function addNote(text){ if(!rec) return; const lp=rec.pts[rec.pts.length-1], p=geo.f?[geo.f.lat,geo.f.lon]:(NATIVE&&lp?[lp[0],lp[1]]:null), n={t:Math.round(Date.now()/1000),x:(text||'').trim()||'Mark'};
  if(p){ n.la=+p[0].toFixed(5); n.lo=+p[1].toFixed(5); } rec.notes.push(n); saveNow(); drawRec(); syncRec(); if(view==='log') renderLog();
  banner('Note saved at '+hms(n.t-rec.t0)+(p?'.':'. No GPS fix yet, so it has a time but no position.'),false,3000); }
function stopLog(){ if(!rec) return;
  if(NATIVE&&!stopLog.flushed){ /* stop the phone's recorder first, then collect the last points it saved */
    AT.call('stop').catch(()=>{}).then(natSync).then(()=>{ stopLog.flushed=true; try{ stopLog(); }finally{ stopLog.flushed=false; } }); return; }
  clearInterval(natTick); const l=rec; l.t1=Math.round(Date.now()/1000); rec=null; delete U.rec; dropAwake(); clearRec(); syncRec();
  if(!l.pts.length&&!l.notes.length){ U.logs=U.logs.filter(x=>x!==l); saveNow(); banner('Nothing was recorded, so the log was discarded.',false,5000); if(view==='log') renderLog(); return; }
  saveNow(); banner('Field log saved: '+logSummary(l)+'.',false,6000); showLog(l,true); showView('log');
  if(NATIVE) (pref('autoPhotos')?scanMedia(l,false).catch(()=>{}):Promise.resolve()).then(()=>pref('autoBackup')?backupFile():null).catch(()=>{}); }
function noteMark(n,l){ const num=l.notes.indexOf(n)+1; const m=L.marker([n.la,n.lo],{keyboard:false,icon:L.divIcon({className:'notepin',html:String(num),iconSize:[22,22],iconAnchor:[11,11]})}); m._note=n;
  m.bindPopup(el('div',{class:'ctx'},el('b',{text:num+'. '+n.x}),el('span',{style:'color:#5b6660',text:hms(n.t-l.t0)+' in · '+new Date(n.t*1000).toLocaleTimeString([],{hour12:H12(),hour:'numeric',minute:'2-digit'})})),{maxWidth:240}); m.on('popupopen',()=>{ const c=m.getPopup().getContent(), ph=photosOf(l,n); c.querySelectorAll('.phs,.nacts').forEach(x=>x.remove()); if(ph.length) c.append(mediaStrip(l,ph.slice(0,6)));
    const redo=()=>{ saveNow(); map.closePopup(); if(rec===l){ drawRec(); syncRec(); } else if(shownLog===l.id) showLog(l,false); if(view==='log') renderLog(); };
    const rn=el('button',{class:'btn sm',type:'button'},'Rename'); rn.addEventListener('click',()=>{ const i=el('input',{type:'text','aria-label':'Note text',style:'width:100%'}); i.value=n.x; let done=false; const ok=()=>{ if(done) return; done=true; const t=i.value.trim(); if(t&&t!==n.x){ n.x=t; delete n.mk; redo(); } else map.closePopup(); };
      i.addEventListener('keydown',e=>{ if(e.key==='Enter') ok(); }); i.addEventListener('blur',ok); c.querySelector('b').replaceWith(i); i.focus(); i.select(); });
    const dl=el('button',{class:'btn sm',type:'button'},'Delete'); let armed=false; dl.addEventListener('click',()=>{ if(!armed){ armed=true; dl.textContent='Really delete?'; return; } l.notes=l.notes.filter(x=>x!==n); (l.media||[]).forEach(x=>{ if(x.nt===n.t&&!l.notes.some(y=>y.t===n.t)) delete x.nt; }); redo(); });
    const pl=n.pl&&byId(n.pl), ap=el('button',{class:'btn sm',type:'button'},pl?'Open its place':'+ Add to my places'); ap.addEventListener('click',()=>{ map.closePopup(); if(pl){ select(pl,true); return; } openForm({lat:n.la,lon:n.lo,name:n.x,story:'Found on a field log on '+new Date(n.t*1000).toLocaleDateString(undefined,{month:'long',day:'numeric',year:'numeric'})+'.',from:{log:l.id,t:n.t}}); });
    const sp=spotLink(n.x,n.la,n.lo,'Noted on a walk on '+new Date(n.t*1000).toLocaleDateString(undefined,{month:'long',day:'numeric',year:'numeric'})+'.','Send to the public Atlas');
    c.append(el('div',{class:'nacts'},rn,dl,rec===l?null:ap,rec===l?null:sp),rec===l?null:WHICH()); m.getPopup().update(); }); return m; }
function clearRec(){ if(recLine){ map.removeLayer(recLine); recLine=null; } recMarks.forEach(m=>map.removeLayer(m)); recMarks=[]; }
function drawRec(){ if(!map||!rec) return; clearRec();
  recLine=L.polyline(rec.pts.map(p=>[p[0],p[1]]),{color:pref('trk'),weight:4,opacity:0.9,interactive:false}).addTo(map);
  rec.notes.forEach(n=>{ if(n.la!=null) recMarks.push(noteMark(n,rec).addTo(map)); }); }
/* tapping a note in the Log tab: show that log if it is not on the map, go to the note's pin and open it */
function goNote(l,n,row){
  if(!map) return; if(n.la==null){ banner('That note was written before the phone had a location, so it has no pin.',false,5000); return; }
  if(rec!==l&&shownLog!==l.id){ showLog(l,false); if(view==='log') renderLog(); }
  const m=(rec===l?recMarks:shownLayers).find(x=>x._note===n);
  map.setView([n.la,n.lo],Math.max(map.getZoom(),18)); if(m){ if(goNote.top&&goNote.top!==m) goNote.top.setZIndexOffset(0); goNote.top=m; m.setZIndexOffset(1000); m.openPopup(); }
  goNote.at=l.id+':'+l.notes.indexOf(n); document.querySelectorAll('.lognotes li.on').forEach(x=>x.classList.remove('on'));
  const r=row&&row.isConnected?row:document.querySelector('.lognotes li[data-k="'+goNote.at+'"]'); if(r) r.classList.add('on'); }
/* ---- photos and video taken during a log (Android app only) ----
   The app asks the phone which photos and videos the camera saved during the log. Nothing is copied: a log keeps a short
   reference per item in l.media = [{k:'i'|'v', id, n:name, t:seconds, d:video length, la, lo, nt:time of the note it belongs to, fx:set by hand}].
   A photo's place is where the track was at the second it was taken. It joins the next note written within pref('near')
   metres of that place (photo first, then the note), else the note before it; otherwise it stays on the track by itself.
   A video is a stretch of time, so it is the part of the track walked while it ran. */

function trackPos(l,t){ const p=l.pts, n=p.length-1; if(n<0) return null; const end=l.t1||p[n][2];
  if(t<=p[0][2]) return t>=l.t0-90?[p[0][0],p[0][1]]:null; if(t>=p[n][2]) return t<=end+90?[p[n][0],p[n][1]]:null;
  let a=0,b=n; while(b-a>1){ const m=(a+b)>>1; if(p[m][2]<=t) a=m; else b=m; }
  const f=p[b][2]>p[a][2]?(t-p[a][2])/(p[b][2]-p[a][2]):0; return [+(p[a][0]+(p[b][0]-p[a][0])*f).toFixed(6),+(p[a][1]+(p[b][1]-p[a][1])*f).toFixed(6)]; }
const vids=l=>(l.media||[]).filter(m=>m.k==='v'), photosOf=(l,n)=>(l.media||[]).filter(m=>m.k==='i'&&m.nt===n.t), loosePhotos=l=>(l.media||[]).filter(m=>m.k==='i'&&!l.notes.some(n=>n.t===m.nt));
function clipAt(l,t){ const v=vids(l); for(let i=0;i<v.length;i++) if(t>=v[i].t&&t<=v[i].t+v[i].d) return {n:i+1,at:t-v[i].t,v:v[i]}; return null; }
function noteFor(l,m){ if(m.la==null) return null; const ns=l.notes.filter(n=>n.la!=null), near=n=>n&&hav(m.la,m.lo,n.la,n.lo)*1609.34<=(+pref('near')||25);
  const next=ns.find(n=>n.t>=m.t), prev=ns.filter(n=>n.t<m.t).pop(); return near(next)?next.t:near(prev)?prev.t:null; }
function placeMedia(l,raw){ const t0=l.t0, t1=l.t1||Math.round(Date.now()/1000), old={}, out=[]; (l.media||[]).forEach(m=>{ old[m.k+m.id]=m; });
  const inWalk=(a,b)=>a<=t1+60&&b>=t0-60;
  raw.forEach(r=>{ if(/screenshot|screen ?record/i.test(r.bucket||'')) return; const tk=Math.round((r.taken||0)/1000);
    if(r.kind==='video'){ const d=Math.round((r.duration||0)/1000); let end=r.modified||0, start=end-d;   /* the file was last written when filming stopped */
      if(!end||!inWalk(start,end)){ if(tk&&inWalk(tk-d,tk)){ end=tk; start=tk-d; } else if(tk&&inWalk(tk,tk+d)){ start=tk; end=tk+d; } else return; }
      const p=trackPos(l,Math.min(Math.max(start,t0),t1)); out.push({k:'v',id:r.id,n:r.name||'video',t:start,d:d,la:p?p[0]:null,lo:p?p[1]:null}); }
    else { const t=tk&&inWalk(tk,tk)?tk:(r.modified&&inWalk(r.modified,r.modified)?r.modified:0); if(!t) return;
      const p=trackPos(l,t), m={k:'i',id:r.id,n:r.name||'photo',t:t,la:p?p[0]:null,lo:p?p[1]:null}, was=old['i'+r.id];
      if(was&&was.fx){ m.fx=1; if(was.nt!=null) m.nt=was.nt; } else { const nt=noteFor(l,m); if(nt!=null) m.nt=nt; }
      out.push(m); } });
  out.sort((a,b)=>a.t-b.t); l.media=out; return out; }
function scanMedia(l,ask){ if(!NATIVE) return Promise.reject(new Error('Photos can only be matched in the Android app.'));
  return AT.call('media',{from:l.t0-60,to:(l.t1||Math.round(Date.now()/1000))+60,ask:!!ask}).then(r=>{ placeMedia(l,(r&&r.items)||[]); l.mscan=Math.round(Date.now()/1000); l.macc=(r&&r.access)||'all'; saveNow();
    if(shownLog===l.id) showLog(l,false); if(view==='log') renderLog(); return l.media; }); }
const thumbs=new Map();
function thumb(m,size){ if(m.th) return Promise.resolve(m.th); if(m.x||!NATIVE) return Promise.reject(new Error('no preview')); const k=m.k+m.id+':'+size; if(!thumbs.has(k)) thumbs.set(k,AT.call('thumb',{id:m.id,kind:m.k==='v'?'video':'image',size:size}).then(r=>r.data,e=>{ thumbs.delete(k); throw e; })); return thumbs.get(k); }
function thumbBtn(l,m){ const b=el('button',{class:'ph'+(m.k==='v'?' vid':''),type:'button','aria-label':(m.k==='v'?'Video ':'Photo ')+m.n});
  thumb(m,256).then(d=>{ b.append(el('img',{src:d,alt:''})); },()=>{ b.classList.add('gone'); });
  b.addEventListener('click',e=>{ e.stopPropagation(); goMedia(l,m); }); return b; }
function mediaStrip(l,list){ const d=el('div',{class:'phs'}); list.forEach(m=>d.append(thumbBtn(l,m))); return d; }
/* go to one photo or video on the map and open a card for it */
function goMedia(l,m){ if(!map) return; if(rec!==l&&shownLog!==l.id){ showLog(l,false); if(view==='log') renderLog(); }
  const tm=new Date(m.t*1000).toLocaleTimeString([],{hour12:H12(),hour:'numeric',minute:'2-digit',second:'2-digit'}), box=el('div',{class:'ctx mpop'}); let pop=null;
  const im=el('img',{alt:''}); box.append(im); thumb(m,640).then(d=>{ im.src=d; im.onload=()=>pop&&pop.update(); },()=>im.remove());
  if(m.k==='v'){ const n=vids(l).indexOf(m)+1; box.append(el('b',{text:'Video '+n+' · '+hms(m.d)+' long'}),el('span',{class:'mx',text:m.n}),el('span',{class:'mx',text:'Starts '+hms(m.t-l.t0)+' into the log · '+tm}));
    const inside=l.notes.filter(x=>x.t>=m.t&&x.t<=m.t+m.d); if(inside.length) box.append(el('span',{class:'mx',text:'Notes in it: '+inside.map(x=>hms(x.t-m.t)+' '+x.x).join(' · ')})); }
  else { const c=clipAt(l,m.t); box.append(el('b',{text:'Photo · '+tm}),el('span',{class:'mx',text:m.n+' · '+hms(m.t-l.t0)+' into the log'+(c?' · video '+c.n+' at '+hms(c.at):'')})); }
  if(NATIVE&&!m.x) box.append(el('button',{class:'btn sm',type:'button',onclick:()=>AT.call('openMedia',{id:m.id,kind:m.k==='v'?'video':'image'}).catch(e=>banner((e&&e.message)||'Could not open it.',true,6000))},m.k==='v'?'Play the video':'Open the photo'));
  if(m.k==='i'&&l.notes.length){ const sl=el('select',{'aria-label':'Attach this photo to a note'},el('option',{value:''},'Not attached to a note')); l.notes.forEach((x,i)=>sl.append(el('option',{value:String(x.t)},(i+1)+'. '+x.x)));
    sl.value=l.notes.some(x=>x.t===m.nt)?String(m.nt):''; sl.addEventListener('change',()=>{ if(sl.value) m.nt=+sl.value; else delete m.nt; m.fx=1; saveNow(); map.closePopup(); if(shownLog===l.id) showLog(l,false); if(view==='log') renderLog(); });
    box.append(el('label',{class:'mx'},'Belongs to ',sl)); }
  let at=m.la!=null?[m.la,m.lo]:map.getCenter();
  if(m.k==='v'){ const seg=l.pts.filter(p=>p[2]>=m.t&&p[2]<=m.t+m.d).map(p=>[p[0],p[1]]); if(seg.length>1){ at=seg.reduce((a,b)=>b[0]>a[0]?b:a);   /* the card hangs above the stretch's northern end, and the map leaves room for it, so the card never covers the stretch */
      map.fitBounds(L.latLngBounds(seg),{paddingTopLeft:[24,Math.min(200,Math.round(map.getSize().y*0.55))],paddingBottomRight:[24,24],maxZoom:18,animate:false}); } else if(m.la!=null) map.setView(at,Math.max(map.getZoom(),17)); }
  else if(m.la!=null) map.setView(at,Math.max(map.getZoom(),18));
  pop=L.popup({maxWidth:250,autoPan:m.k!=='v',autoPanPaddingTopLeft:[10,10]}).setLatLng(at).setContent(box).openOn(map); }
function hideLog(){ shownLayers.forEach(x=>map&&map.removeLayer(x)); shownLayers=[]; shownLog=null; }
function showLog(l,fit){ hideLog(); if(!map) return; shownLog=l.id; const ll2=l.pts.map(p=>[p[0],p[1]]);
  if(ll2.length>1) shownLayers.push(L.polyline(ll2,{color:'#ffffff',weight:6,opacity:0.8,interactive:false}).addTo(map),L.polyline(ll2,{color:pref('trk'),weight:3.5,opacity:0.95,interactive:false}).addTo(map));
  vids(l).forEach((m,i)=>{ const seg=l.pts.filter(p=>p[2]>=m.t&&p[2]<=m.t+m.d).map(p=>[p[0],p[1]]), a=trackPos(l,Math.max(m.t,l.t0)), b=trackPos(l,Math.min(m.t+m.d,l.t1||m.t+m.d)); if(a) seg.unshift(a); if(b) seg.push(b);
    if(seg.length>1) shownLayers.push(L.polyline(seg,{color:'#f5a524',weight:13,opacity:0.75,interactive:false}).addTo(map).bringToBack());   /* the stretch walked while filming */
    if(m.la!=null){ const k=L.marker([m.la,m.lo],{keyboard:false,zIndexOffset:-100,icon:L.divIcon({className:'vidpin',html:'\u25B6 '+(i+1),iconSize:[34,20],iconAnchor:[17,30]})}); k.on('click',()=>goMedia(l,m)); shownLayers.push(k.addTo(map)); } });
  loosePhotos(l).forEach(m=>{ if(m.la==null) return; const k=L.marker([m.la,m.lo],{keyboard:false,zIndexOffset:-200,icon:L.divIcon({className:'phpin',html:'',iconSize:[14,14],iconAnchor:[7,7]})}); k.on('click',()=>goMedia(l,m)); shownLayers.push(k.addTo(map)); });
  l.notes.forEach(n=>{ if(n.la!=null){ shownLayers.push(noteMark(n,l).addTo(map)); ll2.push([n.la,n.lo]); } });
  if(fit&&ll2.length) map.fitBounds(L.latLngBounds(ll2).pad(0.25),{maxZoom:18}); }
function syncRec(){ const bar=$('#recbar'); if(!bar) return; clearInterval(recTick);
  if(!rec){ bar.hidden=true; $('#rec-form').hidden=true; return; }
  bar.hidden=false; const upd=()=>{ const lv=document.getElementById('log-live'); if(rec&&lv) lv.textContent=logSummary(rec); if(rec) $('#rec-t').textContent=hms(Date.now()/1000-rec.t0)+' · '+fmtMi(trackMi(rec.pts),2)+(rec.notes.length?' · '+rec.notes.length+(rec.notes.length===1?' note':' notes'):''); };
  upd(); recTick=setInterval(upd,1000); }
function gpx(l){ const esc=s=>String(s).replace(/[<>&"]/g,c=>({'<':'&lt;','>':'&gt;','&':'&amp;','"':'&quot;'})[c]), iso=t=>new Date(t*1000).toISOString();
  return '<?xml version="1.0" encoding="UTF-8"?>\n<gpx version="1.1" creator="Lost &amp; Hidden Atlas" xmlns="http://www.topografix.com/GPX/1/1">\n<metadata><name>'+esc(l.name)+'</name><time>'+iso(l.t0)+'</time></metadata>\n'+
    l.notes.filter(n=>n.la!=null).map(n=>'<wpt lat="'+n.la+'" lon="'+n.lo+'"><time>'+iso(n.t)+'</time><name>'+esc(n.x)+'</name></wpt>\n').join('')+
    '<trk><name>'+esc(l.name)+'</name><trkseg>\n'+l.pts.map(p=>'<trkpt lat="'+p[0]+'" lon="'+p[1]+'"><time>'+iso(p[2])+'</time></trkpt>\n').join('')+'</trkseg></trk>\n</gpx>\n'; }
function notesText(l){ const tm=t=>new Date(t*1000).toLocaleTimeString([],{hour12:H12(),hour:'numeric',minute:'2-digit',second:'2-digit'});
  return l.name+'\nStarted '+new Date(l.t0*1000).toLocaleString([],{hour12:H12()})+' · '+logSummary(l)+'\n\n'+(l.notes.length?l.notes.map(n=>hms(n.t-l.t0)+'  '+tm(n.t)+'  '+n.x+(n.la!=null?'  ('+n.la+', '+n.lo+')':'')+(c=>c?'  [video '+c.n+' at '+hms(c.at)+']':'')(clipAt(l,n.t))+(p=>p.length?'  [photos: '+p.map(m=>m.n).join(', ')+']':'')(photosOf(l,n))).join('\n'):'No notes.')+'\n'+
    (vids(l).length?'\nVideos\n'+vids(l).map((m,i)=>(i+1)+'  '+m.n+'  starts '+hms(m.t-l.t0)+' into the log ('+tm(m.t)+'), '+hms(m.d)+' long').join('\n')+'\n':'')+
    (loosePhotos(l).length?'\nPhotos not attached to a note\n'+loosePhotos(l).map(m=>hms(m.t-l.t0)+'  '+tm(m.t)+'  '+m.n+(m.la!=null?'  ('+m.la+', '+m.lo+')':'')+(c=>c?'  [video '+c.n+' at '+hms(c.at)+']':'')(clipAt(l,m.t))).join('\n')+'\n':''); }
/* A walk as one file another person can open in the Atlas: track, notes, where each video ran, and small previews of the photos. */
/* For sharing: the walk with its first and last stretch cut off (Settings, "Trim the ends"), so a file does not show where it began. null = too short to trim. */
function trimmed(l){ const cut=+pref('trim')||0, p=l.pts; if(!cut||l.imp||p.length<2) return l;
  let a=-1,b=-1,d=0; for(let i=1;i<p.length;i++){ d+=hav(p[i-1][0],p[i-1][1],p[i][0],p[i][1])*1609.34; if(d>=cut){ a=i; break; } }
  d=0; for(let i=p.length-2;i>=0;i--){ d+=hav(p[i+1][0],p[i+1][1],p[i][0],p[i][1])*1609.34; if(d>=cut){ b=i; break; } }
  if(a<0||b<0||b-a<2) return null; const ta=p[a][2], tb=p[b][2];
  return Object.assign({},l,{pts:p.slice(a,b+1),t0:ta,t1:tb,notes:l.notes.filter(n=>n.t>=ta&&n.t<=tb),media:(l.media||[]).filter(m=>m.t>=ta&&m.t+(m.d||0)<=tb)}); }
const TOOSHORT='This walk is shorter than the ends you asked to trim, so nothing was shared. Change "Trim the ends" in Settings to share it.';
function walkFile(l){ const o={atlas:'walk',v:1,name:l.name,t0:l.t0,t1:l.t1,pts:l.pts,notes:l.notes.map(n=>{ const c={t:n.t,x:n.x}; if(n.la!=null){ c.la=n.la; c.lo=n.lo; } return c; }),media:[]};
  return Promise.all((l.media||[]).map((m,i)=>{ const c={k:m.k,n:m.n,t:m.t}; if(m.la!=null){ c.la=m.la; c.lo=m.lo; } if(m.d!=null) c.d=m.d; if(m.nt!=null) c.nt=m.nt;
    return i<80&&pref('previews')?thumb(m,400).then(d=>{ c.th=d; return c; },()=>c):c; })).then(ms=>{ o.media=ms; return JSON.stringify(o); }); }
function readWalk(text,fileName){ const num=x=>typeof x==='number'&&isFinite(x), id='log'+Date.now().toString(36);
  if(/^\s*</.test(text)){ /* a GPX file from any app */
    const d=new DOMParser().parseFromString(text,'application/xml'); if(d.querySelector('parsererror')) throw new Error('That GPX file could not be read.');
    const sec=e=>{ const t=e.querySelector('time'), v=t?Date.parse(t.textContent):NaN; return isFinite(v)?Math.round(v/1000):null; }, ll=e=>[+(+e.getAttribute('lat')).toFixed(6),+(+e.getAttribute('lon')).toFixed(6)];
    let pts=[...d.querySelectorAll('trkpt,rtept')].map(e=>{ const p=ll(e); return [p[0],p[1],sec(e)]; }).filter(p=>num(p[0])&&num(p[1]));
    const base=(pts.find(p=>p[2]!=null)||[0,0,Math.round(Date.now()/1000)])[2]; pts=pts.map((p,i)=>[p[0],p[1],p[2]!=null?p[2]:base+i*2]);
    const notes=[...d.querySelectorAll('wpt')].map((e,i)=>{ const p=ll(e), nm=e.querySelector('name'); return {t:sec(e)!=null?sec(e):base+i,x:(nm&&nm.textContent.trim())||'Waypoint '+(i+1),la:+p[0].toFixed(5),lo:+p[1].toFixed(5)}; }).filter(n=>num(n.la)&&num(n.lo)).sort((a,b)=>a.t-b.t);
    if(!pts.length&&!notes.length) throw new Error('That GPX file has no track or waypoints in it.');
    const nm=d.querySelector('metadata > name, trk > name'); return {id:id,name:((nm&&nm.textContent.trim())||fileName.replace(/\.gpx$/i,'')||'GPX track')+' (opened)',site:null,t0:pts.length?pts[0][2]:notes[0].t,t1:pts.length?pts[pts.length-1][2]:notes[notes.length-1].t,pts:pts,notes:notes,imp:1}; }
  let j; try{ j=JSON.parse(text); }catch(e){ throw new Error('That file is not a shared walk or a GPX track.'); }
  if(j&&'status' in j&&'logs' in j) throw new Error('That is a full Atlas backup. Restore it under Guide, "Your data and backups".');
  if(!j||j.atlas!=='walk'||!Array.isArray(j.pts)||!Array.isArray(j.notes)) throw new Error('That file is not a shared walk or a GPX track.');
  const pts=j.pts.filter(p=>Array.isArray(p)&&num(p[0])&&num(p[1])&&num(p[2])).slice(0,60000).map(p=>[p[0],p[1],p[2]]);
  const notes=j.notes.filter(n=>n&&num(n.t)&&typeof n.x==='string').slice(0,2000).map(n=>{ const c={t:n.t,x:n.x.slice(0,300)}; if(num(n.la)&&num(n.lo)){ c.la=n.la; c.lo=n.lo; } return c; });
  const media=(Array.isArray(j.media)?j.media:[]).filter(m=>m&&(m.k==='i'||m.k==='v')&&num(m.t)).slice(0,500).map((m,i)=>{ const c={k:m.k,id:'x'+i,x:1,n:String(m.n||'').slice(0,120),t:m.t}; if(num(m.la)&&num(m.lo)){ c.la=m.la; c.lo=m.lo; } if(num(m.d)) c.d=m.d; else if(m.k==='v') c.d=0; if(num(m.nt)) c.nt=m.nt; if(typeof m.th==='string'&&/^data:image\/(jpeg|png|webp);base64,[A-Za-z0-9+\/=]+$/.test(m.th)&&m.th.length<400000) c.th=m.th; return c; });
  if(!pts.length&&!notes.length) throw new Error('That walk is empty.');
  return {id:id,name:String(j.name||'Shared walk').slice(0,120)+' (shared)',site:null,t0:num(j.t0)?j.t0:(pts[0]||notes[0])[2]||notes[0].t,t1:num(j.t1)?j.t1:null,pts:pts,notes:notes,media:media,imp:1}; }
function openWalk(file){ const r=new FileReader(); r.onerror=()=>banner('That file could not be read.',true,6000);
  r.onload=()=>{ let l; try{ l=readWalk(String(r.result),file.name||''); }catch(e){ banner((e&&e.message)||'That file could not be opened.',true,9000); return; }
    if(!Array.isArray(U.logs)) U.logs=[]; U.logs.unshift(l);
    try{ localStorage.setItem(LS,JSON.stringify(U)); }catch(e){ if(l.media&&l.media.some(m=>m.th)){ l.media.forEach(m=>{ delete m.th; }); try{ localStorage.setItem(LS,JSON.stringify(U)); banner('Opened, but without photo previews: there was not enough room to keep them.',true,9000); }catch(e2){ U.logs.shift(); banner('There is not enough storage left to keep that walk.',true,9000); return; } } else { U.logs.shift(); banner('There is not enough storage left to keep that walk.',true,9000); return; } }
    showView('log'); showLog(l,true); renderLog(); banner('Opened "'+l.name+'": '+logSummary(l)+'.',false,6000); };
  r.readAsText(file); }
/* For editing footage: where each note and photo falls inside each video. */
function editSheet(l){ const tc=x=>{ x=Math.max(0,Math.round(x)); return [Math.floor(x/3600),Math.floor(x%3600/60),x%60].map(v=>String(v).padStart(2,'0')).join(':'); }, tm=t=>new Date(t*1000).toLocaleTimeString([],{hour12:H12(),hour:'numeric',minute:'2-digit',second:'2-digit'});
  const out=[l.name,'Edit sheet: the time inside each video where a note was written or a photo was taken.',''], used=new Set();
  vids(l).forEach((m,i)=>{ out.push('VIDEO '+(i+1)+'   '+m.n+'   started '+tm(m.t)+'   length '+tc(m.d));
    const rows=l.notes.filter(n=>n.t>=m.t&&n.t<=m.t+m.d).map(n=>[n.t,'NOTE ',n.x,n]).concat((l.media||[]).filter(p=>p.k==='i'&&p.t>=m.t&&p.t<=m.t+m.d).map(p=>[p.t,'PHOTO',p.n+((nn=>nn?'  (with "'+nn.x+'")':'')(l.notes.find(n=>n.t===p.nt))),p])).sort((a,b)=>a[0]-b[0]);
    rows.forEach(r=>{ used.add(r[3]); out.push('  '+tc(r[0]-m.t)+'   '+r[1]+'  '+r[2]); }); if(!rows.length) out.push('  (no notes or photos during this video)'); out.push(''); });
  const rest=l.notes.filter(n=>!used.has(n)).map(n=>[n.t,'NOTE ',n.x]).concat((l.media||[]).filter(p=>p.k==='i'&&!used.has(p)).map(p=>[p.t,'PHOTO',p.n])).sort((a,b)=>a[0]-b[0]);
  if(rest.length){ out.push('NOT DURING ANY VIDEO   (time into the walk, clock time)'); rest.forEach(r=>out.push('  '+tc(r[0]-l.t0)+'   '+tm(r[0])+'   '+r[1]+'  '+r[2])); out.push(''); }
  return out.join('\n'); }
/* ---------- episode kit ----------
   From one finished field log, everything needed to cut and publish a video about it:
     stops     the Atlas places the walk came to, in the order reached (kitStops)
     parts     the walk cut into "walking" and "at a stop", with the clips, photos and notes that fall in each (kitParts)
     chapters  draft YouTube chapters: where each stop starts if the clips are joined end to end, uncut (kitChapters)
     words     a description with what each place is, how to visit and the sources from its place record (kitDescription)
     picture   a 1920 x 1080 route map on the public-domain USGS base map (kitMap)
   Nothing is uploaded. The picture and the distance use the trimmed walk (Settings, "Trim the ends"), so they do not show where the car was. */
let kitOpen=null;
const KITSITE='https://mrroot3r.github.io/Lost-and-Hidden-Atlas/';
function kitStops(l){ const p=l.pts, out=[]; if(p.length<2) return out;
  let a=90,b=-90,c=180,d=-180; p.forEach(q=>{ if(q[0]<a)a=q[0]; if(q[0]>b)b=q[0]; if(q[1]<c)c=q[1]; if(q[1]>d)d=q[1]; });
  sites().forEach(s=>{ const q=pos(s); if(q.lat<a-0.006||q.lat>b+0.006||q.lon<c-0.008||q.lon>d+0.008) return;
    /* a visit starts when the track comes within reach of the pin and ends when it has gone half as far again; the longest visit is the stop */
    const reach=Math.min(250,Math.max(60,(PREC[s.prec]||PREC.site)[2])); let ins=false, v=null, best=null, near=1e9;
    p.forEach(k=>{ const m=hav(q.lat,q.lon,k[0],k[1])*1609.344; if(m<near) near=m;
      if(!ins&&m<=reach){ ins=true; v={t0:k[2],t1:k[2]}; if(!best) best=v; } else if(ins){ if(m>reach*1.5) ins=false; else { v.t1=k[2]; if(v.t1-v.t0>best.t1-best.t0) best=v; } } });
    if(best) out.push({s:s,t0:best.t0,t1:best.t1,m:Math.round(near),la:q.lat,lo:q.lon}); });
  return out.sort((x,y)=>x.t0-y.t0); }
function kitParts(l,stops){ const end=l.t1||(l.pts.length?l.pts[l.pts.length-1][2]:l.t0), parts=[]; let t=l.t0;
  stops.forEach((st,i)=>{ const nx=stops[i+1], a=Math.max(st.t0,t), b=Math.max(a,nx?Math.min(st.t1,nx.t0):st.t1);
    if(a>t) parts.push({k:'walk',t0:t,t1:a,name:'On the way to '+st.s.name}); parts.push({k:'stop',t0:a,t1:b,st:st,n:i+1,name:st.s.name}); t=b; });
  if(end>t||!parts.length) parts.push({k:'walk',t0:t,t1:Math.max(end,t),name:stops.length?'After '+stops[stops.length-1].s.name:'The walk'});
  const last=parts[parts.length-1], inP=(P,x)=>x>=P.t0&&(x<P.t1||(P===last&&x<=P.t1+120));
  parts.forEach(P=>{ P.notes=l.notes.filter(n=>inP(P,n.t)); P.photos=(l.media||[]).filter(m=>m.k==='i'&&inP(P,m.t));
    P.clips=vids(l).map((m,i)=>({n:i+1,v:m,a:Math.max(m.t,P.t0),b:Math.min(m.t+m.d,P.t1)})).filter(c=>c.b>c.a); });
  return parts; }
/* seconds into the footage, if every clip is laid end to end in the order it was shot; a moment between clips counts as the start of the next one */
function kitRun(l,t){ let run=0; const v=vids(l); for(let i=0;i<v.length;i++){ if(t<v[i].t) return run; if(t<=v[i].t+v[i].d) return run+(t-v[i].t); run+=v[i].d; } return null; }
function kitChapters(l,parts){ const v=vids(l), out=[]; if(!v.length) return out; const total=v.reduce((s,m)=>s+m.d,0);
  const add=(sec,name)=>{ if(sec==null||sec>total-10) return; const p=out[out.length-1]; if(p&&sec-p[0]<10) return; out.push([Math.round(sec),name]); };
  out.push([0,parts.length&&parts[0].k==='stop'&&parts[0].clips.length&&kitRun(l,parts[0].clips[0].a)<10?parts[0].name:'Setting out']);
  const stops=parts.filter(P=>P.k==='stop'&&P.clips.length);
  stops.forEach(P=>add(kitRun(l,P.clips[0].a),P.name));
  if(out.length<3){   /* too few stops to make chapters: use the notes as well */
    const all=out.concat(l.notes.filter(n=>clipAt(l,n.t)).map(n=>[Math.round(kitRun(l,n.t)),n.x])).sort((x,y)=>x[0]-y[0]); out.length=0;
    all.forEach(x=>{ const p=out[out.length-1]; if(x[0]>total-10&&out.length) return; if(p&&x[0]-p[0]<10) return; out.push(x); }); }
  return out; }
const kitChapText=ch=>ch.map(c=>hms(c[0])+' '+c[1]).join('\n');
function kitDescription(l,stops,ch){ const tl=trimmed(l)||l, out=[], first=x=>{ x=String(x||'').trim(); const m=/^.*?[.!?](?=\s|$)/.exec(x); return m?m[0]:x; };
  out.push(l.name.replace(/\s*·\s*[A-Z][a-z]{2} \d{1,2}$/,''),'');
  if(stops.length){ out.push(stops.length===1?'In this video:':'In this video, in the order we reached them:');
    stops.forEach(o=>{ const s=o.s; out.push('• '+s.name+(s.town?', '+s.town:'')+(s.years?' ('+s.years+')':'')+((s.hook||s.story)?': '+(s.hook||first(s.story)):'')); }); out.push(''); }
  if(ch.length>=3){ out.push('Chapters',kitChapText(ch),''); }
  out.push('On foot: '+fmtMi(trackMi(tl.pts),1)+' in '+fmtMin(Math.max(1,Math.round(((tl.t1||tl.t0)-tl.t0)/60)))+'.');
  const acc=stops.filter(o=>o.s.accn||ACC[o.s.acc]); if(acc.length){ out.push('','Before you go'); acc.forEach(o=>out.push(('• '+o.s.name+': '+(ACC[o.s.acc]||'')+(o.s.accn?(ACC[o.s.acc]?'. ':'')+first(o.s.accn):'')).replace(/[.\s]*$/,'.')+(o.s.hrs?' Hours: '+o.s.hrs.replace(/[.\s]*$/,'.'):''))); }
  const src=stops.filter(o=>Array.isArray(o.s.links)&&o.s.links.length); if(src.length){ out.push('','Sources and further reading'); src.forEach(o=>{ out.push(o.s.name+':'); o.s.links.forEach(k=>out.push('  '+k[0]+' '+k[1])); }); }
  if(String(pref('kitSign')||'').trim()) out.push('',String(pref('kitSign')).trim());
  out.push('','Route recorded with the Lost & Hidden Atlas: '+KITSITE+(stops.length?'#'+stops[0].s.id:''),'Route map: base map from USGS The National Map.');
  return out.join('\n'); }
/* the whole kit as one text file: clips, photos and notes grouped by place, then the chapters and the description */
function kitText(l){ const stops=kitStops(l), parts=kitParts(l,stops), ch=kitChapters(l,parts), tm=t=>new Date(t*1000).toLocaleTimeString([],{hour12:H12(),hour:'numeric',minute:'2-digit'});
  const out=['EPISODE KIT: '+l.name,new Date(l.t0*1000).toLocaleDateString([],{dateStyle:'long'})+' · '+logSummary(l),'','BY PLACE, IN THE ORDER WALKED','Times are h:mm:ss into the walk unless they say "in the clip".',''];
  parts.forEach(P=>{ if(P.k==='walk'&&!P.notes.length&&!P.photos.length&&!P.clips.length) return;
    out.push((P.k==='stop'?P.n+'. '+P.name.toUpperCase()+(P.st.s.town?', '+P.st.s.town:''):P.name.toUpperCase())+'   '+hms(P.t0-l.t0)+' to '+hms(P.t1-l.t0)+' ('+tm(P.t0)+')'+(P.k==='stop'?'   '+Math.max(1,Math.round((P.t1-P.t0)/60))+' min there, pin '+P.st.m+' m from the track':''));
    P.clips.forEach(c=>out.push('   VIDEO '+c.n+'  '+c.v.n+'   '+(c.a<=c.v.t&&c.b>=c.v.t+c.v.d?'all of it ('+hms(c.v.d)+')':hms(c.a-c.v.t)+' to '+hms(c.b-c.v.t)+' in the clip')));
    if(P.photos.length) out.push('   PHOTOS  '+P.photos.map(m=>m.n).join(', '));
    P.notes.forEach(n=>{ const c=clipAt(l,n.t); out.push('   NOTE  '+hms(n.t-l.t0)+'  '+n.x+(c?'   (video '+c.n+' at '+hms(c.at)+')':'')); }); out.push(''); });
  if(!stops.length) out.push('This walk did not come within reach of any place on the Atlas, so nothing is grouped by place.','');
  out.push('YOUTUBE CHAPTERS (DRAFT)',ch.length>=3?kitChapText(ch):vids(l).length?'Fewer than three chapters could be made from this walk; YouTube needs at least three.':'No video is matched to this walk yet, so there are no chapter times. Use "Find photos and video" in the app first.',
    ch.length>=3?'These assume every clip is joined end to end in the order shot, with nothing cut. Shift them to match your edit. YouTube needs the first at 0:00, at least three, each 10 seconds or longer.':'','','DESCRIPTION','',kitDescription(l,stops,ch));
  return out.join('\n'); }
/* ---- the route map picture ---- */
const KITMAP={topo:['Topo','https://basemap.nationalmap.gov/arcgis/rest/services/USGSTopo/MapServer/tile/{z}/{y}/{x}'],air:['Aerial','https://basemap.nationalmap.gov/arcgis/rest/services/USGSImageryOnly/MapServer/tile/{z}/{y}/{x}']};
async function kitMap(l,style){ const tl=trimmed(l); if(!tl) throw new Error(TOOSHORT); const pts=tl.pts; if(pts.length<2) throw new Error('This walk has no track to draw.');
  const stops=kitStops(l), Wd=1920, Ht=1080, fl=714, fr=Wd-110, ft=110, fb=Ht-110, ox=(fl+fr)/2, oy=(ft+fb)/2, wx=(lo,z)=>(lo+180)/360*256*Math.pow(2,z), wy=(la,z)=>{ const s=Math.sin(rad(la)); return (0.5-Math.log((1+s)/(1-s))/(4*Math.PI))*256*Math.pow(2,z); };
  let a=90,b=-90,c=180,d=-180; const grow=(la,lo)=>{ if(la<a)a=la; if(la>b)b=la; if(lo<c)c=lo; if(lo>d)d=lo; }; pts.forEach(q=>grow(q[0],q[1])); stops.forEach(o=>grow(o.la,o.lo));
  /* the zoom that fits the walk in the frame, in fractions; tiles come from the whole zoom at or below it (the base map stops at 16) and are stretched */
  const w0=Math.max(1e-9,wx(d,0)-wx(c,0)), h0=Math.max(1e-9,wy(a,0)-wy(b,0)), zf=Math.min(17.5,Math.log2(Math.min((fr-fl)/w0,(fb-ft)/h0))), zt=Math.max(1,Math.min(16,Math.floor(zf+0.35))), k=Math.pow(2,zf-zt);
  const cx=(wx(c,zt)+wx(d,zt))/2, cy=(wy(a,zt)+wy(b,zt))/2, X=lo=>(wx(lo,zt)-cx)*k+ox, Y=la=>(wy(la,zt)-cy)*k+oy;
  const cv=document.createElement('canvas'); cv.width=Wd; cv.height=Ht; const g=cv.getContext('2d'); g.fillStyle='#e9e6dc'; g.fillRect(0,0,Wd,Ht);
  const x0=Math.floor((cx-ox/k)/256), x1=Math.floor((cx+(Wd-ox)/k)/256), y0=Math.floor((cy-oy/k)/256), y1=Math.floor((cy+(Ht-oy)/k)/256), n=Math.pow(2,zt), jobs=[]; let miss=0;
  for(let tx=x0;tx<=x1;tx++) for(let ty=y0;ty<=y1;ty++){ if(ty<0||ty>=n) continue; const u=KITMAP[style][1].replace('{z}',zt).replace('{y}',ty).replace('{x}',((tx%n)+n)%n);
    jobs.push(fetch(u).then(r=>{ if(!r.ok) throw 0; return r.blob(); }).then(bl=>createImageBitmap(bl)).then(im=>{ g.drawImage(im,Math.round((tx*256-cx)*k+ox),Math.round((ty*256-cy)*k+oy),Math.ceil(256*k)+1,Math.ceil(256*k)+1); }).catch(()=>{ miss++; })); }
  await Promise.all(jobs);
  if(style==='air'){ g.fillStyle='rgba(0,0,0,.18)'; g.fillRect(0,0,Wd,Ht); } else { g.fillStyle='rgba(255,255,255,.22)'; g.fillRect(0,0,Wd,Ht); }
  const path=()=>{ g.beginPath(); pts.forEach((q,i)=>{ const x=X(q[1]), y=Y(q[0]); if(i) g.lineTo(x,y); else g.moveTo(x,y); }); };
  g.lineJoin='round'; g.lineCap='round'; path(); g.strokeStyle='#fff'; g.lineWidth=13; g.stroke(); path(); g.strokeStyle=pref('trk'); g.lineWidth=7; g.stroke();
  const font=(px,wt)=>{ g.font=(wt||700)+' '+px+'px system-ui,-apple-system,"Segoe UI",Roboto,Arial,sans-serif'; };
  [pts[0],pts[pts.length-1]].forEach(q=>{ g.beginPath(); g.arc(X(q[1]),Y(q[0]),9,0,7); g.fillStyle='#fff'; g.fill(); g.lineWidth=4; g.strokeStyle='#111'; g.stroke(); });
  stops.forEach((o,i)=>{ const x=X(o.lo), y=Y(o.la); g.beginPath(); g.arc(x,y,25,0,7); g.fillStyle='#111'; g.fill(); g.lineWidth=5; g.strokeStyle='#fff'; g.stroke(); font(28); g.fillStyle='#fff'; g.textAlign='center'; g.textBaseline='middle'; g.fillText(String(i+1),x,y+1); });
  /* the panel: title, distance and time, numbered stops */
  g.textAlign='left'; g.textBaseline='alphabetic'; const title=l.name.replace(/\s*·\s*[A-Z][a-z]{2} \d{1,2}$/,''), fit=(t,px,wt,max)=>{ font(px,wt); if(g.measureText(t).width<=max) return t; while(t.length>4&&g.measureText(t+'…').width>max) t=t.slice(0,-1); return t.trim()+'…'; };
  const rows=stops.slice(0,9), pw=620, ph=118+rows.length*46+(stops.length>9?40:0)+(rows.length?14:0), px0=44, py0=44;
  g.fillStyle='rgba(255,255,255,.93)'; g.beginPath(); if(g.roundRect) g.roundRect(px0,py0,pw,ph,18); else g.rect(px0,py0,pw,ph); g.fill();
  g.fillStyle='#111'; g.fillText(fit(title,40,800,pw-56),px0+28,py0+58); font(27,500); g.fillStyle='#333'; g.fillText(fmtMi(trackMi(pts),1)+' on foot · '+fmtMin(Math.max(1,Math.round(((tl.t1||tl.t0)-tl.t0)/60))),px0+28,py0+98);
  rows.forEach((o,i)=>{ const y=py0+150+i*46; g.beginPath(); g.arc(px0+46,y-10,17,0,7); g.fillStyle='#111'; g.fill(); font(20); g.fillStyle='#fff'; g.textAlign='center'; g.fillText(String(i+1),px0+46,y-3); g.textAlign='left'; g.fillStyle='#111'; g.fillText(fit(o.s.name,28,600,pw-112),px0+76,y); });
  if(stops.length>9){ font(24,500); g.fillStyle='#333'; g.fillText('and '+(stops.length-9)+' more',px0+76,py0+150+9*46); }
  /* scale bar, north, credit */
  const mpp=156543.03392*Math.cos(rad((a+b)/2))/Math.pow(2,zf);   /* metres to one pixel of the picture */
  const bars=KM()?[[20,'20 m'],[50,'50 m'],[100,'100 m'],[200,'200 m'],[500,'500 m'],[1000,'1 km'],[2000,'2 km'],[5000,'5 km'],[10000,'10 km'],[20000,'20 km']]:[[30.48,'100 ft'],[60.96,'200 ft'],[152.4,'500 ft'],[304.8,'1,000 ft'],[402.336,'¼ mi'],[804.672,'½ mi'],[1609.344,'1 mi'],[3218.688,'2 mi'],[8046.72,'5 mi'],[16093.44,'10 mi']];
  const bar=bars.filter(o=>o[0]/mpp<=300).pop()||bars[0], len=bar[0]/mpp, lab=bar[1], sx=44, sy=Ht-52;
  g.fillStyle='rgba(255,255,255,.93)'; g.fillRect(sx-12,sy-44,len+24,66); g.strokeStyle='#111'; g.lineWidth=5; g.beginPath(); g.moveTo(sx,sy-10); g.lineTo(sx,sy+4); g.lineTo(sx+len,sy+4); g.lineTo(sx+len,sy-10); g.stroke(); font(24,600); g.fillStyle='#111'; g.fillText(lab,sx+8,sy-12);
  g.fillStyle='rgba(255,255,255,.93)'; g.beginPath(); g.arc(Wd-84,92,44,0,7); g.fill(); g.fillStyle='#111'; g.beginPath(); g.moveTo(Wd-84,58); g.lineTo(Wd-68,104); g.lineTo(Wd-84,94); g.lineTo(Wd-100,104); g.closePath(); g.fill(); font(22); g.textAlign='center'; g.fillText('N',Wd-84,128);
  const cr='Base map: USGS The National Map'; font(21,500); g.textAlign='right'; const cw=g.measureText(cr).width; g.fillStyle='rgba(255,255,255,.88)'; g.fillRect(Wd-cw-36,Ht-44,cw+36,44); g.fillStyle='#222'; g.fillText(cr,Wd-18,Ht-15);
  return {canvas:cv,miss:miss,tiles:jobs.length,stops:stops.length}; }
async function sendBlob(name,blob,btn){
  if(NATIVE){ const b64=await new Promise((res,rej)=>{ const r=new FileReader(); r.onload=()=>res(String(r.result).split(',')[1]||''); r.onerror=()=>rej(r.error); r.readAsDataURL(blob); }); await AT.call('share',{name:name,base64:b64,mime:blob.type}); return; }
  try{ const f=new File([blob],name,{type:blob.type}); if(navigator.canShare&&navigator.canShare({files:[f]})&&/Android|iPhone|iPad/.test(navigator.userAgent)){ await navigator.share({files:[f],title:name}); return; } }catch(e){ if(e&&e.name==='AbortError') return; }
  const a=el('a',{href:URL.createObjectURL(blob),download:name}); document.body.append(a); a.click(); a.remove(); }
function kitPanel(l,fn){ const stops=kitStops(l), parts=kitParts(l,stops), ch=kitChapters(l,parts), nv=vids(l).length, box=el('div',{class:'kit'});
  const plural=(n,w)=>n+' '+w+(n===1?'':'s'), B=(t,f)=>{ const b=el('button',{class:'btn sm',type:'button'},t); b.addEventListener('click',()=>f(b)); return b; };
  box.append(el('h4',{text:'Episode kit'}),el('p',{class:'snote',text:stops.length?'The walk came to '+plural(stops.length,'place')+' on the Atlas. Clips, photos and notes are grouped under each.':'This walk did not come within reach of any place on the Atlas, so there is nothing to group by place. The route map and the notes still work.'}));
  if(stops.length){ const ol=el('ol',{class:'kitstops'}); parts.filter(P=>P.k==='stop').forEach(P=>{ const li=el('li',{role:'button',tabindex:'0'},el('b',{text:P.name}),el('small',{text:['reached '+hms(P.t0-l.t0),Math.max(1,Math.round((P.t1-P.t0)/60))+' min',P.clips.length?plural(P.clips.length,'clip'):'',P.photos.length?plural(P.photos.length,'photo'):'',P.notes.length?plural(P.notes.length,'note'):''].filter(Boolean).join(' · ')}));
      li.addEventListener('click',()=>select(P.st.s,true)); ol.append(li); }); box.append(ol); }
  const chBox=el('pre',{class:'kitpre',text:ch.length>=3?kitChapText(ch):nv?'Fewer than three chapters could be made; YouTube needs at least three. Add a note at each thing you film and they become chapters.':NATIVE?'No video is matched to this walk yet. Tap "Find photos and video" above, then open the kit again.':'Chapter times come from the videos the Android app matches to a walk. This walk has none.'});
  box.append(el('h5',{text:'YouTube chapters (draft)'}),chBox,ch.length>=3?el('p',{class:'snote',text:'These assume the clips are joined end to end in the order shot, with nothing cut. Shift them to match your edit.'}):null);
  const pic=el('div',{class:'kitpic'}), sty=el('select',{'aria-label':'Base map for the picture'},Object.keys(KITMAP).map(k=>el('option',{value:k,text:KITMAP[k][0]})));
  if(KITMAP[pref('kitBase')]) sty.value=pref('kitBase'); sty.addEventListener('change',()=>setPref('kitBase',sty.value));
  const draw=async b=>{ const was=b.textContent; b.disabled=true; b.textContent='Drawing…'; pic.textContent='';
    try{ const r=await kitMap(l,sty.value), blob=await new Promise(res=>r.canvas.toBlob(res,'image/png')); const im=el('img',{alt:'Route map of this walk',src:URL.createObjectURL(blob)}); pic.append(im,el('div',{class:'row',style:'margin-top:6px'},B(NATIVE?'Share the picture':'Save the picture',bb=>sendBlob(fn+'-route-map.png',blob,bb).catch(()=>banner('The picture could not be shared.',true,6000))),el('span',{class:'snote',text:'1920 × 1080'+(r.miss?' · '+r.miss+' of '+r.tiles+' map tiles did not load, so parts are blank. Try again with a signal.':'')})));
    }catch(e){ pic.append(el('p',{class:'pn',text:(e&&e.message)||'The picture could not be drawn.'})); }
    b.disabled=false; b.textContent=was; };
  box.append(el('div',{class:'row',style:'margin-top:8px'},ch.length>=3?B('Copy chapters',b=>copy(kitChapText(ch),b)):null,B('Copy description',b=>copy(kitDescription(l,stops,ch),b)),B(NATIVE?'Share the whole kit':'Save the whole kit',b=>sendFile(fn+'-episode-kit.txt',kitText(l),'text/plain',b))),
    el('h5',{text:'Route map picture'}),el('div',{class:'row'},sty,B('Draw the route map',draw)),el('p',{class:'snote',text:'A 1920 × 1080 picture for the video, on the public-domain USGS base map. The ends of the walk are trimmed as set in Settings.'}),pic);
  return box; }
/* In the app: keep a copy of everything in the phone's Downloads, where it survives the app being removed. */
let lastBackup=0;
function backupFile(){ if(!NATIVE) return Promise.reject(new Error('Only in the Android app.')); return AT.call('saveBackup',{name:'atlas-backup.json',text:JSON.stringify(U)}).then(r=>{ lastBackup=Date.now(); return r; }); }
async function sendFile(name,text,type,btn){
  if(NATIVE){ try{ await AT.call('share',{name:name,text:text,mime:type}); }catch(e){ copy(text,btn); banner('Sharing failed, so the text was copied instead.',true,5000); } return; }
  const blob=new Blob([text],{type:type});
  try{ const f=new File([blob],name,{type:type}); if(navigator.canShare&&navigator.canShare({files:[f]})){ await navigator.share({files:[f],title:name}); return; } }catch(e){ if(e&&e.name==='AbortError') return; }
  try{ const a=el('a',{href:URL.createObjectURL(blob),download:name}); document.body.append(a); a.click(); a.remove(); }catch(e){ copy(text,btn); } }
function renderLog(){
  const v=$('#v-log'); if(!v) return; v.textContent=''; if(!Array.isArray(U.logs)) U.logs=[];
  const top=el('div',{class:'sec pad'},el('h3',{text:'Field log'}));
  if(rec){ top.append(el('p',null,el('b',{text:'Recording: '}),rec.name),el('p',{class:'mono',id:'log-live',style:'font-size:13px',text:logSummary(rec)}),
      el('div',{class:'row'},el('button',{class:'btn pri',type:'button',onclick:()=>{ $('#rec-note').click(); }},'+ Note here'),el('button',{class:'btn',type:'button',onclick:stopLog},'Stop and save'))); }
  else { top.append(el('p',{text:'Records where you walk and lets you drop timed notes on the spot. Afterwards you get the track for mapping and a note list with times to line up against your footage.'}),
      el('div',{class:'row'},el('button',{class:'btn pri',type:'button',onclick:()=>startLog(null)},'Start a field log'),sel?el('button',{class:'btn',type:'button',onclick:()=>startLog(sel)},'Start at '+sel.name):null)); }
  if(NATIVE){ top.append(el('p',{class:'snote',style:'margin-top:8px',text:'Recording carries on with the screen off or the app in the background; Android shows a notification while it runs. If Android stops the app, the track so far is kept and the log picks up when you open the Atlas again.'}));
    const tips=el('div',{class:'row',style:'margin-top:8px'}); top.append(tips);
    AT.call('status').then(st=>{
      if(st.gps===false) tips.before(el('p',{class:'pn',text:'Location is switched off on this phone, so nothing can be recorded until it is on.'}));
      if(st.battery===false) tips.append(el('button',{class:'btn sm',type:'button',onclick:()=>AT.call('battery')},'Stop Android pausing it'));
      if(st.background===false) tips.append(el('button',{class:'btn sm',type:'button',onclick:()=>AT.call('appSettings')},'Allow location all the time'));
      if(st.battery===false||st.background===false) tips.after(el('p',{class:'snote',style:'margin-top:6px',text:(st.battery===false?'"Stop Android pausing it" asks Android not to shut the app down to save battery, the usual reason a recording ends early. ':'')+(st.background===false?'"Allow location all the time" is optional: under Permissions, Location. It lets Android restart a recording by itself.':'')}));
    }).catch(()=>{}); }
  else top.append(el('p',{class:'snote',style:'margin-top:8px',text:'It only records while this page is open and the screen is on. The Atlas keeps the screen awake while it records, where the phone allows. Logs are saved in this browser and are included in your backup.'}));
  const pick=el('input',{type:'file',id:'walk-file',hidden:true,onchange:e=>{ const f=e.target.files[0]; e.target.value=''; if(f) openWalk(f); }});
  top.append(el('div',{class:'row',style:'margin-top:10px'},el('button',{class:'btn sm',type:'button',onclick:()=>pick.click()},'Open a shared walk or GPX file'),pick));
  v.append(top);
  const done=U.logs.filter(l=>l!==rec);
  if(!done.length){ v.append(el('p',{class:'pad',style:'color:var(--mute);padding-block:12px',text:rec?'':'No saved logs yet.'})); return; }
  done.forEach(l=>{
    const shown=shownLog===l.id, fn=l.name.replace(/[^\w]+/g,'-').replace(/^-|-$/g,'').toLowerCase()||'field-log';
    const title=el('b',{text:l.name});
    const ren=el('button',{class:'btn sm',type:'button',onclick:()=>{ const i=el('input',{type:'text','aria-label':'Log name'}); i.value=l.name; const ok=()=>{ l.name=i.value.trim()||l.name; saveNow(); renderLog(); }; i.addEventListener('keydown',e=>{ if(e.key==='Enter') ok(); }); i.addEventListener('blur',ok); title.replaceWith(i); i.focus(); }},'Rename');
    const cp=el('button',{class:'btn sm',type:'button'},'Copy notes'); cp.addEventListener('click',()=>copy(notesText(l),cp));
    const gx=el('button',{class:'btn sm',type:'button'},NATIVE?'Share route (GPX)':'GPX track'); gx.addEventListener('click',()=>{ const tl=trimmed(l); if(!tl){ banner(TOOSHORT,true,10000); return; } sendFile(fn+'.gpx',gpx(tl),'application/gpx+xml',gx); });
    const sw=el('button',{class:'btn sm',type:'button'},'Share this walk'); sw.addEventListener('click',()=>{ const tl=trimmed(l); if(!tl){ banner(TOOSHORT,true,10000); return; } sw.disabled=true; sw.textContent='Packing…'; walkFile(tl).then(t=>sendFile(fn+'.atlas.json',t,'application/json',sw)).catch(()=>banner('The walk could not be packed.',true,6000)).then(()=>{ sw.disabled=false; sw.textContent='Share this walk'; }); });
    const es=vids(l).length?el('button',{class:'btn sm',type:'button'},'Edit sheet'):null; if(es) es.addEventListener('click',()=>sendFile(fn+'-edit-sheet.txt',editSheet(l),'text/plain',es));
    const ek=l.pts.length>1?el('button',{class:'btn sm'+(kitOpen===l.id?' on':''),type:'button','aria-expanded':String(kitOpen===l.id),onclick:()=>{ kitOpen=kitOpen===l.id?null:l.id; renderLog(); }},'Episode kit'):null;
    const del=el('button',{class:'btn sm',type:'button'},'Delete'); let armed=false; del.addEventListener('click',()=>{ if(!armed){ armed=true; del.textContent='Really delete?'; setTimeout(()=>{ armed=false; del.textContent='Delete'; },4000); return; } if(shownLog===l.id) hideLog(); U.logs=U.logs.filter(x=>x!==l); saveNow(); if(NATIVE) AT.call('remove',{logId:l.id}).catch(()=>{}); renderLog(); });
    const site=l.site&&byId(l.site);
    const box=el('div',{class:'sec pad logitem'},title,el('p',{class:'sub2',text:new Date(l.t0*1000).toLocaleString([],{hour12:H12(),dateStyle:'medium',timeStyle:'short'})+' · '+logSummary(l)}),
      el('div',{class:'row',style:'margin-top:6px'},map?el('button',{class:'btn sm'+(shown?' on':''),type:'button',onclick:()=>{ if(shown) hideLog(); else showLog(l,true); renderLog(); }},shown?'Hide on map':'Show on map'):null,sw,gx,cp,es,ek,ren,del),
      site?el('p',{style:'margin-top:6px'},el('button',{class:'btn sm',type:'button',onclick:()=>select(site,true)},'Open '+site.name)):null);
    if(l.notes.length){ const ul=el('ul',{class:'lognotes'}); l.notes.forEach((n,i)=>{ const k=l.id+':'+i, li=el('li',{role:'button',tabindex:'0','data-k':k,class:(goNote.at===k?'on':'')+(n.la==null?' nopin':'')},el('span',{class:'num',text:String(i+1)}),el('span',{class:'mono',text:hms(n.t-l.t0)}),el('span',{class:'nx',text:n.x})); const cl=clipAt(l,n.t), ph=photosOf(l,n); if(cl) li.append(el('span',{class:'clip',title:'Position in video '+cl.n,text:'\u25B6'+cl.n+' '+hms(cl.at)})); if(ph.length) li.append(mediaStrip(l,ph)); const go=()=>goNote(l,n,li); li.addEventListener('click',go); li.addEventListener('keydown',e=>{ if(e.key==='Enter'||e.key===' '){ e.preventDefault(); go(); } }); ul.append(li); });
      box.append(el('details',{open:shown},el('summary',{text:l.notes.length+(l.notes.length===1?' note':' notes')}),ul)); }
    const med=l.media||[], vd=vids(l), lp=loosePhotos(l), np=med.length-vd.length, plural=(n,w)=>n+' '+w+(n===1?'':'s');
    if((NATIVE&&!l.imp)||med.length){ const row=el('div',{class:'row',style:'margin-top:8px;align-items:center'});
      if(NATIVE&&!l.imp){ const fb=el('button',{class:'btn sm',type:'button'},l.mscan?'Look again for photos':'Find photos and video');
        fb.addEventListener('click',()=>{ fb.disabled=true; fb.textContent='Looking…'; scanMedia(l,true).then(m=>{ banner(m.length?'Found '+plural(m.filter(x=>x.k==='i').length,'photo')+' and '+plural(vids(l).length,'video')+' from this walk.':'No photos or videos from this walk were found on the phone.',false,6000); },
          e=>{ banner((e&&e.message)||'The phone\'s photos could not be read.',true,10000); renderLog(); }); }); row.append(fb); }
      row.append(el('span',{class:'snote',text:med.length?plural(np,'photo')+' · '+plural(vd.length,'video'):(l.mscan?'None found for this walk.':'')})); box.append(row);
      if(NATIVE&&l.macc==='some') box.append(el('p',{class:'snote',style:'margin-top:6px'},'Android is only letting the Atlas see photos you picked by hand, so some may be missing. ',el('button',{class:'btn sm',type:'button',onclick:()=>AT.call('appSettings')},'Open permissions'),' and set Photos and videos to "Allow all".')); }
    if(vd.length){ const ul=el('ul',{class:'lognotes'}); vd.forEach((m,i)=>{ const li=el('li',{role:'button',tabindex:'0'},el('span',{class:'num vn',text:'\u25B6'+(i+1)}),el('span',{class:'mono',text:hms(m.t-l.t0)}),el('span',{class:'nx',text:hms(m.d)+' long · '+m.n})); li.addEventListener('click',()=>goMedia(l,m)); ul.append(li); });
      box.append(el('details',{open:shown},el('summary',{text:plural(vd.length,'video')+' (time shown is where each starts in the log)'}),ul)); }
    if(lp.length) box.append(el('details',{open:shown},el('summary',{text:plural(lp.length,'photo')+' not attached to a note'}),mediaStrip(l,lp)));
    if(kitOpen===l.id&&ek) box.append(kitPanel(l,fn));
    v.append(box); });
}
function resumeLog(){
  if(NATIVE){ AT.call('status').then(st=>{
      let l=U.rec?logById(U.rec):null;
      if(st.recording&&st.logId&&(!l||l.id!==st.logId)){ /* the phone is recording a log this page has no record of: adopt it */
        l=logById(st.logId); if(!Array.isArray(U.logs)) U.logs=[];
        if(!l){ l={id:st.logId,name:'Field log · recovered',site:null,t0:Math.round((st.started||Date.now())/1000),t1:null,pts:[],notes:[],nat:0}; U.logs.unshift(l); }
        U.rec=l.id; saveNow(); }
      if(!l){ if(U.rec){ delete U.rec; saveNow(); } return; }
      rec=l; drawRec(); syncRec(); nmEnsure(true); nmPush(true);
      if(st.recording&&st.logId===l.id){ const go=()=>{ natSync().then(()=>{ drawRec(); syncRec(); if(view==='log') renderLog(); }); natWatch(); };
        if(st.running) go(); else AT.call('start',{logId:l.id,title:l.name}).then(go,go);   /* Android had stopped the recorder: start it again in the same log */
        setTimeout(()=>banner(st.running?'Your field log is still recording.':'Android had paused the recording. It is running again in the same log.',!st.running,7000),1200); }
      else natSync().then(()=>{ l.t1=l.pts.length?l.pts[l.pts.length-1][2]:l.t0; rec=null; delete U.rec; saveNow(); clearRec(); syncRec(); if(view==='log') renderLog(); });
    }).catch(()=>{}); return; }
  if(!U.rec) return; const l=logById(U.rec); if(!l){ delete U.rec; return; }
  const lastT=l.pts.length?l.pts[l.pts.length-1][2]:l.t0;
  if(map&&navigator.geolocation&&Date.now()/1000-lastT<1800){ rec=l; locate(); keepAwake(); drawRec(); syncRec(); setTimeout(()=>banner('Picked your field log back up where it stopped.',false,6000),1200); }
  else { l.t1=lastT; delete U.rec; saveNow(); } }

/* a double tap on a pin: to street level, or one step closer when already there; on a numbered disc: at least the usual steps, toward the disc */
const DBLZ=17;
function dblPin(ll){ map.setView(ll,Math.min(map.getMaxZoom(),Math.max(DBLZ,map.getZoom()+1))); }
/* The first tap of a double tap on a disc has already begun its own zoom (a single tap opens the group), so the steps are
   counted from where the map stood before that tap; otherwise the result would turn on how fast the two taps came. */
let dblFrom={t:0,z:0};
function dblGroup(b,ll){ const n=Math.max(1,Math.min(4,+pref('dbl')||3)), z0=Date.now()-dblFrom.t<800?dblFrom.z:map.getZoom(), fit=map.getBoundsZoom(b.pad(0.25));      /* a tight group: until its pins fill the view; a loose one: the usual steps, toward the disc */
  const go=()=>{ if(fit>=z0+n) map.fitBounds(b.pad(0.25),{maxZoom:DBLZ}); else map.setView(ll,Math.min(map.getMaxZoom(),z0+n)); };
  if(map._animatingZoom) map.once('zoomend',()=>setTimeout(go,0)); else go(); }      /* the first tap's zoom is still running: a view set now would be undone when it lands */
/* markers */
const STARD='M12.00,1.60 L14.76,8.80 L22.46,9.20 L16.47,14.05 L18.47,21.50 L12.00,17.30 L5.53,21.50 L7.53,14.05 L1.54,9.20 L9.24,8.80Z';
function pinIcon(s,far,dx,dy){      /* far: a favourite while the numbered discs are showing, drawn small; dx,dy: pixels it is pushed aside, off a disc */
  const star=s.st==='standing'&&!s.mine;      /* a place of the reader's own stays a diamond: .pin.mine */
  const c=['pin']; if(HOLLOW[s.st]) c.push('hollow'); if(star) c.push('sq'); if(s.now) c.push('now'); if(s.mine) c.push('mine');
  const my=U.status[s.id]; if(my) c.push('my-'+my); if(isFav(s.id)) c.push('fav'); if(far) c.push('far'); if(sel&&sel.id===s.id) c.push('sel');
  const anc=[11-(dx||0),11-(dy||0)];
  const col=(CAT[s.cat]||CAT.landmark)[1];
  /* a standing place is a star (an outline drawn under the fill, so it reads on any aerial); the rest are round */
  if(star) return L.divIcon({className:'pinwrap',html:'<svg class="'+c.join(' ')+'" viewBox="0 0 24 24" style="--c:'+col+'">'+(s.now?'<path class="p" d="'+STARD+'"/>':'')+'<path class="o" d="'+STARD+'"/><path class="f" d="'+STARD+'"/></svg>',iconSize:[22,22],iconAnchor:anc});      /* .p is the "changing now" pulse */
  return L.divIcon({className:'pinwrap',html:'<span class="'+c.join(' ')+'" style="--c:'+col+'"></span>',iconSize:[22,22],iconAnchor:anc});
}
/* Zoomed out to town level or wider, pins that would sit on top of each other are replaced by one numbered disc.
   A cell of the screen with four or more pins becomes a disc; the selected place always keeps its own pin. */
const CLUSZ=9, HEATZ=9, CLUSPX=58, CLUSMIN=4;      /* HEATZ was 8 for a day (pins from zoom 9): round Albany that put 1,350 pins on the map and a pinch crawled, so the owner had it put back (November 22, 2026) */
const clusSize=n=>{ const st=n<10?0:n<30?1:n<100?2:n<300?3:4; return [st,[30,36,42,46,52][st]]; };      /* a disc's colour step and width by its count */
function clusterPlan(show){ if(!pref('cluster')||map.getZoom()>(pref('heat')?HEATZ:CLUSZ)) return null;      /* the heat and the discs give way to pins at the same step, zoom 10 */
  if(pref('heat')) return heatPlan(show);
  const z=map.getZoom(), cells=new Map();
  sites().forEach(s=>{ if(!show.has(s.id)||(sel&&sel.id===s.id)||isFav(s.id)) return; const p=pos(s), q=map.project([p.lat,p.lon],z), k=Math.floor(q.x/CLUSPX)+','+Math.floor(q.y/CLUSPX);
    let c=cells.get(k); if(!c){ c={ids:[],la:0,lo:0,a:90,b:-90,c:180,d:-180}; cells.set(k,c); }
    c.ids.push(s.id); c.la+=p.lat; c.lo+=p.lon; if(p.lat<c.a)c.a=p.lat; if(p.lat>c.b)c.b=p.lat; if(p.lon<c.c)c.c=p.lon; if(p.lon>c.d)c.d=p.lon; });
  const single=new Set(); let groups=[]; cells.forEach(c=>{ if(c.ids.length<CLUSMIN) c.ids.forEach(i=>single.add(i)); else groups.push(c); });
  /* A disc is drawn at the middle of its places, not of its square, so two neighbouring squares could put their discs on top of each
     other: on the opening map New York's 1,830 hid New England's 917. Discs that would overlap are joined, the larger taking the
     smaller, until none do. A few hundred discs at most, so the pairs are cheap to try. */
  const where=g=>{ const n=g.ids.length, q=map.project([g.la/n,g.lo/n],z); g.x=q.x; g.y=q.y; g.rad=clusSize(n)[1]/2; };
  groups.forEach(where);
  for(let pass=0;pass<5;pass++){ let joined=false; groups.sort((a,b)=>b.ids.length-a.ids.length);
    for(let i=0;i<groups.length;i++){ const a=groups[i]; if(!a) continue;
      for(let j=i+1;j<groups.length;j++){ const b=groups[j]; if(!b||Math.hypot(a.x-b.x,a.y-b.y)>=(a.rad+b.rad)*0.94) continue;
        a.ids=a.ids.concat(b.ids); a.la+=b.la; a.lo+=b.lo; if(b.a<a.a)a.a=b.a; if(b.b>a.b)a.b=b.b; if(b.c<a.c)a.c=b.c; if(b.d>a.d)a.d=b.d; where(a); groups[j]=null; joined=true; } }
    groups=groups.filter(Boolean); if(!joined) break; }
  if(sel) single.add(sel.id); (U.fav||[]).forEach(i=>{ if(show.has(i)) single.add(i); });      /* a favourite stands alone at every zoom */
  return {single:single,groups:groups}; }
/* The heat map, a trial (the owner, November 22, 2026: the discs make it "a little harder to find the clusters of pins", and he asked for
   "a smooth thing by colour"). Zoomed out, the places are counted in squares of HEATPX screen pixels, as the discs count them in
   squares of CLUSPX, and each square is painted as a soft blob whose strength goes with the logarithm of its count; the blobs run
   together, and the strength is turned into colour by the same steps as the discs, blue for a few to red for many. It is ONE
   picture laid on the map (an image overlay a screen and a half wide, so a drag shows no edge and a zoom animates it), made again
   when the zoom, the filters or the ground change. A favourite and the chosen place keep their pins. A tap on colour says about
   how many places are there; the map's own double-tap goes closer. */
const HEATPX=16; let heatLayer=null, heatSig='', heatNow=null;
function heatPlan(show){
  const z=map.getZoom(), cells=new Map(), single=new Set(); let total=0, max=0, hot=null;
  sites().forEach(s=>{ if(!show.has(s.id)) return; if((sel&&sel.id===s.id)||isFav(s.id)){ single.add(s.id); return; }
    const p=pos(s), q=map.project([p.lat,p.lon],z), k=Math.floor(q.x/HEATPX)+','+Math.floor(q.y/HEATPX);
    let c=cells.get(k); if(!c){ c={n:0,x:0,y:0}; cells.set(k,c); } c.n++; c.x+=q.x; c.y+=q.y; total++; });
  cells.forEach(c=>{ if(c.n>max){ max=c.n; hot=c; } });
  /* what counts as "full": not the one fullest square (Albany's, which left the rest of the continent a grey wash) but the count that
     nine squares in ten fall under, and never less than three */
  const ns=[]; cells.forEach(c=>ns.push(c.n)); ns.sort((a,b)=>a-b); const ref=Math.max(3,ns.length?ns[Math.floor(ns.length*0.9)]:3);
  return {single:single,groups:[],heat:{z:z,cells:cells,total:total,max:max,ref:ref,hot:hot?map.unproject([hot.x/hot.n,hot.y/hot.n],z):null}}; }
const HEATSTOPS=[[0,[58,110,200]],[0.3,[40,170,170]],[0.55,[240,200,60]],[0.78,[240,130,40]],[1,[205,40,30]]];      /* blue for a few, through teal, yellow and orange, to red for many: the discs' purple and rose went muddy over the map */
let heatPal=null;
function heatPalette(){ if(heatPal) return heatPal; heatPal=new Uint8ClampedArray(256*3);
  for(let i=0;i<256;i++){ const t=i/255; let a=HEATSTOPS[0], b=HEATSTOPS[HEATSTOPS.length-1]; for(let j=1;j<HEATSTOPS.length;j++) if(t<=HEATSTOPS[j][0]){ a=HEATSTOPS[j-1]; b=HEATSTOPS[j]; break; }
    const u=b[0]===a[0]?0:(t-a[0])/(b[0]-a[0]); for(let k=0;k<3;k++) heatPal[i*3+k]=a[1][k]+(b[1][k]-a[1][k])*u; }
  return heatPal; }
function drawHeat(h){
  if(!h||!h.total){ if(heatLayer){ map.removeLayer(heatLayer); heatLayer=null; } heatSig=''; heatNow=null; return; }
  heatNow=h; const vb=map.getBounds(), sig=h.z+'|'+h.cells.size+'|'+h.total+'|'+h.max+'|'+h.ref;
  if(heatLayer&&sig===heatSig&&heatLayer.getBounds().contains(vb)) return;      /* the same heat, and the view is still inside the picture */
  if(!map.getPane('heat')){ const pn=map.createPane('heat'); pn.style.zIndex=370; pn.style.pointerEvents='none'; }      /* under the pane the old lines, the lead dots and the old town centres are drawn in (380): over them it tinted the towns' discs and they looked odd (the owner, November 22, 2026) */
  const B=vb.pad(0.75), nw=map.project(B.getNorthWest(),h.z), se=map.project(B.getSouthEast(),h.z), S=0.5;      /* half size: it is a blur, and a quarter of the pixels to colour */
  const W=Math.max(8,Math.round((se.x-nw.x)*S)), H=Math.max(8,Math.round((se.y-nw.y)*S)), cv=document.createElement('canvas'); cv.width=W; cv.height=H;
  const g=cv.getContext('2d'), R=HEATPX*1.45*S;
  h.cells.forEach(c=>{ const x=(c.x/c.n-nw.x)*S, y=(c.y/c.n-nw.y)*S; if(x<-R||y<-R||x>W+R||y>H+R) return;
    /* strength by the count's share of the fullest square, lifted so that one place still shows and a few hundred are not all the same red.
       Neighbouring blobs lie over each other and add up to about twice one blob's middle, so each is painted at half strength */
    const t=0.14+0.86*Math.pow(Math.min(1,c.n/h.ref),0.6), gr=g.createRadialGradient(x,y,0,x,y,R); gr.addColorStop(0,'rgba(0,0,0,'+(0.5*t).toFixed(3)+')'); gr.addColorStop(0.55,'rgba(0,0,0,'+(0.2*t).toFixed(3)+')'); gr.addColorStop(1,'rgba(0,0,0,0)');
    g.fillStyle=gr; g.fillRect(x-R,y-R,R*2,R*2); });
  const im=g.getImageData(0,0,W,H), d=im.data, pal=heatPalette();
  for(let i=0;i<d.length;i+=4){ const a=d[i+3]; if(!a) continue; const k=a*3; d[i]=pal[k]; d[i+1]=pal[k+1]; d[i+2]=pal[k+2]; d[i+3]=a<16?a*8:Math.min(215,128+a*0.4); }      /* a soft edge, then see-through enough to read the map under it, more so where places are few */
  g.putImageData(im,0,0);
  const url=cv.toDataURL('image/png');
  if(heatLayer){ heatLayer.setUrl(url); heatLayer.setBounds(B); } else heatLayer=L.imageOverlay(url,B,{pane:'heat',interactive:false,className:'heatimg'}).addTo(map);
  heatSig=sig; }
/* a tap on the heat: about how many places are within a thumb's width of it */
function heatTap(ll){ const h=heatNow; if(!h||map.getZoom()!==h.z) return false; const q=map.project(ll,h.z), cx=Math.floor(q.x/HEATPX), cy=Math.floor(q.y/HEATPX); let n=0;
  for(let i=-1;i<=1;i++) for(let j=-1;j<=1;j++){ const c=h.cells.get((cx+i)+','+(cy+j)); if(c) n+=c.n; }
  if(!n) return false; banner((n===1?'One place':n<10?n+' places':'About '+(n<100?Math.round(n/5)*5:Math.round(n/10)*10)+' places')+' around here. Double-tap to zoom in.',false,3500); return true; }
try{ window.__atlasHeat=()=>heatNow&&heatLayer?{cells:heatNow.cells.size,total:heatNow.total,max:heatNow.max,hot:heatNow.hot?[heatNow.hot.lat,heatNow.hot.lng]:null}:null; }catch(e){}
/* Pins are on the map only in and around the view, a screen's width beyond each edge. With every place on the map,
   each zoom step moved 800 pins and took a mid-range phone about 80 ms; it took 16 ms with none. A pin that has been made
   is kept (pinPool) and put back when its ground comes into view again. Called when the map stops moving, and whenever
   the list, the filters or the chosen place change. */
const pinPool=new Map(); let clusSig='', pinGen=0; const PINFIRST=80, PINLOT=30;
/* Two fingers on the map (the setting pinchStand, on unless switched off; the owner, November 22, 2026). A one-finger drag
   slides the whole map as one sheet. A pinch does not: at every frame Leaflet moves each pin on the map separately, and round
   Albany that is 800 pins, so the map crawled while two fingers were down. The heat map, which is one picture stretched,
   pinched smoothly on his phone. So for the length of a pinch the place pins are hidden and one picture of them, drawn here,
   is stretched with the map in their place; when the fingers lift it is taken away and the pins, which Leaflet has kept up
   to date all the while, are shown again. Tried as a trial on his phone and kept: "that completely 100% fixed how it feels".
   The pins grow and shrink with the map during the pinch. A picture stretched far goes soft (he saw it on the stars after a
   long pinch), and one shrunk far no longer reaches the edges, so pinchPaint() draws it again whenever it has been stretched
   past 1.4 or shrunk under 0.7, at the size the pins have by then (mag): nothing jumps, it is only sharp again.
   pinDraw() draws one pin as app.css does (.pin, .zfar .pin, .pin.sq, .hollow, .mine, .fav, .sel, .my-ok, .my-asked, the
   faded .my-filmed and .my-skip); a pulsing pin (.now) is drawn with a steady ring, as it is for a reader who has asked for
   less motion. A change to how a pin looks in app.css needs the same change here. */
let pinchSt=null, pinStar=null;
function pinDraw(g,s,x,y,far,ring,accent){
  const col=(CAT[s.cat]||CAT.landmark)[1], star=s.st==='standing'&&!s.mine, fav=isFav(s.id), my=U.status[s.id], chosen=!!sel&&sel.id===s.id;
  const halo=my==='ok'?[26,150,65]:my==='asked'?[224,138,0]:null, disc=(r,c)=>{ g.beginPath(); g.arc(x,y,r,0,6.2832); g.fillStyle=c; g.fill(); };
  if(star){ const k=(far?15:22)/24*(fav?1.25:1); g.save(); g.translate(x-12*k,y-12*k); g.scale(k,k); g.lineJoin='round'; if(!pinStar) pinStar=new Path2D(STARD);
    const line=(w,c)=>{ g.lineWidth=w; g.strokeStyle=c; g.stroke(pinStar); }, ow=fav?8:halo?7:5;
    if(chosen) line(ow+6/k,accent);
    if(s.now) line(9,'rgba(240,120,30,.6)');
    if(fav) line(8+2.4/k,'rgba(0,0,0,.5)');      /* the soft dark edge the page gives a favourite star */
    line(ow,fav?'#fff':halo?'rgba('+halo+',.9)':'rgba(0,0,0,.65)'); g.fillStyle=col; g.fill(pinStar); line(2,ring); g.restore(); }
  else { const r=far?5:8;
    if(chosen){ g.beginPath(); g.arc(x,y,r+4.5,0,6.2832); g.lineWidth=3; g.strokeStyle=accent; g.stroke(); }
    if(s.mine){ g.save(); g.translate(x,y); g.rotate(0.7854); const b=far?1.5:2; g.fillStyle='rgba(0,0,0,.6)'; g.fillRect(-r-1,-r-1,2*r+2,2*r+2); g.fillStyle=ring; g.fillRect(-r,-r,2*r,2*r); g.fillStyle=col; g.fillRect(-r+b,-r+b,2*(r-b),2*(r-b)); g.restore(); }
    else { const hol=!!HOLLOW[s.st], b=hol?(far?2.5:3.5):(far?1.5:2);
      if(halo){ disc(r+4,'rgba('+halo+',.75)'); disc(r+1,'rgba(0,0,0,.6)'); }
      else if(fav){ disc(r+4.5,'rgba(0,0,0,.8)'); disc(r+3,'#fff'); }
      else { if(s.now) disc(r+4,'rgba(240,120,30,.6)'); disc(r+1,'rgba(0,0,0,.6)'); }
      disc(r,hol?col:ring); disc(r-b,hol?'#fff':col); } }
}
/* the picture for the map as it stands now, with the pins drawn mag times their size; it takes the place of any picture before it */
function pinchPaint(mag){
  const css=getComputedStyle(map.getContainer()), ring=(css.getPropertyValue('--pinring')||'').trim()||'#fff', accent=(css.getPropertyValue('--accent')||'').trim()||'#2563eb', far=map.getContainer().classList.contains('zfar');
  const vb=map.getBounds().pad(0.35), nwLL=vb.getNorthWest(), nw=map.latLngToLayerPoint(nwLL), se=map.latLngToLayerPoint(vb.getSouthEast()), w=Math.round(se.x-nw.x), h=Math.round(se.y-nw.y), k=Math.min(2.5,window.devicePixelRatio||1), edge=20*mag;
  const cv=document.createElement('canvas'); cv.className='pinstand leaflet-zoom-animated'; cv.width=Math.round(w*k); cv.height=Math.round(h*k); cv.style.width=w+'px'; cv.style.height=h+'px';
  const g=cv.getContext('2d'); g.scale(k,k); const list=[];
  markers.forEach((m,id)=>{ const t=byId(id); if(!t) return; const q=map.latLngToLayerPoint(m.getLatLng()), x=q.x-nw.x, y=q.y-nw.y; if(x<-edge||y<-edge||x>w+edge||y>h+edge) return;
    list.push([(sel&&sel.id===id?2e6:isFav(id)?1e6:t.cat==='landmark'?-1e6:0)+y,t,x,y]); });      /* the order the pins are stacked in: down the screen, favourites and the chosen place on top */
  /* a faded pin (one marked filmed or skipped) is drawn whole on a scrap first and laid down faint: drawn faint part by part, its ring showed through its middle */
  const T=Math.ceil(48*mag*k), scrap=document.createElement('canvas'), sg=scrap.getContext('2d'); scrap.width=scrap.height=T;
  list.sort((a,b)=>a[0]-b[0]).forEach(a=>{ const my=U.status[a[1].id];
    if(my==='filmed'||my==='skip'){ sg.setTransform(1,0,0,1,0,0); sg.clearRect(0,0,T,T); sg.setTransform(k*mag,0,0,k*mag,T/2,T/2); pinDraw(sg,a[1],0,0,far,ring,accent); g.globalAlpha=0.45; g.drawImage(scrap,a[2]-T/k/2,a[3]-T/k/2,T/k,T/k); g.globalAlpha=1; return; }
    g.save(); g.translate(a[2],a[3]); g.scale(mag,mag); pinDraw(g,a[1],0,0,far,ring,accent); g.restore(); });
  let pane=map.getPane('pinstand'); if(!pane){ pane=map.createPane('pinstand'); pane.style.zIndex=600; pane.style.pointerEvents='none'; }
  pane.appendChild(cv); L.DomUtil.setTransform(cv,nw,1); if(pinchSt) pinchSt.cv.remove(); else map.getPane('markerPane').classList.add('pinch-on');
  pinchSt={cv:cv,nwLL:nwLL,z0:map.getZoom(),w:w,h:h,mag:mag};
}
function pinchFrame(e){ if(!e||!e.pinch) return;
  if(!pinchSt){ if(!pref('pinchStand')||!markers.size) return; pinchPaint(1); return; }
  const k=map.getZoomScale(map.getZoom(),pinchSt.z0); if(k>1.4||k<0.7){ pinchPaint(pinchSt.mag*k); return; }
  L.DomUtil.setTransform(pinchSt.cv,map.latLngToLayerPoint(pinchSt.nwLL),k); }
function pinchAnim(e){ if(pinchSt) L.DomUtil.setTransform(pinchSt.cv,map._latLngToNewLayerPoint(pinchSt.nwLL,e.zoom,e.center),map.getZoomScale(e.zoom,pinchSt.z0)); }      /* the fingers lift: Leaflet glides to a whole zoom step, and the picture glides with it */
function pinchEnd(){ if(!pinchSt) return; pinchSt.cv.remove(); pinchSt=null; map.getPane('markerPane').classList.remove('pinch-on'); }
try{ window.__atlasPinch=()=>pinchSt?{nw:[pinchSt.nwLL.lat,pinchSt.nwLL.lng],z0:pinchSt.z0,w:pinchSt.w,h:pinchSt.h,mag:pinchSt.mag}:null; }catch(e){}
function syncMarkers(){
  if(!map) return;
  const show=new Set(visible.map(s=>s.id)); if(sel) show.add(sel.id);
  const plan=clusterPlan(show), vb=map.getBounds().pad(1), S=vb.getSouth(), N=vb.getNorth(), W=vb.getWest(), E=vb.getEast();
  const all=sites(), want=new Map();
  all.forEach(s=>{ if(!show.has(s.id)||(plan&&!plan.single.has(s.id))) return; const p=pos(s);
    if((sel&&sel.id===s.id)||(p.lat>=S&&p.lat<=N&&p.lon>=W&&p.lon<=E)) want.set(s.id,s); });
  /* a pin no longer wanted comes off now if it is in or near the view (a filter, a place folded into a disc), and a lot a frame if it is
     off beyond the edges, where nobody sees it go: a zoom step in left some 500 of them to take off at once */
  const vnow=map.getBounds().pad(0.3), going=[];
  markers.forEach((m,id)=>{ if(want.has(id)) return; if(vnow.contains(m.getLatLng())){ map.removeLayer(m); markers.delete(id); } else going.push(id); });
  if(pinPool.size>all.length){ const ids=new Set(all.map(s=>s.id)); pinPool.forEach((m,id)=>{ if(!ids.has(id)) pinPool.delete(id); }); }      /* a place of your own that was deleted */
  /* While the numbered discs are showing, a favourite still has its own pin, but smaller, and a pin that would sit on a disc is
     drawn on its rim, over it: in the middle it hid the number, and pushed clear of the disc it was not plain where the place
     was (the owner, November 21, 2026). The discs on the screen: */
  const discs=plan&&plan.groups.length?plan.groups.map(c=>{ const n=c.ids.length, q=map.latLngToLayerPoint([c.la/n,c.lo/n]); return {x:q.x,y:q.y,r:clusSize(n)[1]/2}; }):null;
  const put=s=>{
    const p=pos(s), far=!!plan&&!plan.heat&&isFav(s.id)&&!(sel&&sel.id===s.id); let dx=0, dy=0;      /* smaller beside the discs' numbers; over the heat there is no number to hide, so full size */
    if(discs&&!(sel&&sel.id===s.id)){ const q=map.latLngToLayerPoint([p.lat,p.lon]); for(const g of discs){ const ex=q.x+dx-g.x, ey=q.y+dy-g.y, d=Math.hypot(ex,ey), need=g.r+(far?2:4);      /* its middle goes just outside the rim, so it sits on the disc's edge like a badge, on the side its place is on, clear of the number. Any pin that stands alone, favourite or not */
        if(d<need){ const ux=d<1?0.7071:ex/d, uy=d<1?-0.7071:ey/d; dx+=Math.round(ux*(need-d)); dy+=Math.round(uy*(need-d)); } } }
    const ic=pinIcon(s,far,dx,dy), sig=ic.options.html+(dx||dy?'|'+dx+','+dy:''); let m=pinPool.get(s.id);
    if(!m){ m=L.marker([p.lat,p.lon],{icon:ic,keyboard:false,riseOnHover:true}); m._sig=sig;
      const tip=el('span',{text:s.name}); m.bindTooltip(tip,{direction:'top',offset:[0,-9]});
      m.on('click',()=>{ if(adding||pickingHome) return; select(byId(s.id)||s,false); });
      m.on('dblclick',()=>{ if(adding||pickingHome) return; dblPin(m.getLatLng()); });
      m.on('dragend',()=>{ const q=m.getLatLng(); U.moved[s.id]=[+q.lat.toFixed(6),+q.lng.toFixed(6)]; save(); m.dragging.disable(); banner('Pin moved. It is saved in this browser.',false,3500); refresh(); });
      pinPool.set(s.id,m); }
    else { const q=m.getLatLng(); if(q.lat!==p.lat||q.lng!==p.lon) m.setLatLng([p.lat,p.lon]); if(m._sig!==sig){ m.setIcon(ic); m._sig=sig; } }      /* an icon is rebuilt only when it would look different */
    if(!markers.has(s.id)){ m.addTo(map); markers.set(s.id,m); }
    const zo=sel&&sel.id===s.id?1000:isFav(s.id)?600:(dx||dy)?300:(s.cat==='landmark'?-200:0);      /* a pin moved to a disc's rim is drawn over the disc */ if(m._zo!==zo){ m._zo=zo; m.setZIndexOffset(zo); }
  };
  /* New pins go on from the middle of the view outwards, a first lot now and the rest a lot a frame, so the page is never held while
     hundreds are made. All at once, the step from heat or discs to pins put some 800 pins on the map in one go round Albany
     (every place within a screen of the view, there so that a drag shows pins) and held a mid-range phone for about a second:
     the lag the owner felt. A pin already on the map is only brought up to date, which is cheap, so that is done now. A later
     call drops whatever is still waiting. */
  const gen=++pinGen, mid=map.getCenter(), kx=Math.cos(mid.lat*Math.PI/180), later=[];
  want.forEach(s=>{ if((sel&&sel.id===s.id)||markers.has(s.id)) put(s); else { const p=pos(s); later.push([Math.abs(p.lat-mid.lat)+Math.abs(p.lon-mid.lng)*kx,s]); } });
  if(later.length){ later.sort((a,b)=>a[0]-b[0]); let i=0;
    const lot=n=>{ const end=Math.min(later.length,i+n); for(;i<end;i++) put(later[i][1]); };
    const more=()=>{ if(gen!==pinGen) return; lot(PINLOT); if(i<later.length) requestAnimationFrame(more); };
    lot(PINFIRST); if(i<later.length) requestAnimationFrame(more); }
  if(going.length){ let j=0; const off=()=>{ if(gen!==pinGen) return; const end=Math.min(going.length,j+PINLOT*2); for(;j<end;j++){ const m=markers.get(going[j]); if(m){ map.removeLayer(m); markers.delete(going[j]); } } if(j<going.length) requestAnimationFrame(off); }; requestAnimationFrame(off); }
  drawHeat(plan&&plan.heat||null);
  /* the grouped pins are made again only when the groups change, not each time the map is nudged */
  const sig=plan?map.getZoom()+'|'+plan.groups.map(c=>c.ids.length+':'+c.la.toFixed(3)+':'+c.lo.toFixed(3)).join():'';
  if(sig===clusSig&&(!sig||clusLayer)) return; clusSig=sig;
  if(clusLayer){ map.removeLayer(clusLayer); clusLayer=null; }
  if(plan&&plan.groups.length){ clusLayer=L.layerGroup();
    plan.groups.forEach(c=>{ const n=c.ids.length, cs=clusSize(n), st=cs[0], d=cs[1];      /* colour and size by count, cool to hot (app.css, .clus.c0 to .c4) */
      const m=L.marker([c.la/n,c.lo/n],{keyboard:false,zIndexOffset:-100,icon:L.divIcon({className:'clus c'+st,html:String(n),iconSize:[d,d],iconAnchor:[d/2,d/2]})});
      m.bindTooltip(n+' places. Tap to zoom in',{direction:'top',offset:[0,-d/2]});
      m.on('click',()=>{ if(adding||pickingHome) return; const z0=map.getZoom(), B=L.latLngBounds([c.a,c.c],[c.b,c.d]).pad(0.25); dblFrom={t:Date.now(),z:z0};
        /* a tap always goes closer. A disc that took in its neighbours can cover ground as wide as the view, and fitting that would not move the map at all */
        if(map.getBoundsZoom(B)>z0) map.fitBounds(B,{maxZoom:Math.max(z0+2,CLUSZ+1)}); else map.setView(m.getLatLng(),z0+1); });
      m.on('dblclick',()=>{ if(adding||pickingHome) return; dblGroup(L.latLngBounds([c.a,c.c],[c.b,c.d]),m.getLatLng()); });
      m.addTo(clusLayer); });
    clusLayer.addTo(map); }
}
function drawHome(){ if(!map) return; if(homeMarker){ map.removeLayer(homeMarker); homeMarker=null; } if(!homePicked()) return; const H=homeObj();
  homeMarker=L.marker([H.lat,H.lon],{interactive:false,keyboard:false,zIndexOffset:-500,icon:L.divIcon({className:'pinwrap',html:'<span class="homepin">H</span>',iconSize:[24,24],iconAnchor:[12,12]})}).addTo(map); }
function drawSel(){
  if(!map) return; selShapes.forEach(x=>map.removeLayer(x)); selShapes=[];
  if(!sel) return; const p=pos(sel), acc=getComputedStyle(document.documentElement).getPropertyValue('--accent').trim()||'#a33a24';
  selShapes.push(L.circle([p.lat,p.lon],{radius:(PREC[sel.prec]||PREC.site)[2],color:acc,weight:1.5,dashArray:'5 5',fill:false,interactive:false}).addTo(map));
  if(sel.th){ selShapes.push(L.polyline([[sel.th[0],sel.th[1]],[p.lat,p.lon]],{color:'#1f5fbf',weight:2,dashArray:'2 6',interactive:false}).addTo(map));
    const tm=L.marker([sel.th[0],sel.th[1]],{keyboard:false,icon:L.divIcon({className:'pinwrap',html:'<span class="thpin">P</span>',iconSize:[20,20],iconAnchor:[10,10]})}).addTo(map);
    tm.bindTooltip(el('span',{text:'Park: '+(sel.thn||'trailhead')}),{direction:'top',offset:[0,-8]}); selShapes.push(tm); }
}
function showHist(){
  if(!map) return; if(histLayer){ map.removeLayer(histLayer); histLayer=null; }
  if(!sel||!U.ui.hist||!sel.tm) return; const who=sel, b=sel.tm.b;
  topoSrc(who).then(src=>{ if(sel!==who||!U.ui.hist) return;
    if(!src){ if(AT) banner(navigator.onLine===false?'This place\'s old map is not on the phone yet. It needs a signal the first time.':'The old map for this place could not be loaded.',true,6000); return; }
    if(histLayer) map.removeLayer(histLayer);
    histLayer=L.imageOverlay(src,[[b[0],b[1]],[b[2],b[3]]],{pane:'hist',opacity:U.ui.histOp,interactive:false}).addTo(map); });
}
function onMapClick(e){
  if(spotting){ if(finePointer()) spotDrop(e.latlng.lat,e.latlng.lng); return; }      /* on a phone only the Drop button drops: a slip of the thumb is not a spot */
  if(asking){ setAsking(false); whoPopup({lat:e.latlng.lat,lon:e.latlng.lng}); return; }
  if(pickingHome){ pickingHome=false; stage.classList.remove('adding'); $('#addbar').hidden=true; setSpot(e.latlng.lat,e.latlng.lng); return; }
  if(adding){ placeAt(e.latlng.lat,e.latlng.lng); return; }
  if(pref('heat')&&pref('cluster')&&map.getZoom()<=HEATZ) heatTap(e.latlng);
}
function scoutLinks(p,town){
  const c=p.lat.toFixed(5)+','+p.lon.toFixed(5);
  return [
    ['Google Maps','https://www.google.com/maps/search/?api=1&query='+c],
    ['Google satellite','https://www.google.com/maps/@?api=1&map_action=map&center='+c+'&zoom=18&basemap=satellite'],
    ['Street View','https://www.google.com/maps/@?api=1&map_action=pano&viewpoint='+c],
    ['Google Earth 3D','https://earth.google.com/web/@'+c+',0a,700d,35y,0h,45t,0r'],
    ['Old air photos','https://www.historicaerials.com/location/'+p.lat.toFixed(5)+'/'+p.lon.toFixed(5)+'/1952/17'],
    ['Old topo maps','https://ngmdb.usgs.gov/topoview/viewer/#15/'+p.lat.toFixed(4)+'/'+p.lon.toFixed(4)],
    ['OpenHistoricalMap','https://www.openhistoricalmap.org/#map=16/'+p.lat.toFixed(5)+'/'+p.lon.toFixed(5)],
    town?['Sanborn fire maps','https://www.loc.gov/collections/sanborn-maps/?q='+encodeURIComponent(town+' New York')]:null
  ].filter(Boolean);
}
/* The box a long press or a right click opens: a small one (the owner, November 23, 2026). The coordinates are one small line that
   copies; Add and Send side by side; the three maps he uses in one row; the rest under "More", which a desktop opens by itself.
   Which of Add and Send is which is said in each button's own hint and no longer in a paragraph. "Measure drive times from here"
   is gone from here: the start place is chosen on the Places tab. On a map too short to hold the box above the point (the map
   dragged down to its strip) it sits flat against the top of the map instead of becoming a scrolling bubble, with a ring on the spot. */
let ctxFlat=null;
function ctxFlatOff(){ if(!ctxFlat) return; ctxFlat.box.remove(); if(map){ map.removeLayer(ctxFlat.mark); map.off('click popupopen',ctxFlatOff); } ctxFlat=null; }
function ctxClose(){ ctxFlatOff(); if(map) map.closePopup(); }
function onContext(e){
  ctxClose();
  const p={lat:e.latlng.lat,lon:e.latlng.lng}; const box=el('div',{class:'ctx spot'});
  const cb=el('button',{class:'ctx-ll',type:'button',title:'Copy these coordinates','aria-label':'Copy the coordinates '+ll(p)},ll(p)); cb.addEventListener('click',()=>copy(ll(p),cb)); box.append(cb);
  const add=el('button',{class:'btn sm',type:'button',title:'Add a place of your own here. It stays on this device.','aria-label':'Add to my places',onclick:()=>{ ctxClose(); quickAdd({lat:+p.lat.toFixed(6),lon:+p.lon.toFixed(6)}); }},'+ My places');
  const send=spotLink('',p.lat,p.lon,'','Send to Atlas'); send.title='Send this spot to the public Atlas, the map everyone sees. A short form opens with these coordinates filled in; what you send is checked before it goes on.'; send.setAttribute('aria-label','Send this spot to the public Atlas');
  box.append(el('div',{class:'ctx-row two'},add,send));
  const S=scoutLinks(p), by=n=>S.find(l=>l[0]===n), lk=(n,label)=>{ const a=ext(by(n)[1],label||n,'btn sm'); if(label) a.title=n; return a; };
  box.append(el('div',{class:'ctx-row three'},lk('Google Maps'),lk('Street View'),lk('Google Earth 3D','Earth 3D')));
  const more=el('details',{class:'ctxmore'},el('summary',{text:'More'})); more.open=!!(window.matchMedia&&matchMedia('(hover:hover) and (pointer:fine)').matches);
  more.append(el('div',{class:'ctx-row two'},lk('Google satellite'),lk('Old air photos')));
  if(!schematic) more.append(el('button',{class:'btn sm',type:'button',onclick:()=>{ ctxClose(); whoPopup(p); }},'Whose land is it?'));
  box.append(more);
  /* how tall will it be? measured off the page, at the width it will have */
  const probe=el('div',{style:'position:absolute;left:-9999px;top:0;width:252px;font-size:13px'},box); document.body.append(probe); const h=box.offsetHeight; box.remove(); probe.remove();
  const mh=map.getSize().y;
  if(mh<h+62){
    const x=el('button',{class:'ctx-x',type:'button','aria-label':'Close',onclick:ctxClose},'\u00d7'), flat=el('div',{class:'ctxflat'},x,box);
    L.DomEvent.disableClickPropagation(flat); L.DomEvent.disableScrollPropagation(flat); $('#map').append(flat);
    const mark=L.circleMarker(e.latlng,{radius:9,color:'#ff2d95',weight:3,fill:false,interactive:false,className:'ctxmark'}).addTo(map);
    ctxFlat={box:flat,mark}; setTimeout(()=>{ if(ctxFlat&&ctxFlat.box===flat) map.on('click popupopen',ctxFlatOff); },0);      /* a tap on the map, or anything else opening, puts it away */
    return; }
  const pop=L.popup({maxWidth:252,minWidth:252,maxHeight:Math.max(150,mh-40)}).setLatLng(e.latlng).setContent(box).openOn(map);
  more.addEventListener('toggle',()=>pop.update());
}

/* ---------- views ---------- */
let view='list';
function showView(v){ view=v; if(v!=='detail') dropFormPin(); if(v==='list'&&listFrom!==nearFrom()){ if(F.max) refresh(); else renderList(); }      /* the position changed while another tab was open */
  ['list','detail','trip','log','guide','near'].forEach(k=>{ $('#v-'+k).hidden=(k!==v); });
  $('#tab-list').setAttribute('aria-selected',String(v==='list'||v==='detail')); $('#tab-trip').setAttribute('aria-selected',String(v==='trip')); $('#tab-guide').setAttribute('aria-selected',String(v==='guide')); $('#tab-log').setAttribute('aria-selected',String(v==='log')); $('#tab-near').setAttribute('aria-selected',String(v==='near'));
  nmCompass(v==='near'); if(v==='near'){ nmEnsure(true); renderNear(); if(NM.org==='me'&&geo.id===null&&U.last&&map) locate(); }
  if(v==='trip') renderTrip(); if(v==='guide') renderGuide(); if(v==='log') renderLog(); }
function refresh(){ buildFilters(); renderList(); spotCard(); syncMarkers(); $('#trip-n').textContent=U.trip.length; if(view==='trip') renderTrip(); }
function select(s,fly){
  dropFormPin(); sel=s; renderDetail(s); showView('detail'); syncMarkers(); drawSel(); showHist();
  document.querySelectorAll('#list .item.cur').forEach(n=>n.classList.remove('cur'));
  if(map&&fly!==null){ const p=pos(s), z=Math.max(map.getZoom(),s.prec==='area'?14:15); if(fly) map.flyTo([p.lat,p.lon],z,{duration:0.8}); else map.panTo([p.lat,p.lon]); }
  try{ history.replaceState(null,'','#'+s.id); }catch(e){ try{ location.hash=s.id; }catch(x){} }
}
function deselect(){ sel=null; drawSel(); showHist(); syncMarkers(); showView('list'); renderList(); try{ history.replaceState(null,'','#'); }catch(e){} }

/* ---- a photo at the top of a place page ----
   Taken when the page opens from the place's Wikipedia article: the picture Wikipedia itself chose for the article
   (pageimages, free licences only), shown only when the article is about this place (photoFits: coordinates near the
   pin, which also keeps out a person's portrait, and a shared word in the names), and only when the file's page (asked of
   Wikipedia, which answers for Commons files too) gives the photographer and licence for the credit.
   Drawings of maps, seals and flags (an .svg file, or a name that says so) are skipped. Setting: wikiPhotos. */
const PHOTO=new Map();
function wikiTitle(s){ for(const l of s.links||[]){ const u=Array.isArray(l)?l[1]:String(l); const m=/^https?:\/\/en\.(?:m\.)?wikipedia\.org\/wiki\/([^#?]+)/.exec(u||''); if(!m) continue;
    let t; try{ t=decodeURIComponent(m[1]).replace(/_/g,' '); }catch(e){ continue; }
    if(/^(list of|lists of|national register of historic places listings)/i.test(t)||t.includes(':')) continue;   /* a list's picture is of some other place */
    return t; } return null; }
/* the photographer's name out of Commons' Artist field, which is HTML and sometimes a whole banner: parsed with DOMParser,
   which loads none of the images in it; a long banner gives way to its first link to a user page */
/* is the article about this place? Many places link the article on their town, whose picture is a skyline. So the
   article's coordinates must be within 1 km of the pin, and its title must share a word with the place's names that is
   not a word of the town, the state or a common word of building names. */
const PH_COMMON=new Set('the and of at on in new york north south east west upper lower old great little county city town village historic district site former saint street avenue road park building house hall church school mill works company station state national'.split(' '));
const phWords=t=>String(t||'').toLowerCase().normalize('NFD').replace(/[\u0300-\u036f]/g,'').split(/[^a-z0-9]+/).filter(w=>w.length>=3&&!PH_COMMON.has(w));
function photoFits(s,title,co){ if(!co||!isFinite(co.lat)||!isFinite(co.lon)) return false;
  if(L.latLng(s.lat,s.lon).distanceTo([co.lat,co.lon])>1000) return false;
  const all=t=>' '+String(t||'').toLowerCase().normalize('NFD').replace(/[\u0300-\u036f]/g,'').replace(/&/g,' and ').split(/[^a-z0-9]+/).filter(Boolean).join(' ')+' ';
  const tt=all(title.replace(/\s*\(.*\)\s*$/,''));
  if(tt.trim().includes(' ')&&(all(s.name).includes(tt)||all(s.name2).includes(tt))) return true;   /* the whole title is in the name: Altamont station */
  const town=new Set(phWords(s.town)), mine=new Set([...phWords(s.name),...phWords(s.name2)].filter(w=>!town.has(w)));
  return phWords(title.replace(/\s*\(.*\)\s*$/,'')).some(w=>!town.has(w)&&mine.has(w)); }
/* a credit sometimes carries the photographer's e-mail address: the name is credit enough */
const noMail=t=>String(t||'').replace(/[\s,;:·|\/-]*[(<\[]?\s*(?:mailto:)?[\w.+-]+@[\w-]+(?:\.[\w-]+)+\s*[)>\]]?/g,'').replace(/\s+/g,' ').replace(/^[\s,;:·|\/-]+|[\s,;:·|\/-]+$/g,'');
function photoBy(h){ const d=new DOMParser().parseFromString('<body>'+String(h||'')+'</body>','text/html').body; const t=noMail((d.textContent||'').replace(/\s+/g,' ').trim());
  if(t&&t.length<=70) return t;
  const a=[...d.querySelectorAll('a')].find(x=>/User:/.test(x.getAttribute('href')||'')&&noMail(x.textContent)); if(a) return noMail(a.textContent).slice(0,70);
  return (!t||d.querySelector('table,img,figure'))?'':t.slice(0,68).replace(/\s+\S*$/,'')+'…'; }      /* a long plain credit (an archive's full name) is cut short; a banner with no name in it gives nothing */
/* Most places' photo details are gathered ahead of time (tools/photos.py -> data/photos.json): the picture's address and size and
   whose it is, or 0 for "looked, nothing usable". The file is fetched once, in a quiet moment after the page opens, and then a
   place page shows its picture at once, with its room already kept, and asks Wikipedia nothing. A place the file does not
   hold (written since it was made) is asked for as before. */
let PHX=null, phxWait=null;
function phxLoad(){ if(!phxWait) phxWait=(AT?AT.fetch('data/photos.json'):fetch('data/photos.json'+VQ)).then(r=>{ if(!r.ok) throw new Error('http '+r.status); return r.json(); }).then(j=>{ PHX=(j&&j.p)||{}; }).catch(()=>{ PHX={}; }); return phxWait; }
const phxOf=s=>{ const v=PHX&&PHX[s.id]; return Array.isArray(v)?{src:v[0],w:v[1],h:v[2],who:v[3],lic:v[4],page:v[5],where:/commons\.wikimedia\.org/.test(v[5])?'Wikimedia Commons':'Wikipedia',title:v[6]}:v===0?0:undefined; };
function placePhoto(s){ if(PHOTO.has(s.id)) return PHOTO.get(s.id);
  if(!PHX){ return phxLoad().then(()=>placePhoto(s)); }
  { const k=phxOf(s); if(k!==undefined) return Promise.resolve(k||null); }
  const t=wikiTitle(s); if(!t) return Promise.resolve(null);
  const q=(base,o)=>fetch(base+'?'+new URLSearchParams(Object.assign({action:'query',format:'json',origin:'*'},o))).then(r=>{ if(!r.ok) throw new Error('http '+r.status); return r.json(); });
  const pr=q('https://en.wikipedia.org/w/api.php',{redirects:'1',prop:'pageimages|coordinates',piprop:'thumbnail|name',pithumbsize:'900',pilicense:'free',titles:t}).then(j=>{
      const pg=Object.values((j.query||{}).pages||{})[0]||{};
      if(!pg.coordinates||!pg.thumbnail||!pg.pageimage||!photoFits(s,pg.title||t,pg.coordinates[0])) return null;
      if(/\.svg$/i.test(pg.pageimage)||/(^|[^a-z])(map|locator|location|seal|flag|logo|coat[ _]of[ _]arms|diagram|plan)([^a-z]|$)/i.test(pg.pageimage)) return null;
      return q('https://en.wikipedia.org/w/api.php',{prop:'imageinfo',iiprop:'extmetadata|url',iiextmetadatafilter:'Artist|LicenseShortName',titles:'File:'+pg.pageimage}).then(c=>{   /* Wikipedia answers for Commons files too: one site to ask */
        const f=Object.values((c.query||{}).pages||{})[0]||{}, ii=(f.imageinfo||[])[0], m=ii&&ii.extmetadata||{};
        const who=photoBy((m.Artist||{}).value), lic=photoBy((m.LicenseShortName||{}).value);
        if(!ii||!who||!lic) return null;           /* no credit, no picture */
        return {src:pg.thumbnail.source,w:pg.thumbnail.width,h:pg.thumbnail.height,who:who,lic:lic,page:ii.descriptionurl||('https://commons.wikimedia.org/wiki/File:'+encodeURIComponent(pg.pageimage)),where:/commons\.wikimedia\.org/.test(ii.descriptionurl||'commons.wikimedia.org')?'Wikimedia Commons':'Wikipedia',title:pg.title}; }); })
    .catch(()=>{ PHOTO.delete(s.id); return null; });   /* a failure is asked again next time */
  PHOTO.set(s.id,pr); return pr; }
/* a tap on the picture: the same photo large over the page, with its credit; a tap anywhere (or Escape) puts it away.
   A bigger copy (1280 px, one of the sizes Wikimedia serves) is asked for where the address is a Wikimedia thumbnail; if that fails the copy already shown is used. */
function photoBig(ph){ let n=$('#photobig');
  if(!n){ n=el('div',{id:'photobig',hidden:true,role:'dialog','aria-label':'The photograph, larger'}); document.body.append(n);
    n.addEventListener('click',e=>{ if(e.target.tagName!=='A') n.hidden=true; }); document.addEventListener('keydown',e=>{ if(e.key==='Escape') n.hidden=true; }); }
  n.textContent=''; const big=/\/\d+px-[^/]+$/.test(ph.src)?ph.src.replace(/\/\d+px-([^/]+)$/,'/1280px-$1'):ph.src;
  const img=el('img',{src:big,alt:ph.title?'Photograph from the Wikipedia article '+ph.title:'Photograph of this place from Wikimedia Commons'}); img.addEventListener('error',()=>{ if(img.getAttribute('src')!==ph.src) img.src=ph.src; });
  n.append(img,el('p',null,'Photo: '+ph.who+' · '+ph.lic+' · ',ext(ph.page,ph.where),el('span',{text:' · Tap to close'}))); n.hidden=false; }
/* pictures of the place from elsewhere: an image search by name in the reader's browser. Nothing of it comes into the Atlas. */
const morePhotos=s=>ext('https://www.google.com/search?udm=2&q='+encodeURIComponent([s.name,s.town,STATE[REG_STATE[s.reg]]].filter(Boolean).join(' ')),'More photos','btn sm');
function photoBox(s){ if(!pref('wikiPhotos')||s.mine||navigator.onLine===false) return null;
  /* a stored picture with no article title was found on Wikimedia Commons near the pin (tools/photo_find.py): such a place
     needs no Wikipedia article of its own */
  if(!wikiTitle(s)&&!phxOf(s)) return null;
  const box=el('figure',{class:'dphoto',hidden:true});
  const fill=ph=>{ const img=el('img',{src:ph.src,alt:ph.title?'Photograph from the Wikipedia article '+ph.title:'Photograph of this place from Wikimedia Commons',decoding:'async'}); if(ph.w>0&&ph.h>0){ img.width=ph.w; img.height=ph.h; }
    img.addEventListener('error',()=>{ box.hidden=true; });
    img.title='Tap to see it larger'; img.addEventListener('click',()=>photoBig(ph));
    box.append(img,el('figcaption',null,(ph.title?'From Wikipedia\'s article on '+ph.title+'. ':'')+'Photo: '+ph.who+' · '+ph.lic+' · ',ext(ph.page,ph.where)));
    box.hidden=false; };
  const known=phxOf(s);
  if(known===0) return null;                 /* looked up ahead of time: nothing usable */
  if(known){ fill(known); return box; }      /* known ahead of time: in the page from the first frame, so nothing moves */
  placePhoto(s).then(ph=>{ if(!ph||!box.isConnected) return; fill(ph); });
  return box; }
/* The head of a place page cuts a long name to two lines when the phone is on its side. When that happens the whole name
   is written at the top of the part that scrolls, so nothing is lost. Asked again when the window changes shape. */
function nameFit(){ const v=$('#v-detail'), h=v&&v.querySelector('.dhead h2'), intro=v&&v.querySelector('.dintro'); if(!h||!intro) return;
  const cut=h.scrollHeight>h.clientHeight+2, old=intro.querySelector('.fullname');
  if(cut&&!old) intro.prepend(el('p',{class:'fullname',text:h.textContent})); else if(!cut&&old) old.remove(); }
window.addEventListener('resize',debounce(()=>{ if(view==='detail') nameFit(); },150));
/* "on November 18, 2026" for a place that began as a reader's tip (s.tip is that day), or nothing */
/* When it is open. s.hrs is what a source said when the place was written up, so the row says which month that was (the batch's own date):
   hours change. A place that takes visitors also gets a search for it by name, where Google Maps shows today's hours; so does a standing
   place of worship that is only seen from the street, because its services are when it is open. Other places have no Hours row. */
const takesVisitors=s=>s.acc==='open'||(s.cat==='worship'&&s.st==='standing'&&s.acc!=='ask'&&!s.mine);
function hoursAsOf(s){ const b=s.new&&BATCHES.find(x=>x.key===s.new), m=/^(\d{4})-(\d\d)/.exec(s.hrd||'')||(b&&/^(\d{4})-(\d\d)/.exec(b.added||'')); return m?new Date(+m[1],+m[2]-1,1).toLocaleDateString(undefined,{month:'long',year:'numeric'}):''; }
function hoursDd(s){ if(!s.hrs&&!takesVisitors(s)) return null;
  const dd=el('dd',{class:'hrs'}), when=s.hrs?hoursAsOf(s):'';
  if(s.hrs) dd.append(el('span',{text:s.hrs}));
  dd.append(el('div',null,when?el('small',{text:'As read '+when+(s.hru?', ':'.')}):null,when&&s.hru?ext(s.hru,'on this page','hsrc'):null,when?' ':'',ext('https://www.google.com/maps/search/?api=1&query='+encodeURIComponent([s.name,s.town,STATE[REG_STATE[s.reg]]].filter(Boolean).join(', ')),'Today\u2019s hours in Google Maps')));
  return dd; }
const tipDay=s=>{ const m=/^(\d{4})-(\d\d)-(\d\d)$/.exec(s.tip||''); return m?' on '+new Date(+m[1],+m[2]-1,+m[3]).toLocaleDateString(undefined,{month:'long',day:'numeric',year:'numeric'}):''; };
/* A place of the reader's own: the button that sends it to the public Atlas is at the top of its page, not far down under
   My notes (the owner, November 21, 2026). Pressing a Send link is remembered (U.sent), so the page can say so and so that
   the copy steps aside once the public Atlas has the place (twins()). */
function sendRow(s){ const day=(U.sent||{})[s.id], wrap=el('div',{class:'sendrow'});
  const b=el('button',{class:'btn sm'+(day?'':' pri'),type:'button',id:'lead-send','aria-expanded':'false'},day?'Send to the public Atlas again':'Send to the public Atlas');
  b.addEventListener('click',()=>{ const old=wrap.querySelector('.sharebox'); if(old){ old.remove(); b.setAttribute('aria-expanded','false'); return; }
    const box=shareBox('lead',{place:s.name,where:[s.town,s.lat.toFixed(5)+', '+s.lon.toFixed(5)].filter(Boolean).join(' \u00b7 '),text:[s.story,s.years?'Years: '+s.years:'',(STS[s.st]||'')+', '+((CAT[s.cat]||[''])[0])].filter(Boolean).join('. '),source:(s.links&&s.links[0]&&s.links[0][1])||'',access:(ACC[s.acc]||'')});
    box.querySelectorAll('a').forEach(a=>a.addEventListener('click',()=>{ if(!U.sent) U.sent={}; U.sent[s.id]=new Date().toISOString().slice(0,10); save(); }));
    wrap.append(box); b.setAttribute('aria-expanded','true'); });
  wrap.append(b); if(day) wrap.append(el('small',{class:'snote',style:'display:block;margin-top:4px',text:'Sent on '+day+'. It shows on the public Atlas once it has been researched; this copy then steps aside.'}));
  return wrap; }
function twinNote(s){ if(s.mine) return null; const T=twinsOf(s.id); if(!T.length) return null; const m=T[0];
  return el('div',{id:'twin-note',class:'sendrow'},el('small',{class:'snote',style:'display:block',text:'Your own place "'+m.name+'" is on this spot, so its pin is hidden: this is the public Atlas\u2019s entry for it.'}),
    el('div',{class:'row',style:'margin-top:6px'},
      el('button',{class:'btn sm',type:'button',id:'twin-show',onclick:()=>{ if(!U.keep) U.keep={}; U.keep[m.id]=1; save(); refresh(); renderDetail(s); }},'Show my copy'),
      el('button',{class:'btn sm',type:'button',id:'twin-del',onclick:()=>{ U.custom=U.custom.filter(x=>x.id!==m.id); if(Array.isArray(U.fav)) U.fav=U.fav.filter(i=>i!==m.id); U.trip=U.trip.filter(i=>i!==m.id); save(); refresh(); renderDetail(s); }},'Delete my copy'))); }
function renderDetail(s){
  const v=$('#v-detail'); v.textContent=''; v.scrollTop=0;
  const p=pos(s), d=dt(s), H=homeObj(), dst=dest(s), cat=CAT[s.cat]||CAT.landmark, pr=PREC[s.prec]||PREC.site;
  const inTrip=U.trip.indexOf(s.id)>=0;
  /* head */
  const tags=el('div',{class:'dmeta'},
    el('span',{class:'chip'},dot(s),s.mine?'My place · '+cat[0]:cat[0]),
    el('span',{class:'tag stag',title:ST[s.st]},dot(s),STS[s.st]),
    el('span',{class:'tag p-'+s.prec,text:pr[0],title:pr[1]}),
    s.conf==='lead'?el('span',{class:'tag lead',text:'Lead: confirm first',title:'From published local history but not re-checked against a source.'}):null,
    s.conf==='mixed'?el('span',{class:'tag lead',text:'Partly verified',title:'The outline is checked; some details are still leads.'}):null,
    s.now?el('span',{class:'tag now',text:'Changing now'}):null,
    s.tip?el('span',{class:'tag tipd',text:'Sent in by a reader',title:'A reader told the Atlas about this place'+tipDay(s)+'. Whatever could be checked against sources is in the text.'}):null);
  /* the head that stays put while the page scrolls is one row of buttons and the name, nothing more: on a phone on its
     side the column is short, and the photo, the line under the name and the badges scroll away with the rest */
  v.append(el('div',{class:'dhead pad'},
    el('div',{class:'dtop'},
      el('button',{class:'btn sm',type:'button',onclick:deselect,'aria-label':'Back to all places',title:'All places'},'← Back'),
      el('div',{class:'dtop-r'},
        el('button',{class:'btn sm favb'+(isFav(s.id)?' on':''),type:'button',id:'d-fav','aria-pressed':String(isFav(s.id)),'aria-label':isFav(s.id)?'Remove from my favourites':'Add to my favourites',title:isFav(s.id)?'In my favourites: tap to remove':'Add to my favourites: its pin stays on the map at every zoom',onclick:()=>{ const on=favToggle(s); banner(on?'Added to your favourites. Its pin now shows at every zoom; Filters has "My favourites".':'Removed from your favourites.',false,on?5000:2500); renderDetail(s); }},isFav(s.id)?'\u2665':'\u2661'),
        el('button',{class:'btn sm'+(inTrip?' on':''),type:'button',onclick:()=>{ const i=U.trip.indexOf(s.id); if(i>=0) U.trip.splice(i,1); else U.trip.push(s.id); save(); $('#trip-n').textContent=U.trip.length; renderDetail(s); }},inTrip?'✓ In trip':'+ Add to trip'),
        map?el('button',{class:'btn sm',type:'button',onclick:()=>map.flyTo([p.lat,p.lon],17,{duration:0.7})},'Zoom in'):null)),
    el('h2',{text:s.name})),
    el('div',{class:'dintro pad'},
    el('p',{class:'sub2',text:[s.name2,s.town,s.years,s.bk==='y'?'Red brick':s.bk==='s'?'Some red brick':''].filter(Boolean).join(' · ')}),
    tags,
    s.mine?sendRow(s):null, twinNote(s),
    photoBox(s),
    s.mine?null:(()=>{ const a=morePhotos(s); a.id='d-morephotos'; a.title='Search the web for pictures of this place by its name. Opens outside the Atlas.'; return el('p',{class:'dmore'},a); })()));
  nameFit();
  /* getting there */
  const times=el('div',{class:'times'});
  if(nearFrom()){ const l=dtl(s); times.append(el('div',{class:'time home',id:'dt-live'},el('b',{text:'~'+fmtMin(l.min)}),'from where you are · '+miTxt(l.mi))); }
  if(homePicked()) times.append(el('div',{class:'time'+(nearAt?'':' home')},el('b',{text:(d.est?'~':'')+fmtMin(d.min)}),'from '+H.name+' · '+miTxt(d.mi)));
  /* one time, from the reader's own start place; other cities' times were noise to anyone who does not live there */
  times.append(el('button',{class:'btn sm',type:'button',id:'dt-change',onclick:()=>{ openSettings(); setTimeout(()=>{ const n=$('#set-home'); if(n){ n.scrollIntoView({block:'center'}); n.focus(); } },80); }},homePicked()?'Change start place':'Set a start place to see the drive time'));
  /* with the position on, leave the origin out: Google Maps then starts from where the phone is */
  const gd='https://www.google.com/maps/dir/?api=1'+(nearAt||!homePicked()?'':'&origin='+H.lat+','+H.lon)+'&destination='+dst.lat+','+dst.lon+'&travelmode=driving';
  const cbtn=el('button',{class:'btn sm',type:'button'},'Copy'); cbtn.addEventListener('click',()=>copy(ll(p),cbtn));
  const hrs=hoursDd(s);
  v.append(el('div',{class:'sec pad'},el('h3',{text:'Getting there'}),times,
    el('dl',{class:'kv',style:'margin-top:8px'},
      el('dt',{text:'Access'}),el('dd',{text:ACC[s.acc]||''}),
      hrs?el('dt',{text:'Hours'}):null,hrs,
      el('dt',{text:'Effort'}),el('dd',{text:(EFF[s.eff]||'')+(s.th?' from '+(s.thn||'the trailhead'):'')}),
      s.pl?el('dt',{text:'Land'}):null,s.pl?el('dd',null,el('span',{class:'sw',style:'--c:'+(PADC[s.pl[2]]||PADC.UK)[1]}),' '+s.pl[0]+' · '+(PADC[s.pl[2]]||PADC.UK)[0]):null,
      el('dt',{text:'Pin'}),el('dd',null,el('span',{class:'mono',text:ll(p)}),' ',cbtn)),
    s.accn?el('p',{style:'margin-top:8px',text:s.accn}):null,
    s.th?el('p',{style:'color:var(--mute);font-size:12.5px',text:'Drive times and directions go to the parking spot (blue P on the map), not the pin.'}):null,
    el('div',{class:'row',style:'margin-top:8px'},ext(gd,'Directions in Google Maps','btn pri'),ext('https://www.google.com/maps/search/?api=1&query='+dst.lat+','+dst.lon,s.th?'Parking in Google Maps':'Open pin: hours, photos','btn'))));
  /* whose land */
  { const who=el('div',{class:'who'}), moved=!!U.moved[s.id];
    const line=s.mine||moved?'Check the spot before you go.':s.pl?'The pin falls on '+s.pl[0]+(s.pl[1]?' ('+s.pl[1]+')':'')+', mapped as "'+(PADC[s.pl[2]]||PADC.UK)[0].toLowerCase()+'."':'The pin is not on mapped public land, so treat it as private until you have checked.';
    v.append(el('div',{class:'sec pad'},el('h3',{text:'Whose land is it?'}),
      el('p',{style:'font-size:12.5px;color:var(--mute)',text:line+(s.prec==='area'?' This pin is approximate, so look up the actual spot on the map too.':'')}),
      schematic?null:el('div',{class:'row'},el('button',{class:'btn sm',type:'button',onclick:()=>lookup(p,who)},'Look up the owner at the pin')),who,letterBox(s))); }
  /* scout */
  const sc=el('div',{class:'sec pad'},el('h3',{text:'Scout it from your desk'}));
  sc.append(el('p',{style:'font-size:12.5px;color:var(--mute)',text:pr[1]+' The dashed ring on the map shows that margin.'}));
  if(s.pn) sc.append(el('p',{class:'pn',text:s.pn}));
  if(map&&!schematic){
    const look=(base,ck,zoom,hist)=>()=>{ U.ui.hist=!!hist; if(base==='streets'&&navigator.onLine===false) base='topo'; setBase(base); cmp.on=!!ck; cmp.lap=0; if(ck){cmp.key=ck;cmp.mode='swipe';cmp.x=0.5;} setCmp(); syncBar(); showHist(); const hc=document.getElementById('d-hist'); if(hc) hc.checked=!!hist; map.flyTo([p.lat,p.lon],zoom,{duration:0.7}); };
    sc.append(el('div',{class:'row',style:'margin-bottom:8px'},
      s.tm?el('button',{class:'btn sm',type:'button',onclick:look('streets',null,15,true)},s.tm.y+' map'):null,
      el('button',{class:'btn sm',type:'button',onclick:look('leaf',null,18,false)},'Leaf-off aerial'),
      el('button',{class:'btn sm',type:'button',onclick:look('lidar',null,17,false)},'LiDAR'),
      el('button',{class:'btn sm',type:'button',onclick:look('leaf','lidar',17,false)},'Swipe aerial ↔ LiDAR'),
      el('button',{class:'btn sm',type:'button',onclick:look('streets',null,15,false)},'Streets')));
  }
  if(s.tm){
    const pic=el('img',{alt:s.tm.y+' USGS map around '+s.name}); topoSrc(s).then(u=>{ if(u) pic.src=u; else pic.remove(); });
    const ck=el('input',{type:'checkbox',id:'d-hist',checked:!!U.ui.hist,onchange:e=>{U.ui.hist=e.target.checked;save();showHist();syncBar();}});
    sc.append(el('div',{class:'hist'},
      el('label',{class:'lopt',for:'d-hist'},ck,el('span',null,'Lay the '+s.tm.y+' USGS map over whatever layer is showing',el('small',{text:s.tm.q+' sheet, 1:'+Number(s.tm.sc).toLocaleString([],{hour12:H12()})+'. Old surveys can sit 50–100 m off; match roads and streams.'}))),
      el('input',{type:'range',id:'d-hist-op',min:'0.1',max:'1',step:'0.05',value:String(U.ui.histOp),'aria-label':'Old map strength',oninput:e=>{U.ui.histOp=+e.target.value;save();if(histLayer)histLayer.setOpacity(U.ui.histOp);}}),
      pic));
  }
  const grid=el('div',{class:'scout',style:'margin-top:8px'}); scoutLinks(p,s.town).forEach(l=>grid.append(ext(l[1],l[0],'btn sm'))); sc.append(grid);
  if(map&&!schematic) sc.append(el('h3',{text:'Take it offline',style:'margin-top:14px'}),offlineBox(s.id,[p],s.name));
  v.append(sc);
  /* story */
  const st=el('div',{class:'sec pad'},el('h3',{text:'What was here'}));
  if(s.fr) st.append(el('p',{class:'fr',text:s.fr}));
  if(s.story) st.append(el('p',{text:s.story}));
  if(s.look) st.append(el('p',null,el('b',{text:'Look for: '}),s.look));
  if(s.hook) st.append(el('p',{class:'hook',text:s.hook}));
  if(s.story||s.look||s.hook||s.fr) v.append(st);
  v.append(visitSection(s));
  /* mine */
  const sv=el('span',{class:'note-saved',text:''});
  const stSel=el('select',{id:'my-status',onchange:e=>{ if(e.target.value) U.status[s.id]=e.target.value; else delete U.status[s.id]; save(); syncMarkers(); sv.textContent='Saved'; }},Object.keys(MY).map(k=>el('option',{value:k,text:MY[k]})));
  stSel.value=U.status[s.id]||'';
  const ta=el('textarea',{id:'my-notes',placeholder:'Parking, who to call, shot ideas, what you found…',oninput:debounce(e=>{ if(e.target.value.trim()) U.notes[s.id]=e.target.value; else delete U.notes[s.id]; save(); sv.textContent='Saved'; },300)});
  ta.value=U.notes[s.id]||'';
  const mine=el('div',{class:'sec pad'},el('h3',{text:'My notes'}),
    el('div',{class:'row'},el('label',{class:'field'},el('span',{text:'Progress'}),stSel)),
    el('label',{class:'field',style:'margin-top:8px'},el('span',{text:'Notes'}),ta),
    el('div',{class:'row',style:'margin-top:8px'},
      map?el('button',{class:'btn sm',type:'button',onclick:()=>{ if(rec) showView('log'); else startLog(s); }},rec?'Field log is recording':'Start a field log here'):null,
      map?el('button',{class:'btn sm',type:'button',onclick:()=>{ const m=markers.get(s.id); if(m){ m.dragging.enable(); banner('Drag the pin to the right spot, then let go.',false,6000); } }},'Move the pin'):null,
      U.moved[s.id]?el('button',{class:'btn sm',type:'button',onclick:()=>{ delete U.moved[s.id]; save(); refresh(); select(s,true); }},'Put pin back'):null,
      s.mine?el('button',{class:'btn sm',type:'button',onclick:()=>openForm(s)},'Edit'):null,
      s.mine?delBtn(s):null,
      sv),
    (()=>{ const fl=s.from&&logById(s.from.log), fn=fl&&fl.notes.find(x=>x.t===s.from.t); if(!fn) return null; const ph=photosOf(fl,fn);   /* a place made from a field-log note keeps its photos and its walk */
      return el('div',{style:'margin-top:10px'},el('p',{class:'snote',text:'From your field log "'+fl.name+'", note "'+fn.x+'".'}),ph.length?mediaStrip(fl,ph):null,
        el('div',{class:'row',style:'margin-top:6px'},el('button',{class:'btn sm',type:'button',onclick:()=>{ showLog(fl,true); banner('Showing the walk that found it.',false,4000); }},'Show the walk on the map'))); })(),
    storeOK?null:el('p',{style:'color:var(--warn);font-size:12.5px;margin-top:8px',text:'This browser is not saving data right now, so notes will be lost when you close the page.'}));
  v.append(mine);
  /* nearby */
  const near=sites().filter(o=>o.id!==s.id).map(o=>{ const q=pos(o); return [o,hav(p.lat,p.lon,q.lat,q.lon)]; }).filter(x=>x[1]<=3).sort((a,b)=>a[1]-b[1]).slice(0,10);
  if(near.length){ const ul=el('ul',{class:'near'}); near.forEach(x=>ul.append(el('li',null,el('button',{type:'button',onclick:()=>select(x[0],true)},dot(x[0]),' '+x[0].name),el('span',{text:x[1]<0.1?(KM()?Math.round(x[1]*1609.34)+' m':Math.round(x[1]*5280)+' ft'):fmtMi(x[1],1)}))));
    v.append(el('div',{class:'sec pad'},el('h3',{text:'Close by, as the crow flies'}),ul)); }
  const nl=nearLines(p);
  if(nl.length){ const ul=el('ul',{class:'near'}); nl.forEach(x=>ul.append(el('li',null,el('button',{type:'button',onclick:()=>setLine(x.parts?{f:x.f,parts:x.parts}:{f:x.f})},el('span',{class:'sw'+(LK[x.f.k][2]?' dash':''),style:'--c:'+LK[x.f.k][1]}),' '+(x.f.n||('Unnamed '+LK[x.f.k][0].toLowerCase()))+(x.f.y?' ('+x.f.y+')':'')),el('span',{text:x.d<30?'on it':Math.round(x.d)+' m'}))));
    v.append(el('div',{class:'sec pad'},el('h3',{text:'Old lines passing here'}),ul,el('p',{style:'color:var(--mute);font-size:12.5px;margin-top:6px',text:'Pick one to follow it and see every Atlas place along the way.'}))); }
  /* sources */
  if(s.links&&s.links.length){ const ul=el('ul',{class:'links'}); s.links.forEach(l=>ul.append(el('li',null,ext(l[1],l[0])))); v.append(el('div',{class:'sec pad'},el('h3',{text:'Sources'}),ul)); }
}
function delBtn(s){ const b=el('button',{class:'btn sm',type:'button'},'Delete'); let armed=false;
  b.addEventListener('click',()=>{ if(!armed){ armed=true; b.textContent='Really delete?'; setTimeout(()=>{armed=false;b.textContent='Delete';},4000); return; }
    U.custom=U.custom.filter(x=>x.id!==s.id); if(Array.isArray(U.fav)) U.fav=U.fav.filter(i=>i!==s.id); delete U.status[s.id]; delete U.notes[s.id]; delete U.moved[s.id]; U.trip=U.trip.filter(i=>i!==s.id); save(); sel=null; drawSel(); showView('list'); refresh(); });
  return b; }

/* add / edit your own place */
/* ---------- placing by hand, and spots ----------
   + Add puts a cross at the middle of the map: you move the map under it and press "Place here" (a click or tap on the spot
   works too). The form then opens with a pin you can still drag until you save. "Spot many" is the quick way to hand over a
   whole street of buildings for research: every press of Drop leaves a bare numbered mark, with no form. Spots are U.spots,
   [{lat,lon,t,note?}], shown on the map and counted on the Places tab until they are copied out and cleared. */
const finePointer=()=>{ try{ return matchMedia('(pointer:fine)').matches; }catch(e){ return true; } };
let formPin=null, spotLayer=null, aimWait=null;
function aimShow(on){ let a=$('#aim'); if(!a&&map){ a=el('div',{id:'aim','aria-hidden':'true'}); a.hidden=true; map.getContainer().append(a); } if(a) a.hidden=!on; }
function addBar(){ const on=adding||spotting, n=(U.spots||[]).length;
  $('#add-centre').hidden=!on; $('#add-many').hidden=!adding; $('#spot-undo').hidden=!(spotting&&n); $('#add-here').hidden=!(on&&geo.ll);
  $('#add-centre').textContent=spotting?'Drop':'Place here'; $('#add-cancel').textContent=spotting?'Done':'Cancel';
  if(spotting) $('#addbar span').textContent=n+(n===1?' spot':' spots')+'. Put the cross on a building'+(finePointer()?', or click one.':'.');
  else if(adding) $('#addbar span').textContent='Put the cross on the place, or '+(finePointer()?'click':'tap')+' it.';
  $('#addbar').classList.toggle('many',on); aimShow(on); clearInterval(aimWait); aimWait=null;
  if(on&&!geo.ll) aimWait=setInterval(()=>{ if(!(adding||spotting)){ clearInterval(aimWait); aimWait=null; } else if(geo.ll){ clearInterval(aimWait); aimWait=null; $('#add-here').hidden=false; } },700); }
function placeAt(lat,lon){ adding=false; stage.classList.remove('adding'); $('#addbar').hidden=true; addBar(); quickAdd({lat:+(+lat).toFixed(6),lon:+(+lon).toFixed(6)}); }
/* The quick card (the owner, November 21, 2026). Standing in front of something with a camera running, the full form was too
   much to look at and to type: what you know there is what it is, and little else. So a new place gets one row of four taps,
   and a tap saves it. The setting addMore adds the kind, the year and the name above that row for whoever wants them; "More
   details" opens the full form. The map is moved so the pin is in the middle of what still shows of it. */
const QWHAT=[['standing','Standing','building'],['ruins','Ruin','ruin'],['traces','Trace','trace'],['curio','Odd find','']];
const QKIND=[['landmark','House','house'],['worship','Church','church'],['industry','Mill','mill'],['civic','Public building','public building'],['rail','Railroad','railroad building'],['landmark','Other','']];
function quickAdd(seed){
  const s={lat:seed.lat,lon:seed.lon}, v=$('#v-detail'), more=!!pref('addMore'); v.textContent=''; showView('detail'); dropFormPin();
  const atText=()=>s.lat.toFixed(5)+', '+s.lon.toFixed(5)+(map?' \u00b7 drag the pink pin to adjust':'');
  if(map){ formPin=L.marker([s.lat,s.lon],{draggable:true,keyboard:false,zIndexOffset:900,icon:L.divIcon({className:'formpin',html:'',iconSize:[26,26],iconAnchor:[13,13]})}).addTo(map);
    formPin.on('drag dragend',()=>{ const ll=formPin.getLatLng(); s.lat=+ll.lat.toFixed(6); s.lon=+ll.lng.toFixed(6); const t=$('#f-at'); if(t) t.textContent=atText(); });
    setTimeout(()=>{ if(!formPin) return; map.invalidateSize(); map.panTo([s.lat,s.lon],{animate:false}); },60); }
  let kind=-1; const kinds=el('div',{class:'qa-chips',id:'qa-kind'}), year=el('input',{type:'text',id:'qa-year',inputMode:'numeric',maxLength:4,placeholder:'Year, if you know it',autocomplete:'off'}), name=el('input',{type:'text',id:'qa-name',placeholder:'Name, if you know it',maxLength:80,autocomplete:'off'});
  QKIND.forEach((k,i)=>{ const b=el('button',{type:'button',class:'chip','aria-pressed':'false'},k[1]); b.addEventListener('click',()=>{ kind=kind===i?-1:i; [...kinds.children].forEach((c,j)=>c.setAttribute('aria-pressed',String(j===kind))); }); kinds.append(b); });
  const keep=w=>{ const k=more&&kind>=0?QKIND[kind]:null, odd=w==='curio', noun=(k&&k[2])||(odd?'':QWHAT.find(x=>x[0]===w)[2]);
    const day=new Date().toLocaleDateString([],{month:'short',day:'numeric'}), typed=more?name.value.trim():'', y=more?(year.value.match(/\d{3,4}/)||[''])[0]:'';
    const nm=typed||((odd?'Odd find':'Unnamed '+noun+(k&&k[2]&&w!=='standing'?' ('+QWHAT.find(x=>x[0]===w)[2]+')':''))+' ('+day+')');
    const o={id:'my-'+Date.now().toString(36),mine:true,name:nm,name2:'',town:'',years:y,reg:'',cat:odd?'curio':(k?k[0]:'landmark'),st:odd?'standing':w,prec:'exact',acc:'view',eff:'walk',conf:'lead',lat:s.lat,lon:s.lon,tags:[],story:'',look:'',hook:'',accn:'',links:[],now:false};
    U.custom.push(o); save(); dropFormPin(); deselect(); refresh(); banner('Saved: '+nm+'. Tap its pin to add details or send it in.',false,5000); };
  const what=el('div',{id:'qa-what'}); QWHAT.forEach(w=>{ const b=el('button',{type:'button',class:'btn','data-w':w[0]},w[1]); b.addEventListener('click',()=>keep(w[0])); what.append(b); });
  v.append(el('div',{class:'pad',id:'quickadd',style:'padding-block:12px'},
    el('div',{class:'row',style:'justify-content:space-between'},el('button',{class:'btn sm',type:'button',onclick:()=>deselect()},'\u2190 Cancel'),el('button',{class:'btn sm',id:'qa-more',type:'button',onclick:()=>openForm({lat:s.lat,lon:s.lon})},'More details')),
    el('p',{class:'mono',id:'f-at',style:'color:var(--mute);margin:8px 0 0',text:atText()}),
    more?kinds:null, more?el('div',{class:'row',style:'margin-top:8px'},year,name):null,
    el('p',{class:'qa-q',text:'What is it? One tap saves it.'}),what)); }
function dropFormPin(){ if(formPin){ formPin.remove(); formPin=null; } }
function spotStart(){ if(!map) return; asking=false; pickingHome=false; adding=false; spotting=true; stage.classList.add('adding'); $('#addbar').hidden=false; addBar(); }
function spotDrop(lat,lon){ if(!Array.isArray(U.spots)) U.spots=[]; U.spots.push({lat:+(+lat).toFixed(6),lon:+(+lon).toFixed(6),t:Date.now()}); saveNow(); drawSpots(); addBar(); }
function drawSpots(){ if(spotLayer){ spotLayer.remove(); spotLayer=null; } const S=U.spots||[];
  if(map&&S.length) spotLayer=L.layerGroup(S.map((x,i)=>{ const m=L.marker([x.lat,x.lon],{keyboard:false,zIndexOffset:300,icon:L.divIcon({className:'spotpin',html:String(i+1),iconSize:[22,22],iconAnchor:[11,11]})}); m.on('click',()=>spotOpen(i)); return m; })).addTo(map);
  spotCard(); }
function spotOpen(i){ const x=(U.spots||[])[i]; if(!x||!map) return; const inp=el('input',{type:'text',id:'spot-note',placeholder:'A few words, if you like',maxlength:'140',autocomplete:'off'}); inp.value=x.note||'';
  const box=el('form',{class:'spotbox',onsubmit:e=>{ e.preventDefault(); const v=inp.value.trim(); if(v) x.note=v; else delete x.note; saveNow(); map.closePopup(); spotCard(); }},
    el('b',{text:'Spot '+(i+1)}),inp,el('div',{class:'row'},el('button',{class:'btn sm pri',id:'spot-save',type:'submit'},'Save'),
      el('button',{class:'btn sm',type:'button',onclick:()=>{ U.spots.splice(i,1); saveNow(); map.closePopup(); drawSpots(); if(spotting) addBar(); }},'Remove')));
  L.popup({maxWidth:250}).setLatLng([x.lat,x.lon]).setContent(box).openOn(map); }
window.__spotOpen=spotOpen;
/* spots as they go to Claude: a number, a point, the day, and the few words if any (tools/visits.py reads this) */
function spotExport(){ return (U.spots||[]).map((x,i)=>({n:i+1,lat:x.lat,lon:x.lon,note:x.note||'',t:new Date(x.t||Date.now()).toISOString().slice(0,10)})); }
function spotCard(){ const c=$('#spotcard'); if(!c) return; const S=U.spots||[], noted=S.filter(x=>x.note).length; c.textContent=''; c.hidden=!S.length; if(!S.length) return;
  const cp=el('button',{class:'btn sm pri',id:'spots-copy',type:'button'},'Copy for Claude'); cp.addEventListener('click',()=>copy(JSON.stringify({spots:spotExport()},null,1),cp));
  const sh=el('button',{class:'btn sm',type:'button'},'Show on map'); sh.addEventListener('click',()=>{ if(map) map.fitBounds(L.latLngBounds(S.map(x=>[x.lat,x.lon])).pad(0.3),{maxZoom:17}); });
  const mo=el('button',{class:'btn sm',type:'button'},'Add more'); mo.addEventListener('click',spotStart);
  const cl=el('button',{class:'btn sm',id:'spots-clear',type:'button'},'Clear'); let armed=false;
  cl.addEventListener('click',()=>{ if(!armed){ armed=true; cl.textContent='Tap again to clear all'; setTimeout(()=>{ armed=false; cl.textContent='Clear'; },3500); return; } U.spots=[]; saveNow(); drawSpots(); if(spotting) addBar(); });
  /* through the form, like a place, so that anybody can send them (the owner, November 21, 2026): one line a spot in the form's text,
     which holds about 1,500 characters, so a long list goes as several links (tools/spotlines.py reads them back) */
  const lines=S.map((x,i)=>(i+1)+'. '+x.lat.toFixed(5)+', '+x.lon.toFixed(5)+(x.note?' '+x.note:'')), parts=[]; let cur=[];
  lines.forEach((l,i)=>{ if(cur.length&&cur.map(j=>lines[j]).join('\n').length+l.length+1>1400){ parts.push(cur); cur=[]; } cur.push(i); }); if(cur.length) parts.push(cur);
  const send=el('div',{class:'row',style:'margin-bottom:8px'}); parts.forEach(pt=>{ const a=S[pt[0]], L=shareLinks('lead',{place:'Spots: '+pt.length+' marked for research',where:a.lat.toFixed(5)+', '+a.lon.toFixed(5),text:pt.map(j=>lines[j]).join('\n'),source:'I was there',access:''});
    send.append(ext(L.form||L.gh,parts.length>1?'Send spots '+(pt[0]+1)+' to '+(pt[pt.length-1]+1):'Send to the public Atlas','btn sm pri spots-send')); });
  cp.classList.remove('pri');
  c.append(el('div',{},el('b',{text:S.length+(S.length===1?' spot':' spots')+' to research'}),
    el('p',{text:'Marks you dropped on buildings worth looking into'+(noted?', '+noted+' with a note':'')+'. Send them to the public Atlas to have them researched (a page opens, filled in; press Submit there), then clear them.'}),
    send,el('div',{class:'row'},cp,sh,mo,cl))); }
function openForm(seed){
  const editing=!!seed.id, s=editing?seed:{lat:seed.lat,lon:seed.lon,name:seed.name||'',town:'',years:'',cat:'industry',st:'ruins',prec:'site',acc:seed.story?'ask':'public',eff:'walk',story:seed.story||'',link:'',from:seed.from};
  const v=$('#v-detail'); v.textContent=''; showView('detail'); dropFormPin();
  const atText=()=>s.lat.toFixed(5)+', '+s.lon.toFixed(5)+(editing||!map?'':' \u00b7 drag the pink pin on the map to adjust');
  if(!editing&&map){      /* the pin stays movable until the place is saved */
    formPin=L.marker([s.lat,s.lon],{draggable:true,keyboard:false,zIndexOffset:900,icon:L.divIcon({className:'formpin',html:'',iconSize:[26,26],iconAnchor:[13,13]})}).addTo(map);
    formPin.on('drag dragend',()=>{ const ll=formPin.getLatLng(); s.lat=+ll.lat.toFixed(6); s.lon=+ll.lng.toFixed(6); const t=$('#f-at'); if(t) t.textContent=atText(); }); }
  const f=(id,label,node)=>el('label',{class:'field',for:id,style:'margin-top:8px'},el('span',{text:label}),node);
  const opt=(map,val,id)=>{ const x=el('select',{id:id},Object.keys(map).map(k=>el('option',{value:k,text:Array.isArray(map[k])?map[k][0]:map[k]}))); x.value=val; return x; };
  const name=el('input',{type:'text',id:'f-name',required:true}); name.value=s.name;
  const town=el('input',{type:'text',id:'f-town'}); town.value=s.town||'';
  const years=el('input',{type:'text',id:'f-years',placeholder:'e.g. 1880–1924'}); years.value=s.years||'';
  const cat=opt(CAT,s.cat,'f-cat'), st=opt(STS,s.st,'f-st'), prec=opt({exact:'Exact',site:'On site',area:'Approximate'},s.prec,'f-prec'), acc=opt(ACC,s.acc,'f-acc'), eff=opt(EFF,s.eff,'f-eff');
  const story=el('textarea',{id:'f-story',placeholder:'What stood here, what is left, where you heard about it'}); story.value=s.story||'';
  const link=el('input',{type:'url',id:'f-link',placeholder:'https://'}); link.value=(s.links&&s.links[0]&&s.links[0][1])||'';
  const err=el('p',{style:'color:var(--warn);margin:8px 0 0'});
  const form=el('form',{class:'pad',style:'padding-block:12px',onsubmit:e=>{ e.preventDefault();
    if(!name.value.trim()){ err.textContent='Give the place a name.'; name.focus(); return; }
    let url=link.value.trim(); if(url&&!/^https?:\/\//i.test(url)){ err.textContent='Links need to start with http:// or https://'; link.focus(); return; }
    const o={id:editing?s.id:'my-'+Date.now().toString(36),mine:true,name:name.value.trim(),name2:'',town:town.value.trim(),years:years.value.trim(),reg:s.reg||'',cat:cat.value,st:st.value,prec:prec.value,acc:acc.value,eff:eff.value,conf:'lead',lat:s.lat,lon:s.lon,tags:[],story:story.value.trim(),look:'',hook:'',accn:'',links:url?[['Source',url]]:[],now:false,from:s.from};
    if(editing) U.custom=U.custom.map(x=>x.id===o.id?o:x); else U.custom.push(o);
    if(o.from){ const fl=logById(o.from.log), fn=fl&&fl.notes.find(x=>x.t===o.from.t); if(fn){ fn.pl=o.id; saveNow(); } }
    save(); refresh(); select(o,false); }},
    el('button',{class:'btn sm',type:'button',onclick:()=>{ if(editing) select(seed,false); else deselect(); }},'← Cancel'),
    el('h2',{style:'font-size:22px;margin-top:8px',text:editing?'Edit your place':'Add a place'}),
    el('p',{class:'mono',id:'f-at',style:'color:var(--mute);margin:2px 0 0',text:atText()}),
    f('f-name','Name',name),el('div',{class:'row'},f('f-town','Town',town),f('f-years','Years',years)),
    el('div',{class:'row'},f('f-cat','Kind of place',cat),f('f-st',"What's left",st)),
    el('div',{class:'row'},f('f-acc','Access',acc),f('f-eff','Effort',eff)),
    f('f-prec','How sure is the pin?',prec),f('f-story','Notes',story),f('f-link','Source link',link),err,
    el('div',{class:'row',style:'margin-top:12px'},el('button',{class:'btn pri',type:'submit'},editing?'Save changes':'Save place')),
    el('p',{style:'color:var(--mute);font-size:12.5px;margin-top:10px',text:'Places you add are saved in this browser. Use Guide › Your data to back them up or hand them to Claude to merge into the master list.'}));
  v.append(form); name.focus();
}

/* ---------- sending a visit report or a lead to the Atlas ----------
   The site has no server, so a report leaves the reader's browser by one of three doors, each opened already filled in:
     - a Google Form the owner keeps (no account needed to send; GUIDE.md section 15 says how it is made). Until SHARE.form
       holds its address the button is not shown;
     - a GitHub issue form (.github/ISSUE_TEMPLATE/lead.yml and visit.yml; the sender needs a free GitHub account);
     - the clipboard, as plain text.
   Nothing is sent until the reader presses Submit on the page that opens. What arrives is read by tools/inbox.py and is
   treated as a tip to be checked, never as fact. */
const SHARE={gh:'https://github.com/Mrroot3r/Lost-and-Hidden-Atlas/issues/new',
  /* the owner's Google Form and its question ids; tools/form_ids.py prints these two lines from the form's link */
  form:'https://docs.google.com/forms/d/e/1FAIpQLScsxGx4EgDT2vQqAkU_JkCOlY7arNAGa9da0-55y6K6v1r_Dw/viewform',
  ent:{kind:'entry.1512318193',place:'entry.1603685238',where:'entry.1784127289',text:'entry.245411565',source:'entry.1131631114',access:'entry.2120312031'}};
const cut=(t,n)=>{ t=String(t||''); return t.length>n?t.slice(0,n-1)+'…':t; };
/* f: {place, where, text, source, access} for a lead; for a visit also {id, when, found, spot} */
function shareText(kind,f){ return (kind==='visit'?['Visit report for the Lost & Hidden Atlas','Place: '+f.place+(f.id?' ('+f.id+')':''),'Visited: '+(f.when||''),'Found: '+(f.found||''),'What is there: '+(f.text||''),'Access as found: '+(f.access||''),'True spot: '+(f.spot||'the pin is right, or not known')]
    :['A place for the Lost & Hidden Atlas','Place: '+(f.place||''),'Where: '+(f.where||''),'What I know: '+(f.text||''),'Source or how I know: '+(f.source||''),'Can the public go there: '+(f.access||'')]).join('\n'); }
function shareLinks(kind,f){ const q=o=>Object.keys(o).filter(k=>o[k]).map(k=>encodeURIComponent(k)+'='+encodeURIComponent(cut(o[k],1500))).join('&');
  const gh=SHARE.gh+'?'+(kind==='visit'
    ?q({template:'visit.yml',title:'Visit: '+cut(f.place,80),place:f.place+(f.id?' ('+f.id+')':''),when:f.when,found:f.found,there:f.text,access:f.access,spot:f.spot})
    :q({template:'lead.yml',title:'Lead: '+cut(f.place||'a place',80),place:f.place,where:f.where,know:f.text,source:f.source}));
  let form='';
  if(SHARE.form&&SHARE.ent.place){ const e=SHARE.ent, o={}; const put=(k,v)=>{ if(e[k]&&v) o[e[k]]=v; };
    put('kind',kind==='visit'?'A visit report':'A place I know about'); put('place',f.place+(kind==='visit'&&f.id?' ('+f.id+')':''));
    put('where',kind==='visit'?[f.when?'Visited '+f.when:'',f.spot?'true spot '+f.spot:''].filter(Boolean).join('; '):f.where);
    put('text',kind==='visit'?[f.found,f.text].filter(Boolean).join('. '):f.text); put('source',f.source); put('access',f.access);
    form=SHARE.form+(SHARE.form.indexOf('?')<0?'?':'&')+'usp=pp_url&'+q(o); }
  return {gh:gh,form:form}; }
/* one link that sends a spot, coordinates already filled in: from a field-log note or a long press on the map */
/* one quiet line under the two kinds of button, so it is plain which is which */
const WHICH=()=>el('p',{class:'which',text:'My places stay on this device. The public Atlas is the map everyone sees: what you send is checked before it goes on.'});
function spotLink(name,la,lo,text,label){ const L=shareLinks('lead',{place:name||'',where:(+la).toFixed(5)+', '+(+lo).toFixed(5),text:text||'',source:'I was there',access:''}); return ext(L.form||L.gh,label||'Send this spot to the public Atlas','btn sm spot-send'); }
function shareBox(kind,f){ const L=shareLinks(kind,f), cp=el('button',{class:'btn sm',type:'button'},'Copy as text'); cp.addEventListener('click',()=>copy(shareText(kind,f),cp));
  return el('div',{class:'sharebox'},
    el('p',{class:'snote',style:'display:block',text:(kind==='visit'?'Send this report':'Send this place')+' so the map can be corrected for everyone. A page opens with it filled in; nothing is sent until you press Submit there. What you send is public, so leave out anything private. Reports are checked before the map changes.'}),
    el('div',{class:'row'},
      L.form?ext(L.form,'Send it (no account needed)','btn pri share-form'):null,
      ext(L.gh,L.form?'Post it on GitHub':'Post it on GitHub (free account)','btn sm share-gh'),cp)); }
/* ---------- visit reports ----------
   What was really there when the owner went: U.visits[id] = [{t:'2026-11-16', v:'found'|'else'|'nothing'|'blocked', x: what is there,
   a: access as found, at:[lat,lon] the true spot or null}], newest first. They travel in "Copy my additions for Claude"
   (Settings, Your data) and tools/visits.py turns that into a list of corrections to pins, texts and the LiDAR ledger. */
const VISIT={found:'Found it',else:'Something else is there',nothing:'Nothing there',blocked:'Could not get to it'};
let visitOpen=null;      /* {id, i} while a report is being written or edited; i is its place in the list, -1 for a new one */
function visitSection(s){ if(!U.visits) U.visits={}; const list=U.visits[s.id]||[], pin=pos(s), sec=el('div',{class:'sec pad',id:'visits'},el('h3',{text:'Visit reports'}));
  const dist=at=>hav(pin.lat,pin.lon,at[0],at[1])*1609.344, far=m=>KM()?Math.round(m)+' m':Math.round(m*3.28084)+' ft';
  list.forEach((r,i)=>{ if(visitOpen&&visitOpen.id===s.id&&visitOpen.i===i) return;
    sec.append(el('div',{class:'visit-item'},el('b',{text:new Date(r.t+'T12:00:00').toLocaleDateString([],{dateStyle:'medium'})+' · '+(VISIT[r.v]||r.v)}),r.at?el('small',{text:' · true spot '+far(dist(r.at))+' from the Atlas pin'}):null,
      r.x?el('p',{text:r.x}):null,r.a?el('p',{class:'snote',style:'display:block',text:'Access: '+r.a}):null,
      el('div',{class:'row'},el('button',{class:'btn sm visit-send',type:'button','aria-expanded':'false',onclick:e=>{ const it=e.target.closest('.visit-item'), old=it.querySelector('.sharebox'); if(old){ old.remove(); e.target.setAttribute('aria-expanded','false'); return; }
          const b0=BASE.find(x=>x.id===s.id)||s; it.append(shareBox('visit',{place:s.name+(s.town?', '+s.town:''),id:s.mine?'':s.id,when:r.t,found:VISIT[r.v]||r.v,text:r.x,access:r.a,spot:r.at?r.at[0]+', '+r.at[1]:(s.mine?b0.lat+', '+b0.lon:'')})); e.target.setAttribute('aria-expanded','true'); }},'Send to the public Atlas'),
        el('button',{class:'btn sm visit-edit',type:'button',onclick:()=>{ visitOpen={id:s.id,i:i}; renderDetail(s); const n=$('#visit-form'); if(n) n.scrollIntoView({block:'nearest'}); }},'Edit'),
        el('button',{class:'btn sm visit-del',type:'button',onclick:()=>{ if(!confirm('Delete this visit report?')) return; list.splice(i,1); if(!list.length) delete U.visits[s.id]; save(); renderDetail(s); }},'Delete')))); });
  if(!(visitOpen&&visitOpen.id===s.id)){ sec.append(el('div',{class:'row'},el('button',{class:'btn sm',type:'button',id:'visit-add',onclick:()=>{ visitOpen={id:s.id,i:-1}; renderDetail(s); const n=$('#visit-form'); if(n) n.scrollIntoView({block:'nearest'}); }},list.length?'+ Another visit':'+ I was here')),
      list.length?null:el('p',{class:'snote',style:'display:block;margin-top:6px',text:'Been there? Say what you found and where it really is, then tap "Send to the public Atlas" on the report so the pin and the text get corrected for everyone.'}));
    return sec; }
  const old=visitOpen.i>=0?list[visitOpen.i]:null, d0=new Date(), today=d0.getFullYear()+'-'+String(d0.getMonth()+1).padStart(2,'0')+'-'+String(d0.getDate()).padStart(2,'0');
  let verdict=old?old.v:'';
  const chips=el('div',{class:'chips'},Object.keys(VISIT).map(k=>el('button',{class:'chip visit-v',type:'button','data-v':k,'aria-pressed':String(verdict===k),onclick:e=>{ verdict=k; chips.querySelectorAll('.chip').forEach(n=>n.setAttribute('aria-pressed',String(n.getAttribute('data-v')===k))); }},VISIT[k])));
  const tx=el('textarea',{id:'visit-x',placeholder:'A laid-stone cellar about 5 m square, a well 10 m east of it, apple trees…'}); tx.value=old?old.x||'':'';
  const ta=el('input',{type:'text',id:'visit-a',placeholder:'Parked at the gate on the forest road; posted on the east side',autocomplete:'off'}); ta.value=old?old.a||'':'';
  const td=el('input',{type:'date',id:'visit-t',max:today}); td.value=old?old.t:today;
  const farN=el('small',{class:'snote',id:'visit-far',style:'display:block'}), msg=el('span',{class:'note-saved',id:'visit-msg'});
  const R=(id,val,label,dis)=>{ const n=el('input',{type:'radio',name:'visit-at',id:id,value:val,disabled:!!dis}); n.addEventListener('change',upd); return el('label',{class:'lopt',for:id},n,el('span',null,label)); };
  const spot=()=>{ const k=(sec.querySelector('input[name="visit-at"]:checked')||{}).value; if(k==='me'&&geo.ll) return [+geo.ll[0].toFixed(6),+geo.ll[1].toFixed(6)]; if(k==='map'&&map){ const c=map.getCenter(); return [+c.lat.toFixed(6),+c.lng.toFixed(6)]; } if(k==='keep'&&old&&old.at) return old.at; return null; };
  function upd(){ const at=spot(); farN.textContent=at?'That is '+far(dist(at))+' from the Atlas pin. The pin on your map moves there when you save.':''; }
  const box=el('div',{id:'visit-form'},
    el('label',{class:'field'},el('span',{text:'What did you find?'}),chips),
    el('label',{class:'field',for:'visit-x',style:'margin-top:8px'},el('span',{text:'What is really there'}),tx),
    el('label',{class:'field',for:'visit-a',style:'margin-top:8px'},el('span',{text:'Access as you found it'}),ta),
    el('div',{class:'field',style:'margin-top:8px'},el('span',{text:'The true spot'}),
      R('visit-at-pin','pin','The pin is right, or I cannot say'),
      old&&old.at?R('visit-at-keep','keep','Keep the spot from this report'):null,
      R('visit-at-me','me','Where I am standing now',!geo.ll),
      map?R('visit-at-map','map','The middle of the map (move the map until the spot is dead centre)'):null,
      geo.ll?null:el('small',{class:'snote',style:'display:block',text:'For "where I am standing", tap Me under the map first.'}),farN),
    el('label',{class:'field',for:'visit-t',style:'margin-top:8px'},el('span',{text:'Date of the visit'}),td),
    el('div',{class:'row',style:'margin-top:10px'},
      el('button',{class:'btn pri',type:'button',id:'visit-save',onclick:()=>{ if(!verdict){ msg.textContent=' Choose what you found first.'; return; }
        const at=spot(), r={t:td.value||today,v:verdict,x:tx.value.trim(),a:ta.value.trim(),at:at};
        if(!U.visits[s.id]) U.visits[s.id]=[]; if(old) U.visits[s.id][visitOpen.i]=r; else U.visits[s.id].unshift(r);
        U.visits[s.id].sort((x,y)=>x.t<y.t?1:x.t>y.t?-1:0);
        if(['','todo','scouted','asked','ok',undefined].indexOf(U.status[s.id])>=0&&verdict!=='blocked') U.status[s.id]='visited';
        if(at&&dist(at)>4) U.moved[s.id]=at;
        visitOpen=null; saveNow(); refresh(); select(byId(s.id)||s,true); banner('Visit report saved. Tap "Send to the public Atlas" on it to share it.',false,6000); }},'Save the report'),
      el('button',{class:'btn',type:'button',onclick:()=>{ visitOpen=null; renderDetail(s); }},'Cancel'),msg));
  sec.append(box); sec.querySelector(old&&old.at?'#visit-at-keep':'#visit-at-pin').checked=true;
  /* the choice "where I am standing" opens up as soon as the phone knows where it is */
  if(!geo.ll){ const t=setInterval(()=>{ const n=document.getElementById('visit-at-me'); if(!n){ clearInterval(t); return; } if(geo.ll){ n.disabled=false; clearInterval(t); } },700); }
  return sec; }
/* the reports as they go to Claude: each with the place's name and the Atlas's own pin, so the list reads on its own */
function visitExport(){ const out=[]; Object.keys(U.visits||{}).forEach(id=>{ const s=byId(id), b=BASE.find(x=>x.id===id)||s; if(!s||!U.visits[id].length) return;
    out.push({id:id,name:s.name,town:s.town||'',cat:s.cat,pin:[b.lat,b.lon],mine:!!s.mine,reports:U.visits[id]}); }); return out; }

/* ---------- trip ---------- */
let trip={real:null,t0:'',day:''};
/* Where the Atlas's own time estimate for a trip begins: the reader's position while it is on, otherwise the start place if one
   was chosen, otherwise nowhere (the estimate is then between the stops only). The route handed to Google Maps names no start at
   all, so Google begins at the phone's position and offers Start; and nothing goes back to anywhere (the owner, November 21, 2026:
   the way home is one tap in Google Maps, and a route that began at fixed coordinates only offered a preview). */
function tripFrom(){ const a=nearFrom(); if(a) return {lat:a[0],lon:a[1],name:'where you are',live:true}; if(homePicked()){ const H=homeObj(); return {lat:H.lat,lon:H.lon,name:H.name}; } return null; }
/* sunrise and sunset for a calendar day at a place (the NOAA sunrise equation; good to a couple of minutes) */
function sunTimes(day,lat,lon){ const d=new Date(day+'T12:00:00'), J=Math.floor(d.getTime()/86400000)+2440587.5, n=Math.ceil(J-2451545.0+0.0008), js=n-lon/360, M=rad((357.5291+0.98560028*js)%360);
  const C=1.9148*Math.sin(M)+0.02*Math.sin(2*M)+0.0003*Math.sin(3*M), lam=rad((M*180/Math.PI+C+180+102.9372)%360), jt=2451545.0+js+0.0053*Math.sin(M)-0.0069*Math.sin(2*lam);
  const dec=Math.asin(Math.sin(lam)*Math.sin(rad(23.44))), cw=(Math.sin(rad(-0.833))-Math.sin(rad(lat))*Math.sin(dec))/(Math.cos(rad(lat))*Math.cos(dec)); if(cw>1||cw<-1) return null;
  const w=Math.acos(cw)*180/Math.PI/360, T=j=>new Date((j-2440587.5)*86400000); return {rise:T(jt-w),set:T(jt+w)}; }
/* the day by the clock: when you reach each stop, when you are done, and whether that is before sunset */
function tripClock(pts,st){ const d0=new Date(), pad=n=>String(n).padStart(2,'0'), today=d0.getFullYear()+'-'+pad(d0.getMonth()+1)+'-'+pad(d0.getDate());
  if(!trip.day) trip.day=today; if(!trip.t0){ const q=new Date(Math.ceil((d0.getTime()+5*60000)/900000)*900000); trip.t0=pad(q.getHours())+':'+pad(q.getMinutes()); }
  const stay=+pref('tripStop')||45, start=new Date(trip.day+'T'+trip.t0+':00'), legs=[], off=pts.length-st.length; for(let i=1;i<pts.length;i++) legs.push(trip.real&&trip.real.legs&&trip.real.legs.length===pts.length-1?trip.real.legs[i-1]:roughMin(hav(pts[i-1].lat,pts[i-1].lon,pts[i].lat,pts[i].lon)).min);
  const at=[]; let t=start.getTime(); st.forEach((s,i)=>{ const k=i-1+off; if(k>=0) t+=legs[k]*60000; at.push(new Date(t)); t+=stay*60000; });      /* off is 1 when the list begins with a starting point, 0 when it is the stops alone */
  const last=st[st.length-1], lp=pos(last), sun=sunTimes(trip.day,lp.lat,lp.lon); let late=-1; if(sun) at.forEach((a,i)=>{ if(late<0&&a.getTime()+stay*60000>sun.set.getTime()) late=i; });
  return {at:at,end:new Date(t),sun:sun,late:late,stay:stay,real:!!(trip.real&&trip.real.legs)}; }
const hm=d=>d.toLocaleTimeString([],{hour12:H12(),hour:'numeric',minute:'2-digit'});
function tripStops(){ return U.trip.map(byId).filter(Boolean); }
function legMiles(pts){ let m=0; for(let i=1;i<pts.length;i++) m+=hav(pts[i-1].lat,pts[i-1].lon,pts[i].lat,pts[i].lon); return m; }
function bestOrder(){
  const H=tripFrom(), st=tripStops(); if(st.length<3){ return; }
  const P=st.map(dest), n=P.length, used=new Array(n).fill(false); let cur=H||P[0], ord=[];      /* with no starting point the first stop stays first */
  for(let k=0;k<n;k++){ let b=-1,bd=1e9; for(let i=0;i<n;i++){ if(used[i]) continue; const d=hav(cur.lat,cur.lon,P[i].lat,P[i].lon); if(d<bd){bd=d;b=i;} } used[b]=true; ord.push(b); cur=P[b]; }
  const len=o=>legMiles((H?[H]:[]).concat(o.map(i=>P[i])));
  let improved=true, guard=0;
  while(improved&&guard++<60){ improved=false;
    for(let i=0;i<n-1;i++) for(let j=i+1;j<n;j++){ const o2=ord.slice(0,i).concat(ord.slice(i,j+1).reverse(),ord.slice(j+1)); if(len(o2)+1e-6<len(ord)){ ord=o2; improved=true; } } }
  U.trip=ord.map(i=>st[i].id); save(); trip.real=null;
}
function gmapsLinks(){
  const P=tripStops().map(dest), out=[], f=p=>p.lat.toFixed(5)+','+p.lon.toFixed(5);
  for(let i=0;i<P.length;i+=10){ const seg=P.slice(i,i+10), way=seg.slice(0,-1).map(f).join('|');      /* ten stops a link: nine on the way and the last as the destination */
    out.push('https://www.google.com/maps/dir/?api=1&destination='+f(seg[seg.length-1])+(way?'&waypoints='+encodeURIComponent(way):'')+'&travelmode=driving'); }
  return out;
}
function renderTrip(){
  const v=$('#v-trip'); v.textContent=''; const st=tripStops(), H=tripFrom();
  const box=el('div',{class:'pad',style:'padding-block:12px'}); v.append(box);
  box.append(el('h2',{style:'font-size:22px',text:'Trip builder'}),el('p',{style:'color:var(--mute);margin:4px 0 10px',text:'Add places from their pages, put them in order, then hand the route to Google Maps for live traffic and turn-by-turn.'}));
  if(!st.length){ box.append(el('p',{class:'empty',text:'No stops yet. Open a place and choose "Add to trip".'})); return; }
  const ul=el('ol',{class:'stops'}), pts0=(H?[H]:[]).concat(st.map(dest)), ck=tripClock(pts0,st);
  st.forEach((s,i)=>{ const mv=d=>()=>{ const j=i+d; if(j<0||j>=U.trip.length) return; const a=U.trip; const t=a[i]; a[i]=a[j]; a[j]=t; trip.real=null; save(); renderTrip(); };
    ul.append(el('li',null,el('span',null,el('button',{type:'button',style:'background:none;border:0;padding:0;font-weight:600;text-align:left;color:var(--ink)',onclick:()=>select(s,true)},s.name),el('small',{text:[s.town,EFF[s.eff],ACC[s.acc]].filter(Boolean).join(' · ')}),el('small',{class:'stop-at'+(ck.late>=0&&i>=ck.late?' late':''),text:'there about '+hm(ck.at[i])})),
      el('span',{class:'mv'},el('button',{class:'btn sm',type:'button','aria-label':'Move up',disabled:i===0,onclick:mv(-1)},'↑'),el('button',{class:'btn sm',type:'button','aria-label':'Move down',disabled:i===st.length-1,onclick:mv(1)},'↓'),el('button',{class:'btn sm',type:'button','aria-label':'Remove',onclick:()=>{U.trip.splice(i,1);trip.real=null;save();refresh();}},'✕')))); });
  box.append(ul);
  const pts=pts0, r=roughMin(legMiles(pts)), frm=H?' from '+H.name:' between the stops';
  const sum=el('p',{id:'trip-sum',style:'margin:10px 0'});
  if(trip.real) sum.append(el('b',{class:'mono',text:fmtMin(trip.real.min)}),' driving'+frm+', '+miTxt(trip.real.mi)+' by road, before stops and traffic.');
  else if(pts.length<2) sum.append('One stop and no starting point yet: turn on Me, or add a second stop, for a drive time.');
  else sum.append(el('b',{class:'mono',text:'~'+fmtMin(r.min)}),' driving'+frm+', about '+miTxt(Math.round(r.mi))+'. Rough estimate from straight-line distance.');
  box.append(sum);
  /* the clock */
  const dayI=el('input',{type:'date',id:'trip-day','aria-label':'Day of the trip',onchange:e=>{ if(e.target.value){ trip.day=e.target.value; renderTrip(); } }}), t0I=el('input',{type:'time',id:'trip-t0','aria-label':'Leaving at',onchange:e=>{ if(e.target.value){ trip.t0=e.target.value; renderTrip(); } }});
  dayI.value=trip.day; t0I.value=trip.t0;
  const stS=el('select',{id:'trip-stop','aria-label':'Time at each stop',onchange:e=>{ setPref('tripStop',+e.target.value); renderTrip(); }},[20,30,45,60,90,120].map(m=>el('option',{value:String(m),text:fmtMin(m)+' at each stop'}))); stS.value=String(ck.stay);
  const clk=el('div',{id:'trip-clock'},el('div',{class:'row'},el('label',{class:'field'},el('span',{text:'Day'}),dayI),el('label',{class:'field'},el('span',{text:'Leave at'}),t0I)),el('div',{class:'row',style:'margin-top:6px'},stS),
    el('p',{style:'margin:8px 0 0'},'Done about ',el('b',{class:'mono',text:hm(ck.end)}),ck.sun?'. Sunset at the last stop is '+hm(ck.sun.set)+'.':'.',ck.real?'':' Times use rough drive estimates until you tap "Get real drive time".'));
  if(ck.late>=0) clk.append(el('p',{class:'pn trip-warn',text:(ck.at[ck.late].getTime()>ck.sun.set.getTime()?'You would reach '+st[ck.late].name+' after sunset.':'Sunset comes while you are at '+st[ck.late].name+'.')+' Leave earlier, shorten the stops or drop a stop.'}));
  box.append(clk);
  const real=el('button',{class:'btn',type:'button',disabled:pts.length<2,onclick:async()=>{ real.disabled=true; real.textContent='Checking…';
    try{ const c=pts.map(p=>p.lon.toFixed(5)+','+p.lat.toFixed(5)).join(';'); const j=await (await fetch('https://router.project-osrm.org/route/v1/driving/'+c+'?overview=false')).json(); if(j.code!=='Ok') throw 0;
      trip.real={min:Math.round(j.routes[0].duration/60),mi:Math.round(j.routes[0].distance/1609.34),legs:(j.routes[0].legs||[]).map(l=>l.duration/60)}; renderTrip(); }
    catch(e){ real.disabled=false; real.textContent='Routing service unreachable. Use Google Maps'; } }},'Get real drive time');
  box.append(el('div',{class:'row',style:'margin-top:10px'},el('button',{class:'btn',type:'button',disabled:st.length<3,onclick:()=>{bestOrder();renderTrip();}},'Shortest order'),real));
  const links=gmapsLinks(); const lr=el('div',{class:'row',style:'margin-top:10px'});
  links.forEach((u,i)=>lr.append(ext(u,links.length>1?'Google Maps, part '+(i+1):'Open route in Google Maps','btn pri'))); box.append(lr);
  if(links.length>1) box.append(el('p',{style:'color:var(--mute);font-size:12.5px',text:'Google Maps takes ten stops per route, so long trips are split.'}));
  const cp=el('button',{class:'btn sm',type:'button'},'Copy stop list'); cp.addEventListener('click',()=>copy(st.map((s,i)=>(i+1)+'. '+s.name+' ('+s.town+') '+ll(dest(s))).join('\n'),cp));
  box.append(el('div',{class:'row',style:'margin-top:10px'},cp,el('button',{class:'btn sm',type:'button',onclick:()=>{U.trip=[];trip.real=null;save();refresh();}},'Clear trip')));
  if(map&&!schematic) box.append(el('h3',{class:'lbl',style:'display:block;margin-top:16px',text:'Take the whole trip offline'}),offlineBox('trip:'+U.trip.join(','),st.map(pos),'Trip: '+st.map(x=>x.name).join(', ')));
  if(st.some(s=>s.acc!=='public')) box.append(el('p',{class:'pn',style:'margin-top:12px',text:'Heads up: '+st.filter(s=>s.acc!=='public').map(s=>s.name+' ('+ACC[s.acc].toLowerCase()+')').join('; ')+'.'}));
}

/* ---------- guide ---------- */
let guideBuilt=false;
/* Backups, where the app gets its places, and offline storage: shown at the end of Settings. */
function dataSections(v){
  const sec=(title,open,kids)=>{ const b=el('div',{class:'gb'}); kids.forEach(k=>k&&b.append(k)); return el('details',{class:'pad',open:open},el('summary',{text:title}),b); };
  const P=t=>el('p',{text:t});
  /* your data */
  const out=el('textarea',{id:'bk-out',readOnly:true,style:'min-height:90px;font-family:var(--fm);font-size:11.5px'});
  const dump=()=>JSON.stringify(U);
  const b1=el('button',{class:'btn sm',type:'button'},'Copy backup'); b1.addEventListener('click',()=>{ out.value=dump(); copy(out.value,b1); });
  const b2=el('button',{class:'btn sm',type:'button',onclick:()=>{ out.value=dump(); try{ const a=el('a',{href:URL.createObjectURL(new Blob([out.value],{type:'application/json'})),download:'lost-hidden-atlas-backup.json'}); document.body.append(a); a.click(); a.remove(); }catch(e){} }},'Save backup file');
  const b3=el('button',{class:'btn sm',type:'button'},'Copy my additions for Claude'); b3.addEventListener('click',()=>{ const t=JSON.stringify({added:U.custom,movedPins:U.moved,notes:U.notes,progress:U.status,visits:visitExport(),spots:spotExport()},null,1); out.value=t; copy(t,b3); });
  const inp=el('textarea',{id:'bk-in',placeholder:'Paste a backup here',style:'min-height:60px;font-family:var(--fm);font-size:11.5px'});
  const msg=el('span',{class:'note-saved'});
  const load=txt=>{ try{ const j=JSON.parse(txt); if(!j||typeof j!=='object'||!('status' in j)) throw 0; U=Object.assign(U0(),j); U.ui=Object.assign(U0().ui,j.ui||{}); if(!LD[U.ui.base]) U.ui.base='streets'; if(!U.me) U.me={}; aliasMigrate(); save(); applyTheme(); drawScale(); pushPrefs(); buildHome(); drawHome(); refresh(); msg.textContent='Restored.'; }catch(e){ msg.textContent='That does not look like an Atlas backup.'; } };
  const file=el('input',{type:'file',id:'bk-file',accept:'.json,application/json',onchange:e=>{ const f=e.target.files[0]; if(!f) return; const r=new FileReader(); r.onload=()=>load(String(r.result)); r.readAsText(f); }});
  const bkf=NATIVE?(()=>{ const m2=el('span',{class:'note-saved'}), b=el('button',{class:'btn sm',type:'button'},'Save a backup file now'); b.addEventListener('click',()=>{ m2.textContent=' Saving…'; backupFile().then(r=>{ m2.textContent=' Saved to '+r.where+'.'; },e=>{ m2.textContent=' '+((e&&e.message)||'Could not save.'); }); });
    return el('div',null,P('The app also saves a backup file by itself each time a field log ends: Download / Lost Hidden Atlas / atlas-backup.json on the phone. It stays there if the app is removed. To bring it back, use "Restore" below and pick that file.'),el('div',{class:'row'},b,m2)); })():null;
  v.append(sec('Your data and backups',false,[bkf,
    P('Your progress, notes, moved pins, added places and trip are saved in this browser on this device only. They do not sync. Back them up before you clear browser data, and restore on another device.'),
    el('div',{class:'row'},b1,LOCAL?b2:null,b3),out,
    el('label',{class:'field',for:'bk-in',style:'margin-top:10px'},el('span',{text:'Restore'}),inp),
    el('div',{class:'row',style:'margin-top:6px'},el('button',{class:'btn sm',type:'button',onclick:()=>load(inp.value)},'Restore from pasted text'),file,msg),
    P('To grow the master list, use "Copy my additions for Claude" and paste it into a chat. Claude can fold them into the Atlas with drive times and old-map overlays. It carries your visit reports too: what you found at each place and where it really is.')]));
  if(AT){ const info=el('p'), res=el('span',{class:'note-saved'}), addr=el('input',{type:'url',id:'at-base','aria-label':'Atlas address',autocomplete:'off'}); addr.value=AT.base;
    const show=()=>{ info.textContent='Place data: build '+AT.dataV+(AT.fromCache?', downloaded from the address below.':', as built into the app.')+(AT.pending?' Build '+AT.pending+' is downloaded and loads the next time the app starts.':''); };
    const run=()=>{ res.textContent=' Checking…'; return AT.check().then(r=>{ show(); res.textContent=r.state==='same'?' You have the latest.':' New data downloaded'+(r.places?' ('+r.places+' places)':'')+'.'; if(r.state!=='same') res.append(' ',el('button',{class:'btn sm',type:'button',onclick:()=>location.reload()},'Load it now')); },
      e=>{ res.textContent=' '+(navigator.onLine===false?'No signal.':'Could not read that address: '+((e&&e.message)||'no answer')+'.'); }); };
    show();
    v.append(sec('Where the app gets its places',false,[
      P('The app works with no signal using the places built into it. When it has a connection it looks for newer places, lines and leads at the address below and keeps them on the phone.'),
      info,el('div',{class:'row'},el('button',{class:'btn sm',type:'button',onclick:run},'Check for new places'),res),
      el('label',{class:'field',for:'at-base',style:'margin-top:10px'},el('span',{text:'Atlas address'}),addr),
      el('div',{class:'row',style:'margin-top:6px'},
        el('button',{class:'btn sm',type:'button',onclick:()=>{ if(!AT.setBase(addr.value)){ res.textContent=' That is not a web address.'; return; } addr.value=AT.base; run(); }},'Use this address'),
        el('button',{class:'btn sm',type:'button',onclick:()=>{ AT.setBase(AT.def); addr.value=AT.base; run(); }},'Back to the original')),
      NATIVE?(()=>{ const line=el('p',{class:'mono',style:'font-size:12px',text:'App status: reading…'}), cb=el('button',{class:'btn sm',type:'button'},'Copy app status'); let last='';
        AT.call('status').then(st=>{ last=JSON.stringify(Object.assign({data:AT.dataV,base:AT.base},st)); line.textContent='App '+(st.version||'?')+' · Android API '+st.android+' · '+st.phone+' · location '+(st.fine?'allowed':'NOT allowed')+(st.background?' (all the time)':'')+' · battery '+(st.battery?'unrestricted':'restricted')+' · photos '+(st.media||'?')+' · GPS '+(st.gps?'on':'OFF')+(st.recording?' · recording: '+st.fixes+' fixes, '+st.kept+' kept, last '+st.lastFixAgo+' s ago at '+Math.round(st.lastAccuracy)+' m':'')+(st.error?' · last error: '+st.error:''); },()=>{ line.textContent='App status could not be read.'; });
        cb.addEventListener('click',()=>copy(last||line.textContent,cb)); return el('div',null,line,el('div',{class:'row'},cb)); })():null,
      P('Change the address only if the Atlas moves to a new home. The new site must be a copy of this one and must allow other sites to read it (the Access-Control-Allow-Origin header).')])); }
  const stor=el('p',{text:'Checking…'}), sl=el('ul',{class:'links'});
  const fillStor=async()=>{ await tcScan(); let q=''; try{ const e=await navigator.storage.estimate(); if(e&&e.quota) q=' This browser allows the Atlas about '+mb(e.quota)+'.'; }catch(x){}
    stor.textContent='Saved for offline: '+TC.pinN+' tiles, '+mb(TC.pinSize)+'. Recently viewed: '+mb(TC.size)+' (oldest dropped past 150 MB).'+q;
    sl.textContent=''; Object.keys(U.saved).forEach(k=>{ const a=U.saved[k]; sl.append(el('li',{text:(a.label||k)+' · '+a.mb+' · '+new Date(a.at).toLocaleDateString()})); }); };
  const clr=el('button',{class:'btn sm',type:'button'},'Delete all saved map tiles'); let armed=false;
  clr.addEventListener('click',async()=>{ if(!armed){ armed=true; clr.textContent='Really delete them?'; setTimeout(()=>{armed=false;clr.textContent='Delete all saved map tiles';},4000); return; } await tcClear(); U.saved={}; save(); armed=false; clr.textContent='Delete all saved map tiles'; fillStor(); });
  const offSec=sec('Offline maps and storage',false,[P('The Atlas keeps a copy of every leaf-off, LiDAR, topo and lot-line tile it loads, so zooming back out or coming back to a place is instant. Areas you save from a place page or the trip are kept until you delete them.'),stor,sl,el('div',{class:'row'},clr),
    P('For offline use, open the Atlas from the downloaded file or your own web address, not the online copy in Claude. On iPhone, Safari may clear saved tiles if you do not open the Atlas for a few weeks; adding it to your Home Screen helps.')]);
  if(HOSTED){ const all=BASE.filter(x=>x.tm), ab=el('button',{class:'btn sm',type:'button'},'Keep every old map on this phone ('+all.length+' maps, about '+Math.round(all.length*0.031)+' MB)'), am=el('span',{class:'note-saved'});
    ab.addEventListener('click',async()=>{ ab.disabled=true; let ok=0,bad=0; for(let i=0;i<all.length;i+=6){ await Promise.all(all.slice(i,i+6).map(x=>(AT?topoSrc(x).then(u=>!!u):fetch(topoImg(x)).then(r=>r.ok,()=>false)).then(good=>{ if(good) ok++; else bad++; }))); am.textContent=' '+(ok+bad)+' of '+all.length; } am.textContent=' Done: '+ok+' kept'+(bad?', '+bad+' failed':'')+'.'; ab.disabled=false; });
    offSec.lastChild.append(el('p',{text:(AT?'The app opens with no signal: the place list, lines and leads are built in.':'This hosted copy keeps itself on the phone after the first visit, so it opens with no signal.')+' Old survey maps are fetched one place at a time as you open them; saving a place for offline keeps its old map too.'+(LX?' Old rail and canal lines are fetched one state at a time, when the map or a place page first goes there, and then kept; saving a place for offline fetches its state.':'')}),el('div',{class:'row'},ab,am)); }
  offSec.addEventListener('toggle',()=>{ if(offSec.open) fillStor(); }); v.append(offSec);
}
function renderGuide(){
  if(guideBuilt) return; guideBuilt=true;
  const v=$('#v-guide'); const sec=(title,open,kids)=>{ const b=el('div',{class:'gb'}); kids.forEach(k=>k&&b.append(k)); return el('details',{class:'pad',open:open},el('summary',{text:title}),b); };
  const P=t=>el('p',{text:t});
  const cats=el('div',{class:'legend'}); Object.keys(CAT).forEach(k=>cats.append(el('span',null,el('span',{class:'dot',style:'--c:'+CAT[k][1]}),CAT[k][0])));
  const shapes=el('div',{class:'legend',style:'margin-top:8px'},
    el('span',null,el('span',{class:'dot star',style:'--c:#666'}),'Star: still standing'),
    el('span',null,el('span',{class:'dot',style:'--c:#666'}),'Solid circle: ruins or traces'),
    el('span',null,el('span',{class:'dot hollow',style:'--c:#666'}),'Ring: nothing left, a marker, or under water'),
    el('span',null,el('span',{class:'dot mine',style:'--c:#666'}),'Diamond: a place you added'));
  v.append(sec('How to find a ruin with this',true,[
    P('Every pin carries an honest rating. "Pin on the spot" means it sits on the structure or marker. "Pin within the site" means it is inside the footprint. "Pin approximate" means the right vicinity only, and the dashed ring on the map shows how far off it could be.'),
    el('ul',null,
      el('li',{text:'Pick a place, then tick "Lay the old USGS map over the pin." Sheets from the 1890s to 1930s draw the hotels, trolley spurs and villages that are gone.'}),
      el('li',{text:'Switch the map to Leaf-off aerial. Where a state flies in early spring, foundations and cellar holes show through bare trees.'}),
      el('li',{text:'Switch to LiDAR, zoom in, and change the light direction under More. Walls, canal prisms, rail grades and coaster footings stand out as straight lines no forest makes.'}),
      el('li',{text:'Tap Compare to swipe aerial against LiDAR. Turn on Public land and tap Owner? to see whose ground it is before you go.'}),
      el('li',{text:'Follow the lines. Old railroads, trolley lines and canals are drawn on the map; stations, mills, hotels and locks sat right beside them. Click a line to list the Atlas places along it in order, then walk the rest of it on LiDAR looking for platforms and foundations.'}),
      el('li',{text:'On site, open the Log tab and start a field log. It draws where you walk and lets you drop timed notes, then exports the track (GPX) and a note list with times to match against your footage.'}),
      el('li',{text:'Found the real spot? Open My notes, choose "Move the pin," and drag it. Right-click (or long-press) anywhere on the map for coordinates and links.'}),
      el('li',{text:'Been to a place? Open it and tap "I was here": say what you found, how you got in, and mark the true spot from where you stand. Then tap "Send to the public Atlas" on the report and the map gets corrected for everyone.'}),
      el('li',{text:'Know a place that is not on the map? Tap "+ Add", put the cross on it, tap what it is, then open its pin and tap "Send to the public Atlas". You do not need to research it: the spot is enough, and it is looked into later. A place that began this way carries the badge "Sent in by a reader", and Filters can show only those. No name is ever shown.'})),
    el('div',{id:'share-blank'},el('p',{class:'snote',style:'display:block;margin-top:8px',text:'Or send a place without a pin:'}),shareBox('lead',{place:'',where:'',text:'',source:'',access:''})),
    cats,shapes,el('div',{class:'legend',style:'margin-top:8px'},Object.keys(LK).map(k=>el('span',null,el('span',{class:'sw'+(LK[k][2]?' dash':''),style:'--c:'+LK[k][1]}),LK[k][0])))]));
  v.append(sec('Near me: what is close, and a buzz when you pass it',false,[
    P('The Near tab lists everything on file within a few miles of where you stand, nearest first: the places, the unchecked leads, vanished places, old mines and quarries, and old town centres. Each row has an arrow, a distance and a compass direction. Tap a row and the top of the tab turns into one big arrow and distance for that spot, with a dashed line to it on the map. Tap Stop to let it go.'),
    P('If the phone has a compass the arrows turn as you turn, so the arrow points the way to walk from the top of the phone. Without one, arrows are map directions: up is north, the same as the map.'),
    P('With an alert distance set, the phone buzzes and a notice shows when you come within that distance of a place or lead. It fires once for each spot, and again only after you have walked well away and come back. Old town centres are listed but never set it off.'),
    P(NATIVE?'With the screen off, the buzz works only while a field log is recording, because the recorder is what keeps the GPS running. The notification then names what you are near. The app gives the recorder everything within 25 miles each time it is opened.':'In a browser the alert works only while this page is open, the screen is on and location is switched on. In the Android app it also works with the screen off while a field log is recording.'),
    P('Lead positions are rough. A vanished place or an old mine can be a hundred metres or more from its dot, so treat the buzz as "look around here", and check whose land it is before you leave the trail.')]));
  v.append(sec('Episode kit: from a walk to a video',false,[
    P('Every finished field log has an Episode kit button. It works out which Atlas places the walk came to, in the order you reached them, and puts the clips, photos and notes from the walk under each one.'),
    el('ul',null,
      el('li',{text:'YouTube chapters: where each place starts, counted as if your clips were joined end to end in the order shot with nothing cut. They are a draft; shift them to match your edit. With fewer than three places, your notes become chapters too.'}),
      el('li',{text:'A description: what each place is, how far you walked, what to know before going, and the sources from each place page.'}),
      el('li',{text:'The whole kit as one text file, with the time inside each clip where each place, photo and note falls.'}),
      el('li',{text:'A route map picture, 1920 by 1080, with the stops numbered. It is drawn on the USGS base map, which is in the public domain, so it is safe to put in a video.'})),
    P('The picture and the distance respect "Trim the ends of a shared walk" in Settings, so they need not show where you parked. Clips and photos are matched to a walk only in the Android app.')]));
  const air=el('div',{class:'tk'}); D.aerial.forEach(t=>air.append(el('div',null,ext(t[2],t[0]),el('span',{text:t[1]}))));
  v.append(sec('Old air photos and maps',false,[P('No free service streams 1940s–50s air photos for this region as a map layer, so the Atlas builds in what can be streamed (state flights back to the 1990s, LiDAR, and scanned USGS sheets) and links out for the rest. Every place page has an "Old air photos" button that opens the spot in Historic Aerials.'),air]));
  const tk=el('div',{class:'tk'}); D.toolkit.forEach(t=>tk.append(el('div',null,ext(t[2],t[0]),el('span',{text:t[1]}))));
  v.append(sec('Research toolkit',false,[tk,el('p',{style:'margin-top:10px'},el('b',{text:'Five tells of a lost building: '}),D.tells.join(' '))]));
  const rules=el('ul'); D.rules.forEach(r=>rules.append(el('li',{text:r})));
  v.append(sec('Rules of the road',false,[rules]));

  const UL=a=>el('ul',null,a.map(t=>el('li',{text:t})));
  v.append(sec('Access, permission and the law',false,[
    P('Condensed from your field manual. General information, not legal advice; statutes change and the facts of each case matter.'),
    UL(['Open land: under Penal Law §140.00(5) you are lawfully on "unimproved and apparently unused land" that is neither fenced nor posted, until the owner tells you to leave.',
      'Fences, posted signs and buildings change that. Entering a building, or land fenced to keep people out, without permission is criminal trespass (§140.10, a class B misdemeanor). Plain trespass (§140.05) is a violation.',
      'How it gets worse: taking a souvenir, forcing a door or carrying pry tools can turn a trespass into burglary (§140.20, a class D felony) or possession of burglar\'s tools (§140.35).',
      'Posted land stays posted for a year even if someone tears the signs down (ECL §11-2111).',
      'Railroads in use are private property with their own police. Stay off them, and out of tunnels.']),
    el('p',null,el('b',{text:'Massachusetts is different: '}),'the open-land rule above is New York law and does not carry over. Massachusetts treats entering or staying on land or in buildings after being forbidden, in person or by a posted notice, as criminal trespass (M.G.L. c. 266, §120). State parks and forests there are run by DCR, which has its own permit rules for commercial filming and drones. Read the current text before a Massachusetts trip.'),
    el('p',null,el('b',{text:'Rhode Island: '}),'the New York open-land rule does not carry over here either. Rhode Island makes it a crime to trespass willfully, or to stay on land with no legitimate purpose, after the owner or the owner\'s agent has forbidden it (R.I. Gen. Laws §11-44-26: up to a $1,000 fine, up to a year in jail, or both). State parks and management areas are run by DEM. Owner lookup and lot lines are not built for Rhode Island yet; ask the town assessor. Read the current text before a Rhode Island trip.'),
    el('p',null,el('b',{text:'Everywhere else: '}),'the rules differ again in every other state and in each Canadian province. This guide has notes only for '+STATES.filter(st=>st.legal).map(st=>st.name).join(', ')+', so look up the trespass law of the state or province before a trip there.'),
    el('p',null,el('b',{text:'Bright-line rules: '}),'No buildings without permission. Never cross a fence or pass a posted sign without permission. Never take anything. Carry nothing that looks like an entry tool. Leave as soon as you are asked.'),
    el('p',null,el('b',{text:'If someone approaches: '}),'stop filming if asked, explain honestly what you are doing, show ID, and leave by the shortest route. Show your permission letter and the owner\'s number if you have them. Do not run, hide, argue or lie.'),
    el('p',null,el('b',{text:'Asking: '}),'every place page has "Whose land is it?" with an owner lookup and a permission letter you can copy. Set the place to "Asked the owner" or "Have permission" under My notes to keep track.')]));
  v.append(sec('State land, filming and drones',false,[
    UL(['Nothing leaves state land. 6 NYCRR 190.8(g) bars removing or damaging anything of archaeological interest, so a bottle or a rail spike stays where it lies.',
      'Monetized filming on DEC land needs a Temporary Revocable Permit: $25, applied for at least 30 days ahead, 60 for the Forest Preserve.',
      'State parks and historic sites need a Photography/Film Permit for commercial or publicity filming; allow about 14 days.',
      'Drones: a monetized channel flies under FAA Part 107 with Remote ID. DEC allows hobby flights over Wild Forest and State Forest, bans drones in Wilderness, Primitive and Canoe areas, and wants a permit for commercial flights. State parks need written approval for any launch or landing.',
      'Respect closures and "do not enter the ruins" notices; DEC has asked visitors to stay out of the Overlook Mountain House shell.']),
    P('Check the unit\'s own page before each trip. The Public land layer and the "Land" line on a place page tell you which unit you are on.')]));
  v.append(sec('Safety checklist',false,[
    UL(['Never go alone. Leave a written plan with the site, the parking spot and a check-in time.',
      'Expect no signal in the mountains and deep woods. Save the area offline from the place page and carry a satellite messenger.',
      'Stay out of mines, adits, tanks and other confined spaces.',
      'Indoors, with permission: test floors near the walls, stay off roofs and stairs, and assume asbestos, lead paint, mold and guano. Wear a P100 half-face respirator, not a dust mask.',
      'Check DEC remediation listings before visiting old industrial sites.',
      'Blaze orange in the fall deer seasons. Tick check afterwards.',
      'Boots with shank soles, gloves, a headlamp and a spare, and a first-aid kit.'])]));
  const fo=el('div',{class:'tk'}); [
    ['Old Fulton NY Post Cards','Millions of scanned New York newspaper pages. Search a mill or hotel name with "fire", "auction" or "abandoned".','https://fultonhistory.com/'],
    ['NYS Historic Newspapers','Free county-by-county newspaper archive.','https://nyshistoricnewspapers.org/'],
    ['CRIS: state historic records','National Register nominations and survey forms with plans, dates and owners. Enter as a guest.','https://cris.parks.ny.gov/'],
    ['NYS entity search','Find the people behind an LLC that owns a site.','https://apps.dos.ny.gov/publicInquiry/'],
    ['Abandoned Rails','Histories of abandoned lines, to pair with the rail layer.','https://www.abandonedrails.com/'],
    ['OpenRailwayMap','Abandoned and razed lines as mapped by volunteers.','https://www.openrailwaymap.org/']
  ].forEach(t=>fo.append(el('div',null,ext(t[2],t[0]),el('span',{text:t[1]}))));
  v.append(sec('Finding owners and stories',false,[
    P('Every New York city, town and village must appoint a historian. They know where the ruins are and usually who owns them, so ask "what was here?" rather than "how do I get in?"'),
    fo,
    el('p',null,el('b',{text:'Sharing locations: '}),'name public-land sites openly, since that sends viewers somewhere legal. For fragile private sites, name the region and not the route, or hold the video until the owner is on side.')]));
  v.append(sec('Add places with your own Claude',false,[P('The Atlas grows by research sessions: a Claude session reads the sources, looks at every pin on the aerial and sends its places in. If you have Claude with Claude Code, yours can do the same for any town or county you choose, on your own account. Nothing of it reaches the map until the owner of the Atlas has looked at it. To tell us about a single place, "+ Add" and then "Send to the public Atlas" on its page is quicker.'),
    el('div',{class:'row'},ext('https://github.com/Mrroot3r/Lost-and-Hidden-Atlas/blob/main/CONTRIBUTING.md','How to add places with your own Claude','btn sm'))]));
  v.append(sec('Settings, backups and storage',false,[P('Backups, restoring, offline map storage and the app\'s own settings are under the gear: tap More under the map, then the gear next to Done.'),
    el('div',{class:'row'},el('button',{class:'btn sm',type:'button',onclick:()=>openSettings()},'Open Settings')),P('Settings holds: colours, units and clock; how the map opens and your start place; Near me (how far to list, when to buzz); the field log; the episode kit; trimming a shared walk; backups; where the app gets its places; offline storage.'),
    el('div',{class:'row'},el('button',{class:'btn sm',type:'button',onclick:()=>{ openSheet(); showSettings(true); }},'Open settings'))]));
  v.append(sec('About this data',false,[
    P(BASE.length+' places, built '+D.built+'. '+BASE.filter(s=>s.tm).length+' have an old USGS map overlay. Pins: '+BASE.filter(s=>s.prec==='exact').length+' exact, '+BASE.filter(s=>s.prec==='site').length+' on site, '+BASE.filter(s=>s.prec==='area').length+' approximate.'),
    P('Drive times from the listed start cities were calculated by road with no traffic, so add a little. A place more than about 450 miles from your start city, or with no road to it, shows a rough estimate marked ~. Pick your own start point from "Drive times from."'),
    P('Later batches added '+BASE.filter(s=>s.new).length+' places: '+BATCHES.map(b=>b.label+' ('+b.n+')').join(', ')+'. Their pins come from the source named in each pin note and many were not checked on imagery, so read the pin note before you drive.'),
    P('Histories come from the Lost & Hidden catalogue and its linked sources. "Lead" entries were not re-checked against a source. Hours, access rules and demolition schedules change, so confirm before you drive.'),
    P('Imagery: New York State ITS Geospatial Services (orthoimagery and LiDAR), MassGIS and the Vermont Center for Geographic Information (their own spring flights and LiDAR), RIGIS and the University of Rhode Island Environmental Data Center (Rhode Island March 2026 aerials and 2022 LiDAR), the New Jersey Office of GIS (2020 aerials), CT ECO at the University of Connecticut (spring 2023 aerials and LiDAR), NH GRANIT at the University of New Hampshire (2021 and 2022 aerials, LiDAR), the Pennsylvania Emergency Management Agency through PASDA at Penn State (2021 to 2023 aerials), the Maine GeoLibrary (aerials and LiDAR), the Kansas NG911 program through the Kansas Geological Survey (2024 aerials), USGS (topographic maps, The National Map, and the 3DEP ground model: it is the LiDAR layer in every state without its own, and the stone walls and LiDAR finds in Massachusetts were read from it), Esri and its data partners (streets and satellite). Rail and canal lines: OpenStreetMap contributors and OpenHistoricalMap (old lines), U.S. DOT North American Rail Network (lines in use); volunteer-mapped, so a missing line does not mean no line. Historic pockets: marker titles and positions from HMdb.org, the Historical Marker Database (hmdb.org), which the Atlas holds only in part for the busiest counties; National Register of Historic Places listings from the National Park Service, with positions corrected from Wikidata; town and village centres from OpenStreetMap contributors. The score shown on a pocket is a rough guide worked out by the Atlas, not a rating from any of these sources. Old lines are drawn for New York, the six New England states, New Jersey and Pennsylvania so far; other places have none yet. Public land: USGS Protected Areas Database (PAD-US), which can miss small local parks and lags new purchases. Owners and lot lines: NYS tax parcel file, NYS DEC and MassGIS property tax parcels; not every New York county shares owner names, and none of it is a survey. Leads: OpenStreetMap contributors, unchecked. Vanished places: U.S. Board on Geographic Names, Geographic Names Information System file of August 2021, unchecked. Old mines and quarries: U.S. Geological Survey Mineral Resources Data System, unchecked. Vector outline: Natural Earth. Routing: OSRM and OpenStreetMap contributors.')]));
}
function fitVisible(){ if(!map||!visible.length) return; const b=L.latLngBounds(visible.map(s=>{const p=pos(s);return [p.lat,p.lon];})); map.fitBounds(b.pad(0.15),{maxZoom:14}); }

/* ---------- wiring ---------- */
function buildHome(){
  const h=$('#home'); h.textContent='';
  if(!homePicked()) h.append(el('option',{value:'',text:'Not chosen yet'}));
  STATES.forEach(st=>{ const hs=HUBS.filter(x=>x.st===st.k); if(hs.length) h.append(el('optgroup',{label:st.name},hs.map(x=>el('option',{value:x.id,text:x.name})))); });
  HUBS.filter(x=>!x.st).forEach(x=>h.append(el('option',{value:x.id,text:x.name})));
  if(U.home.id==='custom') h.append(el('option',{value:'custom',text:(U.home.name||'My spot')+' ('+U.home.lat.toFixed(3)+', '+U.home.lon.toFixed(3)+')'}));
  h.append(el('option',{value:'pick',text:'Pick a spot on the map…'}));
  h.value=homePicked()?U.home.id:'';
}
$('#home').addEventListener('change',e=>{
  const v=e.target.value; if(v==='') return;
  if(v==='pick'){ const was=homePicked()?U.home.id:''; if(!map){ e.target.value=was; return; } pickingHome=true; stage.classList.add('adding'); $('#addbar').hidden=false; $('#addbar span').textContent='Click the map where you start from.'; e.target.value=was; return; }
  if(v==='custom') return;
  U.home={id:v,by:1}; save(); buildHome(); drawHome(); refresh(); if(sel) renderDetail(sel); { const H=homeObj(); if(map&&e.go) map.setView([H.lat,H.lon],10); }
});
/* The search box also goes to a spot (the owner, November 23, 2026: find a street in Google Maps, copy the coordinates, paste them
   here and be taken there). Coordinates, or a Google Maps link that carries them, move the map at once and are not a search of the
   places. Words still narrow the list as before, and a row under the box offers to look them up as a street, town or address:
   one question to OpenStreetMap's Nominatim, asked only on that tap or on Enter, never as you type (its rules forbid that). */
function readCoords(t){ t=String(t||'').trim(); if(!t) return null; let m, la, lo;
  if(/^https?:\/\//i.test(t)){ m=t.match(/!3d(-?\d+(?:\.\d+)?)!4d(-?\d+(?:\.\d+)?)/)||t.match(/[?&](?:q|ll|query|center|destination|viewpoint)=(-?\d+(?:\.\d+)?)(?:,|%2C)\s*(-?\d+(?:\.\d+)?)/i)||t.match(/@(-?\d+(?:\.\d+)?),(-?\d+(?:\.\d+)?)/); if(!m) return null; la=+m[1]; lo=+m[2]; }
  else { m=t.match(/^\(?\s*(-?\d{1,2}\.\d+|-?\d{1,2})\s*°?\s*([NS])?\s*[,;\s]\s*(-?\d{1,3}\.\d+|-?\d{1,3})\s*°?\s*([EW])?\s*\)?$/i); if(!m) return null;
    if(m[1].indexOf('.')<0&&m[3].indexOf('.')<0) return null;                     /* "12 34" is not a place on the map */
    la=+m[1]; lo=+m[3]; if(m[2]&&/s/i.test(m[2])) la=-la; if(m[4]&&/w/i.test(m[4])) lo=-Math.abs(lo); }
  if(lo>0) lo=-lo;                                                                /* everything the Atlas covers is west of Greenwich */
  if(!isFinite(la)||!isFinite(lo)||!inMap(la,lo)) return null;
  return {lat:la,lon:lo}; }
let goMark=null, goSeq=0;
function goClear(){ if(goMark&&map) map.removeLayer(goMark); goMark=null; }
function goTo(la,lo,label,box){ if(!map) return; goClear(); ctxClose();
  if(box&&box.length===4&&isFinite(+box[0])&&Math.abs(box[1]-box[0])<0.5&&Math.abs(box[3]-box[2])<0.5) map.fitBounds([[+box[0],+box[2]],[+box[1],+box[3]]],{maxZoom:17,animate:false}); else map.setView([la,lo],Math.max(map.getZoom(),16),{animate:false});
  goMark=L.circleMarker([la,lo],{radius:11,color:'#ff2d95',weight:4,fillColor:'#ff2d95',fillOpacity:.15,className:'gomark',bubblingMouseEvents:false}).addTo(map);
  if(label) goMark.bindTooltip(label,{direction:'top',offset:[0,-10]});
  goMark.on('click',()=>onContext({latlng:L.latLng(la,lo)}));                     /* the small box: add it, send it, see it in other maps */ }
function goRow(html,fn){ const b=el('button',{class:'btn sm',type:'button'}); b.innerHTML=html; b.addEventListener('click',fn); return b; }
const esc=t=>String(t).replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
function goShort(name){ return String(name||'').split(',').map(x=>x.trim()).filter(x=>x&&!/^\d{5}(-\d{4})?$/.test(x)&&!/^(United States|Canada)$/i.test(x)&&!/^[A-Z]\d[A-Z] ?\d[A-Z]\d$/.test(x)).slice(0,4).join(', '); }
async function goLook(q){ const g=$('#goto'), my=++goSeq; g.replaceChildren(el('p',{class:'gonote',text:'Looking up "'+q+'"…'}));
  let j=null; try{ const b=map?map.getBounds():null, vb=b?'&viewbox='+[b.getWest(),b.getNorth(),b.getEast(),b.getSouth()].map(x=>x.toFixed(4)).join(','):'';
    const r=await fetch('https://nominatim.openstreetmap.org/search?format=jsonv2&limit=4&countrycodes=us,ca'+vb+'&q='+encodeURIComponent(q)); j=await r.json(); }catch(e){ j=null; }
  if(my!==goSeq) return;
  if(!j){ g.replaceChildren(el('p',{class:'gonote',text:'Could not look that up (no connection?). Pasted coordinates work without one.'})); return; }
  const hits=j.filter(x=>inMap(+x.lat,+x.lon));
  if(!hits.length){ g.replaceChildren(el('p',{class:'gonote',text:'Nothing found on the map for "'+q+'". Try adding the town and state, or paste coordinates.'})); return; }
  g.replaceChildren(...hits.map(x=>goRow(esc(goShort(x.display_name)),()=>goTo(+x.lat,+x.lon,goShort(x.display_name),x.boundingbox))),el('p',{class:'gonote',text:'Streets and towns from OpenStreetMap. The places below are the Atlas\'s own.'})); }
function goSync(v,auto){ const g=$('#goto'); goSeq++; const c=readCoords(v);
  if(!v){ g.hidden=true; g.replaceChildren(); goClear(); return false; }
  if(c){ g.hidden=false; g.replaceChildren(goRow('Go to <b>'+ll(c)+'</b>',()=>goTo(c.lat,c.lon,ll(c)))); if(auto) goTo(c.lat,c.lon,ll(c)); return true; }
  if(/^https?:\/\//i.test(v)){ g.hidden=false; g.replaceChildren(el('p',{class:'gonote',text:'That link carries no coordinates. In Google Maps, press and hold the spot, copy the two numbers it shows, and paste them here.'})); return true; }
  if(v.length<3){ g.hidden=true; g.replaceChildren(); return false; }
  g.hidden=false; g.replaceChildren(goRow('Find <b>'+esc(v)+'</b> on the map: street, town or address',()=>goLook(v))); return false; }
try{ window.__atlasGo={read:readCoords}; }catch(e){}
$('#q').addEventListener('input',debounce(e=>{ const v=e.target.value.trim(), spot=goSync(v,true); F.q=spot?'':v; renderList(); syncMarkers(); syncFcount(); },150));
$('#q').addEventListener('keydown',e=>{ if(e.key!=='Enter') return; const v=e.target.value.trim(), c=readCoords(v); if(c) goTo(c.lat,c.lon,ll(c)); else if(v.length>=3&&!/^https?:\/\//i.test(v)) goLook(v); });
/* the Filters button opens the panel under the search box and shows how many filters are on (the search box is not counted) */
$('#filt-btn').addEventListener('click',()=>{ const d=$('#filters'); d.open=!d.open; syncFcount(); });
$('#sort').addEventListener('change',e=>{ U.ui.sort=e.target.value; save(); renderList(); });
$('#sort').value=U.ui.sort||'time';
document.querySelectorAll('.tabs button').forEach(b=>b.addEventListener('click',()=>{ const v=b.getAttribute('data-view'); if(v==='list'&&sel&&view!=='detail'){ showView('detail'); } else if(v==='list'){ if(sel) deselect(); else showView('list'); } else showView(v); }));
$('#add-here').addEventListener('click',()=>{ if(!geo.ll) return; if(spotting) spotDrop(geo.ll[0],geo.ll[1]); else placeAt(geo.ll[0],geo.ll[1]); });
$('#add-centre').addEventListener('click',()=>{ if(!map) return; const c=map.getCenter(); if(spotting) spotDrop(c.lat,c.lng); else if(adding) placeAt(c.lat,c.lng); });
$('#add-many').addEventListener('click',spotStart);
$('#spot-undo').addEventListener('click',()=>{ if(U.spots&&U.spots.length){ U.spots.pop(); saveNow(); drawSpots(); addBar(); } });
$('#add-place').addEventListener('click',()=>{ if(!map) return; asking=false; spotting=false; adding=true; stage.classList.add('adding'); $('#addbar').hidden=false; addBar(); });
$('#rec-note').addEventListener('click',()=>{ const f=$('#rec-form'); f.hidden=!f.hidden; if(!f.hidden){ $('#rec-text').value=''; try{ $('#rec-text').focus(); }catch(e){} } });
$('#rec-form').addEventListener('submit',e=>{ e.preventDefault(); addNote($('#rec-text').value); $('#rec-form').hidden=true; });
{ const b=$('#rec-stop'); let armed=false; b.addEventListener('click',()=>{ if(!armed){ armed=true; b.textContent='Tap again to stop'; setTimeout(()=>{ armed=false; b.textContent='Stop'; },3500); return; } armed=false; b.textContent='Stop'; stopLog(); }); }
$('#add-cancel').addEventListener('click',()=>{ adding=false; spotting=false; pickingHome=false; asking=false; stage.classList.remove('adding'); $('#addbar').hidden=true; addBar(); syncBar(); });
$('#sheet-x').addEventListener('click',closeSheet); $('#sheet-set').addEventListener('click',()=>showSettings(sheetMode!=='set')); $('#scrim').addEventListener('click',closeSheet);
document.addEventListener('keydown',e=>{ if(e.key==='Escape'){ if(!$('#sheet').hidden){ closeSheet(); } else if(adding||spotting||pickingHome||asking){ $('#add-cancel').click(); } else if(view==='detail'&&sel&&!/^(INPUT|TEXTAREA|SELECT)$/.test((e.target.tagName||''))) deselect(); } });
if(window.matchMedia('(min-width:821px)').matches) $('#filters').open=false;

buildHome(); buildFilters(); renderList(); $('#trip-n').textContent=U.trip.length;
if(pref('open')!=='last'&&LD[pref('open')]) U.ui.base=pref('open');
if(window.L){ initMap(); buildBar(); resumeLog(); pushPrefs(); }
else { $('#map').append(el('div',{class:'pad',style:'padding-block:40px;max-width:46ch;margin:auto',text:'The map library could not load, most likely because this device is offline. The list, place pages and links still work. Reload when you are back online.'})); $('#lbar').hidden=true; }
setTimeout(()=>{ if(pref('wikiPhotos')&&navigator.onLine!==false) phxLoad(); },2500);      /* photo details, once things are quiet */
if(HOSTED&&!AT&&'serviceWorker' in navigator&&(location.protocol==='https:'||location.hostname==='localhost')) navigator.serviceWorker.register('sw.js').catch(()=>{});
/* the phone's Back button, in the app: close whatever is open; returning false lets Android put the app in the background */
window.atlasBack=()=>{
  if(!$('#sheet').hidden){ closeSheet(); return true; }
  if(adding||spotting||pickingHome||asking){ $('#add-cancel').click(); return true; }
  if(!$('#rec-form').hidden){ $('#rec-form').hidden=true; return true; }
  if(map&&map._popup&&map._popup.isOpen&&map._popup.isOpen()){ map.closePopup(); return true; }
  if($('#app').classList.contains('mapbig')){ $('#app').classList.remove('mapbig'); buildBar(); setTimeout(()=>map&&map.invalidateSize(),60); return true; }
  if(view==='detail'&&sel){ deselect(); return true; }
  if(view==='near'&&NM.goal){ nmGoal(null); return true; }
  if(view!=='list'){ showView(sel?'detail':'list'); return true; }
  return false; };
/* in the app: look for newer places shortly after start, and again when a connection comes back */
if(AT){ const look=()=>AT.check().then(r=>{ if(r.state==='updated'){ banner('New places downloaded'+(r.places?' ('+r.places+' in all)':'')+'. Tap here to load them.',false); $('#banner').onclick=()=>location.reload(); } },()=>{});
  setTimeout(look,5000); window.addEventListener('online',()=>{ if(Date.now()-AT.checked>36e5) look(); });
  document.addEventListener('visibilitychange',()=>{ if(!document.hidden&&Date.now()-AT.checked>6*36e5) look(); }); }
(function fromHash(){ const id=decodeURIComponent((location.hash||'').replace(/^#/,'')); const s=id&&(byId(id)||byId(ALIAS[id])); if(s) select(s,true); })();      /* a link to a replaced id opens the entry that replaced it */
window.addEventListener('hashchange',()=>{ const id=decodeURIComponent((location.hash||'').replace(/^#/,'')); const s=id&&(byId(id)||byId(ALIAS[id])); if(s&&(!sel||sel.id!==s.id)) select(s,true); });
})();
