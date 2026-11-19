# cny_uznp: Cortland County, NY: Cortland, Homer, Little York, Truxton, Marathon and the Otselic valley
state: New York
region: cny
date: 2026-11-19
places: 21
file: data_cny_uznp.py

## What this batch is
Twenty-one places in Cortland County, New York, drawn at random by `choose.py --state ny` (region `cny`, which offered Homer, Cortland and Phelps); the Atlas had nothing within 15 km of Homer. Nearly all standing. Cortland: the 1890 House Museum (Wickwire mansion), the Suggett House Museum (county historical society), the 1837 cobblestone Unitarian Universalist church, the 1924 courthouse, the Crescent Corset factory (J.C. Penney's corset works, now Crescent Commons; red brick from the Register form), the 1914 fire headquarters and the Randall Farm cobblestone house (private). Homer: the three 1881 lenticular truss bridges, the village green and Old Homer Village district (with the Barber Block / Keator Opera House and the White and Hannum markers folded in) and Glenwood Cemetery. Preble: the 1906 Little York trolley-park pavilion (Cortland Repertory Theatre) and the Preble Congregational church. Truxton: the c. 1872 Lehigh Valley depot (now the town hall). McGraw: the 1901 Presbyterian church and the New York Central College marker (an 1848 college open to all races and both sexes). Marathon: the Peck Memorial Library and the Tarbell Building. Solon: the 1844 Hatheway stone house (event venue, view only). Taylor and Cincinnatus: the Union Valley and Taylor Center churches and Heritage Hall (1832 church). Sources: Wikipedia raw text and the county Register list (`wiki_raw.py`), HMdb marker pages (an 8-mile `nearbylist` round Cortland, Marathon and Truxton gave ~200 markers in three requests), managing bodies' pages with `page.py` (1890 House, cortlandhistory.org, townoftruxton.com, peckmemoriallibrary.org, experiencecortland.com, hathawayhousecny.com), the Cobblestone Museum catalogue, the Crescent Corset Register form, and uucas.org for the cobblestone church's service time (uucortland.org answered 403). Not checked: anything on the ground; most interiors; service times for the Preble, McGraw, Union Valley and Taylor Center churches (all `view`); Heritage Hall's opening times; parking for most of the Cortland and country places; red brick for 14 places (Wikimedia answered 429 on every picture, so `brick.py look` was not used). Pins: Little York pavilion and Hatheway moved with `pix.py` onto the buildings; the Preble church, McGraw church, fire headquarters and Union Valley church stay on the Register or marker point with `prec='site'` because which building is which could not be told on the aerial.

## Leads
Places you read about and could not finish. One row each; delete the example row. Leave the table header.

| Place | Where | What is known | What is missing |
|---|---|---|---|
| Cortland County Poor Farm | Lorings Crossing Road, Cortlandville (Register point 42.62667, -76.13722 falls on a solar farm) | County farm bought 1836; 13 buildings and a block piggery at listing in 1982 (Wikipedia); a 2024 Voices (New York Folklore) article describes a burned wing, Y-shaped main building, barn and schoolhouse off Lorings Crossing Road | The buildings' true position (not found on the aerial), owner, and present state from a second source |
| Stage Coach Inn (Royal Johnson House) | Lapeer (Register point 42.44081, -76.10097 is in an open field) | c. 1830 inn, post office and dance hall with the upstairs hall intact (Wikipedia, Register 09001080) | Street address or true position; private home, view only |
| Town Line Bridge site | Taylor (HMdb 154476, 42.56489, -75.89300) | 1888 Berlin Iron Bridge Co. lenticular truss, demolished August–September 2018 (Wikipedia) | Anything left to see (abutments?) |
| Old Stone Mill site | Virgil, Parker Street and Route 392 (HMdb 226602, 42.49067, -76.09843) | Gaius Rudd's mill 1856, later Angell's or Rockdale Mill, destroyed by flood 1935 (marker) | Any ruin on the ground; owner |
| Brink's Tavern / Three Bear Inn | 3 Broome Street, Marathon (HMdb 131026) | Founded 1799 by Abraham Brink, "forerunner of the present Three Bear Inn" (marker) | Whether the building is the old tavern, and whether it still operates |
| Tannery site | 18 Tannery Street, Marathon (HMdb 264681) | Tannery 1860, rebuilt 1877, chrome tannery closed 1924 (marker) | Anything left on the ground |
| Port Watson | Port Watson Street, Cortland (HMdb 25425) | Elkanah Watson's river port c. 1805: mills, brewery, rope walk, arks sent to Pennsylvania (marker) | Any remains |

## Tips
- `page.py -g` must come before the address: `page.py "<url>" -g '...'` reads the pattern as a second address and errors.
- Wikimedia answered 429 to `brick.py look` on the first try and again after a minute and a half; with an unattended session it was quicker to leave brick at `'?'`.
- NPGallery placeholders here: 82001115, 01001502, 08000930, 02001639, 09001080, 77000938, 10000513, 86002517, 84002208. 16000391 (Crescent Corset, 2016) has full text.
- Register points off the thing in Cortland County: the Poor Farm (on a solar array), the Stage Coach Inn (in a field), Little York Pavilion (on the park road), and the Hatheway marker (on Route 41).
- The federal bridge inventory (bridgelookup.com) gives 1878 for Homer's Wall Street lenticular truss where the Register gives 1881.
- uucortland.org answers 403; its partner church uucas.org gives the joint service time.
