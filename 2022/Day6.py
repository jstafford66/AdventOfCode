import LoadInput
import re
import math

debug = False

if debug:
    lines = LoadInput.LoadLines('Day6ex.txt')
else:
    lines = LoadInput.LoadLines('Day6input.txt')

def parseinput(lines):
    
    return 


def part1(lines, disinct):

    input = lines[0]

    for index in range(len(input)):
        marker = input[index:index+disinct]
        test = set(marker)
        if len(marker) == len(test):
            return index + disinct

print(part1(lines,4))
print(part1(lines,14))