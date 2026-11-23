# ne_wkpm: Nebraska: a third scatter across the state
state: Nebraska
region: ne
date: 2026-11-23
places: 11
file: data_ne_wkpm.py

## What this batch is
Eleven places across Nebraska, which had 45 before and has 56 now: Fort Atkinson (Fort Calhoun), the Genoa Indian school, the Bordeaux Trading Post / Museum of the Fur Trade (Chadron), the William Jennings Bryan House (Lincoln), the Picotte hospital (Walthill), the Midwest Theater (Scottsbluff), the Harold Lloyd birthplace (Burchard), the Pawnee County Courthouse, the Bell Bridge (Valentine), the Burlington Depot (Red Cloud) and Ash Hollow. Facts come from National Register and Landmark forms read as text from NPGallery with page.py, the Museum of the Fur Trade's own visit page, the Friends of Fort Atkinson page, and Wikipedia for outlines. history.nebraska.gov and outdoornebraska.gov answered 403, so state-site hours were not read (hours='?'); only the fur-trade museum has hours. Nothing was seen on the ground. Not checked: whether the Bryan House, the Picotte center, the Genoa museum and the Midwest Theater are open now, the Harold Lloyd house's owner, parking at most places, the Bordeaux post's date (1837 founding vs 1845-46 building, both given), and the exact spot of Ash Hollow's wagon ruts (the pin is the cave). Three Register points fell in fields or on a railroad yard (Bordeaux, Picotte, Burlington Depot) and were moved to street-address or OpenStreetMap points; Fort Atkinson's was moved onto the reconstructed walls. Red brick: the Genoa shop building is 'some', the Pawnee courthouse 'no' (tan brick), wood or steel places 'no', the rest '?'. Four photographs were chosen with photo_find.py; the Bell Bridge has none on Commons.

## Leads
Places read about and not finished.

| Place | Where | What is known | What is missing |
|---|---|---|---|
| Dry Valley Church and Cemetery | Mullen vicinity, Cherry County, NE (42.263889, -101.086111, Register list) | On the National Register (07000660) | The NPGallery form is a placeholder; no source read |
| Spade Ranch Store | Ellsworth, Sheridan County, NE (42.059444, -102.281111, Register list) | On the National Register (10000629) | No source read |
| Robidoux Pass | Gering, NE (41.808889, -103.836667, Register list) | National Historic Landmark on the Oregon Trail, 1848 to 1851 | A source on what is there and the public way in |
| Valentine Public School | Valentine, NE (42.87541, -100.54702, Register list) | Now a museum (Register list) | A page with hours |
| Red Cloud Opera House and the Cather town buildings | Red Cloud, NE | Webster County has 37 Register rows | Only the depot was done |

## Tips
- NPGallery's text route read Landmark and Register forms for Nebraska well (Fort Atkinson, Picotte and Bryan are NHL forms under NHLS); the Dry Valley Church form is a placeholder.
- `page.py --all` on furtrade.org/visit gave the hours and admission; the home page line was cut short by `-g`.
- Register coordinates in Nebraska fell off the building three times in eleven; the street-address point from `geo.py` and OpenStreetMap's museum point were right.
- OpenStreetMap lists the Red Cloud depot at 437 S Seward Street, Commons at 238 N Seward Street: the pin is on the building, the street number is not settled.
