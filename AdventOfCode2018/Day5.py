
import re

example = 'dabAcCaCBAcCcaDA'

data = open("Day5Input.txt").read()

current = example

start = data

size = []

for x in 'abcdefghijklmnopqrstuvwxyz':
	current = start.replace(x.lower(), '').replace(x.upper(),'')
	print(x)
	print('...')
	removed = True
	while removed:
		removed = False
		for index in range(0, len(current)-1):
			
			if (current[index].islower() and current[index+1].isupper()) or (current[index].isupper() and current[index+1].islower()):
				if current[index].lower() == current[index+1].lower():
					#print("Removed: " + current[index] + current[index+1])
					current = current.replace(current[index] + current[index+1],'')
					removed = True
					break
		#print(current, len(current))
	
	size.append(len(current))
	
print(current, len(current))
print('---------------')
print(len(current))

print(min(size))