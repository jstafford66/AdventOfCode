import LoadInput

debug = False

if debug:
    lines = LoadInput.LoadLines('Day2ex.txt')
else:
    lines = LoadInput.LoadLines('Day2input.txt')


def part1(lines):
    
    horiz = 0
    depth = 0
    aim = 0
    
    for line in lines:
        cmd, amt = line.split(' ')

        if cmd == 'forward':
            horiz += int(amt)
            depth += int(amt) * aim
        elif cmd == 'down':
            aim += int(amt)
        elif cmd == 'up':
            aim -= int(amt)
        
    return horiz * depth


print(part1(lines))