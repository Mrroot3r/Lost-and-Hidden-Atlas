#!/usr/bin/env python3
"""The first picture on the repository's front page is retaken when another hundred places are on the map (tools/first_picture.py).
   python3 tools/first_picture_test.py"""
import sys,os,json,subprocess,tempfile
T=os.path.dirname(os.path.abspath(__file__)); fails=[]
def ok(name,cond,extra=''):
    print(('ok   ' if cond else 'FAIL ')+name+(('  ['+str(extra)[:160]+']') if extra!='' else ''))
    if not cond: fails.append(name)
d=tempfile.mkdtemp(); os.makedirs(os.path.join(d,'docs','features'))
def page(n): open(os.path.join(d,'index.html'),'w').write('<script type="application/json" id="d-sites">'+json.dumps({'sites':[{'id':'p%d'%i} for i in range(n)]})+'</script>')
def run(*a): return subprocess.run([sys.executable,os.path.join(T,'first_picture.py'),d]+list(a),capture_output=True,text=True)
open(os.path.join(d,'README.md'),'w').write('<b>The whole map</b><br>More than 5,000 old places across the United States and Canada. Other text with 5,000 in it.')
page(8441); r=run('need')
ok('with no record of the last picture, one is needed',r.returncode==0,r.stdout+r.stderr)
r=run('done'); rd=open(os.path.join(d,'README.md')).read()
ok('done: the count is kept beside the picture',open(os.path.join(d,'docs','features','01-map.count')).read().strip()=='8441')
ok('done: the caption says "More than 8,400 old places", and nothing else in the page is touched','More than 8,400 old places across' in rd and 'Other text with 5,000 in it.' in rd,rd[:120])
page(8480); ok('39 more places: no new picture',run('need').returncode!=0)
page(8502); ok('past the next hundred: a new picture',run('need').returncode==0)
run('done'); page(8490); ok('a few places fewer (one taken off the map): no new picture',run('need').returncode!=0)
page(0); ok('a page with no places is an error, not a picture of an empty map',run('need').returncode!=0 and run('done').returncode!=0)
print(f'{len(fails)} FAILED' if fails else 'first picture test: 7 checks passed'); sys.exit(1 if fails else 0)
