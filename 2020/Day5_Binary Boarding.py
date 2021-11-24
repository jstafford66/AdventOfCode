import LoadInput
import math

debug = False

if debug:
    lines = LoadInput.LoadLines('d5ex.txt')
else:
    lines = LoadInput.LoadLines('d5input.txt')

def determineRow(input):

    min = 0
    max = 127
    
    for c in input:
        
        if c == 'F':
            max = math.floor((max-min) / 2) + min
        elif c == 'B':
            min = math.ceil((max-min) / 2) + min
    
    return max



def determineCol(input):

    min = 0
    max = 7
    
    for c in input:
        
        if c == 'L':
            max = math.floor((max-min) / 2) + min
        elif c == 'R':
            min = math.ceil((max-min) / 2) + min
    
    return max

def getSeatNumber(row, col):
    return (row * 8) + col

def getAllSeatNumbers(lines):
    seats = []

    for line in lines:
        input = line.strip()
        row = determineRow(input[0:7])
        col = determineCol(input[-3:])
        seat = getSeatNumber(row, col)

        seats.append(seat)
    
    return seats

def part1(lines):
    seats = getAllSeatNumbers(lines)
    ans = max(seats)
    return ans

def part2(lines):
    seats = getAllSeatNumbers(lines)

    l = min(seats)
    h = max(seats)

    for i in range(l, h):
        if (i not in seats) and (i + 1 in seats):
            return i

print(part2(lines))