
#lines = ['abcdef','bababc','abbcde','abcccd','aabcdd','abcdee','ababab']

#lines = ['abcde','fghij','klmno','pqrst','fguij','axcye','wvxyz']

lines = open('Day2_1input.txt').readlines()

twos = set([])
threes = set([])

for line in lines:
	#print(line)
	for char in ''.join(set(line)):
		num = line.count(char)
		#print(char)
		if num == 2 and line not in twos:
			twos.add(line)
			#print("two")
		elif num == 3 and line not in threes:
			threes.add(line)
			#print("three")

num_two = len(twos)
num_three = len(threes)

print(str(num_two) + " * " + str(num_three) + " = " + str(num_two * num_three))

def getDifferentIndexes(s1, s2):
	if len(s1) != len(s2):
		return[]
	return [i for i in range(len(s1)) if s1[i] != s2[i]]
	
input_len = len(lines)

oneOff = []

for line in lines:
	next = lines.index(line) + 1
	line_len = len(line) - 1
	
	while next < input_len:
		diff = getDifferentIndexes(line, lines[next])
		#print(diff)
		
		if len(diff) == 1:
			print(diff)
			print(line)
			print(lines[next])
			print(line[0:diff[0]]+line[diff[0]+1:])
			
		next = next + 1

print(oneOff)