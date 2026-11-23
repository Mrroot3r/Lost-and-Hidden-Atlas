# lowell_uwrz: Massachusetts: old Lowell, City Hall, churches and the buildings round them
state: Massachusetts
region: nshore
date: 2026-11-23
places: 15
file: data_lowell_uwrz.py

## What this batch is
Fifteen standing buildings in Lowell, where the Atlas had only the canal system: City Hall, the Pollard Memorial Library, the Memorial Auditorium, the 1893 post office (now a juvenile court) and the 1932 post office (Morse Federal Building), St. Patrick's, Immaculate Conception, St. Anne's Episcopal, First United Baptist, the former St. Jean Baptiste (bought in 2025 for a Kerouac center) and St. Michael churches, the old county jail (Keith Academy, now condominiums), Lowell Cemetery with the Talbot Chapel, the 1876 Boston & Maine depot (now Middlesex Community College's arts center) and Coburn Hall of the Lowell Normal School. The names came from one video (job 9, the record is source/videos/20241213_DUZf0QKiyOw.md); every fact is from a source opened here. Sources: Wikipedia, the City of Lowell Historic Board's pages, the Doors Open Lowell one-page building histories (PDFs), the National Park Service's St. Anne's page, Lost New England (jail), WBUR and GBH (St. Jean Baptiste), and the parishes', library's, cemetery's and city's own pages for hours. Not checked: Mass or service times for St. Patrick's, St. Anne's and First United Baptist (no page of their own read); the cemetery's daily hours; the depot's and the Morse building's opening hours; inside every building. Sources disagree on the Immaculate Conception's date (1868 against 1871–1877) and on the old post office's (1893 against 1895), and both are given. The jail pin is the 201 Thorndike Street address point, one of three numbers the condominiums use; that it sits on the old jail itself was not proved on a picture. Brick from the Commons photographs chosen: only the depot is red brick.

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| J. C. Ayer & Company laboratory | Lowell, MA (165 Market Street) | Patent-medicine works from 1859 to 1917; in the City Hall Historic District (City of Lowell Historic Board) | What the Market Street building is now and whether it stands; HMdb marker 117899 answered 403 |
| Masonic Temple | Lowell, MA (79 Dutton Street) | Built 1928, still the Masons' hall, Grecian and Egyptian halls inside (Doors Open Lowell sheet) | Whether it opens other than on Doors Open days |
| Lowell Textile School (Southwick Hall) | Lowell, MA (UMass Lowell north campus) | Named in the video | Any source read |
| Hildreth Building | Lowell, MA (Merrimack Street) | Named in the video as standing | Any source read |

## Tips
- Doors Open Lowell's one-page building histories read cleanly with `page.py`: `https://doorsopenlowell.org/s/<Name>-DOL-2024.pdf`; guessed names fail, so take the link from a web search (St. Anne's, St. Patrick, Coburn Hall, Masonic Temple, First-United, Boston-and-Maine-Depot worked).
- The City of Lowell Historic Board has a page for each individually listed building (`lowellma.gov/984` lists them in its margin) with dates and later uses.
- `page.py` on a PDF failed with a `_cffi_backend` error after setup installed `pypdf`; `pip install --ignore-installed cffi cryptography` fixed it.
- richardhowe.com and hmdb.org answered 403 to `page.py`.
