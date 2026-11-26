# de_vfba: Delaware: Kent, Sussex and southern New Castle
state: Delaware
region: de
date: 2026-11-22
places: 16
file: data_de_vfba.py
tidied: 2026-11-26

## What this batch is
Third pass over Delaware, taken with `choose.py --thinnest` (35 places before, 51 after). 16 places spread over all three counties. Kent: Belmont Hall (Smyrna), Christ Church and Woodburn (Dover), the Camden Friends Meetinghouse, the Old Stone Tavern at Little Creek and the Parson Thorne Mansion in Milford. Sussex: the Highball Signal in Delmar, St. George's Chapel near Harbeson, Cool Spring Presbyterian Church, the Redden Forest lodge, the De Vries monument in Lewes and the Governor Ross Mansion in Seaford. New Castle: the Corbit–Sharp House in Odessa, the New Castle ice piers, Cooch's Bridge and the Liston Range Rear Light. Sources: Wikipedia read as raw text (`wiki_raw.py`, with `--rows` for the Kent and Sussex Register lists), and the pages of whoever runs each place read with `page.py`: history.delaware.gov (state sites list, Cooch's Bridge, Belmont Hall), woodburn.delaware.gov, archives.delaware.gov marker pages (Cool Spring, St. George's, Carey's Camp), the Delaware Forest Service, historicodessa.org, seafordhistoricalsociety.com, allsaintsandstgeorges.org, pym.org, an NPS article on the ice piers, HMdb and Lighthousefriends.com. Every pin was looked at on the aerial and the LiDAR; five were moved onto the building. Not checked: anything on the ground; the Parson Thorne Mansion's hours (only the county visitor bureau's listing was read, so `hours='?'`); Christ Church Dover's and Cool Spring's service times (no page of their own was read); who owns the Old Stone Tavern (the federal land map marks it as state land) and the ground of the De Vries monument; parking at most places. The ice piers pin stands for the group in the river; the Highball Signal, Liston light and De Vries monument pins are on the right spot by the sources but the object itself was not made out on the aerial. `check.py` warns that the Highball Signal pin is just outside Delaware's outline; on the aerial it is north of the State Street line, in Railroad Park.

## Leads
Moved to `LEADS.md` on 2026-11-26 by the tidy job (5 rows). New leads for this ground go in the note of the batch that finds them.

| Place | Where | What is known | What is missing |
|---|---|---|---|

## Tips
Folded into `GUIDE.md` and the tools on 2026-11-26 by the tidy job (4 tips).
