# albco_kaom: Albany County: Guilderland, the hilltowns, Bethlehem and Coeymans
state: New York
region: albco
date: 2026-11-18
places: 16
file: data_albco_kaom.py

## What this batch is
Sixteen places in Albany County outside the city, drawn at random by `choose.py` (region `albco`, which offered Altamont). The county's ruins were already well covered, so this batch is mostly the standing buildings worth a visit. Guilderland: the Altamont D&H station (now the library), the Mynderse-Frederick House and the 1860 Cobblestone Schoolhouse in Guilderland Center (both town-owned), the Apple Tavern (Appel Inn) at Osborne Corners, Hamilton Union Presbyterian Church and the Schoolcraft House on US 20. Colonie: the Pruyn House. Bethlehem: the Cedar Hill Schoolhouse museum, the Delmar post office (Indian Ladder mural) and the Van Deusen stone house. Hilltowns: St. Paul's Lutheran Church at Berne (the 1845 Anti-Rent convention), the Rensselaerville grist mill and hamlet, and the Potter Hollow school. Coeymans and New Scotland: the Ariaanje Coeymans House and the Onesquethaw Valley stone houses. Sources: Wikipedia as raw text (`wiki_raw.py`, including `--rows` for the county list), the Register form for St. Paul's (text layer read), the Town of Colonie, Pruyn House, Altamont Free Library, Town of Guilderland, Appel Inn, Pomeroy Foundation, HMdb, Cobblestone Museum and Altamont Enterprise pages through `page.py`, and four albanyhilltowns.com pages through the web fetch tool (`page.py` could not connect). Pins: addresses through the ArcGIS geocoder, the grist mill from OpenStreetMap, markers from HMdb and Pomeroy; all looked at on the leaf-off aerial and LiDAR. Red brick was settled from the Wikipedia pictures for six places (`brick.py look`); the Cedar Hill school is painted brick, so `no`. Not checked: anything on the ground; the grist mill's hours (from a page last revised in 2009); the Cedar Hill museum's hours (from 2021); the post office's hours; who owns the Ariaanje Coeymans House and the Potter Hollow school; parking at most standing places; service times at the churches. Area pins: the Rensselaerville hamlet (the district point) and the Onesquethaw Valley (the district marker on Indian Fields Road, not a house). The Van Deusen pin is its 2026 marker; the house was not picked out on the aerial among the new development.

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Lainhart farm and Dutch barn | Altamont, NY (Register point 42.72389, -74.03222) | Wikipedia: Dutch barn about 1819, 1851 farmhouse and outbuildings, family burial ground of 1796, still in the Lainhart family | The Register point is in woods on the aerial; the farm's road frontage and a pin on the barn |
| Bethlehem House (Rensselaer Nicoll House) | Bethlehem, NY, Dinmore Road (42.54389, -73.76667) | Wikipedia: brick house of about 1735 with gambrel roof, enlarged 1796, 1810 and 1830 | Owner and whether it can be seen from a public road |
| Teunis Houghtaling House (Vredehuis) | Clarksville, NY (42.56472, -73.97556) | Wikipedia: frame house of about 1770, enlarged about 1790, family cemetery | Owner, visibility, a second source |
| Mull House and Cemetery | Coeymans, NY (42.50472, -73.78194) | Wikipedia: gambrel-roofed house of about 1825, about 12 markers in its cemetery | Owner and visibility |
| Presbyterian Church in New Scotland and cemetery | New Scotland, NY (42.6314, -73.9061) | Wikipedia: 1849 church, congregation 1787, about 500 burials from the 18th century on | Church page for service times; pin check |
| First Reformed Church of Bethlehem | Selkirk, NY (42.56207, -73.80507) | Wikipedia: church of about 1890 on land granted in 1795 | Church page, interior |
| Coeymans-Bronck Stone House | Coeymans, NY (address restricted on the Register list) | Listed on coeymanshistory.org's register page | A position and whether the public can see it |

## Tips
- altamontenterprise.com shows a paywall page ("maximum number of views this month") to `page.py` for some articles and not others in the same session; the full text came back for 2017–2025 articles but not for two 2016 ones.
- `page.py` could not connect to albanyhilltowns.com (the Albany County hilltowns wiki), but the web fetch tool read its pages directly; it has the Rensselaerville and Berne histories.
- Wikipedia's coordinate for the Apple Tavern (Guilderland) is in an empty field 900 m east of the inn; the ArcGIS geocoder knows "Appel Inn" as a place name.
- The Guilderland Path Through History flyer (on guilderlandschools.org) lists which town-owned houses open and when; it is the only source found for visiting the Schoolcraft House.
