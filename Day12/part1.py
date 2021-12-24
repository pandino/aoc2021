from pprint import pprint
from collections import defaultdict

# filename = 'Day12/test_tiny.txt'
# filename = 'Day12/test.txt'
filename = 'Day12/input.txt'

graph = defaultdict(list)

with open(filename, 'r') as f:
    for line in f:
        a, b = line.strip().split('-')
        if a == 'start' or b == 'end':
            graph[a].append(b)
            continue
        if b == 'start' or a == 'end':
            graph[b].append(a)
            continue
        graph[a].append(b)
        graph[b].append(a)

pathes = [['start']]
ended = []
while len(pathes) > 0:
    next_pathes = []
    for path in pathes:
        next_points = graph[path[-1]]
        for next_point in next_points:
            if next_point == 'end':
                ended.append(path + [next_point])
                continue
            if next_point.isupper():
                next_pathes.append(path + [next_point])
                continue
            if next_point in path:
                continue
            next_pathes.append(path + [next_point])
    pathes = next_pathes
print(f'Day12; Part1; Pathes: {len(ended)}')

pathes = [(cave, ['start']) for cave in graph if cave != 'start' and cave.islower()]
ended = set()
while len(pathes) > 0:
    next_pathes = []
    for cave, path in pathes:
        next_points = graph[path[-1]]
        for next_point in next_points:
            if next_point == 'end':
                ended.add(tuple(path + [next_point]))
                continue
            if next_point not in path or next_point.isupper() or (next_point == cave and path.count(cave) < 2):
                next_pathes.append((cave, path + [next_point]))
    pathes = next_pathes
print(f'Day12; Part2; Pathes: {len(ended)}')