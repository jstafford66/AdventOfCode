from os import truncate
import LoadInput

debug = False

if debug:
    lines = LoadInput.LoadLines('Day4ex.txt')
else:
    lines = LoadInput.LoadLines('Day4input.txt')

def parseInput(lines):
    numbers = []
    boards = []

    current_board = None

    for index, line in enumerate(lines):
        line = line.strip()
        if index == 0:
            numbers = line.split(',')
            continue

        # make a new board
        if line == "":
            if current_board != None:
                boards.append(current_board)
            
            current_board = []
        else:
            row = [(int(spot), 0) for spot in line.split(' ') if spot != '']
            current_board.append(row)
    
    boards.append(current_board)

    return numbers, boards

def markBoard(board, number):

    for row in board:
        for spot_index, spot in enumerate(row):
            if spot[0] == number:
                row[spot_index] = (spot[0], 1)

    return board

def testWinner(board):
    winner = False

    for row in board:
        marks = [spot[1] for spot in row]
        if sum(marks) == len(row):
            winner = True
            break

    if not winner:
        for col_index in range(len(board[0])):
            column = [row[col_index] for row in board]
            marks = [spot[1] for spot in column]

            if sum(marks) == len(column):
                winner = True
                break

    return winner

def calculateScore(board, number):

    unmarked_total = 0
    for row in board:
        unmarked = [spot[0] for spot in row if spot[1] == 0]
        unmarked_total += sum(unmarked)
    
    return unmarked_total * number
          
def part1(numbers, boards):  
    score = -1
    for numb in numbers:
        numb = int(numb)
        for board in boards:
            markBoard(board, numb)
        
        for board in boards:
            win = testWinner(board)

            if win:
                score = calculateScore(board, numb)
                break
        
        if score > -1:
            break
    return score

def part2(numbers,boards):
    winners = []

    score = -1
    for numb in numbers:
        numb = int(numb)
        for board in boards:
            markBoard(board, numb)
        
        for board_index, board in enumerate(boards):
            win = testWinner(board)

            if win and board_index not in winners:
                winners.append(board_index)
            
            if len(winners) == len(boards):
                score = calculateScore(board, numb)
                break

        if score > -1:
            break
    
    return score

numbers, boards = parseInput(lines)

print(part2(numbers, boards))
