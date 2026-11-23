# nb_kfxr: Saint John, the Fundy islands, the river and the Miramichi, New Brunswick
state: New Brunswick
region: nb
date: 2026-11-23
places: 13
file: data_nb_kfxr.py

## What this batch is
Thirteen places spread across New Brunswick, which had 40: Saint John (Fort Howe, Partridge Island, the City Market, the Stone Church), the Kennebecasis valley (Trinity Church at Kingston, the Hampton court house), Maugerville on the Saint John River, the two lighthouses of the Fundy islands (Swallowtail on Grand Manan, Head Harbour on Campobello), two Miramichi buildings (the Marine Hospital at Douglastown and the 1829 court house), the nuns' cemetery at Tracadie and the cathedral at Edmundston. Fort Howe and Partridge Island were rows in the Leads table of nb_tqwk.md and are now deleted from it. Every place is from its Canadian Register of Historic Places statement (read with page.py); Wikipedia (wiki_raw.py) for Fort Howe, Partridge Island, Swallowtail and Head Harbour. Opening times for the City Market, the Stone Church, Trinity (Kingston), Maugerville and the cathedral come only from web search results that quote the operators' pages; none of those pages was opened, and each hours line says to confirm. Not checked: any interior, who owns the Fundy islands' lighthouse grounds, parking (only Head Harbour has a lot), whether Partridge Island can be landed on (the Register says no public access), and the exact position of the Tracadie cemetery and of the Head Harbour and Fort Howe buildings (the aerial could not show them; those pins are the area). Photographs: Hampton, Swallowtail, Head Harbour, the Marine Hospital and the cathedral were chosen from the finder's lists, the last three on their captions and positions only, without looking at the sheet.

## Leads
Places read about and not finished.

| Place | Where | What is known | What is missing |
|---|---|---|---|
| Fort Nerepis | Woodmans Point, Grand Bay-Westfield (Register point 45.3702) | National Historic Site 13166; the Register says the fort's remains have never been found, a cairn and plaque mark the point | A source for what is on the ground and public access |
| Bonar Law House | Rexton (Five Rivers), Kent County | Register id 6215 listed in the county list; its Register page would not open | Register text, hours, a source for what it is today |
| Tracadie lazaretto | Tracadie-Sheila | Cemetery added; Register lists the lazaretto's story | A source for the lazaretto building or museum |
| Old Ganong Candy Factory, Todd Mansion, St. Croix Cotton Mill Site | St. Stephen | Register ids 8449, 8357, 10612; pages would not open | Register text, museum hours |
| Middle Island, Miramichi | Miramichi River | 1847 Irish quarantine island; the hospital building was moved to Manse Street in Loggieville (Register 5571, local) | Register 5908 would not open; boat access |

## Tips
- historicplaces.ca resets many connections in a run of requests: fetch one page at a time with a timeout and retry the ones under 1,000 bytes a minute later (about half came back on retry).
- The Wikipedia county lists carry lat/lon but a few rows have a comment instead of a number; the Register's own address line, fed to the ArcGIS geocoder, was the better start for a pin, except the cathedral at Edmundston, where it fell on a building across the street.
- A web search was the only way to see hours: it returns quoted lines from official pages but not the pages themselves.
