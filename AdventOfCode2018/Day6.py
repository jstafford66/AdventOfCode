
#input = open("Day6example.txt").readlines()

input = open("Day6input.txt").readlines()

w = 360
h = 360

def getCoords(lines):
	coords = []
	for line in lines:
		coords.append(line.replace(' ', '').replace('\n','').split(','))
	return coords
	

def buildGrid(coords):
	
	grid = [[{'index':-1, 'dist':1000} for y in range(w)] for x in range(h)]
	
	for index in range(0, len(coords)):
		cx = int(coords[index][0])
		cy = int(coords[index][1])
		
		print(index, cx,cy)
		for x in range(0,w):
			for y in range(0,h):
				dist = getDistance(cx,cy,x,y)
				#print(x,y, dist, grid[x][y]['dist'])
				#print(grid[x][y]['dist'], dist)
				if grid[x][y]['dist'] == dist:
					grid[x][y]['dist'] = dist
					grid[x][y]['index'] = '.'
				elif grid[x][y]['dist'] > dist:
					grid[x][y]['dist'] = dist
					grid[x][y]['index'] = index
		
		#printGrid(grid)
		#print("---------------------")
	
	#print(grid)
	return grid
		
		
def getDistance(ax, ay, bx, by):
	xdist = max(ax,bx)-min(ax,bx)
	ydist = max(ay,by)-min(ay,by)
	#print('dist', xdist, ydist, ax, ay, bx, by)
	return xdist+ydist

def getAreas(grid, coords):
	distances = [0 for i in range(0, len(coords))]
	
	for x in range(0,w):
		for y in range(0,h):
			index = grid[x][y]['index']
			if index == '.':
				continue
			
			if x == 0 or x == w-1 or y == 0 or y == h-1:
				distances[index] = -1
			elif distances[index] != -1:
				distances[index] = distances[index] + 1
			
	return distances
	
def printGrid(grid):
	out = open('Day6Grid.txt','w')

	for y in range(0,h):
		col = ''
		for x in range(0,w):
			col = col + (str(grid[x][y]['index'])).ljust(6)
			
		out.write(col + '\n')
		#print(col)
	out.close()
	
coords = getCoords(input)
grid = buildGrid(coords)

printGrid(grid)

areas = getAreas(grid,coords)
print(areas)
print(max(areas))