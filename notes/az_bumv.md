# az_bumv: Arizona: a first scatter across the state
state: Arizona
region: az
date: 2026-11-22
places: 16
file: data_az_bumv.py

## What this batch is
Sixteen places spread over the Arizona counties earlier batches had not touched (only Cochise and Yavapai had been worked, plus the capitol in Phoenix), one or two a county: Yuma Territorial Prison and the Yuma Quartermaster Depot (Yuma); Swansea ghost town (La Paz, BLM); the Durlin (Oatman) Hotel and Winsor Castle at Pipe Spring (Mohave); Riordan Mansion and Wupatki Pueblo (Coconino); Hubbell Trading Post (Apache); La Posada and the Winslow depot (Navajo); the Gila County Courthouse in Globe; Casa Grande Ruins and the 1891 Pinal County Courthouse in Florence (Pinal); Vulture City (Maricopa); the Fort Lowell hospital ruins in Tucson (Pima); Tumacácori mission and Tubac Presidio (Santa Cruz). Sources: Wikipedia read as raw text with `wiki_raw.py`; Arizona State Parks facility pages, NPS hours, history and "places" pages, the BLM Swansea page, yumaprison.org, the Tucson Presidio Trust and laposada.org read with `page.py`. Pins looked at on Esri satellite (and the LiDAR sheet); Hubbell, Pipe Spring, La Posada, the Pinal courthouse and Tumacácori were moved. Not checked: anything on the ground; hours for the Oatman Hotel, La Posada, the Globe arts centre (cobrevalleyarts.org would not connect) and Vulture City (the owner's tour page answered 404); NPS entrance fees for Wupatki, Tumacácori and Pipe Spring; which building at Hubbell is the trading post itself (pin is on the compound); the exact roof over the Fort Lowell hospital ruins (pin marks the park area). Durlin Hotel: Wikipedia and the Register give 1924, the NPS page says built 1902 and rebuilt 1924 (conf mixed). Pipe Spring and Hubbell lie within the Kaibab Paiute and Navajo reservations but are National Park Service sites that invite visitors; Mission San Xavier del Bac (Tohono O'odham Nation) was left out for that reason, to be decided by someone who knows how the native layer should take it.

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Mission San Xavier del Bac | Tucson, AZ (32.107, -111.008) | Wikipedia: rebuilt 1783–1797, oldest European building in Arizona, on the San Xavier reservation | Whether it belongs on the main map or the native layer; the parish's own visiting hours |
| McFarland State Historic Park (first Pinal County Courthouse, 1877) | Florence, AZ | Named in the Second Pinal County Courthouse article | Arizona State Parks page not read; pin |
| Wukoki and Citadel pueblos | Wupatki National Monument, AZ | NPS "things to do" pages exist for both | Not read; pins |
| Durlin Hotel neighbours: Oatman historic structures | Oatman, AZ | Wikipedia has "List of historic structures in Oatman, Arizona" | Not read |

## Tips
- NPS `planyourvisit/hours.htm` read in full with `page.py --all` for Hubbell, Pipe Spring, Tumacácori, Casa Grande and Wupatki; `basicinfo.htm` gave only headings.
- Arizona State Parks slugs are not always the park name: Tubac Presidio is `azstateparks.com/tubac/...`; the Yuma prison has no facility page there, its museum site `yumaprison.org/admission/` gives hours.
- Casa Grande Ruins: the NPS hours page says 9 to 4, an older "Enjoying" page says the visitor centre is 9 to 5; the hours page was used.
- `nom.py` returned "HTTP Error 629" once when called quickly in a row; a pause of two seconds between calls fixed it.
- `pix.py pin` coordinates are pixels in the whole sheet; a first move of the Pinal courthouse went the wrong way and was put right on the second pin check. Always run the pin check again after moving.
