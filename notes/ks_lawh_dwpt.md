# ks_lawh_dwpt: Lawrence and Douglas County, Kansas (second pass)
state: Kansas
region: ks
date: 2026-11-24
places: 9
file: data_ks_lawh_dwpt.py

## What this batch is
Nine places in Lawrence and Vinland, Douglas County, Kansas, picked from Register listings the Atlas did not yet have: the 1904 Carnegie library, the Roberts "Castle" mansion, the Morse and Benedict houses, the Griffin house, the John Kelly stone building, the Barnes-Hoskinson farm, the Chi Omega house and the Breezedale streetcar suburb. I meant to work Kansas City's other parts (Lee's Summit and Cass County, Clay and Platte counties, Johnson County), but start.py and a check of the Register lists against every place file showed almost every listing there already on the Atlas, so I took Douglas County, where about twenty listings were still missing, and kept the nine with something to see. Facts come from the National Register nominations on NPGallery that have a text layer (library 1975, Castle 1974, Morse 1991, Benedict 1991, read whole) and the Kansas Historical Society's register pages (summaries only, for the Griffin house, the Kelly building, Barnes-Hoskinson, Chi Omega and Breezedale). Where only a summary was read, the entry says so. Not checked: anything on the ground, owners, current use of the library and the Castle, hours (none recorded), the Kelly building's exact position (the pin is the farm address) and which Barnes farm building is the farmhouse. Pictures: five of nine have none (the tool found none at the Kelly farm; Morse, Benedict, Chi Omega and Breezedale had only pictures of other places). The Barnes-Hoskinson picture is of the Barnes Apple Barn, which Commons files under the same farmstead name.

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Oregon-California Trail segments (First United Methodist Church swales) | 867 US-40, west edge of Lawrence, KS | Register 2016 listing (summary read): two swales about nine miles east of Big Springs on the combined trail | Whether anything can be seen from a public place; the nomination text |
| Hancock (12th Street) Historic District, Oread Historic District | Lawrence, KS | Register residential districts | Summaries only; they are houses |
| Mary Carrol Griffin neighbours: Roberts-Luther-Mitchell House | 1313 Massachusetts St, Lawrence, KS | Register 2022; next door to the Castle, once Roberts's too | Nomination has no text on NPGallery |
| Buck Creek School | Jefferson County, KS | Wikipedia: c. 1878 limestone school, closed 1952, on the Register since 1988 | Neither OpenStreetMap (39.06583, -95.29692) nor the Wikipedia point (39.06778, -95.29472) is known to be on the building |

## Tips
- Clay, Platte, Cass, south Jackson and Johnson County, Kansas are nearly all on the Atlas: checking a Register list name by name against `grep -il "<name>" source/tools/data_*.py` takes a minute and saves choosing an exhausted part. Douglas County still had about twenty unlisted Register entries; Leavenworth County outside the city (Delaware Cemetery, Little Stranger Church and Cemetery, Lansing) has about three more.
- Old nominations on NPGallery (numbers before about 2000) usually have a text layer and page.py reads them in full; the newer ones (100xxxxx) have none, so the Kansas Historical Society's summary is the only source.
- The Kansas Historical Society's register pages run to 13 pages for Douglas County; the page.py output has the record text in one line, so split it on "Inventory Record ." to list the names.
