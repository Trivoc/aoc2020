def read_input():
    with open("input.txt", "r") as input_file:
        return [line.strip() for line in input_file]


def traverse(location, delta_x, delta_y, wraparound):
    new_x = (location[0]+delta_x) % wraparound
    new_y = location[1] + delta_y
    return new_x, new_y


def check_slope(slopemap, delta_x, delta_y):
    location = (0, 0)
    wraparound = len(slopemap[0])
    trees = 0
    while location[1] < len(slopemap):
        current_line = slopemap[location[1]]
        if current_line[location[0]] == '#':
            trees += 1
        location = traverse(location, delta_x, delta_y, wraparound)

    return trees


def solve_part_1(input):
    return check_slope(input, 3, 1)


def solve_part_2(input):
    traversal1 = check_slope(input, 1, 1)
    traversal2 = check_slope(input, 3, 1)
    traversal3 = check_slope(input, 5, 1)
    traversal4 = check_slope(input, 7, 1)
    traversal5 = check_slope(input, 1, 2)
    return traversal1 * traversal2 * traversal3 * traversal4 * traversal5



input = read_input()
print(f'Part 1 solution: {solve_part_1(input)}')
print(f'Part 2 solution: {solve_part_2(input)}')
