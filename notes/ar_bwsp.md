# ar_bwsp: Arkansas: Heber Springs, Mountain View and the Little Red River hills
state: Arkansas
region: ar
date: 2026-11-18
places: 18
file: data_ar_bwsp.py

## What this batch is
Eighteen places in Cleburne County (drawn at random inside region `ar`) and the two counties beside it, Van Buren and Stone: three stone or brick courthouses (Heber Springs, Clinton, Mountain View), rural one-room and NYA stone schools (Brewer, Dill, Quitman, West Richwoods, Roasting Ear), the 1908 Missouri and North Arkansas Railroad truss at Shirley and the 1936 WPA bridge over the railroad's Edgemont Cut, the 1945 wire-cable suspension bridge at Allison, the Damascus CCC camp arch, Brewer's Mill and the Commercial Hotel in Mountain View, the Woodrow Store, the Gunn mule barn in Quitman, the 1933 band shell in Spring Park, and the CCC dam at Mirror Lake with the Mitchell mill below it. Nearly every fact comes from the National Register nomination forms, read as text with `page.py` from NPGallery `_text` (all had text layers), and the Wikipedia articles (`wiki_raw.py`); the U.S. Forest Service Blanchard Springs pages, the Cleburne County Spring Park page and a Clio entry filled in access and later use. Nothing was checked on the ground. Most nominations are 1985 to 2016, so whether a store, mill, hotel or school is still standing, in the same use, or open to visitors was NOT checked for any of them; courthouse hours were not checked. The Mitchell mill at Blanchard Springs rests on one local photo site (2Cooleys, ozarkmtns.com) and the pin is the dam, not the mill. Woodrow Store and Roasting Ear Church and School are area pins (building not identified on the aerial). Red brick: left `?` wherever a source names brick without its colour.

## Leads
Places you read about and could not finish. One row each; delete the example row. Leave the table header.

| Place | Where | What is known | What is missing |
|---|---|---|---|
| Cleburne County Farm Cemetery and CCC Camp Heber remains | Heber Springs, AR (35.455556, -92.0375) | Poor-farm cemetery 1896–1943 with about ten fieldstone markers and a granite list monument; some CCC Camp Heber (#3782) features "remain to the northwest" (NRHP 05001066) | The site is inside a newer housing subdivision on private land; which CCC remains survive and whether they can be seen from a public road |
| Dew Drop Inn | Mountain View, AR (35.869444, -92.120278) | The other surviving 1920s hotel in Mountain View (NRHP 85002231; named in the Commercial Hotel form) | Form not read; current state |
| Van Buren County Road 2E Bridge | Scotland, AR (35.511389, -92.698056) | Three-span stone and concrete WPA bridge of 1940 on a tributary of Driver's Creek (NRHP 95000570) | Pin not checked on the aerial; parking |
| Winkley Bridge | Heber Springs, AR | National Register listing 84000020 (Wikipedia list gives no coordinate) | The NPGallery text came back nearly empty (893 characters), so no source on what it is or whether it survives was read |
| Titan II ICBM Launch Complex 374-7 | Southside, Van Buren County, AR | NRHP 98001434, address restricted | Who owns it and whether anything can be seen from a public road |

## Tips
- Arkansas nomination forms on NPGallery (`_text`) all had text layers, including the 1985 Stone County multiple-resource forms; `page.py -g` on them gives building dates, materials and owners in one call.
- encyclopediaofarkansas.net entry addresses guessed from a title answer 404 with no archived copy; take the exact address from a web search result first.
- Older Arkansas forms give a UTM reference but no latitude and longitude, and no tool converts UTM; a short inverse-UTM formula was needed to place the Brewer School (the National Register list coordinate was ~200 m off, in a field). A `tools/utm.py` would help.
- `places_test.js` still fails only on `onesquethaw-valley` ("18th century"), as earlier notes said; this batch changes nothing it reads.
- The pin check's `land:` line for the Mirror Lake dam said "North Sylamore Creek ... (OA)" on the first run and "not on mapped public land" on the second, 23 m away; the federal land map answer can flip between runs.
