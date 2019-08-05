import sqlite3

class Athlete():
    def __init__(self, first, last, school, gender, grad_year=None, athlete_id = None):
        self.first = first
        self.last = last
        self.school = school
        self.gender = gender
        self.grad_year = grad_year
        self.athlete_id = athlete_id

    def to_database(self, c):
        if self.athlete_id is None:
            self.athlete_id = get_next_athlete_id(c)
        c.execute("""INSERT INTO athletes VALUES(?,?,?,?,?,?)""",(self.first, self.last, self.school, self.athlete_id, self.gender, self.grad_year))

    def get_athlete_id(self):
        return self.athlete_id

    def __str__(self):
        return first + " " +last + ", " + school + ", " + grad_year

    def get_school(self):
        return self.school


events = {"60m":'s', '100m' : 's', '200m' : 's', '400m' : 's', '800m' : 's', '1500m' : 's', 'mile' : 's', '3000m' : 's',
    '5000m' : 's', '10000m' : 's', '60h' : 's', '100h' : 's', '110h' : 's', '400h' : 's', '3000sc' : 's', 'lj' : 'm',
    'hj' : 'm', 'tj' : 'm', 'sp' : 'm', 'wt' : 'm', 'disc' : 'm', 'jav' : 'm', 'pv' : 'm', 'ht' : 'm'}

class Performance():
    def __init__(self, event, mark, athlete_id, date, meet_id):
        self.event = event
        self.mark = mark
        self.athlete_id = athlete_id
        self.date = date
        self.meet_id = meet_id

    def to_database(self, c):
        c.execute("""INSERT INTO performances VALUES(?,?,?,?,?)""",(self.event, self.mark, self.athlete_id, self.date, self.meet_id))


class Meet():
    def __init__(self, meet_id, meet_name, date):
        self.meet_id = meet_id
        self.meet_name = meet_name
        self.date = date

    def to_database(c):
        if self.meet_id is None:
            self.meet_id = get_next_meet_id(c)
        c.execute("""INSERT INTO meets VALUES(?,?,?)""",(self.meet_id, self.meet_name, self.date))

def get_next_athlete_id(c):
    next = c.execute("""SELECT athlete_id FROM athletes ORDER BY athlete_id DESC""").fetchone()
    if next is None:
        return 1
    else:
        return next[0] +1

def get_next_meet_id(c):
    next = c.execute("""SELECT meet_id FROM meets ORDER BY athlete_id DESC""").fetchone()
    if next is None:
        return 1
    else:
        return next[0] +1

def get_athlete_school(c, id):
    return c.execute("""SELECT school FROM atheletes WHERE athlete_id =?""",(id,)).fetchone()[0]

def get_all_athletes(c):
    return c.execute("""SELECT * FROM athletes""").fetchall()


def get_athletes_by_school(c, school):
    return c.execute("""SELECT * FROM athletes WHERE school=?""",(school,)).fetchall()


def get_athletes_by_name(c, first, last):
    return c.execute("""SELECT * FROM athletes WHERE first=? AND last=?""",(first,last)).fetchall()

def get_athletes_by_name_school(c, first, last, school):
    return c.execute("""SELECT * FROM athletes WHERE first=? AND last=? AND school=?""",(first,last, school)).fetchall()

def get_performances_by_athlete(c, id):
    return c.execute("""SELECT * FROM performances WHERE athlete_id=? ORDER BY event ASC""",(id,)).fetchall()

def get_event_pr(c, id, event):
    if events[event] == "s":
        return c.execute("""SELECT mark FROM performances WHERE athlete_id=? AND event=? ORDER BY mark ASC""",(id,event)).fetchone()[0]
    else:
        return c.execute("""SELECT mark FROM performances WHERE athlete_id=? AND event=? ORDER BY mark DESC""",(id,event)).fetchone()[0]

def get_all_for_event(c, id, event):
    return c.execute("""SELECT mark FROM performances WHERE athlete_id=? AND event=? ORDER BY mark DESC""",(id,event)).fetchall()

def drop_tables():
    conn = sqlite3.connect('example.db')
    c = conn.cursor()
    c.execute("""DROP TABLE athletes""")
    c.execute("""DROP TABLE performances""")
    c.execute("""DROP TABLE meets""")
    conn.commit()
    conn.close()

def create_tables():
    conn = sqlite3.connect('example.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS athletes (first text , last text, school text, athlete_id int, gender text, grad_year int)''')
    c.execute("""CREATE TABLE IF NOT EXISTS performances (event text, mark float, athlete_id int, our_date date, meet_id int)""")
    c.execute("""CREATE TABLE IF NOT EXISTS meets (meet_id int, meet_name text, our_date date)""")
    conn.commit()
    conn.close()

if __name__ == "__main__":
    drop_tables()
    create_tables()
    conn = sqlite3.connect('example.db')
    c = conn.cursor()
    elizabeth = Athlete("elizabeth", "weeks", "MIT", "F", 2021)
    katie = Athlete("katie", "williams", "MIT", "F", 2021)
    summer = Athlete("summer-solstice", "thomas", "Williams", "F", 2020)
    elizabeth.to_database(c)
    katie.to_database(c)
    summer.to_database(c)
    p1 = Performance('tj', 11.53, 1, '2019-04-28', 1)
    p1.to_database(c)
    p2 = Performance('100h', 24.20, 1, '2019-04-28', 1)
    p2.to_database(c)
    p3 = Performance('100h', 15.50, 3, '2019-04-28', 1)
    p3.to_database(c)
    p4 = Performance('800m', 130.0, 2, '2019-04-28', 1)
    p4.to_database(c)
    p5 = Performance('tj', 11.20, 1, '2019-05-28', 2)
    p5.to_database(c)
    p6 = Performance('tj', 10.53, 2, '2019-04-28', 1)
    p7 = Performance('tj', 10.75, 2, '2019-03-28', 4)
    p6.to_database(c)
    p7.to_database(c)
    p8 = Performance('tj', 11.03, 3, '2019-04-28', 1)
    p9 = Performance('tj', 10.78, 3, '2019-03-28', 4)
    p8.to_database(c)
    p9.to_database(c)

    print(get_next_athlete_id(c))
    print(get_all_athletes(c))
    print(get_athletes_by_school(c, "MIT"))
    print(get_athletes_by_school(c, "Williams"))
    print(get_event_pr(c, 1, 'tj'))
    print(get_performances_by_athlete(c,1))
    print(get_all_for_event(c, 1,'tj'))
    conn.commit()
    conn.close()
