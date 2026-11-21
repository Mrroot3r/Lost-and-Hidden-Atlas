#!/usr/bin/env python3
"""Lost & Hidden Atlas: run the LiDAR sweep on your own computer.

    python atlas_sweep.py                 sweep every unit named in units.txt, one after another, until all are done
    python atlas_sweep.py near 42.45 -74.6 25      list public-land units within 25 miles of a point that nobody has swept
    python atlas_sweep.py find "Bear Swamp"        look a unit up by name
    python atlas_sweep.py status          what the ledger holds

What it does: the sweep downloads the bare-ground LiDAR model for a state forest or other public unit, finds pits and
stone walls in it, and matches the pits against buildings drawn on the survey maps of about 1900. That is the slow,
dull half of the work and it needs no AI: this script does it here, for as long as you leave it running. The other half,
looking at each candidate and deciding what it is, is done afterwards by Claude from the results in the "work" folder.

It uses the Atlas's own tools, fetched fresh from GitHub each time it starts, so it never drifts from the Atlas.
Nothing is uploaded and nothing outside this folder is touched.

Watch it:   the window prints a line for every step;  STATUS.txt  always holds where it is;  log.txt  holds everything.
It is done when the window says ALL DONE and a file  FINISHED.txt  appears. Stop it any time with Ctrl+C or by closing
the window: it carries on from where it stopped the next time you start it.
"""
import sys, os, json, time, subprocess, datetime, urllib.request, urllib.parse, shutil, re

HERE = os.path.dirname(os.path.abspath(__file__))
WORK = os.path.join(HERE, 'work')                      # the Atlas workspace: tools/, lidar/units (the ledger), research/lidar (downloads)
REPO = 'Mrroot3r/Lost-and-Hidden-Atlas'
UA = {'User-Agent': 'lost-hidden-atlas-sweep/1.0', 'Accept': 'application/vnd.github+json'}
NEED = ('numpy', 'scipy', 'PIL', 'requests', 'rasterio')
PIPNAME = {'PIL': 'pillow'}
TOOLS = re.compile(r'^(lidar(_[a-z0-9]+)?|ortho|topocrop|walls_structure)\.py$')
MINUTES = '9'                                          # how long one call of the Atlas tool works before it stops cleanly and is called again


def now(): return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')


def say(msg):
    line = '%s  %s' % (now()[11:], msg)
    print(line, flush=True)
    with open(os.path.join(HERE, 'log.txt'), 'a', encoding='utf-8') as f: f.write(now()[:11] + line + '\n')


def status(text):
    tmp = os.path.join(HERE, 'STATUS.txt.tmp')
    with open(tmp, 'w', encoding='utf-8') as f: f.write('Last update: %s\n%s\n' % (now(), text))
    os.replace(tmp, os.path.join(HERE, 'STATUS.txt'))
    if os.name == 'nt': os.system('title Atlas LiDAR sweep: ' + re.sub(r'[^A-Za-z0-9 ,.:()-]', '', text.split('\n')[0])[:90])


def get(url, tries=5):
    for k in range(tries):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60) as r: return r.read()
        except Exception as e:
            if k == tries - 1: raise
            time.sleep(5 * (k + 1))


def check_python():
    if sys.version_info < (3, 9): sys.exit('This needs Python 3.9 or newer; this is %s.' % sys.version.split()[0])
    missing = []
    for m in NEED:
        try: __import__(m)
        except Exception: missing.append(PIPNAME.get(m, m))
    if not missing: return
    say('Installing what the tools need (once): ' + ' '.join(missing))
    r = subprocess.run([sys.executable, '-m', 'pip', 'install', '--user'] + missing)
    if r.returncode != 0:
        sys.exit('pip could not install them. Run this yourself, then start again:\n   "%s" -m pip install %s' % (sys.executable, ' '.join(missing)))
    say('Installed. Starting again so Python can see them.')
    sys.exit(subprocess.run([sys.executable] + sys.argv).returncode)


def listing(path):
    """the files in one folder of the repository: [(name, download address)]"""
    parent, name = os.path.split(path)
    kids = json.loads(get('https://api.github.com/repos/%s/contents/%s?ref=main' % (REPO, urllib.parse.quote(parent))))
    sha = next(k['sha'] for k in kids if k['name'] == name)
    tree = json.loads(get('https://api.github.com/repos/%s/git/trees/%s' % (REPO, sha)))
    return [(t['path'], 'https://raw.githubusercontent.com/%s/main/%s/%s' % (REPO, path, urllib.parse.quote(t['path']))) for t in tree['tree'] if t['type'] == 'blob']


def refresh():
    """the Atlas's LiDAR tools and its ledger of what has been swept, fresh from GitHub"""
    for d in ('tools', 'src', 'lidar/units', 'research/lidar'): os.makedirs(os.path.join(WORK, d), exist_ok=True)
    try:
        tools = [(n, u) for n, u in listing('source/tools') if TOOLS.match(n)]
        for n, u in tools:
            with open(os.path.join(WORK, 'tools', n), 'wb') as f: f.write(get(u))
        inbox = os.path.join(WORK, 'research', 'lidar', 'from_github'); shutil.rmtree(inbox, ignore_errors=True); os.makedirs(inbox, exist_ok=True)
        units = [(n, u) for n, u in listing('source/lidar/units') if n.endswith('.json')]
        for n, u in units:
            with open(os.path.join(inbox, n), 'wb') as f: f.write(get(u))
        r = tool(['pull', os.path.join('research', 'lidar', 'from_github')], quiet=True)
        say('Tools and ledger are up to date: %d tool files, %d units already swept by the Atlas.' % (len(tools), len(units)))
    except Exception as e:
        if not os.path.exists(os.path.join(WORK, 'tools', 'lidar.py')): sys.exit('Could not fetch the Atlas tools from GitHub (%s). Check the internet connection and start again.' % str(e)[:120])
        say('Could not reach GitHub just now (%s); carrying on with the tools already here.' % str(e)[:80])


def tool(args, quiet=False, echo=None):
    """run the Atlas's own tools/lidar.py in the work folder; returns everything it printed"""
    env = dict(os.environ, PYTHONUTF8='1', PYTHONIOENCODING='utf-8')
    p = subprocess.Popen([sys.executable, os.path.join('tools', 'lidar.py')] + args, cwd=WORK, env=env, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, encoding='utf-8', errors='replace')
    out = []
    for line in p.stdout:
        out.append(line)
        if not quiet: (echo or say)('   ' + line.rstrip())
    p.wait()
    return ''.join(out)


def units_wanted():
    f = os.path.join(HERE, 'units.txt')
    if not os.path.exists(f): sys.exit('There is no units.txt beside this script. Put one unit name on each line (python atlas_sweep.py near <lat> <lon> <miles> lists them).')
    return [l.strip() for l in open(f, encoding='utf-8') if l.strip() and not l.lstrip().startswith('#')]


def sweep_all():
    names = units_wanted(); done = []; skipped = []; t0 = time.time()
    fin = os.path.join(HERE, 'FINISHED.txt')
    if os.path.exists(fin): os.replace(fin, os.path.join(HERE, 'FINISHED_previous.txt'))
    say('%d units to sweep. Stop any time with Ctrl+C; it carries on from there next time.' % len(names))
    for i, name in enumerate(names, 1):
        head = 'Unit %d of %d: %s' % (i, len(names), name)
        fails = 0; rounds = 0
        while True:
            rounds += 1
            status('%s\nWorking (round %d). Finished so far: %d. Skipped: %d.\nStarted %s ago.' % (head, rounds, len(done), len(skipped), str(datetime.timedelta(seconds=int(time.time() - t0)))))
            say('%s (round %d)' % (head, rounds))
            out = tool(['sweep', name, '--minutes', MINUTES])
            if 'DONE:' in out or 'already swept' in out:
                done.append(name); break
            if 'NO SUCH UNIT' in out or 'SKIPPED' in out:
                skipped.append((name, 'the Atlas tool would not take this name (see log.txt)')); break
            if 'NOT FINISHED' in out or 'TIME IS UP' in out:
                m = re.search(r'(\d+) of (\d+) tiles', out)
                if m: status('%s\n%s of %s tiles scanned. Finished so far: %d. Skipped: %d.' % (head, m.group(1), m.group(2), len(done), len(skipped)))
                if rounds >= 400: skipped.append((name, 'still not finished after 400 rounds')); break
                continue
            fails += 1                                   # no ground model, a failed step, or something unexpected
            if fails >= 3: skipped.append((name, 'failed three times (see log.txt)')); break
            say('   That did not work; waiting two minutes and trying again (%d of 3).' % fails); time.sleep(120)
    took = str(datetime.timedelta(seconds=int(time.time() - t0)))
    summary = tool(['status'], quiet=True).split('\nNext:')[0]          # the tool's advice to a model, and its warnings about place lists that are not on this computer, are left out
    summary = '\n'.join(l for l in summary.split('\n') if 'WARNING' not in l)
    text = 'Finished %s, after %s.\n\nSwept: %d\n%s\n\nSkipped: %d\n%s\n\nWhat the ledger holds now:\n%s\nThe results are in work/lidar/units and work/lidar/walls. Tell Claude the sweep is finished.\n' % (
        now(), took, len(done), '\n'.join('  ' + n for n in done) or '  (none)', len(skipped), '\n'.join('  %s: %s' % s for s in skipped) or '  (none)', summary)
    with open(fin, 'w', encoding='utf-8') as f: f.write(text)
    status('ALL DONE. %d swept, %d skipped, in %s. See FINISHED.txt.' % (len(done), len(skipped), took))
    say('ALL DONE: %d swept, %d skipped, in %s. See FINISHED.txt.' % (len(done), len(skipped), took))
    try:
        import winsound
        for _ in range(3): winsound.Beep(880, 300); time.sleep(0.15)
    except Exception: pass


if __name__ == '__main__':
    os.chdir(HERE)
    check_python()
    refresh()
    a = sys.argv[1:]
    try:
        if a and a[0] in ('near', 'find', 'status'): tool(a, echo=lambda s: print(s[3:]))
        elif a: sys.exit(__doc__)
        else: sweep_all()
    except KeyboardInterrupt:
        status('Stopped by hand at %s. Start it again and it carries on.' % now()); say('Stopped by hand. Start it again and it carries on.')
