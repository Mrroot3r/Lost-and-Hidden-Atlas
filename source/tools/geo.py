import json,urllib.request,urllib.parse,time,sys
UA={'User-Agent':'lost-hidden-atlas-research/1.0'}
def arc(q):
    u='https://geocode.arcgis.com/arcgis/rest/services/World/GeocodeServer/findAddressCandidates?'+urllib.parse.urlencode({'SingleLine':q,'f':'json','maxLocations':1,'outFields':'Addr_type,Match_addr','searchExtent':'-75.2,41.6,-73.2,44.3'})
    j=json.load(urllib.request.urlopen(urllib.request.Request(u,headers=UA),timeout=30))
    c=j.get('candidates') or []
    if not c: return None
    c=c[0]; return (round(c['location']['y'],5),round(c['location']['x'],5),c['attributes'].get('Addr_type'),c['score'],c['address'])
def gnis(name):
    w=f"gaz_name = '{name}' AND state_alpha = 'NY'"
    out=[]
    for lyr in range(0,20):
        pass
    return out
if __name__=='__main__':
    qs=json.load(open(sys.argv[1]))
    res=json.load(open(sys.argv[2])) if len(sys.argv)>2 and __import__('os').path.exists(sys.argv[2]) else {}
    for k,q in qs.items():
        if k in res: continue
        try: res[k]=arc(q)
        except Exception as e: res[k]=['ERR',str(e)]
        print(k,'|',q,'->',res[k]); time.sleep(0.15)
    json.dump(res,open(sys.argv[2],'w'),indent=0)
