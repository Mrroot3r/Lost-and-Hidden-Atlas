# midh_vrtk: Southern Dutchess: Beacon, Fishkill, Wappingers Falls, Chelsea and New Hamburg
state: New York
region: midh
date: 2026-11-20
places: 20
file: data_midh_vrtk.py

## What this batch is
Twenty places in southern Dutchess County, the first pass there (region `midh`, drawn at random by `choose.py --state ny`, which offered Wappingers Falls and New Hamburg; the Atlas had four places within 15 km of Wappingers Falls: the Mount Beacon incline and three west of the river). Nearly all standing. Beacon: the Madam Brett Homestead (c. 1709, DAR museum), Mount Gulian (rebuilt 1966–1975 on the burned 1730s house), the Howland Library by Richard Morris Hunt, the fieldstone 1930s post office, St. Luke's Episcopal and the red-brick Reformed Dutch Church of Fishkill Landing (both Frederick Clarke Withers), the Mount Beacon fire tower (CCC 1931, restored 2013), and the stone abutments of the demolished Tioronda bowstring bridge. Fishkill: the Van Wyck Homestead (1732, supply-depot headquarters), the First Reformed Dutch Church (1731 or 1725: the sources disagree) and Trinity Church (c. 1769), Stony Kill Farm (DEC) and Dutchess Manor. Wappinger: the Mesier Homestead, the 1940 Roosevelt post office (old village hall), the Bain Commercial Building, Grinnell Library, the Chelsea Grammar School, Carnwath Farms, and Zion Memorial Chapel (St. Nicholas-on-the-Hudson) at New Hamburg. Sources: Wikipedia read with `wiki_raw.py`; the managing bodies' pages read with `page.py` (Town of Fishkill historian, Town of Wappinger historic sites, Wappingers and Fishkill historical societies, mountgulian.org, DAR, DEC, Scenic Hudson, Howland Cultural Center, Grinnell Library, St. Nicholas); HMdb for the two Fishkill churches. Not checked: anything on the ground; service times for St. Luke's, Trinity Fishkill and the Fishkill Dutch church (no page of their own read: the Dutch church's 10 a.m. Sunday time is from the town's page and is in the access note only); post office lobby hours; whether a newer span now sits on the Tioronda abutments; who now owns the Reformed Church of Beacon. Pins: Stony Kill Farm marks the farm in general (falls in a field), Carnwath Farms is the address point (manor not picked out), Dutchess Manor was moved onto the building with the big lot, taken to be the manor but not confirmed. Brick for Bain and Chelsea from their Wikipedia photographs.

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Dia Beacon (Nabisco carton plant) | Beacon (Register 41.5, -73.9828) | Register list: largely intact Nabisco factory turned art museum | diaart.org answered 403 to page.py; Wikipedia's article gave no text to wiki_raw.py; hours and building facts from a readable source |
| Hopewell Junction depot | Hopewell Junction (Register 41.5850, -73.8067) | Register-listed depot, run as a museum | hopewelldepot.org now serves spam; the museum's own page and hours |
| Tioronda Hat Works ruins | Beacon, beside Madam Brett Park (about 41.489, -73.975) | Scenic Hudson's park page says the hat works' ruins sit next to the park | Owner, date and whether they can be seen from the park |
| Zion Episcopal Church, Wappingers Falls | 12 Satterlee Place, Wappingers Falls | Wikipedia (village article): dedicated May 6, 1836 | Whether the 1836 building stands; a page of its own |
| Fishkill Supply Depot burial ground | Town of Fishkill, south of the Van Wyck Homestead | Wikipedia: hundreds of graves found by radar in 2007 | What can be seen and whether there is public access |

## Tips
- The Town of Fishkill historian's page (`fishkill-ny.gov/town-history.html`) and the Town of Wappinger's (`townofwappingerny.gov/historic-sites-museums/`) list every public historic site with an address and often hours, and read in full with `page.py --all`.
- `hopewelldepot.org` has been taken over by a spam site; do not take anything from it.
- Web search here returned links only, no quoted text; every hours row came from a page read with `page.py`.
