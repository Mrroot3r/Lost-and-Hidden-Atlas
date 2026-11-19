# vtc_kaqi: Washington County, Vermont
state: Vermont
region: vtc
date: 2026-11-19
places: 19
file: data_vtc_kaqi.py

## What this batch is
Nineteen places in Washington County, Vermont (region drawn at random by `choose.py`): the abandoned granite quarries of Millstone Hill (Barre Town Forest), the Jones Brothers shed (Vermont Granite Museum), Hope Cemetery, the Old Labor Hall, the Twing gristmill and Barre City Hall and Opera House in Barre; the 1907 railroad turntable in Montpelier; the Old Meeting House and the Old Brick Church in East Montpelier; the Kent Tavern and the Old West Church at Kents Corner, Calais; the Northfield Falls / Lower Cox Brook pair and the Stony Brook covered bridge, the Old Red Mill and the 1852 depot in Northfield; the Roxbury fish hatchery; the Great Eddy and Warren covered bridges; and the 1944 B-24 wreck on Camel's Hump. Sources: Wikipedia (`wiki_raw.py --rows` on the county's Register list, then each article), HMdb marker texts (nearby lists round Barre, East Barre, Waterbury, Northfield and Waitsfield), and managing bodies' pages through `page.py` (Millstone Trails Association, Vermont Granite Museum, Vermont State Parks, Green Mountain Club, Town of Roxbury, Old Brick Church), with Seven Days (2026) for the Kent's state ownership and VTDigger for the Labor Hall, the hatchery's reopening and the bomber. Not checked: anything on the ground; hours for Hope Cemetery, the Opera House, Turntable Park, the Old Meeting House, the Old West Church and the hatchery; who owns the Old Red Mill and whether its machinery survives (the source is the 1977 Register form); the owner of Turntable Park. Pins that mark an area, not the thing: `camels-hump-b24-wreck` (nearest mapped point of the Alpine Trail to the summit; no source gives the wreck's coordinate) and `millstone-hill-quarries` (one flooded pit among dozens). Pins at `site` because the building was not told apart on the aerial: Kent Tavern, Old West Church, Old Brick Church, Old Meeting House, Old Red Mill. Brick: five set from Wikipedia pictures opened in the session (Twing mill, Old Brick Church, Northfield depot yes; Opera House yellow brick and Granite Museum siding no), the Kent Tavern from Seven Days ("red-brick"); the Old Labor Hall left '?' because its brick looks painted in the one picture.

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Kents Corner sawmill | Calais, VT (north of the Kent Hill Road junction on Robinson Cemetery Road) | A 19th-century sawmill (Wikipedia, 2006 Register increase); Seven Days dates the sawmill to 1803 | Owner, whether it can be seen from the road, a pin |
| Waterbury Feed Company mill and dam | Waterbury, VT (44.34306, -72.74778, Mill Village Historic District) | The only surviving mill of Mill Village, with its dam and penstock of about 1830 (Wikipedia) | Owner and current use; a pin on the building |
| Upper Cox Brook and Slaughter House covered bridges | Northfield, VT (44.17361, -72.65528; 44.16833, -72.65444) | 1872 queen post bridges (Wikipedia); named in the Northfield Falls entry only | Separate entries if wanted |
| Pine Brook Covered Bridge | Waitsfield, VT (44.20583, -72.79194) | 1872 king post, one of two left in the state (Wikipedia) | Not added for want of time; town road |
| Vermont State Hospital campus | Waterbury, VT (44.33182, -72.75055) | 1890 asylum, now the Waterbury State Office Complex; Register district 2016 (Wikipedia) | Which buildings survive and what the public may see |
| Green Mountain Seminary | Waterbury Center, VT (44.3775, -72.71806) | 1869 Italianate Free Will Baptist seminary (Wikipedia) | Current use and owner |
| National Clothespin Factory | Montpelier, VT (44.25222, -72.57111) | 1918 factory, the last US wooden clothespin maker until 2003 (Wikipedia) | Current tenants, a picture for brick |

## Tips
- `page.py`'s `-g` must come before the URL; after it, the pattern is read as a second URL and fails (the guide says so for `wiki_raw.py`; it bit here too).
- The NPS "Central Vermont" travel itinerary pages (`nps.gov/nr/travel/centralvermont/cvNN.htm`) that search results still list all answer 404 with no archived copy.
- The Green Mountain Club's "airplane crashes along the Long Trail" page answers 404; its Monroe and Alpine trails page (`greenmountainclub.org/?p=21274`) names the B-24 wreck on the Alpine Trail.
- Rock of Ages ended quarry tours and closed its visitor center in 2025 (search result title, vnews.com); the Millstone Trails Association's page still mentions the visitor center.
- HMdb nearby lists round Barre (5-mile radius) gave positions for most Barre buildings in one request.
