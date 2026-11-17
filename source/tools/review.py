"""List what a pull request adds or changes among the places, for a reviewer (GUIDE.md section 14).
   python3 source/tools/review.py [repo] [base] [--built <index.html of a build of the branch>]
        default repo: current folder; default base: origin/main
Run it in a checkout of the pull request's branch. It compares a built place list (index.html) with the base and prints
every new or changed place with its sources, plus flags worth a second look. It reads nothing from the network.

A pull request carries sources only, so the branch's own index.html is the same as the base's and says nothing. Build the
branch first (source/tools/setup.sh, then tools/all.sh in the workspace) and the tool finds that build by itself in
$ATLAS/dist/web (or /home/claude/atlas/dist/web); or name one with --built."""
import sys,json,re,subprocess,os
_a=sys.argv[1:]; built=None
if '--built' in _a: i=_a.index('--built'); built=_a[i+1]; _a=_a[:i]+_a[i+2:]
repo=_a[0] if len(_a)>0 else '.'; base=_a[1] if len(_a)>1 else 'origin/main'
def sites(txt):
    m=re.search(r'<script type="application/json" id="d-sites">(.*?)</script>',txt,re.S)
    return {s['id']:s for s in json.loads(m.group(1).replace('<\\/','</'))['sites']} if m else {}
old=sites(subprocess.run(['git','-C',repo,'show',base+':index.html'],capture_output=True,text=True).stdout)
src=repo+'/index.html'
if built: src=built if built.endswith('.html') else os.path.join(built,'index.html')
elif subprocess.run(['git','-C',repo,'diff','--quiet',base,'--','index.html']).returncode==0:
    # the branch has no built list of its own: look for a workspace build
    ws=os.path.join(os.environ.get('ATLAS') or '/home/claude/atlas','dist','web','index.html')
    if os.path.exists(ws): src=ws; print('This branch carries sources only; reading the workspace build',ws,'\n(make sure it was built from THIS branch: setup.sh, then all.sh).')
    else:
        print('This branch carries sources only, so its index.html is the same as the base and there is nothing to compare.\nBuild it first:  bash source/tools/setup.sh   then   ATLAS=<workspace> bash <workspace>/tools/all.sh\nthen run this again, or name a build:  --built <workspace>/dist/web'); sys.exit(2)
new=sites(open(src,encoding='utf-8').read())
KEYS=('name','town','reg','cat','st','prec','acc','eff','lat','lon','years','story','look','accn','links','conf')
added=[i for i in new if i not in old]; gone=[i for i in old if i not in new]
changed=[i for i in new if i in old and any(new[i].get(k)!=old[i].get(k) for k in KEYS)]
print(f'{len(added)} added, {len(changed)} changed, {len(gone)} removed (base {base})')
if gone: print('REMOVED ids (published ids must never disappear or be renamed):',', '.join(gone))
def show(s,was=None):
    flags=[]
    if not s.get('links') and s.get('conf')!='lead': flags.append('no source link')
    if s.get('conf')=='lead': flags.append('unverified lead')
    if s.get('prec')=='exact': flags.append('claims an exact pin: is the structure visible on the aerial?')
    if s.get('acc')=='public' and s.get('pl') and s['pl'][2] in('XA','RA'): flags.append('marked public, but the public-land map says closed or restricted')
    if s.get('acc')=='public' and not s.get('pl'): flags.append('marked public, but the pin is not on mapped public land')
    if not s.get('accn'): flags.append('no access note')
    if re.search(r'\b(reportedly|rumou?red|said to|legend|haunted)\b',(s.get('story','')+s.get('look','')),re.I): flags.append('hearsay wording: is it sourced?')
    n=len(re.findall(r'\b1[5-9]\d\d\b|\b20[0-2]\d\b|\b\d+(?:,\d{3})*(?:\.\d+)? (?:acres|feet|miles|people|families|men)\b',s.get('story','')+' '+s.get('look','')))
    print(f"\n### {s['id']}  ({s.get('name')}, {s.get('town')})  [{s.get('reg')}/{s.get('cat')}/{s.get('st')}/{s.get('prec')}/{s.get('acc')}/conf={s.get('conf') or 'sourced'}]")
    print(f"pin {s.get('lat')},{s.get('lon')}   land: {s.get('pl') or 'not on mapped public land'}   {n} dated or numeric claims to check")
    for k in('years','story','look','accn'):
        if s.get(k): print(f'  {k}: {s[k]}')
    for l in s.get('links') or []: print('  source:',l[0],'->',l[1])
    if was:
        for k in KEYS:
            if was.get(k)!=s.get(k): print(f'  CHANGED {k}: {str(was.get(k))[:140]}  =>  {str(s.get(k))[:140]}')
    if flags: print('  FLAGS:',' | '.join(flags))
for i in added: show(new[i])
for i in changed: show(new[i],old[i])
print('\nReview steps: GUIDE.md section 14.')
