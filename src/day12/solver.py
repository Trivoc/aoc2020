from time import time
from math import cos
from math import sin
from math import radians


def read_input_split(split_on):
    with open("input.txt", "r") as input_file:
        return input_file.read().strip().split(split_on)


def transpose(action, value, pos):
    x = pos[0]
    y = pos[1]
    if action == 'N':
        y = y + value
    if action == 'S':
        y = y - value
    if action == 'E':
        x = x + value
    if action == 'W':
        x = x - value
    return x, y


def rotate(action, value, rotation):
    if action == 'R':
        rotation = (rotation - value) % 360
    if action == 'L':
        rotation = (rotation + value) % 360
    return rotation


def traverse(value, pos, rotation):
    x = pos[0]
    y = pos[1]
    x = round(x + (cos(radians(rotation)) * value))
    y = round(y + (sin(radians(rotation)) * value))
    return x, y


def rotate_clockwise(rotate_times, waypoint_pos):
    x = waypoint_pos[0]
    y = waypoint_pos[1]
    for i in range(0, rotate_times):
        x, y = y, -x
    return x, y


def rotate_cclockwise(rotate_times, waypoint_pos):
    x = waypoint_pos[0]
    y = waypoint_pos[1]
    for i in range(0, rotate_times):
        x, y = -y, x
    return x, y


def rotate_waypoint(action, value, waypoint_relative):
    rotate_times = value // 90
    if action == 'R':
        rotated = rotate_clockwise(rotate_times, waypoint_relative)
    if action == 'L':
        rotated = rotate_cclockwise(rotate_times, waypoint_relative)
    return rotated


def approach(value, waypoint, boat):
    delta_x = waypoint[0]
    delta_y = waypoint[1]
    x = boat[0] + delta_x * value
    y = boat[1] + delta_y * value
    return x, y


def solve_part_1(inp):
    current = {'rotation': 0, 'pos': (0, 0)}
    for instruction in inp:
        action = instruction[0]
        value = int(instruction[1:])
        if action in ['N', 'S', 'W', 'E']:
            current['pos'] = transpose(action, value, current['pos'])
        if action in ['R', 'L']:
            current['rotation'] = rotate(action, value, current['rotation'])
        if action == 'F':
            current['pos'] = traverse(value, current['pos'], current['rotation'])
    return abs(current['pos'][0]) + abs(current['pos'][1])


def solve_part_2(inp):
    current = {'waypoint_relative': (10, 1), 'boat': (0, 0)}
    for instruction in inp:
        print(instruction)
        action = instruction[0]
        value = int(instruction[1:])
        if action in ['N', 'S', 'W', 'E']:
            current['waypoint_relative'] = transpose(action, value, current['waypoint_relative'])
        if action in ['R', 'L']:
            current['waypoint_relative'] = rotate_waypoint(action, value, current['waypoint_relative'])
        if action == 'F':
            current['boat'] = approach(value, current['waypoint_relative'], current['boat'])
        print(current)
    return abs(current['boat'][0]) + abs(current['boat'][1])


split_input = read_input_split('\n')
print(split_input)

start = time()
solution1 = solve_part_1(split_input)
solution2 = solve_part_2(split_input)
stop = time()

print(f'Part 1 solution: {solution1}')
print(f'Part 2 solution: {solution2}')
print(f'Total time: {stop - start}')
