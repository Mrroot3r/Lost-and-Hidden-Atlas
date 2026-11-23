# Which old survey sheet a sweep may read for buildings, and how a sheet is read. One place for the numbers, used by
# lidar_sweep.py (which sheets) and lidar_buildings.py (how), and checked by lidar_test.py.
#
# New York and Massachusetts were surveyed at 1:62,500 before 1915, and that is all a sweep there reads. Round Kansas City the
# first surveys are 1:125,000 sheets of the 1890s, too coarse to show a house, and the first detailed sheets came between 1910
# and 1936, some at 1:62,500, some at 1:48,000 or 1:24,000. The owner's rule for Missouri and Kansas (November 23, 2026): a sheet
# up to 1936 is old enough; a later one is not, because a building on it need not be old.
import re
def rule(text):
    """'1936,any' -> (1936, True): the latest year a sheet may have, and whether scales more detailed than 1:62,500 count."""
    text=text or '1915'
    return int(text.split(',')[0]), text.endswith(',any')
def sheet_ok(year,scale,last,anyscale):
    return year<=last and (scale<=62500 if anyscale else scale==62500)
def reading(tif):
    """How a sheet is read, from its file name. The finder looks for a solid black square. On a 1:62,500 sheet read at 2.5 m a pixel
    a building symbol is about 12 pixels; a more detailed sheet is read at a finer step in proportion, so the symbol comes out
    about the same size. Those sheets draw roads heavier for the size of a building: read with the old rule, Missouri's 1936
    Kearney sheet (1:48,000) gave 71 "buildings" in a 4 km square, most of them road junctions, railway ticks and lettering; with a
    wider opening, a fuller and squarer shape and paper round it, 23, nearly all the map's own squares. The 1:62,500 sheets are
    read exactly as they always were."""
    m=re.search(r'_(\d+)_geo\.tif$',tif); scale=int(m.group(1)) if m else 62500
    strict=scale!=62500
    return {'res':2.5*min(1.0,max(0.38,scale/62500.0)),'strict':strict,'open':8 if strict else 6,'top':22 if strict else 20,'fill':0.7 if strict else 0.6}
def keeps(w,h,fill,ring,rd):
    """Is a solid mark w by h pixels a building? fill: how much of its box is ink. ring: how much of a 6-pixel band round it is ink."""
    if not(rd['open']<=h<=rd['top'] and rd['open']<=w<=rd['top']) or fill<rd['fill']: return False
    if not rd['strict']: return True
    # a building stands alone and is nearly square. A junction, a tick or a serif has ink carrying on round it; a building has
    # paper, though a big solid square may have a lane at its door (seen on the 1933 Blue Springs sheet)
    if max(w,h)/min(w,h)>1.6: return False
    return ring<=(0.18 if min(w,h)>=13 and fill>=0.8 else 0.12)
