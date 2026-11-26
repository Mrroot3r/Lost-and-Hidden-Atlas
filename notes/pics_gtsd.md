# Pictures batch gtsd (22 November 2026, scheduled run)
tidied: 2026-11-26

What this batch is: pictures only, for places already on the map that had none. No new places, no pins, no text. Pictures chosen by looking at Commons candidate sheets from `tools/photo_find.py next 5`.

Counts: 9 places got a picture from a sheet looked at in this session. 1 place (Treadwell mine ruins, Douglas) was recorded as none by me, because its candidates were a survey map and two thumbnails that would not load. 4 places were recorded as none by the tool itself, with nothing on Commons (Crescent Station, Dawn community / Harney Farm, Cook Hill crossroads cellar, Dutton Ridge ringed pit).

Places with a picture: Bankhead (Banff), Bergmann Hotel (Juneau), Charlton hamlet and Freehold church, First Presbyterian Southold (a pre-1923 postcard, the only historic view chosen), Hudson-Athens Lighthouse, Nutana (Pioneer) Cemetery, Zion Memorial Chapel (St Nicholas-on-the-Hudson), Stevenson Cottage (Saranac Lake), Wallace 1910 fire memorial (Nine Mile Cemetery).

Where the choice was less than certain:
- Bergmann Hotel: the two candidates whose names fit best (a 2017 photograph by Michaelh2001 and one at 3 m from the pin) did not load as thumbnails, so they were not seen. The chosen picture is by gillfoto, described on Commons as the Bergman Hotel in July 2017; it shows a boarded three-storey building, which fits the place's condemnation and vacancy, but a person should check the name and the size against the hotel.
- Treadwell: none chosen. The ca 1889 mill view (LAROCHE 133) is the likeliest, and a person may want to look at it.
- First Presbyterian Southold: the postcard shows a church with a monument in front; the church on the pin dates from 1803, and the postcard's date is not stated on the sheet.
- Wallace 1910 fire memorial: the chosen view is of the cemetery's cobblestone monument taken from above, with its grave covers visible; the other memorials on Commons belong to the Pulaski Tunnel and Bullion Mine sites and were not chosen.
- Bankhead: the chosen view is of a concrete powerhouse ruin, not of the whole town, which is what the place describes.
- Zion Memorial Chapel and Charlton: the chapel and church match their names and the pin.

Pull request: the only file is tools/pics_gtsd.py. The build was run twice because main moved between the first build and publish; the second build is the one published.

Tips for the next session: Commons thumbnails sometimes do not load at all (grey tiles), and a second `look` a few minutes later may still leave them grey. Note which candidate could not be seen, rather than choosing blind. A round of five took about 8 to 10 minutes in this session.
