
ex1 = [0,3,6]
ex2 = [1,3,2]
ex3 = [3,1,2]

data = [1,0,15,2,10,13]


def part1(start):

    num = {}

    turn = 2
    last = start[0]

    while True:

        # first get through the start list
        if (turn-1) < len(start):
            current = start[turn-1]

        # if las was first time spoken... 0
        elif last not in num.keys():
            current = 0

        # else repeat, age since last time spoken
        else:
            current = (turn-1) - num[last]
        
        num[last] = turn-1
        last = current

        if turn == 30000000:
            ans = last
            break

        #if turn % 100 == 0:
        #    print(turn, last)

        turn += 1

        if turn > 30000000:
            break

    return ans

print(part1(data))