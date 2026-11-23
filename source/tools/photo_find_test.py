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
ok('a "none" recorded under an earlier, narrower search is asked again',ag(('','2026-11-19','nothing on Commons within 150 m'))is True and ag(('','2026-11-21','only a street sign'))is True and ag(('','2026-11-22','x'*9,1))is True)
ok('a "none" recorded under the search as it is now is not, and a chosen picture never is',ag(('','2026-11-22','only a street sign',getattr(pf,'SEARCH',0)))is False and ag(row)is False and ag(tuple(row)+('loose',))is False)
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
got=pn(PL,{'d':row,'e':('','2026-11-22','only a street sign',getattr(pf,'SEARCH',0))})
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
# ---- the search was widened again (November 21, 2026): the owner found the finder passing over photographs that are on Commons ----
G=lambda n,d=None: getattr(pf,n,d)
ok('a TIFF photograph is offered (the Library of Congress building surveys are TIFF, and Commons serves a JPEG of each)',pf.usable(dict(good,mime='image/tiff'))=='',pf.usable(dict(good,mime='image/tiff')))
ok('a PDF or an SVG is still not a photograph',pf.usable(dict(good,mime='application/pdf'))!='' and pf.usable(dict(good,mime='image/svg+xml'))!='')
ok('a survey drawing sheet is not offered',pf.usable(dict(good,mime='image/tiff',title='File:Old Mill, Exampleville, Example County, NY HAER NY,1-EX,1- (sheet 2 of 6).tif'))!='')
ok('a survey credit reads as a name',pf.credit('<div class="fn value">\nLowe, Jet, creator</div>')=='Jet Lowe' and pf.credit('Historic American Buildings Survey, creator')=='Historic American Buildings Survey',[pf.credit('<div class="fn value">\nLowe, Jet, creator</div>'),pf.credit('Historic American Buildings Survey, creator')])
va=G('variants',lambda n:[])
V=va('Adirondac (Tahawus) and McIntyre furnace')
ok('a long title is also tried by its parts and by the name in brackets',V[:1]==['Adirondac and McIntyre furnace'] and 'McIntyre furnace' in V and 'Adirondac' in V and 'Tahawus' in V,V)
V=va("Brimmer Farm: George Brimmer's grave (1755)")
ok('a year in brackets is not a name',"George Brimmer's grave" in V and 'Brimmer Farm' in V and not any('1755' in v for v in V),V)
po=G('places_of',lambda s:[])
ok('the hamlet in brackets counts as the town too',po({'name':'Knox District School No. 5','town':"Knox (Thompson's Lake)"})[:2]==['knox','thompson s lake'],po({'name':'Knox District School No. 5','town':"Knox (Thompson's Lake)"}))
nm=G('named',lambda t,s:None)
ADK={'id':'adirondac','name':'Adirondac (Tahawus) and McIntyre furnace','town':'Newcomb','lat':44.0872,'lon':-74.0557,'prec':'site'}
LYN={'id':'lynde','name':'Lynde Point Light','town':'Old Saybrook','lat':41.2700,'lon':-72.3400,'prec':'exact'}
ok('a survey photograph that names one part of the title and the hamlet names the place',nm('File:Jet Lowe, Photographer, June, 1978. MCINTYRE IRON WORKS. EAST PORTAL FURNACE. - Adirondack Iron and Steel Company, New Furnace, Hudson River, Tahawus, Essex County, NY HAER NY,16-TAHA,1-28.tif',ADK)==2)
ok('a name one word short, with the town, half names it: offered, marked to look twice',nm('File:Lynde Lighthouse, Old Saybrook, Connecticut.jpg',LYN)==1,nm('File:Lynde Lighthouse, Old Saybrook, Connecticut.jpg',LYN))
ok('three telling words with no town half name it too',nm('File:Lynde Point Light 2019.jpg',LYN)==1)
ok('the town alone does not name it, nor does one word of a short name',nm('File:Main Street, Old Saybrook.jpg',LYN)==0 and nm('File:Custom House, Salem.jpg',{'name':'Sag Harbor Custom House','town':'Sag Harbor'})==0)
ok('the old rule still holds: every telling word and the town',nm('File:Custom House, Sag Harbor, New York.jpg',{'name':'Sag Harbor Custom House','town':'Sag Harbor'})==2)
qs=G('queries',lambda s:[])(ADK)
ok('Commons is asked under the whole title with the town, and under each telling part by itself, five questions at most',qs[:1]==['Adirondac and McIntyre furnace Newcomb'] and 'McIntyre furnace' in qs and len(qs)<=5,qs)
t3=G('thumb330',lambda u:u)
ok('the sheet asks for a small copy of a TIFF as of a JPEG',t3('https://thumb.wikimedia.org/wikipedia/commons/thumb/d/d9/X.tif/lossy-page1-960px-thumbnail.tif.jpg')=='https://thumb.wikimedia.org/wikipedia/commons/thumb/d/d9/X.tif/lossy-page1-330px-thumbnail.tif.jpg' and t3('https://upload.wikimedia.org/wikipedia/commons/thumb/a/ab/Old_mill.jpg/900px-Old_mill.jpg')=='https://upload.wikimedia.org/wikipedia/commons/thumb/a/ab/Old_mill.jpg/330px-Old_mill.jpg',t3('https://thumb.wikimedia.org/wikipedia/commons/thumb/d/d9/X.tif/lossy-page1-960px-thumbnail.tif.jpg'))
# gathering, with Commons' answers canned
def pg(title,dlat=None,mime='image/jpeg',desc='',cats=()):
    d={'title':title,'imageinfo':[{'mime':mime,'width':3000,'height':2000,'thumburl':'https://upload.wikimedia.org/wikipedia/commons/thumb/a/ab/x.jpg/900px-x.jpg','thumbwidth':900,'thumbheight':600,'descriptionurl':'https://commons.wikimedia.org/wiki/'+title.replace(' ','_'),
       'extmetadata':{'LicenseShortName':{'value':'CC BY-SA 4.0'},'Artist':{'value':'Pat Example'},'ImageDescription':{'value':desc}}}],'categories':[{'title':c} for c in cats]}
    if dlat is not None: d['coordinates']=[{'lat':LYN['lat']+dlat,'lon':LYN['lon']}]
    return d
asked=[]
def canned(params,tries=8):
    asked.append(params)
    g=params.get('generator')
    if g=='geosearch': return {'query':{'pages':[pg('File:Shore road.jpg',0.0009),pg('File:Lynde Point Lighthouse from the water, Old Saybrook.jpg',0.0045),pg('File:Yacht club.jpg',0.0045),pg('File:Keeper at the door.tif',0.0002,mime='image/tiff')]}}
    if g=='search': return {'query':{'pages':[pg('File:Lynde Point Light, Old Saybrook CT.jpg'),{'title':'Category:Lynde Point Light'},{'title':'Category:Lighthouses in Connecticut'},pg('File:Lynde Point Light replica at a fairground (namesake far away).jpg',0.3)]}}
    if g=='categorymembers' and params.get('gcmtitle')=='Category:Lynde Point Light': return {'query':{'pages':[pg('File:Inner Light 1905.jpg'),pg('File:Somewhere else entirely.jpg',0.3)]}}
    return {'query':{'pages':[]}}
def canned2(params,tries=8):
    # Commons answers in two parts when there is much to say: the second part carries what the first left out
    if params.get('generator')!='geosearch': return {'query':{'pages':[]}}
    if 'clcontinue' in params: return {'query':{'pages':[dict(pg('File:Tower by the river.jpg',0.0003),categories=[{'title':'Category:Lynde Point Light'},{'title':'Category:Old Saybrook, Connecticut'}])]}}
    return {'continue':{'clcontinue':'x|y','continue':'||'},'query':{'pages':[dict(pg('File:Tower by the river.jpg',0.0003),categories=[])]}}
if G('gather'):
    real=pf._get; pf._get=canned2
    try: C2=pf.gather(LYN)
    finally: pf._get=real
    ok('when Commons answers in two parts both are read: a file whose categories come in the second part is known by them',[c.get('how') for c in C2]==['pin+name'],[(c['title'],c.get('how')) for c in C2])
else: ok('when Commons answers in two parts both are read',False)
FEN={'id':'fendall','name':'Fendall Hall','town':'Eufaula','lat':41.27,'lon':-72.34,'prec':'exact'}
def canned3(params,tries=8):
    g=params.get('generator')
    if g=='search': return {'query':{'pages':[pg('File:Fendall Hall, Eufaula, Alabama.jpg',0.23),pg('File:Fendall Hall, Eufaula (other side of the world).jpg',9.0),{'title':'Category:Fendall Hall'},{'title':'Category:Halls in Alabama'}]}}
    if g=='categorymembers' and params.get('gcmtitle')=='Category:Fendall Hall': return {'query':{'pages':[pg('File:Front porch.jpg')]}}
    return {'query':{'pages':[]}}
if G('gather'):
    real=pf._get; pf._get=canned3
    try: C3=pf.gather(FEN)
    finally: pf._get=real
    H3={c['title']:c.get('how') for c in C3}
else: H3={}
ok('a file that names the place and its town but carries a position some miles off is kept, to look twice (the Register gives Fendall Hall a point 27 km out of town, and Commons copied it); one a thousand kilometres off is a namesake',H3.get('File:Fendall Hall, Eufaula, Alabama.jpg')=='loose' and not any('other side' in t for t in H3),H3)
ok('a category that bears exactly the place\'s name is opened though the name has one telling word',H3.get('File:Front porch.jpg')=='category',H3)
ga=G('gather')
if ga:
    real=pf._get; pf._get=canned; slp=pf.time.sleep; pf.time.sleep=lambda x:None
    try: C=ga(LYN)
    finally: pf._get=real; pf.time.sleep=slp
    H={c['title']:c.get('how') for c in C}
else: C=[]; H={}
ok('a photograph taken at the pin is offered whatever its name, a TIFF among them',H.get('File:Shore road.jpg')=='pin' and H.get('File:Keeper at the door.tif')=='pin',H)
ok('one taken further off is offered when it names the place, and not when it does not',H.get('File:Lynde Point Lighthouse from the water, Old Saybrook.jpg')=='far' and 'File:Yacht club.jpg' not in H,H)
ok('one found by its name is offered',H.get('File:Lynde Point Light, Old Saybrook CT.jpg')=='name',H)
ok('the photographs in a category named for the place are offered; a category of the whole state is not opened',H.get('File:Inner Light 1905.jpg')=='category' and sum(1 for a in asked if a.get('generator')=='categorymembers')==1,H)
ok('Commons is asked for pictures, not for the scanned books that hold the same words',all('-filemime:pdf' in a.get('gsrsearch','') for a in asked if a.get('generator')=='search') and any(a.get('generator')=='search' for a in asked))
ok('every question asks for the position of every file, not of the first ten (Commons gives ten unless asked; the first finder saw at most ten photographs near a pin)',bool(asked) and all(a.get('colimit')=='max' for a in asked if a.get('generator')),[a.get('colimit') for a in asked])
ok('a photograph whose own position is somewhere else is a namesake, by name or by category',not any('namesake' in t or 'Somewhere else' in t for t in H),H)
ok('those that name the place come first, the unnamed one at the pin last',[c['title'] for c in C][:1]==['File:Lynde Point Light, Old Saybrook CT.jpg'] and [c['title'] for c in C][-1:]==['File:Shore road.jpg'],[c['title'] for c in C])
MES={'name':'Mesier Homestead','town':'Wappingers Falls','lat':41.6,'lon':-73.9}
ok('a file name run together is read as its words',nm('File:MesierHomestead.JPG The house in Wappingers Falls, New York',MES)==2,nm('File:MesierHomestead.JPG The house in Wappingers Falls, New York',MES))
ok('both words of a two-word name with no town half name it (look twice); one of the two does not',nm('File:Mesier Homestead in winter.jpg',MES)==1 and nm('File:Homestead in winter.jpg',MES)==0)
qc=G('queries',lambda s:[])({'name':'Coxsackie Light site','town':'Coxsackie'})
ok('Commons is not asked for the word "site" or "ruins": no photograph is called that',qc and not any(' site' in q for q in qc) and 'Coxsackie Light' in qc,qc)
pk=G('pick',lambda C:[])
many=[dict(title='File:P%02d.jpg'%i,how='pin',m=i) for i in range(30)]+[dict(title='File:L%d.jpg'%i,how='loose',m=None) for i in range(6)]+[dict(title='File:N.jpg',how='name',m=None)]
got=pk(many)
ok('of many candidates sixteen are shown: those that name the place first, and room is kept for four that half name it',len(got)==16 and got[0]['title']=='File:N.jpg' and sum(1 for c in got if c['how']=='loose')==4,[c['title'] for c in got])
os_=G('other_state',lambda t,st:None)
ok('a file that names another state and not this one is marked: the classic namesake',os_('File:Crawfordville Baptist Church, Crawfordville, Florida.jpg','Georgia') is True and os_('File:Crawfordville Baptist Church, Georgia.jpg','Georgia') is False and os_('File:Baptist church.jpg','Georgia') is False)
ok('"Washington" and "Georgia" in a name are not taken for the states, and a place with no known state is never marked',os_('File:Washington Park lake house, Albany.jpg','New York') is False and os_('File:Old mill, Florida.jpg',None) is False and os_('File:West Virginia Central depot, Virginia.jpg','Virginia') is False)
if G('gather'):
    import io,contextlib
    f3=os.path.join(tempfile.mkdtemp(),'pics_abcd.py'); real=pf._get; pf._get=lambda params,tries=8:{'query':{'pages':[]}}; cwd=os.getcwd(); os.chdir(tempfile.mkdtemp())
    try:
        with contextlib.redirect_stdout(io.StringIO()): n0=pf.look(dict(LYN,id='empty-place'),f3); n1=pf.look(dict(LYN,id='just-looking'))
    finally: pf._get=real; os.chdir(cwd)
    R3=pf.all_pics(os.path.dirname(f3))
    ok('a place Commons has nothing for is recorded as none by the tool, under today\'s search, so nobody looks at an empty sheet and it is not asked again',n0==0 and R3.get('empty-place',('x',))[0]=='' and pf.asked_again(R3['empty-place']) is False and pf.row_problem(R3['empty-place'])=='',str(R3)[:160])
    ok('but only when a file to record in is given: a bare look records nothing',n1==0 and 'just-looking' not in R3)
else: ok('a place Commons has nothing for is recorded as none by the tool',False)
if G('gather'):
    asked4=[]
    def canned4(params,tries=8):
        asked4.append(params)
        if params.get('generator')=='search': return {'query':{'pages':[pg('File:Lynde Point Light, Old Saybrook %d.jpg'%i) for i in range(3)]}}
        return {'query':{'pages':[]}}
    real=pf._get; pf._get=canned4
    try: C4=pf.gather(LYN)
    finally: pf._get=real
    ok('Commons allows about ten questions a minute, so none is wasted: once three photographs name the place no further name question is asked and no category opened',len(C4)==3 and sum(1 for a in asked4 if a.get('generator')=='search')==1 and not any(a.get('generator')=='categorymembers' for a in asked4),[a.get('generator') for a in asked4])
    ok('and the questions are spaced to stay under that allowance',6<=getattr(pf,'PACE',0)<=8,getattr(pf,'PACE',None))
# ---- logging in to Commons (November 22, 2026): a logged-in tool is allowed several thousand questions an hour where one known only
#      by its address gets a few hundred. The login is a bot password that lives outside the repository, in two environment
#      variables; without them the tool works as before.
import io,contextlib
class FakeResp:
    def __init__(s,j,code=200): s._j=j; s.status_code=code; s.headers={}
    def json(s): return s._j
    def raise_for_status(s): pass
class FakeSess:
    def __init__(s,result='Success'): s.calls=[]; s.result=result; s.headers={}
    def get(s,url,params=None,**k): s.calls.append(('get',dict(params or {}))); return FakeResp({'query':{'tokens':{'logintoken':'tok+\\'}}} if (params or {}).get('meta')=='tokens' else {'query':{'pages':[]}})
    def post(s,url,data=None,**k): s.calls.append(('post',dict(data or {}))); return FakeResp({'login':{'result':s.result,'reason':'nope'}})
lg=getattr(pf,'login',None); ok('the tool has a way to log in to Commons',callable(lg) and hasattr(pf,'new_session') and hasattr(pf,'pace'))
if callable(lg) and hasattr(pf,'new_session'):
    SECRET='s3cret-bot-pass-do-not-print'; fs=FakeSess(); buf=io.StringIO()
    with contextlib.redirect_stdout(buf), contextlib.redirect_stderr(buf): got=lg(fs,'Someone@atlas-pictures',SECRET)
    posts=[c[1] for c in fs.calls if c[0]=='post']
    ok('login: asks Commons for a login token, then sends the name, the password and the token in the body of a POST',got is True and fs.calls[0][0]=='get' and fs.calls[0][1].get('type')=='login' and len(posts)==1 and posts[0].get('lgname')=='Someone@atlas-pictures' and posts[0].get('lgpassword')==SECRET and posts[0].get('lgtoken')=='tok+\\' and posts[0].get('action')=='login',str([(c[0],sorted(c[1])) for c in fs.calls]))
    ok('login: the password is never in the address of a request',not any(SECRET in json.dumps(c[1]) for c in fs.calls if c[0]=='get'))
    fs2=FakeSess('Failed'); buf2=io.StringIO()
    with contextlib.redirect_stdout(buf2), contextlib.redirect_stderr(buf2): got2=lg(fs2,'Someone@atlas-pictures',SECRET)
    ok('login: a refused login says so and is not treated as logged in',got2 is False and 'not' in buf2.getvalue().lower(),buf2.getvalue()[:100])
    ok('login: nothing printed holds the password or the account name',SECRET not in buf.getvalue()+buf2.getvalue() and 'Someone' not in buf.getvalue()+buf2.getvalue(),(buf.getvalue()+buf2.getvalue())[:120])
    # the whole path: with the two variables set the first question logs in, later ones say "I am logged in" and are spaced closer; without them nothing changes
    real_new=pf.new_session; slp=pf.time.sleep; waits=[]; pf.time.sleep=lambda x:waits.append(x); env=dict(os.environ)
    try:
        for k in ('ATLAS_COMMONS_USER','ATLAS_COMMONS_PASS'): os.environ.pop(k,None)
        a=FakeSess(); pf.new_session=lambda:a; pf._S.clear(); pf._last[0]=0.0; pf._get({'action':'query','list':'search'}); pf._get({'action':'query','list':'search'})
        ok('with no login set: no login is tried, no question claims to be logged in, and the questions keep their old spacing',not any(c[0]=='post' for c in a.calls) and not any('assert' in c[1] for c in a.calls) and pf.pace()==pf.PACE and any(w>5 for w in waits),str(waits)[:80])
        os.environ['ATLAS_COMMONS_USER']='Someone@atlas-pictures'; os.environ['ATLAS_COMMONS_PASS']=SECRET; waits.clear()
        b=FakeSess(); pf.new_session=lambda:b; pf._S.clear(); pf._last[0]=0.0; pf._get({'action':'query','list':'search'}); pf._get({'action':'query','list':'search'})
        qs=[c[1] for c in b.calls if c[0]=='get' and c[1].get('meta')!='tokens']
        ok('with a login set: the tool logs in once, before its first question, and every question then says it is logged in',sum(1 for c in b.calls if c[0]=='post')==1 and len(qs)==2 and all(q.get('assert')=='user' for q in qs) and b.calls[0][1].get('meta')=='tokens',str([(c[0],c[1].get('assert'),c[1].get('meta')) for c in b.calls]))
        ok('logged in, the questions are spaced closer, but not closer than Commons allows a logged-in tool',1.5<=pf.pace()<=3 and pf.pace()<pf.PACE and not any(w>5 for w in waits),'%s %s'%(pf.pace(),str(waits)[:60]))
        c=FakeSess('Failed'); pf.new_session=lambda:c; pf._S.clear(); pf._last[0]=0.0
        with contextlib.redirect_stdout(io.StringIO()): pf._get({'action':'query','list':'search'})
        ok('a login that is refused: the tool carries on without it, at the old spacing',pf.pace()==pf.PACE and not any('assert' in x[1] for x in c.calls))
    finally: pf.new_session=real_new; pf.time.sleep=slp; os.environ.clear(); os.environ.update(env); pf._S.clear()
rp=G('row_problem',lambda v:'missing')
ok('a chosen row may say how the picture was found, and a "none" under which search',rp(tuple(row)+('loose',))=='' and rp(tuple(row))=='' and rp(('','2026-11-22','nothing on Commons near the pin',2))=='' and rp(('','2026-11-22','only a street sign'))=='',[rp(tuple(row)+('loose',)),rp(('','2026-11-22','nothing on Commons near the pin',2))])
ok('a row with a picture from elsewhere, or no credit, is refused',rp(('https://example.org/a.jpg',900,600,'Pat','CC BY 4.0','https://commons.wikimedia.org/wiki/File:A.jpg','2026-11-22'))!='' and rp((row[0],900,600,'','CC BY 4.0',row[5],'2026-11-22'))!='' and rp(tuple(row)+('made up',))!='')
d2=tempfile.mkdtemp(); f2=os.path.join(d2,'pics_wxyz.py'); pf.write_pick(f2,'a-place',tuple(row)+('far',)); pf.write_pick(f2,'b-place',('','2026-11-22','nothing on Commons near the pin',2))
A2=pf.all_pics(d2); out2=pf.merge({},A2,{'a-place','b-place'})
ok('such rows are written, read back and built into the site like the others',A2.get('a-place')==tuple(row)+('far',) and A2.get('b-place')[0]=='' and out2.get('a-place',[None])[:6]==list(row[:6]) and not out2.get('b-place'),str(out2)[:120])
print(f'{len(fails)} FAILED' if fails else 'photo_find test: all checks passed'); sys.exit(1 if fails else 0)
