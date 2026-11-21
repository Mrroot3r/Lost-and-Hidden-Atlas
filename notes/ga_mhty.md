# ga_mhty: Georgia: the coast, Ebenezer, Augusta, Macon, Andersonville and the north
state: Georgia
region: ga
date: 2026-11-21
places: 15
file: data_ga_mhty.py

## What this batch is
A first scatter of 15 places across Georgia outside the northeast Piedmont, where all 20 earlier Georgia places were: on the coast Fort Pulaski, the Wormsloe tabby ruins, Fort McAllister, Midway Congregational Church, Jerusalem Lutheran Church at Ebenezer, Horton House on Jekyll Island, Fort Frederica, Hofwyl-Broadfield Plantation and the Dungeness ruins on Cumberland Island; inland Andersonville, Hay House in Macon, Sibley Mill in Augusta, the Dahlonega courthouse, the Chief Vann House and Cooper's Furnace. Facts came from Wikipedia (tools/wiki_raw.py), and hours from the managing bodies' own pages read with tools/page.py: the National Park Service (Fort Pulaski's hours page is drawn by script, so its "Explore Fort Pulaski" and visitor-center pages were used), Georgia State Parks (gastateparks.org), the Jekyll Island Authority, the Midway Museum, the Jerusalem Lutheran congregation, Hay House, HMdb and recreation.gov. Not checked: anything on the ground; adult admission prices (the state pages read gave only the children's rate); Hay House tour times (its hours page would not open); hours at Cooper's Furnace and Horton House; whether Midway Church opens outside its April service; Andersonville's fees; which dock and how long a walk Dungeness is from the Cumberland Island ferry. The Wormsloe ruin, the Horton House walls and the Wormsloe, McAllister and Frederica parking lots are under trees on the aerial; their points come from OpenStreetMap. Brick: yes for Fort Pulaski (25 million bricks, Wikipedia), Jerusalem Lutheran and the Vann House (sources say brick) and Sibley Mill (a Commons photograph); no for the tabby ruins, Andersonville and Cooper's stone stack; the rest '?'.

## Leads
Places you read about and could not finish. One row each; delete the example row. Leave the table header.

| Place | Where | What is known | What is missing |
|---|---|---|---|
| Columbus Ironworks | Columbus, GA (32.46306, -84.99528) | Built 1853, made cannon, pistols and swords for the Confederacy, now the Columbus Georgia Convention & Trade Center (Wikipedia; pin checked on the aerial, on the building) | Written and pin checked, then taken out: check.py says the pin is in Alabama, because Georgia's outline runs about 1.5 km east of the Chattahoochee here and the border test only measures to outline corners (nearest 3 km away). Needs the tool fix in Tips, then it can go in as written |
| Chesser Island Homestead | Okefenokee National Wildlife Refuge, near Folkston, GA (30.70667, -82.16222, Wikipedia) | A yellow-pine homestead built 1927 by Tom and Iva Chesser, with smokehouse, syrup shed and corncrib, kept by the refuge (Wikipedia: Chesser Island) | The refuge's own page for hours and the swamp-park entrance fee |
| Midway Museum key to the church | Midway, GA | The museum opposite gives tours Tuesday to Saturday 10 to 4 | Whether it opens Midway Church to visitors, from its own page or by telephone |

## Tips
- check.py's border test (`near_state`) measures only to the outline's corner points, so a pin on the right bank of a river border far from a corner fails as the wrong state: Columbus, Georgia, 300 m east of the Chattahoochee, is "in al". Measuring to the outline's edges, not its corners, would let it through as a warning.
- gastateparks.org pages read well with page.py; the hours are in the "Hours." block, so `page.py --all <url> | grep -o '.{200}Hours.{300}'` gives days and times when `-g` returns only part of them. The address for Hofwyl-Broadfield is `HofwylBroadfieldPlantation` (the hyphenated one is 404).
- Wikipedia's "Hay House" is not the Macon mansion: the article is "Johnston–Felton–Hay House".
- exploregeorgia.org answers 403 to page.py, as the first Georgia batch found.
