import LoadInput
import re
import math
import ast
from TwoDimensionGrid import TwoDGrid

debug = False

day = 13

if debug:
    lines = LoadInput.LoadLines('Day{0}ex.txt'.format(day))
else:
    lines = LoadInput.LoadLines('Day{0}input.txt'.format(day))

def parseinput(lines):

    packets = []

    pair = []
    for line in lines:
        if line != "":
            list = ast.literal_eval(line)
            pair.append(list)
        else:
            packets.append(pair)
            pair = []
    
    packets.append(pair)


    return packets

# When comparing two values, the first value is called left and the second value is called right. Then:

# If both values are integers, the lower integer should come first. 
#   If the left integer is lower than the right integer, the inputs are in the right order. 
#   If the left integer is higher than the right integer, the inputs are not in the right order. 
#   Otherwise, the inputs are the same integer; continue checking the next part of the input.
# 
# If both values are lists, compare the first value of each list, then the second value, and so on. 
#   If the left list runs out of items first, the inputs are in the right order. 
#   If the right list runs out of items first, the inputs are not in the right order. 
#   If the lists are the same length and no comparison makes a decision about the order, continue checking the next part of the input.
# 
# If exactly one value is an integer, convert the integer to a list which contains that integer as its only value, 
#   then retry the comparison. For example, 
#   if comparing [0,0,0] and 2, convert the right value to [2] (a list containing 2); 
#   the result is then found by instead comparing [0,0,0] and [2].

def testPart(left, right):
    
    if isinstance(left, int) and isinstance(right, int):
        if left < right:
            return 0
        elif left == right:
            return 2
        else:
            return 1
    elif isinstance(left, list) and isinstance(right, list):
        compare_count = min(len(left), len(right))
        compare = 0
        while compare < compare_count:
            result = testPart(left[compare], right[compare])
            compare += 1
            if result == 2:
                continue
            else:
                return result
        
        # we ran out of items:
        if len(left) < len(right):
            return 0
        elif len(left) == len(right):
            return 2
        else:
            return 1
    elif isinstance(left, int) and isinstance(right, list):
        return testPart([left], right)
    elif isinstance(left, list) and isinstance(right, int):
        return testPart(left, [right])
    else:
        return -1

def part1(lines):
    ans1 = 0
    ans2 = 0

    packets = parseinput(lines)

    correct_packets = []

    for index, packet in enumerate(packets):

        left = packet[0]
        right = packet[1]

        result = testPart(left, right)
        if result == 0:
            correct_packets.append(index+1)
    
    ans1 = sum(correct_packets)

    return ans1,ans2

def part2(lines):
    ans1 = 0

    packets = parseinput(lines)

    divider_packets = [[[2]],[[6]]]

    flat_packets = [[[2]],[[6]]]
    for packet in packets:
        flat_packets.extend(packet)
    
    sorted = False
    while not sorted:

        index = 0
        sorted = True
        while index < (len(flat_packets)-1):
            result = testPart(flat_packets[index], flat_packets[index+1])
            if result == 1:
                # swap these two
                sorted = False
                swap = flat_packets.pop(index+1)
                flat_packets.insert(index, swap)

            index +=1

    divider_index = []
    for divider in divider_packets:
        found = False
        index = 0
        while not found:
            result = testPart(divider, flat_packets[index])
            if result == 2 or result == -1:
                divider_index.append(index +1)
                found = True
                break
            index += 1

    ans1 = divider_index[0] * divider_index[1]
    return ans1

print(part1(lines))
print(part2(lines))
