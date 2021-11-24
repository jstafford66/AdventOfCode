import LoadInput
import re

debug = False

if debug:
    lines = LoadInput.LoadLines('d2ex.txt')
else:
    lines = LoadInput.LoadLines('d2input.txt')

def parseLine(line):
    ex = '(\d+)\-(\d+)\s([a-z])\:\s([a-z]+)'
    match = re.findall(ex, line)

    return match[0]

def part1(rows):
    
    foundValid = 0

    for l in rows:
        lower, upper, letter, password = parseLine(l)

        number = password.count(letter)

        if number >= int(lower) and number <= int(upper):
            foundValid = foundValid + 1
    
    return foundValid

def part2(rows):
    foundValid = 0

    for l in rows:
        lower, upper, letter, password = parseLine(l)

        if (password[int(lower)-1] == letter or password[int(upper)-1] == letter) and not (password[int(lower)-1] == letter and password[int(upper)-1] == letter):
            foundValid = foundValid + 1
    
    return foundValid

print(part2(lines))