
def loadinput(loc):
    x = open(loc).read()
    return x

def getLayers(data, width, height):
    layers = []

    w = 0
    h = 0

    layer = {'0':0, '1':0, '2':0, 'img':[]}
    row = ""

    for n in data:
        layer[n] = layer[n] + 1

        row += n  
        w = w + 1

        if w >= width:
            layer['img'].append(row)
            row = ""
            w = 0
            h = h + 1
        
        if h >= height:
            layers.append(layer)
            layer = {'0':0, '1':0, '2':0, 'img':[]}
            h = 0
            w = 0

    return layers

def findSmallestZeroLayer(layers):
    layer = layers[0]

    for l in layers:
        if l['0'] < layer['0']:
            layer = l
    
    return layer

def day8Part1(input, width, height):
    layers = getLayers(input, width, height)
    layer = findSmallestZeroLayer(layers)

    print("Answer: ", layer['1'] * layer['2'])

def createImg(layers, width, height):

    img = []
    for r in layers[0]['img']:
        i = []
        for s in r:
            i.append(' ')
        
        img.append(i)

    for layer in reversed(layers):

        i = layer['img']

        for h in range(height):
            for w in range(width):
                # 0 - Black, 1 - White, 2 - Trans
                if i[h][w] == '0':
                    img[h][w] = " "
                elif i[h][w] == '1':
                    img[h][w] = "#"
                # elif i[h][w] == '2':
                #     continue
    
    return img

def printImg(img):
    for r in img:
        print(''.join(r))

#day8Part1('212222222202', 3, 2)
#day8Part1(loadinput('Day8input.txt'), 25, 6)

img = createImg(getLayers(loadinput('Day8input.txt'), 25, 6), 25, 6)
printImg(img)