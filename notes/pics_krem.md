# Pictures batch krem (2026-11-21)
tidied: 2026-11-26

Job 8, "pictures", run as a scheduled session. No new places and no pins: only photographs chosen for 30 places already on the map that had none.

Result: 14 places got a picture, 16 got none (recorded with `set ... none`). The picture details (address, credit, licence) were taken from Wikimedia Commons by `tools/photo_find.py`; nothing was typed by hand.

Hesitations, one line each:
- Merchants' Row, Perryville: the place is a street of buildings. Chose one Federal-style building on Buell Street (candidate 4); the others on the row look similar.
- Sharlot Hall Museum / Governor's Mansion, Prescott: chose the exterior of the log mansion (candidate 4, "Governors Mansion-1864-2"); the rest were interiors.
- Stephens County Courthouse, Breckenridge: candidates 1 and 2 seem to show the same 1926 courthouse; chose candidate 2 as the clearer front view.
- Prince Edward Battery, Charlottetown: chose the candidate captioned "The battery at Victoria Park" (earthwork with cannon); the battery is the grassed mound.
- Old Albany Academy (Philip Hooker): several candidates named the same red-brick building; chose the 2015 front view (candidate 9).
- Enlarged Erie Canal Lock 15, Cohoes: chose the ruined lock chamber in the grass (candidate 1, 3 m from the pin).
- Old Burial Hill, Marblehead: the burial ground itself; chose the hill with stones and gazebo (candidate 1).
- Thompson Memorial A.M.E. Zion Church, Auburn: chose a 2022 photograph taken mid-restoration (the building looks the same); the NPS photographs are of conservation work.
- Territorial Court House, Fort Macleod: chose the red-brick courthouse with its name sign (candidate 1, by name).
- Hospital Bridge, Downieville: chose the Pratt truss from the side (candidate 1, 0 m from the pin).
- Westport depot, Pollard Theatre, Whipple bridge at Normanskill Farm, Chalouperie Godbout: clear exterior views of the named building; chosen as the clearest candidate.

None (candidates or search found nothing that plainly shows the place): LeQuille Mill, Albany Basin, Alder Brook pit, Ramsay Stone House, Knox's Dam (the candidates were a bed and breakfast), Old Methodist Church Chester, Potsdam Civic Center, Old St. James (Port Hill), Boyd Pony Express Station, Stoddard glassworks, N. W. Faison House (candidate showed a different museum building), Gate 52 range remains, Erie Canal Lock One (highway views only), Diamond Head fire control station (summit views and trail tunnels, nothing clearly the station), St. Paul's Lutheran Church Berne (nothing within 150 m), Masonic Temple Idaho City (only HABS drawings, which were not used).

Not checked: nothing on the map was re-checked against the aerial in this batch (no pins were changed). The first five-place look ran past the shell's two-minute limit; the rerun with a longer limit answered, and no place was skipped.

Tips for the next picture session:
- Five-place looks can time out at two minutes in a shell: run `look` with a longer timeout (about 500 seconds) for each five.
- The list command reports 1,060 waiting places; the first 30 are picked by the tool's own order, so the next session will get different places.
