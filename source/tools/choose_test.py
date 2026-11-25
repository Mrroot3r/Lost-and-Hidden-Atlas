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
print(f'{len(fails)} FAILED' if fails else 'choose test: 11 checks passed'); sys.exit(1 if fails else 0)
