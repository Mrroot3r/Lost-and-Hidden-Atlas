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

const CAT={amuse:['Amusement & trolley parks','#d6338a'],hotel:['Hotels & resorts','#c8322b'],canal:['Canal works','#2f8fd0'],rail:['Rail, trolley & bridges','#4b4f54'],industry:['Mills, iron, brick & ice','#b4691f'],burial:['Burial grounds','#6b4fa0'],town:['Ghost & drowned towns','#2e9e4a'],civic:['Downtown losses','#c79a00'],fort:['Forts & depots','#7a6a1e'],water:['Water works & buried creeks','#19a3b3'],inst:['Estates, institutions & parks','#1f4e79'],light:['Lighthouses','#f08a24'],landmark:['Standing landmarks','#8a8f94'],lidar:['LiDAR finds, unverified','#00a88f']};
const ST={ruins:'Ruins you can see',traces:'Traces: grades, piers, earthworks',standing:'Still standing',marker:'Marker only',gone:'Nothing visible',water:'Under water'};
const STS={ruins:'Ruins',traces:'Traces',standing:'Standing',marker:'Marker only',gone:'Nothing visible',water:'Under water'};
const STRANK={ruins:0,standing:1,traces:2,marker:3,gone:4,water:5};
const PREC={exact:['Pin: exact','On the structure or marker itself, within about 30 m.',30],site:['Pin: on site','Inside the documented footprint, within about 150 m.',150],area:['Pin: approximate','Right vicinity, but the exact spot is not established. Scout it with the old map and LiDAR first.',500]};
const ACC={public:'Public land or street',view:'View from the public way',ask:'Ask permission first',permit:'Permit required',boat:'On the water'};
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
const ext=(href,text,cls)=>el('a',{href:href,target:'_blank',rel:'noopener',class:cls||'',text:text});
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
const U0=()=>({v:1,home:{id:'alb'},status:{},notes:{},moved:{},custom:[],trip:[],saved:{},dtc:null,me:{},logs:[],last:null,ui:{base:'streets',year:'Latest',light:'nw',hist:true,histOp:0.8,sort:'time',land:false,lots:false,leads:false,lines:{oldrail:true,canal:true,rail:false}}});
let U=U0(), storeOK=true;
try{ const raw=localStorage.getItem(LS); if(raw){ const j=JSON.parse(raw); U=Object.assign(U0(),j); U.ui=Object.assign(U0().ui,j.ui||{}); U.ui.lines=Object.assign(U0().ui.lines,(j.ui||{}).lines||{}); if(U.ui.base==='lidar1') U.ui.base='lidar'; if(!U.me||typeof U.me!=='object') U.me={}; } }catch(e){ storeOK=false; }
/* ---- settings (the gear in the map options sheet). Stored in U.set; anything missing falls back to SET0. ---- */
const SET0={theme:'auto',units:'mi',clock:'auto',trk:'#e11d74',open:'last',start:'last',follow:true,autoPhotos:true,near:25,detail:'normal',buzz:true,trim:0,previews:true,autoBackup:true,kitBase:'topo',kitSign:'',cluster:true};
const pref=k=>(U.set&&k in U.set)?U.set[k]:SET0[k];
const H12=()=>pref('clock')==='24'?false:pref('clock')==='12'?true:undefined;   /* undefined lets the phone's own setting decide */
const KM=()=>pref('units')==='km';
const fmtMi=(mi,dg)=>KM()?(mi*1.609344).toFixed(dg)+' km':(+mi).toFixed(dg)+' mi';            /* a distance measured in miles, shown in the chosen unit */
const miTxt=mi=>KM()?Math.round(mi*1.609344)+' km':mi+' mi';
const STEP=()=>({fine:2,normal:4,coarse:10})[pref('detail')]||4;                                 /* metres between saved track points */
function applyTheme(){ const t=pref('theme'), r=document.documentElement; if(t==='light'||t==='dark') r.setAttribute('data-theme',t); else r.removeAttribute('data-theme'); r.style.setProperty('--trk',pref('trk')); }
applyTheme();
const save=debounce(()=>{ try{ localStorage.setItem(LS,JSON.stringify(U)); }catch(e){ storeOK=false; } },250);

const sites=()=>BASE.concat(U.custom);
const byId=id=>sites().find(s=>s.id===id);
const pos=s=>{ const m=U.moved[s.id]; return m?{lat:m[0],lon:m[1]}:{lat:s.lat,lon:s.lon}; };
const dest=s=>s.th?{lat:s.th[0],lon:s.th[1]}:pos(s);
function homeObj(){ if(U.home.id==='custom') return {id:'custom',name:U.home.name||'My spot',lat:U.home.lat,lon:U.home.lon}; return HUBS.find(h=>h.id===U.home.id)||HUBS[0]; }
const MAXB=[[17.5,-170.0],[72.0,-50.0]];
const inMap=(la,lo)=>la>=MAXB[0][0]&&la<=MAXB[1][0]&&lo>=MAXB[0][1]&&lo<=MAXB[1][1];
/* Until a start place is chosen by hand, it follows the nearest start city to where the reader is (or last was). */
function nearHome(ll,say){ if(!ll||U.home.by===1||U.home.id==='custom') return false; let b=null,bd=1e9; HUBS.forEach(h=>{ const d=hav(ll[0],ll[1],h.lat,h.lon); if(d<bd){ bd=d; b=h; } });
  if(!b||bd>300||b.id===U.home.id) return false; U.home={id:b.id,by:2}; save();
  if(say){ buildHome(); drawHome(); refresh(); banner('Drive times now count from '+b.name+', the nearest start city. Change it under the gear in Map options.',false,7000); } return true; }
function startView(){ const v=U.ui.view, H=homeObj();
  if(pref('start')!=='home'&&v&&inMap(v[0],v[1])) return {c:[v[0],v[1]],z:Math.max(3,Math.min(20,v[2]||9))};
  if(H.id==='alb') return {c:[42.82,-73.86],z:9}; return {c:[H.lat,H.lon],z:H.id==='custom'?11:10}; }
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
function dt(s){
  const h=U.home.id;
  if(h!=='custom'&&s.dt&&s.dt[h]&&!U.moved[s.id]) return {min:s.dt[h][0],mi:s.dt[h][1],est:false};
  if(U.dtc&&U.dtc.key===homeKey()&&U.dtc.t[s.id]) return {min:U.dtc.t[s.id][0],mi:U.dtc.t[s.id][1],est:false};
  const H=homeObj(),d=dest(s),r=roughMin(hav(H.lat,H.lon,d.lat,d.lon)); return {min:r.min,mi:r.mi,est:true};
}
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
const F={line:null,q:'',cat:new Set(),st:new Set(),reg:'',acc:new Set(),eff:new Set(),max:0,tag:'',now:false,lead:false,oldmap:false,pub:false,fresh:'',my:'any',hideDone:false};
/* Searching. Each place's words are gathered once, lower-cased and with accents removed: its names, its town, and the
   rest (years, kind, what is left, region, the texts, the access note, series tags). Every word typed must be found
   somewhere. In the list, places with all the words in their name come first, then name or town, then the rest. */
const HAY=new Map(), fold=x=>String(x||'').toLowerCase().normalize('NFD').replace(/[\u0300-\u036f]/g,'');
function hay(s){ let h=HAY.get(s.id); if(!h||h.s!==s){ h={s:s,n:fold(s.name+' '+(s.name2||'')),t:fold(s.town),
  x:fold([s.years,(CAT[s.cat]||[])[0],STS[s.st],REG[s.reg],s.hook,s.story,s.look,s.accn,Array.isArray(s.tags)?s.tags.join(' '):s.tags].filter(Boolean).join(' '))}; HAY.set(s.id,h); } return h; }
let qMemo=['',[]];
function qWords(){ if(qMemo[0]!==F.q) qMemo=[F.q,fold(F.q).split(/\s+/).filter(Boolean)]; return qMemo[1]; }
function qTier(s){ const h=hay(s), w=qWords(); return w.every(x=>h.n.indexOf(x)>=0)?0:w.every(x=>h.n.indexOf(x)>=0||h.t.indexOf(x)>=0)?1:2; }
function match(s){
  if(F.line&&!F.line.ids.has(s.id)) return false;
  if(F.q){ const h=hay(s); if(!qWords().every(w=>h.n.indexOf(w)>=0||h.t.indexOf(w)>=0||h.x.indexOf(w)>=0)) return false; }
  if(F.cat.size&&!F.cat.has(s.cat)) return false;
  if(F.st.size&&!F.st.has(s.st)) return false;
  if(F.reg&&s.reg!==F.reg) return false;
  if(F.acc.size&&!F.acc.has(s.acc)) return false;
  if(F.eff.size&&!F.eff.has(s.eff)) return false;
  if(F.max&&dt(s).min>F.max) return false;
  if(F.tag&&(s.tags||[]).indexOf(F.tag)<0) return false;
  if(F.now&&!s.now) return false;
  if(F.lead&&!(s.conf==='lead'||s.conf==='mixed'||s.prec==='area')) return false;
  if(F.oldmap&&!s.tm) return false;
  if(F.pub&&!(s.pl&&s.pl[2]==='OA')) return false;
  if(F.fresh&&s.new!==F.fresh) return false;
  const my=U.status[s.id]||'';
  if(F.my==='mine'){ if(!s.mine) return false; } else if(F.my!=='any'&&my!==F.my) return false;
  if(F.hideDone&&(my==='filmed'||my==='skip')) return false;
  return true;
}
function activeCount(){ return (F.line?1:0)+(F.q?1:0)+F.cat.size+F.st.size+(F.reg?1:0)+F.acc.size+F.eff.size+(F.max?1:0)+(F.tag?1:0)+(F.now?1:0)+(F.lead?1:0)+(F.oldmap?1:0)+(F.pub?1:0)+(F.fresh?1:0)+(F.my!=='any'?1:0)+(F.hideDone?1:0); }
function clearF(){ setLine(null,true); F.q='';F.cat.clear();F.st.clear();F.reg='';F.acc.clear();F.eff.clear();F.max=0;F.tag='';F.now=false;F.lead=false;F.oldmap=false;F.pub=false;F.fresh='';F.my='any';F.hideDone=false; }
/* batches of places, oldest first; each data file names its own, so a new state needs no change here */
const BATCHES=D.batches||[];
const PRESETS=(BATCHES.length?[['Newest: '+BATCHES[BATCHES.length-1].label,()=>{ F.fresh=BATCHES[BATCHES.length-1].key; }]]:[]).concat([
  ['Worcester County',()=>{ F.reg='worc'; }],
  ['Ruins you can walk to',()=>{ F.st.add('ruins');F.st.add('traces');F.acc.add('public'); }],
  ['Trolley parks',()=>{ F.tag='trolleyparks'; }],
  ['Within 30 min',()=>{ F.max=30; }],
  ['Changing now',()=>{ F.now=true; }],
  ['Standing landmarks',()=>{ F.cat.add('landmark'); }],
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
  fb.append(chipGroup("What's left to see",STS,F.st));
  fb.append(chipGroup('Kind of place',CAT,F.cat,true));
  const reg=el('select',{id:'f-reg',onchange:e=>{F.reg=e.target.value;refresh();}},el('option',{value:'',text:'All regions'}),STATES.map(st=>{ const used=st.regions.filter(r=>BASE.some(x=>x.reg===r[0])); return used.length?el('optgroup',{label:st.name},used.map(r=>el('option',{value:r[0],text:r[1]}))):null; }));
  reg.value=F.reg;
  const max=el('select',{id:'f-max',onchange:e=>{F.max=+e.target.value;refresh();}},[[0,'Any drive'],[15,'15 min or less'],[30,'30 min or less'],[45,'45 min or less'],[60,'1 hour or less'],[90,'1½ hours or less'],[120,'2 hours or less']].map(o=>el('option',{value:String(o[0]),text:o[1]})));
  max.value=String(F.max);
  fb.append(el('div',{class:'row'},el('label',{class:'field'},el('span',{text:'Region'}),reg),el('label',{class:'field'},el('span',{text:'Drive time'}),max)));
  fb.append(chipGroup('Access',ACC,F.acc));
  fb.append(chipGroup('Effort',EFF,F.eff));
  const ser=el('select',{id:'f-tag',onchange:e=>{F.tag=e.target.value;refresh();}},el('option',{value:'',text:'Any series'}),D.series.map(s=>el('option',{value:s.tag,text:s.title})));
  ser.value=F.tag;
  const my=el('select',{id:'f-my',onchange:e=>{F.my=e.target.value;refresh();}},el('option',{value:'any',text:'Any'}),Object.keys(MY).map(k=>el('option',{value:k,text:MY[k]})),el('option',{value:'mine',text:'Places I added'}));
  my.value=F.my;
  fb.append(el('div',{class:'row'},el('label',{class:'field'},el('span',{text:'Video series'}),ser),el('label',{class:'field'},el('span',{text:'My progress'}),my)));
  if(BATCHES.length){ const bs=el('select',{id:'f-batch',onchange:e=>{F.fresh=e.target.value;refresh();}},el('option',{value:'',text:'Any time'}),BATCHES.slice().reverse().map(b=>el('option',{value:b.key,text:b.label+' ('+b.n+')'}))); bs.value=F.fresh; fb.append(el('label',{class:'field'},el('span',{text:'Added in'}),bs)); }
  const tog=(label,key)=>el('button',{class:'chip',type:'button','aria-pressed':F[key]?'true':'false',onclick:()=>{F[key]=!F[key];refresh();}},label);
  fb.append(el('div',{class:'fgrp'},el('span',{class:'lbl',text:'Only show'}),el('div',{class:'chips'},tog('Changing right now','now'),tog('Leads and rough pins','lead'),tog('Has an old map overlay','oldmap'),tog('On open public land','pub'),tog('Hide filmed and skipped','hideDone'))));
  fb.append(el('div',null,el('button',{class:'btn sm',type:'button',onclick:()=>{clearF();$('#q').value='';refresh();}},'Clear all filters')));
  const pr=$('#presets'); pr.textContent='';
  PRESETS.forEach(p=>pr.append(el('button',{class:'chip',type:'button',onclick:()=>{clearF();$('#q').value='';p[1]();refresh();}},p[0])));
}

/* ---------- list ---------- */
let visible=[], listAll=false, listKey=''; const LISTCAP=120;
function sortSites(a){
  const k=U.ui.sort;
  const t=new Map(a.map(s=>[s.id,dt(s).min]));
  if(F.line){ a.sort((x,y)=>F.line.ord.get(x.id)-F.line.ord.get(y.id)); return a; }
  if(k==='name') a.sort((x,y)=>x.name.localeCompare(y.name));
  else if(k==='reg') a.sort((x,y)=>(REG[x.reg]||'').localeCompare(REG[y.reg]||'')||x.name.localeCompare(y.name));
  else if(k==='left') a.sort((x,y)=>STRANK[x.st]-STRANK[y.st]||t.get(x.id)-t.get(y.id));
  else a.sort((x,y)=>t.get(x.id)-t.get(y.id));
  if(F.q){ const tier=new Map(a.map(s=>[s.id,qTier(s)])); a.sort((x,y)=>tier.get(x.id)-tier.get(y.id)); }      /* the sort keeps the chosen order inside each tier */
  return a;
}
function dot(s){ return el('span',{class:'dot'+(HOLLOW[s.st]?' hollow':'')+(s.st==='standing'?' sq':''),style:'--c:'+((CAT[s.cat]||CAT.landmark)[1])}); }
function renderList(){
  visible=sortSites(sites().filter(match));
  const ul=$('#list'); ul.textContent='';
  const n=activeCount();
  $('#fcount').textContent=n?n+' on':'';
  $('#count').textContent=visible.length+' of '+sites().length+' places';
  const lc=$('#linechip'); lc.textContent=''; lc.hidden=!F.line; if(F.line){ lc.append(el('span',{class:'chip','aria-pressed':'true'},el('span',{class:'sw',style:'--c:'+LK[F.line.k][1]}),'Along '+F.line.label,el('button',{type:'button',class:'x','aria-label':'Stop following this line',onclick:()=>{setLine(null);refresh();}},'✕'))); }
  if(!visible.length){ ul.append(el('li',{class:'empty pad'},'Nothing matches. Clear a filter or two.')); return; }
  /* a long list is shown in two steps: the first 120 rows now, the rest when asked for. The map shows every pin either way. */
  const key=visible.length+'|'+(visible[0]?visible[0].id:'')+'|'+F.q; if(key!==listKey){ listKey=key; listAll=false; }
  const frag=document.createDocumentFragment(), rows=listAll?visible:visible.slice(0,LISTCAP);
  if(sel&&!listAll&&rows.indexOf(sel)<0&&visible.indexOf(sel)>=0) rows.push(sel);
  rows.forEach(s=>{
    const d=dt(s), my=U.status[s.id];
    frag.append(el('li',null,el('button',{class:'item pad'+(sel&&sel.id===s.id?' cur':''),type:'button','data-id':s.id,onclick:()=>select(s,true)},
      dot(s),
      el('span',null,el('b',{text:s.name}),el('small',{text:[s.town,s.years].filter(Boolean).join(' · ')}),
        el('small',null,STS[s.st],s.now?' · changing now':'',s.prec==='area'?' · rough pin':'',my?' · '+MY[my]:'',U.trip.indexOf(s.id)>=0?' · in trip':'')),
      el('span',{class:'mins'},(d.est?'~':'')+fmtMin(d.min),el('i',{text:miTxt(d.mi)})))));
  });
  ul.append(frag);
  if(rows.length<visible.length) ul.append(el('li',{class:'pad'},el('button',{class:'btn',type:'button',id:'list-more',onclick:()=>{ listAll=true; renderList(); }},'Show the other '+(visible.length-rows.length)+' places')));
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
function exportUrl(base,c,extra){ const n=Math.pow(2,c.z),r=2*W/n,x0=-W+c.x*r,y1=W-c.y*r,px=PXQ();
  return base+'?bbox='+[x0,y1-r,x0+r,y1].map(v=>v.toFixed(2)).join(',')+'&bboxSR=3857&imageSR=3857&size='+px+','+px+'&format=jpg&f=image'+(extra||''); }
function xyz(tpl,c,maxN){ let z=c.z,x=c.x,y=c.y,dz=0; if(z>maxN){ dz=z-maxN; x=x>>dz; y=y>>dz; z=maxN; }
  const u=tpl.replace('{z}',z).replace('{y}',y).replace('{x}',x); return dz?{url:u,dz:dz,ox:c.x-(x<<dz),oy:c.y-(y<<dz)}:u; }
const RIG='https://maps.edc.uri.edu/rigis/rest/services/', RILEAF=RIG+'IMG/RI_202603_RGB_3in_web/ImageServer/exportImage', RIDEM=RIG+'TOPO/Elevation_2022_Lidar_web/ImageServer/exportImage';
const hsRule=g=>'&interpolation=RSP_BilinearInterpolation&renderingRule='+encodeURIComponent(JSON.stringify({rasterFunction:'Hillshade',rasterFunctionArguments:{Azimuth:g[1],Altitude:g[2],ZFactor:g[3]},variableName:'DEM'}));
const NYHS='https://elevation.its.ny.gov/arcgis/rest/services/NYS_Statewide_Hillshade/MapServer/export', NYDEM='https://elevation.its.ny.gov/arcgis/rest/services/Latest_DEM/ImageServer/exportImage';
function leafUrl(c){ const p=tileCenter(c), r=regionOf(p[0],p[1]);
  if(r==='ny') return exportUrl('https://orthos.its.ny.gov/arcgis/rest/services/wms/'+U.ui.year+'/MapServer/export',c);
  if(r==='ma') return xyz('https://tiles.arcgis.com/tiles/hGdibHYSPO59RG1h/arcgis/rest/services/orthos2023/MapServer/tile/{z}/{y}/{x}',c,20);
  if(r==='vt') return xyz('https://maps.vcgi.vermont.gov/arcgis/rest/services/EGC_services/IMG_VCGI_CLR_WM_CACHE/ImageServer/tile/{z}/{y}/{x}',c,19);
  if(r==='ri'&&c.z>=12) return exportUrl(RILEAF,c);
  return xyz('https://services.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}',c,19); }
function lidarUrl(c){ const p=tileCenter(c), r=regionOf(p[0],p[1]);
  if(r==='ny'){ if(c.z<14) return exportUrl(NYHS,c); const g=LIGHT[U.ui.light]||LIGHT.nw;
    return exportUrl(NYDEM,c,hsRule(g)); }
  if(r==='ri'&&c.z>=11) return exportUrl(RIDEM,c,hsRule(LIGHT[U.ui.light]||LIGHT.nw));
  if(r==='ma') return xyz('https://tiles.arcgis.com/tiles/hGdibHYSPO59RG1h/arcgis/rest/services/LiDAR_ShadedRelief/MapServer/tile/{z}/{y}/{x}',c,18);
  if(r==='vt') return xyz('https://maps.vcgi.vermont.gov/arcgis/rest/services/EGC_services/IMG_VCGI_LIDARHILLSHD_WM_CACHE_v1/ImageServer/tile/{z}/{y}/{x}',c,19);
  return xyz('https://services.arcgisonline.com/arcgis/rest/services/Elevation/World_Hillshade/MapServer/tile/{z}/{y}/{x}',c,15); }
const LD={
  streets:{n:'Streets',d:'Roads and place names',mk:p=>L.tileLayer('https://services.arcgisonline.com/ArcGIS/rest/services/World_Street_Map/MapServer/tile/{z}/{y}/{x}',{pane:p,maxZoom:20,maxNativeZoom:19,attribution:'Esri, HERE, Garmin, USGS'})},
  leaf:{n:'Leaf-off aerial',d:'State spring flights. The ground shows through bare trees',mk:p=>new FnLayer('',{pane:p,maxZoom:20,minZoom:9,fn:leafUrl,attribution:'NYS ITS, MassGIS, VCGI, RIGIS'})},
  lidar:{n:'LiDAR terrain',d:'Bare ground with the trees stripped off. Sharpens to 1 m as you zoom in',mk:p=>new FnLayer('',{pane:p,maxZoom:20,fn:lidarUrl,attribution:'NYS ITS, MassGIS, VCGI, RIGIS, Esri'})},
  sat:{n:'Satellite',d:'World imagery, usually leaves on',mk:p=>L.tileLayer('https://services.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}',{pane:p,maxZoom:20,maxNativeZoom:19,attribution:'Esri, Maxar, Earthstar Geographics'})},
  topo:{n:'USGS topo, current',d:'Contours, streams and trails',mk:p=>new CachedXYZ('https://basemap.nationalmap.gov/arcgis/rest/services/USGSTopo/MapServer/tile/{z}/{y}/{x}',{pane:p,maxZoom:20,maxNativeZoom:16,attribution:'USGS The National Map'})},
  oldtopo:{n:'USGS topo, 1940s–80s',d:'Scanned paper quads. Purple marks later photo-revisions',mk:p=>L.tileLayer('https://services.arcgisonline.com/ArcGIS/rest/services/USA_Topo_Maps/MapServer/tile/{z}/{y}/{x}',{pane:p,maxZoom:20,maxNativeZoom:15,attribution:'USGS, National Geographic, i-cubed'})}
};
let cmp={on:false,key:'lidar',mode:'swipe',x:0.5,op:0.6};

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
async function tileBlob(url,pin){
  const hit=await tcGet(url,pin); if(hit) return hit;
  if(TC.pending.has(url)){ const b=await TC.pending.get(url); if(b&&pin) tcPut(url,b,true,b.size); return b; }
  const pr=(async()=>{ const r=await fetch(url,{mode:'cors',credentials:'omit'}); if(!r.ok) throw new Error('http '+r.status);
    const ct=r.headers.get('content-type')||''; if(ct.indexOf('image')<0&&ct.indexOf('octet-stream')<0) throw new Error('not an image');
    const b=await r.blob(); TC.fetchOk++; tcPut(url,b,!!pin); return b; })();
  TC.pending.set(url,pr);
  try{ return await pr; }catch(e){ TC.fetchFail++; throw e; } finally{ TC.pending.delete(url); } }
const CacheMixin={ createTile:function(c,done){
  const img=document.createElement('img'); img.alt=''; img.setAttribute('role','presentation'); const url=this.getTileUrl(c);
  const direct=()=>{ img.onload=()=>{ TC.directOk++; if(TC.fetchOk===0&&TC.fetchFail>=4&&TC.directOk>=4) TC.off=true; done(null,img); }; img.onerror=e=>done(e,img); img.src=url; };
  if(TC.off){ direct(); return img; }
  tileBlob(url).then(b=>{ const u=URL.createObjectURL(b); img.onload=()=>{ URL.revokeObjectURL(u); done(null,img); }; img.onerror=()=>{ URL.revokeObjectURL(u); done(new Error('bad tile'),img); }; img.src=u; },
    ()=>{ if(navigator.onLine===false){ done(new Error('offline'),img); } else direct(); });
  return img; } };
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
  OFF.forEach(o=>{ const lyr=LD[o[0]].mk('tilePane'); for(let z=o[1];z<=o[2];z++){ lyr._tileZoom=z; pts.forEach(p=>tilesAround(p,z,OFFR).forEach(t=>set.add(lyr.getTileUrl({x:t[0],y:t[1],z:z})))); } });
  return Array.from(set); }
async function saveArea(id,urls){
  const tok={id:id,cancel:false,done:0,n:urls.length,bytes:0,fail:0,render:null}; saving=tok; let i=0;
  try{ if(navigator.storage&&navigator.storage.persist) navigator.storage.persist(); }catch(e){}
  const upd=()=>{ if(tok.render) tok.render(); };
  const worker=async()=>{ while(i<urls.length&&!tok.cancel){ const u=urls[i++]; try{ const b=await tileBlob(u,true); tok.bytes+=b.size; }catch(e){ tok.fail++; } tok.done++; upd(); } };
  await Promise.all([worker(),worker(),worker(),worker()]); saving=null; tok.finished=true; upd(); return tok; }
const mb=b=>(b/1048576).toFixed(b<10485760?1:0)+' MB';
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
    topoWarm((id.indexOf('trip:')===0?id.slice(5).split(','):[id]).map(byId).filter(Boolean));
    const t=saveArea(id,urls); saving.render=show; show(); const r=await t;
    if(!r.cancel||r.done>0){ U.saved[id]={at:Date.now(),label:label,mb:mb(r.bytes),n:r.done-r.fail,miss:r.fail+(r.n-r.done),y:U.ui.year,pts:pts.map(p=>[+p.lat.toFixed(5),+p.lon.toFixed(5)])}; save(); }
    show(); if(r.cancel) msg.textContent='Stopped. '+(r.done-r.fail)+' tiles kept.'; else if(r.fail) msg.textContent+=' Some tiles failed; try Save again on better wifi.'; });
  if(saving&&saving.id===id) saving.render=show;
  show();
  return el('div',{class:'offl'},el('p',{style:'font-size:12.5px;color:var(--mute);margin:0 0 6px',text:'Downloads the leaf-off aerial ('+(U.ui.year==='Latest'?'latest flight':U.ui.year==='napp'?'1990s infrared':U.ui.year+' flight')+'), sharp LiDAR ('+(LIGHT[U.ui.light]||LIGHT.nw)[0].toLowerCase()+') and USGS topo for about 500 m around '+(pts.length>1?'each stop':'the pin')+', so you can scout with no signal. Use wifi. Streets and satellite are not saved.'}),btn,bar,msg); }

function banner(msg,warn,ms){ const b=$('#banner'); if(!msg){ b.hidden=true; return; } b.textContent=msg; b.className='float'+(warn?' warn':''); b.hidden=false; b.title='Click to dismiss'; b.onclick=()=>{b.hidden=true;}; clearTimeout(banner.t); if(ms) banner.t=setTimeout(()=>b.hidden=true,ms); }

function initMap(){
  FnLayer=L.TileLayer.extend({ options:{updateWhenZooming:false,keepBuffer:4},
    getTileUrl:function(c){ const t=this.options.fn(c); return typeof t==='string'?t:t.url; },
    createTile:function(c,done){ const t=this.options.fn(c); if(typeof t==='string') return CacheMixin.createTile.call(this,c,done);
      const box=document.createElement('div'); box.style.overflow='hidden'; const sz=this.getTileSize().x, k=1<<t.dz;
      const img=CacheMixin.createTile.call({getTileUrl:()=>t.url},c,e=>done(e,box));
      img.style.cssText='position:absolute;max-width:none;width:'+sz*k+'px;height:'+sz*k+'px;left:'+(-t.ox*sz)+'px;top:'+(-t.oy*sz)+'px'; box.appendChild(img); return box; } });
  CachedXYZ=L.TileLayer.extend(Object.assign({options:{keepBuffer:4}},CacheMixin));
  setTimeout(tcScan,4000);
  window.addEventListener('offline',()=>banner('No signal. Leaf-off, LiDAR and Topo still show for areas you saved or looked at recently.',true,9000));
  window.addEventListener('online',()=>{ banner('Back online.',false,2500); drawLines(); });
  map=L.map('map',{zoomControl:false,maxZoom:20,minZoom:3,zoomSnap:1,worldCopyJump:false,maxBounds:MAXB,maxBoundsViscosity:0.6}); if(U.last&&U.last.ll) nearHome(U.last.ll,false); { const sv=startView(); map.setView(sv.c,sv.z); }
  L.control.zoom({position:'bottomright'}).addTo(map);
  drawScale();
  map.attributionControl.setPrefix(false);
  map.createPane('cmp').style.zIndex=250;
  map.createPane('hist').style.zIndex=350;
  map.on('moveend',()=>{ if(U.ui.land) drawLand(); if(view==='near'&&NM.org==='map') nmDraw(); const c=map.getCenter(); U.ui.view=[+c.lat.toFixed(5),+c.lng.toFixed(5),map.getZoom()]; save(); });
  if(!LD[U.ui.base]) U.ui.base='streets';
  setBase(U.ui.base,true);
  map.on('zoomend',onZoom); onZoom();
  map.on('move zoom zoomend moveend resize viewreset',clipCmp);
  map.on('click',onMapClick);
  map.on('contextmenu',onContext);
  map.on('mousemove',e=>{ const r=$('#readout'); r.hidden=false; r.textContent=e.latlng.lat.toFixed(5)+', '+e.latlng.lng.toFixed(5)+' · z'+map.getZoom(); });
  window.addEventListener('resize',debounce(()=>map.invalidateSize(),150));
  setupSwipe(); drawLines(); drawLand(); drawLots(); drawLeads(); drawPockets(); Object.keys(XL).forEach(drawXL); try{ window.__atlasMap=map; }catch(e){}
  syncMarkers(); drawHome();
  map.on('dragstart',()=>{ dragging=true; }); map.on('dragend',()=>{ dragging=false; });
  if(U.last&&U.last.ll) placeDot(U.last.ll,false);
}
function onZoom(){ map.getContainer().classList.toggle('zfar',map.getZoom()<12); if(markers.size||clusLayer) syncMarkers(); }
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
  const sw=$('#swipe'); const pane=map.getPane('cmp');
  if(!cmp.on||schematic){ sw.hidden=true; pane.style.clip=''; pane.style.opacity=''; return; }
  cmpLayer=LD[cmp.key].mk('cmp').addTo(map);
  if(cmp.mode==='swipe'){ pane.style.opacity=''; sw.hidden=false; $('#swipe-l').textContent=LD[U.ui.base].n; $('#swipe-r').textContent=LD[cmp.key].n; placeSwipe(); }
  else { sw.hidden=true; pane.style.clip=''; pane.style.opacity=cmp.op; }
  onZoom();
}
function clipCmp(){ if(!map) return; const pane=map.getPane('cmp'); if(!cmp.on||cmp.mode!=='swipe'){ return; }
  const sz=map.getSize(),nw=map.containerPointToLayerPoint([0,0]); const x=nw.x+sz.x*cmp.x;
  pane.style.clip='rect('+nw.y+'px,'+(nw.x+sz.x)+'px,'+(nw.y+sz.y)+'px,'+x+'px)'; }
function placeSwipe(){ $('#swipe').style.left=(cmp.x*100)+'%'; clipCmp(); }
function setupSwipe(){
  const g=$('#swipe .grip'); let drag=false;
  g.addEventListener('pointerdown',e=>{ drag=true; try{g.setPointerCapture(e.pointerId);}catch(x){} e.preventDefault(); });
  g.addEventListener('pointermove',e=>{ if(!drag) return; const r=stage.getBoundingClientRect(); cmp.x=Math.min(0.97,Math.max(0.03,(e.clientX-r.left)/r.width)); placeSwipe(); });
  const up=()=>{drag=false;}; g.addEventListener('pointerup',up); g.addEventListener('pointercancel',up);
  g.addEventListener('keydown',e=>{ if(e.key==='ArrowLeft'){cmp.x=Math.max(0.03,cmp.x-0.03);placeSwipe();} if(e.key==='ArrowRight'){cmp.x=Math.min(0.97,cmp.x+0.03);placeSwipe();} });
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
  cmp:'<path d="M12 3v18M4 6h5v12H4zM15 6h5v12h-5z"/>',
  who:'<circle cx="9" cy="8" r="3.500"/><path d="M3 20c0-3.500 2.500-6 6-6 1.500 0 2.800.400 3.800 1.200M17 13v.01M17 16v5M14.500 9.500a2.500 2.500 0 1 1 3.500 2.300"/>',
  opt:'<path d="M4 7h9M17 7h3M4 17h3M11 17h9"/><circle cx="15" cy="7" r="2"/><circle cx="9" cy="17" r="2"/>',
  loc:'<circle cx="12" cy="12" r="4"/><path d="M12 2v4M12 18v4M2 12h4M18 12h4"/>',
  big:'<path d="M4 9V4h5M20 9V4h-5M4 15v5h5M20 15v5h-5"/>',
  list:'<path d="M4 6h16M4 12h16M4 18h16"/>'
};
function ico(k){ const s=document.createElement('span'); s.className='ic'; s.innerHTML='<svg viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">'+ICON[k]+'</svg>'; return s; }
const BAR=[['streets','Streets','Street map'],['leaf','Leaf-off','Leaf-off aerial: spring flights with bare trees'],['lidar','LiDAR','LiDAR terrain: bare ground with the trees stripped off'],['sat','Satellite','Satellite imagery'],['topo','Topo','Current USGS topo map'],['oldtopo','Old topo','USGS paper maps, 1940s to 1980s'],
  ['rails','Old rails','Old railroad and trolley lines'],['canal','Canals','Canals, old and current'],['hist','Old map','Lay the old survey sheet over the selected place'],['land','Public land','Shade public and protected land by access'],['lots','Lot lines','Property lines (New York and Massachusetts, zoom in close)'],['leads','Leads','Unchecked ruins, mines and kilns from OpenStreetMap'],
  ['cmp','Compare','Swipe between two layers'],['who','Owner?','Tap the map to see whose land it is']];
let asking=false, lotLayer=null;
function barState(k){
  if(LD[k]) return !schematic&&U.ui.base===k;
  if(k==='rails') return !!U.ui.lines.oldrail; if(k==='canal') return !!U.ui.lines.canal;
  if(k==='hist') return !!U.ui.hist; if(k==='land') return !!U.ui.land; if(k==='lots') return !!U.ui.lots; if(k==='leads') return !!U.ui.leads;
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
  else if(k==='leads'){ U.ui.leads=!U.ui.leads; save(); drawLeads(); if(U.ui.leads) banner('Yellow dots are unchecked ruins, mines, kilns and quarries from OpenStreetMap. Tap one.',false,7000); }
  else if(k==='cmp'){ cmp.on=!cmp.on; if(cmp.on){ cmp.key=U.ui.base==='lidar'?'leaf':'lidar'; cmp.mode='swipe'; cmp.x=0.5; } setCmp(); }
  else if(k==='who'){ setAsking(!asking); }
  syncBar(); }
function setAsking(on){ asking=on; adding=false; pickingHome=false; $('#add-here').hidden=true; stage.classList.toggle('adding',on); $('#addbar').hidden=!on; if(on) $('#addbar span').textContent='Tap the map to see whose land it is.'; syncBar(); }
function buildBar(){
  const sc=$('#lscroll'), fx=$('#lfix'); sc.textContent=''; fx.textContent='';
  BAR.forEach((b,i)=>{ if(schematic&&(LD[b[0]]||b[0]==='cmp'||b[0]==='lots'||b[0]==='land'||b[0]==='who')) return;
    if((i===6||i===12)&&sc.childNodes.length) sc.append(el('span',{class:'lsep'}));
    sc.append(el('button',{class:'lb',type:'button',id:'lb-'+b[0],title:b[2],'aria-label':b[2],'aria-pressed':'false',onclick:()=>barTap(b[0])},ico(b[0]),el('span',{class:'lt',text:b[1]}))); });
  fx.append(el('button',{class:'lb',type:'button',id:'lb-opt',title:'Flight year, light direction, compare and line options','aria-label':'More map options',onclick:openSheet},ico('opt'),el('span',{class:'lt',text:'More'})));
  fx.append(el('button',{class:'lb',type:'button',id:'lb-loc',title:'Show where I am','aria-label':'Show where I am','aria-pressed':String(geo.id!==null),onclick:()=>{ if(map) locate(); }},ico('loc'),el('span',{class:'lt',text:'Me'})));
  const big=$('#app').classList.contains('mapbig');
  fx.append(el('button',{class:'lb',type:'button',id:'lb-big',title:'Make the map fill the screen','aria-label':big?'Show the list':'Bigger map',onclick:()=>{ $('#app').classList.toggle('mapbig'); buildBar(); if(map) setTimeout(()=>map.invalidateSize(),60); }},ico(big?'list':'big'),el('span',{class:'lt',text:big?'List':'Full'})));
  syncBar(); }
function syncBar(){ BAR.forEach(b=>{ const n=document.getElementById('lb-'+b[0]); if(n) n.setAttribute('aria-pressed',String(barState(b[0]))); }); if(!$('#sheet').hidden) buildSheet(); }
let sheetMode='map';
function drawScale(){ if(!map) return; if(drawScale.c) map.removeControl(drawScale.c); drawScale.c=L.control.scale({position:'bottomleft',imperial:!KM(),metric:KM()}).addTo(map); }
/* send the recorder's settings to the phone; it reads them when a recording starts and when a mark is dropped */
function pushPrefs(){ if(NATIVE) AT.call('configure',{units:pref('units'),step:STEP(),every:({fine:1000,normal:2000,coarse:5000})[pref('detail')]||2000,buzz:!!pref('buzz')}).catch(()=>{}); }
function setPref(k,v){ if(!U.set) U.set={}; U.set[k]=v; saveNow(); applyTheme(); drawScale(); pushPrefs();
  if(k==='cluster') syncMarkers();
  if(k==='trk'){ if(rec) drawRec(); const sl=shownLog&&logById(shownLog); if(sl) showLog(sl,false); }
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
  const sw=el('div',{class:'swatches',role:'radiogroup','aria-label':'Track colour'}); [['#e11d74','Pink'],['#2563eb','Blue'],['#dc2626','Red'],['#7c3aed','Purple'],['#111827','Black']].forEach(c=>{ const b=el('button',{type:'button',role:'radio','aria-checked':String(pref('trk')===c[0]),'aria-label':c[1],title:c[1],style:'--c:'+c[0]}); b.addEventListener('click',()=>{ setPref('trk',c[0]); buildSettings(); }); sw.append(b); });
  const hs=el('select',{id:'set-home'}); [...$('#home').children].forEach(n=>hs.append(n.cloneNode(true))); hs.value=U.home.id; hs.addEventListener('change',()=>{ const h=$('#home'); h.value=hs.value; if(hs.value==='pick') closeSheet(); const ev=new Event('change'); ev.go=true; h.dispatchEvent(ev); });
  const fq=el('input',{type:'text',id:'set-find',placeholder:'Town, address, ZIP or 39.10, -94.58',autocomplete:'off',enterkeyhint:'search'}), fb=el('button',{type:'button',class:'btn',text:'Set'}), fm=el('small',{class:'snote',text:'Use this when the device cannot find you, such as a desktop with location turned off. Names are looked up with OpenStreetMap; coordinates are not sent anywhere.'});
  const go=async()=>{ fb.disabled=true; fm.textContent='Looking…'; const r=await findSpot(fq.value); fb.disabled=false; if(r.err){ fm.textContent=r.err; return; } setSpot(r.lat,r.lon,r.name); if(map) map.setView([r.lat,r.lon],11); buildSettings(); };
  fb.addEventListener('click',go); fq.addEventListener('keydown',e=>{ if(e.key==='Enter'){ e.preventDefault(); go(); } });
  const nmPick=(k,label,list,sub)=>{ const id='set-nm-'+k, x=el('select',{id:id},list.map(c=>el('option',{value:String(c[0]),text:c[0]?(KM()?c[2]:c[1]):'Off'}))); x.value=String(nmSet()[k]);
    x.addEventListener('change',()=>{ const o={}; o[k]=+x.value; nmSave(o); const n=$('#near-'+k); if(n) n.value=x.value; }); return el('label',{class:'field setrow',for:id},el('span',{text:label}),x,sub?el('small',{class:'snote',text:sub}):null); };
  const ks=el('textarea',{id:'set-kitSign',rows:'2',placeholder:'More walks: youtube.com/@yourchannel'}); ks.value=pref('kitSign'); ['change','blur'].forEach(ev=>ks.addEventListener(ev,()=>{ if(ks.value.trim()!==pref('kitSign')) setPref('kitSign',ks.value.trim()); }));
  const add=(...a)=>a.forEach(x=>{ if(x) lb.append(x); });      /* Element.append(null) would print the word "null" */
  add(H('Look and units'),
    pick('theme','Theme',[['auto','Follow the phone'],['light','Light'],['dark','Dark']]),
    pick('units','Distances',[['mi','Miles and feet'],['km','Kilometres and metres']]),
    pick('clock','Clock',[['auto','Follow the phone'],['12','12-hour (2:30 PM)'],['24','24-hour (14:30)']]),
    el('div',{class:'field setrow'},el('span',{text:'Track colour'}),sw),
    H('Map'),
    pick('open','The map opens showing',[['last','Whatever was last showing']].concat(['streets','leaf','lidar','sat','topo'].filter(k=>LD[k]).map(k=>[k,LD[k].n]))),
    tog('cluster','Group pins that crowd together when zoomed out','A numbered disc stands for the pins under it. Tap it to zoom in to them.'),
    tog('follow','Keep the map on me as I move','When your dot walks off the edge of the map, the map moves with it.'),
    pick('start','The map opens at',[['last','Where I left it'],['home','My start place']]),
    el('label',{class:'field setrow',for:'set-home'},el('span',{text:'Start place'}),hs,el('small',{class:'snote',text:'Drive times count from here. Until you choose one, the Atlas uses the start city nearest to where you are or last were.'})),
    el('div',{class:'field setrow'},el('label',{for:'set-find',text:'Or type your start place'}),el('div',{class:'findrow'},fq,fb),fm),
    H('Near me'),
    nmPick('r','List what is within',NMR),
    nmPick('al','Buzz when I walk within',NMA,NATIVE?'While a field log is recording the phone buzzes with the screen off too. Old town centres are listed but never buzz.':'Works while the Atlas is open and showing where you are. Old town centres are listed but never buzz.'),
    el('small',{class:'snote',text:'Which kinds count (places, leads, vanished places, mines, town centres) is chosen with the chips at the top of the Near tab.'}),
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
  lb.append(el('button',{class:'btn sm',id:'sheet-tips',type:'button','aria-pressed':String(!!U.ui.tips),onclick:()=>{ U.ui.tips=!U.ui.tips; save(); buildSheet(); }},U.ui.tips?'Hide the explanations':'What do these do?'));
  const H=t=>el('h3',{text:t}), note=t=>el('small',{class:'snote',text:t});
  const ck=(id,on,label,sub,fn)=>el('label',{class:'lopt',for:id},el('input',{type:'checkbox',id:id,checked:!!on,onchange:e=>fn(e.target.checked)}),el('span',null,label,sub?el('small',null,sub):null));
  if(schematic){ lb.append(el('p',{style:'margin:8px 0 0',text:LOCAL?'Live imagery could not load, so the map is showing a built-in outline. Old-map overlays and every scouting link still work. Reload when you are back online.':'This online copy cannot load live imagery, so the map is a built-in outline. Old-map overlays and every scouting link still work. Open the Atlas file, or host it, for satellite, leaf-off, LiDAR, public land and owner lookups.'})); }
  else {
    lb.append(H('Leaf-off aerial'));
    const y=el('select',{id:'leaf-year','aria-label':'Flight year',onchange:e=>{ U.ui.year=e.target.value; save(); if(U.ui.base==='leaf') setBase('leaf'); if(cmp.on&&cmp.key==='leaf') setCmp(); }},YEARS.map(v=>el('option',{value:v,text:v==='napp'?'1990s infrared':v==='Latest'?'Latest flight':v})));
    y.value=U.ui.year; lb.append(el('div',{class:'lsub'},el('span',{text:'Flight year'}),y),note('The year applies to New York. Blank? That year skipped this county. Massachusetts and Vermont show their own latest state flight (the Vermont one is not always leaf-off). Rhode Island shows its March 2026 state flight once you zoom in past town level. Connecticut and New Hampshire fall back to satellite for now.'));
    lb.append(H('LiDAR light'));
    const s=el('select',{id:'lidar-light','aria-label':'Light direction',onchange:e=>{ U.ui.light=e.target.value; save(); if(U.ui.base==='lidar') setBase('lidar'); if(cmp.on&&cmp.key==='lidar') setCmp(); }},Object.keys(LIGHT).map(v=>el('option',{value:v,text:LIGHT[v][0]})));
    s.value=U.ui.light; lb.append(el('div',{class:'lsub'},s),note('Changing the light makes faint walls and grades pop. It applies in New York and Rhode Island once you zoom in past town level. Massachusetts and Vermont use their own fixed-light LiDAR.'));
    lb.append(H('Compare two layers'));
    lb.append(ck('cmp-on',cmp.on,'Show a second layer over the map','Drag the divider, or fade one over the other',v=>{ cmp.on=v; setCmp(); syncBar(); }));
    if(cmp.on){
      const ks=el('select',{id:'cmp-key','aria-label':'Second layer',onchange:e=>{cmp.key=e.target.value;setCmp();}},Object.keys(LD).map(k=>el('option',{value:k,text:LD[k].n}))); ks.value=cmp.key;
      const ms=el('select',{id:'cmp-mode','aria-label':'Compare mode',onchange:e=>{cmp.mode=e.target.value;setCmp();buildSheet();}},el('option',{value:'swipe',text:'Swipe'}),el('option',{value:'fade',text:'Fade'})); ms.value=cmp.mode;
      lb.append(el('div',{class:'lsub'},ks,ms));
      if(cmp.mode==='fade') lb.append(el('div',{class:'lsub'},el('input',{type:'range',id:'cmp-op',min:'0',max:'1',step:'0.05',value:String(cmp.op),'aria-label':'Second layer strength',oninput:e=>{cmp.op=+e.target.value;map.getPane('cmp').style.opacity=cmp.op;}})));
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
  lb.append(ck('leads-on',U.ui.leads,'Unchecked leads','Ruins, mines, kilns, quarries and old farms mapped by OpenStreetMap volunteers. Nobody has checked them for the Atlas',v=>{ U.ui.leads=v; save(); drawLeads(); syncBar(); }));
  lb.append(ck('xl-vanished',xlOn('vanished'),'Vanished places','Hamlets, churches, forts, airfields, hospitals and post offices the federal names file marks as gone. Orange dots, from town level in. Nine Northeast states, Missouri and Kansas',v=>{ xlSet('vanished',v); buildSheet(); }));
  if(xlOn('vanished')) lb.append(ck('xl-schools',U.ui.xl&&U.ui.xl.schools,'Old school sites too','Mostly one-room schoolhouses. There are thousands, so they are off unless you ask',v=>xlSet('schools',v)));
  lb.append(ck('xl-mines',xlOn('mines'),'Old mines and quarries','Iron mines, quarries, clay pits and prospects from the U.S. Geological Survey. Grey dots, from town level in. Positions are rough',v=>xlSet('mines',v)));
  lb.append(ck('pock-on',U.ui.pockets,'Historic pockets','Old town centres, and other places where historical markers and National Register listings bunch together. Purple discs; zoom in to see each marker and listing',v=>{ U.ui.pockets=v; save(); drawPockets(); buildSheet(); }));
  if(U.ui.pockets&&POCK){ const all=pockNear(pockList.mode), other=pockList.mode==='other';
    lb.append(ck('pock-c',U.ui.pockC,'Old town centres only','Hide the other pockets: estates, mill sites, battlefields, campuses',v=>{ U.ui.pockC=v; save(); pockReset(); }));
    const seg=el('div',{class:'pockseg'}); [['rich','Richest'],['near','Nearest'],['other','Other pockets']].forEach(m=>seg.append(el('button',{class:'btn sm'+(pockList.mode===m[0]?' on':''),type:'button','aria-pressed':String(pockList.mode===m[0]),onclick:()=>{ pockList={mode:m[0],n:8}; buildSheet(); }},m[1])));
    lb.append(note(other?'Estates, mill sites, battlefields and other pockets within 40 miles of your start place.':'Old town centres within 40 miles of your start place. Tap one to go there.'),seg);
    if(all.length){ const ul=el('div',{class:'pocklist'}); all.slice(0,pockList.n).forEach(o=>ul.append(el('button',{class:'btn sm',type:'button',onclick:()=>{ closeSheet(); map.setView([o.k[0],o.k[1]],15); }},el('b',{text:o.k[7]}),el('small',{text:' '+pockLine(o)})))); lb.append(ul);
      if(all.length>pockList.n) lb.append(el('button',{class:'btn sm',type:'button',id:'pock-more',onclick:()=>{ pockList.n+=8; buildSheet(); }},'Show more ('+(all.length-pockList.n)+')')); }
    else lb.append(note('None are mapped within 40 miles of your start place yet. The layer covers '+Object.keys(POCK.s||{}).map(x=>STATE[x]||x).join(', ')+' so far.')); }
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
function linesData(){ if(LINES) return LINES; const n=document.getElementById('d-lines'); if(!n){ loadLines(); return []; }
  try{ LINES=JSON.parse(n.textContent); }catch(e){ LINES=[]; } return prepLines(LINES); }
function loadLines(){ if(linesWait||LINES) return;
  linesWait=(AT?AT.fetch('data/lines.json'):fetch('data/lines.json'+VQ)).then(r=>{ if(!r.ok) throw new Error('http '+r.status); return r.json(); }).then(a=>{ LINES=prepLines(a); drawLines();
      if(sel&&view==='detail'&&!/^(INPUT|TEXTAREA|SELECT)$/.test((document.activeElement||{}).tagName||'')){ const v=$('#v-detail'), y=v.scrollTop; renderDetail(sel); v.scrollTop=y; } })
    .catch(()=>{ linesWait=null; if(!linesTold){ linesTold=true; banner('Old rail and canal lines could not load. They will try again when you are back online.',true,7000); } }); }
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
   zoom step, which took about 0.4 s of a 0.5 s step on a mid-range phone. So:
   - a piece of line is on the map only while its half-degree cell is in or near the view, and is first made then;
   - zoomed out to town level or wider (zoom 9 and under) a thinned copy is drawn: nothing it drops is a pixel wide;
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
function lineSets(){ if(lineSet) return lineSet; const data=linesData(); if(!data.length) return null; lineSet={};
  Object.keys(LGRP).forEach(g=>{ lineSet[g]=[]; });
  const grpOf={}; Object.keys(LGRP).forEach(g=>LGRP[g][1].forEach(k=>{ grpOf[k]=g; }));
  data.forEach(f=>{ const g=grpOf[f.k]; if(!lineSet[g]) return; lineChunks(f).forEach(ch=>{ let a=90,b=-90,c=180,d=-180; ch.forEach(p=>p.forEach(q=>{ if(q[0]<a)a=q[0]; if(q[0]>b)b=q[0]; if(q[1]<c)c=q[1]; if(q[1]>d)d=q[1]; }));
    lineSet[g].push({f:f,ch:ch,b:L.latLngBounds([a,c],[b,d]),lo:null,hi:null,on:''}); }); });
  return lineSet; }
function lineMake(c,mode){ const f=c.f, st=LK[f.k]; let geo=c.ch;
  if(mode==='lo'){ geo=[]; c.ch.forEach(p=>{ const q=thinPart(p,0.0009); if(q.length>2||Math.abs(q[0][0]-q[q.length-1][0])+Math.abs(q[0][1]-q[q.length-1][1])>0.0012) geo.push(q); }); if(!geo.length) geo=[c.ch[0]]; }
  const pl=new CasedLine(geo,{pane:'lines',renderer:lineCanvas,color:st[1],weight:f.k==='rr'?1.5:2.6,casing:f.k==='rr'?3.5:5,opacity:1,dashArray:st[2],bubblingMouseEvents:false});
  pl.on('click',e=>{ if(adding||pickingHome||asking){ onMapClick(e); return; } let part=c.ch[0], bd=1e12; if(c.ch.length>1) c.ch.forEach(q=>{ const d=distToPart(e.latlng.lat,e.latlng.lng,q); if(d<bd){ bd=d; part=q; } }); linePopup(f,part,e.latlng); });
  return pl; }
/* zoomed out past town level (zoom 8 and under) the whole of a kind of line is one layer, thinned to what a pixel can show */
function lineWide(g){ const out=[];
  LGRP[g][1].forEach(k=>{ const geo=[]; linesData().forEach(f=>{ if(f.k!==k) return; f.c.forEach(p=>{ const q=thinPart(p,0.004); if(q.length>2||Math.abs(q[0][0]-q[q.length-1][0])+Math.abs(q[0][1]-q[q.length-1][1])>0.005) geo.push(q); }); });
    if(!geo.length) return; const st=LK[k];
    const pl=new CasedLine(geo,{pane:'lines',renderer:lineCanvas,color:st[1],weight:k==='rr'?1.5:2.6,casing:k==='rr'?3.5:5,opacity:1,dashArray:st[2],bubblingMouseEvents:false});
    pl.on('click',e=>{ if(adding||pickingHome||asking){ onMapClick(e); return; } const la=e.latlng.lat, lo=e.latlng.lng; let bf=null, bp=null, bd=1e12;
      linesData().forEach(f=>{ if(f.k!==k||la<f.bb[0]-0.1||la>f.bb[2]+0.1||lo<f.bb[1]-0.1||lo>f.bb[3]+0.1) return; f.c.forEach(q=>{ const d=distToPart(la,lo,q); if(d<bd){ bd=d; bf=f; bp=q; } }); });
      if(bf) linePopup(bf,bp,e.latlng); });
    out.push(pl); });
  return out; }
function syncLines(){ if(!map||!lineSets()) return; const z=map.getZoom(), mode=z<=8?'xl':z<=9?'lo':'hi', vb=map.getBounds().pad(0.35);
  if(!lineSet._w) lineSet._w={};
  Object.keys(LGRP).forEach(g=>{ const on=!!U.ui.lines[g], wide=on&&mode==='xl';
    if(wide&&!lineSet._w[g]) lineSet._w[g]=lineWide(g);
    (lineSet._w[g]||[]).forEach(pl=>{ if(wide&&!map.hasLayer(pl)) pl.addTo(map); else if(!wide&&map.hasLayer(pl)) map.removeLayer(pl); });
    lineSet[g].forEach(c=>{ const want=on&&mode!=='xl'&&vb.intersects(c.b)?mode:'';
      if(c.on===want) return;
      if(c.on) map.removeLayer(c[c.on]);
      if(want){ if(!c[want]) c[want]=lineMake(c,want); c[want].addTo(map); }
      c.on=want; }); });
  if(lineHi) lineHi.bringToBack(); }
function drawLines(){
  if(!map) return; if(!lineCanvas){ map.createPane('lines').style.zIndex=380; lineCanvas=L.canvas({pane:'lines',tolerance:7}); }
  if(!LINES){ linesData(); if(!LINES) return; }
  if(!map._lnOn){ map._lnOn=true; map.on('moveend',syncLines); }
  syncLines();
}
function nearLines(p){ const out=[], seen=new Set(); linesData().forEach(f=>{ if(f.k==='rr'||f.k==='cn') return; if(f.n){ const d=distToFeat(p,f); if(d<=350&&!seen.has(f.k+f.n)){ seen.add(f.k+f.n); out.push({f:f,d:d}); } }
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
let LEADS=null, leadGrp=null;
function drawLeads(){
  if(!map) return;
  if(!U.ui.leads){ if(leadGrp) map.removeLayer(leadGrp); return; }
  if(!LEADS){ leadsLoad(); if(!LEADS) return; }
  if(!leadGrp){
    leadGrp=L.layerGroup();
    LEADS.p.forEach(p=>{ const m=L.circleMarker([p[0],p[1]],{pane:'lines',renderer:lineCanvas,radius:5.5,color:'#3a2f00',weight:1.3,fillColor:'#ffd500',fillOpacity:0.95,bubblingMouseEvents:false}).addTo(leadGrp);
      m.on('click',e=>{ if(adding||pickingHome||asking){ onMapClick(e); return; } leadPopup(p); }); }); }
  leadGrp.addTo(map); }
/* ---------- two more lead layers, drawn only where the map is looking ----------
   data/vanished.json (tools/vanished.py): places the federal names file of 2021 marks "(historical)".
       p = [lat,lon,type,name,GNIS id,state]
   data/mines.json (tools/mines.py): past producers and prospects from the USGS Mineral Resources Data System.
       p = [lat,lon,type,name,MRDS id,commodity,'P' past producer|'S' prospect,last year worked or 0,state]
   Both are fetched only when switched on. There are thousands of points, so they are indexed on a grid and only the
   ones in view are drawn, from zoom XL[k].z. */
const XL={
  vanished:{file:'data/vanished.json',z:10,fill:'#ff8a3d',ring:'#5a2600',what:'vanished place',
    src:'From the U.S. Board on Geographic Names file of 2021, which marks it "historical": it no longer exists or no longer serves that purpose. Something may still stand. The position can be 100 m or more out.',
    seed:x=>'Lead from the federal place-names file (GNIS '+x[4]+'), which marks it historical. Not checked yet.'},
  mines:{file:'data/mines.json',z:9,fill:'#aeb7c2',ring:'#1f2a36',what:'old mine or quarry',
    src:'From the USGS Mineral Resources Data System, last updated in 2011. The position is often only good to a few hundred metres. Old workings can be flooded, fenced or on private land: do not enter shafts or adits.',
    seed:x=>'Lead from the USGS Mineral Resources Data System (record '+x[4]+'). Not checked yet.'} };
Object.keys(XL).forEach(k=>{ XL[k].k=k; XL[k].data=null; XL[k].idx=null; XL[k].layer=null; XL[k].wait=null; });
const xlOn=k=>!!(U.ui.xl&&U.ui.xl[k]);
const xlShow=(k,x)=>k!=='vanished'||x[2]!==1||!!(U.ui.xl&&U.ui.xl.schools);     /* old school sites are two thirds of the file: off unless asked for */
function xlLoad(k,quiet){ const X=XL[k]; if(X.data||X.wait) return;
  X.wait=(AT?AT.fetch(X.file):fetch(X.file+VQ)).then(r=>{ if(!r.ok) throw new Error('http '+r.status); return r.json(); })
    .then(j=>{ X.data=j; X.idx={}; j.p.forEach(x=>{ const g=Math.floor(x[0]*20)+','+Math.floor(x[1]*20); (X.idx[g]=X.idx[g]||[]).push(x); }); drawXL(k); if(!$('#sheet').hidden&&sheetMode==='map') buildSheet(); nmLoaded(); })
    .catch(()=>{ X.wait=null; if(!quiet||xlOn(k)) banner('That layer could not load. Check your signal and switch it on again.',true,6000); }); }
function xlInView(k,b){ const X=XL[k], out=[]; if(!X.idx) return out;
  for(let i=Math.floor(b.getSouth()*20);i<=Math.floor(b.getNorth()*20);i++) for(let j=Math.floor(b.getWest()*20);j<=Math.floor(b.getEast()*20);j++) (X.idx[i+','+j]||[]).forEach(x=>{ if(xlShow(k,x)&&b.contains([x[0],x[1]])) out.push(x); });
  return out; }
function drawXL(k){ const X=XL[k]; if(!map) return;
  if(X.layer){ map.removeLayer(X.layer); X.layer=null; }
  if(!xlOn(k)) return;
  if(!X.data){ xlLoad(k); return; }
  if(!map._xlOn){ map._xlOn=true; map.on('moveend',()=>Object.keys(XL).forEach(drawXL)); }
  if(map.getZoom()<X.z) return;
  if(!lineCanvas){ map.createPane('lines').style.zIndex=380; lineCanvas=L.canvas({pane:'lines',tolerance:7}); }
  const g=L.layerGroup(); xlInView(k,map.getBounds().pad(0.1)).slice(0,1500).forEach(x=>{
    const m=L.circleMarker([x[0],x[1]],{pane:'lines',renderer:lineCanvas,radius:5,color:X.ring,weight:1.3,fillColor:X.fill,fillOpacity:0.95,bubblingMouseEvents:false}).addTo(g);
    m.on('click',e=>{ if(adding||pickingHome||asking){ onMapClick(e); return; } xlPopup(k,x); }); });
  X.layer=g.addTo(map); }
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
let POCK=null, pockGrp=null, pockTier={}, pockItems=null, pockLab=null, pockWait=null, pockIdx={}, pockDet={}, pockList={mode:'rich',n:8};
const PKK={b:'building',d:'historic district',s:'site',t:'structure',o:'object'}, PKS={C:'city',t:'town',v:'village',h:'hamlet'};
const pockC=k=>k[10]==='c';
const pockColor=k=>{ const s=k[11]; return !pockC(k)?'#8d86ad':s>=40?'#3b1a9e':s>=25?'#5b3fd6':s>=14?'#7a62e8':'#9d8bf2'; };
function pockPx(k,z){ const real=k[2]/(156543.03392*Math.cos(rad(k[0]))/Math.pow(2,z)); return Math.max(real,pockC(k)?5+Math.min(8,k[11]/6):3.5+Math.min(4,k[11]/9)); }
/* Zoomed out, only the richest show, or a state full of old villages is one purple smear: each disc has a zoom it appears from. */
const PKT=['p11','p10','p9','c11','c10','c9','c8','c0'];
const pockFrom=k=>{ const s=k[11]; return pockC(k)?(s>=30?0:s>=22?8:s>=14?9:s>=8?10:11):(s>=25?9:s>=15?10:11); };
/* close in, a disc would tint the whole screen: fade its fill and leave the ring */
function pockZoom(){ if(!U.ui.pockets||!pockGrp) return; const z=map.getZoom(), f=z>=16?0.03:z>=14?0.12:0.3;
  const want=PKT.filter(t=>pockTier[t]&&z>=+t.slice(1)).join();       /* plain pockets underneath, the richest town centres on top */
  if(want!==pockGrp._want){ pockGrp._want=want; pockGrp.clearLayers(); want.split(',').forEach(t=>{ if(t) pockGrp.addLayer(pockTier[t]); }); }
  POCK.k.forEach(k=>{ if(!k.c||z<pockFrom(k)) return; k.c.setRadius(pockPx(k,z)); const ff=pockC(k)?f:f*0.4; if(k.f!==ff){ k.f=ff; k.c.setStyle({fillOpacity:ff}); } }); }
function pockLoad(quiet){ if(POCK||pockWait) return;
  pockWait=(AT?AT.fetch('data/pockets.json'):fetch('data/pockets.json'+VQ)).then(r=>{ if(!r.ok) throw new Error('http '+r.status); return r.json(); })
    .then(j=>{ POCK=j; drawPockets(); if(!$('#sheet').hidden&&sheetMode==='map') buildSheet(); nmLoaded(); })
    .catch(()=>{ pockWait=null; if(!quiet||U.ui.pockets) banner('Historic pockets could not load. Check your signal and turn them on again.',true,6000); }); }
/* after "old town centres only" is switched: draw the discs afresh */
function pockReset(){ if(pockGrp){ map.removeLayer(pockGrp); pockGrp=null; } if(POCK) POCK.k.forEach(k=>{ k.c=null; k.f=null; }); drawPockets(); }
function drawPockets(){
  if(!map) return;
  if(!U.ui.pockets){ if(pockGrp) map.removeLayer(pockGrp); [pockItems,pockLab].forEach(g=>{ if(g) map.removeLayer(g); }); pockItems=pockLab=null; return; }
  if(!POCK){ pockLoad(); return; }
  if(!lineCanvas){ map.createPane('lines').style.zIndex=380; lineCanvas=L.canvas({pane:'lines',tolerance:7}); }
  if(!pockGrp){ const first=!map._pockOn; map._pockOn=true; pockGrp=L.layerGroup(); pockTier={}; const z=map.getZoom();
    for(let i=POCK.k.length-1;i>=0;i--){ const k=POCK.k[i], tc=pockC(k), c=pockColor(k);     /* plain pockets first, so that town centres sit on top */
      if(U.ui.pockC&&!tc) continue;
      k.c=L.circleMarker([k[0],k[1]],{pane:'lines',renderer:lineCanvas,radius:pockPx(k,z),color:tc?c:'#6d6790',weight:tc?2:1.2,dashArray:tc?null:'3 4',opacity:0.95,fillColor:c,fillOpacity:tc?0.3:0.12,bubblingMouseEvents:false}); const t=(tc?'c':'p')+pockFrom(k); k.c.addTo(pockTier[t]||(pockTier[t]=L.layerGroup()));
      k.c.on('click',e=>{ if(adding||pickingHome||asking){ onMapClick(e); return; } pockPopup(k,e.latlng); }); }
    if(first){ map.on('zoomend',pockZoom); map.on('moveend',pockDetail); } }
  pockGrp.addTo(map); pockGrp._want=null; pockZoom(); pockDetail(); }
/* names on the best town centres in view, so a disc can be told without tapping it. Best score first; a name that
   would sit on top of one already placed is left out. */
function pockLabels(){
  if(pockLab){ map.removeLayer(pockLab); pockLab=null; }
  const z=map.getZoom(); if(!U.ui.pockets||!POCK||z<10) return;
  const b=map.getBounds(), cap=z>=13?22:14, g=L.layerGroup(), put=[]; let n=0;
  for(const k of POCK.k){ if(!pockC(k)||n>=cap) break; if(z<pockFrom(k)||!b.contains([k[0],k[1]])) continue;
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
  if(!U.ui.pockets||!POCK||map.getZoom()<15) return;
  const c=map.getCenter(), need={}; POCK.k.forEach(k=>{ if(!need[k[8]]&&Math.abs(k[0]-c.lat)<0.25&&Math.abs(k[1]-c.lng)<0.35) need[k[8]]=1; }); Object.keys(need).forEach(pockFetch);
  const b=map.getBounds().pad(0.15), g=L.layerGroup(); let n=0;
  for(let i=Math.floor(b.getSouth()*50);i<=Math.floor(b.getNorth()*50);i++) for(let j=Math.floor(b.getWest()*50);j<=Math.floor(b.getEast()*50);j++) (pockIdx[i+','+j]||[]).forEach(q=>{ const x=q[1];
    if(q[0]==='d'){ L.polygon(x[2][1],{pane:'lines',renderer:lineCanvas,color:'#5b3fd6',weight:1.5,dashArray:'5 5',fill:false,interactive:false}).addTo(g); return; }
    if(n>700||!b.contains([x[0],x[1]])) return; n++;
    const mk=q[0]==='m'?L.circleMarker([x[0],x[1]],{pane:'lines',renderer:lineCanvas,radius:4.5,color:'#ffffff',weight:1.5,fillColor:'#5b3fd6',fillOpacity:1,bubblingMouseEvents:false})
                       :L.circleMarker([x[0],x[1]],{pane:'lines',renderer:lineCanvas,radius:5.5,color:'#3b1a9e',weight:2,fillColor:'#ffffff',fillOpacity:1,bubblingMouseEvents:false});
    mk.on('click',e=>{ if(adding||pickingHome||asking){ onMapClick(e); return; } pockItemPopup(q[0],x); }); mk.addTo(g); });
  pockItems=g.addTo(map); }
function pockCounts(k){ const a=[]; if(k[3]) a.push(k[3]+' historical marker'+(k[3]>1?'s':'')+(k[9]&&k[9]*1.5<k[3]?' at '+k[9]+' spot'+(k[9]>1?'s':''):'')); if(k[4]) a.push(k[4]+' listed place'+(k[4]>1?'s':'')); if(k[5]) a.push(k[5]+' historic district'+(k[5]>1?'s':'')+(k[6]?' ('+k[6]+' buildings)':'')); return a.join(' · '); }
function pockPopup(k,latlng){
  const tc=pockC(k);
  const box=el('div',{class:'ctx'},el('b',{text:k[7]}),
    el('span',{style:'color:#5b6660',text:(tc?'Old town centre'+(PKS[k[13]]?' ('+PKS[k[13]]+')':''):'A pocket of markers and listings')+' · score '+Math.round(k[11])}),
    el('span',{style:'color:#5b6660',text:pockCounts(k)}));
  if(k[12]) box.append(el('span',{style:'color:#5b6660',text:'Its dated plaques mostly speak of the '+k[12]+'.'}));
  box.append(el('span',{style:'color:#5b6660',text:tc?'Ranked by how much still stands on the National Register and how old the plaques are. A guide to where to walk, not a promise.':'Many plaques mark something that is gone, so walk it and look.'}),
    el('button',{class:'btn sm',type:'button',onclick:()=>{ map.closePopup(); map.setView([k[0],k[1]],Math.max(map.getZoom(),16)); }},'Zoom in to see each one'));
  scoutLinks({lat:k[0],lon:k[1]}).slice(0,2).forEach(l=>box.append(ext(l[1],l[0],'btn sm')));
  L.popup({maxWidth:270}).setLatLng(latlng||[k[0],k[1]]).setContent(box).openOn(map); }
function pockItemPopup(t,x){
  const pt={lat:x[0],lon:x[1]}, name=x[3]||'Unnamed';
  const box=el('div',{class:'ctx'},el('b',{text:name}));
  if(t==='m'){ box.append(el('span',{style:'color:#5b6660',text:'Historical marker. From HMdb.org, the Historical Marker Database.'}), ext('https://www.hmdb.org/m.asp?m='+x[2],'Read the marker on HMdb.org','btn sm')); }
  else { box.append(el('span',{style:'color:#5b6660',text:'National Register of Historic Places: '+(PKK[x[4]]||'listing')+(x[6]?', listed '+x[6]:'')+(x[5]>1?', '+x[5]+' contributing buildings':'')+'. The position is approximate and the listing may no longer stand.'}), ext('https://npgallery.nps.gov/AssetDetail/NRIS/'+x[2],'National Park Service record','btn sm')); }
  box.append(el('button',{class:'btn sm',type:'button',onclick:()=>{ map.closePopup(); openForm({lat:x[0],lon:x[1],name:name,story:(t==='m'?'From a historical marker listed on HMdb.org (marker '+x[2]+').':'From a National Register listing (reference '+x[2]+').')+' Not checked yet.'}); }},'+ Add to my places'));
  box.append(el('button',{class:'btn sm',type:'button',onclick:()=>whoPopup(pt)},'Whose land is it?'));
  L.popup({maxWidth:270}).setLatLng([x[0],x[1]]).setContent(box).openOn(map); }
/* for the map options sheet: old town centres within reach of the start place, richest or nearest first, or the other pockets.
   "Nearest" leaves out the thinnest centres when there are plenty, so the list is not all crossroads with one plaque. */
function pockNear(mode){ if(!POCK) return []; const H=homeObj();
  let a=POCK.k.filter(k=>(mode==='other')!==pockC(k)).map(k=>({k:k,mi:hav(H.lat,H.lon,k[0],k[1])})).filter(o=>o.mi<=40);
  if(mode==='near'){ const solid=a.filter(o=>o.k[11]>=10); if(solid.length>=8) a=solid; return a.sort((x,y)=>x.mi-y.mi); }
  return a.sort((x,y)=>y.k[11]-x.k[11]); }
function pockLine(o){ const k=o.k, a=[Math.round(o.mi)+' mi'], reg=k[4]+k[6]; if(reg) a.push(reg+' on the Register'); else if(k[5]) a.push('historic district'); if(k[9]) a.push(k[9]+' plaque spot'+(k[9]>1?'s':'')); if(k[12]) a.push(k[12]); return a.join(' · '); }
function leadPopup(p){
  const pt={lat:p[0],lon:p[1]}, kind=LEADS.t[p[2]];
  const box=el('div',{class:'ctx'},el('b',{text:p[3]||kind}),el('span',{style:'color:#5b6660',text:(p[3]?kind+' · ':'')+'unchecked lead from OpenStreetMap'}));
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
  return 'Dear [owner\'s name],\n\nMy name is '+f('name','[your name]')+'. I produce '+f('chan','[channel name]')+', a history-focused YouTube channel ('+f('link','[channel link]')+') documenting the lost buildings and industries of the Capital Region, Catskills and Adirondacks. I am researching '+s.name+(s.town?' in '+s.town:'')+', which I understand you own. I would like permission for a one-time daytime visit of about two hours with one partner to photograph and film what remains.\n\n'+
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
    if(rec){ if(geo.ll) map.setView(geo.ll,Math.max(map.getZoom(),16)); banner('Location stays on while a field log is recording.',false,4000); return; }
    navigator.geolocation.clearWatch(geo.id); geo.id=null; geo.f=null; geo.ll=null; mark(false);
    if(U.last){ placeDot(U.last.ll,false); saveNow(); banner('Location off. The grey dot marks where you last were.',false,4000); }
    return; }
  const fail=msg=>{ if(geo.id!==null){ try{ navigator.geolocation.clearWatch(geo.id); }catch(e){} } geo.id=null; geo.f=null; geo.ll=null; mark(false); if(geo.dot&&U.last) placeDot(U.last.ll,false); banner(msg,true,12000); if(rec&&!NATIVE) stopLog(); };
  if(!navigator.geolocation){ fail('This browser has no location service.'); return; }
  geo.first=true; geo.f=null; mark(true); banner('Finding you…',false,6000);
  try{ geo.id=navigator.geolocation.watchPosition(g=>{ const c=g.coords, t=g.timestamp||Date.now(), p=gpsFilter(c,t); if(!p) return;
      const was=geo.ll; geo.ll=p; U.last={ll:[+p[0].toFixed(6),+p[1].toFixed(6)],t:Date.now()}; saveSlow(); placeDot(p,true); recPoint(p,c.accuracy||50,t); geo.acc=c.accuracy||50; nmFix(p,geo.acc);
      /* follow: if the dot was on screen and has now walked off it, bring the map along */
      if(pref('follow')&&!geo.first&&was&&!dragging){ const inner=map.getBounds().pad(-0.12); if(!inner.contains(p)&&map.getBounds().contains(was)) map.panTo(p,{animate:true,duration:0.6}); }
      if(geo.first){ geo.first=false; nearHome(p,true); banner('You are the blue dot, good to about '+Math.round(c.accuracy)+' m. Tap Me again to stop.',false,6000); map.setView(p,Math.max(map.getZoom(),16)); }
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
const nmDist=mi=>{ if(KM()){ const m=mi*1609.344; return m<950?Math.max(10,Math.round(m/10)*10)+' m':(m/1000).toFixed(m<20000?1:0)+' km'; } const f=mi*5280; return f<1000?Math.max(10,Math.round(f/10)*10)+' ft':mi.toFixed(mi<1?2:mi<10?1:0)+' mi'; };
/* fetch whichever lead files the chosen kinds need; each tells nmLoaded() when it arrives */
function leadsLoad(quiet){ if(LEADS) return; const n=document.getElementById('d-leads');
  if(n){ try{ LEADS=JSON.parse(n.textContent); }catch(e){ LEADS={t:[],p:[]}; } return; }
  if(!leadsLoad.wait) leadsLoad.wait=(AT?AT.fetch('data/leads.json'):fetch('data/leads.json'+VQ)).then(r=>r.json()).then(j=>{ LEADS=j; drawLeads(); nmLoaded(); }).catch(()=>{ leadsLoad.wait=null; if(!quiet||U.ui.leads) banner('Leads could not load. Check your signal and tap Leads again.',true,6000); }); }
function nmEnsure(force){ const t=Date.now(); if(!force&&t-(NM.ens||0)<60000) return; NM.ens=t; const S=nmSet(); if(S.k.l) leadsLoad(true); if(S.k.v) xlLoad('vanished',true); if(S.k.m) xlLoad('mines',true); if(S.k.c) pockLoad(true); }
function nmLoaded(){ NM.ver++; NM.cand=null; clearTimeout(NM.lt); NM.lt=setTimeout(()=>nmPush(false),1200); nmDraw(true); }
/* every target of the chosen kinds within rmi miles of c */
function nmCollect(c,rmi){ const S=nmSet(), out=[], add=(id,k,la,lo,n,t,o)=>{ if(hav(c[0],c[1],la,lo)<=rmi) out.push({id:id,k:k,la:la,lo:lo,n:n,t:t,o:o}); };
  if(S.k.p) sites().forEach(s=>{ const q=pos(s), my=U.status[s.id]; add('p:'+s.id,'p',q.lat,q.lon,s.name,[s.cat==='lidar'?'LiDAR find, not verified':STS[s.st],s.town,my?MY[my]:''].filter(Boolean).join(' · '),s); });
  if(S.k.l&&LEADS) LEADS.p.forEach(p=>add('l:'+p[0]+','+p[1],'l',p[0],p[1],p[3]||LEADS.t[p[2]],(p[3]?LEADS.t[p[2]]+' · ':'')+'unchecked lead',p));
  [['v','vanished'],['m','mines']].forEach(q=>{ const X=XL[q[1]]; if(!S.k[q[0]]||!X.idx) return; const dla=rmi/69+0.002, dlo=rmi/(69*Math.cos(rad(c[0])))+0.002;
    for(let i=Math.floor((c[0]-dla)*20);i<=Math.floor((c[0]+dla)*20);i++) for(let j=Math.floor((c[1]-dlo)*20);j<=Math.floor((c[1]+dlo)*20);j++) (X.idx[i+','+j]||[]).forEach(x=>{ if(xlShow(q[1],x)) add(q[0]+':'+x[4],q[0],x[0],x[1],x[3]||X.data.t[x[2]],xlLine(q[1],x)+' · unchecked lead',x); }); });
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
  if(!t){ if(NM.line){ map.removeLayer(NM.line); NM.line=null; } if(NM.ring){ map.removeLayer(NM.ring); NM.ring=null; } return; }
  if(!NM.ring) NM.ring=L.circleMarker([t.la,t.lo],{radius:13,color:'#e11d74',weight:3,fill:false,interactive:false}).addTo(map); else NM.ring.setLatLng([t.la,t.lo]);
  if(o&&o.how!=='map'){ if(!NM.line) NM.line=L.polyline([o.p,[t.la,t.lo]],{color:'#e11d74',weight:2.5,dashArray:'7 7',interactive:false}).addTo(map); else NM.line.setLatLngs([o.p,[t.la,t.lo]]); }
  else if(NM.line){ map.removeLayer(NM.line); NM.line=null; } }
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
    const S=nmSet(), rs=el('select',{id:'near-r','aria-label':'How far to look'},NMR.map(c=>el('option',{value:String(c[0]),text:'Within '+(KM()?c[2]:c[1])}))), as=el('select',{id:'near-al','aria-label':'Alert me when this close'},NMA.map(c=>el('option',{value:String(c[0]),text:c[0]?'Alert within '+(KM()?c[2]:c[1]):'No alert'})));
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
  else st.append(...[el('b',{text:o.how==='live'?'From where you are'+(geo.acc?', good to '+Math.round(geo.acc)+' m':''):o.how==='map'?'From the middle of the map':geo.id!==null?'Finding you… Showing where you last were':'From where you last were, '+nmAgo(U.last.t)}),o.how==='last'&&geo.id===null?find():null,useMap].filter(Boolean));
  const kb=$('#near-k'); kb.textContent=''; let all=[];
  if(o){ all=nmCands(o.p).map(x=>{ x.mi=hav(o.p[0],o.p[1],x.la,x.lo); x.b=brg(o.p[0],o.p[1],x.la,x.lo); return x; }).filter(x=>x.mi<=S.r).sort((a,b)=>a.mi-b.mi); }
  const wait={l:!LEADS,v:!XL.vanished.data,m:!XL.mines.data,c:!POCK};
  Object.keys(NMK).forEach(k=>{ const n=all.filter(x=>x.k===k).length; kb.append(el('button',{class:'chip',type:'button','aria-pressed':String(!!S.k[k]),title:k==='c'?'Old town centres are listed but never set off the alert':k==='v'?'Old school sites are left out unless they are switched on under More, Vanished places':'',onclick:()=>{ const kk=Object.assign({},nmSet().k); kk[k]=kk[k]?0:1; nmSave({k:kk}); }},el('span',{class:'sw',style:'--c:'+NMK[k][1]}),NMK[k][0]+(S.k[k]&&o?(wait[k]?' …':' '+n):''))); });
  $('#near-note').textContent=(NM.hd!=null?'Compass on: arrows point the way to walk. ':'Arrows: up is north. ')+(S.al?(navigator.vibrate?'Buzzes':'A notice shows')+' within '+nmLab(NMA,S.al)+' of a place or lead'+(NATIVE?' (screen off: only while a log records).':'.'):'');
  const g=$('#near-goal'), G=NM.goal; g.textContent=''; g.hidden=!G;
  if(G){ const far=o?hav(o.p[0],o.p[1],G.la,G.lo):null, b=o?brg(o.p[0],o.p[1],G.la,G.lo):0;
    g.append(...[o?nmArrow(b,true):null,el('div',null,el('b',{class:'nmbig',text:o?nmDist(far)+' '+dirTxt(b):'Waiting for your position'}),el('span',{text:G.n}),el('small',{text:G.t})),
      el('div',{class:'nmgo'},btn('Details',()=>nmOpen(G)),btn('Stop',()=>nmGoal(null)))].filter(Boolean)); nmGoalDraw(); }
  if(o&&!all.length) ul.append(el('li',{class:'empty pad',text:Object.keys(wait).some(k=>S.k[k]&&wait[k])?'Loading the lead lists…':'Nothing on file within '+nmLab(NMR,S.r)+'. Try a wider circle, or switch on more kinds above.'}));
  const cap=NM.more?400:60, frag=document.createDocumentFragment();
  all.slice(0,cap).forEach(x=>frag.append(el('li',null,el('button',{class:'item pad nmitem'+(G&&G.id===x.id?' cur':''),type:'button','data-id':x.id,onclick:()=>nmGoal(x,true)},
    nmArrow(x.b),el('span',null,el('b',{text:x.n}),el('small',null,el('span',{class:'sw',style:'--c:'+NMK[x.k][1]}),x.t)),el('span',{class:'mins'},nmDist(x.mi),el('i',{text:dirTxt(x.b)}))))));
  ul.append(frag); if(all.length>cap) ul.append(el('li',{class:'pad',style:'padding-block:10px'},btn('Show all '+all.length,()=>{ NM.more=true; nmDraw(true); })));
  v.scrollTop=top; }
/* every GPS fix comes through here: refresh the list, and alert when something has come within range */
function nmFix(p,acc){ nmDraw(NM.org==='me'&&NM.how!=='live'); if(NM.goal) nmGoalDraw(); const S=nmSet(); if(!S.al) return; nmEnsure(); if(NATIVE&&rec) nmPush(false); if(acc>35) return;
  let hit=null, more=0; nmCands(p).forEach(x=>{ if(x.k==='c') return; const m=hav(p[0],p[1],x.la,x.lo)*1609.344;
    if(m<=S.al){ if(!NM.in.has(x.id)){ NM.in.add(x.id); if(!hit||m<hit.m){ if(hit) more++; hit={x:x,m:m}; } else more++; } } else if(m>S.al*2+30) NM.in.delete(x.id); });
  if(!hit) return; const x=hit.x;
  if(!(NATIVE&&rec)){ try{ if(navigator.vibrate) navigator.vibrate([260,140,260]); }catch(e){} }   /* while a log records in the app, the recorder buzzes */
  banner('Close by: '+x.n+', about '+nmDist(hit.m/1609.344)+' '+dirTxt(brg(p[0],p[1],x.la,x.lo))+(more?', and '+more+' more':'')+'. Tap to point me there.',false,20000);
  $('#banner').onclick=()=>{ $('#banner').hidden=true; showView('near'); nmGoal(x,true); }; }
/* in the Android app: hand the recorder everything within 25 miles, so it can buzz with the screen off */
function nmPush(force){ if(!NATIVE) return; const S=nmSet(), p=geo.ll||(U.last&&U.last.ll);
  if(!S.al||!p){ if(force||NM.push){ NM.push=null; AT.call('targets',{r:0,list:[]}).catch(()=>{}); } return; }
  if(!force&&NM.push&&NM.push.v===NM.ver&&hav(p[0],p[1],NM.push.c[0],NM.push.c[1])<8) return;
  const list=nmCollect(p,25).filter(x=>x.k!=='c').map(x=>{ x.mi=hav(p[0],p[1],x.la,x.lo); return x; }).sort((a,b)=>a.mi-b.mi).slice(0,4000).map(x=>[+(+x.la).toFixed(5),+(+x.lo).toFixed(5),x.id,String(x.n||'').slice(0,60)]);
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
    const pl=n.pl&&byId(n.pl), ap=el('button',{class:'btn sm',type:'button'},pl?'Open its place':'Add to the Atlas'); ap.addEventListener('click',()=>{ map.closePopup(); if(pl){ select(pl,true); return; } openForm({lat:n.la,lon:n.lo,name:n.x,story:'Found on a field log on '+new Date(n.t*1000).toLocaleDateString(undefined,{month:'long',day:'numeric',year:'numeric'})+'.',from:{log:l.id,t:n.t}}); });
    c.append(el('div',{class:'nacts'},rn,dl,rec===l?null:ap)); m.getPopup().update(); }); return m; }
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
  const acc=stops.filter(o=>o.s.accn||ACC[o.s.acc]); if(acc.length){ out.push('','Before you go'); acc.forEach(o=>out.push(('• '+o.s.name+': '+(ACC[o.s.acc]||'')+(o.s.accn?(ACC[o.s.acc]?'. ':'')+first(o.s.accn):'')).replace(/[.\s]*$/,'.'))); }
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

/* markers */
function pinIcon(s){
  const c=['pin']; if(HOLLOW[s.st]) c.push('hollow'); if(s.st==='standing') c.push('sq'); if(s.now) c.push('now'); if(s.mine) c.push('mine');
  const my=U.status[s.id]; if(my) c.push('my-'+my); if(sel&&sel.id===s.id) c.push('sel');
  return L.divIcon({className:'pinwrap',html:'<span class="'+c.join(' ')+'" style="--c:'+((CAT[s.cat]||CAT.landmark)[1])+'"></span>',iconSize:[22,22],iconAnchor:[11,11]});
}
/* Zoomed out to town level or wider, pins that would sit on top of each other are replaced by one numbered disc.
   A cell of the screen with four or more pins becomes a disc; the selected place always keeps its own pin. */
const CLUSZ=9, CLUSPX=58, CLUSMIN=4;
function clusterPlan(show){ if(!pref('cluster')||map.getZoom()>CLUSZ) return null;
  const z=map.getZoom(), cells=new Map();
  sites().forEach(s=>{ if(!show.has(s.id)||(sel&&sel.id===s.id)) return; const p=pos(s), q=map.project([p.lat,p.lon],z), k=Math.floor(q.x/CLUSPX)+','+Math.floor(q.y/CLUSPX);
    let c=cells.get(k); if(!c){ c={ids:[],la:0,lo:0,a:90,b:-90,c:180,d:-180}; cells.set(k,c); }
    c.ids.push(s.id); c.la+=p.lat; c.lo+=p.lon; if(p.lat<c.a)c.a=p.lat; if(p.lat>c.b)c.b=p.lat; if(p.lon<c.c)c.c=p.lon; if(p.lon>c.d)c.d=p.lon; });
  const single=new Set(), groups=[]; cells.forEach(c=>{ if(c.ids.length<CLUSMIN) c.ids.forEach(i=>single.add(i)); else groups.push(c); });
  if(sel) single.add(sel.id); return {single:single,groups:groups}; }
function syncMarkers(){
  if(!map) return;
  const show=new Set(visible.map(s=>s.id)); if(sel) show.add(sel.id);
  const plan=clusterPlan(show), pinned=id=>show.has(id)&&(!plan||plan.single.has(id));
  const all=sites(), ids=new Set(all.map(s=>s.id));
  markers.forEach((m,id)=>{ if(!ids.has(id)||!pinned(id)){ map.removeLayer(m); markers.delete(id); } });
  all.forEach(s=>{
    if(!pinned(s.id)) return;
    const p=pos(s), ic=pinIcon(s), sig=ic.options.html; let m=markers.get(s.id);
    if(!m){ m=L.marker([p.lat,p.lon],{icon:ic,keyboard:false,riseOnHover:true}); m._sig=sig;
      const tip=el('span',{text:s.name}); m.bindTooltip(tip,{direction:'top',offset:[0,-9]});
      m.on('click',()=>{ if(adding||pickingHome) return; select(byId(s.id)||s,false); });
      m.on('dragend',()=>{ const q=m.getLatLng(); U.moved[s.id]=[+q.lat.toFixed(6),+q.lng.toFixed(6)]; save(); m.dragging.disable(); banner('Pin moved. It is saved in this browser.',false,3500); refresh(); });
      m.addTo(map); markers.set(s.id,m); }
    else { const q=m.getLatLng(); if(q.lat!==p.lat||q.lng!==p.lon) m.setLatLng([p.lat,p.lon]); if(m._sig!==sig){ m.setIcon(ic); m._sig=sig; } }      /* an icon is rebuilt only when it would look different */
    m.setZIndexOffset(sel&&sel.id===s.id?1000:(s.cat==='landmark'?-200:0));
  });
  if(clusLayer){ map.removeLayer(clusLayer); clusLayer=null; }
  if(plan&&plan.groups.length){ clusLayer=L.layerGroup();
    plan.groups.forEach(c=>{ const n=c.ids.length, d=n<10?30:n<40?36:42;
      const m=L.marker([c.la/n,c.lo/n],{keyboard:false,zIndexOffset:-100,icon:L.divIcon({className:'clus',html:String(n),iconSize:[d,d],iconAnchor:[d/2,d/2]})});
      m.bindTooltip(n+' places. Tap to zoom in',{direction:'top',offset:[0,-d/2]});
      m.on('click',()=>{ if(adding||pickingHome) return; map.fitBounds(L.latLngBounds([c.a,c.c],[c.b,c.d]).pad(0.25),{maxZoom:Math.max(map.getZoom()+2,CLUSZ+1)}); });
      m.addTo(clusLayer); });
    clusLayer.addTo(map); }
}
function drawHome(){ if(!map) return; if(homeMarker) map.removeLayer(homeMarker); const H=homeObj();
  homeMarker=L.marker([H.lat,H.lon],{interactive:false,keyboard:false,zIndexOffset:-500,icon:L.divIcon({className:'pinwrap',html:'<span class="homepin">H</span>',iconSize:[24,24],iconAnchor:[12,12]})}).addTo(map); }
function drawSel(){
  if(!map) return; selShapes.forEach(x=>map.removeLayer(x)); selShapes=[];
  if(!sel) return; const p=pos(sel), acc=getComputedStyle(document.documentElement).getPropertyValue('--accent').trim()||'#a3238e';
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
  if(asking){ setAsking(false); whoPopup({lat:e.latlng.lat,lon:e.latlng.lng}); return; }
  if(pickingHome){ pickingHome=false; stage.classList.remove('adding'); $('#addbar').hidden=true; setSpot(e.latlng.lat,e.latlng.lng); return; }
  if(adding){ adding=false; stage.classList.remove('adding'); $('#addbar').hidden=true; $('#add-here').hidden=true; openForm({lat:+e.latlng.lat.toFixed(6),lon:+e.latlng.lng.toFixed(6)}); }
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
function onContext(e){
  const p={lat:e.latlng.lat,lon:e.latlng.lng}; const box=el('div',{class:'ctx'});
  const cb=el('button',{class:'btn sm',type:'button'},ll(p)); cb.addEventListener('click',()=>copy(ll(p),cb)); box.append(cb);
  scoutLinks(p).slice(0,5).forEach(l=>box.append(ext(l[1],l[0],'btn sm')));
  if(!schematic) box.append(el('button',{class:'btn sm',type:'button',onclick:()=>whoPopup(p)},'Whose land is it?'));
  box.append(el('button',{class:'btn sm',type:'button',onclick:()=>{ map.closePopup(); openForm({lat:+p.lat.toFixed(6),lon:+p.lon.toFixed(6)}); }},'+ Add a place here'));
  box.append(el('button',{class:'btn sm',type:'button',onclick:()=>{ map.closePopup(); pickingHome=true; onMapClick(e); }},'Measure drive times from here'));
  L.popup({maxWidth:260}).setLatLng(e.latlng).setContent(box).openOn(map);
}

/* ---------- views ---------- */
let view='list';
function showView(v){ view=v; ['list','detail','trip','log','guide','near'].forEach(k=>{ $('#v-'+k).hidden=(k!==v); });
  $('#tab-list').setAttribute('aria-selected',String(v==='list'||v==='detail')); $('#tab-trip').setAttribute('aria-selected',String(v==='trip')); $('#tab-guide').setAttribute('aria-selected',String(v==='guide')); $('#tab-log').setAttribute('aria-selected',String(v==='log')); $('#tab-near').setAttribute('aria-selected',String(v==='near'));
  nmCompass(v==='near'); if(v==='near'){ nmEnsure(true); renderNear(); if(NM.org==='me'&&geo.id===null&&U.last&&map) locate(); }
  if(v==='trip') renderTrip(); if(v==='guide') renderGuide(); if(v==='log') renderLog(); }
function refresh(){ buildFilters(); renderList(); syncMarkers(); $('#trip-n').textContent=U.trip.length; if(view==='trip') renderTrip(); }
function select(s,fly){
  sel=s; renderDetail(s); showView('detail'); syncMarkers(); drawSel(); showHist();
  document.querySelectorAll('#list .item.cur').forEach(n=>n.classList.remove('cur'));
  if(map&&fly!==null){ const p=pos(s), z=Math.max(map.getZoom(),s.prec==='area'?14:15); if(fly) map.flyTo([p.lat,p.lon],z,{duration:0.8}); else map.panTo([p.lat,p.lon]); }
  try{ history.replaceState(null,'','#'+s.id); }catch(e){ try{ location.hash=s.id; }catch(x){} }
}
function deselect(){ sel=null; drawSel(); showHist(); syncMarkers(); showView('list'); renderList(); try{ history.replaceState(null,'','#'); }catch(e){} }

function renderDetail(s){
  const v=$('#v-detail'); v.textContent=''; v.scrollTop=0;
  const p=pos(s), d=dt(s), H=homeObj(), dst=dest(s), cat=CAT[s.cat]||CAT.landmark, pr=PREC[s.prec]||PREC.site;
  const inTrip=U.trip.indexOf(s.id)>=0;
  /* head */
  const tags=el('div',{class:'dmeta'},
    el('span',{class:'chip'},dot(s),s.mine?'My place · '+cat[0]:cat[0]),
    el('span',{class:'tag',text:STS[s.st],title:ST[s.st]}),
    el('span',{class:'tag p-'+s.prec,text:pr[0],title:pr[1]}),
    s.conf==='lead'?el('span',{class:'tag lead',text:'Lead: confirm first',title:'From published local history but not re-checked against a source.'}):null,
    s.conf==='mixed'?el('span',{class:'tag lead',text:'Partly verified',title:'The outline is checked; some details are still leads.'}):null,
    s.now?el('span',{class:'tag now',text:'Changing now'}):null);
  v.append(el('div',{class:'dhead pad'},
    el('div',{class:'row',style:'justify-content:space-between'},
      el('button',{class:'btn sm',type:'button',onclick:deselect},'← All places'),
      el('div',{class:'row',style:'gap:6px'},
        el('button',{class:'btn sm'+(inTrip?' on':''),type:'button',onclick:()=>{ const i=U.trip.indexOf(s.id); if(i>=0) U.trip.splice(i,1); else U.trip.push(s.id); save(); $('#trip-n').textContent=U.trip.length; renderDetail(s); }},inTrip?'✓ In trip':'+ Add to trip'),
        map?el('button',{class:'btn sm',type:'button',onclick:()=>map.flyTo([p.lat,p.lon],17,{duration:0.7})},'Zoom in'):null)),
    el('h2',{text:s.name}),
    el('p',{class:'sub2',text:[s.name2,s.town,s.years].filter(Boolean).join(' · ')}),
    tags));
  /* getting there */
  const times=el('div',{class:'times'});
  times.append(el('div',{class:'time home'},el('b',{text:(d.est?'~':'')+fmtMin(d.min)}),'from '+H.name+' · '+miTxt(d.mi)));
  /* the three nearest other start cities, not all of them */
  if(s.dt) HUBS.filter(h=>h.id!==U.home.id&&s.dt[h.id]).sort((a,b)=>s.dt[a.id][0]-s.dt[b.id][0]).slice(0,3).forEach(h=>times.append(el('div',{class:'time'},el('b',{text:fmtMin(s.dt[h.id][0])}),h.name)));
  const gd='https://www.google.com/maps/dir/?api=1&origin='+H.lat+','+H.lon+'&destination='+dst.lat+','+dst.lon+'&travelmode=driving';
  const cbtn=el('button',{class:'btn sm',type:'button'},'Copy'); cbtn.addEventListener('click',()=>copy(ll(p),cbtn));
  v.append(el('div',{class:'sec pad'},el('h3',{text:'Getting there'}),times,
    el('dl',{class:'kv',style:'margin-top:8px'},
      el('dt',{text:'Access'}),el('dd',{text:ACC[s.acc]||''}),
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
    const look=(base,ck,zoom,hist)=>()=>{ U.ui.hist=!!hist; if(base==='streets'&&navigator.onLine===false) base='topo'; setBase(base); cmp.on=!!ck; if(ck){cmp.key=ck;cmp.mode='swipe';cmp.x=0.5;} setCmp(); syncBar(); showHist(); const hc=document.getElementById('d-hist'); if(hc) hc.checked=!!hist; map.flyTo([p.lat,p.lon],zoom,{duration:0.7}); };
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
      s.mine?delBtn(s):null,sv),
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
    U.custom=U.custom.filter(x=>x.id!==s.id); delete U.status[s.id]; delete U.notes[s.id]; delete U.moved[s.id]; U.trip=U.trip.filter(i=>i!==s.id); save(); sel=null; drawSel(); showView('list'); refresh(); });
  return b; }

/* add / edit your own place */
function openForm(seed){
  const editing=!!seed.id, s=editing?seed:{lat:seed.lat,lon:seed.lon,name:seed.name||'',town:'',years:'',cat:'industry',st:'ruins',prec:'site',acc:seed.story?'ask':'public',eff:'walk',story:seed.story||'',link:'',from:seed.from};
  const v=$('#v-detail'); v.textContent=''; showView('detail');
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
    el('p',{class:'mono',style:'color:var(--mute);margin:2px 0 0',text:s.lat.toFixed(5)+', '+s.lon.toFixed(5)}),
    f('f-name','Name',name),el('div',{class:'row'},f('f-town','Town',town),f('f-years','Years',years)),
    el('div',{class:'row'},f('f-cat','Kind of place',cat),f('f-st',"What's left",st)),
    el('div',{class:'row'},f('f-acc','Access',acc),f('f-eff','Effort',eff)),
    f('f-prec','How sure is the pin?',prec),f('f-story','Notes',story),f('f-link','Source link',link),err,
    el('div',{class:'row',style:'margin-top:12px'},el('button',{class:'btn pri',type:'submit'},editing?'Save changes':'Save place')),
    el('p',{style:'color:var(--mute);font-size:12.5px;margin-top:10px',text:'Places you add are saved in this browser. Use Guide › Your data to back them up or hand them to Claude to merge into the master list.'}));
  v.append(form); name.focus();
}

/* ---------- trip ---------- */
let trip={round:true,real:null};
function tripStops(){ return U.trip.map(byId).filter(Boolean); }
function legMiles(pts){ let m=0; for(let i=1;i<pts.length;i++) m+=hav(pts[i-1].lat,pts[i-1].lon,pts[i].lat,pts[i].lon); return m; }
function bestOrder(){
  const H=homeObj(), st=tripStops(); if(st.length<3){ return; }
  const P=st.map(dest), n=P.length, used=new Array(n).fill(false); let cur=H, ord=[];
  for(let k=0;k<n;k++){ let b=-1,bd=1e9; for(let i=0;i<n;i++){ if(used[i]) continue; const d=hav(cur.lat,cur.lon,P[i].lat,P[i].lon); if(d<bd){bd=d;b=i;} } used[b]=true; ord.push(b); cur=P[b]; }
  const len=o=>legMiles([H].concat(o.map(i=>P[i])).concat(trip.round?[H]:[]));
  let improved=true, guard=0;
  while(improved&&guard++<60){ improved=false;
    for(let i=0;i<n-1;i++) for(let j=i+1;j<n;j++){ const o2=ord.slice(0,i).concat(ord.slice(i,j+1).reverse(),ord.slice(j+1)); if(len(o2)+1e-6<len(ord)){ ord=o2; improved=true; } } }
  U.trip=ord.map(i=>st[i].id); save(); trip.real=null;
}
function gmapsLinks(){
  const H=homeObj(), P=tripStops().map(dest), out=[]; if(!P.length) return out;
  const pts=[H].concat(P).concat(trip.round?[H]:[]), f=p=>p.lat.toFixed(5)+','+p.lon.toFixed(5);
  for(let i=0;i<pts.length-1;i+=10){ const seg=pts.slice(i,i+11); if(seg.length<2) break;
    const way=seg.slice(1,-1).map(f).join('|');
    out.push('https://www.google.com/maps/dir/?api=1&origin='+f(seg[0])+'&destination='+f(seg[seg.length-1])+(way?'&waypoints='+encodeURIComponent(way):'')+'&travelmode=driving'); }
  return out;
}
function renderTrip(){
  const v=$('#v-trip'); v.textContent=''; trip.round=U.ui.round!==false; const st=tripStops(), H=homeObj();
  const box=el('div',{class:'pad',style:'padding-block:12px'}); v.append(box);
  box.append(el('h2',{style:'font-size:22px',text:'Trip builder'}),el('p',{style:'color:var(--mute);margin:4px 0 10px',text:'Add places from their pages, put them in order, then hand the route to Google Maps for live traffic and turn-by-turn.'}));
  if(!st.length){ box.append(el('p',{class:'empty',text:'No stops yet. Open a place and choose "Add to trip".'})); return; }
  const ul=el('ol',{class:'stops'});
  st.forEach((s,i)=>{ const mv=d=>()=>{ const j=i+d; if(j<0||j>=U.trip.length) return; const a=U.trip; const t=a[i]; a[i]=a[j]; a[j]=t; trip.real=null; save(); renderTrip(); };
    ul.append(el('li',null,el('span',null,el('button',{type:'button',style:'background:none;border:0;padding:0;font-weight:600;text-align:left;color:var(--ink)',onclick:()=>select(s,true)},s.name),el('small',{text:[s.town,EFF[s.eff],ACC[s.acc]].filter(Boolean).join(' · ')})),
      el('span',{class:'mv'},el('button',{class:'btn sm',type:'button','aria-label':'Move up',disabled:i===0,onclick:mv(-1)},'↑'),el('button',{class:'btn sm',type:'button','aria-label':'Move down',disabled:i===st.length-1,onclick:mv(1)},'↓'),el('button',{class:'btn sm',type:'button','aria-label':'Remove',onclick:()=>{U.trip.splice(i,1);trip.real=null;save();refresh();}},'✕')))); });
  box.append(ul);
  const pts=[H].concat(st.map(dest)).concat(trip.round?[H]:[]), r=roughMin(legMiles(pts));
  const sum=el('p',{style:'margin:10px 0'});
  if(trip.real) sum.append(el('b',{class:'mono',text:fmtMin(trip.real.min)}),' driving, '+miTxt(trip.real.mi)+' by road, before stops and traffic.');
  else sum.append(el('b',{class:'mono',text:'~'+fmtMin(r.min)}),' driving, about '+miTxt(Math.round(r.mi))+'. Rough estimate from straight-line distance.');
  box.append(sum);
  const rt=el('input',{type:'checkbox',id:'trip-round',checked:trip.round,onchange:e=>{U.ui.round=trip.round=e.target.checked;save();trip.real=null;renderTrip();}});
  box.append(el('label',{class:'lopt',for:'trip-round'},rt,el('span',null,'Round trip from '+H.name)));
  const real=el('button',{class:'btn',type:'button',onclick:async()=>{ real.disabled=true; real.textContent='Checking…';
    try{ const c=pts.map(p=>p.lon.toFixed(5)+','+p.lat.toFixed(5)).join(';'); const j=await (await fetch('https://router.project-osrm.org/route/v1/driving/'+c+'?overview=false')).json(); if(j.code!=='Ok') throw 0;
      trip.real={min:Math.round(j.routes[0].duration/60),mi:Math.round(j.routes[0].distance/1609.34)}; renderTrip(); }
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
  const b3=el('button',{class:'btn sm',type:'button'},'Copy my additions for Claude'); b3.addEventListener('click',()=>{ const t=JSON.stringify({added:U.custom,movedPins:U.moved,notes:U.notes,progress:U.status},null,1); out.value=t; copy(t,b3); });
  const inp=el('textarea',{id:'bk-in',placeholder:'Paste a backup here',style:'min-height:60px;font-family:var(--fm);font-size:11.5px'});
  const msg=el('span',{class:'note-saved'});
  const load=txt=>{ try{ const j=JSON.parse(txt); if(!j||typeof j!=='object'||!('status' in j)) throw 0; U=Object.assign(U0(),j); U.ui=Object.assign(U0().ui,j.ui||{}); if(!LD[U.ui.base]) U.ui.base='streets'; if(!U.me) U.me={}; save(); applyTheme(); drawScale(); pushPrefs(); buildHome(); drawHome(); refresh(); msg.textContent='Restored.'; }catch(e){ msg.textContent='That does not look like an Atlas backup.'; } };
  const file=el('input',{type:'file',id:'bk-file',accept:'.json,application/json',onchange:e=>{ const f=e.target.files[0]; if(!f) return; const r=new FileReader(); r.onload=()=>load(String(r.result)); r.readAsText(f); }});
  const bkf=NATIVE?(()=>{ const m2=el('span',{class:'note-saved'}), b=el('button',{class:'btn sm',type:'button'},'Save a backup file now'); b.addEventListener('click',()=>{ m2.textContent=' Saving…'; backupFile().then(r=>{ m2.textContent=' Saved to '+r.where+'.'; },e=>{ m2.textContent=' '+((e&&e.message)||'Could not save.'); }); });
    return el('div',null,P('The app also saves a backup file by itself each time a field log ends: Download / Lost Hidden Atlas / atlas-backup.json on the phone. It stays there if the app is removed. To bring it back, use "Restore" below and pick that file.'),el('div',{class:'row'},b,m2)); })():null;
  v.append(sec('Your data and backups',false,[bkf,
    P('Your progress, notes, moved pins, added places and trip are saved in this browser on this device only. They do not sync. Back them up before you clear browser data, and restore on another device.'),
    el('div',{class:'row'},b1,LOCAL?b2:null,b3),out,
    el('label',{class:'field',for:'bk-in',style:'margin-top:10px'},el('span',{text:'Restore'}),inp),
    el('div',{class:'row',style:'margin-top:6px'},el('button',{class:'btn sm',type:'button',onclick:()=>load(inp.value)},'Restore from pasted text'),file,msg),
    P('To grow the master list, use "Copy my additions for Claude" and paste it into a chat. Claude can fold them into the Atlas with drive times and old-map overlays.')]));
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
    offSec.lastChild.append(el('p',{text:(AT?'The app opens with no signal: the place list, lines and leads are built in.':'This hosted copy keeps itself on the phone after the first visit, so it opens with no signal.')+' Old survey maps are fetched one place at a time as you open them; saving a place for offline keeps its old map too.'}),el('div',{class:'row'},ab,am)); }
  offSec.addEventListener('toggle',()=>{ if(offSec.open) fillStor(); }); v.append(offSec);
}
function renderGuide(){
  if(guideBuilt) return; guideBuilt=true;
  const v=$('#v-guide'); const sec=(title,open,kids)=>{ const b=el('div',{class:'gb'}); kids.forEach(k=>k&&b.append(k)); return el('details',{class:'pad',open:open},el('summary',{text:title}),b); };
  const P=t=>el('p',{text:t});
  const cats=el('div',{class:'legend'}); Object.keys(CAT).forEach(k=>cats.append(el('span',null,el('span',{class:'dot',style:'--c:'+CAT[k][1]}),CAT[k][0])));
  const shapes=el('div',{class:'legend',style:'margin-top:8px'},
    el('span',null,el('span',{class:'dot',style:'--c:#666'}),'Solid: something to see'),
    el('span',null,el('span',{class:'dot hollow',style:'--c:#666'}),'Hollow: nothing left'),
    el('span',null,el('span',{class:'dot sq',style:'--c:#666'}),'Square: still standing'),
    el('span',null,el('span',{class:'dot',style:'--c:#666;border-radius:1px;transform:rotate(45deg)'}),'Diamond: a place you added'));
  v.append(sec('How to find a ruin with this',true,[
    P('Every pin carries an honest rating. "Exact" means it sits on the structure or marker. "On site" means it is inside the footprint. "Approximate" means the right vicinity only, and the dashed ring on the map shows how far off it could be.'),
    el('ul',null,
      el('li',{text:'Pick a place, then tick "Lay the old USGS map over the pin." Sheets from the 1890s to 1930s draw the hotels, trolley spurs and villages that are gone.'}),
      el('li',{text:'Switch the map to Leaf-off aerial. New York flies in early spring, so foundations and cellar holes show through bare trees.'}),
      el('li',{text:'Switch to LiDAR, zoom in, and change the light direction under More. Walls, canal prisms, rail grades and coaster footings stand out as straight lines no forest makes.'}),
      el('li',{text:'Tap Compare to swipe aerial against LiDAR. Turn on Public land and tap Owner? to see whose ground it is before you go.'}),
      el('li',{text:'Follow the lines. Old railroads, trolley lines and canals are drawn on the map; stations, mills, hotels and locks sat right beside them. Click a line to list the Atlas places along it in order, then walk the rest of it on LiDAR looking for platforms and foundations.'}),
      el('li',{text:'On site, open the Log tab and start a field log. It draws where you walk and lets you drop timed notes, then exports the track (GPX) and a note list with times to match against your footage.'}),
      el('li',{text:'Found the real spot? Open My notes, choose "Move the pin," and drag it. Right-click (or long-press) anywhere on the map for coordinates and links.'})),
    cats,shapes,el('div',{class:'legend',style:'margin-top:8px'},Object.keys(LK).map(k=>el('span',null,el('span',{class:'sw'+(LK[k][2]?' dash':''),style:'--c:'+LK[k][1]}),LK[k][0])))]));
  const ser=el('div',{class:'series'}); D.series.forEach(s=>{ const n=BASE.filter(x=>(x.tags||[]).indexOf(s.tag)>=0).length;
    ser.append(el('button',{type:'button',onclick:()=>{ clearF(); $('#q').value=''; F.tag=s.tag; showView('list'); refresh(); fitVisible(); }},el('b',{text:s.title+' · '+n+' stops'}),el('small',{text:s.note}))); });
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
  v.append(sec('Video series ideas',false,[P('Each one filters the map to its stops. Timing assumes leaf-off months, November to April, for anything in the woods.'),ser]));
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
      'Expect no signal in much of the Adirondacks and Catskills. Save the area offline from the place page and carry a satellite messenger.',
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
  v.append(sec('Settings, backups and storage',false,[P('Backups, restoring, offline map storage and the app\'s own settings are under the gear: tap More under the map, then the gear next to Done.'),
    el('div',{class:'row'},el('button',{class:'btn sm',type:'button',onclick:()=>openSettings()},'Open Settings')),P('Settings holds: theme, units and clock; how the map opens and your start place; Near me (how far to list, when to buzz); the field log; the episode kit; trimming a shared walk; backups; where the app gets its places; offline storage.'),
    el('div',{class:'row'},el('button',{class:'btn sm',type:'button',onclick:()=>{ openSheet(); showSettings(true); }},'Open settings'))]));
  v.append(sec('About this data',false,[
    P(BASE.length+' places, built '+D.built+'. '+BASE.filter(s=>s.tm).length+' have an old USGS map overlay. Pins: '+BASE.filter(s=>s.prec==='exact').length+' exact, '+BASE.filter(s=>s.prec==='site').length+' on site, '+BASE.filter(s=>s.prec==='area').length+' approximate.'),
    P('Drive times from the listed start cities were calculated by road with no traffic, so add a little. A place more than about 450 miles from your start city, or with no road to it, shows a rough estimate marked ~. Pick your own start point from "Drive times from."'),
    P('Later batches added '+BASE.filter(s=>s.new).length+' places: '+BATCHES.map(b=>b.label+' ('+b.n+')').join(', ')+'. Their pins come from the source named in each pin note and many were not checked on imagery, so read the pin note before you drive.'),
    P('Histories come from the Lost & Hidden catalogue and its linked sources. "Lead" entries were not re-checked against a source. Hours, access rules and demolition schedules change, so confirm before you drive.'),
    P('Imagery: New York State ITS Geospatial Services (orthoimagery and LiDAR), MassGIS and the Vermont Center for Geographic Information (their own spring flights and LiDAR), RIGIS and the University of Rhode Island Environmental Data Center (Rhode Island March 2026 aerials and 2022 LiDAR), USGS (topographic maps, The National Map), Esri and its data partners (streets and satellite). Rail and canal lines: OpenStreetMap contributors and OpenHistoricalMap (old lines), U.S. DOT North American Rail Network (lines in use); volunteer-mapped, so a missing line does not mean no line. Historic pockets: marker titles and positions from HMdb.org, the Historical Marker Database (hmdb.org), which the Atlas holds only in part for the busiest counties; National Register of Historic Places listings from the National Park Service, with positions corrected from Wikidata; town and village centres from OpenStreetMap contributors. The score shown on a pocket is a rough guide worked out by the Atlas, not a rating from any of these sources. Old lines are drawn for all of New York and Massachusetts so far, with a strip of western Connecticut and Vermont; other places have none yet. Public land: USGS Protected Areas Database (PAD-US), which can miss small local parks and lags new purchases. Owners and lot lines: NYS tax parcel file, NYS DEC and MassGIS property tax parcels; not every New York county shares owner names, and none of it is a survey. Leads: OpenStreetMap contributors, unchecked. Vanished places: U.S. Board on Geographic Names, Geographic Names Information System file of August 2021, unchecked. Old mines and quarries: U.S. Geological Survey Mineral Resources Data System, unchecked. Vector outline: Natural Earth. Routing: OSRM and OpenStreetMap contributors.')]));
}
function fitVisible(){ if(!map||!visible.length) return; const b=L.latLngBounds(visible.map(s=>{const p=pos(s);return [p.lat,p.lon];})); map.fitBounds(b.pad(0.15),{maxZoom:14}); }

/* ---------- wiring ---------- */
function buildHome(){
  const h=$('#home'); h.textContent='';
  STATES.forEach(st=>{ const hs=HUBS.filter(x=>x.st===st.k); if(hs.length) h.append(el('optgroup',{label:st.name},hs.map(x=>el('option',{value:x.id,text:x.name})))); });
  HUBS.filter(x=>!x.st).forEach(x=>h.append(el('option',{value:x.id,text:x.name})));
  if(U.home.id==='custom') h.append(el('option',{value:'custom',text:(U.home.name||'My spot')+' ('+U.home.lat.toFixed(3)+', '+U.home.lon.toFixed(3)+')'}));
  h.append(el('option',{value:'pick',text:'Pick a spot on the map…'}));
  h.value=U.home.id;
}
$('#home').addEventListener('change',e=>{
  const v=e.target.value;
  if(v==='pick'){ if(!map){ e.target.value=U.home.id; return; } pickingHome=true; stage.classList.add('adding'); $('#addbar').hidden=false; $('#addbar span').textContent='Click the map where you start from.'; e.target.value=U.home.id; return; }
  if(v==='custom') return;
  U.home={id:v,by:1}; save(); buildHome(); drawHome(); refresh(); if(sel) renderDetail(sel); { const H=homeObj(); if(map&&e.go) map.setView([H.lat,H.lon],10); }
});
$('#q').addEventListener('input',debounce(e=>{ F.q=e.target.value.trim(); renderList(); syncMarkers(); $('#fcount').textContent=activeCount()?activeCount()+' on':''; },150));
$('#sort').addEventListener('change',e=>{ U.ui.sort=e.target.value; save(); renderList(); });
$('#sort').value=U.ui.sort||'time';
document.querySelectorAll('.tabs button').forEach(b=>b.addEventListener('click',()=>{ const v=b.getAttribute('data-view'); if(v==='list'&&sel&&view!=='detail'){ showView('detail'); } else if(v==='list'){ if(sel) deselect(); else showView('list'); } else showView(v); }));
$('#add-here').addEventListener('click',()=>{ if(!geo.ll) return; adding=false; stage.classList.remove('adding'); $('#addbar').hidden=true; $('#add-here').hidden=true; openForm({lat:+geo.ll[0].toFixed(6),lon:+geo.ll[1].toFixed(6)}); });
$('#add-place').addEventListener('click',()=>{ if(!map) return; asking=false; adding=true; $('#add-here').hidden=!geo.ll; stage.classList.add('adding'); $('#addbar').hidden=false; $('#addbar span').textContent='Click the map where the place is.'; });
$('#rec-note').addEventListener('click',()=>{ const f=$('#rec-form'); f.hidden=!f.hidden; if(!f.hidden){ $('#rec-text').value=''; try{ $('#rec-text').focus(); }catch(e){} } });
$('#rec-form').addEventListener('submit',e=>{ e.preventDefault(); addNote($('#rec-text').value); $('#rec-form').hidden=true; });
{ const b=$('#rec-stop'); let armed=false; b.addEventListener('click',()=>{ if(!armed){ armed=true; b.textContent='Tap again to stop'; setTimeout(()=>{ armed=false; b.textContent='Stop'; },3500); return; } armed=false; b.textContent='Stop'; stopLog(); }); }
$('#add-cancel').addEventListener('click',()=>{ adding=false; pickingHome=false; asking=false; stage.classList.remove('adding'); $('#addbar').hidden=true; syncBar(); });
$('#sheet-x').addEventListener('click',closeSheet); $('#sheet-set').addEventListener('click',()=>showSettings(sheetMode!=='set')); $('#scrim').addEventListener('click',closeSheet);
document.addEventListener('keydown',e=>{ if(e.key==='Escape'){ if(!$('#sheet').hidden){ closeSheet(); } else if(adding||pickingHome||asking){ $('#add-cancel').click(); } else if(view==='detail'&&sel&&!/^(INPUT|TEXTAREA|SELECT)$/.test((e.target.tagName||''))) deselect(); } });
if(window.matchMedia('(min-width:821px)').matches) $('#filters').open=false;

buildHome(); buildFilters(); renderList(); $('#trip-n').textContent=U.trip.length;
if(pref('open')!=='last'&&LD[pref('open')]) U.ui.base=pref('open');
if(window.L){ initMap(); buildBar(); resumeLog(); pushPrefs(); }
else { $('#map').append(el('div',{class:'pad',style:'padding-block:40px;max-width:46ch;margin:auto',text:'The map library could not load, most likely because this device is offline. The list, place pages and links still work. Reload when you are back online.'})); $('#lbar').hidden=true; }
if(HOSTED&&!AT&&'serviceWorker' in navigator&&(location.protocol==='https:'||location.hostname==='localhost')) navigator.serviceWorker.register('sw.js').catch(()=>{});
/* the phone's Back button, in the app: close whatever is open; returning false lets Android put the app in the background */
window.atlasBack=()=>{
  if(!$('#sheet').hidden){ closeSheet(); return true; }
  if(adding||pickingHome||asking){ $('#add-cancel').click(); return true; }
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
(function fromHash(){ const id=decodeURIComponent((location.hash||'').replace(/^#/,'')); const s=id&&byId(id); if(s) select(s,true); })();
window.addEventListener('hashchange',()=>{ const id=decodeURIComponent((location.hash||'').replace(/^#/,'')); const s=id&&byId(id); if(s&&(!sel||sel.id!==s.id)) select(s,true); });
})();
