# la_wpfv: Cane River and Natchitoches: Creole plantations, bousillage houses and a Spanish capital
state: Louisiana
region: la
date: 2026-11-19
places: 17
file: data_la_wpfv.py

## What this batch is
Second pass in Louisiana, region la drawn at random; worked Natchitoches Parish (Natchitoches town, the Cane River and Isle Brevelle, Robeline and Marthaville) plus Fort Jesup just over the line in Sabine Parish. Seventeen places, nearly all standing: Magnolia and Oakland plantations and the Texas and Pacific depot (the three units of Cane River Creole National Historical Park), Melrose, St. Augustine church and cemetery, the Badin-Roque poteaux-en-terre house, Cherokee Plantation house, the American Cemetery, the Prudhomme-Rouquier and Roque bousillage houses, the Minor Basilica, the old parish courthouse, the Southern Cotton Oil Mill, Los Adaes and Fort Jesup state historic sites, St. Anne Church at Spanish Lake and the City Hotel at Marthaville. Sources: Wikipedia through wiki_raw.py; NPS park pages (hours, fees, directions, history) and nps.gov/places pages for the two state sites through page.py; HMdb marker texts and positions (two nearby lists gave nearly every pin); the 2017 Southern Cotton Oil Mill Register form; melroseplantation.org; the Diocese of Alexandria's basilica page; the Natchitoches visitors' bureau; SAH Archipedia for Fort Jesup; a 2022 Natchitoches Parish Journal report for the Roque House. NOT checked: Los Adaes and Fort Jesup hours and fees (lastateparks.com answers 403, explorelouisiana.com too, and search results quoted no text); Melrose admission and parking; who owns and opens the Prudhomme-Rouquier and Roque houses and the American Cemetery; whether the Badin-Roque house opens; the City Hotel's present use (pin moved onto the building south of the street, not confirmed as the hotel); St. Augustine and St. Anne interiors; the genealogy library hours in the old courthouse. Dates disagree and are given both ways for Magnolia (founding, enslaved count), the depot (last passenger train 1965 or 1969), the basilica (three sets of dates) and the Roque House (1797 or 1803). Brick: only Magnolia's quarters settled (yes, from a Wikipedia photo); the basilica and Melrose pictures are black-and-white HABS photographs and the courthouse article has none, so they stay '?'. Nothing checked on the ground.

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Old Plauche Place (Ducournau Plantation) | Natchez, LA (marker 31.674245, -93.022005) | c. 1836 poteaux-sur-sole and bousillage Creole cottage on Metoyer's 1780s grant (HMdb 70645) | The marker stands on a road through fields; which house it is and who owns it |
| Fort St. Jean Baptiste State Historic Site | Natchitoches, LA | A 1979 reconstruction of the 1716 French post beside the American Cemetery (HMdb 106118, 106119) | Left out as a replica; add only if wanted, with Louisiana State Parks hours |
| Kate Chopin House (Bayou Folk Museum) site | Cloutierville, LA (31.540556, -92.917222) | Register list: destroyed by fire in 2008 | Whether anything stands or is marked at the site |
| Maison de Marie Thérèse (Coincoin-Prudhomme House) | Bermuda, LA (31.673889, -93.018333) | Register-listed; HABS photo named on the Wikipedia list | No article read; owner, access, what stands |
| Kaffie-Frederick General Mercantile and Ducournau Building (1835) | Front Street, Natchitoches | Ducournau Building 1835 on an HMdb marker (109797) | A source on what survives inside and whether the store is open |
| Carnahan Store, Flora Commissary, Caspiana Plantation Store | Cloutierville, Flora, Natchitoches | Register-listed plantation stores (Wikipedia list) | No article; owners and condition |
| Desadier School site | Bayou Bourbeaux (31.828380, -92.973110) | 1870s school for Native American children, HMdb 257808 (marker of 2024) | Whether the school building stands |

## Tips
- Louisiana State Parks (lastateparks.com) and explorelouisiana.com both answer HTTP 403 to page.py, and search results for their hours came back as titles only: state historic site hours could not be read in an unattended session.
- The nps.gov/places pages for Los Adaes and Fort Jesup (state sites on El Camino Real de los Tejas) read well and give address and what visitors can see.
- Two HMdb nearby lists (3-mile radius round downtown Natchitoches and round Isle Brevelle, 31.62, -92.98) gave positions for the Cane River park signs, the Melrose buildings and most downtown houses in two requests.
- The NPS Cane River pages warn that GPS sends visitors wrong; take parking from parking.py and the park's directions page.
