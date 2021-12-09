from pprint import pprint

test_data = '16,1,2,0,4,2,7,1,2,14'

with open('Day07/input.txt', 'r') as f:
    input_data = f.readline()

source = input_data

def fuel_consumed(state, position):
    return sum(abs(point - position) for point in state)


input_data = [int(d) for d in source.split(',')]
ordered_points = set(input_data)
start_index = 0
end_index = max(ordered_points) 

while True:
    middle_index = start_index + ((end_index - start_index) // 2)
    middle_fuel = fuel_consumed(input_data, middle_index)
    middle_fuel_next = fuel_consumed(input_data, middle_index+1)
    if middle_fuel > middle_fuel_next:
        start_index = middle_index + 1
    else:
        end_index = middle_index
    if start_index == end_index:
        break

final_fuel = fuel_consumed(input_data, start_index)
print(f'Day07; Part1; Minimum fuel consumed: {final_fuel}')
        
    
