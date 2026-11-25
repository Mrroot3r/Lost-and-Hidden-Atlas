# ks_olth_wbqn: Johnson County, Kansas (fourth pass)
state: Kansas
region: ks
date: 2026-11-25
places: 10
file: data_ks_olth_wbqn.py

## What this batch is
Ten places round Olathe in Johnson County, Kansas: in Overland Park the Conser Building and the Overland Park Presbyterian Church; in Lenexa Holy Trinity's stone church of 1911 and the frame Ann Huseman Building; in De Soto Abbott's Hall; in Shawnee the Fangro House, the Governor Reeder Mansion site, the 1909 State Savings Bank and the LeCluyse House; and the Kansas School for the Deaf's Roth Building in Olathe. The Atlas already held 23 places within 15 km of Olathe and the National Register lists for the county were used up by three earlier batches, so the names came from the Kansas Historical Society's 2009 Johnson County survey report (downloaded as a PDF and read with pdftotext), the Clio walking tour of Olathe, Overland Park and Shawnee (all 28 stops read), the Holy Trinity parish's history page, a KCUR guide to Shawnee, the Tonganoxie Mirror and the Johnson County Post. Web search summaries were used to find pages, not as sources, except where a note says so. Pins are address lookups checked on the 2024 state aerial; nothing was checked on the ground. No opening times were found for any place (hours are `?` or not given). Not checked: whether the Presbyterian church was made into a hotel, which date the Roth Building bears (the survey and the school disagree), whether any of the Fangro House can be seen from the street, and the exact building of the State Savings Bank (pin is `area`). Pictures: Abbott's Hall and the Huseman Building have one (the Huseman choice is a likely one: a small white frame shop 110 m from the pin); the rest have none on Commons. Commons login worked.

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Salem Lutheran Church | 9143 Haskins Street, Lenexa, KS (38.96206, -94.74043) | 2009 county survey: 1924 Gothic Revival limestone, replacing an 1888 frame church that burned | A second source and whether it is open |
| Spring Family store | Midland Drive, Shawnee, KS | 2009 county survey: L-plan stone commercial building of about 1925 | An address and a second source |
| Old Shawnee Jail | Old Shawnee Town, Shawnee, KS | 2009 survey: stone jail of 1843, taken apart and rebuilt at the town in 1966 | Whether it should be listed apart from Shawnee Town 1929 |
| Dutton-Thomas-Soule Farm | 7925 Sunflower Road, De Soto vicinity, KS | State Register 2006, Italianate/Late Victorian farm | The nomination is a scan; no other page found |
| Edgerton Grange Hall | 400 Nelson, Edgerton, KS | State Register 1998 | Nomination is a scan; no other page found |
| Dr. William C. Harkey House | 224 E. Main, Gardner, KS | State Register 1986, Queen Anne; a Harkey House Historical Society formed in 1986 | Nomination is a scan; no date or description found |
| George Hodges House and Charles Hyer House (Hycrest) | 425 S. Harrison and 505 E. Cedar, Olathe, KS | State Register 1990 and 1984 | Both nominations are scans; a web search found nothing |
| Olathe Santa Fe Depot | Olathe, KS | City history page says built 1881 | Whether it still stands (olatheks.gov answered 403) |

## Tips
- Johnson County is saturated for Register listings: after four batches only scanned State Register nominations remain. The 2009 county survey report (`https://www.kansashistory.gov/resource/survey/jocosurveyreport2009.pdf`, 160 pages, text layer; `page.py --all` cuts it off at 12,000 characters, so download it with curl and run `pdftotext -layout`) names dozens of stone and frame buildings by address in each town and is the best next source for Lenexa, De Soto, Shawnee, Overland Park and Gardner.
- The Clio tour pages (`https://theclio.com/tour/1012/<n>`) read well with `page.py --all`. Clio entries for the same buildings exist outside this tour (the Conser Building is `theclio.com/entry/189036`).
- A building named in the county survey can have two addresses in later news (the Overland Park Presbyterian Church: 8109 Overland Park Drive in 2009, 8029 in 2022); give both and do not assume one building.
- Recent Kansas nominations (2021 on) are not on NPGallery (the text address returns a small PNG); use the `nominationsNRDB` address from the Kansas Historical Society's register search. Older State Register nominations there are scans with no text layer.
- hmdb.org answered 403 from `page.py` and the archived copies could not be fetched.
- `publish.sh` stops if the batch time is in the future: take the time from `date -u` after the data file is finished, not before.
