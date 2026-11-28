#!/usr/bin/env python3
"""The form finder (tools/form.py): what it reads out of the Park Service's record page and a state's own index.
   python3 tools/form_test.py        run it after changing tools/form.py
No network: the pages are short pieces of the real ones, kept here. On November 26, 2026 a night of Kansas City sessions
called 65 listings "no source": the Park Service's forms for them say "not yet digitized", Missouri had moved its copies,
and the fetch tool will not open the Internet Archive. Every one of them had a record page with its architect and years,
and most a full form at Missouri's new address."""
import sys,os
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
import form
fails=[]
def ok(name,cond,extra=''):
    print(('ok   ' if cond else 'FAIL ')+name+(('  ['+str(extra)[:170]+']') if extra!='' else ''))
    if not cond: fails.append(name)
REC='''<div>DOWNLOAD THIS PDF</div><a href="/GetAsset/5c7387a8-4483-45cf-ac9c-652cb491763f">x</a><a href="/GetAsset/bb2423a2-fb32-40db-94b9-d8f38d663d17">y</a>
<b>Title:</b> Ivanhoe Masonic Temple <b>National Register Information System ID:</b> 85000942 <b>Applicable Criteria:</b> EVENT ARCHITECTURE/ENGINEERING
<b>Architectural Styles:</b> CLASSICAL REVIVAL <b>Architects:</b> Smith,Rea &amp; Lovitt <b>Areas Of Significance:</b> ARCHITECTURE SOCIAL HISTORY
<b>Periods Of Significance:</b> 1900-1924 <b>Significant Years:</b> 1920 1922 <b>Resource Type:</b> BUILDING <b>Keywords:</b> smith,rea &amp; lovitt ; 1920 ; 1922
<b>Note:</b> 2301 E. Linwood Blvd. and 3201 Park Ave. <b>Related Collections:</b> National Register of Historic Places Collection <b>Resource Format:</b> pdf
<b>File Size (bytes):</b> 22151 <b>Date Published:</b> 5/2/1985 <b>Parks:</b> National Register of Historic Places <b>Locations:</b> State: Missouri County: Jackson County Kansas City ; 2301 E. Linwood Blvd. and 3201 Park Ave. <b>Rating:</b>'''
r=form.parse_record(REC)
ok('the record page gives the name',r.get('Title')=='Ivanhoe Masonic Temple',r.get('Title'))
ok('the architects, with the ampersand read',r.get('Architects')=='Smith,Rea & Lovitt',r.get('Architects'))
ok('the style and the years',r.get('Architectural Styles')=='CLASSICAL REVIVAL' and r.get('Significant Years')=='1920 1922',[r.get('Architectural Styles'),r.get('Significant Years')])
ok('the address (the Note) and the day it was listed',r.get('Note','').startswith('2301 E. Linwood') and r.get('Date Published')=='5/2/1985',[r.get('Note'),r.get('Date Published')])
ok('and the files it offers',r.get('assets')==['5c7387a8-4483-45cf-ac9c-652cb491763f','bb2423a2-fb32-40db-94b9-d8f38d663d17'],r.get('assets'))
ok('a page with none of it gives nothing, not a crash',form.parse_record('<html>Error</html>').get('Title') is None)
ok('the placeholder is known for what it is',form.placeholder('The PDF file for this National Register record has not yet been digitized.  ') and form.placeholder('') and not form.placeholder('NPS Form 10-900 United States Department of the Interior '*40))
IDX='''<p><a href="/media/pdf/inter-state-building" data-entity-type="media" title="Inter-State Building">Inter-State Building</a>, 417 E. 13th St./1300 Locust St., Kansas City (6/12/08)</p>
<p><a href="/media/pdf/ivanhoe-masonic-temple" data-entity-type="media" title="Ivanhoe Masonic Temple">Ivanhoe Masonic Temple</a>, 2301 E. Linwood Blvd. and 3201 Park Ave., Kansas City (5/02/85)</p>
<p><a href="https://mostateparks.com/media/pdf/bixby-walter-e-house">Bixby, Walter E., House</a>, 6505 State Line Rd., Kansas City (11/14/78)</p>
<p><a href="/page/other">Not a form</a></p>'''
ix=form.parse_mo_index(IDX)
ok('Missouri\'s index: each listing with its address, its day and where its form is',len(ix)==3 and ix[1]['slug']=='ivanhoe-masonic-temple' and '2301 E. Linwood' in ix[1]['rest'] and ix[2]['slug']=='bixby-walter-e-house',ix)
ok('a listing is found by the Register\'s name for it',form.find_in_index(ix,'Ivanhoe Masonic Temple')['slug']=='ivanhoe-masonic-temple')
ok('with the surname first or last',form.find_in_index(ix,'Walter E. Bixby House')['slug']=='bixby-walter-e-house')
ix2=ix+form.parse_mo_index('<p><a href="/media/pdf/anderson-electric-car-co-building">Anderson Electric Car Co. Building</a>, 3240 Main St., Kansas City (12/12/2022)</p><p><a href="/media/pdf/anderson-elijah-teague-house">Anderson, Elijah Teague, House</a>, 406 N. Pine, Republic (11/14/80)</p>')
e=form.find_in_index(ix2,'Anderson Electric Car Company Building')
ok('"Co." in the state\'s index is "Company" in the Register',e is not None and e['slug']=='anderson-electric-car-co-building',e)
ok('a near name that could be two listings finds neither',form.find_in_index(ix2,'Anderson House') is None)
ok('and a name that is not there finds nothing',form.find_in_index(ix,'Temple Block Building') is None)
V='<iframe src="/themes/common-assets/pdf-viewer/viewer.html?file=https%3A%2F%2Fmostateparks.com%2Fsites%2Fg%2Ffiles%2Fzuston361%2Ffiles%2Fmedia%2Fpdf%2F2025%2F02%2Ftemple-block-building.pdf"></iframe>'
ok('the form\'s own address is read out of Missouri\'s viewer page',form.pdf_in_viewer(V)=='https://mostateparks.com/sites/g/files/zuston361/files/media/pdf/2025/02/temple-block-building.pdf',form.pdf_in_viewer(V))
ok('an old Missouri address is known as one that moved',form.moved('https://mostateparks.com/sites/mostateparks/files/Anderson-Electric-Car-Company-Building.pdf') and form.moved('https://dnr.mo.gov/shpo/nps-nr/85000942.pdf') and not form.moved('https://mostateparks.com/media/pdf/x') and not form.moved('https://example.org/a.pdf'))
ok('the ladder of what to try names the form finder first for a Register form and never stops at the archive',form.ladder('https://npgallery.nps.gov/NRHP/GetAsset/NRHP/85000942_text')[0].startswith('python3 tools/form.py') and len(form.ladder('https://example.org/history'))>=4)
# a site the shell cannot reach at all is not a dead page: the web fetch tool is another road to it (the asylum pass, November 28, 2026:
# ohio.edu, sah-archipedia.org, in.gov and seven more would not connect from page.py, and the web fetch tool read most of them)
ok('a refused connection is told from a dead page',form.unreachable("ERROR HTTPSConnectionPool(host='www.ohio.edu', port=443): Max retries exceeded with url: / (Caused by ProxyError('Unable to connect to proxy', OSError('Tunnel connection failed: 403 Forbidden')))") and form.unreachable('ERROR [Errno -2] Name or service not known') and not form.unreachable('HTTP 404') and not form.unreachable('HTTP 403'))
L_=form.ladder('https://www.ohio.edu/athens/bldgs/ridges.html','ERROR ProxyError Tunnel connection failed: 403 Forbidden')
ok('for one, the web fetch tool is the first thing to try, with the same address',L_[0].startswith('The web fetch tool') and 'same address' in L_[0] and 'ohio.edu' in L_[0],L_[0])
ok('and a dead page keeps the usual order',not form.ladder('https://example.org/gone.html','HTTP 404')[0].startswith('The web fetch tool, first'))
print(f'{len(fails)} FAILED' if fails else 'form test: 19 checks passed'); sys.exit(1 if fails else 0)
