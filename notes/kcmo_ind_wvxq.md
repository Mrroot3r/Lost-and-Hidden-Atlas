# kcmo_ind_wvxq: Independence, Missouri
state: Missouri
region: kcmo
date: 2026-11-23
places: 11
file: data_kcmo_ind_wvxq.py

## What this batch is
Eleven places in Independence, Missouri (houses shown by tour, the 1859 jail, the Truman Home, the courthouse, the depot, two churches, the mill remnant, the trail ruts, the Drumm institute). The Atlas had none in the town. Sources: Wikipedia as raw text, the operators' own visit pages (Vaile Mansion, Bingham-Waggoner Estate, Jackson County Historical Society, National Park Service), the City of Independence's visitor pages, MillPictures.com, and web search results quoting the Truman Library. The National Register forms could not be read (NPGallery gives a placeholder for the older ones). Not checked on the ground: interiors, what the Truman Courthouse keeps of the 1836 building, whether the mill building is open, exact line of the trail ruts, Trinity Church and Stone Church service times. Three pins were moved after the aerial (Vaile, Bingham-Waggoner, Trinity). Brick is "?" for most because no source opened gave the material.

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Englewood Theater | Englewood Arts District, Independence, MO | Art deco theatre of 1949, vacant for years, bought by a nonprofit in 2025, put on the National Register in 2026 (news results) | A street address or coordinate from a source; the nomination |
| Mount Washington School | 570 S. Evanston Ave, Independence, MO | Four-room brick school of 1903, National Register 2013, reworked as senior housing (search result) | A source that opens; whether anything is shown to the public |
| Temple Lot and Independence Temple, Auditorium | Lexington Ave, Independence, MO | Temple Lot (1831 dedication, Wikipedia); Stone Church is added | Whether the headquarters buildings are old enough or worth a pin |
| Other Independence register houses | Independence, MO | National Register list names Lewis Jones, Kritser, Charles Minor, Owens-McCoy, Woodson-Sawyer, Noland and Georgen houses | A source for each that says what stands and who owns it |
| Blue Mills | Independence, MO | National Register listing with the coordinates withheld | Skipped on purpose: address-restricted |

## Tips
- Searches for operators' page addresses guessed from memory mostly 404ed (jchs.org, indepmo.org); search first and take the address from the result.
- page.py without --all prints only lines with clock times; with --all lines are long, so pipe through tr -s ' .' and grep -o for a phrase.
- nom.py found nothing for a theatre by name; give it a street address.
