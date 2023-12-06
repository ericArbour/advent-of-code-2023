import re

num_regex = re.compile(r"\d+")


def parse_line(line):
    num_str = "".join(num_regex.findall(line))
    return int(num_str)


def calc_race(race):
    dur, record = race
    breakers = [speed for speed in range(dur + 1) if (dur - speed) * speed > record]
    return len(breakers)


def main():
    """
    This could probably be faster with one of the following approaches:
    1. Start from 0 to find the first record breaking number, start from some number
    based on the duration to find the last record breaking number, then total everything
    in between.
    2. Binary search to find the first and last, then total everything in between.
    """
    with open("input.txt", "r") as f:
        puzzle_input = f.read()

    race = tuple(parse_line(line) for line in puzzle_input.splitlines())
    print(calc_race(race))


if __name__ == "__main__":
    main()
