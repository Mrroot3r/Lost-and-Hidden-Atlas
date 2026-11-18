# mohw_beqc: Herkimer County: Little Falls, the old canals, Newport and the West Canada Creek
state: New York
region: mohw
date: 2026-11-18
places: 18
file: data_mohw_beqc.py

## What this batch is
Eighteen places in Herkimer County south of the Adirondacks, the first close pass there (region `mohw` drawn at random by `choose.py --state ny`; it offered Richfield Springs, which is in Otsego County, so the session took the Herkimer County side of the region, which held only the Little Falls lock, Herkimer Home and the Remington works). Canal remains: the Little Falls Aqueduct ruins (1822, central arch fell 1993), the guard lock of the 1795 Western Inland canal, Enlarged Erie Lock 36 below Lock E-17, and the Castle Creek Aqueduct with Lock 35 at Indian Castle. Standing: Fort Herkimer Church, Indian Castle Church (1769), the 1834 Herkimer jail, Salisbury Center covered bridge, the Newport, Middleville (Route 29 and Lalino) and Old City Road stone arch bridges, the Yale lock factory site and octagon house at Newport, Cold Brook Feed Mill, the Italian Community Bake Oven at Little Falls, Snells Bush Church, Trinity Church at Fairfield, the Norway Baptist Church (Norway History Center) and Holy Trinity Monastery at Jordanville. Sources were read with `wiki_raw.py` and `page.py`: Wikipedia, HMdb marker pages, the Pomeroy Foundation, the American Canal Society's Enlarged Erie index sheet (Erie-Canal3.pdf, read as text), eriecanal.org, the Little Falls Historical Society, Mohawk Valley Museums (church, museum and society pages with hours), the NY State Covered Bridge Society and the monastery's own visitor page. No National Register form was read (see Tips). Not checked: anything on the ground; whether the Cold Brook mill still has its machinery or stands as described in 1974; what of the Yale factory ruins shows from the road; the guard lock stonework (`area` pin on its marker); the farm road to the Castle Creek remains (eriecanal.org, 2008-2009); service times at Trinity, Snells Bush and the Fort Herkimer Church interior; jail tour dates; owners of the bake oven, Snells Bush, Cold Brook and the Middleville arches; parking for most rural places. Pins were looked at with `pincheck.py --lidar`: Fort Herkimer Church moved onto its OpenStreetMap building, Salisbury Center and Old City Road moved onto the road crossings with `pix.py`; the LiDAR shows Lock 36's chamber and the aqueduct stone pile. Snells Bush's pin is in a field 60 m from a lone building that may be the church. Red brick: 13 `no` from sources naming stone or wood, 4 `?`.

## Leads
Places you read about and could not finish. One row each.

| Place | Where | What is known | What is missing |
|---|---|---|---|
| Enlarged Erie Lock 40 | Jacksonburg, Herkimer County (ACS: 43.01590, -74.90398) | eriecanal.org: buried, only the top of the north wall visible, on a private road (Stegich Road) on private land; Clinton's Ditch Lock 7 and Culvert 71 nearby | A public view point; it is private |
| Enlarged Erie Locks 38 and 39 | Little Falls (ACS: 43.03959, -74.85809 and 43.03755, -74.86142; OpenStreetMap "Old Lock 38 Wall", "Old Lock 39 Wall") | ACS sheet: Lock 38 part of north wall, Lock 39 part of south wall | A source on what shows now and from where |
| Balloon Farm (Gates mansion) | Frankfort (Wikipedia 43.04056, -75.07917; the Register list gives 43.0003, -75.1267) | 1878 house where Carl Myers ran his aeronautical works from 1889; marker for Carlotta the Lady Aeronaut | Which coordinate is right; private house, view only |
| Fort Herkimer Waste Weir | German Flatts (OpenStreetMap ruin, 43.01892, -74.95536) | Mapped as a ruin on the Erie Canalway Trail by the church | Any written source |
| Fairfield Academy and Medical College | Fairfield, near Trinity Church | Medical college 1812-1839 (Mohawk Valley Museums); two HMdb markers 0.2 mile from Trinity Church | What, if anything, stands |
| Herkimer County Courthouse and Reformed Church | Herkimer, beside the 1834 jail | National Register listings | A source on fabric and access |

## Tips
- Every npgallery `NRHP/GetAsset/NRHP/<ref>_text` tried for Herkimer County (74001243, 07001019, 91002035) returns a one-page PDF titled "NRHP_PDF_Placeholder_Blurb", which `page.py` reports as NO TEXT LAYER (a scan). It is not a scan of the form; `page.py` could say so by checking the PDF title.
- Mohawk Valley Museums (`mohawkvalleymuseums.us/museums/<name>/`) has a page with address, phone and season hours for most churches, museums and societies in Herkimer and Montgomery counties; the slug is the place name (indian-castle-church, fort-herkimer-church, norway-history-center-and-historical-society).
- The American Canal Society's Enlarged Erie sheet (`americancanalsociety.org/wp-content/uploads/2019/08/Erie-Canal3.pdf`) has a coordinate for every lock and aqueduct, but its condition column drifts out of line from Lock 40 west; read the condition for those from eriecanal.org instead.
- `check.py` refuses `burial` as a tag; the series tag for a churchyard is `cemeteries`.
- `places_test.js` still fails on main with `zion-cemetery-baynard-mausoleum` (as the hud_sgld note said); this batch changes nothing it reads.
