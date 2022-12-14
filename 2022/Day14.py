import LoadInput
import re
import math
from TwoDimensionGrid import TwoDGrid

debug = True

day = 14

if debug:
    lines = LoadInput.LoadLines('Day{0}ex.txt'.format(day))
else:
    lines = LoadInput.LoadLines('Day{0}input.txt'.format(day))

def parseinput(lines):

    cave = TwoDGrid(default_value='.')

    for line in lines:
        coords = re.findall("(\d+\,\d+)", line)

        path = []
        for p in coords:
            point = p.split(',')
            path.append((int(point[0]), int(point[1])))
        
        for index in range(len(path)-1):
            s = path[index]
            e = path[index+1]

            for col in range(min(s[0],e[0]), max(s[0],e[0])+1):
                for row in range(min(s[1],e[1]), max(s[1],e[1])+1):
                    cave.SetPointVal((col,row), '#')
            
            cave.SetPointVal(e,'#')

    cave.print2D()
    return cave

sand_source = (500, 0)
def part1(lines):
    ans1 = 0
    ans2 = 0

    cave = parseinput(lines)

    fell_out = False
    units_rest = 0

    while not fell_out:
        
        loc = (sand_source[0], sand_source[1]+1)
        stopped = False
        while not stopped:
            spot = cave.GetPoint(loc)
            if spot == '.':
                loc = (loc[0], loc[1]-1)
                continue

    return ans1,ans2

def part2(lines):
    ans1 = 0


    return ans1

print(part1(lines))
print(part2(lines))
