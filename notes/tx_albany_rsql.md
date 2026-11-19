# tx_albany_rsql: Texas Forts Trail: Albany, Fort Griffin and neighbours
state: Texas
region: tx
date: 2026-11-19
places: 22
file: data_tx_albany_rsql.py

## What this batch is
A first pass over the Texas Forts Trail country round Albany (region `tx` drawn at random by `choose.py`; the Atlas had nothing within 40 km). Twenty-two places in six counties: in Shackelford County, Fort Griffin State Historic Site, the Fort Griffin town site ("the Flat": civil jail and Masonic lodge hall), the 1885 Fort Griffin Brazos River Bridge, the 1896 Clear Fork (Woodson) suspension bridge, and in Albany the courthouse, the Old Jail Art Center, the Ledbetter Picket House, the White Elephant Saloon building and the Rye-Caperton House; in Jones County, Fort Phantom Hill, the Jones County Courthouse, the Anson Opera House and the old First Presbyterian church in Anson, and St. John's Methodist and First Baptist in Stamford; in Throckmorton, the courthouse and the 1893 jail museum; Fort Belknap near Newcastle (Young County); in Breckenridge, the Stephens County Courthouse and the Old First National Bank; in Baird, the T&P depot and the first Callahan County jail. Sources were read in this session with `page.py`, `wiki_raw.py` and `geo.py`/`nom.py`: HMdb marker texts (nearby lists round seven county seats), THC's Fort Griffin pages and visitors guide PDF, the Old Jail Art Center's visit page, the Fort Phantom Hill Foundation's home page, SAH Archipedia, Bridgemeister, the THC suspension-bridge page and three Register forms from the THC Atlas. Not checked: anything on the ground; hours for Fort Phantom Hill, Fort Belknap, the Throckmorton jail museum and the Baird depot museum (no page of their own could be read, so `hours='?'`); service times at the Stamford churches; who owns the Fort Griffin town lots, the Woodson bridge, Fort Belknap and the Anson Opera House; whether the Woodson bridge still carries traffic; whether the Anson Presbyterian church still opens as a museum; that the Breckenridge bank is the Swenson Memorial Museum (search results only). The Fort Griffin fort pin is on the ruins area, not a single building (`site`). The Throckmorton courthouse pin was moved onto the building the marker directions point to but the aerial is unclear (`site`). How much of Fort Griffin is original is given as the sources disagree (`conf='mixed'`); Fort Phantom Hill's chimney count differs between the foundation's page and Wikipedia.

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| SH 23 Bridge at the Clear Fork of the Brazos (1929) | U.S. 283 north of Fort Griffin, TX (32.932778, -99.215) | Register form 96001106 and SAH Archipedia: the only surviving THD standard Parker through truss; mentioned in the Fort Griffin bridge entry | A current check that it still stands (1995 rating made it eligible for replacement) and a pin on the aerial |
| Hubbard Creek Bridge | FM 601, 7.5 miles east of SH 6, near Albany, TX (32.690278, -99.164722) | Register form 96001105: 150-foot riveted Pratt through truss, state-owned | Its year, and whether it still stands |
| Matthews Memorial Presbyterian Church | 211 S. Jacobs St, Albany, TX (HMdb 86401) | Marker is RTHL 3257 only; an 1898 section and cornerstone per HMdb photos | A source for its history and service times |
| Fort Davis family fort | Clear Fork of the Brazos, Stephens County, TX (Register 92001363, 32.915278, -99.093056) | HMdb 93646: some 120 people lived there in the last year of the Civil War | Whether anything is left and whether there is public access |
| Callahan County Courthouse (1929) | Baird, TX (32.39486, -99.3943) | HMdb 80804: Voelcker & Dixon, Classical Revival | Left out as less worth a trip; add if a session wants Baird filled |
| Swenson Land & Cattle Co. headquarters | E. McHarg & S. Weatherbee St, Stamford, TX (HMdb 92580) | Headquarters here from 1927 | What the building is and its age |

## Tips
- In Texas, HMdb nearby lists (5 miles) round seven county seats gave nearly every candidate and its position; a short loop of `page.py --all` on marker pages, cut between "Inscription." and "Topics.", reads 30 markers in a few minutes.
- `geo.py` with ", TX" and a ZIP gave PointAddress matches on the building for every Albany, Anson and Breckenridge address tried.
- THC Fort Griffin: the history page is at `thc.texas.gov/state-historic-sites/fort-griffin/fort-griffin-history` (the `historic-sites/...` form is 404); the visitors guide PDF lists every ruin and reconstruction.
- Small-town museums here (Fort Belknap, Baird depot, Throckmorton jail) had no page of their own that a search found; only directories (museumsusa, texastimetravel, mapquest), which are not sources for hours.
- `resync.sh` was needed once (two batches merged while working); a new batch time and a new branch name worked.
