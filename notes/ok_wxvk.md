# ok_wxvk: Oklahoma: second scatter
state: Oklahoma
region: ok
date: 2026-11-24
places: 12
file: data_ok_wxvk.py

## What this batch is
Twelve places spread across Oklahoma outside Logan County and Oklahoma City (the thinnest region when `choose.py --thinnest` ran, 52 places before): Sequoyah's Cabin (Akins), the Chickasaw Capitols (Tishomingo), the Creek Council House (Okmulgee), Honey Springs Battlefield (Checotah), the Provine/Lucille's station (Hydro), the Whited Grist Mill (Elk City), Camp Nichols (Cimarron County), the Waynoka depot and Harvey House, Dwight Mission (Marble City), Immaculate Conception Church (Pawhuska), the Aldridge Hotel (McAlester) and the Greer County Courthouse (Mangum). Found from Wikipedia's county Register lists (`wiki_raw.py --rows`), articles read as raw text, and the Oklahoma Historical Society, Cherokee Nation, Chickasaw Nation and National Park Service pages. Hours for the Waynoka museum and the Elk City museum are what web search results quoted, not a page read; the Creek Council House has none. Not checked: interiors, what survives at Dwight Mission, Camp Nichols' walls (private land, pin is the Wikipedia point), Mass times at Pawhuska, the Provine pin (the building beside it could not be confirmed as the station; prec is area), Dwight's pin (moved to the nearest historic-looking camp buildings). Pictures: 7 places show their Wikipedia picture, two got Commons pictures, Honey Springs and Waynoka have none.

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Hominy Osage Round House, Marland Filling Station, Osage Agency | Hominy and Pawhuska, OK | On the Register (Osage County list); Round House at 36.4114, -96.3853 | A page of whoever runs each, access, a source for the standing state |
| Beaver County Courthouse, Presbyterian Church, Lane Cabin | Beaver, OK (36.8158, -100.5211) | Register list: red brick courthouse of 1926 around one of 1907 | An article or page to read; hours |
| Fort Sill Old Post Quadrangle, Holy City of the Wichitas | Comanche County, OK | National Historic Landmark and a 1926 passion play site | Pages from the Army museum and the refuge, access rules |
| Hotel Franklin, Greer County Armory | Mangum, OK (34.8739, -99.5064) | Register list | A source that says what remains |

## Tips
- Oklahoma Register county lists on Wikipedia (`wiki_raw.py --rows`) are quick; many Panhandle and Woods County rows have no coordinate.
- The NPS `nps.gov/places/` page exists for Provine Service Station but not for Magnolia Station (Texola) or the Whited mill.
- Register-list points for Route 66 stations and for Dwight Mission were off the building; check them on the aerial.
- Waynoka's museum site is waynoka.org (the page for the depot reads with `page.py --all`); waynokaok.com is dead.
