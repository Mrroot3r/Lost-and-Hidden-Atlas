# sar_pgzb: Saratoga County: Round Lake to Schuylerville
state: New York
region: sar
date: 2026-11-19
places: 20
file: data_sar_pgzb.py

## What this batch is
Twenty places in Saratoga County, drawn at random by `choose.py` (region `sar`, which offered Round Lake and Malta). The region had mostly gone hotels and canal locks, so this batch is mostly what stands: the Round Lake camp-meeting village and Auditorium (with the 1847 Davis-Ferris organ), the 1888 Ruhle Road lenticular truss (moved from Salem in 2001) and the Dunning Street Cemetery in Malta, Brookside and the Union Mill in Ballston Spa, and in Saratoga Springs the gasholder house, the 1915 trolley Drink Hall (visitor center), Yaddo's gardens, the Gideon Putnam Burying Ground, the Spa park bathhouses, and the Canfield Casino and Grant Cottage, which replace the thin pins `lm-canfield-casino-and-congress-park` and `lm-grant-cottage`. Further east: the Saratoga battlefield (pin on the Neilson House), the Schuyler House, the Saratoga Monument with Victory Woods, the Old Saratoga Reformed Church, St. Stephen's and the Bullard Block in Schuylerville, and Stillwater United Church; and the Copeland covered bridge in Edinburg. Sources: Wikipedia through `wiki_raw.py`; the Ruhle Road Register form (historicbridges.org copy); NPS hours, directions and place pages; NYS Parks; the Round Lake Auditorium, Brookside, Saratoga Springs History Museum, Grant Cottage and Discover Saratoga pages; the NYS Covered Bridge Society and Visit Sacandaga; New York by Rail for Yaddo; CNY Hiking for what is seen at the battlefield stops. Every pin was looked at on the aerial (and the LiDAR sheet); four were moved (Grant Cottage, Copeland bridge and the Old Saratoga Reformed Church to OpenStreetMap points, and the Putnam burying ground off a house with `pix.py`). Red brick: four settled from Wikipedia photographs with `brick.py look` (Canfield Casino, Bullard Block and the Reformed church red brick, Schuyler House clapboard); six left at `'?'`. Not checked: anything on the ground; Yaddo's hours are from New York by Rail, not Yaddo (yaddo.org refused); parking at Round Lake, Ruhle Road, Dunning Street, the Copeland bridge and the Putnam ground; whether the gasholder site is still fenced and empty in 2026 (the aerial shows the round building on an open paved lot); who owns the land at the Ruhle Road bridge; interiors of the churches and the Union Mill.

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Marshall House | Schuylerville, NY, west of NY 32 a mile north of the village (Wikipedia 43.11111, -73.58056) | Wikipedia: 1770–73 farmhouse, British field hospital in 1777 and Baroness Riedesel's refuge; cannonball damage kept; owned and lived in by the Bullard family since 1930 | Up a long private drive; whether anything can be seen from the road, and whether the owners still show it |
| Victory Mills | Victory, NY (43.08908, -73.59188) | Wikipedia: 1918 cotton mill, burned May 31, 2025 and demolished | Nothing left to see; listed so nobody adds it |
| Grooms Tavern Complex | Grooms Corners, Clifton Park, NY (42.83472, -73.84472) | Wikipedia: about 1825 tavern and store, 1840s wagon and blacksmith shop | Owner and present use; whether it is seen from the road |
| Saratoga Surrender Site | US 4 half a mile south of Schuylerville | Wikipedia: 19-acre park owned by the Open Space Institute, run by the NPS since 2021, dawn to dusk, plaques and two cannon | A coordinate and the NPS page; mostly markers |
| Jonesville Store | Jonesville, Clifton Park, NY (42.91028, -73.82333) | Wikipedia: about 1860 country store and post office, still a store | Present use (the Register list calls it vacant, Wikipedia a store) |

## Tips
- The NPS Saratoga hours page (`nps.gov/sara/planyourvisit/hours.htm`) gives every unit's season in one place; `nps.gov/places/schuyler-estate.htm` is the Schuyler House page (the obvious `schuyler-house.htm` is 404).
- The Drink Hall's Wikipedia coordinate is about 1 km off; OpenStreetMap's point for 297 Broadway is on it. The Gideon Putnam Burying Ground's Register point is on a house across South Franklin Street.
- `yaddo.org` refuses `page.py` (403) and `yaddogardens.org` would not connect.
- `brooksidemuseum.org/visit/` has the Saratoga County History Center's hours in one line.
