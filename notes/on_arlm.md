# on_arlm: Kingston and the southern Rideau Canal
state: Ontario
region: on
date: 2026-11-19
places: 19
file: data_on_arlm.py

## What this batch is
Nineteen places in and around Kingston, Ontario and along the southern Rideau Canal, the first real batch for Ontario (region `on` had one place). Kingston: Murney, Shoal and Cathcart Martello towers, the Fort Frontenac bastion footings, Fort Henry, Kingston Penitentiary, Rockwood Asylum (vacant), Bellevue House, City Hall and Market Square, St. George's Cathedral and the Frontenac County Court House. Rideau Canal: Kingston Mills locks and blockhouse, Jones Falls (stone arch dam, Sweeney House, blacksmith's shop), Davis Lock lockmaster's house and the Narrows Lock blockhouse. Leeds and Grenville: the Old Stone Mill and St. Paul's Church (1811) at Delta, Lyndhurst Bridge (1857) and the Brockville Railway Tunnel. Sources: Wikipedia raw text (`wiki_raw.py`); Parks Canada lockstation, history and 2026 hours pages, the federal heritage directory (FHBRO and national historic site entries) and HistoricPlaces.ca through `page.py`; rideau-info.com; the Delta Mill Society; Brockville Tourism and Brockville Daily. Pins are OpenStreetMap points from `nom.py`/`osmnear.py`, looked at on the aerial; Brockville tunnel moved to its south approach, Fort Frontenac moved to the street corner and left at `area` (the bastion footings could not be made out). Not checked: hours for Fort Henry, Murney Tower and the Kingston Pen tours (their pages would not open); who owns the Rockwood grounds; whether Sweeney House, the blacksmith's shop and the Davis house are open inside (rideau-info.com says interpretation at Jones Falls ended in 2022); the Narrows and Cathcart interiors; landing rules on Cedar Island. Canada has no 1 m LiDAR and no public-land layer, so every `public` place gets CHECK ACCESS from the pin check; the managing body is named in each access note. Red brick: Bellevue, the penitentiary and the cathedral set `no` from their Wikipedia lead photographs; Murney Tower, Fort Henry, Fort Frontenac, Kingston Mills and the Brockville tunnel are `?`.

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Prison for Women (P4W) | Kingston, ON (across King Street West from Kingston Penitentiary) | Women's federal prison 1934–2000 (Wikipedia, Kingston Penitentiary); vacant; Union Park developer FAQ says the building is unsafe to enter and is being redeveloped | A coordinate from the aerial and the redevelopment's present state |
| Fort Frederick and the Point Frederick tower | Kingston, ON (Royal Military College grounds) | One of the five Kingston fortification works (Wikipedia, Murney Tower) | Its own article or Parks Canada page, and whether the RMC grounds are open |
| Newboro blockhouse | Newboro, ON (10 Blockhouse Lane, Parks Canada) | One of four Rideau blockhouses; Parks Canada lists "historic accommodation" at Newboro | A source on the blockhouse itself (the FHBRO directory should have one) |
| Delta walking-tour buildings | Delta, ON | The Delta Mill Society tour lists twelve stops (Denaut House 1849, Old Town Hall 1879, Bell Store, Hicock House c.1845) | Pins and the tour's full text for each; most are private houses, view only |
| Jones Falls guardhouse (1838) | Jones Falls, ON | Parks Canada history page names it, east of the third lock | A pin on the aerial |

## Tips
- Parks Canada lockstation pages (`parks.canada.ca/lhn-nhs/on/rideau/visit/posteeclusage-lockstation/ecluse-lock-<name>`) read in full with `page.py --all -n 3000` and give the civic address and a GPS position; ignore their "Constructed: 1908-1912" line, a template slip (the canal opened in 1832). The history pages are at `.../histoire-history/histoire-decluse-lock-history/<name>` (no hyphens: `kingstonmills`, `jonesfalls`).
- The federal heritage directory (`pc.gc.ca/apps/dfhd/page_fhbro_eng.aspx?id=<n>` and `page_nhs_eng.aspx?id=<n>`) reads well with `page.py --all` and gives dates, materials and the custodian for each Rideau building.
- `forthenry.com`, `kingstonhistoricalsociety.ca` (Murney Tower) and `kingstonpentour.getanchor.io` gave no hours to `page.py` (empty, 404 or 530).
- In Canada every `public` place gets CHECK ACCESS from the pin check, because there is no public-land layer; expected.
- `brick.py look` on Wikipedia lead photographs settled three Kingston limestone buildings quickly; no 429s at a 10-second pace.
