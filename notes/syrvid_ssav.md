# syrvid_ssav: New York: downtown Syracuse and the university hill
state: New York
region: cny
date: 2026-11-24
places: 13
file: data_syrvid_ssav.py

## What this batch is
Thirteen standing buildings in downtown Syracuse and on the Syracuse University hill, taken from the names in one walking-tour video (Old World Exploration, "Old World Syracuse, NY"; the record is source/videos/20231117_mDgKOhAsoxU.md). The video was a tip only: every fact comes from Wikipedia read with wiki_raw.py (the Syracuse Register list with --rows and each building's article), Syracuse University Libraries' building-history pages (Crouse College, Hendricks Chapel, Lyman Hall), the Assumption parish's own history and Mass pages, the Landmark Theatre's own page, M&T Bank's January 2020 sale announcement (Gridley Building), a CNY Central report of July 2026 on the Mizpah's reopening, and an 1896 county history of the First Baptist Church. Downtown: City Hall, the 1907 courthouse, the Mizpah Tower, Hotel Syracuse, the Landmark Theatre, the Niagara Mohawk Building, the Syracuse Savings Bank, the Gridley Building and the Third National Bank. North Side: the Franciscan Church of the Assumption (the parish gives 1865 to 1872 and the Register district description about 1880; both are given, conf mixed). The university: Crouse College, Hendricks Chapel and Lyman Hall. All 13 pins were checked on the New York leaf-off aerial and sit on their buildings. Red brick was settled from sources or the article pictures for 12; the Assumption church is left '?', because its only Commons picture is captioned as the convent next door. NOT checked: interiors and whether visitors may go into the university buildings, City Hall's and the courthouse's office hours, the hotel's and the Mizpah's own pages, and Hendricks Chapel's service times (its site would not connect).

## Leads
Places you read about and could not finish. One row each.

| Place | Where | What is known | What is missing |
|---|---|---|---|
| Empire House (Voorhees House) | North Salina Street at Clinton Square, Syracuse, NY | An 1869 history (onondaga.nygenweb.net/hotels/empirehouse.html) says the brick hotel was rebuilt from 1843 and reopened in 1846 as the Voorhees House, later the Empire House | Whether any of it stands; a search summary said a Syracuse University page called it destroyed, but that page would not open |
| Manufacturers' building, New York State Fairgrounds | Geddes, NY | Named in a video only | Which building, and whether it stands |

## Tips
- Syracuse University Libraries' building pages (library.syracuse.edu/special-collections-research-center/university-archives/buildings/<name>/) give dates, architects, materials and later changes for each campus building and read in full with page.py --all.
- hendricks.syracuse.edu and hendrickschapel.syracuse.edu would not connect from page.py; syr.gov (City of Syracuse) answers 403; pacny.net's Mizpah page is 404.
- assumptionsyr.org is a Squarespace site: page.py reads /history and /mass, and the home page's source carries office hours in its openingHours field.
- The Register list's 1912 date for the Mizpah Tower differs from a Commons photo caption's 1914 (designed by Gordon Wright); neither the nomination nor another source was read.
