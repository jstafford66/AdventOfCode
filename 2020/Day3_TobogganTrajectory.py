import LoadInput
from TwoDimensionGrid import TwoDGrid

debug = False

if debug:
    lines = LoadInput.LoadLines('d3ex.txt')
else:
    lines = LoadInput.LoadLines('d3input.txt')

def getMap(lines, grid=None, right=0):
    if grid == None:
        g = TwoDGrid()
    else:
        g = grid

    down = 0
    for line in lines:
        r = right
        for c in line:
            g.SetPointVal((r, down), c)
            r = r + 1
        down = down + 1
    
    return g, r, down

def part1(lines, slope):

    grid, right, down = getMap(lines)

    position = (0,0)

    trees = 0
    while(position[1] < down):
        position = (position[0]+slope[0], position[1]+slope[1])

        if position[0] >= right:
            grid, right, down = getMap(lines, grid, right)

        val = grid.GetPoint(position)
        if val == '#':
            trees = trees + 1
    
    return trees

def part2(lines):
#Right 1, down 1.
    a = part1(lines, (1,1))
#Right 3, down 1. (This is the slope you already checked.)
    b = part1(lines, (3,1))
#Right 5, down 1.
    c = part1(lines, (5,1))
#Right 7, down 1.
    d = part1(lines, (7, 1))
#Right 1, down 2.
    e = part1(lines, (1, 2))

    return a * b * c * d * e

#print(part1(lines,(3,1)))

print(part2(lines))