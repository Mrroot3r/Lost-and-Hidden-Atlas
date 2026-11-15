import sys,json
sys.path.insert(0,'tools')
from img import panel
from PIL import Image, ImageDraw
from concurrent.futures import ThreadPoolExecutor
def sheet(name,sites,S=480,per_row=2):
    # sites: list of (label,lat,lon,hw,layerA,layerB)
    jobs=[]
    for s in sites:
        for lyr in (s[4],s[5]):
            jobs.append((lyr,s[1],s[2],s[3],S,True,f"{s[0]} {lyr} hw{s[3]}"))
    with ThreadPoolExecutor(6) as ex: ims=list(ex.map(lambda a: panel(*a),jobs))
    rows=(len(sites)+per_row-1)//per_row
    out=Image.new('RGB',(S*2*per_row,S*rows))
    for k,im in enumerate(ims):
        site=k//2; r=site//per_row; c=(site%per_row)*2+(k%2)
        out.paste(im,(c*S,r*S))
    out.save(f'img/{name}.jpg',quality=80); print('saved',name,out.size)
if __name__=='__main__':
    spec=json.load(open(sys.argv[1]))
    for name,sites in spec.items(): sheet(name,sites)
