import LoadInput

debug = False

if debug:
    lines = LoadInput.LoadLines('Day1ex.txt')
else:
    lines = LoadInput.LoadLines('Day1input.txt')


def part1(lines):
    green = 5

    prev = -1
    increase = -1
    for l in lines:
        if int(l) > prev:
            increase += 1
        
        prev = int(l)
    
    return increase

def part2(lines):

    depths = [int(l) for l in lines]
    prev_sum = -1
    increase = -1
    for index in range(len(depths)-2):
        a = depths[index:index+3]
        a_s = sum(a)
        if a_s > prev_sum:
            increase +=1

        prev_sum = a_s
    
    return increase

print(part2(lines))