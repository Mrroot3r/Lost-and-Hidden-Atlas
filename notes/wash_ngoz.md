# wash_ngoz: Eastern Washington County: Black Mountain tower, the Pember, Burton Hall and village markers
state: New York
region: wash
date: 2026-11-22
places: 11
file: data_wash_ngoz.py

## What this batch is
Eleven places in the eastern towns of Washington County that the Atlas had little or nothing in (region `wash`, drawn by `choose.py --state ny`): the 1918 Black Mountain fire tower in Dresden (Lake George Wild Forest, with the Pike Brook Road parking point), the Pember Library and Museum in Granville (hours from the library's own page), Hebron District School No. 16 at East Hebron, Burton Hall (the 1901 Easton town hall, from its 2015 Register form, which read in full on NPGallery), the Adamsville Baptist Church (from the lead in `notes/wash_diyi.md`), and six marker-based entries: the Fort Ann First Baptist Church site with its bell fragment, the oldest house in Fort Ann, the Our Lady of Mount Carmel bell in Granville, the Skene's Mills site at Whitehall, Smith's Basin and the old mill sites at Hartford. Sources: Wikipedia through `wiki_raw.py`, HMdb marker pages through `page.py`, the DEC's Lake George Wild Forest page and its 2010 fire tower study. Every pin was looked at on the leaf-off aerial; the Adamsville pin was moved onto the church. Not checked: nothing was seen on the ground; the two sources disagree on when the Black Mountain tower closed (early 1989 or 1990), and both versions are given; the Rogers 1763 carving rests on Wikipedia; Burton Hall's office hours and Adamsville's service times were not found; the Hebron school's owner, and whether it is the Hebron Historical Society's schoolhouse museum, were not checked (no page of the New York society was found); the Pember museum may keep different hours from the library. Six entries rest on a single marker text.

## Leads
Places you read about and could not finish. One row each; delete the example row. Leave the table header.

| Place | Where | What is known | What is missing |
|---|---|---|---|
| Home Farm (Mirriam-Bartholomew House) | East Whitehall, NY (Register list 43.543187, -73.354027; Wikipedia article 43.53694, -73.32889) | Wikipedia: brick Greek Revival house c. 1840, 17 contributing farm buildings, Register 2008 | The list point falls on a wooded road with no farm on the aerial; an address. NPGallery has only a placeholder for 08001147 |
| Old Champlain Canal prism, Kinner's bridge to Whitehall | Town of Whitehall, NY (OpenStreetMap "Old Champlain Canal" derelict canal near 43.52219, -73.41118) | American Canal Society index: canal visible from the Wood Creek guard lock (Lock 20) to Whitehall, all on one level | A public place to see it from; on the aerial it lies between the railroad and the barge canal |
| Dresden District School No. 2 | North Road, Clemons, NY | Register form (100003631, on NPGallery as an asset PDF): one-room school c. 1880, now a sometime summer residence | A position and a public view; private house |
| First Baptist Church in the Town of Granville | County Routes 12A and 22A, North Granville, NY (HMdb 181682, 43.45039, -73.32588) | 1932 state marker: erected 1784 | Whether any building is left |

## Tips
- Washington County's Register list gives Burton Hall a Wikipedia coordinate about 10 km from the building; the Register form's address (1071 State Route 40) and the ArcGIS geocoder put it right.
- The DEC fire tower study (`extapps.dec.ny.gov/docs/lands_forests_pdf/ftowerstudy.pdf`, 406 pages) reads with `page.py -g` and has a note on every Adirondack tower.
- `hebronhistoricalsociety.org` belongs to Hebron, Connecticut; no page of Hebron, New York's society was found.
- The Pember's own site (thepember.org) gives no regular hours; the library's page `gralib.sals.edu` does, on its front page.
