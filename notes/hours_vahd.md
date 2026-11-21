# hours_vahd: hours for 2 churches and 21 museums, theatres and other open places in New York
state: New York
region: ny
date: 2026-11-21
places: 0
file: hours_vahd.py

## What this batch is
An "hours" session (PROMPTS.md type 7): no new places and no pins. `tools/hours.py` showed only two places of worship still waiting anywhere (both in New York), so they were taken first, then New York's museums, house museums, theatres and other places that take visitors, from `tools/hours.py list "New York"`. 23 places recorded: 14 with times from the page of whoever runs them, read in the session with `hours.py page` or `page.py --all` (two, Arkell and Whiteface, read with the web fetch tool because the page reader was refused), and 9 recorded `?`.

Hours recorded (the page is in the file; the address or town on each page was checked against the place):
- Syracuse Weighlock (Erie Canal Museum), 318 Erie Blvd E: daily 10 to 4.
- Cayuga Museum and Case Research Lab, 203 Genesee St., Auburn: Wednesday to Saturday 10 to 5, lab tour times.
- Hanford Mills Museum, 51 County Highway 12, East Meredith: mid-May to mid-October; the page says closed for 2026, reopening May 15, 2027.
- Arkell Museum, 2 Erie Boulevard, Canajoharie: March to December hours. The same site also says "open for the 2025 season", so the hours may not have been updated for 2026.
- Cottage Lawn, 435 Main Street, Oneida: self-guided and guided tour times from the Madison County Historical Society's page.
- The Old House, Cutchogue (27320 Route 25): the Historical Council's tour season and times.
- Cedar Hill Schoolhouse, 1003 River Road: the page says only that "Regular Sunday Museum Hours concluded October 25"; no times given.
- General Jacob Brown Mansion: the hours are the Brownville-Glen Park Library's (216 Brown Blvd.), which Wikipedia says is in the mansion with the village offices. Village office hours were not found.
- Whiteface Veterans Memorial Highway: ORDA's page, 2026 season (May 15 to October 12), 8:45 to 5:30.
- Old Stone Barracks: Valcour Brewing Company's hours (49 Ohio Ave).
- Montgomery Worsted Mills: City Winery Hudson Valley (23 Factory St). The page reader caught Tuesday to Sunday; Monday was not in what it printed, so it is left out.
- Cohoes Music Hall: box office hours (58 Remsen St.).
- Glove Theatre: shows only; doors 45 minutes before each show (42 North Main Street).

Not checked: nothing was seen on the ground and no telephone call was made.

## Pages that would not open, or gave no times
| Place | Page tried | What happened |
|---|---|---|
| Duanesburg-Florida Baptist Church | web searches | No page of the congregation's own; only directories and a 2008 newspaper list |
| Old Stone Presbyterian Church, Esperance | web searches | Only directories found (searches for "Old Stone Church" bring up churches in other states) |
| Chapman Museum, Glens Falls | chapmanmuseum.org (403); archived copy of November 17, 2026 (web fetch not approved) | Not read |
| Northport Historical Society | northporthistorical.org/exhibits (403); archived copy of July 2024 (web fetch not approved) | Not read |
| Wells Memorial Library, Upper Jay | wellsmemoriallibrary.org (403; web fetch not approved) | Not read |
| Yaddo gardens | yaddo.org (403; web fetch not approved) | Not read |
| Gloversville Free Library | gloversvillelibrary.org | Only "today's hours" and a Monday curbside note; no week of hours |
| Spencertown Academy | spencertownacademy.org | Events only; no gallery hours |
| Palace Theatre, Albany | palacealbany.org/box-office and /visit/faq (HTTP 406) | Not read |
| Morristown Land Office (library) | nyslittree.org page for Morristown Public Library | It gives hours, but the site is a statewide library directory, not the library's own page: not used |

Also tried and not recorded (left waiting for another session): Horseheads Historical Society (site would not connect), Warwick Historical Society (Baird's Tavern; site would not connect), Rensselaerville Historical Society (site would not connect), Sherman Free Library (page drawn by script; cefls.org 403), Kelly Round Barn (only a Hanford Mills "explore more" listing gave the Pakatakan market's hours: a listing, not the market's own page), Grooms Tavern (the Town of Clifton Park historian's hours are for 475 Moe Road, not the tavern), Oneonta, Angelica and Alfred offices (only the towns' pages were found, not the city or village that occupies the building).

Closed or sold: none found in this batch.

## Leads
None.

## Tips
- No places of worship are waiting any more (November 21, 2026); the hours job is now museums and the like.
- `hours.py page` sometimes prints a day row that `page.py --all` does not show (City Winery's hours sit in a block the text reader drops); trust only what was printed and leave out what was not.
- Many small-museum and library sites in the North Country answer 403 to the page reader, and the web fetch tool's request for approval goes unanswered in unattended runs. A session someone is watching could finish Chapman, Northport, Yaddo and Wells Memorial quickly.
- Post offices: USPS location pages give the tools nothing usable (an earlier note says the same); skip them.
