#!/usr/bin/env python3
"""Which of several places of one name is meant: tools/start.py asks the geocoder for a handful and takes the best here.
"Montgomery, New York" came back as Montgomery County, "Nassau, New York" as Nassau County on Long Island, "Glenville,
New York" as a Glenville in Connecticut and "Bel Air, Maryland" as a hamlet 200 km from the county seat (the sessions'
notes, November 2026). The rule: stay in the state or province the query names; there, a city, town or village comes
before a hamlet or a neighbourhood, and those before a county, unless the query itself says "County"."""
import re,os,sys
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from states import STATES
NAME={s['k']:s['name'] for s in STATES}
RANK={'city':0,'town':0,'village':0,'municipality':0,'borough':0,'hamlet':1,'suburb':1,'neighbourhood':1,'quarter':1,'locality':1,'county':3,'state':4}
def state_of(query):
    """the state or province named last in the query, as its full name, or ''"""
    last=query.split(',')[-1].strip()
    if len(last)==2 and last.lower() in NAME: return NAME[last.lower()]
    for n in NAME.values():
        if n.lower()==last.lower(): return n
    return ''
def pick(results,query):
    """(the best answer or None, the other answers in the same state worth offering)"""
    if not results: return None,[]
    st=state_of(query) if ',' in query else ''
    inst=[r for r in results if st and re.search(r'(^|, )'+re.escape(st)+r'(,|$)',r.get('display_name',''))]
    if not inst: return results[0],[]
    wants_county='county' in query.lower() or 'parish' in query.lower()
    key=lambda r:(0 if wants_county and r.get('addresstype')=='county' else RANK.get(r.get('addresstype'),2))
    order=sorted(range(len(inst)),key=lambda i:(key(inst[i]),i))
    return inst[order[0]],[inst[i] for i in order[1:]]
