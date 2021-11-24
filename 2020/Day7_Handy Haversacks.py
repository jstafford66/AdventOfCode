import LoadInput
import re

debug = False

if debug:
    lines = LoadInput.LoadLines('d7ex.txt')
else:
    lines = LoadInput.LoadLines('d7input.txt')

def parseInput(lines):

    bagMap = {}

    for line in lines:
        line = line.strip()[0:-1]

        match = re.findall("([\w\s]+) bags contain ([\w\s,]+)", line)

        outside = match[0][0]

        container = {}
        bagMap[outside] = container

        containsbags = match[0][1]
        bag_list = containsbags.split(',')

        for bag in bag_list:
            if bag == 'no other bags':
                continue

            match = re.findall("(\d+) ([\w\s]+)bags?", bag)

            number = int(match[0][0].strip())
            color = match[0][1].strip()
            container[color] = number
        
    return bagMap
        
def getContainerBags(color, bag_map, counted=[]):

    count = 0

    for container, bags in bag_map.items():
        if color in bags:
            if container not in counted:
                count = count + 1
                counted.append(container)
            count = count + getContainerBags(container, bag_map, counted)
    
    return count

def getInsideBags(container, bag_map):
    count = 0

    for color, number in bag_map[container].items():
        count = count + number
        count = count + (getInsideBags(color, bag_map) * number)
    
    return count

bag_map = parseInput(lines)

#number = getContainerBags('shiny gold', bag_map)

number = getInsideBags('shiny gold', bag_map)

print(number)