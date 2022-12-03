import LoadInput

debug = False

if debug:
    lines = LoadInput.LoadLines('Day3ex.txt')
else:
    lines = LoadInput.LoadLines('Day3input.txt')

def getPriority(letter):
    val = ord(letter)
    if val >= 97:
        return val - 96
    else:
        return val - 38

def part1(lines):
    s = 0

    for line in lines:
        l = int(len(line)/2)
        comp1 = set(line[0:l])
        comp2 = set(line[l:])
        same = getPriority((comp1 & comp2).pop())
        s += same
    
    return s

def part2(lines):

    s = 0

    for groups in zip(*(iter(lines),) * 3):
        same = (set(groups[0]) & set(groups[1]) & set(groups[2])).pop()
        pri = getPriority(same)
        s += pri

    return s

print(part2(lines))
