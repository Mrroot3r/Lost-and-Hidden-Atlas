# va_klru: Virginia: a third scatter, Eastern Shore to Big Stone Gap
state: Virginia
region: va
date: 2026-11-22
places: 15
file: data_va_klru.py

## What this batch is
Fifteen standing places spread across Virginia, which had 32 (the fewest of any state or province not held by another session, claimed with `choose.py --thinnest`): the Eastville Court Green (1731 courthouse, clerk's office, debtors' prison), Ker Place (Onancock), Yeocomico Church (Kinsale), Belle Grove (Middletown), Tredegar Iron Works (Richmond), George Washington's Gristmill and Distillery (Mount Vernon), Gadsby's Tavern (Alexandria), the Jackson Ferry Shot Tower and the Foster Falls iron-furnace village (New River Trail), Fort Monroe and the Casemate Museum (Hampton), Rapidan Camp (Shenandoah National Park), the Southwest Virginia Museum (Big Stone Gap), the 1750 Isle of Wight Courthouse (Smithfield), Glencoe Mansion (Radford) and the Sutherlin Mansion (Danville). Facts come from Wikipedia read with `wiki_raw.py`; hours, fees and access from the pages of whoever runs each place read with `page.py` (Northampton Historic Preservation Society, shorehistory.org, copleparish.com, bellegrove.org, acwm.org and nps.gov, mountvernon.org, alexandriava.gov, dcr.virginia.gov, fortmonroe.org, glencoemuseum.org, danvillemuseum.org) and a Smithfield Times article. Red brick from sources or the Wikipedia photographs opened with `brick.py look`. Pins: OpenStreetMap points (`nom.py`) where they existed, else Wikipedia; Belle Grove was moved about 160 m onto the house. Not checked: anything on the ground; clock times at the Eastville Court Green and Gadsby's Tavern (the pages give days only); any opening hours for the 1750 Isle of Wight Courthouse (`hours='?'`); whether the Shot Tower can be climbed now (the two state park pages disagree: scheduled summer days, or no tours during renovation; `conf='mixed'`); whether the Foster Falls furnace stack can be walked to; parking at Yeocomico, Gadsby's and Smithfield; the Shenandoah entrance fee; which Fort Monroe lot visitors use. Rapidan Camp is pinned from Wikipedia under trees (a level spot by the streams on the LiDAR). `check.py` warns that Gadsby's Tavern is just outside Virginia's outline; the pin is on the tavern in Old Town Alexandria on the aerial.

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Longdale Furnace (Lucy Selina Furnace) | Longdale Furnace, Alleghany County, VA (37.80917, -79.68444; HMdb marker 46386 at Route 269 and Iron Ore Lane) | Stone stack of 1827, iron company office, laboratory, two brick chimneys and machine shop in a Register district (Wikipedia; Virginia DHR 003-0338) | Where the stack stands, and whether it can be seen from a public road; DHR says many listed buildings are private dwellings |
| Australia Furnace | Alleghany County, VA (HMdb marker 107981) | Hot-blast furnace begun 1852, bought by Tredegar's owner in 1862 (HMdb marker text) | Position of the ruin and who owns the ground |
| Dismal Swamp Canal | Chesapeake, VA to North Carolina (Wikipedia 36.55667, -76.38056) | Dug by hand from 1793, opened 1805, oldest continually operating man-made canal in the United States (Wikipedia) | A lock or other old work to pin (Deep Creek lock?) and the managing body's page |
| Wilderness Road State Park | near Ewing, VA (36.63389, -83.52361) | Karlan Mansion and a replica of Martin's Station fort (Wikipedia) | The state park page for hours; whether the mansion opens |

## Tips
- `nom.py` answers HTTP 629 when asked faster than about once a second; a `sleep 2` between calls fixed it.
- The ACWM visit page (acwm.org/visit/) gives "Open Daily 10 AM–5 PM" without saying which of its sites; check it against the Tredegar page if one turns up.
- The Virginia State Parks page for New River Trail (`--all -n 40000`) holds the Shot Tower and Foster Falls rules that the Shot Tower page lacks, including that tower tours are stopped for renovation.
- `www.genuinesmithfieldva.com` business pages answer 404 with no archived copy.
