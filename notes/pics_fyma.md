# Pictures batch fyma (2026-11-22)

A scheduled pictures run. It chose photographs for 13 places that had none, in three rounds of `photo_find.py next 5`. The run stopped at the 40-minute limit, so about 30 places were not reached.

Results:
- 8 places got a picture chosen by looking.
- 5 places got "none" from the looking (no candidate plausibly showed the place).
- 6 places were recorded as "none" by the tool itself (Commons had nothing for them).

Places where I hesitated:
- st-pauls-anglican-harbour-grace: chose the Commons file that names the church exactly, St. Paul's Anglican Church, Harbour Grace. Commons places that file 23 km away, so the position is doubtful; the picture itself looks like the church. The church-hall file was a different building.
- rossie-iron-works: the only candidate is a 1992 HAER survey of a blast furnace plant in Pennsylvania, so it was set to none.
- east-nassau-central-school: a brick school with arched windows, named "(formerly)". Its date (1930) was not checked against the picture.
- homer-village-green: chose the Octagon House in the Old Homer Village district, 43 m from the pin. It is a building in the district, not the green itself.
- sacandaga-park: chose the Sacandaga Railroad Station, 299 m from the pin. It names the station, not the park; whether it stands inside the park was not checked.
- west-brookfield-railroad-depots: chose the former station (now the Quaboag Historical Society Museum), 19 m from the pin.
- port-townsend-carnegie-library: several good views; chose the front view.
- ozark-trails-obelisk-langston: chose the west face, 8 m from the pin.
- monument-lefebvre: the one name match (Monument Lefebvre.jpg) would not load on the sheet, so it could not be seen; set to none.
- valley-falls-historic-district: the candidates were a Central Falls, Rhode Island mill (another state); set to none.
- essex-village-historic-district: no candidate showed the village; set to none.
- old-military-crossing-cohoes: the candidates show the modern Crescent Dam, not the crossing; set to none.

Not checked: the rest of the waiting places. The next session can start with `python3 tools/photo_find.py next 5`.
