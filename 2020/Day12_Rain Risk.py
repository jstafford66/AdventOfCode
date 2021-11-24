import LoadInput
import math

debug = False

if debug:
    lines = LoadInput.LoadLines('d12ex.txt')
else:
    lines = LoadInput.LoadLines('d12input.txt')

def parseInput(lines):

    instructions = []

    for line in lines:
        cmd = line[0]
        amt = int(line[1:])
        instructions.append((cmd,amt))
    
    return instructions

north = 0
east = 90
south = 180
west = 270

def calcNewDir(cur, amt):
    cur += amt
    cur = cur % 360
    return cur

'''
Action N means to move north by the given value.
Action S means to move south by the given value.
Action E means to move east by the given value.
Action W means to move west by the given value.
Action L means to turn left the given number of degrees.
Action R means to turn right the given number of degrees.
Action F means to move forward by the given value in the direction the ship is currently facing.
'''

def runInstructions(instructions):
    n_pos = 0
    e_pos = 0
    face = east

    for inst in instructions:
        cmd = inst[0]
        amt = inst[1]

        if cmd == 'N':
            n_pos += amt
        elif cmd == 'S':
            n_pos -= amt
        elif cmd == 'E':
            e_pos += amt
        elif cmd == 'W':
            e_pos -= amt
        elif cmd == 'L':
            face = (face - amt) % 360
        elif cmd == 'R':
            face = (face + amt) % 360
        elif cmd == 'F':
            if face == north:
                n_pos += amt
            elif face == south:
                n_pos -= amt
            elif face == east:
                e_pos += amt
            elif face == west:
                e_pos -= amt
            else:
                print ("WAT", face)
        else:
            print("huh?", cmd)
    
    return n_pos, e_pos, face

def runInstructions2(instructions):
    n_pos = 0
    e_pos = 0
    face = east

    way_n = 1
    way_e = 10

    for inst in instructions:
        cmd = inst[0]
        amt = inst[1]

        if cmd == 'N':
            way_n += amt
        elif cmd == 'S':
            way_n -= amt
        elif cmd == 'E':
            way_e += amt
        elif cmd == 'W':
            way_e -= amt
        elif cmd == 'L':
            if amt == 90:
                n = way_n
                way_n = way_e * 1
                way_e = n * -1
            elif amt == 180:
                way_n = way_n * -1
                way_e = way_e * -1
            elif amt == 270:
                n = way_n
                way_n = way_e * -1
                way_e = n * 1
            else:
                print('amt?', amt)
            #face = (face - amt) % 360
        elif cmd == 'R':
            if amt == 90:
                n = way_n
                way_n = way_e * -1
                way_e = n * 1
            elif amt == 180:
                way_n = way_n * -1
                way_e = way_e * -1
            elif amt == 270:
                n = way_n
                way_n = way_e * 1
                way_e = n * -1
            else:
                print('amt?', amt)
            #face = (face + amt) % 360
        elif cmd == 'F':
            n_pos += way_n * amt
            e_pos += way_e * amt
        else:
            print("huh?", cmd)
    
    return n_pos, e_pos, face

def part1(instructions):
    n, e, d = runInstructions(instructions)

    dist = abs(n) + abs(e)

    return dist

def part2(instructions):
    n, e, d = runInstructions2(instructions)

    dist = abs(n) + abs(e)

    return dist


instructions = parseInput(lines)

print(part2(instructions))