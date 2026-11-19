# vtn_kfjq: Addison County, Vermont
state: Vermont
region: vtn
date: 2026-11-19
places: 19
file: data_vtn_kfjq.py

## What this batch is
Nineteen places in Addison County, Vermont (region vtn drawn at random by `choose.py`), nearly all standing: on the lake shore the Chimney Point tavern, the John Strong mansion, Hawley's ferry house in Kingsland Bay State Park, the Larrabee's Point ferry landing and 1823 warehouse, and the Chipman's Point warehouses and burned-hotel foundations; inland the East Shoreham covered railroad bridge, the Old Stone Blacksmith Shop in Cornwall, Middlebury's Frog Hollow stone mill and Old Stone Row, the Pulp Mill covered bridge, the Rattling Bridge between Weybridge and New Haven, the Robert Frost farm in Ripton, Rokeby, the Ferrisburgh Union Meetinghouse, the two Starksboro meeting houses, the Hoag gristmill, the moved New Haven Junction depot and the Leicester meeting house. Facts are from Wikipedia read with `wiki_raw.py` (the county's Register list with `--rows`), one HMdb marker, Addison Independent and WCAX news pages, and the managers' pages read with `page.py` (Vermont State Historic Sites, Vermont State Parks, the DAR mansion site, Rokeby's visit page). Not checked: Chimney Point's 2027 days and fees (the state page only says closed for the season), the Stone Mill's hours (its site answers 403), the Frost farm rules (only Wikipedia says the grounds are open in daylight), the Larrabee ferry times, and every interior marked so. Pins that are not on the thing itself: the Old Stone Blacksmith Shop (on VT 30 beside it, area), Hawley's ferry house (middle of the park buildings, site), the New Haven Junction depot (on the library it was moved beside, site). Red brick was read from the Wikipedia picture for the six brick buildings; Larrabee's Point is left '?' (the picture shows only the stone warehouse, not the brick house).

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Hand's Cove blockhouse | Shoreham, VT (43.8672, -73.3656) | Where Allen and Arnold crossed to take Ticonderoga in 1775; a dovetailed log blockhouse on an old stone base and a brick Greek Revival Hand house (Wikipedia) | Who owns it now and whether anyone may see it; looks private |
| Halpin Covered Bridge | Middlebury, VT (44.05, -73.14111) | 1850 Town lattice, 41 ft above the Muddy Branch, the highest covered bridge in the state; serves only the Halpin farm (Wikipedia) | Whether Halpin Bridge Road is a public road to the bridge |
| Middlebury Gorge Concrete Arch Bridge | East Middlebury, VT (43.97, -73.08639) | 1924 arch on VT 125 that outlived the 1927 flood (Wikipedia) | A safe place to stop and see it from |
| Fort Cassin | Ferrisburgh, VT (mouth of Otter Creek) | War of 1812 battery; no Wikipedia article under that title | A source and what is left |

## Tips
- `vermontbridges.org` county pages answer 404; `stonemillvt.com` answers 403 to `page.py`.
- The Vermont State Historic Sites hours page drops a site's dates once its season ends ("closed for the season"); the season's opening day came from a WCAX story.
- Several Addison County Register coordinates were off the building (Chimney Point on the bridge road, Hawley's in the bay, Rattling Bridge 190 m into woods, Union Meetinghouse on US 7); `osmnear.py ... buildings` and the highways layer's `bridge=yes` found the right spot.
- In this session the whole job ran without the web fetch tool: `page.py`, `wiki_raw.py` and search results were enough.
