import LoadInput
import math
import re

debug = False

if debug:
    lines = LoadInput.LoadLines('d14ex.txt')
else:
    lines = LoadInput.LoadLines('d14input.txt')

def parseInput(lines):

    addr_re = 'mem\[(\d+)\]'

    instructions = []
    for line in lines:
        parts = line.strip().split(' ')
        if parts[0] == 'mask':
            instructions.append({'mask':parseMask(parts[2])})
        else:
            match = re.findall(addr_re, parts[0])

            instructions.append({'addr':int(match[0]), 'value':int(parts[2])})
    
    return instructions

def parseMask(mask):

    bits ={}
    for index, bit in enumerate(mask):
        if bit != 'X':
            bits[index] = bit
    
    return bits

def maskValue(value, mask):
    bits = list(format(value,'#038b')[2:])

    for index, bit in mask.items():
        bits[index] = bit
    
    result = int(''.join(bits), 2)
    return result
    
def getAddresses(addr, start=0):

    addresses = []

    address = []
    if start > 0:
        address = addr[0:start]

    for index in range(start, len(addr)):
        bit = addr[index]
        if bit != 'X':
            address.append(bit)
        else:
            addr[index] = '1'
            addresses += getAddresses(addr, index)
            addr[index] = '0'
            addresses += getAddresses(addr, index)
            addr[index] = 'X'
            break
    
    if len(addresses) == 0:
        addresses.append(address)

    return addresses

def decodeAddr(addr, mask):
    bits = list(format(addr,'#038b')[2:])

    addresses = []
    for index, bit in enumerate(bits):
        if index in mask:
            if mask[index] == '1':
                bits[index] = mask[index]
        else:
            bits[index] = 'X'
    
    addresses = getAddresses(bits)

    for index, address in enumerate(addresses):
        addresses[index] = int(''.join(address), 2)
    
    return addresses

'''"{0:b}".format(37)'''

def runInstructions(instructions):

    memory = {}

    mask = None

    for index, inst in enumerate(instructions):

        if 'mask' in inst:
            mask = inst['mask']
            continue

        value = maskValue(inst['value'], mask)
        memory[inst['addr']] = value
    
    return memory

def runInstructions2(instructions):

    memory = {}

    mask = None

    for index, inst in enumerate(instructions):

        if 'mask' in inst:
            mask = inst['mask']
            continue

        addresses = decodeAddr(inst['addr'], mask)

        for addr in addresses:
            memory[addr] = inst['value']
    
    return memory

def part1(memory):

    total = 0
    for addr, value in memory.items():
        total += value
    
    return total

instructions = parseInput(lines)
memory = runInstructions2(instructions)

print(part1(memory))
