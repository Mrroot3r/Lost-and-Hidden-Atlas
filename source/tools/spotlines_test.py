#!/usr/bin/env python3
"""Offline checks of tools/spotlines.py (spots sent through the form, as tools/inbox.py reads them): python3 tools/spotlines_test.py"""
import os,sys
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
import spotlines as S
n=0
def ok(c,what):
    global n; n+=1
    if not c: print('FAIL:',what); sys.exit(1)
t='1. 42.65852, -73.77767 brick warehouse, arched windows\n2. 42.66145, -73.77308\n3. 42.7, -73.9 too few decimals'
r=S.spots('Spots: 3 marked for research',t)
ok(len(r)==2,'two good lines, the one with a rough coordinate left out')
ok(r[0]==(1,42.65852,-73.77767,'brick warehouse, arched windows') and r[1]==(2,42.66145,-73.77308,''),'number, point and note')
ok(S.spots('Womens club of albany','1. 42.65852, -73.77767 x')==[],'only a submission that says it is spots is read as spots')
ok(S.spots('Spots: 1','nothing here')==[],'no lines, no spots')
ok(S.spots('spots: 2 marked','1) 42.65852,-73.77767\r\n2) 44.12345 , -70.54321 mill')[1]==(2,44.12345,-70.54321,'mill'),'a bracket, no space, a carriage return')
ok(S.spots('Spots: 1','1. 99.12345, -73.77767')==[],'a latitude that cannot be is left out')
print('spotlines test: %d checks passed'%n)
