# hours_amjw: hours for 36 places of worship in New York, Newfoundland and Labrador, Texas and New Jersey
state: New York
region: ny
date: 2026-11-20
places: 0
file: hours_amjw.py

## What this batch is
An "hours" session (PROMPTS.md type 7): no new places and no pins. All four New York places of worship still waiting were looked up, then the whole of the Newfoundland and Labrador (15), Texas (9) and New Jersey (8) lists from `tools/hours.py list "<state>" --kind worship`. Five got times from the page of whoever runs them, each read in the session with `hours.py page`; 31 are recorded `?` because no page of their own gave any.

Hours recorded (the page is in the file; the address or town on each page was checked against the place):
- St. James Episcopal, La Grange, Texas: its own site (stjameslagrange.org), which names the 1885 building. Sunday 8:00 and 10:30.
- Crosswicks Friends Meeting House: Philadelphia Yearly Meeting's page for the Crosswicks meeting (PO Box in Crosswicks). Worship 10 to 11 September to June, 9:30 to 10:30 in summer.
- Salem Friends Meeting House: Salem Quarter's own page (southjerseyquakers.org), 200 E Broadway. Worship 10:30 to 11:30.
- Hibernia Methodist Episcopal Church (now a library branch): the Rockaway Township Free Public Library's contact page (419 Green Pond Rd): Mondays 11 to 5, Wednesdays 2 to 8. The MAIN consortium page gives the same.

Not checked: nothing was seen on the ground and no telephone call was made.

## Pages that would not open, or gave no times
| Place | Page tried | What happened |
|---|---|---|
| Nine Partners Meeting House, Millbrook NY | millbrookhistoricalsociety.org/events | Talks and events only; no open days |
| Beth David Synagogue, Amenia NY | templebethdavid.org | 403, and not shown to be the Amenia congregation (many Temple Beth Davids) |
| Smithfield Presbyterian, Amenia NY | ameniany.gov/houses-of-worship | Town list; no times. No site of the church's own found |
| First Reformed, Wynantskill NY | frcoc.org (404) | No site of its own found |
| All 15 Newfoundland churches | centraldiocese.ca/parishes, rcsj.org, heritage.nf.ca, historicplaces.ca | The Central diocese page lists the Bonavista, Catalina and Trinity parishes' churches with a telephone and no times. rcsj.org has parish pages for Divine Mercy and the Basilica, not for St. Patrick's on Patrick Street. trinityhistoricalsociety.com gives its own sites' season (June 1 to October 9, 9:30 to 5) but does not run the churches |
| St. George's, Brigus | communitystories.ca; historicplacesdays.ca | The Historic Places Days hours (weekdays 10 to 2) carry a 902 Nova Scotia phone number: a different St. George's, not recorded |
| Painted churches at Dubina, Ammannsville, Praha, High Hill (Texas) | 2809.sites.ecatholic.com/parishfinder and victoriadiocese-org.sites.ecatholic.com (Diocese of Victoria, 403 to the tool, no archive); schulenburgchamber.org (403; archive copy 2026-05-12 not fetched) | Only mass-time aggregators gave times; not used |
| First Baptist and St. John's Methodist, Stamford TX | (web search only) | No page of their own found |
| Bethlehem Lutheran, Round Top TX | roundtop.com | Timed out; a tourism page in any case |
| Arney's Mount, Old Stone Church Kingwood, Locktown Baptist, Old Pittsgrove (New Jersey) | (web search only) | No page of their own found |
| Alloways Creek Friends Meetinghouse NJ | salemquarter.net/?p=406 | Salem Quarter's history page: the meeting was laid down in 1938; no worship times |

Closed or changed hands (from the place's own text or a search result, not settled):
- Former Cathedral of the Immaculate Conception, Harbour Grace: privately owned since its sale (the place's note cites CBC on a brewery plan).
- First Presbyterian Church building, Anson TX: a Waymarking page calls it "1929 - Anson-Jones Museum". Not a source; worth checking whether the building is now a museum with hours.

## Leads
None.

## Tips
- Newfoundland parishes seldom have pages of their own; the dioceses list churches with a phone number only. Expect `?` there.
- The Diocese of Victoria (Texas painted churches) answers 403 to the page tool and has no archive copy; try the web fetch tool on its parish finder in an attended session.
- For Quaker meetings in New Jersey and Pennsylvania, pym.org/meetings/meeting/<name>-friends-meeting/ gives worship times; southjerseyquakers.org has Salem Quarter's meetings.
