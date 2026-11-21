# wy_udiz: Wyoming: a first scatter
state: Wyoming
region: wy
date: 2026-11-21
places: 19
file: data_wy_udiz.py

## What this batch is
Nineteen places spread across Wyoming (outside Carbon County, which `wy_iwfl` covered), taken by `choose.py --thinnest` with 19 places on the map before and 38 after: Fort Laramie, Register Cliff and the Guernsey ruts on the North Platte; South Pass City and Miner's Delight in the South Pass gold district; Fort Bridger and the J.C. Penney mother store and house at Kemmerer; Mormon Row in Grand Teton; the Irma Hotel, Heart Mountain and the Old Faithful Inn in the northwest; Trail End, the Sheridan Inn and Fort Phil Kearny round Sheridan; the territorial prison and the Ames pyramid on the Laramie Plains; Fort Caspar, Fort Fetterman and the Cheyenne depot. Wikipedia was read as raw text with `wiki_raw.py`; hours and access come from the managers' own pages read with `page.py` (Wyoming State Parks "about-" pages, NPS hours and fee pages, the BLM, the City of Casper's Fort Caspar page, the Heart Mountain foundation, the Cheyenne Depot Museum, Yellowstone National Park Lodges, the Irma and the Sheridan Inn). Not checked: anything on the ground; fees at most state sites; the Irma's restaurant hours (`hours='?'`); the J.C. Penney House's hours, which come only from an undated WyoHistory.org field-trip page (`conf='mixed'`), and whether the old store still trades; whether a park gate stands on Antelope Flats Road for Mormon Row; winter access to Miner's Delight; whether Fort Fetterman's grounds may be walked out of season. Pins moved on the aerial: Fort Laramie (the Wikipedia point was 1.7 km east, in a field by the bridge) and Fort Fetterman (600 m southeast in sage). Pins at `site` precision because the exact building was not picked out: Fort Laramie (parade ground), Fort Bridger, the territorial prison, Fort Caspar (on the modern museum; the stockade is 150 m northwest), Heart Mountain (on the interpretive center, not the barracks), Miner's Delight (small roofs seen beside the pin). Red brick was left '?' for most; 'some' for Heart Mountain only because the foundation's page names the red brick hospital chimney.

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Sunrise Mine Historic District | Sunrise, Platte County (42.33194, -104.70306) | Wikipedia: CF&I iron-mining company town, Register district 2005, glory hole and brick housing | Owner and whether visitors are let in |
| Gebo ghost town and cemetery | 11 miles north of Thermopolis (43.79083, -108.23028) | Wikipedia: coal town 1907-1938, bulldozed 1971, some buildings and the cemetery remain | What stands, owner, access |
| Atlantic City and St. Andrew's Episcopal Church | Atlantic City, Fremont County (church 42.4969, -108.7308 from the Register list) | Register-listed church and Carpenter Hotel district; Wikipedia's town article names the Atlantic City Mercantile | A source on the church and the Mercantile, hours |
| Fort Washakie and the Wind River Agency blockhouse | Fort Washakie, Wind River Reservation | Register historic district; Shoshone-Episcopal Mission destroyed by fire 2016 | Reservation land: a tribal page inviting visitors (GUIDE.md section 8) |

## Tips
- Wyoming State Parks "about-" pages give hours, phone and address in one run after "Hours . ." when read with `page.py --all -n 40000`; Ames Monument has no "about-" page (404) but `index.php/places-to-go/ames-monument` reads.
- Wikipedia's coordinate for Fort Laramie National Historic Site is about 1.7 km east of the fort, and Fort Fetterman's about 600 m southeast of the buildings; `nom.py "Fort Laramie National Historic Site"` and `nom.py "Fort Fetterman State Historic Site"` were nearer.
- `parking.py` near Trail End, Sheridan, offered a high school's lot first; check that a lot is not a school's.
- The BLM's Miner's Delight page and its South Pass page give two different phone numbers for the Lander Field Office (382- and 332-8400); neither was used.
