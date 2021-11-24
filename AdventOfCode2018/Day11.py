
ex = False

if ex:
	sn = 42
	
else:
	sn = 8979


def getGrid(sn):
	
	print(sn)
	grid = []
	
	for x in range(0, 300):
		grid.append([])
		for y in range(0,300):
			id = x + 10
			apl = (((id * y) + sn) * id)
			
			bpl = int(apl / 100) % 10
			
			if bpl < 0:
				bpl = 0
			
			pl = bpl - 5
			grid[x].append(pl)
			
	return grid

def getHigh(grid, size):
	
	max = -30000
	maxp = [-1,-1]
	
	for x in range(len(grid)-size):
		for y in range(len(grid[x])-size):
			s = 0
			for xx in range(x, x + (size)):
				for yy in range(y, y + (size)):
					s = s + grid[xx][yy]
			
			if s > max:
				max = s
				maxp = [x,y]
	
	return maxp, max

#print(getHigh(getGrid(sn), 3))

grid = getGrid(sn)

max = 0
maxs = 0
maxp = [-1,-1]

since = 0

for size in range(3, 300):
	
	print(size)
	p, s = getHigh(grid,size)
	
	if s > max:
		max = s
		maxs = size
		maxp = p
		since = 0
		print(maxp, maxs, max)
		print("***************")
	else:
		since = since + 1
	if since > 5:
		break
		
print(maxp, maxs, max)

