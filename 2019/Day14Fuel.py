import re
import math

def loadInput(loc):
    regex = r'^((?:\d+ [A-Z]+, )*\d+ [A-Z]+) => (\d+) ([A-Z]+)$'

    lines = open(loc).readlines()

    reactions = {}

    for line in lines:
        match = re.search(regex, line)

        output_amount = int(match.group(2))
        output = match.group(3)

        inputs = []

        for input in match.group(1).split(', '):
            input_amount, input = input.split(' ')
            inputs.append((int(input_amount), input))
        
        reactions[output] = (output_amount, inputs)

    return reactions

def CalcOre(reactions, element, need, extras):
    
    if element not in extras:
        extras[element] = 0

    # ORE is the last stop, if we are here we need to add this much ore
    if element == 'ORE':
        return need
    # If there is enough extra from other reactions to cover this
    # we don't need more ore, but adjust the extra.
    elif need <= extras[element]:
        extras[element] -= need
        return 0
    
    # use all of the extra from other reactions
    if extras[element] > 0:
        need -= extras[element]
        extras[element] = 0

    ore_needed = 0
    
    creates = reactions[element][0]
    element_inputs = reactions[element][1]

    # How many reactions are needed to get enough of the element
    # Need X , reaction creates Y (round up, can only create whole amounts)
    multiple = math.ceil(need / creates)

    for in_amount, in_element in element_inputs:
        # We need to get the right amount
        in_amount *= multiple
        # Get How much ore this element needs
        add_ore = CalcOre(reactions, in_element, in_amount, extras)
        ore_needed += add_ore
    
    # Consume this element for the reactionc
    # We Created some and consumed some
    extras[element] += (creates * multiple) - need
    
    return ore_needed


reactions = loadInput('day14input.txt')

ore_for_one = CalcOre(reactions, 'FUEL', 1, {})

total_ore = 1000000000000

start = math.ceil(total_ore / ore_for_one)

while True:
    ore_needed = CalcOre(reactions, 'FUEL', start, {})

    if ore_needed >= total_ore:
        break

    remain = total_ore - ore_needed
    more = remain / ore_for_one
    if more <= 1:
        break

    start += math.floor(more)
    print(start)

print(start) #5586022