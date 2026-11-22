# mi_wmdx: Michigan: a first scatter across the state
state: Michigan
region: mi
date: 2026-11-22
places: 18
file: data_mi_wmdx.py

## What this batch is
Eighteen places spread across Michigan, which had 24 places, all but the Capitol in Marquette County: in the Keweenaw (Central Mine and village, Quincy Mine No. 2 hoist house, Eagle Harbor Light, Calumet Theatre, Fort Wilkins), the eastern Upper Peninsula (Bay Furnace at Onota, Whitefish Point Light, Point Iroquois Light), Iron Mountain (the Cornish Pump), the Straits (Fort Mackinac, Colonial Michilimackinac), Lake County (Marlborough cement plant ruins), Port Huron (Fort Gratiot Light), Detroit (Michigan Central Station, Historic Fort Wayne), Marshall (Honolulu House), Monroe (River Raisin battlefield) and Saginaw (Castle Museum). History came from Wikipedia and the county Register lists, read with tools/wiki_raw.py. Hours and access came from the pages of whoever runs each place, read with tools/page.py. Four pins were moved to OpenStreetMap points (tools/nom.py) because the Wikipedia or Register coordinate fell in water or on a lot: Calumet Theatre, Fort Wilkins, Point Iroquois and the Cornish Pump. Not checked: nothing on the ground. No summer hours could be read for Fort Wilkins (the History Center's visitor page answers 404) or the Cornish Pump (its page said only "closed for the season"), and the summer hours for Fort Gratiot weren't checked either. Marlborough's owner was not found: it is view-only from James Road, and Wikipedia and a radio station's page disagree about what is left of the village (conf='mixed'). The Bay Furnace stack can't be seen under the trees on the aerial. Red brick is '?' wherever no source said what colour the brick is (Fort Wayne, Michigan Central, Quincy, Fort Gratiot, Whitefish Point, Fort Mackinac, Central, Cornish Pump).

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Quincy Mining Company stamp mills | Osceola Township, MI (47.146667, -88.46) | Register list: stamp mill first built in the 1880s on Torch Lake | Owner and whether the public may visit |
| Calumet and Hecla Industrial District | Calumet, MI (47.2425, -88.45) | Register list: ten structures of the Calumet and Hecla mines | Which buildings stand and which are open (Keweenaw National Historical Park pages) |
| Schoolcraft Furnace Site | Munising, MI (46.423889, -86.6225) | Register list: iron furnace begun 1867 | What is left to see and who owns it |
| Ardis Furnace | Iron Mountain, MI (45.836944, -88.052778) | Register list: experimental blast furnace built 1908 by John T. Jones | What is left and access |
| Alabaster Historic District | Alabaster, MI (44.186667, -83.567778) | Register list: open-pit gypsum mine, processing buildings, company town | Owner and access |
| Mission Point Light | Old Mission Point, MI (44.99131, -85.47947) | Wikipedia: 1870 wooden light, copy of the Mama Juda Light | The township's page for hours |
| Grist Mill Bridge, Dam and Mill Site | Duplain Township, MI (43.0899, -84.4058) | Register list: Parker truss bridge, Elsie mill pond dam, mill site | A source that says what is left and its access |

## Tips
- page.py --all printed only the page's first line (the menu) for the Keweenaw County Historical Society's schedule page. The cached copy in research/pages/ had the full text, so the hours were read from that.
- michigan.gov/mhc visitor-information pages answer HTTP 404 from page.py, but the parent page (michigan.gov/mhc/museums/fwchl) opens and gives admission, though no hours.
- In the Upper Peninsula, Wikipedia and Register coordinates for lighthouses and forts on the shore often fall in the water; nom.py found the right point every time.
