
import LoadInput
import re

debug = False

if debug:
    lines = LoadInput.LoadLines('Day8ex.txt')
else:
    lines = LoadInput.LoadLines('Day8input.txt')

parse_ex = re.compile('[a-g]+')

def ParseInput(lines):
    # displays[{patterns[], output[]}]

    displays = []

    for line in lines:
        patterns, output = line.split('|')
        displays.append({'patterns': parse_ex.findall(patterns.strip()), 'output': parse_ex.findall(output.strip())})
    
    return displays

def part1(displays):
    # find number of 1,4,7,8

    count = 0

    for display in displays:
        for out in display['output']:
            if len(out) in [2,3,4,7]:
                count += 1
    
    return count

seg_convert = {
    0:{'correct': list('abcefg'), 'len': 6, 'index':[0,1,2,4,5,6]},
    1:{'correct':list('cf'), 'len': 2, 'index':[2,5]},
    2:{'correct':list('acdeg'), 'len': 5, 'index':[0,2,3,4,6]},
    3:{'correct':list('acdfg'), 'len': 5, 'index':[0,2,3,5,6]},
    4:{'correct':list('bcdf'), 'len': 4, 'index':[1,2,3,4]},
    5:{'correct':list('abdfg'), 'len': 5, 'index':[0,1,3,5,6]},
    6:{'correct':list('abdefg'), 'len': 6, 'index':[0,1,3,4,5,6]},
    7:{'correct':list('acf'), 'len': 3, 'index':[0,2,5]},
    8:{'correct':list('abcdefg'), 'len': 7, 'index':[0,1,2,3,4,5,6]},
    9:{'correct':list('abcdfg'), 'len': 6, 'index':[0,1,2,3,5,6]}}

def determineSegments(patterns):
    # [a,b,c,d,e,f,g]
    segment = ['','','','','','','']
    ones = set([pat for pat in patterns if len(pat) == 2][0])
    fours = set([pat for pat in patterns if len(pat) == 4][0])
    sevens = set([pat for pat in patterns if len(pat) == 3][0])
    eights = set([pat for pat in patterns if len(pat) == 7][0])

    segs_6 = [set(pat) for pat in patterns if len(pat) == 6]

    # top segment is the difference between 7 and 1
    segment[0] = list(sevens - ones)[0]

    for pat in segs_6:
        missing = eights - pat
        seg = list(missing)[0]
        # if the missing value is in ones... then this is 6
        # and we know the order of c and f
        if seg in ones:
            segment[2] = list(missing)[0]
            segment[5] = list(ones - missing)[0]
        # if the missing value is in four, but not in ones then this is zero
        # then we know the missing one is d and we know b 
        elif seg in fours:
            segment[3] = seg
            segment[1] = list((fours - ones) - missing)[0]
        # if the missing value is not in 4 or ones, then this is 9
        # and we know e
        else:
            segment[4] = seg

    # now we know g because all the rest are found
    segment[6] = list(eights - set(segment))[0]  

    return segment      

def determineOutput(output, segment):
    out_digit = ''

    six = [key for key, info in seg_convert.items() if info['len'] == 6]
    five = [key for key, info in seg_convert.items() if info['len'] == 5]

    for digit in output:
        if len(digit) == 2:
            out_digit += '1'
        elif len(digit) == 3:
            out_digit += '7'
        elif len(digit) == 4:
            out_digit += '4'
        elif len(digit) == 7:
            out_digit += '8'
        elif len(digit) == 6:
            for number in six:
                letters = set([segment[index] for index in seg_convert[number]['index']])
                dif = letters - set(digit)
                if len(dif) == 0:
                    out_digit += str(number)
                    break
        elif len(digit) == 5:
            for number in five:
                letters = set([segment[index] for index in seg_convert[number]['index']])
                dif = letters - set(digit)
                if len(dif) == 0:
                    out_digit += str(number)
                    break
    
    out_value = int(out_digit)
    return out_value

def part2(displays):
    outputs = []

    for display in displays:
        segment = determineSegments(display['patterns'])
        outputs.append(determineOutput(display['output'], segment))
    
    return sum(outputs)

displays = ParseInput(lines)
print(part2(displays))