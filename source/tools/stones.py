#!/usr/bin/env python3
"""Record the words cut on a building (a cornerstone, a datestone, over the door). Run from the workspace after
tools/build_sites.py. tools/stonerule.py says what counts and holds the rules.
   python3 tools/stones.py set <id> "<the words as cut>" "<how they are known>"
                                   record them. A place that has a row keeps it in the same file; a new one goes in this
                                   workspace's own tools/stones_<four letters>.py, which goes out with tools/publish.sh
   python3 tools/stones.py list    everything recorded, with the kind and year read from the words
   python3 tools/stones.py find    places whose write-up mentions a cornerstone, a datestone or an inscription and that
                                   have no words yet: where to look first
The words come from somebody who read them on the ground, a picture that shows them, or a source that quotes them exactly.
tools/visits.py and tools/inbox.py print the command for a report from the ground."""
import sys,os,re,json,glob,ast,random
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__))); sys.dont_write_bytecode=True
import stonerule as R
HEAD='# The words cut on a building, found out after the place was written (tools/stones.py writes this file; tools/stonerule.py\n# holds the rules). id: (the words as cut, how they are known)\n'
def read(f):
    s=open(f,encoding='utf-8').read(); return ast.literal_eval(s[s.index('STONE=')+6:])
def files(): return sorted(glob.glob('tools/stones_*.py'))
def allrows():
    d={}
    for f in files(): d.update(read(f))
    return d
def myfile():
    kf='tools/.stones_key'
    if not os.path.exists(kf): open(kf,'w').write(''.join(random.SystemRandom().choice('abcdefghjkmnpqrstvwxyz') for _ in range(4)))
    return 'tools/stones_%s.py'%open(kf).read().strip()
def write(f,d): open(f,'w',encoding='utf-8').write(HEAD+'STONE={\n'+''.join(' %r:%r,\n'%(k,tuple(d[k])) for k in sorted(d))+'}\n')
def put(pid,row):
    f=next((g for g in files() if pid in read(g)),None) or myfile()
    d=read(f) if os.path.exists(f) else {}; d[pid]=row; write(f,d); return f
def sites(): return json.load(open('build/sites.json',encoding='utf-8'))
a=sys.argv[1:]
if a[:1]==['set']:
    if len(a)!=4: sys.exit('python3 tools/stones.py set <id> "<the words as cut>" "<how they are known>"')
    pid,row=a[1],(a[2].strip(),a[3].strip())
    if pid not in {s['id'] for s in sites()}: sys.exit('%s is not a place id (run tools/build_sites.py first if it is new)'%pid)
    p=R.row_problem(row)
    if p: sys.exit('Not recorded: '+p)
    f=put(pid,row); print('Recorded in %s: %s  "%s"  (%s%s). It goes out with your pull request (tools/publish.sh).'%(f,pid,row[0],R.LABEL[R.kind(row[0])],', '+str(R.year(row[0])) if R.year(row[0]) else '')); sys.exit(0)
if a[:1]==['list']:
    d=allrows()
    for k in sorted(d): print('%-46s %-13s %-5s "%s"   [%s]'%(k[:46],R.LABEL[R.kind(d[k][0])],R.year(d[k][0]) or '',d[k][0][:60],d[k][1][:60]))
    print('%d place(s).'%len(d)); sys.exit(0)
if a[:1]==['find']:
    d=allrows(); n=0
    for s in sites():
        if s['id'] in d or s.get('sx'): continue
        t=' '.join(str(s.get(k) or '') for k in('story','look')); m=re.search(r'[^.]*\b(cornerstone|corner stone|datestone|date stone|inscri\w+|carved over|lintel (?:reads|says)|tablet (?:reads|says))\b[^.]*\.',t,re.I)
        if m: n+=1; print('%s  (%s, %s)\n    "%s"'%(s['id'],s['name'][:50],s.get('town',''),m.group(0).strip()[:260]))
    print('%d place(s) whose write-up mentions a cornerstone, a datestone or an inscription and that have no words yet.'%n); sys.exit(0)
sys.exit(__doc__)
