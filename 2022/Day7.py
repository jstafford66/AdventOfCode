import LoadInput
import re
import math

debug = False

if debug:
    lines = LoadInput.LoadLines('Day7ex.txt')
else:
    lines = LoadInput.LoadLines('Day7input.txt')

# recursive functions are fun.
def updateParentSize(current_dir, size):
    # update the current dir size
    current_dir['size'] += size
    # if the current dir has a parent, then update it's size too
    if current_dir['parent']:
        updateParentSize(current_dir['parent'], size)

def parseinput(lines):

    root = {'parent':None, 'dirs':{}, 'files':{}, 'size':0 }

    current_dir = root

    for line in lines:
        # command line
        if str.startswith(line, '$'):
            cmd = line[2:4]

            # is this a change directory
            if cmd == 'cd':
                # get the directory name
                cd_dir = line[5:]
                # if they want us to go to root
                if cd_dir == '/':
                    current_dir = root
                # if they want to go up one level
                elif cd_dir == '..':
                    current_dir = current_dir['parent']
                # move to the named directory
                # this assumes that it exists / has been processed already, probably not safe.
                else:
                    current_dir = current_dir['dirs'][cd_dir]
            # really no work for this program when it sees this command.
            elif cmd == 'ls':
                continue
        # add a directory to the current directory
        elif str.startswith(line, 'dir'):
            current_dir['dirs'][line[4:]] = {'parent':current_dir, 'dirs':{}, 'files':{}, 'size':0 }
        # add a file to the current directory
        else:
            size, file = line.split(' ')
            current_dir['files'][file] = {'parent':current_dir, 'dirs':None, 'files':None, 'size':int(size) }
            # since we know the size has changed, just update the entire directory chain now.
            updateParentSize(current_dir, int(size))

    return root

# more recursive fun
def getAllDirSizes(startdir):

    dirs = []
    # if there are directories in this directory
    # this is the exit condition, important.
    if startdir['dirs']:
        # go through every dir and get the size.
        for d in startdir['dirs']:
            # add it to the list
            dirs.append((d, startdir['dirs'][d]['size']))
            # go through the childern and add them to the list.
            dirs.extend(getAllDirSizes(startdir['dirs'][d]))
        
    return dirs


def part1(lines):
    ans1 = 0

    root = parseinput(lines)

    dir_sizes = getAllDirSizes(root)

    # give me every directory size less than or equal to ....
    small = [d[1] for d in dir_sizes if d[1] <= 100000]
    # add them togehter for part 1
    ans1 = sum(small)

    # figure out how much space we need to free up.
    maxsize = 70000000
    minfree = 30000000

    free_size = maxsize - root['size']
    need = minfree - free_size

    # find every directory bigger than that
    bigger = [d[1] for d in dir_sizes if d[1] >= need]
    # we want the smallest one bigger than that, this is part 2
    ans2 = min(bigger)

    return ans1, ans2

print(part1(lines))
