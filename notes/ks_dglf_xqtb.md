# ks_dglf_xqtb: Douglas County, Kansas: leftovers
state: Kansas, Missouri
region: kcmo, ks
date: 2026-11-24
places: 10
file: data_ks_dglf_xqtb.py

## What this batch is
Ten places, a scheduled run aimed at the Kansas City area. I tried Johnson County, Kansas and Lexington and Lafayette County, Missouri first, and found them nearly used up: earlier sessions had taken almost every Register listing worth adding, and the Missouri forms are not on line (NPGallery gives a placeholder, mostateparks.com forms answered 404). Lawrence and Douglas County, Kansas still had Register listings not on the map, and Kansas forms read well. Added: the East Lawrence Industrial Historic District (red-brick warehouses), the Vinland fairgrounds, the Elmwood Stock Farm barn, the McQuillan, O'Sullivan and Sowers-Crawford farmsteads (all private working farms), the Oregon and California trail swales at Lawrence, Clinton's 1866 limestone school, the Merritt Insley House in Leavenworth, and Mount Washington School in Independence (brick, vacant since 2008 as of the 2013 form). Sources: Register forms read as text (Kansas Historical Society PDFs and NPGallery), the Society's register summaries, Douglas County's event page, the Lawrence Journal-World, Clio. Pictures come from Commons (the forms' own photographs are there under CC BY-SA). Not checked: anything on the ground, hours, whether any private farm can be seen from a road, present use of the Insley House, Mount Washington School and Clinton's hall. Pins: the Insley House and Clinton are area pins (the house and the hall could not be picked out on the aerial); Sowers-Crawford is the Register list point on a farmstead; the swales pin is the list point and the swales are too faint to see. Brick: Insley is 'yes' from a Commons photograph although the 1986 form said it was painted white; the rest are from forms or pictures opened, or '?'.

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Clinton Township Hall (Clinton School No. 25) | Clinton, KS (38.9117, -95.3906, village centre only) | 1996 Register form: limestone, "No. 25 erected 1866", township hall on township road 1180 N at 604 E; the Register's own point falls in Clinton Lake | Which building it is on the aerial; whether it is open |
| Parmenter Hall pictures and hours | Baker University, Baldwin City, KS | Already on the Atlas | Nothing to add; noted only because it was found twice |
| Houses in Lexington, MO (Catron, Cheatham, Gosewisch, Tevis, Stramcke, Spratt-Allen-Aull, Dinwiddie, Houx-Hoefer-Rehkop) | Lafayette County, MO | Register listings, with addresses on the Missouri State Parks list | A readable source for each; the forms are not on line and a web search found only list pages |
| Machpelah Cemetery | 900 S. 20th St., Lexington, MO | City page: first burial 1839, made a corporation in 1849, Saluda steamboat victims' mass grave, Register 2022 | Not added in this batch; ready to add from the city and chamber pages |
| Old West Lawrence, Pinkney I and II, Breezedale, Johnson Block historic districts | Lawrence, KS | Register residential districts | Sources beyond the Society's summaries; they are houses |
| Lee's Summit and Independence house districts (Bayles, Howard, Morningside and others), Georgen, Hughes and Lewis-Webb houses | Jackson County, MO | Register list | Readable forms and a reason to go |

## Tips
- Johnson County, Kansas and Lexington, Missouri are largely done: `tools/start.py` counts places, but compare the Register list rows to the map by coordinate, not by name (I first compared names and wrongly thought three places were missing). A name test misses ids that differ from names.
- The Kansas Historical Society's nomination PDFs (`kansashistory.gov/resource/national_register/nominationsNRDB/...`, linked from its register search pages) read well with `pypdf`; `page.py -g .` shows only a few lines of them. Forms from before about 2000 are mostly scans.
- Missouri Register forms are placeholders on NPGallery; the 2013 Mount Washington School form was an exception and read fine.
- A form's boundary points can fall in a lake (Clinton, Kansas): look at the aerial before trusting them.
- Commons holds the forms' own photographs for 2020s Kansas listings, geotagged, so `photo_find.py` finds pictures for farms and barns that have no Wikipedia article.
