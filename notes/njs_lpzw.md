# njs_lpzw: Burlington County, New Jersey: Pine Barrens iron and cranberry towns, Mount Holly, Quaker meeting houses
state: New Jersey
region: njs
date: 2026-11-19
places: 17
file: data_njs_lpzw.py

## What this batch is
Seventeen places in Burlington County, the first pass there (region `njs`, drawn with `choose.py`): Batsto Village, Atsion Mansion, the Martha Furnace site, the Hampton Furnace ruins, the Friendship cranberry village ruins, Whitesbog Village (all Wharton or Brendan T. Byrne State Forest); the Burlington County Prison museum and the Old Schoolhouse in Mount Holly; Smithville; Kirby's Mill; Peachfield; Point Breeze (Joseph Bonaparte's estate, now a state park with the 1820 Gardener's House); Arney's Mount and Crosswicks Friends meeting houses; St. Mary's Church, Burlington; the North Pemberton station; the White Horse Inn (Shamong Hotel) in Chatsworth. Sources: Wikipedia with `wiki_raw.py` (the county's Register list with `--rows`), HMdb markers (nearby lists and marker pages through `page.py`), the Pinelands Alliance ghost-town page (the only source for Hampton Furnace and Friendship), Journey Through Jersey for state and county site hours, and the operators' own pages (whitesbog.org, peachfield.org, drgreenway.org, stmarysburlington.org). Not checked: anything on the ground; Wharton State Forest hours and rules (no state page opened); Kirby's Mill current opening (only 2011–2017 sources); the Point Breeze Discovery Center hours (taken from D&R Greenway's opening announcement, undated); the White Horse Inn's present use; times of worship at Arney's Mount and Crosswicks; which building at the Arney's Mount junction is the meeting house (pin on the road junction, `prec='site'`); the Martha furnace mound itself (pin is the Wikipedia point on the Batona Trail, `prec='area'`). Red brick: one `yes` (Old Schoolhouse, from a Commons photo), one `no` (Arney's Mount, stone per Wikipedia), the rest `?`. Pins with no thing seen: Martha Furnace (area), Friendship (open field where the source puts the foundations).

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Buzby's General Store | Chatsworth, NJ (39.819167, -74.535556, Register list) | Built 1865 at Routes 532 and 563; run by the Buzby family for 102 years; John McPhee's base for The Pine Barrens (PhillyVoice, Stockton blog); Register 04000222; closed and put up for sale (PhillyVoice, date not read) | Its present owner and use; whether it opens |
| Hermann (glass works ruins) | Mullica River, Washington Township, Burlington County, NJ | Pinelands Alliance: site of a late 19th-century glass factory, several ruins in the forest along the river, Wharton State Forest | A coordinate and a second source |
| Pasadena / Brooksbrae brick works ruins | Manchester Township, Ocean County, NJ (Pasadena WMA about 39.892, -74.416) | Pinelands Alliance: extensive ruins of a brick-making factory in the woods; it names Brendan Byrne State Forest | A coordinate for the ruins and the owner (state forest or WMA) |
| Hanover Furnace | Browns Mills, NJ | Register 74001155; no coordinate in the Wikipedia list | Any source on what is left and where; likely inside Joint Base McGuire-Dix-Lakehurst (not checked) |
| Alloway blueberry farm | Washington Township, NJ (39.73662, -74.57920, HMdb 298769) | Marker: one of the first cultivated blueberry farms, now abandoned and returning to forest, state-owned; 950 ft down a path off Hawkins Bridge Road | Whether anything stands; a second source |
| Speedwell furnace site | Tabernacle Township, NJ (39.76414, -74.544562, HMdb 244465) | Marker: sawmill 1770, furnace and forge 1773 by Benjamin Randolph; log house stood until 1948 | Whether anything is left to see |
| Francis Hopkinson House | Bordentown, NJ (40.148333, -74.713889) | Register 71000496 | A source on the house today and its access |
| Upper Springfield Meeting House | Wrightstown, NJ (40.043649, -74.640909, HMdb 35918) | Register 79001479 | Read the marker and a source on the building |

## Tips
- Journey Through Jersey slugs that worked here: `batsto`, `atsion-mansion`, `burlington-county-prison-museum`, `historic-smithville-park`, `north-pemberton-railroad-station-museum`; `kirbys-mill`, `peachfield`, `whitesbog-village` and `whitesbog` are 404. The hours sit in the first 700 characters of `page.py --all`.
- The nj.gov Whitesbog brochure PDF (`.../historic/docs/Whitesbog_11 x 17 version_web.pdf`) answered 404 to `page.py`; the HMdb Whitesbog markers (35117, 34274) and whitesbog.org's FAQ cover the same ground.
- The Pinelands Alliance ghost-town page (`page.py --all -n 7000`) lists Atsion, Batsto, Friendship, Hampton Furnace, Harrisville, Hermann, Martha, Pasadena and Weymouth with one line on what is left of each.
- `look.py ... --lidar` fails ("not enough values to unpack"); the `--lidar` sheet from `pincheck.py` was enough.
- The Register coordinate for Arney's Mount Friends Meetinghouse is in woods 110 m from the junction its article names; the ArcGIS intersection search ("Juliustown Rd & Arneys Mount Rd") gave the junction.
- `publish.sh` stopped once because main had moved; `resync.sh` then a fresh batch time worked as the guide says.
