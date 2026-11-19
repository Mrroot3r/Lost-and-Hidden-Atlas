# nny_rkwt: Gouverneur, Rossie, Antwerp and Carthage country
state: New York
region: nny
date: 2026-11-19
places: 13
file: data_nny_rkwt.py

## What this batch is
Thirteen places between the Thousand Islands and the Adirondack edge, drawn at random by `choose.py --state ny` (region `nny`, which offered Antwerp); the Atlas had nothing within 20 km of Antwerp or Gouverneur. Southwestern St. Lawrence County: the Rossie Iron Works (1813 furnace site, foundry ruins), Gouverneur's marble First Presbyterian Church with the Gouverneur Museum in its old manse, the Gouverneur post office, the Richville Welsh church, Edwards Town Hall and the old Fine Town Hall. Jefferson County: the Village of Antwerp Historic District, Carthage's State Street district and First Baptist Church, the 1820 Hubbard stone house at Champion, the St. Regis Paper Mill Canal at Deferiet, the LeRay Mansion on Fort Drum (permit: a post visitor pass) and Densmore Church on Wellesley Island. Mostly standing buildings. Sources: Wikipedia through `wiki_raw.py`, HMdb marker pages, the First Presbyterian Register form (15000607, the only form here NPGallery holds as text), the SLCHA Quarterly of April 1956 for Rossie, and the managing bodies' own pages through `page.py`. Not checked: anything on the ground. What stands at Rossie rests on the 1956 account plus a roofless walled building seen on the aerial (pin moved onto it; conf mixed). Service times for every church except Densmore's summer concerts; the Fine Town Hall's present use; whether the Hubbard House opens; LeRay Mansion tour times (Wikipedia says daily tours; no Army page read gave them). Brick for four places came from Wikipedia photographs (two red, the post office buff, LeRay white); Edwards Town Hall, Antwerp and the canal are left '?'.

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Victoria lead mine chimney | Rossie, NY (USGS Victoria Mine 44.35558, -75.6515) | blacklakeny.com: a chimney of the Victoria lead mine stands about a mile from Rossie toward Oxbow; NYSGA 1983 field guide says the Rossie lead veins are on private land | A current source or picture of the chimney, its exact spot, and an owner who lets people look |
| Hammond red sandstone quarry | Hammond, NY (HMdb 82404 marker, 44.39008, -75.74207) | Marker (R. T. Elethorpe Hist. Society): late-1800s quarry, 600 men cut pink, red and yellow sandstone paving blocks | The quarry itself: nothing was seen on the aerial round the marker; needs its location and owner |
| Harrisville grist mill and chair factory | Harrisville, NY (HMdb 152688, 152686) | Pomeroy markers: Joseph Pahud's grist mill of 1857 (closed 1938) and chair factory of 1859 (closed 1950s); a depot of 1887 (HMdb 133162) | Whether any of the buildings stand: nothing clearly a mill on the aerial at the markers |
| Caledonia iron mine and the "Old Iron Works" | Rossie/Spragueville, NY (OpenStreetMap ruin 44.27608, -75.53604) | SLCHA 1956: the Caledonia mine near Spragueville, found 1812, fed the Rossie furnace | A source tying the OpenStreetMap point to a ruin, and the owner |
| Wood's Grist Mill, Sterlingville and LeRaysville archaeological districts | Fort Drum, NY | Register listings 95000072, 95000070, 95000069 | Inside the post; no source read on what is left or whether visitors are taken there |
| Rossie Hotel (1811) and Laidlaw House | Rossie, NY | blacklakeny.com names both | Whether they stand, and where |

## Tips
- Nearly every older Register form for Jefferson and St. Lawrence counties is an NPGallery placeholder; the NARA copies (`s3.amazonaws.com/NARAprodstorage/.../NPS_NY/<ref>.pdf`) that web search lists answer 403 to `page.py`.
- The SLCHA Quarterly back issues (`slcha.org/wp-content/uploads/quarterly/...pdf`) read in full with `page.py` and are good on St. Lawrence County industry.
- HMdb puts the Paper Mill Canal marker "in Carthage", but it is at Deferiet; the canal is plain on the leaf-off aerial just north of the NY 3 bridge.
- The Fort Drum history-tours page is 404 and army.mil articles answer 403 to `page.py`; the gate page (`home.army.mil/drum/index.php/my-fort/all-services/gate-information`) reads.
- The Gouverneur Museum's own page and the Town of Gouverneur's page give different Wednesday hours (1–2 p.m. and 1–3 p.m.).
