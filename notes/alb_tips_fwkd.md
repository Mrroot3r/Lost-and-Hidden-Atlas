# alb_tips_fwkd: Albany: two places readers sent in
state: New York
region: alb
date: 2026-11-19
places: 2
file: data_alb_tips_fwkd.py

## What this batch is
The first two places to carry `tip=`: both came through the Atlas's form on November 18, 2026, and the owner of the Atlas said in the maintainer chat that he sent them himself from a walk, so what he saw is taken as a field report. 759 Madison Avenue (an 1889 Queen Anne mansion on Historic Albany Foundation's "Places in Peril" list; the reader says only a shell is left) and a buried brick walk in Washington Park north of the tennis courts. Sources: the foundation's page read whole with `page.py --all`; Wikipedia's Washington Park Historic District article with `wiki_raw.py -g`. Pins were looked at on the leaf-off aerial. Not checked: who owns 759 Madison Avenue now, its state beyond the reader's report, any city demolition record, the brick of either place, park hours, and what the brick walk is.

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|

## Tips
- The form's sheet writes dates as 11/18/2026; `inbox.py` now prints the day as 2026-11-18 (for `tip=`) and the row's ref (for `source/inbox/done.txt`), which it did not print before.
- Two general web searches for a street address returned pages of property listings and nothing else. `page.py -g "Madison"` on Historic Albany Foundation's Places in Peril page found the building at once: for a derelict building in Albany, try that page first.
- John Taylor's grounds (bought for the park in 1882) are worth a search in the Albany Institute's and the Albany Public Library's map collections for a plan showing walks.
