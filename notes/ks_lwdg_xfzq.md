# ks_lwdg_xfzq: Lawrence and Douglas County, Kansas (third pass)
state: Kansas
region: ks
date: 2026-11-24
places: 20
file: data_ks_lwdg_xfzq.py

## What this batch is
Twenty standing places in Douglas County, Kansas, that the earlier batches (ks_kwud, ks_pmvt, ks_dgmn) lacked: three University of Kansas halls (Green Hall, now Lippincott Hall; Strong Hall; Bailey Hall), houses (Snow, Duncan, Lane-Greenlees, Lane-Duncan stable, Brender), St. Luke AME Church, the 1906 post office, the Union Pacific depot, the barb wire and Zimmerman Steel buildings, Klock's grocery, the ECM building, and one building each in Baldwin City (Palmyra Post Office, Masonic lodge), Lecompton and Eudora (Seybold Building, State Bank). Chosen as the Douglas County Register listings with nothing on the map; this run was started to fill in the Kansas City area and Johnson, Wyandotte and Clay counties were found nearly done. Sources: the Kansas Historical Society Register summaries (page.py, all 13 pages saved), NPGallery form text for Green Hall, Strong Hall, Snow House and Duncan House, Wikipedia (wiki_raw.py) for Strong, Bailey and Chewning, and web search results for what the post office, depot and Palmyra Post Office are used for now. Not checked: anything on the ground, interiors, who may go in and when (the depot's hours conflict between sources, so hours='?'), parking, and the colour of most walls (brick='?' except where a source says). The Register summaries for the barb wire building, Klock's and the ECM building say little, so those entries are short. Pins are address points; the Green Hall pin was moved to the OpenStreetMap building for Lippincott Hall after the first point proved 140 m off.

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Fernand-Strong House | 1515 University Dr, Lawrence, KS | Register 2008: Italianate frame house, c. 1872, once lived in by Chancellor Strong and James Naismith | Not written up; a source on its use today |
| Samuel Riggs House, Shalor Eldridge House, Benedict House | Lawrence, KS | Register houses (Italian Villa; Greek Revival; Stick/Eastlake) | Descriptions beyond the style |
| Oregon-California Trail segments at First Methodist Church | 867 US-40, Lawrence, KS | Register summary read | Public access |

## Tips
- The Kansas Historical Society register search pages (`natreg_listings/search/page:N/county:DG/...`) read well with `page.py --all`; about 13 pages cover a county.
- ArcGIS address points put Strong Hall (38.95858, -95.24768) within 15 m of the existing Spooner Hall pin (38.95854, -95.24759): one of the two is probably off, since they are separate buildings. Not checked.
- The Register list's "Green Hall" is Lippincott Hall at KU; a Commons search by "Green Hall" finds photos named Lippincott Hall.
- Wikimedia's API answered "too many requests" to plain curl calls; use the tools.
