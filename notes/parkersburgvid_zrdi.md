# parkersburgvid_zrdi: Parkersburg, West Virginia: from a video walk-through
state: West Virginia
region: wv
date: 2026-11-28
places: 13
file: data_parkersburgvid_zrdi.py

## What this batch is
Thirteen places in downtown Parkersburg and its neighbourhoods, from the names in one video of old photographs of the city (job 9, video YFBFlb_i1_k; the record is source/videos/20260731_YFBFlb_i1_k.md; the captions read ran to 34:52 of 35 minutes). Added: the Blennerhassett Hotel, the Wood County Courthouse, Trinity Episcopal, St. Francis Xavier, First Baptist, First Presbyterian (now St. Patrick's Anglican) and First United Methodist churches, the Masonic Temple, the Union Trust Building, the Jackson Memorial Fountain in City Park, the Julia-Ann Square Historic District, the B&O's Parkersburg Bridge over the Ohio (Sixth Street Railroad Bridge) and Parkersburg High School with its 1924 stadium. Sources: Wikipedia as raw text (wiki_raw.py), the National Register records and forms through form.py (Register forms for the hotel, Trinity, the Masonic Temple, the Union Trust, the bridge and the high school district all had a text layer), SAH Archipedia's Buildings of West Virginia entries read with page.py (the Parkersburg essay, node 7082, names what urban renewal took), the 2023 Downtown Parkersburg Historic District nomination PDF on wvculture.org (text layer, 65 pages), the hotel's own page, the parish pages of Trinity (trinity-church.org) and St. Francis Xavier (stx-pburg.org), and Wood County's clerk page for the courthouse hours. Not checked: service times for First Baptist, First Presbyterian/St. Patrick's and First United Methodist (no congregation page found or it would not connect), the hotel's restaurant hours, City Park hours, whether the fountain now standing is the 2020 replica Wikipedia describes (not seen on the ground), and every interior beyond what SAH Archipedia describes. Red brick for the hotel, St. Francis Xavier, First Baptist and the high school comes from the Commons photographs; the Union Trust and First Presbyterian were left unset. The Masonic Temple is three storeys in Wikipedia and four in the 1982 Register form; the fountain is dated 1903 by SAH Archipedia and 1905 by Wikipedia (both entries carry conf mixed).

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Calvary Baptist Church | Parkersburg, WV | Named in the video; no source found | Whether an old building stands, and a source |
| Smoot Theater | downtown Parkersburg, WV | National Register 82001787; SAH Archipedia has an entry (node 22846) | Not read; a likely addition with the theatre's own hours |
| Odd Fellows Lodge (H. Rus Warne, 1897) | 5th Street, Parkersburg, WV | SAH Archipedia node 22848 and the 2023 downtown nomination describe it | Not read in full |
| Oil and Gas Museum (W. H. Smith Hardware Co., 1899) | 119 Third Street, Parkersburg, WV | Register 03000349; the 2023 nomination says it is the museum | Museum hours |
| Blennerhassett Museum of Regional History | 137 Juliana Street, Parkersburg, WV | The 2023 nomination: the Starr Grocery building of 1902, a history centre since 1988 | Hours from the state park's page |
| Old City Building bell and gargoyles | Parkersburg municipal building, WV | News reports say the 1890s City Building's bell and gargoyles are shown in the present municipal building's lobby | A page from the city confirming they are on show, and hours |
| Schools named in the video (Garfield, McKinley, Nash, Park, Willard) and the YMCA | Parkersburg, WV | Names only; the federal names file lists Nash among old school sites | Whether any stands |

## Tips
- SAH Archipedia's Parkersburg entries (sah-archipedia.org/buildings/WV-01-WD<n>, or node/<n>) read in full with page.py --all -n 20000; the text sits after "Terms of Use" in what page.py prints, and the cached page lists the neighbours' node numbers.
- The 2023 Downtown Parkersburg Historic District nomination (wvculture.org/wp-content/uploads/2023/11/WV_WoodCo_DowntownParkersburgHistoricDistrict_Form.pdf) gives a current, building-by-building account of downtown, including which lots are now empty: read it with page.py --all -n 400000 and grep.
- fumcparkersburg.org would not connect.
