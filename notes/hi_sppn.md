# hi_sppn: Kauaʻi, Maui, Molokaʻi, Lānaʻi and Hilo
state: Hawaii
region: hi
date: 2026-11-23
places: 20
file: data_hi_sppn.py

## What this batch is
A first scatter on the Hawaiian islands the Atlas barely had: Hawaii was the state with the fewest places (36, all on Oʻahu and West Hawaiʻi plus the Kōloa mill), claimed with `choose.py --thinnest`. Twenty places: on Kauaʻi, Pāʻulaʻula (Russian Fort Elizabeth), Kīkīaola (Menehune Ditch), Grove Farm, the Kauaʻi Museum (Wilcox Building), Alekoko Fishpond, Waiʻoli Mission House and Kīlauea Point Lighthouse; on Maui, the Bailey House, Kaʻahumanu Church, Halekiʻi-Pihana heiau, Holy Ghost octagonal church in Kula, Piʻilanihale Heiau at Kahanu Garden and Makawao Union Church; on Molokaʻi the R. W. Meyer Sugar Mill; on Lānaʻi the Kaunolū Village Site; on Hawaiʻi Island, the Lyman Mission House, Haili Church and Palace Theater in Hilo, the Star of the Sea Painted Church at Kalapana and the Old Volcano House (Volcano Art Center Gallery). Hawaii now has 56. Candidates came from `wiki_raw.py --rows` on "National Register of Historic Places listings in Hawaii" (Kauaʻi, Maui, Molokaʻi, Lānaʻi rows) and "... on the island of Hawaii"; facts from Wikipedia via `wiki_raw.py`, and access and hours from the pages of whoever runs each place, read with `page.py` (state parks, US Fish and Wildlife Service, NPS, Grove Farm, Kauaʻi Museum, Maui Historical Society, Kula Catholic Community, NTBG, Makawao Union Church, Lyman Museum, Haili Church, Palace Theater, Volcano Art Center). Archived copies were used for Grove Farm (February 3, 2026), Kīlauea Point (October 21, 2026), the Lyman Museum (January 9, 2026) and Go Hawaii's Kaunolū page (September 17, 2025); each entry says so. Not checked: hours for Kahanu Garden, the Molokaʻi Museum, the Painted Church, the Volcano Art Center and Kaʻahumanu Church's services; Grove Farm's tour days; Haili Church's service day; who owns Kaunolū (marked view-only); none was visited. Pāʻulaʻula has been closed for construction since March 24, 2025 "until further notice", and after Hurricanes Nolo and Lowell the state said on November 12, 2026 that most Kauaʻi state parks remained closed: the entry says so. Pins: two Register/Wikipedia points were well off and were moved onto what the aerial shows (Alekoko pond 480 m, Piʻilanihale's stone platform 550 m); the Kaʻahumanu Church Register point is over 1 km off and the OpenStreetMap point was used; Kaunolū was under cloud and is an area pin. Sources disagree on the Meyer mill (Wikipedia: animal power, 1876–1889; NPS: 1878 mill with a steam engine) and on the Bailey House hours: both given, `conf='mixed'`. Red brick: 'no' only where a source says stone, wood, concrete or lava rock; '?' elsewhere.

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Chee Kung Tong Society Building | Wailuku, HI (20.893333, -156.508056) | Register list row: collapsed in 1996, only the gate and foundation remain | A source on access and whether the gate still stands; look on the aerial |
| Haraguchi Rice Mill | Hanalei Valley, HI (22.2097, -159.4767) | Register list row: one of four former rice mills in Hanalei Valley | Owner, tour or viewing arrangements |
| Wailua Complex of Heiaus | Wailua, Kauaʻi (22.04372, -159.335959) | Register row; in Wailua River State Park | Which heiau to pin; state park page, and whether the park is open after the 2026 hurricanes |
| Kalaupapa and Molokaʻi Light | Kalaupapa, Molokaʻi (21.212222, -156.9725) | Wikipedia: grounds and tower closed to visitors; the peninsula is restricted | NPS rules for entering Kalaupapa now |
| Wananalua Congregational Church and Hāna courthouse | Hāna, Maui (20.752002, -155.986579) | Register rows | Wikipedia title not found; a source on the church |
| Honokaʻa main street (People's Theatre, Bank of Hawaiʻi, Hotel Honokaa Club and others) | Honokaʻa, HI (20.0792, -155.4677) | Many Register rows on one street (list "on the island of Hawaii") | Sources for each building; a good first stop for the next Hawaiʻi Island batch |
| Hilo downtown (District Courthouse, S. Hata Building, Federal Building, Volcano Block) | Hilo, HI (19.7290, -155.0890) | Register rows with coordinates | Read the Register forms |

## Tips
- In this container the pin check and `photo_find.py look` failed with "cannot import name '_imaging' from 'PIL'" until `python3 -m pip install --break-system-packages --ignore-installed Pillow` (the fix an earlier note gave); also `setup.sh` reported every module missing because plain `pip` installs for Python 3.11 while `python3` is 3.13 here: use `python3 -m pip`.
- The Hawaii state parks pages carry the statewide closure notices; the Pāʻulaʻula page's own construction closure notice (March 2025) sits at the top, above "Hours", and the `-g` summary drops it: read with `--all`.
- `nom.py` did not find Russian Fort Elizabeth, Piʻilanihale, Kīkīaola, Makawao Union Church, the Molokaʻi Museum or Kaunolū by name.
- HMdb's marker for the Menehune Ditch (m=27646) gives a position about 600 m from the Register point, on the road beside the ditch.
- `lymanmuseum.org` answers 403 to `page.py`; the archived copy read. The `kulacatholiccommunity.org` Mass schedule page mixes two churches: the Holy Ghost times follow "HOLY GHOST MISSION".
