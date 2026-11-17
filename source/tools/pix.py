#!/usr/bin/env python3
"""Turn a spot you can see in a picture into a coordinate, so nobody works it out by hand.
   python3 tools/pix.py pin  <lat> <lon> <x> <y>            a pincheck.py sheet (aerial or --lidar): lat,lon = the pin printed
                                                            over the tile, x,y = the pixel in the SHEET where the thing is
   python3 tools/pix.py look <lat> <lon> <half_m> <x> <y>   a look.py picture: lat,lon,half_m as given to look.py
   python3 tools/pix.py move <lat> <lon> <east_m> <north_m> shift a point by metres (west and south are negative)
x runs right and y runs down from the top-left corner of the whole picture; which tile the pixel is in is worked out.
Tiles are web-mercator squares with north up: pincheck 420 px = 300 m, look 560 px = 2*half_m.
Prints the new coordinate and how far it is from the old one. Run the pin check again afterwards to see the ring on it."""
import sys,math
def merc(la,lo): return lo*20037508.34/180, math.log(math.tan((90+la)*math.pi/360))*20037508.34/math.pi
def unmerc(x,y): return math.degrees(2*math.atan(math.exp(y*math.pi/20037508.34))-math.pi/2), x*180/20037508.34
a=sys.argv[1:]
try:
    kind=a[0]; la,lo=float(a[1]),float(a[2])
    if kind=='move': e,n=float(a[3]),float(a[4])
    else:
        if kind=='pin': px,half,x,y=420,150.0,float(a[3]),float(a[4])
        elif kind=='look': px,half,x,y=560,float(a[3]),float(a[4]),float(a[5])
        else: raise ValueError
        x%=px; y%=px                                   # the pixel inside its own tile, wherever the tile sits in the sheet
        e=(x-px/2)*2*half/px; n=(px/2-y)*2*half/px
except (IndexError,ValueError): sys.exit(__doc__)
k=1/math.cos(math.radians(la)); mx,my=merc(la,lo); nla,nlo=unmerc(mx+e*k,my+n*k)
print(f'{nla:.5f}, {nlo:.5f}    ({abs(e):.0f} m {"east" if e>=0 else "west"}, {abs(n):.0f} m {"north" if n>=0 else "south"} of {la}, {lo}; {math.hypot(e,n):.0f} m in all)')
