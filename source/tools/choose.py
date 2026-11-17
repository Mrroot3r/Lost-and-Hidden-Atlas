#!/usr/bin/env python3
"""Choose ground for a "you choose" session so that sessions started together do not pick the same place.
   python3 tools/choose.py                     show the candidates and what is taken; choose nothing
   python3 tools/choose.py --claim <clone>     pick one AT RANDOM among thin regions nobody has taken, and claim it
   python3 tools/choose.py --release <clone>   give the claim up (run it after the pull request is open)
Why random: "take the thinnest region" is the same answer for every session, so four sessions started in one hour all
took the same county. A claim is one line added to claims.txt on the repository's "claims" branch, pushed at once. Git refuses the second of
two pushes made at the same moment, and that session reads again and picks other ground, so two sessions cannot hold
the same region. A claim lapses after eight hours. Ground named in an open pull request counts as taken too.
A region is thin when it has few places; regions in the states the tools know best (leaf-off imagery, LiDAR, old town
centres) are twice as likely to come up. After the claim, run  python3 tools/start.py "<the region's start city>"."""
import sys,os,re,json,time,random,subprocess,urllib.request,datetime
HERE=os.path.dirname(os.path.abspath(__file__)); W=os.path.dirname(HERE); os.chdir(W); sys.path.insert(0,HERE)
REPO='Mrroot3r/Lost-and-Hidden-Atlas'
def api(path):
    for k in range(3):
        try: return json.load(urllib.request.urlopen(urllib.request.Request('https://api.github.com/repos/%s/%s'%(REPO,path),headers={'User-Agent':'lost-hidden-atlas-research/1.0','Accept':'application/vnd.github+json'}),timeout=30))
        except Exception as e: err=e; time.sleep(2+2*k)
    raise err
def git(clone,*a): return subprocess.run(['git','-C',clone]+list(a),capture_output=True,text=True)
if not os.path.exists('build/sites.json'): subprocess.run([sys.executable,'tools/build_sites.py'],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
from states import STATES
S=json.load(open('build/sites.json')); cnt={}
for s in S: cnt[s['reg']]=cnt.get(s['reg'],0)+1
DEEP={'ny','ma','vt','ct','nh','ri','nj','pa','me'}
REG=[(c,l,st['name'],st['k']) for st in STATES for c,l in st['regions']]
BR='claims'      # one long-lived branch holding claims.txt: "region  UTC time  tag" a line. Pushing to it is the lock:
                 # git refuses the second of two pushes made from the same state, and that session reads again and re-picks.
def read_claims(clone):
    """(lines, parent commit or None), fresh from the remote"""
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
    """claims made in the last 8 hours and not released: region -> [tag]"""
    now=datetime.datetime.now(datetime.timezone.utc); out={}; gone=set()
    for l in lines:
        p=l.split()
        if len(p)>=3 and p[0]=='released': gone.add(p[2])
    for l in lines:
        p=l.split()
        if len(p)<3 or p[0]=='released' or p[2] in gone: continue
        try: t=datetime.datetime.strptime(p[1],'%Y%m%dT%H%M%S').replace(tzinfo=datetime.timezone.utc)
        except ValueError: continue
        if (now-t).total_seconds()<8*3600: out.setdefault(p[0],[]).append('claimed '+p[1]+' ('+p[2]+')')
    return out
def open_prs():
    r=subprocess.run(['gh','api','repos/%s/pulls?state=open&per_page=50'%REPO],capture_output=True,text=True) if subprocess.run(['which','gh'],capture_output=True).returncode==0 else None
    if r is not None and r.returncode==0: return json.loads(r.stdout)
    return api('pulls?state=open&per_page=50')
def taken(clone=None):
    """region code -> why it is taken"""
    out={}
    if clone: out=live(read_claims(clone)[0])
    else:
        try:
            import base64; out=live(base64.b64decode(api('contents/claims.txt?ref='+BR)['content']).decode().split('\n'))
        except Exception: pass
    try:
        for p in open_prs():
            txt=(p['title']+' '+p['head']['ref']).lower()
            for c,l,sn,k in REG:
                words=[w for w in re.split(r'[^a-z]+',l.lower()) if len(w)>4 and w not in ('county','valley','north','south','western','eastern','central','northern','southern','places','massachusetts','connecticut','vermont','hampshire','jersey','pennsylvania','island','maine')]
                if c in re.split(r'[^a-z0-9]+',p['head']['ref'].lower()) or (words and any(w in txt for w in words)): out.setdefault(c,[]).append('open pull request #%d'%p['number'])
    except Exception as e: print('(The open pull requests could not be listed: %s. Look at them on GitHub before trusting this list.)'%str(e)[:60])
    return out
def pick(tk):
    cand=[(c,l,sn,k) for c,l,sn,k in REG if c not in tk]
    w=[(2.0 if k in DEEP else 1.0)/(cnt.get(c,0)+3) for c,l,sn,k in cand]
    return random.SystemRandom().choices(cand,weights=w,k=1)[0]
a=sys.argv[1:]
if a[:1]==['--release']:
    clone=a[1]; f=os.path.join(W,'.claim')
    if not os.path.exists(f): sys.exit('No claim is recorded in this workspace.')
    reg,stamp,tag=open(f).read().split()
    for k in range(5):
        lines,par=read_claims(clone)
        if write_claims(clone,lines+['released %s %s'%(stamp,tag)],par,'release '+reg).returncode==0: os.remove(f); print('Released the claim on '+reg+'.'); sys.exit(0)
        time.sleep(1+k)
    print('The release could not be pushed; the claim lapses by itself eight hours after it was made.'); sys.exit(0)
if a[:1]==['--claim']:
    clone=a[1]
    if os.path.exists(os.path.join(W,'.claim')): sys.exit('This workspace already holds a claim: '+open(os.path.join(W,'.claim')).read().strip()+'. Work on that, or --release it first.')
    pushed=False
    for attempt in range(8):
        lines,par=read_claims(clone); tk=taken(clone); c,l,sn,k=pick(tk)
        stamp=datetime.datetime.now(datetime.timezone.utc).strftime('%Y%m%dT%H%M%S'); tag='%04x'%random.SystemRandom().randrange(65536)
        r=write_claims(clone,lines+['%s %s %s'%(c,stamp,tag)],par,'claim '+c)
        if r.returncode==0: pushed=True; open(os.path.join(W,'.claim'),'w').write('%s %s %s'%(c,stamp,tag)); break
        if 'rejected' in r.stderr or 'fetch first' in r.stderr or 'non-fast-forward' in r.stderr: time.sleep(random.SystemRandom().uniform(0.5,2.5)); continue     # another session wrote first: read again and pick again
        print('The claim could not be pushed (%s). Chosen at random all the same.'%(r.stderr.strip().split('\n')[-1][:90])); break
    hubs=[h for h in json.load(open('build/hubs.json')) if h.get('st')==k] if os.path.exists('build/hubs.json') else []
    print('CHOSEN: region %s = %s, %s (%d places so far).'%(c,l,sn,cnt.get(c,0)))
    if pushed: print('Claimed on the "claims" branch. Run  python3 tools/choose.py --release %s  once your pull request is open.'%clone)
    print('Work anywhere inside that region: pick a town or county in it and run  python3 tools/start.py "<Town, %s>"'%sn+(('   (start cities in the state: '+', '.join(h['name'] for h in hubs[:3])+')') if hubs else ''))
    print('Use reg=\'%s\', and a file name and batch key that start with it and end in four random letters, such as data_%s_%s.py with key %s_xxxx.'%(c,c,''.join(random.SystemRandom().choice('abcdefghjkmnpqrstvwxyz') for _ in range(4)),c))
    sys.exit(0)
tk=taken()
print('Regions, thinnest first (x2 = twice as likely to be drawn; TAKEN = claimed or in an open pull request):')
for c,l,sn,k in sorted(REG,key=lambda r:cnt.get(r[0],0))[:45]: print('  %-6s %-34s %-16s %3d %s %s'%(c,l[:34],sn[:16],cnt.get(c,0),'x2' if k in DEEP else '  ','TAKEN: '+', '.join(tk[c])[:60] if c in tk else ''))
if tk: print('Taken now: '+'; '.join('%s (%s)'%(c,', '.join(v)[:50]) for c,v in tk.items()))
print('To choose and claim one at random:  python3 tools/choose.py --claim <path to the clone>')
