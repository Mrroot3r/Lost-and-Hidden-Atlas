# pe_eawz: Summerside, Prince Edward Island
state: Prince Edward Island
region: pe
date: 2026-11-20
places: 19
file: data_pe_eawz.py

## What this batch is
Nineteen places in Summerside, which had only the Indian Head light on the map: City Hall (the 1880s Fuller post office), the 1911 armoury (now the Summerside Interpretive Centre and PEI Fox Museum), the 1873 law courts, the three Wyatt Heritage Properties (Wyatt House Museum, Lefurgey Cultural Centre, MacNaught History Centre), Bishop's Machine Shop Museum, the Holman Homestead, four churches and the former Church of Scotland "Kirk", the 1895 back range light, the Crockett-Gallant commercial block, the ballast-stone Bowness House, the first convent school, Memorial Square with the drill shed site, and the 1927 CNR station. Histories come from the Canadian Register statements (historicplaces.ca, read with `page.py --all`, ids from the `{{HPC row}}` templates of Wikipedia's Summerside list); museum hours and histories from Culture Summerside's own pages (culturesummerside.com); Anglican service times from the Parish of St. Mary & St. John's own page; the station's later story from HMdb 141017 and CBC (2017). Red brick for St. Mary's, Crockett-Gallant, Holman and Lefurgey from the Register's own photographs (`brick.py look` on the page's `hpimages/Thumbnails/<n>_Medium.jpg`). Not checked: Trinity United and the Baptist church have no page of their own that was found, so no service times; City Hall's office hours; the Holman ice cream parlour's hours; the station's owner and use since the city offered it for sale in 2017; whether Crockett's still trades. Bishop's Machine Shop has two addresses on the city's own site (71 Spring Street on its page, 101 Water Street on the summary page); the pin follows the first and OpenStreetMap. The Wyatt House was "closed for maintenance" on Culture Summerside's page in November 2026. Bowness House and the Parish School pins are on the Register list point among several houses (`prec='site'`). Nothing was checked on the ground.

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Patrick Fanning House (Summerside Inn) | 98 Summer Street, Summerside, PE (46.3953, -63.7903 Register list) | Register 1650: Queen Anne house of 1891 for the merchant P. T. Fanning; home of premiers Thane and Alex Campbell; "now an inn" in the Register statement | Whether it is still an inn; a page of its own |
| R. T. Holman store building | 250 Water Street, Summerside, PE | Register 16273 (Holman Homestead statement): Holman's three-storey brick store of 1895, joined to his 1874 four-storey brick warehouse in 1919 as the Holman Department Store | A source of its own and its present use |
| Summerside Register houses | Summerside, PE (Spring, Central, Granville, Notre Dame streets) | About 70 more Register rows, most of them houses named for their builders | Read the statements; a `town` entry for the Spring Street heritage district could hold them |

## Tips
- In Summerside the Register list point was within 20 m of the building for most places, but the PEIR Armoury's fell about 120 m away on a lot and Trinity United's 40 m off; `osmnear.py <lat> <lon> 250 buildings` listed the named buildings (museum, city hall, ice cream parlour, station with its 1927 start date) and settled both.
- The historicplaces.ca photograph number is not the place id: `grep -o 'hpimages/Thumbnails/[0-9]*_Medium.jpg'` in the cached page; asking for `<place id>_Medium.jpg` gave a 404 or, for Lefurgey, somebody else's building.
- historicplaces.ca answered all 24 pages with a 2-second pause and no resets this time.
- The City of Summerside's own site (summerside.hosted.civiclive.com) answered 403 to `page.py` with no archived copy; culturesummerside.com, the city's culture department, read in full and gives hours for every city museum on its "at a glance" page (`/copy-of-what-s-on`).
- `choose.py --claim --state qc,nb,ns,pe,nl` accepted the comma list this time.
