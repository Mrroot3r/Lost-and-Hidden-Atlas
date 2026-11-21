# ks_nrqf: Kansas: a first statewide scatter
state: Kansas
region: ks
date: 2026-11-21
places: 17
file: data_ks_nrqf.py

## What this batch is
Seventeen places spread across Kansas, which had 19, all round Kansas City, Lawrence and Topeka: Fort Larned, Fort Scott, Fort Hays and the Fort Harker buildings in Kanopolis; the Hollenberg Pony Express Station; Nicodemus; the Chase County Courthouse, Spring Hill Ranch (Tallgrass Prairie National Preserve) and the Kaw Mission in the Flint Hills; the Beecher Bible and Rifle Church; the Basilica of St. Fidelis in Victoria; Big Brutus; the Coronado Heights WPA castle; the Garden of Eden in Lucas; the Mine Creek battlefield; Cottonwood Ranch; and the Goodnow House. Facts come from Wikipedia (wiki_raw.py) and the managing bodies' own pages read with page.py: nps.gov hours and news pages, kansashistory.gov site pages and Kansapedia, the parish page of St. Fidelis, the City of Cottonwood Falls, bigbrutus.org, gardenofedenlucas.org and the Lindsborg visitors' page. Not checked: Fort Harker museum hours (no page of the Ellsworth County Historical Society found), service times of the Beecher Bible and Rifle Church (only a visitors' bureau page says Sunday services and tours on request), Coronado Heights hours, which Fort Scott buildings are original and which rebuilt, which Nicodemus buildings open beyond the Township Hall, the Tallgrass Prairie summer hours (only a 2024 winter notice gave times), parking at Cottonwood Ranch and the Goodnow House, and the Garden of Eden's owner. Nothing was seen on the ground. Hollenberg's state page said "closed until further notice" in November 2026. Pins: Big Brutus, Coronado Heights and Mine Creek were moved with pix.py (the Mine Creek pin is now the visitor center, area); Nicodemus is the middle of the town (area); the rest sat on or inside their sites on the 2024 Kansas aerial. Fort Scott brick='some' from a Commons photograph showing a red brick building on the parade ground; Fort Hays and Nicodemus are brick='?'.

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Elk Falls and its iron bridge | Elk Falls, KS (37.37333, -96.19333) | A small old town on the Elk River, founded 1870 (Wikipedia) | A source for the bridge and what stands; Wikipedia has no bridge article under the obvious title |
| Fort Hays brick | Hays, KS | Four original buildings stand | What they are built of (brick.py look) |

## Tips
- kansashistory.gov/<site> short addresses (fort_hays, hollenberg, kaw_mission, mine_creek) give the hours, address and season in `page.py --all`; cottonwood_ranch and goodnow_house do not, but their "plan your visit" pages (found by web search) do.
- Several Kansas state historic sites close for the winter (early October to April); the KSNT/Yahoo story "Seven Kansas historic sites to close in October" lists which stay open year-round.
- nps.gov hours.htm for Fort Scott and Nicodemus is drawn by script and comes back empty; the visitorcenters.htm page (Fort Scott) and the nps.gov/places/township-hall.htm page (Nicodemus) give the times.
- photo_find.py look on four places took over two minutes: run it with a long timeout or in the background.
