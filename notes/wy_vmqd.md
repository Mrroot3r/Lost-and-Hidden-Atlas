# wy_vmqd: Wyoming: a third scatter
state: Wyoming
region: wy
date: 2026-11-23
places: 13
file: data_wy_vmqd.py

## What this batch is
Thirteen places across Wyoming, taken by `choose.py --thinnest` with 46 places on the map before and 59 after: Cambria Casino near Newcastle, the Reliance Tipple, Point of Rocks Stage Station, the Sunrise iron-mine town, the Union Pacific roundhouse at Evanston, the Rock Church at Auburn, Gebo ghost town (a LEADS.md row, now removed), Fort Yellowstone at Mammoth, the Swan Land and Cattle headquarters at Chugwater, Names Hill, Hotel Higgins at Glenrock, the Aladdin general store and Welty's store at Dubois. Sources: National Register county lists and Wikipedia as raw text, WyoHistory.org, Wyoming State Parks pages (Point of Rocks, Names Hill), and web-search results for access and hours. Every pin was looked at on the aerial and LiDAR sheets.

Not checked: hours for every private business (Higgins, Aladdin, Welty's, Evanston roundhouse is only a third-party listing); who owns Sunrise (a search result says private), Gebo, Swan and Cambria, and what can be seen from the road at each; the inside of any building; brick for Fort Yellowstone and Gebo (`?`). Gebo's pin is Wikipedia's town position, not the cemetery. Names Hill's coordinate agrees with Wikipedia, the BLM and HMdb (the state parks page gives a latitude a degree off).

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Hot Springs State Park State Bath House | Thermopolis (43.65, -108.20) | Free public bath house; winter hours Mon–Sat 8–5:30, Sun 12–5:30 per state parks search result | Building's history and original fabric from a source |
| Downtown Thermopolis, Newcastle Commercial District, Thermopolis Hot Springs | Thermopolis and Newcastle | Register districts; start.py lists both old centres with no Atlas place | Which buildings stand and what each is |
| Fort Washakie Historic District, St. Michael's Mission | Fremont County | On the Register list | Whether visitors are invited on the reservation |
| Jackson Park Brick Row, Lander Downtown | Lander | Register listings | Sources and pins |

## Tips
- wyoparks.wyo.gov pages for Point of Rocks and Names Hill read with `page.py --all -n 40000`; grep for "Hours" because the menu fills the first 2,000 characters.
- Sweetwater County Museum's own tipple page is a 404; WyoHistory.org's field-trip pages (`/field-trips/<name>`) gave short access notes for several sites.
- `nom.py` found nothing for Names Hill, the roundhouse at Evanston or Cambria; Wikipedia coordinates were right for Names Hill and the roundhouse needed `osmnear.py ... -g ound`.
