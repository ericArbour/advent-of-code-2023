def get_first_digit(string: str) -> str:
    for char in string:
        if char.isdigit():
            return char

    raise ValueError("There must be at least one digit")


def get_value(line: str) -> int:
    first_digit = get_first_digit(line)
    last_digit = get_first_digit(line[::-1])

    return int(first_digit + last_digit)


def main() -> None:
    f = open("input.txt", "r")
    puzzle_input = f.read()

    total = 0

    for line in puzzle_input.splitlines():
        total += get_value(line)

    print("answer:", total)


if __name__ == "__main__":
    main()
