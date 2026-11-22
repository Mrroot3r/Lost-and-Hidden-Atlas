# Pictures batch pics_dazn (2026-11-22)

## What this batch is

Pictures only, no new places and no pins. The tool picked places already on the map that had no picture, five at a time, and each sheet was looked at before a choice was recorded in tools/pics_dazn.py. Every picture address, credit and licence comes from Wikimedia Commons through the tool.

Counts:
- 38 places went through the tool in this session.
- 17 got a picture chosen by looking at the sheet.
- 13 were looked at and given none, because no candidate plausibly showed the place.
- 8 were recorded as none by the tool itself, because Commons had nothing near the pin, under its names or in a category of its own.

## Where I hesitated

- lyme-common-horse-sheds: the common and its church, not the horse sheds, which do not show. Chosen as the wide view of the common.
- cannington-manor: the All Saints church is found by name only partly (LOOK TWICE); the picture shows a white wooden church with a bell tower, while the place text calls it a log church.
- clarksville-hamlet: a house named Clark House, not the hamlet as a whole.
- blackstone-canal-uxbridge: taken 388 m away and names the canal; it shows a stone arch bridge over water with a weir.
- masonic-building-downieville: the caption of the chosen picture names the Masonic Building, but I could not confirm from the sheet that it is the 1864 building on this corner.
- norumbega-park: an old postcard of the park's streetcar terminal, public domain. The park's buildings and the ballroom do not show.
- terlingua-ghost-town: a theatre in the ghost town, 59 m from the pin, rather than a ruin.
- souris-historic-lighthouse: the Commons caption gives 14.1 m for the tower; the place text gives 18.5 m. It is the same lighthouse by name.
- Left as none, though a picture might have been wanted: kaena-point-railroad (only coast and highway shown), beaver-kill (park lawn, not the ravine), cataract-firehouse-cohoes (no picture of the 1848 firehouse among the candidates).

## Tips for the next session

- The first run of "next 5" went past the two-minute limit of the shell here. Run it with a longer timeout (up to ten minutes) and do not interrupt it.
- Sheets of five places take a few minutes to produce; the tool's own wait is the cause, not a fault.
