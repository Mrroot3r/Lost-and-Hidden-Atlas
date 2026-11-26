#!/usr/bin/env python3
"""The rules for what a place says about its brick (used by tools/brick.py, tools/check.py and tools/build_sites.py;
test tools/brick_test.py). No network, no files.

Three things are recorded:
  brick   yes | some | no | ?     RED brick to be seen there, as before. Red or red-brown brick counts. Yellow, buff, dark,
                                  glazed and PAINTED brick do not (the owner, November 26, 2026: brick painted red is not
                                  red brick).
  bcol    the colour of the brick you can see, when there is any, judged from a picture or a source's words:
            red       red or red-brown
            buff      yellow, cream, buff or tan (Milwaukee's cream brick)
            dark      brown, purple-brown or black, by its own colour and not by soot
            glazed    glazed or enamelled face brick, of any colour
            painted   painted over, so its own colour cannot be seen
            mixed     red together with another of these
            none      somebody looked and there is no brick at all (stone, wood, concrete, earth)
          Left out when nobody could tell.
  fireb   the words of a SOURCE that says fire brick (refractory brick) is there: a kiln, a furnace, a coke oven, a
          boiler setting. Never from a picture: fire brick is mostly buff, and a picture cannot tell it from buff face brick.
In tools/bricks_*.py a row is (brick, how it is known) or (brick, how it is known, bcol or '', fireb or '')."""
COLOURS=('red','buff','dark','glazed','painted','mixed')
_CODE={'red':'r','buff':'b','dark':'d','glazed':'g','painted':'p','mixed':'m','none':'x'}
def code(c): return _CODE.get(c or '','')
def _fit(brick,bcol,fireb):
    """why these three do not go together, or None"""
    if bcol=='none': return None if brick=='no' else "bcol='none' says there is no brick at all, so brick must be 'no', not '%s'"%brick
    if bcol and bcol not in COLOURS: return "bcol='%s' must be one of %s (or left out)"%(bcol,', '.join(COLOURS))
    if bcol and brick not in ('yes','some','no'): return "bcol is given but brick is '%s': say yes, some or no for red brick first"%brick
    if brick=='yes' and bcol and bcol!='red': return "brick='yes' means red brick is the main thing you see, so bcol cannot be '%s'; if only part is red say brick='some' with bcol='mixed', and if none is, brick='no'"%bcol
    if brick=='some' and bcol and bcol not in ('red','mixed'): return "brick='some' means part of it is red brick, so bcol is 'red' or 'mixed', not '%s'; brick that is all %s is brick='no'"%(bcol,bcol)
    if brick=='no' and bcol in ('red','mixed'): return "brick='no' says there is no red brick, but bcol='%s' says there is"%bcol
    if fireb and len(str(fireb).strip())<12: return "fireb must be the words of the source that says fire brick is there (and where it says it), not '%s'"%fireb
    return None
def row_problem(v):
    """what is wrong with one row of a bricks_*.py file, or None"""
    if not isinstance(v,(list,tuple)) or len(v) not in (2,4): return "must be ('yes'|'some'|'no', 'how it is known') or ('yes'|'some'|'no', 'how it is known', colour or '', fire-brick source or '')"
    if v[0] not in ('yes','some','no'): return "the first value must be yes, some or no"
    if len(str(v[1]).strip())<12: return "say how it is known: the picture's address, or the words of the source"
    if len(v)==2: return None
    return _fit(v[0],v[2] or '',v[3] or '')
def place_problem(p):
    """what is wrong with a place's own brick, bcol and fireb, or None (brick itself is checked by check.py as before)"""
    return _fit(p.get('brick') or '',p.get('bcol') or '',p.get('fireb') or '')
