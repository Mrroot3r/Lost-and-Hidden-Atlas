"""Who owns the ground under a point, from the state's own tax-parcel file. New York and Massachusetts; for Missouri only the
parcels the state owns; for Kansas nothing (neither state has a file for the whole state).
   python3 tools/parcel.py [--state ny|ma|mo|ks] <lat> <lon> [<lat> <lon> ...]
Prints the owner TYPE and property class, never the owner's name: names of private owners do not go in the repository.
Without --state the state is taken from the coarse outlines (good to a kilometre or two at a border).

New York (NYS Tax Parcels Public; only some counties publish owner names): owner name starting "NYS"/"State of New
York" is state land; class 9xx is public or conservation land.

Massachusetts (MassGIS standardized assessors' parcels, every town): the state's own use-code table, read from the
layer in November 2026, gives 900 United States; 901 and 910-929 the Commonwealth (910/920 DCR parks and forests,
911/921 Fish and Game, 915/925 DCR water supply land); 902-903, 930-939, 980-989 and 991-994 towns, cities, counties
and districts; and 904-908, 940-979, 990 and 995-996 private schools, charities (950: conservation organizations),
churches, housing and utility authorities, and 121A corporations. Those last are tax-exempt but NOT public land, so
they are reported apart: a land trust's reservation may be open to walkers, a church lot is not."""
import sys,os,re,requests
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from lidar_dem import state_of
NY='https://services6.arcgis.com/EbVsqZ18sv1kVJ3k/arcgis/rest/services/NYS_Tax_Parcels_Public/FeatureServer/1/query'
MA='https://services1.arcgis.com/hGdibHYSPO59RG1h/ArcGIS/rest/services/Massachusetts_Property_Tax_Parcels/FeatureServer/0/query'
MA2='https://arcgisserver.digital.mass.gov/arcgisserver/rest/services/AGOL/L3Parcels_feature_service/FeatureServer/0/query'     # the state's own server, same layer
COMM=re.compile(r"COMMONWEALTH|COMMONWLTH|COMM\.? OF MASS|STATE OF MASS|^MASS(ACHUSETTS)?,? (COMM|DEPT|DIV|DEPARTMENT|DIVISION)|DEP(T|ARTMENT)\.? OF (CONSERV|ENVIRON|FISH)|DIV(ISION)?\.? OF (FISH|STATE PARKS|WATER)")
def ma_kind(owner,code):
    """The owner type of a Massachusetts parcel from its owner name and state use code."""
    o=(owner or '').upper().strip(); c=(code or '').strip()
    if COMM.search(o): return 'STATE LAND'
    if c[:2] in ('91','92') or c[:3]=='901': return 'public land (use code 9xx: the Commonwealth)'
    if c[:3] in ('900','902','903','991','992','993','994') or c[:2] in ('93','98'): return 'public land (use code 9xx: federal, town, city or county)'
    if c[:1]=='9': return 'tax-exempt but not government (use code 9xx: a land trust, charity, school, church or authority)'
    if not o and not c: return 'owner not published'
    return 'PRIVATE'
MO='https://gis.mo.gov/arcgis/rest/services/OA/FMDCrealEstate_StateOwnedParcels/MapServer/1/query'      # "State Owned Property": the parcels the state owns, from the counties that give theirs
def mo_kind(owner):
    """Missouri publishes no parcel file for the whole state, only the parcels the state itself owns (Office of Administration, from
    the counties that supply theirs). A point on one is state land. A point on none is NO ANSWER, never "private": the county may
    simply not be in the file (Jackson County's conservation areas are not), and federal land (the Corps of Engineers' lakes) never is."""
    o=(owner or '').upper().strip()
    if not o: return None
    if re.search(r'CURATORS|UNIVERSITY|COLLEGE',o): return 'public land (in Missouri\'s file of state-owned property: a university or college, whose grounds are not a park)'
    if re.search(r'MISSOURI|^MO\b|^STATE OF|CONSERVATION COMMISSION|DEP(T|ARTMENT)\.? OF (NATURAL|CONSERVATION)',o): return 'STATE LAND'
    return 'public land (in Missouri\'s file of state-owned property)'
def q(url,la,lo,fields):
    return requests.get(url,params={'geometry':f'{lo},{la}','geometryType':'esriGeometryPoint','inSR':4326,'spatialRel':'esriSpatialRelIntersects','outFields':fields,'returnGeometry':'false','f':'json'},timeout=60).json().get('features',[])
def look(la,lo,st):
    """One printed line for a point; the part after '->' is read by tools/lidar.py check."""
    if st=='mo':
        fs=q(MO,la,lo,'NAME1,COUNTY,GIS_ACRES'); p=fs[0]['attributes'] if fs else {}; kind=mo_kind(p.get('NAME1'))
        if not kind: return f'{la} {lo} no parcel record (Missouri publishes only state-owned parcels, and none is here: the public-land record decides)'
        return f"{la} {lo} -> {kind} | class state-owned | {round(p.get('GIS_ACRES') or 0,1)} acres | {(p.get('COUNTY') or '').title()} County | "
    if st=='ks': return f'{la} {lo} no parcel record (Kansas publishes no parcel file for the whole state: the public-land record decides)'
    if st=='ma':
        F='OWNER1,USE_CODE,LOT_SIZE,LOT_UNITS,CITY,SITE_ADDR,POLY_TYPE'
        try: fs=q(MA,la,lo,F)
        except Exception: fs=q(MA2,la,lo,F)
        fs=[f for f in fs if (f['attributes'].get('POLY_TYPE') or '') in ('FEE','TAX','')] or fs
        if not fs: return f'{la} {lo} no parcel record (the point is on a road, a railway or water)'
        p=fs[0]['attributes']; kind=ma_kind(p.get('OWNER1'),p.get('USE_CODE')); ac=p.get('LOT_SIZE')
        try: ac=round(float(ac)/(43560.0 if (p.get('LOT_UNITS') or 'A').upper().startswith('S') else 1.0),1)
        except Exception: ac=None
        return f"{la} {lo} -> {kind} | class {p.get('USE_CODE')} | {ac} acres | {(p.get('CITY') or '').title()} | {(p.get('SITE_ADDR') or '').title() if kind!='PRIVATE' else 'address withheld'}"
    fs=q(NY,la,lo,'PRIMARY_OWNER,PROP_CLASS,ACRES,MUNI_NAME,OWNER_TYPE,PARCEL_ADDR')
    if not fs: return f'{la} {lo} no parcel record (the county may not publish, or the point is on a road)'
    p=fs[0]['attributes']; o=(p.get('PRIMARY_OWNER') or '').upper()
    kind='STATE LAND' if o.startswith(('NYS','STATE OF NEW YORK','NEW YORK STATE','PEOPLE OF THE STATE')) else ('public or conservation land (class 9xx)' if str(p.get('PROP_CLASS','')).startswith('9') else ('owner not published' if not o else 'PRIVATE'))
    return f"{la} {lo} -> {kind} | class {p.get('PROP_CLASS')} | {p.get('ACRES')} acres | {p.get('MUNI_NAME')} | {(p.get('PARCEL_ADDR') or '') if kind!='PRIVATE' else 'address withheld'}"
if __name__=='__main__':
    a=sys.argv[1:]; st=None
    if a[:1]==['--state']: st=a[1].lower(); a=a[2:]
    for i in range(0,len(a)-1,2):
        la,lo=a[i],a[i+1]
        try: print(look(la,lo,st or state_of(float(la),float(lo)) or 'ny'))
        except Exception as e: print(la,lo,'lookup failed:',str(e)[:60])
