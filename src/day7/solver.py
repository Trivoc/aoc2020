def read_input_split(split_on):
    with open("input.txt", "r") as input_file:
        return input_file.read().strip().split(split_on)


def build_tup(bag_statement):
    if 'no other bags' in bag_statement:
        return 0, "NONE"
    splits = bag_statement.split(' ')
    return int(bag_statement[0]), f'{splits[1]} {splits[2]}'


def parse(inp):
    bagmap = {}
    count = 0
    for line in inp:
        bags = line.split(' bags contain ')
        bag = bags[0]
        containees = bags[1].split(', ')
        containee_list = []
        for x in containees:
            containee_list.append(build_tup(x))
        bagmap[bag] = containee_list
    return bagmap


def search_nested(container_Set, bagstring, bagmap):
    relevant = {colour: containees for colour, containees in bagmap.items() if bagstring in (cols for _, cols in containees)}
    if not relevant:
        container_Set.add(bagstring)
        return
    for key, value in relevant.items():
        for (amount, colour) in value:
            if colour == bagstring:
                container_Set.add(key)
                search_nested(container_Set, key, bagmap)
    return len(container_Set)


def find_all_in(bag_string, bagmap):
    sum = 0
    print(bag_string)
    if bag_string in bagmap.keys():
        for count, colour in bagmap[bag_string]:
            sum += count * find_all_in(colour, bagmap)
            sum += count
    return sum


def solve_part_1(inp):
    bagmap = parse(inp)
    print(bagmap)
    return search_nested(set(), 'shiny gold', bagmap)



def solve_part_2(inp):
    bagmap = parse(inp)
    return find_all_in('shiny gold', bagmap)


split_input = read_input_split('\n')
print(split_input)
parsed = parse(split_input)
print(f'Part 1 solution: {solve_part_1(split_input)}')
print(f'Part 2 solution: {solve_part_2(split_input)}')
