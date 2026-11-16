#!/usr/bin/env python3
"""Draws lidar/examples.jpg: what to keep and what to set aside, as LiDAR chips of the kind "lidar.py next" shows.
   python3 tools/lidar_examples.py
Every chip is a real candidate that was looked at; the caption is the verdict it got. LIDAR.md refers to the letters.
Add a line to EX when a new kind of false alarm turns up, and run this again (needs the network and Pillow)."""
import sys,os,numpy as np
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from lidar_dem import dem,shade
from PIL import Image,ImageDraw,ImageFont
EX=[  # letter, lat, lon, verdict, what it is
 ('A',42.795560,-73.316688,'KEEP','pit inside straight banks: a walled yard'),
 ('B',42.427596,-74.318405,'KEEP','pit + mound inside a rectangle of banks'),
 ('C',42.787473,-73.436672,'KEEP','sharp square pit beside an old road'),
 ('D',44.503483,-73.952426,'KEEP','sharp pit with a spoil mound'),
 ('E',42.526304,-74.272597,'KEEP','round pit with a raised rim'),
 ('F',42.550295,-74.488698,'KEEP','sharp pit 25 m off a forest road'),
 ('G',42.464534,-74.335509,'no water','pond shore'),
 ('H',42.491083,-74.374887,'no natural','stream gullies'),
 ('I',42.792958,-74.300869,'no road','road ditch'),
 ('J',42.813366,-73.462470,'no road','parking area'),
 ('K',42.770576,-73.461106,'no modern','built earthworks, square and fresh'),
 ('L',42.806073,-74.319605,'no coarse','ground model in flat facets'),
 ('M',42.665024,-74.034922,'no natural','many pits on rough rock'),
 ('N',44.565402,-73.664224,'no faint','soft dimple, no edges'),
]
S=230; CAP=34; cols=6; rows=(len(EX)+cols-1)//cols
try: F=ImageFont.load_default(size=12); FB=ImageFont.load_default(size=13)
except TypeError: F=FB=ImageFont.load_default()
o=Image.new('RGB',(cols*S,rows*(S+CAP)),'black'); d=ImageDraw.Draw(o)
for i,(lab,la,lo,v,what) in enumerate(EX):
    z,sc=dem(la,lo,70,140); im=Image.fromarray(np.asarray(shade(z,sc))).convert('RGB').resize((S-4,S-4),Image.LANCZOS)
    x=(i%cols)*S; y=(i//cols)*(S+CAP); o.paste(im,(x+2,y+2)); c=(x+S//2,y+S//2)
    for dx,dy in ((-22,0),(22,0),(0,-22),(0,22)): d.line((c[0]+dx*0.45,c[1]+dy*0.45,c[0]+dx,c[1]+dy),fill=(255,0,160),width=2)
    d.text((x+5,y+S),'%s  %s'%(lab,v),fill=(120,255,120) if v=='KEEP' else (255,150,120),font=FB)
    d.text((x+5,y+S+16),what,fill=(235,235,235),font=F)
os.makedirs('lidar',exist_ok=True); o.save('lidar/examples.jpg',quality=85); print('wrote lidar/examples.jpg',o.size)
