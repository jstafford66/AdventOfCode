import LoadInput
import re
import math
from TwoDimensionGrid import TwoDGrid

debug = False

day = 10

if debug:
    lines = LoadInput.LoadLines('Day{0}ex.txt'.format(day))
else:
    lines = LoadInput.LoadLines('Day{0}input.txt'.format(day))

def parseinput(lines):

    stack = []

    for line in lines:
        split = line.split(' ')

        cmd = split[0]
        if len(split) == 1:
            input = 0
        else:
            input = int(split[1])

        stack.append((cmd, input))
    
    return stack

def part1(lines):
    ans1 = 0
    ans2 = 0

    cmd_stack = parseinput(lines)

    cycle = 0
    cmd_cycles = {'noop':1, 'addx':2}

    x_register = 1
    update_cycle = -1

    #20th, 60th, 100th, 140th, 180th, and 220th cycles
    intersting_cycles = [20,60,100,140,180,220]
    signal_strengths = []

    current_cmd = None

    screen = TwoDGrid(default_value='.')
    screen_coord = (0,0)
    cur_sprite_range = [-1,0,1]

    while True:
        cycle += 1

        if cycle in intersting_cycles:
            signal_strengths.append(x_register * cycle)
        
        if not current_cmd:
            current_cmd = cmd_stack.pop(0)
            update_cycle = cycle + cmd_cycles[current_cmd[0]] - 1

        # draw pixel
        if screen_coord[0] in cur_sprite_range:
            screen.SetPointVal(screen_coord, '#')
        else:
            screen.SetPointVal(screen_coord, '.')
        
        screen_coord = (screen_coord[0]+1,screen_coord[1])
        if (cycle % 40) == 0:
            screen_coord = (0, screen_coord[1]+1)

        if cycle == update_cycle:
            x_register += current_cmd[1]
            cur_sprite_range = list(range(x_register-1,x_register+2))
            current_cmd = None
            update_cycle = -1
        
        if len(cmd_stack) == 0 and not current_cmd:
            print(cycle)
            break
    
    ans1 = sum(signal_strengths)
    screen.print()

    return ans1,ans2

def part2(lines):
    ans1 = 0


    return ans1

print(part1(lines))
print(part2(lines))
