# ne_fhrx: Nebraska: a first scatter across the state
state: Nebraska
region: ne
date: 2026-11-21
places: 16
file: data_ne_fhrx.py

## What this batch is
Sixteen standing places and trail sites spread across Nebraska, which had 20 places, nearly all in the southeast river towns: Omaha (Joslyn Castle, Union Station/Durham Museum), Lincoln (Kennard House), Beatrice (Gage County Courthouse, the Freeman School at Homestead NHP), Fairbury (Rock Creek Station), Red Cloud (Willa Cather Childhood Home), Kearney (Fort Kearny), McCook (Norris House), Champion (Champion Mill), North Platte (Buffalo Bill Ranch), Sidney (Fort Sidney), Comstock (Dowse Sod House), Burwell (Fort Hartsuff), Neligh (Neligh Mill) and Crawford (Fort Robinson). Facts come from the Wikipedia articles (`wiki_raw.py`), National Park Service "places" pages (Freeman School, Rock Creek Station, Fort Kearny), and the managing bodies' own pages where they opened. History Nebraska's pages (Neligh Mill, Norris House, Kennard House, Fort Robinson History Center) answer 403 to `page.py` but were read with the web fetch tool. outdoornebraska.gov (Game and Parks) refused both tools except one news item, so Fort Hartsuff, Buffalo Bill Ranch, Rock Creek Station, Fort Kearny and Champion Mill have `hours='?'`; Buffalo Bill's season is given in the access note from Visit North Platte (the visitor bureau, not the park). Fort Sidney's season is from the Western Nebraska Tourism Coalition; the Dowse Sod House's operator and hours were not found. The Willa Cather row is the Cather Center's hours (tours start there). No interior was seen; nothing was checked on the ground. Pins: Freeman School and Buffalo Bill's barn were moved onto the building with `pix.py`; Neligh Mill (pin on the marker, mill not picked out) is `area`; Rock Creek Station is `area` on the Wikipedia point with the park entrance as `th`; the Cather house pin is an interpolated address (`site`). Parking not checked at Hartsuff, Dowse, Champion and Buffalo Bill.

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Fort Atkinson State Historical Park | Fort Calhoun, NE (41.455, -96.01417) | 1819–1827 Army post; the state built a replica fort on the site in the 1980s–90s (Wikipedia) | Whether any original trace is shown; hours (outdoornebraska.gov refused) |
| Johnson Cabin Museum | Blue Springs, NE (40.140662, -96.662267) | On the Register (Gage County list, 15000488) | Any source on what it is and who opens it |
| Ash Hollow State Historical Park | Lewellen, NE (41.29806, -102.12) | Cave and Windlass Hill on the Oregon Trail (Wikipedia) | Which old buildings (if any) stand; hours |

## Tips
- outdoornebraska.gov (every Game and Parks park page) answers 403 to `page.py`; the web fetch tool read one `outdoornebraska.gov/?p=` news item but no park page was tried with it. Search results give titles only, no quoted text.
- history.nebraska.gov answers 403 to `page.py` but the web fetch tool read its site pages fine in an unattended session (six pages, no approval asked).
- NPS `nps.gov/places/<name>.htm` pages exist for Nebraska state parks on the trails (Rock Creek Station, Fort Kearny) and give the address and an entrance coordinate.
- The Wikipedia coordinate for Fort Robinson is about 3 km west of the post; `nom.py "Fort Robinson Museum, Nebraska"` gives the History Center.
- The Willa Cather Foundation's site gives two addresses for its Center (413 and 425 North Webster).
