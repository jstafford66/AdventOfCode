
import LoadInput

debug = False

if debug:
    fish = LoadInput.LoadCSV('Day6ex.txt')
else:
    fish = LoadInput.LoadCSV('Day6input.txt')


def part1(fish_list, sim_days):

    for day in range(sim_days):

        zeros = []

        for index, f in enumerate(fish_list):
            if f == 0: 
                zeros.append((index,f))
                fish_list[index] = 7

            fish_list[index] -= 1

        fish_list += [8 for f in zeros]
    
        if day % 10 == 0:
            print(day, len(fish_list))

    return len(fish_list)

def part2(fish_list, sim_days):
    fish_age = [0]*9
    for f in fish_list:
        fish_age[f] += 1
    
    for day in range(sim_days):
        zeros = fish_age.pop(0)
        fish_age[6] += zeros
        fish_age.append(zeros)

    return sum(fish_age)

print(part2(fish, 256))