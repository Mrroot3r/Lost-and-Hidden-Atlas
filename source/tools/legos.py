#!/usr/bin/env python3
"""Record which places have "Legos" (mutules with their pegs, guttae) and the grooved blocks that go with them (triglyphs).
Run from the workspace after tools/build_sites.py. tools/legorule.py says what they are and holds the rules.
   python3 tools/legos.py words                 places whose own text names mutules, guttae or triglyphs and that have no
                                                answer yet, with the sentence; and the Register forms kept in research/forms
                                                that name them. A sentence that names them is how it is known.
   python3 tools/legos.py set <id> pegs|holes|yes|no "<how it is known>" [--trig yes|no]
                                                record it in tools/legos_<four letters>.py (this workspace's own file, so
                                                sessions side by side do not collide); it goes out with tools/publish.sh
   python3 tools/legos.py list                  everything recorded in the legos files
An answer is never taken from the style of a building. A reader's or the owner's report from the ground is how most are known:
tools/visits.py and tools/inbox.py print those with the command to run here."""
import sys,os,re,json,glob,ast,random
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__))); sys.dont_write_bytecode=True
import legorule as L
HEAD='# "Legos" (mutules and their pegs) and triglyphs found out after a place was written (tools/legos.py writes this file;\n# tools/legorule.py holds the rules). id: (pegs|holes|yes|no, triglyphs yes|no or \'\', how it is known)\n'
def read(f):
    s=open(f,encoding='utf-8').read(); return ast.literal_eval(s[s.index('LEGO=')+5:])
def allrows():
    d={}
    for f in sorted(glob.glob('tools/legos_*.py')): d.update(read(f))
    return d
def myfile():
    kf='tools/.legos_key'
    if not os.path.exists(kf): open(kf,'w').write(''.join(random.SystemRandom().choice('abcdefghjkmnpqrstvwxyz') for _ in range(4)))
    return 'tools/legos_%s.py'%open(kf).read().strip()
def write(f,d):
    open(f,'w',encoding='utf-8').write(HEAD+'LEGO={\n'+''.join(' %r:%r,\n'%(k,tuple(d[k])) for k in sorted(d))+'}\n')
def sites(): return json.load(open('build/sites.json',encoding='utf-8'))
a=sys.argv[1:]
if a[:1]==['set']:
    trig=''
    if '--trig' in a: i=a.index('--trig'); trig=a[i+1] if i+1<len(a) else ''; a=a[:i]+a[i+2:]
    if len(a)!=4: sys.exit('python3 tools/legos.py set <id> pegs|holes|yes|no "<how it is known>" [--trig yes|no]')
    pid,ans,how=a[1],a[2],a[3].strip(); row=(ans,trig,how)
    if pid not in {s['id'] for s in sites()}: sys.exit('%s is not a place id (run tools/build_sites.py first if it is new)'%pid)
    p=L.row_problem(row)
    if p: sys.exit('Not recorded: '+p)
    f=myfile(); d=read(f) if os.path.exists(f) else {}; d[pid]=row; write(f,d)
    print('Recorded in %s: %s  %s%s. It goes out with your pull request (tools/publish.sh).'%(f,pid,ans,', triglyphs '+trig if trig else '')); sys.exit(0)
if a[:1]==['list']:
    d=allrows()
    for k in sorted(d): print('%-52s %-6s trig=%-3s  %s'%(k,d[k][0],d[k][1] or '-',d[k][2][:90]))
    print('%d place(s) recorded in the legos files.'%len(d)); sys.exit(0)
if a[:1]==['words']:
    d=allrows(); n=0
    for s in sites():
        if s['id'] in d or s.get('lg') or s.get('tg'): continue
        t=' '.join(str(s.get(k) or '') for k in('story','look')); w=L.words(t)
        if not w: continue
        n+=1; lg,tg=L.from_text(t); first=sorted(w)[0]
        print('%s  (%s, %s)\n    names: %s\n    "%s"\n    python3 tools/legos.py set %s %s "The entry\'s own source describes it: %s"%s'%(s['id'],s['name'],s.get('town',''),', '.join(sorted(w)),L.sentence(t,first)[:300],s['id'],lg or '?',L.sentence(t,first)[:120].replace('"',"'"),' --trig yes' if tg else ''))
    print('%d place(s) whose own text names mutules, guttae or triglyphs and that have no answer yet.'%n)
    for f in sorted(glob.glob('research/forms/*.txt')):
        t=open(f,encoding='utf-8',errors='ignore').read(); w=L.words(t)
        if w: print('Register form %s names %s: "%s"'%(os.path.basename(f)[:-4],', '.join(sorted(w)),re.sub(r'\s+',' ',L.sentence(t,sorted(w)[0]))[:240]))
    sys.exit(0)
sys.exit(__doc__)
