# syrchina_vggh: Syracuse China (Onondaga Pottery Company), Syracuse, NY
state: New York
region: cny
date: 2026-11-24
places: 2
file: data_syrchina_vggh.py

## What this batch is
Two places tied to Syracuse China (the Onondaga Pottery Company, "O.P. Co."), asked for by the owner for a follow-up visit on video: the site of the Court Street plant in Lyncourt (Town of Salina), opened 1921 or 1922 by the sources' two dates, closed by Libbey on April 9, 2009 and torn down in April 2012, now a commercial plaza; and the Onondaga Historical Museum at 321 Montgomery Street, which holds the company's archive and ware and has a permanent Syracuse China exhibit. Wikipedia was read with `wiki_raw.py`; every other page (the Onondaga Historical Association's history, programme and visit pages, a 2012 YNN article it keeps, Abandoned America, a 1996 DEC fact sheet on the plant's landfill, the Restaurant Ware Collectors Network) was read with the web fetch tool, because `page.py` could not connect to ordinary sites from this machine. Not checked: whether any building now on the plant site is a piece of the old plant (the address pin falls on a long standing building beside a cleared slab, so the plant pin is `area`); the plant address 2801 Court Street rests on Abandoned America quoting an older Wikipedia text and on the OpenStreetMap address point. Museum hours are the association's regular hours from its own page; it showed temporary longer hours through November 24, 2026, and its research centre was closed for renovation. Sehr Park's rules were not checked. The phone-size smoke test could not run (no Playwright browser here); GitHub's check runs it.

## Leads
Places you read about and could not finish. One row each; delete the example row. Leave the table header.

| Place | Where | What is known | What is missing |
|---|---|---|---|
| Onondaga Pottery Company, original West Fayette Street works | West Fayette Street, old village of Geddes (Syracuse west side), NY | The Onondaga Historical Association captions a photograph "Onondaga Pottery Company Factory on West Fayette Street" and calls it the original Fayette Street plant; ware made there carries its own style of date code (Restaurant Ware Collectors Network). Wikipedia says W. H. Farrar began a pottery in Geddes in 1841 and moved it seventeen years later to what became the Onondaga Pottery site | A street number or cross street and what stands there now. A Sanborn fire-insurance sheet of Syracuse would settle it; the Library of Congress map site kept serving a human check to this machine's browser |
| W. H. Farrar's first pottery, Geddes | Geddes, NY | Onondaga's Centennial (1896, on the county GenWeb site) says Farrar made red ware from Geddes clay and that the stoneware pottery later burned | Any location |

## Tips
- From this channel's cloud machine `page.py` could not connect to cnyhistory.org or other ordinary sites; the web fetch tool read them all.
- The Library of Congress (loc.gov) map pages showed a Cloudflare check in the remote browser and served a fresh check after it was ticked: count Sanborn sheets as unreachable from here.
- OpenStreetMap names the plant's entry drive Pottery Road (`osmnear.py ... highways`), a quick way to find the old works' ground.
- Wikimedia Commons has a 2018 photograph of 321 Montgomery Street described as the old Bell Telephone Building, home of the association; `photo_find.py look` found it 28 m from the pin.
