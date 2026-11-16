#!/usr/bin/env python3
"""Print how tools/pockets.py ranked the old town centres and other pockets round a point, to judge the ranking in a
place you know. Reads build/pockets.json.

   python3 tools/pock_report.py                      within 40 miles of Albany
   python3 tools/pock_report.py 42.878 -73.197 25    within 25 miles of Bennington"""
import json,math,sys
P=json.load(open('build/pockets.json'))['k']
la0,lo0=(float(sys.argv[1]),float(sys.argv[2])) if len(sys.argv)>2 else (42.6526,-73.7562)
R=float(sys.argv[3]) if len(sys.argv)>3 else 40
def mi(a,b,c,d): return math.hypot((c-a)*69,(d-b)*69*math.cos(math.radians(a)))
near=[k for k in P if mi(la0,lo0,k[0],k[1])<=R]
c=[k for k in near if k[10]=='c']; o=[k for k in near if k[10]=='p']
print(f'within {R:.0f} mi:',len(c),'centres,',len(o),'other pockets')
for k in sorted(c,key=lambda k:-k[11])[:30]: print('  C %5.1f  %-32s %2d mi  %2d spots %-12s %2d listed %d dist (%d bldg)'%(k[11],k[7][:32],mi(la0,lo0,k[0],k[1]),k[9],k[12],k[4],k[5],k[6]))
print('  other pockets:')
for k in sorted(o,key=lambda k:-k[11])[:8]: print('  P %5.1f  %-32s %2d mi  %2d spots %-12s %2d listed %d dist (%d bldg)'%(k[11],k[7][:32],mi(la0,lo0,k[0],k[1]),k[9],k[12],k[4],k[5],k[6]))
