from IntComp import intComp, loadDayInput
from TwoDimensionGrid import TwoDGrid
import functools

class Arcade:

    """ 
    0 is an empty tile. No game object appears in this tile.
    1 is a wall tile. Walls are indestructible barriers.
    2 is a block tile. Blocks can be broken by the ball.
    3 is a horizontal paddle tile. The paddle is indestructible.
    4 is a ball tile. The ball moves diagonally and bounces off objects.
    """
    tiles = [' ', 'W', '#', '_', 'o']

    def __init__(self, program):
        self.comp = intComp(program, waitForIn=True)
        self.grid = TwoDGrid(default_value=' ')
        self.score = 0
        self.ball_x = 0
        self.player_x = 0
    
    def play(self):

        x = 0
        y = 0
        t = 0

        while not self.comp.halted:
            
            x = self.comp.run()
            y = self.comp.run()
            t = self.comp.run()

            if self.comp.halted:
                break

            # The computer will return None if it is waiting for input
            # handle input scenario before trying to handle output
            if self.comp.waiting:
                action = 0
                if self.ball_x < self.player_x:
                    action = -1
                elif self.ball_x > self.player_x:
                    action = 1
                self.comp.putInput(action)
                # Continue here to get the computer to run again
                continue

            # Handle the score next because it isn't part of the field
            if x == -1 and y == 0:
                self.score = t
                print(self.score)
                continue

            # Save the field
            self.grid.SetPointVal((x,y), Arcade.tiles[t])

            # Track the ball
            if t == 4:
                self.ball_x = x
            # Track the player
            if t == 3:
                self.player_x = x
        
        return self.score

def part1():
    arc = Arcade(loadDayInput('Day13input.txt'))
    arc.play()
    arc.grid.print()

    blocks = list(arc.grid.grid.values()).count(Arcade.tiles[2])
    print(blocks)

def part2():
    prog = loadDayInput('Day13input.txt')
    #set to free mode
    prog[0] = 2

    arc = Arcade(prog)
    score = arc.play()
    blocks = list(arc.grid.grid.values()).count(Arcade.tiles[2])

    if blocks > 0:
        print("Lost")
    else:
        print("Won")
    
    print(score)

part2()