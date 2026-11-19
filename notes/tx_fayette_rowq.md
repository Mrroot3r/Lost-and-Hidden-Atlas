# tx_fayette_rowq: Texas: Fayette County
state: Texas
region: tx
date: 2026-11-19
places: 17
file: data_tx_fayette_rowq.py

## What this batch is
A first pass over Fayette County, Texas (region `tx` drawn at random by `choose.py`; the Atlas had nothing within 30 km of La Grange), with the Burton Farmers Gin just over the line in Washington County. Seventeen places: in La Grange, the Kreische Brewery ruins and house, the Monument Hill tomb of the Dawson and Mier men, the Fayette County Courthouse, the old county jail, the N. W. Faison House, St. James Episcopal Church and the Katy depot; the four painted churches round Schulenburg (High Hill, Ammannsville, Praha, Dubina); the 1888 Bedstead Truss Bridge in Schulenburg's Wolters Park; Bethlehem Lutheran Church and the Winedale Stagecoach Inn near Round Top; the Zapp Building and the Precinct No. 2 Courthouse on Fayetteville's square; and the Burton Farmers Gin (Texas Cotton Gin Museum). Sources were read in this session with `page.py` (THC site pages for Kreische Brewery and Monument Hill, which give hours and tickets; National Register forms as PDFs from the THC Atlas; HMdb nearby lists round La Grange, Round Top and Schulenburg and eight marker pages; Texas Parks & Wildlife magazine; a Houston Chronicle feature; the Texas Cotton Gin Museum's page; Texas Time Travel and Briscoe Center pages) and `wiki_raw.py`. Not checked: anything on the ground; the Greater Schulenburg Chamber of Commerce's painted-church pages (HTTP 403; the open days come from the Chronicle feature, whose date was not checked); hours of the Faison House, the Katy depot, Winedale (the university's visiting page answered 404) and the courthouses' insides; the current owner and use of the old jail and the Zapp Building; the material of the Kreische brewery walls. Sources disagree, and both versions are given, on the jail's date (1881 or 1883), Ammannsville's (1917 or 1918) and the Winedale inn's (about 1834 or the 1840s). Pins: five were moved (Praha, Dubina, Bethlehem Lutheran, Zapp, the Burton gin) from the aerial or OpenStreetMap; the Dubina pin is the cross-shaped building by the cemetery, taken to be the church from its plan. The Kreische and Monument Hill pins were confirmed on the LiDAR sheet. Red brick: High Hill `yes` and the Zapp Building `some` (Register forms); the Kreische ruins and the Faison House `?`.

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Moore's Fort | Round Top, TX (HMdb marker 183544: 30.06423, -96.69804; 303 South White Street) | 1831 blockhouse of John Henry Moore, "oldest structure in Fayette County", moved and restored and given to the Texas Pioneer Arts Foundation in 1976 (HMdb marker text) | Henkel Square is now run as shops (henkelsquareroundtop.com); whether the fort still stands there and can be seen was not checked |
| Schulenburg Cotton Compress | Schulenburg, TX (Register list 29.678611, -96.9125; James and Main streets) | 1886 Morse cotton press, worked until 1968, in excellent condition in 1979 (Register form 79002938) | Whether the building and press still stand today; owner |
| Sengelmann Hall and City Meat Market | Schulenburg, TX (29.679822, -96.905228) | Brick commercial hall with limestone finials, high integrity inside and out (Register form 09000451) | Current use and opening; brick colour |
| Dubina store ruins | Dubina, TX, beyond the curve of CR 480 toward the East Navidad River | Ruins of a multi-purpose commercial complex facing the old road bed (Dubina district Register form 03000970) | Position, owner and whether they are visible from the public road |
| East Navidad River Bridge | FM 1579 near Schulenburg, TX (29.682939, -96.846481) | 1920s Texas Highway Department concrete cantilever bridge, 70-foot centre span, still a road bridge (Register form 14000497) | Its building year from the form; a safe place to stop and look |

## Tips
- In Texas the THC Atlas Register forms (`https://atlas.thc.state.tx.us/NR/pdfs/<ref>/<ref>.pdf`) read well with `page.py`, but a batch of nine took over six minutes in one shell call: run them in a loop that writes each to a file, one call per few forms.
- `research/pages/` names cached pages by hash, not by reference number; to search a cached form, find it by its first line (`head -c 150`) and then strip the tags.
- thc.texas.gov uses short names: `historic-sites/kreische-brewery` and `historic-sites/monument-hill` work, `historic-sites/monument-hill-kreische-brewery` is 404.
- schulenburgchamber.org (the painted-church tours) answers 403 to `page.py`, and the archived copies could not be fetched.
- `nom.py` found Bethlehem Lutheran, the Zapp Building and St. Mary's in Praha by name; `osmnear.py ... buildings` found nothing round Dubina or Burton.
