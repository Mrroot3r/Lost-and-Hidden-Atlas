# bosvid_wklo: Boston, Massachusetts: halls, hotels, theatres and churches named in a walk through old Boston
state: Massachusetts
region: bos
date: 2026-11-27
places: 15
file: data_bosvid_wklo.py

## What this batch is
Fifteen standing buildings in Boston, taken from the names in one Old World Exploration video ("Old World Boston", 2022;
the record is source/videos/20220916_UZ6B9IDo9BA.md). The video gave 43 names; it is a tip only, and every fact comes from
Wikipedia read as raw text and, for hours, the managing bodies' own pages (Trinity Church's tours and worship pages, the
Boston Public Library's Central Library page, the Faneuil Hall Marketplace front page, the Mother Church page). Pins are
Wikipedia coordinates looked at on the MassGIS aerial; the Cyclorama pin was moved 67 m onto its dome, and the Majestic and
Orpheum theatres are pinned to the site only. Not checked: hours for South Station, the three theatres and halls, Quincy
Market and the Mother Church (all hours='?'); the inside of Old City Hall and the Custom House (whether the public may go in
or up the tower); Fort Independence tour times come only from search-result text quoting the state's 2026 tour sheet, which
refused to open (conf='mixed'). Red brick is '?' for most; Horticultural Hall is red brick from its Commons picture.

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Masonic Temple (Grand Lodge of Massachusetts) | Boston, MA (Tremont and Boylston Streets) | Named in the video; the Grand Lodge article has no coordinates or building history | A source for the building and whether it gives tours |
| Burrage House | Boston, MA (Commonwealth Avenue) | Perhaps the "mansion" the video shows; no Wikipedia article under that title | Confirm which mansion was meant; a source for the house |
| Hotel Somerset, St. James Hotel (Franklin Square House) | Boston, MA | Named in the video; no Wikipedia article under the titles tried | A source and whether each still stands |
| Post Office and Sub-Treasury, Hotel Westminster, Chickering Hall, Hotel Kensington | Boston, MA | Named in the video; probably gone, not confirmed | A source saying they were demolished, so the record can say "gone" |

## Tips
- In Boston mass.gov (Castle Island and its tour sheet), oldcityhall.com, necmusic.edu and bostoncenterforthearts.org all refused both page.py and the web fetch tool; christianscience.com answers only its front page (/the-mother-church), with no times on it.
- Wikipedia's infobox "address =" line (grep the raw text kept in research/wikiraw/) is a quick sourced street address for an access note.
