import LoadInput

debug = False

if debug:
    lines = LoadInput.LoadLines('d16ex.txt')
else:
    lines = LoadInput.LoadLines('d16input.txt')

def parseInput(lines):

    rules = []
    ticket = []
    nearby = []
    
    parsing_rules = True

    index = 0
    while index < len(lines):
        line = lines[index].strip()

        if line == 'your ticket:':
            ticket = parseTicket(lines[index+1])
            #skip the next line
            index += 1
        elif line == 'nearby tickets:':
            parsing_rules = False
        elif line != "":
            if parsing_rules:
                rules.append(parseRule(line))
            else:
                nearby.append(parseTicket(line))
        
        index += 1
    
    return rules, ticket, nearby
        

def parseRule(line):
    rule = {'range':[]}
    
    parts = line.split(":")
    
    rule['name'] = parts[0]
    range_parts = parts[1].strip().split(' ')
    rule['range'] += parseRange(range_parts[0])
    rule['range'] += parseRange(range_parts[2])
    
    return rule

def parseRange(values):
    r = list(map(int,values.split('-')))
    data = [i for i in range(r[0], r[1]+1)]
    return data

def parseTicket(line):
    return list(map(int, line.split(',')))

def findInvalidValues(rules, nearby):

    invalid_values = []
    invalid_tickets = []

    for ticket in nearby:
        for val in ticket:
            valid = []
            for rule in rules:
                valid.append(val in rule['range'])
            
            if not any(valid):
                invalid_values.append(val)
                invalid_tickets.append(ticket)
    
    return invalid_values, invalid_tickets

def part1(rules, nearby):
    values = findInvalidValues(rules, nearby)

    ans = sum(values)
    return ans

def orderRules(rules, nearby):

    # for each rule, find the ticket indexes that meet the criteria in all nearby
    for rule in rules:
        valid_index = []
        invalid_index = []

        for ticket in nearby:
            for index, value in enumerate(ticket):
                rng = rule['range']
                if value in rng:
                    if index not in invalid_index and index not in valid_index:
                        valid_index.append(index)
                else:
                    if index in valid_index:
                        valid_index.remove(index)
                    invalid_index.append(index)
        
        rule['valid_index'] = valid_index
    
    taken_index = []
    process_rules = [i for i in range(len(rules))]
    
    proc_index = 0
    while len(process_rules) > 0:
        rule = rules[process_rules[proc_index]]
        if len(rule['valid_index']) == 1:
            taken_index.append(rule['valid_index'][0])
            del process_rules[proc_index]
        else:
            for i in taken_index:
                if i in rule['valid_index']:
                    rule['valid_index'].remove(i)
        
        if len(process_rules) > 0:
            proc_index = (proc_index + 1) % len(process_rules)
    
    return rules

def part2(rules, ticket, nearby):
    inv_values, inv_tickets = findInvalidValues(rules, nearby)

    for ivt in inv_tickets:
        nearby.remove(ivt)
    
    rules = orderRules(rules, nearby)

    vals = []
    for rule in rules:
        if 'departure' in rule['name']:
            vals.append(ticket[rule['valid_index'][0]])
    
    ans = 1
    for v in vals:
        ans *= v
    
    return ans

rules, ticket, nearby = parseInput(lines)

print(part2(rules, ticket, nearby))