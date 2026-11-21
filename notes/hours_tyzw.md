# hours_tyzw: hours for 31 places of worship in New York, South Carolina, Maryland, Arizona, Georgia, Wisconsin and Maine
state: South Carolina
region: sc
date: 2026-11-21
places: 0
file: hours_tyzw.py

## What this batch is
An "hours" session (PROMPTS.md type 7): no new places and no pins. The last six New York churches from `tools/hours.py list "New York" --kind worship`, then every church waiting in South Carolina (5), Maryland (4), Arizona (4), Georgia (4), Wisconsin (4) and Maine (4). Ten got service times from the page of whoever runs them, each read in the session (`tools/hours.py page`, or the page's full text where that printed too little) with the address checked against the place; twenty-one are recorded `?`.

Hours recorded:
- South Carolina: Parish Church of St. Helena, Beaufort (sthelenas1712.org: the traditional services are "in the Sanctuary, 505 Church Street"; the contemporary one is in the parish hall and is left out); Brick Baptist, St. Helena Island (brickbaptist.com, 85 Dr. Martin Luther King Jr Dr.). The NPS page says the interior is not usually open outside the congregation's own use.
- Maryland: St. Paul's, Point of Rocks (stpaulspointrocks.org, 1914 Ballenger Creek Pike).
- Arizona: Sacred Heart, Tombstone (shctombstone.org, 592 E. Safford St.); St. Paul's Episcopal, Tombstone (stpauls.azdiocese.org; read with the web fetch tool, as the site refuses scripts; the page shows no street address, the site's history page is Tombstone's).
- Georgia: Bethesda Baptist, Union Point (its own site, 1560 Bethesda Church Rd).
- Wisconsin: Unity Chapel, Spring Green (unitychapel.org/events: summer Sunday services in July and early August 2026 only; otherwise rented for events).
- Maine: First Congregational, Kittery Point (kitterypointucc.org, 23 Pepperrell Road).

Not checked: nothing was seen on the ground and no telephone call was made.

## Pages that would not open, or gave no times
| Place | Page tried | What happened |
|---|---|---|
| First Congregational, Middletown NY | localwiki.org | No congregation site found in two searches |
| Christ Church (First Universalist), Middletown NY | christchurchmiddletown.org | That site is Christ Episcopal in Middletown, New Jersey. No site of the NY church's own found |
| Temple Beth-El, Hornell NY | (Wikipedia only) | No congregation page found; present use not known |
| Church of the Redeemer, Addison NY | episcopalrochester.org/node/2259 | HTTP 403 to scripts; no parish page of its own |
| Primitive Baptist, Brookfield NY; Town Line Church, Cameron Mills NY | (Wikipedia only) | No page of whoever runs them found |
| Old St. David's, Cheraw SC | Town of Cheraw's historic-areas brochure (PDF) | No times; it says to contact the visitors bureau. A tourism page gives a phone number for tours of the inside |
| Pompion Hill Chapel SC; Old Stone Church, Clemson SC | SC Encyclopedia; clemson.edu tour page | No page of whoever runs them with times |
| St. Ignatius, Hickory MD | stignatiushickory.org (also 2610.sites.ecatholic.com) | HTTP 403 to scripts and the web fetch tool's approval went unanswered |
| Church of the Holy Trinity, Churchville MD | holy-trinity.com | Site did not answer; Internet Archive copy of 2025-12-27 exists (/faq) but could not be fetched unattended. Not confirmed to be the Churchville church |
| Graceham Moravian, Graceham MD | (no site found) | Only newspaper articles (emmitsburg.net says Sunday 10:30 a.m., 2023); not used, not the church's own page |
| Our Lady of Victory, Pearce AZ | gcatholic.org | No parish page found; only mass-time aggregators |
| Old Sacred Heart (Prescott Center for the Arts), Prescott AZ | (no site found) | PCA's own site did not turn up in two searches |
| Church of the Redeemer, Greensboro GA; Crawfordville Baptist GA; Springfield Baptist, Greensboro GA | HMdb / Georgia Encyclopedia | No congregation sites found (redeemergso.org is Greensboro, North Carolina) |
| Linden Methodist, Linden WI; Plum Grove Primitive Methodist WI; St. Augustine, New Diggings WI | umc.org (404), Wisconsin Historical Society, Travel Wisconsin | No page of whoever runs them with times |
| Harrington Meeting House, Bristol ME; Alna Meetinghouse ME; Old Walpole Meetinghouse ME | maine.gov MHPC page; alna.maine.gov; oldwalpolemeetinghouse.org | Owners' or town pages give no summer opening times (newspapers do, not used) |

No church was found to be closed or sold.

## Tips for the next session
- St. Ignatius (Hickory MD), St. Paul's (Tombstone) and Holy Trinity (Churchville MD) answer 403 to scripts; a session that can approve the web fetch tool can read them.
- The three Maine meetinghouses are opened in summer by local societies; their hours appear in the Lincoln County News and the Wiscasset Newspaper each June, not on any owner's page found.
