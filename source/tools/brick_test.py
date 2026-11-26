#!/usr/bin/env python3
"""Brick colour and fire brick (tools/brickrule.py, used by brick.py, check.py and build_sites.py).
   python3 tools/brick_test.py        run it after changing brickrule.py or how brick.py records an answer
The owner, November 26, 2026: painted brick is not red brick, and the brick's colour is worth recording beside the
red-brick answer; fire brick is marked only when a source says so, because a picture cannot tell it from buff face brick."""
import sys,os
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
import brickrule as R
fails=[]
def ok(name,cond,extra=''):
    print(('ok   ' if cond else 'FAIL ')+name+(('  ['+str(extra)[:170]+']') if extra!='' else ''))
    if not cond: fails.append(name)
H='a picture of the building, https://example.org/x.jpg'
ok('the colours',R.COLOURS==('red','buff','dark','glazed','painted','mixed'))
ok('an old row with only the red-brick answer still stands',R.row_problem(('yes',H)) is None and R.row_problem(('no',H)) is None)
ok('a row with a colour stands',R.row_problem(('no',H,'buff','')) is None and R.row_problem(('some',H,'mixed','')) is None and R.row_problem(('yes',H,'red','')) is None)
ok('a colour that is not one of the six is refused',R.row_problem(('no',H,'yellow','')) is not None)
ok('red brick as the main thing cannot be buff, painted or mixed',all(R.row_problem(('yes',H,c,'')) for c in ('buff','dark','glazed','painted','mixed')))
ok('no red brick cannot have the colour red, nor "mixed", which says some of it is red',R.row_problem(('no',H,'red','')) is not None and R.row_problem(('no',H,'mixed','')) is not None)
ok('some red brick goes with red or mixed, not with one other colour alone',R.row_problem(('some',H,'red','')) is None and R.row_problem(('some',H,'buff','')) is not None)
ok('painted brick is never red brick',R.row_problem(('some',H,'painted','')) is not None and R.row_problem(('no',H,'painted','')) is None)
ok('fire brick needs the source\'s words, twelve characters or more',R.row_problem(('no',H,'buff','yes')) is not None and R.row_problem(('no',H,'buff','the kiln is lined with fire brick (state park page)')) is None)
ok('fire brick may be marked with no colour seen',R.row_problem(('no',H,'','ovens of firebrick, per the Register form')) is None)
ok('how it is known is still wanted',R.row_problem(('no','x','buff','')) is not None)
ok('a row of the wrong shape is refused, not crashed on',R.row_problem(('no',H,'buff')) is not None and R.row_problem('yes') is not None)
ok('the letter the map carries for each colour',[R.code(c) for c in R.COLOURS]==['r','b','d','g','p','m'] and R.code('')=='' )
ok('in a place list: bcol and fireb are checked the same way',R.place_problem({'brick':'no','bcol':'buff'}) is None and R.place_problem({'brick':'yes','bcol':'buff'}) is not None and R.place_problem({'brick':'no','bcol':'puce'}) is not None and R.place_problem({'brick':'?','bcol':'buff'}) is not None and R.place_problem({'brick':'no','fireb':'coke ovens lined with fire brick (park sign)'}) is None and R.place_problem({'brick':'no','fireb':'yes'}) is not None and R.place_problem({'brick':'yes'}) is None)
ok('"none" says somebody looked and there is no brick at all: only with no red brick',R.row_problem(('no',H,'none','')) is None and R.row_problem(('some',H,'none','')) is not None and R.row_problem(('yes',H,'none','')) is not None)
ok('and the map carries it as x, so the place is not asked about again',R.code('none')=='x')
print(f'{len(fails)} FAILED' if fails else 'brick test: 16 checks passed'); sys.exit(1 if fails else 0)
