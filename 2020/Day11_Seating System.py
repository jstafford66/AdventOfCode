import LoadInput
from TwoDimensionGrid import TwoDGrid

debug = False

if debug:
    lines = LoadInput.LoadLines('d11ex.txt')
else:
    lines = LoadInput.LoadLines('d11input.txt')

def parseInput(lines):

    seats = TwoDGrid()

    height = len(lines)
    width = 0
    for y in range(len(lines)):
        row = lines[y]
        width = len(row)
        for x in range(len(row)):
            chair = row[x]

            seats.SetPointVal((x,y), chair)
    
    return seats, width, height

def getOcupideAdj(pos, seats):

    test = [(0,-1), (0,1), (-1,0), (1,0), (-1,-1), (-1,1), (1,-1),(1,1)]

    ocupied = 0

    for adj in test:
        p = pos
        chair = '.'
        while chair == '.':
            p = (int(p[0]+adj[0]), int(p[1]+adj[1]))
            chair = seats.GetSnapShotPoint(p)
            if chair == 0:
                chair = '.'
                break

        if chair == '#':
            ocupied += 1
    
    return ocupied

def runRules(seats, pos):
    changed = False
    seat = seats.GetSnapShotPoint(pos)

    if seat == '.':
        return changed

    ocupied = getOcupideAdj(pos, seats)

    if ocupied == 0 and seat != '#':
        seats.SetPointVal(pos, '#')
        changed = True
    elif ocupied >= 5 and seat != 'L':
        seats.SetPointVal(pos, 'L')
        changed = True

    return changed

def countOccupied(seats, width, height):

    count = 0
    for w in range(width):
        for h in range(height):
            pos = (w,h)
            chair = seats.GetPoint(pos)

            if chair == '#':
                count += 1
    return count

def runSeatSim(seats, width, height):

    changed = True
    count = 0

    while changed:

        seats.SnapShot()
        changed = False

        for w in range(width):
            for h in range(height):
                pos = (w,h)

                changed |= runRules(seats, pos)           
        
        count += 1
        print(count)
        #seats.print()
    
    ocupied = countOccupied(seats, width, height)

    return ocupied

seats, width, height = parseInput(lines)

print('answer:', runSeatSim(seats, width, height))