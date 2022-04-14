import LoadInput
import re
import math
from itertools import count

example = False

if example:
    input = 'target area: x=20..30, y=-10..-5'
else:
    input = 'target area: x=195..238, y=-93..-67'

lines = LoadInput.LoadLines('Day17ex.txt')
ex_vels = []
for line in lines:
    vels = line.split(' ')
    for vel in vels:
        if vel != '':
            sp = vel.split(',')
            ex_vels.append((int(sp[0]), int(sp[1])))

def parseInput(line):
    reg = re.compile('(\-?\d+)\.\.(\-?\d+)')

    matches = reg.findall(line)

    x1 = int(matches[0][0])
    x2 = int(matches[0][1])
    y1 = int(matches[1][0])
    y2 = int(matches[1][1])

    target_area = [(min(x1,x2), max(y1, y2)),(max(x1,x2), min(y1,y2))]

    return target_area

def simTrajectory(start, velocity, target_area):
    max_h = start[1]

    x_pos, y_pos = start[0],start[1]

    x_vel, y_vel = velocity[0], velocity[1]

    step_in_target = False

    for step in count():
        x_pos = x_pos+x_vel
        y_pos = y_pos+y_vel

        max_h = max(max_h, y_pos)

        # This step is in the target area?
        if (x_pos >= target_area[0][0] and x_pos <= target_area[1][0]) and (y_pos <= target_area[0][1] and y_pos >= target_area[1][1]):
            step_in_target = True
            break
        
        # The step is past the target area?
        if (x_pos > target_area[1][0] or y_pos < target_area[1][1]):
            break

        # The step is before the target area?
        # and we are not moving in the x dir any longer
        if (y_pos <= target_area[0][1] and y_pos >= target_area[1][1]) and x_pos < target_area[0][0] and x_vel == 0:
            break

        if x_vel < 0:
            x_vel += 1
        elif x_vel > 0:
            x_vel -= 1
        
        y_vel -= 1
    
    return step_in_target, (x_pos, y_pos), max_h


def part1(target_area):
    start = (0,0)

    max_h = 0
    max_h_vel = start

    last_target = False
    past_target = False

    min_x_velocity = math.floor(math.sqrt(0-(2*-1*target_area[0][0])))

    for x in count(start=1):

        max_h_y = 0
        max_x = 0
        end_this = False
        for y in range(1,1000):
            velocity = (x,y)
            in_target, pos, full_h = simTrajectory(start, velocity, target_area)
         
            max_x = max(max_x, pos[0])
            last_target = in_target

            # We only care about max height if it achieved the target
            if not in_target:
                continue

            # if the height achieved on the last sim was lower
            # then we have moved past the needed y velocity
            if full_h < max_h_y:
                break
            # otherwise save this one
            elif full_h > max_h_y:
                max_h_y = full_h
                max_h_vel = velocity
                    
        if max_h_y > max_h:
            max_h = max_h_y
        
        # we've reeached an x veloicty that won't achieve max height
        if max_h_y < max_h:
            break

        # if past_target:
        #     break
    
    return max_h, max_h_vel

def part2(target_area):
    start = (0,0)

    starts = []

    for x in range(1, target_area[1][0]+100):
        for y in range(target_area[1][1]-1, 100):
            velocity = (x,y)
            if velocity == (6,0):
                green = 5

            in_target, pos, full_h = simTrajectory(start, velocity, target_area)

            if velocity in ex_vels and not in_target:
                green = 5

            if in_target:
                starts.append(velocity)
    
    return len(starts)

target_area = parseInput(input)

#print(part1(target_area))

print(part2(target_area))
