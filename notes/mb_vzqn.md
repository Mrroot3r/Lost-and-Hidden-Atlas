# mb_vzqn: Manitoba: fourth scatter
state: Manitoba
region: mb
date: 2026-11-24
places: 13
file: data_mb_vzqn.py

## What this batch is
Thirteen places across Manitoba (52 before, 65 after): the Brandon air-training hangar, Frelsis church at Grund, the Clearwater water tower, the Negrych homestead near Gilbert Plains, the Dauphin engine house, Our Lady of Seven Sorrows at Camperville, the Fort Dauphin monument at Winnipegosis, the Manitoba Glass Company foundations at Beausejour, Gabel's store at Ladywood, St. Elias log church at Sirko, the Fort Garry Hotel and Union Station in Winnipeg, and the Archway Warehouse at Norway House. Found from the Province's list of Provincial Heritage Sites (gov.mb.ca/chc/hrb/prov/index.html), which names about 120 sites by town; each place rests on its Province page and its Manitoba Historical Society page (read with page.py; coordinates are the Society's, except the Fort Garry Hotel, moved to OpenStreetMap's point). Hours come from the Air Training museum's own season notice, the Negrych society's page and VIA Rail's station page. Pins were looked at on the aerial. Not checked: whether any church can be entered or when it holds services, who owns the Dauphin engine house, road access to Norway House, parking at most sites, the Fort Garry Hotel's hours, admission charges, and whether Gabel's store still opens as a museum. Brick: set from sources only where they say wood, log or stone; the Dauphin engine house, the Camperville church and the Fort Dauphin monument are "?".

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Souris Suspension Bridge | Souris (49.61661, -100.25505) | Original of 1904 swept away in 2011; a new bridge replaced it (MHS page sourisbridge) | Whether the replacement counts; it is not the old structure |
| Galloway Bros. Department Store | Gladstone | 1902 store, badly burned December 25, 2022 and demolished February 2024 (MHS, via a search result) | Nothing left to add |
| Glenboro CPR Water Tower | Glenboro (49.55474, -99.28863) | Wooden tower of 1904 burned by arson in April 2008; park and monument on the site (MHS) | Nothing left but a monument |
| CPR engine house and turntable | La Rivière (49.24060, -98.67651) | Demolished in the 1960s; engine-house foundations remain (MHS) | Whether the foundations can be seen from a public way |
| Provincial Heritage Sites not yet on the Atlas | Manitoba | From the Province's list: Brandon Court House, Brandon CPR station, Paterson/Matheson House, Carberry and Minnedosa display buildings, Virden CPR station, Wawanesa church, Dauphin Canadian Northern station, Winnipeg Beach water tower, Lac du Bonnet tower, Holy Trinity Church (Winnipeg), Walker Theatre, Legislative Building | Sources opened and pins checked for each |

## Tips
- The Province's index page (gov.mb.ca/chc/hrb/prov/index.html) lists every Provincial Heritage Site by area, and each has a short page at .../prov/pNNN.html with the owner and a designation date; read it with page.py --all. A web search for "mhs.mb.ca <site name>" finds the Historical Society slug where guessing fails (about half of guesses returned the 609-character not-found page).
- The Historical Society's pages can be ahead of the Province's: they record a store's changes, a tower burned in 2008 and a store demolished in 2024, which the Province's pages still list as standing. Read the Society's page before adding a provincial site.
- photo_find.py found Commons pictures for only one of ten small Manitoba sites (the Brandon hangar, a vintage postcard).
- hours.py page printed almost nothing for airmuseum.ca and the VIA page; page.py --all with grep found the notice and the station hours.
