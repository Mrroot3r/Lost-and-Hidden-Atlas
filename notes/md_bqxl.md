# md_bqxl: Harford County, Maryland: Susquehanna canal, mills and meeting houses
state: Maryland
region: md
date: 2026-11-19
places: 16
file: data_md_bqxl.py

## What this batch is
Sixteen places in Harford County, Maryland, the first on the map there: Jerusalem Mill Village and the Jericho Covered Bridge on the Little Gunpowder; in Susquehanna State Park the Rock Run Grist Mill, the Carter-Archer House, the Jersey Toll House with the river piers of the 1817 bridge, the Stafford Flint Furnace, Lock 8 and the Deer Creek dam remains, and Lock 9 at the vanished town of Lapidum; in Havre de Grace the Concord Point Lighthouse and the canal Lock House; and Deer Creek Friends Meetinghouse, Holy Trinity at Churchville, St. Ignatius at Hickory, Tudor Hall, the Hays House and Ladew Topiary Gardens. Wikipedia was read with `wiki_raw.py` (the county's Register list with `--rows`); Maryland DNR pages and the DNR Rock Run walking-tour PDF, HMdb marker pages (Maryland State Parks' own signs at Rock Run, Lapidum, Deer Creek and Stafford), NPS, the museums' and Ladew's own pages, Baltimore Yearly Meeting, the Historical Society of Harford County, a Harford County press release and the Catholic Review were read with `page.py`. Not checked: Tudor Hall's museum hours, St. Ignatius and Holy Trinity service times and interiors, whether the Jersey Toll House opens inside, and the Rock Run mill's current open days (the DNR leaflet's weekend hours are undated; the history page gives none). Lock 8 and Lock 9 are pinned at the State Parks markers beside them, not on the stonework. The Ladew pin is on the garden lawn; which building is the 1749 manor house was not settled. Brick: one picture opened (Jerusalem Mill: stone and painted board with a red brick chimney, `some`); the Lock House, Concord Point keeper's house, Stafford furnace and Ladew are `?`.

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Broad Creek Soapstone Quarries | Whiteford, MD (no coordinate) | Register listing 75000903 | Address restricted (archaeology): needs a source that the public may visit, and a position |
| Husband Flint Mill Site | Kalmia, MD (no coordinate) | Register listing 75000902 | Address restricted; no position or access source |
| Priest Neal's Mass House and Mill Site | Bel Air, MD (39.598611, -76.259167) | Register listing 90000352; St. Ignatius marker names the Jesuit house of St. Joseph at Priest's Ford | Owner and whether anything can be seen from a public road |
| Harford Furnace Historic District | Bel Air, MD (39.493333, -76.260556) | Register listing 90001020 | Whether any furnace remains survive, and access; MHT form not read |
| Ma & Pa Railroad remains, Forest Hill | Forest Hill, MD (39.58469, -76.38609) | HMdb 187768: Ma & Pa station site, line closed 1958 | What survives on the ground and the county trail's access page |
| Pooles Island Light | Edgewood, MD (39.2905, -76.2664) | Register 97000060, Wikipedia article | On Aberdeen Proving Ground: whether any public view or boat access is allowed |
| Gunpowder and Presbury meetinghouses | Aberdeen Proving Ground, MD (39.4036, -76.3081; 39.3875, -76.3067) | Register listings 74000954, 74000955 | Inside a closed army post: whether visits are ever allowed |

## Tips
- `start.py "Bel Air, Maryland"` geocoded to a hamlet called Bel Air in Allegany County, 200 km west; use `nearby.py <lat> <lon>` or give the county ("Bel Air, Harford County, Maryland").
- The Maryland State Parks markers on HMdb (Rock Run, Lapidum, Deer Creek, Stafford) quote the park's own signs in full and give a position; one HMdb nearby list round Rock Run gave nearly every Susquehanna State Park place.
- DNR's `parkinfo.aspx?parkname=<park>` page gives a street address for each historic building and area in a park, and the hours by area.
- `osmnear.py ... buildings` named the right building every time here (Jerusalem Mill museum, St. Ignatius historic church beside the new one); the OpenStreetMap protected-area or park points from `nom.py` fell in fields and woods.
- The St. Ignatius parish site (`2610.sites.ecatholic.com`) answered 403 with no archived copy.
