# al_zbty: Alabama: a second scatter, Florence to Mobile
state: Alabama
region: al
date: 2026-11-21
places: 15
file: data_al_zbty.py

## What this batch is
A second scatter of 15 places across Alabama, which had 19 when the session began. North: the Forks of Cypress column ruin (Florence), the Old State Bank (Decatur), Pond Spring, the Joseph Wheeler Plantation (Hillsboro), the Weeden House (Huntsville), the Fort Payne Depot Museum. Centre: St. Michael and All Angels, Anniston. Black Belt and Montgomery: Magnolia Grove (Greensboro), Sturdivant Hall and the Edmund Pettus Bridge (Selma), Dexter Avenue King Memorial Baptist Church. South-east: Fendall Hall (Eufaula), Claybank Log Church (Ozark). South: the Old Monroe County Courthouse (Monroeville), Church Street Graveyard (Mobile), the Mount Vernon Arsenal and Searcy Hospital (view only; burned April 2026). Facts from Wikipedia (tools/wiki_raw.py, with the Register rows from --rows) and the managing bodies' pages read with tools/page.py: the Alabama Historical Commission's visit pages (Magnolia Grove, Fendall Hall, Pond Spring, Forks of Cypress), weedenhousemuseum.com, monroecountymuseum.org, dexterkingmemorial.org/tours, stmichaelsanniston.org (history page), cityofmobile.gov; the Encyclopedia of Alabama, the Muscle Shoals National Heritage Area and HMdb. National Register forms were not read. Nothing was checked on the ground. Not checked: hours for the Fort Payne Depot Museum and Church Street Graveyard (no page read gave any) and St. Michael's service times; Sturdivant Hall's hours come from the Encyclopedia of Alabama because the museum's site (sturdivanthall.com) shows only a hosting placeholder; Claybank Church's daylight hours come from exploresouthernhistory.com, not the association; admission amounts at the three Commission houses; parking everywhere (parking.py mapped lots in the towns but whose they are was not checked, so no th= was given). Forks of Cypress ownership: Wikipedia and the Encyclopedia say the state (AHC) owns it, the AHC and the Heritage Area call it private property; entry is conf='mixed', view only from Jackson Road. The Old State Bank is closed for restoration (Heritage Area page). Pins at area precision: Pond Spring (Wikipedia point in woods, buildings not told apart) and the Mount Vernon Arsenal (the HMdb marker at the road). Claybank's pin is on the one small building beside the cemetery, inferred to be the church (site precision). Red brick from Wikipedia photographs for Forks of Cypress, Dexter Avenue, the Old Monroe County Courthouse and Church Street Graveyard; six places are '?'. Fendall Hall has no free photograph on Commons near the pin.

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| The Tavern | Eufaula, AL (31.89167, -85.14167) | Built 1836, Eufaula's oldest frame structure; used as an Episcopal church and a Confederate hospital (Register list row, Wikipedia stub, 105 Riverside Drive) | Who owns it now and whether it is a house, an inn or open; the stub gives nothing more |
| Shorter Mansion | Eufaula, AL | On the Register (72000156); the list coordinate (-85.146) looks right for Eufaula while Fendall Hall's in the same list was 27 km off | Not read in this session: a source for its history, current use and hours |
| Talladega Courthouse Square | Talladega, AL (33.435, -86.1025) | A Register historic district (72000181); start.py lists Talladega as an old town centre with no Atlas place | No article; needs the Register form or a city page |
| Huntsville Depot | Huntsville, AL | Already a lead in notes/al_hsqw.md | Current access unknown since the museum left in 2024 |

## Tips
- The Register list coordinate for Fendall Hall, Eufaula (-85.425) is 27 km west of the house; nom.py's OpenStreetMap building was right. Check Barbour County list points.
- sturdivanthall.com serves only an aaPanel hosting placeholder; the Encyclopedia of Alabama article gives the house's hours and owner.
- The Muscle Shoals National Heritage Area pages (msnha.una.edu) read cleanly with page.py and give current closures and directions for northwest Alabama sites (Old State Bank closed for restoration; Forks of Cypress directions).
- HMdb marker 70593 (Mount Vernon Arsenal) gave its position as plain "31.088122,-88.024183" in the cached page, not in the Touch-link form the guide describes; grep for a bare lat,lon pair as well.
