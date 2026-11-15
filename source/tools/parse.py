import re, json
md=open('src/catalogue.md').read().split('\n')
entries=[]; sec=sub=None; cur=None
LINK=re.compile(r'\[([^\]]+)\]\(<?([^)>]+(?:\([^)]*\))?[^)>]*)>?\)')
def links_of(t):
    out=[]
    for m in re.finditer(r'\[([^\]]+)\]\((<[^>]+>|[^)\s]+)\)',t):
        out.append([m.group(1), m.group(2).strip('<>')])
    return out
def strip_links(t):
    t=re.sub(r'\[([^\]]+)\]\((<[^>]+>|[^)\s]+)\)','',t)
    t=re.sub(r'(\s*·\s*)+',' ',t).strip()
    return t
for line in md:
    if line.startswith('## '): sec=line[3:]; sub=None; cur=None; continue
    if line.startswith('### '): sub=line[4:]; cur=None; continue
    m=re.match(r'- \[ \] \*\*(.+?)\*\*\s*—\s*(.*)$',line)
    if m:
        cur={'title':m.group(1),'conf':m.group(2),'sec':sec,'sub':sub,'paras':[]}
        entries.append(cur); continue
    if cur is not None and line.startswith('  ') and line.strip():
        cur['paras'].append(line.strip())
    elif line.strip() and not line.startswith('  '):
        cur=None
out=[]
for i,e in enumerate(entries):
    story=''; notes={}; links=[]
    for j,p in enumerate(e['paras']):
        links+=links_of(p)
        t=strip_links(p)
        if not t: continue
        if j==0 and not t.startswith('*'):
            story=t; continue
        # split labelled notes
        parts=re.split(r'\*(Look for|Hook|Access|Also here|Lead|Source material|Background):\*',t)
        if parts[0].strip():
            notes.setdefault('note',[]).append(parts[0].strip())
        for k in range(1,len(parts),2):
            notes.setdefault(parts[k],[]).append(parts[k+1].strip())
    out.append({'i':i,'title':e['title'],'conf':e['conf'],'sec':e['sec'],'sub':e['sub'],'story':story,'notes':{k:' '.join(v) for k,v in notes.items()},'links':links})
json.dump(out,open('src/entries.json','w'),indent=1,ensure_ascii=False)
for o in out: print(o['i'],'|',o['title'][:70],'|',o['conf'][:22],'|',list(o['notes'].keys()),len(o['links']))
# landmarks table
rows=[]
on=False
for line in md:
    if line.startswith('## Standing landmarks'): on=True; continue
    if on and line.startswith('## '): break
    if on and line.startswith('| ') and 'Map](' in line:
        c=[x.strip() for x in line.strip('|').split('|')]
        rows.append({'name':c[0],'q':re.search(r'query=([^)]+)\)',c[1]).group(1),'town':c[2],'built':c[3],'visit':c[4],'why':c[5]})
json.dump(rows,open('src/landmarks.json','w'),indent=1,ensure_ascii=False)
print(len(out),len(rows))
