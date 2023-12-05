import re

num_regex = re.compile(r"\d+")


def parse_number_part(numbers_part):
    winners_strs, held_numbers_str = numbers_part.split(" | ")
    winners = num_regex.findall(winners_strs)
    held_numbers = num_regex.findall(held_numbers_str)
    return set(winners), held_numbers


def score(winners, held_numbers):
    held_winners = [
        held_number for held_number in held_numbers if held_number in winners
    ]
    winners_count = len(held_winners)
    return 2 ** (winners_count - 1) if winners_count else 0


def main():
    with open("input.txt", "r") as f:
        puzzle_input = f.read()
        lines = puzzle_input.splitlines()
        numbers_parts = [line.split(": ")[1] for line in lines]
        answer = sum(
            score(*parse_number_part(numbers_part)) for numbers_part in numbers_parts
        )
        print("answer:", answer)


if __name__ == "__main__":
    main()
