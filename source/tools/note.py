#!/usr/bin/env python3
"""Make the note file for a batch: the one place a research session writes about its work.
   python3 tools/note.py <batch key> [clone]      writes <clone>/notes/<batch key>.md and prints its path
Run it AFTER publish.sh has made the branch, then fill the file in. A session does not edit GUIDE.md, LEADS.md or
PROMPTS.md: several sessions run at once, each used to add its lines at the same spots in those files, and every pull
request after the first then had to be untangled by hand. A file of your own cannot collide with anybody's.
The note has three parts:
   What this batch is    what you added, how the sources were read, and what was NOT checked (it used to be a line in
                         GUIDE.md section 10 and a row in section 8)
   Leads                 places you read about and could not finish, as table rows (they used to go in LEADS.md)
   Tips                  anything about a tool, a source or the guide that the next session should know (they used to be
                         edits to GUIDE.md)
tools/start.py prints the notes, leads and tips that bear on a piece of ground, so the next session does read them."""
import sys,os,json,importlib,glob,datetime
HERE=os.path.dirname(os.path.abspath(__file__)); W=os.path.dirname(HERE); sys.path.insert(0,HERE)
if len(sys.argv)<2: sys.exit(__doc__)
def make(key,clone,quiet=False):
    mod=None
    for f in glob.glob(os.path.join(HERE,'data_*.py')):
        if os.path.basename(f) in('data_a.py','data_b.py'): continue
        m=importlib.import_module(os.path.basename(f)[:-3])
        if getattr(m,'BATCH',{}).get('key')==key: mod=m; break
    if not mod: print('No data file in tools/ has the batch key "%s".'%key); return
    from states import STATES
    reg={}
    for p in mod.PLACES: reg[p['reg']]=reg.get(p['reg'],0)+1
    st=sorted({s['name'] for s in STATES for c,l in s['regions'] if c in reg})
    os.makedirs(os.path.join(clone,'notes'),exist_ok=True); path=os.path.join(clone,'notes',key+'.md')
    if os.path.exists(path): print('It is already there: '+path); return
    open(path,'w',encoding='utf-8').write('''# %s: %s
state: %s
region: %s
date: %s
places: %d
file: %s.py

## What this batch is
(One short paragraph. What you added. How the sources were read: which tools, which sites. What was NOT checked: on the
ground, hours, owners, parking, pins that mark only a trailhead. Delete this bracketed text.)

## Leads
Places you read about and could not finish. One row each; delete the example row. Leave the table header.

| Place | Where | What is known | What is missing |
|---|---|---|---|
| Example mill | Town, ST (42.12345, -73.12345 if you have it) | What a source says, and which source | What would let it be added |

## Tips
- (Anything about a tool, a source or the guide that would have saved you time, or that is wrong. One line each.
  "None" if there is nothing. Delete this bracketed text.)
'''%(key,mod.BATCH.get('label',key),', '.join(st) or '?',', '.join(sorted(reg)),datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d'),len(mod.PLACES),os.path.basename(mod.__file__)[:-3]))
    print(path); print('Fill it in, then: git -C %s add -A'%clone)

if sys.argv[1]=='--new':            # publish.sh: a note for every batch added after this tool was that has none yet
    clone=sys.argv[2]
    for f in sorted(glob.glob(os.path.join(HERE,'data_*.py'))):
        if os.path.basename(f) in('data_a.py','data_b.py'): continue
        m=importlib.import_module(os.path.basename(f)[:-3]); b=getattr(m,'BATCH',{})
        if str(b.get('added',''))>='2026-11-17 22:00' and not os.path.exists(os.path.join(clone,'notes',b['key']+'.md')): make(b['key'],clone)
    sys.exit(0)
key=sys.argv[1]
clone=sys.argv[2] if len(sys.argv)>2 else (open(os.path.join(W,'.repo')).read().strip() if os.path.exists(os.path.join(W,'.repo')) else '')
if not clone or not os.path.isdir(os.path.join(clone,'.git')): sys.exit('Give the path to the repository clone: python3 tools/note.py %s <clone>'%key)
make(key,clone)
