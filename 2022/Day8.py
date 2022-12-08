import LoadInput
import re
import math
from TwoDimensionGrid import TwoDGrid

debug = False

day = 8

if debug:
    lines = LoadInput.LoadLines('Day{0}ex.txt'.format(day))
else:
    lines = LoadInput.LoadLines('Day{0}input.txt'.format(day))

def parseinput(lines):

    trees = TwoDGrid()

    for row, line in enumerate(lines):
        for column, ch in enumerate(line):
            trees.SetPointVal((column, row), int(ch))

    return trees

# 55x
# 5x3
# x5x
# 

def viewFromAbove(point, y_bound, tree_grid):
    view = True
    
    for r in range(point[1]-1, y_bound[0]-1, -1):
        cur = tree_grid.PeekPoint(point)
        test = tree_grid.PeekPoint((point[0], r))
        if test >= cur:
            return False
    
    return view

def viewFromBelow(point, y_bound, tree_grid):
    view = True
    
    for r in range(point[1]+1, y_bound[1]+1):
        cur = tree_grid.PeekPoint(point)
        test = tree_grid.PeekPoint((point[0], r))
        if test >= cur:
            return False
    
    return view

def viewFromLeft(point, x_bound, tree_grid):
    view = True
    
    for c in range(point[0]-1, x_bound[0]-1, -1):
        if tree_grid.PeekPoint(point) <= tree_grid.PeekPoint((c, point[1])):
            return False
    
    return view

def viewFromRight(point, x_bound, tree_grid):
    view = True
    
    for c in range(point[0]+1, x_bound[1]+1):
        if tree_grid.PeekPoint(point) <= tree_grid.PeekPoint((c, point[1])):
            return False
    
    return view

def countAbove(point, y_bound, tree_grid):
    view = 0
    
    for r in range(point[1]-1, y_bound[0]-1, -1):
        view += 1
        cur = tree_grid.PeekPoint(point)
        test = tree_grid.PeekPoint((point[0], r))
        if test >= cur:
            break
    
    return view

def countBelow(point, y_bound, tree_grid):
    view = 0
    
    for r in range(point[1]+1, y_bound[1]+1):
        view += 1
        cur = tree_grid.PeekPoint(point)
        test = tree_grid.PeekPoint((point[0], r))
        if test >= cur:
            break
    
    return view

def countLeft(point, x_bound, tree_grid):
    view = 0
    
    for c in range(point[0]-1, x_bound[0]-1, -1):
        view += 1
        if tree_grid.PeekPoint(point) <= tree_grid.PeekPoint((c, point[1])):
            break
    
    return view

def countRight(point, x_bound, tree_grid):
    view = 0
    
    for c in range(point[0]+1, x_bound[1]+1):
        view += 1
        if tree_grid.PeekPoint(point) <= tree_grid.PeekPoint((c, point[1])):
            break
    
    return view


def part1(lines):
    ans1 = 0
    ans2 = 0

    tree_grid = parseinput(lines)

    x_bound = tree_grid.getXBounds()
    y_bound = tree_grid.getYBounds()

    visible_trees = []
    senic_scores = []

    for row in range(y_bound[0], y_bound[1]+1):
        for col in range(x_bound[0], x_bound[1]+1):
            is_visible = False

            if row == y_bound[0] or row == y_bound[1] or col == x_bound[0] or col == x_bound[1]:
                is_visible = True
                senic_scores.append(0)
            else:
                point = (col, row)
                is_visible = any([viewFromAbove(point, y_bound, tree_grid), viewFromBelow(point, y_bound, tree_grid),
                    viewFromLeft(point,x_bound,tree_grid), viewFromRight(point,x_bound, tree_grid)])
                
                counts = [countAbove(point, y_bound, tree_grid), countBelow(point, y_bound, tree_grid),
                    countLeft(point,x_bound,tree_grid), countRight(point,x_bound, tree_grid)]
                
                senic_scores.append(math.prod(counts))

            if is_visible:
                visible_trees.append((col, row))

    ans1 = len(visible_trees)
    ans2 = max(senic_scores)

    return ans1,ans2

print(part1(lines))
