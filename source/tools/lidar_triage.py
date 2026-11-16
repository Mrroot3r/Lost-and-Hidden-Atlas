"""A quick first look at many LiDAR candidates at once (GUIDE.md section 13).
   python3 tools/lidar_triage.py out.jpg spots.txt
        spots.txt holds one "label lat lon" per line. Draws a grid of shaded-relief chips, 140 m across, six to a row,
        with pink ticks on each spot. Use it to throw out the faint and the obviously natural before making the
        full comparison sheets (lidar_sheet.py sheet), which cost far more time to draw and to read."""
import sys,numpy as np
sys.path.insert(0,'tools')
from lidar_dem import dem,shade
from PIL import Image,ImageDraw
C=[l.split() for l in open(sys.argv[2]) if l.strip()]
n=len(C); cols=6; rows=(n+cols-1)//cols; S=230
o=Image.new('RGB',(cols*S,rows*S),'black'); d=ImageDraw.Draw(o)
for i,(lab,la,lo) in enumerate(C):
    try:
        z,sc=dem(float(la),float(lo),70,140); im=Image.fromarray(np.asarray(shade(z,sc))).convert('RGB').resize((S-4,S-4),Image.LANCZOS)
    except Exception as e:
        im=Image.new('RGB',(S-4,S-4),(60,0,0))
    x=(i%cols)*S; y=(i//cols)*S; o.paste(im,(x+2,y+2)); c=(x+S//2,y+S//2)
    for dx,dy in ((-22,0),(22,0),(0,-22),(0,22)): d.line((c[0]+dx*0.45,c[1]+dy*0.45,c[0]+dx,c[1]+dy),fill=(255,0,160),width=2)
    d.rectangle((x+2,y+2,x+60,y+16),fill=(0,0,0)); d.text((x+5,y+3),lab,fill=(255,255,120))
o.save(sys.argv[1],quality=85); print(o.size)
