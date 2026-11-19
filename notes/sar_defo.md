# sar_defo: Saratoga County: Moreau, Corinth and downtown Saratoga Springs
state: New York
region: sar
date: 2026-11-19
places: 11
file: data_sar_defo.py

## What this batch is
Eleven places in region `sar`, drawn at random by `choose.py --claim`: northern Saratoga County, where the Atlas had nothing in South Glens Falls, Gansevoort or the village of Corinth, and the standing buildings of downtown Saratoga Springs that earlier batches (which took the spa, the park and the lost hotels) had left. North: Parks-Bentley Place (museum, open), the Gansevoort Mansion (the lead row in `notes/sar_wqmx.md`, now deleted), International Paper's 1905 office and time office at Corinth, the Spier Falls dam, and the Lynwood Baptist church at Hadley. Saratoga Springs: the Batcheller Mansion (inn), Universal Preservation Hall, the post office and city hall corner, High Rock Park, Franklin Square and the race course. Sources: Wikipedia read raw (`wiki_raw.py`), HMdb marker pages and other pages through `page.py`, the Register form for the International Paper building (NPGallery text, read in full), the Town of Moreau, Village of South Glens Falls, Greenway and Saratoga TODAY pages for Parks-Bentley, NYRA's ticket and guest-services pages, UPH's visit page, the Batcheller inn's history page, WNYT on city hall, nnywaterfalls.com for Spier Falls. Every pin was looked at on the leaf-off aerial; two were moved (the race course from the infield pond onto the grandstand, the Lynwood church 27 m onto the red building by the cemetery). Not checked: anything on the ground; the Gansevoort Mansion's present use (Wikipedia's "inn and cafe" has no current page; `conf='mixed'`); whether the Lynwood church holds services (one marker is the only source; `conf='mixed'`); Parks-Bentley's hours, where three sources disagree (all given); the post office's counter hours and UPH's and the Batcheller inn's (`hours='?'`); whether the Spier Falls powerhouse was repaired after the September 2024 fire; the International Paper building's present use (vacant in the 2017 form). Red brick from pictures opened: Parks-Bentley yes, UPH yes, Gansevoort Mansion some (chimneys; clapboard house); the rest `?`.

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Col. Sidney Berry House | West River Road, Northumberland, NY (Wikipedia 43.21278, -73.58556; HMdb 149755 marker at 1439 West River Road, 43.21492, -73.58424) | Register: house of about 1800; 1936 state marker: home of Col. Sidney Berry, Revolutionary officer, first county surrogate and first town supervisor | Which house it is (the two points are 250 m apart) and whether anything sets it apart from an ordinary private house |
| Old Champlain Canal Lock 10 and the Northumberland river crossing | Northumberland, NY (HMdb 185836, 43.12293, -73.58746) | HMdb (Lakes to Locks panel): boats were towed across the Hudson above the Saratoga Falls dam from Lock 10 to Lock 11; Jesse Billings's boatyard, dry dock, ice docks and his brick bank (now a private house) | Whether any lock stone survives (the American Canal Society's Champlain sheet would give the coordinate) |
| Hudson River Mill site pin | Corinth (id `hudson-river-mill`, data_c.py) | The pin is at 43.2267, -73.8897, about 5 km southwest of the village; the Register form for the International Paper office puts the mill at Palmer Falls beside 15 Pine Street (43.247, -73.820) | A pins session to move it, or merge it into `international-paper-office-corinth` |

## Tips
- `parksbentleyplace.org` is drawn by script; the Town of Moreau's historical-society page (`townofmoreau.org/historical_society.asp`) gives the address, and Saratoga TODAY printed the 2026 season hours.
- HMdb nearby lists at a 5-mile radius round Gansevoort, South Glens Falls, Corinth, Hadley and Wilton gave the candidate list in five requests; many returned markers are over the river in Warren and Washington counties, so check each marker's county.
- The Saratoga Race Course's Wikipedia point is in the infield pond; OpenStreetMap names the grandstand building (`osmnear.py ... buildings -g grand`).
