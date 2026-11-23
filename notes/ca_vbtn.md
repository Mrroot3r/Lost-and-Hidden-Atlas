# ca_vbtn: California: a first scatter from Shasta to the Mojave
state: California
region: ca
date: 2026-11-23
places: 11
file: data_ca_vbtn.py

## What this batch is
Eleven places spread across California, from Shasta and Weaverville in the north to the Mojave and Death Valley, drawn by `choose.py --thinnest` (California, 39 places before, 50 after). Hours, fees and what each park keeps come from the pages of California State Parks (`tools/page.py --all https://www.parks.ca.gov/?page_id=<park number>`, read in the session) for Weaverville Joss House, Shasta, Bodie, Columbia, Empire Mine and Fort Ross; the Mariposa courthouse from the Office of Historic Preservation listing; dates and what survives from Wikipedia. Not checked: the National Park Service pages for Manzanar, Kelso Depot and Harmony Borax Works (script-drawn or 404, so hours are `?`; a search result quoted Friday to Monday 9 to 4:30 for Manzanar in 2024, not recorded), Mission San Antonio's own page (hours `?`, and the route through the Fort Hunter Liggett reserve gate), interiors, parking on the ground, and what exactly stands at Harmony Borax Works. Red brick is `?` except Shasta (State Parks says brick buildings) and Columbia (rebuilt in brick after 1857).

## Leads
Places read about and not finished.

| Place | Where | What is known | What is missing |
|---|---|---|---|
| Cerro Gordo | Inyo County, CA | Mining ghost town, privately owned | A page of the owners with visiting rules |
| Mission La Purisima | Lompoc, CA | State park mission | Park page (page id was Refugio's, not found) |
| Calico | San Bernardino County, CA | Silver-mining ghost town | A source on what is original and visiting hours |
| Old Sacramento, Folsom Powerhouse, Point Reyes lighthouse | CA | Candidates only | Not looked up |

## Tips
- California State Parks pages are at `https://www.parks.ca.gov/?page_id=<number>` and the number is the park's own: 457 Weaverville Joss House, 456 Shasta, 509 Bodie, 552 Columbia, 499 Empire Mine, 449 Fort Ross. `page.py --all` returns the hours, fees and description; the number 603 was Refugio State Beach, not La Purisima, so check the title line.
- Wikipedia's point for the town of Shasta is 1.3 km from the park's ruins; the street-address lookup for 15312 Highway 299 landed on them. `photo_find.py` candidate distances showed it at once: a list of "1,300 m, BY NAME ONLY" candidates means the pin is wrong.
- nps.gov planyourvisit pages came back empty from `page.py` (script-drawn) and several guessed addresses were 404; the operating-hours page address is only found by web search.
- `app_smoke.js` tests the Android www build and failed on `dist/web` (it waits for a "Start a field log" button); it was not relevant to a places-only change.
