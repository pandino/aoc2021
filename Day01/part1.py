""" Advent of Code 2021. Day 1. Part 1"""

counter = 0
with open('input.txt', 'r', encoding='utf8') as f:
    last = int(f.readline())
    for heigh in (int(line) for line in f):
        if heigh > last:
            counter += 1
        last = heigh
    print(f'Day 1, part 1 solution: {counter}')

rolling_sums = [0, 0, 0, 0]
counter = 0
with open('input.txt', 'r', encoding='utf8') as f:
    heights = [int(line) for line in f]
prev = None
for i in range(len(heights)):
    if i <= len(heights) - 3:
        current = heights[i] + heights[i+1] + heights[i+2]
        if prev and (current > prev):
            counter += 1
        prev = current
print(f'Day 1, part 2 solution: {counter}')
        