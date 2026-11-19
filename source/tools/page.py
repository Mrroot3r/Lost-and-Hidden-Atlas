#!/usr/bin/env python3
"""Read a web page as text and print the sentences that match a pattern.
   python3 tools/page.py [-n CHARS] [-g pattern] URL ...     (cached in research/pages/)
   python3 tools/page.py --all [-n CHARS] URL ...            the whole text in reading order, for a history page you
                                                             need to read through (default 12,000 characters: a Register
                                                             form's description is usually further in, so add -n 200000)
A PDF (a National Register form, a county walking-tour guide) is read too: its text layer is pulled out and treated
like a page. A PDF that is only scanned pictures has no text layer; the tool says so, and then there is nothing to
read without OCR (say "form is a scan, not read" and use another source).
A page that will not open (refused, timed out, 403, 404) is looked for in the Internet Archive, and the newest copy kept
there is read instead, under a line saying ARCHIVED COPY and its date (or, where this machine is not let through to the
archive, the tool prints the address of that copy to open with the web fetch tool). Hours, fees and rules taken from an archived copy
must be written with that date ("as of an archived copy of March 2024"), because they may have changed.
A page that is drawn by script comes back nearly empty; the tool says so. Then search the web for the page's own words
limited to that site: search results often link a plain copy of the same page that this tool can read."""
import sys,re,os,hashlib,html,requests
a=sys.argv[1:]; N=1500; ALL='--all' in a
if ALL: a.remove('--all'); N=12000
pat=r'hours|fee|admission|open |closed|parking|trail|mile|permit|gate|daily|season|free|access|road|owned|managed|private|ruin|remain'
while a and a[0] in('-n','-g'):
    if a[0]=='-n': N=int(a[1])
    else: pat=a[1]
    a=a[2:]
os.makedirs('research/pages',exist_ok=True)
def archived(u,why):
    """The newest copy the Internet Archive holds of a page that would not open, or None."""
    try:
        j=requests.get('https://archive.org/wayback/available',params={'url':u},timeout=40).json().get('archived_snapshots',{}).get('closest')
        if not j or not j.get('available'): return None
        ts=j['timestamp']; day='%s-%s-%s'%(ts[:4],ts[4:6],ts[6:8]); r=None
        try: r=requests.get('https://web.archive.org/web/%sid_/%s'%(ts,u),headers=UA,timeout=90)
        except Exception: pass
        if r is None or r.status_code!=200:          # this machine may not be let through to the archive; the web fetch tool usually is
            print('##',u,'->',why+'. The Internet Archive holds a copy of '+day+' that this tool could not fetch: open  https://web.archive.org/web/%s/%s  with the web fetch tool, and give that date with any hours, fees or rules you take from it.'%(ts,u)); return ''
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
            if r.status_code==200: t=pdf_text(r.content,u) if r.content[:5]==b'%PDF-' else r.text
            else: why='HTTP %d'%r.status_code
        except Exception as e: why='ERROR '+str(e)[:90]
        if t is None:
            t=archived(u,why)
            if t is None: print('##',u,'->',why,'and no archived copy was found\n'); continue
            if t=='': print(); continue
        open(p,'w',encoding='utf-8').write(t)
    m=re.match(r'<!-- archived copy of (\d{8})',t); raw=t
    if m and os.path.exists(p) and not ALL: print('## (archived copy of %s-%s-%s, not the live page)'%(m.group(1)[:4],m.group(1)[4:6],m.group(1)[6:8]))
    t=re.sub(r'(?is)<(script|style|noscript|svg|nav|footer|header)[^>]*>.*?</\1>',' ',t)
    t=re.sub(r'(?i)<(br|/p|/div|/li|/h\d|/tr)[^>]*>','. ',t); t=html.unescape(re.sub(r'<[^>]+>',' ',t)); t=re.sub(r'\s+',' ',t)
    if len(t)<600 and raw.lower().count('<script')>=3: print('##',u,'-> this page is DRAWN BY SCRIPT: only %d characters of text came back ("%s"). Search the web for its title limited to this site and read the plain copy a result links to, or use another source.'%(len(t),t.strip()[:80]))
    if ALL: print('##',u,f'({len(t)} chars of text)\n'+t[:N]+('\n[... %d more characters; raise -n to see them]'%(len(t)-N) if len(t)>N else '')+'\n'); continue
    sents=[s.strip(' .') for s in re.split(r'(?<=[.!?])\s+',t)]; seen=set(); out=[]; used=0
    for s in sents:
        if len(s)<25 or len(s)>420 or s in seen or not re.search(pat,s,re.I): continue
        seen.add(s)
        if used+len(s)>N: break
        out.append(' - '+s); used+=len(s)
    print('##',u,f'({len(t)} chars of text)\n'+'\n'.join(out)+'\n')
