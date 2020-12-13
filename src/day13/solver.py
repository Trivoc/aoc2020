from time import time
from functools import reduce


def read_input_split(split_on):
    with open("input.txt", "r") as input_file:
        return input_file.read().strip().split(split_on)


def find_y(tuple):
    z, (rem, mod) = tuple
    y = z % mod
    for i in range(0, mod):
        if (y * i) % mod == 1:
            y = i
            break
    return y


def crt(busses):
    product_mod = reduce((lambda x, y: x * y), (mod for (rem, mod) in busses))
    a = [rem for rem, mod in busses]
    z = [(product_mod // mod) for rem, mod in busses]
    nums = list(zip(z, busses))
    y = [find_y(a) for a in nums]
    w = [y * z for y, z in zip(y, z)]
    result = 0
    for i in range(0, len(w)):
        result += (w[i]*a[i])
    return result % product_mod


def solve_part_1(inp):
    timestamp = int(inp[0])
    busses = [int(x) for x in inp[1].split(',') if x.isnumeric()]
    remainder = sorted([(x, (0 - timestamp) % x) for x in busses], key=lambda x: x[1])
    return remainder[0][0] * remainder[0][1]



def solve_part_2(inp):
    busses = [(int(x) - offset, int(x)) for offset, x in enumerate(inp[1].split(',')) if x.isnumeric()]
    return crt(busses)


split_input = read_input_split('\n')
print(split_input)

start = time()
solution1 = solve_part_1(split_input)
solution2 = solve_part_2(split_input)
stop = time()

print(f'Part 1 solution: {solution1}')
print(f'Part 2 solution: {solution2}')
print(f'Total time: {stop - start}')
