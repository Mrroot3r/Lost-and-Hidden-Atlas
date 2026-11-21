#!/usr/bin/env python3
"""Offline checks of tools/placepick.py (which of several places of one name start.py takes): python3 tools/placepick_test.py"""
import os,sys
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
import placepick as P
n=0
def ok(c,what):
    global n; n+=1
    if not c: print('FAIL:',what); sys.exit(1)
R=lambda name,typ,la=1,lo=2:{'display_name':name,'addresstype':typ,'lat':str(la),'lon':str(lo)}
J=[R('Montgomery County, New York, United States','county'),R('Village of Montgomery, Town of Montgomery, Orange County, New York, 12549, United States','village'),R('Montgomery, Alabama, United States','city')]
b,others=P.pick(J,'Montgomery, New York')
ok(b['addresstype']=='village','a village in the state named beats a county of the same name')
ok(len(others)==1 and 'Montgomery County, New York' in others[0]['display_name'],'the other one in that state is offered; the one in another state is not')
J=[R('Glenville, Greenwich, Fairfield County, Connecticut, United States','suburb'),R('Town of Glenville, Schenectady County, New York, United States','town')]
ok(P.pick(J,'Glenville, New York')[0]['addresstype']=='town','a place in another state is passed over')
J=[R('Bel Air, Allegany County, Maryland, United States','hamlet'),R('Bel Air, Harford County, Maryland, United States','town')]
b,others=P.pick(J,'Bel Air, Maryland'); ok(b['addresstype']=='town' and len(others)==1,'a town beats a hamlet of the same name in the same state, and the hamlet is offered')
J=[R('Nassau County, New York, United States','county'),R('Village of Nassau, Town of Nassau, Rensselaer County, New York, United States','village')]
ok('Rensselaer' in P.pick(J,'Nassau, New York')[0]['display_name'],'Nassau the village, not Nassau County')
ok(P.pick([R('Albany County, New York, United States','county')],'Albany County, New York')[0]['addresstype']=='county','asked for a county, a county is right')
J=[R('Paris, Ontario, Canada','town'),R('Paris, Texas, United States','city')]
ok(P.pick(J,'Paris')[0]['display_name'].startswith('Paris, Ontario'),'no state named: the first answer stands')
ok(P.pick(J,'Paris, Quebec')[0]['display_name'].startswith('Paris, Ontario'),'nothing in the state named: the first answer stands')
ok(P.pick([],'X, New York')==(None,[]),'no answers')
ok(P.pick(J,'Paris, TX')[0]['display_name'].startswith('Paris, Texas'),'a two-letter state key')
print('placepick test: %d checks passed'%n)
