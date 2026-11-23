# nd_wrkp: North Dakota: forts, ranch ruins, churches and bridges across the state
state: North Dakota
region: nd
date: 2026-11-23
places: 11
file: data_nd_wrkp.py

## What this batch is
Eleven places across North Dakota (Bowman, Divide, Billings, Cass, Grand Forks, Richland, Ward, Emmons counties and others) added to a state that had 38: Fort Dilts, Writing Rock, Roosevelt's Elkhorn Ranch (foundations only), the De Mores packing plant chimney, three small churches, two bridges, the Campbell log house and the Willows Hotel. Claimed with `choose.py --thinnest`. Sources: SHSND site pages, NPS Elkhorn pages, Grand Forks County Historical Society pages, the Buffalo city page, and Wikipedia via `wiki_raw.py` for the Register entries. Not checked: interiors, hours for the churches, the Campbell House, the bridges and the hotel (no page of the owner gave any; the Campbell House is `hours='?'`), whether the two bridges still carry traffic, ownership of the bridges. Pins were looked at on the aerial only; no LiDAR. The Buffalo church, Campbell House, Midway Bridge and the Coulee church pins are `site` or `area` because the building could not be picked out. Only one picture found (Chimney Park); Writing Rock has none on Commons that fits.

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Saints Peter and Paul Catholic Church Complex | Strasburg, ND (46.13611, -100.16167, Register list) | Register-listed church complex in Emmons County | Wikipedia has no article; no source read for dates or access |
| St. Stanislaus Church Historic District | Warsaw, ND (48.29472, -97.25306) | 1901 church by John W. Ross, rectory, academy, cemetery (Wikipedia) | Access and condition; only Wikipedia read |
| Icelandic Evangelical Lutheran Church (St. John's Ukrainian Orthodox museum) | Pembina, ND (48.96205, -97.24293) | Now a museum run by the Fort Pembina Historical Society (Wikipedia) | Hours and dates |
| Cedar Creek Bridge | near Haynes, ND (46.05056, -102.22694) | 1908 Pratt through truss, Twin City Bridge Co. (Wikipedia) | Whether it stands and the public road to it |

## Tips
- Wikipedia's county Register lists for small North Dakota counties often redirect to one long state list: `wiki_raw.py --rows` then returns the same ten rows for every county.
- history.nd.gov slugs: `dilts`, `writingrock`, `chateau`, `pembina` work; `stevenson`, `seward` and `writing` do not.
- NPS `planyourvisit/elkhorn-ranch-unit.htm` gives the road and trail details.
- When `build_sites.py` says a data file is not readable, an unescaped apostrophe in a string is the usual cause.
