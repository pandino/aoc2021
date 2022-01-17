from heapq import heappop, heappush
from collections import defaultdict
from platform import java_ver

# filename = 'Day15/test.txt'
filename = 'Day15/input.txt'

def a_star(map_array, size, scale, start, finish):
    def _risk(point):
        x, y = point
        x_proj = x % size[0]
        y_proj = y % size[1]
        x_sector = x // size[0]
        y_sector = y // size[1]
        risk = map_array[x_proj][y_proj] + x_sector + y_sector
        if risk > 9:
            risk += 1
        return risk % 10

    def _neightbors(point):
        x, y = point
        ns = ((x+dx, y+dy) for dx, dy in ((1, 0),(-1, 0),(0, 1),(0, -1)))
        for n in ns:
            if 0 <= n[0] < size[0]*scale and 0 <= n[1] < size[1]*scale:
                yield n

    queue = []
    heappush(queue, (0, start))
    lowest_point = {start: 0}       # The lowest total risk for each point
    previous_point = {start: None}     # The previous point from the shortest path

    while len(queue) > 0:
        current_score, current_position = heappop(queue)

        if current_position == finish:
            return ([], current_score)

        for next_point in _neightbors(current_position):
            score = current_score + _risk(next_point)
            if next_point not in lowest_point or lowest_point[next_point] > score:
                lowest_point[next_point] = score
                previous_point[next_point] = current_position
                heappush(queue, (score, next_point))

    return None


if __name__ == '__main__':
    cavern = []

    with open(filename, 'r') as f:
        for line in f:
            cavern.append([int(i) for i in line.strip()])

    y_size = len(cavern)
    x_size = len(cavern[0])
    start = (0, 0)
    finish = (x_size-1, y_size-1)

    result = a_star(cavern, (x_size, y_size), 1, start, finish)
    if result:
        lowest_path, score = result
        print(f'Day 15; Part 1; Total risk: {score}')
    else:
        print(f'No solution found)')

    scale = 5
    finish = ((x_size*scale) - 1, (y_size*scale) - 1)

    result = a_star(cavern, (x_size, y_size), scale, start, finish)
    if result:
        lowest_path, score = result
        print(f'Day 15; Part 2; Total risk: {score}')
    else:
        print(f'No solution found)')

    