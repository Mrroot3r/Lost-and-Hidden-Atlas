# ns_dgmr: Nova Scotia: Halifax, Cape Breton, the Valley and the Northumberland shore
state: Nova Scotia
region: ns
date: 2026-11-23
places: 16
file: data_ns_dgmr.py

## What this batch is
Sixteen places in Nova Scotia outside Annapolis and Lunenburg counties, drawn as the province or state with the fewest places on the map (43 before, 59 after): the Halifax Citadel, Prince of Wales Tower, Fortress of Louisbourg, Fort Edward blockhouse (Windsor), Clifton (Haliburton House), Uniacke House, Grand-Pré, Covenanters' Church, Balmoral Grist Mill, Sutherland Steam Mill, the Chignecto Ship Railway terminus, Beaubassin and Fort Lawrence, the Argyle court house (Tusket), Chebogue Meeting House, Cape Forchu light and McCulloch House (Pictou). Sources: Canadian Register of Historic Places pages (read with page.py where the site answered), Parks Canada hours pages for the Citadel, Louisbourg and Grand-Pré, the Nova Scotia Museum's Clifton and Uniacke sites, Wikipedia raw text, the ArcGIS geocoder and OpenStreetMap for positions. Every pin was looked at on the aerial; four were moved (Louisbourg, Clifton, Uniacke, Grand-Pré).
Not checked: nothing was seen on the ground. The Clifton and Uniacke times come from search-result text quoting the museums' pages (the pages themselves showed no clock times). No hours were read for Balmoral, the Argyle court house, Fort Edward, Prince of Wales Tower, the Covenanters' and Chebogue churches. The Sutherland Steam Mill closing is Wikipedia's statement only. Brick is '?' for places where no source or picture settled it. Parking is described loosely; no lot was checked on the ground.

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Grassy Island Fort | Canso, NS (45.3374, -61.0) | National historic site (Register id 11666) | the Register page and Parks Canada page would not open; no source read |
| Sainte-Marie Church | Church Point, NS (44.334, -66.1) | Register id 5390, Digby County | the Register page reset the connection twice; not read |
| Heritage Goldenville Society (former church) | Goldenville, NS | Register id 15156; gold-mining district | only the first part of the page was read; mine ruins not looked into |
| Pictou Iron Foundry, Pictou Academy, Pictou station | Pictou, NS | Register ids 14796, 14445, 7470 | not read |
| Springhill Coal Mining NHS, Joggins | Cumberland County | Register ids 17988, 14787 | not read |

## Tips
- historicplaces.ca reset the connection on about half of the pages even at 5 to 8 second pauses; a second try in a separate run read three more. Pages cut off at `-n 5000` lose the description: use `-n 8000` or more.
- The Wikipedia list's `lat`/`lon` fields hold the Register point: the Argyle court house point was 25 km off (43.5735, -65.7678); the geocoder's PointAddress for the address was right. The Wikipedia point for Uniacke House was 290 m off; OpenStreetMap's was right.
- museum.novascotia.ca pages for single museums answer 404; each museum has its own host (clifton.novascotia.ca, uniacke.novascotia.ca) whose /visit page lists fees but did not show clock times to page.py.
- There is no 1 m LiDAR for Nova Scotia, so the pin check ran on the aerial only.
