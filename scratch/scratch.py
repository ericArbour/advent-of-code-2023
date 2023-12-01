def solve_part_1(puzzle_input: str) -> int:
    result = 0

    for index, digit in enumerate(puzzle_input):
        next_index = (index + 1) % len(puzzle_input)

        if digit == puzzle_input[next_index]:
            result += int(digit)

    return result


def solve_part_2(puzzle_input: str) -> int:
    result = 0

    for index, digit in enumerate(puzzle_input):
        length = len(puzzle_input)
        midpoint = length // 2
        next_index = (index + midpoint) % length

        if digit == puzzle_input[next_index]:
            result += int(digit)

    return result


def main() -> None:
    f = open("input.txt", "r")
    puzzle_input = f.read()
    print("part 1", solve_part_1(puzzle_input))
    print("part 2", solve_part_2(puzzle_input))


if __name__ == "__main__":
    main()
