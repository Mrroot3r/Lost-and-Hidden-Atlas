# ms_ihap: Mississippi: Natchez, the northeast hills, the Delta and the Trace
state: Mississippi
region: ms
date: 2026-11-23
places: 16
file: data_ms_ihap.py

## What this batch is
Sixteen places spread over ground the first two Mississippi batches left empty, claimed with `choose.py --thinnest` (Mississippi had 36 places, 52 after). Northeast: the Verandah-Curlee House (Corinth), the 1854 Jacinto Courthouse, the Elvis Presley Birthplace (Tupelo). Natchez Trace: French Camp Historic Village. Natchez: Melrose, the William Johnson House, King's Tavern. Delta: Fort Pemberton (Greenwood), the Clarksdale depot that holds the Delta Blues Museum, Grace Episcopal (Rosedale). Central and east: the 1857 Hinds County courthouse at Raymond, the Hazlehurst depot, Stuckey's Bridge near Meridian, Zion Baptist (Collinsville), the Baptist Church of Christ at Sardis (Winston County), Hopewell Presbyterian near Oxford. Sources were read with `wiki_raw.py` (Register lists by county with `--rows`, articles) and `page.py`: SAH Archipedia (Buildings of Mississippi), NPS pages (Natchez NHP hours and fees, Corinth unit, French Camp), the American Battlefield Trust, HMdb, elvispresleybirthplace.com, deltabluesmuseum.org, the Stuckey's Bridge Register form, Hill Country History. Pins were checked on the aerial; five Wikipedia or Register coordinates were off the building and were replaced by ArcGIS geocoder points (William Johnson House was 1.3 km off). Not checked: nothing on the ground. Hours not found on a managing body's page for the Verandah-Curlee House (its old web address now carries unrelated pages), Jacinto, French Camp village, the Hazlehurst depot museum, Fort Pemberton park, and the churches. King's Tavern: Wikipedia (2022) says closed and for sale; current use not checked; its date is 1769 (Wikipedia) or about 1798 (SAH), both given. Melrose tour fee: $11 on the NPS hours page, $10 on the fees page, both given. Whether Fort Pemberton's breastworks still show (a 1958 marker said so) and whether Stuckey's Bridge is open to cars: not checked. Pins not on the thing: Fort Pemberton (missing-marker position, on the highway by the woods), Stuckey's Bridge (on the river, bridge hidden by trees), Elvis Birthplace (in trees in the park). Brick from photographs chosen with `photo_find.py` (Johnson House and Hazlehurst depot yes; Verandah garden wall and French Camp chimney some) and from SAH text (Jacinto yes); frame churches and the iron bridge no.

## Leads
Places you read about and could not finish. One row each; delete the example row. Leave the table header.

| Place | Where | What is known | What is missing |
|---|---|---|---|
| Confederate siege line (Beauregard Line), Shiloh NMP Corinth unit | Corinth, MS; NPS sign on Polk Street, then just under a mile down a dirt road | 1862 earthworks with a trail, platforms and panels (NPS site bulletin "Confederate Siege Line") | A coordinate for the trailhead or the works; OSM and the NPS places page gave none |
| Old First Presbyterian Church | Kosciusko, MS | 1899 Romanesque Revival church, Register 1992 (Wikipedia) | Wikipedia's coordinate (33.0586, -89.5875) and its address, 603 Smythe Street (geocoder 33.05067, -89.57785), are 1.2 km apart; which is the church |
| Old Augusta Historic Site | 2 miles north of New Augusta, Perry County, MS (31.2244, -89.0497) | County seat 1818–1906, abandoned; brick and concrete rubble in woods (Wikipedia, HMdb 1949 marker) | Owner and a legal way in; it adjoins the Leaf River Cellulose mill |
| College Hill Presbyterian Church | College Hill, near Oxford, MS | 1844 brick church burned August 13, 2022; congregation plans a new sanctuary and a project on the old site (chpcoxford.org) | What, if anything, stands on the old site |
| Magnolia Hotel | Biloxi, MS (30.39472, -88.88944) | 1847 hotel moved 1972 by the city (Wikipedia) | Its use now: the Mardi Gras museum it held is listed at another address |
| Ocean Springs L&N depot | Ocean Springs, MS (30.415278, -88.826944) | 1907 depot, Register list says used as a visitor centre | A source on its use and hours |

## Tips
- For a Mississippi first pass, `wiki_raw.py --rows -g` across all 82 county Register lists in one loop finds the sites with an article in a few minutes; SAH Archipedia (`sah-archipedia.org/node/<n>`) then gives the best "what survives" text and reads well with `page.py --all`.
- Wikipedia and Register coordinates for small-town Mississippi buildings were off in 5 of 17 pins; the ArcGIS geocoder's POI hits were right each time.
- NPS hours pages for Natchez (`nps.gov/natc/planyourvisit/hours.htm`) read in full with `page.py --all` when the text after "Contact Us" is printed; the default view showed only the header.
