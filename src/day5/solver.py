import time

def read_input():
    with open("input.txt", "r") as input_file:
        return [line.strip() for line in input_file]


def binary_search(string, low, high, splitter):
    if low == high:
        return low
    if string[0] == splitter:
        return binary_search(string[1:], low, (low + high) // 2, splitter)
    else:
        return binary_search(string[1:], (low+high+1) // 2, high, splitter)


def calculate_id(seat_string):
    row = binary_search(seat_string[:-3], 0, 127, 'F')
    column = binary_search(seat_string[-3:], 0, 7, 'L')
    return row * 8 + column


def solve_part_1(input):
    ids = list(map(calculate_id, input))
    return max(ids)


def solve_part_2(input):
    ids = list(map(calculate_id, input))
    missing = list(filter(lambda x: x not in ids, range(min(ids), max(ids))))
    return missing[0]


input = read_input()
print(input)
print(f'Part 1 solution: {solve_part_1(input)}')
print(f'Part 2 solution: {solve_part_2(input)}')

