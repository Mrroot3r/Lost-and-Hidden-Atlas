#!/usr/bin/env python3
"""Words a reader should not meet on a place page, put right when the site is built.

Place text is written by research sessions, and some of it carries workshop talk: "orda.org would not open in this session",
"the pin check showed", a pin note that reads "OpenStreetMap bridge (tools/nom.py)". The owner shows the Atlas on camera, and a
reader has no idea what a session or tools/nom.py is. tools/build_sites.py passes every place's story, look, access, hours and
pin note through here, so the sources stay as their sessions wrote them and text written tomorrow is put right too.
Only wording is changed, never a fact. Test: tools/plainwords_test.py."""
import re
WHEN='when this was written'
RULES=[
 # a photograph or page "opened in this session" is just a photograph or page; one "read in this session" was read
 (r'\s+(?:that was |which was )?opened (?:in )?this session\b',''),
 (r'\b(read|seen|found|checked|consulted|looked at|read about)\s+(?:in )?this session\b',r'\1'),
 (r"\brefuse[sd] this session's tools\b",'refuses to open'),
 (r'\brefused this session\b','refused to open '+WHEN),
 (r'\s+by this session\b',''),
 (r'\bthis session takes to be\b','is taken to be'),
 (r'\bin this session\b',WHEN),
 (r"\bthis session's\b","this research's"),
 (r'\bthis session\b','this research'),
 (r'\b((?:would|could|did) not (?:open|load|answer|be opened|be read|be reached))\s+from here\b',r'\1 '+WHEN),
 (r'\bthe pin[- ]check aerial\b','the aerial'),
 (r'\b(?:the )?pin[- ]check (?=aerial|tile|sheet|picture)',''),
 (r'\(pin check,','(checked on the aerial,'),
 (r'\b([Tt])he pin check\b',r'\1he aerial'),
 (r'\b[Pp]in check\b','the aerial'),
]
def text(t):
    """a place's story, look, access or hours as a reader should see it"""
    if not isinstance(t,str) or not t: return t
    for a,b in RULES: t=re.sub(a,b,t)
    return re.sub(r'  +',' ',t)
PY=r'(?:tools/)?\w+\.py'
def pin_note(t):
    """a pin note as a reader should see it: no tool is named. What a tool found is credited to the map it reads"""
    if not isinstance(t,str) or not t: return t
    t=re.sub(r'\s*\([^()]*\b'+PY+r'\b[^()]*\)','',t)                                              # any brackets that name a tool: "(tools/nom.py)", "(look.py, 250 m)"
    t=re.sub(r',?\s+found with '+PY,'',t)                                                         # "..., found with nom.py"
    t=re.sub(r'\s+(?:with|using|by|via)\s+'+PY+r'(?:\s+and\s+'+PY+r')?(?:\s+on an? (?:closer |wider |\d+ m )?'+PY+r' view)?','',t)   # "moved with look.py and pix.py"
    t=re.sub(r'(OpenStreetMap[^.;]{0,60}?),?\s+from (?:tools/)?(?:parking|nom|osmnear)\.py',r'\1',t)  # "the OpenStreetMap lot from parking.py"
    t=re.sub(r'\b(?:tools/)?(?:parking|nom|osmnear|osm_leads_box|geo)\.py\b','OpenStreetMap',t)
    t=re.sub(r'\b(?:tools/)?check\.py\b',"the Atlas's own check",t)
    t=re.sub(r'\b(?:tools/)?(?:look|pix|pincheck)\.py\b','the aerial',t)
    t=re.sub(r'\s*\b'+PY+r'\b(?: move)?','',t)                                                    # anything left
    t=re.sub(r'\bprec stays (site|area)\b',r'the pin still marks the \1',t)                          # the data field's name is not a word
    t=re.sub(r"\bprec(?:ision)?(?: is|\s*=)?:?\s*'?(site|area)'?(?=\W|$)",r'the pin marks the \1',t)
    t=re.sub(r"\bprec(?:ision)?(?: is| stays|\s*=)?:?\s*'?exact'?(?=\W|$)",'the pin is exact',t)
    t=re.sub(r'\s+([,.;:)])',r'\1',t)
    return text(t)
FIELDS=('story','look','accn','hook','hrs','hours')
def site(s):
    """one built place, its reader-facing text put right in place"""
    for f in FIELDS+('pn',):
        if isinstance(s.get(f),str): s[f]=pin_note(s[f])
    return s
