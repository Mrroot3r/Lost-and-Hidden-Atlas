#!/usr/bin/env python3
"""Read the question ids out of the owner's Google Form, so the app can open it already filled in.
   python3 tools/form_ids.py "https://docs.google.com/forms/d/e/<long id>/viewform"
Prints the two lines to put in SHARE in src/app.js (form and ent). The form needs these questions, in any order, with
these words somewhere in their titles (GUIDE.md section 15 has the exact form to make):
   "What are you sending"   multiple choice: "A place I know about", "A visit report"
   "Place"   "Where"   "What do you know"   "Source"   "public" (can the public go there)
The form must be open to anyone with the link, with "collect email addresses" switched off."""
import sys,re,json,urllib.request
if len(sys.argv)<2: sys.exit(__doc__)
u=sys.argv[1].split('?')[0]
if u.endswith('/edit'): sys.exit('That is the editing address. Press Send in the form, choose the link tab, and give that link (it ends in /viewform).')
try: h=urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':'Mozilla/5.0'}),timeout=40).read().decode('utf-8','replace')
except Exception as e: sys.exit('Could not open the form: '+str(e)[:100])
m=re.search(r'FB_PUBLIC_LOAD_DATA_\s*=\s*(\[.*?\]);\s*</script>',h,re.S)
if not m: sys.exit('This does not look like a public Google Form page (is it open to anyone with the link?).')
d=json.loads(m.group(1)); qs=[(q[1],q[4][0][0]) for q in d[1][1] if q and len(q)>4 and q[4]]
want=(('kind',('what are you sending',)),('place',('place',)),('where',('where',)),('text',('what do you know','what you know')),('source',('source','how do you know')),('access',('public','access')))
ent={}; used=set()
for k,ws in want:
    for t,i in qs:
        if i not in used and any(w in (t or '').lower() for w in ws): ent[k]='entry.%d'%i; used.add(i); break
print('questions found:'); [print('   entry.%d  %s'%(i,t)) for t,i in qs]
miss=[k for k,_ in want if k not in ent]
if miss: print('NOT FOUND:',', '.join(miss),'-> check the question titles against the list in this tool\'s help.')
final=re.sub(r'/viewform.*$','/viewform',d and u)
print('\nIn src/app.js, SHARE:\n  form:%s,\n  ent:%s};'%(json.dumps(final),json.dumps(ent).replace('"',"'")))
