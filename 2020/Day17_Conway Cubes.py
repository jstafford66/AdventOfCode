import LoadInput
from TwoDimensionGrid import TwoDGrid

debug = False

if debug:
    lines = LoadInput.LoadLines('d17ex.txt')
else:
    lines = LoadInput.LoadLines('d17input.txt')

def parseInput(lines):

    cubes = TwoDGrid(default_value=0)

    height = len(lines)
    width = 0
    for y in range(len(lines)):
        row = lines[y].strip()
        width = len(row)
        for x in range(len(row)):
            cube = 1 if row[x] == '#' else 0
            cubes.SetPointVal((x,y,0,0), cube)
    
    return cubes, width, height

def getOcupideAdj(pos, cubes):

    test = [(-1,-1,-1,-1), (0,-1,-1,-1), (1,-1,-1,-1), (-1,0,-1,-1), (0,0,-1,-1), (1,0,-1,-1), (-1,1,-1,-1), (0,1,-1,-1), (1,1,-1,-1),
        (-1,-1,0,-1),  (0,-1,0,-1),  (1,-1,0,-1),  (-1,0,0,-1), (0,0,0,-1), (1,0,0,-1),  (-1,1,0,-1),  (0,1,0,-1),  (1,1,0,-1),
        (-1,-1,1,-1),  (0,-1,1,-1),  (1,-1,1,-1),  (-1,0,1,-1),  (0,0,1,-1),  (1,0,1,-1),  (-1,1,1,-1),  (0,1,1,-1),  (1,1,1,-1),
        (-1,-1,-1,0), (0,-1,-1,0), (1,-1,-1,0), (-1,0,-1,0), (0,0,-1,0), (1,0,-1,0), (-1,1,-1,0), (0,1,-1,0), (1,1,-1,0),
        (-1,-1,0,0),  (0,-1,0,0),  (1,-1,0,0),  (-1,0,0,0),            (1,0,0,0),  (-1,1,0,0),  (0,1,0,0),  (1,1,0,0),
        (-1,-1,1,0),  (0,-1,1,0),  (1,-1,1,0),  (-1,0,1,0),  (0,0,1,0),  (1,0,1,0),  (-1,1,1,0),  (0,1,1,0),  (1,1,1,0),
        (-1,-1,-1,1), (0,-1,-1,1), (1,-1,-1,1), (-1,0,-1,1), (0,0,-1,1), (1,0,-1,1), (-1,1,-1,1), (0,1,-1,1), (1,1,-1,1),
        (-1,-1,0,1),  (0,-1,0,1),  (1,-1,0,1),  (-1,0,0,1),  (0,0,0,1), (1,0,0,1),  (-1,1,0,1),  (0,1,0,1),  (1,1,0,1),
        (-1,-1,1,1),  (0,-1,1,1),  (1,-1,1,1),  (-1,0,1,1),  (0,0,1,1),  (1,0,1,1),  (-1,1,1,1),  (0,1,1,1),  (1,1,1,1)]

    ocupied = 0

    for adj in test:
        p = pos
        p = (int(p[0]+adj[0]), int(p[1]+adj[1]), int(p[2]+adj[2]),int(p[3]+adj[3]))
        cube = cubes.GetSnapShotPoint(p)
        ocupied += cube
    
    return ocupied

def runRules(cubes, pos):
    changed = False
    cube = cubes.GetSnapShotPoint(pos)

    ocupied = getOcupideAdj(pos, cubes)

    if cube == 1 and (ocupied == 2 or ocupied == 3):
        cubes.SetPointVal(pos, 1)
    elif cube == 1:
        cubes.SetPointVal(pos, 0)
        changed = True
    elif cube == 0 and ocupied == 3:
        cubes.SetPointVal(pos, 1)
        changed = True
    elif cube == 0:
        cubes.SetPointVal(pos, 0)

    return changed

def countOccupied(cubes):
    count = cubes.countWithValue(1)
    return count

def runSim(cubes, count):

    #print("Cycle 0")
    #cubes.print3D()

    for it in range(count):
        cubes.SnapShot()

        x_min, x_max = cubes.getXBounds()
        y_min, y_max = cubes.getYBounds()
        z_min, z_max = cubes.getZBounds()
        w_min, w_max = cubes.getWBounds()

        w = w_min-1
        while w <= w_max+1:
            z = z_min-1
            while z <= z_max+1:
                y = y_min-1
                while y <= y_max+1:
                    x = x_min-1
                    while x <= x_max+1:
                        pos = (x,y,z,w)
                        runRules(cubes, pos)
                        x+=1
                    y+=1
                z+=1
            w+=1

        #print("Cycle", it+1)
        #cubes.print3D()           
    
    ocupied = countOccupied(cubes)

    return ocupied

cubes, width, height = parseInput(lines)

print('answer:', runSim(cubes, 6))