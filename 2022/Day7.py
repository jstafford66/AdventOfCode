import LoadInput
import re
import math

debug = False

if debug:
    lines = LoadInput.LoadLines('Day7ex.txt')
else:
    lines = LoadInput.LoadLines('Day7input.txt')


def updateParentSize(current_dir, size):
    current_dir['size'] += size
    if current_dir['parent']:
        updateParentSize(current_dir['parent'], size)


def parseinput(lines):

    root = {'parent':None, 'dirs':{}, 'files':{}, 'size':0 }

    current_dir = root

    for line in lines:
        # command line
        if str.startswith(line, '$'):
            cmd = line[2:4]

            if cmd == 'cd':
                cd_dir = line[5:]
                if cd_dir == '/':
                    current_dir = root
                elif cd_dir == '..':
                    current_dir = current_dir['parent']
                else:
                    current_dir = current_dir['dirs'][cd_dir]
            elif cmd == 'ls':
                continue
        elif str.startswith(line, 'dir'):
            current_dir['dirs'][line[4:]] = {'parent':current_dir, 'dirs':{}, 'files':{}, 'size':0 }
        else:
            size, file = line.split(' ')
            current_dir['files'][file] = {'parent':current_dir, 'dirs':None, 'files':None, 'size':int(size) }
            updateParentSize(current_dir, int(size))

    return root

def getAllDirSizes(startdir):

    dirs = []

    if startdir['dirs']:
        for d in startdir['dirs']:
            dirs.append((d, startdir['dirs'][d]['size']))
            dirs.extend(getAllDirSizes(startdir['dirs'][d]))
        
    return dirs


def part1(lines):
    ans1 = 0

    root = parseinput(lines)

    dir_sizes = getAllDirSizes(root)

    small = [d[1] for d in dir_sizes if d[1] <= 100000]
    ans1 = sum(small)

    maxsize = 70000000
    minfree = 30000000

    free_size = maxsize - root['size']
    need = minfree - free_size

    bigger = [d[1] for d in dir_sizes if d[1] >= need]
    ans2 = min(bigger)

    return ans1, ans2

print(part1(lines))
