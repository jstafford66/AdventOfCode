
ex = False

front = 4
back = 10000

if ex:
	lines = open('Day12ex.txt').readlines()
	
else:
	lines = open('Day12in.txt').readlines()


def parseInput(lines):
	
	plants = '.'*front + lines[0][15:-1] + '.'*back
		
	n = {}	
	for i in range(2, len(lines)):
		n[lines[i][0:5]]=lines[i][9]
	
	print(n)
	print(plants)
	return plants, n 

def run(plants, n, generations):
	
	#print(len(plants))
	prev = 0
	for g in range(0, generations):
		
		#print(plants)
		next = ''
		for i in range(0, len(plants)):
			if i == 0:
				p = '..' + plants[i:i+3]
			elif i == 1:
				p = '.' + plants[i-1:i+3]
			else:
				p = plants[i-2:i+3].ljust(5,'.')
			
			#print(p,i)
			if p in n:
				#print(p, n[p])
				next = next + n[p]
			else:
				next = next + '.'
		
		#print(next)
		plants = next
		cnt = count(plants)
		print("gen:",g+1, cnt, cnt - prev)
		prev = cnt
	return plants

def count(plants):
	count = 0
	start = 0 - front
	for i in range(0,len(plants)):
		if plants[i] == '#':
			count = count + ((i - front))
	
	return count
	
plants, n = parseInput(lines)

x = count(run(plants,n, 500))
print(x)
print(((50000000000-500)*78) + x)