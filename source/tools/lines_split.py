#!/usr/bin/env python3
"""Cut the old rail and canal lines into what the hosted copy fetches.

build/lines.json holds every line the Atlas has, and each feature says which state it is in ("s", put there by
tools/lines.py). The Android app and the single-file copies read that one file. A browser on the hosted copy would have
to download all of it, states it will never look at included, so tools/make.py calls split() and the hosted copy gets:

   data/lines/<state>.json   one state's lines at full detail: the same features, without "s"
   data/lines/wide.json      every state's lines thinned for a wide view (zoom 8 and wider), by kind: {"ab":[piece,...],...}
   the index, in the page data as "lx":  {"w": stamp of wide.json, "s": {state: {"h": stamp, "c": [squares]}}}

A stamp is the first 8 characters of the file's MD5 and goes in the file's address, so the address changes only when the
content does and a phone keeps the copy it has across builds. "c" lists the quarter-degree squares the state's lines
touch, as pairs floor(lat*4), floor(lon*4): the app fetches a state when one of its squares is in or near the view.
(Half-degree squares were tried first. A line filed under New York dips a few kilometres into Pennsylvania near Great
Bend, which put New York in a square 55 km deep, and a phone looking at Scranton fetched all of New York for nothing.)

Only the standard library is used, because GitHub runs this at every build.

   python3 tools/lines_split.py          what it would write from build/lines.json, and how big
"""
import json,hashlib,math
WIDE_TOL=0.004        # what the app's zoom 7-8 level thins to (LLEV in app.js); a wider view thins this again
SQ=4                  # squares to a degree in the index; LSQ in app.js must say the same
def stamp(txt): return hashlib.md5(txt.encode('utf-8')).hexdigest()[:8]
def thin(part,tol):
    """Douglas-Peucker in degrees, the same as thinPart() in app.js."""
    n=len(part)
    if n<3: return part
    keep=bytearray(n); keep[0]=keep[n-1]=1; todo=[(0,n-1)]; kx=math.cos(math.radians(part[0][0])); t2=tol*tol
    while todo:
        a,b=todo.pop(); ax=part[a][1]*kx; ay=part[a][0]; dx=part[b][1]*kx-ax; dy=part[b][0]-ay; l2=dx*dx+dy*dy; md=0; mi=-1
        for i in range(a+1,b):
            px=part[i][1]*kx-ax; py=part[i][0]-ay
            t=(px*dx+py*dy)/l2 if l2 else 0
            t=0 if t<0 else 1 if t>1 else t
            ex=px-t*dx; ey=py-t*dy; e=ex*ex+ey*ey
            if e>md: md=e; mi=i
        if md>t2: keep[mi]=1; todo.append((a,mi)); todo.append((mi,b))
    return [part[i] for i in range(n) if keep[i]]
def squares(feats):
    """Every quarter-degree square a state's lines pass through. A long straight piece can cross a square without a point
    in it, so each stretch between two points counts for every square of the box round it."""
    out=set()
    for f in feats:
        for p in f['c']:
            for i in range(len(p)):
                a=p[i]; b=p[i-1] if i else a
                for la in range(math.floor(min(a[0],b[0])*SQ),math.floor(max(a[0],b[0])*SQ)+1):
                    for lo in range(math.floor(min(a[1],b[1])*SQ),math.floor(max(a[1],b[1])*SQ)+1): out.add((la,lo))
    return sorted(out)
def split(feats):
    """-> ({state: text of its file}, text of wide.json, the index). A feature with no "s" (a file from before the
    lines were sorted by state) goes under "zz", so nothing is ever left out."""
    by={}; wide={}
    for f in feats:
        by.setdefault(f.get('s') or 'zz',[]).append({'k':f['k'],'n':f['n'],'y':f['y'],'c':f['c']})
        for p in f['c']:
            q=thin(p,WIDE_TOL)
            if len(q)<3 and abs(q[0][0]-q[-1][0])+abs(q[0][1]-q[-1][1])<=WIDE_TOL*1.3: continue      # shorter than a pixel at zoom 8
            r=[]
            for la,lo in q:
                pt=[round(la,4),round(lo,4)]
                if not r or r[-1]!=pt: r.append(pt)
            if len(r)>1: wide.setdefault(f['k'],[]).append(r)
    files={}; idx={'w':'','s':{}}
    for st in sorted(by):
        files[st]=json.dumps(by[st],separators=(',',':'),ensure_ascii=False)
        idx['s'][st]={'h':stamp(files[st]),'c':[v for c in squares(by[st]) for v in c]}
    wtxt=json.dumps({k:wide[k] for k in sorted(wide)},separators=(',',':'))
    idx['w']=stamp(wtxt)
    return files,wtxt,idx
if __name__=='__main__':
    import time; t=time.time()
    files,wtxt,idx=split(json.load(open('build/lines.json',encoding='utf-8')))
    for st in sorted(files): print(f'  data/lines/{st}.json  {len(files[st].encode("utf-8"))//1024:5d} KB  {len(idx["s"][st]["c"])//2:3d} squares  stamp {idx["s"][st]["h"]}')
    print(f'  data/lines/wide.json {len(wtxt)//1024:5d} KB  {sum(len(p) for v in json.loads(wtxt).values() for p in v)} points')
    print(f'  index in the page: {len(json.dumps(idx,separators=(",",":")))} bytes; {time.time()-t:.1f} s')
