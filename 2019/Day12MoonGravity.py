import re
from math import gcd
from functools import reduce

class moon:

    def __init__(self, position):
        self.position = position
        self.velocity = [0,0,0]
        self.start = [i for i in position]
    
    def applyGravity(self, other_moon):

        if self.position[0] > other_moon.position[0]:
            self.velocity[0] -= 1
        elif self.position[0] < other_moon.position[0]:
            self.velocity[0] += 1
        
        if self.position[1] > other_moon.position[1]:
            self.velocity[1] -= 1
        elif self.position[1] < other_moon.position[1]:
            self.velocity[1] += 1
        
        if self.position[2] > other_moon.position[2]:
            self.velocity[2] -= 1
        elif self.position[2] < other_moon.position[2]:
            self.velocity[2] += 1    
    
    def updatePosition(self):

        self.position[0] += self.velocity[0]
        self.position[1] += self.velocity[1]
        self.position[2] += self.velocity[2]
    
    def getEnergy(self):
        potential = sum([abs(x) for x in self.position])
        kinetic = sum([abs(x) for x in self.velocity])

        total = potential * kinetic
        return total
    
    def atStart(self, axis):
        val = self.position[axis] == self.start[axis] and self.velocity[axis] == 0
        return val

def loadInput(loc):
    regex = r'([\-\d]+)'

    lines = open(loc).readlines()

    moons = []

    for l in lines:
        match = re.findall(regex, l)

        moons.append(moon([int(match[0]), int(match[1]), int(match[2])]))

    return moons

def applyGravity(moons):
    for m1 in moons:
        for m2 in moons:
            if m1 == m2:
                continue
            
            m1.applyGravity(m2)
    
    return moons

def updatePositions(moons):
    for m1 in moons:
            m1.updatePosition()
    
    return moons

def getEnergy(moons):
    energy = 0
    for m in moons:
        energy += m.getEnergy()
    
    return energy

def part1(moons, steps):

    for n in range(steps):
        moons = applyGravity(moons)
        moons = updatePositions(moons)
    
    return getEnergy(moons)

moons = loadInput('day12input.txt')
#print(part1(moons, 100))
    
def _lcm(a, b):
    return (a * b) // gcd(a, b)

def lcm(lst):
    return reduce(_lcm, lst)

def part2(moons):

    lcms = {}

    steps = 0
    # need to find least common multiple for each element of position
    while len(lcms) < 3:
        moons = applyGravity(moons)
        moons = updatePositions(moons)
        
        steps += 1
        
        for axis in range(3):
            atStart = [m.atStart(axis) for m in moons]

            if axis not in lcms and all(atStart):
                lcms[axis] = steps
            
    least = lcm(lcms.values())

    return least

print(part2(moons))