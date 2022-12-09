import LoadInput
import re
import math
from TwoDimensionGrid import TwoDGrid

debug = False

day = 9

if debug:
    lines = LoadInput.LoadLines('Day{0}ex.txt'.format(day))
else:
    lines = LoadInput.LoadLines('Day{0}input.txt'.format(day))

def parseinput(lines):

    steps = []
    for line in lines:
        dir, count = line.split(' ')

        steps.append((dir, int(count)))

    return steps

def moveH(dir, h):
    new_point = h

    if dir == 'R':
        new_point = (h[0]+1,h[1])
    elif dir == 'U':
        new_point = (h[0],h[1]+1)
    elif dir == 'L':
        new_point = (h[0]-1,h[1])
    elif dir == 'D':
        new_point = (h[0],h[1]-1)
    
    return new_point

def moveT(t, h):
    new_point = t
    # in same column?
    if t[0] == h[0]:
        # if h is two steps away up
        if h[1]-t[1] >= 2:
            new_point = (t[0], t[1]+1)
        # if h is two steps away down
        elif t[1]-h[1] >= 2:
            new_point = (t[0], t[1]-1)
    # in the same row?
    elif t[1] == h[1]:
        # if h is two steps away right
        if h[0]-t[0] >= 2:
            new_point = (t[0]+1,t[1])
        # if two steps away left
        elif t[0]-h[0] >= 2:
            new_point = (t[0]-1,t[1])
    else:
        # if h is two steps away up
        if h[1]-t[1] >= 2:
            if h[0] > t[0]:
                new_point = (t[0]+1, t[1]+1)
            else:
                new_point = (t[0]-1, t[1]+1)
        # if h is two steps away down
        elif t[1]-h[1] >= 2:
            if h[0] > t[0]:
                new_point = (t[0]+1, t[1]-1)
            else:
                new_point = (t[0]-1, t[1]-1)
         # if h is two steps away right
        elif h[0]-t[0] >= 2:
            if h[1] > t[1]:
                new_point = (t[0]+1, t[1]+1)
            else:
                new_point = (t[0]+1, t[1]-1)
        # if two steps away left
        elif t[0]-h[0] >= 2:
            if h[1] > t[1]:
                new_point = (t[0]-1, t[1]+1)
            else:
                new_point = (t[0]-1, t[1]-1)
    
    return new_point


def part1(lines):
    ans1 = 0
    ans2 = 0

    h_grid = TwoDGrid(default_value=0)
    t_grid = TwoDGrid(default_value=0)

    steps = parseinput(lines)

    start = (0,0)
    h = (0,0)
    t = (0,0)

    h_grid.IncrementPoint(h)
    t_grid.IncrementPoint(t)

    for dir, count in steps:
        for i in range(count):
            h = moveH(dir, h)
            new_t = moveT(t,h)

            h_grid.IncrementPoint(h)

            if not (new_t == t):
                t_grid.IncrementPoint(new_t)
            t = new_t
        
    ans1 = len(t_grid.getPointsGreaterThan(0))

    return ans1,ans2

def part2(lines):

    t_grid = TwoDGrid(default_value=0)

    steps = parseinput(lines)

    start = (0,0)
    points = [(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)]

    t_grid.IncrementPoint(start)

    for dir, count in steps:
        for i in range(count):
            points[0] = moveH(dir, points[0])

            for knot in range(1, len(points)):
                new_t = moveT(points[knot],points[knot-1])

                if knot == 9 and not (new_t == points[9]):
                    t_grid.IncrementPoint(new_t)
                points[knot] = new_t
        
    ans1 = len(t_grid.getPointsGreaterThan(0))
    return ans1

print(part2(lines))
