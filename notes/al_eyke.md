# al_eyke: Alabama: a third scatter, the Gulf coast to the Tennessee Valley
state: Alabama
region: al
date: 2026-11-24
places: 11
file: data_al_eyke.py

## What this batch is
Eleven places in Alabama, the state with the fewest on the map: Fort Morgan, Fort Gaines, Oakleigh and the Bragg-Mitchell Mansion in the Mobile Bay area; the First White House of the Confederacy (Montgomery); The Oaks at Tuskegee; the Gorgas House (Tuscaloosa); 16th Street Baptist Church and Rickwood Field (Birmingham); the Huntsville Depot; Ivy Green (Tuscumbia). Sources were read with wiki_raw.py and page.py: Wikipedia, the Encyclopedia of Alabama, the Alabama Historical Commission, the National Park Service and each place's own page; hours for Oakleigh, Rickwood, Fort Morgan's admission and the 16th Street tour days were also confirmed against web-search results that quote the managers' pages. Not checked: anything on the ground, parking (marked as not checked), interiors, Huntsville Depot's current status beyond Wikipedia, ticket prices for several houses. Oakleigh's own site (historicmobile.org) gave no hours and its days conflict between listings, so conf is mixed. Pins were looked at on the aerial; all sit on the buildings. Three pictures were chosen with photo_find.py (Fort Morgan, The Oaks, Gorgas House).

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Cathedral-Basilica of the Immaculate Conception | Mobile, AL | Wikipedia article title did not resolve; no official page with Mass times turned up in search | A source for its history and its own hours page |
| Burritt on the Mountain | Huntsville, AL (34.71583, -86.53944) | Open-air museum of 19th-century buildings moved to a 1930s mansion; hours on its own page (Tuesday to Saturday, Sunday afternoon, seasonal times) | Which pieces are original 19th-century fabric; left out as the mansion dates from 1935-38 |
| Alabama Theatre | Birmingham, AL (33.51491, -86.80918) | Built 1927 by Publix, original Wurlitzer organ (Wikipedia) | A hours or tour page that was read |

## Tips
- Choosing the thinnest ground: the --thinnest flag picks a whole state, and start.py lists nothing statewide; use a central town with a radius of 400 km.
- Many Alabama manager sites (ahc.alabama.gov property pages, huntsvillealabama.gov, oakleighmuseum.com) 404 or time out in page.py; web search results quote the pages and the Encyclopedia of Alabama is a reliable fallback.
- page.py cuts sentences at "a.m." so times appear truncated; read the lines before and after, or search the cached page in research/pages/.
