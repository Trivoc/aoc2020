from time import time
from functools import reduce


def read_input_split(split_on):
    with open("input.txt", "r") as input_file:
        return input_file.read().strip().split(split_on)


def intervals(interval_string):
    intervals = interval_string.strip().split(' or ')
    interval_1 = [int(i) for i in intervals[0].split('-')]
    interval_2 = [int(i) for i in intervals[1].split('-')]
    return interval_1, interval_2


def parse_rules(rules):
    rule_dict = {}
    for line in rules.split('\n'):
        field, value = line.split(':')
        rule_dict[field] = intervals(value)
    return rule_dict


def parse_ticket(ticket_line):
    return [int(i) for i in ticket_line.split(',')]


def solve_part_1(inp):
    print(rules)
    all_intervals = list(sum([(first, second) for first, second in rules.values()], ()))
    error_rate = 0
    for line in inp.split('\n')[1:]:
        ticket = parse_ticket(line)
        ticket_valid = True
        for value in ticket:
            value_valid = False
            for interval in all_intervals:
                if interval[0] <= value <= interval[1]:
                    value_valid = True
                    break
            if not value_valid:
                error_rate += value
                ticket_valid = False
        if ticket_valid:
            valid_tickets.append(ticket)
    return error_rate


def in_interval(interval, value):
    return interval[0] <= value <= interval[1]


def outside_both_intervals(field, value):
    return not in_interval(rules[field][0], value) and not in_interval(rules[field][1], value)


def trim_decided(determined, possibles):
    other_field_indices = ((of, ind) for of, ind in possibles.items() if of != determined and len(possibles[determined]) == 1)
    for of, indices in other_field_indices:
        possibles[of] = [ind for ind in indices if ind not in possibles[determined]]


def solve_part_2(inp):
    possibles = {key: list(range(0, len(inp[0]))) for key in rules.keys()}

    while any([len(value) != 1 for value in possibles.values()]):
        for ticket in inp:
            for index, val in enumerate(ticket):
                for field, indices in possibles.items():
                    if outside_both_intervals(field, val) and index in indices:
                        possibles[field].remove(index)
                    trim_decided(field, possibles)

    return reduce(lambda a, b: a * b, [int(my_ticket[i[0]]) for f, i in possibles.items() if 'departure' in f])


split_input = read_input_split('\n\n')

start = time()
rules = parse_rules(split_input[0])
my_ticket = parse_ticket(split_input[1].split('\n')[1])
valid_tickets = []

solution1 = solve_part_1(split_input[2])
solution2 = solve_part_2(valid_tickets)
stop = time()

print(f'Part 1 solution: {solution1}')
print(f'Part 2 solution: {solution2}')
print(f'Total time: {stop - start}')
