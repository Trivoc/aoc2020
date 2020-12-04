import string

def read_input():
    with open("input.txt", "r") as input_file:
        return [line.strip() for line in input_file]

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
    for key in mock:
        if key not in pass_in:
            return False
    return True


def validate_height(height_string):
    unit = height_string[-2:]
    value = int(height_string[:-2])
    if unit == 'cm':
        return 150 <= value <= 193
    else:
        return 59 <= value <= 76

    return True


def validate_hair(hair_string):
    hex_digits = string.hexdigits
    return hair_string.startswith('#') and all(list(map(lambda x: x in hex_digits, list(hair_string[1:]))))


def validate_eyes(eyes_string):
    return eyes_string in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']


def validate_pid(pid_string):
    return pid_string.isnumeric and len(pid_string) == 9


def validate_passport_further(pass_in):
    return (1920 <= int(pass_in['byr']) <= 2002 and
            2010 <= int(pass_in['iyr']) <= 2020 and
            2020 <= int(pass_in['eyr']) <= 2030 and
            validate_height(pass_in['hgt']) and
            validate_hair(pass_in['hcl']) and
            validate_eyes(pass_in['ecl']) and
            validate_pid(pass_in['pid']))


def to_tuple(entry):
    return tuple(entry.split(':'))


def parse_data(lines):
    dicts = []
    current_passport = {}
    for line in lines:
        if line == '':
            dicts.append(current_passport)
            current_passport = {}
        else:
            entries = line.split(' ')
            tuples = list(map(lambda x: tuple(x.split(':')), entries))
            for key, value in tuples:
                current_passport[key] = value
    dicts.append(current_passport)
    return dicts





def solve_part_1(input):
    passports = parse_data(input)
    print(passports)
    print(len(passports))
    return len(list(filter(validate_passport, passports)))


def solve_part_2(input):
    passports = list(filter(validate_passport, parse_data(input)))
    return len(list(filter(validate_passport_further, passports)))


input = read_input()
print(input)
print(f'Part 1 solution: {solve_part_1(input)}')
print(f'Part 2 solution: {solve_part_2(input)}')
