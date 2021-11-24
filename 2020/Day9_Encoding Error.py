import LoadInput
from itertools import combinations

debug = False

if debug:
    lines = LoadInput.LoadLines('d9ex.txt')
    preamble = 5
else:
    lines = LoadInput.LoadLines('d9input.txt')
    preamble = 25

def parseInput(lines):
    values = [int(l) for l in lines]
    return values

def isValid(val, preamb):
    pairs = set(list(combinations(preamb, 2)))
    sums = [sum(p) for p in pairs]
    valid = val in sums
    return valid

def part1(lines):

    numbers = parseInput(lines)

    for i in range(preamble, len(numbers)):
        preamb = numbers[i-preamble:i]
        val = numbers[i]
        if not isValid(numbers[i], preamb):
            return numbers[i]

def part2(lines):

    invalid = part1(lines)
    numbers = parseInput(lines)

    for length in range(2, len(numbers)):
        for i in range(len(numbers)-length):
            values = numbers[i:i+length]
            s = sum(values)
            if s == invalid:
                return min(values) + max(values)

print(part2(lines))