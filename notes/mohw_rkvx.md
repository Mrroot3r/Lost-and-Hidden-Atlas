# mohw_rkvx: Rome, the Oneida Carry, Delta and northern Oneida County
state: New York
region: mohw
date: 2026-11-19
places: 21
file: data_mohw_rkvx.py

## What this batch is
Twenty-one places in Rome and the north of Oneida County, New York (region `mohw`, drawn at random by `choose.py --state ny`, which offered Boonville, Palatine Bridge and Nelliston). Before this the Atlas had nothing within 12 km of Rome and one place (the Five Lock Combine) within 20 km of Boonville. Rome and the Oneida Carry: rebuilt Fort Stanwix (NPS), the Fort Bull / Fort Wood Creek earthworks (Rome Historical Society, guided tour only), the closed and decaying Erie Canal Village where the Erie was begun in 1817 (private, view from the road), the Lower Landing marker for the 1792 Western Inland lock, Zion Church (Upjohn, 1850), the Jervis house and library, the Arsenal House, the Rome courthouse, the 1928 Capitol Theatre with its Möller organ, and the Oriskany Battlefield. North: drowned Delta and its dam, the Western Town Hall built from Delta's hotel, the Floyd house (private), Camroden church, the Steuben Memorial and grave, Remsen's 1831 Stone Meeting House, the Wethersfield stone schoolhouse, the Holland Patent stone churches, Trenton Falls and its lost hotel, and in Boonville the Black River Canal warehouse/museum (the LEADS.md row, now removed) and the Erwin Library and Pratt House. Sources: Wikipedia with `wiki_raw.py`, HMdb markers (nearby lists round Rome, Delta, Boonville, Forestport), Rome Historical Society, NPS, NY State Parks pages, the canal museum's 2026 newsletter, Atlas Obscura and local radio-station news, all with `page.py`. No National Register form could be read: NPGallery gave placeholders for all seven tried. Not checked: opening hours of Jervis library, the Capitol, Erwin library/Pratt arts centre, the Stone Meeting House and Zion Church; Trenton Falls open days (the town's 2026 notice was gone, archived copy not fetched); who owns Erie Canal Village now; whether the Delta dam can be walked. Pins: the Stone Meeting House pin is Prospect Street, not the building (`prec='area'`); Trenton Falls is the falls, the hotel site was not located; Arsenal House is the Wikipedia point. Nothing was seen on the ground. Red brick: Jervis 'yes' and Arsenal House 'no' (painted) from Wikipedia photos; the Capitol, the courthouse, Erie Canal Village and the Pratt House left '?'.

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Mappa Hall | Barneveld, Town of Trenton, Oneida County, NY (Wikipedia 43.27306, -75.18944 falls in trees between houses) | Wikipedia: limestone Federal house of 1801–1809 for Adam G. Mappa, private home; Register 1982 | The building's position (no address found; geocoder and OpenStreetMap had nothing) |
| Black River Canal Lock 96 | Near Lyons Falls, Lewis County, NY (HMdb 258685: 43.58739, -75.34889) | HMdb marker only | Marker text and what remains; region is probably `nny` |
| Utica | Oneida County, NY | Atlas has nothing within 10 km of downtown; the Oneida County Register list has about 40 Utica rows: Union Station, Utica State Hospital (Old Main), Stanley Theater, Globe Woolen Mills, Fountain Elms, Rutger-Steuben Park | A session of its own |
| Delta drawdown remains | Delta Lake, Town of Western, NY | WIBX feature shows stone foundations and roads exposed when the lake was drained about 60 years ago | Whether anything shows at low water, and where |

## Tips
- Rome Historical Society's `romehistoricalsociety.org/historic-sites` reads in full with `page.py --all` and gives ownership, visiting rules and coordinates for Fort Bull, the Unknown Soldiers tomb and the Lower Landing.
- NY State Parks pages moved to `parks.ny.gov/visit/historic-sites/<name>-state-historic-site` and `parks.ny.gov/visit/state-parks/<name>`; the old `historic-sites/<name>/details.aspx` addresses are 404.
- NPGallery returned placeholders for every Oneida County form tried (03000093, 05000991, 95001277, 06001204, 91001670, 87002275, 09000635).
- `parking.py` gave a lot on Fort Stanwix's side that the aerial shows is a building roof (43.21167, -75.45737), and the "Erie Canalway Trail lot" at Erie Canal Village sits among the village's private buildings.
