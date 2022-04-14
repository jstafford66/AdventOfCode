import LoadInput
from math import floor, ceil
from copy import deepcopy

example = False

if example:
    lines = LoadInput.LoadLines('Day18ex.txt')
else:
    lines = LoadInput.LoadLines('Day18input.txt')


def parseInput(lines):
    numbers = []

    for line in [list(line) for line in lines]:
        numbers.append(parseNumber(line))
    
    return numbers

def parseNumber(line):

    number = []
    depth = 0

    for ch in line:
        if ch == '[':
            depth += 1
        elif ch == ']':
            depth -= 1
        elif ch == ',':
            continue
        else:
            number.append({'v':int(ch), 'd':depth})
    
    return number

def incrementDepth(number):
    for num in number:
        num['d'] += 1
    return number

def addNumbers(left, right):
    result = incrementDepth(left)
    result += incrementDepth(right)

    return result

def reduceNumber(number):
    
    finished_reducing = False
    while not finished_reducing:
        depth = calcDepth(number)
        # explode until all depth < 5
        while depth > 4:
            number = explodeNum(number)
            depth = calcDepth(number)

        # split large numbers
        if needsSplit(number):
            number = splitNum(number)
        depth = calcDepth(number)
        finished_reducing = (depth < 5) and not needsSplit(number)
    
    return number

def explodeNum(number):
    
    for index, num in enumerate(number):
        if num['d'] > 4:
            # this value moves the first number to the left, if there is one
            if index - 1 >= 0:
                number[index-1]['v'] += number[index]['v']
            # the value next to this one moves to the first number to the right
            # if there is one
            if index + 2 < len(number):
                number[index+2]['v'] += number[index+1]['v']
            
            # replace this number with zero at a lower depth
            number[index] = {'v':0, 'd':num['d']-1}
            # remove the next value
            number.pop(index+1)
            break

    return number

def splitNum(number):

    for index, num in enumerate(number):
        val = num['v']
        depth = num['d']
        if val > 9:
            left, right = getSplitValue(val)
            number[index]['v'] = left
            number[index]['d'] = depth+1

            number.insert(index+1, {'v': right, 'd': depth+1})
            break
    
    return number

def getSplitValue(integer):
    left = floor(integer / 2)
    right = ceil(integer / 2)
    return left, right

def calcDepth(number):
    depths = [num['d'] for num in number]
    largest = max(depths)

    return largest

def needsSplit(number):
    values = [num['v'] for num in number]
    largest = max(values)
    return largest > 9

def numberToStr(number):

    num_copy = number.copy()
    num = num_copy.pop(0)
    last_depth = num['d']
    str_number = '['*last_depth + str(num['v'])

    while len(num_copy) > 0:
        num = num_copy.pop(0)
        value = num['v']
        depth = num['d']

        if last_depth < depth:
            str_number += ',' + '['*(depth - last_depth)
        elif last_depth > depth:
            str_number += ']'*(last_depth-depth) + ','
        elif last_depth == depth:
            str_number += ','
        
        last_depth = depth
        str_number += str(value)
    
    str_number += ']'*(last_depth)
    
    return str_number

def sumInput(numbers):

    while len(numbers) > 1:
        left = numbers.pop(0)
        right = numbers.pop(0)

        result = addNumbers(left, right)
        result = reduceNumber(result)
        numbers.insert(0, result)
    
    result = numbers[0]
    return result

def calcMagnatude(number):

    copy_num = number.copy()

    index = 0
    while index < len(copy_num)-1:
        left = copy_num[index]
        right = copy_num[index+1]

        if left['d'] == right['d']:
            mag = (left['v']*3) + (right['v']*2)
            copy_num.insert(index, {'v':mag, 'd':left['d']-1})
            copy_num.pop(index+1)
            copy_num.pop(index+1)
            index = 0
            continue

        index +=1
    
    return copy_num[0]['v']

# # Test parsing input
# print(numberToStr(parseInput(['[1,2]'])[0])=='[1,2]')
# print(numberToStr(parseInput(['[[1,2],3]'])[0])=='[[1,2],3]')
# print(numberToStr(parseInput(['[9,[8,7]]'])[0])=='[9,[8,7]]')
# print(numberToStr(parseInput(['[[1,9],[8,5]]'])[0])=='[[1,9],[8,5]]')
# print(numberToStr(parseInput(['[[[[1,2],[3,4]],[[5,6],[7,8]]],9]'])[0])=='[[[[1,2],[3,4]],[[5,6],[7,8]]],9]')
# print(numberToStr(parseInput(['[[[9,[3,8]],[[0,9],6]],[[[3,7],[4,9]],3]]'])[0])=='[[[9,[3,8]],[[0,9],6]],[[[3,7],[4,9]],3]]')
# print(numberToStr(parseInput(['[[[[1,3],[5,3]],[[1,3],[8,7]]],[[[4,9],[6,9]],[[8,2],[7,3]]]]'])[0])=='[[[[1,3],[5,3]],[[1,3],[8,7]]],[[[4,9],[6,9]],[[8,2],[7,3]]]]')

# # Test exploding 5 True
# test1 = parseInput(['[[[[[9,8],1],2],3],4]'])
# print(numberToStr(explodeNum(test1[0])) == '[[[[0,9],2],3],4]')
# test2 = parseInput(['[7,[6,[5,[4,[3,2]]]]]'])
# print(numberToStr(explodeNum(test2[0])) == '[7,[6,[5,[7,0]]]]')
# print(numberToStr(explodeNum(parseInput(['[[6,[5,[4,[3,2]]]],1]'])[0])) == '[[6,[5,[7,0]]],3]')
# test5 = parseInput(['[[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]]'])
# print(numberToStr(explodeNum(test5[0])) == '[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]')
# print(numberToStr(explodeNum(parseInput(['[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]'])[0])) == '[[3,[2,[8,0]]],[9,[5,[7,0]]]]')

# test9 = parseInput(['[[[[4,0],[5,0]],[[[4,5],[2,6]],[9,5]]],0]'])
# print(numberToStr(explodeNum(test9[0]))== '[[[[4,0],[5,4]],[[0,[7,6]],[9,5]]],0]')

# # Test Splitting 1 True
# split_test = parseInput(['[[[[[4,3],4],4],[7,[[8,4],9]]],[1,1]]'])
# print(numberToStr(reduceNumber(split_test[0])) == '[[[[0,7],4],[[7,8],[6,0]]],[8,1]]')

# print(calcMagnatude(parseNumber(list('[[1,2],[[3,4],5]]'))) == 143)

def part2(numbers):

    largest = 0

    for left_index in range(len(numbers)-1):
        for right_index in range(len(numbers)):
            if left_index == right_index:
                continue

            left = deepcopy(numbers[left_index])
            right = deepcopy(numbers[right_index])
            result = addNumbers(left, right)
            result = reduceNumber(result)
            result = calcMagnatude(result)
            largest = max(result, largest)

            right = deepcopy(numbers[left_index])
            left = deepcopy(numbers[right_index])
            result = addNumbers(left, right)
            result = reduceNumber(result)
            result = calcMagnatude(result)
            largest = max(result, largest)
    
    return largest

numbers = parseInput(lines)

# #part 1
# sum_result = sumInput(numbers)
# print(calcMagnatude(sum_result))

print(part2(numbers))