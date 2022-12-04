import LoadInput
import re

debug = False

if debug:
    lines = LoadInput.LoadLines('Day4ex.txt')
else:
    lines = LoadInput.LoadLines('Day4input.txt')

def part1(lines):
    
    full_lap = []
    any_lap = []

    for line in lines:
        l = line.split(',')
        one = [int(x) for x in l[0].split('-')]
        two = [int(x) for x in l[1].split('-')]

        a = set(range(one[0], one[1]+1))
        b = set(range(two[0], two[1]+1))

        inter = a & b

        if len(inter) == len(a) or len(inter) == len(b):
            full_lap.append(inter)
        
        if len(inter) > 0:
            any_lap.append(inter)
    
    return len(full_lap), len(any_lap)

print(part1(lines))
