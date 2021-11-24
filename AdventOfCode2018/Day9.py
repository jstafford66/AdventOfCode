from collections import deque, defaultdict

ex = False

if ex:
	data = [{'players': 9, 'stop': 25},
		{'players': 10, 'stop': 1618},
		{'players': 13, 'stop': 7999},
		{'players': 17, 'stop': 1104},
		{'players': 21, 'stop': 6111},
		{'players': 30, 'stop': 5807},
	]
else:
	data = [{'players': 466, 'stop': (71436*100)}]


def insertNext(table, current, next):
	
	if not table or len(table) == 1:
		table.append(next)
		return (len(table) - 1)

	next_i = (current+2)
	
	if next_i > len(table):
		next_i = next_i - len(table)
	
	#print("inserting at: ", next_i)
	table.insert(next_i,next)
	
	return next_i

def removeMarble(table, current):
	
	rem_index = current - 7
	if rem_index < 0:
		rem_index = len(table) + rem_index
	
	rem = table[rem_index]

	#print('Removing... current:', current, 'rem_index:', rem_index, 'die:', rem)
	
	del table[rem_index]
	#table.remove(rem)

	return rem, rem_index
	
def play(game_data):
	
	players = game_data['players']
	stop = game_data['stop']
	
	print(players, stop)
	scores = [0 for x in range(0, players)]
	table = []

	marble_score = 0
	marble_count = 0
	cindex = 0
	
	while marble_count <= stop:
		
		player_index = marble_count % players

		if marble_count > 0 and (marble_count % 23) == 0:
			#print(table)

			rmarble, cindex = removeMarble(table, cindex)
			marble_score = rmarble + marble_count
			scores[player_index] = scores[player_index] + marble_score
			
			#print('Score marble:', marble_count, 'Current I:', cindex, "Current:", table[cindex], 'Removed:', rmarble, 'Marble score:', marble_score)
			#print('*************************************************')
		else:
			cindex = insertNext(table, cindex, marble_count)
			#print(table)

		marble_count = marble_count + 1
		if marble_count % 10000 == 0:
			print(marble_count)
	
	
	high = max(scores)
	print(scores)
	print(high)

def printTable(table):
	ind = [x for x in range(0, len(table))]
	print(ind)
	print(table)

#play(data[0])


def play_game(max_players, last_marble):
    scores = defaultdict(int)
    circle = deque([0])

    for marble in range(1, last_marble + 1):
        if marble % 23 == 0:
            circle.rotate(7)
            scores[marble % max_players] += marble + circle.pop()
            circle.rotate(-1)
        else:
            circle.rotate(-1)
            circle.append(marble)

    return max(scores.values()) if scores else 0

print(play_game(466, 71436*100))
