#!/usr/bin/env python3
"""What a place says about its "Legos" (tools/legorule.py, tools/legos.py, and their use in check.py and build_sites.py).
   python3 tools/lego_test.py      run it after changing legorule.py, legos.py or how an answer is recorded or built
What it holds them to: an answer is pegs, holes, yes, no or ? and a yes of any kind says how it is known; the downspout
blocks (triglyphs) are recorded beside it; a place's own answer wins over a later file; the words that find candidates
in a text are the proper names; and nothing is ever a yes from the style of a building alone."""
import sys,os,subprocess,tempfile,shutil,re,json
W=os.path.dirname(os.path.dirname(os.path.abspath(__file__))); sys.path.insert(0,os.path.join(W,'tools')); sys.dont_write_bytecode=True
import legorule as L
fails=[]; n=[0]
def ok(name,cond,extra=''):
    n[0]+=1; print(('ok   ' if cond else 'FAIL ')+name+(('  ['+str(extra)[:200]+']') if extra!='' else ''))
    if not cond: fails.append(name)
HOW="National Register form: 'a Doric entablature with mutules and triglyphs'"
ok('the codes the app is given',[L.code(a) for a in('pegs','holes','yes','no','?','',None)]==['p','h','y','n','','',''])
ok('pegs with how it is known is fine',L.place_problem(dict(lego='pegs',legow=HOW)) is None)
ok('nothing said at all is fine',L.place_problem({}) is None and L.place_problem(dict(lego='?')) is None)
ok('a yes with no word of how it is known is refused',bool(L.place_problem(dict(lego='pegs'))) and bool(L.place_problem(dict(lego='holes',legow='seen'))))
ok('an answer that is not one of the five is refused',bool(L.place_problem(dict(lego='some',legow=HOW))))
ok('triglyphs alone need how it is known too',bool(L.place_problem(dict(trig='yes'))) and L.place_problem(dict(trig='yes',legow=HOW)) is None)
ok('trig is yes, no or left out',bool(L.place_problem(dict(lego='pegs',trig='maybe',legow=HOW))))
ok('"the style says so" is not how it is known',bool(L.place_problem(dict(lego='yes',legow='It is a Greek Revival building, so it will have them'))) and bool(L.place_problem(dict(lego='pegs',legow='Doric order, therefore mutules'))),L.place_problem(dict(lego='yes',legow='It is a Greek Revival building, so it will have them')))
ok('a row in a legos file is (answer, trig, how)',L.row_problem(('holes','',"Seen on the ground and photographed, November 2026")) is None and L.row_problem(('no','no','Looked at every side on the ground, November 2026')) is None)
ok('a row always says how it is known, a no included',bool(L.row_problem(('no','',''))) and bool(L.row_problem(('pegs','yes'))))
ok('a row cannot be "not checked" and nothing more',bool(L.row_problem(('?','',HOW))))
ok('but it can record the triglyphs alone',L.row_problem(('?','yes',HOW)) is None)
# the words that find candidates in a text
ok('words: mutules, guttae and triglyphs are found',L.words('A Doric entablature with mutules, guttae and triglyphs.')=={'mutule','guttae','triglyph'},L.words('A Doric entablature with mutules, guttae and triglyphs.'))
ok('words: Doric or Greek Revival alone finds nothing',L.words('A Greek Revival temple front with Doric columns and a heavy cornice.')==set())
ok('words: the sentence that says it is given back',L.sentence('Built in 1831. A wooden portico of fluted columns and triglyphs whose pediment repeats the roof. It burned.','triglyph').startswith('A wooden portico'))
ok('what a text supports: triglyphs said, Legos not',L.from_text('Doric columns, triglyphs in the cornice and pediment.')==('', 'yes') and L.from_text('mutules with guttae under the cornice')==('yes','') and L.from_text('a plain cornice')==('',''))

# a report from the ground, as the app sends it ("Legos seen: holes; triglyphs too"), becomes the command that records it
ok('a sent line is read: kind and triglyphs',L.read_line('Legos seen: holes; triglyphs too. Under the tower cornice')==('holes','yes','Under the tower cornice') and L.read_line('Legos seen: pegs')==('pegs','','') and L.read_line('Legos seen: none')==('no','','') and L.read_line('Found it. A mill.') is None,L.read_line('Legos seen: holes; triglyphs too. Under the tower cornice'))
c=L.report_cmd('a-church','holes','yes','Under the tower cornice',"the Atlas's keeper",'2026-11-28')
ok('the command to record it says who saw it, when, and their words',c=="python3 tools/legos.py set a-church holes \"Seen on the ground by the Atlas's keeper, 2026-11-28: Under the tower cornice\" --trig yes",c)
ok('and what it writes passes the rules',L.row_problem(('holes','yes',"Seen on the ground by a reader, 2026-11-28")) is None)
r=subprocess.run([sys.executable,os.path.join(W,'tools','visits.py'),'/dev/stdin'],input=json.dumps({'visits':[],'legos':[{'id':'a-church','place':'A Church, X','lego':'pegs','trig':'','note':'six by three','t':'2026-11-28'}]}),capture_output=True,text=True)
ok('tools/visits.py prints the owner\'s Legos marks as commands',"legos.py set a-church pegs" in r.stdout and 'six by three' in r.stdout,(r.stdout+r.stderr)[-300:])
# ---- the tool and the build, in a scratch copy of the workspace's tools
d=tempfile.mkdtemp(); T=os.path.join(d,'tools'); os.makedirs(T); os.makedirs(os.path.join(d,'build'))
for f in('legos.py','legorule.py'): shutil.copy(os.path.join(W,'tools',f),T)
json.dump([dict(id='a-church',name='A Church',town='X',st='standing',story='Doric portico with triglyphs and mutules.',look=''),dict(id='b-house',name='B House',town='X',st='standing',story='A plain house.',look=''),
           dict(id='c-bank',name='C Bank',town='X',st='standing',story='x',look='',lg='p')],open(os.path.join(d,'build','sites.json'),'w'))
def run(*a): return subprocess.run([sys.executable,os.path.join(T,'legos.py')]+list(a),capture_output=True,text=True,cwd=d)
r=run('set','a-church','holes','Seen on the ground and photographed, November 2026','--trig','yes')
fs=[f for f in os.listdir(T) if re.fullmatch(r'legos_[a-z]{4}\.py',f)]
ok('set writes this workspace\'s own legos_<four letters>.py',r.returncode==0 and len(fs)==1,(r.stdout+r.stderr)[-200:])
if fs:
    ns={}; exec(open(os.path.join(T,fs[0])).read(),ns)
    ok('the row holds the answer, the triglyphs and how it is known',ns.get('LEGO',{}).get('a-church')==('holes','yes','Seen on the ground and photographed, November 2026'),ns.get('LEGO'))
    ok('the file is data and nothing else',not re.search(r'^\s*(import|from|def|for|class)\b',open(os.path.join(T,fs[0])).read(),re.M))
r=run('set','a-church','pegs','it is Greek Revival so it must'); ok('set refuses a yes that rests on the style',r.returncode!=0,(r.stdout+r.stderr)[-160:])
r=run('set','no-such-place','pegs',HOW); ok('set refuses an id that is not a place',r.returncode!=0)
r=run('set','b-house','no','Looked at every side on the ground, November 2026'); r2=run('list')
ok('list shows what is recorded',r2.returncode==0 and 'a-church' in r2.stdout and 'holes' in r2.stdout and 'b-house' in r2.stdout,r2.stdout[-200:])
r=run('words'); ok('words lists the places whose own text names the feature, and not the ones already answered',('a-church' not in r.stdout) and ('b-house' not in r.stdout),r.stdout[-300:])
shutil.rmtree(d)
print(f'{len(fails)} FAILED' if fails else f'lego test: {n[0]} checks passed'); sys.exit(1 if fails else 0)
