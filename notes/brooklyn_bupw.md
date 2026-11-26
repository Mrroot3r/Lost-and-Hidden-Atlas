# brooklyn_bupw: Brooklyn, New York
state: New York
region: nyc
date: 2026-11-21
places: 18
file: data_brooklyn_bupw.py
tidied: 2026-11-26

## What this batch is
The first 18 places in Brooklyn itself (Kings County), all standing, from a "videos" session (job 9). The names came from one video, "Old World Brooklyn" by Old World Exploration (https://www.youtube.com/watch?v=weEKwxAlFs8), whose transcript was read on the owner's computer; the record of all 95 names and what came of each is `source/videos/20260417_weEKwxAlFs8.md`. The video was a tip only: no fact comes from it. Added: the 23rd, 13th and 14th Regiment armories, the Alhambra Apartments, Borough Hall, Boys High School and Girls' High School, the Soldiers' and Sailors' Arch, the Old Brooklyn Fire Headquarters, the Hotel Bossert, the Montauk Club, Queen of All Saints Church, the Eagle Warehouse, Erasmus Hall, St. Ann & the Holy Trinity, the Crescent Athletic Club House, the General Post Office and Green-Wood Cemetery's main gate. Sources: Wikipedia read as raw text (`wiki_raw.py`) for every place, and three managing bodies' pages read with `page.py` and `hours.py page` (Green-Wood's hours, the Prospect Park Alliance on the arch, Queen of All Saints' Mass times). Pins are ArcGIS PointAddress results (the arch: Wikipedia's point), each looked at on the leaf-off aerial; two were moved with `pix.py` (Montauk Club, post office). Red brick was settled from the lead photograph of each article where the text did not say. NOT checked: anything on the ground; no Landmarks Commission report or Register form was opened, so each place rests on Wikipedia alone apart from hours; the present use of the Boys High and Girls' High buildings; interiors; whether the 1787 Erasmus academy can be seen from the street (the pin is on the Flatbush Avenue front, not on it); which half of the post office block is the 1892 building; St. Ann & the Holy Trinity's hours (its site answered 403); parking, which is street parking everywhere and was not looked for except Green-Wood, where the mapped parking inside the main gate is given. The pin check was run without `--lidar` (built-up city blocks). Three of the armories and shelters are lived in: the notes say to look from the street.

## Leads
Moved to `LEADS.md` on 2026-11-26 by the tidy job (3 rows). New leads for this ground go in the note of the batch that finds them.

| Place | Where | What is known | What is missing |
|---|---|---|---|

## Tips
Folded into `GUIDE.md` and the tools on 2026-11-26 by the tidy job (4 tips).
