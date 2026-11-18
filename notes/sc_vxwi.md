# sc_vxwi: Beaufort County, South Carolina: tabby ruins, forts and old churches
state: South Carolina
region: sc
date: 2026-11-18
places: 15
file: data_sc_vxwi.py

## What this batch is
Fifteen places in Beaufort County, South Carolina, the first real batch for the state: the tabby and brick church ruins at Old Sheldon and the St. Helena Chapel of Ease; three forts (Fort Frederick's 1730s tabby walls at Port Royal, the Spanish-American War batteries at Fort Fremont, and the 1864 earthwork of Fort Howell, built by the 32nd USCT); the Stoney-Baynard tabby ruins in Sea Pines; the Baynard Mausoleum and Zion cemetery; two lighthouses (Hunting Island, climbable, and the Hilton Head rear range light in Palmetto Dunes); and standing places worth the trip: the Parish Church of St. Helena (1724), the Verdier House and the Arsenal in Beaufort, the Brick Baptist Church and Penn Center on St. Helena Island, and the Church of the Cross in Bluffton. Sources: Wikipedia raw text (wiki_raw.py, with the Register list rows), National Register nominations read as text from NPGallery (`npgallery.nps.gov/NRHP/GetAsset/NRHP/<ref>_text` worked for every form tried except Fort Frederick's, a scan with no text layer), and the managers' pages: Beaufort County news (Fort Fremont), SCDNR's Fort Frederick panels, SC State Parks, the Hilton Head Island Land Trust, NPS (Reconstruction Era NHP), Penn Center, the Church of the Cross, Palmetto Dunes and the rear-range lighthouse's own site. NOT checked: anything on the ground; the hours at Old Sheldon, the Parish Church of St. Helena, the Verdier House (historicbeaufort.org 403), the Arsenal museum and the Zion cemetery (Heritage Library page 404); who owns the Chapel of Ease ruin; how outside visitors get into Sea Pines for the Stoney-Baynard ruins (marked ask); whether Fort Fremont's separately listed brick hospital is inside the county preserve; the Hunting Island climb fee. Pins moved by sight: Fort Fremont and Fort Howell onto their earthworks on the LiDAR, the Church of the Cross onto the building matching its photograph. Fort Frederick is site precision (walls not plain on aerial or LiDAR). Red brick: 'no' for nine from sources or Commons photographs; '?' for Old Sheldon and the Brick Baptist Church (only black-and-white photographs, though both are brick), St. Helena's, Penn Center and the rear range light. Old Sheldon dates and fire history, Fort Frederick's building years, the Arsenal's year and Stoney-Baynard's year are given both ways (conf mixed).

## Leads
Places you read about and could not finish. One row each; delete the example row. Leave the table header.

| Place | Where | What is known | What is missing |
|---|---|---|---|
| Sams Plantation tabby ruins | Dataw Island, Beaufort County, SC | Register form 88001820: ruins of at least twelve tabby buildings (house, kitchen, cemetery wall, chapel) among a golf course; Dataw Historic Foundation gives gate passes on request and runs a History & Learning Center beside the ruins, open 8 a.m. to 8 p.m. | A position: the Register point (32.43083, -80.59444) is in open marsh and the ruins could not be found on the aerial |
| Callawassie Sugar Works | Callawassie Island, Okatie, SC (32.33556, -80.85722) | Register form 13001096: tabby boiling house walls to about 12 ft and the mill base, c.1815–16 | A public way in: the island is a private community and no visitor rule was found |
| Tabby Manse | Beaufort, SC (32.43264, -80.67642) | Wikipedia: c.1786 house with tabby walls over two feet thick | Whether it is a house, an inn or anything the public may visit |
| Fort Fremont hospital | St. Helena Island, SC (Register 88001819, 32.3081, -80.6436) | Brick post hospital of Fort Fremont, listed separately | Whether it is in the county preserve or private, and what it looks like now |
| Charlesfort-Santa Elena site | Parris Island, SC (32.3064, -80.6756) | Register 74001822: the French and Spanish settlement sites | The rules for visiting a site on the Marine Corps depot |
| Fort Mitchell | Hilton Head Island, SC (Register 100001036, address restricted) | Civil War earthwork on Skull Creek | A source for its position and access inside Hilton Head Plantation |

## Tips
- NPGallery's text route (`https://npgallery.nps.gov/NRHP/GetAsset/NRHP/<ref>_text`) read South Carolina Register forms well through page.py; the state's own register site (`schpr.sc.gov`) answers 403.
- Several South Carolina Register list points were off: Sams Plantation's is in marsh, Fort Howell's by a road junction 160 m from the earthwork, the Church of the Cross's on the river shore. The LiDAR sheet showed the forts plainly.
- historicbeaufort.org answers 403 to page.py; heritagelib.org's old page addresses answer 404.
- tools/look.py at 1,500 m is too coarse to find a ruin under trees; the --lidar tiles of pincheck were what found Fort Fremont and Fort Howell.
