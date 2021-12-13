import LoadInput

example = False

if example:
    lines = LoadInput.LoadLines('Day12ex.txt')
else:
    lines = LoadInput.LoadLines('Day12input.txt')

def parseInput(lines):
    map = {}

    for line in lines:
        a, b = line.split('-')

        if a not in map:
            map[a] = []
        if b not in map:
            map[b] = []
        
        map[a].append(b)
        map[b].append(a)

    return map

def findMultipleSmallCaves(path):
    small_caves = [cave for cave in path if not cave.isupper()]
    test = set(small_caves)

    return len(small_caves) != len(test)

def findPaths(map, initial, path = None):
    paths = []

    if path == None:
        path = []
    path.append(initial)

    for cave in map[initial]:
        this_path = path.copy()

        if cave == 'start':
            continue

        if not cave.isupper():
            # if there is already a small cave visited twice
            # and this cave is in there... then skip it.
            if findMultipleSmallCaves(this_path) > 0 and cave in this_path:
                continue
            
        if cave == 'end':
            this_path.append(cave)
            paths.append(this_path)
            continue

        paths += findPaths(map, cave, this_path)
    
    return paths

def part1(map):

    paths = findPaths(map, 'start')

    ans = len(paths)
    return ans

map = parseInput(lines)
print(part1(map))