# hours_asze: hours for the last 7 waiting churches and 18 museums, historic sites and theatres
state: New York
region: ny
date: 2026-11-22
places: 0
file: hours_asze.py
tidied: 2026-11-26

## What this batch is
An "hours" session (PROMPTS.md type 7): no new places and no pins. All seven places of worship still waiting anywhere (three in New York, two in Iowa, one each in Kansas and Tennessee) were looked up; with no church left, 18 others from `tools/hours.py list` (museums, house museums, historic sites, a capitol, theatres) followed. Nine got hours from the page of whoever runs them, read in the session; sixteen are recorded `?`.

Hours recorded:
- Basilica of Saints Peter and Paul, Chattanooga: the parish's own site (26886.sites.ecatholic.com/mass-times) gives the church open for prayer daily 7:30 a.m. to 5:30 p.m. The text read gave no Mass times and no street address; the site was matched to the basilica by its search result. A person may want to confirm.
- Cathedral of the Epiphany, Sioux City: the parish's own site (sccathedral-org.sites.ecatholic.com) gives "Cathedral Church Hours" under 1003 Douglas Street (the parish's Epiphany Center is 1000 Douglas Street). No Mass times were in the text read.
- Old State House, Little Rock (oldstatehouse.com, 300 W. Markham); Tennessee State Capitol (the Tennessee State Museum's page on tn.gov: guided tour times); Fort Henry, Kingston (forthenry.com admissions page: main season only, closed now, reopening spring 2027); Sarah Whitman Hooker House (its own site: tours by appointment); Historic Homestake Opera House, Lead (its own site: Schedule a Tour, plus events); Boulton Historic Site (Jacobsburg Historical Society's Hours & Directions page: open during special events May to December).
- The ecatholic.com parish sites refuse `tools/hours.py page` (HTTP 403); they were read with the web fetch tool, which took about five minutes and was refused on a second page of the same site.

Not checked: nothing was seen on the ground and no telephone call was made. No church was found to be closed or sold.

## Pages that would not open, or gave no times
| Place | Page tried | What happened |
|---|---|---|
| Gallatin Reformed (Gallatin Community Church), Gallatinville NY | millertonnews.com article; web searches | No page of the congregation's own found |
| Linlithgo Reformed Church, Livingston NY | rca.org; web searches | No page of its own found; whether it still holds services is unknown |
| Glenco Mills Methodist Chapel NY | nylandmarks.org | Preservation grant page only; no owner's page |
| First Congregational (former), Sioux City IA | web searches | No page found for Iglesia Evangelica Pentecostes Principe de Paz |
| Niotaze Methodist Episcopal, Kansas | umc.org finder | 404; no page of its own |
| Minuteman Delta-09 silo SD | nps.gov/mimi hours page | Hours drawn by script; the Delta-09 page says only that visitors can tour the site daily (the hours tool wants clock times) |
| Willard Bunnell House, Homer MN | winonahistory.org tour page | "Select days during the summer months", 0 events listed; no times |
| Batoche NHS SK | parks.canada.ca hours page | Drawn by script; says only "closed for the season" |
| Cove Point Lighthouse MD | calvertmarinemuseum.com | Only the museum's own hours (Solomons), not the lighthouse's |
| Fordyce Bathhouse AR | nps.gov/hosp hours and Fordyce pages | Visitor center hours not in the page text |
| Alley Spring Mill MO | nps.gov/ozar hours and fall/winter pages | No mill hours in the text |
| Frontier Drugstore Museum, Guthrie OK | drugmuseum.org | Own site has address and phone, no hours |
| Copshaholm, South Bend IN | historymuseumsb.org | HTTP 403 |
| Nikkei Internment Memorial Centre BC | newdenver.ca | HTTP 403, no archived copy |
| Hagood Mill SC | hagoodmill.net | Would not connect |
| Loyalist House, Saint John NB | (loyalisthouse.com, only an old archived copy) | No current page of its own found |
| Barter Theatre VA | bartertheatre.com visit and FAQ | Box office phone only, no hours in the text |

## Tips for the next session
Folded into `GUIDE.md` and the tools on 2026-11-26 by the tidy job (3 tips).
