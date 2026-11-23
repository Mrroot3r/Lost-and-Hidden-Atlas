# paw_sgsm: Pittsburgh, from a video walk-through
state: Pennsylvania
region: paw
date: 2026-11-23
places: 19
file: data_paw_sgsm.py

## What this batch is
The first places in the city of Pittsburgh (region `paw`), worked from one video walk-through of the city's old buildings (record: `source/videos/20220920_3u7zwkVitHU.md`; the video was a tip only). 19 places, all standing or traces: downtown on Grant's Hill (Richardson's Allegheny County Courthouse and old jail, the Union Trust Building, the City-County Building, Union Station's Burnham rotunda), Oakland (Cathedral of Learning, Heinz Memorial Chapel, Soldiers and Sailors Memorial Hall, Carnegie Institute and Library, Phipps Conservatory), the North Side (Allegheny Post Office, now the Children's Museum; the Carnegie Free Library of Allegheny), the South Side (Duquesne and Monongahela inclines, the P&LE station at Station Square), Riverview Park (Allegheny Observatory), East Liberty (East Liberty Presbyterian; the empty Saints Peter and Paul, the "Dogma church"), Troy Hill (Saint Anthony's Chapel) and Lawrenceville (Allegheny Arsenal, its 1814 powder magazine in Arsenal Park). Facts are from Wikipedia read as raw text; hours from the managing bodies' own pages read with the hours tool (Phipps, Nationality Rooms, Heinz Chapel, Children's Museum, Duquesne Incline, Carnegie museums, East Liberty Presbyterian, the observatory's events page). Not checked: hours for Saint Anthony's Chapel (its site answered 403), Soldiers and Sailors (its own pages gave none), the Monongahela Incline and the old jail museum; whether the Grand Concourse restaurant in the P&LE station is still open; the condition of the arsenal magazine today and where in the park it stands (the pin marks the park); whether the public may walk under the Union Station rotunda; Friday hours of the Nationality Rooms. Red brick is "no" only where a source names granite or limestone; the rest are "?". Pins are ArcGIS PointAddress matches or OpenStreetMap points, all looked at on the state leaf-off aerial; the Phipps pin was moved onto the glasshouses. `check.py` warns that "Cathedral of Learning" reads as a church: it is a university building and `inst` stands.

## Leads
Places you read about and could not finish. One row each.

| Place | Where | What is known | What is missing |
|---|---|---|---|
| Benedum Center (Stanley Theatre) | Pittsburgh, PA, 237 Seventh Street | 1927–28 movie palace by Hoffman-Henon, reopened 1987 (Wikipedia) | Pin, hours of tours, picture; ran out of time |
| Heinz Hall (Loew's Penn Theatre) | Pittsburgh, PA, 600 Penn Avenue (40.4427, -80.0015) | 1927 Rapp & Rapp movie palace, reopened 1971 as the symphony's hall (Wikipedia) | Box office or tour hours; pin check |
| Omni William Penn Hotel | Pittsburgh, PA, 530 William Penn Place (40.4406, -79.9966) | Opened March 11, 1916; Historic Hotels of America (Wikipedia) | Pin check and write-up |
| Kaufmann's department store building | Pittsburgh, PA, Fifth Avenue and Smithfield Street | Macy's closed and sold it in 2015 for redevelopment as "Kaufmann's Grand on Fifth" (Wikipedia, Kaufmann's) | What the building is now; a source for the building itself |
| Sarah Heinz House | Pittsburgh, PA, Heinz and Ohio streets (40.45479, -79.99319) | Settlement house of 1914 built by H. J. Heinz (Wikipedia) | Current use and access |
| Western Pennsylvania School for Blind Children | Pittsburgh, PA, Oakland (40.44981, -79.95309) | Permanent building of 1894 (Wikipedia) | Which building is the old one; access |
| Old Allegheny County Jail Museum | Pittsburgh, PA, in the old jail, Ross Street | Part of the cell block is a museum (Wikipedia, Allegheny County Courthouse) | Hours from its own page |

## Tips
- Pittsburgh street addresses all came back as ArcGIS PointAddress matches on the right building; only the Phipps "One Schenley Park" match fell on a road circle.
- saintanthonyschapel.org answers 403 to the page tools; stanthonyschapel.org does not resolve.
- Phipps hours are on `phipps.conservatory.org/visit-and-explore/visit/hours-and-admission/` (the www and /visit addresses give 404 or no hours).
- The Pennsylvania leaf-off server took about ten minutes for 21 tiles without LiDAR.
