from collections import Counter
from enum import Enum


class HandType(Enum):
    HIGH_CARD = 1
    ONE_PAIR = 2
    TWO_PAIR = 3
    THREE_OF_KIND = 4
    FULL_HOUSE = 5
    FOUR_OF_KIND = 6
    FIVE_OF_KIND = 7


cards = ("A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J")
card_score = {card: score for score, card in enumerate(reversed(cards))}


class Hand:
    cards_str: str
    card_counter: Counter
    bid: int

    def __init__(self, cards_str, bid):
        self.cards_str = cards_str
        self.card_counter = Counter(cards_str)
        self.bid = bid

    def get_type(self):
        non_joker_dict = {
            item[0]: item[1] for item in self.card_counter.items() if item[0] != "J"
        }
        j_count = self.card_counter.get("J", 0)
        counts = sorted(non_joker_dict.values(), reverse=True)

        if j_count == 5 or counts[0] + j_count == 5:
            return HandType.FIVE_OF_KIND
        if counts[0] + j_count == 4:
            return HandType.FOUR_OF_KIND
        if counts[0] + j_count == 3 and len(counts) > 1 and counts[1] == 2:
            return HandType.FULL_HOUSE
        if counts[0] + j_count == 3:
            return HandType.THREE_OF_KIND
        if counts[0] + j_count == 2 and len(counts) > 1 and counts[1] == 2:
            return HandType.TWO_PAIR
        if counts[0] + j_count == 2:
            return HandType.ONE_PAIR
        return HandType.HIGH_CARD

    def __eq__(self, other):
        return self.cards_str == other.cards_str

    def __gt__(self, other):
        self_hand_type = self.get_type()
        other_hand_type = other.get_type()
        if self_hand_type == other_hand_type:
            return self.hand_of_same_type_gt(self.cards_str, other.cards_str)

        return self_hand_type.value > other_hand_type.value

    @staticmethod
    def hand_of_same_type_gt(cards_str_1, cards_str_2):
        for n in range(len(cards_str_1)):
            card1 = cards_str_1[n]
            card2 = cards_str_2[n]
            if card1 == card2:
                continue

            score1 = card_score[card1]
            score2 = card_score[card2]
            return score1 > score2

        return False


def line_to_hand(line):
    cards_str, bid_str = line.split(" ")
    bid = int(bid_str)

    return Hand(cards_str, bid)


def main():
    with open("input.txt", "r") as f:
        puzzle_input = f.read()

    hands = [line_to_hand(line) for line in puzzle_input.splitlines()]
    answer = sum(hand.bid * (n + 1) for n, hand in enumerate(sorted(hands)))
    print("answer", answer)


if __name__ == "__main__":
    main()
