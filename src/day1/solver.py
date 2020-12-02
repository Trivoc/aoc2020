def read_input():
    with open("./input.txt", "r") as input_file:
        return [line.strip() for line in input_file]


def solve_part_1(input):
    for index_outer in range(1, len(input)):
        for index_inner in range(index_outer, len(input)):
            inner = int(input[index_inner])
            outer = int(input[index_outer])
            if inner + outer == 2020:
                return inner * outer


def solve_part_2(input):
    for index_outer in range(1, len(input)):
        for index_inner in range(index_outer, len(input)):
            for index_innest in range(index_inner, len(input)):
                innest = int(input[index_innest])
                inner = int(input[index_inner])
                outer = int(input[index_outer])
                if inner + outer + innest == 2020:
                    return inner * outer * innest



input = read_input()
print(input)
solution1 = solve_part_1(input)
solution2 = solve_part_2(input)
print(f'Part 1 solution: {solve_part_1(input)}')
print(f'Part 2 solution: {solution2}')
