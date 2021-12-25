from pprint import pprint
filename = 'Day13/input.txt'
# filename = 'Day13/test.txt'

points = set()
instructions = []

def fold(points, instruction):
    axes, number = instruction
    for point in list(points):
        x, y = point
        if axes == 'x':
            if x > number:
                x = (number * 2) - x
                points.remove(point)
                points.add((x, y))
        elif axes == 'y':
            if y > number:
                y = (number * 2) - y
                points.remove(point)
                points.add((x, y))

with open(filename, 'r') as f:
    for line in f:
        if not line.strip():
            break
        coords = line.split(',')
        x = int(coords[0])
        y = int(coords[1])
        points.add((x, y))
    
    for line in f:
        tokens = line.split()
        data = tokens[-1].split('=')
        instructions.append((data[0], int(data[1])))

points = frozenset(points)

day1_points = set(points)
fold(day1_points, instructions[0])
print(f'Day13; Part01; Dots after 1 folding: {len(day1_points)}')

day2_points = set(points)
for instruction in instructions:
    fold(day2_points, instruction)
xmax = max(x for x, _ in day2_points) + 1
ymax = max(y for _, y in day2_points) + 1
for y in range(ymax):
    for x in range(xmax):
        if (x, y) in day2_points:
            print('#', end='')
        else:
            print(' ', end='')
    print()