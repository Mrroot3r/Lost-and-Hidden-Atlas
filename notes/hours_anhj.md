# hours_anhj: hours for 29 places of worship (New York, Prince Edward Island, Saskatchewan, Manitoba)
state: New York, Prince Edward Island, Saskatchewan, Manitoba
region: ny
date: 2026-11-21
places: 0
file: hours_anhj.py
tidied: 2026-11-26

## What this batch is
An "hours" session (PROMPTS.md type 7): no new places and no pins. Every church still waiting in New York (11), then Prince Edward Island (8), Saskatchewan (5) and Manitoba (5), from `tools/hours.py list "<state>" --kind worship`. Seven got service times from the page of whoever runs them, read in the session; 22 are recorded `?` because no page of their own could be found after two searches.

Hours recorded (the page read is in the file; the town or street on each page was checked against the place):
- St. John's Episcopal, Monticello: the Episcopal Church's own listing (episcopalassetmap.org node 368), 15 St. John's St.: Sunday 9:30 a.m., and "open on Thursdays 3:30 to 5:30".
- B'nai Israel (the Woodbourne Shul): its own site, 457 Route 52: minyanim around the clock in the summer season. The opening date it gives ("Thursday, June 20th") has no year, so only "from late June" is recorded.
- St. John the Baptist, Miscouche; St. Augustine's, Rustico; All Saints, Cardigan: the Diocese of Charlottetown's Mass-times table of February 2026 (PDF). Earlier sessions could not read its days; the column positions were read with pdfplumber this time (Sunday column at x≈886, Saturday vigil at ≈798, Tuesday at ≈376, Thursday at ≈531), checked against St. Paul's, Summerside, which has a Mass in every column. St. Augustine's own site (staugustineschurch.ca) would not connect.
- All Saints Anglican, Katepwa Beach: the Resort Village of Katepwa Beach's own page (the church is its municipal heritage property): Sundays 9:30 a.m., May long weekend to September long weekend.

Not checked: nothing was seen on the ground and no telephone call was made.

## Pages that would not open, or gave no times
| Place | Page tried | What happened |
|---|---|---|
| St. Paul's Lutheran, Liberty NY | st-pauls-lutheran-church.squarespace.com | It gives Sunday 10:00 a.m., but its history page puts it at Oswego and Vine Streets: a different St. Paul's, not the Chestnut Street church. Recorded `?` |
| Old St. James, Port Hill PE | nspeidiocese.ca parish page | The diocese lists it as "Old St. James – Birch Hill (deconsecrated)"; the parish's 10:30 a.m. Sunday service is not in it |
| Church of the Resurrection, Dauphin MB | archeparchy.ca/dauphin/ | The archeparchy gives Divine Liturgy times (Tue, Thu, Sun 9:30 a.m.) at 801 Jackson Street, which is the parish's 1990 church; the old church on the map is not said to be used. Recorded `?` |
| St. Laurent Shrine, SK | saintlaurentshrine.com; padiocese.ca/st-laurent-shrine | Neither gives dates. The Diocese of Saskatoon's event page (rcdos.ca/event/st-laurent-pilgrimage/) says pilgrimages are July 15–16, August 15 and September 8, with no year shown; it is not the shrine's own diocese (Prince Albert), so not recorded |
| Sacred Heart, Lebret SK | archdiocese of Regina | No parish page found; sacredheartparish.ca is a parish in Delta, BC |
| St. Mark's Lutheran, Middleburgh; Gallupville Lutheran and Methodist; Woodbourne Reformed; Loch Sheldrake, Mountaindale and Glen Wild synagogues; Glen Wild Methodist (private) | web searches | Only directories and Wikipedia |
| Trinity United and Summerside United Baptist, Summerside; St. David's United, Georgetown; Little Sands church | web searches | Only directories (pe.211.ca, newspaper listings) |
| St. Peter's, Qu'Appelle; Christ Church, Abernethy | quappelle.anglican.ca/churches | The diocese's list gives an address and telephone for Katepwa Beach only; no times |
| St. Andrew's on the Red; Christ Church, The Pas; St. Peter Dynevor; Old St. Michael's, Gardenton | web searches | No parish page found (rmofstandrews.com/p/worship is a municipal directory) |

No church was found to be closed or sold, apart from Old St. James, Port Hill, which the diocese calls deconsecrated (the place text already treats it as the old church).

## Tips for the next session
Folded into `GUIDE.md` and the tools on 2026-11-26 by the tidy job (2 tips).
