# nb_albert_acoa: Albert County, Dorchester and Sackville, New Brunswick
state: New Brunswick
region: nb
date: 2026-11-20
places: 20
file: data_nb_albert_acoa.py
tidied: 2026-11-26

## What this batch is
Twenty places in southeastern New Brunswick, where the Atlas had nothing between Moncton and Fort Beauséjour. Albert County: the old shiretown at Hopewell Cape (Albert County Museum: the 1845 gaol, tax and records offices and the 1904 courthouse), the Albert Mines albertite site (private, look from the road), the Steeves House museum, the New Brunswick Railway Museum and the Albert Manufacturing Company's 1907 red-brick office with the gypsum mill buildings in Hillsborough, the Riverside Consolidated School and Victoria Manor at Riverside-Albert, Coverdale United Church, Cape Enrage Lighthouse, and the Fundy National Park headquarters building and saltwater pool at Alma. Westmorland County: Keillor House, the St. James Textile Museum (Saint James Presbyterian Church), the Bell Inn, Rocklyn and the penitentiary in Dorchester; the Campbell Carriage Factory, the Boultenhouse Heritage Centre, the Intercolonial station and the Sackville Harness shop in Sackville. Sources: the Canadian Register statement for 18 of them (historicplaces.ca with `page.py --all -n 60000`; every page read on the first try, one at a time), Wikipedia through `wiki_raw.py`, Lighthouse Friends (Cape Enrage), CBC (Albert Mines access; Harness shop closed 2021), and the operators' pages for hours (albertcountymuseum.com, steeveshousemuseum.ca, keillorhousemuseum.com, tantramarheritage.ca, parks.canada.ca). Pins from ArcGIS PointAddress results where there was a house number, otherwise the Register list point; the railway museum and station points fell on the road and were moved onto the buildings with `pix.py`. **Not checked:** anything on the ground; hours for the railway museum (no page of its own found), Cape Enrage (capeenrage.ca answered 403), the Albert County Museum's summer hours and the Carriage Factory's summer hours (both pages read in the off season); Keillor House and the Textile Museum hours are the society's 2025 season; who owns Cape Enrage light (Wikipedia and Lighthouse Friends disagree, conf='mixed'); the present use of the Bell Inn, Victoria Manor and the Harness shop building; whether trains still stop at Sackville; the Albert Manufacturing mill buildings and silos (from the Register, not seen to stand). Pins that mark an area, not the thing: Albert Mines (Register point in woods, no ruin seen). No 1 m LiDAR and no public-land layer in New Brunswick, so every pin said "not on mapped public land". Red brick: yes for the Albert Manufacturing office only; '?' for the Albert County Museum; no for the rest, from the Register's materials.

## Leads
Moved to `LEADS.md` on 2026-11-26 by the tidy job (6 rows). New leads for this ground go in the note of the batch that finds them.

| Place | Where | What is known | What is missing |
|---|---|---|---|

## Tips
Folded into `GUIDE.md` and the tools on 2026-11-26 by the tidy job (5 tips).
