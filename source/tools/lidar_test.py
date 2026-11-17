#!/usr/bin/env python3
"""Offline test of the LiDAR ledger (tools/lidar.py): no network, works in a scratch folder. The ledger checks need only the
standard library; the last block (which state a point is in, coarse ground, the Massachusetts parcel rules, the tiled
aerial) needs numpy, scipy, PIL and requests and says so if they are missing.
   python3 tools/lidar_test.py
Run it after changing tools/lidar.py. It covers the parts a mistake would quietly spoil: ids that must never change,
the one-candidate-per-line file, the verdict rules, folding two copies of the ledger together, and the draft guard."""
import sys,os,json,tempfile,shutil,subprocess,io,contextlib
HERE=os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0,HERE)
tmp=tempfile.mkdtemp(prefix='lidartest'); os.chdir(tmp); os.makedirs('tools'); os.makedirs('src'); os.makedirs('research/lidar')
import lidar
lidar.HERE=os.path.join(tmp,'tools')          # place lists are looked for here: none yet
ok=0
def t(name,cond):
    global ok
    if not cond: print('FAIL:',name); shutil.rmtree(tmp,ignore_errors=True); sys.exit(1)
    ok+=1
def out(fn,*a):
    b=io.StringIO()
    with contextlib.redirect_stdout(b):
        try: fn(*a)
        except SystemExit: pass
    return b.getvalue()
C=lambda la,lo,pla,plo,dist,dep,size,unit='Alpha Beta State Forest': {'unit':unit,'lat':la,'lon':lo,'plat':pla,'plon':plo,'dist':dist,'depth':dep,'size':size,'sheet':'NY_Test_1_1900_62500_geo.tif','year':1900}
S={'units':{'Alpha Beta State Forest':{'file':'x','buildings':5,'pits':3,'sheets':['NY_Test_1_1900_62500_geo.tif']},'Able Baker State Forest':{'file':'y','buildings':1,'pits':1,'sheets':[]}},
   'cands':[C(42.1,-74.1,42.1001,-74.1001,20,0.7,[8,8]),C(42.1002,-74.1,42.1001,-74.1001,60,0.7,[8,8]),      # one pit, two buildings: the nearer is kept
            C(42.2,-74.2,42.2001,-74.2001,10,1.4,[9,7]),C(42.3,-74.3,42.3001,-74.3001,80,0.9,[15,6]),
            C(42.5,-74.5,42.5001,-74.5001,30,1.0,[7,7],'Able Baker State Forest')]}
json.dump(S,open('research/lidar/sweep.json','w'))
L=lidar.load(); t('empty ledger',L=={})
n=lidar.sync(L); L=lidar.load()
t('one row per pit',n==4 and len(L['Alpha Beta State Forest']['cands'])==3)
t('codes from initials, a clash gets another',{u['code'] for u in L.values()}=={'absf','abbsf'})
a=L['Alpha Beta State Forest']; t('best rank is number 1',a['cands'][0]['id']==a['code']+'1' and a['cands'][0]['depth']==1.4)
t('nearest building kept',[c for c in a['cands'] if c['lat']==42.1001][0]['dist']==20)
raw=open('lidar/units/alpha-beta-state-forest.json').read(); t('one candidate per line',raw.count('\n')==len(a['cands'])+3 and json.loads(raw)['name']=='Alpha Beta State Forest')
ids=[c['id'] for c in a['cands']]; S['cands'].append(C(42.4,-74.4,42.4001,-74.4001,5,1.5,[8,8])); json.dump(S,open('research/lidar/sweep.json','w'))
lidar.sync(L); t('a swept unit is never renumbered',[c['id'] for c in lidar.load()['Alpha Beta State Forest']['cands']]==ids)
i1,i2,i3=ids
t('no needs a reason',not lidar.mark_one(lidar.load(),[i1,'no'])[0] and not lidar.mark_one(lidar.load(),[i1,'no','because'])[0])
t('no with a reason',lidar.mark_one(lidar.load(),[i1,'no','water','pond','shore'])[0])
c=lidar.get(lidar.load(),i1)[1]; t('reason and note stored',c['status']=='no' and c['why']=='water' and c['note']=='pond shore' and c.get('when'))
t('yes needs the full sheet first',not lidar.mark_one(lidar.load(),[i2,'yes'])[0])
L=lidar.load(); u,c=lidar.get(L,i2); c['seen']='x'; lidar.save(u)
t('yes after the sheet',lidar.mark_one(lidar.load(),[i2,'yes','square','pit'])[0])
t('unknown id refused',not lidar.mark_one(lidar.load(),['zz9','no','faint'])[0])
t('a changed verdict drops the old reason',lidar.mark_one(lidar.load(),[i1,'maybe'])[0] and 'why' not in lidar.get(lidar.load(),i1)[1])
# draft: refused without an ownership check, refused on private land, written when the records allow it
t('draft needs check',"check" in out(lidar.cmd_draft,[i2+':test-road-pit']))
L=lidar.load(); u,c=lidar.get(L,i2); c['check']={'rule':'private','parcel':{'kind':'PRIVATE'},'padus':None,'town':'T','county':'Albany','road':''}; lidar.save(u)
t('draft refuses private land','may not be published' in out(lidar.cmd_draft,[i2+':test-road-pit']) and not [f for f in os.listdir('tools') if f.startswith('data_')])
L=lidar.load(); u,c=lidar.get(L,i2); c['check']={'rule':'padus','parcel':None,'padus':{'unit':'Alpha Beta State Forest','manager':'m','access':'OA'},'town':'Testtown','county':'Schoharie','road':'Test Road'}; lidar.save(u)
t('bad short name refused','not a usable short name' in out(lidar.cmd_draft,[i2+':Pit']))
o=out(lidar.cmd_draft,[i2+':test-road-pit']); fs=[f for f in os.listdir('tools') if f.startswith('data_lidar_')]
t('draft written',len(fs)==1 and 'wrote' in o)
txt=open('tools/'+fs[0]).read(); t('draft carries the measured facts and the caveat',"'lidar-test-road-pit'" in txt and 'Testtown' in txt and "'scho'" in txt and 'about 8 by 8 m and 0.7 m deep' in txt and 'No tax-parcel record could be checked' in txt and 'TODO' in txt)
compile(txt,fs[0],'exec'); t('draft is valid Python',True)
c=lidar.get(lidar.load(),i2)[1]; t('candidate now published',c['status']=='published' and c['place']=='lidar-test-road-pit')
t('a published candidate is left alone',not lidar.mark_one(lidar.load(),[i2,'no','faint'])[0])
os.remove('tools/'+fs[0]); t('a lost draft can be reopened',lidar.mark_one(lidar.load(),[i2,'yes'])[0])
# folding two copies together: the later verdict wins, nothing is dropped
shutil.copytree('lidar/units','other'); O=lidar.read_dir('other'); ou=O['Alpha Beta State Forest']
for c in ou['cands']:
    if c['id']==i3: c.update({'status':'no','why':'road','when':'2099-01-01'})
    if c['id']==i2: c.update({'status':'new'}); c.pop('when',None)
json.dump(ou,open('other/alpha-beta-state-forest.json','w'))
json.dump({'name':'Gamma State Forest','code':'gsf','state':'done','cands':[]},open('other/gamma-state-forest.json','w'))
lidar.merge_from('other'); L=lidar.load()
t('merge brings in a new unit','Gamma State Forest' in L)
t('merge takes the later verdict',lidar.get(L,i3)[1]['status']=='no' and lidar.get(L,i3)[1]['why']=='road')
t('merge keeps the verdict the other copy lacks',lidar.get(L,i2)[1]['status']=='yes')
t('status runs',('units swept' in out(lidar.cmd_status,[])) and 'report' not in out(lidar.cmd_report,[]))
# ---- more than one state (New York and Massachusetts)
t('a unit without a state is New York',lidar.st_of({})=='ny' and lidar.st_of({'st':'ma'})=='ma' and lidar.st_of(None)=='ny')
t('--state is taken out of the arguments',lidar.take_state(['Some Forest','--state','MA'])==(['Some Forest'],'ma') and lidar.take_state(['x'])==(['x'],None))
t('--state refuses a state the tool is not set up for','must be one of' in out(lidar.take_state,['x','--state','vt']))
t('regions go by state: Franklin County is two places',lidar.REGION['ny']['Franklin']=='adk' and lidar.REGION['ma']['Berkshire']=='berk' and lidar.REGION['ma']['Franklin'].startswith('TODO'))
t('every state names its box and its ground model',all(len(v['box'].split(','))==4 and v['src'] in ('ny','3dep','ma') for v in lidar.STATES.values()))
json.dump({'name':'Zeta State Forest','rings':[[[-72.7,43.9],[-72.69,43.9],[-72.69,43.91],[-72.7,43.9]]]},open('research/lidar/unit_ZetaStateForest.json','w'))
_us=lidar.unit_state; lidar.unit_state=lambda rings:'vt'
o=out(lidar.cmd_sweep,['Zeta State Forest'])
t('a unit in a state the tool does not cover is refused, and no ledger file is made','SKIPPED' in o and 'VT' in o and 'Zeta State Forest' not in lidar.load() and not os.path.exists('research/lidar/unit_ZetaStateForest.json'))
lidar.unit_state=_us
L=lidar.load(); g=L['Gamma State Forest']; g['st']='ma'; lidar.save(g)
t('status counts the states apart','Massachusetts 1' in out(lidar.cmd_status,[]))
t('a second unit of the same name in another state is refused','already has a unit of this name' in out(lidar.cmd_sweep,['Gamma State Forest','--state','ny']))
# ---- the ground model, the parcel rules and the aerial: these need numpy, scipy, PIL and requests (the site build has them)
try:
    import numpy as np, lidar_dem, parcel, ortho
    from scipy import ndimage as ndi
except Exception as e: print('(skipped: the ground-model, parcel and aerial checks need numpy, scipy, PIL and requests: %s)'%str(e)[:60])
else:
    t('the outlines tell New York from Massachusetts',lidar_dem.state_of(42.65,-73.75)=='ny' and lidar_dem.state_of(42.4226,-72.2253)=='ma' and lidar_dem.state_of(41.0,-69.0) is None)
    os.environ.pop('LIDAR_SRC',None)
    t('the ground model goes by the state',lidar_dem.source(42.65,-73.75)=='ny' and lidar_dem.source(42.4226,-72.2253)=='3dep')
    os.environ['LIDAR_SRC']='ma'; t('LIDAR_SRC overrides it',lidar_dem.source(42.65,-73.75)=='ma'); os.environ.pop('LIDAR_SRC')
    rng=np.random.default_rng(3); big=ndi.gaussian_filter(rng.normal(0,1,(300,300)),25)*400; fine=big+ndi.gaussian_filter(rng.normal(0,1,(300,300)),0.8)*0.05
    t('real 1 m ground is not called coarse',not lidar_dem.coarse(fine))
    t('a 10 m model blown up to 1 m is called coarse',lidar_dem.coarse(ndi.zoom(fine[::10,::10],10,order=1)))
    t('still water is not called coarse',not lidar_dem.coarse(np.zeros((200,200),'float32')+7))
    t('an empty answer is known as empty',lidar_dem.empty(np.full((50,50),-9999.0)) and lidar_dem.empty(np.full((50,50),np.nan)) and not lidar_dem.empty(fine))
    K=parcel.ma_kind
    t('Massachusetts: the Commonwealth by name is state land',K('COMMONWEALTH OF MASS','9150')=='STATE LAND' and K('MASS COMMONWEALTH OF DCR','')=='STATE LAND')
    t('Massachusetts: a house lot is private',K('SOMEBODY JANE','101')=='PRIVATE')
    t('Massachusetts: a town lot is public, a land trust is not government',K('TOWN OF SOMEWHERE','9300').startswith('public') and K('A LAND TRUST INC','950').startswith('tax-exempt') and not K('A CHURCH','960').startswith('public'))
    t('Massachusetts: nothing known is not called private',K('','')=='owner not published')
    class R:
        status_code=200
        def __init__(s,z,y,x):
            from PIL import Image
            b=io.BytesIO(); Image.new('RGB',(256,256),((x*37)%256,(y*53)%256,90)).save(b,'PNG'); s.content=b.getvalue()
    import re as _re
    ortho.requests.get=lambda u,**k: R(*[int(v) for v in _re.search(r'/tile/(\d+)/(\d+)/(\d+)$',u).groups()])
    im=ortho.tiles(ortho.MA,42.4226,-72.2253,100,500)
    t('the Massachusetts aerial is pieced together from tiles to the size asked',im.size==(500,500) and len(set(im.resize((8,8)).convert('L').tobytes()))>1)
shutil.rmtree(tmp,ignore_errors=True); print('lidar ledger test:',ok,'checks passed')
