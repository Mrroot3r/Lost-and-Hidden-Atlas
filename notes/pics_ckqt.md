# Pictures batch ckqt (2026-11-22, scheduled run)
tidied: 2026-11-26

What this batch is: a pictures job (PROMPTS.md job 8). No new places, no pins, no text. It chose photographs for 30 places already on the map that had none, by looking at the candidate sheets from tools/photo_find.py. Only source/tools/pics_ckqt.py and this note are new.

Result: 12 places got a picture, 18 got none. Every address, credit and licence came from Wikimedia Commons through the tool.

Places that got a picture: Église de Saint-Jean (Saint-Jean-de-l'Île-d'Orléans, QC), Souris Town Hall (PE), Cross Mountain Miners' Circle (Briceville, TN), Eureka Main Street (Eureka, UT), Tanner Store (Wartburg, TN), Old Capitol (Corydon, IN), St. Thomas' Church (St. John's, NL), Kip-Beekman-Heermance ruin (Rhinecliff, NY), Charlottetown City Hall (PE), Russell, Majors & Waddell House (Nebraska City, NE), Torreon (Lincoln, NM), Culvert Road (Medina, NY).

Hesitations, one line each:
- Cross Mountain Miners' Circle: two named candidates show the same obelisk ring; the wider view looking west was chosen over the closer one 206 m away.
- Eureka Main Street: an area pin; the lower-section street view by name was chosen. Eureka Springs, Arkansas candidates were left out as a namesake.
- Église de Saint-Jean: several candidates by name show the same church; the stone front with the belfry (by name, 5 m from the pin) was chosen over the wider view from the shore, which is also the same church.
- Souris Town Hall: the only candidate at the pin, 6 m away, shows the stone building with its sign; kept.
- Tanner Store: the storefront with the TANNERS sign was chosen; the other candidate was a tunnel photo.
- Old Capitol (Corydon): the chosen view has a historical marker in front and trees partly in the way, but the building is plainly the limestone capitol.
- St. Thomas' Church: two candidates from 50 m and 69 m show the same church; the front view was chosen.
- Kip-Beekman-Heermance ruin: the wall-fragment view was chosen over the cellar hole and the marker, as the one that shows the standing ruin from outside.
- Charlottetown City Hall: many by-name candidates show the same red brick building; the first, a wide view from the street, was chosen.
- Russell, Majors & Waddell House: the candidate 23 m from the pin, captioned as the Old Freighters Museum and the Majors residence, was chosen; a by-name candidate at 407 N. 14th Street looks like the same building.
- Torreon: the wide village view at about 0 m from the pin was chosen; a by-name historic NARA photograph shows a different wall surface from the current tower, so it was left out.
- Culvert Road: the south-entrance view was chosen over the north entrance and the plaque; the photos are 2025 views, which is the current state.

Places that got none, and why (one line each):
- Blue Job fire tower, Lidar CCC Road pits, Lidar Beaver Dam Road house site, Lime Rock kilns, Old House (Lansingburgh), Bloomington (Clinton Lake), Little Sands church, Aspinwall Hotel site, Fish House (Northampton), Hoosac Tunnel: nothing on Commons within the search radius, or only a train, a 1917 photograph of troops and similar matter; no picture shows the place.
- Salem Tavern smokehouse: candidates showed the Tavern itself and its shed alley, not the smokehouse foundation.
- Irondale Schoolhouse: candidates were night views of Main Street, Millerton; no picture shows the schoolhouse.
- Orleans County Grammar School: only ground-foundation photographs of a different school in Brownington, Vermont.
- Governor Furnas House: only architect's drawings and plans; no photograph.
- Split Rock Furnace: two named photographs show what look like two different stone structures; neither chosen.
- Hale Hālāwai O Hōlualoa: candidates were sea turtles, fish and butterflies; none showed the church.
- Knaut-Rhuland House: candidates were neighbouring Lunenburg houses and a church, not this house.
- Nassau village (Church Street district): an area pin; candidates were single houses and the library, with no street view of Church Street or the Academy.

Not checked or not done: nothing was skipped. The first Commons check gave 429; after a minute it answered 200 and every look ran. No look failed with a network error after that.
Build: tools/all.sh ran clean on the workspace (syntax ok, no errors). publish.sh took in other batches that merged meanwhile by itself and said so; no resync was needed.
App smoke test was not run: this batch changes no app code.
