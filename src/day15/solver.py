from time import time


def read_input_split(split_on):
    with open("input.txt", "r") as input_file:
        return input_file.read().strip().split(split_on)


def calculate_next(prev_tuple):
    (last_time, before_that) = prev_tuple
    if before_that == 0:
        return 0
    else:
        return last_time - before_that


def solve_part_1(inp, nth):
    starting = [int(i) for i in inp[0].split(',')]
    memory = {}
    last_spoken = 0

    for i, num in enumerate(starting):
        memory[num] = (i+1, 0)
        last_spoken = num

    for i in range(len(starting)+1, nth+1):
        new_num = calculate_next(memory[last_spoken])
        if new_num not in memory.keys():
            memory[new_num] = (i, 0)
        else:
            (last_time, before_that) = memory[new_num]
            memory[new_num] = (i, last_time)
        last_spoken = new_num
    return last_spoken


def solve_part_2(inp):
    return solve_part_1(inp, 30000000)


split_input = read_input_split('\n')
print(split_input)

start = time()
solution1 = solve_part_1(split_input, 2020)
solution2 = solve_part_2(split_input)
stop = time()

print(f'Part 1 solution: {solution1}')
print(f'Part 2 solution: {solution2}')
print(f'Total time: {stop - start}')
