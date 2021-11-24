import LoadInput

debug = False

if debug:
    lines = LoadInput.LoadLines('d21ex.txt')
else:
    lines = LoadInput.LoadLines('d21input.txt')

def parseInput(lines):
    alergen_map = {}
    ingredient_map = {}
    ingredient_lists = []

    for line in lines:
        split_alergens = line.split("(")

        ingred_list = split_alergens[0].strip()
        ingredients = ingred_list.split(' ')

        ingredient_lists.append(ingredients)

        alergens = [a.strip().replace(')','') for a in split_alergens[1][len('contains'):].split(',')]

        for alergen in alergens:
            if alergen not in alergen_map:
                alergen_map[alergen] = []
            alergen_map[alergen].append(ingredients)
        
        for ingredient in ingredients:
            if ingredient not in ingredient_map:
                ingredient_map[ingredient] = set([])
            ingredient_map[ingredient] |= set(alergens)

    return alergen_map, ingredient_map, ingredient_lists

def cleanAlergenMap(alergen_map):

    clean_map = {}
    only_one = []
    for alergen, lists in alergen_map.items():
        first = set(lists[0])
        for i in range(1, len(lists)):
            first &= set(lists[i])
        
        clean_map[alergen] = list(first)

        if len(clean_map[alergen]) == 1:
            only_one.append(alergen)
    
    oi = 0
    while oi < len(only_one):
        oo = only_one[oi]
        ingred = clean_map[oo][0]
        for alergen, li in clean_map.items():
            if alergen == oo:
                continue
            if ingred in li:
                li.remove(ingred)
            if len(li) == 1 and alergen not in only_one:
                only_one.append(alergen)
        
        oi+=1
    
    return clean_map

def part1(clean_map, ingredient_map, ingredient_lists):
    ingredients = list(ingredient_map.keys())

    for alergen, li in clean_map.items():
        for ingred in li:
            if ingred in ingredients:
                ingredients.remove(ingred)

    count = 0
    for li in ingredient_lists:
        for ingred in ingredients:
            if ingred in li:
                count += 1
    return count

def part2(clean_map):
    alergens = list(clean_map.keys())
    alergens.sort()

    bad_list = ''
    for alergen in alergens:
        bad_list += clean_map[alergen][0] + ','
    
    return bad_list

alergen_map, ingredient_map, ingredient_lists = parseInput(lines)

clean_map = cleanAlergenMap(alergen_map)

print(part1(clean_map, ingredient_map, ingredient_lists))

print(part2(clean_map))