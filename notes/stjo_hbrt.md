# stjo_hbrt: St. Joseph, Missouri
state: Missouri
region: kcmo
date: 2026-11-26
places: 18
file: data_stjo_hbrt.py

## What this batch is
Eighteen National Register places in St. Joseph (Buchanan County), about 48 miles from Kansas City: the courthouse, the 1891 police station, a bank, wholesale and commercial blocks, the Missouri Theater, Robidoux Row, Patee House and the Jesse James house, a fire station, a school, houses and the county infirmary. The Atlas had one place there. Facts come from Wikipedia read as raw text, the Allied Arts Council page for the Missouri Theater and the St. Joseph Museums page. The National Register forms could not be read (NPGallery holds a placeholder; the Missouri State Parks copies answer 404; the Internet Archive copy is refused by the fetch tool). Not checked: any interior, ownership of the houses, parking, and the days and times of Robidoux Row, Patee House, the Jesse James house and the police-station museum (no page of their own would open; listings disagree, so `hours='?'`). Pins: the Wikipedia point for the courthouse, Robidoux Row, Wyeth Flats and the infirmary was off and was moved by the aerial or OpenStreetMap; City Hose No. 9 and the Sachau Saloon are `prec='area'` because the aerial did not show which building is which. Red brick was set only for Patee House (a picture shows it); the rest are `'?'` because the sources say "brick" without a colour.
Why St. Joseph: the Kansas City ground is nearly used up. Jackson County still lists 65 Register places the Atlas lacks, but nearly all are 1920s apartment blocks, demolished (Blackstone Hotel, Holy Name church, Smith and Sons, Alana, Wiltshire, Ivanhoe temple) or have a form that cannot be opened; Cass, Platte, Clay, Lafayette and Johnson counties have one or two left each.

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Aines Farm Dairy Building (Foremost Dairy) | 3110 Gillham Road, Kansas City, MO (39.0698, -94.5768) | Moderne dairy plant of the 1940s, 50,000 sq ft, 100,000 gallons a day (Clio, Midtown KC Post) | The nomination form; today's use |
| Anderson Electric Car Company Building | 3240 Main Street, Kansas City, MO | Listed 2022; opened about 1912 as an electric-car dealership next to ABC Storage (Flatland KC) | The form; architect and condition |
| Seven Oaks School | 3711 Jackson Avenue, Kansas City, MO (39.058, -94.5346) | Opened September 1927, Mission/Spanish Revival, architect Charles A. Smith, closed 1997 | Today's use; a source for the building itself |
| Nettleton Home | 5125 Swope Parkway, Kansas City, MO | Colonial Revival, Wilder & Wight; given 1900 as a home for elderly women; moved out 1917 | Present use; the form |
| Rest of St. Joseph | Cathedral Hill, Museum Hill, Wholesale Row and about 20 more Register entries (St. Joseph, MO) | Listed in Wikipedia's Buchanan County list | Read the rest the same way |

## Tips
- Missouri State Parks nomination PDFs (mostateparks.com/sites/mostateparks/files/...) now answer 404, and the fetch tool will not open web.archive.org: in Kansas City a Register place with no Wikipedia article, no Clio entry and no news story cannot be written up.
- `choose.py --dry` refuses Jackson County because 65 listings remain, though most cannot be sourced; the message suggests Clio and SAH Archipedia, which only help for some.
- The Wikipedia list for Kansas City is split in "Jackson County, Missouri: Downtown Kansas City" and "...: Kansas City other"; `wiki_raw.py --rows` reads both.
- OpenStreetMap (`nom.py`) placed the Robidoux Row museum and Green Acres Rest Home correctly where the Wikipedia points were off.
