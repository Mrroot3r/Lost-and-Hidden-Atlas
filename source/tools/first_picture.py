#!/usr/bin/env python3
"""Keeps the first picture on the repository's front page (docs/features/01-map.jpg) in step with the map.
   python3 tools/first_picture.py <repository root> need    exit 0 when the picture should be retaken, 1 when not
   python3 tools/first_picture.py <repository root> done    after retaking it: record the count, bring the caption's number up to date
The picture shows the whole map with its numbered bubbles, so it goes stale as places are added (the owner, November 25, 2026:
"keep that one updated as we add places"). The site build (.github/workflows/site.yml) asks "need" after every build and retakes
the picture with tools/shots.js when the map has passed another hundred places since the last one: often enough to be true,
seldom enough that the repository does not gain a picture with every merge. The count at the last picture is kept in
docs/features/01-map.count. Test: tools/first_picture_test.py."""
import sys,os,re,json
root=sys.argv[1]; what=sys.argv[2] if len(sys.argv)>2 else 'need'
def count():
    m=re.search(r'id="d-sites">(.*?)</script>',open(os.path.join(root,'index.html'),encoding='utf-8').read(),re.S)
    d=json.loads(m.group(1)) if m else {}
    return len(d.get('sites',d) if isinstance(d,dict) else d)
cf=os.path.join(root,'docs','features','01-map.count')
n=count(); last=int(open(cf).read().strip() or 0) if os.path.exists(cf) else 0
if n<100: sys.exit('first_picture: the built page lists %d places; not taking a picture of that.'%n)
if what=='need':
    go=n//100>last//100; print('%d places now, %d at the last picture: %s'%(n,last,'retake it' if go else 'keep it')); sys.exit(0 if go else 1)
if what=='done':
    open(cf,'w').write('%d\n'%n)
    p=os.path.join(root,'README.md'); s=open(p,encoding='utf-8').read()
    s2=re.sub(r'More than [\d,]+ old places','More than {:,} old places'.format(n//100*100),s,count=1)
    if s2!=s: open(p,'w',encoding='utf-8').write(s2)
    print('Recorded %d places; the caption says more than %s.'%(n,'{:,}'.format(n//100*100))); sys.exit(0)
sys.exit('first_picture: need or done')
