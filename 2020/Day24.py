import LoadInput
from TwoDimensionGrid import TwoDGrid

debug = True

if debug:
    lines = LoadInput.LoadLines('d24ex.txt')
else:
    lines = LoadInput.LoadLines('d24input.txt')

def parseInput(lines):

    directions = []

    for line in lines:
        line = line.strip()

        path = []
        while len(line) > 0:
            '''e, se, sw, w, nw, and ne.'''
            if len(line) > 1 and line[0:2] in ['se', 'sw', 'nw', 'ne']:
                path.append(line[0:2])
                line = line[2:]
            else:
                path.append(line[0])
                line = line[1:]
        
        directions.append(path)
    
    return directions

increment = {'ne':(.5,.5), 'e':(1,0), 'se':(.5,-.5), 'sw':(-.5,-.5), 'w':(-1,0), 'nw':(-.5,.5)}

#increment = {'ne':(1,1), 'e':(1,0), 'se':(1,-1), 'sw':(-1,-1), 'w':(-1,0), 'nw':(-1,1)}

def runDirections(directions):
    grid = TwoDGrid(default_value='w')
    start = (0,0)

    for path in directions:
        tile_pt = start
        for direction in path:
            inc = increment[direction]
            tile_pt = (tile_pt[0]+inc[0], tile_pt[1]+inc[1])
        
        tile_color = grid.GetPoint(tile_pt)
        if tile_color == 'w':
            grid.SetPointVal(tile_pt, 'b')
        else:
            grid.SetPointVal(tile_pt, 'w')
        
    return grid

def countBNeighbors(grid, point):

    count = 0

    for d, inc in increment.items():
        neigh = (point[0]+inc[0], point[1]+inc[1])
        if grid.PeekPoint(neigh) == 'b':
            count+=1
    return count

def peekNeighbors(grid, point):
    neighs = {}
    for d, inc in increment.items():
        neigh = (point[0]+inc[0], point[1]+inc[1])
        neighs[neigh] = grid.PeekPoint(neigh)
    return neighs
    
def flipDayTiles(grid):
    
    tiles_to_flip = []

    # we are only checking the black tiles
    # because they are the only ones that can cause a flip
    cur_points = grid.getPointsWithValue('b')

    for point in cur_points:
        # get the neighbor count for this point
        n_count = countBNeighbors(grid, point)
        # We know this one is black... do we need to flip it?
        if n_count == 0 or n_count > 2:
            # save it for later
            tiles_to_flip.append(point)
        
        # go through all of the neighbors of this tile.
        # white tiles can only be flipped if they are an 
        # immediate neighbor to a black tile...
        for d, inc in increment.items():
            n_point = (point[0]+inc[0], point[1]+inc[1])
            n_count = countBNeighbors(grid, n_point)
            
            if grid.GetPoint(n_point) == 'b':
                if n_count == 0 or n_count > 2:
                    tiles_to_flip.append(n_point)
            else:
                if n_count == 2:
                    tiles_to_flip.append(n_point)
    
    # converting to a set should remove duplicates
    # because it is entirely possible we added duplicates above
    flip = list(set(tiles_to_flip))
    for point in flip:
        if grid.GetPoint(point) == 'w':
            grid.SetPointVal(point, 'b')
        else:
            grid.SetPointVal(point, 'w')
    
    return grid

def part1(grid):
    ans = grid.countWithValue('b')

    return ans

def part2(grid):

    green = 5
    for it in range(100):
        grid = flipDayTiles(grid)
        #num = grid.countWithValue('b')

    ans = grid.countWithValue('b')
    return ans

directions = parseInput(lines)
grid = runDirections(directions)

print(part1(grid))
print(part2(grid))