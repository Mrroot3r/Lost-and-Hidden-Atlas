# fl_ezoz: Florida: first scatter, Pensacola to Key West
state: Florida
region: fl
date: 2026-11-21
places: 13
file: data_fl_ezoz.py

## What this batch is
Thirteen places spread across Florida outside St. Augustine (which fl_xhar covers): Kingsley Plantation (Jacksonville), Fort Clinch (Fernandina Beach), the Bronson–Mulholland House (Palatka), the New Smyrna sugar mill ruins, the Yulee sugar mill ruins (Homosassa), the Gamble Plantation mansion (Ellenton), Bok Tower (Lake Wales), the Koreshan Unity settlement (Estero), Cape Florida Light (Key Biscayne), Fort Zachary Taylor (Key West), Fort Pickens (Pensacola), San Marcos de Apalache and St. Marks Light (Wakulla County). Sources: Wikipedia via wiki_raw.py; operators' pages via page.py: NPS (Timucuan hours and visiting pages, Gulf Islands Fort Pickens Area and history pages), the Florida State Parks system guide booklet PDF (park descriptions and the few hours it gives), USFWS St. Marks refuge pages, Volusia County's Sugar Mill Ruins page, Bok Tower Gardens' FAQ, the City of Palatka facility page. Not checked: anything on the ground; hours for Fort Clinch, Yulee, Koreshan, Fort Zachary Taylor and Cape Florida (floridastateparks.org park pages answer 403; the general "8 a.m. to sunset" is from Wikipedia and stays in the access notes, not hours=); Fort Pickens hours (no NPS page read gave them); Bronson–Mulholland House hours (the city page gives none; Clio's are in the access note only); parking for Yulee, New Smyrna, Koreshan, Fort Zachary Taylor, Bronson–Mulholland and Gamble. Site-precision pins (the building was not picked out on the aerial): Kingsley Plantation, Yulee, Cape Florida Light, Gamble mansion. The Gamble mansion's opening is conf='mixed' (Wikipedia says both "closed to the public in 2014" and "guided tours available"). Moved with pix.py: New Smyrna onto the coquina ruin, St. Marks Light out of the bay onto the keeper's house.

## Leads
Places you read about and could not finish. One row each.

| Place | Where | What is known | What is missing |
|---|---|---|---|
| Fort Jefferson | Garden Key, Dry Tortugas, FL (24.6286, -82.87221) | Written up and pin-checked this session (Wikipedia; NPS hours, fees and directions pages: fort open sunrise to sunset, $15 entrance, ferry from Key West); photo Fort_Jefferson_FL3.jpg on Commons fits | check.py says the pin is in no listed state: the Florida outline in tools/outlines.py does not reach the Dry Tortugas. Needs the outline widened (a tool change for the owner or maintainer), then the entry can be added |
| Prospect Bluff Historic Sites (Fort Gadsden, the "Negro Fort") | Apalachicola National Forest, near Sumatra, FL (29.93333, -85.01667) | Ruins of the 1814 British fort and the 1818 Fort Gadsden (Wikipedia) | Forest Service closure order closed the whole site until August 12, 2026; whether it has reopened was not found |
| Egmont Key, Fort Dade ruins | Egmont Key, mouth of Tampa Bay, FL (lighthouse 27.60081, -82.76067) | 1858 lighthouse and Spanish–American War Fort Dade ruins, boat only (Wikipedia; FSP guide) | A pin on the ruins themselves and the operator's ferry and hours page |
| Mission San Luis | Tallahassee, FL (30.44909, -84.31991) | Living-history museum; the buildings are 1990s and later reconstructions on the 1656 mission site (Wikipedia) | Decide whether a reconstruction belongs; hours from the operator |
| Pensacola Light and Fort Barrancas | NAS Pensacola, FL | 1859 tower open daily (Wikipedia); Fort Barrancas in Gulf Islands NS | Access rules for the naval air station gate |

## Tips
- The Florida State Parks system guide booklet (floridastateparks.org/sites/default/files/media/file/FSPSystemGuide_Booklet_ForReview-1.pdf) reads with page.py and has one paragraph per park with its address, and hours for some (San Marcos, Gamble, Bulow, The Barnacle); it is the operator, so usable where the park pages answer 403.
- tools/outlines.py's Florida outline leaves out the Dry Tortugas, so check.py refuses Fort Jefferson (see Leads); widening it would open Florida's best-known fort.
- A Wikipedia infobox coordinate for a lighthouse can fall in the water (St. Marks); the keeper's house showed on the parking-lot tile.
