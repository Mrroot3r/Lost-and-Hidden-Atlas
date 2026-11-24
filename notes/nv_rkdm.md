# nv_rkdm: Nevada: depots, stage stations and small-town landmarks
state: Nevada
region: nv
date: 2026-11-23
places: 14
file: data_nv_rkdm.py

## What this batch is
Fourteen places across Nevada (Reno, Virginia City, Austin, Ely, Winnemucca, Elko, Overton, Goodsprings, Gerlach and three Pony Express and army sites), taken from the National Register county lists and Wikipedia articles (tools/wiki_raw.py). The managing bodies' own pages mostly would not open (page.py got 403 or 404), so hours, owners and what stands today come from web search results quoting museum, National Park Service and news pages. Not checked: nearly every standing building's interior, current use of the Martin Hotel, Chollar Mansion and Goodsprings Schoolhouse, hours for the Reno depot, Elko museum, Lake Mansion tours, and the red brick of most (only the Reno depot was settled, from a Commons photograph). Pins: nine were looked at on the aerial; Fort Ruby and Schellbourne are area pins (nothing identifiable on the aerial); the Elko museum pin marks the museum, not the cabin; the Winnemucca courthouse and Lost City pins were moved from the Register or Wikipedia coordinate to the OpenStreetMap position.

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Bristol Wells | near Pioche, NV (38.1027, -114.6914) | Ghost town with stone charcoal ovens, smelter 1880s; National Register | What stands today and who owns the ground |
| Gem Theater and Brown's Hall, Pioche | Pioche, NV (37.9301, -114.4511) | National Register listings | Source for what is open |
| Manhattan School | Manhattan, NV (38.5397, -117.0739) | National Register 2006 | Anything but the list row |
| Tonopah historic district houses | Tonopah, NV | About 40 Register rows in one district | Pick the best standing ones |

## Tips
- Searching the web for the museum's own name gave hours when page.py could not open the site; say in the entry when the figure comes from a snippet.
- National Register list coordinates can fall hundreds of metres off (Winnemucca courthouse 600 m, Lost City Museum on the highway); run nom.py before trusting them.
