# tn_sfxf: Tennessee: furnaces, mounds, forts and frontier houses
state: Tennessee
region: tn
date: 2026-11-22
places: 16
file: data_tn_sfxf.py

## What this batch is
A first statewide scatter for Tennessee, the thinnest state when the session was claimed with `choose.py --thinnest` (21 places, nearly all on the northern Cumberland Plateau). Sixteen places from Memphis to the Virginia line: in the west Fort Pillow, Pinson Mounds and the Woodruff-Fontaine House in Memphis; on the Western Highland Rim the Great Western Iron Furnace and the Dover Hotel (Fort Donelson's surrender house) in Stewart County and the Montgomery Bell Tunnel in Cheatham County; in Middle Tennessee Cragfont, the Great Falls Cotton Mill at Rock Island, the Old Stone Fort and Falls Mill; in the east the Tellico Blockhouse foundations, the Burra Burra Mine and Ducktown Basin Museum, Blount Mansion in Knoxville, Rocky Mount, the Chester Inn in Jonesborough and the Elizabethton Covered Bridge. Sources read in the session: Wikipedia (`wiki_raw.py`), National Register forms from NPGallery (text layers read for Falls Mill, Cragfont, Woodruff-Fontaine, Rocky Mount, Tellico Blockhouse, Burra Burra, Blount Mansion, Great Western Furnace and the Great Falls Cotton Mill), HMdb markers, and the managing bodies' pages (tnstateparks.com with `page.py --all`, the Tennessee Historical Commission's state historic site pages, nps.gov for Fort Donelson, and the museums' own sites). Hours are from those pages, read November 22, 2026. Not checked: anything on the ground; the parking at Cragfont, Falls Mill, Rocky Mount, Burra Burra, Woodruff-Fontaine, the Great Western Furnace and the Montgomery Bell Tunnel (no mapped lot; the park's address point for the Narrows fell in woods); who owns the Elizabethton bridge and who manages the Great Western Furnace ground now (the pin check says Land Between The Lakes WMA); regular hours at Woodruff-Fontaine (its page gave only a holiday closure); Harpeth River park hours. Pins: Fort Pillow and the Old Stone Fort are area pins inside large earthworks; the Great Falls Cotton Mill pin was moved 120 m from the Register point (which fell on the park road in woods) to a long pale roof on the aerial, taken to be the mill but not certain; Blount Mansion's pin is on the grounds, not plainly on the house. Disagreements written into the entries (conf mixed): Rocky Mount's house dated 1770–72 by its 1970 Register form but late 1820s by tree-ring dating; the Burra Burra headframe (dismantled 1966 per the form, after 1958 per the museum) and the count of surviving buildings; the Falls Mill wheel (32 ft per the mill, 34 ft per the form); the tunnel's year (1818 or 1819); why the Great Western Furnace closed. Pictures: two chosen with `photo_find.py` (Great Western Furnace, Dover Hotel); none fitted the cotton mill or the Old Stone Fort.

## Leads
Places you read about and could not finish. One row each; delete the example row. Leave the table header.

| Place | Where | What is known | What is missing |
|---|---|---|---|
| Newlee Iron Furnace | Cumberland Gap (36.60144, -83.66817, HMdb marker 207276) | NPS page: 1819 blast furnace below Gap Cave, sandstone with fire-brick lining; HMdb says part of the 30-foot stack stands | HMdb files the marker in Lee County, Virginia, though the NPS calls the event there "Cumberland Gap, Tennessee": settle which side of the line the stack is on, then add it under va or tn |
| Newsom's Mill | Harpeth River State Park, 8729 Newsom Station Road, Nashville | Park page: one of the oldest gristmills in Davidson County, early or mid-1800s | A source for what stands, and a pin |
| Fort Donelson earthworks | Dover (Register point 36.487222, -87.851944) | Fort Donelson National Battlefield; park hours read on nps.gov/fodo/planyourvisit/hours.htm | Write-up of the fort and river batteries from the park's own pages |
| Hunt-Phelan House | Memphis (35.1375, -90.04389) | Wikipedia: c. 1830, Grant's and Polk's headquarters | Whether it is open today and who owns it |

## Tips
- tnstateparks.com park pages hide the hours in the gift shop and "Contact Information" blocks: `page.py --all <url> | grep -o '.\{160\}Hours.\{200\}'` pulls them out in one line each.
- The Tennessee Historical Commission's pages for state historic sites (`tn.gov/historicalcommission/state-programs/state-historic-sites/<name>.html`) give address and hours in a short page; `fort-loudoun` and `tellico-blockhouse` answer 404 (those are state parks: use tnstateparks.com).
- `nom.py` answered "HTTP Error 629" after about a dozen quick lookups; a three-second pause between calls was enough.
- The Ducktown Basin Museum's home page carries an old December 2024 closing notice and an undated renovation notice beside the current hours: ask by phone before trusting either.
