import LoadInput
import re
import math
from TwoDimensionGrid import TwoDGrid

debug = False

day = 12

if debug:
    lines = LoadInput.LoadLines('Day{0}ex.txt'.format(day))
else:
    lines = LoadInput.LoadLines('Day{0}input.txt'.format(day))

def addEdge(current, neighbor, height_map):
    this_height = ord(height_map.GetPoint(current))
    neigh_height = ord(height_map.GetPoint(neighbor))

    if (this_height+1) >= neigh_height:
        height_map.AddPointEdge(current, 1, neighbor)

def parseinput(lines):

    height_map = TwoDGrid(default_value=None)

    start_point = (0,0)
    end_point = start_point

    for row in range(len(lines)):
        for col in range(len(lines[row])):
            point = (col, row)
            height = lines[row][col]
            if height == 'S':
                start_point = (col, row)
                height = 'a'
            elif height == 'E':
                end_point = (col, row)
                height = 'z'
            
            height_map.SetPointVal(point, height)

    for row in range(len(lines)):
        for col in range(len(lines[row])):
            # add edges
            this_point = (col, row)

            # look up
            if row > 0:
                neigh_point = (col, row-1)
                addEdge(this_point, neigh_point, height_map)
            
            # look right
            if col < len(lines[row])-1:
                neigh_point = (col+1, row)
                addEdge(this_point, neigh_point, height_map)
            
             # look left
            if col > 0:
                neigh_point = (col-1, row)
                addEdge(this_point, neigh_point, height_map)
            
            # look down
            if row < len(lines)-1:
                neigh_point = (col, row+1)
                addEdge(this_point, neigh_point, height_map)
                
    return height_map, start_point, end_point

def part1(lines):
    ans1 = 0
    ans2 = 0

    height_map, start, end = parseinput(lines)

    shortest = height_map.ShortestPath(start, end)

    return shortest,ans2

def part2(lines):
    height_map, start, end = parseinput(lines)

    all_low_points = height_map.getPointsWithValue('a')

    shortest = -1

    for low_point in all_low_points:
        dist = height_map.ShortestPath(low_point, end)

        # if this is negative 1, we never reached the end.
        if dist == -1:
            continue

        if shortest == -1 or dist < shortest:
            shortest = dist

    return shortest

print(part1(lines))
print(part2(lines))
