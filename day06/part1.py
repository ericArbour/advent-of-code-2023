import re
import math

num_regex = re.compile(r"\d+")


def parse_line(line):
    num_strs = num_regex.findall(line)
    return tuple(int(num_str) for num_str in num_strs)


def calc_race(race):
    dur, record = race
    breakers = [speed for speed in range(dur + 1) if (dur - speed) * speed > record]
    return len(breakers)


def main():
    with open("input.txt", "r") as f:
        puzzle_input = f.read()

    parsed_lines = [parse_line(line) for line in puzzle_input.splitlines()]
    races = [*zip(*parsed_lines)]
    answer = math.prod(calc_race(race) for race in races)

    print("answer:", answer)


if __name__ == "__main__":
    main()
