# tulsa_cacf: Tulsa: oil-boom downtown and Greenwood
state: Oklahoma
region: ok
date: 2026-11-26
places: 11
file: data_tulsa_cacf.py

## What this batch is
Eleven standing buildings in downtown Tulsa and the Greenwood district, taken from the names in one walk-through video (Old World Exploration, "Old World Tulsa Oklahoma"; the record of every name is `source/videos/20230715_cEdk7OE6wyA.md`). Downtown: the Exchange National Bank tower (320 South Boston), the Mayo Hotel, the Philtower, the Beacon Building, the 1917 federal building and post office, Holy Family Cathedral, First Christian Church on South Boulder, First United Methodist Church, and the old Central High School (now the Public Service Company of Oklahoma offices). Greenwood: Vernon A.M.E. Church and the rebuilt 100 block of North Greenwood Avenue. Sources: Wikipedia read as raw text, the 2003 Downtown Tulsa self-guided walking tour (a PDF that `page.py` reads), the Oklahoma Historical Society's October 2026 press release, Tulsa LocalWiki, Clio, Public Radio Tulsa, and the pages of the cathedral, Vernon A.M.E. and Greenwood Rising for hours. Pins are address lookups or OpenStreetMap buildings, all looked at on the aerial; three were moved onto their buildings. Not checked: whether the public may walk into the Philtower, 320 South Boston or Beacon lobbies; parking downtown; First United Methodist's service times (no page of its own found); the year of First Christian Church (a travel guide says dedicated February 1920; a historical marker, seen only in a search result, says 1919). Red brick from Commons pictures for four places; the rest are '?'.

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| University of Tulsa early buildings | Tulsa, OK (campus, about 36.152, -95.945) | A 2014 student paper calls Harwell Hall (1920) the oldest building standing; McFarlin, Tyrrell and Phillips halls 1930 | A university or Register source for the buildings and what the public may see |
| Morningside Hospital | Tulsa, OK, 512 North Boulder Avenue (first building) | Began 1918 in a brick building there; moved to 16th and Utica (now Hillcrest Medical Center) in 1925 or 1928 | Whether either early building stands |

## Tips
- The 2003 Downtown Tulsa walking tour PDF (`d1pk12b7bb81je.cloudfront.net/okdataengine/appmedia/documents/0/830/walkbrochurebw.pdf`) reads cleanly with `page.py --all` and dates fifty downtown buildings in one go; its years differ from Wikipedia's by a year or two for several, so give both.
- `videos.py check` reads "added <id>:" with the colon as part of the id; put a remark after the id in brackets.
- HMdb.org answered 403 to `page.py`, and the web fetch tool cannot open web.archive.org; marker texts could be seen only in search results.
- Holy Family Cathedral's own page `tulsacathedral.com/mass-times` gives the Mass times cleanly with `hours.py page`.
