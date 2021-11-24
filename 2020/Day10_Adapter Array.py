import LoadInput
import math

debug = False

if debug:
    lines = LoadInput.LoadLines('d10ex.txt')
else:
    lines = LoadInput.LoadLines('d10input.txt')

def parseInput(lines):
    values = [int(l) for l in lines]
    return values

def part1(values):

    values.sort()

    connects = [0,0,0]

    largest = max(values)
    mine = largest + 3

    last = 0
    values.append(mine)

    for val in values:
        dif = val - last
        last = val
        connects[dif-1] += 1

    return connects[0] * connects[2]

def buildMap(values):
    
    values.sort()
    values.reverse()

    mp = {}

    for val in values:
        nums = [i for i in values if i < val and i >= val-3]
        mp[val] = nums
    
    return mp

def getOptions(val, mp):
    count = 0

    opts = mp[val]

    if len(opts) > 1:
        count = count + len(opts)

    for option in opts:
        count = count + (getOptions(option, mp))
    
    return count

def getPaths(val, paths):
    if val in paths.keys():
        return paths[val]
    
    return 0

def part2_2(values):

    values.sort()
    largest = max(values)
    mine = largest + 3
    values.append(mine)

    paths = {}

    paths[0] = 1

    for val in values:
        paths[val] = getPaths(val-1,paths) + getPaths(val-2,paths) + getPaths(val-3,paths)
    
    m = paths[mine]
    return m

def part2(values):
    values.sort()
    mp = buildMap(values)

    count = getOptions(values[0], mp)

    return count

values = parseInput(lines)

part1(values)


print(part2_2(values))