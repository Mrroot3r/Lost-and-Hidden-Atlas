# fl_ajmb: Florida: second scatter, DeFuniak Springs to Key West
state: Florida
region: fl
date: 2026-11-22
places: 19
file: data_fl_ajmb.py

## What this batch is
Nineteen places spread across Florida, none on the map before, taking the state from 32 to 51: the Chautauqua Hall of Brotherhood (DeFuniak Springs), St. Mary's Episcopal Church (Madison), the Orman House (Apalachicola), the Lodge at Wakulla Springs, Dudley Farm (Newberry), the Marjorie Kinnan Rawlings home (Cross Creek), the Dunlawton sugar-mill ruins (Port Orange), Ponce de Leon Inlet Light, the Tampa Bay Hotel (Plant Hall), the Fort De Soto batteries, Ca' d'Zan (Sarasota), the Edison and Ford Winter Estates (Fort Myers), the House of Refuge at Gilbert's Bar (Stuart), Jupiter Inlet Light, the Ancient Spanish Monastery (North Miami Beach), Coral Castle (Homestead), the Bahia Honda Rail Bridge, Indian Key and Fort East Martello (Key West). Sources: Wikipedia articles and Register lists via wiki_raw.py; operators' pages via page.py (the Florida State Parks system guide booklet PDF, Volusia County, Pinellas County, Ponce Inlet Lighthouse, Plant Museum, The Ringling, Edison Ford, Historical Society of Martin County, Jupiter Lighthouse, spanishmonastery.com, coralcastle.com, kwahs.org, stmarysofmadison.org, the Wakulla lodge's history page); one HMdb marker for the Chautauqua hall. Not checked: anything on the ground; hours for the Orman House, Bahia Honda and Indian Key (state park pages answer 403) and for the Wakulla park gate; owner and opening of the Chautauqua hall; parking at St. Mary's, Orman House, Plant Hall area beyond the museum's own page, Ca' d'Zan, Edison Ford, the monastery, Coral Castle and Fort East Martello. The Dudley Farm pin is on the farm-building cluster seen on the aerial (area precision), not on a named farmhouse. Dunlawton's county page said the gardens were closed for high water when read. Fort East Martello has no picture (Commons had only an interior).

## Leads
Places you read about and could not finish. One row each.

| Place | Where | What is known | What is missing |
|---|---|---|---|
| Historic Spanish Point | Osprey, FL (27.2013, -82.4903) | Museum grounds with a pioneer homestead, packing house, chapel and Calusa shell midden (Wikipedia) | Operator's hours page; which buildings are old |
| Dial-Goza House, Wardlaw-Smith House | Madison, FL (30.470, -83.413) | Register listings in the Madison old town centre (Register list) | Not read; owners and whether either opens |
| West Martello Tower | Key West, FL (24.546944, -81.786111) | Register listing (76000602); garden club grounds | Not read; operator's hours |
| DeLand Hall | DeLand, FL (29.035, -81.303333) | Register listing (83001441), Stetson University | Not read |

## Tips
- Florida State Parks web pages still answer 403 to page.py; the system guide booklet PDF gives hours for Dudley Farm and the Rawlings home but not for most parks.
- tools/geo.py (ArcGIS PointAddress) put the Madison church, the Spanish Monastery and Fort East Martello on their buildings where Wikipedia or Register points fell on roads or trees; Wikipedia's Dudley Farm point is on State Road 26.
- ringling.org/visit/help, edisonford.org (front page footer), coralcastle.com/visit and kwahs.org/visit/<museum> read in full with page.py; plantmuseum.com/discover/visit-accessibility gives the museum hours.
