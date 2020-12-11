import timeit


def read_input_split(split_on):
    with open("input.txt", "r") as input_file:
        return input_file.read().strip().split(split_on)


def paths_to_joltage(path_map, key):
    acc = 0
    for i in range(1, 4):
        if key-i in path_map:
            acc += path_map[key - i]
    return acc


def solve_part_1(inp):
    prev = 0
    diff_1 = []
    diff_3 = []
    joltages = [i for i in inp]
    joltages.append(inp[-1] + 3)

    for i in joltages:
        diff = i - prev
        if diff == 1:
            diff_1.append(i)
        if diff == 3:
            diff_3.append(i)
        prev = i
    return len(diff_1) * len(diff_3)


def solve_part_2(inp):
    joltages = [0] + [i for i in inp]
    joltages.append(inp[-1] + 3)

    path_map = {0: 1}
    for i in joltages[1:]:
        path_map[i] = paths_to_joltage(path_map, i)
    return path_map[joltages[-1]]





split_input = read_input_split('\n')
split_input = sorted([int(s) for s in split_input])
print(split_input)

start = timeit.default_timer() * 1000 * 1000
solution1 = solve_part_1(split_input)
solution2 = solve_part_2(split_input)
stop = timeit.default_timer() * 1000 * 1000

print(f'Part 1 solution: {solution1}')
print(f'Part 2 solution: {solution2}')
print(f'Total time: {stop - start}')
