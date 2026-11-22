# conf_ngwx: Vischer Ferry and the edges of Cohoes and Waterford
state: New York
region: conf, sar
date: 2026-11-22
places: 7
file: data_conf_ngwx.py

## What this batch is
Seven places at the edges of region `conf`, drawn at random by `choose.py --state ny`. Cohoes, Waterford, Watervliet and Green Island had been worked by seven earlier batches, so the Register lists for Albany and Saratoga counties and HMdb's nearby lists left only a few standing places there: the Northside Historic District in Waterford (an area pin, moved off the Wikipedia point, which falls on open ground by a mill) and two 1890s Queen Anne houses side by side on Imperial Avenue, Cohoes (Dickey and Lackman). The rest is Vischer Ferry in Clifton Park, which `start.py` listed as an old town centre with no Atlas place, filed under `sar` as earlier conf batches filed Halfmoon: the hamlet and historic district (pin at the district marker), the Amity Reformed Church (1888) and its burying ground, Ferry Drive with the Vischer homestead, the grist mill foundation and the 1900–1902 bridge abutments (pin is the parking area; the mill foundation and abutments come from the town marker only and were not seen on the aerial or LiDAR), the 1815 Abraham Best House and School No. 5 on Moe Road (draft Register nomination on parks.ny.gov). Sources were read with `wiki_raw.py` and `page.py`: Wikipedia, HMdb marker pages, the Town of Clifton Park's marker page, the School No. 5 nomination. Not checked: anything on the ground; service times at the Amity church (no congregation page found; `hours='?'`); who owns the Ferry Drive lot and the woods with the mill foundation (marked view); red brick for six of the seven (the sources say brick but not its colour). All pins were looked at on the leaf-off aerial and LiDAR.

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| St. Brigid's Church (update to the conf_aunk row) | Watervliet, NY, 695 Fifth Avenue | The Evangelist, April 2018: last Mass June 25, 2018; church and older school sold to Wicked Smart LLC, a sportswear maker; hall to the Association of Bosniaks of Albany. HMdb 253752: the first St. Brigid's was dedicated July 11, 1851 at Salem (4th Avenue) and Mansion (7th Street), so the Fifth Avenue church may be a later building | Which building stands on Fifth Avenue, its date, and whether the 1851 church survives |
| Immaculate Heart of Mary (former Immaculate Conception Church) | Watervliet, NY, 25th Street and 7th Avenue | The Evangelist 2018: the merged parish's one worship site; diocese page gives a Saturday 4 p.m. vigil Mass | The building's date and history from a source |
| Champlain Canal Lock C-1 | Halfmoon, NY (OpenStreetMap lock gate 42.82356, -73.66419) | Lakes to Locks Passage page: picnic area, boat launch, gate locked outside lock-season hours | A source for its date and anything that makes it worth a pin beyond the Waterford flight |
| Isaac Eddy House | Waterford, NY (HMdb 145305, Middle and Third Streets) | HMdb: built 1826 by the owner of the Franklin Ink Works, a "Waterford gable" house | A second source; could be added to the Waterford village entry rather than its own pin |

## Tips
- In this region the Register lists and HMdb's nearby lists are nearly exhausted for Cohoes, Waterford, Watervliet and Green Island; the next `conf` draw should go straight to the Clifton Park and Halfmoon edges or to church histories (parish pages, The Evangelist's 2018 archive on evangelist.org reads well with `page.py`).
- HMdb's nearby list page (`nearbylist.asp`) gives marker numbers and titles in one request; `grep -o "m.asp?m=[0-9]*'>[^<]*"` on the cached page lists them all.
- troyirish.org answers 403 to `page.py` with no archived copy.
