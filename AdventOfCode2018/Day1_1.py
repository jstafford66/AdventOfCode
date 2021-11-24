

#lines = ['+1', '-2', '+3', '+1']
input = open('Day1_1input.txt')

lines = input.readlines()

def update_freq(cur_freq, line):
	oper = line[0]
	val = int(line[1:])
	if(oper == '-'):
		updated_freq = cur_freq - val
	elif(oper == '+'):
		updated_freq = cur_freq + val
	return updated_freq

start_freq = 0
for line in lines:
	start_freq = update_freq(start_freq, line)

print(start_freq)

line_index = 0
freqencies = set([])
found = False
start_freq = 0
num_lines = len(lines)
loops = 0
while not found:
	
	start_freq = update_freq(start_freq, lines[line_index])
	
	if start_freq in freqencies:
		print("Duplicate: " + str(start_freq))
		break
	
	freqencies.add(start_freq)
	
	line_index = line_index + 1
	if line_index >= num_lines:
		line_index = 0
		loops = loops + 1
		print("Loop" + str(loops) + "  freq:" + str(start_freq))