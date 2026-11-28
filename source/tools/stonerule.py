#!/usr/bin/env python3
"""The rules for the words cut on a building (used by tools/stones.py, tools/check.py and tools/build_sites.py; test
tools/stone_test.py). No network, no files.

WHY (the owner, November 28, 2026): "there's a lot of different ways they say buildings are founded or erected ... I want to
record the words on the building itself, because I think that's interesting to put them into categories", and "I've been
going to the places in real life and looking at what it actually says, and nothing ever lines up with online".

Two things are recorded:
  stone    the words exactly as cut, on a cornerstone, a datestone, over the door or on a tablet set in the wall when the
           place was built: "ERECTED 1892", "FOUNDED A.D. 1850", "ANNO DOMINI MDCCCXCII". Not a description of the stone,
           and not a modern plaque or a historical marker put up later.
  stonew   HOW THEY ARE KNOWN: somebody read them on the ground, a picture that shows them, or a source that quotes them.
The KIND is not recorded: it is read from the words (kind()), by the stone's own word. So is the year (year()), from figures
or Roman numerals. Where the stone's year is not within the years the write-up gives, the place page says both (differs()):
the stone is one voice and the sources are another, and neither is silently corrected.
In tools/stones_*.py a row is (words, how they are known)."""
import re
KINDS=('erected','built','founded','established','dedicated','rebuilt','organized','incorporated','laid','ad','date','name','other')
LABEL={'erected':'Erected','built':'Built','founded':'Founded','established':'Established','dedicated':'Dedicated','rebuilt':'Rebuilt','organized':'Organized',
       'incorporated':'Incorporated','laid':'Laid','ad':'A.D.','date':'A date only','name':'A name and a date','other':'Other words'}
_K=[('rebuilt',r'\bre-?buil(?:t|ded)\b|\bre-?erected\b|\brestored\b'),('erected',r'\berected\b'),('built',r'\bbuilt\b|\bconstructed\b'),('founded',r'\bfounded\b'),
    ('established',r'\bestablished\b|\bestd?\b\.?|\binstituted\b'),('dedicated',r'\bdedicated\b|\bconsecrated\b'),('organized',r'\borgani[sz]ed\b'),('incorporated',r'\bincorporated\b|\binc\b\.?'),
    ('laid',r'\blaid\b')]
_ROM=r'\bM{1,2}(?:CM|CD|D?C{0,3})(?:XC|XL|L?X{0,3})(?:IX|IV|V?I{0,3})\b'
def _roman(s):
    v={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}; t=0
    for i,ch in enumerate(s): t+=-v[ch] if i+1<len(s) and v[ch]<v[s[i+1]] else v[ch]
    return t
def year(words):
    """the first year on the stone, from figures or Roman numerals, or None"""
    w=str(words or ''); best=None
    for m in re.finditer(r'\b(1[4-9]\d\d|20[0-2]\d)\b',w): best=(m.start(),int(m.group(1))); break
    for m in re.finditer(_ROM,w.upper()):
        y=_roman(m.group(0))
        if 1400<=y<=2029 and (best is None or m.start()<best[0]): best=(m.start(),y)
        break
    return best[1] if best else None
def kind(words):
    """the kind of wording, by the stone's own word; the earliest such word wins ("FOUNDED 1850, REBUILT 1911" is founded)"""
    w=str(words or '').lower(); hits=[(m.start(),k) for k,p in _K for m in [re.search(p,w)] if m]
    if hits: return sorted(hits)[0][1]
    if re.search(r'\ba\.? ?d\b\.?|\banno domini\b',w): return 'ad'
    rest=re.sub(_ROM,' ',re.sub(r'\b(1[4-9]\d\d|20[0-2]\d)\b',' ',str(words or '').upper()))
    if year(words) and not re.search(r'[A-Za-z]{3}',rest): return 'date'      # a bare year, or initials and a year
    return 'name' if year(words) else 'other'
def _words_problem(w):
    w=str(w or '').strip()
    if len(w)<3 or len(w)>240: return "stone must be the words as cut ('ERECTED 1892'), between 3 and 240 characters"
    if re.search(r'^(a|an|the)\b.*\b(cornerstone|datestone|date stone|stone|plaque|tablet|inscription)\b',w,re.I) and not year(w): return "'%s' describes the stone: give the words that are cut on it, exactly, or leave it out"%w[:60]
    if not re.search(r'[A-Za-z0-9]{2}',w): return "'%s' is not words"%w
    return None
def _fit(stone,how):
    if not str(stone or '').strip(): return None
    p=_words_problem(stone)
    if p: return p
    if len(str(how or '').strip())<12: return "say how the words are known (stonew): read on the ground and by whom, a picture that shows them, or the source that quotes them"
    return None
def place_problem(p): return _fit(p.get('stone') or '',p.get('stonew') or '')
def row_problem(v):
    if not isinstance(v,(list,tuple)) or len(v)!=2: return "must be ('<the words as cut>', 'how they are known')"
    if not str(v[0] or '').strip(): return "a row gives the words"
    return _fit(v[0],v[1])
def differs(y,years):
    """(the stone's year, the write-up's years) when the stone's year is outside every span the write-up gives, else None"""
    if not y or not str(years or '').strip(): return None
    ys=[int(x) for x in re.findall(r'\b(1[4-9]\d\d|20[0-2]\d)\b',str(years))]
    if not ys: return None
    spans=re.findall(r'(1[4-9]\d\d|20[0-2]\d)\s*[–-]\s*(1[4-9]\d\d|20[0-2]\d)',str(years))
    if y in ys or any(int(a)<=y<=int(b) for a,b in spans): return None
    return (y,str(years))
# ---- a report from the ground, as the app sends it: Building says: "ERECTED 1892" (cornerstone). <a line more>
def read_line(text):
    m=re.match(r'\s*Building says:\s*"(.+?)"(?:\s*\(([^()]{2,40})\))?\.?\s*(.*)$',text or '',re.S)      # the words are in quotes: they may hold full stops ("A.D. 1887")
    if not m or not m.group(1).strip(): return None
    return (m.group(1).strip(),(m.group(2) or '').strip(),(m.group(3) or '').strip())
def report_cmd(pid,words,where,note,who,when):
    how='Seen on the ground by %s, %s'%(who,when)+((': '+'. '.join(x for x in (where,note) if x)) if (where or note) else '')
    return 'python3 tools/stones.py set %s "%s" "%s"'%(pid,words.replace('"',"'"),how.replace('"',"'"))
