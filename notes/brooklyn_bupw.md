# brooklyn_bupw: Brooklyn, New York
state: New York
region: nyc
date: 2026-11-21
places: 18
file: data_brooklyn_bupw.py

## What this batch is
The first 18 places in Brooklyn itself (Kings County), all standing, from a "videos" session (job 9). The names came from one video, "Old World Brooklyn" by Old World Exploration (https://www.youtube.com/watch?v=weEKwxAlFs8), whose transcript was read on the owner's computer; the record of all 95 names and what came of each is `source/videos/20260417_weEKwxAlFs8.md`. The video was a tip only: no fact comes from it. Added: the 23rd, 13th and 14th Regiment armories, the Alhambra Apartments, Borough Hall, Boys High School and Girls' High School, the Soldiers' and Sailors' Arch, the Old Brooklyn Fire Headquarters, the Hotel Bossert, the Montauk Club, Queen of All Saints Church, the Eagle Warehouse, Erasmus Hall, St. Ann & the Holy Trinity, the Crescent Athletic Club House, the General Post Office and Green-Wood Cemetery's main gate. Sources: Wikipedia read as raw text (`wiki_raw.py`) for every place, and three managing bodies' pages read with `page.py` and `hours.py page` (Green-Wood's hours, the Prospect Park Alliance on the arch, Queen of All Saints' Mass times). Pins are ArcGIS PointAddress results (the arch: Wikipedia's point), each looked at on the leaf-off aerial; two were moved with `pix.py` (Montauk Club, post office). Red brick was settled from the lead photograph of each article where the text did not say. NOT checked: anything on the ground; no Landmarks Commission report or Register form was opened, so each place rests on Wikipedia alone apart from hours; the present use of the Boys High and Girls' High buildings; interiors; whether the 1787 Erasmus academy can be seen from the street (the pin is on the Flatbush Avenue front, not on it); which half of the post office block is the 1892 building; St. Ann & the Holy Trinity's hours (its site answered 403); parking, which is street parking everywhere and was not looked for except Green-Wood, where the mapped parking inside the main gate is given. The pin check was run without `--lidar` (built-up city blocks). Three of the armories and shelters are lived in: the notes say to look from the street.

## Leads
Fifty names from the video were not reached and are listed as "not checked" in the record; the likeliest to stand are below.

| Place | Where | What is known | What is missing |
|---|---|---|---|
| Brooklyn Masonic Temple | Brooklyn, NY (Clermont and Lafayette Avenues, beside Queen of All Saints) | Named in the video as standing; no Wikipedia article under that title | A source for dates and present use |
| Kings County Savings Bank | Brooklyn, NY, 135 Broadway, Williamsburg (40.71028, -73.96417) | Wikipedia: Second Empire bank of 1860–67, run by the Williamsburg Art & Historical Center since 1996; article read, not written up | Hours from the centre's own page; a look at the pin |
| Brooklyn Museum, Brooklyn Academy of Music, Pratt Institute main building, Temple Bar Building, Troop C Armory, Union League Club (Grant Square), Williamsburgh Trust Company building, 47th Regiment Armory, Brooklyn Navy Yard Sands Street gate | Brooklyn, NY | Named in the video; none opened beyond the Academy of Music and Navy Yard article openings | Sources, pins, access |

## Tips
- `publish.sh` stopped once because a Kansas batch merged meanwhile; `resync.sh` then `all.sh` and a second `publish.sh` to the branch name with a letter added worked as the guide says.
- Wikipedia article titles that failed here: "Boys' High School (Brooklyn)" (it is "Boys High School (Brooklyn)"), "Brooklyn General Post Office" (it is "Federal Building and Post Office (Brooklyn)"), "Eagle Warehouse and Storage Company" (it has an ampersand).
- A web search for a Brooklyn church's hours returned titles only; `hours.py page https://www.qasrcc.org/mass-times` read Queen of All Saints' times cleanly. stannholytrinity.org answers 403 to both tools.
- For ten places at once, `brick.py look` with 12 seconds between calls was never refused by Wikimedia.
