# Pictures batch pics_vkzk (2026-11-21)

## What this batch is

A pictures job (PROMPTS.md job 8): photographs for 30 places already on the map that had none, chosen by looking at Wikimedia Commons candidates with `tools/photo_find.py`. No new places, no pins, no text. The file is `tools/pics_vkzk.py`.

Result: 8 places got a picture, 22 got none.

Pictures chosen: Ohio Canal groundbreaking site (Heath), Old Centre (Centre College, Danville), Seacow Head Lighthouse (Fernwood), St. Ann's Church (Woonsocket), Avery Depot (Avery, Idaho), Butternut Creek Aqueduct (DeWitt), Palace Station (Crown King), Sherman Free Library (Port Henry).

The rate of "none" is higher than the one-third to one-half the job expected, because most of the 30 had no candidate near the pin or only by-name candidates in the wrong town.

## Where I hesitated

- Ohio Canal groundbreaking site: the photo is a roadside stone wall with the marker at 199 m from the pin, with a house behind it. It is the site's own marker, so I took it, but it is a marginal view.
- Palace Station: the cabin and its sign are seen from 96 m, partly hidden by trees. It is the building, and the file is named for it, so I took it.
- Old Centre: several near-identical views. I took the wider one from 79 m.
- Seacow Head: the 2015 view from 95 m is the clearest whole-tower view.
- Butternut Creek Aqueduct: the chosen view shows the arches from the bridge, with a small figure far off that is not the subject.
- Sherman Free Library: one named candidate and one unnamed candidate of what looks like the same building. I took the named one.
- Star Fort (Ninety Six): the only candidate near the pin is a grassy earthwork with no star outline, so I left it as none.
- Old North Bridge (Concord): the candidates were 1930s postcards by name and statue close-ups, so none.
- Saint-Narcisse (Quebec): the candidates show an annex of the old plant, not the powerhouse, so none.
- Enfield Falls Canal: only historic postcards and modern views away from the pin, so none.
- Fort Totten: the candidates were interpretive signs, a plaque and a Metro station, so none.
- Brandywine Battlefield Park: the candidates were the entrance marker and a separate church inside the park, so none.
- Old Parish Church, Sheffield (Massachusetts): every by-name candidate is a Sheffield in England, so none.
- Vedder Cemetery (Rotterdam): a plaque close-up and stones against a wall, so none.

## Operations

- Wikimedia Commons answered 429 at the start, then 200 after about four minutes; the job went ahead.
- Several `look` runs took longer than the shell's two-minute limit. Those ran in the background, with the output written to `research/`.
- publish.sh stopped once because main had moved. resync.sh was run as it said, the site was rebuilt, and publish was run again.

## Tips for the next pictures session

- Run each `look` with a generous timeout, or in the background. Each look fetches its candidates one at a time.
- Places whose only candidates are "by name" for a namesake town (Sheffield, Woonsocket, Fort Totten) are usually none. Check the town line first.
- For lighthouses and churches, the wide view from the road is almost always the best candidate.
