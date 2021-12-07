import LoadInput

debug = False

if debug:
    positions = LoadInput.LoadCSV('Day7ex.txt')
else:
    positions = LoadInput.LoadCSV('Day7input.txt')

def part1(positions):

    max_pos = max(positions)
    min_pos = min(positions)

    fuel_consump = []

    for pos in range(min_pos, max_pos+1):
        fuel_consump.append(sum([abs(sub - pos) for sub in positions]))

    return min(fuel_consump)

def part2(positions):

    max_pos = max(positions)
    min_pos = min(positions)

    fuel_consump = []

    for pos in range(min_pos, max_pos+1):
        fuel_consump.append(sum([sum(range(1, abs(sub - pos)+1)) for sub in positions]))

    return min(fuel_consump)

print(part2(positions))