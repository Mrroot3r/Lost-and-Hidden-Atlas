# mohw_akpe: Utica, New York
state: New York
region: mohw
date: 2026-11-21
places: 19
file: data_mohw_akpe.py

## What this batch is
Nineteen standing places in Utica, with one each in Whitesboro and New Hartford (region `mohw`, drawn at random by `choose.py --state ny`, which offered Dolgeville, Utica and Roseboom; Utica had nothing on the Atlas within 13 km, and a lead row asked for "a session of its own"). Utica: Old Main of the Utica State Hospital (1843), Union Station (1914), the Stanley Theatre (1928), Fountain Elms at the Munson, Grace Church, St. Joseph & St. Patrick, the Rutger Park mansions (Conkling House and Munn's Castle), the public library, the Globe Woolen mills, the F.X. Matt brewery, Forest Hill Cemetery, the Oneida County History Center (former Christian Science church), First Presbyterian (Cram), Tabernacle Baptist, Calvary Church, the Uptown Theatre and the Pirnie federal building. Whitesboro: the 1807 Whitestown Town Hall. New Hartford: St. Stephen's (1825). Sources: Wikipedia read with `wiki_raw.py` and the Oneida County Register list with `--rows`; Great American Stations; the Munson's, Grace Church's, St. Joseph & St. Patrick's, the library's, saranac.com's and Forest Hill Cemetery's own pages; the Landmarks Society of Greater Utica; Mohawk Valley Museums (for the History Center's hours, since the society's own site is drawn by script); a 2026 Governor's office release on the psychiatric campus; Spectrum News 2017 on the Globe mill. Pins from the ArcGIS geocoder's PointAddress results, all looked at on the aerial; four Wikipedia points were off the building and were moved (Globe mill, Pirnie building, Whitestown Town Hall, St. Stephen's). Not checked: nothing on the ground; interiors of almost all; service times for First Presbyterian, Tabernacle Baptist, Calvary (now the Cathedral of the Theotokos) and St. Stephen's; Union Station's and the Stanley's opening hours (left `?`); whether the Globe mill loft conversion is finished, and which of the buildings by the pin are the mill (pin is `area`); exactly which building at the Munson is Fountain Elms (pin is on the museum, `site`); the History Center building's date. Red brick was set from Wikimedia photographs opened with `brick.py look` for nine places and from Wikipedia's text for four; six are `?`.

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Enlarged Erie Canal aqueduct over Oriskany Creek | Oriskany, Town of Whitestown, NY (OpenStreetMap ruin, 43.15628, -75.32998) | Mapped as "Enlarged Erie Canal Aqueduct" | Any written source on what stands; eriecanal.org has no page for it (OriskanyCreek.html and Oriskany.html are 404) |
| Bagg's Square East Historic District | Utica, by Union Station (Register 43.1030, -75.2233; 100001362) | Register list: buildings that served canal and railroad traffic, late 19th to mid-20th century; the Doyle Hardware, Hurd & Fitzgerald, Daily Press and Hieber (Children's Museum) buildings are listed separately nearby | A source on which buildings stand and are worth a stop; no Wikipedia article |
| Utica Steam and Mohawk Valley Cotton Mill; Avalon Knitting Mill; Byington Mill | Utica (Register 43.1027, -75.2387; 43.0998, -75.2140; 43.1024, -75.2216) | On the Oneida County Register list, no articles | Present use and a source |
| Middle Mill Historic District | New York Mills (Wikipedia 43.105, -75.29278) | Wikipedia: Mill No. 2 complex, two churches, workers' rows and a commercial block, 31 buildings, listed 1976 | Whether the mill stands and what it is now |
| Utica Armory | Utica (Wikipedia 43.07972, -75.20917) | Wikipedia: 1930, William Haugaard, Tudor towers and a drill shed | Present use and owner |
| Memorial Church of the Holy Cross | 841 Bleecker Street, Utica | Wikipedia: 1891 High Victorian Gothic, now a Ukrainian Orthodox church | Not looked at on the aerial; service times |

## Tips
- In Utica, Wikipedia and Register points are often a block off (Pirnie building 180 m, Globe mill among houses); `geo.py` with house number and ZIP landed on the building every time.
- A Commons photograph description gave the Matt brewery's address as 811 Edward Street; do not confuse it with 811 Court Street, which a rental listing gives for the Lofts at Globe Mill.
- oneidacountyhistory.org is drawn by script; mohawkvalleymuseums.us has its hours. thestanley.org has no hours page (box-office and visit addresses are 404). amtrak.com station pages answer 403; greatamericanstations.com reads in full.
- munson.art/plan-your-visit reads with `page.py --all` (the matching-lines mode returned nothing) and gives the museum hours.
