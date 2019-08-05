import sqlite3

class Athlete():
    def __init__(self, first, last, school, athlete_id, grad_year=None):
        self.first = first
        self.last = last
        self.school = school
        self.grad_year = grad_year
        self.athlete_id = athlete_id

class Event(enum.Enum):
    100m = 's'
    200m = 's'
    tj = 'm'

class Performance():
    def __init__(self, event, mark, athlete_id, date, meet_id):
        self.event = event
        self.mark = mark
        self.athlete_id = athlete_id
        self.date = date
        self.meet_id = meet_id

class Meet():
    def __init__(self, meet_id, meet_name, date):
        self.meet_id = meet_id
        self.meet_name = meet_name
        self.date = date

def add_athlete(first, last, school, grad_year=None):
    conn = sqlite3.connect('example.db')
    c = conn.cursor()

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
    c.execute("""CREATE TABLE IF NOT EXISTS athletes (text first, text last, text school, int athlete_id, int grad_year)""")
    c.execute("""CREATE TABLE IF NOT EXISTS performances (text event, float mark, int athlete_id, date our_date, int meet_id)""")
    c.execute("""CREATE TABLE IF NOT EXISTS meets (int meet_id, text meet_name, date our_date)""")
    conn.commit()
    conn.close()
