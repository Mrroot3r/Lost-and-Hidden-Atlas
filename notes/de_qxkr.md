# de_qxkr: Delaware: churches, stations and old houses, Kent, Sussex and New Castle
state: Delaware
region: de
date: 2026-11-28
places: 12
file: data_de_qxkr.py

## What this batch is
Twelve Register-listed standing places spread over all three counties (Kent 9, Sussex 1, New Castle 2): five chapels and churches, two Delaware Railroad stations, a college's first building, two 1700s brick houses and a gambrel-roofed mill. Facts come from the Park Service Register records and forms (form.py), Wikipedia raw text, and the Delaware Public Archives marker and houses-of-worship pages for Thomas Chapel and Old Drawyers. Not checked: owners, parking, hours (none found on the pages of whoever runs these places), interiors, and whether the Park Service form for Todd's Chapel and Bethel Church could be read (the scans are poor). Brick colour was not stated by any source, so brick is '?' except where a source says wood. Five pins (Thomas Chapel, Todd's Chapel, Loockerman Hall, Felton and Wyoming stations) could not be matched to a building with certainty on the aerial and are marked area. The Android smoke test (tools/app_smoke.js) failed waiting for the field-log button; this batch changes only data. Felton's picture was chosen from the caption without opening the sheet.

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Golden Mine | Milford, DE (38.90528, -75.48556) | c. 1763 frame house in cypress shingles with brick addition (Wikipedia) | owner, access |
| Mordington | Frederica, DE (38.96861, -75.49417) | c. 1785 Georgian brick house; doorways and woodwork moved to Winterthur (Wikipedia) | owner, access |
| Smyrna Opera House | Smyrna, DE (39.29988, -75.60635) | Register listing 80000930 is the Smyrna district | no article read |
| Bethel Methodist Protestant Church | Andrewsville, DE (38.86378, -75.63646) | Gothic, 1871 and 1905 (Park Service record) | form scan unreadable |
| Mispillion Lighthouse and Beacon | Milford, DE | tower rebuilt as a replica elsewhere, steel tower demolished 2008 (Wikipedia) | nothing left at site |
| Blackwater Presbyterian, Portsville Lighthouse, Georgetown gas plant, Cherbourg Round Barn | Sussex and Kent | all demolished per Wikipedia | not added: nothing to see |

## Tips
- form.py gave the Cherbourg Round Barn the Kent County Courthouse form and the Smyrna listing a 388,000-character district form: check the first lines before relying on one.
- The gaps list for Delaware is full of demolished listings; Wikipedia's first paragraph says so quickly.
- The Atlas had 63 Delaware places at the start; this is the fourth Delaware pass.
