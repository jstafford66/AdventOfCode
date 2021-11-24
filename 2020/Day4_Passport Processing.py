import LoadInput
import copy
import re

debug = False

if debug:
    lines = LoadInput.LoadLines('d4ex2.txt')
else:
    lines = LoadInput.LoadLines('d4input.txt')

###
###byr (Birth Year)
###iyr (Issue Year)
###eyr (Expiration Year)
###hgt (Height)
###hcl (Hair Color)
###ecl (Eye Color)
###pid (Passport ID)
###cid (Country ID)
####

def part1(lines):

    valid = {
    'ecl':False, 
    'byr':False, 
    'iyr':False,
    'eyr':False,
    'hgt':False,
    'hcl':False,
    'pid':False,
    }

    
    count = 0

    current = copy.deepcopy(valid)
    for line in lines:
        if line.strip() == "":
            good = True
            for k, found in current.items():
                good = good and found
            if good:
                count = count + 1

            current = copy.deepcopy(valid)
            continue

        for k, i in current.items():
            if k in line:
                current[k] = True

    return count

def height(val):
    units = val[-2:]
    hgt = val[0:-2]

    if not hgt.isnumeric():
        return False
    
    hgt = int(hgt)

    if units == "cm" and hgt >=150 and hgt <= 193:
        return True
    
    if units == "in" and hgt >= 59 and hgt <= 76:
        return True
    
    return False


def part2(lines):

    valid = {
    'ecl':False, 
    'byr':False, 
    'iyr':False,
    'eyr':False,
    'hgt':False,
    'hcl':False,
    'pid':False,
    }

    
    '''
    byr (Birth Year) - four digits; at least 1920 and at most 2002.
    iyr (Issue Year) - four digits; at least 2010 and at most 2020.
    eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
    hgt (Height) - a number followed by either cm or in:
    If cm, the number must be at least 150 and at most 193.
    If in, the number must be at least 59 and at most 76.
    hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
    ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
    pid (Passport ID) - a nine-digit number, including leading zeroes.
    cid (Country ID) - ignored, missing or not.
    '''

    process = {
    'ecl':lambda val: val in ['amb', 'brn', 'gry', 'grn', 'hzl', 'oth', 'blu'],
    'byr':lambda val: len(val) == 4 and int(val) >= 1920 and int(val) <= 2002, 
    'iyr':lambda val: len(val) == 4 and int(val) >= 2010 and int(val) <= 2020, 
    'eyr':lambda val: len(val) == 4 and int(val) >= 2020 and int(val) <= 2030,
    'hgt':height,
    'hcl':lambda val: len(val) == 7 and len(re.findall("[0-9a-f]{6}", val[1:])) > 0,
    'pid':lambda val: len(val) == 9 and len(re.findall("\d{9}", val)) > 0
    }

    count = 0

    current = copy.deepcopy(valid)
    for line in lines:
        if line.strip() == "":
            good = True
            for k, found in current.items():
                good = good and found
            if good:
                count = count + 1

            current = copy.deepcopy(valid)
            continue

        items = line.split(' ')
        itempairs = [i.strip().split(':') for i in items]

        for p in itempairs:
            key = p[0]
            val = p[1]
            if key == 'cid':
                continue
            current[key] = process[key](val)

    good = True
    for k, found in current.items():
        good = good and found
    if good:
        count = count + 1

    return count


print(part2(lines))