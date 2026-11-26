#!/usr/bin/env python3
"""The tidy job: fold what research sessions left in notes/<batch key>.md into the shared files. ONE session does it,
working alone, and it is the only kind of session that edits GUIDE.md and LEADS.md for research (GUIDE.md section 6).

   python3 tools/tidy.py <clone>                      what is waiting, and the steps, in order
   python3 tools/tidy.py <clone> --leads              move every lead row out of the notes into LEADS.md
   python3 tools/tidy.py <clone> --done [key ...]     when the tips are written into the guide: take them out of the notes
                                                      (every waiting note, or only the keys given) and mark the notes tidied

Why it exists: sessions run side by side, so each writes only its own note. tools/start.py reads the notes, but it prints
at most fourteen tips, the newest first, so a tip in an old note is soon never read again. The tidy job moves what is worth
keeping to where every later session will find it:
   leads   -> LEADS.md, one list (start.py already searches it by place)
   tips    -> GUIDE.md section 16, under "Every state" or the state's own heading (start.py prints those two lists);
              a site that will not open goes in the table in section 3; a tip that is really a fault in a tool is fixed
              in the tool, or written into its usage text, and not copied anywhere
   "What this batch is" stays in the note. start.py shows it to the next session in that state. Only the table in GUIDE.md
              section 8 needs its "Places so far" cell brought up to date for the states the notes cover.
Run it from the working folder (it reads build/sites.json), after publish.sh has made a branch in the clone."""
import sys,os,re,json,glob,math,datetime
a=sys.argv[1:]
if not a or a[0].startswith('-'): sys.exit(__doc__)
clone=a[0]; mode=a[1] if len(a)>1 else ''; keys=a[2:]
NOTES=os.path.join(clone,'notes'); LEADS=os.path.join(clone,'LEADS.md'); GUIDE=os.path.join(clone,'GUIDE.md')
if not os.path.isdir(NOTES) or not os.path.exists(LEADS): sys.exit('That is not a clone of the repository: no notes/ folder or no LEADS.md in '+clone)
TODAY=os.environ.get('TIDY_DATE') or datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d')
HEAD_ROW='| Place | Where | What is known | What is missing |'
def sec_span(t,name):
    """(start of body, end of body) of the section '## name' in a note, or None."""
    m=re.search(r'^## '+re.escape(name)+r'[^\n]*\n',t,re.M)
    if not m: return None
    n=re.search(r'^## ',t[m.end():],re.M); return m.end(),(m.end()+n.start() if n else len(t))
def read(path):
    t=open(path,encoding='utf-8').read(); head=t.split('\n## ')[0]
    get=lambda k:(re.search(r'^'+k+r':\s*(.*)$',head,re.M) or [None,''])[1].strip()
    body=lambda name:(lambda s:t[s[0]:s[1]] if s else '')(sec_span(t,name))
    leads=[l for l in body('Leads').split('\n') if l.startswith('|') and not l.startswith('| Place') and not l.startswith('|---') and not l.startswith('| Example mill')]
    tips=[]
    for l in body('Tips').split('\n'):                    # a tip may run over several lines: a line that does not start a new one is joined on
        if l.strip().startswith('- '): tips.append(l.strip())
        elif tips and l.strip() and not l.startswith('#'): tips[-1]+=' '+l.strip()
    tips=[x for x in tips if 'Delete this bracketed text' not in x and x.lower().rstrip('.') not in('- none','- nothing')]
    return {'key':os.path.basename(path)[:-3],'path':path,'text':t,'state':get('state'),'region':get('region'),'date':get('date'),'places':get('places'),'tidied':get('tidied'),'leads':leads,'tips':tips}
notes=[read(f) for f in sorted(glob.glob(os.path.join(NOTES,'*.md'))) if os.path.basename(f)!='README.md']
waiting=[n for n in notes if n['leads'] or n['tips'] or not n['tidied']]
norm=lambda s:re.sub(r'[^a-z0-9]+',' ',s.lower()).strip()
first=lambda row:row.split('|')[1].strip() if row.count('|')>=2 else row
def lead_rows(): return [l.rstrip('\n') for l in open(LEADS,encoding='utf-8') if l.startswith('|') and not l.startswith('| Place') and not l.startswith('|---')]

if mode=='--leads':
    have={norm(first(r)) for r in lead_rows()}; add=[]; skipped=[]
    for n in notes:
        for r in n['leads']:
            k=norm(first(r))
            if k in have: skipped.append((n['key'],first(r),r.strip()))
            else: have.add(k); add.append(r.strip())
    if add:
        t=open(LEADS,encoding='utf-8').read()
        open(LEADS,'w',encoding='utf-8').write(t+('' if t.endswith('\n') else '\n')+'\n'.join(add)+'\n')
    for n in notes:
        if not n['leads']: continue
        s=sec_span(n['text'],'Leads')
        t=n['text'][:s[0]]+'Moved to `LEADS.md` on '+TODAY+' by the tidy job ('+str(len(n['leads']))+(' rows' if len(n['leads'])!=1 else ' row')+'). New leads for this ground go in the note of the batch that finds them.\n\n'+HEAD_ROW+'\n|---|---|---|---|\n\n'+n['text'][s[1]:]
        open(n['path'],'w',encoding='utf-8').write(t)
    print('%d lead row(s) moved into LEADS.md from %d note(s).'%(len(add),sum(1 for n in notes if n['leads'])))
    for k,nm,row in skipped: print('  not copied, LEADS.md already has a row of that name: %s (from notes/%s.md). Compare the two and keep the fuller in LEADS.md; a place of the same name in another town is another place: add it. The note\'s row (the note no longer holds it):\n    %s'%(nm,k,row))
    print('Next: the tips. Run  python3 tools/tidy.py %s  again for the list.'%clone); sys.exit(0)

if mode=='--done':
    pick=[n for n in notes if (n['key'] in keys if keys else (n['tips'] or not n['tidied']))]
    miss=[k for k in keys if k not in {n['key'] for n in notes}]
    if miss: sys.exit('No such note: '+', '.join(miss))
    left=[n['key'] for n in pick if n['leads']]
    if left: sys.exit('These notes still hold lead rows: '+', '.join(left)+'. Run  python3 tools/tidy.py %s --leads  first.'%clone)
    for n in pick:
        t=n['text']; s=sec_span(t,'Tips')
        if s and n['tips']: t=t[:s[0]]+'Folded into `GUIDE.md` and the tools on '+TODAY+' by the tidy job ('+str(len(n['tips']))+(' tips' if len(n['tips'])!=1 else ' tip')+').\n'+t[s[1]:]
        if not n['tidied']: t=re.sub(r'^(file:[^\n]*\n)',lambda m:m.group(1)+'tidied: '+TODAY+'\n',t,count=1,flags=re.M) if re.search(r'^file:',t,re.M) else t.replace('\n','\ntidied: '+TODAY+'\n',1)
        open(n['path'],'w',encoding='utf-8').write(t)
    print('%d note(s) marked tidied: %s'%(len(pick),', '.join(n['key'] for n in pick) or 'none'))
    print('Now: git -C %s add -A, commit (say what you folded in, what you dropped and why), push, open ONE pull request, stop.'%clone); sys.exit(0)

if mode: sys.exit('Unknown option '+mode+'\n\n'+__doc__)

# ---------------- the report ----------------
S=[]
for p in ('build/sites.json',os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','build','sites.json')):
    if os.path.exists(p): S=json.load(open(p)); break
print('== Notes: %d in all, %d waiting for the tidy job'%(len(notes),len(waiting)))
for n in waiting: print('  %-22s %-12s %-28s %2d lead row(s), %2d tip(s)%s'%(n['key'],n['date'],n['state'][:28],len(n['leads']),len(n['tips']),'' if n['tidied'] else ', table row not yet brought up to date'))
if not waiting: print('  Nothing to do.'); sys.exit(0)

nl=sum(len(n['leads']) for n in notes)
print('\n== Step 1. Leads: %d row(s) in the notes'%nl)
print('  python3 tools/tidy.py %s --leads     moves them into LEADS.md and empties the tables in the notes.'%clone if nl else '  None waiting.')
# rows that look as if their place has since been added
def near(row):
    out=[]
    for m in re.finditer(r'(-?\d{2}\.\d{3,}),\s*(-\d{2,3}\.\d{3,})',row):
        la,lo=float(m.group(1)),float(m.group(2))
        for s in S:
            d=math.hypot((s['lat']-la)*111320,(s['lon']-lo)*111320*math.cos(math.radians(la)))
            if d<=150: out.append((d,s))
    nm=norm(first(row)); nw=nm.split(); whole=' '+norm(row)+' '
    if len(nm)>=8:
        for s in S:
            sn=norm(s['name']); sw=sn.split()
            if (' '+norm(s.get('town') or '')+' ') not in whole: continue          # the same name in another town is another place (Electric Park, Forest Park)
            short,long_=(sn,nm) if len(sw)<=len(nw) else (nm,sn)                 # one name inside the other, as whole words in a row:
            if sn==nm or (short.count(' ')>=1 and len(short)>=10 and (' '+short+' ') in (' '+long_+' ')): out.append((-1,s))      # "red bridge" is not in "covered bridge"
    seen=set(); res=[]
    for d,s in sorted(out,key=lambda x:x[0]):
        if s['id'] not in seen: seen.add(s['id']); res.append((d,s))
    return res[:2]
if S:
    hits=[]
    for src,rows in [('LEADS.md',lead_rows())]+[('notes/'+n['key']+'.md',n['leads']) for n in notes]:
        for r in rows:
            h=near(r)
            if h: hits.append((src,first(r),h))
    print('  Rows that may already be on the map (a place of the same name in the same town, or one within 150 m of the row\'s coordinate): %d'%len(hits))
    for src,nm,h in hits[:40]: print('    %s: "%s"  ~  %s'%(src,nm[:60],'; '.join('%s (%s)'%(s['id'],'same name' if d<0 else '%d m'%d) for d,s in h)))
    if hits: print('  Open each: if the place was added, delete the row; if it is a different thing close by, leave it.')
else: print('  (build/sites.json not found: run this from the working folder to have the rows checked against the map)')

nt=sum(len(n['tips']) for n in waiting)
print('\n== Step 2. Tips: %d, from %d note(s). Decide for each one, then write it where it belongs'%(nt,sum(1 for n in waiting if n['tips'])))
print('''  - A source that works, or a way of reading one: GUIDE.md section 16, under "### Every state" if it holds anywhere,
    else under the state's own "### <State>" heading (add the heading, in alphabetical order, if it is not there).
    One line each, able to stand alone, with the address pattern or the command in it. Merge tips that say the same thing.
  - A site that will not open: a row in the table in GUIDE.md section 3, "What a cloud session usually cannot reach".
  - A fault in a tool, or something its usage text should have said: fix the tool or its text, run its test, and do not
    copy the tip. If the fix is more than small, write the tip under "Every state" and say so in the pull request.
  - True only of one batch's ground, already in the guide, or something you cannot make sense of: leave it out, and list it
    in the pull request as dropped, with the reason.
  Do not reword a tip into something its note did not say, and do not add tips of your own here.''')
g=open(GUIDE,encoding='utf-8').read() if os.path.exists(GUIDE) else ''
m=re.search(r'^## 16\.[^\n]*\n(.*?)(?=^## \d|\Z)',g,re.M|re.S)
heads=re.findall(r'^### (.+)$',m.group(1),re.M) if m else []
print('  Headings in section 16 now: '+(', '.join(heads) if heads else 'none (the section is missing: add "## 16. What research sessions have learned" at the end of GUIDE.md)'))
by={}
for n in waiting:
    for t in n['tips']: by.setdefault(n['state'] or '?',[]).append((n['key'],t))
for st in sorted(by):
    print('  --- '+st)
    for k,t in by[st]: print('    [%s] %s'%(k,t))

st_notes={}
for n in waiting:
    if n['tidied']: continue
    for st in [x.strip() for x in n['state'].split(',') if x.strip()]: st_notes.setdefault(st,[]).append(n)
print('\n== Step 3. The table in GUIDE.md section 8: bring the "Places so far" cell up to date for %d state(s)'%len(st_notes))
if st_notes:
    try:
        sys.path.insert(0,os.path.dirname(os.path.abspath(__file__))); from states import STATES
        regs={s['name']:[c for c,l in s['regions']] for s in STATES}
    except Exception: regs={}
    for st in sorted(st_notes):
        cnt={}
        for s in S:
            if s.get('reg') in regs.get(st,[]): cnt[s['reg']]=cnt.get(s['reg'],0)+1
        row=next((l for l in g.split('\n') if l.startswith('| '+st+' |')),None)
        print('  %s: %d place(s) on the map now%s. Note(s): %s. %s'%(st,sum(cnt.values()),(' ('+', '.join('%s %d'%(k,v) for k,v in sorted(cnt.items()))+')') if len(cnt)>1 else '',', '.join('notes/%s.md (%s places, region %s)'%(n['key'],n['places'],n['region']) for n in st_notes[st]),
              'It has its own row.' if row else 'It has no row of its own: it is counted in "The other ... states"; give it a row and lower that count.'))
    print('  Keep a cell short: how many places, which parts of the state, and "see notes/<key>.md". The detail is in the notes.')
print('\n== Step 4. When the tips are written and the table is right')
print('  python3 tools/tidy.py %s --done      takes the tips out of the notes and marks the notes tidied.'%clone)
print('  Then one pull request. In it: how many leads moved, where each kept tip went, and each tip dropped and why.')
