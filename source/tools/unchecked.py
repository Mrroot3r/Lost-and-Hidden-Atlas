#!/usr/bin/env python3
"""Research that went onto the map without a second look.

A research-only pull request from the owner's own sessions merges by itself once the checks pass (.github/workflows/
check.yml, GUIDE.md section 3), and is labelled "not double-checked". This lists those, oldest first, so a stronger
model can be sent to review them later (GUIDE.md section 14).

   python3 tools/unchecked.py              the pull requests still waiting for a second look, with their data files
   python3 tools/unchecked.py --done 81    after reviewing #81 in full (section 14): take the label off and put "double-checked" on
   python3 tools/unchecked.py --sample     the lighter check the owner asked for: one place drawn at random from each waiting
                                           batch, and the pin-check command for them (run it from the working folder)
   python3 tools/unchecked.py --sampled 81 82 ...    after looking at those pins: mark the batches "sample-checked"

"double-checked" means somebody opened the sources and looked at every pin. "sample-checked" means the automated checks ran
over every place and one pin drawn at random was looked at on the aerial; it says the batch is not careless, not that every
place in it is right.

Needs the gh command signed in to the repository."""
import sys,json,subprocess
REPO='Mrroot3r/Lost-and-Hidden-Atlas'; LAB='not double-checked'
def gh(*a,inp=None):
    r=subprocess.run(['gh','api']+list(a),capture_output=True,text=True,input=inp)
    if r.returncode: sys.exit('gh could not do that: '+(r.stderr.strip() or r.stdout.strip())[:200])
    return json.loads(r.stdout) if r.stdout.strip() else None
a=sys.argv[1:]
def relabel(nums,new,colour,what):
    if not any(l['name']==new for l in gh('repos/%s/labels?per_page=100'%REPO)): gh('-X','POST','repos/%s/labels'%REPO,'-f','name='+new,'-f','color='+colour,'-f','description='+what)
    for n in nums:
        n=n.lstrip('#')
        gh('-X','POST','repos/%s/issues/%s/labels'%(REPO,n),'--input','-',inp=json.dumps({'labels':[new]}))
        subprocess.run(['gh','api','-X','DELETE','repos/%s/issues/%s/labels/%s'%(REPO,n,LAB.replace(' ','%20'))],capture_output=True)
        print('#%s is marked %s.'%(n,new))
# ---- a pin (or anything else about a place) that a session could not settle from here: an issue for a person to look at.
# The owner's idea, November 20, 2026: "a folder for that, some more stuff for me or someone else to work on".
#   python3 tools/unchecked.py --human <place id> "<what was looked at, and why it could not be told>"   (add --dry to see it without filing)
#   python3 tools/unchecked.py --human              lists the ones still open
HUMAN='needs a human'
if a[:1]==['--human']:
    import os
    dry='--dry' in a; b=[x for x in a[1:] if x!='--dry']
    if not b:
        got=gh('repos/%s/issues?state=open&labels=%s&per_page=100'%(REPO,HUMAN.replace(' ','%20'))) or []
        print('%d waiting for a person (https://github.com/%s/issues?q=is%%3Aopen+label%%3A%%22needs+a+human%%22):'%(len(got),REPO))
        for i in got: print('  #%d  %s'%(i['number'],i['title']))
        sys.exit(0)
    if len(b)<2 or len(b[1].strip())<20: sys.exit('Give the place id and a sentence or two: what you looked at and why it could not be told from here.')
    W=os.path.dirname(os.path.dirname(os.path.abspath(__file__))); sj=os.path.join(W,'build','sites.json')
    if not os.path.exists(sj): sys.exit('Run this from the working folder after build_sites.py: build/sites.json is not there.')
    pl=next((x for x in json.load(open(sj)) if x['id']==b[0]),None)
    if not pl: sys.exit('No place has the id '+b[0])
    title='Needs a look: %s, %s (%s)'%(pl['name'],pl.get('town',''),pl['id'])
    body='\n'.join(['**Place:** [%s](https://mrroot3r.github.io/Lost-and-Hidden-Atlas/#%s), %s'%(pl['name'],pl['id'],pl.get('town','')),
        '**Pin:** %s, %s  ·  batch `%s`'%(pl['lat'],pl['lon'],pl.get('new') or 'first catalogue'),'',
        '**What a session could not settle from here:**',b[1].strip(),'',
        'A person who knows the place, or stands there, can settle it: say in a comment what is right (and where the thing really is, if the pin is off), then a maintainer session makes the correction and closes this.',
        '','_Filed by `tools/unchecked.py --human`._'])
    if dry: print('WOULD FILE, labelled "%s":\n%s\n\n%s'%(HUMAN,title,body)); sys.exit(0)
    if not any(l['name']==HUMAN for l in gh('repos/%s/labels?per_page=100'%REPO)): gh('-X','POST','repos/%s/labels'%REPO,'-f','name='+HUMAN,'-f','color=d93f0b','-f','description=A session could not settle this from an aerial or a source: a person needs to look')
    same=[i for i in (gh('repos/%s/issues?state=open&labels=%s&per_page=100'%(REPO,HUMAN.replace(' ','%20'))) or []) if '(%s)'%pl['id'] in i['title']]
    if same: print('Already waiting: #%d %s'%(same[0]['number'],same[0]['title'])); sys.exit(0)
    r=gh('-X','POST','repos/%s/issues'%REPO,'--input','-',inp=json.dumps({'title':title,'body':body,'labels':[HUMAN]}))
    print('Filed #%d for a person to look at: %s'%(r['number'],r['html_url'])); sys.exit(0)
# ---- a check.py warning that was looked at and stands: record it, so it is not printed every day (tools/checked_ok.json)
#   python3 tools/unchecked.py --ok <place id> "<what you looked at and why the entry is right as it is>"
if a[:1]==['--ok']:
    import os
    if len(a)<3 or len(a[2].strip())<15: sys.exit('Give the place id and a sentence: what you looked at and why the entry is right as it is.')
    W=os.path.dirname(os.path.dirname(os.path.abspath(__file__))); f=os.path.join(W,'tools','checked_ok.json')
    d=json.load(open(f,encoding='utf-8')) if os.path.exists(f) else {}
    d[a[1]]=a[2].strip(); json.dump(d,open(f,'w',encoding='utf-8'),indent=1,ensure_ascii=False,sort_keys=True)
    print('Recorded. check.py will not repeat that warning for %s. The file goes out with your pull request (tools/publish.sh).'%a[1]); sys.exit(0)
if a[:1]==['--done']: relabel(a[1:2],'double-checked','0e8a16','Research reviewed in full: sources opened, every pin looked at'); sys.exit(0)
if a[:1]==['--sampled']: relabel(a[1:],'sample-checked','1d76db','Research that passed the automated checks, with one pin drawn at random looked at on the aerial'); sys.exit(0)
prs=[]; pg=1
while True:          # a page holds 100, and three sessions an hour fill one in a day and a half
    got=gh('repos/%s/issues?state=closed&labels=%s&per_page=100&sort=created&direction=asc&page=%d'%(REPO,LAB.replace(' ','%20'),pg)) or []
    prs+=[i for i in got if i.get('pull_request')]
    if len(got)<100: break
    pg+=1
if a[:1]==['--sample']:
    import os,re,random,glob
    W=os.path.dirname(os.path.dirname(os.path.abspath(__file__))); sj=os.path.join(W,'build','sites.json')
    if not os.path.exists(sj): sys.exit('Run this from the working folder after build_sites.py: build/sites.json is not there.')
    S=json.load(open(sj)); rnd=random.Random(a[1] if len(a)>1 else None); picks=[]; none=[]; hrs=[]; hnone=[]
    for i in prs:
        allf=[f['filename'].split('/')[-1] for f in gh('repos/%s/pulls/%d/files?per_page=100'%(REPO,i['number'])) if f['filename'].startswith('source/tools/')]
        fs=[f for f in allf if f.startswith('data_')]
        if not fs and any(f.startswith('hours_') for f in allf):      # a batch of looked-up hours has no pin: one of its rows is drawn, to be read against the page it came from
            import ast
            rows=[]
            for f in allf:
                if not f.startswith('hours_'): continue
                try:
                    t=ast.parse(open(os.path.join(W,'tools',f),encoding='utf-8').read())
                    for n in t.body:
                        if isinstance(n,ast.Assign) and getattr(n.targets[0],'id','')=='HOURS': rows+=[(k,v) for k,v in ast.literal_eval(n.value).items() if v and v[0] not in('','?')]
                except (OSError,ValueError,SyntaxError): pass
            if rows: k,v=rnd.choice(rows); hrs.append((i['number'],k,v[0],v[2] if len(v)>2 else ''))
            else: hnone.append(i['number'])
            continue
        keys=[]
        for f in fs:
            try: keys+=re.findall(r"BATCH\s*=\s*\{\s*'key'\s*:\s*'([^']+)'",open(os.path.join(W,'tools',f),encoding='utf-8').read())
            except OSError: pass
        L=[x for x in S if x.get('new') in keys]
        if L: picks.append((i['number'],rnd.choice(L)['id']))
        else: none.append(i['number'])
    print('%d batch(es) waiting; one place drawn from each of %d:'%(len(prs),len(picks)))
    for n,pid in picks: print('  #%d  %s'%(n,pid))
    if none: print('No places found for: '+' '.join('#%d'%n for n in none)+' (a brick-only pull request, or its list is not in this working folder: resync first)')
    print('\nLook at them (sheets of twelve in research/):\n  python3 tools/pincheck.py '+' '.join(pid for n,pid in picks))
    print('Then, for the batches whose pin is on its building, ruin or site:\n  python3 tools/unchecked.py --sampled '+' '.join(str(n) for n,pid in picks))
    print('A pin that is off: fix it in a pull request first (GUIDE.md section 14), and leave that batch for a full review.')
    if hrs:
        print('\n%d batch(es) of looked-up hours; one row drawn from each. Open the page and see that it gives these times for this building:'%len(hrs))
        for n,k,txt,url in hrs: print('  #%d  %s\n       recorded: %s\n       python3 tools/hours.py page %s'%(n,k,txt,url))
        print('For each one the page bears out:  python3 tools/unchecked.py --sampled <its number>. One it does not: correct the row with tools/hours.py set, and leave the batch.')
    if hnone: print('\nBatches of hours in which nothing was found for any place (nothing to read against a page), which can be marked as they are:\n  python3 tools/unchecked.py --sampled '+' '.join(str(n) for n in hnone))
    print('A pin you cannot tell either way (trees, a new roof, nothing to match the description): do not guess and do not mark the batch.\n  python3 tools/unchecked.py --human <place id> "<what you looked at and why it could not be told>"\nfiles it for a person to look at; leave that batch waiting.')
    sys.exit(0)
if not prs: print('Nothing is waiting for a second look.'); sys.exit(0)
print(len(prs),'pull request(s) merged without a second look, oldest first:')
for i in prs:
    fs=[f['filename'].split('/')[-1] for f in gh('repos/%s/pulls/%d/files?per_page=100'%(REPO,i['number'])) if f['filename'].startswith('source/tools/data_') or f['filename'].startswith('source/tools/bricks_') or f['filename'].startswith('source/tools/hours_')]
    print('  #%d  %s  merged %s  %s'%(i['number'],i['title'][:70],(i.get('closed_at') or '')[:10],' '.join(fs)))
print('Review one as GUIDE.md section 14 says (tools/review.py <number>), fix what is wrong in a new pull request, then:  python3 tools/unchecked.py --done <number>')
