# id_edum: Idaho: Wallace, the Silver Valley and the Milwaukee Road
state: Idaho
region: id
date: 2026-11-20
places: 15
file: data_id_edum.py

## What this batch is
The first batch for northern Idaho (region drawn at random by `choose.py`): 15 places in Shoshone County, plus the Cataldo Mission just over the line in Kootenai County. Wallace (the whole-town historic district, the Northern Pacific depot museum, the Carnegie library, the 1935–36 post office, the Sierra Silver Mine Tour), the 1910 fire (the Pulaski Tunnel trail and the firefighters' monuments in Nine Mile Cemetery), Mullan's schoolhouse-turned-church, Murray and its 1880s Masonic hall, the 1932 log Baptist church at Pinehurst, Burke ghost town, and the Milwaukee Road country (the Avery depot and the Route of the Hiawatha). Facts come from National Register forms read with `page.py` (NPGallery `_text`; every form tried had a text layer), Wikipedia via `wiki_raw.py`, and the managing bodies' own pages: npdepot.org, Idaho Parks and Recreation's Old Mission page, the Forest Service's Pulaski Tunnel Trail page, silverminetour.org and ridethehiawatha.com. Not checked: anything on the ground; whether the Murray Feehan log house, St. Andrew's (Mullan) and the Pine Creek church still look as their forms of 1980, 1999 and 1982 describe; library, Avery depot and Pine Creek church hours (no page of their own found); the Route of the Hiawatha's season dates (its page said "closed for the season"); Burke's current buildings and owners (view from State Highway 4 only). The Hiawatha and Pulaski pins are area pins in forest; the Sierra mine pin is the ticket office, not the mine. The depot's date disagrees (form 1901, Wikipedia list 1906) and the mine tour's two pages disagree on the season end; both are marked `conf='mixed'`. Red brick: settled only for the library (Wikipedia photograph); the depot, Wallace district, Murray, Burke, the Hiawatha, the Pulaski tunnel and the Avery depot are left '?'.

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Grand Forks (burned 1910 railway town) | Avery, ID (47.353227, -115.673701) | Register site; Wikipedia says the site is little changed since the 1910 fire burned it | The Register form text is under 700 characters; a source on what is visible and the land manager's access |
| Avery Ranger Station | Avery, ID (47.251063, -115.805636) | 1909–1930s log office, bunkhouse and dwellings (Register form, 1974); operations moved to a new station in 1967 | Which buildings still stand and whether the Forest Service lets the public see them |
| Miner's Hat (hat-shaped building) | Kellogg, ID (47.5362, -116.1134) | Register 2021 (100007007); NPGallery has no text for it | Any source on what it is and who owns it |
| Kellogg Boy Scout Cabin | Kellogg, ID (47.5369, -116.1277) | Register 2021 (100007006) | Any source |
| Magee Ranger Station | Pritchard, ID (47.844054, -116.252468) | Register 1981 (81000208) | Form not read; access |
| Oasis Bordello Museum | Wallace, ID | Search results describe a museum in an old brothel | No page of its own was found to give hours or history |
| Morning Mine compressor foundations | Mullan, ID (47.46706, -115.84395) | OpenStreetMap ruin lead | Any written source and owner |

## Tips
- Idaho Register forms for Shoshone County (1974 to 1999) all had text layers; the 2021 listings (100007006, 100007007) and Grand Forks have almost none.
- `nom.py` found nothing for the Sierra mine tour, the Pulaski trailhead or the Old Mission; `geo.py` gave a PointAddress for 509 Cedar Street, Wallace.
- Web search here returned titles and links only, no quoted text: hours had to come from `page.py` on the managing body's page.
- visitidaho.org answers 403 to `page.py`; cdapress.com 403 and inlander.com 429. spokanehistorical.org reads well (the `mail.` subdomain search results link does not).
- The only OpenStreetMap lot `parking.py` listed near the Old Mission is a riverside boat launch, not the visitor lot.
