from pprint import pprint

test_data = '16,1,2,0,4,2,7,1,2,14'

with open('Day07/input.txt', 'r') as f:
    input_data = f.readline()

source = input_data

def fuel_consumed_part1(state, position):
    return sum(abs(point - position) for point in state)


input_data = [int(d) for d in source.split(',')]
ordered_points = set(input_data)
start_index = 0
end_index = max(ordered_points) 

def solver(input_data, start_index, end_index, fuel_calculator):
    while True:
        middle_index = start_index + ((end_index - start_index) // 2)
        middle_fuel = fuel_calculator(input_data, middle_index)
        middle_fuel_next = fuel_calculator(input_data, middle_index+1)
        if middle_fuel > middle_fuel_next:
            start_index = middle_index + 1
        else:
            end_index = middle_index
        if start_index == end_index:
            break
    return fuel_calculator(input_data, start_index)

final_fuel = solver(input_data, start_index, end_index, fuel_consumed_part1)
print(f'Day07; Part1; Minimum fuel consumed: {final_fuel}')
        
def fuel_consumed_part2(state, position):
    total = 0
    for point in state:
        d = abs(point - position)
        total += d * (d + 1) // 2
    return total
    
final_fuel = solver(input_data, start_index, end_index, fuel_consumed_part2)
print(f'Day07; Part2; Minimum fuel consumed: {final_fuel}')