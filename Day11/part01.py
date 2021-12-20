filename = 'Day11/input.txt'

SIZE = 10

def neightbors(x, y):
    for dy in (-1, 0, +1):
        for dx in (-1, 0, +1):
            if (dx == 0 and dy == 0) or x + dx <0 or x + dx >= SIZE or y + dy < 0 or y + dy >= SIZE:
                continue
            yield (x + dx, y + dy)
            

with open(filename, 'r') as f:
    puzzle = []
    for line in f:
        puzzle.append([int(n) for n in line.strip()])
steps = 0
flashes = 0
while steps < 1000:
    flashed = True
    steps += 1
    for y in range(SIZE):
        for x in range(SIZE):
            puzzle[y][x] += 1
    while flashed:
        flashed = False
        for y in range(SIZE):
            for x in range(SIZE):
                if puzzle[y][x] and puzzle[y][x] > 9 :
                        puzzle[y][x] = None
                        flashed = True
                        flashes += 1
                        for xp, yp in neightbors(x, y):
                            if puzzle[yp][xp] is not None:
                                puzzle[yp][xp] += 1
    for y in range(SIZE):
        for x in range(SIZE):
            if puzzle[y][x] is None:
                puzzle[y][x] = 0
    all_flashed = True
    for y in range(SIZE):
        for x in range(SIZE):
            if puzzle[y][x] != 0:
                all_flashed = False
    if all_flashed:
        print(f'Day 11; Part 02; All flashes at {steps} steps')
        break
    if steps == 100:
        print(f'Day 11; Part 01; Flashes: {flashes}')

