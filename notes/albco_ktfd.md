# albco_ktfd: Albany County: Knox, Westerlo, New Scotland, Coeymans and Altamont
state: New York
region: albco
date: 2026-11-19
places: 14
file: data_albco_ktfd.py

## What this batch is
Fourteen standing places in Albany County outside the city, a second pass after `albco_kaom` (region `albco`, drawn by `choose.py --state ny`). Hilltowns: Knox District School No. 5 in Thompson's Lake State Park, Westerlo hamlet (old Chesterville) and its markers, the Baptist Church of Preston Hollow. New Scotland: the Presbyterian Church and cemetery, the Jerusalem Reformed Church at Feura Bush, Clarksville hamlet on the Delaware Turnpike, the Teunis Houghtaling House (a LEADS.md row, now added). Bethlehem: the 1864 Slingerlands D&H station on the Helderberg-Hudson Rail Trail. Coeymans: the Acton Civill Polytechnic Academy (red brick, now senior apartments), the 1840 brick Reformed Dutch church on Church Street (now apartments), the McCarty Stone Cottage, District School No. 7 at Coeymans Hollow (red brick) and the Israel Shear House. Altamont: the Maple Avenue business street rebuilt after the 1886 fire. Sources: Wikipedia (`wiki_raw.py`), HMdb marker pages (`page.py`), the Register forms for the Coeymans Landing Historic District (100001767, 364 pages, text layer) and the McCarty Stone Cottage (15000474), NYS Parks, Altamont Enterprise, U.W. Marx, the Ravena Coeymans Historical Society, and albanyhilltowns.com through the web fetch tool. Not checked: anything on the ground; interiors and opening times of District School No. 7, the Knox school and the churches; service times; rail trail hours; who owns the Slingerlands station building; brick on ten places (no photograph opened). Several entries (Westerlo, Clarksville, Preston Hollow, Feura Bush) rest on state blue-and-gold or local markers and one hilltowns page. Pins: Knox school, District School No. 7, the Acton Civill and the Houghtaling House were moved onto buildings on the aerial with `pix.py` (no building label confirmed them); the Israel Shear House is `area` (the Register point is in trees between houses); Westerlo, Clarksville and Altamont are area pins on the markers.

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Selkirk Yard roundhouses | Selkirk, NY (OpenStreetMap ruin lead 42.54131, -73.8194) | Bethlehem town historian's blog (2014): the yard was finished in 1924 for the Castleton Cut-Off; two roundhouses stood there, one now only a "ghost image" in aerial views | Whether anything stands; it is inside an active CSX yard, so likely view only from nowhere |
| Bennett Hill Farm | New Scotland, NY (42.570278, -73.956111) | Wikipedia: house of 1821 with an 1830s Greek Revival addition, main barn 1797, smokehouse about 1810 | Owner, whether it can be seen from a road, a second source |
| Lainhart Farm Complex and Dutch Barn | Altamont, NY (42.72389, -74.03222) | Wikipedia: farm leased from Stephen Van Rensselaer by Michael Leonhardt (died 1796); Dutch barn | Barn date, owner, visibility |
| Former Methodist Episcopal church (1836) | 36 Church Street, Coeymans (42.47454, -73.79567) | Coeymans Landing HD form: brick Greek Revival church of 1836, now not a church | Present use; worth its own entry beside the 1840 Reformed church |
| Dr. John Babcock House | Selkirk, NY (42.549444, -73.813056) | Wikipedia: 1851 two-story red brick house with summer kitchen, 1840 barn; sold 2023 | Visibility from the road; it is a private house |
| Mill ruins and flume cuts at Coeymans Creek falls | Coeymans Landing, beside the Ariaanje Coeymans House | Coeymans Landing HD form: some mill foundations survive, and cuts in the rock at the upper falls mark sluices used from about 1670 | Whether the existing `ariaanje-coeymans-house` entry should mention them, and a public view point |

## Tips
- The Coeymans Landing Historic District form (`https://npgallery.nps.gov/NRHP/GetAsset/NRHP/100001767_text`) reads with `page.py -n 200000`; strip tags from the cached file in `research/pages/` and search for a street address such as "24 Church Street" to get a building's entry.
- A web-fetch helper reading seven albanyhilltowns.com pages took about six minutes; the Wayback copy of newscotlandpc.com/history.html failed waiting for approval.
- The Altamont Enterprise's 2005 article on the fairground buildings is behind its monthly view limit.
- NPGallery forms for New Scotland Presbyterian (2010), Knox School 5 (2005), District School No. 7, Teunis Houghtaling, the Altamont fair building, Coeymans School and Bennett Hill all returned the placeholder.
- The Altamont village markers on HMdb (Maple Avenue, numbers 131427–131500 and 145181–145191) give a paragraph each on the rebuilt business street.
