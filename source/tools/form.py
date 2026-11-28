#!/usr/bin/env python3
"""Find something to read about a National Register listing, by every road in turn, and say exactly what was found.
   python3 tools/form.py 85000942                       by its reference number (tools/gaps.py prints them)
   python3 tools/form.py 85000942 85001344 78001651     several at once
   python3 tools/form.py mo "Temple Block"              by state and part of the name
   python3 tools/form.py --ladder <address>             what to try when a page will not open
It never gives up at the first dead address. For each listing it tries, in this order:
  1. THE PARK SERVICE'S RECORD (npgallery.nps.gov/AssetDetail/NRIS/<number>). It is always there, and it is a source: the
     name, the street address, the architect or builder, the style, the significant years and the day of listing. A place
     can be written up from this and a look at the building, when the form itself cannot be read.
  2. THE PARK SERVICE'S FORM. Many are only a one-page placeholder ("has not yet been digitized"); the tool says so.
  3. THE STATE'S OWN COPY, at its present address. Missouri moved every form in 2025: the old addresses that web searches
     and Wikipedia still give (mostateparks.com/sites/mostateparks/files/..., dnr.mo.gov/shpo/nps-nr/...) answer 404, but
     the state's index (mostateparks.com/page/missouri-national-register-listings) links each form at its new one, with the
     address and the day of listing beside it. A scanned form is read by OCR where this machine has tesseract.
  4. WHAT ELSE TO TRY, when none of that gives a description: the ladder below.
The text of a form is kept in research/forms/<number>.txt; search that file, do not print it whole.
Two cautions. A listing is not proof that the building stands: many have been pulled down, and neither the record nor an
old form says so. Look at the pin on the aerial (tools/pincheck.py) and search the news for the name with "demolished".
And a listing that turns out gone, or to have nothing readable, is recorded so no session looks it up again:
   python3 tools/choose.py --skip <clone> <state> <number> gone|nosource|notwanted|onatlas "<why, or the Atlas id>"
The web fetch tool will not open web.archive.org, so an archived copy is not a road: do not spend time on it."""
import sys,os,re,json,html,subprocess,unicodedata
HERE=os.path.dirname(os.path.abspath(__file__)); W=os.path.dirname(HERE)
UA={'User-Agent':'lost-hidden-atlas-research/1.0'}
LABELS=['Title','National Register Information System ID','Applicable Criteria','Architectural Styles','Architects','Areas Of Significance','Periods Of Significance','Significant Years','Significant Names','Cultural Affiliations','Resource Type','Keywords','Note','Related Collections','Resource Format','File Size (bytes)','Date Published','Parks','Locations','Rating','Categories','Asset ID','Related Portals']

def _text(h): return re.sub(r'\s+',' ',html.unescape(re.sub(r'<[^>]+>',' ',h or ''))).strip()

def parse_record(h):
    """the labelled lines of the Park Service's record page, and the ids of the files it offers"""
    t=_text(h); out={}; pos=[]
    for l in LABELS:
        m=re.search(re.escape(l)+r'\s*:',t)
        if m: pos.append((m.start(),m.end(),l))
    pos.sort()
    for i,(a,b,l) in enumerate(pos):
        v=t[b:(pos[i+1][0] if i+1<len(pos) else b+300)].strip()
        if v and l not in out: out[l]=v[:400]
    out['assets']=list(dict.fromkeys(re.findall(r'GetAsset/([0-9a-f]{8}-[0-9a-f-]{27})',h or '')))
    return out

def placeholder(t):
    """the one-page stand-in for a form that was never scanned, or nothing at all"""
    t=(t or '').strip(); return len(t)<400 or ('not yet been digitized' in t and len(t)<1500)

ABBR={'co':'company','bldg':'building','bros':'brothers','st':'saint','ste':'sainte','mt':'mount','ft':'fort','rr':'railroad','ry':'railway','no':'number','ave':'avenue','hd':'historic district','apts':'apartments'}
def _words(name):
    s=unicodedata.normalize('NFKD',name or '').encode('ascii','ignore').decode().lower().replace("'",'')
    return frozenset(x for w in re.findall(r'[a-z0-9]+',s) for x in ABBR.get(w,w).split() if x not in ('the','and','of','a'))

def parse_mo_index(h):
    """Missouri's county pages: [{'name','slug','rest'}], rest being the address, town and day of listing"""
    out=[]
    for m in re.finditer(r'<a[^>]*href="(?:https://mostateparks\.com)?/media/pdf/([^"#?]+)"[^>]*>(.*?)</a>(.*?)(?=</p>|<br|<a |$)',h or '',re.S):
        n=_text(m.group(2))
        if n: out.append({'slug':m.group(1),'name':n,'rest':_text(m.group(3)).lstrip(', ')})
    return out

def find_in_index(ix,name):
    """the one listing of that name: the same words in any order ("Bixby, Walter E., House"), abbreviations spelled out.
    Failing that, the one listing that shares at least four fifths of its words; two that do, and it finds neither."""
    w=_words(name)
    if not w: return None
    same=[r for r in ix if _words(r['name'])==w]
    if same: return same[0]
    near=[r for r in ix if len(w)>=3 and len(w&_words(r['name']))/float(len(w|_words(r['name'])))>=0.8]
    return near[0] if len(near)==1 else None

def pdf_in_viewer(h):
    m=re.search(r'file=(https%3A%2F%2F[^"&]+\.pdf)',h or '') or re.search(r'(https://mostateparks\.com/sites/g/files/[^"\s]+\.pdf)',h or '')
    if not m: return None
    import urllib.parse; return urllib.parse.unquote(m.group(1))

def moved(u):
    """an address of Missouri's that died when the state moved its forms"""
    return bool(re.search(r'mostateparks\.com/sites/mostateparks/files/|dnr\.mo\.gov/shpo/',u or ''))

def unreachable(why):
    """the shell could not connect to the site at all (the network here lets few sites through), as against a page that answered 404 or 403"""
    return bool(re.search(r'ProxyError|Tunnel connection failed|Name or service not known|NameResolution|Temporary failure in name resolution|Max retries exceeded|Connection refused|ConnectionError|Connection reset|Network is unreachable|timed out|SSLError',str(why or ''),re.I))
def ladder(u,why=''):
    """what to try when a page will not open, in order. Never the Internet Archive through the web fetch tool: it is refused."""
    L=[]
    if unreachable(why):
        host=re.sub(r'^https?://([^/]+).*$',r'\1',u or '')
        L.append('The web fetch tool, first, with this same address: the shell here could not connect to %s at all, which says nothing about the page. The web fetch tool takes another road and reads most such sites (it did for ohio.edu, sah-archipedia.org, in.gov and others on November 28, 2026). Do not retry page.py for this site in this session.'%host)
    if re.search(r'npgallery\.nps\.gov|mostateparks\.com|dnr\.mo\.gov|nps-nr|national.register|/NRHP/',u or '',re.I) or moved(u):
        L.append('python3 tools/form.py <the listing\'s reference number>   (or: form.py <state> "<part of the name>"): the Park Service\'s record, its form, and the state\'s copy at its present address')
    L+=['The site\'s own search or front page: a 404 often means the page moved, not that it is gone. Fetch the front page with page.py --all and look for the section.',
        'A web search for the page\'s title in quotes: results often quote the page, or link a plain copy that page.py reads.',
        'Other sources for the same building: Clio (theclio.com, tours and entries), SAH Archipedia (sah-archipedia.org), the county historical society\'s tour page, the town\'s walking-tour PDF, nps.gov/places/<name>.htm, a Wikipedia category page for the county\'s buildings.',
        'The web fetch tool for a live page that refuses page.py (403). It will NOT open web.archive.org, and an unattended run cannot answer its approval prompt: try it once, then move on.',
        'If nothing gives a description: the Park Service\'s record alone (name, address, architect, years) plus a look at the building on the aerial is enough for a short entry. If even that fails, record it:  python3 tools/choose.py --skip <clone> <state> <number> nosource "<what you tried>"']
    return L

# ---------------------------------------------------------------- the network half
def _get(u,timeout=90):
    import requests
    for k in range(2):
        try: return requests.get(u,headers=UA,timeout=timeout)
        except Exception as e: err=e
    class R: status_code=0; content=b''; text=''
    R.err=str(err)[:80]; return R

def _pdf_text(b,path):
    """the text layer of a PDF; where there is none and this machine has tesseract, the first 14 pages by OCR"""
    open(path,'wb').write(b); t=''
    try: t=subprocess.run(['pdftotext','-layout',path,'-'],capture_output=True,text=True,timeout=180).stdout
    except Exception:
        try:
            import pypdf; t='\n'.join((p.extract_text() or '') for p in pypdf.PdfReader(path).pages)
        except Exception: t=''
    if len(t.strip())>=400: return t,'text layer'
    import shutil
    if not (shutil.which('tesseract') and shutil.which('pdftoppm')): return t,'a scan with no text layer (no OCR on this machine)'
    d=path+'.pp'; os.makedirs(d,exist_ok=True); out=[]
    try:
        subprocess.run(['pdftoppm','-r','150','-gray','-l','14','-png',path,os.path.join(d,'p')],timeout=300)
        for f in sorted(os.listdir(d)): out.append(subprocess.run(['tesseract',os.path.join(d,f),'-','--psm','4'],capture_output=True,text=True,timeout=120).stdout)
    except Exception: pass
    return '\n'.join(out),'read by OCR from a scan (first 14 pages; expect misread letters, check every date against the record)'

MO_PAGES=['page/national-register-listings/Adair-Franklin','basic-page/national-register-listings/Gasconade-Jackson','page/national-register-listings/Jasper-StFrancois','basic-page/national-register-listings/SteGenevieve-Wright','page/national-register-listings/STLCity-STLCounty']
def mo_index():
    f=os.path.join(W,'cache','forms','mo_index.json')
    if os.path.exists(f): return json.load(open(f,encoding='utf-8'))
    ix=[]; top=_get('https://mostateparks.com/page/missouri-national-register-listings')
    pages=list(dict.fromkeys(re.findall(r'href="/((?:basic-)?page/national-register-listings/[^"#]+)"',top.text or ''))) or MO_PAGES
    for p in pages:
        r=_get('https://mostateparks.com/'+p)
        if r.status_code==200: ix+=parse_mo_index(r.text)
    if len(ix)>500: os.makedirs(os.path.dirname(f),exist_ok=True); json.dump(ix,open(f,'w',encoding='utf-8'))
    return ix

def state_copy(st,name,ref,out):
    """the state's own copy of the form: (text, how, address) or (None, why, None)"""
    if st!='mo': return None,'no road to this state\'s own copies is written yet (Missouri only); add one to state_copy() in tools/form.py when you find where a state keeps them',None
    ix=mo_index()
    if not ix: return None,'Missouri\'s index did not answer (mostateparks.com/page/missouri-national-register-listings); try again in a few minutes',None
    e=find_in_index(ix,name)
    if not e: return None,'not found by name in Missouri\'s index of %d listings; open the county page and look by street address'%len(ix),None
    v=_get('https://mostateparks.com/media/pdf/'+e['slug']); u=pdf_in_viewer(v.text)
    if not u: return None,'Missouri lists it (%s) but its page gave no file'%e['rest'],'https://mostateparks.com/media/pdf/'+e['slug']
    r=_get(u,timeout=240)
    if r.status_code!=200 or r.content[:5]!=b'%PDF-': return None,'Missouri\'s file did not download (HTTP %s)'%r.status_code,u
    t,how=_pdf_text(r.content,os.path.join(out,ref+'_state.pdf'))
    return t,how+'; Missouri\'s index line: '+e['rest'],u

def look(ref,st=None,name=None):
    out=os.path.join(W,'research','forms'); os.makedirs(out,exist_ok=True); got=[]
    print('='*100); print('LISTING %s'%ref)
    r=_get('https://npgallery.nps.gov/AssetDetail/NRIS/'+ref); rec=parse_record(r.text) if r.status_code==200 else {}
    if rec.get('Title'):
        print('1. PARK SERVICE RECORD  https://npgallery.nps.gov/AssetDetail/NRIS/'+ref+'   (a source: cite it as the National Register record)')
        for l in ('Title','Note','Locations','Architects','Architectural Styles','Significant Years','Periods Of Significance','Areas Of Significance','Significant Names','Resource Type','Date Published'):
            if rec.get(l): print('     %-24s %s'%({'Note':'Address / note','Date Published':'Listed'}.get(l,l)+':',rec[l]))
        got.append('the record'); name=name or rec['Title']
        m=re.search(r'State:\s*([A-Za-z ]+?)\s+County',rec.get('Locations',''))
        if m and not st:
            sys.path.insert(0,HERE)
            try:
                from states import STATES; st=next((s['k'] for s in STATES if s['name'].lower()==m.group(1).strip().lower()),None)
            except Exception: pass
    elif r.status_code==200: print('1. PARK SERVICE RECORD: it has no record page for this number (listings of the last ten years or so often have none). The state\'s copy is the road for these.')
    else: print('1. PARK SERVICE RECORD: did not answer (HTTP %s). Try again; it is seldom down for long.'%r.status_code)
    txt=None
    for a in rec.get('assets',[])[:3]:
        p=_get('https://npgallery.nps.gov/GetAsset/'+a,timeout=240)
        if p.status_code==200 and p.content[:5]==b'%PDF-':
            t,how=_pdf_text(p.content,os.path.join(out,ref+'_nps_'+a[:8]+'.pdf'))
            if not placeholder(t): txt=(t,how,'https://npgallery.nps.gov/GetAsset/'+a); break
    if txt: print('2. PARK SERVICE FORM: read (%s), %d characters   %s'%(txt[1],len(txt[0]),txt[2])); got.append('the form (Park Service)')
    else: print('2. PARK SERVICE FORM: only the placeholder ("not yet digitized"), or no file. That is common and is not the end.')
    if not txt and st and name:
        t,how,u=state_copy(st,name,ref,out)
        if re.search(r'demolish|delist|razed|destroyed',how or '',re.I): print('   >>> THE STATE\'S INDEX SAYS IT IS GONE OR DELISTED: '+how.split('index line: ')[-1]+'   Do not write it up as standing. Set it aside:  python3 tools/choose.py --skip <clone> %s %s gone "<that line>"'%(st,ref))
        if t and not placeholder(t): txt=(t,how,u); print('3. STATE\'S COPY: read (%s), %d characters   %s'%(how,len(t),u)); got.append('the form (state copy)')
        else: print('3. STATE\'S COPY: %s%s'%(how,'   '+u if u else ''))
    elif not txt: print('3. STATE\'S COPY: not tried (the state or the name is not known; give them:  form.py <state> "<name>")')
    if txt:
        f=os.path.join(out,ref+'.txt'); open(f,'w',encoding='utf-8').write('SOURCE: %s\nHOW: %s\n\n%s'%(txt[2],txt[1],txt[0]))
        print('   kept in research/forms/%s.txt  Search it:  grep -n -i -E "built|erected|architect|brick|stone|stor(y|ies)|altered|present" research/forms/%s.txt | head -40'%(ref,ref))
        t1=re.sub(r'\s+',' ',txt[0]); m=re.search(r'(Describe the present and original|Narrative Description|7\.\s*Description)',t1); i=m.start() if m else max(t1.lower().find('description'),0); print('   it begins: '+t1[i:i+500])
    print('READ: '+(', '.join(got) if got else 'nothing')+'.')
    if 'the record' in got and not txt: print('The record alone gives the name, address, architect and years: enough for a short entry once you have LOOKED at the building (pincheck). For more, try:')
    if not txt:
        for i,l in enumerate(ladder('https://npgallery.nps.gov/')[1:],1): print('   %d. %s'%(i,l))
    print('Does it still stand? Neither the record nor the form says. Look at the pin on the aerial and search the news for "%s demolished".'%(name or ref))

if __name__=='__main__':
    a=sys.argv[1:]
    if not a: sys.exit(__doc__)
    os.chdir(W)
    if a[0]=='--ladder':
        for i,l in enumerate(ladder(a[1] if len(a)>1 else ''),1): print('%d. %s'%(i,l))
        sys.exit(0)
    if re.fullmatch(r'\d{8,9}',a[0]):
        for ref in a: look(ref)
        sys.exit(0)
    st=a[0].lower(); q=' '.join(a[1:]).lower(); f='cache/nrhp/%s.json'%st
    if not os.path.exists(f): subprocess.run([sys.executable,'tools/gaps.py',st],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
    if not os.path.exists(f): sys.exit('No Register list for "%s" here. Give a reference number instead.'%st)
    rows=[r for r in json.load(open(f,encoding='utf-8')) if q in r['n'].lower()]
    if not rows: sys.exit('No listing in %s has "%s" in its name. The Register writes a person\'s name surname first ("Long, R. A., House").'%(st.upper(),q))
    if len(rows)>4:
        print('%d listings match; give more of the name, or the number:'%len(rows))
        for r in rows[:30]: print('  %-10s %s, %s'%(r.get('ref',''),r['n'],r.get('town','')))
        sys.exit(0)
    for r in rows: look(r['ref'],st,r['n'])
