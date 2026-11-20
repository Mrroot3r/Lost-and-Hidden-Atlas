# ab_klbx: Across Alberta: missions, fur posts, mines and mansions
state: Alberta
region: ab
date: 2026-11-20
places: 16
file: data_ab_klbx.py

## What this batch is
Sixteen places spread across Alberta outside the Crowsnest Pass (Alberta had 16 before, all in the southwest; now 32): the Father Lacombe Chapel (St. Albert, 1861), Rutherford House (Edmonton), Victoria Settlement (Fort Victoria, near Smoky Lake), Lac La Biche Mission, the Rocky Mountain House fur-trade forts and their two chimneys, Stephansson House (Markerville), the Brazeau Collieries minesite (Nordegg), the Big Valley station and roundhouse ruins, the Atlas Coal Mine (East Coulee), the Star Mine Suspension Bridge (Rosedale), the Brooks Aqueduct, Medalta Potteries (Medicine Hat), the Lethbridge Viaduct, the Bar U Ranch, Lougheed House (Calgary) and Historic Dunvegan (Peace River). Facts come from the Canadian Register statements on historicplaces.ca (read with `page.py --all`; the ids from the `{{HPC row}}` templates in Wikipedia's Alberta lists), Wikipedia raw text, and for hours the operators' own pages (Government of Alberta site pages, Arts and Heritage Foundation of St. Albert, laclabichemission.com, atlascoalmine.ab.ca, medalta.org, Clearwater County, canadiannorthern.ca, lougheedhouse.com, the City of Lethbridge) and Parks Canada's 2025 Rocky Mountain House activity guide PDF. Not checked: Bar U hours and admission (Parks Canada pages would not open; `hours='?'`); Brooks Aqueduct hours (its page gives none); Star Mine bridge parking and owner beyond Wikipedia; most parking; nothing seen on the ground. Victoria Settlement is pinned at area precision on Wikipedia's point (river-bank trees); Rocky Mountain House is pinned on the visitor centre, not the chimneys. Several season dates are from 2025 pages (Stephansson House, Rocky Mountain House). Medalta's closing year disagrees between the national (1954) and provincial (1958/1966) statements; both given, `conf='mixed'`. Red brick: Rutherford House from the Register, Medalta from the Wikipedia photograph of the kilns.

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Fort George and Buckingham House | Near Elk Point, AB (53.862, -110.757 from Wikipedia) | North West Company and Hudson's Bay posts of 1792–1800, interpretive centre since 1993 (Wikipedia) | The operator page (elkpoint.ca directory) answered 404; no hours, access or what is visible on the ground |
| Cave and Basin | Banff, AB | National historic site; Register ids 3088 (bathing pavilion) and 7567 | Parks Canada pages would not open from here; not read |
| Frog Lake | Near Frog Lake, AB (53.8312, -110.3587 from the Register list) | National historic site, Register id 18201 | Statement not read; access and what remains not checked |
| Markerville Creamery | Markerville, AB | Register id 8453 (provincial) | Statement and operator page not read |
| St. Charles Mission church and rectory | Dunvegan, AB | Stand beside Historic Dunvegan (Register statement 8769); shown on the site's tours (Wikipedia) | Their own dates and fabric not read |

## Tips
- parks.canada.ca and pc.gc.ca refused every connection from `page.py` (archived copies only, which need the web fetch tool). Parks Canada's brochure PDFs on `pcweb2.azureedge.net` (found by web search) read fine with `page.py` and give hours, fees and trail maps.
- Government of Alberta historic sites each have their own site (`<sitename>.ca/visit`: rutherfordhouse.ca, stephanssonhouse.ca, victoriasettlement.ca, historicdunvegan.ca, brooksaqueduct.ca) that `page.py --all` reads cleanly. historicdunvegan.ca also keeps an old "site closure" page that contradicts its visit page.
- The ArcGIS geocoder returned three different POI points (kilometres apart) for "Victoria Settlement Provincial Historic Site"; none could be trusted.
- The pin check's CHECK ACCESS lines are expected for every Canadian place (there is no public-land map for Canada); answer them in the access note.
