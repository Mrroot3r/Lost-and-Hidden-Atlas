# mes_vpdi: Southern York County, Maine: forts, garrisons, mills and the old village of York
state: Maine
region: mes
date: 2026-11-18
places: 16
file: data_mes_vpdi.py

## What this batch is
Sixteen places in southern York County, Maine (region `mes`, drawn by `choose.py`): Fort McClary, the Fort Foster batteries, the Conway Junction turntable pit, the Perkins tide mill site, the First Congregational Church and Lady Pepperrell House at Kittery Point, the Old York Gaol, York Corner Schoolhouse, John Hancock Warehouse, McIntire Garrison and Nubble Light in York, Hamilton House with Vaughan Woods and the Portsmouth Company Counting House in South Berwick, the Old Grist Mill and bridge in East Lebanon, Laudholm Farm in Wells and the Alfred Shaker village. Wikipedia was read as raw text (`wiki_raw.py`), Register forms as PDF text from npgallery (turntable, Laudholm), and access from maine.gov park pages, the Town of Kittery's Fort Foster page, Old York's admission page, the Kennebunkport Conservation Trust, Wells Reserve and the Maine Coastal Program's Coastal Public Access Guide (South Berwick to York, May 2026), all through `page.py`. Brick was set from Wikimedia photographs fetched with `brick.py look` (Laudholm and Alfred left '?': no usable photograph). Not checked: anything on the ground; Historic New England's hours for Hamilton House (403); the Counting House Museum's and Alfred Shaker Museum's hours; whether the Hancock Warehouse opens; the turntable parcel's owner (the scanned form is unclear); which Shaker buildings stand; Wells Reserve fees. Pins at site precision because the building itself was not picked out: Lady Pepperrell, Old Gaol, Schoolhouse, Hancock Warehouse, McIntire Garrison, Laudholm. Hamilton House is pinned at the Vaughan Woods lot (area) because the state outline puts the house in New Hampshire; Alfred marks the village (area).

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Great Falls Manufacturing Company Newichawannock Canal | Acton, ME (43.5694, -70.971144, Register list) | Register historic district 14000460, extends into Wakefield, NH | No Wikipedia article; form not read; access and what survives |
| Frost Garrison and House | Eliot, ME (43.1617, -70.7489) | Wikipedia: c.1735 single-family garrison and c.1778 house in a subdivision off Garrison Drive | Private; whether anything is visible from a public road |
| Dennett Garrison | Kittery, ME (43.10083, -70.75972) | Wikipedia: c.1710 First Period house, 100 Dennett Road, family-owned in 1978 | Private; current owner and view from road |
| Sarah Orne Jewett House | South Berwick, ME (43.234722, -70.803611) | Register list; Historic New England museum | HNE pages answer 403; hours, interior |
| Buxton Powder House | Buxton Center, ME (43.648333, -70.546389) | Register 76000120 | No article; form not read |

## Tips
- historicnewengland.org answers 403 to `page.py` and its archived copies cannot be fetched; search-result titles are the only thing readable.
- The Atlas's state outline (`source/build/states.json`) runs about 240 m east of the Salmon Falls River at Hamilton House, South Berwick, so `check.py` puts a pin on the house in New Hampshire. A riverside Maine place on that border may need its pin on the Maine-side parking lot.
- Wikipedia's coordinate for the Perkins Tide Mill (Kennebunkport) is on a house about 400 m from the Trust's Grist Mill property; the ArcGIS geocoder finds 8 Mill Lane.
- The Maine Coastal Program's Coastal Public Access Guide PDFs (maine.gov/dmr, one per stretch of coast, May 2026) read with `page.py` and give parking counts, dogs, fees and a coordinate for every shore park and fort.
- `places_test.js` fails only on `onesquethaw-valley` (another batch's "18th century" entry under "Standing, from before 1800"); this batch does not touch it.
- `alfredshakermuseum.com` is drawn by script; no plain copy found.
