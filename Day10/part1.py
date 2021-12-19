filename = 'Day10/input.txt'

couples = {'(': ')',
           '[': ']',
           '{': '}',
           '<': '>'}

scores = { ')': 3, ']': 57, '}': 1197, '>': 25137}

with open(filename, 'r') as f:
    puzzles = [line.strip() for line in f]
total_illegals = 0
for puzzle in puzzles:
    stack = []
    for s in puzzle:
        if s in couples:
            stack.append(s)
            continue
        m = couples[stack.pop()]
        if m == s:
            continue
        print(f"Expected '{m}', but found '{s}' instead.")
        total_illegals += scores[s]
        break
print(f'Day 10; Part 1; Solution: {total_illegals}') 

part2_scores = { ')': 1, ']': 2, '}': 3, '>': 4}
total_scores = []
for puzzle in puzzles:
    stack = []
    total_score = 0
    for s in puzzle:
        if s in couples:
            stack.append(s)
            continue
        m = couples[stack.pop()]
        if m == s:
            continue
        break
    else:
        if len(stack) > 0:
            for n in stack[::-1]:
                total_score *= 5
                total_score += part2_scores[couples[n]]
            total_scores.append(total_score)
solution_index = len(total_scores) // 2
solution = sorted(total_scores)[solution_index]
print(f'Day 10; Part 1; Solution: {solution}') 