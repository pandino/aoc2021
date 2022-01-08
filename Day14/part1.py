# filename = 'Day14/input.txt'
filename = 'Day14/test.txt'

steps = 10

with open(filename, 'r') as f:
    chain = f.readline().strip() #.split()
    rules = {}
    for line in f:
        if line.strip() == '':
            continue
        a, b = line.strip().split(' -> ')
        rules[(a[0], a[1])] = b

for _ in range(steps):
    new_chain = [chain[0]]
    for i in range(0, len(chain) - 1):
        element = (chain[i], chain[i+1])
        if element in rules:
            new_chain.append(rules[element])
            new_chain.append(chain[i+1])
        else:
            new_chain.append(chain[i+1])
    chain = new_chain

counter = {}
for c in chain:
    if c in counter:
        counter[c] += 1
    else:
        counter[c] = 1

print(f'Day 14; Part 1; Solution: {max(counter.values()) - min(counter.values())}')