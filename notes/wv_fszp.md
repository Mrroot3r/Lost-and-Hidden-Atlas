# wv_fszp: West Virginia: a second scatter across the state
state: West Virginia
region: wv
date: 2026-11-22
places: 17
file: data_wv_fszp.py

## What this batch is
Seventeen places spread over seventeen West Virginia counties, which had 33 places, most in Jefferson County and the New River Gorge: Grave Creek Mound (Moundsville), the B&O Martinsburg Shops roundhouse, Fort Ashby, Indian Mound Cemetery (Romney), the 1796 Mansion House in Tu-Endie-Wei State Park (Point Pleasant), the Carnifex Ferry and Droop Mountain battlefields, the Bramwell and Matewan historic districts, Graceland (Elkins), Arthurdale, Jackson's Mill (Weston), the Lee Cabin in Lost River State Park, the Glen Ferris Inn, the Sites Homestead at Seneca Rocks, Camden Park (a 1903 trolley park with an Adena mound) and the Kimball World War Memorial. Facts come from Wikipedia (`wiki_raw.py`, including Register list rows) and, read with `page.py`, the pages of WV Culture (Grave Creek), WV State Parks, WV Tourism, the Friends of Ashby's Fort, WV DAR, SAH Archipedia, NPS, Arthurdale Heritage, the Forest Service (Seneca Rocks), WVU Jackson's Mill, Davis & Elkins College, the Mine Wars Museum, WV Public Broadcasting and the Glen Ferris Inn. Not checked: anything on the ground; hours of the Martinsburg roundhouse, the Mansion House, Droop Mountain's museum, the Lee Cabin, Jackson's Mill, Graceland's restaurant, the Glen Ferris Inn, Camden Park (its site refused the request) and the Kimball memorial; parking almost everywhere; interiors. Pins that mark only an area: Carnifex Ferry and Droop Mountain (OpenStreetMap park points; each has a parking lot as its trailhead point), Bramwell (district point), the Lee Cabin (Wikipedia point in woods; no building seen). The Lee Cabin's date differs between two Wikipedia articles (about 1800 or about 1820), and the Glen Ferris Inn's between 1815, 1839 and 1848 (`conf='mixed'`). Red brick: Glen Ferris 'yes' (Wikipedia names a red brick wing), Bramwell 'some' and Fort Ashby 'no' from Commons photographs, 'no' where a source names stone, wood, logs or earth; '?' for the rest.

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Bulltown Historic District | Burnsville Lake, Braxton County, WV (38.78861, -80.56639, Wikipedia point for Bulltown) | Wikipedia's Bulltown article mentions Union trenches, seven Confederate graves and a historic centre at the Corps of Engineers lake | A source of its own (no Wikipedia article for the district) and the Corps' page for hours |
| Lee House, Lost River State Park | 38.89571, -78.92544 (OpenStreetMap building "Lee House") | Possibly the Lighthorse Harry Lee Cabin, 200 m from the Wikipedia point | Confirm it is the cabin, then move the pin of lee-cabin-lost-river |
| Mansion House museum hours | Point Pleasant, WV | DAR chapter opens it seasonally (Wikipedia) | Days and times from the chapter or the park |

## Tips
- WV State Parks park pages (`wvstateparks.com/park/<name>/`) give the address and little else to `page.py`; WV Tourism's company pages (`wvtourism.com/company/<name>`) carried museum hours for Carnifex Ferry when read with `page.py --all`.
- `camdenpark.com` answers HTTP 403 to `page.py`; no hours were read.
- `jacksonsmill.wvu.edu/historic-area` is 404; the live page is `/facilities/historic-area`.
- Register list coordinates for Arthurdale fell on a house; the ArcGIS geocoder on Arthurdale Heritage's address (18 Q Rd) landed on the museum buildings.
