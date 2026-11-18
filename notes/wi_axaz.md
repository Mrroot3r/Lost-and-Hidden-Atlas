# wi_axaz: Mineral Point, Dodgeville and the Wisconsin lead region
state: Wisconsin
region: wi
date: 2026-11-18
places: 19
file: data_wi_axaz.py

## What this batch is
Nineteen places in the Wisconsin lead region: Iowa County (Pendarvis and the Merry Christmas Mine Hill trails, the 1856 depot in Mineral Point, the 1859 courthouse, Dodge Mining Camp Cabin and Old Rock School in Dodgeville, the Linden, Hyde and Plum Grove churches, the Thomas Stone Barn, the Helena Shot Tower at Tower Hill State Park, Unity Chapel and Taliesin) and Lafayette County (First Capitol, Prairie Spring Hotel, St. Augustine Church at New Diggings, Gratiot House, the Badger Mine at Shullsburg, the Benton stone water tower). All standing except the Mine Hill (ruins). Sources read in the session: Wikipedia with `wiki_raw.py` (articles and the Register list rows for both counties), the DNR's Tower Hill info and history pages, the Wisconsin Historical Society's Pendarvis and First Capitol home pages and the 2019 Mine Hill trail guide PDF, the Mineral Point Chamber listing for the depot, Travel Wisconsin, SAH Archipedia, Iowa County's clerk page, the Iowa County Historical Society, The Prairie Enthusiasts (Thomas Tract), American Players Theatre's 2026 Taliesin guide and SWNews4U. Not checked: Taliesin's tour season and prices (its site answered 403), the Badger Mine's hours (site drawn by script), the Dodge cabin's opening times, the First Capitol and Pendarvis opening days for 2027, owners of Unity Chapel, Linden church, St. Augustine, Benton tower and Gratiot House (OpenStreetMap tags Gratiot House a guest house; not used as a fact), and every interior except where a source describes it. Five pins were moved off fields or roads with look.py and pix.py (First Capitol, Taliesin, Gratiot House, Benton tower, Pendarvis); the Pendarvis parking point is the nearest mapped lot and is not confirmed as the site's own lot. The Mine Hill pin is an area pin. Brick: no red brick named by any source; '?' where no source said what the building is made of (depot, Unity Chapel, Taliesin, First Capitol, Badger Mine). Nothing seen on the ground.

## Leads

| Place | Where | What is known | What is missing |
|---|---|---|---|
| Hyde's Mill | Ridgeway, WI (Mill Creek, near Hyde) | Wisconsin Historical Society property record HI47303 and photographers' pages show an old mill; the record page answered HTTP 522 | A source opened that says what stands, its date and owner, and a pin |
| Spensley Farm smelting furnace | Mineral Point, WI (Register 97000330, no coordinate in the article) | Wikipedia: James Spensley's house, spring house, lead-smelting furnace and barn | Where it is, what is left of the furnace, and whether anything can be seen from a public road |
| Mottley Family Farmstead | Ivey Road, Willow Springs, WI (42.80389, -90.14583) | Wikipedia: abandoned 1854 farm on an isolated ravine, 1.5-storey limestone farmhouse c.1860 and bank barn | Owner and whether it can be seen from Ivey Road; check the pin on the aerial |
| Linden High School | Linden, WI (42.915556, -90.268611) | Register list: 1913 two-storey brick school, German Renaissance Revival | Its present use and whether the brick is red |
| Mineral Point Historic District / Shake Rag Street | Mineral Point, WI (42.865, -90.176944) | Register list: the Cornish cottages on Shake Rag Street and the old town | A walking-tour source that names the best buildings to add one by one |
| Belmont Mound and the Military Road | Belmont, WI | Belmont Mound State Park lot turned up by parking.py near First Capitol; Fort Defiance stockade named in the Prairie Spring Hotel article | A source for anything left of Fort Defiance or the road |

## Tips
- The Register list for Iowa County gives the Tower Hill shot tower's own point on the bluff edge, which the federal land map puts just outside the park; the pin check then says CHECK ACCESS though the park owns it.
- Register list and Wikipedia coordinates in rural Wisconsin landed in crop fields for First Capitol, Taliesin and Gratiot House (130 to 250 m off); `nom.py` found OpenStreetMap points on the right buildings for First Capitol and Gratiot House.
- taliesinpreservation.org answers 403 to `page.py`; American Players Theatre's yearly "Area Guide Spotlight" posts describe the tours.
- badgermineandmuseum.com is drawn by script; Travel Wisconsin and SWNews4U carry the tour facts but not the hours.
- The Wisconsin Historical Society site pages (pendarvis.wisconsinhistory.org, firstcapitol.wisconsinhistory.org) read with `page.py`, but their "plan your visit" pages answer 404; the home page carries the season.
- `check.py` refused tag 'burial' (that is a category); the cemetery series tag is `cemeteries`. Nothing in `pincheck.py` or `build_sites.py` catches it earlier.
