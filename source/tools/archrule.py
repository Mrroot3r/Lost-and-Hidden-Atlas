#!/usr/bin/env python3
"""The rules for who designed or built a place (used by tools/archs.py, tools/check.py and tools/build_sites.py; test
tools/arch_test.py). No network, no files.

WHY (the owner, November 27, 2026): "there's a gajillion buildings with the same architect ... people would like to tap on a
building and see all buildings made by this architect". On that day 1,532 of 8,913 places named an architect in their text,
spelled 1,154 ways, so nothing could be tapped or counted. A name now has a field of its own and one spelling.

Three things are recorded:
  arch     the architect or architects: a person or a firm, as a source gives it. Several are separated by '; ' (or given
           as a list). Where a source names a firm, the firm is the name ("Wight and Wight").
  builder  who built it, when a source says so and it is not the architect: a contractor, a master builder, or an outfit
           such as the Works Progress Administration or the Civilian Conservation Corps.
  archw    HOW IT IS KNOWN, needed when either is given: the source and, where it helps, its words.
Never a guess from the look of a building or from who worked in the town.
In tools/archs_*.py a row is (architects, builder or '', how it is known).

ONE NAME, ONE SPELLING. canon() gives the spelling the Atlas uses: the one in SAME when the name is listed there, else the
name as written. key() is what two spellings are compared by ('&' and 'and', full stops and spacing make no difference).
Add a line to SAME when one person turns up under two names; the test holds the list to itself."""
import re, unicodedata
def key(name):
    s=unicodedata.normalize('NFKD',name or '').encode('ascii','ignore').decode().lower()
    s=s.replace('&',' and '); s=re.sub(r"[.,'’]",' ',s); return re.sub(r'\s+',' ',s).strip()
# spelling met -> the spelling the Atlas uses. Keys are compared by key(), so write them any way.
SAME={
 'Frank Packard':'Frank L. Packard',
 'H. H. Richardson':'Henry Hobson Richardson',
 'Shepley, Rutan & Coolidge':'Shepley, Rutan and Coolidge',
 'McKim, Mead and White':'McKim, Mead & White',
 'Carrere & Hastings':'Carrère and Hastings', 'Carrère & Hastings':'Carrère and Hastings',
 'Rapp & Rapp':'Rapp and Rapp',
 'Wight & Wight':'Wight and Wight',
 'Patton and Miller':'Patton & Miller',
 'Richard M. Upjohn':'Richard Michell Upjohn',
 'A. J. Davis':'Alexander Jackson Davis',
 'Works Progress Administration (WPA)':'Works Progress Administration', 'WPA':'Works Progress Administration',
 'CCC':'Civilian Conservation Corps',
}
_SAME={key(k):v for k,v in SAME.items()}
def canon(name):
    n=re.sub(r'\s+',' ',str(name or '')).strip(' ;,'); return _SAME.get(key(n),n)
def names(v):
    """the names in an arch= or builder= value, each in the Atlas's spelling, in order, without repeats"""
    parts=v if isinstance(v,(list,tuple)) else str(v or '').split(';'); out=[]
    for p in parts:
        c=canon(p)
        if c and key(c) not in [key(x) for x in out]: out.append(c)
    return out
_NOT=re.compile(r'^(unknown|unk|none|n/?a|\?+|not known|anonymous|various|multiple|local builder|unknown architect|architect unknown)$',re.I)
_GUESS=re.compile(r'\b(probabl|likely|presum|perhaps|possibly|from the look|looks like|must be|i think|maybe)',re.I)
def _name_problem(n):
    if _NOT.match(n.strip()): return "'%s' is not a name: leave the field out when no source names anybody"%n
    if len(n)<4 or len(n)>70 or len(n.split())>9 or not re.search(r'[A-Za-z]{2}',n): return "'%s' does not read as the name of a person or a firm (several names are separated by '; ')"%n[:60]
    return None
def _fit(arch,builder,how):
    a=names(arch); b=names(builder)
    for n in a+b:
        p=_name_problem(n)
        if p: return p
    if a or b:
        how=str(how or '').strip()
        if len(how)<12: return "say how it is known (archw): the source, and its words where that helps"
        if _GUESS.search(how): return "archw reads as a guess ('%s'). A name needs a source that gives it; otherwise leave it out"%how[:60]
    return None
def place_problem(p):
    """what is wrong with a place's own arch, builder and archw, or None"""
    return _fit(p.get('arch') or '',p.get('builder') or '',p.get('archw') or '')
def row_problem(v):
    """what is wrong with one row of an archs_*.py file, or None"""
    if not isinstance(v,(list,tuple)) or len(v)!=3: return "must be ('<architect>; <architect>', '<builder>' or '', 'how it is known')"
    if not names(v[0]) and not names(v[1]): return "a row names an architect or a builder"
    return _fit(v[0],v[1],v[2])
