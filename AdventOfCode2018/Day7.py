
import re

ex = False

if ex:
	lines = open('Day7ex.txt').readlines()
	num = 2
	t = 1
else:
	lines = open('Day7in.txt').readlines()
	num = 5
	t = 61


def getLineSteps(line):
	expression = 'Step\s(\w).+step\s(\w)'
	
	match = re.search(expression,line)
	
	return match.group(1), match.group(2)
	
def parseSteps(lines):
	
	steps = {}
	
	for line in lines:
		a, b = getLineSteps(line)
		
		if a not in steps:
			steps[a] = {'next':[b], 'prev':[]}
		elif b not in steps[a]['next']:
			steps[a]['next'].append(b)
		
		if b not in steps:
			steps[b] = {'next':[], 'prev':[a]} 
		elif a not in steps[b]['prev']:
			steps[b]['prev'].append(a)
	
	return steps

def getFirst(steps):
	available = []
	for key, value in steps.items():
		if not value['prev']:
			available.append(key)	
	
	available = sorted(available)
	#print(available)
	return available
	
def getNext(steps, available, complete):
	next = None
	for a in available:
		if set(steps[a]['prev']).issubset(complete):
			next = a
			available.remove(a)
			break
		#print("Skip " + a + " Because prev " + str(steps[a]['prev']) + " not in complete")
	return next

def addNewAvailable(available, next):

	for i in steps[next]['next']:
		if i not in available:
			available.append(i)
	
	return sorted(available)
	
def getOrder(steps):
	
	seq = []
	
	available = getFirst(steps)
	
	while available:
		next = getNext(steps, available, seq)
			
		#print("next", next, steps[next]['next'])
		seq.append(next)
			
		available = addNewAvailable(available, next)
		
		#print("available", available)
		#print("seq", seq)
		#print('------------')
	
	return seq
	
steps = parseSteps(lines)

#print(steps)

seq = getOrder(steps)

#print(seq)
print('********')
print(''.join(seq))


letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

times = {}
for i in range(0, len(letters)):
	times[letters[i]] = i + t

def getTime(steps):
	print(times)
	seconds = -1
	
	workers = [{'task':None, 'time':0} for x in range(0,num)]
	complete = []
	available = getFirst(steps)
	current = []
	
	while available or current:
		seconds = seconds + 1

		for worker in workers:
			if worker['task']:
				if worker['time'] == 0:
					print('item complete:', item)
					item = worker['task']
					complete.append(item)
					
					available = addNewAvailable(available, item)
					current.remove(item)
					worker['task'] = None
				else:
					worker['time'] = worker['time'] - 1
						
			if not worker['task']:
				item = getNext(steps, available, complete)
				if item:
					worker['task'] = item
					worker['time'] = times[item] - 1
					current.append(item)
		
			print(worker)
			
		print('ava:', available, 'cur:',current)
		print('comp:',complete, 'time:', seconds)
		print("-------------------------------------")
	
	return seconds

time = getTime(steps)
print('Time:', time)