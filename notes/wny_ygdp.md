# wny_ygdp: New York: Livingston County and the north end of Letchworth
state: New York
region: wny
date: 2026-11-19
places: 17
file: data_wny_ygdp.py

## What this batch is
Seventeen places in Livingston County, New York (region `wny`, drawn at random by `choose.py --state ny`, which offered Geneseo, Dansville and Batavia); the Atlas had nothing within 30 km of Geneseo. Three Letchworth State Park sites just over the line in Wyoming County are filed under `wny` too. Ruins and traces: the Jackson Sanatorium ("Castle on the Hill", Dansville, private, view only), the Genesee Valley Canal locks at Oakland, the Gibsonville CCC camp chimney, the drowned hamlet of St. Helena (gone, marker and trail). Standing: the Avon Five Arch Bridge, the Caledonia fish hatchery (1864, still working), the Seneca Council House and Nancy Jemison cabin, the Mount Morris Dam, the 1838 cobblestone school (county museum), the Kellerman log cabin (1816), Conesus Amusement Hall, St. Paul's Lutheran in Dansville (Clara Barton's Red Cross chapter), the Leicester DL&W depot, Genesee Wesleyan Seminary and College Hall in Lima, the National Hotel at Cuylerville. Markers: Groveland Ambuscade Park and Boyd & Parker Park. Sources: Wikipedia via `wiki_raw.py` (the county Register list with `--rows`), HMdb nearby lists round six towns and the marker pages (texts and positions), DEC's hatcheries page, NYS Parks pages for Letchworth and the Greenway, recreation.gov for the dam, the Village of Avon and Avon Preservation pages, the Dansville library's Castle page, the county historical society and chamber pages. Not checked: anything on the ground; which lock chambers survive at Oakland (pin is the trail marker, `prec='area'`); the sanatorium's present condition beyond "privately owned"; present use of the National Hotel and the Leicester depot; owner of Groveland Ambuscade Park (marked view-only); Letchworth's entrance fee amount; hours of the Avon park, Boyd & Parker Park and the Kellerman cabin park. The Genesee Wesleyan pin is on the lawn between campus buildings. Brick from Wikipedia photographs for the Leicester depot and College Hall; the sanatorium is called brick by the Dansville library but its colour was not seen.

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Nunda canal locks and 1870 canal warehouse | Nunda, NY (17 Locks marker 42.57846, -77.94779) | HMdb marker: 17 locks lifted the Genesee Valley Canal over the hill to Portage; the Friends of the Genesee Valley Greenway's 2023 walk visited three lock sites, a footbridge and "an existing 1870 canal warehouse" in the village | Where the warehouse is, and whether any lock stone shows; Nunda Historical Society at 24 Portage Street |
| Genesee Valley Canal and railroad remnants, Letchworth Trail 7 | Letchworth State Park, east rim (marker across the gorge 42.58837, -78.03563) | HMdb 76061 says remnants of both can be seen on Trail #7 | A trail map or source placing the remnants |
| Livingston County Poorhouse | Geneseo, Lakeville Road at Millennium Drive (42.79668, -77.79061) | HMdb 176863: established 1829; buildings on the site 1850–1879; residents moved out 1964 | Whether any building stands, and who owns it |
| Murray Hill (J. R. Murray mansion and state TB hospital) | Mount Morris (42.73151, -77.88449) | HMdb 181999: mansion about 1839, state TB hospital 1936, county offices since 1971 | Which old buildings survive |
| Craig Colony / Groveland Shaker village | Sonyea, Groveland (Black and White Farm Barn, Register 42.666111, -77.808333) | Wikipedia: Shaker village 1836–1892, then Craig Colony for Epileptics 1896–1968; now Groveland Correctional Facility | Whether anything can be seen from a public road; prison land |
| Hemlock Fairground grandstand | Hemlock (42.79361, -77.61111) | Wikipedia: Register district, grandstand 1870, fair in the last week of July | The fair's own page for dates and access outside fair week |

## Tips
- In Livingston County the HMdb nearby lists (5 miles round Geneseo, Mount Morris, Nunda, Dansville, Avon and Caledonia) gave a position and a text for nearly every place; one more round the Council Grounds (1 mile) gave all the Letchworth markers.
- `geo.py` reads a JSON object (`{"key":"address"}`) and needs an output file as a second argument; given "30 Center Street, Geneseo, NY 14454" it returned an address in Lee, Massachusetts. `osmnear.py <lat> <lon> 150 buildings` put the museum and the Conesus town hall on the right building instead.
- army.mil and dvidshub.net (Mount Morris Dam season articles) answer 403 to `page.py`; recreation.gov's tour page reads and gives the season and that the outdoor area is open year-round.
- `parking.py` maps no lot at the Avon Five Arch Bridge or at Groveland Ambuscade Park.
