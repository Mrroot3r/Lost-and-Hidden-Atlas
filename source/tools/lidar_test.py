#!/usr/bin/env python3
"""Offline test of the LiDAR ledger (tools/lidar.py): no network, standard library only, works in a scratch folder.
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
shutil.rmtree(tmp,ignore_errors=True); print('lidar ledger test:',ok,'checks passed')
