def read_input_split(split_on):
    with open("input.txt", "r") as input_file:
        return input_file.read().strip().split(split_on)


def exec_statement(code, offset, acc):
    if code == 'acc':
        return 1, acc + (int(offset))
    if code == 'jmp':
        return int(offset), acc
    if code == 'nop':
        return 1, acc


def run(program):
    index = 0
    acc = 0
    executed = set()
    while index in range(0, len(program)):
        instruction, offset = program[index].split()
        offset, new_acc = exec_statement(instruction, offset, acc)
        index += offset
        if index in executed:
            return 'LOOP', acc
        executed.add(index)
        acc = new_acc
    return 'DONE', acc


def solve_part_1(inp):
    (_, acc) = run(inp)
    return acc


def solve_part_2(inp):
    programs = []
    for i in range(0, len(inp)):
        line = inp[i]
        if 'nop' in line:
            programs.append(inp[:i] + [line.replace('nop', 'jmp')] + inp[i+1:])
        if 'jmp' in line:
            programs.append(inp[:i] + [line.replace('jmp', 'nop')] + inp[i+1:])
    for prog in programs:
        (sig, acc) = run(prog)
        if sig == 'DONE':
            return acc


split_input = read_input_split('\n')
print(split_input)
print(f'Part 1 solution: {solve_part_1(split_input)}')
print(f'Part 2 solution: {solve_part_2(split_input)}')
