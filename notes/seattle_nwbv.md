# seattle_nwbv: Seattle: Pioneer Square, downtown and the university
state: Washington
region: wa
date: 2026-11-24
places: 18
file: data_seattle_nwbv.py

## What this batch is
Eighteen places in Seattle, Washington, from the names in one video about the city's old buildings (Old World Exploration, June 2024; the record is source/videos/20240614_84-HNbjpS50.md). The video was used only as a list of names: 34 names, 18 added, 2 gone, 1 not found, 13 not checked. Added: Smith Tower, the Pioneer Square totem pole, the Seattle Underground (pinned at the tour's start, `prec='area'`), the Frye Hotel, the Colman, Hoge and Central buildings, the Burke Building arch (`conf='mixed'`: a plaque in the plaza gives 1895, the architecture database 1889–1891), the 1933 Federal Office Building, the King County Courthouse, Union Station, the Cobb Building, the Olympic Hotel, the Times Square Building, St. James Cathedral, and on the University of Washington campus Suzzallo Library, Parrington Hall and Architecture Hall (the 1909 fair's Fine Arts Building). Sources: Wikipedia as raw text, the Pacific Coast Architecture Database (pcad.lib.washington.edu) for the Burke Building and the Frye Hotel, SAH Archipedia for Parrington Hall and Architecture Hall. Hours from the pages of Smith Tower (observatory), the Underground Tour and the UW Libraries (Suzzallo, the week of Thanksgiving, so not a normal week). Not checked: St. James Cathedral's Mass and opening times (its site would not load), the Olympic Hotel's public rooms, whether Union Station's hall, the Federal Office Building's post-office lobby and the courthouse can be walked into and when, interiors of most buildings, and red brick for nine places. Every pin is OpenStreetMap's point for the building, and all sat on the building on the aerial. No parking points: the two campus lots `parking.py` gave fell on a building and in trees, so the campus entries say only "university pay lots". The University of Washington buildings are marked view: no page read said what the campus allows visitors. Nothing was checked on the ground.

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Lowman & Hanford Building | 616 First Avenue, Seattle, WA (facing Pioneer Place) | Printing and stationery firm's building after the 1889 fire, two storeys raised to four in 1892 (Pacific Coast Architecture Database, building 6148); a caption in the Wikipedia article on Pioneer Square names it | A source saying what stands now and a look at the pin |
| Cunningham Hall (A-Y-P Women's Building) | University of Washington, Seattle, WA | The 1909 fair's Women's Building survives, named for Imogen Cunningham (Wikipedia, Alaska–Yukon–Pacific Exposition) | Its own source and pin |
| Pioneer Building | First Avenue and James Street, Seattle, WA (47.60222, -122.33361) | Elmer Fisher, 1892, stone, red brick, terra cotta (Wikipedia); the Underground Tour runs from it | Not named in the video; a full write-up |

## Tips
- The Seattle Register list on Wikipedia (`wiki_raw.py --rows "National Register of Historic Places listings in Seattle"`) has 232 rows but most downtown office buildings are not under their own names there; read each building's article by title instead.
- pcad.lib.washington.edu (Pacific Coast Architecture Database) reads fully with `page.py --all` and covers demolished and unlisted Seattle buildings with dates, address and fate.
- stjames-cathedral.org came back nearly empty to `page.py` and `hours.py`, and 503 to the web fetch tool; web searches gave only directory listings.
- `parking.py` points on the University of Washington campus are lot names on roads and fell on a building and in trees: check the TRAILHEAD tile.
