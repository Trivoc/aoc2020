from functools import reduce


def read_input(split_on):
    with open("input.txt", "r") as input_file:
        return input_file.read().strip().split(split_on)


def solve_part_1(groups):
    joined_groups = list(map(lambda x: x.replace('\n', ''), groups))
    unique_no = list(map(lambda string: len(set(string)), joined_groups))
    return sum(unique_no)


def solve_part_2(groups):
    grouped_answers = list(map(lambda string: set(string.split('\n')), groups))
    print(grouped_answers)
    sum = 0
    for answer_set in grouped_answers:
        list_of_charsets = list(set(a) for a in answer_set)
        intersect = reduce(lambda x, y: x.intersection(y), list_of_charsets)
        sum += len(intersect)
    return sum


input = read_input('\n\n')
print(input)
print(f'Part 1 solution: {solve_part_1(input)}')
print(f'Part 2 solution: {solve_part_2(input)}')
