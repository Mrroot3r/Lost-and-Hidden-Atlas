# riprov_wssn: Providence County, Rhode Island: stone-enders, Slater mills and Woonsocket
state: Rhode Island
region: riprov
date: 2026-11-20
places: 16
file: data_riprov_wssn.py

## What this batch is
Sixteen places in Providence County, Rhode Island (region `riprov`, drawn at random by `choose.py`). Earlier passes took ruins; this one is mostly the oldest standing buildings: the three stone-enders (Eleazer Arnold House 1693, Clemence–Irons House 1691, Smith–Appleby House 1696/1702), the Daggett House (1685), the Saylesville Friends Meetinghouse (1703-04), Hearthside and the Moffett Mill on the Great Road, Old Slater Mill, Slatersville mill village, the Museum of Work and Culture and the St. Ann fresco church in Woonsocket, the Brown & Hopkins store in Chepachet, the Foster Town House, Mount Vernon Tavern, the Old Congregational Church in North Scituate, and one ruin, the Ramtail factory in Foster (from `LEADS.md`; its row is deleted). Wikipedia was read as raw text; hours from the owners' pages with `page.py` (NPS hours page, Friends of Hearthside, RIHS, St. Ann centre, Pawtucket DAR, Providence Friends, Smith-Appleby House, Brown & Hopkins). The Foster entries lean on the RI Historical Preservation Commission's Foster survey report (about 1982). Not checked: anything on the ground; Historic New England's own pages (HTTP 403), so the Arnold and Clemence–Irons houses have `hours='?'` with the season from Hearthside's page and Wikipedia in the access note; Brown & Hopkins gives no times; Foster Town House and the North Scituate church have no visiting times; who owns the Ramtail ruin (the federal map puts the point in a unit named "Barden Reservoir", owner type unknown, so it is `ask` and `conf='mixed'`). Moffett Mill's pin is the 585 Great Road address point (`site`); the mill itself could not be picked out under trees. Ramtail's pin is the Waymarking position; the LiDAR shows hollows and an old track there that fit the survey's foundations.

## Leads
Places you read about and could not finish. One row each; delete the example row. Leave the table header.

| Place | Where | What is known | What is missing |
|---|---|---|---|
| Cranston foundry ruins (Furnace Hill Brook Historic and Archeological District) | Cranston, RI | Wikipedia (NRHP 80000097): remains of an iron foundry of 1812 up Furnace Hill Brook, and Native sites partly destroyed by the I-295/Route 37 interchange in 1967; Commons has a category "Cranston Foundry Ruins" | Who owns the ground, a public way in and a coordinate; only listicle pages turned up |
| Ochee Spring Quarry | Johnston, RI | Wikipedia: Native soapstone (steatite) quarry on a privately owned outcrop behind 787 Hartford Avenue | Private; only a landowner's leave would make it more than a lead |
| Hopkins Mills village | Foster, RI | RIHPC Foster survey: 1700s mill hamlet on Old Danielson Pike with a c.1820 schoolhouse, 1869-71 Union Chapel, cemetery from the 1760s and the 1923 Dolly Cole bridge | A current source on what stands and who may visit |
| Valentine Whitman Jr. House | 1147 Great Road, Lincoln, RI | Friends of Hearthside: stone-ender of 1694, sold by the town to Preserve Rhode Island in 2019 for restoration; not open | Whether the restoration is done and any opening |

## Tips
- Historic New England's property pages (`historicnewengland.org/property/...` and `?p=` links) answer HTTP 403 to `page.py`, and the Clemence–Irons page has no archived copy; the Friends of Hearthside "visit-folder" page carried the Arnold House season and the Saylesville meeting house times.
- The RI Historical Preservation Commission's town survey PDFs (`preservation.ri.gov/.../survey_pdfs/<town>.pdf`) read with `page.py -n 400000`; search the cached copy in `research/pages/` with a short Python regex for one place's paragraph.
- The Wikipedia point for the Daggett House is 1.9 km off, outside Slater Park; `nom.py "Daggett House, Pawtucket"` gave the building.
- `publish.sh` stopped once because two batches merged while this one was being written; `resync.sh` then a fresh batch time, `all.sh` and `publish.sh` took about two minutes.
