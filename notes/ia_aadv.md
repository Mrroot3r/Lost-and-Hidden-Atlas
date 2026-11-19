# ia_aadv: Iowa: a first scatter
state: Iowa
region: ia
date: 2026-11-19
places: 15
file: data_ia_aadv.py

## What this batch is
Fifteen places scattered across Iowa, which had one (the Hurstville lime kilns): Motor Mill, Fort Atkinson, Montauk, the Dubuque Shot Tower and the Wapsipinicon Mill in the northeast; the Pine Creek Gristmill and the Old Capitol in the east; the Van Buren County Courthouse and Bentonsport in the southeast; the Roseman covered bridge, Terrace Hill and the Buxton marker in the middle and south; the Squirrel Cage Jail and the Woodbury County Courthouse on the Missouri; the Park Inn Hotel in Mason City. Mostly standing places, chosen as the best-known old buildings worth a trip in each corner; Fort Atkinson is part original, part rebuilt. Facts from Wikipedia read with `wiki_raw.py` and from the managing bodies' pages read with `page.py` (Iowa DNR, State Historical Society of Iowa, Clayton County Conservation and motormill.org, Buchanan County Historical Society, Historical Society of Pottawattamie County, Old Capitol Museum, Terrace Hill, Wright on the Park, Woodbury County, Villages of Van Buren and its Bentonsport walking-tour PDF, Madison County Tourism, Iowa DOT), and HMdb for the Shot Tower and Buxton. Not checked: hours for the Old Capitol (its pages list events only) and the Woodbury County Courthouse (`hours='?'`), the Van Buren courthouse's business hours (no times given); whether the Shot Tower's inside opens and who owns it; parking at the Roseman bridge, Montauk, Bentonsport and the Squirrel Cage Jail; red brick for Montauk and the Park Inn (black-and-white photographs only), Terrace Hill (Wikimedia refused the picture twice), Bentonsport and the Buxton marker. Buxton is pinned at its state marker in Lovilia, not at the townsite. Nothing was seen on the ground.

## Leads
Places you read about and could not finish. One row each; delete the example row. Leave the table header.

| Place | Where | What is known | What is missing |
|---|---|---|---|
| Buxton townsite ruins | Monroe County, IA, east of Lovilia (Wikipedia 41.15833, -92.82111) | National Register 1983; Wikipedia says a few structures remain as ruins, land mostly forest or farm | Owner and any public way in; which ruins and where (the Register form, ref 83000392, was not read) |
| Kate Shelley High Bridge (Boone Viaduct, 1901) | West of Boone, IA | Wikipedia: Union Pacific built a new bridge beside the old span in 2006 to 2009 | Whether the 1901 bridge still stands and where it can be seen from legally (Kate Shelley park, Moingona) |
| Amana Colonies | Iowa County, IA | Not read in this session | Everything; a strong candidate for a second Iowa batch |
| Hotel Manning | Keosauqua, IA | Named in the Van Buren courthouse article as built by Edwin Manning, on the Register | Its own source, status and hours |

## Tips
- Iowa DNR park pages (`iowadnr.gov/...`) and history.iowa.gov read in full with `page.py --all`; both give hours plainly.
- oldcap.uiowa.edu (Old Capitol Museum) is drawn by script; its visit pages give only the events calendar, no opening hours.
- Wikipedia's coordinate for the Pottawattamie County (Squirrel Cage) Jail is about 2 km north of the building; the ArcGIS PointAddress for 226 Pearl Street is on it.
- `parking.py`'s lot point at Motor Mill fell in trees on the aerial; the Montauk lots it lists are all in Clermont town, 700 m and more away.
- `pincheck.py --lidar` for 15 pins ran past the two-minute shell timeout: run it in the background.
