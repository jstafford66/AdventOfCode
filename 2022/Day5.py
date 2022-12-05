import LoadInput
import re
import math

debug = False

if debug:
    lines = LoadInput.LoadLinesRaw('Day5ex.txt')
else:
    lines = LoadInput.LoadLinesRaw('Day5input.txt')

def parseinput(lines):
    
    cratestack = []
    movestack = []

    parseStack = True

    stacks = math.ceil(len(lines[0])/4)
    for s in range(0,stacks):
        cratestack.append([])

    for line in lines:
        l = line

        if line.strip() == "":
            parseStack = False
            continue

        if parseStack:
            row = []

            for s in range(0,stacks):
                crate = (l[0:3])[1].strip()
                l = l[4:]
                
                if not (crate == '') and not crate.isnumeric():
                    cratestack[s].append(crate)
        else:
            num, start, end = re.findall("move\s(\d+)\sfrom\s(\d+)\sto\s(\d+)", line)[0]
            movestack.append({'n':int(num),'s':int(start)-1,'e':int(end)-1})
    
    return cratestack, movestack, stacks


def part1(lines):

    crates, moves, numstacks = parseinput(lines)   

    for move in moves:
        f = move['s']
        t = move['e']
        n = move['n']

        items = crates[f][0:n]
        crates[f] = crates[f][n:]
        crates[t][0:0] = items
        #for i in items:
        #    crates[t].insert(0,i)
        
    ans = ''
    for s in range(0,numstacks):
        ans += crates[s][0]

    return ans

print(part1(lines))
