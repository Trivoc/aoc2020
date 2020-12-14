from time import time


def read_input_split(split_on):
    with open("input.txt", "r") as input_file:
        return input_file.read().strip().split(split_on)


def get_mem(string):
    return ''.join([c for c in string if c.isnumeric()])


def masked_val(value, mask):
    padded = bin(int(value))[2:].zfill(36)
    masked = []
    for i, c in enumerate(padded):
        if mask[i] != 'X':
            masked.append(mask[i])
        else:
            masked.append(c)
    return ''.join(masked)


def all_keys_r(mask):
    first_index = mask.find('X')
    if first_index == -1:
        return [mask]
    mask_0 = mask.replace('X', '0', 1)
    mask_1 = mask.replace('X', '1', 1)
    return all_keys_r(mask_0) + all_keys_r(mask_1)


def all_keys(key, mask):
    padded_key = list(bin(int(key))[2:].zfill(36))
    for i, c in enumerate(mask):
        if mask[i] == 'X':
            padded_key[i] = 'X'
        if mask[i] == '1':
            padded_key[i] = '1'
    return all_keys_r(''.join(padded_key))


def solve_part_1(inp):
    mem, mask = {}, 0
    for i in inp:
        splits = i.split(' = ')
        if 'mask' == splits[0]:
            mask = splits[1]
        else:
            key = get_mem(splits[0])
            mem[key] = masked_val(splits[1], mask)
    return sum(int(i, 2) for i in mem.values())


def solve_part_2(inp):
    mem, mask = {}, 0
    for i in inp:
        splits = i.split(' = ')
        if 'mask' == splits[0]:
            mask = splits[1]
        else:
            key = get_mem(splits[0])
            for key in all_keys(key, mask):
                mem[key] = splits[1]
    return sum(int(i) for i in mem.values())


split_input = read_input_split('\n')
print(split_input)

start = time()
solution1 = solve_part_1(split_input)
solution2 = solve_part_2(split_input)
stop = time()

print(f'Part 1 solution: {solution1}')
print(f'Part 2 solution: {solution2}')
print(f'Total time: {stop - start}')
