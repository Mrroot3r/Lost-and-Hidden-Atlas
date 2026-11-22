# albco_wtnh: Albany County hilltowns: Berne, Knox, Westerlo and New Scotland
state: New York
region: albco
date: 2026-11-22
places: 14
file: data_albco_wtnh.py

## What this batch is
Fourteen places in the Helderberg hilltowns (Berne, Knox, Westerlo) and the farm country of New Scotland and Bethlehem, drawn at random by `choose.py --state ny` (region `albco`). Berne: the Town Hall in the old Upper Hotel (1824; whether the present building is the 1824 hotel or a rebuilding after the 1914 fire is not settled), the hamlet with its Fox Creek mill sites and surviving hotel and store buildings, the West Mountain Methodist Episcopal church ruin (1888) and cemetery, the Baptist Church Burying Ground on Peasley Road, Partridge Run's bought-out hill farms (pin is the DEC Beaver Road lot) and Switzkill Farm (Albany County since 2025). Knox: the Saddlemire Homestead museum (1885), the hamlet on Route 156 and the Sholtes Dutch barn (`conf='lead'`: only the marker; the barn was not picked out). Westerlo: the Quaker meeting site of 1803 (marker; burying ground not seen on the aerial). New Scotland and Bethlehem: the Union Dutch Reformed Church (1825) with its 1840 horse shed, the David Allen stone house and Lime Kiln Farm, Smoke House Hill Farm and the Rowe Farm. Sources: HMdb marker pages and Altamont Enterprise articles through `page.py`; albanyhilltowns.com through the web fetch tool (`page.py` cannot connect); Wikipedia through `wiki_raw.py`; DEC property pages and the Helderberg unit management plan; the Mohawk Hudson Land Conservancy's 2021 Switzkill page. Not checked: any place on the ground; whether the West Mountain church still stands (the hilltowns pages are undated); hours for the Berne museum and library (the town page sends readers to a library page not found) and for the Saddlemire museum beyond "special events in summer"; Switzkill's access rules under the county; the Union church's regular service times; parking in Berne hamlet. Several entries (Knox barn, Smoke House Hill Farm, David Allen house, Quaker site) rest on one marker each. Every pin was looked at on the leaf-off aerial and LiDAR; the Rowe Farm pin was moved from a field to the nearest farmyard, which was not proved to be the Rowe farmyard. No Commons pictures fit any of the new places.

## Leads
Places you read about and could not finish. One row each; delete the example row. Leave the table header.

| Place | Where | What is known | What is missing |
|---|---|---|---|
| Brate's Hotel ruins | Berne, NY, Cass Hill Road at Duck Hill Road (geocoder 42.57434, -73.99641, near Reidsville) | albanyhilltowns.com "Brate's Hotel": built and run by Charles and Nancy Smith Brate; "portions of the hotel can still be seen in the woods" | Dates, owner of the woods, a look at the spot on the aerial/LiDAR |
| West Mountain Methodist church, standing or fallen | Berne, NY (42.58309, -74.17507) | Added as `west-mountain-me-church-ruin` from undated pages | A dated photograph or visit |
| Helderberg Grange hall and the 1851 Methodist church, Knox | Knox, NY (hamlet, Route 156) | albanyhilltowns.com "Historic Homes (Knox)": grange "now abandoned", private; Methodist church of 1851 "now abandoned", across from old District School No. 2 (firehouse) | Which buildings they are; a second source |
| Bradt Hollow School (District No. 17) | Berne, NY, Bradt Hollow Road | albanyhilltowns.com: built about 1860, refurbished for the Bicentennial, sometimes used for school demonstrations | A coordinate and owner |
| Alcove Historic District | Coeymans, NY (42.46944, -73.92667) | Wikipedia: 14-acre district, eight contributing buildings (1980); the Valley Paper Mill chimney is already on the Atlas | The Register form (NPGallery gives only a placeholder) to say what else stands |

## Tips
- albanyhilltowns.com still refuses `page.py` but the web fetch tool reads it; its "Berne - Then and Now", "Berne visitor attractions and facilities", "Churches of the past" and "Historic Homes (Knox)" pages list building by building what stands.
- The Altamont Enterprise `node/<n>` addresses read in full with `page.py --all` (no paywall met on four articles).
- `tools/geo.py` wants a JSON object of `{key: query}` (a list fails) and an output file as a second argument (without it, it crashes after printing).
- HMdb's nearby list for a hilltown returns many one-line 1932 state markers; they make leads but seldom a place on their own.
