
import LoadInput
import heapq

debug = False

if debug:
    lines = LoadInput.LoadLines('Day9ex.txt')
else:
    lines = LoadInput.LoadLines('Day9input.txt')


def parseInput(lines):
    grid = []

    for line in lines:
        grid.append([int(p) for p in line.strip()])
    
    return grid

def part1(grid):

    low_points = []
    for y, row in enumerate(grid):
        for x, height in enumerate(row):
            neighbors = []
            #above
            if y > 0:
                neighbors.append(grid[y-1][x])
            #left
            if x > 0:
                neighbors.append(grid[y][x-1])
            # below
            if y < len(grid)-1:
                neighbors.append(grid[y+1][x])
            # right
            if x < len(row)-1:
                neighbors.append(grid[y][x+1])
            
            if height < min(neighbors):
                low_points.append(height)
    
    risks = [p+1 for p in low_points]

    return sum(risks)

def getLowPoints(grid):
    low_points = []
    for y, row in enumerate(grid):
        for x, height in enumerate(row):
            neighbors = []
            #above
            if y > 0:
                neighbors.append(grid[y-1][x])
            #left
            if x > 0:
                neighbors.append(grid[y][x-1])
            # below
            if y < len(grid)-1:
                neighbors.append(grid[y+1][x])
            # right
            if x < len(row)-1:
                neighbors.append(grid[y][x+1])
            
            if height < min(neighbors):
                low_points.append({'loc': (x,y), 'val':height})
    
    return low_points

def findBasin(loc, grid, visited=None):
    size = 1

    if visited == None:
        visited = set([loc])
    else:
        visited.add(loc)

    #Search each of the 4 directions
    search_points = []
    # up
    if loc[1] > 0:
        search_points.append((loc[0], loc[1]-1))
    # left
    if loc[0] > 0:
        search_points.append( (loc[0]-1, loc[1]))    
    # down
    if loc[1] < len(grid)-1:
        search_points.append((loc[0], loc[1]+1))
    # right
    if loc[0] < len(grid[0])-1:
        search_points.append((loc[0]+1, loc[1]))
    
    for point in search_points:
        val = grid[point[1]][point[0]]

        # don't visit a point twice
        if visited != None and point in visited:
            continue

        if val < 9:
            found, touched = findBasin(point, grid, visited)
            size += found
            visited = visited.union(touched)
    
    return size, visited

def part2(grid):
    low_points = getLowPoints(grid)

    basins = []

    for point in low_points:
        basins.append(findBasin(point['loc'], grid)[0])
    
    largest = heapq.nlargest(3,basins)
    res = largest[0] * largest[1] * largest[2]
    return res

grid = parseInput(lines)
print(part2(grid))