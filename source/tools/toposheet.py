import sys,json
from PIL import Image, ImageDraw
M=json.load(open('build/topo/meta.json'))
def sheet(name,ids,S=480,cols=4):
    rows=(len(ids)+cols-1)//cols
    out=Image.new('RGB',(S*cols,S*rows),(40,40,40))
    for k,i in enumerate(ids):
        try: im=Image.open(f'build/topo/{i}.webp').convert('RGB').resize((S,S))
        except Exception as e: continue
        d=ImageDraw.Draw(im); c=S//2
        d.ellipse((c-10,c-10,c+10,c+10),outline=(255,0,255),width=2)
        m=M[i]; hwm=(m['b'][2]-m['b'][0])*111320/2
        d.rectangle((0,0,S,14),fill=(0,0,0)); d.text((3,1),f"{i} {m['y']} hw~{hwm:.0f}m",fill=(255,255,0))
        out.paste(im,((k%cols)*S,(k//cols)*S))
    out.save(f'img/{name}.jpg',quality=85); print(name,out.size)
ids=sys.argv[2:]
sheet(sys.argv[1],ids)
