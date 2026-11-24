# adk_ticon_rkwm: Ticonderoga: the La Chute mill village and the fort
state: New York
region: adk
date: 2026-11-24
places: 16
file: data_adk_ticon_rkwm.py

## What this batch is
Sixteen places in Ticonderoga, Essex County, New York (region `adk`, aimed at the Adirondacks by the owner's channel; `start.py` found no Atlas place in the old village, which scores 37 with 12 listed places and 2 districts, and only the thin landmark pin for the fort). Added: Fort Ticonderoga as a full entry (`was='lm-fort-ticonderoga'`), the French Lines and Carillon Battlefield, the lower falls and their mill sites in Bicentennial Park, the upper falls dams and mill sites at Alexandria, Frazier Bridge, the Heritage Museum (the 1888 paper-company office), and ten downtown Register buildings (gristmill, Pad Factory, Gilligan and Stevens Block, bank, post office, Black Watch Library, Community Building, Liberty Monument, Hancock House, armory). Sources: Wikipedia as raw text with `wiki_raw.py`; HMdb marker pages for the La Chute Riverwalk panels; the Town of Ticonderoga's parks, Frazier Bridge and museum pages; Fort Ticonderoga's hours, Mount Defiance and Carillon Battlefield pages and trail guide; Essex County tourism and Lakes to Locks Passage listings. Every web page other than Wikipedia was read with the web fetch tool, because the shell could not reach those sites. No Register form was read (NPGallery unreachable). Not checked: anything on the ground; hours for the Heritage Museum, Hancock House, library and post office (the listings disagree or are old, so `hours='?'` with what they say in the access note); which building is which for the bank, post office, gristmill, Pad Factory and Gilligan block (pins are `site`); parking along the upper end of the river walk; red brick for seven buildings (sources say brick but not its colour). The upper falls pin is the history panel, not a mill (`prec='area'`). The French Lines pin was moved onto the zigzag bank that the LiDAR shows plainly. The Community Building's Wikipedia coordinate is 1.3 km off, at Moses Circle; it is pinned at 132 Montcalm Street, the address the town gives.

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Crandall Marine Railway | Hart (Heart's) Bay, about 3 miles southwest of Ticonderoga village, NY (Wikipedia 43.8075, -73.44861) | Lake George Steamboat Company's 1927 dry dock, Register 2011; head house, tracks and cradle (Wikipedia, lakegeorge.com) | Whether the public can see it, and from where; the company's own page was not read |
| St. Mary's Church and Rectory | 22 Father Jogues Place, Ticonderoga, NY | Register 1988; the parish page (rcdony.org) gives the address only | A description of the building and service times from the parish's own site (southernadirondackcatholics.org, not read) |
| Mount Defiance | Ticonderoga, NY (Wikipedia 43.83145, -73.40679) | Where the British put guns in 1777; road to the summit in season on the fort's ticket (fortticonderoga.org) | Left out: no building or remains named on the summit beyond a picnic pavilion |
| Baldwin Branch of the D&H | Lake George outlet to Baldwin, Ticonderoga, NY (HMdb 158379, 43.83682, -73.43035) | Line of 1874-75 to Baldwin Dock, passengers to 1932, closed to Baldwin 1939, last tracks lifted 1981 | Whether anything of the line or Baldwin station can be seen |
| Ticonderoga High School, Delano House, Burleigh House, Clark House, Ferris House, Amherst Avenue and Lake George Avenue districts | Ticonderoga, NY | Register 1988-89 (Wikipedia) | Left out as houses and a school with nothing more said of them |

## Tips
- From this channel's cloud shell, the map and imagery hosts (orthos.its.ny.gov, ArcGIS, USGS elevation), Wikipedia, Wikimedia Commons and the geocoder all answered; every other web site (dec.ny.gov, npgallery.nps.gov, web.archive.org, fortticonderoga.org, the town's site) was refused by the network, so `page.py` failed everywhere and HMdb answered 403. The web fetch tool read all of them, including HMdb.
- Web search here returned titles and links only, with no quoted text: hours had to be read page by page.
- `smoke.js` could not run: Playwright's browser download is switched off in this environment, and no browser is installed. The phone-size test was left to GitHub's check.
- Register list coordinates in Ticonderoga were off for six of the downtown buildings (the bank and post office share one point on houses 70 to 170 m away); `nom.py` and the ArcGIS geocoder brought them onto the right block.
