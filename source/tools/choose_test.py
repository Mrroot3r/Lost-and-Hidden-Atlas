#!/usr/bin/env python3
"""Which regions an open pull request takes (tools/claims_pr.py, used by tools/choose.py).
   python3 tools/choose_test.py      run it after changing how choose.py reads the open pull requests
On November 25, 2026 one open pull request, "Add 8 places in Jefferson and rural Leavenworth counties, Kansas", took all
three regions of Kansas and Missouri (ks, kcmo "Kansas City, Missouri" and mo "Missouri outside Kansas City"), because any
word of a region's label counted, the state names among them, and the hourly Kansas City research had nowhere to go."""
import sys,os
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from states import STATES
import claims_pr
fails=[]
def ok(name,cond,extra=''):
    print(('ok   ' if cond else 'FAIL ')+name+(('  ['+str(extra)[:160]+']') if extra!='' else ''))
    if not cond: fails.append(name)
R=lambda title,ref='claude/confident-johnson-5aw1qo': sorted(claims_pr.regions_named(title,ref,STATES))
r=R('Add 8 places in Jefferson and rural Leavenworth counties, Kansas')
ok('a Kansas pull request takes Kansas, and neither region of Missouri',r==['ks'],r)
r=R('Independence, Missouri: six more places (kcmo_ind2_qfhm)')
ok('a pull request that names its region code takes that region only',r==['kcmo'],r)
r=R('Kansas City, Missouri: ten places in the West Bottoms')
ok('"Kansas City, Missouri" is the Kansas City region, not Kansas and not the rest of Missouri',r==['kcmo'],r)
r=R('Kansas City, Kansas: Strawberry Hill churches')
ok('"Kansas City, Kansas" is Kansas',r==['ks'],r)
r=R('Carnegie libraries, Arkansas: 14 places')
ok('Arkansas is not Kansas',r==['ar'],r)
r=R('West Virginia: 12 places in the New River Gorge')
ok('West Virginia is not Virginia',r==['wv'],r)
r=R('Carnegie libraries in Missouri outside Kansas City: 22 places','carnegie-mo-zzzz')
ok('a branch that carries a region code takes it',r==['mo'],r)
r=R('Johnson County, Kansas, third pass: 10 places','ks-jcwr-johnson-third')
ok('a branch code and a state name together are one region',r==['ks'],r)
r=R('Troy & Lansingburgh: eight mill buildings')
ok('a distinctive word of a region\'s name still takes it (Lansingburgh)','troy' in r,r)
r=R('Pictures: record 13 places with no usable photograph','claude/keen-hypatia-g38jwd')
ok('a pull request that names no ground takes none',r==[],r)
r=R('The long-press / right-click box, made small','small-spot-menu')
ok('nor does an app change',r==[],r)
# ---- ground with nothing left (tools/dry.py). On November 25, 2026 the Kansas City runs kept going back to counties that ten
# notes in a row had called worked out, and one run spent 25 minutes to add two places. A region can now be marked dry:
# the draw skips it for 30 days; and a run measures what is left before it starts (tools/gaps.py).
import dry, datetime
T=lambda s: datetime.datetime.strptime(s,'%Y%m%dT%H%M%S').replace(tzinfo=datetime.timezone.utc)
now=T('20261126T040000')
L=['kcmo 20261126T010000 ab12','released 20261126T010000 ab12','dry kcmo 20261126T013000 ab12 2','dry ks 20261020T000000 cd34 5','dry mo 20261125T000000 ee55 3','wet mo 20261125T120000 owner']
d=dry.dry_regions(L,now)
ok('a region marked dry today is dry',('kcmo' in d),d)
ok('a mark older than 30 days has lapsed',('ks' not in d),d)
ok('a mark taken back (wet) no longer counts',('mo' not in d),d)
ok('the reason says when and how many leads were left','2' in d.get('kcmo','') and '2026-11-26' in d.get('kcmo',''),d.get('kcmo'))
ok('a dry mark is not read as a claim by an older copy of the chooser (its second word is no time)',all(not __import__('re').fullmatch(r'\d{8}T\d{6}',l.split()[1]) for l in L if l.startswith(('dry','wet'))))
ok('a run may give ground up twice, not a third time',dry.may_redraw(0) and dry.may_redraw(1) and not dry.may_redraw(2))
# what is left: Register listings with no Atlas place near them and none of the same name
NR=[{'ref':'1','n':'Old Mill','k':'building','town':'A','county':'X','lat':39.0,'lon':-94.0},
    {'ref':'2','n':'First Church','k':'building','town':'A','county':'X','lat':39.1,'lon':-94.1},
    {'ref':'3','n':'Smith House','k':'building','town':'B','county':'Y','lat':39.2,'lon':-94.2},
    {'ref':'4','n':'Mound Group','k':'site','town':'B','county':'Y','lat':39.3,'lon':-94.3},
    {'ref':'5','n':'Wilson, John, House','k':'building','town':'C','county':'Y','lat':39.4,'lon':-94.4},
    {'ref':'6','n':"O'Bannon Homestead",'k':'building','town':'C','county':'Y','lat':39.5,'lon':-94.5},
    {'ref':'7','n':'Depot','k':'building','town':'D','county':'Z','lat':45.0,'lon':-94.0}]
AT=[{'id':'old-mill-a','name':'Old Mill','name2':'','reg':'r1','lat':39.0005,'lon':-94.0005},
    {'id':'john-wilson-house','name':'John Wilson House','name2':'','reg':'r1','lat':39.41,'lon':-94.4},
    {'id':'obannon-homestead','name':'O’Bannon Homestead (the old farm)','name2':'','reg':'r1','lat':39.51,'lon':-94.5},
    {'id':'far','name':'Far Place','name2':'','reg':'r2','lat':45.01,'lon':-94.0}]
g=dry.gaps(NR,AT,'r1')
names=sorted(x['n'] for x in g)
ok('a listing with an Atlas place beside it is not a gap','Old Mill' not in names,names)
ok('a listing with no Atlas place near and none of its name is a gap','First Church' in names and 'Smith House' in names,names)
ok('an archaeological site is not offered','Mound Group' not in names,names)
ok('a name the Register writes surname first matches the Atlas place of that name','Wilson, John, House' not in names,names)
ok('an apostrophe written two ways still matches',"O'Bannon Homestead" not in names,names)
g2=dry.gaps([{'ref':'8','n':'Hyde Park','k':'district','town':'E','county':'X','lat':39.0,'lon':-93.0}],AT+[{'id':'hp','name':'Hyde Park','name2':'','reg':'r1','lat':39.0,'lon':-93.2}],'r1')
ok('the same name 17 km away is another place: still a gap',len(g2)==1,g2)
ok('a listing that belongs to another region is left to that region','Depot' not in names,names)
ok('few gaps means dry: the limit is eight',dry.is_dry(7) and not dry.is_dry(8))
# ---- by county: a region is too big a piece to call dry (Kansas City's own county had 79 listings left while the counties
# round it had none), so what is left is counted county by county, and a session is sent to the nearest county with enough
g=dry.gaps(NR,AT,None)
ok('with no region asked, every listing of the state is weighed',sorted(x['n'] for x in g)==['Depot','First Church','Smith House'],[x['n'] for x in g])
BIG=[{'ref':str(i),'n':'House %d'%i,'k':'building','town':'T','county':c,'lat':la+i*0.02,'lon':lo} for c,la,lo,n in (('Near',39.2,-94.5,9),('Far',38.6,-90.2,30),('Thin',39.3,-94.4,3),('Marked',39.25,-94.45,12)) for i in range(n)]
tb=dry.county_table(dry.gaps(BIG,[],None))
ok('the table counts what is left in each county',{c:v['left'] for c,v in tb.items()}=={'Near':9,'Far':30,'Thin':3,'Marked':12},{c:v['left'] for c,v in tb.items()})
ks=dry.next_counties(tb,'zz',{dry.key('zz','Marked'):'x'},near=(39.1,-94.58))
ok('near a city: the nearest county with eight or more left comes first; a thin one and a dry one are passed over',[c for c,v in ks]==['Near','Far'],[c for c,v in ks])
ok('a county key is the state and the county, lower case, no spaces',dry.key('mo','St. Louis')=='mo:st.louis' and dry.key('MO','Cape Girardeau')=='mo:capegirardeau')
ok('a county with plenty left cannot be called dry (25 or more)',dry.can_mark(24) and not dry.can_mark(25))
ks2=[c for c,v in dry.next_counties(tb,'zz',{},near=None,rnd=__import__('random').Random(1))]
ok('with no city named the counties are drawn by lot among those with enough',set(ks2)<={'Near','Far','Marked'} and len(ks2)==3,ks2)
# ---- one listing set aside (November 26, 2026): Jackson County had 65 listings "left", several of them pulled down years ago
# (the Blackstone Hotel, Holy Name Church), and every session found that out afresh. A listing found gone, without a source,
# not wanted or already on the Atlas under another name is recorded once and leaves the count.
L2=['skip mo:85000942 20261126T140000 ab12 gone demolished_2000_per_Missouri_index','skip mo:1 20251001T000000 cd34 nosource old','skip mo:3 20261126T140500 ab12 onatlas smith-house-b','skip mo:2 20261126T141000 ab12 bogus x','dry mo:cass 20261126T013000 ab12 2']
sk=dry.skipped(L2,now)
ok('a listing set aside today is known, with its reason',sk.get('mo:85000942','').startswith('gone') and 'mo:3' in sk,sk)
ok('one set aside over a year ago is looked at again',('mo:1' not in sk),sk)
ok('a reason that is not one of the four is not taken',('mo:2' not in sk),sk)
ok('a dry mark is not a skipped listing and a skipped listing is not a dry mark',('mo:cass' not in sk) and ('mo:85000942' not in dry.dry_regions(L2,now)))
g=dry.gaps(NR,AT,None,skip={'3'})
ok('a listing set aside leaves the count',sorted(x['n'] for x in g)==['Depot','First Church'],[x['n'] for x in g])
ok('a session may set aside forty listings and no more',dry.may_skip(39) and not dry.may_skip(40))
ok('the four reasons',dry.KINDS==('gone','nosource','notwanted','onatlas'))
print(f'{len(fails)} FAILED' if fails else 'choose test: 38 checks passed'); sys.exit(1 if fails else 0)
