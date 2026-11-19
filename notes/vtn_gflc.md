# vtn_gflc: Orleans County, Vermont
state: Vermont
region: vtn
date: 2026-11-19
places: 17
file: data_vtn_gflc.py

## What this batch is
Seventeen places in Orleans County, Vermont, plus Island Pond station just over the line in Essex County (region vtn drawn at random by `choose.py`, which named Brownington Village; the Atlas had nothing within 30 km). Brownington: the Old Stone House (Alexander Twilight's 1836 granite dormitory, now the county museum), the 1841 Congregational church where Twilight is buried, and the 1823 grammar school with the Prospect Hill observatory. Barton: the Brick Kingdom factory ruins on the Brick Kingdom Trail along the falls, and the CCC granite bathhouse at Crystal Lake State Park. Newport: the 1886 county courthouse, the 1904 federal building and the 1899 Goodrich library, and the 1918 Clyde Pond dam at Arnolds Falls. Also the Haskell Free Library and Opera House on the border at Derby Line, Greensboro Depot (1872), the Orne covered bridge (a 2000 replica of the 1879/1881 bridge that was burned), Irasburg town hall, the Holland church museum, the Sweeney store at East Charleston, the Runaway Pond marker at Glover (1810) and the Grand Trunk station at Island Pond. Sources were Wikipedia through `wiki_raw.py`, HMdb marker texts through `page.py`, the Vermont Historical Society's Essex and Orleans museum directory, and the managers' own pages (haskelloperahouse.org, vtstateparks.com, goodrichlibrary.org, the Crystal Lake Falls Historical Association's Google site). Not checked: anything on the ground; the Old Stone House Museum's own visit page (HTTP 403), so its hours come from the VHS directory; which ruin on the Brick Kingdom Trail was which mill (the pin is the Pierce House Museum); whether the Brownington church or the Irasburg hall open outside events; the owners of the Greensboro depot, the Sweeney store and the Clyde Pond dam; where the Prospect Hill observatory stands (not pinned); and the build date of the Island Pond station building. Two pins were moved on the aerial: the Crystal Lake bathhouse (the park point was in woods; it is now on the long building above the beach, read from the aerial) and the Clyde Pond dam (the marker's address point was a house). Red brick was set from Wikimedia pictures for the Haskell (buff-orange brick walls, red chimneys: some), the county courthouse and the Goodrich library (yes); the federal building from its Wikipedia text; Island Pond's only picture is a 1907 postcard, so left '?'.

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Lane Opera House site | Newport, VT (44.93642, -72.20782, HMdb 122633) | 1892 three-storey brick opera house seating 800; first Newport city meeting 1918; burned 1923 (HMdb marker) | Nothing to see but the marker; add only for a series on lost opera houses |
| Fox Hall | Westmore, VT (44.77333, -72.07333) | c. 1900 Shingle-style summer house of the mayor of Yonkers on Lake Willoughby, with icehouse (Wikipedia) | On a private road; whether it can be seen from VT 5A or the lake |
| River Road Covered Bridge site | Troy, VT (44.95583, -72.39417) | 1910 Town lattice, the only covered bridge in Troy, burned February 6, 2021 (Wikipedia) | Whether the abutments are left, and a reason to visit |
| William Hayden House | Albany, VT (44.71, -72.39056) | 1854 brick Greek Revival house on VT 14, granite-trimmed, carved stone gateposts (Wikipedia) | Private house; whether it is worth a view-only entry; picture for brick |
| Derby Academy Old North Hall | Derby, VT (44.94985, -72.13248, HMdb 75586) | Academy founded 1840; Derby Historical Society museum in the "Old North Hall", summer Sunday afternoons (VHS directory) | The hall's date and pin; the marker says the early building was replaced in 1957 |
| Barton Mountain quarries | Barton, VT (44.76999, -72.13259, USGS) | Granite quarry on the east side of Crystal Lake, stone carried by steamboat, used for the CCC bathhouse (Vermont State Parks) | Whether anything is left and whether there is public access |
| Belvidere Mountain asbestos mine | Lowell, VT | Last asbestos mine in the eastern US; tailings and cleanup (Wikipedia, Lowell article) | Hazard; a viewpoint from a public road and an owner |

## Tips
- `oldstonehousemuseum.org` answers HTTP 403 to `page.py` with no archived copy; the Vermont Historical Society's Essex and Orleans museum directory (`vermonthistory.org/essex-and-orleans-county-museum-directory`) gave hours and fees for the Old Stone House, Holland, Island Pond, Barton, Derby and Craftsbury societies in one page.
- `wiki_raw.py` died with a raw traceback (connection reset by the proxy) on one batch of titles; rerunning the titles one call later worked.
- `brick.py look` hit Wikimedia's 429 on the second picture in a row; a `sleep 60` inside the same call ran past the shell's two-minute limit, so wait in a separate call.
- The `pincheck.py --lidar` run on 17 town pins took under two minutes here.
- The Crystal Lake State Park point in OpenStreetMap is in woods on the shore, not at the beach or bathhouse.
