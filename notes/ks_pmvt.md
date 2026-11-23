# ks_pmvt: Lawrence, Eudora and Vinland, Kansas
state: Kansas
region: ks
date: 2026-11-23
places: 16
file: data_ks_pmvt.py

## What this batch is
Sixteen places in Douglas County, Kansas, in the Kansas City area: in Lawrence the Eldridge House Hotel, the 1903 courthouse, the old Watkins bank and city hall (now a museum), the 1904 Carnegie library, Plymouth Congregational Church, Spooner Hall and Dyche Hall at the University of Kansas, the Haskell Institute campus, Oak Hill Cemetery, the Reuter organ works, the 1956 Santa Fe depot and the saddle-roofed 1956 house; in Eudora the old stone Holy Family church, the Cohn store and Beni Israel Cemetery; and the Barnes Apple Barn at Vinland. The Atlas had 3 places in Lawrence before (14 in the county from the earlier trail and territorial batch). Sources: the Kansas Historical Society's Douglas County register summaries (page.py, all 13 pages), Wikipedia (wiki_raw.py), and two museums' own visit pages for hours (Watkins, KU Natural History Museum). Addresses were geocoded with ArcGIS directly (countryCode USA, region Kansas) and every pin looked at on the Kansas 2024 aerial; Spooner Hall, Oak Hill and Holy Family were moved onto what the aerial or OpenStreetMap showed. Not checked: anything on the ground; hours of the Eldridge, churches, cemeteries, the depot and campus buildings; who owns the Carnegie building and what it is used for now; Haskell's visitor rules (the pin is the campus, not a building); National Register nomination forms (summaries only); the Holy Family "oldest Catholic church in use in Kansas" claim rests on the register summary quoting parish records. The Barnes Apple Barn date is disputed (c. 1857 in the register summary, 1891 in a Commons photo caption). Brick was settled from a source or picture for the depot, stone buildings and the Cohn store only.

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Parmenter Hall, Baker University | Baldwin City, KS (38.7783, -95.1875) | Register 1977, Second Empire (Kansas Historical Society summary) | A source for its date and use |
| Lucy Hobbs Taylor Building | 809 Vermont St, Lawrence, KS (38.9681, -95.2381) | Register 1982, Italianate; she was the first woman to graduate from dental school (Wikipedia) | A source that dates the building and says what it is now |
| Old Lawrence districts (Old West Lawrence, Oread, Downtown) | Lawrence, KS | Register districts of 1972, 2007 and 2004 | Which individual buildings are worth a pin |
| Eudora Main Street and First Methodist Church of Eudora | Eudora, KS (38.9464, -95.0961) | Register 2021 listings | Not read |

## Tips
- ArcGIS findAddressCandidates through tools/geo.py is New York-biased (it returned Troy, Chatham and Saratoga for Lawrence streets); call it directly with countryCode=USA and region=Kansas, and every street address came back as a PointAddress.
- The Register list coordinate for Holy Family in Eudora and the street address both fell on a house; the old stone church is the OpenStreetMap "Old Holy Family Catholic Church" 150 m west, which Commons photographs confirmed. Compare Commons photo positions with your pin when photo_find.py says "137 m from the pin".
- Kansas register summaries by page: the county search is alphabetical, ten to a page; my page numbers for each listing are in the place links.
