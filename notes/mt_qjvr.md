# mt_qjvr: Montana: Great Falls, Bozeman, Miles City, Dillon, Lewistown and the high plains
state: Montana
region: mt
date: 2026-11-24
places: 13
file: data_mt_qjvr.py

## What this batch is
Thirteen places spread over Montana (Great Falls, Bozeman, Miles City, Dillon, Lewistown, Red Lodge, Fort Shaw, White Sulphur Springs, Troy, Scobey), taken from Wikipedia's National Register county lists and articles, the Register nomination forms for the Kent barn and Troy jail, the Gallatin History Museum, C. M. Russell Museum and USDA pages. Hours are confirmed only for the Gallatin History Museum and the C. M. Russell Museum (their own pages). Not checked: the Paris Gibson Square, Fort Shaw and Olive Hotel own pages (could not be opened or not found), present use of the Kent barn and Hotel Metlen, what is left at Fort Logan and Fort Keogh, and every interior. Brick is '?' where no source or picture settled it. Six pins (Fort Shaw, Fort Keogh, Fort Logan, Kent barn, CM Russell, Metlen) are only the area: the aerial did not show the building.
Pictures: Paris Gibson Square and Fort Shaw have Commons photographs; the Russell house has none.

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Fergus County leads: Reed's Fort post office, Symmes Park Missile, Lewistown Carnegie Library | Lewistown, MT (47.06, -109.43) | On the Register list | No article or manager page read |
| Fromberg opera house, depot and bridges | Fromberg, MT (45.39, -108.91) | On the Register list | No source read |
| Double Arrow Lookout and Lodge | Seeley Lake, MT (47.16, -113.53) | On the Register list | No article or Forest Service page read |
| Missoula hotels (Florence, Brunswick, Grand Pacific) | Missoula, MT (46.875, -113.992) | Wikipedia articles exist | Not read; current use unknown |

## Tips
- WebSearch gives hours and phone numbers fast, but they come from directories; page.py on a museum's own site worked for Gallatin and Russell once the cached HTML was read (research/pages).
- `tools/page.py` text output for some sites is one flat line; grep the cached html in research/pages for the hours.
- Guessed museum web addresses usually fail; take the address from a search result first.
