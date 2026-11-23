# sc_rccj: South Carolina: a second scatter, York County to the Lowcountry
state: South Carolina
region: sc
date: 2026-11-23
places: 16
file: data_sc_rccj.py

## What this batch is
Sixteen places in parts of South Carolina the first two batches left empty, so the state goes from 36 places to 52. In the north: Landsford Canal (Robert Mills's 1823 granite locks, state park), Historic Brattonsville (1776–1855 plantation village and museum) and the Lancaster County Courthouse (1828, restored after the 2008 arson). In the west: the Newberry Opera House (1881), the Abbeville Opera House (1904–08), the Burt-Stark Mansion (Davis's last council of war) and Ashtabula near Pendleton (c.1825, shown by the Pendleton Historic Foundation). In the Midlands and the Pee Dee: the rammed-earth Church of the Holy Cross at Stateburg, the Old Horry County Courthouse (now Conway City Hall) and Hebron Church at Bucksville. In the Lowcountry: Hopsewee, Drayton Hall, the Powder Magazine (1713, closed to general visitors since February 2025), the Old Exchange and Provost Dungeon, the Pon Pon Chapel ruins at Jacksonboro, and the Rivers Bridge battlefield earthworks. Sources were read with `wiki_raw.py` (Wikipedia raw text), `page.py` (South Carolina State Parks, Drayton Hall, the Old Exchange, chmuseums.org, newberryoperahouse.com, the Pendleton Historic Foundation, hopsewee.com, discoversouthcarolina.com, the Charleston City Paper) and HMdb marker pages for Pon Pon Chapel. Pins came from OpenStreetMap (`nom.py`, `osmnear.py`) or Wikipedia and were all looked at on the aerial; Landsford Canal, Lancaster, Brattonsville and Pon Pon also on the LiDAR sheet. Moved: Lancaster (the Wikipedia point was 300 m off, on a parking area), Brattonsville (OSM point in a field) and Landsford (Wikipedia point on a river island, moved onto the canal channel the LiDAR shows). Not checked: nothing on the ground; no hours from the owner's own page for the Abbeville Opera House (its site did not read), the Burt-Stark Mansion (hours only from the state tourism office's article), Hopsewee (tour days not on the page read), the Church of the Holy Cross and Hebron Church (no service times found), the Lancaster courthouse and Conway City Hall (opening not checked). Rivers Bridge has no mapped parking and its pin marks the park, not the earthworks. Red brick left `?` for eight places where no source or picture opened settled it.

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Musgrove Mill State Historic Site | Laurens/Spartanburg/Union county line, SC (34.59354, -81.85248) | 1780 Revolutionary battle site by the Enoree River; a state historic site (Wikipedia) | What is left to see (mill site, house) and the park's hours page |
| Warren Mill and Hickman Mill | Warrenville and Graniteville, SC (33.552022, -81.808603; 33.564912, -81.809036) | Textile mills on the Register (Aiken County list, 2016) | Any source on their state and who owns them |
| Old Ebenezer Church | Latta, SC (address restricted in the Register list) | Register-listed church, Marion County | Location and a source |
| Powder Magazine reopening | Charleston, SC | Closed to general admission since February 28, 2025 (Charleston City Paper) | Check whether the Colonial Dames have reopened it, then change acc to open with hours |

## Tips
- `www.powdermag.org` does not answer at all; the Charleston City Paper (March 2025) explains why: the museum closed to general visitors.
- The Pon Pon Chapel ruins are best sourced from three HMdb markers (7120, 66489, 7073): one says the chapel and four acres were deeded to the Colleton County Historical Society in 1970; the Wikipedia article is two sentences.
- Wikipedia's coordinate for the Lancaster County Courthouse falls 300 m off; `osmnear.py ... buildings -g court` found "Lancaster Historic Courthouse" on OpenStreetMap.
- Landsford Canal's Wikipedia coordinate is on an island in the Catawba; the LiDAR sheet shows the canal channel clearly along the west bank.
- In a data file, an apostrophe added in a later text replacement must be escaped (`doctor\'s`); `safe_data.py` then reports a misleading "invalid character '–'" on the line.
