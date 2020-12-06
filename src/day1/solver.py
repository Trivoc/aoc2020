import itertools


def read_input():
    with open("./input.txt", "r") as input_file:
        return [line.strip() for line in input_file]


def solve_part_1(input):
    return [int(a) * int(b) for a,b in itertools.combinations(input, 2) if int(a) + int(b) == 2020].pop()


def solve_part_2(input):
    return [int(a) * int(b) * int(c) for a,b,c in itertools.combinations(input, 3)
            if int(a) + int(b) + int(c) == 2020].pop()


input = read_input()
print(input)
print(f'Part 1 solution: {solve_part_1(input)}')
print(f'Part 2 solution: {solve_part_2(input)}')


