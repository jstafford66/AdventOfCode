import LoadInput
from TwoDimensionGrid import TwoDGrid
import math
import itertools

debug = False

if debug:
    lines = LoadInput.LoadLines('d20ex.txt')
else:
    lines = LoadInput.LoadLines('d20input.txt')

def parseInput(lines):

    tiles = {}

    tile_index = -1
    tile_grid = []

    for line in [line.strip() for line in lines]:
        
        if line == '':
            tiles[tile_index] = {'tile':tile_grid}
            tile_grid = []
            tile_index = -1
        elif 'Tile' in line:
            tile_index = int(line.split(' ')[1][0:-1])
            y = 0
        else:
            tile_grid.append(line)
    
    tiles[tile_index] = {'tile':tile_grid}

    return tiles

def getEdges(tile):
    grid = tile['tile']
    left = []
    right = []

    for y in range(len(grid)):
        left.append(grid[y][0])
        right.append(grid[y][-1])
        
    tile['left'] = ''.join(left)
    tile['right'] = ''.join(right)
    tile['top'] = grid[0]
    tile['bottom'] = grid[-1]

    return tile

def rotateTileClockwise(tile):
    grid = tile['tile']
    rotated = [''.join(reversed(a)) for a in zip(*grid)]
    tile['tile'] = rotated
    getEdges(tile)

def filpTileVertical(tile):
    grid = tile['tile']
    flippedV = list(reversed(grid))
    tile['tile'] = flippedV
    getEdges(tile)

def flipTileHorizontal(tile):
    grid = tile['tile']
    flippedH = [row[::-1] for row in grid]
    tile['tile'] = flippedH
    getEdges(tile)

def stripBorder(tile):
    grid = tile['tile']
    image = [row[1:-1] for row in grid]
    image = image[1:-1]
    tile['img'] = image
    return image

def getMatchingSide(a,b):
    count = 0
    sides = ['left', 'right','top','bottom']
    sidea = None
    sideb = None
    orientation = None
    for s1 in sides:
        for s2 in sides:
            if a[s1] == b[s2]:
                sidea = s1
                sideb = s2
                orientation = 'F'
                count +=1
            elif a[s1] == b[s2][::-1]:
                sidea = s1
                sideb = s2
                orientation = 'R'
                count +=1
    
    return count, sidea, sideb, orientation

def FindGrid(tiles, corners):
    # put the tile indexes into an arbitray 2d array
    tile_indexes = list(tiles.keys())

    print('Tile Count:',len(tile_indexes))
    # how long are the sides of the grid?
    n = int(math.sqrt(len(tile_indexes)))
    print("Grid Size:", n)

    picture = [[] for i in range(n)]
    for j in range(n):
        picture[j] = [-1 for i in range(n)]

    first_corner = corners[0]
    picture[0][0] = first_corner
    in_picture = [first_corner]

    y = 0
    while y < n:
        reset = False
        x = 0
        while x < n-1:
            reset = False
            curr_tile_id = picture[y][x]
            curr_tile = tiles[curr_tile_id]
            # my goal is to find the neighbor that is to the right of the current tile
            for n_id in curr_tile['neighbors']:

                if n_id in in_picture:
                    continue

                neigh_tile = tiles[n_id]
                count, sa, sb, orient = getMatchingSide(curr_tile, neigh_tile)

                # tiles are rotated correctly
                # and the neighbor is to the right
                if sa == 'right':
                    if sb == 'left':
                        # neighbor tile needs to be flipped vertically to match
                        if orient == 'R':
                            filpTileVertical(neigh_tile)
                    elif sb == 'top':
                        # flip vertical and then rotate
                        filpTileVertical(neigh_tile)
                        rotateTileClockwise(neigh_tile)
                        if orient == 'R':
                            filpTileVertical(neigh_tile)
                    elif sb == 'right':
                        # flip horizontal
                        flipTileHorizontal(neigh_tile)
                        if orient == 'R':
                            filpTileVertical(neigh_tile)
                    elif sb == 'bottom':
                        rotateTileClockwise(neigh_tile)
                        if orient == 'R':
                            filpTileVertical(neigh_tile)
                    # neighbor is to the right so update the grid
                    picture[y][x+1] = n_id
                    in_picture.append(n_id)
                elif sa == 'bottom':
                    if sb == 'left':
                        rotateTileClockwise(neigh_tile)
                        if orient == 'F':
                            flipTileHorizontal(neigh_tile)
                    elif sb == 'top':
                        if orient == 'R':
                            flipTileHorizontal(neigh_tile)
                    elif sb == 'right':
                        flipTileHorizontal(neigh_tile)
                        rotateTileClockwise(neigh_tile)
                        if orient == 'F':
                            flipTileHorizontal(neigh_tile)                         
                    elif sb == 'bottom':
                        filpTileVertical(neigh_tile)
                        if orient == 'R':
                            flipTileHorizontal(neigh_tile)                        
                    # neighbor is to the bottom so update the grid
                    picture[y+1][x] = n_id
                    in_picture.append(n_id)
                elif sa == 'top':
                    if y > 0:
                        print("Flipping current row shouldn't happen")
                    # the current row all needs to flip vertically
                    for ri in range(n):
                        t_id = picture[y][ri]
                        if t_id == -1:
                            continue
                        fl_tile = tiles[t_id]
                        filpTileVertical(fl_tile)
                    x-=1
                    break
                elif sa == 'left':
                    if x > 0:
                        print("Flipping current column shouldn't happen")
                    # the current column needs to be flipped horizontally.
                    for ci in range(n):
                        t_id = picture[ci][x]
                        if t_id == -1:
                            continue
                        fl_tile = tiles[t_id]
                        flipTileHorizontal(fl_tile)
                    y-=1
                    reset = True
                    break
            if reset:
                break
            x+=1
        y+=1
                
    image = []
    for y in range(n):
        row = []
        for x in range(n):
            row.append(tiles[picture[y][x]]['tile'])
        
        image.append(row)

    return picture, image

def genImage(tiles, picture):

    ## build the gird the the tile data
    # removed the borders
    grid_img = []
    for y_index, y in enumerate(picture):
        row = []
        for x_index, tile_id in enumerate(y):
            tile = tiles[tile_id]
            tile_img = stripBorder(tile)
            row.append(tile_img)
        grid_img.append(row)
    
    # go through the new grid and combine all if the tile rows
    # to make a single image
    image = []
    for grid_row in grid_img:
        for tile_line_idex in range(len(grid_row[0])):
            line = [gc[tile_line_idex] for gc in grid_row]
            img_line = ''.join(line)
            image.append(img_line)
    
    return image

def rotateImageClockwise(image):
    rotated = [''.join(reversed(a)) for a in zip(*image)]
    return rotated

def filpImageVertical(image):
    flippedV = list(reversed(image))
    return flippedV

def flipImageHorizontal(image):
    flippedH = [row[::-1] for row in image]
    return flippedH

def parseMonster():
    monst_lines = LoadInput.LoadLines('d20monst.txt')
    monst_points = []

    height = len(monst_lines)
    for y, line in enumerate(monst_lines):
        line = line.replace('\n','')
        width = len(line)
        for x, c in enumerate(line):
            if c == '#':
                monst_points.append((x,y))
    
    return monst_points, height, width

'''
                  # 
#    ##    ##    ###
 #  #  #  #  #  #   
'''
def highlightMonsters(image, monst_points, monst_h, monst_w):
    found_monst = False
    #loop over the image to see if we can find the monster
    for y in range(len(image)-monst_h):
        row = image[y]
        for x in range(len(row)-monst_w):

            monst_match = []
            # loop over the moster points to see if we can find 
            # parts in the image that match
            for mp in monst_points:
                ip = (x+mp[0], y+mp[1])
                img_ch = image[ip[1]][ip[0]]
                if  img_ch == '#':
                    # save the image points in this list,
                    # because we are going to change them to a different char latter
                    monst_match.append(ip)
                # if there wasn't a match there really is no reason to go through the
                # whole thing
                else:
                    break
            # if we found the same number of points in the image as in the monster
            # then we found a monster.
            if len(monst_match) == len(monst_points):
                found_monst = True

                # change the image to indicate the monster we found
                for ip in monst_match:
                    row = list(image[ip[1]])
                    row[ip[0]] = '0'
                    image[ip[1]] = ''.join(row)
    
    return found_monst, image

''' rot 1, horiz 1'''
def searchImageForMonst(image):
    monst_points, monst_h, monst_w = parseMonster()
    
    rot = 0
    while rot < 4:

        horiz = 0
        while horiz < 2:

            vert = 0
            while vert < 2:
                found, image = highlightMonsters(image, monst_points, monst_h, monst_w)

                if found:
                    break
                else:
                    image = filpImageVertical(image)
                vert+=1
            
            if found:
                break
            else:
                image = flipImageHorizontal(image)
            horiz+=1
        
        if found:
            break
        else:
            image = rotateImageClockwise(image)
        rot += 1
    
    return found, image
    
def countMatchingSides(a, b):
    count = getMatchingSide(a,b)
    return count[0]

def FindCorners(tiles):
    # put the tile indexes into an arbitray 2d array
    tile_indexes = list(tiles.keys())

    print('Tile Count:',len(tile_indexes))
    # how long are the sides of the grid?
    n = int(math.sqrt(len(tile_indexes)))
    print("Grid Size:", n)

    for ti in tile_indexes:
        a = tiles[ti]
        if 'neighbors' not in a:
            a['neighbors'] = []
        for tj in tile_indexes:
            if ti == tj:
                continue

            b = tiles[tj]
            count = countMatchingSides(a,b)
            if count > 0:
                a['neighbors'].append(tj)
    
    corners = []
    for ti in tile_indexes:
        a = tiles[ti]
        if len(a['neighbors']) == 2:
            corners.append(ti)
    
    return corners

def part1(corners):
    ans = 1
    for c in corners:
        ans *= c
    return ans

def part2(image):
    cnt = 0

    for row in image:
        cnt += row.count('#')
    
    return cnt

print("Parsing Input")
tiles = parseInput(lines)

print("Loading All Edges")
for tile_index, tile in tiles.items():
    getEdges(tile)

print("finding corners")
corners = FindCorners(tiles)

print(part1(corners))

picture, image = FindGrid(tiles, corners)

image = genImage(tiles, picture)

found, image = searchImageForMonst(image)

print(part2(image))