# men_hqzv: Downeast and northern Maine: forts, a tavern, a lighthouse and Acadian buildings
state: Maine
region: men
date: 2026-11-23
places: 14
file: data_men_hqzv.py

## What this batch is
Fourteen places across Washington, Hancock, Waldo and Aroostook counties, Maine (region `men`, which held 2 places when `choose.py --thinnest` claimed it): the state historic forts Knox, Pownall (Fort Point), O'Brien and Kent, the earthworks of Fort George in Castine and the site of Fort Sullivan in Eastport, Burnham Tavern and the Machias station, Little River Light, the Acadian Village at Van Buren, two Houlton landmarks, the Calais Observatory stones and the Ellsworth dam. Wikipedia was read as raw text; hours and fees for the four state sites come from the Bureau of Parks and Lands pages (maine.gov/fortknox, /fortobrien, /fortkent, /fortpoint) read with `page.py`; Burnham Tavern from its own tours page; the Acadian Village from the National Park Service page; Little River Light from the American Lighthouse Foundation and the Friends' directions page. Not checked: Fort George and Fort Sullivan hours and ownership, Barracks Museum hours, Machias station hours, Acadian Village daily times, Little River open-house dates, owners of the Calais stones and the Ellsworth dam, the interiors of every standing building. Pins were looked at on the Maine aerial; four were moved (Pownall 80 m, O'Brien 200 m, the Acadian Village 380 m, the Ellsworth power house 45 m). The Fort Sullivan pin is the general site (`prec='area'`); the magazine ruin was not found.

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Barracks Museum and magazine ruin, Fort Sullivan | Eastport, ME (44.9074, -66.98795) | Wikipedia: an officers' quarters is the Border Historical Society's museum, open July and August; a magazine ruin off McKinley Street | The society's own page with days and times, and the magazine's position |
| Eastport Historic District, Boynton Street HD, Central Congregational Church | Eastport, ME (44.905, -66.985) | National Register listings | Not read |
| Pike's Mile Markers, Calais Free Library, Holmes Cottage and Hamilton House | Calais, ME (45.188, -67.277) | National Register listings, two run by the St. Croix Historical Society | Not read |
| Lubec Channel Light, McCurdy Smokehouse, Lincoln House (Dennysville) | Lubec and Dennysville, ME | National Register listings | Not read |
| Aroostook County Courthouse and Jail, Smith Bridge site | Houlton, ME (46.1247, -67.8397) | Register list | Not read |
| Timmerhuset, Gustaf Adolph Lutheran Church | New Sweden, ME (46.9386, -68.1206) | Register list and Wikipedia | Hours and a source on what survives inside |
| Black Mansion (Woodlawn), Jonathan Fisher Memorial, Bass Harbor Head Light | Ellsworth, Blue Hill, Tremont, ME | Hancock County Register list | Not read |

## Tips
- `choose.py --thinnest` gave a region, not a state; Maine's other two regions already had 38 places.
- maine.gov/<fortknox|fortobrien|fortkent|fortpoint> read well with `page.py --all` and give the season, fee and a state coordinate. The state coordinate for Fort O'Brien and Fort Kent lands on a road and a bridge approach; the address lookup was better.
- The address lookup for 859 Main Street, Van Buren falls on the road, not on the Acadian Village's buildings, which lie 380 m to the east.
- Nearly every Register row in Aroostook County says "no coordinates (often address restricted)"; only about a third have a point.
- None of the Aroostook or Downeast leads layers (leads, vanished, mines) is rich in names here; `start.py` gave a mapped ruin without a name and vanished sites already well known.
