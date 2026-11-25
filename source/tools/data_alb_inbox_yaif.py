# November 25, 2026: the daily inbox run. One Albany church that a reader marked on the map through the Atlas's form on
# November 24, 2026 with the single word "Church". The sources that say what it is were opened in this session: the
# parish's own history page and home page (read whole with tools/page.py --all) and The Evangelist's article on the
# parish centennial (dated 2002 at its foot, posted on the paper's site in 2018; read whole). Not checked: the architect,
# what the church is built of (The Evangelist mentions repairs to its stone; no picture was found on Wikimedia Commons), and the interior beyond what the parish says.
from data_b import N
def L(t,u): return [t,u]
BATCH={'key':'alb_inbox_yaif','label':'Albany: a church a reader marked','added':'2026-11-25 05:19'}
BSH=L('Church of the Blessed Sacrament: History & Archives','https://blessedsacramentalbany.org/history')
BSP=L('Church of the Blessed Sacrament: parish home page (Mass times, church hours)','https://blessedsacramentalbany.org/')
EVA=L('The Evangelist: Albany parish marks 100 years of being blessed','https://evangelist.org/news/2018/apr/06/albany-parish-marks-100-years-of-being-blessed')
PLACES=[
N('church-of-the-blessed-sacrament-albany','Church of the Blessed Sacrament, Central Avenue','Albany','alb','worship','standing',42.67362,-73.78186,'exact','open','drive','','1902–1903',
  'A Gothic Roman Catholic church on Central Avenue in Albany\'s West End, founded in 1902 for Catholic families moving out to work in the railroad shops of West Albany. The parish was incorporated on September 11, 1902; the parish says the church was built that year with a temporary rear wall, and The Evangelist that the bishop dedicated it a year later, calling it one of the prettiest in the diocese. Its stained glass was made in 1910 by Franz Mayer of Munich, and in 1952 the back wall came out for a new sanctuary, an altar with a baldacchino and two side chapels. The parish now keeps the records and some statues of several closed Albany parishes. A reader marked it on the map on November 24, 2026.',
  'From Central Avenue: the Gothic church, with the parish school beside it. Inside, the parish says, are the 1910 Mayer of Munich windows, a marble crucifix and statues from the high altar of St. Joseph\'s Church in Ten Broeck Triangle, and a pulpit from St. Lawrence\'s in Troy; the 1952 baldacchino stands over the altar. The church is open every day for private prayer (see Hours).',
  'A railroad-shop parish\'s 1902 Gothic church, glazed by Mayer of Munich in 1910.',
  'An active Roman Catholic parish church, 607 Central Avenue (Diocese of Albany). Visitors may come in for private prayer in the daily open hours or for Mass; the parish office is open weekdays. Park on Central Avenue or the side streets where the signs allow. Hours from the parish home page, read November 2026.',
  [BSH,BSP,EVA],brick='?',tip='2026-11-24',
  hours='Open daily 7 a.m.–2 p.m. Mass Sat 4 p.m.; Sun 9 a.m. (6 p.m. in Urdu); Mon 7 a.m., Tue & Thu noon, Wed 9 a.m. on school days'),
]
PIN_NOTES={
 'church-of-the-blessed-sacrament-albany':'On the church roof, seen on the New York leaf-off aerial, in OpenStreetMap\'s building for 607 Central Avenue, named Church of the Blessed Sacrament; the reader\'s point, 42.67358, -73.78187, is 4 m away on the same roof.',
}
