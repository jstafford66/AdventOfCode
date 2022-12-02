import LoadInput

debug = False

if debug:
    lines = LoadInput.LoadLines('Day1ex.txt')
else:
    lines = LoadInput.LoadLines('Day1input.txt')

def p1(lines):
    calories = []
    pack = []

    for line in lines:
        if line == "":
            calories.append(pack)
            pack = []
        else:
            pack.append(int(line))
    
    calories.append(pack)
    totals = [sum(p) for p in calories]
    totals.sort()
    m = max(totals)

    l = totals[-3:]
    s = sum(l)
    return m, s
d
print(p1(lines))