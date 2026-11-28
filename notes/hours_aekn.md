# hours_aekn: hours for 24 places of worship in Kansas and Missouri
state: Kansas
region: ks
date: 2026-11-28
places: 0
file: hours_aekn.py

## What this batch is
An "hours" session (PROMPTS.md type 7): no new places and no pins. New York had no church waiting, so the Kansas list (21) and then the Missouri list were worked. Five places got times from the page of whoever runs them, each read with `tools/hours.py page` and its address or town checked; nineteen are recorded `?`.

Hours recorded:
- Holy Trinity, Lenexa KS (trinity-lenexa.solutiosoftware.com Mass page): the Masses are in the newer main church; the page gives no times for the old stone chapel that the entry is about, so no `--open`.
- Antioch Christian Church, Kansas City MO (acckc.org, 4805 N Antioch Rd): service times; the page does not say whether they are held in the 1859 chapel.
- German Evangelical Lutheran church (Pirtle Winery), Weston MO (pirtlewinery.com): the winery's opening hours.
- Holy Trinity, Weston MO (the Diocese of Kansas City-St. Joseph's parish locator, 407 Cherry St).
- St. Peter's Episcopal, Harrisonville MO (stpetersharrisonville.com, 400 W. Wall St): Sunday 9:30 Holy Eucharist.

Not checked: nothing was seen on the ground and no telephone call was made.

## Pages that would not open, or gave no times
| Place | Page tried | What happened |
|---|---|---|
| Edgerton UMC KS | edgeumc.org | A namesake in Smithfield; no page of its own found |
| First Presbyterian, Clinton Parkway, Lawrence KS | fpclawrence.org | Would not connect; only directories found |
| Salem Lutheran, Lenexa KS | salemlenexa.org | Would not connect; only directories found |
| Assumption, Edgerton KS | theleaven.org decree | The archdiocese paper says Assumption parish merged with Sacred Heart, Gardner (2011, now Divine Mercy parish); no parish page with times found. Whether Mass is still said in the Edgerton church was not settled |
| St. Mary's, Strawberry Hill KCK; St. John the Divine, Argentine KCK | (two searches each) | Only aggregators; archkck.org's parish list answered 403 |
| Little Stranger Church, Leavenworth KS | squarespace page from search | 404 |
| St. Luke's Episcopal, Excelsior Springs MO | diowestmo.org parish list | The list gives no site for it |
| St. Ann, Excelsior Springs MO | kcsjcatholic.org locator | Not in the part of the locator that loads; stannparish.org is a namesake in Texas |
| First Methodist, Excelsior Springs MO; First Presbyterian, Independence MO | cloversites / oldfirstchurch.org | Namesakes (West Plains MO; Tallahassee) |
| Pilgrim Lutheran Church for the Deaf, KC MO | pilgrimcenterkc.org/pilgrim-chapel | Now "Pilgrim Chapel"; the page gives no times |
| First Methodist Eudora, Stony Point Lutheran, Appanoose Brethren, New Lancaster Grange, Radical UB Lecompton, Overland Park Presbyterian, former First Christian Manhattan (all KS) | the entry's own source | Private, an event venue, empty or no longer a church: no page of its own with visiting times |

## Leads not finished
Still waiting, tried once or not at all: Campbell Chapel AME Atchison, First Christian and Second Baptist Olathe, Welborn Congregational KCK, Old Presbyterian De Soto, St. Luke AME Lawrence (KS); Zion AME Lexington, Weston UMC, Old Presbyterian and Pleasant Ridge Baptist Weston, Linwood Presbyterian and Beth Shalom (Victorious Life) KC, Barbee Memorial Excelsior Springs, Lee's Summit Christian Church building, New Hope Primitive Baptist Richmond, First Swedish Baptist KC (MO).

## Tips for the next session
- `tools/hours.py page` missed "9:30 o'clock" on the St. Peter's Harrisonville page (no a.m./p.m.); when a page shows nothing, read the kept copy in research/pages/ before giving up.
- The Kansas list left is mostly small congregations with no website; the diocese and conference pages are the better bet than web searches.
