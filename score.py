from classes import *
import sqlite3
import sys
import re
from regular_expressions import *

def average_ranking(c, athletes, event, num_needed):
    scorers = []
    for athlete in athletes:
        performances = get_all_for_event(c, athlete.get_athlete_id(), event)
        total = 0
        for mark in performances:
            total += mark[0]
        average = total/len(performances)
        if len(scorers)<num_needed:
            scorers.append((average, athlete))
            scorers.sort()
        elif events[event]=='s' and average<scores[-1][0]:
            del scores[-1]
            scorers.append((average, athlete))
            scorers.sort()
        elif events[event]=='m' and average>scores[0][0]:
            del scores[0]
            scorers.append((average, athlete))
            scorers.sort()
    if events[event]=='m':
        scorers.reverse()
    return scorers


def pr_ranking(c, athletes, event, num_needed):
    scorers = []
    for athlete in athletes:
        pr = get_event_pr(c, athlete.get_athlete_id(), event)
        if len(scorers)<num_needed:
            scorers.append((pr, athlete))
            scorers.sort()
        elif events[event]=='s' and pr<scores[-1][0]:
            del scores[-1]
            scorers.append((pr, athlete))
            scorers.sort()
        elif events[event]=='m' and pr>scores[0][0]:
            del scores[0]
            scorers.append((pr, athlete))
            scorers.sort()
    if events[event]=='m':
        scorers.reverse()
    return scorers

def most_recent(c, athletes, event, num_needed):
    pass

def season_average(c, athletes, event, num_needed):
    pass

def season_pr(c, athletes, event, num_needed):
    pass


methods = {"average": average_ranking, "pr": pr_ranking, "season_pr": season_pr, "recent": most_recent, "season_average": season_average}
scores = {"8": [10,8,6,5,4,3,2,1], "3": [5,3,1]}

# athletes is a list of athlete ids
def score_event(c, athletes, event, scoring, method):
    print("hi")
    scores_by_school = {}
    results = methods[method](c, athletes, event, len(scores[scoring]))
    index = 0
    for mark, athlete in results:
        if athlete.get_school() in scores_by_school:
            scores_by_school[athlete.get_school()] += scores[scoring][index]
        else:
            scores_by_school[athlete.get_school()] = scores[scoring][index]
        index += 1
    return scores_by_school, results


def performance_list_predictions(file_name):
    file = open(file_name, "r")
    f = file.readlines()
    for i in range(120):
        print(re.match(run_event_perf, f[i]))



if __name__ == "__main__":
    performance_list_predictions(sys.argv[1])
    # conn = sqlite3.connect('example.db')
    # c = conn.cursor()
    # elizabeth = Athlete("elizabeth", "weeks", "MIT", "F", 2021, 1)
    # katie = Athlete("katie", "williams", "MIT", "F", 2021, 2)
    # summer = Athlete("summer-solstice", "thomas", "Williams", "F", 2020, 3)
    # print(score_event(c, [elizabeth, katie, summer], 'tj', "3", "average"))
    # print(score_event(c, [elizabeth, katie, summer], 'tj', "3", "pr"))
    # conn.close()
