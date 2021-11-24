import LoadInput

debug = False

if debug:
    lines = LoadInput.LoadLines('d19ex2.txt')
else:
    lines = LoadInput.LoadLines('d19input.txt')

def parseInput(lines):

    rules = {}
    messages = []

    parse_rules = True

    for line in lines:
        line = line.strip()

        if line == '':
            parse_rules = False
            continue

        if parse_rules:
            index, expression = parseRule(line)
            rules[index] = expression
        else:
            messages.append(line)
    return rules, messages

def parseRule(line):

    rule = line.split(':')
    index = int(rule[0].strip())

    parts = rule[1].strip().split('|')

    expression = []

    for p in parts:
        p.strip()

        if '"' in p:
            expression.append(p.replace('"', ''))
        else:
            exp = []
            for x in p.split(' '):
                if x.strip() != "":
                    exp.append(int(x))
            expression.append(exp)
    
    return index, expression

def iterateExp(rules, exp):
    if isinstance(exp, list):
        col = [[] for i in range(len(exp))]

        for col_index, r_index in enumerate(exp):
            a, b = iterateRules(rules, r_index)
            if a:
                col[col_index] += a
            if b:
                col[col_index] += b
        
        opts = []

        a_col = col[0]

        if len(col) > 1:
            b_col = col[1]
            for a in a_col:
                for b in b_col:
                    opts.append(a + b)
            
            concat = []
            if len(col) > 2:
                for o in opts:
                    for c in col[2]:
                        concat.append(o+c)
            else:
                concat = opts
        else:
            concat = a_col

        return concat
    else:
        return exp

def iterateRules(rules, index=0):

    expresssions = rules[index]

    combos = [None, None]

    exp1 = expresssions[0]
    opts = iterateExp(rules, exp1)        
    combos[0] = opts
    
    if len(expresssions) > 1:
        exp2 = expresssions[1]
        opts = iterateExp(rules, exp2)        
        combos[1] = opts

    return combos[0], combos[1]

def getValidCombos(rules):
    combos, c = iterateRules(rules)
    return combos
        
def countValidMessages(messages, valid_combos):

    count = 0
    for m in messages:
        if m in valid_combos:
            count += 1
        
        
    return count

rules, messages = parseInput(lines)

#valid_combos = getValidCombos(rules)

#print(countValidMessages(messages, valid_combos))

'''
1 or 2
8: 42 | 42 8

2 or 6
11: 42 31 | 42 11 31
'''
'''
3 : 8 11
4 : 8 8 11
5 : 8 8 8 11
6 : 8 8 8 8 11
7 : 8 8 8 8 8 11
'''
rule_combs = {3:[[42,42,31]],
4: [[42, 42, 42, 31]],
5: [[42, 42, 42, 42, 31],[42,42,42,31,31]],
6: [[42, 42, 42, 42, 42, 31], [42,42,42,42,31,31]],
7: [[42, 42, 42, 42, 42, 42, 31], [42, 42, 42, 42,42,31,31], [42,42,42,42,31,31,31]],
8: [[42, 42, 42, 42, 42, 42, 42, 31], [42,42,42,42,42,42,31,31], [42,42,42,42,42,31,31,31]],
9: [[42, 42, 42, 42, 42, 42, 42, 42, 31],[42,42,42,42,42,42,42,31,31], [42,42,42,42,42,42,31,31,31], [42,42,42,42,42,31,31,31,31]],
10: [[42, 42, 42, 42, 42, 42, 42, 42, 42, 31],[42,42,42,42,42,42,42,42,31,31], [42,42,42,42,42,42,42,31,31,31], [42,42,42,42,42,42,31,31,31,31]],
11: [[42, 42, 42,42,42,42,42,42,42,42,31],[42,42,42,42,42,42,42,42,42,31,31], [42,42,42,42,42,42,42,42,31,31,31], [42,42,42,42,42,42,42,31,31,31,31], [42,42,42,42,42,42,31,31,31,31,31]],
12: [[42,42,42,42,42,42,42,42,42,42,42,31],[42,42,42,42,42,42,42,42,42,42,31,31], [42,42,42,42,42,42,42,42,42,31,31,31], [42,42,42,42,42,42,42,42,31,31,31,31], [42,42,42,42,42,42,42,31,31,31,31,31]]
}
def part2(messages, valid42, valid31):
    max_message = max([len(m) for m in messages])

    mod_length = len(valid42[0])
    min_length = (len(valid42[0])*2) + (len(valid31[0]))
    
    valid = []
    for m in messages:
        # chunk this thing up into groups of 8
        m_split = [m[i:i+mod_length] for i in range(0, len(m), mod_length)]

        patterns = rule_combs[len(m_split)]

        for pattern in patterns:
            v = True
            for index, part in enumerate(pattern):
                if part == 42 and m_split[index] not in valid42:
                    v = False
                    break
                elif part == 31 and m_split[index] not in valid31:
                    v = False
                    break
            if v:
                valid.append(m)    
    
    ans = len(valid)

    return ans


valid42, x = iterateRules(rules, 42)

for i in x:
    valid42.append(i)

valid31, x = iterateRules(rules, 31)
for i in x:
    valid31.append(i)

print(part2(messages, valid42, valid31))