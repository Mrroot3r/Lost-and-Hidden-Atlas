# pae_kqwd: Delaware County and the Brandywine, Pennsylvania
state: Pennsylvania
region: pae
date: 2026-11-19
places: 17
file: data_pae_kqwd.py

## What this batch is
The first places in Delaware County, Pennsylvania (region `pae`, drawn at random with `choose.py`), with the Brandywine side of southern Chester County. 17 places, nearly all standing: New Sweden (the Printzhof foundations in Governor Printz Park, the Morton Homestead, the Lower Swedish Cabin), the 1799 Lazaretto quarantine hospital, Penn-era buildings (Caleb Pusey House 1683, the 1724 Chester Courthouse, the Thomas Massey House, Chichester Friends Meetinghouse), Newlin Grist Mill (1704, still grinding), the Sycamore Mills village and dam in Ridley Creek State Park, and the Brandywine battle ground (Brandywine Battlefield Park, John Chads House, Barns-Brinton tavern, Birmingham and Old Kennett meetinghouses), Primitive Hall and Mason and Dixon's Star Gazers' Stone. Wikipedia was read with `wiki_raw.py`; HMdb, the PHMC Brandywine page, DCNR's Ridley Creek pages, Natural Lands' ChesLen page, Visit Delco, Birmingham Friends, Kennett Friends and Primitive Hall's own site with `page.py`. No Register form was read. Not checked: hours for the Chadds Ford Historical Society houses, Newlin Grist Mill, the Thomas Massey House, the Caleb Pusey House, the Morton Homestead, Governor Printz Park, the Lazaretto offices and the Chester Courthouse (their sites refused the tool or were not found, and the archived copies could not be opened unattended); whether the Benjamin Ring house at the battlefield is a rebuilding (Wikipedia says both restored and destroyed by fire in the 1930s); the date of the Lower Swedish Cabin (1640s or about 1700). Red brick was settled from Wikipedia text or a Commons photograph opened in the session for 14 places; Sycamore Mills, Brandywine Battlefield Park and the John Chads House springhouse are not settled (the Chads house is `some`, for its brick chimney). The Brandywine pin is the park (area) and its trailhead the visitor-center lot; the Sycamore Mills pin is the dam (area). No pin marks only a trailhead.

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Chester Waterside Station (PECO) | Chester, PA (39.82917, -75.38389) | Wikipedia: 1916 Beaux-Arts coal power station by John T. Windrim, now offices; a red brick 1925 machine shop on the site became an indoor training space in 2016 | Whether it can be seen from a public street or the riverfront, and the pin |
| Taylor/Frazer House ruins | Thornbury Township, PA (OSM ruin 39.92553, -75.50143) | An OpenStreetMap-mapped ruin | Any source on what it was, and the owner |
| Twaddell's Mill and House; Brinton's Mill; Strode's Mill | Chadds Ford Twp (39.8442, -75.5786), Birmingham Twp (39.8853, -75.6036), East Bradford Twp (39.9286, -75.6178), PA | On the Register lists for Delaware and southern Chester counties | What stands, the owner, and whether any can be seen from a road |
| William Brinton 1704 House | Chadds Ford Township, PA (39.8964, -75.5611) | On the Delaware County Register list with an article | Not read; access and tours |
| Printz Park New Sweden farmstead | Governor Printz Park, Essington, PA | Wikipedia: the Bridgeton, NJ farmstead buildings were rebuilt in the park 2019–2020, dedicated 2022 | Who runs the park and opens the buildings, and when |

## Tips
- The Pennsylvania leaf-off server took about a minute a tile. Six copies of `pincheck.py` on named ids, each in its own folder of symlinks to the workspace (build, cache, dist, lidar, src, test, tools) with its own `research/`, ran side by side without clobbering each other's sheets (they are all named `pincheck_picked_*`).
- The ArcGIS PointAddress for a street address put the Caleb Pusey House and Birmingham Friends Meetinghouse on the building where the Wikipedia coordinates were 70 to 90 m off in trees.
- chaddsfordhistory.org and newlingristmill.org answer 403 to `page.py`; thomasmasseyhouse.org resets the connection; uplandboro.org 403 with no archived copy. Web searches here returned titles and links only, no quoted text.
- The Old Kennett Meetinghouse article gives two different hours for its summer meetings (11 a.m. and 9 a.m.).
