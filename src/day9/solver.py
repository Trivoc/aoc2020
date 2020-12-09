from itertools import combinations
from time import time

def read_input_split(split_on):
    with open("input.txt", "r") as input_file:
        return input_file.read().strip().split(split_on)


def solve_part_1(inp, preamble_size):
    for i, value in enumerate(inp[preamble_size:]):
        preamble = inp[i:i+preamble_size]
        exists = False
        for a, b in combinations(preamble, 2):
            if a + b == value:
                exists = True
        if not exists:
            return value


def solve_part_2(inp, number):
    index = inp.index(number)
    for lower, _ in enumerate(inp[:index]):
        curr_sum = 0
        for current in range(lower, index):
            curr_sum += inp[current]
            if curr_sum > number:
                break
            if curr_sum == number:
                sliced = inp[lower:current]
                return min(sliced) + max(sliced)
    return -1


split_input = read_input_split('\n')
print(split_input)
split_input = [int(s) for s in split_input]
start = time()
solution1 = solve_part_1(split_input, 25)
solution2 = solve_part_2(split_input, solution1)
stop = time()
print(f'Part 1 solution: {solution1}')
print(f'Part 2 solution: {solution2}')
print(f'time: {stop - start}')

