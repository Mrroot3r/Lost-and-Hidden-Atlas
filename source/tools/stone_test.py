#!/usr/bin/env python3
"""The words cut on a building (tools/stonerule.py, tools/stones.py, and their use in check.py and build_sites.py).
   python3 tools/stone_test.py      run it after changing stonerule.py, stones.py or how the words are recorded or built
What it holds them to: the words are kept exactly as cut, with how they are known; the kind comes from the stone's own
word (erected, built, founded, established, dedicated, A.D., a bare date); the year is read from figures or Roman numerals;
and a year that differs from the write-up's is said, never smoothed over."""
import sys,os,subprocess,tempfile,shutil,re,json
W=os.path.dirname(os.path.dirname(os.path.abspath(__file__))); sys.path.insert(0,os.path.join(W,'tools')); sys.dont_write_bytecode=True
import stonerule as R
fails=[]; n=[0]
def ok(name,cond,extra=''):
    n[0]+=1; print(('ok   ' if cond else 'FAIL ')+name+(('  ['+str(extra)[:200]+']') if extra!='' else ''))
    if not cond: fails.append(name)
HOW="Seen on the ground by the Atlas's keeper, 2026-11-28: cornerstone"
ok('the kind is the stone\'s own word',[R.kind(x) for x in('ERECTED 1892','Built 1850','FOUNDED A.D. 1850','ESTABLISHED 1871','Est. 1871','DEDICATED MAY 3 1892','Rebuilt 1911','ORGANIZED 1832','Incorporated 1866','LAID JULY 4 1890')]==['erected','built','founded','established','established','dedicated','rebuilt','organized','incorporated','laid'],[R.kind(x) for x in('ERECTED 1892','Built 1850','FOUNDED A.D. 1850','ESTABLISHED 1871','Est. 1871','DEDICATED MAY 3 1892','Rebuilt 1911','ORGANIZED 1832','Incorporated 1866','LAID JULY 4 1890')])
ok('A.D. and Anno Domini are a kind when no other word is there, and a bare year is "date only"',[R.kind(x) for x in('A.D. 1887','ANNO DOMINI MDCCCXCII','1887','MDCCCXCII','First National Bank')]==['ad','ad','date','date','other'],[R.kind(x) for x in('A.D. 1887','ANNO DOMINI MDCCCXCII','1887','MDCCCXCII','First National Bank')])
ok('a name with a year is its own kind; initials with a year are a date; old spellings are read',[R.kind(x) for x in('UNION BLOCK 1892','J.M. 1780','Rebuilded, Enlarged & Improved by Andrew Carnegie, 1891','Vigilant, Instituted, 1817','MURNAY TOWER')]==['name','date','rebuilt','established','other'],[R.kind(x) for x in('UNION BLOCK 1892','J.M. 1780','Rebuilded, Enlarged & Improved by Andrew Carnegie, 1891','Vigilant, Instituted, 1817','MURNAY TOWER')])
ok('the year is read from figures and from Roman numerals',[R.year(x) for x in('ERECTED 1892','ANNO DOMINI MDCCCXCII','A.D. MCMXII','Founded 1850, rebuilt 1911','First National Bank')]==[1892,1892,1912,1850,None],[R.year(x) for x in('ERECTED 1892','ANNO DOMINI MDCCCXCII','A.D. MCMXII','Founded 1850, rebuilt 1911','First National Bank')])
ok('the label for a kind is plain',R.LABEL['erected']=='Erected' and R.LABEL['ad']=='A.D.' and R.LABEL['date']=='A date only')
ok('words with how they are known are fine; nothing said is fine',R.place_problem(dict(stone='ERECTED 1892',stonew=HOW)) is None and R.place_problem({}) is None)
ok('words with no word of how they are known are refused',bool(R.place_problem(dict(stone='ERECTED 1892'))))
ok('a description is not the words ("a cornerstone with the date")',bool(R.place_problem(dict(stone='a cornerstone with the date on it',stonew=HOW))) and bool(R.place_problem(dict(stone='?',stonew=HOW))))
ok('a row in a stones file is (words, how)',R.row_problem(('ERECTED 1892',HOW)) is None and bool(R.row_problem(('ERECTED 1892',''))) and bool(R.row_problem(('ERECTED 1892',))))
ok('the stone and the write-up agree, or the difference is said',R.differs(1892,'1890–1892') is None and R.differs(1892,'1892') is None and R.differs(1887,'1890–1892')==(1887,'1890–1892') and R.differs(None,'1890') is None and R.differs(1892,'') is None)
ok('a sent line is read',R.read_line('Building says: "ERECTED 1892" (cornerstone). North-east corner')==('ERECTED 1892','cornerstone','North-east corner') and R.read_line('Building says: "A.D. 1887"')==('A.D. 1887','','') and R.read_line('Found it.') is None,R.read_line('Building says: "A.D. 1887"'))
c=R.report_cmd('a-church','ERECTED 1892','cornerstone','North-east corner','a reader','2026-11-28')
ok('the command to record it says who saw it, when and where',c=='python3 tools/stones.py set a-church "ERECTED 1892" "Seen on the ground by a reader, 2026-11-28: cornerstone. North-east corner"',c)
# ---- the tool, in a scratch copy
d=tempfile.mkdtemp(); T=os.path.join(d,'tools'); os.makedirs(T); os.makedirs(os.path.join(d,'build'))
for f in('stones.py','stonerule.py'): shutil.copy(os.path.join(W,'tools',f),T)
json.dump([dict(id='a-church',name='A Church',town='X',story='The cornerstone was laid in 1890.',look=''),dict(id='b-house',name='B House',town='X',story='A plain house.',look='')],open(os.path.join(d,'build','sites.json'),'w'))
def run(*a): return subprocess.run([sys.executable,os.path.join(T,'stones.py')]+list(a),capture_output=True,text=True,cwd=d)
r=run('set','a-church','ERECTED 1892',HOW); fs=[f for f in os.listdir(T) if re.fullmatch(r'stones_[a-z]{4}\.py',f)]
ok('set writes this workspace\'s own stones_<four letters>.py',r.returncode==0 and len(fs)==1,(r.stdout+r.stderr)[-200:])
if fs:
    ns={}; exec(open(os.path.join(T,fs[0])).read(),ns); ok('the row holds the words as cut and how they are known',ns.get('STONE',{}).get('a-church')==('ERECTED 1892',HOW),ns.get('STONE'))
    run('set','a-church','ERECTED A.D. 1892',HOW); ns={}; exec(open(os.path.join(T,fs[0])).read(),ns)
    ok('a correction replaces the row in the same file',len([f for f in os.listdir(T) if f.startswith('stones_')])==1 and ns['STONE']['a-church'][0]=='ERECTED A.D. 1892')
ok('set refuses an id that is not a place, and a description',run('set','zz','ERECTED 1892',HOW).returncode!=0 and run('set','b-house','a stone with a date',HOW).returncode!=0)
r=run('find'); ok('find lists places whose write-up mentions a cornerstone or datestone and that have no words yet',r.returncode==0 and 'a-church' not in r.stdout and 'b-house' not in r.stdout,r.stdout[-200:])
r=subprocess.run([sys.executable,os.path.join(W,'tools','visits.py'),'/dev/stdin'],input=json.dumps({'visits':[],'stones':[{'id':'a-church','place':'A Church, X','says':'ERECTED 1892','where':'cornerstone','note':'','t':'2026-11-28'}]}),capture_output=True,text=True)
ok('tools/visits.py prints the owner\'s readings as commands','stones.py set a-church "ERECTED 1892"' in r.stdout,(r.stdout+r.stderr)[-300:])
shutil.rmtree(d)
print(f'{len(fails)} FAILED' if fails else f'stone test: {n[0]} checks passed'); sys.exit(1 if fails else 0)
