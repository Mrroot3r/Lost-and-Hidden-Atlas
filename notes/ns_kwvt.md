# ns_kwvt: Annapolis Royal and Annapolis County, Nova Scotia
state: Nova Scotia
region: ns
date: 2026-11-19
places: 21
file: data_ns_kwvt.py

## What this batch is
Twenty-one places in Annapolis County, the first real batch in Nova Scotia beyond York Redoubt. Annapolis Royal: Fort Anne (the 1702–1708 Vauban earthworks, the 1708 and 1790s powder magazines, the garrison cemeteries; Charles Fort, under it, folded in), the Sinclair Inn (1708–1711), Adams-Ritchie House (1747), the de Gannes-Cosby House (1708), the O'Dell House Museum, St. Luke's (1815), the 1837 court house and the 1915 red-brick railway station. The Annapolis Basin shore: Port-Royal Habitation (1939 reconstruction), the Melanson Settlement (Acadian village site, traces only), North Hills Museum, Schafner Point and Victoria Beach lighthouses, Goat Island Baptist Church (c. 1810), Old St. Edward's at Clementsport (1797, box pews and pulpit) and the LeQuille woodworking mill. Up the valley: James House in Bridgetown, the Tupperville and Mount Hanley schoolhouses, Hampton lighthouse, and Old Holy Trinity at Middleton (1789–1797, box pews). Facts come from the Canadian Register statement for each place (historicplaces.ca via `page.py --all`), Parks Canada's visit and hours pages, the Annapolis Heritage Society's pages, the Old Holy Trinity trust's site and Middleton's town page, the James House Museum's site, and Lighthousefriends.com for lighthouse positions, owners and parking. Not checked: hours for every community museum (the Annapolis Heritage Society's three museums showed only "closed for the season"; Old St. Edward's, Tupperville, Mount Hanley and James House had no hours page read; Hampton lighthouse hours are Lighthousefriends' only); the present use of Adams-Ritchie House and the railway station; service times at St. Luke's and Goat Island; the owners of Schafner Point and Victoria Beach lights rest on Lighthousefriends alone. Red brick is recorded only for the station (the Register says red brick), 'no' for the wooden lighthouses and the Melanson site, and '?' elsewhere. Pins were checked on the Esri aerial only (no `--lidar`: no 1 m LiDAR here); Melanson was under cloud, Victoria Beach is `area`, LeQuille `area`, and Hampton's pin is near the wharf head rather than plainly on the tower.

## Leads
Places you read about and could not finish. One row each.

| Place | Where | What is known | What is missing |
|---|---|---|---|
| Torbrook iron mines | Torbrook, NS (44.914, -64.978, community) | Wikipedia and notyourgrandfathersmining.ca: mined from the mid-1800s, Canada Iron Company's No. 2 mine employed 120 in 1910, closed about 1913 | Any source on what is left on the ground and who owns it |
| Margaretsville "Tower" | Margaretsville, NS (Register id 10084; 45.0494, -65.0649) | A federal Register listing named only "Tower" | historicplaces.ca page 10084 would not read; what it is |
| Old St. Alban's Church | Lequille, NS (Register id 14126) | 1892 Gothic Revival chapel of ease, deconsecrated, now a private house | Left out: a private home; view only |
| Bailey House | 150 St. George Street, Annapolis Royal (Register id 2911) | c. 1770 house per the Register's nearby list | Its statement not read |
| CFB Cornwallis buildings | Cornwallis, NS (Register ids 11236, 11252) | Federal heritage buildings on the old naval training base | Statements not read; access |

## Tips
- In the Wikipedia "List of historic places in Annapolis County, Nova Scotia", each `{{HPC row}}` has three id fields, `idf` (federal), `idp` (provincial) and `idm` (municipal); all three are historicplaces.ca ids for `place-lieu.aspx?id=`. Parse all three, not just `idp`.
- The same list put the de Gannes-Cosby House at 44.4427, -65.3045 (about 33 km off); the ArcGIS geocoder's PointAddress for the street address was right. It put 50 Dugway Road, Lequille 2 km off (StreetAddress), where the list point was better.
- historicplaces.ca read every page but one (10084) through `page.py --all -n 60000` with a 5-second pause between pages.
- Parks Canada hours pages: `https://www.parks.canada.ca/lhn-nhs/ns/<site>/visit/heures-hours` (Port-Royal uses `hours-heures`); the `www.` host answered where `parks.canada.ca` reset the connection, and a second try a few seconds later worked.
- Lighthousefriends.com pages (`light.asp?ID=`) give a position, parking and owner under "Visitor Information"; they are a write-up, so hours from them are flagged as not from the owner.
- Web search in this session returned titles and links only, no quoted text.
