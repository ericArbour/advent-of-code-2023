import re

num_regex = re.compile(r"\d+")


def parse_numbers_part(numbers_part):
    winners_strs, held_numbers_str = numbers_part.split(" | ")
    winners = num_regex.findall(winners_strs)
    held_numbers = num_regex.findall(held_numbers_str)
    return set(winners), held_numbers


def count_held_winners(winners, held_numbers):
    held_winners = [
        held_number for held_number in held_numbers if held_number in winners
    ]
    return len(held_winners)


def parse_puzzle_line(line):
    card_part, numbers_part = line.split(": ")
    card_num = int(num_regex.search(card_part).group())
    winner_count = count_held_winners(*parse_numbers_part(numbers_part))
    next_card = card_num + 1
    rewarded_cards = list(range(next_card, next_card + winner_count))
    return (card_num, rewarded_cards)


def solve(card_nums, result_map, cache):
    if len(card_nums) == 0:
        return 0

    total = 0
    for card_num in card_nums:
        if card_num in cache:
            total += cache[card_num]
            continue

        score = 1 + solve(result_map[card_num], result_map, cache)
        total += score
        cache[card_num] = score

    return total


def main() -> None:
    with open("input.txt", "r") as f:
        puzzle_input = f.read()
        lines = puzzle_input.splitlines()
        result_map = dict(parse_puzzle_line(line) for line in lines)
        initial_card_nums = list(result_map.keys())

        answer = solve(initial_card_nums, result_map, {})

        print("answer:", answer)


if __name__ == "__main__":
    main()
