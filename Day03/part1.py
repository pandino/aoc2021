DIGITS=30

def most_common(numbers, position):
    transposed = list(zip(*numbers))
    ones = sum(1 for digit in transposed[position] if digit == '1')
    if ones >= (len(transposed[position]) - ones):
        return '1'
    return '0'

def less_common(numbers, position):
    transposed = list(zip(*numbers))
    ones = sum(1 for digit in transposed[position] if digit == '1')
    if ones < (len(transposed[position]) - ones):
        return '1'
    return '0'

def bin_to_dec(digits):
    result = 0
    for digit in (int(digit) for digit in digits):
        result = result << 1
        result = result | digit
    return result

with open('Day03/input.txt', 'r', encoding='utf8') as f:
    result = []
    raw_numbers = f.readlines()
    numbers = (number.strip() for number in raw_numbers)
    transposed = zip(*numbers)
    for digits in transposed:
        ones = sum(1 for digit in digits if digit == '1')
        if ones >= (len(digits)//2):
            result.append(1)
        else:
            result.append(0)
    gamma = 0
    epsilon = 0
    for digit in result:
        gamma = gamma << 1
        gamma = gamma | digit
    for digit in (1 if digit == 0 else 0 for digit in result):
        epsilon = epsilon << 1
        epsilon = epsilon | digit
    print(f'Day03, Part 1. Gamma: {gamma}; Epsilon: {epsilon}; Result: {gamma * epsilon}')

    # Part 2
    numbers = [number.strip() for number in raw_numbers]
    for i in range(DIGITS):
        reference = most_common(numbers, i)
        numbers = [number for number in numbers if number[i] == reference]
        if len(numbers) == 1:
            break
    oxygen = bin_to_dec(numbers[0])

    numbers = [number.strip() for number in raw_numbers]
    for i in range(DIGITS):
        reference = less_common(numbers, i)
        numbers = [number for number in numbers if number[i] == reference]
        if len(numbers) == 1:
            break
    co2 = bin_to_dec(numbers[0])

    print(f'Day03, Part 2. Oxygen: {oxygen}; CO2: {co2}; Result: {oxygen * co2}')
