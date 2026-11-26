# portland_me_furi: Portland, Maine: the city rebuilt after the 1866 fire, and its harbour forts
state: Maine
region: mes
date: 2026-11-26
places: 18
file: data_portland_me_furi.py

## What this batch is
Eighteen places from one Old World Exploration video about Portland, Maine (record: `source/videos/20250221_7XUOlfNvMZY.md`, 54 names). Nothing was on the Atlas within 5 km of Portland before. Added: the Portland Observatory, Victoria Mansion, City Hall, the Custom House, the Gignoux federal courthouse, the Porteous, Mitchell and Braun building, the Woodman and Rackleff blocks and the Fidelity Trust Building downtown; First Parish, the Cathedral of the Immaculate Conception, State Street Church, St. Dominic's (now the Maine Irish Heritage Center: the video called it gone), Sacred Heart (closed after a last Mass in October 2026, per Wikipedia) and Williston-West (now offices); Fort Gorges and Fort Preble in the harbour; and the Casco Castle tower in South Freeport. Sources: Wikipedia raw text, Park Service records and forms (`form.py`), and the pages of Greater Portland Landmarks, Victoria Mansion, Friends of Fort Gorges, Southern Maine Community College and State Street Church. Not checked: anything on the ground; City Hall and the Heritage Center hours (`hours='?'`); First Parish service times; the cathedral's Mass times come from a web search quoting the diocese's listing because the diocese page answers 403; the Observatory's season is the 2025 one still on its page; visitor parking at Fort Preble; red brick for nine places (`'?'`). Williston-West's date disagrees (1877 on the form, 1897 on Wikipedia and the Register record): `conf='mixed'`. Four pins were moved on the aerial (cathedral, Woodman, Fort Preble, the Gignoux courthouse, whose Wikipedia and Register point is about 550 m off on a road junction).

## Leads
Places you read about and could not finish. One row each; delete the example row. Leave the table header.

| Place | Where | What is known | What is missing |
|---|---|---|---|
| Thompson Block | 117-125 Middle St, Portland, ME (Register 43.658889, -70.253056) | Register record: 1867-1868, George M. Harding; the online form is only a photograph sheet | A description or a picture to say what stands |
| Baxter Library building (1888) | Congress St, Portland, ME | Named in the video as standing; no source opened | Wikipedia or Register text; the Wikipedia title "Baxter Library" does not exist |
| St. Joseph's Academy and Convent | Stevens Ave, Portland, ME (Register 43.6790, -70.2941) | Register list 100000806, 100008511 | Read the form with form.py |
| Cumberland County Courthouse | Federal St, Portland, ME | Built 1910, named in the Gignoux article | A source on the building; it is not on the Register list |

## Tips
- The Edward T. Gignoux courthouse's Wikipedia and Register list point (43.65861, -70.26167) is about 550 m west of the building; OpenStreetMap's courthouse point is right.
- portlandmaine.gov did not connect from `page.py`; portlanddiocese.org and firstparishportland.org answered 403 to `page.py` and the web fetch tool.
- portlandlandmarks.org/observatory is gone (404); the Observatory's season is on `/portland-observatory` and `/faq-observatory`.
- victoriamansion.org/visit-us reads in full with `page.py --all`; its FAQ text, with the regular and holiday hours, is on that page.
- `pix.py pin` worked out the right point from a tile in the second sheet when given the y within that sheet.
