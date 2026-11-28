#!/usr/bin/env python3
"""What is left to add, county by county: National Register listings the Atlas does not have.
   python3 tools/gaps.py mo                       Missouri: how many listings are left in each county, most first
   python3 tools/gaps.py mo "Pettis"              the listings left in Pettis County (name, kind, town, point, reference)
   python3 tools/gaps.py mo --near 39.10,-94.58   the counties nearest that point with enough left to work, nearest first
Run it BEFORE researching, right after the claim (tools/choose.py prints the same table for the state it drew). It takes
under a minute and stands in for the comparison several sessions wrote for themselves; one spent an hour on it.
A listing counts as left when no Atlas place is within 300 m of its point and none of the same name is within 3 km.
Archaeological sites are left out. Fewer than eight left in a county: do not start there. Counties marked DRY were given
up by a session in the last thirty days (tools/choose.py --dry) and are passed over.
The Register is not the only source (a town's walking tour, Clio, a county survey, the old town centres start.py
prints): a county with few listings left may still be worth a batch if you have such a source IN HAND, never on the hope
of finding one. Many listings are plain houses and apartment blocks: take what is worth a visit.
The Canadian provinces have no such list here, so nothing can be counted for them."""
import sys,os,re,json,subprocess
HERE=os.path.dirname(os.path.abspath(__file__)); W=os.path.dirname(HERE); os.chdir(W); sys.path.insert(0,HERE)
import dry
from states import STATES
def claim_lines():
    """the lines of claims.txt on the repository's "claims" branch (claims, dry counties, listings set aside), or []"""
    try:
        import base64,urllib.request
        j=json.load(urllib.request.urlopen(urllib.request.Request('https://api.github.com/repos/Mrroot3r/Lost-and-Hidden-Atlas/contents/claims.txt?ref=claims',headers={'User-Agent':'lost-hidden-atlas-research/1.0'}),timeout=30))
        return base64.b64decode(j['content']).decode().split('\n')
    except Exception: return []
def state_says_gone(st,reg):
    """reference numbers the state's own index marks demolished or delisted (Missouri's does, beside each listing)"""
    if st!='mo': return set()
    try:
        import form
        ix=[e for e in form.mo_index() if re.search(r'demolish|delist|removed|razed|destroyed',e['rest'],re.I)]
        if not ix: return set()
        by={}
        for r in reg: by.setdefault(form._words(r['n']),[]).append(str(r.get('ref','')))
        return {x for e in ix for x in by.get(form._words(e['name']),[])}
    except Exception: return set()
def left(st,lines=None):
    """(listings left in the state, or None when it cannot be measured; the state's name or why not).
    Listings a session set aside (choose.py --skip) and those the state's index marks demolished are not counted."""
    S=next((s for s in STATES if s['k']==st),None)
    if S is None: return None,'No state has the key "%s" (two letters, such as mo, ks, ny).'%st
    f='cache/nrhp/%s.json'%st; _why=''
    if not os.path.exists(f):      # the download's failure used to be thrown away, so a session saw "no list" with no reason (the asylum pass, November 28, 2026)
        try:
            _r=subprocess.run([sys.executable,'tools/nrhp_state.py',S['name'].upper(),st],capture_output=True,text=True,timeout=600)
            if _r.returncode: _why=([l for l in ((_r.stderr or '')+(_r.stdout or '')).strip().split('\n') if l.strip()] or [''])[-1][:160]
        except Exception as _e: _why=str(_e)[:160]
    if not os.path.exists(f): return None,'There is no National Register list for %s here: a Canadian province, or the Park Service\'s map service did not answer from this workspace%s. The count by county cannot be made this session; work from tools/start.py and the open leads, and say so in your note.'%(S['name'],' ('+_why+')' if _why else '')
    if not os.path.exists('build/sites.json'): subprocess.run([sys.executable,'tools/build_sites.py'],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
    reg=json.load(open(f,encoding='utf-8')); lines=claim_lines() if lines is None else lines
    skip={k.split(':',1)[1] for k in dry.skipped(lines) if k.startswith(st+':')}|state_says_gone(st,reg)
    return dry.gaps(reg,json.load(open('build/sites.json',encoding='utf-8')),None,skip=skip),S['name']
def table_lines(st,g,dry_now,near=None,n=3,passed=()):
    """the lines choose.py and this tool print: where to go, and where not to"""
    t=dry.county_table(g); out=[]
    nx=dry.next_counties(t,st,dict(dry_now,**{k:'left by this session' for k in passed}),near=near,n=n)
    if nx: out.append(('Nearest counties with enough left: ' if near else 'Counties to take (drawn by lot among those with enough left): ')+'; '.join('%s (%d left, round %.2f,%.2f)'%(c,v['left'],v['lat'],v['lon']) for c,v in nx))
    else: out.append('NO county of this state has %d or more listings left that is not marked dry. Draw other ground.'%dry.LIMIT)
    thin=sorted(c for c,v in t.items() if v['left']<dry.LIMIT); dd=sorted(c for c in t if dry.key(st,c) in dry_now)
    if dd: out.append('Marked DRY (given up in the last %d days; do not go there): '%dry.DAYS+', '.join(dd))
    out.append('Counties not named here have fewer than %d left or none: do not start a batch in one of them on Register lists alone.'%dry.LIMIT)
    return out,nx
if __name__=='__main__':
    a=sys.argv[1:]; near=None
    if '--near' in a:
        i=a.index('--near'); near=tuple(float(x) for x in a[i+1].split(',')); del a[i:i+2]
    if not a: sys.exit(__doc__)
    st=a[0].lower(); g,name=left(st)
    if g is None: print(name); print('NOT COUNTED. Judge the ground from what start.py prints and the sources you can open in the first ten minutes.'); sys.exit(0)
    dn=dry.dry_regions(claim_lines())
    if len(a)>1:
        rows=[r for r in g if (r.get('county') or '').lower()==a[1].lower().replace(' county','')]
        print('%s County, %s: %d National Register listing(s) the Atlas does not have.%s'%(a[1],name,len(rows),'  (marked DRY: '+dn[dry.key(st,a[1])]+')' if dry.key(st,a[1]) in dn else ''))
        for r in rows: print('  %-9s %-48s %-9s %-18s %.5f,%.5f  nearest Atlas place %.1f km'%(r.get('ref',''),r['n'][:48],r['k'],(r.get('town') or '')[:18],r['lat'],r['lon'],r['far']/1000))
        if dry.is_dry(len(rows)): print('Fewer than %d: do not start a batch here on these alone.'%dry.LIMIT)
        else: print('Read about them with  python3 tools/form.py <number> [<number> ...]  (the record, the form, the state\'s copy). Check each name against the place lists before writing (grep the id too): a Register point can be 300 m off the pin. One that is gone, unreadable, not wanted or already on the Atlas:  python3 tools/choose.py --skip <clone> %s <number> gone|nosource|notwanted|onatlas "<why or the Atlas id>"'%st)
        sys.exit(0)
    t=dry.county_table(g)
    print('%s: %d National Register listing(s) the Atlas does not have, in %d counties.'%(name,len(g),len(t)))
    for c,v in sorted(t.items(),key=lambda x:-x[1]['left'])[:30]: print('  %-22s %4d%s'%(c,v['left'],'   DRY' if dry.key(st,c) in dn else ''))
    for l in table_lines(st,g,dn,near)[0]: print(l)
