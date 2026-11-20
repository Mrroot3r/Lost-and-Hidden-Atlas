#!/usr/bin/env python3
"""The photo finder's rules, without the network.   python3 tools/photo_find_test.py
Run it after changing tools/photo_find.py. What it holds the tool to: only a freely licensed photograph with a
photographer to credit is offered (never a map, a seal, a drawing file, a sliver of a panorama or a thumbnail-sized
picture); a credit carries no e-mail address; a choice is written to a pics_*.py file that tools/safe_data.py accepts;
and when the site is built a picture from a place's own Wikipedia article wins over a found one, a found one fills a
place that had none, and "looked, nothing fits" shows nothing."""
import sys,os,json,tempfile,importlib
HERE=os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0,HERE)
fails=[]
def ok(name,cond,extra=''):
    print(('ok   ' if cond else 'FAIL ')+name+(('  ['+str(extra)[:150]+']') if extra!='' else ''))
    if not cond: fails.append(name)
try: pf=importlib.import_module('photo_find')
except Exception as e: print('FAIL photo_find.py can be imported without running anything  [%s]'%str(e)[:120]); print('1 FAILED'); sys.exit(1)
good=dict(src='x',title='File:Old mill, Exampleville.jpg',mime='image/jpeg',width=3000,height=2000,lic='CC BY-SA 4.0',artist='<a href="//commons.wikimedia.org/wiki/User:Pat">Pat Example</a>')
ok('a free photograph with a photographer is usable',pf.usable(good)=='' ,pf.usable(good))
for why,ch in (('a non-commercial licence',dict(lic='CC BY-NC 2.0')),('no licence',dict(lic='')),('no photographer',dict(artist='')),('a drawing file',dict(mime='image/svg+xml')),
               ('a small picture',dict(width=500,height=400)),('a map',dict(title='File:Map of Exampleville 1890.jpg')),('a seal',dict(title='File:Seal of Example County.png')),
               ('a sliver of a panorama',dict(width=9000,height=1200)),('a logo',dict(title='File:Exampleville Mill logo.jpg'))):
    c=dict(good,**ch); ok('not offered: '+why,pf.usable(c)!='',pf.usable(c))
ok('public domain and CC0 are free too',pf.usable(dict(good,lic='Public domain'))=='' and pf.usable(dict(good,lic='CC0'))=='')
ok('the credit is the name, with no e-mail address',pf.credit('Pat Example (pat'+chr(64)+'example.org)')=='Pat Example',pf.credit('Pat Example (pat'+chr(64)+'example.org)'))
nw=pf.name_words('Sag Harbor Custom House (Dering house)')
ok('the telling words of a name leave out "house", "church" and the like',nw==['sag','harbor','custom'],nw)
ok('a file that names the town and every telling word names the place',pf.names_it('File:Custom House, Sag Harbor, New York.jpg The old custom house',nw,'sag harbor'))
ok('one that names another town does not',not pf.names_it('File:Custom House, Salem.jpg The custom house',nw,'sag harbor'))
ok('nor one that names the town but not the place',not pf.names_it('File:Main Street, Sag Harbor.jpg',nw,'sag harbor'))
d=tempfile.mkdtemp(); f=os.path.join(d,'pics_test.py')
row=('https://upload.wikimedia.org/wikipedia/commons/thumb/a/ab/Old_mill.jpg/900px-Old_mill.jpg',900,600,"Pat O'Example",'CC BY-SA 4.0','https://commons.wikimedia.org/wiki/File:Old_mill.jpg','2026-11-20')
pf.write_pick(f,'old-mill-exampleville',row); pf.write_pick(f,'no-picture-place',('','2026-11-20','Only a street sign nearby'))
sys.path.insert(0,d); back=importlib.import_module('pics_test').PICS
ok('a choice and a "nothing fits" are written and read back as they were',back.get('old-mill-exampleville')==row and back.get('no-picture-place')[0]=='',str(back)[:120])
import subprocess
r=subprocess.run([sys.executable,os.path.join(HERE,'safe_data.py'),d],capture_output=True,text=True)
ok('safe_data.py reads the file and accepts it',r.returncode==0 and '1 place list' in (r.stdout+r.stderr),(r.stdout+r.stderr).strip()[-140:])
P={'has-wiki':['w.jpg',900,600,'A','CC BY 4.0','https://commons.wikimedia.org/wiki/File:W.jpg','Article'],'had-none':0}
out=pf.merge(P,{'has-wiki':row,'had-none':row,'new-place':row,'no-picture-place':('','2026-11-20','x'),'gone-id':row},{'has-wiki','had-none','new-place','no-picture-place'})
ok('a picture from the place\'s own article wins over a found one',out['has-wiki'][0]=='w.jpg')
ok('a found picture fills a place that had none, with no article title',out['had-none'][:6]==list(row[:6]) and out['had-none'][6]=='' and out['new-place'][6]=='',str(out.get('had-none'))[:100])
ok('"looked, nothing fits" shows nothing, and a place that no longer exists is left out','no-picture-place' not in out or not out['no-picture-place'],str({k:bool(v) for k,v in out.items()}))
ok('and a place that no longer exists is left out','gone-id' not in out)
print(f'{len(fails)} FAILED' if fails else 'photo_find test: all checks passed'); sys.exit(1 if fails else 0)
