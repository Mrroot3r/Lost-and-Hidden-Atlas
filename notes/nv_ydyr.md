# nv_ydyr: Nevada: mint, courthouse, schools, mills and ghost camps
state: Nevada
region: nv
date: 2026-11-24
places: 14
file: data_nv_ydyr.py

## What this batch is
Fourteen places across Nevada, which had 51 (the thinnest state at the start): the Carson City Mint (Nevada State Museum), the Oats Park school in Fallon, the Lyon County Courthouse in Yerington, the Fernley and Lassen depot, the Minden flour mill, the Aurora and Unionville ghost camps, the Techatticup Mine in Eldorado Canyon, the Huntridge Theater and Fifth Street School in Las Vegas, the Virgin Valley Heritage Museum in Mesquite, the El Cortez in Reno, the Silver State Flour Mill near Paradise Valley and the Hawthorne USO building. Taken from the National Register county lists and Wikipedia articles (tools/wiki_raw.py); owners, hours and what stands today come from web search results quoting museum, city, Travel Nevada and news pages, because the managing bodies' own pages would not open from page.py. Not checked: interiors, nearly every standing building's current use, hours for Fernley, Fifth Street, the USO hall and Minden's tasting room, whether the Aurora townsite lots are public, brick for most places (many are brick='?'). Pins were looked at on the aerial; Techatticup, El Cortez, Hawthorne USO, Mesquite, Fifth Street and Minden were moved (to buildings seen on the aerial or to a street address lookup). Pictures: two chosen from Commons, one place (Silver State Flour Mill) has none. The Fernley depot lead from nv_rkdm is done and its row removed.

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Nevada Central turntable | Austin, NV (39.4971, -117.0839) | National Register 2003, listed in Lander County | Article or managing page, what is left |
| Bristol Wells Town Site | Pioche, NV (38.106, -114.695) | National Register 1972 ghost town, Lincoln County | A source for what stands and road access |
| Hazen Store | Hazen, NV (39.5639, -119.0489) | National Register 2001 | Article or owner, what stands |

## Tips
- Midas Schoolhouse (Elko) looked good on the register list but burned in 2005: read the article before choosing from a Register list.
- Wikipedia says the Silver State Flour Mill was built "in 2028" (vandalism) and gives both 1864 and 1867: use the Register form.
- geocode.arcgis.com findAddressCandidates with a house number gave PointAddress hits on the right building in Reno, Hawthorne, Mesquite and Las Vegas where Register points fell in a road or on a house.
- `photo_find.py new` can run over the two-minute limit; it ran in the background and finished fine.
