
input = '286051'

recipies = [3,7]

cooks = [0,1]

def runPart1(recipies, input):

	while len(recipies) < input + 10:
		recipies = addRecipies(recipies, cooks)
		print(recipies)
		moveCooks(cooks, recipies)
	
	print(''.join(str(x) for x in recipies[input:input+11]))
		
def runPart2(recipies, input):
	
	r = ''.join(str(x) for x in recipies)
	count = 0
	while True:
		r += str(int(r[cooks[0]]) + int(r[cooks[1]]))
		cooks[0] = (cooks[0] + int(r[cooks[0]]) + 1) % len(r)
		cooks[1] = (cooks[1] + int(r[cooks[1]]) + 1) % len(r)
				
		if input in r[-len(input):]:
			x = r[0:-len(input)]
			print('Answer:', len(x))
			break;
		
		if count % 10000 == 0:
			print(count)
		count = count + 1
		
def x(input):
	score = '37'
	elf1 = 0
	elf2 = 1
	
	cnt = 0
	while input not in score[-7:]:
		score += str(int(score[elf1]) + int(score[elf2]))
		elf1 = (elf1 + int(score[elf1]) + 1) % len(score)
		elf2 = (elf2 + int(score[elf2]) + 1) % len(score)
		
		if cnt % 10000 == 0:
			print(cnt)
		cnt += 1
	
	print("ans:", score.index(input))
	
def addRecipies(recipies, cooks):
	sum = recipies[cooks[0]] + recipies[cooks[1]]
		
	if sum > 9:
		b = sum % 10
		a = int((sum - b)/10)
		recipies.append(a)
		recipies.append(b)
	else:
		recipies.append(sum)
	
	return recipies

def moveCooks(cooks, recipies):
	cooks[0] = (cooks[0] + recipies[cooks[0]] + 1) % len(recipies)
	cooks[1] = (cooks[1] + recipies[cooks[1]] + 1) % len(recipies)
	
#runPart2(recipies, input)
x(input)