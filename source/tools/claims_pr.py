"""Which regions an open pull request takes, read from its title and its branch name. Used by tools/choose.py; test tools/choose_test.py.

A region is taken by a pull request when
  - the branch name carries the region's code as a word of its own (ks-jcwr-johnson-third, carnegie-mo-zzzz), or the title does
    inside a batch key (kcmo_ind2_qfhm), or
  - the title or branch has a distinctive word of the region's name (Lansingburgh, Adirondacks, Blackstone), or
  - the state has one region only and the title names the state, or
  - the region is named for a city and the title names that city and its state ("Kansas City, Missouri").
State names are not distinctive words. Before November 25, 2026 they were, with every other long word of a region's label: one
open pull request for rural Kansas took ks, kcmo ("Kansas City, Missouri") and mo ("Missouri outside Kansas City") together,
and the hourly Kansas City research had nowhere to go."""
import re
GENERIC={'county','counties','valley','north','south','western','eastern','central','northern','southern','places','outside','southeast','southwest',
         'northeast','northwest','country','upper','lower','coast','shore','island','islands','lakes','mountains','river','greater','state','city'}
def regions_named(title,ref,STATES):
    txt=(str(title or '')+' '+str(ref or '')).lower()
    refwords=set(re.split(r'[^a-z0-9]+',str(ref or '').lower()))|set(w for k in re.findall(r'[a-z0-9]+(?:_[a-z0-9]+)+',str(title or '').lower()) for w in k.split('_'))
    names=sorted((st['name'].lower() for st in STATES),key=len,reverse=True)
    statewords={w for n in names for w in re.split(r'[^a-z]+',n) if w}
    # which states the text names: longest names first, each blanked once found, so that West Virginia is not also Virginia;
    # whole words, so that Arkansas is not Kansas; and a city called after another state ("Kansas City") is blanked first
    cities=[(c,st['name'].lower(),l.split(',')[0].split('&')[0].strip().lower()) for st in STATES for c,l in st['regions']]
    rest=txt; named=set(); out=set()
    for c,sn,city in cities:
        if ' ' in city and city not in names and any(w in statewords for w in city.split()) and re.search(r'\b'+re.escape(city)+r'\b',rest):
            # "kansas city, missouri" -> the city's own region; "kansas city, kansas" names Kansas the state
            if re.search(r'\b'+re.escape(city)+r'\b[\s,]*'+re.escape(sn)+r'\b',rest): out.add(c)
            rest=re.sub(r'\b'+re.escape(city)+r'\b',' ',rest)
    for n in names:
        if re.search(r'\b'+re.escape(n)+r'\b',rest): named.add(n); rest=re.sub(r'\b'+re.escape(n)+r'\b',' ',rest)
    for st in STATES:
        for c,l in st['regions']:
            if c in refwords: out.add(c); continue
            words=[w for w in re.split(r'[^a-z]+',l.lower()) if len(w)>4 and w not in GENERIC and w not in statewords]
            if any(re.search(r'\b'+re.escape(w),rest) for w in words): out.add(c)
            elif len(st['regions'])==1 and st['name'].lower() in named: out.add(c)
    return out
