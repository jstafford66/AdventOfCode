import copy

ex = False

if ex:
	#file = 'Day13ex.txt'
	file = 'Day13ex2.txt'
else:
	file = 'Day13in.txt'
	
lines = open(file).readlines()

#0:left, 1:straight, 2: right

def parseLines(lines):
	
	map = []
	carts = []
	
	for line in lines:
		row = []
		map.append(row)
		
		for c in line:
			if c == '>' or c == '<':
				row.append('-')
				carts.append({'d':c, 'l':[len(map)-1,len(row)-1], 'i':2, 'c':False})
				
			elif c == '^' or c == 'v':
				row.append('|')
				carts.append({'d':c, 'l':[len(map)-1,len(row)-1], 'i':2, 'c':False})
			else:
				if c != '\n':
					row.append(c)
				
	return map, carts

def moveCarts(map, carts):
		
	for c in carts:
		if c['c']:
			continue
			
		d = c['d']
		if d == '>':
			c['l'][1] = c['l'][1] + 1
		elif d == '<':
			c['l'][1] = c['l'][1] - 1
		elif d == '^':
			c['l'][0] = c['l'][0] - 1
		elif d == 'v':
			c['l'][0] = c['l'][0] + 1
		else:
			print('Moving Failed')
		
		newDir(c, map)

		carts = markCrashed(carts)
		
	return carts
	
def newDir(c, map):
	t = map[c['l'][0]][c['l'][1]]
	d = c['d']
	i = c['i']
	
	if t == '\\':
		if d == '>':
			c['d'] = 'v'
		elif d == '<':
			c['d'] = '^'
		elif d == 'v':
			c['d'] = '>'
		elif d == '^':
			c['d'] = '<'
	elif t == '/':
		if d == '>':
			c['d'] = '^'
		elif d == '<':
			c['d'] = 'v'
		elif d == 'v':
			c['d'] = '<'
		elif d == '^':
			c['d'] = '>'
	elif t == "+":
		if d == '>':
			if i == 2:
				c['d'] = '^'
				c['i'] = 0
			elif i == 1:
				c['d'] = 'v'
				c['i'] = 2
			elif i == 0:
				c['i'] = 1
				
		elif d == '<':
			if i == 2:
				c['d'] = 'v'
				c['i'] = 0
			elif i == 1:
				c['d'] = '^'
				c['i'] = 2
			elif i == 0:
				c['i'] = 1
		elif d == 'v':
			if i == 2:
				c['d'] = '>'
				c['i'] = 0
			elif i == 1:
				c['d'] = '<'
				c['i'] = 2
			elif i == 0:
				c['i'] = 1
		elif d == '^':
			if i == 2:
				c['d'] = '<'
				c['i'] = 0
			elif i == 1:
				c['d'] = '>'
				c['i'] = 2
			elif i == 0:
				c['i'] = 1 
	return c

def isCrash(carts):
	crash = False
	loc = [-1,-1]
	
	for i in range(0,len(carts)):
		for j in range(i+1, len(carts)):
			if carts[i]['l'] == carts[j]['l']:
				return True, carts[i]['l'], carts[i], carts[j]
				
	return crash, loc, None, None

def removeCrashed(carts):
	
	crash, loc, a, b = isCrash(carts)
	while crash:
		carts.remove(a)
		carts.remove(b)
		crash, loc, a, b = isCrash(carts)
		
	return carts

def areCartsCrashed(a, b):
	if a['l'] == b['l']:
		return True
	return False

def markCrashed(carts):
	
	for i in range(0,len(carts)):
		for j in range(i+1, len(carts)):
			if areCartsCrashed(carts[i], carts[j]):
				carts[i]['c'] = True
				carts[j]['c'] = True
		
	return carts

def printMap(map, carts, time):
	m = copy.deepcopy(map)
	
	f = open('Day13o'+str(time)+'.txt', 'w')
	
	for c in carts:
		m[c['l'][0]][c['l'][1]] = c['d']
	
	for y in m:
		line = ''
		for c in y:
			line = line + c
		
		f.write(line + '\n')
	
	f.close()
	print('-------------------------------------')
	
def sortCarts(carts):
	return sorted(carts, key=lambda c: c['l'])
	
def runPart1(map, carts):
	crash = False
	loc = [-1,-1]
	count = 0
	while not crash:
		count = count + 1
		print(count)
		carts = moveCarts(map, carts)
		crash, loc = isCrash(carts)

	print(loc)

def runPart2(map, carts):

	carts = sortCarts(carts)
	count = 0
	while len(carts) > 1:
		count = count + 1
		print(count, len(carts))
		carts = moveCarts(map,carts)
		carts = removeCrashed(carts)
		
		carts = sortCarts(carts)
		#print(carts)

		#printMap(map, carts, count)
		
	print(carts)
	#carts = moveCarts(map, carts)
	#print(carts)
	
map, carts = parseLines(lines)

runPart2(map, carts)
