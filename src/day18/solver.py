from time import time
from math import prod


def read_input_split(split_on):
    with open("input.txt", "r") as input_file:
        return input_file.read().strip().split(split_on)


def calculate(operator, previous, val):
    if operator == '+':
        return previous + val
    else:
        return previous * val


def solve(simplified):
    split = simplified.split(' ')
    result = int(split[0])
    for index, val in enumerate(split):
        if val.isnumeric() and index > 1:
            result = calculate(split[index-1], result, int(val))
    return result


def solve2(simplified):
    plus_split = simplified.split(' * ')
    return prod([solve(split) for split in plus_split])


# use a stack instead
def isolate(expr):
    layer = 0
    first = 0
    found_first = False
    for index, c in enumerate(expr):
        if c == '(':
            layer += 1
            if not found_first:
                first = index+1
                found_first = True
        if c == ')':
            layer -= 1
            if layer == 0:
                return first, index+1


def evaluate(expr, plusPrec = False):
    simplified = expr
    while '(' in simplified:
        first, last = isolate(simplified)
        isolated_val = evaluate(simplified[first:last-1], plusPrec)
        simplified = simplified[0:first-1] + str(isolated_val) + simplified[last: len(expr)]
    if plusPrec:
        return solve2(simplified)
    return solve(simplified)


def solve_part_1(inp):
    return sum(evaluate(expr) for expr in inp)


def solve_part_2(inp):
    return sum(evaluate(expr, plusPrec=True) for expr in inp)


split_input = read_input_split('\n')
print(split_input)

start = time()
solution1 = solve_part_1(split_input)
solution2 = solve_part_2(split_input)
stop = time()

print(f'Part 1 solution: {solution1}')
print(f'Part 2 solution: {solution2}')
print(f'Total time: {stop - start}')
