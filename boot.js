/* Start-up for the Android app. The website does not use this file.
   1. Picks the newest place data on the phone: the copy built into the app, or a newer one downloaded earlier.
   2. Starts the Atlas (app.js).
   3. Gives app.js three helpers through window.ATLAS: data refresh from the Atlas address, old survey maps that are
      fetched once and then kept, and calls to the phone's background field-log recorder. */
(function(){
'use strict';
var DEF='https://mrroot3r.github.io/Lost-and-Hidden-Atlas/';
function norm(u){ u=String(u||'').trim(); if(!/^https?:\/\/[^\s\/]+/i.test(u)) return ''; return u.replace(/[#?].*$/,'').replace(/index\.html$/i,'').replace(/\/*$/,'/'); }
var base=DEF; try{ base=norm(localStorage.getItem('atlas-base'))||DEF; }catch(e){}
var tag=document.getElementById('d-sites'), bundled={}; try{ bundled=JSON.parse(tag.textContent); }catch(e){}
var cap=window.Capacitor, native=!!(cap&&cap.isNativePlatform&&cap.isNativePlatform()&&cap.nativePromise);
var DATA='atlas-data', TOPO='atlas-topo', SITES='atlas-sites.json', urls={}, started=false;
var A=window.ATLAS={def:DEF,base:base,bundledV:bundled.v||'',dataV:bundled.v||'',fromCache:false,native:native,pending:'',checked:0};
function store(n){ return ('caches' in window)?caches.open(n):Promise.reject(new Error('no storage')); }
function get(u){ return fetch(u,{cache:'no-store'}).then(function(r){ if(!r.ok) throw new Error('http '+r.status); return r; }); }

/* the address the app reads places from; changing it takes effect at the next check */
A.setBase=function(u){ var n=norm(u); if(!n) return false; A.base=n; A.pending=''; try{ if(n===DEF) localStorage.removeItem('atlas-base'); else localStorage.setItem('atlas-base',n); }catch(e){} return true; };

/* calls into the phone: FieldLog.start, stop, points, status, share ... (see FieldLogPlugin.java) */
A.call=function(method,options){ return native?cap.nativePromise('FieldLog',method,options||{}):Promise.reject(new Error('This only works in the Android app.')); };

/* data/lines.json, data/leads.json and data/pockets.json: a downloaded copy if there is one, otherwise the copy built into the app */
A.fetch=function(path){ var p=path.split('?')[0]; if(!A.fromCache) return fetch(p);
  return store(DATA).then(function(c){ return c.match(p); }).then(function(r){ return r||fetch(p); },function(){ return fetch(p); }); };

/* one old survey map: fetched from the Atlas address the first time it is needed, then kept on the phone */
A.topo=function(id,v){ var key=id+'?'+(v||''); if(urls[key]) return Promise.resolve(urls[key]);
  var remote=A.base+'topo/'+id+'.webp'+(v?'?'+v:''), k='https://atlas.invalid/topo/'+encodeURIComponent(id)+'?'+(v||'');
  return store(TOPO).then(function(c){ return c.match(k).then(function(hit){ return hit||get(remote).then(function(n){ return c.put(k,n.clone()).then(function(){ return n; },function(){ return n; }); }); }); })
    .then(function(r){ return r.blob(); }).then(function(b){ urls[key]=URL.createObjectURL(b); return urls[key]; }); };

/* look for newer place data at the Atlas address; resolves {state:'same'|'updated'|'ready', v, places} or rejects when offline */
A.check=function(){ var b=A.base;
  return get(b+'version.json').then(function(r){ return r.json(); }).then(function(ver){
    A.checked=Date.now(); var out={state:'same',v:A.dataV,remote:ver.v};
    if(!ver.v||ver.v===A.dataV||!(ver.v>A.bundledV)) return out;
    if(ver.v===A.pending){ out.state='ready'; out.v=ver.v; return out; }
    return Promise.all([get(b+'index.html').then(function(r){ return r.text(); }),get(b+'data/lines.json'),get(b+'data/leads.json'),get(b+'data/pockets.json').then(function(r){ return r; },function(){ return null; })]).then(function(rs){
      var m=/<script type="application\/json" id="d-sites">([\s\S]*?)<\/script>/.exec(rs[0]); if(!m) throw new Error('That address does not hold an Atlas.');
      var j=JSON.parse(m[1]); if(!j||!j.sites||j.sites.length<50||j.v!==ver.v) throw new Error('The Atlas at that address is mid-update. Try again in a minute.');
      return store(DATA).then(function(c){ return c.put('data/lines.json',rs[1]).then(function(){ return c.put('data/leads.json',rs[2]); }).then(function(){ return rs[3]?c.put('data/pockets.json',rs[3]):null; }).then(function(){ return c.put(SITES,new Response(m[1],{headers:{'content-type':'application/json'}})); }); })
        .then(function(){ A.pending=ver.v; out.state='updated'; out.v=ver.v; out.places=j.sites.length; return out; }); }); }); };

/* forget downloaded data and go back to what the app was built with */
A.reset=function(){ return store(DATA).then(function(c){ return c.delete(SITES); }).then(function(){ A.pending=''; }); };

function start(){ if(started) return; started=true; var s=document.createElement('script'); s.src='app.js'; document.body.appendChild(s); }
var guard=setTimeout(start,2500);
store(DATA).then(function(c){ return c.match(SITES); }).then(function(r){ return r?r.text():null; }).then(function(txt){
  if(!txt||started) return; var j=JSON.parse(txt);
  if(j&&j.sites&&j.v&&j.v>A.bundledV){ tag.textContent=txt; A.dataV=j.v; A.fromCache=true; }
}).catch(function(){}).then(function(){ clearTimeout(guard); start(); });
})();
