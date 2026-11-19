# fl_xhar: Florida: St. Augustine and Anastasia Island
state: Florida
region: fl
date: 2026-11-19
places: 17
file: data_fl_xhar.py

## What this batch is
Seventeen places in St. Augustine and on Anastasia Island, St. Johns County: the Castillo de San Marcos and Fort Matanzas, the Spanish coquina quarries that fed them and a marker-only chimney-and-well ruin by the quarry, the Oldest House and the Ximenez-Fatio House, the cathedral, the Nombre de Dios mission chapel, the Tolomato and Huguenot cemeteries, Flagler's Ponce de Leon and Alcazar hotels and Villa Zorayda, the 1891 jail, the lighthouse, the Fort Mose site and the 1898 water works. Sources: Wikipedia via wiki_raw.py, National Register forms (NPGallery text PDFs via page.py, which settled brick for the Ponce, jail, lighthouse and water works), NPS hours/fees/directions pages, the Anastasia State Park brochure PDF, HMdb marker pages, and the operators' own pages where they opened (cathedral, Tolomato, Lightner, lighthouse museum, Flagler College tours, Old Town Trolley for the jail, Fort Mose Historical Society, City of St. Augustine water-works page). The St. Augustine Historical Society, Ximenez-Fatio House and floridastateparks.org web pages refused page.py (403); for those the access note gives the visitor bureau's (visitstaugustine.com) hours and `hours='?'`. Not checked: anything on the ground; parking for most town places (only Mission Nombre de Dios and Fort Mose have a th= lot); interiors beyond what a source says. Pins of area precision: the Old Spanish Chimney and Well (marker position, ruins not seen on the aerial) and Fort Mose (Register point for the buried second fort). The Spanish Coquina Quarries pin is by the trailhead markers, where the LiDAR shows a long pit; the Register point 1 km south-east was not used. The Old Spanish Chimney and Well rests on one 1975 county marker (conf='mixed'); its ownership was not checked, so it is view-only.

## Leads
Places you read about and could not finish. One row each.

| Place | Where | What is known | What is missing |
|---|---|---|---|
| Moultrie Church | Moultrie, FL (29.81516, -81.33605) | On the St. Johns County Register list (14000553) | Not read; a source for what it is and whether it is open |
| Sanchez Homestead | Elkton, FL (29.737778, -81.478611) | On the Register list (01001083) | Not read; owner and access unknown |
| Hastings High School and Community Center | Hastings, FL (29.711111, -81.505) | Register list (06000502, 07000057) | Not read |
| Grace United Methodist Church | St. Augustine, FL (29.895090, -81.314947) | Flagler-era church on the Register list (79003132) | Not read; service times |
| Fort Matanzas visitor center lot | 8635 A1A, FL | OpenStreetMap lot "Nature Trail" 29.71540, -81.23395 | On the aerial the point was under trees, not a lot; find the lot so fort-matanzas can have a th= |

## Tips
- floridastateparks.org (every park page, hours-fees page) answers 403 to page.py; its brochure PDFs under /sites/default/files/media/file/ do read, and give hours and the fee rule.
- visitstaugustine.com listings read in full with page.py and give hours and fees for most St. Augustine attractions whose own sites refuse the tool; they are the county visitor bureau, not the operator, so hours from them stayed out of hours=.
- HMdb nearby list at the National Register point for the Spanish Coquina Quarries placed the quarry trail markers about 1 km north-west of the Register point; the Register point was not where the visitor goes.
- publish.sh stopped once because #186 (the new acc='open' and hours=) merged mid-session; after resync.sh, read the new "Access and hours" part of GUIDE.md section 4 before publishing again.
