#!/usr/bin/env python3
"""Who designed or built a place (tools/archrule.py, tools/archs.py, and their use in check.py and build_sites.py).
   python3 tools/arch_test.py      run it after changing archrule.py, archs.py or how a name is recorded or built
What it holds them to: a name is a person or a firm as a source gives it, with how it is known; one person or firm is one
name however it was spelled (the list of spellings in archrule.SAME, and '&' against 'and'); a builder is kept apart
from an architect; nothing is a guess."""
import sys,os,subprocess,tempfile,shutil,re,json
W=os.path.dirname(os.path.dirname(os.path.abspath(__file__))); sys.path.insert(0,os.path.join(W,'tools')); sys.dont_write_bytecode=True
import archrule as A
fails=[]; n=[0]
def ok(name,cond,extra=''):
    n[0]+=1; print(('ok   ' if cond else 'FAIL ')+name+(('  ['+str(extra)[:200]+']') if extra!='' else ''))
    if not cond: fails.append(name)
HOW="Wikidata's entry for National Register listing 78001234"
ok('names are split on semicolons, in order, without repeats',A.names('Wight and Wight; Louis Curtiss; Wight and Wight')==['Wight and Wight','Louis Curtiss'] and A.names(['Philip Hooker',' Louis Curtiss '])==['Philip Hooker','Louis Curtiss'] and A.names('')==[])
ok('"&" and "and", stops and spacing do not make two firms',A.key('McKim, Mead & White')==A.key('McKim, Mead and White')==A.key('McKim Mead  and White.') and A.key('H.H. Richardson')==A.key('H. H. Richardson'))
ok('a spelling in the list is the same person',A.canon('Frank Packard')==A.canon('Frank L. Packard')=='Frank L. Packard',A.canon('Frank Packard'))
ok('a name not in the list stays as written',A.canon('Louis Curtiss')=='Louis Curtiss')
ok('a place with a name and how it is known is fine',A.place_problem(dict(arch='Louis Curtiss',archw=HOW)) is None and A.place_problem({}) is None)
ok('a name with no word of how it is known is refused',bool(A.place_problem(dict(arch='Louis Curtiss'))) and bool(A.place_problem(dict(builder='W. H. Sternberg',archw='yes'))))
ok('"unknown", a question mark or a sentence is not a name',all(A.place_problem(dict(arch=x,archw=HOW)) for x in('Unknown','?','unknown architect','It was designed by a local man whose name the form does not give at all, sadly')))
ok('a guess is not how it is known',bool(A.place_problem(dict(arch='Louis Curtiss',archw='Probably his, from the look of it'))))
ok('a row in an archs file is (architects, builder, how)',A.row_problem(('Wight and Wight','',HOW)) is None and A.row_problem(('','W. H. Sternberg',HOW)) is None)
ok('a row says something and says how',bool(A.row_problem(('','',HOW))) and bool(A.row_problem(('Louis Curtiss','',''))) and bool(A.row_problem(('Louis Curtiss',HOW))))
ok('the list of spellings does not chain: what a spelling leads to is not itself led elsewhere',all(A.key(v) not in A._SAME or A._SAME[A.key(v)]==v for v in A.SAME.values()),[v for v in A.SAME.values() if A.key(v) in A._SAME and A._SAME[A.key(v)]!=v][:3])
u=A.unify([['Holabird & Roche'],['Holabird and Roche','Louis Curtiss'],['Holabird and Roche'],['Wight & Wight']])
ok('across the map one firm has one spelling: the commoner, or the one in the list',u(['Holabird & Roche','Louis Curtiss'])==['Holabird and Roche','Louis Curtiss'] and u(['Wight & Wight'])==['Wight and Wight'],u(['Holabird & Roche','Louis Curtiss']))
# ---- the tool, in a scratch copy
d=tempfile.mkdtemp(); T=os.path.join(d,'tools'); os.makedirs(T); os.makedirs(os.path.join(d,'build'))
for f in('archs.py','archrule.py'): shutil.copy(os.path.join(W,'tools',f),T)
json.dump([dict(id='a-bank',name='A Bank',town='X'),dict(id='b-house',name='B House',town='X'),dict(id='c-hall',name='C Hall',town='X',ar=['Louis Curtiss'])],open(os.path.join(d,'build','sites.json'),'w'))
def run(*a): return subprocess.run([sys.executable,os.path.join(T,'archs.py')]+list(a),capture_output=True,text=True,cwd=d)
r=run('set','a-bank','Frank Packard; Wight & Wight',HOW,'--builder','W. H. Sternberg')
fs=[f for f in os.listdir(T) if re.fullmatch(r'archs_[a-z]{4}\.py',f)]
ok('set writes this workspace\'s own archs_<four letters>.py',r.returncode==0 and len(fs)==1,(r.stdout+r.stderr)[-200:])
if fs:
    ns={}; exec(open(os.path.join(T,fs[0])).read(),ns)
    ok('the row holds the names as one spelling each, the builder and how it is known',ns.get('ARCH',{}).get('a-bank')==('Frank L. Packard; Wight and Wight','W. H. Sternberg',HOW),ns.get('ARCH'))
    r=run('set','a-bank','Louis Curtiss',HOW)
    ns={}; exec(open(os.path.join(T,fs[0])).read(),ns)
    ok('a second answer for the same place replaces the row, in the same file',len([f for f in os.listdir(T) if f.startswith('archs_')])==1 and ns['ARCH']['a-bank'][0]=='Louis Curtiss',ns.get('ARCH'))
r=run('set','no-such-place','Louis Curtiss',HOW); ok('set refuses an id that is not a place',r.returncode!=0)
r=run('set','b-house','Unknown',HOW); ok('set refuses "Unknown"',r.returncode!=0,(r.stdout+r.stderr)[-120:])
json.dump({'b-house':['Philip Hooker','',HOW],'c-hall':['Somebody Else','',HOW],'zz-nowhere':['Philip Hooker','',HOW],'a-bank':['Unknown','',HOW]},open(os.path.join(d,'rows.json'),'w'))
r=run('rows',os.path.join(d,'rows.json')); ns={}; exec(open(os.path.join(T,fs[0])).read(),ns)
ok('rows takes many at once: good ones in, a place that names somebody already left alone, bad ones refused and said',r.returncode==0 and ns['ARCH'].get('b-house',('',))[0]=='Philip Hooker' and 'c-hall' not in ns['ARCH'] and ns['ARCH']['a-bank'][0]=='Louis Curtiss' and 'zz-nowhere' in r.stdout,(r.stdout+r.stderr)[-300:])
r=run('list'); ok('list shows what is recorded',r.returncode==0 and 'a-bank' in r.stdout and 'Louis Curtiss' in r.stdout,r.stdout[-200:])
shutil.rmtree(d)
print(f'{len(fails)} FAILED' if fails else f'arch test: {n[0]} checks passed'); sys.exit(1 if fails else 0)
