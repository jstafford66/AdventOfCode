from os import truncate
import LoadInput

debug = False

if debug:
    lines = LoadInput.LoadLines('Day3ex.txt')
else:
    lines = LoadInput.LoadLines('Day3input.txt')


def part1(lines):  
    gama = []
    epsilon = []

    bits = [list(line.strip()) for line in lines]

    digits = len(bits[0])

    for index in range(digits):
        row = [bit[index] for bit in bits]
        ones = row.count('1')
        zeros = row.count('0')

        if ones > zeros:
            gama.append(1)
            epsilon.append(0)
        else:
            gama.append(0)
            epsilon.append(1)
        
    green = 5
    gama = int("".join(str(i) for i in gama),2)
    epsilon = int("".join(str(i) for i in epsilon),2)

    return gama * epsilon

def remove(bits, bit_pos, keep_val):
    new_bits = []
    for bit in bits:
        if bit[bit_pos] == keep_val:
            new_bits.append(bit)
    
    return new_bits

def oxy(lines):
    
    bits = [list(line.strip()) for line in lines]

    digits = len(bits[0])

    bit_pos = 0

    while bit_pos < digits:
        row = [bit[bit_pos] for bit in bits]
        ones = row.count('1')
        zeros = row.count('0')

        if ones > zeros or ones == zeros:
            bits = remove(bits, bit_pos, '1')
        else:
            bits = remove(bits, bit_pos, '0')
        
        if len(bits) == 1:
            break
        
        bit_pos += 1
    
    return int("".join(str(i) for i in bits[0]),2)

def co2(lines):
    
    bits = [list(line.strip()) for line in lines]

    digits = len(bits[0])

    bit_pos = 0

    while bit_pos < digits:
        row = [bit[bit_pos] for bit in bits]
        ones = row.count('1')
        zeros = row.count('0')

        if zeros < ones or ones == zeros:
            bits = remove(bits, bit_pos, '0')
        else:
            bits = remove(bits, bit_pos, '1')
        
        if len(bits) == 1:
            break
        
        bit_pos += 1
    
    return int("".join(str(i) for i in bits[0]),2)

def part2(lines):
    ox = oxy(lines)
    c = co2(lines)

    return ox * c

print(part2(lines))
