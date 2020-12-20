from time import time

rules_dict = {}

def read_input_split(split_on):
    with open("input.txt", "r") as input_file:
        return input_file.read().strip().split(split_on)


def parse_rules(rules_list):
    rules = {}
    for rule in rules_list:
        key, rule = rule.split(': ')
        rules[key] = [[r.replace('"', '') for r in s.split(' ')] for s in rule.split(' | ')]
    return rules


def build_possibles(result, evaled):
    if not result:
        return evaled
    joined = [a + b for a in result for b in evaled]
    return joined


def evaluate_rule(rule_no):
    value = rules_dict[rule_no]
    if not value[0][0].isnumeric():
        return [value[0][0]]
    else:
        possibles = []
        for option in value:
            built_options = []
            for rule_no in option:
                evaluated_num = evaluate_rule(rule_no)
                built_options = build_possibles(built_options, evaluated_num)
            possibles.append(built_options)
        return [l for p in possibles for l in p]


def solve_part_1():
    evaluated = set(evaluate_rule('0'))
    return len([m for m in messages if m in evaluated])



def solve_part_2():
    print(rules_dict)
    rules_dict['8'] = [['42'], ['42', '8']]
    rules_dict['11'] = [['42', '31'], ['42', '11', '31']]
    return evaluate_rule('8')
    pass



split_input = read_input_split('\n\n')
print(split_input)
rules_list = split_input[0].split('\n')
messages = split_input[1].split('\n')
rules_dict = parse_rules(rules_list)

start = time()
solution1 = solve_part_1()
solution2 = solve_part_2()
stop = time()

print(f'Part 1 solution: {solution1}')
print(f'Part 2 solution: {solution2}')
print(f'Total time: {stop - start}')
