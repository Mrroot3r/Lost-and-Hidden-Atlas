# wy_kxrt: Wyoming: a second scatter
state: Wyoming
region: wy
date: 2026-11-23
places: 8
file: data_wy_kxrt.py

## What this batch is
Eight places in Wyoming, spread over the state: the Mountain View Hotel at Centennial, Pahaska Tepee near Cody, the Atlantic City Mercantile, the Johnson County Courthouse at Buffalo, Menor's Ferry in Grand Teton, Independence Rock, and the Historic Governors' Mansion and the State Capitol at Cheyenne. Wyoming had 38 places before and 46 after. Sources: Wikipedia as raw text (`wiki_raw.py`), WyoHistory.org, the Wyoming State Parks and National Park Service pages that opened, and web-search results for hours. Not checked: hours for the hotel, Pahaska, the Mercantile, the courthouse and the ferry (their own pages would not open or no page was found; Pahaska's tour times come from a Cody visitor guide, the Capitol's from a search result quoting the state's page); original interiors; who owns the Mercantile and Pahaska beyond "private business". Three Register/Wikipedia coordinates were wrong and were replaced with OpenStreetMap or address points (the Mercantile was a kilometre off in a field, Menor's Ferry was in the river, the Governors' Mansion on the Wikipedia infobox was elsewhere in town). Independence Rock has no picture (only rest-area signs on Commons).

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| St. Andrew's Episcopal Church | Atlantic City, Fremont County (42.4969, -108.7308 from the Register list) | Register-listed 2020s, no Wikipedia article | A source on the building and its services (the Mercantile row in LEADS.md is now on the map; this church remains) |
| Sunrise Mine Historic District | Platte County, near Hartville (42.3319, -104.7030) | Wikipedia: CF&I company town, 1898 to 1980, listed 2005 | Owner and whether the public may walk it; the WyoHistory and State Parks pages tried were 404 |
| Lander Downtown Historic District and the Post Office and Courthouse | Lander (42.8331, -108.7319) | NRHP rows only | Articles and an owner or hours |
| Fort McKinney | Buffalo (44.3328, -106.7394) | NRHP row: preserved buildings, 1878 to 1894 | Wikipedia has no article under that title; owner and access |

## Tips
- Wyoming State Parks pages open at `wyoparks.wyo.gov/index.php/places-to-go/<site>`; the `about-<site>` pattern in the earlier batch gave 404 for the Governors' Mansion.
- NPS `planyourvisit/<name>.htm` guesses and wyoleg.gov (drawn by script) did not read; a web search result quoting the page was the only way to get the Capitol's hours.
- Register points for Atlantic City and Menor's Ferry were far off; `nom.py` put both on the buildings.
