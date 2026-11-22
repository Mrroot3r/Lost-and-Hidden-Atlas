# ab_yknm: Alberta from the Peace to Waterton: elevators, creameries, courthouses and a gas plant
state: Alberta
region: ab
date: 2026-11-22
places: 14
file: data_ab_yknm.py

## What this batch is

Fourteen places spread across Alberta, the province with the fewest places on the map when this session began (32 before, 46 after). From the Peace River country: the Hudson's Bay Company Factor's House at Fort Vermilion and St. Bernard Mission at Grouard (its 1902 church was burned by arson in May 2023; the entry is written as the bishops' cemetery and the burned church). The parkland: Alberta Hospital Building No. 1 (Ponoka), the Old Red Deer Courthouse, the Markerville Creamery, the Diplomat Mine strip-mining machines near Forestburg, and the Rowley grain elevator row. Foothills and mountains: the Turner Valley Gas Plant, the Canmore NWMP Barracks, Cave and Basin (Banff), the Jasper railway station and the Prince of Wales Hotel (Waterton). The south: the Sir Alexander Galt Hospital (Galt Museum, Lethbridge) and the Cardston Courthouse.

Sources: the Canadian Register of Historic Places statement for every place, read whole with `page.py --all -n 60000` (register ids from the `{{HPC row}}` templates of Wikipedia's Alberta historic-place lists); Wikipedia raw text (Grouard, Bad Heart); CBC News and the Catholic Register for the Grouard fire; and the operator's own page for hours (Parks Canada for Cave and Basin, the Galt Museum, the Cardston & District Historical Society, Historic Markerville, rowleyalberta.ca, the Glacier Park Collection, and the Government of Alberta's 2024 historic-sites brochure for Turner Valley).

Not checked: the days and times at the Turner Valley Gas Plant (only "May long weekend to Labour Day"), the Canmore NWMP Barracks (hours `?`), the Prince of Wales Hotel's exact season dates, and who runs the Diplomat Mine interpretive site (left `view`). Whether the burned shell of St. Bernard's church at Grouard still stands after June 2025. Ownership and visiting of the Fort Vermilion Factor's House. Red brick is `?` for the Galt Hospital, the Cardston Courthouse, Grouard, Fort Vermilion and Turner Valley (no source gives the colour). Pins moved onto what the aerial shows: Rowley (500 m), Turner Valley (750 m), Cave and Basin, the Prince of Wales Hotel (650 m) and the Galt. Grouard, Ponoka and Cardston pins are near but not confirmed on the building.

## Leads

| Place | Where | What is known | What is missing |
|---|---|---|---|
| Bad Heart Straw Church | Near Teepee Creek, AB (Register 55.485, -118.288; Wikipedia's Bad Heart 55.49611, -118.2825) | 1954 straw-bale church by Fr. Francis Dales, Provincial Historic Resource 2009 (Register 11819); Wikipedia: closed 1960, refurbished 1985, municipal historic resource 2010 | The Register point is an empty field on the aerial; the church could not be found. A position and the owner |
| Ukrainian Greek Orthodox Church of St. Mary (Szypenitz) | Near Hairy Hill, County of Two Hills, AB (Wikipedia 53.7715, -111.8547) | 1917 brick Bukovynian church with a Lapinski-painted interior, Register 5063 | Wikipedia's point is in a marsh; the church could not be found on the aerial. A position |
| Turner Valley Gas Plant hours | Diamond Valley, AB | Seasonal, May long weekend to Labour Day (2024 brochure) | turnervalleygasplant.ca/visit answered 404; days and times |

## Tips

- historicplaces.ca reset the connection on 3 of 18 requests fired six at a time; one at a time with a 2-second pause they all read.
- Register list coordinates in rural Alberta were off by 500 to 750 m for Rowley, Turner Valley and Waterton, and in empty fields for Bad Heart and Szypenitz; `nom.py` found the Turner Valley Gas Plant's industrial area, and `look.py` at 250 m then showed the plant.
- At Rowley the wooden elevators show on the aerial mainly as long dark shadows beside the rail bed.
- canmoremuseum.com's barracks page answered 404 and its main page gives no barracks hours; flagstaff.ab.ca pages from search results answered 404; albertawow.com now serves a casino page.
- `photo_find.py look` hung on Wikimedia Commons twice (over twenty minutes for five places, then nothing in four minutes for two). Four places were settled from the candidate lists (two none, the Red Deer courthouse given its at-the-pin photograph named for it, whose sheet never drew); Markerville, Rowley, Turner Valley, Canmore, Jasper, the Galt and Cardston were not looked for and still wait for the pictures job.
