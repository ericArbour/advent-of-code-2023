DIGIT_WORDS = ("one", "two", "three", "four", "five", "six", "seven", "eight", "nine")


def get_digit_word_value(string: str) -> str | None:
    for index, word in enumerate(DIGIT_WORDS):
        if string.startswith(word):
            return str(index + 1)

    return None


def get_first_digit(string: str, my_range: range) -> str:
    for i in my_range:
        if string[i].isdigit():
            return string[i]

        digit_word_value = get_digit_word_value(string[i:])
        if isinstance(digit_word_value, str):
            return digit_word_value


def get_value(line: str) -> int:
    first_digit = get_first_digit(line, range(len(line)))
    last_digit = get_first_digit(line, range(len(line) - 1, -1, -1))

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
