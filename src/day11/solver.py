from time import time

orig_matrix = [[]]

def read_input_split(split_on):
    with open("input.txt", "r") as input_file:
        return input_file.read().strip().split(split_on)

def adjacent(x, y):
    above = y - 1
    below = y + 1
    right = x + 1
    left = x - 1

    return [(new_x, new_y) for (new_x, new_y) in
            ((x, above), (x, below), (left, y), (right, y), (right, above), (left, above), (right, below), (left, below))
            if new_x in range(0, len(orig_matrix[0])) and new_y in range(0, len(orig_matrix))]

def in_bounds(x, y):
    return x in range(0, len(orig_matrix[0])) and y in range(0, len(orig_matrix))

def sign_id(i):
    if i < 0:
        return -1
    if i > 0:
        return 1
    return 0

def adjacent_2(matrix, x, y):
    above = y - 1
    below = y + 1
    right = x + 1
    left = x - 1

    immediate_adj = [(new_x, new_y) for (new_x, new_y) in
            ((x, above), (x, below), (left, y), (right, y), (right, above), (left, above), (right, below), (left, below))
            if in_bounds(new_x, new_y)]

    loop = True
    while loop:
        floor_adj = [(adj_x, adj_y) for adj_x, adj_y in immediate_adj if in_bounds(adj_x, adj_y) and matrix[adj_y][adj_x] == '.']
        for adj_x, adj_y in floor_adj:
            deltax = sign_id(adj_x - x)
            deltay = sign_id(adj_y - y)
            immediate_adj.remove((adj_x, adj_y))
            if in_bounds(adj_x + deltax, adj_y + deltay):
                immediate_adj.append((adj_x + deltax, adj_y + deltay))
        if not floor_adj:
            loop = False
    return immediate_adj


def occupied_adjacent(inp, adjacent, x, y):
    return [(x, y) for x, y in adjacent if inp[y][x] == '#']


def change(inp, x, y):
    occupied_adj = occupied_adjacent(inp, adjacent(x, y), x, y)
    return change_seat(inp, occupied_adj, x, y, 4)


def change_2(current, x, y):
    occupied_adj = occupied_adjacent(current, adjacent_2(current, x, y), x, y)
    return change_seat(current, occupied_adj, x, y, 5)


def change_seat(inp, occupied_adj, x, y, limit):
    if inp[y][x] == 'L':
        if not occupied_adj:
            return '#'
        else:
            return 'L'
    if inp[y][x] == '#':
        if len(occupied_adj) >= limit:
            return 'L'
        else:
            return '#'
    else:
        return '.'



def pprint(inp):
    print("================")
    for line in inp:
        print(line)
    print("================")




def solve_part_1(inp):
    current = orig_matrix
    changed = True
    mutations = 0
    while changed:
        new = []
        for y, line in enumerate(inp):
            new.append([])
            for x, symbol in enumerate(line):
                new[y].append(change(current, x, y))
        mutations += 1
        if current == new:
            changed = False
        current = new
    return len([item for line in current for item in line if item == '#'])



def solve_part_2(inp):
    current = orig_matrix
    changed = True
    mutations = 0
    while changed:
        new = []
        for y, line in enumerate(inp):
            new.append([])
            for x, symbol in enumerate(line):
                new[y].append(change_2(current, x, y))
        mutations += 1
        if current == new:
            changed = False
        current = new
    return len([item for line in current for item in line if item == '#'])


split_input = read_input_split('\n')
print(split_input)
orig_matrix = [[s for s in y] for y in split_input]


start = time()
solution1 = solve_part_1(split_input)
solution2 = solve_part_2(split_input)
stop = time()

print(f'Part 1 solution: {solution1}')
print(f'Part 2 solution: {solution2}')
print(f'Total time: {stop - start}')
