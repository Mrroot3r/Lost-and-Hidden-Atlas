# nd_ssxv: North Dakota: forts, homesteads and landmarks across the state
state: North Dakota
region: nd
date: 2026-11-21
places: 19
file: data_nd_ssxv.py

## What this batch is
Nineteen places scattered across North Dakota away from Bismarck and Mandan, which the only earlier batch (nd_cumj) covered; claimed with `choose.py --thinnest` (nd had 19 places). Frontier forts (Fort Totten, Fort Buford, Fort Abercrombie, Fort Ransom's ditched square), fur-trade and Native sites (Gingras Trading Post, Fort Clark's village and posts), the Whitestone Hill battlefield, the Hudson paper town, homesteads and houses (Chateau de Mores, Maltese Cross Cabin, Welk Homestead, Wadeson Cabin, Bagg Bonanza Farm), Oscar-Zero missile alert facility, the Stutsman County Courthouse, the Hi-Line Railroad Bridge, the Sims church and parsonage, the Grassy Butte post office and the Fargo Theatre. Sources: the State Historical Society of North Dakota's site pages (read whole with `page.py --all`; all hours and fees for SHSND sites come from them), NPS pages for the Maltese Cross Cabin, McKenzie County Tourism for Grassy Butte, fargotheatre.org, HMdb markers (Wadeson Cabin, Hudson) and Wikipedia via `wiki_raw.py`. Pins from Wikipedia, the ArcGIS geocoder and HMdb, all looked at on the aerial and LiDAR; Fort Ransom and Fort Clark were moved onto what the LiDAR shows. Not checked: hours for Bagg Bonanza Farm (its site would not open), Sims church and museum, Grassy Butte, the Fargo Theatre box office and the TRNP visitor center (all `hours='?'`); the Chateau de Mores house and the Stutsman courthouse are not picked out on the aerial (pins `area`/`site`); Hudson's pin is the HMdb marker at a road corner; Abercrombie, Fort Clark and Gingras parking not found. Disagreements left in the text: Welk house 1899 or 1893, Wadeson Cabin 1876 or 1878, Grassy Butte post office 1912 or 1914. Brick '?' on Fort Buford, Fort Abercrombie, Bagg farm and the Fargo Theatre.

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Assumption Abbey church | Richardton, ND (46.889, -102.32, Wikipedia) | Benedictine abbey founded 1893, at Richardton since 1899 (Wikipedia) | The abbey's own page: assumptionabbey.org is the Missouri abbey at Ava; building date, fabric and visiting times not read |
| Oak Lawn Church site | 11 miles south of Walhalla, at ND 5 and ND 32 | SHSND: log church of 1885 burned 1954; cemetery and fieldstone marker remain | A coordinate; left out as a marker-only site |
| Fort Union Trading Post | Williston vicinity (47.999444, -104.036944) | NPS site; the buildings are reconstructions | NPS hours page; whether a reconstruction is wanted |
| Grand Forks County Courthouse | Grand Forks (47.92278, -97.02944) | 1913-14 limestone Beaux Arts courthouse with a cast iron dome (Wikipedia) | Whether visitors may go in, from the county's page |
| T. J. Walker Historic District | Fort Ransom, ND (46.521667, -97.930278) | Mill and buildings of miller T. J. Walker, 1880 on (Register) | What stands and who shows it |
| Ronald Reagan Minuteman Missile Site: November-33 | 2 miles east of Cooperstown on ND 200 | SHSND: launch facility topside left intact | A pin of its own |

## Tips
- SHSND's smaller sites (Oak Lawn, Wadeson, Hudson, Ransom) print a menu block that `sed` cuts badly: read them after "Subscribe to SHSND podcasts."
- `nom.py` found almost nothing in rural North Dakota; the ArcGIS geocoder's POI matches (Fort Ransom SHS, Sims Lutheran Church, Bagg Bonanza Farm) and street addresses from the SHSND pages worked.
- `pincheck.py --lidar` on 19 pins takes longer than two minutes: run it with a longer timeout.
- `photo_find.py new` listed Fort Totten as having no picture although its article has one; it found a usable public-domain HABS photo anyway.
