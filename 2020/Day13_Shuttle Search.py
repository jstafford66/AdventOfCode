import LoadInput
import math

debug = False

if debug:
    lines = LoadInput.LoadLines('d13ex.txt')
else:
    lines = LoadInput.LoadLines('d13input.txt')

def parseInput(lines):

    est = int(lines[0])

    bus_list = lines[1].split(',')

    return est, bus_list

def getBusTimes(est, bus):
    mod = est % bus

    early = est - mod
    future = early + bus

    return early, future

def getAllBusTimes(est, bus_list):

    times = {}

    for bus in bus_list:
        if bus != 'x':
            bus = int(bus)
            early, future = getBusTimes(est, bus)
            if early in times:
                times[early].append(bus)
            else:
                 times[early] = [bus]
            if future in times:
                times[future].append(bus)
            else:
                times[future] = [bus]
    
    return times

def part1(est, bus_list):

    times = getAllBusTimes(est, bus_list)

    n = min([key for key, val in times.items() if key >= est])

    bus = times[n]

    if len(bus) > 1:
        print("figure this out")
    
    ans = (n-est) * bus[0]
    return ans

est, bus_list = parseInput(lines)
    
print(part1(est, bus_list))

def part2(bus_list):

    id_remainder = {}

    # find expected remainder for all buses
    for i, bus in enumerate(bus_list):
        if bus == 'x':
            continue
        id_remainder[int(bus)] = int(bus) - i
    
    # find the product of all bus times
    product = 1
    for bus_id in id_remainder.keys():
        product *= bus_id
    
    # total = for each bus (remainder mod bus_id)
    # total = sum(for each bus(partial*(y) === 1 mod bus_id))
    # total = for each bus sum( partial1 * (inv(partial1) mod bus_id) * remainder1 )
    # for each bus solve CMT..  Time remainder from modulo operation
    total = 0
    for bus_id, remainder in id_remainder.items():
        # get the partial product... This is one modulo operation in CMT
        # need whole number so floor divide
        partial = product // bus_id

        # find modular multiplicative inverse to solve for CMT problem
        # this is inverse of the partial produc modulo the bus_id(time bus takes)
        # pow does this
        inverse = pow(partial, -1, bus_id)

        cmt = remainder * partial * inverse
        total += cmt
    
    #shortest time is the sum of all busses modulo the product of all busses.
    s = total % product

    return s

'''17,x,13,19'''
def iterate(bus_list):

    #fast = min([int(b) for b in bus_list if b != 'x'])
    #fast = int(bus_list[0])
    large = max([int(b) for b in bus_list if b != 'x'])
    index = bus_list.index(str(large))
    fast = large - index
    t = 0
    found = False

    while not found:
        t += fast

        f = []
        for i in range(len(bus_list)):
            bus = bus_list[i]

            if bus == 'x':
                f.append(True)
                continue
            
            x = (t+i) % int(bus)
            f.append(x == 0)

        # f = []
        # l = []
        # d = []
        # for i in range(len(bus_list)):
        #     bus = bus_list[i]
        #     if bus == 'x':
        #         l.append(t+i)
        #         d.append(1)
        #         continue

        #     early, future = getBusTimes(t, int(bus))


        found = all(f)
        print(t)

        if t >= 1068788:
            greenn = 5

        # print(d)

        # s = sum(d)
        # if s == 0:
        #     green = 5


    return t

#iterate([17,'x',13,19])

#iterate(bus_list)
#bus_list = [17,'x',13,19]
print(part2(bus_list))