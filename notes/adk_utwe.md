# adk_utwe: Iron towns of Moriah and Crown Point, with Westport and Elizabethtown
state: New York
region: adk
date: 2026-11-19
places: 16
file: data_adk_utwe.py

## What this batch is
Sixteen places in central Essex County, New York (region `adk`, drawn at random by `choose.py --state ny`, which offered Westport); the Atlas had four places within 15 km of Westport and none in Port Henry, Mineville, Witherbee or Elizabethtown. Most of the batch follows the iron industry of Moriah and Crown Point. Port Henry: the 1888 D&H depot, the Iron Center Museum beside the 1875 Witherbees, Sherman & Co. office (Moriah Town Hall), the Sherman Free Library, the Mount Moriah Presbyterian Church and Powerhouse Park (furnace and power-plant ground). Mineville and Witherbee: Memorial Hall with the company headquarters and hospital above it, the tailings-concrete houses of Bridal Row, and the Belfry Mountain fire tower. Moriah: the Colburn blast furnace ruins (private, view from the road). Crown Point: the Crown Point Iron Company's furnace site at Monitor Bay and the Crown Point green. Westport: the 1876 depot (Depot Theatre), the 1928 Lake View Grange (town hall) and the 1837 Wadhams meeting house. Elizabethtown: the old Essex County courthouse (John Brown lay there in 1859) and the Hand and Hale houses. Sources: Lakes to Locks Passage's "Story of Iron in Crown Point & Moriah" tour pages (passageport.org, read with `page.py --all`, cutting at "Henniker, NH"), Wikipedia through `wiki_raw.py`, three Register forms NPGallery has as text (13000626, 15000231, 16000224), the Town of Moriah's page, Protect the Adirondacks and an Adirondack Explorer article. NOT checked: anything on the ground; hours of the library, town halls, county buildings, churches and the Depot Theatre; day-use rules at Monitor Bay Park (a municipal campground); who owns Powerhouse Park beyond the DEC boat launch; whether the Belfry tower cab is open; the current state of the Hale House work. The Iron Center's hours differ between Lakes to Locks Passage (Thu–Sat noon–3, mid-June to mid-October) and the town's page (call first; volunteer-run): both given. The Colburn furnace pin is on the road beside it (LiDAR shows a mound just south); Monitor Bay's pin is on the pier, not the rubble bank south of it; Bridal Row and the Hand–Hale pins are on the street. Brick: two depots settled from Wikimedia photographs (both `no`); seven places are `?`.

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Fletcherville furnace and hamlet | Moriah, NY, off Bartlett Pond Road | Lakes to Locks Passage site 14: last charcoal blast furnace in Essex County (1864–65, 42 ft granite, ten rectangular kilns); the site is overgrown, and the Champlain Area Trails Mountain Spring Road trail runs through it | Whether anything stands on the trail, a coordinate, CATS trail page |
| Cedar Point furnace site | Port Henry, NY (Van Slooten Harbor Marina, about 44.0417, -73.4572) | Site 27: only the tailings-concrete warehouse, now the marina's, remains of the 1875 furnace and Republic Steel's Mill #6 | Who owns the marina ground and whether visitors may walk there |
| White Church | Moriah, NY, Treadwell Road and White Church Road | Site 9 names the church and cemetery as a tour stop | Its date and any history: the page tells only the road's story |
| Westport Historic District | Westport, NY (44.1834, -73.4338) | Listed 2021, 303 contributing buildings | The form (NPGallery returned nothing) |
| Wadhams Grange Hall | 774 NY 22, Westport, NY | Listed 2024 | The form (NPGallery returned nothing) |
| First Congregational Church and Cemetery, Lewis | Lewis, NY (44.2778, -73.5681) | Register listing 04001457 | The form is the NPGallery placeholder; no other source found |
| Henry's Garage (Port Henry fire station) | Port Henry, NY | Site 24: 1911 tailings-concrete garage with a car elevator, fire station since 1971 | Its address or a coordinate on the right building |
| Hammondville furnace and slag pull-off | Hogback Road, Crown Point, NY | Site 7: slag pull-off on the road; the furnace (1846–1870) is across the road on private land | Hammondville is already in the Atlas (`hammondville`); a coordinate for the pull-off would let that entry gain a th= point |

## Tips
- The Lakes to Locks Passage tour pages (`passageport.org/journey/<tour>/<n>-<slug>/`) read in full with `page.py --all -n 40000`; the article starts after "Henniker, NH" in the text, and each page's "Travel Tools" paragraph gives parking, ownership and sometimes a coordinate (the Colburn furnace's).
- A web search for "Elizabethtown walking tour" brought up Elizabethtown, Kentucky's brochure first.
- NPGallery placeholders here: 95000593 (Port Henry depot), 88002750, 05000993, 93001136, 04001457; 100006513 and 100009879 return 893 characters of nothing (not named as a placeholder by `page.py`).
- `adkhistorycenter.org` and `porthenrymoriah.com` would not connect to `page.py`; `shermanfreelibrary.org` returned no text.
