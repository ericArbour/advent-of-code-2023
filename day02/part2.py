from dataclasses import dataclass
from part1 import line_to_game


def main():
    f = open("input.txt", "r")
    puzzle_input = f.read()

    games = [line_to_game(line) for line in puzzle_input.splitlines()]
    answer = sum(game.get_game_power() for game in games)

    print("answer:", answer)


if __name__ == "__main__":
    main()
