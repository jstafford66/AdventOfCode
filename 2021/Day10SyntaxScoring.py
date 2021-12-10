import LoadInput
import math

debug = False

if debug:
    lines = LoadInput.LoadLines('Day10ex.txt')
else:
    lines = LoadInput.LoadLines('Day10input.txt')


def part1(lines):

    # ): 3 points.
    # ]: 57 points.
    # }: 1197 points.
    # >: 25137 points.

    points = {')':3,']':57,'}':1197,'>':25137}

    score = []

    for line in lines:
        stack = []
        corrupt = False
        for c in line.strip():
            if c in ['(','[','{','<']:
                stack.insert(0, c)
            else:
                open = stack.pop(0)

                if (open == '(' and c != ')') or (open == '[' and c != ']') or (open == '{' and c != '}') or (open == '<' and c != '>'):
                    score.append(points[c])
                    corrupt = True
                    break
    
    ans = sum(score)
    return ans

def score(str):
    # ): 1 point.
    # ]: 2 points.
    # }: 3 points.
    # >: 4 points.
    points = {')':1,']':2,'}':3,'>':4}
    score = 0

    for c in str:
        score = (score * 5) + points[c]
    
    return score

def part2(lines):
    
    completions = []
    opposites = {'(':')','[':']','{':'}','<':'>'}

    for line in lines:
        stack = []
        corrupt = False
        line = line.strip()
        for c in line:
            if c in ['(','[','{','<']:
                stack.insert(0, c)
            else:
                open = stack.pop(0)

                if (open == '(' and c != ')') or (open == '[' and c != ']') or (open == '{' and c != '}') or (open == '<' and c != '>'):
                    corrupt = True
                    break
        
        if not corrupt:
            complete = ''

            while len(stack) > 0:
                top = stack.pop(0)
                complete += opposites[top]
            
            completions.append(complete)
    
    scores = []
    for compl in completions:
        scores.append(score(compl))
    
    scores.sort()
    mid = math.floor(len(scores) / 2)
    return scores[mid]


print(part2(lines))
        
