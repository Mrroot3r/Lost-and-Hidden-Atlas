# mohw_iugo: Southern Lewis County: Constableville, Lyons Falls, Port Leyden, Martinsburg
state: New York
region: mohw
date: 2026-11-20
places: 18
file: data_mohw_iugo.py

## What this batch is
Eighteen places in southern Lewis County, New York, the first pass in that county (region `mohw` drawn at random by `choose.py --state ny`, which offered Constableville; the Atlas had nothing in Lewis County, the nearest places being three in Boonville). Constableville: Constable Hall (1810–1819 limestone house museum, hours from its own page), the 1797–1802 Collins house and family cemetery, the village historic district. West Turin: Collinsville Cemetery (1810). Lyons Falls: the Gould Mansion (1902, Gouverneur marble; the library is in its carriage house), Forest Presbyterian Church (1894), Wildwood Cemetery with the 1921 Fisher chapel, and the Black River Canal's last flight of locks (103–109) north of the turning basin. Port Leyden: the canal lock by the community park (HMdb calls it Lock 96; the American Canal Society index puts Lock 95 on that spot: both given), St. Mark's (1865 board-and-batten). Lyonsdale: the flight of four, Locks 87–90, plain on the LiDAR in the median of divided NY 12. Talcottville: the 1789 Talcott Stone House (Edmund Wilson's) and the 1870 Leyden schoolhouse, now the town hall. Martinsburg: the 1812 first county courthouse (town hall), the 1847 red-brick county clerk's office (Martinsburg Historical Society museum), the General Walter Martin house (1803–1805); West Martinsburg's 1840 Methodist church; Pine Grove's 1895 union church with a theatre's sloping floor. Sources: Wikipedia through `wiki_raw.py`; HMdb nearby list and marker pages; the ACS Black River Canal index with GPS (lock by lock); constablehall.org; lyonsfallshistory.org; the 2019 Lyons Falls Brownfield Opportunity Area report on lewiscountyny.gov (mill site and canal locks); lyonsfallsny.gov; martinsburgny.gov; townofleydenny.gov's history PDF; historicallylewis.org; Pomeroy Foundation marker pages; NYGenWeb; historypointer.com for Register addresses; two Register forms that had text (Leyden Common School No. 2, 16000392; First Lewis County Clerk's Office, 100001769). Every other Lewis County form tried is an NPGallery placeholder. NOT checked: nothing on the ground; service times for any church (none found); hours of the Leyden and Martinsburg town halls; who owns the Gould house, the canal bed at Lyons Falls, the Port Leyden park and Wildwood Cemetery; the condition of any lock wall (only the LiDAR and the 2019 report's "four locks... walls repaired" say anything). Pins on the Register point not checked against an address: Collins house, West Martinsburg church, the Stone House (moved off a yard onto NY 12D; which house it is was not settled). Red brick: one yes (the clerk's office, from the HMdb photograph), most others no from the sources' "limestone", "marble" or "frame"; three left `?`.

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Hough's Cave | Martinsburg, Lewis County, NY (HMdb 152850: 43.72013, -75.46639) | 1931 state marker: hiding place on the Underground Railroad; cavers searched for it in 2014 (historicallylewis.org, "The Trial of Horatio Hough") | Whether anything can be found, and the landowner |
| Lyman R. Lyon's Big Barn foundation | Outside Lyons Falls, Lewis County, NY | Built from 1859, 221 by 48 feet, once called the largest barn in the state; "parts of the foundation still exist" (lyonsfallshistory.org) | Location and owner |
| Black River Canal Lock 94 and Locks 99–102 | Port Leyden, NY (ACS: Lock 94 43.57194, -75.33755 along Canal Street; 99–101 about 43.6035, -75.3560; guard lock 102 43.60547, -75.35627) | Coordinates and "seen 2011" in the ACS index | What shows, and the owner |
| Lyons Falls depot | 6819 McAlpine Street, Lyons Falls, NY | Former station, now a private feed-store building (2019 BOA report) | Date, what survives of the station |
| St. John's Church, Lyons Falls | 5838 McAlpine Street, Lyons Falls, NY | Gothic church of brick with limestone trim, after 1909 (lyonsfallshistory.org) | Building date, service times from the parish's own page |
| Osceola Town Hall | Osceola, Lewis County, NY (43.50306, -75.7225) | 1882 Methodist church, town hall since the 1920s (Wikipedia) | Use today, hours |
| Alpina and Lewisburg iron-furnace districts | Town of Diana, Lewis County, NY | Register archaeological districts (95000068, 95000071), "rural iron furnace and village site" | Address restricted; a public way in |

## Tips
- Lewis County's Register forms are mostly NPGallery placeholders; the newer ones (2016 on) have text. historypointer.com/nris/resource/<ref> gives each listing's street or road.
- The American Canal Society's "BRC index with GPS" PDF gives a coordinate for every Black River Canal lock from Rome to Lyons Falls; the Lyonsdale and Port Leyden locks matched the LiDAR exactly.
- A search for Forest Presbyterian Church's services leads to a church of that name in Forest, Virginia (forestchurchpresbyterian.internetoutreachexperts.com): not the Lyons Falls church.
- constablehall.org's /discover/ pages are 404; /about/hall/ and /visit read with page.py.
- lyonsfallslibrary.org answers 403 to page.py and hours.py.
- choose.py offered Constableville under `mohw` though Lewis County reads as North Country; Lowville was left alone for that reason.
