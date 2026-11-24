# ks_lvft_rxne: Kansas: Leavenworth and Fort Leavenworth
state: Kansas
region: ks
date: 2026-11-24
places: 14
file: data_ks_lvft_rxne.py

## What this batch is
Fourteen places in and near Leavenworth, Kansas, that the first Leavenworth batch (ks_xqpd) left out: the A. J. Angell, Merritt Insley, Nathaniel Burt, David Powers and Leanna Giles houses, the William Small Memorial Home, North Broadway and Sumner schools, the AXA Building, the Helmers furniture works, Greenwood Cemetery, the Richard Allen Cultural Center, Stonehaven Farm near Tonganoxie, and the Fort Sully earthwork on Fort Leavenworth. Sources were the Kansas Historical Society's register search (Leavenworth County, six pages), National Register forms read as text from NPGallery (Angell, Insley, Powers), and Wikipedia read one article at a time. The ArcGIS address lookup gave the pins; every pin was looked at on the aerial and the LiDAR sheet. Brick answers come from Commons photographs opened in the session (Angell, Insley, North Broadway, Helmers and Powers red; the Small Home buff) or from a source that says "red brick" (AXA); the rest are '?'. Pictures: ten places had no Wikipedia picture; seven got one from Commons, and Sumner, Giles and Stonehaven have none. Not checked: who owns or uses any of the houses today (the forms are from 1977 to 1987 for several), interiors, hours of the Richard Allen Center (its own page would not load), the Fort Leavenworth visitor rules (the Army page returned an error; the gate rules come from a web search result that quoted it). Fort Sully's pin is Wikipedia's coordinate and marks the area only; on the aerial it falls on a small round feature with a loop of road, and the long earthwork was not made out on the aerial or the LiDAR.

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Senator William A. Harris House | Linwood, KS, a quarter mile west of town on K-32 | National Register 74000841: an 1883 Stick and Eastlake frame house on a limestone base, built for the Shorthorn breeder and later U.S. senator | The aerial showed no house at that spot; a street address or owner is needed before it can be pinned |
| Delaware Cemetery | 10388 222nd St, Linwood, KS | Listed in 2020; first burials Delaware families from about 1860 to 1867 (Kansas Historical Society) | The address lookup put the address in Douglas County, so the real position is unknown |
| Leavenworth Landing Historic District | 201-221 Delaware St, Leavenworth, KS (39.31827, -94.91097) | State Register 1981, Italianate commercial buildings | No description beyond the style; the state nomination was not read |
| Abernathy/Lyle House | 508 S Broadway, Leavenworth, KS | State Register 1989: Classical Revival, Italian Villa and Italianate house | The state nomination was not read |
| Lamborn, Holman and Stonehaven-type farmsteads | Delaware Township and Tonganoxie, Leavenworth County | Register listings 2011 to 2023 with short summaries | Private working farms; no addresses safe to pin without a source for public views |
| Fort Leavenworth National Cemetery | Fort Leavenworth, KS (39.35139, -94.93056) | Established 1862, used from 1844; Wikipedia and Register 99000834 | Whether visitors may go in without a pass, from the cemetery's own VA page |
| Frontier Army Museum | 100 Reynolds Ave, Fort Leavenworth, KS | Web search results give Tuesday to Friday 9 to 4 and Saturday 10 to 4, closed Mondays and federal holidays; one site says Thursday and Friday only | Hours from the Army's own page, and the history of its building |

## Tips
- kansashistory.gov's register search pages (`page.py --all`, pages 1 to 6 for a county) give a summary for most listings and the state-register ones too; splitting the text on "Listed in National Register" finds each record. Many listings have no Wikipedia article, so this is the best source for Kansas.
- NPGallery text forms for 1970s and 1980s Kansas listings read cleanly with `page.py --all` and a grep for sentences with years; `-g` alone cut off the history.
- `photo_find.py look` gave a good wide photograph for most Leavenworth listings because a Commons user photographed the whole county list; those photographs also settle red brick.
- The ArcGIS address lookup put every Leavenworth street address on the right building, but returned a house in another county for a rural address (Delaware Cemetery); check the county.
- home.army.mil pages (Fort Leavenworth) returned HTTP 502 from `page.py`; the web search result text was all there was.
