import string


def read_input(split_on):
    with open("input.txt", "r") as input_file:
        return input_file.read().strip().split(split_on)


def mock_passport():
    return {
        "byr": False,
        "iyr": False,
        "eyr": False,
        "hgt": False,
        "hcl": False,
        "ecl": False,
        "pid": False,
        "cid": True
    }


def validate_passport(pass_in):
    mock = mock_passport()
    mock.pop('cid', None)
    return all([key in pass_in for key in mock])


def validate_height(height_string):
    unit = height_string[-2:]
    value = int(height_string[:-2])
    return 150 <= value <= 193 if unit == 'cm' else 59 <= value <= 76


def validate_hair(hair_string):
    hex_digits = string.hexdigits
    return hair_string.startswith('#') and all([x in hex_digits for x in hair_string[1:]])


def validate_eyes(eyes_string):
    return eyes_string in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']


def validate_pid(pid_string):
    return pid_string.isnumeric and len(pid_string) == 9


def validate_passport_further(pass_in):
    return (1920 <= int(pass_in['byr']) <= 2002 and
            2010 <= int(pass_in['iyr']) <= 2020 <= int(pass_in['eyr']) <= 2030 and
            validate_height(pass_in['hgt']) and
            validate_hair(pass_in['hcl']) and
            validate_eyes(pass_in['ecl']) and
            validate_pid(pass_in['pid']))


def parse_data(input):
    return [dict(tup.split(':') for tup in pport.split()) for pport in input]


def solve_part_1(parsed_input):
    return len([p for p in parsed_input if validate_passport(p)])


def solve_part_2(parsed_input):
    return len([p for p in parsed_input if validate_passport(p) and validate_passport_further(p)])


split_input = read_input('\n\n')
parsed = parse_data(split_input)
print(f'Part 1 solution: {solve_part_1(parsed)}')
print(f'Part 2 solution: {solve_part_2(parsed)}')
