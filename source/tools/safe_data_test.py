#!/usr/bin/env python3
"""safe_data.py must pass every real place list and refuse everything else.   python3 tools/safe_data_test.py
Run it after changing tools/safe_data.py. Each case below is a whole file; nothing in it is ever run."""
import os,sys,tempfile,shutil
HERE=os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0,HERE)
import safe_data
fails=[]
def ok(name,cond,extra=''):
    print(('ok   ' if cond else 'FAIL ')+name+('  ['+extra+']' if extra else ''))
    if not cond: fails.append(name)
HEAD="from data_b import N\nBATCH={'key':'t','label':'T','added':'2026-11-19 00:00'}\n"
GOOD={
 'the usual shape':HEAD+"def L(t,u): return [t,u]\nSRC='x'\nPLACES=[N('a','A','T','alb','civic','standing',42.0,-73.0,'exact','public','drive','','1800','s',links=[L('a','https://a.example/')],conf='mixed',th=[42.0,-73.0])]\nPIN_NOTES={'a':'on the roof'}\n",
 'helpers, a lambda, a comprehension, % and f-strings':HEAD+"HM=lambda n,t:['HMdb: '+t,'https://www.hmdb.org/m.asp?m=%d'%n]\ndef W(t): return ['Wikipedia: '+t,'https://en.wikipedia.org/wiki/'+t.replace(' ','_')]\nX={k:v for k,v in {'a':1}.items()}\nY=[f'{a}-{b}' for a,b in zip('ab','cd') if a!=b]\nZ=sorted(set(Y),key=len)\nPLACES=[]\nPIN_NOTES={}\nPIN_NOTES.update({'a':'b'})\nPLACES+=[]\nassert len(PLACES)==0,'empty'\n",
 'a helper with an if':HEAD+"def P(a,b=''):\n    'doc'\n    x=a+b\n    if b: return x\n    return a\nPLACES=[]\nPIN_NOTES={}\n",
}
BAD={
 'import os':"import os\n",
 'from os import system':"from os import system\n",
 'a relative import':"from . import x\n",
 'import star':"from data_b import *\n",
 'a name data_b does not define':"from data_b import os\n",
 '__import__':"x=__import__('os')\n",
 'eval':"x=eval('1')\n",
 'exec':"exec('x=1')\n",
 'open':"x=open('/etc/passwd')\n",
 'getattr':HEAD+"x=getattr(N,'__globals__')\n",
 'print':"print('hello')\n",
 'an attribute read':HEAD+"x=N.__globals__\n",
 'a dunder chain':"x=().__class__.__bases__[0].__subclasses__()\n",
 'a method that is not on the list':"x='{0.__class__}'.format(1)\n",
 'pop':"x=[1].pop()\n",
 'a class':"class X: pass\n",
 'a for loop':"for x in [1]: y=x\n",
 'a while loop':"while True: x=1\n",
 'with':"with open('x') as f: y=1\n",
 'try':"try:\n    x=1\nexcept Exception:\n    x=2\n",
 'del':"x=1\ndel x\n",
 'raise':"raise SystemExit\n",
 'global':"def f():\n    global x\n    return 1\n",
 'a decorator':HEAD+"@N\ndef f(): return 1\n",
 'a default that calls':"def f(a=__import__('os')): return a\n",
 'an annotation on an argument':"def f(a: __import__('os').system('id')): return a\n",
 'an annotation on the return':"def f() -> __import__('os'): return 1\n",
 'an annotated assignment':"x: int = 1\n",
 'a def inside a def':"def f():\n    def g(): return 1\n    return g\n",
 'a generator':"def f():\n    yield 1\n",
 'a lambda that imports':"f=lambda: __import__('os')\n",
 'a lambda default':"f=lambda a=open: a\n",
 'eval as a sort key':"x=sorted(['1'],key=eval)\n",
 'eval out of a list':"x=[eval][0]('1')\n",
 'a call of a call':HEAD+"x=N()()\n",
 'globals':"x=globals()['y']\n",
 'vars':"x=vars()\n",
 'type':"X=type('X',(),{})\n",
 'breakpoint':"breakpoint()\n",
 'an f-string that imports':"x=f\"{__import__('os')}\"\n",
 'a walrus':"x=[(y:=1)]\n",
 'assigning to an attribute':HEAD+"N.x=1\n",
 'a bare call':HEAD+"N()\n",
 'eval rebound in a comprehension, then used':"x=[1 for eval in [1]]\ny=eval('1')\n",
 'open rebound as an argument, then used':"def f(open): return open\ny=open('/etc/passwd')\n",
 'a builtin rebound by assignment':"getattr=1\n",
 '__builtins__':"x=__builtins__\n",
 '__file__':"x=__file__\n",
 'assigning __builtins__':"__builtins__={}\n",
 'a match statement':"match 1:\n    case 1: x=1\n",
 'async':"async def f(): return 1\n",
 'not Python':"this is not python\n",
}
tmp=tempfile.mkdtemp()
try:
    shutil.copy(os.path.join(HERE,'data_b.py'),tmp)
    for k,src in GOOD.items():
        f=os.path.join(tmp,'data_case.py'); open(f,'w',encoding='utf-8').write(src); b=safe_data.check_file(f)
        ok('allowed: '+k,not b,'; '.join(b)[:160])
    for k,src in BAD.items():
        f=os.path.join(tmp,'data_case.py'); open(f,'w',encoding='utf-8').write(src); b=safe_data.check_file(f)
        ok('refused: '+k,bool(b),(b[0].split(': ',1)[1][:70] if b else 'NOT REFUSED'))
    os.remove(os.path.join(tmp,'data_case.py'))
    # a name that reaches a list only through another list's import of something that is not a list
    open(os.path.join(tmp,'data_evil.py'),'w').write("import os\nX=1\n"); open(os.path.join(tmp,'data_case.py'),'w').write("from data_evil import os\n")
    files,b=safe_data.check_folder(tmp); ok('refused: importing a module out of another list, in both files',sum('data_evil' in x.split(' ')[0] for x in b)>=1 and sum(x.startswith('data_case') for x in b)>=1,str(len(b))+' problems')
    open(os.path.join(tmp,'bricks_case.py'),'w').write("import subprocess\nBRICK={}\n"); files,b=safe_data.check_folder(tmp); ok('brick files are read too',any(x.startswith('bricks_case') for x in b))
    try: safe_data.must(tmp); ok('must() stops the program',False)
    except SystemExit as e: ok('must() stops the program, saying why',str(e).startswith('STOP'))
finally: shutil.rmtree(tmp)
files,b=safe_data.check_folder(HERE); ok('every real place list passes (%d files)'%len(files),len(files)>100 and not b,'; '.join(b)[:300])
print('\n%d FAILED'%len(fails) if fails else '\nsafe_data test: %d checks passed'%(len(GOOD)+len(BAD)+4)); sys.exit(1 if fails else 0)
