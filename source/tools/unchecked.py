#!/usr/bin/env python3
"""Research that went onto the map without a second look.

A research-only pull request from the owner's own sessions merges by itself once the checks pass (.github/workflows/
check.yml, GUIDE.md section 3), and is labelled "not double-checked". This lists those, oldest first, so a stronger
model can be sent to review them later (GUIDE.md section 14).

   python3 tools/unchecked.py              the pull requests still waiting for a second look, with their data files
   python3 tools/unchecked.py --done 81    after reviewing #81: take the label off and put "double-checked" on

Needs the gh command signed in to the repository."""
import sys,json,subprocess
REPO='Mrroot3r/Lost-and-Hidden-Atlas'; LAB='not double-checked'
def gh(*a,inp=None):
    r=subprocess.run(['gh','api']+list(a),capture_output=True,text=True,input=inp)
    if r.returncode: sys.exit('gh could not do that: '+(r.stderr.strip() or r.stdout.strip())[:200])
    return json.loads(r.stdout) if r.stdout.strip() else None
a=sys.argv[1:]
if a[:1]==['--done']:
    n=a[1].lstrip('#')
    gh('-X','POST','repos/%s/labels'%REPO,'-f','name=double-checked','-f','color=0e8a16') if not any(l['name']=='double-checked' for l in gh('repos/%s/labels?per_page=100'%REPO)) else None
    gh('-X','POST','repos/%s/issues/%s/labels'%(REPO,n),'--input','-',inp=json.dumps({'labels':['double-checked']}))
    subprocess.run(['gh','api','-X','DELETE','repos/%s/issues/%s/labels/%s'%(REPO,n,LAB.replace(' ','%20'))],capture_output=True)
    print('#%s is marked double-checked.'%n); sys.exit(0)
prs=[i for i in gh('repos/%s/issues?state=closed&labels=%s&per_page=100&sort=created&direction=asc'%(REPO,LAB.replace(' ','%20'))) if i.get('pull_request')]
if not prs: print('Nothing is waiting for a second look.'); sys.exit(0)
print(len(prs),'pull request(s) merged without a second look, oldest first:')
for i in prs:
    fs=[f['filename'].split('/')[-1] for f in gh('repos/%s/pulls/%d/files?per_page=100'%(REPO,i['number'])) if f['filename'].startswith('source/tools/data_') or f['filename'].startswith('source/tools/bricks_')]
    print('  #%d  %s  merged %s  %s'%(i['number'],i['title'][:70],(i.get('closed_at') or '')[:10],' '.join(fs)))
print('Review one as GUIDE.md section 14 says (tools/review.py <number>), fix what is wrong in a new pull request, then:  python3 tools/unchecked.py --done <number>')
