# adk_gvry: Champlain shore: Keeseville, Valcour Island, Plattsburgh and Essex
state: New York
region: adk
date: 2026-11-18
places: 17
file: data_adk_gvry.py

## What this batch is
Seventeen places on the Champlain shore of Clinton and northern Essex counties, drawn at random by `choose.py --state ny` (region `adk`, which offered Keeseville); the Atlas had one place within 20 km of Keeseville and none round Plattsburgh. Keeseville: the 1843 Stone Arch Bridge, the 1888 Swing Bridge and the closed Upper Bridge (Pratt truss, 1877 or 1878). Ausable Chasm: the US 9 arch, the old railroad bridge foundations and the 1890 Old State Road pony truss, as one place. Port Kent: the Elkanah Watson House (private, view only). Peru: the 1836 Heyworth–Mason stone mill in the town park. Valcour Island (boat only, DEC Forest Preserve): Bluff Point Lighthouse, the Seton Stone House (closed), and three ruin sites from the CCHA heritage trail guide (Raboff camp, the Dawn Valcour commune and Harney farm foundations, the Hudson chimney). Plattsburgh: the Kent-Delord House Museum and the Old Stone Barracks (now Valcour Brewing). Essex County: the Poke-O-Moonshine fire tower, the Adsit Log Cabin, the Octagonal Schoolhouse at Boquet and Essex village (area pin). Sources were read with `wiki_raw.py` and `page.py`: Wikipedia, ASCE's Bridges of Keeseville landmark page, the 2020 Valcour Island Heritage Trail guide (PDF with GPS waypoints), DEC's Lake Champlain Islands Complex page, the CCHA events page, the Kent-Delord House, Valcour Brewing, Ausable Chasm, Protect the Adirondacks, Passageport, Town of Essex and LCBP wayside-sign pages, and a 2021 change.org update for the Upper Bridge. Every pin was looked at on the leaf-off aerial and the LiDAR sheet; the Stone Barracks pin was moved 21 m onto the building, and the Upper Bridge and Hudson chimney were set to `prec='site'`. Not checked: nothing was seen on the ground; whether the Upper Bridge has reopened since 2021; the Valcour ruins' exact spots (guide waypoints only; the LiDAR showed a low mound only at the Dawn site); the Old Stone Barracks' business hours and which lots its visitors may use; the Octagonal Schoolhouse's opening; parking at the Kent-Delord House and the Adsit Cabin; the Adsit Cabin hours come from Passageport, not the town. The US 9 Ausable Chasm bridge has two dates (1932–1933 on Wikipedia, 1925 from the chasm company) and the Adsit Cabin two (1778 or soon after 1790); both entries say so and are `conf='mixed'`.

## Leads
Places you read about and could not finish. One row each; delete the example row. Leave the table header.

| Place | Where | What is known | What is missing |
|---|---|---|---|
| Gill Farm and Camp Penn, Valcour Island | Peru, NY (guide waypoints near N44 37.2 W73 25.4) | The CCHA Valcour Island Heritage Trail guide (2020) lists the Gill Farm (well, house and barn foundations, an old truck) and the Camp Penn dining hall and commons sites | The guide's waypoints are printed out of order beside their labels; which waypoint belongs to which site needs the CCHA's own waypoint list (an archived clintoncountyhistorical.org page) |
| Clintonville ironworks | Clintonville, Town of Au Sable, NY (Pomeroy marker at 44.46647, -73.57683, HMdb 137824) | The Peru Iron Company (1824) built the village; by 1845 it made 1,800 tons of horse nails a year (Clinton County Historical Association) | Any source saying what is left on the ground (forge, dam, kilns) and who owns it |
| Ausable Horse Nail Works | Keeseville, NY | Ran 1863 to 1925 (Wikipedia, Keeseville); 54 machines and 1,000 tons a year by 1880 (CCHA) | Where it stood and whether anything is left |
| Miller Homestead | Au Sable, NY (44.52389, -73.56111) | 1822 stone house with barn foundation remains; Wikipedia says it is a local history museum | Who runs it now and when it opens; no current page was found |
| Keeseville Historic District | Keeseville, NY (44.504444, -73.482778) | National Register district (83001666) with Rembrandt Hall and the Tomlinson House listed beside it | The Register form came back as the NPGallery placeholder; needs a source describing the buildings |

## Tips
- NPGallery `_text` for every Keeseville and Ausable River bridge form (99001319, 99001322, 99001323, 83001665) is the one-page placeholder, as the Herkimer County note found.
- The Valcour Island Heritage Trail guide PDF (champlainvalleynhp.org) prints each GPS waypoint just before its caption, not after; OpenStreetMap's "Seton House" building confirmed that order.
- The National Register coordinate for the Poke-O-Moonshine fire tower (44.38778, -73.50806) is at the road by the trailhead, not on the summit.
- Wikipedia's Kent-Delord House coordinate is about 450 m west of the museum; `nom.py "Kent-Delord House, Plattsburgh"` gives 17 Cumberland Avenue.
- `places_test.js` fails on main as found (3 failures): "Standing, from before 1800" lists `onesquethaw-valley` (data_albco_kaom.py), whose years are "18th century". This batch changes nothing it reads.
- townofausableny.gov answers 403 to `page.py` with no archived copy; the DEC page `dec.ny.gov/places/valcour-island-primitive-area` is 404, but `dec.ny.gov/places/lake-champlain-islands-complex` has the Valcour rules.
