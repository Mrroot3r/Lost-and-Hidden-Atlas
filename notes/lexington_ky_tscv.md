# lexington_ky_tscv: Downtown Lexington, Kentucky
state: Kentucky
region: ky
date: 2026-11-28
places: 10
file: data_lexington_ky_tscv.py

## What this batch is
A "videos" batch (job 9): the names came from one video's tour of old Lexington postcards (the record is `source/videos/20241004_v_AwP1OaoLo.md`, 36 names). Ten standing buildings were added, all downtown or close by: the Old Fayette County Courthouse, Central Christian Church, the Odd Fellows Temple, Old Morrison at Transylvania, the Lexington Opera House, the Sayre Female Institute, the Lexington Herald Building, the federal Post Office and Court House, the Lexington Cemetery with its 1890 gatehouse, and the old Lafayette Hotel (now the Government Center). Sources: Wikipedia (`wiki_raw.py`, including the Fayette County Register list and the Downtown Commercial District list), the Park Service's records and forms (`form.py`; most of these Lexington forms are photograph pages only, so the records gave the architects and years), VisitLEX for the courthouse visitor centre, the cemetery's and the church's own pages, and the Herald-Leader's photo archive (kyphotoarchive.com) for the Lafayette Hotel. Not checked: every interior; the Opera House's hours came from search-result quotes of the Central Bank Center ticket page (the page answers 406); the Government Center's opening hours; Transylvania's campus parking. Red brick is '?' for nearly all: no source gave the brick's colour. The cemetery pin marks the Main Street entrance; the gatehouse could not be picked out under the trees. Eastern State Hospital is recorded "gone": Wikipedia says most of the old buildings were demolished by 2013 and only the administration and laundry buildings are left.

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Northern Bank Building | Lexington, KY: 249–267 West Short Street | Wikipedia's Downtown Commercial District list: 1890, H. L. Rowe, Victorian (it lists two addresses) | Which building it is, and a description |
| Southeast Greyhound Line Building | Lexington, KY: 101 West Loudon Street | National Register 2014 (13001048); the form calls it Moderne, brick | Whether it fits the Atlas's style rule; present use |
| Lexington jail of 1891 | Lexington, KY: East Short Street | The 1976 Lexington Cemetery Register form calls it Romanesque and "still extant" | Whether it still stands, and where exactly |
| Eastern State Hospital administration building | Lexington, KY (38.0825, -84.49794 is the hospital) | Wikipedia: the administration and laundry buildings are all that remain of the old campus | Which building, its date, and whether the public may look |

## Tips
- `wiki_raw.py --rows` has no "listings in Lexington" page: the Fayette County list ("National Register of Historic Places listings in Fayette County, Kentucky") holds the city's 185 rows.
- The courthouse article is "Old Fayette County Courthouse (Kentucky)"; "Fayette County Courthouse" is a disambiguation page.
- lexingtonoperahouse.com and centralbankcenter.com answer 406 to `page.py`; lexingtonky.gov node pages found by search were 404.
