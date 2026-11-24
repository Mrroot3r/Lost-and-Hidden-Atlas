# kalamazoo_bnds: Michigan: old Kalamazoo
state: Michigan
region: mi
date: 2026-11-24
places: 12
file: data_kalamazoo_bnds.py

## What this batch is
Twelve standing buildings in Kalamazoo from one walk-through video of old Kalamazoo buildings (Old World Exploration, "Old World Kalamazoo, Michigan"; the record is source/videos/20240830_CSmQNVkUKRA.md). Added: the Ladies Library Association Building (1878-79), the Lawrence and Chapin iron works building (1870-72), the Masonic Temple (1913-15, now a Hilton Garden Inn), the Michigan Central Depot (1887, now the Kalamazoo Transportation Center), Old Central High School (1912-23), the State Theatre (1927), the Kalamazoo State Hospital water tower (1895) and gatehouse (about 1879), City Hall (1931, Art Deco), First Baptist Church (1853), First Presbyterian Church (1928-30) and East Hall, now Heritage Hall, of Western Michigan University (1905). Facts come from Wikipedia read with wiki_raw.py and from SAH Archipedia (Buildings of Michigan) pages MI-01-KZ1 to KZ26 read with page.py; the Masonic Temple's hotel use from news results; hours from the City of Kalamazoo's City Hall page (read with the web fetch tool) and the two churches' own sites. Not checked: the State Theatre's and the depot's hours (their pages gave none or would not open), the Ladies Library's open days (events only, none listed), whether the gatehouse museum still opens, parking, and every interior. The water tower and gatehouse pins are area pins: neither could be picked out on the aerial, and both stand on the grounds of a working state hospital, so they are marked view from the street. Lawrence and Chapin's brick colour is not settled (brick='?').

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Kalamazoo County Building (Michigan Avenue Courthouse) | Kalamazoo, MI, 227 W. Michigan Avenue | PWA Moderne, 1936-37, by M. J. C. Billingham with Smith, Hinchman and Grylls; reliefs by Corrado Parducci (SAH Archipedia, in the City Hall entry) | A decision whether its style counts as modernist under rule 8; a pin |
| Desenberg Block | Kalamazoo, MI (42.2925, -85.580833, Register list) | 1885-87 by Adler and Sullivan (SAH Archipedia MI-01-KZ11 title page) | The page's text read in full, a pin on the aerial |
| Old Fire House No. 4 and Engine House No. 3 | Kalamazoo, MI, 526 N. Burdick St. and 607 Charlotte Ave. | 1887 and 1907-08 fire stations, both on the Register (Wikipedia) | Present use and a pin |
| Henderson Castle | Kalamazoo, MI | Queen Anne house by Charles A. Gombert, now an inn (SAH Archipedia MI-01-KZ20 title page) | Hours from its own page, a pin |
| Rickman House (Rickman Hotel) | Kalamazoo, MI, 345 N. Burdick St. | 1907-08 hotel across from the depot, now apartments (Wikipedia) | A pin |

## Tips
- SAH Archipedia's Kalamazoo pages are MI-01-KZ1 to KZ26 (KZ27 on answers 404); each reads in full with page.py --all.
- kpl.gov (Kalamazoo Public Library local history) and hmdb.org answered HTTP 403 to page.py; search results quoting kpl.gov were the only way in.
- kalamazoocity.org answers 403 to page.py, but the web fetch tool read the City Hall hours page.
- Amtrak's station page gave no station hours through the web fetch tool.
