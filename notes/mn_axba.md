# mn_axba: Minnesota: a first scatter across the state
state: Minnesota
region: mn
date: 2026-11-20
places: 16
file: data_mn_axba.py

## What this batch is
Sixteen places spread across Minnesota, which had 15 (14 in Washington County): Split Rock Lighthouse, Glensheen, the River Inn and Swinging Bridge at Jay Cooke State Park, the Soudan Underground Mine, the Kettle River Sandstone Company Quarry ruins in Sandstone's Robinson Park, Historic Fort Snelling, the Folsom House at Taylors Falls, the Seppman windmill in Minneopa State Park, the Fort Ridgely foundations, the Harkin Store at West Newton, Pipestone's quartzite downtown, the Wasioja Seminary ruins (stabilised and opened in July 2026), the Dodge County Courthouse at Mantorville, the Pickwick Mill, Historic Forestville and the Comstock House in Moorhead. Facts are from Wikipedia read with wiki_raw.py, two Register forms read with page.py (91000877, 77000761), Dodge County's news page, a KTTC report, and the managing bodies' own pages. MNHS and Minnesota DNR pages are drawn by script, so they were read in a headless Playwright browser on November 20, 2026. Not checked: anything on the ground; the summer hours of the MNHS houses (Folsom, Comstock, Split Rock), which were closed or on winter hours when read; Robinson Park's and the Wasioja ruins' hours and rules; parking at Seppman Mill, the Harkin Store, Glensheen, Folsom House and the Pickwick Mill; whether the Seppmanns' stone house survives; brick at Fort Snelling, Soudan, Forestville, Harkin, Comstock and Wasioja ('?'). Pins: Soudan was moved from the Wikipedia point (in woods) onto the mine buildings, Fort Ridgely onto the commissary. The Kettle River quarry pin is the park outline, not a particular ruin.

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Banning quarry ruins | Banning State Park, Sandstone, MN (46.16472, -92.85444, park point) | Wikipedia: quarrying 1892 to about 1905, remains of the quarry along the Kettle River | The DNR page (November 20, 2026) says most of the park is closed for construction until October 2027; a pin on the ruins |
| Hill Annex Mine | Calumet, MN | Former state park with mine tours | The DNR page says the state park is permanently closed; who owns it now and whether anything can be seen |
| Lac qui Parle Mission | Chippewa County, MN (45.02372, -95.86819) | Wikipedia: 1835 mission, rebuilt chapel, Register archaeological district | Who runs it now and when it opens; Wikipedia's MNHS link is old |
| Wasioja Historic District (the rest) | Wasioja, MN (44.0805, -92.8190) | Register list: Baptist church, stone Doig house, school, Civil War recruiting station, limestone kiln | Each building's position and owner; Legacy Fund pages (legacy.mn.gov) answer 403 to page.py |
| Split Rock Bridge | Split Rock Creek State Park, Ihlen, MN (43.891914, -96.367218) | Register list: 1937–38 quartzite arch, the longest stone arch span on a Minnesota highway | A source opened on access and a pin check |
| Mantorville Historic District and Hubbell House | Mantorville, MN (44.0667, -92.7553) | Register list: 24 buildings of 1854–1918 including the Hubbell House hotel (1856 in one source, 1857 in another) | Hubbell House's own page for hours |

## Tips
- MNHS (mnhs.org/<site>/visit/hours) and Minnesota DNR (dnr.state.mn.us/state_parks/<park>/index.html) pages are drawn by script: page.py and hours.py read the hours rows empty. A ten-line Playwright script (chromium.launch with the HTTPS_PROXY as its proxy, page.goto with waitUntil 'networkidle', then innerText('body')) read every one of them in full. The DNR's tours.html page timed out.
- MNHS's winter pages list every day "Closed" for seasonal houses; read the summer hours in the open season.
- Wikipedia infobox points for big sites (Soudan Mine, Fort Ridgely) fell 400 to 500 m off the buildings; the ArcGIS geocoder's PointAddress hit for the site's street address landed on the right building every time here.
- Web search for MNHS hours returns titles and links only, no quoted text.
