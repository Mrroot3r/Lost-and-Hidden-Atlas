# kcmo_weston_afuv: Weston and Platte City, Missouri
state: Missouri
region: kcmo
date: 2026-11-23
places: 15
file: data_kcmo_weston_afuv.py

## What this batch is
Fifteen places in Weston (13) and Platte City (2), Platte County, Missouri, the "Weston and Platte City" part of the Kansas City area. Before this batch the Atlas had nothing within 15 km of Weston. Weston: the historic district and Main Street, the St. George Hotel, the Weston Brewing Company lagering cellars (O'Malley's Pub), the Holladay (McCormick) Distillery, the 1867 German Evangelical Lutheran church that is now Pirtle Winery, the Weston Historical Museum in the 1902 Baptist church, the 1937 tobacco auction warehouse (Missouri District Warehouse), the tobacco barns in Weston Bend State Park, Pleasant Ridge United Baptist Church (1844), Holy Trinity Catholic Church, the old Presbyterian church (now Christian Assembly), the 1868 Methodist church and Laurel Hill Cemetery. Platte City: the 1866–67 courthouse and the Krause mini-mansion (Ben Ferrel Museum). Sources: Wikipedia read with `wiki_raw.py`; Legends of America's Weston pages, the ACHP Preserve America page, the National Trust, Platte County Landmark, Platte County Citizen, Northeast News, KCUR, KSHB, Missouri Wines, Missouri State Parks and DNR, and the distillery's own page, all read with `page.py`. The National Register forms could not be read (see Tips), so "what original fabric survives" is "not checked" for most standing buildings. Not checked: anything on the ground; interiors; owners of the warehouse, Pleasant Ridge church and Laurel Hill Cemetery; service times for the four churches; which of the two park barns is the display barn; whether the courthouse has reopened after its 2025 renovation. Hours came from an owner's page only for the distillery and Weston Bend State Park; the Weston Historical Museum's hours are as web search results quoted its site (its pages answer 403), and the brewery's and Krause Mansion's are given only as dated newspaper reports in the access note (`hours='?'`). Red brick: courthouse and Krause Mansion from Wikipedia's text; St. George Hotel and the Methodist church from the Commons photographs chosen for them; the rest `?` or `no` (Holy Trinity limestone, warehouse corrugated metal). All pins looked at on Esri satellite; three moved (district onto Main Street, Pleasant Ridge onto the churchyard, courthouse onto the building).

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Pleasant Grove Cemetery and the 1871 Camden Point Confederate memorial | Camden Point, Platte County, MO (address range 14151–14199 Pleasant Grove Rd, about 39.4626, -94.7430, not confirmed) | Wikipedia "Battle of Camden Point" and Platte County Citizen (2014): six Confederates reburied in 1871 under a small white obelisk, headstones added 2000, marker at the entrance; Camden Point Baptist Church cares for it | The cemetery could not be found on the aerial at the address point; a mapped position and whether visitors may walk in |
| Weston Presbyterian church bell and Cody house | Weston, MO | HMdb has markers for the Cody House (600 Main), Weston jail, Bechler, Doppler, Kaufmann and other buildings; positions are in `data/pock/mo.json` | HMdb answers 403, so the marker texts could not be read |
| Sugar Creek Site | Weston, MO | National Register 73001050, address restricted | A source saying the public may visit |

## Tips
- HMdb.org answered HTTP 403 to `page.py` for both the nearby list and single marker pages (November 23, 2026). The marker titles and positions for a town are still in `data/pock/<state>.json` (key `m`), which gave the Weston building names.
- Missouri National Register forms: NPGallery holds only placeholders for Platte County, the old `dnr.mo.gov/shpo/nps-nr/<ref>.pdf` addresses answer 503 and the `mostateparks.com/sites/mostateparks/files/<Name>.pdf` addresses web search still lists answer 404. No form could be read.
- `page.py` on PDFs failed until `python3 -m pip install --break-system-packages cffi` (as earlier notes said); Pillow needed `--ignore-installed` for the pin check.
- westonhistoricalmuseum.org, holytrinitycatholic.org, billiongraves.com and rootsweb answer 403; pchs1882.org (Platte County Historical Society) resets the connection.
- mccormickdistilling.com is now the Holladay Distillery site and gives its hours in plain text.
