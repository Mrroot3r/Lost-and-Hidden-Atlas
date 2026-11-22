# de_vfba: Delaware: Kent, Sussex and southern New Castle
state: Delaware
region: de
date: 2026-11-22
places: 16
file: data_de_vfba.py

## What this batch is
Third pass over Delaware, taken with `choose.py --thinnest` (35 places before, 51 after). 16 places spread over all three counties. Kent: Belmont Hall (Smyrna), Christ Church and Woodburn (Dover), the Camden Friends Meetinghouse, the Old Stone Tavern at Little Creek and the Parson Thorne Mansion in Milford. Sussex: the Highball Signal in Delmar, St. George's Chapel near Harbeson, Cool Spring Presbyterian Church, the Redden Forest lodge, the De Vries monument in Lewes and the Governor Ross Mansion in Seaford. New Castle: the Corbit–Sharp House in Odessa, the New Castle ice piers, Cooch's Bridge and the Liston Range Rear Light. Sources: Wikipedia read as raw text (`wiki_raw.py`, with `--rows` for the Kent and Sussex Register lists), and the pages of whoever runs each place read with `page.py`: history.delaware.gov (state sites list, Cooch's Bridge, Belmont Hall), woodburn.delaware.gov, archives.delaware.gov marker pages (Cool Spring, St. George's, Carey's Camp), the Delaware Forest Service, historicodessa.org, seafordhistoricalsociety.com, allsaintsandstgeorges.org, pym.org, an NPS article on the ice piers, HMdb and Lighthousefriends.com. Every pin was looked at on the aerial and the LiDAR; five were moved onto the building. Not checked: anything on the ground; the Parson Thorne Mansion's hours (only the county visitor bureau's listing was read, so `hours='?'`); Christ Church Dover's and Cool Spring's service times (no page of their own was read); who owns the Old Stone Tavern (the federal land map marks it as state land) and the ground of the De Vries monument; parking at most places. The ice piers pin stands for the group in the river; the Highball Signal, Liston light and De Vries monument pins are on the right spot by the sources but the object itself was not made out on the aerial. `check.py` warns that the Highball Signal pin is just outside Delaware's outline; on the aerial it is north of the State Street line, in Railroad Park.

## Leads
Places you read about and could not finish. One row each.

| Place | Where | What is known | What is missing |
|---|---|---|---|
| Carey's Camp Meeting Ground | Near Millsboro, DE (Wikipedia 38.52333, -75.40611; the archives' address, 22053 Careys Camp Road, geocodes to 38.55842, -75.36759, about 5 km away) | Wikipedia and the Delaware Public Archives: Methodist camp meeting since 1888, 47 wooden "tents" in an oval round a cruciform tabernacle | Neither point shows the oval on the aerial (the address point is a mobile-home park beside a church); a firm location |
| Hearn and Rawlins Mill | Near Seaford, DE (38.67889, -75.59417) | Wikipedia: water-powered grist mill of about 1880 on an earthen dam, two overshot wheels of 1912 | Whether it still stands, owner, and whether it can be seen from the road |
| Bethel Historic District | Bethel, DE (38.57722, -75.63194) | Wikipedia: ship carpenters' houses of a 19th-century shipbuilding village | A source on what to see now; houses are private |
| Spring Garden | Near Laurel, DE (38.56444, -75.56722) | Wikipedia: brick house of about 1782 with an 1860 kitchen and an 1880 frame wing | Owner and whether it can be seen or visited |
| Camden Historic District and Wyoming railroad station | Camden and Wyoming, DE | Register list rows | Sources on what stands |

## Tips
- `milfordhistoricalsociety.org` is Milford, Connecticut, though web search offers it first for the Parson Thorne Mansion in Milford, Delaware. The Delaware society's own page was not found.
- episcopalassetmap.org node 2664, offered for Christ Church Dover, is another church (a Methodist page). The Diocese of Delaware's church list (`delaware.church/episcopal-churches-in-delaware/`) gives each parish's address; christchurchdover.org reset the connection.
- Kent and Sussex Register coordinates were off the building for Christ Church Dover, Parson Thorne and St. George's Chapel (the last in a pond); the ArcGIS PointAddress result and `nom.py` landed on the building.
- `history.delaware.gov/coochs-bridge-historic-site` reads cleanly and gives the site's tour rules.
