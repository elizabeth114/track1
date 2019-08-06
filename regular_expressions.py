import re

run_event = re.compile("(?P<gender>women|men) (?P<event>\d*) meter (run|dash)", re.IGNORECASE)
hj_event = re.compile("(?P<gender>women|men) (?P<event>high jump)", re.IGNORECASE)
separator = re.compile("=======+")
performance = re.compile("(\d*) *(?P<first>[a-zA-Z\-]+) *(?P<last>[a-zA-Z\-]+) *(?P<grade>fr|so|jr|sr) *(?P<school>[a-zA-Z][ a-zA-Z\-]+[a-zA-Z]) *(?P<mark>[0-9.:]+)", re.IGNORECASE)
event_break = re.compile("\n")
if __name__=="__main__":
    match = re.search(event, "hi WOMEN 100 meter run")
    print(match.groupdict())
    match =  re.search(performance, "5 Summer-Solstice Thomas    JR Williams                 15.33   1.3  3    799")
    print(match.groupdict())
    print(match)
