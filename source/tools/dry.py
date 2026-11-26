#!/usr/bin/env python3
"""Ground with nothing left to add, and how a session finds that out before it spends its time (used by tools/choose.py
and tools/gaps.py; test tools/choose_test.py).

Why: on November 25, 2026 the hourly Kansas City sessions kept returning to counties that ten notes in a row had called
worked out. One spent 25 minutes and added two places. Nothing recorded that a region was used up, and each session
measured it afresh with a script of its own.

Two things here, both plain functions with no network:
  gaps(register, atlas, region)   National Register listings in a region that have no Atlas place within 300 m and none
                                  of the same name within 3 km. Archaeological sites are left out (most are address-restricted).
  dry_regions(lines, now)         regions marked dry on the "claims" branch in the last 30 days and not taken back.
A region is dry when fewer than LIMIT listings are left (is_dry). A dry mark is one line in claims.txt:
  dry <region> <UTC time> <tag> <listings left>          and the owner or the maintainer takes one back with
  wet <region> <UTC time> <who>
An older copy of choose.py reads neither as a claim: it looks for a time in the second word and finds a region code."""
import re, math, datetime, unicodedata
LIMIT=8          # fewer Register listings left than this, and the region is dry
DAYS=30          # a dry mark lapses after this many days: places get listed, sources come back, a session may know better
REDRAWS=2        # how many times one session may give ground up and draw again
NEAR_M=300       # an Atlas place this close to a listing's point is taken to be that listing
NAME_M=3000      # and so is one of the same name within this distance (Register points are often a few hundred metres off)

def _t(s):
    try: return datetime.datetime.strptime(s,'%Y%m%dT%H%M%S').replace(tzinfo=datetime.timezone.utc)
    except ValueError: return None

def dry_regions(lines,now=None):
    """region -> why, for marks made in the last DAYS days and not taken back by a later 'wet' line"""
    now=now or datetime.datetime.now(datetime.timezone.utc); out={}; when={}
    for l in lines:
        p=l.split()
        if len(p)<3 or p[0] not in ('dry','wet'): continue
        t=_t(p[2])
        if t is None: continue
        if p[0]=='wet':
            if p[1] in when and t>=when[p[1]]: out.pop(p[1],None); when.pop(p[1],None)
            continue
        if (now-t).total_seconds()>=DAYS*86400: continue
        if p[1] in when and when[p[1]]>t: continue
        left=p[4] if len(p)>4 else '?'
        when[p[1]]=t; out[p[1]]='marked dry %s, %s Register listing(s) left'%(t.strftime('%Y-%m-%d'),left)
    return out

def may_redraw(done): return done<REDRAWS
def is_dry(n): return n<LIMIT

def _words(name):
    """the words of a name, lower case, with accents, apostrophes of either kind and punctuation gone; 'Wilson, John, House'
    and 'John Wilson House' give the same set"""
    s=unicodedata.normalize('NFKD',name or '').encode('ascii','ignore').decode().lower()
    s=re.sub(r"\(.*?\)"," ",s).replace("'","")
    return frozenset(w for w in re.findall(r'[a-z0-9]+',s) if w not in ('the','and','of','a','at','old','former'))

def _m(a,b,c,d): return math.hypot((a-c)*111200,(b-d)*111200*math.cos(math.radians(a)))

def gaps(register,atlas,region):
    """Register listings (dicts with n, k, lat, lon, town, county) that fall in `region` and that the Atlas does not have.
    A listing falls in the region of the nearest Atlas place; with no Atlas place within 150 km it is in none."""
    out=[]
    for r in register:
        if r.get('k')=='site' or r.get('lat') is None: continue
        best=None; bd=1e12; near=[]
        for s in atlas:
            if abs(s['lat']-r['lat'])>1.4: continue
            d=_m(r['lat'],r['lon'],s['lat'],s['lon'])
            if d<bd: bd=d; best=s
            if d<=NAME_M: near.append(s)
        if region is not None and (best is None or bd>150000 or best['reg']!=region): continue
        if bd<=NEAR_M: continue
        w=_words(r['n']); names=[n for n in [_words(s.get('name','')) for s in near]+[_words(s.get('name2','')) for s in near] if n]
        if w and any(w<=n or (len(n)>=2 and n<=w) for n in names): continue      # the same name within NAME_M: the Atlas has it, its pin is elsewhere
        out.append(dict(r,far=int(min(bd,9e8))))
    return out

PLENTY=25        # a county with this many listings left is never called dry: the trouble is the sources, so try others

def key(st,county): return st.lower()+':'+re.sub(r'\s+','',(county or '?').lower())
def can_mark(left): return left<PLENTY

def county_table(g):
    """county -> {'left': listings left, 'lat','lon': their middle}, from gaps(register, atlas, None)"""
    t={}
    for r in g:
        c=r.get('county') or '?'; v=t.setdefault(c,{'left':0,'lat':0.0,'lon':0.0}); v['left']+=1; v['lat']+=r['lat']; v['lon']+=r['lon']
    for v in t.values(): v['lat']/=v['left']; v['lon']/=v['left']
    return t

def next_counties(table,st,dry_now,near=None,rnd=None,n=3):
    """up to n counties worth a batch: LIMIT or more listings left and not marked dry. Near a city (lat, lon): the nearest
    first, so a task tied to a city works outward. Otherwise drawn by lot, weighted by what is left, so sessions started
    together spread out."""
    import random
    c=[(k,v) for k,v in table.items() if k!='?' and v['left']>=LIMIT and key(st,k) not in dry_now]
    if near: return sorted(c,key=lambda kv:_m(near[0],near[1],kv[1]['lat'],kv[1]['lon']))[:n]
    rnd=rnd or random.SystemRandom(); out=[]
    while c and len(out)<n:
        i=rnd.choices(range(len(c)),weights=[v['left']**0.5 for k,v in c],k=1)[0]; out.append(c.pop(i))
    return out
