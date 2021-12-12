# source_data = 'Day08/test.txt'
source_data = 'Day08/input.txt'

from collections import defaultdict

parsed_data = []
with open(source_data, 'r') as f:
    for line in f:
        left_raw, right_raw = line.split('|')
        left = [frozenset(digit) for digit in left_raw.split()]
        right = [frozenset(digit) for digit in right_raw.split()]
        parsed_data.append({'left': left, 'output': right})

simple_digits = 0
simple_count = set([2, 4, 3, 7])
for puzzle in parsed_data:
    for digit in puzzle['output']:
        if len(digit) in simple_count:
            simple_digits += 1
print(f'Day08; Part1; Number of easy digits: {simple_digits}')

from collections import defaultdict

DIGITS = {
    0: 'abcefg',
    1: 'cf',
    2: 'acdeg',
    3: 'acdfg',
    4: 'bcdf',
    5: 'abdfg',
    6: 'abdefg',
    7: 'acf',
    8: 'abcdefg',
    9: 'abcdfg'
}

DIGITS_SET = { x: frozenset(v) for x, v in DIGITS.items() }
REVERSE_DIGIT_SET = { v: str(x) for x, v in DIGITS_SET.items() }

def solver(digits):
    mapping = {} # mapping of default segments to the one in the puzzle
    solved = {} # mapping of known number to digit
    by_length = defaultdict(set)
    for digit in digits:
        by_length[len(digit)].add(digit)
    solved[1] = by_length[2].pop()
    solved[4] = by_length[4].pop()
    solved[7] = by_length[3].pop()
    solved[8] = by_length[7].pop()
    mapping['a'] = solved[7] - solved[1]
    for digit in by_length[6]:
        r = solved[7] - digit
        if len(r) == 1:
            mapping['c'] = r
            solved[6] = digit
            break
    mapping['f'] = solved[1] - mapping['c']
    for digit in by_length[5]:
        r = digit & solved[1]
        if r == mapping['c']:
            solved[2] = digit
        elif len(r) == 2:
            solved[3] = digit
        elif r == mapping['f']:
            solved[5] = digit
        else:
            print(f'Digit unsolved {sorted(digit)}')
    mapping['b'] = solved[4] - solved[3]
    mapping['e'] = solved[6] - solved[5]
    for digit in by_length[6]:
        if solved[6] - digit == mapping['e']:
            solved[9] = digit
    mapping['d'] = solved[4] - solved[7] - mapping['b']
    mapping['g'] = solved[3] - solved[4] - mapping['a']
    return { next(iter(v)): x for x, v in mapping.items()}

digits_by_len = defaultdict(set)
for d, segs in DIGITS.items():
    digits_by_len[len(segs)].add(d)  

sum_of_outputs = 0
for puzzle in parsed_data:
    all_digits = puzzle['left'] + puzzle['output']
    mappings = solver(frozenset(all_digits))
    output = []
    for digit in puzzle['output']:
        segments = frozenset(mappings[seg] for seg in digit)
        output.append(REVERSE_DIGIT_SET[segments])
    sum_of_outputs += int(''.join(output))

print(f'Day08; Part2; Solution: {sum_of_outputs}')