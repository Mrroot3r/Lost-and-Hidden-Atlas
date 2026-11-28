# nb_hrvk: Fredericton, Saint John, Quispamsis and St. Stephen, New Brunswick
state: New Brunswick
region: nb
date: 2026-11-28
places: 12
file: data_nb_hrvk.py

## What this batch is
Twelve National Historic Sites and provincial historic places in New Brunswick that the Atlas lacked (the province had 69): in Fredericton the city hall, the York County court house, St. Anne's Chapel of Ease, St. Paul's United Church, the Arts Building and the William Brydone Jack Observatory; in Saint John the Imperial Theatre, the Chipman Hill townhouses, the Ordnance Store (HMCS Brunswicker) and the site of Fort La Tour; the St. Luke's church at Quispamsis; and the St. Stephen post office. Each was read from its Canadian Register of Historic Places statement (historicplaces.ca, `page.py --all`), plus Wikipedia raw text for four. Register ids came from web searches limited to historicplaces.ca, since the Register's own search page answers HTTP 500. Pins are the federal points in Wikipedia's list of National Historic Sites in New Brunswick, checked on the Esri aerial (no LiDAR; no state imagery for Canada). Not checked: visiting hours for every one (the sources read give none; each is `view` with "not checked"), parking, owners other than what the Register says, and what is inside any building. The Imperial Theatre's Register page records it as a local historic place; whether it is also a National Historic Site was not settled. The batch is Fredericton- and Saint John-heavy because those are where the Register's national listings are; the rest of the province (Miramichi, the north shore, the upper Saint John valley) still has few places.

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Barrack Green Armoury | Saint John, NB (60 Broadview Avenue) | Register id 15924: 1911-12 castellated Tudor-style drill hall by T. W. Fuller, Recognized Federal Heritage Building | Pin and a picture; left out because the Ordnance Store beside it was added |
| Fort Jemseg and Jemseg Archaeological Site | Jemseg, NB | National Historic Site (Wikipedia list); Register id 7990 for the archaeological site | Anything to see on the ground |
| Fort Nerepis, Fort Menagoueche (Fort Charnisay), Fort Meductic, Tonge's Island, La Coupe Dry Dock | Kingston Peninsula, Saint John, Meductic, Aulac, Sackville, NB | All on Wikipedia's National Historic Sites list | Register statements, what survives, access |
| Our Lady of the Assumption Cathedral | Moncton, NB (226 St. George Street) | Register id 6290 was the wrong place (Manitoba); the right pages are 23475 or 5578 | A look at which page, and the interior and hours |

## Tips
- historicplaces.ca's search page answers HTTP 500; a web search with allowed_domains historicplaces.ca finds a place's Register id, and the place page then reads with `page.py --all -n 60000`.
- A web search for a Register id sometimes returns a namesake in another province (a "Our Lady of the Assumption" in Manitoba): check the address line.
- `wiki_raw.py` found no article for "York County Court House (New Brunswick)" or "St. Paul's United Church (Fredericton)"; the Register page is the only source for those.
