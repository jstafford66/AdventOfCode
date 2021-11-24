import itertools
from math import atan2, hypot, pi

# Find all whole number points on the line between to asteroids
# Determine if there are any asteroids on those points

def slope(origin, target):
    if target['x'] == origin['x']:
        return 0
    else:
        m = (target['y'] - origin['y']) / (target['x'] - origin['x'])
        return m

def line_eqn(origin, target):
    x = origin['x']
    y = origin['y']
    c = -(slope(origin, target)*x - y)
    c = y - (slope(origin, target)*x)
    #return 'y = ' + str(slope(target)) + 'x + ' + str(c)
    m = slope(origin, target)
    return {'m':m, 'c':c}

def get_y(x, slope, c):
    # y = mx + c    
    y = (slope*x) + c
    return y

def get_x(y, slope, c):     
    #x = (y-c)/m
    if slope == 0:
        c = 0   #vertical lines never intersect with y-axis
    if slope == 0:
        slope = 1   #Do NOT divide by zero
    x = (y - c)/slope
    return x

def get_points(a, b):
    
    origin = {'x':a[0], 'y':a[1]}
    target = {'x':b[0], 'y':b[1]}
    coord_list = []

    #is vertical line?
    if origin['x'] == target['x']:
        for y in range(min(origin['y'], target['y']), max(origin['y'], target['y'])+1):
            coord_list.append((origin['x'], y))
        return coord_list
    
    #is horizontal line?
    if origin['y'] == target['y']:
        for x in range(min(origin['x'], target['x']), max(origin['x'], target['x'])+1):
            coord_list.append((x, origin['y']))
        return coord_list

    if origin['x'] > target['x']:
        h = target
        target = origin
        origin = h

    #Step along x-axis
    for i in range(origin['x'], target['x']+1):     
        eqn = line_eqn(origin, target)
        y = round(get_y(i, eqn['m'], eqn['c']),2)

        if float(y).is_integer():     
            coord_list.append((i, int(y)))

    if origin['y'] > target['y']:
        h = target
        target = origin
        origin = h

    #Step along y-axis
    for i in range(origin['y'], target['y']+1):
        eqn = line_eqn(origin, target)
        x = round(get_x(i, eqn['m'], eqn['c']),2)

        if float(x).is_integer():
            coord_list.append((int(x), i))

    #return unique list 
    return list(set(coord_list))

def loadInput(loc):
    data = []
    lines = open(loc).readlines()

    for y in range(len(lines)):
        for x in range(len(lines[y])):
            if(lines[y][x]) == '#':
                data.append((x,y))
    
    return data

def getVisibleTo(loc1, locations):
    visible = []

    for loc2 in locations:

        if loc1 == loc2:
            continue

        points = get_points(loc1, loc2)

        points.remove(loc1)
        points.remove(loc2)

        blocked = False
        for point in points:
            if point == loc1 or point == loc2:
                continue

            if point in locations:
                blocked = True
                break

        if not blocked:
            visible.append(loc2)
    
    return visible

def findAllVisible(locations):
    
    visible = {}

    for loc1 in locations:
        visible[loc1] = getVisibleTo(loc1, locations)
        
    return visible

def angle(a, b):
    return atan2(b[0] - a[0], a[1] - b[1]) % (2 * pi)

def destroyAsteroids(loc, locations):

    locations.remove(loc)
    # How to make sure i'm going clockwise?
    vis = getVisibleTo(loc, locations)
    locations.sort(key=lambda b: hypot(b[0] - loc[0], b[1] - loc[1]))

    ranks = {b : sum(angle(loc, b) == angle(loc, c) for c in locations[:i])
        for i, b in enumerate(locations)}
    x, y = sorted(locations, key=lambda b: (ranks[b], angle(loc, b)))[199]

    return x * 100 + y

#y = get_points((1,0), (6,1))          
asteroids = loadInput('Day10input.txt')

def visible(asteroids, a):
    return len(set(angle(a, b) for b in asteroids if a != b))

loc = max(asteroids, key=lambda a: visible(asteroids, a))
print(destroyAsteroids(loc, asteroids))