import LoadInput

debug = False

if debug:
    lines = LoadInput.LoadLines('d1ex.txt')
else:
    lines = LoadInput.LoadLines('d1input.txt')

def part1(lines):
    for i in range(0, len(lines)):
        for j in range(1, len(lines)):
            a = int(lines[i])
            b = int(lines[j])
            if a + b == 2020:
                return a,b

    return False

def part2(lines):
    for i in range(0, len(lines)):
        for j in range(1, len(lines)):
            for x in range(2,len(lines)):
                a = int(lines[i])
                b = int(lines[j])
                c = int(lines[x])
                if a + b + c == 2020:
                    return a,b,c

    return False

a,b = part1(lines)
print(a)
print(b)
print(a*b)

a,b,c = part2(lines)

print(a)
print(b)
print(c)
print(a*b*c)
