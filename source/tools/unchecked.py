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
    S=json.load(open(sj)); rnd=random.Random(a[1] if len(a)>1 else None); picks=[]; none=[]
    for i in prs:
        fs=[f['filename'].split('/')[-1] for f in gh('repos/%s/pulls/%d/files?per_page=100'%(REPO,i['number'])) if f['filename'].startswith('source/tools/data_')]
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
    sys.exit(0)
if not prs: print('Nothing is waiting for a second look.'); sys.exit(0)
print(len(prs),'pull request(s) merged without a second look, oldest first:')
for i in prs:
    fs=[f['filename'].split('/')[-1] for f in gh('repos/%s/pulls/%d/files?per_page=100'%(REPO,i['number'])) if f['filename'].startswith('source/tools/data_') or f['filename'].startswith('source/tools/bricks_') or f['filename'].startswith('source/tools/hours_')]
    print('  #%d  %s  merged %s  %s'%(i['number'],i['title'][:70],(i.get('closed_at') or '')[:10],' '.join(fs)))
print('Review one as GUIDE.md section 14 says (tools/review.py <number>), fix what is wrong in a new pull request, then:  python3 tools/unchecked.py --done <number>')
