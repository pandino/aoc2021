# source_data = 'Day08/test.txt'
source_data = 'Day08/input.txt'

parsed_data = []
with open(source_data, 'r') as f:
    for line in f:
        left_raw, right_raw = line.split('|')
        left = [set(digit) for digit in left_raw.split()]
        right = [set(digit) for digit in right_raw.split()]
        parsed_data.append({'left': left, 'output': right})

simple_digits = 0
simple_count = set([2, 4, 3, 7])
for puzzle in parsed_data:
    for digit in puzzle['output']:
        if len(digit) in simple_count:
            simple_digits += 1
print(f'Day08; Part1; Number of easy digits: {simple_digits}')
    