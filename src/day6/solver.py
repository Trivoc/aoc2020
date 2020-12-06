def read_input(split_on):
    with open("input.txt", "r") as input_file:
        return input_file.read().strip().split(split_on)


def solve_part_1(groups):
    return sum([len(set(s)) for s in (x.replace('\n', '') for x in groups)])


def solve_part_2(groups):
    group_sets = [[set(answers) for answers in person] for person in (answer.split('\n') for answer in groups)]
    intersects = sum(len(set.intersection(*p)) for p in group_sets)
    return intersects

input = read_input('\n\n')
print(input)
print(f'Part 1 solution: {solve_part_1(input)}')
print(f'Part 2 solution: {solve_part_2(input)}')
