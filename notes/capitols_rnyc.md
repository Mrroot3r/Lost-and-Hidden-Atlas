# capitols_rnyc: State capitols, working and former
state: every state but North Dakota (already on the map)
region: one place or two in each state's capital region
date: 2026-11-20
places: 70
file: data_capitols_rnyc.py

## What this batch is
The owner asked for "the capitol buildings for every state ... and even former capitol buildings". Forty-nine working capitols (North Dakota's was on the map; New York's replaces the thin pin `lm-new-york-state-capitol`) and twenty-one former capitol buildings that still stand. Sources were Wikipedia only: its list of state and territorial capitols (names, addresses, years, coordinates), the article for each building, the members of its category "Former state capitols in the United States", and its National Register list for northern Boston for one coordinate. They were read with a small script that printed each article's infobox, opening paragraph and the sentences about materials and visiting. Every pin was looked at on the aerial; seven were moved onto their buildings and twelve are marked `site` or `area` because the building could not be picked out.

NOT checked: no capitol's own visitor page was opened, so there are no hours (`hours='?'` on the 32 places an article says visitors go into) and a capitol is `view` wherever its article says nothing about visiting, though most working capitols do admit the public. Parking was not looked up for any of them and there is no `th=` point. The colour of brick was recorded only where an article states it (`brick='?'` on 44). Interiors are from the articles or "not checked".

## Leads

| Place | Where | What is known | What is missing |
|---|---|---|---|
| Assembly Hall | Washington, MS (31.57917, -91.29778) | A tavern of 1808, on the National Register; Wikipedia files it under former state capitols | The article's opening does not say when the legislature met there; read the rest |
| Constitution Hall | Topeka, KS | A two-storey native stone building begun in 1855 where the Topeka Constitutional Convention met; Wikipedia files it under former state capitols | A coordinate (the article gives none) and what stands today |
| White Horse Tavern | Newport, RI (41.49139, -71.31375) | Built before 1673, said to be the oldest tavern building in the country; filed under former state capitols | The article's opening does not say how it served the colony's government |
| First Minnesota State Capitol | Saint Paul, MN (44.9496, -93.0976) | Filed under former state capitols | Whether anything stands; the article's opening could not be read by the script |
| North Carolina State House | Raleigh, NC (35.7804, -78.6391) | Built 1792–1796, burned in 1831; the present Capitol is on the same square | Nothing stands: a "gone" entry only if a marker is confirmed |
| Territorial Statehouse | Fillmore, UT | Remembered as Utah's territorial capitol, now a state park museum | Not read in this session: no article under the title tried |
| Other former capitols not in Wikipedia's category | Monterey CA (Colton Hall), Golden CO, Prescott AZ, Guthrie OK, Kingston NY (Senate House), Chillicothe OH, New Castle DE, Annapolis MD, St. Mary's City MD | Remembered, not read | Everything: open a source for each before adding it |

## Tips
- The hours job will find the 32 open capitols by itself: `hours='?'` in a place entry does not stop `tools/hours.py` from listing it.
- Wikipedia's list coordinate for a capitol is often 40 to 60 m off the building, on the lawn in front: look at every one.
- Most working capitols are open to visitors on weekdays, but that has to come from each capitol's own page; the ones marked `view` here are the ones to upgrade.
