# njn_ceha: Morris County, New Jersey: ironworks, mines, the Morris Canal and the winter camp at Morristown
state: New Jersey
region: njn
date: 2026-11-18
places: 20
file: data_njn_ceha.py

## What this batch is
Twenty places in Morris County, the first close pass in North Jersey (region drawn with `choose.py`): the Boonton Ironworks ruins and arch bridge in Grace Lord Park, Split Rock Furnace, Historic Speedwell, Cooper Gristmill, the Ford Mansion, Fort Nonsense, the Wick House and the Pennsylvania Line huts at Jockey Hollow, Craftsman Farms, the Old Stone Union Church ruin and the LaTourette mill at Long Valley, the Mount Hope mines, the Ford–Faesch house and Miners' Church, the Morris Canal culvert at Rockaway, the lock tender's house at Hopatcong State Park, the Whippany water tank and railway museum, Fosterfields, and the Hibernia church. Sources: Wikipedia with `wiki_raw.py` (the Register list rows too), HMdb marker texts with `page.py`, NPS pages with `page.py`, the Split Rock Furnace Register form with `page.py`, and, through the web fetch tool before it stopped answering, the 2022 Boonton Ironworks nomination, a county news release, Rockaway Township's Splitrock page and the Park Commission pages for Speedwell and Cooper Gristmill. Not checked: hours for Fosterfields, Mount Hope, Hopatcong State Park and its museum, Craftsman Farms tours, Whippany's summer season, the Ford–Faesch house (owner too), the Long Valley sites and the Hibernia library; parking for Speedwell, the Ford Mansion, Craftsman Farms and Whippany; whether a marked trail passes Split Rock Furnace; how much of the Union Church walls stand. Pins that mark only a parking lot or a marker, not the thing: Boonton Ironworks ruins (Upper Plane Street lot), Mount Hope mines (Teabo Road lot), the Rockaway culvert (marker), the Whippany tank (museum coordinate). Brick is mostly `?`: no picture was opened.

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Waterloo Village (Morris Canal Plane 4 West, lock, mill) | Byram Township, Sussex County, NJ (40.9144, -74.7546, HMdb markers 99054, 231652) | HMdb markers describe the canal features; waterloovillage.org says it is in Allamuchy Mountain State Park | The state park page would not open; waterloovillage.org did not look like the managing body's own site |
| Job Allen Iron Works site | Denville, NJ (40.89428, -74.47388, HMdb 229492) | Marker: forge and farm of Job Allen on the Rockaway River, 1730 | Whether anything shows; marker only |
| Andover Furnace and ironmaster's mansion | Andover, Sussex County, NJ (40.98736, -74.74231, HMdb 63375, 27297, 63376) | Three HMdb markers | Not read; outside Morris County |
| Illumination Gas Plant, Greystone asylum | Parsippany, NJ (40.836111, -74.500833, Register 00000653) | Register list row only | Whether it stands, owner, access |
| Boonton Ironworks furnace stacks, exact spot | Boonton, NJ (district polygon in the 2022 nomination, section 10) | The nomination lists both stacks surviving up to the bosh | A position for the stacks, to move the ruins pin off the parking lot |

## Tips
- The web fetch tool answered for the first four requests (morrisparks.net, nj.gov HPO PDF, county news, Rockaway Township), then every request timed out waiting for approval: fetch the managing bodies' pages you need most first, in one batch.
- morrisparks.net (Morris County Park Commission) answers 403 to `page.py`; morriscountynj.gov news releases too.
- nps.gov reads well with `page.py`; `https://www.nps.gov/morr/planyourvisit/hours.htm` gives every Morristown site's hours. `nps.gov/places/wick-house.htm` and `ford-mansion.htm` are 404.
- HMdb nearby lists: the `grep -o "m.asp?m=[0-9]*'>[^<]*</a> (<a href='[^']*destination=[0-9.,-]*"` on the cached page gives marker number, title and position in one line each.
- Web search results here gave titles and links only, no quoted text, so hours could not be taken from them.
