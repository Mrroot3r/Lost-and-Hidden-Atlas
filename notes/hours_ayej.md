# hours_ayej: hours for the last 9 waiting churches and 9 New York museums and libraries
state: New York
region: ny
date: 2026-11-21
places: 0
file: hours_ayej.py

## What this batch is
An "hours" session (PROMPTS.md type 7): no new places and no pins. `tools/hours.py` showed only nine places of worship waiting anywhere (seven in New York, Sharon Temple in Ontario, Midway Church in Georgia); all nine were looked up, then New York museums and libraries from `hours.py list "New York"`. Every page was read in the session with `hours.py page` or `page.py`, and its street address or town checked against the place.

Eighteen places are in `hours_ayej.py`: nine with hours (Midway Church among them, without "opens to visitors"), nine recorded `?` (the eight below and Christ Church, Wellsburg).
- Hours: Sharon Temple (museum closed for the season; office hours), St. Stephen's New Hartford (Sunday 10 am, its own site, 25 Oxford Road), Old Fort Niagara, Grant Cottage (closed for the season, reopening May 2027), Staatsburgh, Hallockville Museum Farm (page address 6038 Sound Avenue, Riverhead), Skene Memorial Library, Old Stone House Library, Fort Ann.
- Midway Congregational Church, Georgia: the Midway Museum's page about the church gives the museum's tour hours (Tue-Sat 10-4) but does not say the church itself is opened, so it is recorded without "opens to visitors".
- Old Stone House Library: the Fort Ann Historical Society's research page gives Tue 4-5:30, Wed 8:30-10:30, Thu 1-3; a Lakes to Locks Passage page gives Tue-Thu 3-5. Both are in the row.
- Recorded `?`: Calvary Church / Cathedral of the Theotokos, Utica (the archdiocese's site gives no service times and links to no cathedral page); Tabernacle Baptist and First Presbyterian, Utica (no page of their own found); Mount Saviour Monastery (msaviour.org answers 403, its archived copy could not be fetched unattended); Trinity Church, Elmira (now a sports business; no page of its own found); Chemung Valley History Museum (403); Hill-Hold (403; archived copy not fetched); Second House, Montauk (the historical society's site answers 403).

**Closed churches:** Christ Episcopal Church, Wellsburg held its last service and closed in 2011, according to a Star-Gazette story reprinted on the Anglicans Ablaze blog (anglicansablaze.blogspot.com/2011/08/town-and-country-wellsburg-church.html). Recorded `?`; its place text should say it is closed. Trinity Church, Elmira is already described as a sports complex.

**Five landmark pins left out:** `check.py` refuses an hours file entry for a landmark pin (`lm-…`): its hours section asks `i in ids`, while the pics section accepts `lm-` ids through `photo_find.id_ok`, and `hours.py list` offers `lm-` pins. These were read and are ready to add once `check.py` accepts them (a maintainer change, not made here):
```
 'lm-cherry-hill':('Page gives Tue-Sat 12-4 (expanded hours) and Fri & Sat 12-4; last tour 3', '2026-11-21', 'https://www.historiccherryhill.org/', True),
 'lm-great-camp-sagamore':('Guided history tour daily 10 am & 1:30 pm, Jun 14-Oct 16 (2026 season); register ahead', '2026-11-21', 'https://greatcampsagamore.org/tours-hikes-paddles', True),
 'lm-schuyler-mansion':('May 13-Oct 31 (2026): Wed-Sun 10:30-5, guided tours hourly 11-4 (reserve); one tour day Sat Nov 28', '2026-11-21', 'https://parks.ny.gov/historic-sites/schuylermansion/details.aspx', True),
 'lm-ten-broeck-mansion':('Mansion tours Thu & Fri 10, 11, 12, 1; Sat 1, 2, 3; Sun (Jun-Aug) 1, 2, 3; advance tickets recommended', '2026-11-21', 'https://tenbroeckmansion.org/hours-admission/', True),
 'lm-watervliet-shaker-historic-district':('Tue-Sat 10-4 (April to early Oct); Tue-Sun 10-4 (mid Oct-Dec 18); docent tours 11 am & 1 pm Apr-Sep', '2026-11-21', 'https://home.shakerheritage.org/visit/', True),
```

Not checked: nothing was seen on the ground and no telephone call was made.

## Pages that would not open, or gave no times
| Place | Page tried | What happened |
|---|---|---|
| Mount Saviour Monastery | msaviour.org | 403; Internet Archive copy of 2026-10-17 needs the web fetch tool, whose approval went unanswered |
| Chemung Valley History Museum | chemungvalleymuseum.org | 403 |
| Hill-Hold | hillholdandbrickhouse.org | 403; archive copy of 2026-04-09 not fetched |
| Second House, Montauk | montaukhistoricalsociety.org | 403. The Montauk Sun's page gives Memorial Day weekend-June weekends, July-Labor Day daily 10-4: a newspaper, not used |
| Calvary / Theotokos Cathedral, Utica | igoarchusa.orthodoxws.com | The archdiocese's pages give no service times |
| Glove Theatre, Proctors, Spencertown Academy, Fountain Arts Center, Fireman's Hall Alfred, Albany Pump Station | own sites / searches | Event venues with no standing hours on the pages read, or no page of their own; not recorded, left waiting |

## Tips for the next session
- No church waits anywhere now (once this merges); the next hours sessions are museums and house museums.
- `hours.py list` offers landmark pins (`lm-…`) that `check.py` then refuses in an hours file; skip them until that is fixed.
- New York State Parks pages (parks.ny.gov/historic-sites/<name>/details.aspx) read well and give seasons and tour times.
