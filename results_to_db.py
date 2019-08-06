from classes import *
import sys
from html.parser import HTMLParser
from regular_expressions import *
import re
import sqlite3

relays = {"4x100", "4x200", "4x400", "4x800", "DMR", "SMR"}

class_year_convert = {"fr": 3, "so": 2, "jr": 1, "sr":0}
def convert_from_tffrs(file_name, year=2019, month="01", day="01"):
    # parser = MyHTMLParser()
    conn = sqlite3.connect('example.db')
    c = conn.cursor()
    meet_id = get_next_meet_id(c)
    file = open(file_name, "r")
    f = file.readlines()
    done = False
    index = 0
    ev_count = 0
    while index<len(f):
        print(index)
        event_info = re.search(run_event, f[index])
        if event_info is None:
            event_info = re.search(hj_event, f[index])
        print(event_info)
        if event_info is not None:
            event_info = event_info.groupdict()
            count = 0
            while count<2:
                print(count)
                if re.search(separator, f[index]) is not None:
                    count += 1
                index +=1
            while True:
                if re.match(event_break, f[index]):
                    break
                perf = re.search(performance, f[index])
                print(perf)
                if perf is not None:
                    perf = perf.groupdict()
                    athlete_id = get_id_by_name_school_grade(c, perf['first'].lower(), perf['last'].lower(), perf['school'].lower(), year+class_year_convert[perf["grade"].lower()])
                    if athlete_id is None:
                        athlete_id = add_athlete(c, perf["first"].lower(), perf["last"].lower(), perf["school"].lower(), event_info["gender"].lower(), year+class_year_convert[perf["grade"].lower()])
                    new_performance = Performance(event_info["event"].lower(), perf["mark"], athlete_id, str(year)+"-"+month+"-"+day, meet_id)
                    new_performance.to_database(c)
                index += 1
        index+=1
    file.close()
    pretty_print(get_athletes_by_school(c, "williams"))
    pretty_print(get_event_performances(c, "high jump"))
    conn.commit()
    conn.close()

def add_athlete(c, first, last, school, gender, grad_year):
    athlete = Athlete(first, last, school, gender, grad_year)
    return athlete.to_database(c)

def pretty_print(mylist):
    for thing in mylist:
        print(thing)
if __name__ == "__main__":
    drop_tables()
    create_tables()
    convert_from_tffrs(sys.argv[1])
