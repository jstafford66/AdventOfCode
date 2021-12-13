import LoadInput
from TwoDimensionGrid import TwoDGrid

example = False

if example:
    lines = LoadInput.LoadLines('Day13ex.txt')
else:
    lines = LoadInput.LoadLines('Day13input.txt')


def parseInput(lines):

    grid = TwoDGrid(default_value='.')
    folds = []

    points_or_folds = True
    for line in lines:

        if line == "":
            points_or_folds = False
            continue
        
        if points_or_folds:
            point = [int(coord) for coord in line.split(',')]
            grid.SetPointVal((point[0] ,point[1]), '#')
        else:
            dir, coord = line.split('=')
            folds.append((dir[-1], int(coord)))
    
    return grid, folds

def foldHoriz(grid, coord):
    miny, maxy = grid.getYBounds()
    minx, maxx = grid.getXBounds()

    for y_index in range(coord+1, maxy+1):
        dist = y_index - coord
        for x_index in range(minx, maxx+1):
            point = (x_index, y_index)
            if grid.GetPoint(point) == '#':
                new_point = (x_index, y_index - (dist*2))
                grid.SetPointVal(new_point, '#')
            grid.DeletePoint(point)
            
    
    return grid

def foldVert(grid, coord):
    miny, maxy = grid.getYBounds()
    minx, maxx = grid.getXBounds()

    for x_index in range(coord+1, maxx+1):
        dist = x_index - coord
        for y_index in range(miny, maxy+1):
            point = (x_index, y_index)
            if grid.GetPoint(point) == '#':
                new_point = (x_index - (dist*2), y_index)
                grid.SetPointVal(new_point, '#')
            grid.DeletePoint(point)
    
    return grid


def foldGrid(grid, fold):

    if fold[0] == 'y':
        grid = foldHoriz(grid, fold[1])
    elif fold[0] == 'x':
        grid = foldVert(grid, fold[1])
    
    return grid

def part1(grid, folds):

    for fold_index, fold in enumerate(folds):
        grid = foldGrid(grid, fold)

        #print("-------------------------------")
        ##grid.print()

        if fold_index == 0:
            print(grid.countWithValue('#'))
    
    grid.print()

grid, folds = parseInput(lines)

#grid.print()

part1(grid, folds)