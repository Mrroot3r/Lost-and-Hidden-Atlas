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
 # met in the places' own write-ups on November 28, 2026: the same person with a middle name or initial more or less. The
 # spelling kept is Wikidata's where it lists the architect, else the fuller one.
 'A. A. Crowell':'Anthony Allaire Crowell',
 'A. B. Cross':'Asa Beebe Cross',
 'A. J. Warner':'Andrew Jackson Warner',
 'A. M. Jeffers':'Allan M. Jeffers',
 'Albert Fuller':'Albert W. Fuller',
 'Arthur C. Nash':'Arthur Nash',
 'Benjamin Marshall':'Benjamin H. Marshall',
 'Bradford Lee Gilbert':'Bradford Gilbert',
 'C. B. Chappell':'Charles B. Chappell',
 'C. C. Haight':'Charles C. Haight',
 'C. E. Choate':'Charles E. Choate',
 'Charles Alonzo Rich':'Charles A. Rich',
 'Charles Atwood':'Charles B. Atwood',
 'Charles Barber':'Charles I. Barber',
 'Charles Edward Choate':'Charles E. Choate',
 'Charles F. Owsley':'Charles Owsley',
 'Charles Platt':'Charles A. Platt',
 'Charles Z. Klauder':'Charles Klauder',
 'Clarence Shepard':'Clarence E. Shepard',
 'Clarence Wunder':'Clarence E. Wunder',
 'D. Fred Charlton':'Demetrius F. Charlton',
 'Daniel R. Huntington':'Daniel Riggs Huntington',
 'David O. Whilldin':'David Whilldin',
 'E. M. Wood':'Ernest M. Wood',
 'Edward C. Jones':'E.C. Jones',
 'Ehrick Rossiter':'Ehrick K. Rossiter',
 'Emmanuel Masqueray':'Emmanuel Louis Masqueray',
 'Ephraim B. Potter':'Ephraim Potter',
 'Ernest Brostrom':'Ernest O. Brostrom',
 'Eugene C. Gardner':'Eugene Clarence Gardner',
 'Frank Edbrooke':'Frank E. Edbrooke',
 'Frederic DeLongchamps':'Frederic Joseph DeLongchamps',
 'Frederic J. DeLongchamps':'Frederic Joseph DeLongchamps',
 'Frederick Stickney':'Frederick W. Stickney',
 'George A. Clough':'George Albert Clough',
 'George F. Barber':'George Franklin Barber',
 'George G. Meade':'George Meade',
 'George Heins':'George L. Heins',
 'George Mann':'George R. Mann',
 'George Washburn':'George P. Washburn',
 'George Washington Maher':'George W. Maher',
 'Glen W. Huntington':'Glen Huntington',
 'Gottfried Leonard Norrman':'G. L. Norrman',
 'H. Van Buren Magonigle':'Harold Van Buren Magonigle',
 'Hans T. Liebert':'Hans Theodore Liebert',
 'Harold Burton':'Harold W. Burton',
 'Harold H. Ginnold':'Harold Ginnold',
 'Henry Dudley':'Henry C. Dudley',
 'Henry Hoit':'Henry F. Hoit',
 'Henry J. Hardenbergh':'Henry Janeway Hardenbergh',
 'Henry M. Congdon':'Henry Martyn Congdon',
 'Henry Richards':'Henry C. Richards',
 'Henry Trost':'Henry Charles Trost',
 'Horatio N. White':'Horatio Nelson White',
 'Isaac Hamilton Rapp':'Isaac Rapp',
 'J. C. Sunderland':'James C. Sunderland',
 'J. E. Flanders':'James E. Flanders',
 'J. M. Gile':'Jacob M. Gile',
 'J. W. Yost':'Joseph W. Yost',
 'J.C. Holland':'James C. Holland',
 'James Harrison Dakin':'James H. Dakin',
 'John B. Parkinson':'John Parkinson',
 'John Bennes':'John Virginius Bennes',
 'John Francis Rague':'John F. Rague',
 'John Haskell':'John G. Haskell',
 'Joseph Lawlor':'Joseph M. Lawlor',
 'Joseph Shannon':'Joseph A. Shannon',
 'Kirtland Cutter':'Kirtland Kelsey Cutter',
 'Lewis Pilcher':'Lewis F. Pilcher',
 'Louis S. Curtiss':'Louis Curtiss',
 'M. F. Bell':'Morris Frederick Bell',
 'M. F. Cummings':'Marcus F. Cummings',
 'Marcus Cummings':'Marcus F. Cummings',
 'Matthias H. Baldwin':'Matthias Harvey Baldwin',
 'Milton E. Beebe':'Milton Earl Beebe',
 'Nathaniel C. Smith':'Nathaniel Cannon Smith',
 'Nelle E. Peters':'Nelle Peters',
 'Nicholas Clayton':'Nicholas J. Clayton',
 'Oscar Bohlen':'Oscar D. Bohlen',
 'Patrick Keely':'Patrick Charles Keely',
 'Paul Moratz':'Paul O. Moratz',
 'R. L. Daus':'Rudolph Daus',
 'Ralph Walker':'Ralph Thomas Walker',
 'Richard Kletting':'Richard K.A. Kletting',
 'Robert Coit':'Robert C. Coit',
 'Robert Gornall':'Robert F. Gornall',
 'Robert H. Robertson':'R. H. Robertson',
 'Robert William Gibson':'Robert W. Gibson',
 'Rudolph L. Daus':'Rudolph Daus',
 'Samuel Tarbet':'Samuel B. Tarbet',
 'Solomon Layton':'Solomon Andrew Layton',
 'Solon S. Beman':'Solon Spencer Beman',
 'Stephen Earle':'Stephen C. Earle',
 'Thomas H. Morgan':'Thomas Henry Morgan',
 'Thomas Lamb':'Thomas W. Lamb',
 'Thomas W. Williamson':'Thomas Wilson Williamson',
 'W. C. Harris':'William Critchlow Harris',
 'W. H. McLean':'William H. McLean',
 'W. J. Edbrooke':'Willoughby J. Edbrooke',
 'Wallace Dow':'Wallace L. Dow',
 'Walter E. Glover':'Walter Earl Glover',
 'Walter J. Paine':'Walter Jefferson Paine',
 'William A. Lang':'William Lang',
 'William B. Tubby':'William Tubby',
 'William Boyington':'William W. Boyington',
 'William Dodd':'William J. Dodd',
 'William E. Haugaard':'William Haugaard',
 'William Ginther':'WIlliam P. Ginther',
 'William Jay Brown':'William J. Brown',
 'William Kaufman':'William S. Kaufman',
 'William Storey':'William Benson Storey',
}
_SAME={key(k):v for k,v in SAME.items()}
def canon(name):
    n=re.sub(r'\s+',' ',str(name or '')).strip(' ;,'); return _SAME.get(key(n),n)
def unify(lists):
    """Given every place's names, a function that puts a list of names in the one spelling the map uses: the spelling in SAME,
    else the commonest way a name is written across the map ('Holabird & Roche' and 'Holabird and Roche' are one firm)."""
    import collections
    seen=collections.defaultdict(collections.Counter)
    for l in lists:
        for n in l: seen[key(canon(n))][canon(n)]+=1
    best={k:sorted(c.items(),key=lambda x:(-x[1],x[0]))[0][0] for k,c in seen.items()}
    def f(l):
        out=[]
        for n in l:
            c=best.get(key(canon(n)),canon(n))
            if c not in out: out.append(c)
        return out
    return f
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
