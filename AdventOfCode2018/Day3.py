import re

#lines = open('Day3Example.txt').readlines()
lines = open('Day3input.txt').readlines()


w,h = 1000,1000
fabric = [[[] for x in range(w)] for y in range(h)] 

claims = set([])

#10 @ 529,203: 10x21

def fillClaims(lines):
	regex = '\#\s*(\d+)\s*\@\s*(\d+)\,(\d+)\:\s*(\d+)x(\d+)'
	for line in lines:
		
		match = re.search(regex, line)
		
		claim_id = int(match.group(1))
		left = int(match.group(2))
		top = int(match.group(3))
		width = int(match.group(4))
		height = int(match.group(5))
		
		if claim_id not in claims:
			claims.add(claim_id)
			
		for i in range(left, left+width):
			for j in range(top, top+height):
				
				fabric[i][j].append(claim_id)
	
	return fabric, claims

def countOverlapClaims(matrix):
	count = 0
	for i in range(w):
		for j in range(h):
			if len(matrix[i][j]) > 1:
				count = count + 1
		

	return count
	
def fineNonOverlapClaims(matrix):
	overlapped_claims = set([])
	
	for i in range(w):
		for j in range(h):
			if len(matrix[i][j]) > 1:
				for id in matrix[i][j]:
					if id not in overlapped_claims:
						overlapped_claims.add(id)
	
	return overlapped_claims

matrix, claim_set = fillClaims(lines)
overlaps = countOverlapClaims(matrix)

print (overlaps)

over_claims = fineNonOverlapClaims(matrix)

x = claim_set - over_claims

print(x)
