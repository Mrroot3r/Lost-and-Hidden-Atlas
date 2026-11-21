# ms_mlkd: Mississippi: a first scatter from the Gulf Coast to the Delta and the northeast hills
state: Mississippi
region: ms
date: 2026-11-21
places: 15
file: data_ms_mlkd.py

## What this batch is
Fifteen places spread across Mississippi away from the Port Gibson and Natchez river country (batch ms_lwtt), claimed with `choose.py --thinnest` (Mississippi had 21 places). Gulf Coast: Biloxi Lighthouse, Beauvoir, the LaPointe-Krebs House (1757, the state's oldest building). Delta: the ruins of Bryant's Grocery at Money, the Tallahatchie County courthouse at Sumner (Emmett Till trial), Dockery Farms. Vicksburg: the Old Warren County Courthouse museum and the USS Cairo gunboat. Grenada: a Confederate fort of the Yalobusha line at Grenada Lake. Meridian: the Highland Park Dentzel carousel. Columbus and West Point: Friendship Cemetery and Waverley. North: Rowan Oak (Oxford), Montrose (Holly Springs), the CCC works and swinging bridge at Tishomingo State Park. Sources were read with `wiki_raw.py` and `page.py`: the City of Biloxi, visitbeauvoir.org, rowanoak.com, oldcourthouse.org, mdwfp.com and its trail brochure, NPS pages (Till monument, Vicksburg fees), MDAH and SAH Archipedia (Dockery), the Gulf Coast heritage area and WLOX (LaPointe-Krebs), the American Battlefield Trust (Waverley, Grenada), HMdb (Bryant's Grocery, Grenada fort), NPR 2019 and 2023 (Bryant's Grocery), the Meridian Star 2017 (carousel). Pictures for five places were chosen with `photo_find.py`. Not checked: nothing on the ground. Hours not found on a managing body's page for LaPointe-Krebs (WLOX says seven days), the Tallahatchie courthouse and USS Cairo (NPS hours pages are drawn by script and came back empty), the carousel (only a 2017 newspaper), Waverley (no owner's page found), Tishomingo park hours, Grenada Lake, Friendship Cemetery. Beauvoir's page gives tour times but not days. Rowan Oak's parking was not checked. Owner of Bryant's Grocery not checked. Pins that are not on the thing: Montrose (on Salem Avenue at the address point; which house it is was not seen), Grenada fort (the HMdb marker position, in woods; Commons photos of the fort are geotagged about 90 m away), Tishomingo (OSM footbridge, prec area), Waverley (ArcGIS point on a large house, not confirmed as the mansion; Wikipedia's coordinate is in woods). Brick from pictures opened: Biloxi Lighthouse 'no' (white tower), Montrose 'yes' (Commons photo), Tishomingo 'no' (stone towers); Beauvoir 'some' from the Wikipedia text (red-brick piers); the rest '?'.

## Leads
Places you read about and could not finish. One row each; delete the example row. Leave the table header.

| Place | Where | What is known | What is missing |
|---|---|---|---|
| Fort Massachusetts, Ship Island | West Ship Island, MS (30.21247, -88.97280, checked on the aerial) | Brick fort 1859–1866, NPS Gulf Islands National Seashore; ferry from Jones Park, Gulfport mid-March to October; fort Wednesday to Sunday 10:15 a.m. to 2:15 p.m. in season (nps.gov Ship Island page) | Written up in full, but `check.py` refuses the pin: Mississippi's outline does not take in the barrier islands. Needs the outline widened (a tool change, for the maintainer), then the entry can go in as it stood in this session's workspace |
| Dockery Farms tours | Dockery, MS | Foundation manages the site (MDAH) | dockeryfarms.org now carries unrelated pages; a working contact for tours |
| Corinth (Civil War earthworks, contraband camp) | Corinth, MS | Not researched; no Atlas place in the northeast corner except Tishomingo | Sources |

## Tips
- Mississippi's outline leaves out Ship Island and the other Gulf barrier islands, so `check.py` errors on any pin there; find this before writing up an island place.
- NPS "hours" pages (till, vick) are drawn by script: `page.py` reads only the title. The places pages (`nps.gov/places/...`) and the park's planyourvisit page for a unit (Ship Island) read fine.
- `photo_find.py look` doubles as a pin check: Commons photos geotagged 27 to 90 m from a woods pin (Tishomingo, Grenada) confirmed what the aerial could not show.
- For a Mississippi house with no owner's page, the ArcGIS geocoder's POI hit (Waverly Mansion) was closer than Wikipedia's coordinate.
