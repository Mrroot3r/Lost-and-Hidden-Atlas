# hud_gfhh: Northeast Dutchess: Pine Plains, Millerton, Amenia and Wassaic
state: New York
region: hud, midh
date: 2026-11-20
places: 14
file: data_hud_gfhh.py

## What this batch is
Fourteen standing places in northeastern Dutchess County, drawn at random by `choose.py --state ny` (region `hud`, which offered Philmont, Millerton and Pine Plains); the Atlas had nothing between the Taconic Parkway and the Connecticut line here except the Bennett College site. Pine Plains: the Graham-Brush Log House (a lead from `LEADS.md`, row deleted) and Stissing House tavern. Stanford: Attlebury Schoolhouse and Bangall Post Office. North East: the Irondale Schoolhouse at the Millerton rail-trail entrance, the Moviehouse (1905 Grange hall) and the Ezra Clark House at Coleman Station. Amenia: Beth David Synagogue, Indian Rock Schoolhouse, Troutbeck, Smithfield Presbyterian Church, St. Thomas' Amenia Union (Upjohn) and Maxon Mills at Wassaic. Millbrook (`midh`): the Nine Partners brick meeting house. Sources read in the session: Wikipedia with `wiki_raw.py` (the Dutchess County Register list with `--rows`), and with `page.py` the Little Nine Partners Historical Society, stissinghouse.com, The Millerton News, troutbeck.com, wassaicproject.org, stthomasamenia.com, the Episcopal Asset Map, ameniany.gov, The Millbrook Independent, Cinema Treasures, the Pomeroy Foundation and HMdb marker pages. Not checked: hours for Stissing House, Troutbeck, the Moviehouse and Bangall Post Office (`hours='?'`); the Irondale Schoolhouse hours come from a 2025 Millerton News report, not the association's own page; no service times for Beth David, Smithfield or Nine Partners; no interiors seen. Red brick for Beth David, Nine Partners and the Ezra Clark House was settled from the Wikipedia photographs (`brick.py look`). All pins looked at on the leaf-off aerial and LiDAR; Indian Rock Schoolhouse and Bangall Post Office are Register-list points at `site` precision, beside but not plainly on the building. Ruins are thin in this ground: the one real ruin found, the Wassaic charcoal kilns, is in the Leads table below.

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Wassaic beehive charcoal kilns | Wassaic, Amenia, NY (woods by NY 22 near Deep Hollow Road; HMdb 138022 marker at 41.80668, -73.56333) | Two stone beehive kilns of the Reed, Gridley and Co. iron works (in business by 1829), about 30 ft across and 16 ft high; Pomeroy marker says they are all that remains (HMdb); Atlas Obscura says they are not visible from the road, and a user comment says they were fenced off in May 2023 | Owner, and whether any public way lets them be seen; exact pin |
| Irondale (Millerton Iron Company furnace) | Town of North East, NY, north of Millerton on NY 22 | Wikipedia (Millerton): a furnace with two Cooper hot-blast stoves making car-wheel pig iron, 12,000 tons a year in 1890, with a company store, grist mill and post office | Whether anything of the furnace is left, and where |
| Dover Stone Church | Dover Plains, NY (41.73816, -73.58851) | On the Register: a waterfall cave shaped like a church window, promoted by the Harlem railroad as a sight | Not a building; add only if a session takes natural sights with a history |

## Tips
- In northeastern Dutchess the HMdb nearby list returned the same hundred markers whatever the centre, most of them 1930s state "Site of" markers with nothing left to see; the Register list (`wiki_raw.py --rows -g` with the town and hamlet names) gave nearly every place.
- `theharlemvalleynews.net` article addresses now serve a gambling spam page: do not use it as a source.
- `stissinghouse.com` and the Millbrook Historical Society's event pages are drawn by script; `page.py` gets nothing from them.
- NPGallery's text for St. Thomas' Amenia Union (05000261) is the placeholder; the parish's own history page (stthomasamenia.com/history) has the architecture.

