# November 21, 2026: the daily inbox run. Two Albany buildings that readers marked on the map through the Atlas's form on
# November 20, 2026, with a word or two each; the sources that say what they are were opened in this session: the
# Woman's Club of Albany's own history page (read whole with tools/page.py --all), Wikipedia's article on the Washington
# Park Historic District (tools/wiki_raw.py), and two University at Albany pages on the former Albany High School (the
# May 2024 news release, read whole, and the facilities project page, node 98251). Not checked: either interior beyond what the
# university's release describes, and whether the club opens its house to visitors outside rentals and members' events.
# A third mark that day, a house on the south side of Madison Avenue, went to the note's Leads table (no source names it).
from data_b import N
from data_ma import W
def L(t,u): return [t,u]
BATCH={'key':'alb_inbox_ugzq','label':'Albany: two buildings readers marked','added':'2026-11-21 20:49'}
WCA=L('Woman\'s Club of Albany: club history and the house','https://woman39sclubofalbany2.wildapricot.org/History')
UAHS=L('University at Albany: CNSE opens in the renovated former Albany High School (May 21, 2024)','https://www.albany.edu/news-center/news/2024-ualbany-unveils-new-cnse-building-renovated-former-albany-high-school')
UAFP=L('University at Albany: Renovate Former Albany High School Building (Bldg 523), Phases 4-6','https://www.albany.edu/node/98251')
PLACES=[
N('womans-club-of-albany','Woman\'s Club of Albany (Joseph Steefel house)','Albany','alb','landmark','standing',42.65843,-73.77763,'exact','view','walk','','1895',
  'A three-story brick house of 1895 on Madison Avenue facing Washington Park, built for Joseph and Hattie Steefel; Joseph and his brother Barnard owned Steefel\'s clothing store on State Street, and Barnard built the twin house next door. Both were designed by Nolan, Nolan and Stern of Rochester. The Woman\'s Club of Albany, founded in 1910 as a civic reform club, bought the house in 1919; by 2003 only three elderly members were left and the house had fallen into disrepair, and a new group revived the club from 2004. Both Steefel houses are in the Washington Park Historic District.',
  'From the Madison Avenue sidewalk or the park across the street: the club house and its twin side by side on the north side of Madison, just east of South Lake Avenue. Interior not checked; the club hires out its rooms for events.',
  'Twin brick houses of two clothing-store brothers, one a women\'s reform club for over a century.',
  'Owned by the Woman\'s Club of Albany, a private club; see it from the street. Washington Park, a public city park, is across Madison Avenue. Park on the street where the signs allow.',
  [WCA,W('Washington Park Historic District (Albany, New York)')],brick='?',tip='2026-11-20'),
N('former-albany-high-school-western-avenue','Former Albany High School (Philip Schuyler Hall), Western Avenue','Albany','alb','civic','standing',42.66137,-73.77305,'exact','view','walk','','1912–1913',
  'A block-long Neo-Classical school on Western Avenue at North Lake Avenue. The university\'s facilities page says it was built in 1912 and its 2024 release that it opened in 1913; it was Albany High School until 1974, then held Philip Schuyler Elementary School and other programs. The University at Albany bought it from the city school district in 2013 and has turned it into the home of its College of Nanotechnology, Science, and Engineering; the south wing reopened in May 2024 and the auditorium is to be finished in 2027.',
  'Seen from Western Avenue and North Lake Avenue. The renovation shortened the grand staircase on Western Avenue and put in more than 430 new windows; the new main entrance is on the east side, facing the rest of the Downtown Campus. Inside, the university says, the Guastavino tile ceilings of the first-floor central corridor and the old library\'s leather doors were kept. Not open to the public as a visitor site.',
  'Albany\'s 1913 high school, emptied for a decade, now an engineering college.',
  'Owned by the University at Albany (Downtown Campus). See it from the sidewalks of Western Avenue and North Lake Avenue. The campus lots are the university\'s; park on the street where the signs allow.',
  [UAHS,UAFP],brick='?',tip='2026-11-20'),
]
PIN_NOTES={
 'womans-club-of-albany':'OpenStreetMap\'s building for 725 Madison Avenue, named Women\'s Club of Albany: 42.65843, -73.77763. The reader\'s point, 42.65852, -73.77767, is 10 m north, on the same building.',
 'former-albany-high-school-western-avenue':'OpenStreetMap\'s building at 141 Western Avenue, named Philip Schuyler Hall with the old name Albany High School, has its point at 42.66111, -73.77321, at the south front by the Western Avenue plaza; moved 31 m north onto the roof on the leaf-off aerial (tools/pix.py). The reader\'s point, 42.66145, -73.77308, is 9 m from it, on the same building.',
}
