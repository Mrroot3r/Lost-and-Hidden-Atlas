# nyc_hklm: Town of Huntington, Long Island
state: New York
region: nyc
date: 2026-11-20
places: 19
file: data_nyc_hklm.py

## What this batch is
Nineteen places in the Town of Huntington, Suffolk County (region `nyc`, drawn by `choose.py --state ny`, which offered Huntington; `start.py` found no Atlas place within 6 km). Nearly all standing. Huntington village: Old First Presbyterian Church (1784), the Old Burying Ground and site of Fort Golgotha, the Soldiers and Sailors Memorial Building with the Old Town Hall district, the David Conklin Farmhouse, the Kissam House, Bethel AME Church. Lloyd Neck and Lloyd Harbor: the Van Wyck–Lefferts Tide Mill (boat tours only), Joseph Lloyd Manor, the 1711 Henry Lloyd Manor House, Caumsett (Marshall Field III estate), Huntington Harbor Light (boat tours). Also Eatons Neck Light (Coast Guard station, ask first), the Vanderbilt Museum at Centerport, OHEKA Castle, Coindre Hall, the Suydam Homestead (closed for repairs), Cold Spring Harbor's Main Street with the Whaling Museum, and the Northport Carnegie library (historical society museum). Sources: Wikipedia with `wiki_raw.py` (and `--rows` on the town's Register list), the Town of Huntington's "Famous People & Places" PDF sheets, the Huntington Historical Society, Preservation Long Island, NYS Parks, the lighthouse society, the Vanderbilt Museum, OHEKA, the Greenlawn-Centerport Historical Association and the Whaling Museum, all read with `page.py`. Pins from the ArcGIS geocoder or `nom.py`, all looked at on the aerial; two were moved with `pix.py` (the burying ground had landed on a parking lot; the Vanderbilt geocoder point was on a shore building, not the mansion). Not checked: anything on the ground; hours at Henry Lloyd Manor and the Northport museum (its site answered 403); church service times for Old First and Bethel AME (no page of their own found); the Old Burying Ground's owner; parking at most village places. Conflicting dates are given both ways (Whitman house 1816/1819, tide mill 1793/1795, Bethel AME's building c. 1845 or 1925, Coindre Hall sold 1930/1939, lighthouse automated 1949/1967, Conklin farmhouse Sunday hours noon or 1 p.m.).

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Cold Spring Harbor Fish Hatchery & Aquarium (1883 state trout hatchery) | Cold Spring Harbor, NY (Wikipedia 40.8574, -73.4648) | State trout hatchery from 1883 to 1982, then a nonprofit education centre (Wikipedia) | The hatchery's own page for hours and which buildings are old; search found only directories |
| Fort Franklin site, Lloyd Neck | Lloyd Harbor, NY ("Fort Hill", west end of Lloyd Neck) | British fort of 1778, the largest on Long Island in its day (NYS Parks Caumsett page, Town sheet "Lloyds of Lloyd Neck"); Fort Hill Estate is Register-listed (88000599) | Whether anything can be seen from a public way; the land looks private |
| Northport Veterans Administration Hospital Historic District | East Northport, NY (40.897863, -73.313273) | Register district, part of the Second Generation Veterans Hospitals listing | A source on what stands and whether visitors may walk the grounds |
| Old Huntington Town Hall (1910) and Huntington Sewing and Trade School (1905) as their own places | Huntington, NY | Named in the Town sheet on the Memorial Building; folded into that entry here | Their own pages, hours, and brick (the Wikipedia photo of the Town Hall was fetched but not used) |

## Tips
- The Town of Huntington's "Famous People & Places" folder (`huntingtonny.gov/content/13747/99540/16499/default.aspx`) has a one-page PDF history sheet for most of the town's old buildings; the page's cached HTML lists every PDF address. They read cleanly with `page.py`.
- `oldfirstchurch.org` is a church in Tallahassee, not Huntington's Old First; no page of the Huntington church was found.
- northporthistorical.org answers 403 to `page.py` and its archived copy could not be fetched.
- The Huntington Historical Society's tours of the Lefferts Tide Mill and the lighthouse society's tours both leave from Gold Star Battalion Beach (mapped lot at 40.89659, -73.43445).
