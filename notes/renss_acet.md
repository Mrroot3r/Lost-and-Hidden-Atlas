# renss_acet: Rensselaer County: Wynantskill, Bath, Sand Lake, Nassau and Grafton
state: New York
region: hud, renss
date: 2026-11-20
places: 10
file: data_renss_acet.py

## What this batch is
Ten places in southern and eastern Rensselaer County (region `renss`, drawn at random by `choose.py --state ny`), on ground the earlier batches `renss_osux` and `renss_irek` left, plus Riders Mills just over the line in Columbia County (region `hud`), the old town centre `choose.py` offered. All standing: the First Reformed Church of Wynantskill (state marker: the county's oldest church building, 1793), the Clark–Dearstyne–Miller Inn of about 1791 at Bath (Rensselaer city), Jim Cotton's 1915 ice-cream parlor at Sand Lake (finishes the Cotton House lead from `renss_irek`), the Sand Lake Union Cemetery with "Big Thunder" Smith Boughton's grave, the Grafton Inn (1795 house moved by oxen in 1830), the Riders Mills hamlet and 1795 schoolhouse, the Newton–Taber–Marvin Farm in Nassau, East Nassau Central School (1930), Van Rensselaer High School (Art Deco, later Doane Stuart, which announced its closing in June 2026) and Brainard Rural Cemetery. Sources: HMdb marker pages and nearby lists through `page.py`, Wikipedia through `wiki_raw.py` (and `--rows` for the county Register list), the North Greenbush town historian's column PDFs, the Sand Lake Historical Society's marker and Cotton House pages, the Newton–Taber–Marvin Register form (text layer), and historypointer.com's copies of the Register summaries for the inn and the East Nassau school (NPGallery has placeholders only). Every pin was looked at on the leaf-off aerial and LiDAR; Van Rensselaer High School was moved onto the building. Not checked: anything on the ground; every interior; the inn's state since it was listed as vacant in 2008; whether the Grafton Inn still takes guests; present use of the East Nassau school and of Van Rensselaer High after Doane Stuart closes; service times at Wynantskill (no church page found); owners and parking at both cemeteries (Brainard is marked view only for that reason); which building at Riders Mills is the schoolhouse and which mill foundations can be seen. Red brick is `'?'` for nine places (no picture opened); the farm is `'no'` from its form (clapboard on stone).

## Leads
Places you read about and could not finish. One row each.

| Place | Where | What is known | What is missing |
|---|---|---|---|
| Sampson Station, Grafton Lakes State Park | Grafton, NY (OpenStreetMap ruin lead 42.79453, -73.44664) | Only the OpenStreetMap name; the park's master-plan PDFs on parks.ny.gov answer 404 | What it was and what is left |
| Arlington Hotel (Elkhorn) | West Sand Lake, NY (3532 NY 43, 42.64573, -73.59460) | Pomeroy marker 2024 (HMdb 284354): stop 22 on the Troy & New England trolley | Whether the building stands; the marker is in the past tense |
| Craver Farmstead | Craver Road, East Greenbush, NY (Wikipedia 42.62306, -73.64361) | Wikipedia: Federal farmhouse of before 1790 and barn, NRHP 1996; the article reads like a family history | An independent source and whether the house shows from the road |

## Tips
- historypointer.com/nris/resource/<reference number> carries Wikipedia's Register summary, often quoting the form, where NPGallery has only a placeholder; some of its pages are drawn by script and come back empty.
- `wiki_raw.py "Clark-Dearstyne-Miller Inn"` (hyphens) returns the redirect page and `"Clark–Dearstyne–Miller Inn"` (en dashes) returns nothing; read such titles from another copy.
- parks.ny.gov's Grafton Lakes master-plan PDFs answer 404 on both www and plain addresses.
- The renss_irek tip holds: give `start.py` a latitude and longitude for Rensselaer County towns.
