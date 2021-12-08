from collections import defaultdict
from pprint import pprint

def simulator(state, days):
    for day in range(days):
        new_state = defaultdict(int)
        for t in sorted(state):
            if t == 0:
                new_state[6] += state[0]
                new_state[8] += state[0]
            else:
                new_state[t - 1] += state[t]
        state = new_state
    return sum(new_state.values())

test = '3,4,3,1,2'
initial = [int(i) for i in test.split(',')]
state = defaultdict(int)
for i in initial:
    state[i] += 1
total = simulator(state, 80)

print(f'Day06; Part1; Test Dataset; Total fishes: {total}')

with open('Day06/input.txt', 'r') as f:
    initial = (int(i) for i in f.readline().split(','))
state = defaultdict(int)
for i in initial:
    state[i] += 1
total = simulator(state, 80)

print(f'Day06; Part1; Input; Total fishes: {total}')

initial = [int(i) for i in test.split(',')]
state = defaultdict(int)
for i in initial:
    state[i] += 1
total = simulator(state, 256)

print(f'Day06; Part2; Test Dataset; Total fishes: {total}')

with open('Day06/input.txt', 'r') as f:
    initial = (int(i) for i in f.readline().split(','))
state = defaultdict(int)
for i in initial:
    state[i] += 1
total = simulator(state, 256)

print(f'Day06; Part2; Input; Total fishes: {total}')