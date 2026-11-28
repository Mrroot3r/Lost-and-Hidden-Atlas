# bridgeport_wejf: Connecticut: old downtown Bridgeport
state: Connecticut
region: ctsw
date: 2026-11-28
places: 11
file: data_bridgeport_wejf.py

## What this batch is
Eleven standing buildings in downtown Bridgeport and just west of it, from a "videos" session: the names came from one Old World Exploration video (record: source/videos/20260130_5LQ7Pk4bYig.md, 50 names; the captions ran to 27:49 of a 28-minute video, so the whole video was read). The video was used only as a list of names. Added: the Barnum Museum, McLevy Hall (the 1854 city hall and courthouse), the 1888 Fairfield County Courthouse, the Palace and Majestic Theaters with the Savoy Hotel, the Sterling Block and Bishop Arcade, the Court Exchange Building, the 1917 Bridgeport Savings Bank, St. Augustine Cathedral, St. John's Episcopal, the First Baptist Church and the old United Congregational Church (now the Bridgeport Islamic Community Center). Sources: Wikipedia read with wiki_raw.py, the Park Service record of the Downtown South district (form.py; its form text is only photo captions), historicbuildingsct.com for the Court Exchange, the savings bank and First Baptist, the Barnum Museum's own page (closed, aiming to reopen in 2030), and the Cathedral Parish's and St. John's own pages for service times (St. John's page reset page.py and was read with the web fetch tool). Not checked: anything on the ground; the present state of McLevy Hall's restoration; the Palace and Majestic's owner; which corner of Main and State holds the 1917 bank (pin marks the crossing, conf mixed); First Baptist's services (no page of its own found); the Arcade's hours; red brick for most places (no source gave the colour). Downtown places have no parking point: the mapped "lots" near them looked like rooftops on the aerial.

## Leads
Places you read about and could not finish. One row each; delete the example row. Leave the table header.

| Place | Where | What is known | What is missing |
|---|---|---|---|
| City Savings Bank (1914) | 944 Main Street, Bridgeport, CT | Park Service district record photo caption; a Commons photo says Warren R. Briggs, 1914 | A source for its story and present use |
| Columbia Phonograph factory | Bridgeport, CT | Named in the video only | Address, a source, and whether it stands |
| Warner Brothers Corset Company factory | Bridgeport, CT | Named in the video only | Which buildings stand, and a source |
| Beardsley Park | Bridgeport, CT (41.2125, -73.1822) | Register-listed Olmsted park (98000357); the zoo is in it | What old structures there are to see |

## Tips
- Downtown Bridgeport: parking.py offered mapped "lots" on Middle Street, Arch Street and Washington Avenue that look like rooftops or buildings on the 2023 aerial; look before using one as th=.
- historicbuildingsct.com reads well with page.py --all and names architects and builders for buildings Wikipedia lacks.
- saintjohnsbridgeport.org resets page.py; the web fetch tool read it.
