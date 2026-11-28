# nm_wrcv: New Mexico, San Miguel County
state: New Mexico
region: nm
date: 2026-11-28
places: 14
file: data_nm_wrcv.py

## What this batch is
Fourteen places in San Miguel County, New Mexico, spread from the Pecos valley (Pecos, Terrero, Glorieta Baldy) to Rociada, San Miguel del Vado, Variadero on the plains and Las Vegas. All come from National Register listings the Atlas did not have; facts are from the Park Service record and form (`tools/form.py`), Wikipedia articles read as raw text, and the Forest Service page for the lookout. Pins were checked on the aerial; the Pendaries mill, Glorieta Baldy, the Ilfeld chapel and the roundhouse are marked as site pins and the Rogers building and San Miguel del Vado as area pins. Pictures: five from Commons (two bridges, post office, Rogers building, Taichert building) plus six places with a Wikipedia picture; the rest have none on Commons. Red brick: the post office and the Taichert building were settled from a Commons photograph, the Ilfeld chapel from the form; the roundhouse and the Eldorado Hotel are `?` (the forms say brick, not its colour).

Not checked: present use and opening hours of every Las Vegas building (the forms date from 1985), whether the Pendaries mill is open or how the 2022 Calf Canyon fire touched it, service times at the Pecos church (parish page not read), road access to Glorieta Baldy, and the owner of the Variadero road. Glorieta Baldy's county differs (the Register says San Miguel, Wikipedia Santa Fe), and the Presbyterian church's "oldest Protestant church" claim differs between the 1978 form and a preservation page; both are in the entries.

## Leads
Places read about and not finished, all National Register listings in San Miguel County.

| Place | Where | What is known | What is missing |
|---|---|---|---|
| Bell Ranch Headquarters | Bell Ranch, NM (35.52894, -104.09384) | Listed 1970; one of the largest private ranches (Wikipedia) | Private ranch with no public access; a current source for what stands |
| Park Springs Ranch Headquarters Complex | Dilia, NM (35.26558, -104.93087) | Listed 2008; years 1861–1912 in the record | The 2008 form text would not read (scanned map pages); access |
| Conchas Dam Historic District | Conchas Dam, NM (35.38893, -104.19902) | Dam built 1936–39 (Wikipedia); a state park | Form is 440,000 characters of Art Deco concrete work; decide whether it fits |
| St. Paul's Memorial Episcopal Church and Guild Hall | 711/716 National Ave, Las Vegas (35.5962, -105.21836) | Listed 1976 | The form's text layer holds only photo captions |
| Johnsen Mortuary, Douglas Avenue School, Las Vegas Municipal Building, Montezuma Street houses | Las Vegas | Listed; pictured on Commons (Johnsen Mortuary: brick) | Dates and descriptions from their forms |

## Tips
- `gaps.py` lists about 40 houses on one Las Vegas street list; most are ordinary houses. The better targets are the commercial and institutional listings.
- Old 1978 forms scan badly: the useful text is in the "Statement of Significance" block; `grep -o` on the squashed text works.
- The Wikipedia picture-finder sheets of Commons "NRHP" photographs by the same uploader (John Phelan) cover most Las Vegas listings, which settles brick colour fast.
