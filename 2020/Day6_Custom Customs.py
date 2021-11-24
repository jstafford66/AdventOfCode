import LoadInput

debug = False

if debug:
    lines = LoadInput.LoadLines('d6ex.txt')
else:
    lines = LoadInput.LoadLines('d6input.txt')

def parseInput(lines):

    groups = []

    group = {'people':0, 'answers':[]}

    for li in lines:
        ans = li.strip()
        if ans == "":
            groups.append(group)
            group = {'people':0, 'answers':[]}
            continue

        group['people'] = group['people'] + 1

        for c in ans:
            if c not in group['answers']:
                group['answers'].append(c)
    
    groups.append(group)

    return groups

def part1(lines):
    groups = parseInput(lines)

    count = 0
    for g in groups:
        count = count + len(g['answers'])
    
    return count

def part2(lines):
    groups = []

    group = {'people':[]}

    for li in lines:
        ans = li.strip()
        if ans == "":
            groups.append(group)
            group = {'people':[]}
            continue

        person = []

        for c in ans:
            person.append(c)
        
        group['people'].append(person)
    
    groups.append(group)

    count = 0
    for g in groups:
        
        result = set(g['people'][0]).intersection(*g['people'])
        count = count + len(result)
    
    return count

print(part2(lines))