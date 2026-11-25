# ks_frqt: Franklin County, Kansas
state: Kansas
region: ks
date: 2026-11-25
places: 14
file: data_ks_frqt.py

## What this batch is
Fourteen places in Franklin County, Kansas (Ottawa, Wellsville, Lane, Williamsburg, Overbrook), 45 to 55 miles south-west of Kansas City, where the Atlas had only the Ottawa Carnegie library. I went there because the Register lists for Jackson, Clay, Platte, Cass, Ray, Lafayette, Johnson (Kansas), Wyandotte, Leavenworth and Douglas counties had all been worked down to houses and districts: a check of each listing's coordinates against the Atlas found almost nothing left. Sources: the Kansas Historical Society register search for Franklin County (`page.py`), the Park Service's Register forms as text from NPGallery (`NRHP/GetAsset/NRHP/<ref>_text`, read for 11 of them), the Kansas Historical Society's 2017 and 2018 forms (Reid House, Appanoose church), Wikipedia articles (`wiki_raw.py`), and a web search for the Old Depot Museum's hours and for Silkville. Pins: Register or Wikipedia points checked on the 2024 Kansas aerial; three were moved (courthouse, Tauy Jones Hall, Ottawa High School) and three left as area (Hanway house, Pleasant Valley school, Appanoose church: no building could be picked out at the point). Not checked: the insides of every building, who owns the private ones now, present use of the Wellsville bank and the Ottawa schools, whether Walnut Creek Bridge still carries traffic, and hours for the Dietrich Cabin (only Wikipedia's "Sunday afternoons in summer", so `hours='?'`). The Old Depot Museum hours come from a search result quoting the society's page, which was not opened. Red brick for the Ottawa High School and the Appanoose and Wellsville entries comes from a picture or the form; the Ottawa school is `'?'`. Sources disagree on the Tauy Jones House date (1860 on the form, 1863 to 1867 on Wikipedia) and the Hanway house (about 1858 on the form, 1860 on its plaque); both entries are `conf='mixed'`.

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Eight Mile Creek Warren Truss Bridge | Osborne Terrace west of Main St, Ottawa (38.63111, -95.28556 per the Register list) | Listed 2003, a metal truss bridge (Metal Truss Bridges in Kansas thematic nomination) | The 2003 form on the Society's site is a scan with no text and NPGallery text was not tried; a description and whether the bridge still stands |
| Tauy Creek Bridge | Over Tauy Creek north of I-35, Ottawa (38.66472, -95.22306) | Listed 1990, metal truss bridge | The form is a scan; description and condition |
| Middle Creek Tributary Bridge | 5.8 miles west of Princeton (38.49222, -95.37583) | Listed 1985, masonry arch (Masonry Arch Bridges of Kansas) | A description; the Society's form is a scan |
| Tauy Baptist Church | Near Ottawa (38.6809, -95.2115) | Register reference 100010891, listed recently | Any description; no Society page or Wikipedia article found |
| Historic Ottawa Central Business District and Downtown Ottawa Historic District | Ottawa (38.615, -95.268) | Two listings (1972 and 2008); the 2008 form is 83 scanned pages | A readable description of what stands; the district would be a good `town` entry |

## Tips
- NPGallery text (`https://npgallery.nps.gov/NRHP/GetAsset/NRHP/<reference number>_text`) read for every Register form from 1972 to 2008 when the Kansas Historical Society's own PDF of the same form was only a scan; try it before calling a form unread.
- Kansas Historical Society pages link their nomination PDFs under `/resource/national_register/nominationsNRDB/`; the link names are in the page's HTML, not in `page.py`'s text, so pull them with a short `requests` call.
- To find ground the Atlas has not covered, compare a Register county list's coordinates with `build/sites.json` (nearest place over 300 m): around Kansas City the lists for the larger counties have nothing left except houses and districts. Franklin, Jefferson (Oskaloosa, Perry) and Linn counties in Kansas, and Clinton and DeKalb counties in Missouri, still have gaps; Jefferson County has Buck Creek School, the Oskaloosa Methodist church, two Delaware River bridges and Morris Harris Farmstead.
- `wiki_raw.py --rows "National Register of Historic Places listings in Jefferson County, Kansas"` returns a mixed list of many counties for some titles; filter the rows by coordinates.
