# kcmo_ind3_zbtk: Independence, Missouri (third pass)
state: Missouri
region: kcmo
date: 2026-11-24
places: 7
file: data_kcmo_ind3_zbtk.py

## What this batch is
Seven National Register houses in Independence that the two earlier passes left out: Lewis Jones, Lewis-Webb, Owens-McCoy, Overfelt-Campbell-Johnston, Charles Minor, Hughes and Bryant. The ground was "Lee's Summit, Raytown and Grandview", chosen because it had the fewest places; it turned out to be worked out (earlier batches lsr, ray, lsb, jcse cover its Register listings), so the session went to the nearest Register listings still missing, in Independence. Less than the 15 to 20 asked for: the Register lists for Jackson, Cass and Johnson (Kansas) counties are now almost all on the map. Sources read: National Park Service place pages (Lewis-Webb, Owens-McCoy), the Santa Fe Trail Historic Sites pages (Lewis Jones, Blue Mills), historical-marker texts on Waymarking (Overfelt-Johnston, Minor, Hughes, Bryant), the City of Independence's list for addresses. Listing years (1975, 1984, 1992, 1994) and Hughes's architects were read from search-result summaries of NPS records, not from the forms, which are not on line (NPGallery gives a placeholder for the 1990s forms; the Missouri office's PDF server answered 503). Brick answers come from the Commons photographs the session looked at. Pins were checked on the aerial (all on the buildings); each address was found with the ArcGIS geocoder. Not checked: interiors, who owns each house now, whether any is open for tours (all are marked view-only).

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Blue Mills (gristmill 1834, sawmill 1835) | Little Blue River, 3101 Lentz Rd, Independence, MO (about 39.1576, -94.3093, an address point only) | Santa Fe Trail provisioning point, mills in ruins by the 1920s (Santa Fe Trail Historic Sites page); on the Register 1994 | Whether anything is visible on the ground, who owns it, where a visitor may stand |
| Bailey Family Farm Historic District | SW corner of Bailey and Ranson Rds, Lee's Summit, MO (38.8958, -94.3414) | Register 2006, Prairie School farm; a realty page says the farmstead is being built over | The nomination text (the state PDF 404s) and what still stands |
| Englewood Theater | 10917 E. Winner Rd, Independence, MO | Opened 1949, Register 2024-25, Streamline Moderne; nonprofit now plans a restoration (JCHS, KSHB) | Left out as possibly mid-century modern under rule 8; the owner may decide |
| Woodson-Sawyer House ("Araby West") | 1604 W. Lexington, Independence, MO | Italianate brick house of about 1866 per its marker (search summary only) | A page of its own to read |
| Georgen House, Smallwood Noland House | 933 S. Main and 1024 S. Forest, Independence, MO | Register 2000 (Craftsman/Prairie) and 1994 (Greek Revival) | Any readable source describing them |
| Howard Neighborhood and other Lee's Summit house districts | Lee's Summit, MO | Register districts of ordinary houses | Not chosen: little to see |

## Tips
- Wikipedia's county Register lists carry no text for 1990s Missouri listings; NPGallery's `_text` files for them are placeholders, and the state PDFs (dnr.mo.gov, mostateparks.com) were not reachable from `page.py`. NPS "places" pages (nps.gov/places/...) exist for Santa Fe Trail houses and read fine; the NPGallery `GetAsset/<uuid>` links that web search returns do give full PDFs for newer forms (Mount Washington School, Lee's Summit districts).
- `photo_find.py new` said "0 wait for a look" for places that had candidates; `look <ids>` still listed them, so run `look` whatever `new` says.
- A Missouri place id can collide with a Kansas file: `mount-washington-school-independence-mo` already sits in data_ks_dglf_xqtb.py. Search every data file for the id before writing.
- The `kcmo` area near Kansas City is largely done; the next session there should try Cass County towns (Peculiar, Archie, Freeman) or Clay and Platte counties outside the cities, or leads from the vanished-places list.
