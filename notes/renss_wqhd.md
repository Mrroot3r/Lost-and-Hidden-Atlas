# renss_wqhd: Rensselaer County: Greenbush, Schodack, Sand Lake and the river bridges
state: New York
region: alb, hud, renss
date: 2026-11-22
places: 12
file: data_renss_wqhd.py

## What this batch is
Twelve places in southern and western Rensselaer County (region `renss`, drawn by `choose.py --state ny`), with the Livingston Avenue Bridge filed under `alb` and the North Chatham depot just over the Columbia line under `hud`. Most were leads earlier Rensselaer sessions left: the Joachim Staats House (1696) on Papscanee Island, the John Evert Van Alen House, Smith Boughton's (Big Thunder's) house at Alps, the Arlington Hotel trolley stop at West Sand Lake and the Valley Falls mill village. New: the one surviving officers' quarters of the War of 1812 Greenbush Cantonment (250 McCullough Place, a private house), the Greenbush Reformed Church with Citizen Genet's grave, the Blooming Grove Reformed Church, the Barnet Mills (brewery, then shoddy mill, now a vacant brownfield), the North Chatham third-rail substation and depot, the 1902 Livingston Avenue swing bridge (being replaced by 2028) and the 1924 Alfred H. Smith rail bridge at Castleton. Sources: Wikipedia through `wiki_raw.py`; HMdb marker pages; the Valley Falls Register form (2018, text layer); the Town of East Greenbush historic-sites legend and cantonment slide show and the North Greenbush historian's columns (PDFs on the towns' sites); the NYS Military Museum fort page; the Sand Lake Historical Society marker page and newsletter 25-3 (the Calico House); NYSDEC's Barnet Mills brownfield fact sheet and application; NYS Parks' Schodack Island page; the I LOVE NY Papscanee listing; Railway News on the bridge replacement. Not checked: anything on the ground; whether the Arlington House still trades (an HMdb submitter said it did in 2024; conf='mixed'); service times for the three churches (no page of their own was found, only directories, so all are `view`); North Chatham depot opening days, and which building by the trail is the depot (pin on the panel); whether the Staats house and the cantonment house can be seen from public ground; the Corning Preserve's hours. Every place is view-only except Valley Falls (public streets). Pictures: two from Commons (Barnet Mills, North Chatham depot), which also settled their brick; the rest have none.

## Leads
Places you read about and could not finish. One row each.

| Place | Where | What is known | What is missing |
|---|---|---|---|
| Sharpe Homestead and Cemetery | Defreestville, North Greenbush, NY (Register point 42.66111, -73.69917 is in woods) | Wikipedia: 1740 frame house and family cemetery; the town historian's column puts the Sharp homestead farm on Laura Lane (42.65593, -73.70106) | The house's address, and whether it shows from the road |
| Trinity Lutheran (now West Sand Lake Community Church) | 4363 NY 150, West Sand Lake, NY (HMdb 145285) | Sand Lake Historical Society: congregation 1776; the 1816 church burned 1944; present brick church built 1944–54 | Whether a church of 1954 is worth an entry; its own page and service times |
| Witbeck Farm House | East Greenbush, NY | Town historic-sites legend: 1790 red brick Georgian house of the Witbeck family, Anti-Rent leaders | An address or position |
| Genet House (Charmontot) and Cantonment-salvage McCulloch House | East Greenbush, NY | Town legend: 1806 house Genet built for his son; 1843 McCulloch House built from cantonment timber; both private | Addresses |
| Fred's Falls mill | Cropseyville, Brunswick, NY | Rensselaer Land Trust: mill standing by the falls with some original works; private | A coordinate (`nom.py` finds nothing) and a public view point |
| Ball Seminary | Classic Street, Hoosick Falls, NY (HMdb 124805) | 1936 state marker: built 1842, given to the town 1863 for a union school | Whether the building stands |
| Methodist Farm campground | Methodist Farm Road, Crooked Lake, Sand Lake, NY (HMdb 261878) | Sand Lake Historical Society marker: campground of the Troy Methodist Sunday School Association from 1917 | What old buildings stand and whether it is open |

## Tips
- The Town of East Greenbush's Natural Resources Inventory "Historic Sites Legend" PDF (cms2.revize.com/revize/eastgreenbushny/...) lists 28 historic buildings with dates and present use; the North Greenbush historian's columns are PDFs under townofng.com/sites/default/files/2024-05/ and northgreenbush.gov.
- NYSDEC brownfield applications (extapps.dec.ny.gov/data/DecDocs/<site>/...) read with `page.py` and give a site's past uses with dates.
- The HMdb nearby list for six points round the county turned up most of this batch's candidates; many North Greenbush town markers have short texts and good positions.
- historypointer.com pages are drawn by script; `page.py` gets only the title and address.
