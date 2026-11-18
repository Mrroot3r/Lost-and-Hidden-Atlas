# conf_simf: Cohoes, Waterford and the old Champlain Canal
state: New York
region: conf, sar
date: 2026-11-18
places: 15
file: data_conf_simf.py

## What this batch is
Fifteen places in region `conf` (drawn at random by `choose.py --state ny`), with two in Halfmoon filed under `sar` like the Mechanicville and Vischer Ferry places. Old Champlain Canal (all on the Champlain Canalway / Empire State Trail): Lock 4 (north guard lock) at the Waterford Historical Museum, the weigh lock, Locks 5 and 6 at North Waterford, Flynn's Lock 7 with the 1871 waste weir and culvert, and Hewett's Lock 8. Standing: the Waterford Historical Museum (Hugh White Homestead, 1830), Waterford village's Broad and Second Streets (one area pin), the Ormsby-Laughlin mill (1894), the Cluett, Peabody bleachery on Peebles Island, and in Cohoes the Music Hall (1874), Ogden Mill and the Olmstead Street row houses, the former St. John's Church (the library, closed since a wall fell in 2021), City Hall (1895), the 1864 Troy Manufacturing mill with the Egberts & Bailey marker, and the D&H freight house (1910). Sources were read with `wiki_raw.py` and `page.py`: the American Canal Society's Champlain Canal sheet (condition and a coordinate for every lock, which gave the canal pins), the 2019 Champlain Canalway Trail action plan, a Bike It or Hike It trail log, American Trails (Halfmoon), Lakes to Locks Passage, the Pomeroy Foundation, the Spindle City Historic Society's 2023 downtown tour PDF (most of the Cohoes facts), the Waterford Museum's 2009 walking tour and its visit page, HMdb markers, WAMC and NYS Parks. Not checked: nothing on the ground; trail hours for the canal sites (no town page was read: the Town of Halfmoon's page answers 403); the dirt lot at Lock 4 is from the trail log only; whether the unimproved trail north of Upper Newtown Road reaches Lock 8; Lock 6 was not seen on the aerial; current use of the Ormsby-Laughlin mill, the freight house and the Troy Manufacturing mill; what has happened to the St. John's building since May 2024. The freight-house pin was moved onto the long gabled building beside the track, which matches the Wikimedia photo's shape but no source places it. Red brick was settled from Wikimedia photos for the Ormsby-Laughlin mill and the freight house, and from the society's tour for the Music Hall.

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Watervliet Arsenal and its Iron Building | Watervliet, NY (42.71833, -73.70861) | Wikipedia, Clio, ASCE: 1813 arsenal, National Historic Landmark; 1859 cast-iron storehouse, museum closed to the public in 2013 | Whether anything can be seen from outside the fence |
| St. Mark's Episcopal Church | Green Island, NY (42.74167, -73.69167) | Wikipedia: 1866–67 Gothic Revival stone church with polychrome slate roof, 1883 brick rectory, NRHP 1978 | Whether it is still a church and still standing as described |
| Rensselaer and Saratoga Railroad Green Island Shops | Green Island, NY (42.75056, -73.69278) | Wikipedia: 1871 car shop burned March 3, 2011 and was demolished; the roundhouse and octagonal water tower are not mentioned after that | Whether the roundhouse or water tower still stand |
| Hayward grist mill (barber shop) | 94 Remsen St, Cohoes, NY | Spindle City tour: 1854 grist mill; its small turbine is still in the basement | Owner and whether the turbine can be seen |

## Tips
- The Spindle City Historic Society's tour PDFs (`spindlecity.net/Brochures/...2023.pdf`) have text layers and give dates and present uses building by building for downtown Cohoes; the canal brochure in the same folder names which Cohoes Erie lock walls can be seen.
- The ACS Champlain Canal sheet gives degrees-minutes-seconds with "E" in place of the degree sign (`42E46'48.92"N`); every lock from 1 to 9 matched an OpenStreetMap ruin lead to within about 10 m.
- `check.py` refuses `rail` as a tag; the series tag for railroad buildings is `stations`, and a freight house fits none, so leave tags empty.
- `places_test.js` still fails only on `zion-cemetery-baynard-mausoleum` (as the hud_sgld and mohw_beqc notes said); this batch changes nothing it reads.
- NRHP `_text` PDFs for 86000470 and 98000135 were the one-page placeholder, as the mohw_beqc note found in Herkimer County.
