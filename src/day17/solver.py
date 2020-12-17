from time import time


def read_input_split(split_on):
    with open("input.txt", "r") as input_file:
        return input_file.read().strip().split(split_on)


def neighbours(coordinate):
    x, y, z = coordinate
    neighbour_list = []
    for n_x in range(x - 1, x + 2):
        for n_y in range(y - 1, y + 2):
            for n_z in range(z - 1, z + 2):
                neighbour_list.append((n_x, n_y, n_z))
    neighbour_list.remove((x, y, z))
    return neighbour_list


def neighbours_2(coordinate):
    x, y, z, w = coordinate
    neighbour_list = []
    for n_x in range(x - 1, x + 2):
        for n_y in range(y - 1, y + 2):
            for n_z in range(z - 1, z + 2):
                for n_w in range(w - 1, w + 2):
                    neighbour_list.append((n_x, n_y, n_z, n_w))
    neighbour_list.remove((x, y, z, w))
    return neighbour_list


def find_new(space):
    potentials = {}
    for (x, y, z) in space:
        neighbour_list = neighbours((x, y, z))
        for (n_x, n_y, n_z) in neighbour_list:
            if (n_x, n_y, n_z) in potentials:
                potentials[(n_x, n_y, n_z)] += 1
            else:
                potentials[(n_x, n_y, n_z)] = 1
    return [coord for coord, amount in potentials.items() if amount == 3]


def find_new_2(space):
    potentials = {}
    print(space)
    for (x, y, z, w) in space:
        neighbour_list = neighbours_2((x, y, z, w))
        for (n_x, n_y, n_z, n_w) in neighbour_list:
            if (n_x, n_y, n_z, n_w) in potentials:
                potentials[(n_x, n_y, n_z, n_w)] += 1
            else:
                potentials[(n_x, n_y, n_z, n_w)] = 1
    return [coord for coord, amount in potentials.items() if amount == 3]


def count_active_neighbours(space, neighbours_list):
    return len([n for n in neighbours_list if n in space])


def calculate_remaining_active(space):
    still_active = []
    for (x, y, z) in space:
        n = neighbours((x, y, z))
        if count_active_neighbours(space, n) == 2 or count_active_neighbours(space, n) == 3:
            still_active.append((x, y, z))
    return still_active


def calculate_remaining_active_2(space):
    still_active = []
    for (x, y, z, w) in space:
        n = neighbours_2((x, y, z, w))
        if count_active_neighbours(space, n) == 2 or count_active_neighbours(space, n) == 3:
            still_active.append((x, y, z, w))
    return still_active


def solve_part_1(inp):
    space = []
    for y, line in enumerate(inp):
        for x, cube in enumerate(line):
            if cube == '#':
                space.append((x, y, 0))
    print(space)
    for i in range(0, 6):
        new_active = find_new(space)
        remaining_active = calculate_remaining_active(space)
        space = remaining_active + new_active
        space = list(set(space))
    return len(space)



def solve_part_2(inp):
    space = []
    for y, line in enumerate(inp):
        for x, cube in enumerate(line):
            if cube == '#':
                space.append((x, y, 0, 0))
    for i in range(0, 6):
        new_active = find_new_2(space)
        remaining_active = calculate_remaining_active_2(space)
        space = remaining_active + new_active
        space = list(set(space))
    return len(space)


split_input = read_input_split('\n')
print(split_input)

start = time()
solution1 = solve_part_1(split_input)
solution2 = solve_part_2(split_input)
stop = time()

print(f'Part 1 solution: {solution1}')
print(f'Part 2 solution: {solution2}')
print(f'Total time: {stop - start}')
