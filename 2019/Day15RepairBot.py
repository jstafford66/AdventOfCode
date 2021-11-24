from IntComp import intComp, loadDayInput
from TwoDimensionGrid import TwoDGrid

"""
The remote control program executes the following steps in a loop forever:

Accept a movement command via an input instruction.
Send the movement command to the repair droid.
Wait for the repair droid to finish the movement operation.
Report on the status of the repair droid via an output instruction.
Only four movement commands are understood: north (1), south (2), west (3), and east (4). Any other command is invalid. The movements differ in direction, but not in distance: in a long enough east-west hallway, a series of commands like 4,4,4,4,3,3,3,3 would leave the repair droid back where it started.

The repair droid can reply with any of the following status codes:

0: The repair droid hit a wall. Its position has not changed.
1: The repair droid has moved one step in the requested direction.
2: The repair droid has moved one step in the requested direction; its new position is the location of the oxygen system.
"""

inputs = []

class RepairBot:

    north = 1
    south = 2
    west = 3
    east = 4

    # Assume we are going to search clockwise
    directions = [north, east, south, west]
    convert = {1:0, 2:2, 3:3, 4:1}

    wall = 0
    space = 1
    end = 2

    def __init__(self, program, start):
        self.comp = intComp(program, waitForIn=True)
        # start assuming we are going north
        self.dir = 0
        self.position = start
        self.start = start
        self.map = TwoDGrid(default_value=' ')
    
    def search(self, replay):

        self.map.SetPointVal(self.position, 'O')

        visited = []

        inputs = []

        found = False
        while not self.comp.halted and not found:

            # Rotate in a circle and see what is in all directions
            # updte the map with what is found
            rotate = 0
            while rotate < 4:
                status = self.comp.run()
                if self.comp.waiting:
                    self.comp.putInput(RepairBot.directions[self.dir])
                
                status = self.comp.run()

                moved, end, new_pos = self._processStatus(status)

                if moved:
                    # if this happens the program will move the robot.
                    # We want it to stay here for the rotating
                    # so send a move command to get back to where we were
                    self.comp.putInput(self._getOpositeDir(RepairBot.directions[self.dir]))
                    status = self.comp.run()
                if end:
                    found = True
                    self.position = new_pos
                    break

                # Rotate the bot for the next Check
                self.dir = self._getNextDir()
                rotate += 1
                #self.printMap()
            
            self.printMap()

            if found:
                break

            if replay:
                i = replay.pop(0)
            else:
                # Allow user to manually select move
                print(inputs)
                print('north ^ (1), south v (2), west < (3), and east > (4)')
                i = input("Move:")
                while i not in ['1','2','3','4']:
                    i = input("Move:")
                
                i = int(i)

            self.dir = RepairBot.convert[i]

            # Now that we have the next direction:
            # Need to send a command to move there
            self.comp.putInput(i)
            status = self.comp.run()
            moved, end, new_pos = self._processStatus(status)
            if moved:
                inputs.append(i)
                visited.append(self.position)
                self.position = new_pos
            
            if end:
                found = True

        return self.position
    
    def map_ship(self, start):

        self.position = start
        self.map = TwoDGrid(default_value=' ')
        moves = []

        # contains directions (value) we haven't attempted for each
        # coordinate (key)
        unexplored = {}

        while True:
            
            if self.position not in unexplored:
                unexplored[self.position] = [1, 2, 3, 4]
            
            if unexplored[self.position]:
                backtrack = False
                move = unexplored[self.position].pop()
            
            else:
                backtrack = True

                if not moves: # At the start
                    return self.map

                prev = moves.pop()
                move = self._getOpositeDir(prev)
            
            self.dir = RepairBot.convert[move]
            self.comp.putInput(move)
            status = self.comp.run()

            moved, end, new_pos = self._processStatus(status)

            if moved:
                self.position = new_pos

                if not backtrack:
                    moves.append(move)


    def _updateMap(self, tile):
        new_pos = self._getNextPos()
        self.map.SetPointVal(new_pos, tile)
        return new_pos
    
    def _getNextPos(self):
        direction = RepairBot.directions[self.dir]
        if direction == RepairBot.north:
            new_pos = (self.position[0], self.position[1]-1)
        elif direction == RepairBot.south:
            new_pos = (self.position[0], self.position[1]+1)
        elif direction == RepairBot.west:
            new_pos = (self.position[0]-1, self.position[1])
        elif direction == RepairBot.east:
            new_pos = (self.position[0]+1, self.position[1])
        
        return new_pos

    def _processStatus(self, status):
        moved = False
        end = False
        new_pos = self.position

        if status == RepairBot.wall:
            self._updateMap('#')
        elif status == RepairBot.space:
            new_pos = self._updateMap('.')
            moved = True
        elif status == RepairBot.end:
            new_pos = self._updateMap('!')
            moved = True
            end = True
        
        return moved, end, new_pos

    def _getNextDir(self):
        direction = self.dir + 1 if self.dir < (len(RepairBot.directions)-1) else 0
        return direction

    def _getOpositeDir(self, direction):
        if direction == RepairBot.north:
            new_dir = RepairBot.south
        elif direction == RepairBot.south:
            new_dir = RepairBot.north
        elif direction == RepairBot.east:
            new_dir = RepairBot.west
        elif direction == RepairBot.west:
            new_dir = RepairBot.east
        
        return new_dir

    def _openSpace(self, position):
        # is the space at position open?
        tile = self.map.GetPoint(position)
        open_space = tile == ' ' or tile == '.' or tile == 'O'
        return open_space

    def _visited(self, position):
        visted = self.map.GetPoint(position)
        return visted != ' '
    
    def printMap(self):
        self.map.SetPointVal(self.start, '0')
        hold = self.map.GetPoint(self.position)
        self.map.SetPointVal(self.position, 'X')
        self.map.print()
        self.map.SetPointVal(self.position, hold)
        print('---------------------------------------------------------')


start = (0,0)

bot = RepairBot(loadDayInput('day15input.txt'), start)

#end = bot.search([3, 3, 3, 3, 3, 3, 2, 2, 4, 4, 4, 4, 2, 2, 2, 2, 4, 4, 2, 2, 4, 4, 1, 1, 1, 1, 4, 4, 4, 4, 2, 2, 4, 4, 1, 1, 1, 1, 4, 4, 4, 4, 1, 1, 1, 1, 3, 3, 1, 1, 1, 1, 1, 1, 3, 3, 3, 3, 2, 2, 2, 2, 4, 4, 2, 2, 2, 2, 3, 3, 1, 1, 3, 3, 2, 2, 3, 3, 1, 1, 1, 1, 3, 3, 1, 1, 1, 1, 1, 1, 1, 1, 3, 3, 1, 1, 3, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 4, 4, 2, 2, 4, 4, 3, 3, 3, 3, 3, 3, 3, 3, 1, 1, 3, 3, 3, 3, 3, 3, 2, 2, 3, 3, 1, 1, 3, 3, 2, 2, 3, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 4, 4, 2, 2, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 2, 2, 3, 3, 3, 3, 3, 3, 2, 2, 3, 3, 1, 1, 3, 3, 3, 3, 2, 2, 4, 4, 3, 3, 1, 1, 4, 4, 4, 4, 2, 2, 4, 4, 4, 4, 4, 4, 4, 4, 2, 2, 1, 1, 3, 3, 3, 3, 3, 3, 1, 1, 4, 4, 4, 4, 4, 4, 1, 1, 1, 1, 1, 1, 3, 3, 2, 2, 3, 3, 1, 1, 3, 3, 1, 1, 3, 3, 1, 1, 1, 1, 3, 3, 2, 2, 3, 3, 1, 1, 3, 3, 2, 2, 2, 2, 4, 4, 4, 4, 2, 2, 4, 4, 2, 2])

m = bot.map_ship((0,0))

#m.print()

def flood(m, pos, dist=0):
    if m.GetPoint(pos) == '#':
        return dist - 1

    m.SetPointVal(pos, "#")
    n1, n2, n3, n4 = get_neighbours(pos)

    return max(flood(m, n1, dist + 1),
            flood(m, n2, dist + 1),
            flood(m, n3, dist + 1),
            flood(m, n4, dist + 1))

def make_move(position, direction):
    moves = {RepairBot.north: (0, 1), RepairBot.south: (0, -1), RepairBot.west: (-1, 0), RepairBot.east: (1, 0)}
    return tuple(map(sum, zip(position, moves.get(direction))))


def get_neighbours(pos):
    return [make_move(pos, direction) for direction in range(1, 5)]

oxygen_location = None
for coordinate in m.grid.keys():
    if m.grid[coordinate] == '!':
        oxygen_location = coordinate
        break

print (flood(m, oxygen_location))
green = 5

