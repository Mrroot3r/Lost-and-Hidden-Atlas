# cte_jqlk: Windham County, Connecticut: Pomfret to Plainfield
state: Connecticut
region: cte
date: 2026-11-18
places: 15
file: data_cte_jqlk.py

## What this batch is
First real pass over region `cte` (Eastern Connecticut), drawn at random by `choose.py`; fifteen places in Windham County. Standing: the Brayton Grist Mill and the Israel Putnam Wolf Den (Mashamoquet Brook State Park, Pomfret), Old Trinity Church (1771, box pews) and the Unitarian Meetinghouse in Brooklyn, the Prudence Crandall Museum (Canterbury), Roseland Cottage (Woodstock), the Huntington Homestead (Scotland), the Windham Textile and History Museum with the Willimantic thread mills, the Elliottville Lower (Peep Toad) Mill, Cargill Falls Mill (Putnam), the Packerville stone arch bridge and dam and the Glen Falls lenticular truss (Plainfield), and the CCC lumber shed in Natchaug State Forest. Ruins and traces: the Old Furnace State Park iron furnace (Killingly) and the Daniel's Village mill site (Killingly). Sources: Wikipedia read with `wiki_raw.py` (the county's Register list with `--rows`), and with `page.py` the managers' own pages: ctparks.com (Mashamoquet hours), CT DECD (Crandall tours and fees), roselandcottage.org, huntingtonhomestead.org, oldtrinity.net, the Killingly Conservation Commission's Old Furnace page and walk leaflet, lhdct.org (Stone Road Historic Trail), and the CT Office of Tourism listings (ctvisit.com) for the Mill Museum and Huntington Homestead. Not checked: anything on the ground; Old Furnace daily hours and where the furnace remains are (the pin is the park lot, `prec='area'`); Natchaug State Forest hours; the Mill Museum's hours (its own pages are drawn by script); Roseland Cottage tour days and fees (Historic New England answered 403); whether the Brayton mill's interior opens and when; parking at the churches, the Huntington Homestead, the bridges and the private mills. Old Furnace's dates disagree (Wikipedia: before the Revolution to the mid-1800s; Killingly Conservation Commission: built 1831, 1830s-40s), so it is `conf='mixed'`. Brick from pictures opened with `brick.py look` for Cargill Falls (yes), the two Brooklyn churches (no), Roseland Cottage and the Huntington Homestead (some: brick chimneys); Crandall and the Mill Museum left at `?`.

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Willimantic Footbridge | Willimantic (Windham), CT (41.71167, -72.21361 in Wikipedia) | 1906 five-span steel truss footbridge over the river and tracks, National Register 1979. Wikipedia and a Yahoo News report: closed July 2025 for structural damage, replacement likely | Whether it has reopened, been replaced or come down in 2026 |
| Hemlock Glen Industrial Archeological District | Hampton, CT (no coordinate in Wikipedia) | Wikipedia: grist, saw, blacksmith, pin and spoon mill sites from about 1745 to 1925 on a Shetucket tributary; dams, a pond and foundations survive | Where it is and who owns the land; the Register list gives no coordinate |
| Nathaniel Lyon Memorial State Park | Eastford/Ashford, CT, in Natchaug State Forest | Wikipedia (Natchaug State Forest): a small state park round the birthplace of General Nathaniel Lyon | What is left of the birthplace (a waymarking page and HMdb marker 126541 not read) and a coordinate |
| Pineville Mill ruin | Killingly, CT (41.88114, -71.85859, OpenStreetMap ruin) | lhdct.org lists the "Pineville Factory" in the Stone Road Historic Trail district; the Killingly Historical Society's villages page names Pineville | A source on what is left, and who owns it |
| Wauregan Mill | Plainfield, CT (41.74389, -71.91056) | Wikipedia: H-shaped fieldstone mill of 1853 at the heart of a company village of over 100 workers' houses; C&M Corporation used it from 1974 | Its present use and a public viewpoint |
| New Roxbury Ironworks Site | Woodstock, CT | National Register 96000130, address restricted | A source saying the public may visit; do not pin from the list |

## Tips
- The DEEP page for Old Furnace State Park at `test-cd.ct.gov/deep/state-parks/parks/old-furnace-state-park` read in full but gives no hours; `ctparks.com/parks/old-furnace-state-park` gave nothing with `page.py --all`.
- The Killingly Conservation Commission's Old Furnace leaflet (`killinglyconservation.org/_files/ugd/f1f6b2_e011d001a1e243b7befc3159fb8071d3.pdf`) has a dated history of the furnace and the park address.
- `millmuseum.org` and `huntingtonhomestead.org` are drawn by script; the ctvisit.com listings for the same places read cleanly and give fees and days.
- `brick.py look` works on a new batch's ids as soon as `build_sites.py` has run, before publishing; one call in six (Prudence Crandall) saved no picture without saying why.
