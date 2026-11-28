#!/usr/bin/env python3
"""The guard against one place entered twice. Rules only: no network, no files read unless run as a command.
   python3 tools/dupes.py [<clone>]                 every unsettled pair on the map, nearest first
   python3 tools/dupes.py [<clone>] <place id>      the pairs one place is in
tools/check.py uses clash(), find() and apart_problem(); tools/dupes_test.py holds them to their behaviour.

WHY. Eight places were found entered twice on November 26, 2026 (the Insley House, the Wyoming capitol, St. George's in
Austin, Five Combines, Rush, Elkmont, the Lawrence Carnegie library, the Scott ice house). Nothing compared a new entry
with what stood beside it: a session checked the id and, at best, the list start.py printed. Every one of the eight was
within 100 m of its twin, and all but one carried its twin's name or a longer or shorter form of it.

THE RULE. Two entries clash when
  spot   they are within SPOT_M (15 m) of each other, whatever they are called: two pins on one building; or
  name   they are within NAME_M (300 m) and carry the same name. The same name means the same words, or all the words of
         one inside the other. Left out of a name: anything in brackets, the town's own words (so "..., Leavenworth" adds
         nothing), and the, and, of, old, former, site, ruins. A name given in brackets counts only when it is exactly the
         other entry's name ("The Castle" in brackets, and an entry called The Castle).
         A name that only says what kind of thing it is ("Post Office", "The Old House") matches only the very same words.
A clash is not always a mistake: a ghost town and its church, a hotel and its pump house, the old city hall and the new one
across the street. Then the entry says so itself:  apart='<the other id>: <why they are two places>'  (or a list of them).
It is written in the place list, not in a shared file, because sessions run side by side and a shared file collides.

What it deliberately does not catch: two entries for one place under names with no word in common, more than 15 m apart.
A looser rule (any shared word within 60 m) named 120 pairs of neighbours of which three were doubles."""
import re, math, unicodedata, collections
SPOT_M=15; NAME_M=300; WHY_MIN=15
STOP=frozenset('the and of a an at in on old former site ruins ruin remains'.split())
# words that say what kind of thing a place is. A name made only of these ("House", "Post Office", "State Capitol") is inside
# half the names in a town, so it matches another name only when the two are the same words exactly.
KIND=frozenset('''house home mansion farm barn church chapel cathedral meetinghouse synagogue temple building block hall library school
academy college bank hotel inn tavern mill mills factory works store shop station depot bridge courthouse court jail post office city town
village county state capitol federal public municipal theatre theater opera cemetery fort museum district historic park street avenue road
first second third st saint new north south east west main'''.split())

def _toks(s):
    s=unicodedata.normalize('NFKD',s or '').encode('ascii','ignore').decode().lower().replace("'","")
    return frozenset(re.findall(r'[a-z0-9]+',s))-STOP
def _m(a,b,c,d): return math.hypot((a-c)*111200,(b-d)*111200*math.cos(math.radians((a+c)/2)))

def _names(p,tw):
    """(the names outside brackets, the names given in brackets), each a set of words with the town's words taken out"""
    n=p.get('name') or ''; base=re.sub(r'\(.*?\)',' ',n); out=set(); alt=set()
    full=_toks(base); out.add((full-tw) or full)
    first=_toks(re.split(r'[,:]',base)[0])-tw
    if first: out.add(first)
    for br in re.findall(r'\((.*?)\)',n):
        for part in re.split(r'\s*[,;]\s*|\s+or\s+',br):
            t=_toks(part)-tw
            if t: alt.add(t)
    return out,alt
def same_name(a,b):
    tw=_toks(a.get('town'))|_toks(b.get('town')); A,Aalt=_names(a,tw); B,Balt=_names(b,tw)
    for x in A:
        for y in B:
            if x==y or ((x<y or y<x) and not (min(x,y,key=len)<=KIND)): return True
    return bool((Aalt&B)|(Balt&A))

def clash(a,b):
    """('name'|'spot', metres apart) when the two entries look like one place, else None. Takes no account of apart=."""
    d=_m(a['lat'],a['lon'],b['lat'],b['lon'])
    if d<=NAME_M and same_name(a,b): return ('name',d)
    if d<=SPOT_M: return ('spot',d)
    return None

def _apart(p):
    v=p.get('apart') or []
    return [v] if isinstance(v,str) else list(v)
def apart_ids(p): return {str(x).split(':',1)[0].strip() for x in _apart(p)}
def apart_problem(p,ids):
    """what is wrong with an entry's apart=, or None. ids: every place id on the map (landmark pins, lm-..., included)"""
    for x in _apart(p):
        if not isinstance(x,str) or ':' not in x: return "apart= must read '<the other place's id>: <why they are two places>'"
        i,why=[t.strip() for t in x.split(':',1)]
        if i==p['id']: return "apart='%s: ...' names the entry itself; it must name the other place"%i
        if i not in ids: return "apart='%s: ...' names no place on the map (check the id)"%i
        if len(why)<WHY_MIN: return "apart='%s: %s' gives no reason. Say in a few words why they are two places (what each one is)"%(i,why)
    return None

def find(places,only=None):
    """every clash not settled by apart=, as dicts a (the lower id), b, kind, m; nearest first. only: a set of ids, to
    report just the pairs they are in. An entry that replaces another (was=) does not clash with it."""
    G=collections.defaultdict(list); P=list(places)
    for i,p in enumerate(P): G[(int(math.floor(p['lat']/0.004)),int(math.floor(p['lon']/0.008)))].append(i)
    out=[]
    for i,p in enumerate(P):
        ca,cb=int(math.floor(p['lat']/0.004)),int(math.floor(p['lon']/0.008))
        for da in(-1,0,1):
            for db in(-1,0,1):
                for j in G.get((ca+da,cb+db),()):
                    if j<=i: continue
                    q=P[j]
                    if only is not None and p['id'] not in only and q['id'] not in only: continue
                    c=clash(p,q)
                    if not c: continue
                    if q['id'] in apart_ids(p) or p['id'] in apart_ids(q): continue
                    w=lambda r:{r['was']} if isinstance(r.get('was'),str) else set(r.get('was') or ())
                    if q['id'] in w(p) or p['id'] in w(q): continue
                    a,b=sorted((p['id'],q['id'])); out.append(dict(a=a,b=b,kind=c[0],m=c[1]))
    out.sort(key=lambda x:(x['m'],x['a'],x['b'])); return out

def line(x,byid,new=None):
    """the sentence for one clash, written about the newer entry (new: its id; the higher id when not given)"""
    n=new if new in (x['a'],x['b']) else x['b']; o=x['a'] if n==x['b'] else x['b']
    how='and carries the same name' if x['kind']=='name' else 'on the same spot'
    fix=("the map has a thin landmark pin for it: give your entry was='%s' and the pin is replaced"%o) if o.startswith('lm-') else \
        ("do not add it again. Improve the entry that is there, or, if yours is the fuller one, give it was='%s' and take the other out of its list"%o)
    return "%s is %d m from %s (\"%s\"), %s. If it is the same place, %s. If they are two places, say so in the entry: apart='%s: <why they are two places>'"%(n,round(x['m']),o,(byid.get(o) or {}).get('name',''),how,fix,o)

if __name__=='__main__':
    import sys,os,glob,importlib,json
    a=[x for x in sys.argv[1:]]
    W=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    repo=a.pop(0) if a and os.path.isdir(os.path.join(a[0],'source','tools')) else None
    T=os.path.join(repo,'source','tools') if repo else os.path.join(W,'tools')
    sys.path.insert(0,T); sys.dont_write_bytecode=True
    import safe_data; safe_data.must(T)
    P=[]
    from data_a import A
    for r in A: P.append(dict(id=r[1],name=r[2],town=r[3],lat=r[7],lon=r[8],apart=r[13].get('apart','')))
    from data_b import B
    P+=list(B)
    for f in sorted(glob.glob(os.path.join(T,'data_*.py'))):
        nm=os.path.basename(f)[:-3]
        if nm not in('data_a','data_b'): P+=list(getattr(importlib.import_module(nm),'PLACES',[]))
    byid={p['id']:p for p in P}; f=find(P,only=set(a) if a else None)
    for x in f: print('%4d m  %-5s %s  |  %s\n          "%s"  |  "%s"'%(round(x['m']),x['kind'],x['a'],x['b'],byid[x['a']]['name'],byid[x['b']]['name']))
    print('%d pair(s) of entries that look like one place and are not settled%s. (Landmark pins, lm-..., are compared by tools/check.py only.)'%(len(f),' for '+', '.join(a) if a else ''))
