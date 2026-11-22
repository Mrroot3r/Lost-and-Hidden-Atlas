# kcmo_atbq: Missouri: a first scatter across the state
state: Missouri
region: kcmo
date: 2026-11-22
places: 18
file: data_kcmo_atbq.py

## What this batch is
Eighteen places spread across Missouri, which had 23, nearly all in Kansas City: Ha Ha Tonka castle ruins, Maramec Iron Works, Alley Spring Mill, Dillard Mill, Bollinger Mill and the Burfordville Covered Bridge, Watkins Woolen Mill, Fort Davidson, the Louis Bolduc House, the Lemp Brewery, the Oliver Anderson House at Lexington, Federal Mill No. 3 (Missouri Mines), Deutschheim, the Hunter-Dawson House, Arrow Rock and its tavern, the Mark Twain Boyhood Home, the Pony Express stables and the Ray House at Wilson's Creek, and the Sandy Creek Covered Bridge. Facts from Wikipedia read with `wiki_raw.py`; access and hours from Missouri State Parks pages (each site's own page and its hours page, read with `page.py`), National Park Service place pages, French Colonial America's home page and the Pony Express National Museum's hours page. Not checked: hours and fees at Maramec Spring Park and the Mark Twain Boyhood Home (both sites answered 403), Alley Mill's current season (only a 2013 park release could be read) and the Ray House's opening (the park's hours page is drawn by script); street parking in Ste. Genevieve, Hermann, Hannibal and St. Joseph. Maramec's pin is the Register district point at the works, not on the furnace itself. Red brick from Wikimedia pictures looked at with `brick.py look`; four places left `?`. Nothing was checked on the ground.

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Locust Creek Covered Bridge | Pershing State Park, Linn County, MO | Missouri State Parks: the 1868 Howe-truss bridge, 151 ft, the longest of the state's four, has been moved to the park's day-use area and stays closed while its approaches are built | Its new position, and whether it has reopened |
| Patee House | St. Joseph, MO (39.75595, -94.84492) | Wikipedia: 1858 hotel, Pony Express headquarters, now a museum | Hours from its own page; a pin check |
| Old Lead Belt and Iron County | Park Hills to Ironton, MO | Elephant Rocks granite quarries and St. Joe State Park are near Missouri Mines | Sources for what is left of the quarries and the mines |

## Tips
- Missouri State Parks hours pages are at `https://mostateparks.com/hours/<number>/historic-site/<slug>`; the number is only in the site page's links (grep the cached page in `research/pages/` for `href="/hours/`). Guessed `/park/<slug>/hours` addresses come back empty.
- Fort Davidson's state site is `battle-pilot-knob-state-historic-site` on mostateparks.com.
- maramecspringpark.com and marktwainmuseum.org answer 403 to `page.py`.
- Wikipedia's coordinate for Watkins Woolen Mill falls in the park lake and Bollinger Mill's in a field: OpenStreetMap's buildings (`osmnear.py ... buildings -g`) were right.
- The series tag list has no tag for covered bridges; `check.py` refuses `covered`.
