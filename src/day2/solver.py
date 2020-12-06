def read_input_split(split_on):
    with open("input.txt", "r") as input_file:
        return input_file.read().strip().split(split_on)


def format_line(line):
    segments = line.split()
    indices = segments[0].split('-')
    range_tuple = (int(indices[0]), int(indices[1]))
    symbol = segments[1][:-1]
    return range_tuple, symbol, segments[2]


def solve_part_1(formatted_inp):
    return len([pwd for ((l, h), sym, pwd) in formatted_inp if pwd.count(sym) in range(l, h+1)])


def solve_part_2(formatted_inp):
    return len([pwd for ((l, h), sym, pwd) in formatted_inp if (pwd[l-1] == sym) != (pwd[h-1] == sym)])


split_input = read_input_split('\n')
formatted = [format_line(line) for line in split_input]
print(formatted)
print(f'Part 1 solution: {solve_part_1(formatted)}')
print(f'Part 2 solution: {solve_part_2(formatted)}')
