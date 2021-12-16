import LoadInput
import itertools
from operator import itemgetter
from collections import defaultdict

example = False

if example:
    lines = LoadInput.LoadLines('Day14ex.txt')
else:
    lines = LoadInput.LoadLines('Day14input.txt')


def parseInput(lines):
    template = ''
    element_map = {}

    parse_map = False
    for line in lines:
        if line == '':
            parse_map = True
            continue

        if parse_map:
            pair, sub = line.split(' -> ')
            element_map[pair] = sub
        else:
            template = line

    return template, element_map

def defaultValue(): return 0

def parseInput2(lines):
    template = ''
    element_map = {}
    pair_counts = defaultdict(defaultValue)
    letters = []

    parse_map = False
    for line in lines:
        if line == '':
            parse_map = True
            continue

        if parse_map:
            pair, sub = line.split(' -> ')
            element_map[pair] = sub
            letters.append(pair[0])
            letters.append(pair[1])
            letters.append(sub)
        else:
            template = line
    
    pairs = [template[i:i+2] for i in range(0, len(template)-1)]
    for pair in pairs:
        pair_counts[pair] += 1
    
    letters = set(letters)
    return pair_counts, element_map, letters, template

def processStep(template, element_map):

    new_temp = [template[0]]

    for index in range(0, len(template)-1):
        key = template[index:index+2]
        insert = element_map[key]
        new_temp.append(insert)
        new_temp.append(template[index+1])
    
    return ''.join(new_temp)

def part1(template, element_map):

    for step in itertools.count():
        new_temp = processStep(template, element_map)

        if step % 4 == 0:
            print('Step:', step, 'len:', len(template))
        
        if step == 9 or step == 39:
            letters = set(list(new_temp))
            occurences = [(char, new_temp.count(char)) for char in letters]
            max_el = max(occurences, key = itemgetter(1))[1]
            min_el = min(occurences, key=itemgetter(1))[1]

            print("10th Step: len:", len(new_temp), "ans:", max_el - min_el)
            
        if step % 10 == 0:
            print(len(new_temp))

        if step == 40:
            break

        template = new_temp

def getAns(letter_count):

    counts = [count for let, count in letter_count.items()]
    return max(counts) - min(counts)

def part2(pair_counts, element_map, letters, template):

    letter_count = {let:0 for let in letters}

    for l in template:
        letter_count[l] += 1

    for step in itertools.count():

        new_pairs = pair_counts.copy()
        for pair in pair_counts:
            if pair_counts[pair] > 0:
                insert = element_map[pair]
                new_pairs[pair] -= pair_counts[pair]
                new_pairs[pair[0]+insert] += pair_counts[pair]
                new_pairs[insert+pair[1]] += pair_counts[pair]
                letter_count[insert] += pair_counts[pair]
        
        pair_counts = new_pairs
        
        if step == 4:
            count = sum([count for key, count in pair_counts.items()])
            print(count)
        if step == 9:
            print("Part1 Ans:", getAns(letter_count))
        
        if step == 39:
            print("Part2 Ans:", getAns(letter_count))
            break

# template, element_map = parseInput(lines)
# part1(template, element_map)

pair_counts, element_map, letters, template = parseInput2(lines)
part2(pair_counts, element_map, letters, template)