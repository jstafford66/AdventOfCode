from IntComp import intComp, loadDayInput

# Black : 0 (Default)
# White : 1

# Out 1 : Color to paint
# out 2 : Direction (Left: 0, Right: 1)

class robot:

    black = 0
    white = 1

    left = 0
    right = 1

    directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]

    def __init__ (self, program):
        self.panel = {}
        self.position = (0,0)
        self.comp = intComp(program)
        self.dir = 0
    
    def start(self, initial_color):
        
        self.panel[self.position] = initial_color

        while True:
            self.comp.putInput(self.panel[self.position] if self.position in self.panel else robot.black)
            paint_color = self.comp.run()
            move_dir = self.comp.run()

            if paint_color == None or move_dir == None:
                break

            self._paintCurrentPosition(paint_color)
            self._move(move_dir)
        
        return self.panel
    
    def _paintCurrentPosition(self, color):
        self.panel[self.position] = color
    
    def _move(self, dir):
        self.dir = ((self.dir + 1) if dir == 1 else (self.dir - 1 + len(robot.directions))) % len(robot.directions)
        self.position = (self.position[0] + robot.directions[self.dir][0], self.position[1] + robot.directions[self.dir][1])


def part1():
    r = robot(loadDayInput('Day11input.txt'))
    panels = r.start(robot.black)
    print(len(panels))

def part2():
    r = robot(loadDayInput('Day11input.txt'))
    panels = r.start(robot.white)

    mx = max([p[0] for p in panels.keys()])
    my = max([p[1] for p in panels.keys()])

    for row in range(my+5):
        txt = ''
        for col in range(mx+5):
            color = panels.get((col, row), robot.black)
            txt += ' '  if color == robot.black else '#'
        
        print (txt)

part2() #HBGLZKLF
