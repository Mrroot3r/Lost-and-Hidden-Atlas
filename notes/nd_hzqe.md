# nd_hzqe: North Dakota: fieldstone and Swedish churches, schools, a bridge, a depot, a mill and an opera house
state: North Dakota
region: nd
date: 2026-11-28
places: 9
file: data_nd_hzqe.py

## What this batch is
Nine places in Walsh, Traill and Grand Forks counties, North Dakota (which had 70 places; claimed with `choose.py --thinnest`): Viking Bridge (Portland), the Mayville depot museum, St. Catherine's fieldstone church (Whitman), North Trinity "Swede" church (Nash), the Funseth round barn (Kempton), Minto School museum, Pisek School, the North Dakota Mill (Grand Forks) and the Metropolitan Opera House (Grand Forks). Each Register record and form was read with `form.py`; present use, owners and hours came from web search results only, never a managing body's own page, so hours and condition are marked unchecked where no page was read. Pins were checked on the aerial; North Trinity and the depot were moved onto the buildings. Pictures: Commons had one for the Mayville depot and Pisek School (set from the sheet); the rest are none. Brick: Mayville depot is cream/buff and Pisek School red from the Commons pictures; others from forms (Minto buff) or left "?".

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| St. Joseph's Chapel (Minto) | Pulaski Twp, Walsh County, ND (48.30962, -97.14543 on Register and Wikipedia) | 1907 Polish wayside shrine, 8 ft square, moved 12 ft in 1969 (Register form 94000556) | Nothing shows on the aerial at that point or within 300 m; the true position, and whether it still stands, are unknown |
| Elmwood (Williamson House) | Grafton, ND (48.42203, -97.40547) | 1895 Victorian mansion, Register form 85000339 | Present owner, condition and access; private residence in 1985 |
| Traill County: Mayville Historic District and its listed buildings, Hillsboro courthouse, Eielson House (Hatton), Norway and Caledonia bridges | Traill County, ND | Register listings the Atlas lacks (gaps.py) | Not read; forms available through `form.py` |
| Grand Forks downtown Register buildings (Masonic Temple, Viets Hotel, Woolen Mills, Northern Pacific depot) | Grand Forks, ND | gaps.py lists 59 listings | Not read |

## Tips
- `choose.py --thinnest` gave North Dakota again (70 places); gaps.py counties Walsh, Traill and Grand Forks all have forms that `form.py` reads at once.
- 1970s forms (Mayville depot, Funseth barn) say nothing of present use; a web search was the only way to learn it, and gave directory-grade hours.
- A Register point can sit on a section-line crossing with nothing visible (St. Joseph's Chapel): a place that small may need the state's site file.
