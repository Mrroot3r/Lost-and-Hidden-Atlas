#!/usr/bin/env python3
"""Read a web page as text and print the sentences that match a pattern.
   python3 tools/page.py [-n CHARS] [-g pattern] URL ...     (cached in research/pages/; the options may also follow the URL)
   python3 tools/page.py --all [-n CHARS] URL ...            the whole text in reading order, for a history page you
                                                             need to read through (default 12,000 characters: a Register
                                                             form's description is usually further in, so add -n 200000)
A PDF (a National Register form, a county walking-tour guide) is read too: its text layer is pulled out and treated
like a page. A PDF that is only scanned pictures has no text layer; the tool says so, and then there is nothing to
read without OCR (say "form is a scan, not read" and use another source).
A page that will not open (refused, timed out, 403, 404) is looked for in the Internet Archive, and the newest copy kept
there is read instead, under a line saying ARCHIVED COPY and its date (or, where this machine is not let through to the
archive, the tool says so; the web fetch tool will not open web.archive.org either). Whenever a page will not open the tool
prints WHAT TO TRY NEXT (tools/form.py --ladder): never stop at the archive. Hours, fees and rules taken from an archived copy
must be written with that date ("as of an archived copy of March 2024"), because they may have changed.
A page that is drawn by script comes back nearly empty; the tool says so. Then search the web for the page's own words
limited to that site: search results often link a plain copy of the same page that this tool can read."""
import sys,re,os,hashlib,html,requests
a=sys.argv[1:]; N=1500; ALL='--all' in a
if ALL: a.remove('--all'); N=12000
DEFAULT=r'hours|fee|admission|open |closed|parking|trail|mile|permit|gate|daily|season|free|access|road|owned|managed|private|ruin|remain'
pat=DEFAULT; rest=[]
while a:                                  # -n and -g may come before or after the addresses (after them they used to be read as addresses)
    if a[0] in('-n','-g') and len(a)>1:
        if a[0]=='-n': N=int(a[1])
        else: pat=a[1]
        a=a[2:]
    else: rest.append(a.pop(0))
a=rest
DAYTIME=re.compile(r'\b(mon|tues?|wed(nes)?|thu(rs)?|fri|sat(ur)?|sun)(day)?s?\b|\b\d{1,2}(:\d\d)?\s*(a\.?m\.?|p\.?m\.?|noon)',re.I)
ABBR=re.compile(r'(?:\b(?:a\.m|p\.m|No|Nos|St|Ste|Mt|Ft|Dr|Mr|Mrs|Jr|Sr|Ave|Rd|Co|Inc|vs|etc|U\.S|ca|approx)|\b[A-Z])\.$')
def sentences(t):
    """Split text into sentences, but not after a.m., p.m., No., St. and the like when a small letter or a digit follows,
    nor after a single capital (an initial): "9 a.m. to 5 p.m.", "Lock No. 1", "Charles E. Smith" stay whole."""
    out=[]
    for piece in re.split(r'(?<=[.!?])\s+',t):
        if out and ABBR.search(out[-1]) and (re.match(r'[a-z0-9]',piece) or re.search(r'\b[A-Z]\.$',out[-1])): out[-1]+=' '+piece
        else: out.append(piece)
    return out
os.makedirs('research/pages',exist_ok=True)
def nexts(u):
    """a page would not open: say what to try next, so nobody stops here (tools/form.py holds the list)"""
    try:
        sys.path.insert(0,os.path.dirname(os.path.abspath(__file__))); import form
        if form.moved(u): print('   MISSOURI MOVED ITS REGISTER FORMS in 2025; this old address is dead but the form is very likely online. Run  python3 tools/form.py mo "<part of the listing\'s name>"  (or with its reference number).')
        print('   WHAT TO TRY NEXT, in order:')
        for i,l in enumerate(form.ladder(u),1): print('   %d. %s'%(i,l))
    except Exception: pass
def archived(u,why):
    """The newest copy the Internet Archive holds of a page that would not open, or None."""
    try:
        j=requests.get('https://archive.org/wayback/available',params={'url':u},timeout=40).json().get('archived_snapshots',{}).get('closest')
        if not j or not j.get('available'): return None
        ts=j['timestamp']; day='%s-%s-%s'%(ts[:4],ts[4:6],ts[6:8]); r=None
        try: r=requests.get('https://web.archive.org/web/%sid_/%s'%(ts,u),headers=UA,timeout=90)
        except Exception: pass
        if r is None or r.status_code!=200:          # this machine may not be let through to the archive; the web fetch tool usually is
            print('##',u,'->',why+'. The Internet Archive holds a copy of '+day+' that this machine is not let through to (https://web.archive.org/web/%s/%s), and the web fetch tool will not open web.archive.org either: do not spend time on it.'%(ts,u)); nexts(u); return ''
        print('##',u,'->',why+'. Reading the ARCHIVED COPY of %s-%s-%s instead: give that date with any hours, fees or rules you take from it.'%(ts[:4],ts[4:6],ts[6:8]))
        return pdf_text(r.content,u) if r.content[:5]==b'%PDF-' else '<!-- archived copy of %s -->'%ts+r.text
    except Exception: return None
def pdf_text(b,u):
    """The text layer of a PDF as simple HTML paragraphs (so the rest of the tool treats it like a page)."""
    import io,subprocess,tempfile
    txt=''; title=''
    try:
        from pypdf import PdfReader
        rd=PdfReader(io.BytesIO(b)); txt='\n\n'.join((pg.extract_text() or '') for pg in rd.pages); n=len(rd.pages)
        try: title=str((rd.metadata or {}).get('/Title') or '')
        except Exception: pass
    except Exception:
        n='?'
        try:
            with tempfile.NamedTemporaryFile(suffix='.pdf') as f:
                f.write(b); f.flush(); txt=subprocess.run(['pdftotext','-layout',f.name,'-'],capture_output=True,timeout=120).stdout.decode('utf-8','ignore')
        except Exception as e: print('##',u,'-> a PDF, and neither pypdf nor pdftotext could read it (pip install --break-system-packages pypdf):',str(e)[:60])
    if 'placeholder' in (title+' '+txt[:400]).lower(): print('##',u,'-> NPGallery\'s one-page PLACEHOLDER, not the form (its title is "%s"): the form itself is not on line there. Do not try other addresses for it; use another source.'%(title or 'placeholder'))
    elif len(re.sub(r'\s+','',txt))<200: print('##',u,f'-> a PDF of {n} page(s) with NO TEXT LAYER (a scan). Nothing to read here without OCR: use another source and say the form was not read.')
    else: print('##',u,f'-> PDF, {n} page(s), text layer read')
    txt=re.sub(r'-\n(?=[a-z])','',txt)
    return '<p>'+html.escape(re.sub(r'(?<!\n)\n(?!\n)',' ',txt)).replace('\n\n','</p><p>')+'</p>'
UA={'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) lost-hidden-atlas-research/1.0'}
for u in a:
    p='research/pages/'+hashlib.md5(u.encode()).hexdigest()[:12]+'.html'
    if os.path.exists(p): t=open(p,encoding='utf-8',errors='ignore').read()
    else:
        t=None; why=''
        try:
            r=requests.get(u,headers=UA,timeout=90)
            if r.status_code==200 and r.content[:8].startswith((b'\x89PNG',b'\xff\xd8\xff',b'GIF8')):      # a picture, not a page: NPGallery's _text route answers a small PNG (about 893 bytes) for a listing it has no text for
                print('##',u,'-> a PICTURE (%d bytes), not text: there is nothing to read at this address.%s'%(len(r.content),' NPGallery serves this small image for a listing whose form it has no text for (often those numbered 100...): count the form as not read this way and look for the state\'s own copy or another source.' if 'npgallery' in u else ''))
                print(); continue
            if r.status_code==200: t=pdf_text(r.content,u) if r.content[:5]==b'%PDF-' else r.text
            else: why='HTTP %d'%r.status_code
        except Exception as e: why='ERROR '+str(e)[:90]
        if t is None:
            t=archived(u,why)
            if t is None: print('##',u,'->',why,'and no archived copy was found'); nexts(u); print(); continue
            if t=='': print(); continue
        open(p,'w',encoding='utf-8').write(t)
    m=re.match(r'<!-- archived copy of (\d{8})',t); raw=t
    if m and os.path.exists(p) and not ALL: print('## (archived copy of %s-%s-%s, not the live page)'%(m.group(1)[:4],m.group(1)[4:6],m.group(1)[6:8]))
    t=re.sub(r'(?is)<(script|style|noscript|svg|nav|footer|header)[^>]*>.*?</\1>',' ',t)
    t=re.sub(r'(?i)<(br|/p|/div|/li|/h\d|/tr)[^>]*>','. ',t); t=html.unescape(re.sub(r'<[^>]+>',' ',t)); t=re.sub(r'\s+',' ',t)
    if len(t)<600 and raw.lower().count('<script')>=3: print('##',u,'-> this page is DRAWN BY SCRIPT: only %d characters of text came back ("%s"). Search the web for its title limited to this site and read the plain copy a result links to, or use another source.'%(len(t),t.strip()[:80]))
    if ALL: print('##',u,f'({len(t)} chars of text)\n'+t[:N]+('\n[... %d more characters; raise -n to see them]'%(len(t)-N) if len(t)>N else '')+'\n'); continue
    sents=[s.strip(' .') for s in sentences(t)]; seen=set(); out=[]; used=0
    short=lambda x:len(x)<25 and not (pat==DEFAULT and len(x)>=6 and DAYTIME.search(x))      # with the default pattern a short line with a day or a clock time ("Monday 9 a.m.-5 p.m.") is kept
    keep=lambda x:re.search(pat,x,re.I) or (pat==DEFAULT and DAYTIME.search(x))
    for s in sents:
        if short(s) or len(s)>420 or s in seen or not keep(s): continue
        seen.add(s)
        if used+len(s)>N: break
        out.append(' - '+s); used+=len(s)
    cut=used+sum(len(x) for x in sents if x not in seen and not short(x) and len(x)<=420 and keep(x))>N
    print('##',u,f'({len(t)} chars of text)\n'+'\n'.join(out)+('\n[CUT SHORT at %d characters of matching sentences: more of them follow. Raise -n (for a long form, -n 200000), or read the kept copy in research/pages/.]'%N if cut else '')+'\n')
