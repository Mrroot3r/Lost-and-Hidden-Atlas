# mb_kfwn: Manitoba: fifth scatter
state: Manitoba
region: mb
date: 2026-11-28
places: 9
file: data_mb_kfwn.py

## What this batch is
Nine standing places spread across Manitoba (65 before, 74 after), taken from the Province's list of Provincial Heritage Sites that earlier batches had not used: Virden CPR station, Pipestone Municipal Building (Reston), Griswold United Church, St. Elijah Romanian church (Lennard), St. Michael's Ukrainian Catholic church (Trembowla), Old St. James (Winnipeg), St. Anne's log church (Poplar Point), St. Paul's iron church (Churchill) and St. John the Divine (Wawanesa). Each rests on the Province's page and the Manitoba Historical Society's page (read with page.py; the Society's coordinate is the pin). Pins were looked at on the aerial; Trembowla's sits at a road bend among the museum grounds, so it is marked "area". Not checked: hours, parking, whether interiors can be entered (no operator pages were opened), brick colour at Reston. Dates and builders where the two sources differ are given both ways. No picture was found on Commons for any of the nine (all recorded as none).

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Winnipeg Beach CPR water tower (1928 steel tower, Provincial Heritage Site 103) | Stephenson's Point, Winnipeg Beach (about 50.50, -96.97) | Province page: 40 m riveted-steel tower by Vulcan Iron Works, 1928; Society page covers only the older tower's foundation | The tower's own coordinate (nom.py found nothing; the Society page for it was not found) |
| Old Kildonan Presbyterian Church | 201 John Black Avenue, Winnipeg | Province: 1854, stone, Duncan McRae, first Presbyterian church in Western Canada (Site 77) | Society page slug not found; coordinate |
| St. John the Baptist Ukrainian Catholic Church | Dolyny district, near Menzie (Site 66) | Province: 1904 to 1907, domed cross plan, stencils and carved iconostas | Society page and coordinate |
| Christ Church Anglican, Fort Alexander | Fort Alexander First Nation (Site 124) | Province: Red River frame church of 1868 to 1870 | Society page and coordinate; access on reserve land |
| La Rivière CPR station (Site 81) | near La Rivière, RM of Pembina | Province: only station left with this mansard-roof design, privately owned | Coordinate; the Archibald Museum page did not say where the station stands |
| Transcona Cordite Plant | Transcona, Winnipeg | (earlier note) | Society page long and not read in full |

## Tips
- Galloway Bros (Gladstone, Site 42) was demolished in 2024 and the Glenboro water tower (Site 92) burned in 2008: the Province's index still lists both, so read the Society's page first. A search limited to mhs.mb.ca for "Historic Sites of Manitoba <name>" finds the page slug; guesses at slugs mostly fail (3 of 25 hit).
- nom.py returned nothing for any of six Manitoba church names; the Society coordinate was the only pin source.
- photo_find.py: Commons has nothing for small Manitoba churches; candidates were same-name churches in Australia, Ontario and Winnipeg's modern St. Michael's.
