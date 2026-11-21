# co_qmtv: Colorado: a first scatter
state: Colorado
region: co
date: 2026-11-19
places: 17
file: data_co_qmtv.py

## What this batch is
Seventeen places spread across Colorado, which had one (Animas Forks): Saint Elmo and Independence ghost towns, the Redstone coke ovens, the Crystal Mill, Leadville's Tabor Opera House, Georgetown's Hotel de Paris, South Park City at Fairplay, Fort Garland, Bent's Old Fort, Boggsville, the Ludlow tent colony memorial, Dearfield, the Rainbow Arch Bridge at Fort Morgan, the Convicts' Bread Oven in Plateau Canyon, Lowry Pueblo, the Bromide charcoal kilns and the Two-Bar Ranch in Browns Park. Sources: Wikipedia as raw text (`wiki_raw.py`, and `--rows` on the Morgan, Mesa, Routt, Moffat, Rio Grande, Costilla and Bent/Baca county Register lists); NPGallery Register forms 85000221, 00000740, 78000873 and 74000589 (text layers read); and with `page.py` the pages of History Colorado, the NPS (Bent's Old Fort, Dearfield study), the BLM (Lowry), the FWS (Browns Park), Pitkin County, the Aspen Historical Society, bentcountyheritage.org, southparkcity.org, taboroperahouse.net, the Colorado Mountain Club (Crystal Mill) and HMdb. Not checked: nothing on the ground; hours of the Hotel de Paris (its site would not connect), the Tabor Opera House (only the county tourism page gave tour days) and Bent's Old Fort (the NPS page gives no clock times); current access to the Bromide kilns (owned by a non-profit in 1998), the Convicts' Bread Oven (private ranch in 1974) and the Crystal Mill (fee terms from a club page, not the owner); whether walkers may cross the Rainbow Arch Bridge; where to park for Ludlow, Dearfield, Boggsville and the Two-Bar Ranch. Pins for Saint Elmo, the Crystal Mill, Boggsville, the Convicts' oven, Dearfield and the Bromide kilns are `area`; Boggsville's two houses could not be made out on the aerial. Red brick is `?` for most standing buildings: no picture was opened for it.

## Leads
Places you read about and could not finish. One row each; delete the example row. Leave the table header.

| Place | Where | What is known | What is missing |
|---|---|---|---|
| Cokedale coke camp | Cokedale, Las Animas County, CO (Register district 37.14222, -104.61944) | Wikipedia: ASARCO company coal camp of 1906, 92 contributing buildings, houses of coke-and-cement block | Which buildings or ovens are worth a pin, and access |
| Fort Lyon | Las Animas, CO (Register 38.077222, -103.132778) | Register list only (also Fort Lyon National Cemetery) | A source on what stands and whether visitors may go in |
| Old Ladore School | Browns Park NWR, CO (Register 40.78, -108.8929) | Register list: 1911 school, social centre of Browns Park | What it is now and access |
| Hahns Peak Schoolhouse | Hahns Peak Village, CO (40.80627, -106.94440) | Register list: one-room school 1912-1943 | Source and access |

## Tips
- `wiki_raw.py --rows` on "National Register of Historic Places listings in Bent County, Colorado" (and Baca, Costilla) printed a combined "listings in Colorado" table of 117 rows from several small counties: grep it for the town names.
- historycolorado.org Register pages (`/node/<n>`) are often DRAWN BY SCRIPT; some (Bromide kilns) give a paragraph. The Fort Garland museum page there reads fine and gives hours.
- hoteldeparismuseum.org refused the connection from `page.py`; taboroperahouse.net has no /tours or /visit page.
- The pin check took over two minutes for 17 pins with `--lidar`: run it in the background.
- Wikipedia's Redstone coke oven article still says Mid-Continent Coal and Coke owns the ovens; Pitkin County's open-space page counts them in its Coke Ovens Open Space.
