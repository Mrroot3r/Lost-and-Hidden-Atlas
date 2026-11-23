# November 23, 2026: Westport, Midtown and the Country Club Plaza, Kansas City, Missouri.
# Part of filling in the Kansas City area on purpose for a local researcher. Facts come from the linked sources only:
# Wikipedia read as raw text, the Missouri State Parks hours page and the Wornall/Majors museums' own page (both read in full),
# the National Park Service page for the Majors house, and web search results that quote the Westport Historical Society's page.
# National Register forms were not read. Wikipedia and register coordinates were checked against the aerial before the build.
from data_b import N
from data_ma import W

BATCH = {'key': 'kcmo_wpt_dnvk', 'label': 'Kansas City: Westport and Midtown', 'added': '2026-11-23 15:50'}

NRL = ['Wikipedia: National Register listings in Kansas City, Missouri (Jackson County, outside downtown)', 'https://en.wikipedia.org/wiki/National_Register_of_Historic_Places_listings_in_Jackson_County,_Missouri:_Kansas_City_other']

PLACES = [
N('kellys-westport-inn-kc', "Kelly's Westport Inn", 'Kansas City', 'kcmo', 'hotel', 'standing',
  39.05304, -94.59179, 'exact', 'open', 'drive', '', '1850',
  "Wikipedia dates this Westport building to about 1850 and calls it, with the adjoining Chouteau Store, one of the oldest buildings standing in Kansas City; it adds that Mabry Hall on Pennsylvania Avenue is seven years older. A 2016 National Trust feature gives 1850 and says it is believed to be the oldest building in the city, while some sources say 1851. "
  "Albert Gallatin Boone, a grandson of Daniel Boone, ran a store here. A story that a tunnel here was part of the Underground Railroad is denied by Wikipedia, which says the tunnel only joins two basements. It has been a saloon since the end of Prohibition. The Register listing is from 1972.",
  look="The old store front on Westport Road, now a bar. Whether anything of the 1850 interior survives was not checked.",
  hook="A bar in a store that Boone's grandson ran in 1850, in the old trail town of Westport.",
  accn="A working bar at 500 Westport Road, owned privately; go in as a customer. A 2016 listing gives 11 a.m. to 3 a.m. daily, but no page of the bar itself was read, so hours are not given. Parking is on the streets and lots of Westport.",
  links=[W("Kelly's Westport Inn"), ['National Trust for Historic Preservation: Kelly\'s Westport Inn', 'https://savingplaces.org/stories/kellys-westport-inn-in-kansas-city-missouri'], NRL],
  conf='mixed', brick='?', hours='?'),

N('harris-kearney-house-westport-kc', 'Harris-Kearney House (Col. John Harris House)', 'Kansas City', 'kcmo', 'landmark', 'standing',
  39.05406, -94.58784, 'exact', 'open', 'drive', '', '1855',
  "Colonel John Harris built this Greek Revival house in 1855 on Westport Road, next to the Harris House Hotel, and Wikipedia calls it the oldest brick residence in Kansas City. The hotel was used as Union headquarters in the Battle of Westport in 1864 and was torn down in 1922. "
  "That year a group of women, forerunners of the Daughters of Old Westport, bought the house for $1,000 and had it moved to 4000 Baltimore Avenue, where the side portico was lost. The Westport Historical Society bought it in 1976, restored it to its 1855 look and opened it as a museum in 1985.",
  look="A furnished 1855 house museum, with period furniture and items from the Harris and Kearney families. Its original position was at Westport Road and Main Street; it stands now on Baltimore Avenue.",
  accn="Run by the Westport Historical Society at 4000 Baltimore Avenue. Its own page (read as a search result quotes it) gives regular tours on Fridays and Saturdays from 1 to 5 p.m., last tour 4:15, but ties that to pandemic rules and sends readers to its Facebook page for current hours; a visitor-bureau listing gives weekends 1 to 4. Private tours on request: 816-561-1821. Street parking.",
  links=[W('Harris-Kearney House'), ['Westport Historical Society', 'https://www.westporthistorical.com/'], NRL],
  conf='mixed', brick='yes', hours="Tours Fri and Sat 1-5, last tour 4:15 (society's page, dated; check its Facebook page)"),

N('alexander-majors-house-kc', 'Alexander Majors House', 'Kansas City', 'kcmo', 'landmark', 'standing',
  38.97957, -94.60751, 'exact', 'open', 'drive', '', '1856',
  "Alexander Majors built this frontier mansion in 1856, at the edge of the United States. His 300-acre farm was cut by the state line, and the National Park Service says the part beyond the line was outside US jurisdiction and untaxed. "
  "It was the home of the Majors family and a base of Russell, Majors and Waddell, the freighting firm that hauled goods for the army and helped found the Pony Express. The firm failed and Majors lost his fortune. It is on the National Register and is run, with the Wornall House, by the Wornall/Majors House Museums.",
  look="A frontier house museum. Tours are the way in; ghost tours and barn showings are also offered.",
  accn="Museum at 8201 State Line Road, run by the nonprofit Wornall/Majors House Museums. Its page gives May to October, Saturday and Sunday 1 to 5 p.m. without an appointment and other times by appointment; November to April by appointment only. Tours are $8 a person. Parking not checked.",
  links=[['Wornall/Majors House Museums: the Alexander Majors House', 'https://wornallmajors.org/explore/the-alexander-majors-house/'], ['National Park Service: Alexander Majors House', 'https://www.nps.gov/places/alexander-majors-house.htm'], NRL],
  conf='mixed', brick='?', hours='May-Oct Sat and Sun 1-5, no appointment; Nov-Apr by appointment (museum page)'),

N('thomas-hart-benton-home-kc', 'Thomas Hart Benton Home and Studio', 'Kansas City', 'kcmo', 'landmark', 'standing',
  39.06220, -94.59788, 'exact', 'open', 'drive', '', 'c. 1903',
  "The limestone house in Roanoke was built about 1903 for Walter Kirkpatrick of the Kansas City Electric Light Company, designed by George Mathews. It has 24 rooms on three floors. The painter Thomas Hart Benton's family bought it in 1939 for $6,000, and he lived and worked here until he died in 1975. "
  "Missouri made it a state historic site in 1977, kept as he left it; it was listed on the Register in 1980.",
  look="A fortress-like rough-cut limestone front above the street, and the working studio where Benton painted. Tours show the furnished first and second floors and the studio.",
  accn="State historic site, Missouri State Parks, 3616 Belleview Avenue; phone 816-931-5722. Inside only on a 45-minute guided tour, booked online or at the visitor center (groups of 15 or more call two weeks ahead). Grounds and visitor center 10 to 4 Monday and Thursday to Saturday, 11 to 4 Sunday; closed Tuesday and Wednesday and on state holidays. The state's page gives tour times (Sunday from 11; no tours Monday in winter).",
  links=[W('Thomas Hart Benton Home and Studio State Historic Site'), ['Missouri State Parks: facility hours', 'https://mostateparks.com/hours/931/historic-site/thomas-hart-benton-home-and-studio-state-historic-site'], NRL],
  conf='mixed', brick='?', hours='Visitor center Mon, Thu-Sat 10-4, Sun 11-4; guided tours only, none Tue and Wed (Mon tours Apr-Oct only)', th=None),

N('mineral-hall-kc', 'Mineral Hall (Kansas City Art Institute)', 'Kansas City', 'kcmo', 'landmark', 'standing',
  39.04775, -94.58226, 'exact', 'view', 'drive', '', '1903–1904',
  "Louis S. Curtiss, a Kansas City architect born in Canada, designed this Prairie School house with Second Empire, Art Nouveau and neoclassical touches. It took fourteen months to build for William A. Rule, who never lived in it; Roland Bruner bought it in 1905. "
  "A matching addition on the north followed the next year. The building was given to the Kansas City Art Institute in 1968 and was listed on the Register in 1976.",
  look="Rock-faced Jackson County limestone walls in a random pattern, a stone veranda and seven wide stone steps up to an arched entrance on Oak Street. Interior not checked.",
  accn="On the Kansas City Art Institute campus at 4340 Oak Street, owned by the college. Look from the sidewalk; no page about visiting inside was read. Street parking.",
  links=[W('Mineral Hall'), NRL],
  conf='mixed', brick='no', hours=''),

N('seth-ward-homestead-kc', 'Seth E. Ward Homestead', 'Kansas City', 'kcmo', 'landmark', 'standing',
  39.02833, -94.60167, 'site', 'view', 'drive', '', '1871',
  "Wikipedia describes a two-story, T-plan Greek Revival brick house of 1871, designed by Asa Beebe Cross, with a one-story porch across the front. It was a home of Seth E. Ward, and is also known as the Frederick B. Campbell Residence. It was listed on the Register in 1979. "
  "The Register's coordinate is used for the pin and may not sit exactly on the house.",
  look="A plain brick farmhouse with a full-width veranda, surrounded by the later houses of the Country Club District. Interior not checked.",
  accn="Private property in the Country Club District; no source says it opens to the public. Look from the street only and respect the residents. Parking not checked.",
  links=[W('Seth E. Ward Homestead'), NRL],
  conf='mixed', brick='yes', hours=''),

N('bernard-corrigan-house-kc', 'Bernard Corrigan House', 'Kansas City', 'kcmo', 'landmark', 'standing',
  39.02880, -94.60451, 'exact', 'view', 'drive', '', '1912–1913',
  "Bernard Corrigan, a contractor and streetcar owner, hired Louis S. Curtiss to build this Prairie Style house at 55th Street and Ward Parkway; his own firm built it. It is one of the first Kansas City houses to use reinforced concrete widely. Corrigan died in January 1913, two months before he was to move in. "
  "Later owners were the brewer Joseph Heim, from 1917, and the lumberman Robert Sutherland, from 1923, whose widow stayed on. It was listed on the Register in 1978.",
  look="Gray shot-sawn Carthage limestone over a reinforced concrete frame, strong horizontal lines, and art glass in windows and doors; inside, two stained-glass walls in the hall and a two-story ceiling with oak beams, as Wikipedia describes. Whether the public can see the inside was not checked.",
  accn="Private, at 1200 West 55th Street; present use not checked. Look from the street. Parking not checked.",
  links=[W('Bernard Corrigan House'), NRL],
  conf='mixed', brick='no', hours=''),

N('uptown-theater-kc', 'Uptown Theater', 'Kansas City', 'kcmo', 'civic', 'standing',
  39.06086, -94.59120, 'exact', 'view', 'drive', '', '1926–1928',
  "The shops and offices along Broadway were finished in November 1926; work on the theater stopped until Universal bought the building in 1927 and brought in the designer John Eberson. It opened on January 6, 1928, as an \"atmospheric\" theater: the inside copies a Mediterranean courtyard, with a night-sky ceiling of stars, clouds and mechanical flying birds. "
  "It showed films and stage acts until it closed in 1989 over unpaid taxes, its detail whitewashed. A $15 million restoration after 1994 brought the details and colors back. It is now a concert venue and one of the few atmospheric theaters still working. Register listing 1979.",
  look="The restored courtyard-style auditorium, seen at a show; the front of the main floor is now open standing and tables, and the balcony keeps permanent seats.",
  accn="A working concert venue at 3700 Broadway; the building is open to ticket holders on show nights. No page of the venue was read, so no daytime hours are given. Parking is on the surrounding streets.",
  links=[W('Uptown Theater (Kansas City, Missouri)'), NRL],
  conf='mixed', brick='?', hours=''),

N('kansas-city-athenaeum-kc', 'Kansas City Athenaeum (Delta Athenaeum)', 'Kansas City', 'kcmo', 'civic', 'standing',
  39.06917, -94.57389, 'site', 'view', 'drive', '', '1914',
  "A women's club of more than 500 members built this clubhouse at Linwood Boulevard and Campbell Street, reached by three streetcar lines. Members raised $50,000 by selling $5 shares, canned vegetables and needlework, charging husbands a nickel to iron a shirt, and staging operettas. The architect was Samuel Tarbet. It opened on June 3, 1914. "
  "The club met here for 101 years, then sold the building in 2015 to Delta Sigma Theta sorority, which calls it the Delta Athenaeum; the name is cut in the stone. Register listing 1979.",
  look="A second-floor ballroom with six stained glass windows, and a kitchen and dining hall on the ground floor, as Wikipedia describes. Whether they survive unchanged was not checked.",
  accn="Owned by the sorority; no source says visitors may go in. Look from the street. Parking not checked.",
  links=[W('Kansas City Athenaeum'), NRL],
  conf='mixed', brick='?', hours=''),

N('loretto-academy-kc', 'Loretto Academy (The Loretto)', 'Kansas City', 'kcmo', 'civic', 'standing',
  39.05645, -94.60026, 'exact', 'view', 'drive', '', '1904',
  "The Sisters of Loretto came to Kansas City in 1899 and bought this land in 1902; the academy, a boarding and day school for girls, was dedicated in 1904. Its architect, Thomas P. Barnett, soon after became architect of the Cathedral Basilica of St. Louis. Three students died here in a fire in 1909 when a paper costume caught fire at a Halloween party. "
  "It took its first black student in 1947 and left for Wornall Road in 1966. A Bible college used the building for two decades; it was listed on the Register in 1983 and now hosts weddings in its chapel and ballroom, with apartments and offices.",
  look="A big school building with a cathedral-style chapel, now a wedding venue. Wikipedia's note on redevelopment plans is from 2011, so what has been built since was not checked.",
  accn="Private venue near West 39th Street and Mercier; inside only for events and tenants. Look from the street. Parking not checked.",
  links=[W('Loretto Academy (Kansas City, Missouri)'), NRL],
  conf='mixed', brick='?', hours=''),

N('westport-high-school-kc', 'Westport High School (Residences at Park 39)', 'Kansas City', 'kcmo', 'civic', 'standing',
  39.05595, -94.58199, 'exact', 'view', 'drive', '', '1907–1908',
  "The cornerstone was laid on June 8, 1907, and the school opened in fall 1908 beside the older Westport middle school. Wikipedia says it cost nearly $500,000 and was thought the finest in the city; it is built of stone and vitrified brick. "
  "Westport High closed on June 3, 2010 in a district plan to close about 30 schools. It was listed on the Register in 2015 and in April 2024 reopened as the Residences at Park 39, 138 apartments, in a 16-acre development.",
  look="A large red-brick school with stone trim (a photograph on Wikimedia Commons shows red brick walls), now apartments. Whether anything of the school's interior was kept was not checked.",
  accn="Private apartments at 315 East 39th Street; look from the street. Parking not checked.",
  links=[W('Westport High School (Missouri)'), NRL],
  conf='mixed', brick='yes', hours=''),

N('newbern-hotel-kc', 'Newbern Hotel', 'Kansas City', 'kcmo', 'hotel', 'standing',
  39.06332, -94.57904, 'exact', 'view', 'drive', '', '1921–1923',
  "Ernest Brostrom designed this Sullivanesque building for the Armour Building Company; J. O. Jones built it from 1921 to 1923. It was meant to be called Le Pavonien and opened as the Peacock Hotel; Beine Hopkins bought it and renamed it the Newbern in 1925. "
  "Two nine-story towers are joined by a one-story barrel-vaulted hall, and one tower has a curved corner at Armour Boulevard and Cherry Street. Register listing 1980.",
  look="The U-shaped plan with its barrel-vaulted hall between two towers, and Sullivanesque ornament on the walls. Interior not checked.",
  accn="At 525 East Armour Boulevard; present use not checked. Look from the street. Parking not checked.",
  links=[W('Newbern Hotel'), NRL],
  conf='mixed', brick='?', hours=''),

N('sophian-plaza-kc', 'Sophian Plaza', 'Kansas City', 'kcmo', 'hotel', 'standing',
  39.04260, -94.58332, 'exact', 'view', 'drive', '', '1922–1923',
  "Harry Sophian built this eight-story Beaux-Arts apartment hotel, designed by Charles Shepard of Shepard and Wiser, in 1922 and 1923 to match the big houses of Southmoreland. It is H-shaped and free-standing so every side shows, with a colonnaded entrance facing Southmoreland Park. "
  "The Kansas City Star called it an imposing Italian-style high-rise on its opening day, February 24, 1923. It is now a condominium building.",
  look="A colonnaded entry and landscaped grounds facing Southmoreland Park. Interior not checked.",
  accn="Private condominiums at 4618 Warwick Boulevard; look from the street or the park. Parking not checked.",
  links=[W('Sophian Plaza'), NRL],
  conf='mixed', brick='?', hours=''),

N('raphael-hotel-kc', 'Raphael Hotel (Villa Serena Apartments)', 'Kansas City', 'kcmo', 'hotel', 'standing',
  39.03968, -94.59125, 'exact', 'open', 'drive', '', '1928',
  "It opened in 1928 as the Villa Serena, luxury apartments in Italian Renaissance Revival style, chosen to go with the Spanish look of the new Country Club Plaza. The J. C. Nichols Company bought it in 1974 and reopened it in 1975 as a 126-room hotel patterned on small European hotels. "
  "It has belonged to Historic Hotels of America since 2001 and was listed on the Register in 2009.",
  look="Nine stories of Italian Renaissance Revival, a few steps from the Plaza. Interior not checked.",
  accn="A working hotel at 325 Ward Parkway; its restaurant and lobby are the places a non-guest can go. Its page was not read, so hours are not given. Parking not checked.",
  links=[W('Raphael Hotel'), ['Raphael Hotel (official site)', 'https://www.raphaelkc.com'], NRL],
  conf='mixed', brick='?', hours='?'),

N('community-christian-church-kc', 'Community Christian Church (Frank Lloyd Wright)', 'Kansas City', 'kcmo', 'worship', 'standing',
  39.04323, -94.58639, 'exact', 'open', 'drive', '', '1940–1942',
  "The congregation asked Frank Lloyd Wright in April 1940 for a church to replace one lost to fire. He planned a parallelogram with a \"spire of light\"; high costs shrank the auditorium from 1,200 to 900 seats, details were dropped, and the walls were sprayed with gunite over his objections. It was dedicated on January 4, 1942. "
  "The Steeple of Light was only finished in 1994, by the artist Dale Eldred's partner Roberta Lord, and is lit on Fridays, Saturdays and Sundays. It is across from the Plaza.",
  look="A Wright design in gunite with a parallelogram plan; the Steeple of Light in a perforated dome on the northwest corner. Wikipedia says walk-in tours are free and guided tours can be arranged two weeks ahead.",
  accn="Church at 4601 Main Street. Wikipedia and a search summary of third-party listings disagree on days and times for walk-in visits, and the church's own pages were not read, so hours are not given; call ahead. Parking not checked.",
  links=[W('Community Christian Church (Kansas City, Missouri)'), NRL],
  conf='mixed', brick='no', hours='?'),

N('pink-house-hook-kc', 'Pink House (Mary Rockwell Hook)', 'Kansas City', 'kcmo', 'landmark', 'standing',
  39.03667, -94.59639, 'site', 'view', 'drive', '', '1922',
  "Mary Rockwell Hook, a pioneer woman architect who worked mostly from Kansas City, designed this house, built in 1922. Its pink plaster refers to San Francisco, whose 1915 world's fair she had visited. It has two stories, stucco walls, red clay tile roofing, three balconies and a brick chimney with an arcaded, roofed opening. "
  "Register listing 1983, one of several Hook houses in the Sunset Hill area. The Register's coordinate is used for the pin.",
  look="Pink stucco, red tile roof, balconies and a decorated chimney on a residential street. Interior not checked.",
  accn="A private house; no source says it opens. Look from the street. Parking not checked.",
  links=[W('Pink House (Kansas City, Missouri)'), W('Mary Rockwell Hook'), NRL],
  conf='mixed', brick='some', hours=''),
]

PIN_NOTES = {
 'kellys-westport-inn-kc': 'Street address 500 Westport Road, geocoded; to be checked on the aerial.',
 'harris-kearney-house-westport-kc': 'Street address 4000 Baltimore Avenue, geocoded; the house stands here, not at its 1855 site.',
 'alexander-majors-house-kc': 'Street address 8201 State Line Road, geocoded.',
 'thomas-hart-benton-home-kc': 'Street address 3616 Belleview Avenue, geocoded.',
 'mineral-hall-kc': 'Street address 4340 Oak Street, geocoded.',
 'seth-ward-homestead-kc': 'Register and Wikipedia coordinate; the street address was not found in a source read.',
 'bernard-corrigan-house-kc': 'Street address 1200 West 55th Street, geocoded.',
 'uptown-theater-kc': 'Street address 3700 Broadway, geocoded.',
 'kansas-city-athenaeum-kc': 'Wikipedia coordinate at Linwood Boulevard and Campbell Street.',
 'loretto-academy-kc': 'The Register coordinate, which falls on the large school building south of the street; the geocoded street address was a point on the road.',
 'westport-high-school-kc': 'Street address 315 East 39th Street, geocoded.',
 'newbern-hotel-kc': 'Street address 525 East Armour Boulevard, geocoded.',
 'sophian-plaza-kc': 'Street address 4618 Warwick Boulevard, geocoded.',
 'raphael-hotel-kc': 'Street address 325 Ward Parkway, geocoded.',
 'community-christian-church-kc': 'Street address 4601 Main Street, geocoded.',
 'pink-house-hook-kc': 'Register and Wikipedia coordinate; no street address in a source read.',
}
