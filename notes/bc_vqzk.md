# bc_vqzk: British Columbia: a fourth scatter
state: British Columbia
region: bc
date: 2026-11-28
places: 12
file: data_bc_vqzk.py

## What this batch is
Twelve places in British Columbia, claimed with `choose.py --thinnest` (BC had 63): in Victoria the 1863 Congregation Emanu-El synagogue, the 1875 Church of Our Lord, St. Andrew's Cathedral and the Malahat Building (old customs house); the Chinese cemetery at Harling Point in Oak Bay; St. Paul's Church on the Mission reserve in North Vancouver; Chilliwack's 1912 concrete city hall (now the museum); the 1911 Sikh temple at Abbotsford; the Church of the Holy Cross at Skatin; the Chee Kung Tong building in Barkerville (a LEADS.md row, removed); and the sites of Kootenae House near Invermere and Fort Alexandria on the Fraser. Facts and coordinates come from the Canadian Register statements (historicplaces.ca, one page at a time with 3-second pauses, none reset), Wikipedia for Kootenae House, and the pages of Church of Our Lord, St. Andrew's Cathedral (standrewscathedral.com) and the Chilliwack Museum for hours. Hours are `?` for Emanu-El, St. Paul's, the Sikh temple and the Barkerville building (the congregations' and Barkerville's pages did not open; a web search quoted only old tour times for Emanu-El). Not checked: anything on the ground, parking, owners of the Malahat Building and the Alexandria pasture, whether the Skatin church can be visited and how to reach the village. Pins are the Register points; the Holy Cross pin sits in cloud and trees on the aerial (area pin), the Barkerville pin is the middle of the town (area pin), and the two fur-post pins show only open ground. Red brick: Emanu-El and St. Andrew's yes (Register text); Malahat is brick of unseen colour (`?`); the wooden, concrete-and-painted and site entries are no. Pictures were chosen for seven places; none found for St. Paul's, Kootenae House and Fort Alexandria.

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Former Victoria Law Courts (Maritime Museum of BC) | 28 Bastion Square, Victoria, BC (48.42585, -123.36907) | Register: 1889, by Herman Otto Tiedemann, now the museum | Museum hours; brick colour |
| St. Ann's Academy | 835 Humboldt Street, Victoria, BC (48.41922, -123.3633) | Register: brick-clad convent of 1871, 1886 and 1910 with the 1858 cathedral chapel inside | Hours, owner, colour of brick |
| Father Pandosy Mission | Okanagan Mission, Kelowna, BC | Wikipedia: restored 1859 mission museum owned by the Catholic Church | A Register or operator page that opened |

## Tips
- The Register's `CRHP|id|name` ids on Wikipedia's national list are mostly right but a few are shifted by one row; check the title on the page before using one.
- `standrewscathedral.ca` is the Prince Rupert cathedral; Victoria's is `standrewscathedral.com`.
- Guessed operator addresses mostly failed from the shell (Emanu-El, Pandosy Mission, Abbotsford temple, Parks Canada Kootenae); a web search result gave the true address first, then `page.py` read it.
