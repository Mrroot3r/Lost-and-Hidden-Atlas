# ks_xqpd: Kansas: Leavenworth County
state: Kansas
region: ks
date: 2026-11-23
places: 15
file: data_ks_leavenworth_xqpd.py

## What this batch is
Fifteen places in and round Leavenworth, Kansas, where the Atlas had none: the Santa Fe and Union depots and the Terminal freight depot, the 1913 courthouse, the Carnegie library, the Hollywood Theater, First Presbyterian Church (Tiffany and Lamb glass), the Fred Harvey, Brewer and Carroll houses, the Western Branch soldiers' home, the Abernathy factory, Little Stranger Church, Begley Bridge and Hund School. Sources: the Leavenworth County Register list (wiki_raw.py --rows), National Register forms by NPGallery text (page.py -g, because --all stops at 12,000 characters), Wikipedia, and web search results for hours and present use. Pins were checked on the Kansas 2024 aerial; three list points (courthouse, library, Harvey house) were wrong and were replaced by OpenStreetMap or the ArcGIS address lookup. Not checked: the interiors, who owns Fred Harvey House, the Terminal depot, the library and the factory now; the hours of The Depot restaurant, the Old Union Depot and the Performing Arts Center (set to "?"); service times at the church; whether the public may enter the Soldiers' Home grounds; Begley Bridge's exact spot (pin is the area); the Carroll Mansion hours come from a search result quoting the society's contact page, which would not open. The Chapel of the Veterans was not pinned: the Western Branch pin is the campus. Fort Leavenworth was left out because it is an active base with photo ID and vehicle checks.

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| The Rookery, Fort Leavenworth | Fort Leavenworth, KS | Army wayside tour calls it the oldest surviving building on the fort and the oldest continuously occupied residence in Kansas; Wikipedia says built 1832 to 1834 | Exact coordinate; it is a residence on an active base, so access needs a source |
| Frontier Army Museum | 100 Reynolds Ave, Fort Leavenworth, KS (39.34969, -94.91488, OpenStreetMap) | Museum on an active base; photo ID and vehicle inspection needed; sources disagree on hours | Hours from the Army page, and the building's history |
| Helmers Manufacturing Company Building | Leavenworth, KS (39.292356, -94.906858) | National Register 09000809 | The form is a scan with no text layer |
| Chapel of the Veterans, Western Branch | Leavenworth VA campus | Late Gothic Revival by Louis Curtiss (Wikipedia) | Coordinate and whether the public may see it |

## Tips
- NPGallery text forms run to 40,000 or more characters; page.py --all shows only 12,000, mostly the cover sheets. Use page.py -g with words like built|brick|stone to reach the description.
- The Register list coordinate for the Leavenworth County Courthouse is far from the building; check each Leavenworth list point on the aerial.
- The ArcGIS findAddressCandidates PointAddress result put the library and the Harvey house on the building where the list points did not.
