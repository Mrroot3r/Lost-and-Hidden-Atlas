# oh_rddr: Ohio: Newark, Granville and Licking County
state: Ohio
region: oh
date: 2026-11-19
places: 18
file: data_oh_rddr.py

## What this batch is
Eighteen places in Licking County, Ohio (Newark, Heath, Granville, Hebron, Buckeye Lake, Outville, Toboso, Flint Ridge), plus the Deep Cut marker at Millersport just over the line in Fairfield County. The Atlas had nothing within 30 km before. Ancient: the Octagon and Great Circle earthworks, the Alligator effigy mound, the Flint Ridge quarry pits. Canal: the Blackhand Gorge locks and towpath, the canal groundbreaking marker, Hebron Mill on the old turning basin, the Licking Summit Deep Cut. Standing: the 1889 jail (empty since 1987), Sullivan's Home Building Association Bank, the courthouse, the Buxton Inn (1812), the Avery–Downer House museum, St. Luke's (1837), the Old Colony Burying Ground, Bryn Du, the Outville depot; and the fountain that is all that is left of the Buckeye Lake trolley park. Sources were read with `wiki_raw.py` and `page.py`: Wikipedia, HMdb marker pages (full inscriptions and positions; five HMdb nearby lists gave nearly the whole batch), the Ohio DNR pages for Blackhand Gorge and Buckeye Lake, hopewellearthworks.org, WYSU/WYSO, the county archives' blog, the National Trust, bryndu.org and the Robbins Hunter Museum. Not checked: anything on the ground; the hours of the Great Circle and Flint Ridge (ohiohistory.org answered 403); the hours of the Sullivan bank, the courthouse, the jail (occasional tours only), Bryn Du and Buckeye Lake State Park; the exact spot of the Blackhand Gorge locks (pin is on the Canal Lock Trail, prec area) and of the Outville depot (prec area); whether the Deep Cut can still be seen south of Millersport (pin is the marker). Parking was not found for Blackhand Gorge, Flint Ridge (lots at the museum, not confirmed), Bryn Du, Outville or the groundbreaking marker. Brick: Buxton Inn set 'some' from its Wikipedia photo (painted wood, red brick chimneys); seven places left '?'.

## Leads
Places you read about and could not finish. One row each; delete the example row. Leave the table header.

| Place | Where | What is known | What is missing |
|---|---|---|---|
| Wright Earthworks (Wright Square) | Newark, OH | Wikipedia (Newark Earthworks): a wall segment and a parallel wall of the 20-acre square survive; given to the state in 1934 | A position and the Ohio History Connection's visitor details |
| Blackhand Gorge interurban tunnel and B&O Deep Cut | Toboso, OH (gorge about 40.056, -82.248) | Wikipedia: 327-foot interurban tunnel (1903) on the south bank; 64-ft-deep, 700-ft railroad cut (1850–51) | Positions; they are not mapped in OpenStreetMap's hosted layers. The DNR trail map PDF was not read |
| Johnstown Jail | Johnstown, OH (40.151667, -82.685444) | On the National Register (03000274) | Any source on what it is and who owns it; no Wikipedia article |
| Licking County TB Sanatorium | Newark, OH (40.09759, -82.44648) | HMdb 142456: built 1931–32, TB san 1932–1967, now the county health department's building | Whether it is worth a visit (in daily use) |
| Pennsylvania Railroad Station, Newark | Newark, OH (40.055556, -82.400556) | National Register 79001881; opened for tours in 2016 per the county archives blog | A source on its date, use and access |
| Martin Shaub Mill Site/House | St. Albans Township, OH (40.106944, -82.648056) | National Register 85000119 | The nomination form; what of the mill is left; owner |
| Licking County courthouse brick | Newark, OH | Courthouse added as `brick='?'` | A photograph to settle it |

## Tips
- ohiohistory.org answers HTTP 403 to `page.py` with no archived copy, for every site page tried (Great Circle, Octagon, Flint Ridge). hopewellearthworks.org (the World Heritage partnership) reads and gave the Octagon's dawn-to-dusk hours.
- The Register and Wikipedia coordinate for Bryn Du Mansion (40.08528, -82.4925) is about 2 km north of the house; `osmnear.py ... buildings -g 'Bryn'` and the geocoder for 537 Jones Rd agreed on 40.06748, -82.49021.
- `parking.py`'s "Toboso Road" lot for Blackhand Gorge and its "Brownsville Road" lot at Flint Ridge both fell on a road or a small building on the aerial; left out.
- Prehistoric years such as "100 BC–AD 400" give `yearOf()` nothing (it reads only 1500–2029 and "Nth century"), so the earthworks do not appear under "Dates from"; not changed.
- `start.py --prs` printed 0 open pull requests while #133 had been open an hour earlier (it had merged); publish.sh then stopped for that merge and `resync.sh` caught up in one step.
