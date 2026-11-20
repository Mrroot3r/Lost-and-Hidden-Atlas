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
# ---- the search was widened (November 20, 2026): photographs that name the place are always asked for, and come first ----
near=dict(title='File:Main Street.jpg',desc='A street in Sag Harbor',m=20); named_far=dict(title='File:Custom House, Sag Harbor.jpg',desc='',m=None,byname=True)
named_near=dict(title='File:Sag Harbor Custom House front.jpg',desc='',m=60)
r=[c['title'] for c in pf.rank([near,named_far,named_near],nw,'sag harbor')] if hasattr(pf,'rank') else []
ok('a photograph that names the place comes before a nearer one that does not, and among those the one taken at the pin first',r==[named_near['title'],named_far['title'],near['title']],r)
r=[c['title'] for c in pf.rank([dict(near,m=90,title='File:B.jpg'),dict(near,m=10,title='File:A.jpg')],nw,'sag harbor')] if hasattr(pf,'rank') else []
ok('the rest stay nearest first',r==['File:A.jpg','File:B.jpg'],r)
ag=getattr(pf,'asked_again',lambda v:None)
ok('a "none" recorded before the search was widened is asked again',ag(('','2026-11-19','nothing on Commons within 150 m'))is True)
ok('a "none" recorded on the day it was widened or after is not, and a chosen picture never is',ag(('','2026-11-20','only a street sign'))is False and ag(('','2026-11-21','only a street sign'))is False and ag(row)is False)
d2=tempfile.mkdtemp(); later=row[:6]+('2026-11-21',)
pf.write_pick(os.path.join(d2,'pics_zzzz.py'),'place-x',('','2026-11-19','nothing nearby')); pf.write_pick(os.path.join(d2,'pics_aaaa.py'),'place-x',later)
pf.write_pick(os.path.join(d2,'pics_aaaa.py'),'place-y',row); pf.write_pick(os.path.join(d2,'pics_zzzz.py'),'place-y',('','2026-11-22','the picture was of the house next door'))
A=pf.all_pics(d2)
ok('a picture chosen on a later day replaces an earlier "none", whichever file holds it',A.get('place-x')==later,str(A.get('place-x'))[:80])
ok('and a later "none" takes a wrong picture away',A.get('place-y',('x',))[0]=='',str(A.get('place-y'))[:80])
try: cw=pf.name_words('Charlottetown City Hall','charlottetown')
except TypeError: cw=None
ok('a name whose only telling word is its town keeps its plain words too, so "City Hall" is not every photograph of the town',cw==['charlottetown','city','hall'],cw)
ok('then a street view of the town does not name it, and the city hall does',bool(cw) and not pf.names_it('File:Kent St, Charlottetown (471351).jpg Kent St, Charlottetown',cw,'charlottetown') and pf.names_it('File:City Hall, Charlottetown, PEI.jpg',cw,'charlottetown'))
ok('a name with telling words of its own is left as it was',pf.name_words('Sag Harbor Custom House (Dering house)','sag harbor')==['custom'] or pf.name_words('Sag Harbor Custom House (Dering house)','sag harbor')==['sag','harbor','custom'])
ro=getattr(pf,'refused',lambda j:None)
ok('a reply from Commons that carries an error is a refusal, not "no photographs here"',ro({'error':{'code':'ratelimited'}})is True and ro({'batchcomplete':True})is False and ro({'query':{'pages':[]}})is False)
# ---- a research session looks for pictures for its own new places (November 20, 2026) ----
na=getattr(pf,'no_article',lambda p:None)
ok('a new place with no Wikipedia article is one to look for a picture for',na({'links':[['Old mill (National Register nomination)','https://npgallery.nps.gov/x']]})is True and na({'links':[]})is True and na({})is True)
ok('one with an article is left to its article',na({'links':[['Wikipedia: Old Mill','https://en.wikipedia.org/wiki/Old_Mill'],['Other','https://example.org']]})is False)
pn=getattr(pf,'new_places',lambda P,done:None)
PL=[dict(id='a',st='standing',links=[]),dict(id='b',st='standing',links=[['Wikipedia: B','https://en.wikipedia.org/wiki/B']]),dict(id='c',st='gone',links=[]),dict(id='d',st='ruins',links=[]),dict(id='e',st='standing',links=[])]
got=pn(PL,{'d':row,'e':('','2026-11-20','only a street sign')})
ok('of a batch, the places listed are those with no article, still there, and not answered yet',got is not None and [p['id'] for p in got]==['a'],got and [p['id'] for p in got])
try: got=pn(PL,{},{'b'})
except TypeError: got=None
ok('and a place whose article turned out to have no usable picture is listed with them',got is not None and [p['id'] for p in got]==['a','b','d','e'],got and [p['id'] for p in got])
# the article lookup itself (tools/photos.py), with Wikipedia's answers canned: a session asks it about its own new places only
try:
    import photos
    A={'id':'with-pic','name':'Exampleville Old Mill','town':'Exampleville','lat':42.0,'lon':-73.0,'links':[['Wikipedia: Exampleville Old Mill','https://en.wikipedia.org/wiki/Exampleville_Old_Mill']]}
    B=dict(A,id='no-pic',name='Exampleville Depot',links=[['Wikipedia: Exampleville Depot','https://en.wikipedia.org/wiki/Exampleville_Depot']])
    def canned(params,tries=40):
        if params.get('prop','').startswith('pageimages'):
            return [{'query':{'pages':[{'title':'Exampleville Old Mill','coordinates':[{'lat':42.0005,'lon':-73.0}],'pageimage':'Old_mill.jpg','thumbnail':{'source':'https://upload.wikimedia.org/wikipedia/commons/thumb/a/ab/Old_mill.jpg/900px-Old_mill.jpg','width':900,'height':600}},
                                       {'title':'Exampleville Depot','coordinates':[{'lat':42.0005,'lon':-73.0}]}]}}]
        return [{'query':{'pages':[{'title':'File:Old mill.jpg','imageinfo':[{'descriptionurl':'https://commons.wikimedia.org/wiki/File:Old_mill.jpg','extmetadata':{'Artist':{'value':'Pat Example'},'LicenseShortName':{'value':'CC BY-SA 4.0'}}}]}]}}]
    real=photos.ask; photos.ask=canned
    try: R=photos.lookup([(A,photos.title_of(A)),(B,photos.title_of(B))],{}) if hasattr(photos,'lookup') else None
    finally: photos.ask=real
    ok('the article lookup can be asked about a few places and writes no file: a picture where the article has one, 0 where it has none',R is not None and R.get('no-pic')==0 and bool(R.get('with-pic')) and R['with-pic'][3]=='Pat Example' and R['with-pic'][6]=='Exampleville Old Mill',str(R)[:140])
except ImportError as e: print('skip the article lookup check: '+str(e)[:60])
# ---- a trial: a session says what it would choose and nothing is recorded for the map (comparing two models on the same places) ----
tl=getattr(pf,'trial_line',None); tr=getattr(pf,'trial_read',None)
T=(tl('old-mill','https://commons.wikimedia.org/wiki/File:Old_mill.jpg','')+tl('depot','','only a street | sign')+tl('old-mill','https://commons.wikimedia.org/wiki/File:Old_mill_2.jpg','')) if tl else ''
R=tr(T) if tr else None
ok('a trial answer is one line a note file can carry, and reads back: the last answer for a place wins, "none" is an empty picture',R=={'old-mill':'https://commons.wikimedia.org/wiki/File:Old_mill_2.jpg','depot':''},R)
io=getattr(pf,'id_ok',lambda i,ids:None)
ok('a landmark pin (lm-...) may have a picture though it is in no place list; any other unknown id may not',io('lm-thomas-cole-house',{'a'})is True and io('a',{'a'})is True and io('no-such-place',{'a'})is False and io('lm-Bad Id',{'a'})is False)
print(f'{len(fails)} FAILED' if fails else 'photo_find test: all checks passed'); sys.exit(1 if fails else 0)
