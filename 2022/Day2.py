import LoadInput

debug = False

if debug:
    lines = LoadInput.LoadLines('Day2ex.txt')
else:
    lines = LoadInput.LoadLines('Day2input.txt')

rps = {'A':1,'B':2,'C':3,'X':1,'Y':2,'Z':3}

combat = {
    'A':['C','Z'],'X':['C','Z'],
    'B':['A','X'],'Y':['A','X'],
    'C':['B','Y'],'Z':['B','Y'],
}

combat2 = {
    'A':'Y',
    'B':'Z',
    'C':'X',
}

scoring = {'L':0,'D':3,'W':6}

def play(a,b):
    score = rps[b]

    # b lose
    if b in combat[a]:
        score += 0
    # a lose
    elif a in combat[b]:
        score += 6
    else:
        score += 3
    
    return score

def play1(lines):
    score = 0

    for a,b in [l.split() for l in lines]:
        score += play(a,b)
    
    return score

def play2(lines):
    score = 0

    for a,b in [l.split() for l in lines]:

        # lose
        if b == 'X':
            score += play(a, combat[a][0])

        # draw
        elif b == 'Y':
            score += play(a, a)
        else:
            score += play(a, combat2[a])
    
    return score

print(play2(lines))
