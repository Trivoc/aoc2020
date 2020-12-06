def read_input_split(split_on):
    with open("input.txt", "r") as input_file:
        return input_file.read().strip().split(split_on)


def convert(char):
    return {
        'F': '0',
        'L': '0',
        'B': '1',
        'R': '1'
    }[char]


def calculate_id(seat_string):
    binary = ''.join([convert(x) for x in seat_string])
    return int(binary, 2)


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

