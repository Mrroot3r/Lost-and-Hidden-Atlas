# asylum_newe_zlwt: State hospitals and asylums, New England
state: Connecticut, Maine, Massachusetts, New Hampshire, Rhode Island, Vermont
region: bos, cte, cthv, ctsw, mec, men, mes, nhs, nshore, riprov, south, vtc
date: 2026-11-28
places: 17
file: data_asylum_newe_zlwt.py

## What this batch is

Seventeen state hospitals, state schools and two famous private asylums in Connecticut (Connecticut Valley Hospital, Norwich, Fairfield Hills, Mansfield, Southbury), Rhode Island (Butler), New Hampshire (Concord), Vermont (Brandon), Maine (Augusta, Bangor, Pineland) and the Massachusetts ones the Atlas lacked (Taunton, Foxborough, Wrentham, Boston State, McLean, Tewksbury). Sources: Wikipedia's article on each; the Park Service's National Register record and form for thirteen of them (read with the form tool, the Massachusetts forms after joining their spaced-out letters); the Rhode Island nomination and SAH Archipedia for Butler; and current news or the operator's own page for status, sales, demolitions and hours (Patch, the Newtown Bee, Seven Days, Mainebiz, Informed Infrastructure, GBH, Mass.gov, GlobeSt, the Public Health Museum, Pineland Farms, Mass Audubon). Not checked: the brick colour wherever a form says only "brick" (Butler, Mansfield, Southbury, Brandon, Bangor, Pineland, Concord, Augusta's pavilions: all left '?'); which part of the Concord campus is the 1842 Main Building, and Shew Hall's exact building at Middletown (both pins are site precision); the Wrentham Administration Building's spot; the footprint of Taunton's demolished Kirkbride (the pin is on the working campus, area precision); whether Foxborough's 1924 Administration Building still stands; the present state of the Norwich buildings beyond the Administration Building (Wikipedia's 2021 list is uncited). No photos were looked for.

## Leads

| Place | Where | What is known | What is missing |
|---|---|---|---|
| State Hospital for the Insane / State Institutions at Howard (Pastore Center) | Cranston, RI | Rhode Island's state survey: asylum for the incurable insane opened on the Howard farm November 9, 1870, renamed State Hospital for the Insane 1897; Center Building 1888–90 (granite, Stone, Carpenter and Willson), Benjamin Rush (1936, Franklin R. Hindle), Pinel and Dix buildings; five structurally failing buildings at 600 New London Avenue torn down 2025–26 | Which surviving building was the asylum's (the survey calls the Center Building both the almshouse and the core of the 1880s insane buildings); which five were demolished; a pin |
| Laconia State School | Laconia, NH | Named in the task as a candidate | No Wikipedia article under the obvious titles; needs a source for dates, buildings and present state |
| Gardner State Hospital (Gardner State Colony) | Gardner, MA | Wikipedia: closed 1975, now North Central Correctional Institution | Everything else; an active prison, so view only |
| Connecticut Valley Hospital Cemetery | Middletown, CT | Established 1878 (Wikipedia) | Its own article and access were not read; would need apart= with the hospital |
| Webber Cemetery, Malaga Island reburials | New Gloucester, ME | Wikipedia (Pineland Farms): graves from Malaga Island moved to the back of the cemetery on Intervale Road in 1912 | Access and the memorial were not read |

## Tips

- The Massachusetts Register forms (Taunton, Foxborough, Wrentham, Tewksbury) come out of the form tool with a space between every letter; `re.sub(r'(?<=\b\w) (?=\w\b)','',text)` makes them searchable.
- OpenStreetMap names the buildings on several campuses (Augusta, Pineland, McLean, Mansfield, Butler): `osmnear.py <lat> <lon> 700 buildings -g 'name='` found the right building faster than the aerial.
- The Wrentham Register form names mutules and triglyphs on the Administration Building: recorded as Legos from the form's words.
- preservation.ri.gov PDFs do not open with page.py from here; the web fetch tool reads them.
