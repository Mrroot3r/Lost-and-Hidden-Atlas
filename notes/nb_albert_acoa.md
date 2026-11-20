# nb_albert_acoa: Albert County, Dorchester and Sackville, New Brunswick
state: New Brunswick
region: nb
date: 2026-11-20
places: 20
file: data_nb_albert_acoa.py

## What this batch is
Twenty places in southeastern New Brunswick, where the Atlas had nothing between Moncton and Fort Beauséjour. Albert County: the old shiretown at Hopewell Cape (Albert County Museum: the 1845 gaol, tax and records offices and the 1904 courthouse), the Albert Mines albertite site (private, look from the road), the Steeves House museum, the New Brunswick Railway Museum and the Albert Manufacturing Company's 1907 red-brick office with the gypsum mill buildings in Hillsborough, the Riverside Consolidated School and Victoria Manor at Riverside-Albert, Coverdale United Church, Cape Enrage Lighthouse, and the Fundy National Park headquarters building and saltwater pool at Alma. Westmorland County: Keillor House, the St. James Textile Museum (Saint James Presbyterian Church), the Bell Inn, Rocklyn and the penitentiary in Dorchester; the Campbell Carriage Factory, the Boultenhouse Heritage Centre, the Intercolonial station and the Sackville Harness shop in Sackville. Sources: the Canadian Register statement for 18 of them (historicplaces.ca with `page.py --all -n 60000`; every page read on the first try, one at a time), Wikipedia through `wiki_raw.py`, Lighthouse Friends (Cape Enrage), CBC (Albert Mines access; Harness shop closed 2021), and the operators' pages for hours (albertcountymuseum.com, steeveshousemuseum.ca, keillorhousemuseum.com, tantramarheritage.ca, parks.canada.ca). Pins from ArcGIS PointAddress results where there was a house number, otherwise the Register list point; the railway museum and station points fell on the road and were moved onto the buildings with `pix.py`. **Not checked:** anything on the ground; hours for the railway museum (no page of its own found), Cape Enrage (capeenrage.ca answered 403), the Albert County Museum's summer hours and the Carriage Factory's summer hours (both pages read in the off season); Keillor House and the Textile Museum hours are the society's 2025 season; who owns Cape Enrage light (Wikipedia and Lighthouse Friends disagree, conf='mixed'); the present use of the Bell Inn, Victoria Manor and the Harness shop building; whether trains still stop at Sackville; the Albert Manufacturing mill buildings and silos (from the Register, not seen to stand). Pins that mark an area, not the thing: Albert Mines (Register point in woods, no ruin seen). No 1 m LiDAR and no public-land layer in New Brunswick, so every pin said "not on mapped public land". Red brick: yes for the Albert Manufacturing office only; '?' for the Albert County Museum; no for the rest, from the Register's materials.

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Enterprise Foundry | Sackville, NB (73 Lorne Street, 45.8904, -64.3681) | Register idm 7181 lists ten buildings of 1908; Global News (January 19, 2012) and the Tantramar Heritage Trust say fire devastated it in January 2012, and the aerial shows cleared ground | What, if anything, still stands; left out as probably gone |
| Tonge's Island | near Fort Beauséjour, Aulac, NB (45.8528, -64.278) | National Historic Site (Register 14586): La Vallière's manor, capital of Acadia 1678-84, a low rise in the marsh by the Missiguash | Anything to see and a public way to it |
| Acadian battlefield, Hillsborough | Hillsborough, NB (45.9224, -64.6447) | Local historic place (Register idm 18123) | Statement not read |
| Hillsborough local historic places | Hillsborough, NB | About 25 local historic places on the Register (houses, Peck Memorial Hall, Old Post Office, Saint Mary's Anglican and Hillsborough United churches) | Statements not read; a walking-tour batch could take the best of them |
| Sackville Methodist Burying Ground and Four Corners Burying Ground | Sackville, NB (45.9192, -64.3656; 45.9367, -64.3392) | Local historic places (Register idm 4128, 5376) | Statements not read |
| Marshlands Inn | Sackville, NB (45.8968, -64.3641) | Local historic place (Register idm 4099) | Whether it still runs as an inn; hours |

## Tips
- The Register's Wikipedia list for Albert County has no row for the Albert County Museum or Cape Enrage; search for them by name.
- A web search in this session returned titles and links only, with no quoted text: read every page with `page.py`.
- The Register's address line is easy to pull from a cached page: the text between "Share | -->" and "Formally Recognized"; fed to the ArcGIS geocoder it gave PointAddress results that sat on the building for 13 of 15 New Brunswick addresses (`geo.py` is limited to New York, so call findAddressCandidates directly).
- A Register statement can be years old: the Enterprise Foundry statement still describes ten buildings burned in 2012. Look at the aerial before writing up an industrial site.
- Parks Canada's Fundy hours page is `parks.canada.ca/pn-np/nb/fundy/visit/heures-hours` (it gives each visitor centre and the pool).
