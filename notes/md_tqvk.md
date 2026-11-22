# md_tqvk: Maryland: a first scatter, mountains to the Eastern Shore
state: Maryland
region: md
date: 2026-11-22
places: 20
file: data_md_tqvk.py

## What this batch is
Twenty places spread over Maryland, which had 34, nearly all in Frederick and Harford counties: Allegany (Paw Paw Tunnel, Lonaconing furnace), Garrett (Casselman River Bridge, Stanton's Mill, Oakland B&O station), Washington (Fort Frederick, Dunker Church), Howard and Baltimore (Thomas Viaduct, Patterson Viaduct ruins, Bollman truss bridge, Ellicott City B&O station, Phoenix Shot Tower), the Eastern Shore (Old Wye Mill, Old Wye Church, Third Haven Meeting House, Nassawango furnace at Furnace Town, Teackle Mansion) and Southern Maryland (Point Lookout lighthouse and prison camp, Cove Point Lighthouse, Sotterley). Facts come from Wikipedia read as raw text and from the managing bodies' own pages: NPS (C&O Canal, Antietam), Maryland DNR (Fort Frederick, Casselman, Patapsco Valley, Point Lookout), Howard County, Calvert County, Old Wye Mill, Furnace Town, Historic Sotterley, Third Haven Friends Meeting, Spruce Forest Artisan Village, Garrett County museums, HMdb and Clio. Every pin was looked at on the aerial with bare-ground shading; three were moved to OpenStreetMap points (Oakland station, Sotterley, Stanton's Mill) because the Wikipedia coordinate fell in woods or a field. Not checked: anything on the ground; interiors; hours for Teackle Mansion, Cove Point Lighthouse and the Oakland station (`hours='?'`; the Garrett County society's Wednesday to Saturday hours may or may not cover the station); Point Lookout lighthouse days come from Wikipedia, not a park page; the Old Wye Church's services; fees at Antietam, Point Lookout and Patapsco; Savage Park hours. Casselman River Bridge State Park was closed for repairs when read (November 22, 2026), so that place is view-only. The Paw Paw Tunnel pin is over the middle of the tunnel, not a portal; Lonaconing's and Nassawango's stacks could not be picked out under trees. The Bollman bridge's date is given two ways (1852 and moved, or 1869), the Ellicott City station's two ways (1830 or 1831), and the Point Lookout death toll two ways (nearly 4,000 or more than 3,000).

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Old Trinity Church, Church Creek | Church Creek, Dorchester County, MD | Often named as one of the oldest churches in use in the country (memory only; not read) | No Wikipedia title found and not in the Dorchester Register list rows; a source and a coordinate |
| Bloomington Viaduct | Bloomington, Garrett County, MD (39.476944, -79.068056) | National Register listing 76000996 (Register list row) | What stands and where to see it from |
| Kaese Mill | Accident, Garrett County, MD (39.650556, -79.296944) | National Register listing 84001782 (Register list row) | Any description, owner, whether it can be seen from the road |
| Hooper Island Light | Hoopersville, Dorchester County, MD (38.256111, -76.25) | Register listing 02001426 | Offshore; whether it can be seen from land or by a tour boat |
| Tomlinson Inn and the Little Meadows | Grantsville, Garrett County, MD (39.693611, -79.096111) | Register listing 73000920, an inn on the National Road | Description, owner, what can be seen |

## Tips
- dnr.maryland.gov park pages read well with `page.py`; the hours often sit in a side box that only `page.py --all` shows ("9 a.m. to sunset" on the Patapsco page).
- The Howard County museum page (howardcountymd.gov/ecborail) prints its hours only with `--all`; the `-g` filter misses them.
- garrettcountymuseums.com is drawn by script; `page.py` still got the hours line.
- Several Wikipedia coordinates in rural Maryland were off the building (Oakland station, Sotterley, Stanton's Mill); `nom.py` found all three.
