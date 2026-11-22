# wny_vids: Rochester, NY: downtown landmarks, Mount Hope and the Genesee gorge
state: New York
region: wny
date: 2026-11-22
places: 13
file: data_wny_vids.py

## What this batch is
Thirteen standing places in Rochester, New York, taken from the names in one video about the city's old buildings (the record is `source/videos/20240120_G15MaIEaxSM.md`; the video was only a list of names, and every fact comes from a source opened here). Downtown: the Powers Building with the Powers Hotel, the Granite Building, City Hall (the old Federal Building), the Times Square Building, the First National Bank of Rochester (old Monroe County Savings Bank), the City Hall Historic District (old City Hall, Free Academy, St. Luke's, the county courthouse) and the Eastman Theatre; Kodak Tower in High Falls; the Main Street Armory; Mount Hope Cemetery; Rush Rhees Library on the University of Rochester campus; and, on the Genesee gorge, Maplewood Park and the Veterans Memorial Bridge. Sources: Wikipedia read as raw text (the Rochester Register list and each article), the New York State Military Museum's armory page, the National Park Service's Maplewood Park page, the Eastman School box office page and the University of Rochester libraries' hours page. Not checked: anything on the ground; every City of Rochester page (City Hall, Mount Hope, Maplewood, Ontario Beach) answered 403, so City Hall's opening hours, Mount Hope's gate hours and Maplewood's hours and parking are not given; who owns and uses each building in the City Hall district now; whether visitors may enter Rush Rhees Library without a university card; whether the Main Street Armory has reopened since 2024. Red brick is set only for the armory (from a Commons picture) and as "no" where the article names stone or terra cotta facing; the rest are "?". The Eastman Theatre pin is the Gibbs Street address on the school's block; which roof is the hall was not settled from the aerial.

## Leads
Places you read about and could not finish. One row each.

| Place | Where | What is known | What is missing |
|---|---|---|---|
| Ontario Beach Park (Dentzel carousel) | Charlotte, Rochester, NY | Monroe County's park page: 1905 Dentzel carousel installed in 1905 and still in place; park open 7 a.m. to 10 p.m.; HMdb 90327 on the resort era | A pin on the carousel; whether the old bath house is the present community centre |
| Fandango Tower foundations, Mount Hope Cemetery | Rochester, NY | Wikipedia: ruined foundations of the wooden observation tower remain in a kettle in the cemetery | Where in the cemetery; a second source |
| Hotel Seneca, Sagamore Hotel, Hotel Rochester, Savoy, Odenbach's | Downtown Rochester, NY | Named in the video; not researched | Whether any still stands |

## Tips
- Every cityofrochester.gov page tried answered 403 to `page.py`, with archived copies it could not fetch; Monroe County's pages (monroecounty.gov) read fine.
- `W()` from `data_ma` already returns a whole `[label, address]` link: wrapping it in `L()` breaks `photo_find.py new` with a TypeError.
- libcal.lib.rochester.edu/hours reads with `page.py` and gives a week-by-week table for every University of Rochester library.
