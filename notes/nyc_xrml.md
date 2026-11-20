# nyc_xrml: Long Island: East Hampton, Montauk and Sag Harbor
state: New York
region: nyc
date: 2026-11-20
places: 19
file: data_nyc_xrml.py

## What this batch is
Nineteen places on the South Fork of Long Island, drawn at random by `choose.py --state ny` (region `nyc`); `start.py` showed no Atlas place within 25 km of East Hampton or Sag Harbor. Nearly all standing. Montauk: Camp Hero and its AN/FPS-35 radar tower, Montauk Point Lighthouse, the World War II bunkers at Shadmoor State Park, Second House. East Hampton village: Hook Windmill, Home Sweet Home with the Pantigo Windmill, Mulford Farm, the Gardiner Windmill, Clinton Academy with the Town House, the Moran house and studio, the 1895 railroad station. Amagansett: Miss Amelia's Cottage. Springs: the Pollock-Krasner House. Northwest Harbor: Cedar Island (Cedar Point) Lighthouse. Sag Harbor: Old Whalers' Church, the Whaling Museum (Huntting House), the Custom House, and the Round Pond ice house site on the old rail spur in the Long Pond Greenbelt. Bridgehampton: the Beebe Windmill. Sources: Wikipedia and the Register lists for the towns of East Hampton and Southampton (`wiki_raw.py`), and with `page.py` the pages of NYS Parks, Suffolk County Parks, the Village of East Hampton, the East Hampton Historical Society, the whaling museum, Preservation Long Island, Old Whalers' Church, Stony Brook's Pollock-Krasner page, the Amagansett Historical Association and southamptontrails.org, plus the East Hampton Star, Patch and aaqeastend.com. Not checked: anything on the ground; interiors except where a source describes them; hours for Montauk Point Lighthouse (its site would not open), Hook Windmill (only 2012 hours found), Second House and Miss Amelia's Cottage (no hours on their pages); who owns the Beebe Windmill now; parking at Shadmoor, Second House, Pollock-Krasner and the village sites. Pins that are not on the thing itself: Shadmoor is on one squared structure taken to be a bunker from the aerial and LiDAR, not from a source; the Round Pond ice house pin is an OpenStreetMap ruin point, and no source describes what is left; Mulford Farm is a street-address match beside the buildings. Red brick was settled only for the station (yes, Wikipedia photo) and Montauk Point Light (some: painted tower, red brick chimneys on the keeper's house, Wikipedia photo); the rest are `?`.

## Leads
Places you read about and could not finish. One row each. Leave the table header.

| Place | Where | What is known | What is missing |
|---|---|---|---|
| Third House (Theodore Roosevelt County Park) | Montauk, NY (Deep Hollow, about 41.05, -71.89) | Montauk Historical Society page: once Further House, rebuilt 1806, keeper watched cattle in the Fatting and Outer Fields | The county park page read gave no Third House text; a source for what stands and when it opens, and a pin |
| Camp 5 Building (ruins) | Northwest Woods, East Hampton, NY (OSM 41.02506, -72.21582, on East Hampton Town Lands) | Leads layer point only | Anything: what Camp 5 was, a source, a trail in |
| Trout Ponds ruins | Noyack, NY (OSM 40.9896, -72.3491) | Leads layer point only | Anything |
| Montauk Manor | Montauk, NY (41.04833, -71.94972) | Wikipedia: 1926 Tudor Revival resort hotel by Carl Fisher, designed by Schultze and Weaver; now a condominium hotel | The hotel's own page for whether the public rooms open to non-guests |
| Montauk Point Lighthouse hours | Montauk, NY | Entry added with hours='?' | montauklighthouse.com: try in an attended session |
| Wainscott, Hayground and Gardiners Island windmills; Thomas Strong House; Sagaponack district | Town of East Hampton and Southampton | Register rows in the town lists | Owner and whether they can be seen from a public road; Gardiners Island is private |
| Fort Terry and Fort Michie | Plum Island and Great Gull Island, NY (41.18, -72.19; 41.20, -72.12) | Leads layer and federal names file show the batteries | Plum Island is federal and closed; Great Gull is a bird research island: likely boat view only, needs a source |

## Tips
- montauklighthouse.com refuses `page.py` (connection error) and the web fetch tool (robots.txt unreachable); montaukhistoricalsociety.org answers 403 to `page.py` but the web fetch tool read it (its home page is out of date: it still speaks of reopening Second House in 2023).
- easthamptonhistory.org/visit-us/ reads well with `page.py` and lists the society's open days and tours for the month; its property pages (`/mulford-farm/`) are drawn by script, but `/clinton-academy/` reads in full.
- The Village of East Hampton's pages read at `easthamptonvillage.gov/<page>/` (home-sweet-home); the old `.org` address of the historic services page also reads. Guessed pages for the mills there answer 404.
- `brick.py look` timed out after two minutes on one place (Wikimedia was slow): give it a longer timeout, one place at a time.
- Web searches in this run returned titles and links only, no quoted text, so hours could not be taken from search results.
