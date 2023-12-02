from dataclasses import dataclass
import math

RED_MAX = 12
GREEN_MAX = 13
BLUE_MAX = 14


@dataclass
class Game:
    id: int
    rounds: list[dict[str, int]]

    def is_game_possible(self) -> bool:
        impossible_rounds = [
            round
            for round in self.rounds
            if round.get("red", 0) > RED_MAX
            or round.get("green", 0) > GREEN_MAX
            or round.get("blue", 0) > BLUE_MAX
        ]

        return len(impossible_rounds) == 0

    def get_game_power(self) -> int:
        """Used in part 2"""

        max_dict = {}

        for round in self.rounds:
            for color, amount in round.items():
                max_dict[color] = max(max_dict.get(color, 0), amount)

        return math.prod(max_dict.values())


def round_str_to_dict(round_str: str) -> dict[str, int]:
    cubes = (cube.split(" ") for cube in round_str.split(", "))

    return {color: int(amount) for amount, color in cubes}


def line_to_game(line: str) -> Game:
    title, sample = line.split(": ")
    id = int(title.split(" ")[1])
    round_strs = sample.split("; ")
    rounds = [round_str_to_dict(round_str) for round_str in round_strs]

    return Game(id=id, rounds=rounds)


def main():
    f = open("input.txt", "r")
    puzzle_input = f.read()

    games = (line_to_game(line) for line in puzzle_input.splitlines())
    possible_games = (game.id for game in games if game.is_game_possible())

    print("answer:", sum(possible_games))


if __name__ == "__main__":
    main()
