#!/usr/bin/env python3
"""UTM to latitude and longitude. Older National Register forms give a place only as a UTM reference.
   python3 tools/utm.py 15 584500 3946200            zone, easting, northing (northern hemisphere)
   python3 tools/utm.py "15/584500/3946200"          the way the forms often write it
NAD27 forms (most before about 1985) differ from today's maps by up to a few tens of metres in the east and by up to
100 m in the west: treat the result as near the place, and look at the pin on the aerial before using it."""
import sys,math,re
def to_ll(zone,e,n):
    a=6378137.0; f=1/298.257223563; k0=0.9996; e2=f*(2-f); ep2=e2/(1-e2)
    x=e-500000.0; y=n; M=y/k0
    mu=M/(a*(1-e2/4-3*e2**2/64-5*e2**3/256)); e1=(1-math.sqrt(1-e2))/(1+math.sqrt(1-e2))
    p=mu+(3*e1/2-27*e1**3/32)*math.sin(2*mu)+(21*e1**2/16-55*e1**4/32)*math.sin(4*mu)+(151*e1**3/96)*math.sin(6*mu)+(1097*e1**4/512)*math.sin(8*mu)
    C1=ep2*math.cos(p)**2; T1=math.tan(p)**2; N1=a/math.sqrt(1-e2*math.sin(p)**2); R1=a*(1-e2)/(1-e2*math.sin(p)**2)**1.5; D=x/(N1*k0)
    lat=p-(N1*math.tan(p)/R1)*(D**2/2-(5+3*T1+10*C1-4*C1**2-9*ep2)*D**4/24+(61+90*T1+298*C1+45*T1**2-252*ep2-3*C1**2)*D**6/720)
    lon=(D-(1+2*T1+C1)*D**3/6+(5-2*C1+28*T1-3*C1**2+8*ep2+24*T1**2)*D**5/120)/math.cos(p)
    return math.degrees(lat),(zone-1)*6-180+3+math.degrees(lon)
if __name__=='__main__':
    v=[float(x) for x in re.split(r'[\s/,]+',' '.join(sys.argv[1:]).strip()) if x]
    if len(v)!=3: sys.exit(__doc__)
    la,lo=to_ll(int(v[0]),v[1],v[2]); print('%.5f, %.5f'%(la,lo))
