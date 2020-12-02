import requests
from pathlib import Path
from shutil import copyfile


def get_input_path(day):
    return Path(f"src/day{day}/input.txt")

def get_solver_path(day):
    return Path(f"src/day{day}/solver.py")

def get_daily_directory(day):
    return Path(f"src/day{day}/")


def status_ok(status):
    print(f'Result from fetch is {status}')
    if status != 200:
        print("Error fetching input, do you need to update cookie?")
    return status == 200


def get_input_online(year, day):
    with open(".cookie", "r") as cookieFile:
        cookie = cookieFile.read().replace('\n', "")
        contents = requests.get(f"https://adventofcode.com/{year}/day/{day}/input", headers={"Cookie": cookie})

    if not status_ok(contents.status_code):
        return []
    return contents.content.decode('utf-8')


def save_input(input_list, directory_path, input_path):
    directory_path.mkdir(exist_ok=True)
    with open(input_path, "w") as inputFile:
        return inputFile.write(input_list)


def read_input_file(input_path):
    with open(input_path, "r") as input_file:
        return [line.strip() for line in input_file]


def create_module(year, day):
    input_path = get_input_path(day)
    if not input_path.exists():
        print("No input file found, fetching and creating...")
        input_string = get_input_online(year, day)
        save_input(input_string, get_daily_directory(day), input_path)
    else:
        print(f"Input already fetched once, no need to fetch input")

    solver_path = get_solver_path(day)
    if not solver_path.exists():
        print("No solver file found, creating template...")
        copyfile("src/template/template_main.py", f"src/day{day}/solver.py")
    else:
        print("Solver present already")


