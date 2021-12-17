from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])

def neightbors(height_map, current):
   yield height_map[current.y-1][current.x] if current.y - 1 >= 0 else None 
   yield height_map[current.y+1][current.x] if current.y + 1 < len(height_map) else None 
   yield height_map[current.y][current.x-1] if current.x - 1 >= 0 else None 
   yield height_map[current.y][current.x+1] if current.x + 1 < len(height_map[0]) else None

with open('Day09/input.txt') as f:
    puzzle_map = []
    for line in f:
        puzzle_map.append([int(i) for i in line.strip()])

    solution = []
    for y, row in enumerate(puzzle_map):
        for x, p in enumerate(row):
            if p < min(n for n in neightbors(puzzle_map, Point(x, y)) if n is not None):
                solution.append(p)
    print(f'Day09; Part 1; Sum: {sum(s + 1 for s in solution)}')