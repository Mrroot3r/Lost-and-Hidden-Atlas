# ks_dvmh: Johnson County, Kansas
state: Kansas
region: ks
date: 2026-11-23
places: 15
file: data_ks_dvmh.py

## What this batch is
Fifteen places in Johnson County, Kansas (Olathe, Shawnee, Lenexa, Gardner, Edgerton, Fairway, Prairie Village, Overland Park, Stilwell), where the Atlas had none. They were picked from the Kansas Historical Society's register search for Johnson County (read with page.py), plus the Wikipedia articles, the National Park Service's Mahaffie and Gardner Junction pages, the Johnson County, Kansas Historical Society, Ensor Park and City of Lenexa pages. Pins were looked at on the Kansas 2024 aerial only; the LiDAR sheet was not used (none is in woods). Not checked on the ground: all of it. Not checked: interiors; who owns the WPA Beach House, the Stilwell school and Gardner Junction Park; Shawnee Town 1929's hours and which buildings are original; the Foster House's hours; Lackman-Thompson tour times. Mahaffie's hours come from a search result quoting mahaffie.org, which would not open (HTTP 403). Pins that are approximate: Lone Elm swale (area, Register point), Harmon Park swale (OpenStreetMap point), WPA Beach House (Register point on a lakeshore building), Ensor (site; farm buildings lie just south), Gardner Junction (address lookup). Pictures: 4 places have Wikipedia pictures; 4 got a Commons choice (Ensor, WPA Beach House, Foster House, Gardner Junction); the rest had none that fit.

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Downtown Gardner Historic District | Gardner, KS (Main and Elm) | Register 2023: 19 buildings from 1905 to about 1967 | Which buildings stand out; pins |
| Spring Hill Historic District, Edgerton Grange Hall, John McCarthy House, Turner Barn | Spring Hill and Edgerton, KS | State or National Register listings | Not read |
| Shawnee Indian Cemetery | Shawnee, KS | Register 2022; designated a Shawnee sacred site in 2020 | Whether the Shawnee Tribe invites visitors; left out on purpose |

## Tips
- mahaffie.org, lenexa.com and jocogov.org's department pages return 403 or 404 from page.py; the web fetch tool read lenexa.com and gardnerhistoricalmuseum.com.
- The Kansas register search page output is cut by page.py; the whole text is in research/pages/ as HTML.
- ArcGIS findAddressCandidates gave a good coordinate for every street address; nom.py found only some.
