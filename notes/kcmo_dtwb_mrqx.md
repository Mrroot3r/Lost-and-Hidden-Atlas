# kcmo_dtwb_mrqx: Downtown Kansas City and the West Bottoms, Missouri
state: Missouri
region: kcmo
date: 2026-11-23
places: 15
file: data_kcmo_dtwb_mrqx.py

## What this batch is
Fifteen standing buildings and one cemetery in downtown Kansas City, the West Bottoms and Northeast Kansas City, none of which the Atlas had: the Folly Theater, three downtown hotels (President, Savoy, Phillips) and the Rieger Hotel, the Boley, Chambers, Graphic Arts and Argyle buildings, five West Bottoms warehouses and factories (Albert Marty, Creamery Package, Moline Plow, Perfection Stove, Faultless Starch) and Elmwood Cemetery. They come from the National Register lists for downtown Kansas City on Wikipedia. Facts are from Wikipedia's articles (read as raw text), the National Register forms for the Moline Plow, Perfection Stove and Creamery Package buildings, and Clio pages for the Marty and Faultless Starch buildings. Not checked: hours for every hotel, the theatre and the cemetery (no page of their own opened), what the hotel interiors keep, current use of the West Bottoms buildings, whether the Faultless plant still runs. The pins fall on buildings of the right kind on the aerial, but with dense downtown blocks the exact building could not be told apart, so the West Bottoms pins are `site`. Red brick: 'yes' for five West Bottoms buildings from a form or a photograph; the rest '?' or 'some' from the sources. Pictures: four chosen from Commons, none for the Moline building (only an entrance close-up).

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Sewall Paint and Glass Company Building | 1009 W. 8th St, Kansas City, MO (39.1056, -94.5953) | On the National Register (02000469); a red-brick building shown on Commons | A readable Register form (NPGallery has only a placeholder) |
| Heim Brewing bottling plant and Fire Station No. 20 | 507 N. Montgall Ave, Kansas City, MO (39.1198, -94.5492) | Register-listed (15001018, 100009693); a search result says the bottling plant is now a distillery and a garden bar | The Missouri nomination PDFs were not reachable; hours and current use |
| Boarding House, Hall of Waters-era districts, Quality Hill, West Eleventh Street district | Kansas City, MO | Register districts with Wikipedia stubs | Sources describing what survives |
| Independence Boulevard Christian Church; Gillis Orphans' Home; Helping Hand Institute; Studna Garage | Northeast and River Market, Kansas City, MO | Register-listed, coordinates in the Wikipedia list | Any source beyond the list |
| Midland Theatre, Mainstreet Theater, Scarritt Building, Muehlebach | downtown Kansas City, MO | Named in the Hotel President and Folly articles | Not looked up |

## Tips
- Wikipedia's article coordinates for downtown Kansas City buildings are often a block off; the Register list coordinates were better (Chambers, Graphic Arts, Argyle, Rieger).
- NPGallery serves a one-page placeholder for many forms; mostateparks.com PDFs 404 and web.archive.org is blocked for the fetch tool. Clio pages (theclio.com/entry/<n>) open with the fetch tool and are useful for West Bottoms buildings.
- The wiki_raw.py --rows lists for Kansas City are under "National Register of Historic Places listings in Jackson County, Missouri: Downtown Kansas City" and "...: Kansas City other"; the plain "Kansas City, Missouri" page has no rows.
- publish.sh replaced source/tools/checked_ok.json from a stale workspace copy and would have deleted other sessions' entries; check `git status` after it and restore that file from main.
