# in_uafv: Indiana: a second scatter, Calumet to the Ohio
state: Indiana
region: in
date: 2026-11-22
places: 17
file: data_in_uafv.py

## What this batch is
Indiana's second scatter, 17 places, taking the state from 21 to 38, spread over the Calumet (City Methodist Church and Union Station in Gary, the Sheriff's House and Jail in Crown Point), the north (Copshaholm in South Bend, the Limberlost cabin in Geneva), the Wabash country (the Monon High Bridge and the watered Wabash and Erie Canal at Delphi, the Seiberling Mansion in Kokomo, the Debs House in Terre Haute, Bridgeton Mill), the hills (Wylie House in Bloomington, the T. C. Steele house and studio, the Medora Covered Bridge) and the south-west and Ohio (the Ferdinand monastery chapel, Community House No. 2 at New Harmony, the Fort Knox II site at Vincennes, the Culbertson Mansion in New Albany). Mostly standing places people can go into, with two ruins (the Gary church and station) and one marked site. Facts from Wikipedia (`wiki_raw.py`) and the managing bodies' own pages read with `page.py` (Indiana State Museum plan-your-visit pages for Limberlost, T. C. Steele, New Harmony, Vincennes/Fort Knox II and Culbertson; oldsheriffshouse.org; howardcountymuseum.org; debsfoundation.org; libraries.indiana.edu; thedome.org; wabashanderiecanal.org; coveredbridges.com; Indiana Landmarks), HMdb markers, and news (Chicago Sun-Times and FOX 32 on City Methodist, Inside INdiana Business on Bridgeton, Islands.com on Medora). Not checked: anything on the ground; whether City Methodist Church's demolition (contract awarded September 2026) has begun, so it is conf mixed; Copshaholm's hours (the History Museum's page answered 403); Bridgeton Mill's daily times; who owns the Medora bridge and its parking (only a travel article says walkers may cross); Gary Union Station's owner; most parking; how much of the Monon High Bridge is decked today. Red brick was left '?' wherever no source gave the colour; 'no' for the concrete Gary station, the wooden Medora bridge and the log-post Fort Knox II outline. Pins: the Monon High Bridge pin moved off OpenStreetMap's mislabelled truss over State Road 25 onto the rail bridge over Deer Creek; Ferdinand moved onto the chapel and Fort Knox II onto the post outline with `pix.py`; New Harmony set on OpenStreetMap's Community House 2. No pin is only a trailhead.

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Tunnelton's Big Tunnel (B&O, 1857) | Tunnelton, Lawrence County, IN (38.773, -86.341 is the town) | Wikipedia (Tunnelton, Indiana): a 1,731-foot tunnel finished April 15, 1857, the town's namesake | Whether the line is still active (it appears to be CSX), a safe public viewpoint and an owner's word on access |
| Conner House, Conner Prairie | Fishers, IN (39.98453, -86.02886) | Wikipedia: William Conner's house, restored by Eli Lilly, at the centre of the Conner Prairie museum | Conner Prairie's own page for when the house itself is shown (seasonal) |
| Rapp-Owen Granary | New Harmony, IN (38.13020, -87.93592, OpenStreetMap) | Commons: Rapp Granary completed 1818, restored 1997-1999; OpenStreetMap: an event venue | A source for its history and whether visitors may go in |

## Tips
- indianamuseum.org slugs that work: tc-steele-historic-site (and tc-steele), limberlost-state-historic-site, new-harmony-historic-site, culbertson-mansion-historic-site, vincennes-state-historic-site (its page also gives Fort Knox II's free outdoor hours). Read the hours with `page.py --all` and grep "Plan your visit to": the -g lines cut off at "a.m."
- OpenStreetMap's bridge named "Monon High Bridge" near Delphi is the trail's truss over State Road 25; the real High Bridge over Deer Creek is the abandoned railway "High Bridge" about 1.3 km east (`osmnear.py ... -g Monon|bridge`).
- oldsheriffshouse.org's home pages (homespring2.html) answer 404; historic-house-and-jail-tours.html has the tour days.
- historymuseumsb.org (South Bend) answers 403 to `page.py`.
