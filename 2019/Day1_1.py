import math

debug = False

if debug:
	lines = ['100756']
else:
	input = open('Day1_1input.txt')
	lines = input.readlines()

def CalcFuelP1(line):
	return (math.floor(int(line) / 3)) - 2

def CalcFuel(line):
	total = 0
	# How much fuel does the module need
	module = CalcFuelP1(line)

	total = total + module

	# How much fuel does the fuel need?
	fuel = CalcFuelP1(module)
	while fuel > 0:
		total = total + fuel
		fuel = CalcFuelP1(fuel)
		print (str(line) + "-- " + str(fuel))

	return total

print ("GO")
sum_fuel = 0
for line in lines:
	sum_fuel = sum_fuel + CalcFuel(line)

print(sum_fuel)