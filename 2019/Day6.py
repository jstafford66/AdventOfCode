
def loadinput(loc):
    x = open(loc).readlines()
    return x

def populateNodes(orbits, parent, name):
    
    node = {'root': name, 'parent':parent, 'children':[]}

    if name not in orbits.keys():
        node['children'] = None
    else:
        for nodeName in orbits[name]:
            child = populateNodes(orbits, node, nodeName)
            node['children'].append(child)

    return node

def countOrbits(node, dist):
    total = dist
    if node['children']:
        for ch in node['children']:
            s = countOrbits(ch, dist + 1)
            total = total + s

    return total

def populateOrbitMap(definition):

    orbits = {}
    for d in definition:
        rel = d.strip().split(')')

        if rel[0] not in orbits.keys():
            orbits[rel[0]] = [rel[1]]
        else:
            orbits[rel[0]].append(rel[1])
          
    map = populateNodes(orbits, None, 'COM')
    return map

def populateOrbitMap2(definition):

    orbits = {}
    for d in definition:
        rel = d.strip().split(')')
       
        if rel[1] not in orbits.keys():
            orbits[rel[1]] = rel[0]
          
    return orbits

def pathToCom(name, orbits):

    path = []

    while name != 'COM':
        path.append(orbits[name])
        name = orbits[name]
    
    return set(path)
        

x = populateOrbitMap(loadinput('Day6text.txt'))
c = countOrbits(x,0)

print(c)

x = populateOrbitMap2(loadinput('Day6text.txt'))

y = pathToCom("YOU", x)
s = pathToCom("SAN", x)

m = len(y ^ s)

print (m)