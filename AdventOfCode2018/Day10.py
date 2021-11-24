import re

ex = False

if ex:
	lines = open('Day10ex.txt').readlines()
else:
	lines = open('Day10in.txt').readlines()

def parseInput(lines):
	ex = '(-?\d+),\s*(-?\d+)'
	
	points = []
	
	for line in lines:
		lm = re.findall(ex, line)
		if lm:
			points.append({'p':[int(lm[0][0]),int(lm[0][1])], 'v':[int(lm[1][0]), int(lm[1][1])]})
	
	return points
		

def getSeq(points, time):
	
	if time <= 0:
		return points
	
	seq = []
		
	for point in points:
		seq.append([int(point['p'][0] + point['v'][0] * time), int(point['p'][1] + point['v'][1] * time)])
	
	return seq

def isSeqImg(seq):
	
	samex = {}
	
	for point in seq:
		if point[0] in samex:
			samex[point[0]].append(point)
		else:
			samex[point[0]]=[point]
	
	for x, val in samex.items():
		y = sorted(val, key=lambda point: point[1])
		
		cnt = 0
		for index in range(0, len(y)-1):
			if y[index][1] == (y[index+1][1]-1):
				cnt = cnt + 1
			else:
				cnt = 0
			
			if cnt >= 3:
				print(seq)
				return True
	
	return False

def printSeq(points, seq):

	#minx = min([point['p'][0] for point in points])
	#maxx = max([point['p'][0] for point in points])
	#miny = min([point['p'][1] for point in points])
	#maxy = max([point['p'][1] for point in points])
	
	minx = min([s[0] for s in seq])
	maxx = max([s[0] for s in seq])+1
	miny = min([s[1] for s in seq])
	maxy = max([s[1] for s in seq])+1

	
	print(minx,maxx,miny,maxy)
	#grid = [['.'.ljust(15) for y in range(miny, maxy+1)] for x in range(minx, maxx+1)]
	grid = [['.' for y in range(0, maxy+1)] for x in range(0, maxx+1)]

		
	adjx = abs(minx)
	adjy = abs(miny)
	for point in seq:
		x = int(point[0])#+int(adjx)
		y = int(point[1])#+int(adjy)
		#print(x, y)
		#print(len(grid), len(grid[0]))
		#grid[x][y] = '({}[{}],{}[{}])'.format(point['p'][0],x,point['p'][1],y).ljust(15)
		grid[x][y] = '#'
		
	f = open('day10out' + str(time) + '.txt','w')
	for y in range(0, maxy):
		l = ''
		for x in range(0, maxx):
			l = l + grid[x][y]
		
		f.write(l + '\n')
	
	f.close()
	
points = parseInput(lines)

found = False
fnd = 0
time = 1
#time = 1
while fnd < 20:
	seq = getSeq(points,time)
	if isSeqImg(seq):
		print(time)
		print('----------------------------------------')
		printSeq(points, seq)
		found = True
		fnd = fnd + 1
	
	time = time + 1
	if time % 100 == 0:
		print(time)
	
#printSeq(points, getSeq(points, 3))