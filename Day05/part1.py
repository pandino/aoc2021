from collections import namedtuple, defaultdict
from pprint import pprint

Point = namedtuple('Point', ['x', 'y'])
vents = []
field = defaultdict(int)

def is_horiz_or_vert(points):
    point_1, point_2 = points
    return point_1.x == point_2.x or point_1.y == point_2.y

def const(c):
    while True:
        yield c

def draw(field):
    xmax = max(x for x, _ in field.keys()) + 1
    ymax = max(y for _, y in field.keys()) + 1
    for y in range(ymax):
        for x in range(xmax):
            if (x, y) in field:
                print(field[x, y], end='')
            else:
                print('.', end='')
        print()

def draw_line(points):
    global field
    p1, p2 = points
    dx = p1.x - p2.x
    dy = p1.y - p2.y

    if dx == 0:
        gx = const(p1.x)
    else:
        m = 1 if dx < 0 else -1            
        gx = range(p1.x, p2.x + m, m)

    if dy == 0:
        gy = const(p1.y)
    else:
        m = 1 if dy < 0 else -1            
        gy = range(p1.y, p2.y + m, m)

    for x, y in zip(gx, gy):
        field[(x, y)] += 1

with open('Day05/input.txt', 'r') as f:
    for line in f:
        first_point, second_point = line.split('->')
        x1, y1 = first_point.split(',')
        x2, y2 = second_point.split(',')
        vents.append((Point(int(x1), int(y1)),
                      Point(int(x2), int(y2))))

for line in vents:
    if is_horiz_or_vert(line):
        draw_line(line)

solution1 = sum(1 for n in field.values() if n > 1)
print(f'Day05; Part1; Points: {solution1}')

field = defaultdict(int)
for line in vents:
    draw_line(line)

solution2 = sum(1 for n in field.values() if n > 1)
print(f'Day05; Part2; Points: {solution2}')