# wny_vtcb: Yates County, NY: the Keuka Outlet mills, Penn Yan, Dresden and Bluff Point
state: New York
region: wny
date: 2026-11-21
places: 17
file: data_wny_vtcb.py

## What this batch is
Seventeen places, the first pass in Yates County, New York (region `wny`, drawn at random by `choose.py --state ny`, which offered Penn Yan; the Atlas had nothing within 20 km), plus the Sampson Military Museum across Seneca Lake in Romulus. Ruins and traces on the Keuka Outlet Trail: Seneca Mills Falls with its mill walls and Lock 17, Cascade Mills Falls with the abandoned Taylor / J. T. Baker chemical works, and Lock 3 and the canal ditch near Dresden. Standing: the Birkett Mills (1824), the Penn Yan Historic District, Courthouse Park, the Oliver House Museum, the Sampson Theatre, Lake View Cemetery, the Ingersoll Birthplace Museum in Dresden, Esperanza on Bluff Point, Garrett Memorial Chapel, the Friend's Home (Jemima Wilkinson House), Dundee's district and First Presbyterian Church, and the Overackers Corners Schoolhouse. Sources: Wikipedia read with `wiki_raw.py` (and the county Register list with `--rows`), Frances Dumas's Outlet series in the Crooked Lake Review (1989–1990), uncoveringnewyork.com, TrailLink, the Finger Lakes Land Trust's trail page, HMdb, parks.ny.gov, garrettchapel.org, thebirkettmills.com and the Freethought Trail page. Not checked: anything on the ground; what is left at the Outlet sites rests on Dumas (1990) and one 2020s visit write-up; Lock 3 is an area pin from Dumas's "a quarter mile upstream of Route 14"; which mill the ruins across from the Cascade Mills buildings were (the blog says the Seneca Paper Mill, Dumas puts that mill at Seneca Mills Falls); the Keuka Outlet Trail's hours and rules (the Friends of the Outlet site is drawn by script); hours of the Oliver House Museum (yatescountyhistory.org would not connect) and the Overackers schoolhouse; the Ingersoll museum's times (only "weekends in summer and fall"); whether Esperanza still runs as an inn (only booking sites say so); owners of Lake View Cemetery; the dates of the courthouse buildings. The three Register forms tried (95001545, 79001652, 85000591) are NPGallery placeholders.

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Keuka Outlet locks 18–20 | Milo, NY, just upstream (west) of Seneca Mills Falls on the Outlet Trail | Dumas (Crooked Lake Review, April 1990) says they are easy to find where the canal ditch deepens between wetlands | A position: the LiDAR sheet at Seneca Mills shows the ditch; a session could read it with `look.py` and the trail's sign positions |
| Mays Mill, Milo Mill, Shutt's Mill, Fox's Mill sites | Keuka Outlet Trail between Penn Yan and Seneca Mills | Dumas's series has a history of each (crookedlakereview.com, 1989–1990); Shutt's paper mill burned on Halloween 1933; a few stones of Lock 25 lie east of the Fox's Mill road crossing | What is left today and a pin for each; the trail's interpretive signs are not on HMdb |
| Unnamed mapped ruin | 1.3 km east of Penn Yan (42.66028, -77.03776), on the Outlet | An OpenStreetMap ruin lead | A name and source: probably one of the Outlet mills |
| Italy Valley Methodist Church, St. Luke's Episcopal (Branchport), Middlesex Center Methodist Church | Yates County | Register listings (Wikipedia stubs) | Anything beyond the stub: what survives inside, services |
| Penn Yan, Keuka Park & Branchport trolley depot site | Branchport, NY (42.59932, -77.15134) | Pomeroy marker: electric trolley 1897–1927 | Whether anything of the depot or line survives |

## Tips
- Frances Dumas's "Along the Outlet of Keuka Lake" series in the Crooked Lake Review (`crookedlakereview.com/articles/1_33/...`) reads in full with `page.py --all` and gives a history of every mill site on the Outlet, with a lock-by-lock list in the April 1990 part.
- keukaoutlettrail.org (Friends of the Outlet) is drawn by script and `page.py` gets only its title; the Land Trust's gofingerlakes.org page names the maintainer and amenities.
- yatescountyhistory.org would not connect at all (no archived copy either); web search for the History Center returns only directories.
- The federal land map files the Seneca Mills Falls ground as Friends of the Outlet Inc., closed (XA), though the trail and picnic area there are open; `pincheck.py` prints CHECK ACCESS for it.
- Web searches in this session returned titles and links only, no quoted text.
