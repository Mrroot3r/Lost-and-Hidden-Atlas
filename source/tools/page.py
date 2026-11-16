#!/usr/bin/env python3
"""Read a web page as text and print the sentences that match a pattern.
   python3 tools/page.py [-n CHARS] [-g pattern] URL ...     (cached in research/pages/)"""
import sys,re,os,hashlib,html,requests
a=sys.argv[1:]; N=1500; pat=r'hours|fee|admission|open |closed|parking|trail|mile|permit|gate|daily|season|free|access|road|owned|managed|private|ruin|remain'
while a and a[0] in('-n','-g'):
    if a[0]=='-n': N=int(a[1])
    else: pat=a[1]
    a=a[2:]
os.makedirs('research/pages',exist_ok=True)
UA={'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) lost-hidden-atlas-research/1.0'}
for u in a:
    p='research/pages/'+hashlib.md5(u.encode()).hexdigest()[:12]+'.html'
    if os.path.exists(p): t=open(p,encoding='utf-8',errors='ignore').read()
    else:
        try:
            r=requests.get(u,headers=UA,timeout=45); t=r.text
            if r.status_code!=200: print('##',u,'-> HTTP',r.status_code,'\n'); continue
            open(p,'w',encoding='utf-8').write(t)
        except Exception as e: print('##',u,'-> ERROR',str(e)[:90],'\n'); continue
    t=re.sub(r'(?is)<(script|style|noscript|svg|nav|footer|header)[^>]*>.*?</\1>',' ',t)
    t=re.sub(r'(?i)<(br|/p|/div|/li|/h\d|/tr)[^>]*>','. ',t); t=html.unescape(re.sub(r'<[^>]+>',' ',t)); t=re.sub(r'\s+',' ',t)
    sents=[s.strip(' .') for s in re.split(r'(?<=[.!?])\s+',t)]; seen=set(); out=[]; used=0
    for s in sents:
        if len(s)<25 or len(s)>420 or s in seen or not re.search(pat,s,re.I): continue
        seen.add(s)
        if used+len(s)>N: break
        out.append(' - '+s); used+=len(s)
    print('##',u,f'({len(t)} chars of text)\n'+'\n'.join(out)+'\n')
