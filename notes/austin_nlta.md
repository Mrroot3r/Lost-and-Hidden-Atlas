# austin_nlta: Austin, Texas: hotels, mansion, cathedral, opera house and the old asylum
state: Texas
region: tx
date: 2026-11-26
places: 10
file: data_austin_nlta.py

## What this batch is
Ten standing buildings in Austin, taken from the names in one video about the city's old buildings (the record is `source/videos/20250627_PT6YBahgUzc.md`; the video was a tip only, and nothing in the entries comes from it). The Atlas had only the State Capitol within 15 km before. Added: the Driskill Hotel, the Texas Governor's Mansion, the Littlefield Building, the Millett Opera House (Austin Club), the Stephen F. Austin Hotel, Pemberton Castle, O. Henry Hall (the old federal post office and courthouse), Saint Mary Cathedral, the University of Texas Main Building and Tower, and the Austin State Hospital (Texas State Lunatic Asylum). Sources: Wikipedia read with `wiki_raw.py`, the Travis County National Register list (`--rows`), Texas Historical Commission marker pages (`atlas.thc.texas.gov/Details/<n>`, read with `page.py --all`), the State Preservation Board's mansion tour pages, the University Unions tower-tours page, a Texas HHSC news release (Old Main to stay), and the Diocese of Austin's news page for the cathedral's daily Mass times. Pins are address lookups (PointAddress) or OpenStreetMap building outlines, all looked at on the aerial. Not checked: any interior; Sunday Mass times (the parish site answered 403); hotel public-room hours; which building on the State Hospital campus is the 1861 Old Main (pin marks the campus, `prec='area'`); red brick for nine of the ten (left `'?'`); parking (downtown street, not looked up). O. Henry Hall is `conf='mixed'`: Wikipedia gives 1879 in its text and 1881 in its category.

## Leads

| Place | Where | What is known | What is missing |
|---|---|---|---|
| Austin State Hospital Old Main Building (pin) | Austin, TX (campus 30.30827, -97.73715) | Texas Historic Landmark of 1861; HHSC said in 2020 it would stay while the rest was rebuilt | Which building it is on the aerial, to move the pin from the campus to the building |
| H&TC and I&GN depots marker | Austin, TX | Texas Historical Commission marker 5507016288 exists | Not read; whether anything of either depot stands |
| First National Bank of 1896 | Austin, TX | Named in a video only | Whether it stands, and a source |

## Tips
- The Texas Historical Commission marker pages (`atlas.thc.texas.gov/Details/<n>`) read with `page.py --all`; the marker text follows "Marker Text". Some markers (Pemberton Castle) have no text there, only the address and year.
- `smcaustin.org` (Saint Mary Cathedral) and `austindiocese.org` answer 403 to `page.py` and the web fetch tool; `austindiocese.news` reads and gave the daily Mass times.
- `hhs.texas.gov` answers 403; HHSC news releases on `content.govdelivery.com` read well.
- `universityunions.utexas.edu/tower-tours` said "Tower Tours are currently unavailable" (November 2026).
- The Littlefield Building's Commons pictures are muddled with the Scarbrough Building across the street: no picture was chosen.
