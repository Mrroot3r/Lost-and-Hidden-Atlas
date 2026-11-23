#!/usr/bin/env python3
"""Offline checks of tools/videos.py (leads from video transcripts): python3 tools/videos_test.py"""
import os,sys,tempfile
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
import videos as v
n=0
def ok(c,what):
    global n; n+=1
    if not c: print('FAIL:',what); sys.exit(1)
P=v.place_of
ok(P('Old World Salem Massachusetts')==('Salem','ma'),'town and state')
ok(P('Old World Janesville, Wisconsin')==('Janesville','wi'),'comma')
ok(P('Old World Parkersburg West Virginia')==('Parkersburg','wv'),'West Virginia is not Virginia')
ok(P('Old World Concord New Hampshire')==('Concord','nh'),'two-word state')
ok(P('Old World Richmond Virginia')==('Richmond','va'),'Virginia')
ok(P('Old World Nebraska Favourites')==('','ne'),'a state with no town')
ok(P('Old World Chattanooga')==('Chattanooga',None),'a town with no state')
ok(P('Demolished Detroit')==('Detroit',None),'demolished series')
ok(P('Old World Kansas City Missouri')==('Kansas City','mo'),'a state name inside the town')
ok(P('Old World Washington Pennsylvania')==('Washington','pa'),'the last state named wins')
ok(P('Old World Halifax Nova Scotia')==('Halifax','ns'),'a province')
for t in ('Phantom Architects: Samuel Hannaford','After The Event: Germany','Old World Thoughts: Volume One','My Conversation with Jake the Improbable Dreamer','HG Wells: From Fact to Fiction to Fact','Old World Mausoleums','Exploring the Old World','Old World Thoughts Vol 2: Mt Rushmore & Paris'):
    ok(P(t) is None,'not a place video: '+t)
rows=v.read_index(['﻿date,views,minutes,captions,title,address,file','2026-08-28,5000,30,yes,Old World Salem Massachusetts,https://www.youtube.com/watch?v=abc_-123XYZ,20260828_abc_-123XYZ.txt','2026-08-01,9,30,no,Old World Lynn Massachusetts,https://www.youtube.com/watch?v=nocaps00000,20260801_nocaps00000.txt','2026-07-01,70000,40,yes,After The Event: Turkey,https://www.youtube.com/watch?v=turkey00000,20260701_turkey00000.txt'])
ok(len(rows)==3 and rows[0]['id']=='abc_-123XYZ' and rows[0]['views']==5000 and rows[0]['file']=='20260828_abc_-123XYZ.txt','index rows')
d=tempfile.mkdtemp(); os.makedirs(d+'/source/videos')
ok(v.done(d)=={},'nothing done yet')
md=v.skeleton(rows[0],'Salem','ma','Old World Exploration','vid_abcd')
ok('# Video: Old World Salem Massachusetts' in md and 'watch?v=abc_-123XYZ' in md and 'Place: Salem, Massachusetts' in md and '| Name as said |' in md,'skeleton')
body=md+'| Aanam | Salem Athenaeum | standing | 7:29 | added salem-athenaeum |\n| Beach Pavilion | | gone | 8:01 | gone |\n| Cadet Armory | Salem Armory | not said | 8:10 | not checked |\n'
open(d+'/source/videos/20260828_abc_-123XYZ.md','w').write(body)
D=v.done(d); ok(set(D)=={'abc_-123XYZ'} and D['abc_-123XYZ']==1,'done, with one name not checked')
ok(v.problems(body,{'salem-athenaeum'})==[],'a good ledger file')
ok(any('no such place' in p for p in v.problems(body,set())),'an added place must exist')
ok(any('outcome' in p for p in v.problems(body.replace('| gone |\n','| maybe |\n'),{'salem-athenaeum'})),'an unknown outcome')
ok(any('TODO' in p for p in v.problems(md+'| TODO | | | | |\n',set())),'a TODO left in')
# what sessions kept tripping on (their notes, November 2026): a remark after the outcome, or after the place id
ok(v.problems(body.replace('| gone |\n','| gone: razed 1942 |\n'),{'salem-athenaeum'})==[],'an outcome may be followed by a colon and a remark')
ok(v.problems(body.replace('| gone |\n','| gone (razed 1942) |\n'),{'salem-athenaeum'})==[],'or by a remark in brackets')
ok(v.problems(body.replace('added salem-athenaeum','added salem-athenaeum (the 1907 building)'),{'salem-athenaeum'})==[],'a remark after the place id is not read as part of the id')
ok(any('outcome' in p for p in v.problems(body.replace('| gone |\n','| goner |\n'),{'salem-athenaeum'})),'a word that only begins like an outcome is still refused')
ok(any('no names' in p for p in v.problems(md,set())),'an empty table')
free,busy,other=v.sort_out(rows,D,{'vid-nocaps00000':['x']},set())
ok(free==[] and [r['id'] for r in busy]==['nocaps00000'] and [r['id'] for r in other]==['turkey00000'],'done, claimed and not-a-place videos are not offered')
free,busy,other=v.sort_out(rows,{},{},{'nocaps00000'})
ok([r['id'] for r in free]==['abc_-123XYZ'] and [r['id'] for r in busy]==['nocaps00000'],'a video in an open pull request is busy')
L=v.live(['vid-a 20200101T000000 aaaa','vid-b %s bbbb'%v.stamp(),'ny1 %s bbbb'%v.stamp(),'vid-c %s cccc'%v.stamp(),'released %s cccc'%v.stamp()])
ok(set(L)=={'vid-b','ny1'},'claims lapse after eight hours and a release frees every line with its tag')
print('videos test: %d checks passed'%n)
