#!/usr/bin/env python3
"""Test of tools/tidy.py on a made-up clone in a temporary folder (nothing real is touched).   python3 tools/tidy_test.py
Run it after changing tidy.py, the note template in note.py, or how start.py and check.py read a note."""
import os,sys,subprocess,tempfile,re
HERE=os.path.dirname(os.path.abspath(__file__)); T=tempfile.mkdtemp(prefix='tidytest'); os.makedirs(os.path.join(T,'notes'))
fails=[]
def ok(name,cond,extra=''):
    print(('ok   ' if cond else 'FAIL ')+name+(('  ['+str(extra)+']') if extra!='' else ''))
    if not cond: fails.append(name)
def run(*a,rc=0):
    r=subprocess.run([sys.executable,os.path.join(HERE,'tidy.py'),T]+list(a),capture_output=True,text=True,env=dict(os.environ,TIDY_DATE='2026-12-01'),cwd=T)
    return r.returncode,r.stdout+r.stderr
HEAD='| Place | Where | What is known | What is missing |\n|---|---|---|---|\n'
open(os.path.join(T,'LEADS.md'),'w').write('# Leads not yet added\n\n'+HEAD+'| Old kiln | Sometown, NY | A source | A coordinate |\n')
open(os.path.join(T,'GUIDE.md'),'w').write('# Guide\n\n## 8. States\n\n| State | Places so far | Leaf-off and LiDAR |\n|---|---|---|\n| Ohio | One | Satellite |\n\n## 16. What research sessions have learned\n\n### Every state\n- A tip kept earlier.\n\n### Ohio\n- An Ohio tip.\n')
NOTE='''# %s: Somewhere
state: %s
region: xx
date: 2026-11-20
places: 12
file: data_%s.py

## What this batch is
Twelve places. Nothing on the ground was checked.

## Leads
Places you read about and could not finish.

%s%s
## Tips
%s
'''
open(os.path.join(T,'notes','aa_wxyz.md'),'w').write(NOTE%('aa_wxyz','Ohio','aa_wxyz',HEAD,'| Lost mill | Milltown, OH (40.12345, -82.12345) | Wikipedia | An owner |\n| Old kiln | Sometown, NY | The same thing again | More |\n','- `page.py` reads the county site.\n- A second tip that runs\n  over two lines.\n'))
open(os.path.join(T,'notes','bb_qrst.md'),'w').write(NOTE%('bb_qrst','Iowa','bb_qrst',HEAD,'| Ghost depot | Railton, IA | A marker | Anything |\n','- None\n'))
open(os.path.join(T,'notes','README.md'),'w').write('# Session notes\n\n| not | a | lead | row |\n')

rc,out=run(); ok('the report lists both notes as waiting',rc==0 and '2 waiting' in out and 'aa_wxyz' in out and 'bb_qrst' in out,out.split('\n')[0])
ok('it counts three lead rows and two tips, and joins a tip that runs over two lines',"3 row(s) in the notes" in out and 'Tips: 2,' in out and 'over two lines.' in out)
ok('"None" is not a tip, and the README is not a note',out.count('[bb_qrst]')==0 and 'README' not in out)
ok('it names the headings section 16 has, and says a state has no row in the table','Every state, Ohio' in out and 'Iowa' in out and 'no row of its own' in out and 'Ohio: ' in out)
rc,out2=run('--done'); ok('--done refuses while lead rows are still in the notes',rc!=0 and '--leads' in out2,out2.strip()[:70])
rc,out=run('--leads'); L=open(os.path.join(T,'LEADS.md')).read()
ok('--leads appends the new rows to LEADS.md once',rc==0 and L.count('| Lost mill |')==1 and L.count('| Ghost depot |')==1 and L.count('| Place |')==1,out.split('\n')[0])
ok('a row LEADS.md already has by name is not copied, and is reported',L.count('| Old kiln |')==1 and 'Old kiln' in out and 'already has' in out)
n=open(os.path.join(T,'notes','aa_wxyz.md')).read()
ok('the note keeps its heading and table header, without rows',('## Leads' in n) and (HEAD.split('\n')[0] in n) and '| Lost mill |' not in n and 'Moved to `LEADS.md` on 2026-12-01' in n)
ok('its tips are still there until they are written into the guide','`page.py` reads the county site.' in n)
rc,out=run('--leads'); ok('--leads a second time moves nothing',rc==0 and out.startswith('0 lead row(s)') and open(os.path.join(T,'LEADS.md')).read()==L,out.split('\n')[0])
rc,out=run('--done','aa_wxyz'); n=open(os.path.join(T,'notes','aa_wxyz.md')).read(); b=open(os.path.join(T,'notes','bb_qrst.md')).read()
ok('--done with a key tidies that note only',rc==0 and 'tidied: 2026-12-01' in n and 'tidied:' not in b)
ok('the tips are gone from it and it says where they went','`page.py` reads' not in n and 'Folded into `GUIDE.md` and the tools on 2026-12-01' in n and '## Tips' in n)
ok('what the batch was stays in the note','Twelve places. Nothing on the ground was checked.' in n)
ok('the note still passes what check.py asks of it',all(h in n for h in ('## What this batch is','## Leads','## Tips')) and 'Delete this bracketed text' not in n and '| Example mill |' not in n)
tips=[l for l in (re.search(r'^## Tips[^\n]*\n(.*?)(?=^## |\Z)',n,re.M|re.S).group(1)).split('\n') if l.strip().startswith('-')]
rows=[l for l in (re.search(r'^## Leads[^\n]*\n(.*?)(?=^## |\Z)',n,re.M|re.S).group(1)).split('\n') if l.startswith('|') and not l.startswith('| Place') and not l.startswith('|---')]
ok('start.py will find no tips and no leads in it',tips==[] and rows==[])
rc,out=run(); ok('the report now lists only the other note',rc==0 and '1 waiting' in out and 'bb_qrst' in out and '  aa_wxyz' not in out)
rc,out=run('--done'); rc2,out2=run(); ok('--done with no key tidies what is left, and then there is nothing to do',rc==0 and 'Nothing to do' in out2,out2.strip().split('\n')[-1])
rc,out=run('--done','nosuch'); ok('an unknown key is refused',rc!=0 and 'No such note' in out)
import shutil; shutil.rmtree(T,ignore_errors=True)
print(('\n%d FAILED'%len(fails)) if fails else '\ntidy test: 18 checks passed'); sys.exit(1 if fails else 0)
