# Pictures batch zhws (2026-11-21, scheduled run)

What this batch is: a pictures job (PROMPTS.md job 8). No new places, no pins, no text. It chose photographs for 30 places already on the map that had none, by looking at the candidate sheets from tools/photo_find.py. Only tools/pics_zhws.py is new.

Result: 13 places got a picture, 17 got none. Every address, credit and licence came from Wikimedia Commons through the tool.

Places that got a picture: Hope Plantation (Windsor, NC), Tower Dupré (St. Bernard, LA), Matton Shipyard (Cohoes, NY), Mount Albion Cemetery (Albion, NY), Kiernan Plaza / Union Station (Albany, NY), LaHave Islands Marine Museum (NS), Église de Saint-Joachim (QC), Bedstead Truss Bridge (Schulenburg, TX), Willow Springs trail swale (KS), Wallace post office (ID), Texas and Pacific depot (Natchitoches, LA), Chapelles de procession (L'Ange-Gardien, QC), DeWitt County Courthouse (Cuero, TX).

Hesitations, one line each:
- Tower Dupré: the only candidate is a 1974 photograph of the tower standing in the water. The place was destroyed in 2005, so the old picture is the one that shows it; kept.
- Hope Plantation: the chosen picture is the 1803 mansion, the house the pin is about; the pin is an area pin, so the picture is of the main house rather than the whole plantation.
- Matton Shipyard: the chosen picture is one carpenter-shop view of the yard; other candidates were of the same yard, and this one was chosen as the clearest wide view.
- Kiernan Plaza / Union Station: a landmark pin (lm-); the picture is the front of the station on Broadway.
- Église de Saint-Joachim: two candidates carry the name (both by name only, both 6 to 10 m from the pin); the front view of the church was chosen.
- Bedstead Truss Bridge: the only candidate is by name only, taken at Schulenburg and named for the bridge; the truss type and the NRHP note match, but it was not taken at the pin.
- Willow Springs: the picture is the site's Willow Springs sign with the DAR granite marker, not the trail swale itself (the swale candidate showed only a field); kept because the marker is part of the place's title.
- Chapelles de procession: the chosen picture is one of the two procession chapels (Notre-Dame-de-Grâce), not Saint-Roch; kept because it stands 3 m from the pin.
- DeWitt County Courthouse: the same building as the by-name candidate; the closer one, 34 m from the pin, was chosen.
- Wallace post office: three candidates from 36 to 45 m show the same building; the one with the flag and the wider view was chosen.
- Texas and Pacific depot: the chosen picture is a historic grey-tone photograph of the front, public domain, taken from the pin; it is the only view with the arcade front.

Places that got none, and why (one line each):
- Ledbetter Picket House, Church Hill Historic District, Densmore Church, Hedge Lawn, St. Barnabas, Bell Island No. 2 Mine, Oneonta roundhouse, Caroga Museum, Batchellerville Presbyterian Church, Van Der Zee Manor House: nothing on Commons within the search radius.
- Slingerlands freight house: candidates were village houses and a church on the street; none showed the freight house.
- Brownington Congregational Church: a person at a lectern (by name only) and foundation works for a different schoolhouse; not this church.
- I.O.O.F. Hall, Idaho City: other Main Street buildings and a distant, obscured view with a name-only sign; not clear enough.
- Clinton's Ditch: a garden gnome is the subject of the walkway view, and the other candidates were a different lock and a tourism sign.
- Fort Frederick: the by-name candidate is a hand-coloured postcard of a shoreline, not the fort; the other is a marker sign.
- Brownville Historic District: by-name candidates were single buildings in Brownville, Nebraska, plus a Savannah district; none showed the district as a whole.
- Montpelier turntable: ten candidates were flower photographs taken near the pin.

Not checked or not done: nothing was skipped; no look failed with a network error or 429 after the first try (the first Commons check gave 429 with the default curl user agent and 200 with a named one).
Build: tools/all.sh ran clean on the workspace; publish.sh stopped once for a main move (resync.sh run), then rebuilt and published.
App smoke test (tools/app_smoke.js) was not run: it needs the Android www build and a local server, and this batch changes no app code.
