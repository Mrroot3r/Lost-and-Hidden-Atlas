#!/usr/bin/env python3
"""Read a web page as text and print the sentences that match a pattern.
   python3 tools/page.py [-n CHARS] [-g pattern] URL ...     (cached in research/pages/)
   python3 tools/page.py --all [-n CHARS] URL ...            the whole text in reading order, for a history page you
                                                             need to read through (default 12,000 characters)
A PDF (a National Register form, a county walking-tour guide) is read too: its text layer is pulled out and treated
like a page. A PDF that is only scanned pictures has no text layer; the tool says so, and then there is nothing to
read without OCR (say "form is a scan, not read" and use another source)."""
import sys,re,os,hashlib,html,requests
a=sys.argv[1:]; N=1500; ALL='--all' in a
if ALL: a.remove('--all'); N=12000
pat=r'hours|fee|admission|open |closed|parking|trail|mile|permit|gate|daily|season|free|access|road|owned|managed|private|ruin|remain'
while a and a[0] in('-n','-g'):
    if a[0]=='-n': N=int(a[1])
    else: pat=a[1]
    a=a[2:]
os.makedirs('research/pages',exist_ok=True)
def pdf_text(b,u):
    """The text layer of a PDF as simple HTML paragraphs (so the rest of the tool treats it like a page)."""
    import io,subprocess,tempfile
    txt=''
    try:
        from pypdf import PdfReader
        rd=PdfReader(io.BytesIO(b)); txt='\n\n'.join((pg.extract_text() or '') for pg in rd.pages); n=len(rd.pages)
    except Exception:
        n='?'
        try:
            with tempfile.NamedTemporaryFile(suffix='.pdf') as f:
                f.write(b); f.flush(); txt=subprocess.run(['pdftotext','-layout',f.name,'-'],capture_output=True,timeout=120).stdout.decode('utf-8','ignore')
        except Exception as e: print('##',u,'-> a PDF, and neither pypdf nor pdftotext could read it (pip install --break-system-packages pypdf):',str(e)[:60])
    if len(re.sub(r'\s+','',txt))<200: print('##',u,f'-> a PDF of {n} page(s) with NO TEXT LAYER (a scan). Nothing to read here without OCR: use another source and say the form was not read.')
    else: print('##',u,f'-> PDF, {n} page(s), text layer read')
    txt=re.sub(r'-\n(?=[a-z])','',txt)
    return '<p>'+html.escape(re.sub(r'(?<!\n)\n(?!\n)',' ',txt)).replace('\n\n','</p><p>')+'</p>'
UA={'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) lost-hidden-atlas-research/1.0'}
for u in a:
    p='research/pages/'+hashlib.md5(u.encode()).hexdigest()[:12]+'.html'
    if os.path.exists(p): t=open(p,encoding='utf-8',errors='ignore').read()
    else:
        try:
            r=requests.get(u,headers=UA,timeout=90); t=r.text
            if r.status_code!=200: print('##',u,'-> HTTP',r.status_code,'\n'); continue
            if r.content[:5]==b'%PDF-': t=pdf_text(r.content,u)
            open(p,'w',encoding='utf-8').write(t)
        except Exception as e: print('##',u,'-> ERROR',str(e)[:90],'\n'); continue
    t=re.sub(r'(?is)<(script|style|noscript|svg|nav|footer|header)[^>]*>.*?</\1>',' ',t)
    t=re.sub(r'(?i)<(br|/p|/div|/li|/h\d|/tr)[^>]*>','. ',t); t=html.unescape(re.sub(r'<[^>]+>',' ',t)); t=re.sub(r'\s+',' ',t)
    if ALL: print('##',u,f'({len(t)} chars of text)\n'+t[:N]+('\n[... %d more characters; raise -n to see them]'%(len(t)-N) if len(t)>N else '')+'\n'); continue
    sents=[s.strip(' .') for s in re.split(r'(?<=[.!?])\s+',t)]; seen=set(); out=[]; used=0
    for s in sents:
        if len(s)<25 or len(s)>420 or s in seen or not re.search(pat,s,re.I): continue
        seen.add(s)
        if used+len(s)>N: break
        out.append(' - '+s); used+=len(s)
    print('##',u,f'({len(t)} chars of text)\n'+'\n'.join(out)+'\n')
