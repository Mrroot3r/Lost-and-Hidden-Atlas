# kcmo_exsp2_wvnk: Excelsior Springs, second pass
state: Missouri
region: kcmo
date: 2026-11-25
places: 15
file: data_kcmo_exsp2_wvnk.py

## What this batch is
Fifteen places in Excelsior Springs, Clay County, a second pass after kcmo_exsp_hrqd. Every Register-listed building in the four ground counties near here was already on the Atlas (compared by distance against the Register rows), so this batch went to what the Register forms name inside districts. The three forms that read well through `page.py` on NPGallery are the Elms Historic District (2014, 7575106e-7dbc-4474-a57a-8af52b0026f6), the Boarding House District (fb78e52d-b7b9-4048-bb37-975616d209a6) and the multiple-property form "Historic Resources of Excelsior Springs" (023103d8-f693-4dac-a575-e1c33e6e0dda). They gave: two Wabash depots, St. Luke's and St. Ann's churches, the Elms Hotel's pump house, well and carriage house, the Barbee Memorial church and the Hiawatha rooming house in the Boarding House District, and the three districts as entries of their own. Also from the multiple-property form: the Superior No. 1 pagoda, the stone pavilion for the Link Soda spring, and the Salt Sulphur and Sulpho-Saline wells on Salem Road. The Royal Hotel comes from two Excelsior Citizen articles and a search result quoting a Missouri State Parks survey. Not checked: any interior, any owner, all hours (the restaurant in the 1927 depot has hours="?"), whether the Link Soda ruin and the Salem Road wells can be seen from a public way. The pagoda, the Link Soda pavilion and the Salem Road wells were not found on the aerial; their pins are area pins on an address or on the park. Pins for the two commercial districts use the Atlas's own pins for named buildings, not the Wikipedia point, which was 1 km off. Pictures: three places have a Wikipedia article; three got a Commons photo (St. Luke's, St. Ann's, and the old post office for the west district); nine have none.

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Superior No. 1 pagoda | Fishing River Linear Park, Excelsior Springs, MO | Register form: one of two surviving pavilions over their own wells; the city trail guide says it is visible from the Fishing River Linear Park Trail | Its exact spot; the pin is the park area |
| Link Soda and Sulpho Salt pavilion | 200 E. Excelsior St. or 120 E. Bluff St., Excelsior Springs | Register form: a stone pagoda; a state survey quoted in search results: remains of a circular limestone balustrade | Which address is right; whether it shows from a street |
| Ideal Hotel, I.O.O.F. Building, J. C. Penney, Newberry, McCleary Thornton-Minor Hospital | Excelsior Springs, MO | Named, with dates, in the Wikipedia article for the Commercial West district | Addresses and what each is now; the 1999 form is only a placeholder on NPGallery |
| Flanders Dry Goods, A. M. Howard Drug Store, Huey Building, Oriental Bazaar, Excelsior Baths, Eagles Lodge Hall, Kennedy Building | Excelsior Springs, MO | Named in the Wikipedia article for the Commercial East district | Same |
| The Oaks (Snapp Hotel, 1907; rebuilt) | Excelsior Springs, MO | Multiple-property form: Snapp Hotel opened June 1907; contributing to the West district | Address and present state; also listed as an older lead |
| North Main Street well sites | Excelsior Springs, MO | Register form: two of the city's most significant wells at the end of N. Main St keep concrete and metal structures | A spot a visitor can see |

## Tips
- `page.py` reads the 2012 to 2018 Excelsior Springs forms on NPGallery (`GetAsset/<uuid>` links from a web search for "NRIS <ref>"); the `_text` route for the 1999 district forms is a placeholder. The inventory in these forms lists address, name, date and a description of every building: grep for the street names.
- `page.py` splits sentences at "No. 1" and "E.", so a `-g` grep can cut a sentence short; read the cached page in `research/pages/` for the whole text.
- The Wikipedia point for the Commercial West district is about 1 km from downtown; check district points against the Atlas pins for the named buildings.
- The Atlas's Register-by-distance comparison (`build/sites.json` against `wiki_raw.py --rows`) shows Jackson, Clay, Platte, Ray and Cass counties have no listed building left without an Atlas place; the next gain near Kansas City is inside districts' inventories, or in Kansas.
