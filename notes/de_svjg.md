# de_svjg: Delaware: Kent, Sussex and old Wilmington
state: Delaware
region: de
date: 2026-11-20
places: 18
file: data_de_svjg.py

## What this batch is
Second pass over Delaware, taken with `choose.py --thinnest` (16 places, all in New Castle County but Fort Miles). 18 places spread over the state: Old Swedes Church and Fort Christina in Wilmington; the New Castle Court House; in Kent County the Old State House, the John Dickinson Plantation, Barratt's Chapel, the Allee House on Bombay Hook refuge and the Octagonal Schoolhouse; in Sussex County Abbott's Mill, Old Christ Church near Laurel, Prince George's Chapel, the Woodland Ferry, the Fenwick Island Lighthouse, the Indian River Life-Saving Station, Lightship Overfalls, the Delaware Breakwater East End Light, the Old Sussex County Courthouse and the Zwaanendael Museum. Almost all standing; the state has few ruins with a public way in. Sources: the Kent and Sussex Register lists with `wiki_raw.py --rows`, Wikipedia through `wiki_raw.py`, and each managing body's own page through `page.py` (history.delaware.gov for the state museums, destateparks.com, deldot.gov, nps.gov, oldswedes.org, barrattschapel.org, overfalls.org, fenwickislandlighthouse.org, delawarenaturesociety.org, delawarebaylights.org, friendsofbombayhook.org, dagsboro.delaware.gov). Red brick from article photographs opened with `brick.py look` (Old State House, New Castle Court House, Allee House, Zwaanendael: yes; Fenwick: painted white, no); Dickinson and Barratt's left `?` (Wikimedia 429; Barratt's only photo is black and white). Not checked: anything on the ground; Old Christ Church's owner and opening times (no page of its own found) and which building on the aerial is the church (pin moved onto the likeliest); the Octagonal Schoolhouse could not be picked out on the aerial (site pin); Bombay Hook refuge hours (fws.gov visit page 404); Old Sussex County Courthouse hours (the state says call); Prince George's Chapel hours come from an undated state notice; Cape Henlopen State Park fees. Pins that mark a general area: Fort Christina (park), Woodland Ferry (the crossing). `pincheck.py` was run without `--lidar`: every pin is in a town or open ground.

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Fort Saulsbury batteries and the Big Stone Beach fire-control tower | Near Slaughter Beach, DE (Wikipedia 38.93417, -75.33056) | Wikipedia: 1917–1924 batteries of two 12-inch guns each, sold in 1948, privately owned with no public access; the batteries are well preserved; the Big Stone Beach tower remains | Whether anything can be seen from a public road |
| Fourteen Foot Bank Light | Delaware Bay off Bowers Beach, DE (39.0482, -75.1836) | Wikipedia: 1885–86, the first lighthouse built on a pneumatic caisson; 11 miles out, not visible from land | A boat tour that passes it; an entry would be acc='boat' |
| Chipman's Mill site | Laurel, DE (38.56167, -75.54) | Wikipedia: grist mill of 1884 burned by arson in 1986; the millrace survives; the pond is fished from a boat ramp | Who owns the race and whether it can be seen; could join the Old Christ Church entry |
| Belmont Hall | Smyrna, DE (39.294501, -75.595902) | State list of historic sites: Georgian house of 1773, owned by the state, open for tours by appointment and events | A source for the house's history and what survives inside |
| Mispillion Lighthouse (rebuilt) | Shipcarpenter Square, Lewes, DE | Wikipedia: the 1873 lighthouse burned and was rebuilt in Lewes in 2004 as part of a private house; the skeleton tower at the river was demolished in 2008 | Whether it can be seen from a public street; private house |

## Tips
- `page.py` on `history.delaware.gov/new-castle-court-house/` saves a PNG and prints nothing; the working address is `history.delaware.gov/history.delaware.gov/new-castle-court-house-museum` (the doubled host is real). The other state museum pages (`/old-state-house/`, `/john-dickinson-plantation/`, `/zwaanendael-museum/`) read cleanly.
- `history.delaware.gov/historic-sites/` lists every state-owned site run by others (Abbott's Mill, Belmont Hall, the Breakwater light, Fenwick light, Fort Christina, Old Sussex Courthouse, Prince George's Chapel and more) with an address, phone and a line on visiting: one page for a quick Delaware list.
- The fws.gov Bombay Hook visit page answers 404; the Friends of Bombay Hook site reads with `page.py`.
- `parking.py` gave a building (Taylor Street, Wilmington) and a track across a field (Abbotts Pond Road) as lots: check every one on the TRAILHEAD tile.
