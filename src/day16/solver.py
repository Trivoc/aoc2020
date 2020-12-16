from time import time


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


def solve_part_2(inp):
    possibles = {}
    for i, _ in enumerate(inp[0]):
        possibles[i] = [key for key in rules.keys()]

    print(inp)
    for ticket_line in inp:
        print("ticket: ", ticket_line)
        for i, value in enumerate(ticket_line):
            print(possibles[i])
            filtered = possibles[i].copy()
            for field in possibles[i]:
                print(f'check: could value {value} with index {i} be valid for value field {field} with intervals {rules[field]}')
                valid_interval_1, valid_interval_2 = rules[field]
                if not in_interval(valid_interval_1, value) and not in_interval(valid_interval_2, value):
                    print("no")
                    filtered.remove(field)
                else:
                    print("yes")
            possibles[i] = filtered.copy()
            if len(filtered) == 1:
                for key in (key for key in possibles.keys() if key not in filtered):
                    print(filtered)
                    if filtered[0] in possibles:
                        possibles[key].remove(filtered[0])
            print(filtered)
    print(possibles)
    return -1


def update_possible(possibles, index, invalid_for_index):
    for invalid in invalid_for_index:
        if invalid in possibles[index]:
            possibles[index].remove(invalid)
    if len(possibles[index]) == 1:
        for i in (pi for pi in range(0, len(possibles)) if pi != index):
            if possibles[index][0] in possibles[i]:
                print(f'removing {possibles[index][0]} from index {i} which has {possibles[i]}')
                possibles[i].remove(possibles[index][0])


def solve_part_2_2(inp):
    possibles = {}
    for i, _ in enumerate(inp[0]):
        possibles[i] = [key for key in rules.keys()]
    print([len(value) != 1 for value in possibles.values()])

    while any([len(value) != 1 for value in possibles.values()]):
        for ticket in inp:
            for index, value in enumerate(ticket):
                invalid_for_index = set()
                for field in possibles[i]:
                    if not in_interval(rules[field][0], value) and not in_interval(rules[field][1], value):
                        # print(f'index {index} can not be the field {field} as the value is {value} and intervals for field is {rules[field]}')
                        invalid_for_index.add(field)
                update_possible(possibles, index, invalid_for_index)
        print("===============")
        for i, val in possibles.items():
            print(i, val)
    return my_ticket[0] * my_ticket[4] * my_ticket[7] * my_ticket[10] * my_ticket[16] * my_ticket[17]


def outside_both_intervals(field, value):
    return not in_interval(rules[field][0], value) and not in_interval(rules[field][1], value)


def trim_decided(field, possibles):
    for of, i in ((of, i) for of, i in possibles.items() if of != field and len(possibles[field]) == 1):
        possibles[of] = [ind for ind in i if ind != possibles[field][0]]


def solve_part_2_3(inp):
    possibles = {key: list(range(0, len(inp[0]))) for key in rules.keys()}

    while any([len(value) != 1 for value in possibles.values()]):
        for ticket in inp:
            for index, value in enumerate(ticket):
                for field, indices in possibles.items():
                    if outside_both_intervals(field, value) and index in indices:
                        possibles[field].remove(index)
                    trim_decided(field, possibles)


    prod = 1
    for field, indices in possibles.items():
        if 'departure' in field:
            print(my_ticket[indices[0]])
            prod = prod * int(my_ticket[indices[0]])
    return prod





split_input = read_input_split('\n\n')

start = time()
rules = parse_rules(split_input[0])
my_ticket = parse_ticket(split_input[1].split('\n')[1])
valid_tickets = []

solution1 = solve_part_1(split_input[2])
solution2 = solve_part_2_3(valid_tickets)
stop = time()

print(f'Part 1 solution: {solution1}')
print(f'Part 2 solution: {solution2}')
print(f'Total time: {stop - start}')
