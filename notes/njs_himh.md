# njs_himh: Salem County, New Jersey: patterned brick, Fort Mott and Finns Point, Quaker Salem
state: New Jersey
region: njs
date: 2026-11-18
places: 14
file: data_njs_himh.py

## What this batch is
Fourteen places in Salem County, the first close pass in South Jersey (region `njs`, drawn with `choose.py`): the Fort Mott gun batteries, the Finn's Point Rear Range Light, the Hancock House and its Swedish cabin, the Alloways Creek Friends Meetinghouse, the Old Salem County Courthouse, the Salem Friends Meeting House, the Friends Burial Ground with what is left of the Salem Oak, the Dickinson House, the Seven Stars Tavern, the old Pittsgrove Presbyterian Church at Daretown, the empty Salem County Insane Asylum, the Lambert Street School in Alloway, and the markers for Fort Nya Elfsborg and Quinton's Bridge. Sources: Wikipedia's Salem County Register list and articles (`wiki_raw.py`), HMdb marker texts (three nearby lists, then each marker read with `page.py --all`), Register nomination forms with text layers (Pittsgrove 77000904, Alloways Creek 03001306, Dickinson 75001156, Seven Stars 76001184), the VA's Finn's Point page, the Fish and Wildlife Service's Supawna Meadows pages, and Preservation New Jersey for the asylum. The state park pages for Fort Mott and the Hancock House give `page.py` 7 characters, so their hours come from Journey Through Jersey, and each access note says so. Not checked: anything on the ground; meeting times and whether the public can go into the two Quaker meetinghouses, the courthouse and the Pittsgrove church; parking at the range light and at Daretown; the asylum's present condition (newest source 2012); the Salem Oak stump rests on one 2022 blog. Red brick was settled from the Hancock House marker text and from Wikipedia pictures opened with `brick.py look` (Seven Stars, courthouse, Alloways Creek, Pittsgrove, asylum: red brick; Fort Mott: concrete and earth); the Dickinson House picture is a 1936 black-and-white HABS photograph and is left `?`.

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Finn's Point National Cemetery | Fort Mott Road, Pennsville Township, NJ (39.6111, -75.5556; lot 39.61047, -75.55547) | Written and sourced in this session (Wikipedia, VA page: open daily from 8 a.m.; HMdb 312861, 21656): the common grave of 2,436 Confederate prisoners from Fort Delaware under an 85-foot obelisk, and 135 Union guards | Taken out before publishing because `check.py` puts every point of the cemetery in Delaware: the Delaware outline in `source/build/states.json` overlaps the New Jersey shore at Finns Point, and `state_of()` returns the first state that contains a point. Needs the outline or `state_of()` fixed (prefer the region's state when a point is in two outlines), then the entry can go in as written |
| Wistarburgh Glass Works site | Commissioners Pike (CR 581) at Glass House Lane, Alloway Township, NJ (39.5694, -75.3397) | HMdb 298794: Caspar Wistar began making glass here in 1739; the start of South Jersey's glass industry. HMdb reports the 1935 marker missing | Anything to see now, and who owns the ground |
| Fenwick's Grove | Salem-Woodstown Road, Mannington Township, NJ (39.62695, -75.37131, by the County Farm) | HMdb 304140: a 1924 memorial where John Fenwick, founder of Salem, is said to lie buried | Who owns the grove and whether visitors may walk in |
| Mt. Pisgah AME Church | South Yorke Street, Salem, NJ (39.56314, -75.46060) | HMdb 127817: congregation founded by Reuben Cuff in 1800, present building 1878; the marker's text about a national designation is garbled | A clear source for the building and its standing |
| Spike Cutting Machine (mapped ruin) | 39.43014, -75.23618 (Cumberland County, NJ, outside Salem County) | Only an OpenStreetMap ruin name in the leads layer | Any written source |

## Tips
- `check.py` refuses a pin at Finn's Point National Cemetery (and anywhere west of about -75.555 on that shore) as Delaware: the state outlines overlap there and `state_of()` takes the first match. Fort Mott's batteries pass only because they lie in both outlines with New Jersey first. A fix belongs in the outline or in `state_of()`.
- Journey Through Jersey (`journeythroughjersey.com/sites/<name>`) reads well with `page.py` and gives hours for New Jersey state parks and historic sites, whose own `nj.gov/dep` pages give 7 characters.
- `fws.gov/refuge/<name>/visit-us` answered 404; the refuge's main page (`fws.gov/refuge/supawna-meadows`) has the hours and rules.
- OpenStreetMap's "Fort Mott State Park lot" from `parking.py` (39.60548, -75.55092) is a path across a field on the leaf-off aerial; the real lot is beside the Welcome marker (HMdb 21660).
- Web search returned titles and links only, no quoted text, as in Morris County.
