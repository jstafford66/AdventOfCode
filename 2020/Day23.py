from collections import deque

debug = False

if debug:
    cups = deque([int(c) for c in '389125467'])
else:
    cups = deque([int(c) for c in '469217538'])


def playCubsGame(cups, num_moves):

    lowest = min(cups)
    highest = max(cups)

    current = cups[0]

    for move in range(num_moves):
        # destination is one lower than current
        # unless it is in the removed cups
        # then sub 1 until we find one that isn't removed
        dest = current - 1

        #remove the 3 after the current
        # rotate the deque until those 3 are on the end?
        # need to insert them after the destination
        cur_index = cups.index(current)
        
        if cur_index+4 <= len(cups):
            cups.rotate(len(cups)-cur_index-4)
        else:
            cups.rotate(-1*(3 - len(cups)-cur_index))
        
        remove = [cups.pop(), cups.pop(), cups.pop()][::-1]

        while dest in remove or dest < lowest:
            dest -= 1
            if dest < min(cups):
                dest = highest

        dest_index = cups.index(dest)
        cups.rotate(len(cups)-dest_index-1)
        cups.extend(remove)

        current = cups[(cups.index(current)+1)%len(cups)]

    return cups

def getCups(point):
    # rebuild the cups list from the pointers
    final = []
    n = point[1]
    for pnt in range(1,len(point)):
        final.append(n)
        n = point[n]
        
    return final

def playCupsPoint(cups, num_moves):
    lowest = min(cups)
    highest = max(cups)

    # create an array the length of the cups list
    # there is no zero number so that's the default.
    # were not going to use index zero to simplify things
    point = [0 for i in range(len(cups)+1)]

    # every index is a number in cups. 
    # it points to the next one in the list
    for ci, cup in enumerate(cups):
        next_index = (ci+1)%len(cups)
        n = cups[next_index]
        point[cup] = n
    
    #test = getCups(point)
    current = cups[0]

    for move in range(num_moves):
        next3 = [point[current], point[point[current]], point[point[point[current]]]]

        dest = current-1
        while dest in next3 or dest < lowest:
                dest -= 1
                if dest < lowest:
                    dest = highest
        
        hold_dest = point[dest]
        hold_last = point[next3[-1]]
        point[dest] = next3[0]
        point[next3[-1]] = hold_dest
        point[current] = hold_last

        current = point[current]

        #test = getCups(point)
    
    test = getCups(point)
    return test

def addCups(cups):
    lowest = min(cups)
    highest = max(cups)

    cups += [c for c in range(highest+1, 1000001)]

    return cups

def part1(cups):

    cups = list(cups)
    index_1 = cups.index(1)
    aft1 = cups[index_1:][1:]
    bef1 = cups[:index_1]
    ans = ''.join(map(str,aft1+bef1))
    return ans

def part2(cups):
    cups = list(cups)
    index_1 = cups.index(1)
    aft1 = cups[index_1:]
    bef1 = cups[:index_1]

    res = aft1 + bef1

    two = [res[1], res[2]]
    ans = res[1] * res[2]
    return ans

# '''67384529'''
# cups = playCubsGame(cups, 100)
# print(part1(cups))

'''67384529'''
# cups = playCupsPoint(cups, 100)
# print(part1(cups))

cups = addCups(cups)
cups = playCupsPoint(cups, 10000000)

print(part2(cups))