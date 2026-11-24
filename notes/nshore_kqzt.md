# nshore_kqzt: Salem and Marblehead, Massachusetts: first-period houses, McIntire, forts and the waterfront
state: Massachusetts
region: nshore
date: 2026-11-19
places: 23
file: data_nshore_kqzt.py

## What this batch is
Twenty-three places in Salem and Marblehead, where the Atlas had nothing within 9 km of Salem (region drawn at random by choose.py). Salem: the House of the Seven Gables, the Witch House, the Gardner-Pingree, John Ward, Peirce-Nichols and Ropes houses (Peabody Essex Museum), East India Marine Hall, the Custom House, Derby House, Narbonne House and Derby Wharf with its light (Salem Maritime NHP), Hamilton Hall, Charter Street Cemetery, Pioneer Village, Fort Pickering with Winter Island Light, Fort Lee and Bakers Island Light. Marblehead: Fort Sewall, the Jeremiah Lee Mansion, Abbot Hall, St. Michael's Church (1714), the Old Town House and Old Burial Hill. Facts from Wikipedia (wiki_raw.py) and the managing bodies' pages read with page.py: 7gables.org, thewitchhouse.org (drawn by script; one line of hours came back), pem.org, nps.gov/sama and nps.gov/places, pioneervillagesalem.org, essexheritage.org, marbleheadmuseum.org, marbleheadhistory.org, stmichaels1714.org; Destination Salem (salem.org) where the City's pages failed. Pins: ArcGIS PointAddress or OpenStreetMap points, all looked at on the 2023 aerial and LiDAR; Fort Lee moved about 60 m onto the star-shaped ramparts seen on the LiDAR. Red brick from sources or Wikipedia photographs opened in the session (Seven Gables, Gardner-Pingree, Custom House, Witch House, Abbot Hall, St. Michael's, Old Town House looked at); the rest left '?' unless a source names the material. Not checked: anything on the ground; the City of Salem's own hours and rules for Winter Island, Fort Lee and Charter Street Cemetery (salemma.gov answered 404 or reset); Marblehead's park rules for Fort Sewall (403); Bakers Island tour days; whether Derby House and Peirce-Nichols House open at all; the John Ward House pin (site precision). Fort Lee's date and shape differ between Wikipedia (1776, five points) and historyofmassachusetts.org (1742 platforms, four points); both are given.

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Salem Diner | Salem, MA (Register coordinate 42.50111, -70.89639) | Wikipedia: 1941 Sterling Streamliner, car #4106, one of two left in Massachusetts; closed May 31, 2019, with plans in October 2019 to move it and add a roof deck | Whether it still stands where it was, and in what use |
| Salem Willows park and carousel | Salem Neck, Salem, MA (42.535, -70.86944) | Wikipedia: willows planted 1801 for a smallpox hospital walk; public park from 1858; amusement park from 1880 by the Naumkeag Street Railway; a carousel survives at Kiddieland | The City's park page (salemma.gov would not open) and what of the old trolley-park buildings stands |
| Winter Island seaplane hangar | Winter Island, Salem, MA | Wikipedia: Coast Guard Air Station Salem 1935 to 1971; a photograph of the abandoned hangar in 2016 | Whether it still stands after the City's master plan; could be added to fort-pickering-salem's text |

## Tips
- salemma.gov (City of Salem) answered 404 or connection reset to page.py for every node address a search gave, with no archived copy; Destination Salem's pages (salem.org) read cleanly and carry hours for City-run sites.
- marbleheadma.gov answers 403 to page.py.
- The NPS park hours page for Salem Maritime (nps.gov/sama/planyourvisit/hours.htm) gives a table per building and season in plain text with page.py --all; the nps.gov/places pages for each building read in full.
- PEM's walking-tour page (pem.org/visit/tours/salem-walking-tours) is the only place found that says when the Gardner-Pingree and John Ward houses can be seen inside.
