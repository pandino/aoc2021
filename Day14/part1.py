from functools import lru_cache

filename = 'Day14/input.txt'
# filename = 'Day14/test.txt'

total_steps = 40

with open(filename, 'r') as f:
    chain = f.readline().strip() #.split()
    rules = {}
    for line in f:
        if line.strip() == '':
            continue
        a, b = line.strip().split(' -> ')
        rules[(a[0], a[1])] = b

def combine(a, b):
    c = {}
    a_values = list(a.keys())
    b_values = list(b.keys())
    for i in (a_values + b_values):
        if i in a_values and i in b_values:
            c[i] = a[i] + b[i]
        elif i in a_values:
            c[i] = a[i]
        else:
            c[i] = b[i]
    return c

cache = {}

def expand(tup, steps):
    if (tup, steps) in cache:
        return cache[(tup, steps)]
    if steps == 0 or tup not in rules:
        return {tup[1]: 1}
    insertion = rules[tup]
    left = expand((tup[0], insertion), steps-1)
    right = expand((insertion, tup[1]), steps-1)
    total = combine(left, right)
    cache[(tup, steps)] = total
    return total

def solution(total_steps):
    counter = {chain[0]: 1}
    for i in range(0, len(chain) - 1):
        element = (chain[i], chain[i+1])
        counter = combine(counter, expand(element, total_steps))
    return max(counter.values()) - min(counter.values())

print(f'Day 14; Part 1; Solution: {solution(10)}')
print(f'Day 14; Part 2; Solution: {solution(40)}')