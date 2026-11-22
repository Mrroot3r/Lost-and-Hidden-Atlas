# mn_gecb: Minnesota: a second scatter, border to bluff country
state: Minnesota
region: mn
date: 2026-11-22
places: 16
file: data_mn_gecb.py

## What this batch is
Sixteen places spread across Minnesota, which had 32: St. Nicholas Orthodox Church at Caribou on the Canadian line, the Larson Mill in Old Mill State Park (Argyle), Phelps Mill (Otter Tail County), the Hull–Rust–Mahoning Mine View at Hibbing, Milford Mine Memorial Park (Cuyuna Range), Two Harbors Light Station, the Charles Lindbergh House at Little Falls, the End-O-Line turntable at Currie, Danebod at Tyler, the Hermann Heights Monument at New Ulm, the 1859 Little Stone Church at Ottawa, the Cathedral of Our Merciful Saviour at Faribault, Sibley Historic Site at Mendota, the Ramsey Mill ruins at Hastings, the Sheldon Theatre at Red Wing and the Willard Bunnell House at Homer. Sources: Wikipedia read with wiki_raw.py and its county Register lists; Register forms with page.py (98000872, 73000983, 84001480, 70000303); MNopedia; SAH Archipedia; the New Ulm Journal (April 15, 2026: the Hermann Monument's inside closed); managing bodies' pages, most drawn by script and read with a ten-line Playwright script on November 22, 2026. Not checked: nothing on the ground; museum hours at Two Harbors Light Station and the Bunnell House (no tour days listed in November); summer hours at Sibley (closed for the season when read) and the Lindbergh House (MNHS gives only trail hours); Sunday service times at the Faribault cathedral; owner and access at St. Nicholas, Caribou (view only); opening of the Ottawa church; park hours at Milford, Hastings and New Ulm. Pins marking only an area: Milford Mine (park woods, not a foundation), Ramsey Mill (park on the bluff about 150 m above the walls in the gorge), Hull–Rust (the overlook, not the pit). Only Hull–Rust got a picture looked for; the End-O-Line turntable still waits (photo_find.py look hung).

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Tunnel Mill | Spring Valley, MN (43.761811, -92.380018) | 1871 gristmill powered by a tunnel cut through a creek bend; Register list (75000978) | Owner and whether the public may see it; article title not found |
| Toogood Barns | Rochester, MN (44.000194, -92.472553) | Stone barns of about 1870; Register list (75001003) | Owner, access, present state |
| Mayowood Historic District | Rochester, MN (43.994536, -92.519163) | Charles H. Mayo's estate from 1911; Register list (70000306) | Tour season and the managing body's page |
| Dr. William W. Mayo House | Le Sueur, MN (44.4622, -93.9151) | 1859 home and clinic of W. W. Mayo; Register list (69000074) | Who runs it now and its hours |
| Gran Evangelical Lutheran Church | Bagley vicinity, MN (47.543333, -95.484722) | 1897 log church, the first in Clearwater County; Register list (88000593) | Owner, access, pin on the aerial |

## Tips
- MNHS, Winona County Historical Society, Hibbing Mine View, Sheldon Theatre, Danebod and Crow Wing County pages are drawn by script; the Playwright recipe in notes/mn_axba.md (proxy from HTTPS_PROXY, waitUntil networkidle, innerText of body) read them all. faribaultcathedral.com and fmr.org time out on networkidle but still return their text.
- MNHS's Lindbergh House page (November 2026) lists only trail hours; the house's own season was not on the page.
- `photo_find.py look` hung for over six minutes on two places (candidates printed for the first, no sheet drawn); the first was set from its candidate list.
- Wikipedia's Register point for the Ramsey Mill ruins in Hastings is in the park on the bluff, not at the walls in the gorge.
