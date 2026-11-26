# boise_bwzz: Boise, Idaho: downtown and the North End
state: Idaho
region: id
date: 2026-11-26
places: 10
file: data_boise_bwzz.py

## What this batch is
Ten standing buildings in downtown Boise and the North End, worked from the names in one video (Old World Exploration, "Old World Boise, Idaho"; the record is source/videos/20230623_f8uvkruJENk.md). Added: St. John's Cathedral, Boise High School, the Idanha Hotel, the Hoff Building (Hotel Boise), the Owyhee Hotel, the old U.S. Post Office and Federal Building (Borah Building), the Old Ada County Courthouse, the Carnegie Public Library, Longfellow School and the Fort Boise officers' house on the VA hospital grounds (this finishes the Fort Boise lead from id_tdbo). Sources: Wikipedia read with wiki_raw.py, the Ada County Register list, NPGallery nomination forms (Fort Boise 72000433 read in full), the City of Boise's Julia Davis Park history bollard pages, the Idaho Architecture Project, and the cathedral's own page for its visiting and Mass times. Pins are address lookups checked on the aerial; St. John's was moved onto the cathedral, the Idanha set to the OpenStreetMap building. NOT checked: anything on the ground; whether the Old Ada County Courthouse and the old post office open to the public now (both are `view`); which of the old Fort Boise buildings is the officers' house (pin is `area`, on a building OpenStreetMap dates to 1863; a 1974 Commons photo of the commander's quarters sits about 350 m away by its own coordinate); parking is street parking downtown, owners of the mapped lots not checked. The 1938–39 courthouse is Art Deco / Streamline Moderne, not International Style, and was kept.

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Elks Temple | Boise, ID (Register point 43.618333, -116.201389) | Wikipedia: built 1913–14, Tourtellotte & Hummel, listed 1978; the article gives 350 Jefferson St | Whether it still stands and the right address: the geocoder put 350 W Jefferson far from the Register point |
| Ada Odd Fellows Temple | Boise, ID (43.616111, -116.204167) | Register list says only parts of the facade still stand | Unchanged from id_tdbo: a source on what is left |
| Cathedral of the Rockies | Boise, ID, 717 N 11th St (43.6225, -116.2025) | Wikipedia: First United Methodist, Gothic Revival by Harold E. Wagoner; a search result says the present church opened in 1960 | Building date from a page opened in the session, and whether it is worth adding |

## Tips
- HMdb.org answered HTTP 403 to page.py for every marker tried (267460, 267225); the archived copies need the web fetch tool, which nobody approves in a scheduled run.
- The City of Boise's Julia Davis Park bollard pages (cityofboise.org/.../decorative-bollards/<name>/) read cleanly with page.py --all and settle what became of lost Boise buildings (City Hall, the Natatorium, St. Teresa's Academy, the Ada County Courthouse).
- The Idaho Architecture Project (idahoarchitectureproject.org/properties/<slug>/) reads cleanly with page.py --all and gives current use and surviving fabric.
- The Idaho State Law Library's own page now gives 501 W. Front Street, so the Old Ada County Courthouse's present tenants were not settled.
