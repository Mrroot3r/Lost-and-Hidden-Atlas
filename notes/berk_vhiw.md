# berk_vhiw: Southern Berkshires, Massachusetts
state: Massachusetts
region: berk
date: 2026-11-19
places: 20
file: data_berk_vhiw.py

## What this batch is
Twenty places in southern Berkshire County, where the Atlas had nothing between Richmond and the Connecticut line: in Sheffield the 1735 Ashley House, the 1760 Old Parish Church and the Old Covered Bridge (a 1996 replica; sources give 1837 and 1854 for the original); in Great Barrington the W. E. B. Du Bois Boyhood Homesite (foundation and staked house outline), the Clinton A.M.E. Zion Church (under restoration), the Mahaiwe Theater, Searles Castle, Monument Mills and the Rising Paper Mill in Housatonic; in Stockbridge the Mission House, Naumkeag, Chesterwood and the Glendale Power House; the Shaker Mill in West Stockbridge; the Bidwell House in Monterey and, on its trails, the site of Township No. 1's first meeting house (1740s to 1790s); Santarella and the Shaker settlement in Tyringham; the Jug End Barn resort site in Egremont; and the 1839 Montville Baptist Church (Sandisfield Arts Center). Sources: Wikipedia through wiki_raw.py, HMdb marker pages and nearby lists through page.py, the owners' own pages (The Trustees, Bidwell House Museum, duboisnhs.org, chesterwood.org), and a DCR flyer for Jug End read with the web fetch tool. Not checked: anything on the ground; what survives at the meeting house site and Jug End (pins: the meeting house site is an OpenStreetMap point in woods, Jug End is the reservation parking lot); Jug End hours and rules (DCR page refused); hours for the Clinton church, the Shaker Mill bookshop, the Sandisfield Arts Center and the Old Parish Church; which Tyringham Shaker buildings survive (pin is the farm cluster on the road, area only); whether the Rising Paper Mill still runs; the date of the Berkshire Edge article that calls Monument Mills vacant. Interiors not checked for the Mission House, the Old Parish Church, the Mahaiwe and the Clinton church after restoration. Red brick: yes for the Rising Paper Mill, no for seven places whose sources name their material, '?' for the rest.

## Leads
Places you read about and could not finish. One row each.

| Place | Where | What is known | What is missing |
|---|---|---|---|
| Bidwell House grounds: sugar house chimney, cellar holes, charcoal hearth | Monterey, MA (42.21011, -73.21748 sugar house; 42.20766, -73.22123 Bidwell cellar hole) | OpenStreetMap maps a 19th-century sugar house chimney and foundation, the "ca 1750s cellar hole of Rev. Adonijah Bidwell", the McCollum cellar hole and a charcoal hearth on the museum's land; the museum's trail page says its land holds cellar holes, walls and roads | A source naming each, and a look on the ground or the LiDAR |
| Benjamin Osborn House | Mount Washington, MA (42.117222, -73.47) | On the Register list, marked "Destroyed" | Whether anything is left, and who owns the land |
| First Court House of Berkshire County | Great Barrington, MA (42.19379, -73.363194) | HMdb marker: court house built 1764, scene of open resistance on August 16, 1774; marker in front of Town Hall | Nothing stands; only a marker |
| Last battle of Shays' Rebellion | Great Barrington, MA (42.146808, -73.385802) | HMdb: 1904 marker on Sheffield-Egremont Road on the Appalachian Trail, battle of February 27, 1787 | Marker only |
| Kiln or charcoal pits north of Great Barrington | about 42.243 to 42.250, -73.304 to -73.311 | Thirteen unnamed OpenStreetMap "kiln or charcoal pit" points | A source, the owner, a way in |

## Tips
- In this unattended run the web-fetch agent read one mass.gov PDF, then the next mass.gov page failed with PROVENANCE_REQUIRED (approval not answered); fetch the one DCR page you need most first.
- HMdb nearby lists round six points gave most of the leads here; the Du Bois Homesite trail markers have positions that scatter onto Route 23, so do not pin from them blindly.
- Register coordinates in this county were off in five of seven tries (Glendale, Monument Mills, Tyringham Shaker, Searles Castle, Old Covered Bridge); the ArcGIS PointAddress results landed on the building except at Naumkeag (on its lot) and Chesterwood (in trees).
- theberkshireedge.com reads cleanly with page.py, but the date it prints is today's date, not the article's.
- clintonchurchrestoration.org and sandisfieldartscenter.org answer 403 to page.py.
