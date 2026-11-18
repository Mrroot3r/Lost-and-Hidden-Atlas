# cat_qazp: Delaware County, NY: Andes, Roxbury, Margaretville, Delhi and the covered bridges
state: New York
region: cat
date: 2026-11-18
places: 20
file: data_cat_qazp.py

## What this batch is
Twenty places in Delaware County, New York (region `cat`, drawn at random by `choose.py`, which offered Andes, Roxbury and Delhi); the Atlas had only the Pepacton villages nearby. Nearly all standing: the Andes depot and rail trail, the Hunting Tavern Museum, the Old Stone School (District 10) by the Pepacton, the Kelly Round Barn, three Old School Baptist meeting houses (Halcottsville, Roxbury's "Yellow Church", Denver-Vega), Woodchuck Lodge with Boyhood Rock, the Jay Gould Memorial Church (Tiffany windows), the Roxbury depot and mill complex, the Fleischmanns synagogue and Skene library, the Galli-Curci Theatre, Hanford Mills Museum, Fitch's, Hamden and Downsville covered bridges with the pinnacled East Delhi church, the Delhi courthouse square, and the Rock Rift fire tower above the drowned Rock Rift valley (old NY 10 and the O&W bed on the way). Sources: Wikipedia raw text and the county Register list (`wiki_raw.py`); with `page.py` the Hanford Mills, NY State Parks, Woodchuck Lodge trust, Andes Society, Town of Roxbury history, Historical Society of Middletown, Bnai Israel, Tiffany census, Catskill Mountain Club, CNY Hiking, FLT hike sheet and Watershed Post pages. Every pin was looked at on the leaf-off aerial (four moved with `pix.py`, Skene library re-pinned from OpenStreetMap 165 m from Wikipedia's point). Not checked: any interior except where a page describes it; hours for the Roxbury depot museum, Galli-Curci shop, Skene library, Delhi courthouse, the Stone School and the Pakatakan market at the round barn; whether walkers may cross the Downsville bridge since its May 2026 closure to cars; whether the Rock Rift cab can be climbed and NYC DEP rules on that tract; owners of the Halcottsville and Second Roxbury Old School Baptist churches and the East Delhi church. Brick is `?` where no source said and no picture was opened (station, tavern, school, depot, Hanford Mills, Galli-Curci, courthouse, Denver church). The Woodchuck Lodge tour days disagree between State Parks and the lodge trust; both are given.

## Leads
Places you read about and could not finish. One row each.

| Place | Where | What is known | What is missing |
|---|---|---|---|
| Pleasant Valley Meeting House | Tremperskill Road / County Route 1, Andes, NY | Andes Society page: c. 1854 Methodist church and dining hall at the mouth of the Pepacton, bought and restored by the society in 1996, open June to September for events | A coordinate (geocoder and nom.py found nothing) and visiting hours |
| Highmount ski area | Highmount, NY (OpenStreetMap ruin leads "Lift 4", "Poma 5", "T-Bar 3" near 42.14, -74.52) | Abandoned ski lifts mapped as ruins next to Belleayre | Any readable source (unofficialnetworks.com 403) and the owner |
| Judge Gideon Frisbee House (Delaware County Historical Association) | Delhi, NY (42.29917, -74.89139, Wikipedia) | c. 1798 Federal house, DCHA headquarters and museum, NRHP 1976 | dcha-ny.org answers 403 to page.py: hours and what is open |
| McArthur-Martin Hexadecagon Barn | Bloomville, NY (42.37167, -74.78083) | 1883 sixteen-sided barn, 100 ft across, NRHP 1984 (Wikipedia) | Owner and whether it can be seen from a road |
| Pakatakan Artists Colony | Arkville, NY (42.1425, -74.625) | 33 Shingle Style studios and cottages round the 1886 Hoffman House, NRHP 1989 (Wikipedia) | Whether any of it is seen from a public road; all private |

## Tips
- dcha-ny.org (Delaware County Historical Association) answers 403 to `page.py` with no archived copy.
- In Delaware County several Wikipedia coordinates sit on the river beside a covered bridge (Fitch's, Downsville) or 165 m off (Skene library); `nom.py` gave the right building every time it found one.
- `check.py` refuses `burial` as a tag (the series tag is `cemeteries`); the guide's tag list in section 4 has no `burial`, but the category list does, which is easy to mix up.
- `places_test.js` still fails only on `onesquethaw-valley` ("18th century"), as the adk_gvry note said; this batch changes nothing it reads.
