# ar_mkzr: Arkansas: a second scatter across the state
state: Arkansas
region: ar
date: 2026-11-28
places: 12
file: data_ar_mkzr.py

## What this batch is
Twelve National Register listings spread over Arkansas: Spring Mill (Batesville), Quigley's Castle (Eureka Springs), the Three States Lumber powerhouse (Burdette), the Old Randolph County Courthouse (Pocahontas), the McKennon House (Clarksville), the Oark School–Methodist Church, Cotter Bridge, the Taylor Hill Hotel (Coal Hill), the Mo-Ark Baptist Academy (Blue Eye), Winona Church and School, Harmony Presbyterian Church and the Gurdon Jail. Region drawn with `choose.py --thinnest` (Arkansas, 69 places before). Every fact is from the Park Service record and nomination form (`tools/form.py`), plus the Wikipedia article for Spring Mill. Nothing was seen on the ground. Not checked: whether each place still stands as described (the forms date from 1972 to 2008), who owns it now, parking, and opening hours. Web searches for hours returned only directories, so every place says hours not checked. Pins are the Register's list points, looked at on the Esri aerial; five fall on trees or a street and are marked as area pins (Burdette, Pocahontas, Oark, Winona, Harmony), though a Commons photo of the church sits within 30 m of the Winona and Harmony pins. Brick is `?` where a form names brick without a colour. Pictures: eleven from Commons; none fitted Oark (only a store came up).

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Johnson House and Mill | Johnson, Washington County (36.13721, -94.17830) | NR 76000473: 1880–82 brick house with a stencilled parlour ceiling, and a mill site worked since the 1830s; private in 1976 | whether the mill and house still stand and any public access |
| Mount Holly Cemetery | Little Rock (34.7376, -92.2785) | already a row in LEADS.md | its keeper's page for access and hours |
| Stone County barns and farmsteads | Marcella, Pleasant Grove, Big Springs (about 25 listings) | NR 1985 survey of Ozark farm buildings | which survive and are seen from a public road |
| Old Davidsonville and Cadron Settlement | Randolph and Faulkner counties | town sites named in Arkansas state parks material | not researched this session |

## Tips
- `publish.sh` stopped because main moved; `resync.sh` copied the workspace's older `data_b.py` over the clone's, which broke the build (`bcol` unknown). I reset the clone to origin/main, copied back only my two new files, and set the workspace up again with `setup.sh`. Run `setup.sh` fresh before building if a resync is needed.
- `tags=` accepts only the series tags listed by `check.py`; 'mills', 'bridges' and 'schools' are errors.
- Web search gives no hours for small Ozark places; the owners' own pages (QuigleysCastle.com) were not reachable here.
