#!/usr/bin/env python3
"""The rules for what a place says about its "Legos" (used by tools/legos.py, tools/check.py and tools/build_sites.py;
test tools/lego_test.py). No network, no files.

WHAT THEY ARE. Under the eaves of a building in the Doric order, mostly Greek Revival work of the 1820s to 1850s and the
classical banks and courthouses that came later, sit flat blocks studded with rows of pegs, classically three rows of six.
The blocks are MUTULES and the pegs GUTTAE. Below them, in the frieze, are upright grooved blocks, TRIGLYPHS, each with a
short row of six pegs under it. The owner and the people who follow his videos call the peg blocks Legos and the grooved
blocks downspouts, and he catalogues them (November 27, 2026). On some buildings the pegs are holes (the Reformed Dutch
Church of Claverack): that kind is recorded as its own.

Three things are recorded:
  lego    pegs    the blocks with pegs
          holes   the blocks with holes where the pegs would be
          yes     a source says mutules are there and nobody has seen which kind
          no      somebody looked, on the ground or at a picture that shows the eaves closely, and there are none
          ?       looked for and could not tell (a whole-building photograph rarely shows them)
          Left out when nobody has looked.
  trig    yes | no    the grooved blocks (triglyphs) in the frieze. Left out when nobody has looked.
  legow   HOW IT IS KNOWN, for any yes: the words of a source that names them ("mutules", "guttae", "triglyphs"), or that
          somebody saw them on the ground, or the address of a close picture. NEVER from the style: "Greek Revival" or
          "Doric columns" makes a place worth a look and nothing more. Plenty of Greek Revival houses have plain eaves.
In tools/legos_*.py a row is (lego, trig or '', how it is known); lego is '?' there only when the triglyphs alone are known."""
import re
ANS=('pegs','holes','yes','no','?'); YES=('pegs','holes','yes')
_CODE={'pegs':'p','holes':'h','yes':'y','no':'n'}
def code(a): return _CODE.get(a or '','')
_GUESS=re.compile(r'\b(so it|therefore|must have|will have|probabl|likely|presum|typical|usually|should have|style says)',re.I)
def _how_problem(how):
    how=str(how or '').strip()
    if len(how)<15: return "say how it is known (legow): the words of a source that names mutules, guttae or triglyphs, or that it was seen on the ground, or the address of a close picture"
    if _GUESS.search(how): return "legow reads as a guess from the building's style ('%s'). A yes needs a source that names them, a close picture, or somebody who saw them; otherwise leave it out"%how[:60]
    return None
def _fit(lego,trig,how):
    if lego and lego not in ANS: return "lego='%s' must be one of %s (or left out)"%(lego,', '.join(ANS))
    if trig and trig not in ('yes','no'): return "trig='%s' must be yes or no (or left out)"%trig
    if lego in YES or trig=='yes': return _how_problem(how)
    return None
def place_problem(p):
    """what is wrong with a place's own lego, trig and legow, or None"""
    return _fit(p.get('lego') or '',p.get('trig') or '',p.get('legow') or '')
def row_problem(v):
    """what is wrong with one row of a legos_*.py file, or None"""
    if not isinstance(v,(list,tuple)) or len(v)!=3: return "must be ('pegs'|'holes'|'yes'|'no', 'yes'|'no'|'', 'how it is known')"
    if v[0] not in ANS: return "the first value must be pegs, holes, yes, no, or ? when only the triglyphs are known"
    if v[0]=='?' and v[1] not in ('yes','no'): return "a row of '?' says nothing: give it only when the triglyphs are known (yes or no)"
    return _fit(v[0],v[1] or '',v[2]) or _how_problem(v[2])

# ---- finding candidates in a text: only the proper names count
_W={'mutule':r'\bmutules?\b','guttae':r'\bgutt(?:ae|a)\b','triglyph':r'\btriglyphs?\b'}
def words(text): return {k for k,p in _W.items() if re.search(p,text or '',re.I)}
def sentence(text,word):
    """the sentence of the text that holds the word"""
    for s in re.split(r'(?<=[.!?])\s+',text or ''):
        if re.search(_W[word],s,re.I): return s.strip()
    return ''
def from_text(text):
    """(lego, trig) that a text's own words support: 'yes' for mutules or guttae named, 'yes' for triglyphs named"""
    w=words(text); return ('yes' if w&{'mutule','guttae'} else '','yes' if 'triglyph' in w else '')

# ---- a report from the ground, as the app sends it: "Legos seen: holes; triglyphs too. <a line more>"
def read_line(text):
    """(lego, trig, the rest of what they wrote) from a sent report, or None when it is not a Legos report"""
    m=re.match(r'\s*Legos seen:\s*(pegs|holes|none)(;\s*triglyphs too)?\.?\s*(.*)$',text or '',re.I|re.S)
    if not m: return None
    return ({'pegs':'pegs','holes':'holes','none':'no'}[m.group(1).lower()],'yes' if m.group(2) else '',m.group(3).strip())
def report_cmd(pid,lego,trig,note,who,when):
    """the command that records a report from the ground (tools/legos.py)"""
    how='Seen on the ground by %s, %s'%(who,when)+((': '+note.replace('"',"'")) if note else '')
    return 'python3 tools/legos.py set %s %s "%s"'%(pid,lego,how)+(' --trig '+trig if trig else '')
