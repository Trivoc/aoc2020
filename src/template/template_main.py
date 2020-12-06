def read_input_split(split_on):
    with open("input.txt", "r") as input_file:
        return input_file.read().strip().split(split_on)


def solve_part_1(split_input):
    return -1


def solve_part_2(split_input):
    return -1


split_input = read_input_split('\n')
print(input)
print(f'Part 1 solution: {solve_part_1(split_input)}')
print(f'Part 2 solution: {solve_part_2(split_input)}')
