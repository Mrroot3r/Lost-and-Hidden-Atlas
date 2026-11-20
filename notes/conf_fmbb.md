# conf_fmbb: Mohawk crossings, Crescent and Newtonville
state: New York
region: albco, conf, sar
date: 2026-11-20
places: 10
file: data_conf_fmbb.py

## What this batch is
Ten places round the edges of region `conf` (drawn at random by `choose.py --state ny`), which was already worked hard on November 18; three of them finish leads from `conf_edvk` and `conf_kovn`. Cohoes and Colonie's Mohawk crossings: the Old Military Crossing markers below the Crescent dam (with the 1938 Loudoun Ferry Road marker folded in) and, in Halfmoon, the Vandenburgh–Dunsbach ferry site, where the two markers disagree on where Knox crossed in January 1776 (both given, `conf='mixed'`). Crescent: the Church Hill Historic District (2021), with Oakcliff and the Halfmoon Academy sign, area pin. Cohoes: the Fonda House (about 1727), pinned at its Register address, 55 Western Avenue (historypointer.com's copy of the Register entry; the Wikipedia point is 1.3 km off). Newtonville: the 1852 Baptist church that became the post office, and the 1893 Methodist church. Clifton Park Center Baptist Church (1837) and its cemetery, with Sunday hours from the church's own contact page. Waterford: the 1896 station that is now the public library (hours from the library's home page; the earlier village entry calls it "the D&H building of 1835", both given), the Halfmoon Fort marker on US 4 and the Eagle Tavern site marker. Sources were read with `wiki_raw.py` and `page.py` (HMdb marker pages, the Saratoga County History Center, the church and library sites); red brick for three places is from the Wikimedia photographs `brick.py look` fetched. Not checked: anything on the ground; whether the Newtonville building is still a post office (USPS location pages come back as a template with a Washington address, so no hours); the Fonda House's present state (the 2004 Register entry is the newest source, and the aerial shows only a small house among trees); whether the Halfmoon Academy building stands; parking at Newtonville, the Waterford library and the Halfmoon Fort marker. Marker-only places (nothing standing): Old Military Crossing, Halfmoon Fort site, Dunsbach ferry, Eagle Tavern.

## Leads
Places you read about and could not finish. One row each; delete the example row. Leave the table header.

| Place | Where | What is known | What is missing |
|---|---|---|---|
| Cohoes Waterworks Pump House | Cohoes, NY (Harmony Mills district, between the falls overlook and Harmony Mill No. 1) | Spindle City Historic Society, Harmony Mills district brochure 2023, stop 12: begun 1857, still working, built on a lock of the original Erie Canal | Its position: neither OpenStreetMap nor nom.py names it |
| Corporation Hall | Green Island, NY (George and Clinton Streets) | HMdb 256010: first public building on Green Island, 1883 | Which corner building it is; the village history page does not name it |
| Reformed Church of the Boght sites | Colonie (HMdb 24730, 42.78367, -73.7404) and Cohoes (HMdb 255761, Baker Avenue at Vliet Street Extension) | Two markers: congregation organized 1784, church built about 1783, the first north of Albany; a 1929 marker for The Boght settlement beside the first | Anything to see beyond the markers, and where the congregation went |
| West Crescent Methodist church and cemetery | Halfmoon, NY (HMdb 139358, 42.81957, -73.75807, Grays Corners) | Halfmoon Historical Society sign: church and cemetery organized 1841 | Whether the church stands |
| Goodrich School | Colonie, NY (Wikipedia 42.7291, -73.7469) | Wikipedia: Classical Revival brick school of about 1922 with a six-column portico and cupola, National Register 2000 | Present use; the Colonie Village School nearby was torn down (Preservation League), so check it still stands |
| Godfrey Farmhouse | Cohoes, NY | National Archives copy of the Register form (79003240 on s3.amazonaws.com) answers 403 to page.py, as it does for the Fonda House | Address, and whether it stands (the earlier row in conf_edvk still applies) |

## Tips
- The National Archives' Register PDFs (`s3.amazonaws.com/NARAprodstorage/.../NPS_NY/<ref>.pdf`) answer 403 to page.py; historypointer.com/nris/resource/<ref> gives the Register's street address and was the way to place the Fonda House.
- USPS location pages (tools.usps.com/locations/details/...) give no usable hours to page.py or hours.py: every one comes back with the same Washington, DC template.
- The HMdb nearby list for a point was the quickest way to find what this well-worked ground still lacked: list the titles from the cached page with grep for `m.asp?m=`, then read the markers' inscriptions and positions together.
