#!/usr/bin/env python3
"""Lost & Hidden Atlas: collect the titles and transcripts of a YouTube channel's videos.

It reads channels.txt (one channel address on each line), lists every video on each channel, and saves for
each video one text file: its title, address, date, view count, description and the transcript (YouTube's
captions, with a time mark about every half minute). It signs in to nothing and downloads no video.

  python atlas_videos.py            collect everything in channels.txt (carries on where it stopped)
  python atlas_videos.py --max 5    stop after 5 new videos (a quick try)
  python atlas_videos.py --index    only rewrite index.csv from what is saved; fetches nothing
  python atlas_videos.py --gap 40   wait about 40 seconds between videos (45 if not given)

What it writes, beside this file:
  videos/<channel>/<date>_<video id>.txt   one per video
  videos/<channel>/index.csv               every video: date, views, minutes, captions or not, title, address
  STATUS.txt    where it is now          log.txt   everything it did          FINISHED.txt   written at the end

The transcripts are the channel owner's work: they stay on this computer. Only the names of buildings taken
from them go into the Atlas, as leads to be checked, never as a source.
"""
import sys, os, re, csv, time, random, datetime

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, 'videos')
LANGS = ['en', 'en-US', 'en-GB', 'en-CA']
T0 = time.time()


def now(): return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')


def log(msg):
    line = '%s  %s' % (now(), msg)
    print(line, flush=True)
    with open(os.path.join(HERE, 'log.txt'), 'a', encoding='utf-8') as f: f.write(line + '\n')


def status(msg):
    with open(os.path.join(HERE, 'STATUS.txt'), 'w', encoding='utf-8') as f:
        f.write('Last update: %s\n%s\n' % (now(), msg))


def took(): return str(datetime.timedelta(seconds=int(time.time() - T0)))


def slug(s): return re.sub(r'[^A-Za-z0-9_-]+', '', s.replace('@', '')) or 'channel'


def channels():
    p = os.path.join(HERE, 'channels.txt')
    if not os.path.exists(p): sys.exit('channels.txt is missing: put one channel address on each line, like https://www.youtube.com/@oldworldex')
    out = []
    for l in open(p, encoding='utf-8'):
        l = l.strip()
        if not l or l.startswith('#'): continue
        if l.startswith('@'): l = 'https://www.youtube.com/' + l
        out.append(l.rstrip('/'))
    return out


def stamp(ms):
    s = int(ms / 1000); h, m, s = s // 3600, s % 3600 // 60, s % 60
    return '%d:%02d:%02d' % (h, m, s) if h else '%d:%02d' % (m, s)


def transcript(snips, every=30):
    """Caption snippets, each (start in milliseconds, text) -> lines of text, each beginning with a time mark,
    about one line per `every` seconds."""
    lines, cur, start = [], [], None
    for t, text in snips:
        text = re.sub(r'\s+', ' ', text or '').strip()
        if not text: continue
        if start is None: start = t
        if t - start >= every * 1000 and cur:
            lines.append('[%s] %s' % (stamp(start), ' '.join(cur))); cur, start = [], t
        cur.append(text)
    if cur: lines.append('[%s] %s' % (stamp(start), ' '.join(cur)))
    return lines


class SlowDown(Exception): pass


def captions(vid):
    """The video's English captions: the uploader's own if there are any, otherwise YouTube's automatic ones.
    -> (lines, 'uploader' | 'automatic' | 'none'). Raises SlowDown when YouTube refuses this computer for now."""
    import youtube_transcript_api as yta
    E = yta._errors if hasattr(yta, '_errors') else yta
    blocked = tuple(getattr(E, n) for n in ('RequestBlocked', 'IpBlocked', 'TooManyRequests') if hasattr(E, n))
    nothing = tuple(getattr(E, n) for n in ('TranscriptsDisabled', 'NoTranscriptFound', 'VideoUnplayable', 'AgeRestricted', 'VideoUnavailable') if hasattr(E, n))
    try:
        tl = yta.YouTubeTranscriptApi().list(vid)
        try: tr, kind = tl.find_manually_created_transcript(LANGS), 'uploader'
        except Exception as e:
            if blocked and isinstance(e, blocked): raise
            tr, kind = tl.find_generated_transcript(LANGS), 'automatic'
        lines = transcript([(int(x.start * 1000), x.text) for x in tr.fetch()])
        return lines, (kind if lines else 'none')
    except blocked as e: raise SlowDown(type(e).__name__ + ': ' + str(e))
    except nothing: return [], 'none'


def list_videos(YDL, url):
    vids, seen = [], set()
    for tab in ('/videos', '/streams'):
        try:
            with YDL({'extract_flat': 'in_playlist', 'quiet': True, 'no_warnings': True, 'skip_download': True}) as y:
                info = y.extract_info(url + tab, download=False)
        except Exception as e:
            if tab == '/videos': raise
            continue
        for e in info.get('entries') or []:
            if e and e.get('id') and e['id'] not in seen:
                seen.add(e['id']); vids.append({'id': e['id'], 'title': e.get('title') or '', 'views': e.get('view_count'), 'secs': e.get('duration')})
    return vids


def one_video(YDL, vid):
    lines, kind = captions(vid)
    opts = {'skip_download': True, 'quiet': True, 'no_warnings': True, 'ignore_no_formats_error': True}
    with YDL(opts) as y:
        info = y.extract_info('https://www.youtube.com/watch?v=' + vid, download=False)
    return info, lines, kind


def write_video(folder, info, lines, kind):
    date = info.get('upload_date') or '00000000'
    p = os.path.join(folder, '%s_%s.txt' % (date, info['id']))
    head = ['TITLE: ' + (info.get('title') or ''),
            'ADDRESS: https://www.youtube.com/watch?v=' + info['id'],
            'CHANNEL: ' + (info.get('channel') or info.get('uploader') or ''),
            'DATE: %s-%s-%s' % (date[:4], date[4:6], date[6:]),
            'VIEWS: %s' % (info.get('view_count') if info.get('view_count') is not None else '?'),
            'MINUTES: %s' % (round((info.get('duration') or 0) / 60) or '?'),
            'CAPTIONS: ' + {'uploader': "the uploader's own", 'automatic': "YouTube's automatic ones (names are often misspelled)", 'none': 'none'}[kind],
            '', 'DESCRIPTION:', (info.get('description') or '').strip(), '', 'TRANSCRIPT:']
    with open(p + '.part', 'w', encoding='utf-8') as f: f.write('\n'.join(head + (lines or ['(no captions on this video)'])) + '\n')
    os.replace(p + '.part', p)
    return p


def done_ids(folder):
    return {m.group(1) for n in os.listdir(folder) for m in [re.match(r'\d{8}_(.+)\.txt$', n)] if m}


def write_index(folder):
    rows = []
    for n in sorted(os.listdir(folder)):
        if not re.match(r'\d{8}_.+\.txt$', n): continue
        h = {}
        for l in open(os.path.join(folder, n), encoding='utf-8'):
            if l.startswith('DESCRIPTION:'): break
            k, _, v = l.partition(': ')
            h[k] = v.strip()
        rows.append([h.get('DATE', ''), h.get('VIEWS', ''), h.get('MINUTES', ''), 'no' if h.get('CAPTIONS') == 'none' else 'yes', h.get('TITLE', ''), h.get('ADDRESS', ''), n])
    rows.sort(reverse=True)
    with open(os.path.join(folder, 'index.csv'), 'w', newline='', encoding='utf-8-sig') as f:
        w = csv.writer(f); w.writerow(['date', 'views', 'minutes', 'captions', 'title', 'address', 'file']); w.writerows(rows)
    return len(rows)


def main(argv):
    if '--index' in argv:          # only rewrite each channel's index.csv from the text files already saved; fetches nothing
        for n in sorted(os.listdir(OUT)) if os.path.isdir(OUT) else []:
            if os.path.isdir(os.path.join(OUT, n)): print('%s: %d videos in index.csv' % (n, write_index(os.path.join(OUT, n))))
        return
    try:
        from yt_dlp import YoutubeDL as YDL
        import youtube_transcript_api
    except ImportError:
        sys.exit('A piece is missing. Install both with:\n    python -m pip install -U yt-dlp youtube-transcript-api\nthen start again.')
    cap = int(argv[argv.index('--max') + 1]) if '--max' in argv else None
    gap = float(argv[argv.index('--gap') + 1]) if '--gap' in argv else 45.0     # seconds between videos; grows when YouTube objects
    fin = os.path.join(HERE, 'FINISHED.txt')
    try:
        if os.path.exists(fin): os.remove(fin)
    except OSError: pass
    new = failed = nocap = 0; report = []; slow = False
    try:
        for url in channels():
            name = slug(url.rsplit('/', 1)[-1]); folder = os.path.join(OUT, name); os.makedirs(folder, exist_ok=True)
            log('Channel %s: listing its videos...' % url); status('Listing the videos of %s' % url)
            try: vids = list_videos(YDL, url)
            except Exception as e:
                log('   COULD NOT LIST %s: %s' % (url, str(e)[:300])); report.append('%s: could not be listed (see log.txt)' % url); continue
            have = done_ids(folder); todo = [v for v in vids if v['id'] not in have]
            log('   %d videos, %d already saved, %d to fetch.' % (len(vids), len(vids) - len(todo), len(todo)))
            for i, v in enumerate(todo):
                if cap is not None and new >= cap: break
                status('%s: video %d of %d to fetch (%s)\nRunning for %s. Saved so far this run: %d.' % (name, i + 1, len(todo), v['title'][:80], took(), new))
                tries = 0
                while True:
                    try:
                        info, lines, kind = one_video(YDL, v['id'])
                        write_video(folder, info, lines, kind); new += 1; nocap += kind == 'none'
                        if new % 10 == 0: write_index(folder)
                        log('   %d/%d  %s  %s  (%s captions, %d lines)' % (i + 1, len(todo), info.get('upload_date', '?'), (info.get('title') or '')[:70], kind, len(lines)))
                        break
                    except Exception as e:
                        msg = str(e)
                        if isinstance(e, SlowDown) or '429' in msg or 'Too Many Requests' in msg or 'rate-limit' in msg.lower() or 'not a bot' in msg.lower():
                            tries += 1
                            if tries > 8: slow = True; break
                            wait = 60 * (30, 60, 120)[min(tries, 3) - 1]; gap = min(gap * 1.6, 180)
                            log('   YouTube asked us to slow down (%s). Waiting %d minutes, then trying again (%d of 8); after that, %d seconds between videos.' % (re.sub(r'\s+', ' ', msg)[-160:], wait // 60, tries, gap))
                            status('%s: YouTube asked us to slow down. Waiting %d minutes.\nSaved so far this run: %d.' % (name, wait // 60, new)); time.sleep(wait); continue
                        failed += 1; log('   SKIPPED %s (%s): %s' % (v['id'], v['title'][:60], msg[:200])); break
                if slow: break
                time.sleep(random.uniform(gap * 0.8, gap * 1.2))
            n = write_index(folder); left = len(vids) - len(done_ids(folder))
            report.append('%s: %d videos on the channel, %d saved, %d still to fetch' % (name, len(vids), n, left))
            if slow: break
    except KeyboardInterrupt:
        log('Stopped by Ctrl+C. Start it again and it carries on from here.'); status('Stopped by hand after %s. Start it again and it carries on.' % took()); return
    lines = ['Finished %s, after %s.' % (now(), took()), '', 'New this run: %d videos saved (%d of them have no captions), %d skipped with an error.' % (new, nocap, failed), ''] + report + ['']
    if slow: lines += ['STOPPED EARLY: YouTube kept refusing for many hours. Nothing is lost.', 'Wait an hour or more, then run START.bat again: it carries on where it stopped.', '']
    elif cap is not None: lines += ['This was a short try (--max %d). Run START.bat for the rest.' % cap, '']
    elif failed: lines += ['Some videos were skipped with an error (log.txt says why). Running START.bat again tries them once more.', '']
    lines += ['The text files are in the "videos" folder. Tell Claude the videos are collected.']
    with open(fin, 'w', encoding='utf-8') as f: f.write('\n'.join(lines) + '\n')
    status(('STOPPED EARLY (YouTube asked us to slow down). ' if slow else 'ALL DONE. ') + '%d saved this run, in %s. See FINISHED.txt.' % (new, took()))
    log('DONE: %d saved, %d skipped, in %s. See FINISHED.txt.' % (new, failed, took()))


if __name__ == '__main__': main(sys.argv[1:])
