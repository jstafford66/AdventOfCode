import LoadInput

debug = False

if debug:
    lines = LoadInput.LoadLines('d22ex2.txt')
else:
    lines = LoadInput.LoadLines('d22input.txt')

def parseInput(lines):
    player1 = []
    player2 = []

    process_p1 = True
    for line in lines:
        line = line.strip()

        if line == "Player 1:":
            process_p1 = True
        elif line == "Player 2:":
            process_p1 = False
        elif line == '':
            continue
        else:
            if process_p1:
                player1.append(int(line))
            else:
                player2.append(int(line))
    
    return player1, player2

def playCombat(player1, player2):

    rnd = 0
    while len(player1) != 0 and len(player2) != 0:
        rnd +=1
        p1 = player1.pop(0)
        p2 = player2.pop(0)

        if p1 > p2:
            player1.append(p1)
            player1.append(p2)
        else:
            player2.append(p2)
            player2.append(p1)
    
    if len(player1) > 0:
        return player1
    else:
        return player2

def playRecursCombat(player1, player2):
    
    p1_prev = []
    p2_prev = []

    rnd = 0
    while len(player1) != 0 and len(player2) != 0:
        rnd+=1

        # if this is the start of a new round:
        # test the end game...
        if player1 in p1_prev or player2 in p2_prev:
            print('Infinite Rule')
            return player1, 1
        
        p1_prev.append(player1.copy())
        p2_prev.append(player2.copy())

        p1 = player1.pop(0)
        p2 = player2.pop(0)

        # Should we play recursive combat?
        if len(player1) >= p1 and len(player2) >= p2:
            print('Playing SubGame')
            sub_p1 = player1.copy()[0:p1]
            sub_p2 = player2.copy()[0:p2]
            win_deck, win_player = playRecursCombat(sub_p1, sub_p2)

            if win_player == 1:
                player1.append(p1)
                player1.append(p2)
            else:
                player2.append(p2)
                player2.append(p1)

        else:
            if p1 > p2:
                player1.append(p1)
                player1.append(p2)
            else:
                player2.append(p2)
                player2.append(p1)
    
    if len(player1) > 0:
        return player1, 1
    else:
        return player2, 2

def scoreHand(deck):

    score = 0
    for card_index, card in enumerate(reversed(deck)):
        score += card * (card_index+1)
    
    return score

def part1(player1, player2):
    
    winner = playCombat(player1, player2)

    ans = scoreHand(winner)

    return ans

def part2(player1, player2):
    win_deck, win_player = playRecursCombat(player1, player2)

    ans = scoreHand(win_deck)
    return ans

player1, player2 = parseInput(lines)

#print(part1(player1, player2))

print(part2(player1, player2))