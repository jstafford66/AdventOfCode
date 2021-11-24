import re
from datetime import datetime
import functools
import pprint

#lines = open("Day4Example.txt").readlines()

lines = open("Day4Input.txt").readlines()

def getTimeDate(line):
	time_re = "\[(\d+)-(\d+)-(\d+)\s*(\d+):(\d+)\]"
	
	time_match = re.search(time_re, line)
	
	return datetime(int(time_match.group(1)),int(time_match.group(2)),int(time_match.group(3)),int(time_match.group(4)),int(time_match.group(5)))

def getGuardID(line):
	id_re = "Guard\s\#(\d+)"
	
	id_match = re.search(id_re, line)
	
	if id_match:
		return id_match.group(1)
	return None

def getAwakeSleep(line):
	
	if 'asleep' in line:
		return True
	elif 'wakes' in line:
		return False
	
	return None
	
def cmp_items(a, b):
	a_date = getTimeDate(a)
	b_date = getTimeDate(b)
	
	if a_date > b_date:
		return 1
	elif a_date == b_date:
		return 0
	return -1

def sleepSched(lines):
	
	sched = {}
	
	current_guard = None
	
	for line in lines:
		#print (line)
		date = getTimeDate(line)
		
		guard = getGuardID(line)
		asleep = getAwakeSleep(line)
		
		if guard:
			if guard not in sched:
				sched[guard] = {'shifts':[]}
			#'asleep':[{'start':date, 'minutes':time}]
			#print(guard)
			sched[guard]['shifts'].append({'start':date, 'asleep':[]})
			current_guard = guard
		
		if asleep is not None:
			if asleep:
				sched[current_guard]['shifts'][-1]['asleep'].append({'start':date})
			else:
				current_sleep = sched[current_guard]['shifts'][-1]['asleep'][-1]
				start = current_sleep['start']
				dif = int(((date - start).seconds) / 60)
				#print(dif)
				
				current_sleep['minutes'] = dif

	return sched

def calcSleep(sched):
	
	for guard, values in sched.items():
		#print(guard)
		time = 0
		for shift in values['shifts']:
			for snooze in shift['asleep']:
				#print(time, snooze['minutes'])
				time = time + snooze['minutes']
			
			#print(time)
		
		values['sleep_time'] = time
		#print("End Guard")
	#print("End Calc")
	return sched

def getMostSleep(sched):

	most = list(sched.keys())[0]
	time = sched[most]['sleep_time']

	for guard, values in sched.items():
		
		if values['sleep_time'] > time:
			most = guard
			time = values['sleep_time']
	
	return most, time

def getMinute(guard_sched):
	
	minutes = [0 for x in range(60)]
	
	for shift in guard_sched['shifts']:
		for snooze in shift['asleep']:
			#print(int(snooze['start'].minute), snooze['minutes'])
			start = int(snooze['start'].minute)
			for m in range(start, int(start + snooze['minutes'])):
				minutes[m] = minutes[m] + 1
	
			#print(minutes)
			#print("--------------------------")
	max_minute = max(minutes)
	
	return minutes.index(max_minute), max_minute

def printGuardSleep(sched):
	for guard, values in sched.items():
		print (guard, values['sleep_time'])

def guardsMostMinute(sched):

	most_guard = None
	most_minute = -1
	most_hits = -1
	
	for guard, values in sched.items():
		minute, hits = getMinute(values)
		values['minute'] = minute
		values['hits'] = hits
		
		if hits > most_hits:
			most_guard = guard
			most_minute = minute
			most_hits = hits
	
	return most_guard, most_minute, most_hits
		
x = sorted(lines, key=functools.cmp_to_key(cmp_items))

sched = sleepSched(x)

sched = calcSleep(sched)

guard, time = getMostSleep(sched)

printGuardSleep(sched)

#pp = pprint.PrettyPrinter(indent=4)
#pp.pprint(sched[guard])

minute, hits = getMinute(sched[guard])

print(guard, time, minute, hits)
answer = int(guard) * int(minute)
print(answer)
print("---------------")
guard2, minute2, hits2 = guardsMostMinute(sched)
print(guard2, minute2, hits2)
answer2 = int(guard2) * int(minute2)
print(answer2)