#!/usr/bin/env python3
"""Leads from video transcripts: which videos wait, who holds one, and the record of what came of each name.

The owner collects a channel's titles and transcripts on his own computer with tools/atlas_videos.py. The transcripts
stay there (they are the channel owner's work). A session reads ONE video's transcript, lists the buildings it names,
and researches them like any lead. What goes into the repository is the record: source/videos/<date>_<video id>.md,
one row per name with what came of it, so that no name is researched twice.

  python3 tools/videos.py list <index.csv> <clone>          the place videos nobody has worked or holds, most watched first
  python3 tools/videos.py claim <clone> <video id> [<region code>]
                                                            take a video (and the region its town is in) on the "claims"
                                                            branch, as tools/choose.py does; refused if either is held.
                                                            Give it up with:  python3 tools/choose.py --release <clone>
  python3 tools/videos.py new <index.csv> <video id> "<Town>" <state key> <batch key>
                                                            start the record: research/video_<id>.md, a table to fill in
  python3 tools/videos.py check <record.md>                 is the record complete? (every row an outcome, every place real)

`list` cannot tell from the index a video that walks through named buildings from a montage with music and no names
(a running time far shorter than the channel's usual 20 to 60 minutes is a hint), and a title beginning "Demolished"
names mostly buildings that are gone (49 of 53 in one Detroit video): look at the title and length before claiming.

A video is a stranger's tip: never a source for a fact. Names in captions are often misspelled, and "still stands" is
what the narrator thought. Every place added needs sources opened in the session, like any other."""
import sys,os,re,csv,json,time,random,subprocess,datetime
HERE=os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0,HERE)
from states import STATES
REPO='Mrroot3r/Lost-and-Hidden-Atlas'; BR='claims'
NAMES=sorted(((s['name'].lower(),s['k']) for s in STATES),key=lambda x:-len(x[0]))
NAME_OF={s['k']:s['name'] for s in STATES}
NOT_A_PLACE={'mausoleums','thoughts','favourites','favorites'}
OUTCOMES=('added','on the atlas','gone','not found','not checked','not a building','elsewhere')

def place_of(title):
    """('Town','ma') | ('', 'ne') a state with no town | ('Town', None) no state in the title | None: not a video about a place"""
    t=title.strip()
    if ':' in t: return None
    m=re.match(r'(?i)(old world|demolished)\s+(.+)$',t)
    if not m: return None
    rest=re.sub(r'(?i)\s+favou?rites$','',m.group(2)).strip(' ,')
    low=rest.lower()
    if low in NOT_A_PLACE or low.startswith('thoughts'): return None
    for name,k in NAMES:
        if low==name: return ('',k)
        if low.endswith(' '+name) or low.endswith(','+name): return (rest[:-len(name)].strip(' ,'),k)
    return (rest,None)

def read_index(lines):
    out=[]
    for r in csv.DictReader(l.lstrip('\ufeff') for l in lines):
        m=re.search(r'[?&]v=([A-Za-z0-9_-]+)',r.get('address',''))
        if not m: continue
        out.append({'id':m.group(1),'title':r.get('title',''),'date':r.get('date',''),'views':int(r['views']) if (r.get('views') or '').isdigit() else 0,
                    'minutes':r.get('minutes',''),'captions':r.get('captions','')=='yes','address':r['address'],'file':r.get('file','')})
    return out

def rows_of(md):
    """the table's rows as lists of five cells"""
    out=[]
    for l in md.split('\n'):
        if not l.startswith('|') or l.startswith('| Name as said') or re.match(r'\|\s*-',l): continue
        c=[x.strip() for x in l.strip().strip('|').split('|')]
        out.append((c+['']*5)[:5])
    return out

def done(clone):
    """video id -> how many of its names are still 'not checked', from the records in the clone"""
    d=os.path.join(clone,'source','videos'); out={}
    if not os.path.isdir(d): return out
    for n in os.listdir(d):
        m=re.match(r'\d{8}_(.+)\.md$',n)
        if m: out[m.group(1)]=sum(1 for c in rows_of(open(os.path.join(d,n),encoding='utf-8').read()) if c[4].lower()=='not checked')
    return out

def skeleton(row,town,k,channel,batch):
    place=', '.join(x for x in (town,NAME_OF.get(k,k or '')) if x)
    return ('# Video: %s\n\n- Address: %s\n- Channel: %s\n- Date: %s\n- Place: %s\n- Worked: %s, batch %s\n\n'
            'A video is a tip, not a source. "He said" is what the narrator said; the outcome is what a session found.\n\n'
            '| Name as said | Likely name | He said | At | Outcome |\n|---|---|---|---|---|\n')%(row['title'],row['address'],channel,row['date'],place,datetime.date.today().isoformat(),batch)

def problems(md,ids):
    out=[]; R=rows_of(md)
    if 'TODO' in md: out.append('a TODO is still in the record')
    if not R: out.append('the table has no names: list every building the video names, even those not researched')
    for c in R:
        o=c[4].lower()
        if not c[0]: out.append('a row has no name'); continue
        k=next((x for x in OUTCOMES if o==x or (o.startswith(x) and o[len(x)] in ' :,;(.')),None)          # a remark may follow: "gone: razed 1942"
        if not k: out.append('"%s": the outcome must begin with one of: %s'%(c[0],', '.join(OUTCOMES))); continue
        if k in ('added','on the atlas'):
            pid=(c[4][len(k):].strip(' :').split() or [''])[0].strip('`.,;:()')          # the id is the first word; a remark after it is not part of it ("added <id>: remark" too)
            if not pid: out.append('"%s": say which place: %s <place id>'%(c[0],k))
            elif pid not in ids: out.append('"%s": no such place id on the Atlas: %s'%(c[0],pid))
    return out

def sort_out(rows,D,claims,in_prs):
    """(free, busy, other): place videos nobody has worked or holds; those held; those that are not about one place"""
    free,busy,other=[],[],[]
    for r in rows:
        p=place_of(r['title'])
        if p is None: other.append(r); continue
        if r['id'] in D: continue
        r=dict(r,town=p[0],state=p[1])
        (busy if ('vid-'+r['id'] in claims or r['id'] in in_prs or not r['captions']) else free).append(r)
    free.sort(key=lambda r:-r['views'])
    return free,busy,other

def stamp(): return datetime.datetime.now(datetime.timezone.utc).strftime('%Y%m%dT%H%M%S')
def git(clone,*a): return subprocess.run(['git','-C',clone]+list(a),capture_output=True,text=True)
def read_claims(clone):
    git(clone,'fetch','-q','origin','+refs/heads/%s:refs/remotes/origin/%s'%(BR,BR))
    par=git(clone,'rev-parse','-q','--verify','refs/remotes/origin/'+BR).stdout.strip() or None
    txt=git(clone,'show','refs/remotes/origin/%s:claims.txt'%BR).stdout if par else ''
    return [l for l in txt.split('\n') if l.strip()],par
def write_claims(clone,lines,par,msg):
    blob=subprocess.run(['git','-C',clone,'hash-object','-w','--stdin'],input='\n'.join(lines)+'\n',capture_output=True,text=True).stdout.strip()
    tree=subprocess.run(['git','-C',clone,'mktree'],input='100644 blob %s\tclaims.txt\n'%blob,capture_output=True,text=True).stdout.strip()
    com=git(clone,'-c','user.name=atlas-session','-c','user.email=noreply@anthropic.com','commit-tree',tree,*(['-p',par] if par else []),'-m',msg).stdout.strip()
    return git(clone,'push','origin','%s:refs/heads/%s'%(com,BR))
def live(lines):
    """claims made in the last 8 hours and not released: what is held -> [tag]. The same rule as tools/choose.py."""
    now=datetime.datetime.now(datetime.timezone.utc); out={}; gone=set()
    for l in lines:
        p=l.split()
        if len(p)>=3 and p[0]=='released': gone.add(p[2])
    for l in lines:
        p=l.split()
        if len(p)<3 or p[0]=='released' or p[2] in gone: continue
        try: t=datetime.datetime.strptime(p[1],'%Y%m%dT%H%M%S').replace(tzinfo=datetime.timezone.utc)
        except ValueError: continue
        if (now-t).total_seconds()<8*3600: out.setdefault(p[0],[]).append(p[2])
    return out
def open_pr_videos():
    """video ids named in the branch of an open pull request (a video session's branch is video-<id>)"""
    r=subprocess.run(['gh','api','repos/%s/pulls?state=open&per_page=100'%REPO,'--jq','.[].head.ref'],capture_output=True,text=True)
    return {m.group(1) for l in r.stdout.split('\n') for m in [re.match(r'video-(.+)$',l.strip())] if m} if r.returncode==0 else set()

def main(a):
    if len(a)>=3 and a[0]=='list':
        rows=read_index(open(a[1],encoding='utf-8-sig').read().split('\n')); clone=a[2]
        git(clone,'fetch','-q','origin','main'); D=done(clone); claims=live(read_claims(clone)[0])
        free,busy,other=sort_out(rows,D,claims,open_pr_videos())
        print('%d videos collected; %d already worked (%d of them with names still not checked); %d held by another session or without captions; %d not about one place.'%(len(rows),len(D),sum(1 for x in D.values() if x),len(busy),len(other)))
        print('FREE, most watched first (id, views, minutes, town, state):')
        for r in free: print('  %s  %7d  %3s  %s%s'%(r['id'],r['views'],r['minutes'],r['town'] or '(the whole state)',', '+NAME_OF[r['state']] if r['state'] else '   [no state in the title: work it out, and skip it if it is outside the US and Canada]'))
        if not free: print('  none. Nothing to do until more videos are collected.')
        held=sorted(k for k in claims if not k.startswith('vid-'))
        if held: print('Regions held by research sessions just now: '+', '.join(held)+'. Take a video whose town is not in one of them.')
        return
    if len(a)>=3 and a[0]=='claim':
        clone,vid=a[1],a[2]; reg=a[3] if len(a)>3 else None; f=os.path.join(os.path.dirname(HERE),'.claim')
        if os.path.exists(f): sys.exit('This workspace already holds a claim: '+open(f).read().strip()+'. Work on that, or release it first (tools/choose.py --release).')
        if vid in done(clone): sys.exit('TAKEN: that video has already been worked (source/videos/). Pick another.')
        if vid in open_pr_videos(): sys.exit('TAKEN: an open pull request is working that video. Pick another.')
        for attempt in range(8):
            lines,par=read_claims(clone); L=live(lines)
            if 'vid-'+vid in L: sys.exit('TAKEN: another session holds that video. Pick another.')
            if reg and reg in L: sys.exit('TAKEN: a research session holds region %s just now. Pick a video in another region.'%reg)
            st=stamp(); tag='%04x'%random.SystemRandom().randrange(65536)
            new=['vid-%s %s %s'%(vid,st,tag)]+(['%s %s %s'%(reg,st,tag)] if reg else [])
            r=write_claims(clone,lines+new,par,'claim video '+vid)
            if r.returncode==0:
                open(f,'w').write('%s %s %s'%(reg or 'vid-'+vid,st,tag)); print('Claimed video %s%s. Give it up once the pull request is open:  python3 tools/choose.py --release %s'%(vid,' and region '+reg if reg else '',clone)); return
            if 'rejected' in r.stderr or 'fetch first' in r.stderr or 'non-fast-forward' in r.stderr: time.sleep(random.SystemRandom().uniform(0.5,2.5)); continue
            sys.exit('The claim could not be pushed (%s). Attach the repository with push access and run this again.'%(r.stderr.strip().split('\n')[-1][:120]))
        sys.exit('The claims branch was busy eight times running. Run this again.')
    if len(a)>=6 and a[0]=='new':
        rows={r['id']:r for r in read_index(open(a[1],encoding='utf-8-sig').read().split('\n'))}
        if a[2] not in rows: sys.exit('No such video id in '+a[1])
        if a[4] not in NAME_OF: sys.exit('No such state or province key: '+a[4])
        r=rows[a[2]]; os.makedirs('research',exist_ok=True); p='research/video_%s.md'%a[2]
        if os.path.exists(p): sys.exit(p+' is already there.')
        open(p,'w',encoding='utf-8').write(skeleton(r,a[3],a[4],'Old World Exploration' if 'oldworldex' in a[1].replace('\\','/').lower() else 'the channel in '+os.path.basename(os.path.dirname(a[1])),a[5]))
        print('Wrote %s. Add one row for every building the video names. When the work is done, copy it into the clone as source/videos/%s.md'%(p,r['file'][:-4] if r['file'].endswith('.txt') else r['date'].replace('-','')+'_'+a[2])); return
    if len(a)>=2 and a[0]=='check':
        sj=next((x for x in ('build/sites.json',os.path.join(os.path.dirname(HERE),'build','sites.json')) if os.path.exists(x)),None)   # the working folder's built list, wherever this is run from
        if not sj: sys.exit('No build/sites.json: run  python3 tools/build_sites.py  in the working folder first (the clone has no built place list).')
        ids={s['id'] for s in json.load(open(sj))}
        P=problems(open(a[1],encoding='utf-8').read(),ids)
        for p in P: print('PROBLEM: '+p)
        R=rows_of(open(a[1],encoding='utf-8').read()); n=lambda k:sum(1 for c in R if c[4].lower().startswith(k))
        print('%d names: %d added, %d already on the Atlas, %d gone, %d not found, %d not checked, %d other.'%(len(R),n('added'),n('on the atlas'),n('gone'),n('not found'),n('not checked'),len(R)-n('added')-n('on the atlas')-n('gone')-n('not found')-n('not checked')))
        sys.exit(1 if P else 0)
    print(__doc__)
if __name__=='__main__': main(sys.argv[1:])
