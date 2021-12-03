with open('input.txt', 'r', encoding='utf8') as input_data:
    h_position = 0
    depth = 0
    for line in input_data:
        direction, amount = line.split()
        amount = int(amount)
        if 'forward' in direction:
            h_position += amount
        elif 'down' in direction:
            depth += amount
        elif 'up' in direction:
            depth -= amount
    print(f'Day 02; Part 1; Answer: {h_position * depth}')

with open('input.txt', 'r', encoding='utf8') as input_data:
    h_position = 0
    depth = 0
    aim = 0
    for line in input_data:
        direction, amount = line.split()
        amount = int(amount)
        if 'forward' in direction:
            h_position += amount
            depth += aim * amount
        elif 'down' in direction:
            aim += amount
        elif 'up' in direction:
            aim -= amount
    print(f'Day 02; Part 2; Answer: {h_position * depth}')