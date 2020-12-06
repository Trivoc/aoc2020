def read_input_split(split_on):
    with open("input.txt", "r") as input_file:
        return input_file.read().strip().split(split_on)


def solve_part_1(input):
    return -1


def solve_part_2(input):
    return -1


input = read_input_split('\n\n')
print(input)
print(f'Part 1 solution: {solve_part_1(input)}')
print(f'Part 2 solution: {solve_part_2(input)}')
