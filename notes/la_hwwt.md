# la_hwwt: Across Louisiana: steam pumps, earthworks, Creole houses and a burned villa's garden
state: Louisiana
region: la
date: 2026-11-22
places: 18
file: data_la_hwwt.py

## What this batch is
A first statewide scatter in Louisiana (claimed as the thinnest state, 34 places), away from the two earlier batches (New Orleans, Cane River). Eighteen places: in Shreveport the Water Works Museum (McNeil Street steam pumping station), the Strand Theatre and the Central Railroad Station; the Germantown Colony near Minden; the Biedenharn house in Monroe; Frogmore Plantation and its steam cotton gin near Ferriday; Kent House in Alexandria; the Forts Randolph and Buhlow earthworks in Pineville; the Port Hudson siege earthworks; Afton Villa Gardens (ruins garden of a mansion burned in 1963) and Grace Church in St. Francisville; Magnolia Mound and the Pentagon Barracks in Baton Rouge; Laurel Valley sugar plantation near Thibodaux; Shadows-on-the-Teche in New Iberia; St. Martin de Tours church and Maison Olivier in St. Martinville; the Calcasieu Parish Courthouse in Lake Charles. Sources: Wikipedia through wiki_raw.py, and the own pages of the water works museum, the Strand, Biedenharn, Frogmore, Kent House, Afton Villa Gardens, Grace Church, BREC (Magnolia Mound), Laurel Valley, the Shadows and the City of St. Martinville, read with page.py; FortWiki for the state of the Fort Randolph earthworks (a 2020 visit). NOT checked: anything on the ground; hours of the four state historic sites (Port Hudson, Forts Randolph and Buhlow, Longfellow-Evangeline, and the Germantown museum, whose state page answers 404), because lastateparks.com answers 403; Magnolia Mound's regular hours (BREC's page gives prices but no hours); St. Martin de Tours Mass times (parish site 403; the city says daily Masses). Pins moved on the aerial: Frogmore (off a house with a pool onto the row of small red-roofed buildings, likely the cabins), Laurel Valley (off the highway onto the village of cabins). Area-only pins: Port Hudson (state site point in woods) and Afton Villa Gardens (gardens in general). Grace Church and Kent House are under trees on the aerial. Brick: Shadows 'yes' (Wikipedia: handmade red brick), Laurel Valley 'some' (a 1979 HAER photograph of the ruined brick mill), log/earth/bousillage places 'no', the rest '?'.

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Winter Quarters State Historic Site | Lake St. Joseph, south of Newellton, LA (32.01288, -91.1761) | 1805 hunting lodge grown into the one plantation house on Lake St. Joseph the Union army spared; damaged by a tornado in April 2011 and closed indefinitely as of February 2022 (Wikipedia) | Whether it has reopened or can be seen from a public road |
| Chretien Point Plantation | Two miles SW of Sunset, LA (30.38833, -92.10222) | Red-brick mansion of 1831 to 1835; Civil War battle on the grounds (Wikipedia) | Current owner and whether visitors are let in |
| Mansfield State Historic Site | DeSoto Parish, LA (32.01091, -93.66498) | Battlefield of April 8, 1864; park set up by the UDC in 1924 (Wikipedia) | What stands there to see; hours (Louisiana State Parks page 403) |
| Laurel Valley sugar mill ruin | On the Laurel Valley grounds, Thibodaux, LA | 1979 HAER photograph of roofless brick mill walls (Wikimedia Commons) | A source on its state now and an exact position, for an entry of its own |
| Old Castillo Hotel | St. Martinville, LA (30.121389, -91.8275) | Register-listed (Wikipedia list) | No article read; owner and use |

## Tips
- lastateparks.com (every state historic site page and press release) still answers HTTP 403 to page.py, and search results give titles only; the Germantown Colony Museum page on sos.la.gov answers 404.
- page.py --all on Squarespace and GoDaddy sites (shadowsontheteche.org, kenthouse.org) prints only the menu; the hours were in the cached page in research/pages/ and came out by stripping the tags.
- The ArcGIS geocoder found named places (Afton Villa Gardens, Germantown Colony Museum, Frogmore) that nom.py could not; Afton Villa gave two points 1.4 km apart.
- photo_find.py turned up a 1979 HAER picture of a ruined brick sugar mill at Laurel Valley that no article mentions: worth running look early, as a lead finder.
