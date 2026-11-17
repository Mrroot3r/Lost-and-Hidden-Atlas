# hi_atut: Oahu, Hawaii
state: Hawaii
region: hi
date: 2026-11-17
places: 16
file: data_hi_atut.py

## What this batch is
The first Oahu batch (region `hi` drawn by `choose.py`; the only Hawaii place before was the Kōloa mill on Kauai). Sixteen places: four heiau (Puʻu o Mahuka, Keaīwa, Ulupō, the Kapaʻeleʻele fishing shrine at Kahana), the Kūkaniloko birthstones, two fishponds (Huilua, Heʻeia), two lighthouses (Makapuʻu, Diamond Head), the Diamond Head summit Fire Control Station, Battery Randolph, the Royal Mausoleum, the Old Pali Road, the Koko Crater tramway, the Kamananui Valley carriage road and its bridges, and the Oahu Railway grade at Kaʻena Point. Facts come from Wikipedia (`wiki_raw.py`), the Hawaii Division of State Parks page for each state park (read with `page.py`; hours, fees and rules from there), the City of Honolulu parks news page (Koko Crater), the US Army museum page, the Office of Hawaiian Affairs and the Kūkaniloko stewards' site, HMdb markers 73554 and 73555 (Pali Road), and three newspaper archive pages for Moanalua Valley. Every pin was looked at on the aerial and the LiDAR sheet; four were moved (Keaīwa, Diamond Head summit and Battery Randolph to their OpenStreetMap buildings, Heʻeia onto its wall with `pix.py`). Not checked: anything on the ground; hours for the Koko Crater tramway and Kamananui Valley Road (no managing-body page read); where the rail bed shows along the Kaʻena Point trail; where the Kapaʻeleʻele shrine and lookout stand on their loop; whether the Saratoga Road lot by the Army museum is public; when Battery Randolph was built. Pins that mark only a lot or trailhead: `kapaeleele-koa-kahana` (park lot), `kaena-point-railroad` (Mokuleʻia lot); `kamananui-valley-road` is a point on the road, not a bridge; `old-pali-road` is the lookout, not the road. Kūkaniloko is closed to the public (view only). The Heʻeia pond is visited only on the nonprofit's tours (view from Heʻeia State Park).

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Kualoa Sugar Mill ruins | Kualoa, Oahu, HI, by Kamehameha Highway near Kualoa Ranch (about 21.52, -157.836) | Built and run 1863–1870 by C. H. Judd and S. G. Wilder (kualoa.com/about; Wikipedia "Kualoa Ranch"); chimney and part of a building visible from the highway; private ranch land | The ruin could not be picked out on the aerial at two scales; a coordinate on the chimney (the GNIS "Kualoa Sugar Mill Beach" point lands on beach buildings) |
| Kaniakapūpū (Kamehameha III summer palace) | Nuʻuanu, Oahu, HI (21.35075, -157.81446, Wikipedia) | Stone ruins of the 1840s palace (Wikipedia) | Officially off-limits to the public, with citations for trespass (Wikipedia); no public way to view it was found |
| Kahuku Marconi wireless station | Kahuku, Oahu, HI (21.70631, -157.97308, Wikipedia) | Opened 1914; chimney removed 1924; owners demolished the roof and interior of one remaining structure in 2024 (Wikipedia) | Owner, what still stands, and any public view |
| Opana Radar Site | Kawela Bay, Oahu, HI (21.685485, -158.009666, Register list) | Register-listed; "not open to the public" (Wikipedia) | A public viewpoint, if there is one |
| B-24 bomber remains on the ʻAiea Loop Trail | Keaīwa Heiau State Recreation Area, Aiea, HI | State Parks says remnants of a B-24 that crashed in 1944 can be seen along the trail | Where on the 4.8-mile loop; a second source |
| Pahukini Heiau and Kawaewae Heiau | Kailua and Kaneohe, Oahu, HI (21.394722, -157.769722; 21.395222, -157.785556, Register list) | Register-listed heiau; State Parks names Pahukini as one of the heiau round Kawai Nui | Owner, access and a managing-body page |
| Waialua Sugar Mill | Waialua, Oahu, HI | Ran 1865–1996, last plantation on Oahu to close (Wikipedia) | What stands now and who owns it; a coordinate |

## Tips
- `nom.py` hit HTTP 429 after about ten names in a row; `osmnear.py ... buildings -g 'heiau|bunker|museum'` found the Keaīwa Heiau, the Diamond Head Fire Control Station and Battery Randolph by tag when name search failed.
- Hawaii State Parks pages (`dlnr.hawaii.gov/dsp/parks/oahu/<slug>/`) read fine with `page.py`, but the `-g` summary cuts the winter hours: use `--all` and grep "Winter:". Every page ends with the same statewide closure notices, which match most patterns; cut them off at "**IMPORTANT PARK NOTICES".
- `camping.ehawaii.gov` (the state trail permit pages) answers 403.
- The HMdb nearby list round Oahu returned the same Pearl Harbor markers whatever the point; it was not useful for finding ruins here.
- Register list coordinates on Oahu were good for the heiau and lighthouses but off for Keaīwa (400 m, in forest on private watershed land) and Battery Randolph (450 m); Wikipedia's Heʻeia Fishpond point lands on houses.
