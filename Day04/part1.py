from pprint import pprint

def check_board(board):
    for line in board:
        if all(digit == 'x' for digit in line):
            return board
    for line in zip(*board):
        if all(digit == 'x' for digit in line):
            return board
    return None

def sum_board(board):
    total = 0
    for line in board:
        total += sum(i for i in line if i != 'x')
    return total

def mark_board(draw, board):
    for row in board:
        for i, d in enumerate(row):
            if d == draw:
                row[i] = 'x'

draws = []
boards = []
with open('Day04/input.txt', 'r') as f:
    draws = [int(number) for number in f.readline().split(',')]
    f.readline()
    board = []
    for line in f:
        if line.strip():
            board.append([int(digits) for digits in line.split()])
        else:
            boards.append(board)
            board = []
    boards.append(board)

for draw in draws:
    winner = False
    for board in boards:
        mark_board(draw, board)
        win = check_board(board)
        if win:
            winner = True
            print(f'Day04; Part1; Draw = {draw}, Final = {draw * sum_board(board)}')
            break
    if winner:
        break


# Part 2
print('--------------')
draws = []
boards = []
with open('Day04/input.txt', 'r') as f:
    draws = [int(number) for number in f.readline().split(',')]
    f.readline()
    board = []
    for line in f:
        if line.strip():
            board.append([int(digits) for digits in line.split()])
        else:
            boards.append(board)
            board = []
    boards.append(board)

for draw in draws:
    winner = False
    for board in boards:
        mark_board(draw, board)
    for i, board in enumerate(boards):
        if check_board(board):
            if len(boards) == 1:
                winner = True
                pprint(board)
                print(f'Day04; Part2; Draw = {draw}, Final = {draw * sum_board(board)}')
                break
            del boards[i]
    if winner:
        break