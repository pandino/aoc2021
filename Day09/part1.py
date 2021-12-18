from collections import namedtuple, defaultdict

Point = namedtuple('Point', ['x', 'y'])

def neightbors(height_map, current):
   yield height_map[current.y-1][current.x] if current.y - 1 >= 0 else None 
   yield height_map[current.y+1][current.x] if current.y + 1 < len(height_map) else None 
   yield height_map[current.y][current.x-1] if current.x - 1 >= 0 else None 
   yield height_map[current.y][current.x+1] if current.x + 1 < len(height_map[0]) else None

def neightbors2(height_map, current):
   yield Point(current.x, current.y-1) if current.y - 1 >= 0 else None 
   yield Point(current.x, current.y+1) if current.y + 1 < len(height_map) else None 
   yield Point(current.x-1, current.y) if current.x - 1 >= 0 else None 
   yield Point(current.x+1, current.y) if current.x + 1 < len(height_map[0]) else None

with open('Day09/input.txt') as f:
    puzzle_map = []
    for line in f:
        puzzle_map.append([int(i) for i in line.strip()])

    minimums = []
    solution = []
    for y, row in enumerate(puzzle_map):
        for x, p in enumerate(row):
            if p < min(n for n in neightbors(puzzle_map, Point(x, y)) if n is not None):
                minimums.append(Point(x, y))
                solution.append(p)
    print(f'Day09; Part 1; Sum: {sum(s + 1 for s in solution)}')

    basins = []

    for point in minimums:
        visited = set() 
        frontier = set((point, ))
        while len(frontier) > 0:
            current = frontier.pop()
            visited.add(current)
            next_points = neightbors2(puzzle_map, current)
            for next_point in next_points:
                if next_point is None or next_point in visited or puzzle_map[next_point.y][next_point.x] >= 9:
                    continue
                frontier.add(next_point)
        basins.append(len(visited))
    solution = 1
    for n in sorted(basins)[-3:]:
        solution *= n
    print(f'Day 09; Part 2; Solution: {solution}')
        
