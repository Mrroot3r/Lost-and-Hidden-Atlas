# kcmo_mid_rqzv: Kansas City: West Bottoms, downtown, east side and Midtown
state: Missouri
region: kcmo
date: 2026-11-25
places: 10
file: data_kcmo_mid_rqzv.py

## What this batch is
Ten places in Kansas City, Missouri that the Atlas lacked: the Crane Company and C. A. Murdock warehouses and the West Bottoms – North Historic District, the 1911 Kansas City Star Building, the Hoover Brothers Building, the Campbell-Continental bakery, the St. Regis Hotel, Westport Junior High School, the Agee Apartments and Quality Hill. Fewer than the 15 to 20 aimed for. The assigned ground (Lee's Summit, Raytown, Grandview, Blue Springs, Pleasant Hill, Harrisonville, Odessa, Higginsville, Lone Jack, Liberty, Kearney, Richmond, Platte City) turned out to be almost fully covered: every Register listing in Cass, Lafayette, Platte and Ray counties, and in Jackson County outside Kansas City, already had a place, and the small towns' Wikipedia articles name no old buildings. So the batch moved to Kansas City's own Register list, where the Atlas lacks many buildings.
Sources: only National Register registration forms that NPGallery returns as text (2013 and later: read with `page.py --all -n 400000` on `https://npgallery.nps.gov/NRHP/GetAsset/NRHP/<ref>_text`), plus Wikipedia raw text for Quality Hill. Most older forms are the one-page placeholder, and `dnr.mo.gov/shpo/nps-nr/<ref>.pdf` answered HTTP 503. Pins are Esri geocoder street addresses, each looked at on the aerial. The forms give each building's use as of 2013 to 2019, so present use, interiors, hours and parking were not checked. Not added although the forms were readable, because the buildings are mid-century modern: Traders National Bank (1956-62), Plaza Towers (1950), Plaza House Apartments (1955), Interstate Securities (1950), Ten Main Center (1965-68), Executive Plaza (1972), Quality Hill Center (1951-58), Commerce Tower. Brick: red brick only where a form or the picture says so; the Star, Crane, Murdock and Quality Hill are `?` because their forms do not name a colour. Pictures: seven places have a Commons picture; the Star Building, the Hoover Building and Quality Hill have none that fits.

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Aurora Apartments | 3012-3014 Linwood Blvd, Kansas City, MO | Register form (100001758, readable): 1925, ten units, concrete block with red brick veneer, builder Leon Ludwig; Commons has a picture | Modest vernacular building; add if a series wants it |
| Interstate Securities, Traders National Bank, Plaza House and Towers | Downtown and Plaza, Kansas City, MO | Readable forms, all 1950s-60s | Modernist: left out by rule 8 |
| Bellerive Hotel, Barclay Building, Chatham Hotel, Tocoma, Valentine on Broadway | Hanover Place and Valentine, Kansas City, MO | On the Register list with coordinates; forms are placeholders | A readable source for each (NPGallery text and the Missouri copy both failed) |
| Mary Rockwell Hook houses (Bixby, Burnette-Berry, Gary, Katz, Bryson Jones, Nicholson) | Country Club District and Sunset Hill, Kansas City, MO | Register list coordinates | Readable forms; Wikipedia has only a stub for Hook |
| Kansas City National Guard Armory, Seven Oaks School, St. Francis Xavier church, Archbishop O'Hara and St. John's high schools | Kansas City, MO | Register list coordinates; forms are placeholders | A readable source |
| West Bottoms – North Historic District's buildings | West Bottoms, Kansas City, MO | The 2016 form (16000771, 170 pages, readable) describes 29 buildings one by one | Only the district is written up; the best buildings in it could each be added from that form |

## Tips
- Whole counties are done. Before choosing ground, run `tools/start.py` on the largest town of each county and compare Register list rows with the Atlas by name: nothing outside Kansas City was missing in the four counties around Lee's Summit.
- Matching Register names to Atlas ids by words gives false matches (Hyde Park, Chatham Square, Mason City); look at the matched id before believing it.
- NPGallery forms from 2013 on (reference numbers starting 13, 14, 15, 16 and 100...) usually read as text; 2012 and earlier are placeholders. HMdb pages answered 403 from `page.py` in this run.
- `tools/start.py --prs` printed 0 open pull requests; no other session was working Missouri.
