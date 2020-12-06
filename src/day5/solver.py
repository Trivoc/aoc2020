def read_input_split(split_on):
    with open("input.txt", "r") as input_file:
        return input_file.read().strip().split(split_on)


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
    ids = [calculate_id(x) for x in input]
    return max(ids)


def solve_part_2(input):
    ids = [calculate_id(x) for x in input]
    missing = [x for x in range(min(ids), max(ids)) if x not in ids]
    return missing[0]


input = read_input_split('\n')
print(input)
print(f'Part 1 solution: {solve_part_1(input)}')
print(f'Part 2 solution: {solve_part_2(input)}')

