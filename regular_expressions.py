import re

run_event = re.compile("(?P<gender>women|men) (?P<event>\d*) meter (run|dash)", re.IGNORECASE)
field_event = re.compile("(?P<gender>women|men) (?P<event>((high|long|triple) jump|javelin|(hammer|weight) throw|shot put|discus|pole vault))", re.IGNORECASE)
separator = re.compile("=======+")
performance = re.compile("(\d*) *(?P<first>[a-zA-Z\-\']+) *(?P<last>[a-zA-Z\-\']+) *(?P<grade>fr|so|jr|sr) *(?P<school>[a-zA-Z][ a-zA-Z\-]+[a-zA-Z]) *(?P<seed>[0-9.:m]+) *J*(?P<mark>[0-9.:]+)", re.IGNORECASE)
event_break = re.compile("\n")

run_event_perf = re.compile("#\d (?P<gender>women|men)\'s (?P<event>\d+) meters\n", re.IGNORECASE)
perf_performance = re.compile("(\d*) *(?P<first>[a-zA-Z\-\']+) *(?P<last>[a-zA-Z\-\']+) *(?P<grade>fr|so|jr|sr) *(?P<school>[a-zA-Z][ a-zA-Z\-]+[a-zA-Z]) *(?P<seed>[0-9.:]+)", re.IGNORECASE)

if __name__=="__main__":
    match = re.search(event, "hi WOMEN 100 meter run")
    print(match.groupdict())
    match =  re.search(performance, "5 Summer-Solstice Thomas    JR Williams                 15.33   1.3  3    799")
    print(match.groupdict())
    print(match)
