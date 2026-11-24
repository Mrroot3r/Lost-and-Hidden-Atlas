#!/usr/bin/env python3
"""Warnings a session has looked at and accepted stop being repeated (tools/checked_ok.json).
   python3 tools/check_ok_test.py [<clone>]      run it after changing how check.py makes or silences warnings
What it holds check.py to: a warning about a place's kind or its pin just outside a state outline is printed until that
place's id is in the file with a reason; then it is not printed, the summary says how many were accepted, and an id in
the file that no longer raises any warning is reported so the file can be tidied. Errors are never silenced."""
import sys,os,json,subprocess,tempfile,re
W=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REPO=sys.argv[1] if len(sys.argv)>1 else open(os.path.join(W,'.repo')).read().strip()
fails=[]
def ok(name,cond,extra=''):
    print(('ok   ' if cond else 'FAIL ')+name+(('  ['+str(extra)[:160]+']') if extra!='' else ''))
    if not cond: fails.append(name)
def run(okfile):
    env=dict(os.environ,CHECKED_OK=okfile)
    return subprocess.run([sys.executable,os.path.join(W,'tools','check.py'),REPO,'--sources'],capture_output=True,text=True,env=env).stdout
d=tempfile.mkdtemp(); empty=os.path.join(d,'none.json'); open(empty,'w').write('{}')
base=run(empty); warns=re.findall(r'^warning: \S+?:([a-z0-9-]+): (.*)$',base,re.M)
kind=[i for i,t in warns if 'reads as a place of worship' in t]; edge=[i for i,t in warns if 'just outside' in t]
ok('with nothing accepted, kind warnings and state-line warnings are printed',len(kind)>0 and len(edge)>0,f'{len(kind)} kind, {len(edge)} state line')
some=os.path.join(d,'some.json'); json.dump({kind[0]:'looked at: the name is a surname',edge[0]:'on the river that is the state line','no-such-place-id':'gone'},open(some,'w'))
out=run(some); w2=[i for i,t in re.findall(r'^warning: \S+?:([a-z0-9-]+): (.*)$',out,re.M)]
ok('an accepted place is not warned about again',kind[0] not in w2 and edge[0] not in w2,f'{len(warns)} warnings before, {len(w2)} after')
ok('the others still are',all(i in w2 for i in kind[1:]+edge[1:]))
ok('the summary says how many were accepted',bool(re.search(r'2 (more )?(warnings? )?(already )?(looked at|accepted)',out)),[l for l in out.split('\n') if 'accepted' in l or 'looked at' in l][:2])
ok('an id in the file that raises no warning is pointed out',bool(re.search(r'no-such-place-id',out)))
n=lambda s:int(re.search(r'(\d+) errors',s).group(1))
ok('errors are counted the same either way',n(base)==n(out),f'{n(base)} and {n(out)}')
# A river town on the far bank of a coarse outline (the outlines come from the Census Bureau's 1:20,000,000 file: Ohio is 98 points).
# Downtown East Liverpool, Ohio is 1.1 km inside "West Virginia" by them, and until November 24, 2026 that was an error that kept a
# researched place off the map. A pin up to 3 km over a coarse line is warned about; one deep in the other state is still an error.
def where(la,lo,reg): return subprocess.run([sys.executable,os.path.join(W,'tools','check.py'),REPO,'--where',str(la),str(lo),reg],capture_output=True,text=True).stdout.strip()
el=where(40.6187,-80.5773,'oh'); ch=where(38.3498,-81.6326,'oh'); col=where(39.9612,-82.9988,'oh')
ok('state line: downtown East Liverpool, Ohio is warned about, not refused',el.startswith('warning')and 'oh' in el,el)
ok('state line: a pin in Charleston, West Virginia filed under Ohio is still an error',ch.startswith('error'),ch)
ok('state line: a pin in Columbus is simply fine',col.startswith('ok'),col)
print(f'{len(fails)} FAILED' if fails else 'check_ok test: 9 checks passed'); sys.exit(1 if fails else 0)
