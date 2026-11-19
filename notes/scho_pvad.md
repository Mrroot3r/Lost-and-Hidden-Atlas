# scho_pvad: Broome County, NY: Binghamton, the Triple Cities and their six carousels
state: New York
region: scho
date: 2026-11-19
places: 20
file: data_scho_pvad.py

## What this batch is
Twenty places in Broome County, New York, drawn at random by `choose.py --state ny` (region `scho`, which offered Jefferson, Binghamton and Johnson City); the Atlas had nothing within 20 km of Binghamton. Binghamton: the New York State Inebriate Asylum (empty, view only), the Phelps Mansion and Roberson Mansion museums, the Broome County Courthouse, the old 1898 city hall (now apartments), Christ Church (Upjohn, bluestone) and Trinity Memorial Church, the South Washington Street parabolic bridge (footbridge), the DL&W station of 1901, and the Bundy House (its museum closed from August 22, 2026). George F. Johnson's six free carousels (Ross Park, Recreation Park, C. Fred Johnson Park, Highland Park, George W. Johnson Park, West Endicott Park) as six places, and the Square Deal Arch in Endicott. Outside the cities: Chenango Canal Lock 107 and guard lock in Chenango Valley State Park, the 1888 Ouaquaga lenticular bridge, and the Old Hawleyton Methodist church. Sources: Wikipedia as raw text (`wiki_raw.py`, with `--rows` on the Broome County Register list), HMdb marker pages, and the managing bodies' pages read with `page.py` (Broome County carousels page, Village of Johnson City and Village of Endicott parks pages, Town of Union carousel page, phelpsmansion.org, roberson.org, trinitymemorial.org, bundymuseum.org, parks.ny.gov), WNBF and WICZ news pages. Not checked: carousel times at Ross Park, Recreation Park, Highland Park and West Endicott Park (season only, from the county page); service times at Christ Church and Hawleyton; whether the courthouse can be visited inside; the present use of the DL&W station; whether the Johnson City Square Deal Arch is back up (WNBF said in April 2026 it was weeks away); which building in George W. Johnson Park is the carousel pavilion (prec site); parking at Lock 107 and at the Ouaquaga bridge; brick on the old city hall, the DL&W station, the Roberson Mansion (only a black-and-white photo) and the arch. Nothing was visited.

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Kilmer Sanitarium carriage house | 334 Sanitaria Springs Road, Port Crane, NY (HMdb 243455, 42.15819, -75.76348) | Sanitarium of S. Andral Kilmer (Swamp Root), 1892; the carriage house building remains (Colesville marker) | Any source beyond the marker; owner; whether it is seen from the road |
| Chenango Canal aqueduct ruins at Port Crane | I-88 eastbound between mile 3 and exit 3 (HMdb 23064, 42.16013, -75.84682) | Marker: ruins of the aqueduct that carried the canal over the Chenango River lie to the east; the towpath ran by the river | A source on what stands; a legal place to stop (the marker is on the interstate) |
| Johnson City Square Deal Arch | Main Street at the Johnson City–Binghamton line (Wikipedia's Endicott arch point, 42.11139, -75.94611) | 1920 arch, rebuilt 1982, taken down 2024 for restoration; WNBF April 2026: base ready, reassembly weeks away | Whether it is back up |
| Broome County Forum Theatre | Binghamton (42.10389, -75.91222) | 1919 theatre block with a pipe organ, home of the Binghamton Philharmonic and Tri-Cities Opera, NRHP 2008 (Wikipedia) | Box-office or tour page for times |
| Washingtonian Hall (Amos Patterson House) | Endwell (42.11083, -76.00444) | 1799–1800 Federal house, moved 1924, NRHP 1996 (Wikipedia) | Owner and whether it is seen from the road |
| Stone Spillway, National Defense Stockpile Center | Hillcrest, Broome County (address restricted) | NRHP 2004 | Location and access |

## Tips
- Broome County's carousel page (`broomecountyny.gov/community/carousels`) reads in full with `page.py --all` and gives address, phone and season for all six carousels; the City of Binghamton's carousel page answers 403.
- Wikipedia's infobox coordinates for the two Square Deal Arches are swapped: the "Endicott" article's point is at the Johnson City–Binghamton line and the "Johnson City" article's point is in Endicott. OpenStreetMap labels the Endicott arch with the Johnson City name.
- Trinity Memorial Church's Wikipedia/Register point is 3 km east of the church; `nom.py` gives 44 Main Street. The old Binghamton City Hall's Wikipedia point is on State Street; `osmnear.py ... buildings` finds it as "Binghamton Municipal Building", alt name Old City Hall.
- The Episcopal Asset Map result for "Christ Episcopal Church" Binghamton is a New Jersey church (Shrewsbury): check the state.
- The Chenango Canal Prism and Lock 107 Register form (10000359) is an NPGallery placeholder; the HMdb Lock 107 marker and the Town of Fenton history page say what is left.
- Wikimedia refused (429) both tries for the Binghamton City Hall picture.
