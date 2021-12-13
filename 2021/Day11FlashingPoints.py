import LoadInput
import numpy
from itertools import count, pairwise

example = True

if example:
    lines = LoadInput.LoadLines('Day11ex.txt')
else:
    lines = LoadInput.LoadLines('Day11input.txt')


def parseInput(lines):
    grid = []

    for line in lines:
        grid.append([int(c) for c in line])
    
    return grid

def incrementGrid(grid):

    for index, row in enumerate(grid):
        grid[index] = [oct+1 for oct in row]
    
    return grid

def flashOcts(grid):

    flashed = [(x,y) for y, row in enumerate(grid) for x, oct in enumerate(row) if oct > 9]

    for point in flashed:
        grid[point[1]][point[0]] = 0

    expended = set(flashed)
    for point in flashed:
        grid, update = flashAndInc(grid, point, expended)
        expended = expended.union(update)
    
    return len(set(expended))
          
 # up,     down,    left,  right, up left, up right, down left, down right
directions = [(0,-1), (0,1), (-1,0), (1,0), (-1,-1), (1,-1), (-1,1), (1,1)]

def flashAndInc(grid, point, expended):

    for dir in directions:
        neighbor = (point[0]+dir[0], point[1]+dir[1])
        if neighbor[0] < 0 or neighbor[0] > len(grid[0])-1 or neighbor[1] < 0 or neighbor[1] > len(grid)-1:
            continue

        if neighbor not in expended:
            grid[neighbor[1]][neighbor[0]] += 1
    
    flashed = [(x,y) for y, row in enumerate(grid) for x, oct in enumerate(row) if oct > 9]
    for point in flashed:
        grid[point[1]][point[0]] = 0

    expended = expended.union(flashed)
    for point in flashed:
        grid, expended = flashAndInc(grid, point, expended)

    return grid, expended

def part1(grid, num_steps):

    flash_count = 0
    for step in range(num_steps):
        grid = incrementGrid(grid)
        
        flash_count += flashOcts(grid)
    
    return flash_count

def part2(grid):
    num = (len(grid) * len(grid[0]))
    flash_count = 0
    step = 0
    while flash_count < num:
        grid = incrementGrid(grid)
        flash_count = flashOcts(grid)
        step += 1
        if step % 10 == 0:
            print(step)
    
    return step

#grid = parseInput(lines)
#print(part2(grid))

def learnParse(lines):
    grid = numpy.array([[int(c) for c in line] for line in lines])
    return grid

def learnIncNeighbors(grid, point=None, expended=None):

    if point != None and expended != None:
        neighbors = set([(point[0]+dir[1], point[1]+dir[0]) for dir in directions])
        ybound = [-1, len(grid)]
        xbound =[-1, len(grid[0])]

        for ny, nx in neighbors:
            if ny in ybound or nx in xbound or (ny, nx) in expended:
                continue
            grid[ny][nx] += 1
    
    flashed = list(zip(*numpy.where(grid > 9)))
    if expended == None:
        expended = set(flashed)
    else:
        expended = expended.union(flashed)

    for y,x in flashed:
        grid[y][x] = 0

    for point in flashed:
        grid, update = learnIncNeighbors(grid, point, expended)
        expended = expended.union(update)
    
    return grid, expended

def learnPart1(grid):
    
    total = 0
    for step in count():
        if step == 10: print(total)
        if step == 100: print(total)

        grid += 1
        grid, expended = learnIncNeighbors(grid)

        flash_count = len(expended)
        total += flash_count

        if flash_count == 100:
            print(step+1)
            break

grid = learnParse(lines)
total = learnPart1(grid)
print(total)