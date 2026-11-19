# nny_lgvj: St. Lawrence County: Ogdensburg, Morristown, Waddington, Canton and Potsdam
state: New York
region: nny
date: 2026-11-19
places: 20
file: data_nny_lgvj.py

## What this batch is
Twenty places in northern St. Lawrence County, drawn at random by `choose.py --state ny` (region `nny`, whose 18 earlier places were all in Jefferson County; the Atlas had nothing within 40 km of Waddington). Ogdensburg: the Fort de La Présentation site and Abbé Picquet Trail (traces), the Ogdensburg Harbor Lighthouse (private, seen across the river), the 1809–10 Parish Store (McEwen Custom House) and the Parish house that is the Remington Museum of Art. Morristown: McConnell's 1825 stone windmill, the Land Office and Wright's Stone Store (one pin), the 1824 schoolhouse. Waddington: St. Paul's and the 1884 Isaac Johnson town hall (one area pin). Canton: the Falls Island mill ruins and King bowstring bridge (Heritage Park), Herring–Cole Hall. Potsdam: Trinity Episcopal (red sandstone, Tiffany windows) and the Civic Center / Public Museum. Bridges: Madrid Stone Bridge (1882), Raymondville Parabolic (1886, closed), Massena Center Suspension (1910, closed). Also Buck's Bridge church (closed 2018), the Harrison Grist Mill and Trinity Chapel at Morley, Zion Episcopal in Colton, the Lisbon depot museum. Sources: Wikipedia via `wiki_raw.py`; HMdb nearby lists round Ogdensburg, Morristown, Waddington, Potsdam, Canton and Massena; the 2016 lighthouse Register form; the 2026 Waddington district boundary-increase form (parks.ny.gov State Review Board PDF); the Fort La Presentation Association, Grasse River Heritage, Remington Museum, Potsdam Public Museum, Diocese of Albany, Town of Lisbon, LighthouseFriends, Gribblenation, Bridgemeister and HistoricBridges pages through `page.py`. Not checked: nothing on the ground; hours for the fort trail, the windmill park, the Morristown schoolhouse, the Lisbon and Colton museums, Herring–Cole's reading room; owners of the Stone Store, the Harrison Grist Mill and the Buck's Bridge church (Wikipedia says moving the church to the Power and Equipment Museum in Madrid was considered). Pins moved: the Custom House onto the OSM "CBP Ogdensburg" building; the Morley mill and chapel onto the buildings next to their Register points (taken to be them, no photograph). Buck's Bridge church is an area pin in the field by the junction. The Morristown schoolhouse and windmill pins are list/marker points at site precision. Only the lighthouse's brick was settled from a photograph (painted brick upper tower, red brick chimney: `some`).

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Foote-Legge-Stocking Tavern ("1807 Tavern") | Heuvelton, NY (4365 NY 68; 44.65909, -75.32979) | Pomeroy Legends & Lore marker 73 (HMdb 304555): built by Stillman Foote on Billius Stocking's land, Legge tavern keeper | A source for the building's date, fabric and owner; marker is legend-series only |
| Halfway House | Lisbon, NY | Register listing 100009167 (no coordinates in the list) | NPGallery returned a picture, not the form text; a location and description |
| Chase Mills Inn | Chase Mills, NY | Register 78003122 | Form is not on line; location and present state |
| Pierrepont Town Buildings | Pierrepont Center, NY (44.541667, -75.010833) | Register 82001271 | Description; form is an NPGallery placeholder |
| Cox's Mill sandstone house | Hannawa Falls, NY (HMdb 79022, 44.611167, -74.974839) | Gardner Cox's sandstone house; sawmill of 1819 | Owner (likely private) and which house |
| Pyrites paper mill | Pyrites, NY (Grasse River) | North Country at Work photographs of the DeGrasse/Grasse paper mills | Whether anything is left and a public view point |
| Ogden Island and the Waddington power canal | Waddington, NY (HMdb 79491, 79494) | Mansion removed 1957; dam and canal 1804–1925; the 2026 Register form says the Seaway erased the industrial remains | Whether any trace shows at low water; probably nothing to see |
| Fort Lévis (Chimney Island) | St. Lawrence River off Lisbon/Johnstown | Ontario marker (HMdb 178522) on the Canadian shore | Which side of the border the island is on, and what is left |

## Tips
- Most pre-2000 Register forms for St. Lawrence County are NPGallery placeholders; the Wikipedia stubs are thin, so HMdb nearby lists (5 miles round each town) carried most of the batch.
- parks.ny.gov State Review Board PDFs (`parks.ny.gov/sites/default/files/<yyyy-mm>/SRB_...pdf`) are new Register forms with text layers; the Waddington one (140 pages) read with `page.py` and the cached copy in `research/pages/` searched well with a short Python regex.
- The Frederic Remington Art Museum renamed itself the Remington Museum of Art in 2026; its old `hours-of-operation-c16.php` page is 404, hours are at `fredericremington.org/plan-your-visit/`.
- `publish.sh` stopped twice in ten minutes because other batches merged (an app change, then Orange County); `resync.sh` handled both.
