# bos_vozt: Concord and the Battle Road, Massachusetts: North Bridge, authors' houses, Battle Road ruins
state: Massachusetts
region: bos
date: 2026-11-20
places: 20
file: data_bos_vozt.py

## What this batch is
Twenty places in Concord, with the Battle Road in Lincoln and Lexington and one house in Bedford, where the Atlas had nothing within 11 km of Concord (region bos drawn at random by choose.py). Concord: the Old North Bridge with the 1836 Battle Monument and French's Minute Man, the Old Manse, the Robbins House, the Captain David Brown house site (exposed foundation and granite-marked cellar), the Colonel James Barrett Farm, Wright's Tavern, Concord's Colonial Inn, the Thoreau–Alcott House, the Emerson House, Sleepy Hollow Cemetery (Author's Ridge), Orchard House, The Wayside (house shut for 2026), Thoreau's cabin site at Walden, the Pest House, Damon Mill and West Concord's 1894 union station. Battle Road: Hartwell Tavern, the Samuel Hartwell house site (a standing chimney after a 1968 fire) and the Ebenezer Fiske house foundation. Bedford: the Job Lane House. Sources: Wikipedia through wiki_raw.py, HMdb marker pages (the NPS's own trail signs), nps.gov places and plan-your-visit pages, and the managing bodies' pages through page.py (thetrustees.org, louisamayalcott.org, robbinshouse.org, concordscolonialinn.com, joblanefarmmuseum.org, concordmuseum.org). Not checked: Walden Pond hours and fees (mass.gov 403, and the web fetch request timed out unattended); Emerson House hours (its site gave none); whether Wright's Tavern still opens for events and whether the Club Car Cafe still runs in the station; the Robbins House's opening days; the Trustees' page mentions NPS construction at the North Bridge, not confirmed on an NPS page. Brick from Wikimedia photographs for Damon Mill (yes), the Emerson House and Barrett Farm (some: red brick chimneys), the Colonial Inn and Thoreau–Alcott House (no); '?' wherever no picture was opened. No pin is only a trailhead; the Fiske and Brown sites and the station are prec site. Nothing visited on the ground.

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Josiah Nelson house site | Lincoln, MA (42.450109, -71.273106, HMdb 18290) | NPS sign: site of the home of Josiah Nelson, by family tradition wounded by the officers who captured Revere | Whether any foundation can be seen |
| Codman Estate and Gropius House | Lincoln, MA | Historic New England properties | historicnewengland.org answers 403 to page.py; hours and fabric not read |
| Major John Buttrick House | Concord, MA (42.471954, -71.35328, HMdb 18173) | NPS sign: built 1715, home of the officer who ordered the fire at the bridge | Who owns it now and whether it opens |
| Meriam House, Meriam's Corner | Concord, MA (42.4594, -71.3239) | NPS opened it for viewing on set days in 2024 (GAOA page) | Its own NPS page and age |

## Tips
- nps.gov/places addresses for Minute Man carry the date in the name (hartwell-tavern-1733, samuel-hartwell-house-circa-1695); guessed names without it are 404. A web search for "nps.gov/places <name>" finds them.
- The Minute Man "places to go" page (nps.gov/mima/planyourvisit/placestogo.htm) gives each site's hours for the season and a GPS point for each parking lot; the hours page itself has no times in its text.
- The NPS GPS point for the Hartwell Tavern lot fell on Route 2A beside the lot; check NPS lot points on the aerial.
- louisamayalcott.org reads with page.py only without "www"; the www address resets the connection.
- The ArcGIS geocoder gave PointAddress hits on every Concord house tried; the OpenStreetMap Robbins House point sits under tree shadow, with a bigger private house 90 m east that looks like the obvious target on the aerial.
