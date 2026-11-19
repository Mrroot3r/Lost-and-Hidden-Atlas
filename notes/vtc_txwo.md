# vtc_txwo: Lamoille County and Waterbury, Vermont
state: Vermont
region: vtc
date: 2026-11-19
places: 17
file: data_vtc_txwo.py

## What this batch is
Seventeen standing places in Lamoille County (Stowe, Morristown, Hyde Park, Johnson, Wolcott, Elmore, Cambridge) and Waterbury, region drawn at random by `choose.py`: seven covered bridges (Gold Brook/Emily's, Red at Morristown, Power House and Scribner at Johnson, the Fisher railroad bridge at Wolcott, Grist Mill and Poland at Cambridge), the Seaver saw and grist mill and 1822/1918 dam at Moscow, the Noyes House Museum and Peoples Academy with its Grout Observatory in Morrisville, the Lamoille County Courthouse, the Cambridge Meetinghouse, Elmore State Park's CCC beach house and fire tower, and in Waterbury the Feed Company mill, Green Mountain Seminary, the Vermont State Hospital (now the state office complex) and the White Meeting House. Three of these were leads in the vtc_kaqi note (rows deleted). Sources: Wikipedia through `wiki_raw.py`; the National Register forms for Moscow Village (08000744) and the Vermont State Hospital (16000765) through `page.py`; the Town of Waterbury walking-tour PDF; the Vermont Historical Society museum directory (Noyes House hours, which it says may be out of date); VTDigger (Moscow); the Vermont State Parks Elmore page. Not checked: anything on the ground; interiors and opening times of the courthouse, the seminary (Wikipedia's tenants are as of 2009), the White Meeting House and the Grout Observatory; the Lamoille Valley Rail Trail rules (its state page gave HTTP 403); what is in the Feed Company mill now (OpenStreetMap shows a restaurant at 92 Stowe Street). The Power House bridge's date is given both as 1870 and 1872 (`conf='mixed'`); the Feed Company mill as about 1830 (Wikipedia) and about 1835 (walking tour). Brick: the Cambridge Meetinghouse from a Wikimedia photograph; Peoples Academy ("red brick") and the State Hospital (brick with reddish mortar; marked yes) from the texts; courthouse, Noyes House, Feed mill and Elmore left '?' (Wikimedia refused the courthouse picture twice; the others had no picture of the place). No pin marks only a trailhead; the State Hospital pin is placed on the Center Building by judging the layout on the aerial (prec site).

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Stowe CCC Side Camp (Vermont State Ski Dorm) | Stowe, VT (44.52611, -72.77694; Register list says address restricted) | 1935 CCC barracks for 50 men in Mount Mansfield State Forest at 6992 Mountain Road, a ski lodge after 1945 (Wikipedia) | Who runs it now and whether the public may see it; the Register keeps its location restricted |
| Elmore CCC camp remains | Elmore, VT (Elmore State Park) | Wikipedia says the CCC encampment remains are in the area | Where they are; a source that names them |
| Gates Farm Covered Bridge | Cambridge, VT (44.64639, -72.87278) | 1897 Burr arch by George W. Holmes, moved to the Gates farm in 1950, restored 1995 (Wikipedia) | On farm land: whether it can be seen or reached from a public way |
| Halfway House, Mount Mansfield | Cambridge/Underhill, VT (44.53129, -72.8356, OSM mapped ruin) | Leads layer only | Any source; the Green Mountain Club page tried answered 404 |
| Jaynes, Montgomery and Village covered bridges; Mill and Morgan bridges | Waterville and Belvidere, VT | Five 19th-century bridges over the North Branch Lamoille (Wikipedia) | Not added for want of time; town roads |

## Tips
- `publish.sh` stopped once because `safe_data.py` (pull request #156) merged during the session; `resync.sh`, a rebuild and a new batch time fixed it. A data file with small `def HM(...)`/`def NR(...)` helpers passes the new check.
- `railtrails.vermont.gov` (Lamoille Valley Rail Trail) answers HTTP 403 to `page.py`.
- The Vermont Historical Society's county museum directories (`vermonthistory.org/lamoille-county-museum-directory`) give small museums' hours and addresses in one page.
- Web search in this session returned titles and links only, with no quoted text.
