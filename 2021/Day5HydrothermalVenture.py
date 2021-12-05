from os import truncate
import LoadInput
from TwoDimensionGrid import TwoDGrid
import re

debug = False

if debug:
    lines = LoadInput.LoadLines('Day5ex.txt')
else:
    lines = LoadInput.LoadLines('Day5input.txt')

point_ex = re.compile('\d+')
def ParseInput(lines):
    
    grid = TwoDGrid()

    for line in lines:
        coord = [int(c) for c in point_ex.findall(line)]

        min_y = min(coord[1],coord[3])
        max_y = max(coord[1],coord[3])

        min_x = min(coord[0],coord[2])
        max_x = max(coord[0],coord[2])
        if coord[0] == coord[2]:
            for y in range(min_y, max_y+1):
                point = (coord[0], y)
                grid.SetPointVal(point, grid.GetPoint(point) + 1)
        elif coord[1] == coord[3]:
            for x in range(min_x, max_x+1):
                point = (x, coord[1])
                grid.SetPointVal(point, grid.GetPoint(point) + 1)
        else:
            for n in range((max_x-min_x)+1):
                if coord[0] > coord[2] and coord[1] > coord[3]:
                    point = (coord[2]+n, coord[3]+n)
                elif coord[0] < coord[2] and coord[1] < coord[3]:
                    point = (coord[0]+n, coord[1]+n)
                elif coord[0] > coord[2] and coord[1] < coord[3]:
                    point = (coord[0]-n, coord[1]+n)
                else:
                    point = (coord[0]+n, coord[1]-n)

                grid.SetPointVal(point, grid.GetPoint(point) + 1)
    
    return grid

def part1(grid):

    points = grid.getPointsGreaterThan(1)

    return len(points)

grid = ParseInput(lines)

print(part1(grid))