# tn_ojdh: Tennessee: Rugby, Brushy Mountain and Coal Creek
state: Tennessee
region: tn
date: 2026-11-18
places: 19
file: data_tn_ojdh.py

## What this batch is
Nineteen places on Tennessee's northern Cumberland Plateau, drawn at random as region tn: five in the Rugby colony (Christ Church, the Hughes library, Kingstone Lisle, Laurel Dale Cemetery, the R. M. Brooks store), Wartburg's Presbyterian church and Tanner Store, Sixteen Tunnel, Brushy Mountain prison and the Stonecipher-Kelly house at Frozen Head (Morgan County); the Coal Creek War and mine-disaster sites at Briceville and Rocky Top (Anderson County); the old jail, the 1909 bank and Barton Chapel in Huntsville and Robbins, and the O&W railroad bridge in the Big South Fork (Scott County); and the LaFollette coke ovens (Campbell County). Facts come from National Register forms read through NPGallery `_text` with `page.py -g` (every one had a text layer), the Tennessee Historical Commission's O&W nomination, Wikipedia via `wiki_raw.py`, Historic Rugby, Tennessee State Parks, tourbrushy.com, the NPS Big South Fork news page, HMdb and the Coal Creek Watershed Foundation. Not checked: anything on the ground; interiors as they are today (the Rugby church glass and organ are from the 1972 form); hours for the Scott County jail museum, Brushy's season, and the churches; who owns Laurel Dale Cemetery, the two miners' circles and the LaFollette coke ovens now (the 2016 form says private, the federal land map puts the pin in North Cumberland WMA); whether the public may walk Fort Anderson (Register form: private; the foundation calls it a battlefield park). Pins on a general area, not the thing: Fort Anderson (Register coordinate on a wooded hillside), the Old Scott County Jail (pinned on the courthouse, the jail building not picked out). The Brushy closing years conflict (Wikipedia gives a 1972 closure as well as 2009) and the Scott County jail date (1904 or 1907): both entries are conf='mixed'. Red brick left '?' wherever no source or picture gave the colour.

## Leads
Places you read about and could not finish. One row each; delete the example row. Leave the table header.

| Place | Where | What is known | What is missing |
|---|---|---|---|
| Frozen Head CCC camp remains | Frozen Head State Park, Wartburg, TN | The park page says remnants of a CCC camp can be found; the camp ran 1933 to 1941 (Morgan State Forest history PDF) | Where in the park; most trails were closed for renovation in November 2026 |
| Uffington House and Newbury House, Rugby | Rugby, TN | 1880s colony houses in the 1972 Register form; Newbury House is Historic Rugby lodging | Current owners and whether either is open beyond lodging guests |
| Black Creek Fire Lookout Tower | Robbins, TN (36.3869, -84.6109) | 1951 steel tower, Register form 100001828; land likely private | Owner and any public way in |
| Allardt (Gernt Office, Allardt Historic District) | Allardt, Fentress County, TN (36.3808, -84.8839) | German colony of the Allardt Land Company, several Register listings | Not read this session |
| Massengale Homeplace | Rugby State Natural Area, TN | Historic Rugby says a homeplace older than Rugby is on a trail there | What is left and where |

## Tips
- Tennessee's county Register list titles ("...in Morgan County, Tennessee") redirect to the state list for small counties, so `wiki_raw.py --rows` prints 235 rows from many counties; grep its output for the town names.
- The ArcGIS geocoder (`findAddressCandidates` with a Tennessee search extent) found POIs that `nom.py` did not: "Stonecipher/Kelly Home", "RM Brooks Store", "Leach Cemetery". `tools/geo.py` is fixed to New York, so call the address directly.
- HMdb gives the Militia Hill markers in Rocky Top one position, at a road junction among houses; do not pin a place from such a shared position.
- tnstateparks.com park pages read fully with `page.py --all` (hours, closures, the gift shop hours); `/history` sub-pages answered 404.
