# ar_hvkd: Arkansas: a second scatter across the state
state: Arkansas
region: ar
date: 2026-11-23
places: 10
file: data_ar_hvkd.py

## What this batch is
Ten places in the parts of Arkansas still thin on the map: Historic Washington (south-west), Borden House at Prairie Grove, Elkhorn Tavern at Pea Ridge and Old Main and Headquarters House in Fayetteville (north-west), the Rush zinc-mining ghost town on the Buffalo River, Drennen-Scott House at Van Buren, Plum Bayou Mounds near Scott, Parkin Archeological State Park, and Texarkana Union Station. Facts came from Wikipedia (`wiki_raw.py`) and the pages of Arkansas State Parks and the National Park Service (`page.py`). Headquarters House and Drennen-Scott hours come from web search results quoting their operators, whose pages would not open (403 and a connection error); the two sources for Drennen-Scott disagree and both are in the entry. Not checked: interiors, parking, whether the Borden House and Elkhorn Tavern can be entered, who owns Texarkana Union Station, any visit on the ground. Headquarters House and Drennen-Scott pins were moved to address-lookup points because the Wikipedia coordinates were off the building. All ten have a Wikipedia article with a picture, so the picture finder had nothing to do.

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Old Davidsonville Historic State Park | Pocahontas area, Randolph County | A ghost town of the early 1800s; the park's page address guessed from its name gave 404 | A source opened for what is left and its hours |
| Mount Holly Cemetery | Little Rock (34.7376, -92.2785) | Wikipedia: Quapaw Quarter burial ground, listed 1970, ten governors buried; a web address guessed for it was a church of the same name | Its keeper's page for access and hours |
| Rush: Morning Star mine buildings | Buffalo National River, Marion County | Park Service names a hotel and mill ruin and a Hicks store site | Exact points for each; the pin is the district |

## Tips
- `https://www.nps.gov/places/<name>.htm` worked for Elkhorn Tavern but gave 404 for Rush; the Rush article is `nps.gov/articles/rush-historic-district-500856.htm`, found by web search.
- `washcohistoricalsociety.org` and `uafs.edu` would not open with `page.py`; a web search result quoting them was the only source for hours.
- Series tags in a place list must come from the short list `check.py` prints (forts, hotels, stations ...); other words such as "civil-war" or "mounds" stop publish.sh. `st` is `ruins`, not `ruin`; `build` fails with a bare KeyError.
- A Wikipedia web address guessed for a church-named cemetery (mountholly.org) leads to a namesake church: check the page's text before using it.
