# Pictures batch arkp (2026-11-23, scheduled run)

What this batch is: pictures only, for places already on the map with none. No new places, no pins, no text. Chosen by looking at Wikimedia Commons sheets; the tool took each address, credit and licence from Commons.

Counts:
- 10 places got a picture (you can see them in tools/pics_arkp.py): hale-halawai-holualoa, new-manchester-mill, spirit-house-georgetown, pershing-county-courthouse-nv, stillwater-blockhouse, fort-allen-well-weissport, fort-totten-dc, st-marys-church-indian-river, octagon-earthworks-newark, st-elizabeth-hospital-baker.
- 10 places were looked at and said none: samuel-gibson-house, foster-town-house, david-brown-house-site-concord, jungle-habitat, beaver-kill, little-falls-guard-lock, fort-point-trinity, orford-ridge-houses, tunnicliff-inn-cooperstown, roxbury-depot.
- 7 places were recorded as none by the tool itself (Commons had nothing): christ-anglican-abernethy, lidar-gibson-taylor-road-north-house-site, chenango-canal-fly-creek-arch, ninette-sanatorium, round-pond-ice-house-sag-harbor-spur, lidar-gordon-road-pit, triangle-no-1-petrolia.

Places to look at again:
- roxbury-depot: candidate 1 is the depot itself (named, 67 m from the pin), but its thumbnail did not render on the sheet, so it was not seen and was left none. A person should look at it.
- beaver-kill: the one candidate shows Lincoln Park's lawn and skyline, not the ravine; left none.
- foster-town-house: the best candidate's own description says it is not the town house but the town building next door; left none.
- st-elizabeth-hospital-baker: chosen on its name and address (2365 4th Street); the Towers candidates are the same building by name.
- octagon-earthworks-newark: chosen candidate 1 is a grassy embankment on the golf course at the pin; a closer mound photograph (candidate 4) is also available.
- fort-totten-dc: chosen an 1863 survey view named "View in Fort Totten"; it shows the old landscape, not a standing structure.
- stillwater-blockhouse: the blockhouse replica is named and 606 m away; it is the building itself.

Rounds: four `next 5` runs plus one `look` for two places whose sheets were missing. Commons answered slowly with no login set; the tool waited as it does.
