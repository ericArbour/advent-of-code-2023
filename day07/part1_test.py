import unittest
from part1 import Hand
from part1 import HandType


class Part1Test(unittest.TestCase):
    def test_high_card(self):
        hand = Hand("A234J", 0)
        hand_type = hand.get_type()
        expected = HandType.HIGH_CARD
        self.assertEqual(hand_type, expected, "The result is wrong.")

    def test_one_pair(self):
        hand = Hand("245K2", 0)
        hand_type = hand.get_type()
        expected = HandType.ONE_PAIR
        self.assertEqual(hand_type, expected, "The result is wrong.")

    def test_two_pair(self):
        hand = Hand("3K3K4", 0)
        hand_type = hand.get_type()
        expected = HandType.TWO_PAIR
        self.assertEqual(hand_type, expected, "The result is wrong.")

    def test_three_of_kind(self):
        hand = Hand("Q2Q4Q", 0)
        hand_type = hand.get_type()
        expected = HandType.THREE_OF_KIND
        self.assertEqual(hand_type, expected, "The result is wrong.")

    def test_full_house(self):
        hand = Hand("Q2Q2Q", 0)
        hand_type = hand.get_type()
        expected = HandType.FULL_HOUSE
        self.assertEqual(hand_type, expected, "The result is wrong.")

    def test_four_of_kind(self):
        hand = Hand("J2JJJ", 0)
        hand_type = hand.get_type()
        expected = HandType.FOUR_OF_KIND
        self.assertEqual(hand_type, expected, "The result is wrong.")

    def test_five_of_kind(self):
        hand = Hand("77777", 0)
        hand_type = hand.get_type()
        expected = HandType.FIVE_OF_KIND
        self.assertEqual(hand_type, expected, "The result is wrong.")

    def test_comparison(self):
        hand1 = Hand("77777", 0)
        hand2 = Hand("7777J", 0)

        self.assertEqual(hand1 > hand2, True)
        self.assertEqual(hand1 < hand2, False)
        self.assertEqual(hand1 == hand2, False)

        hand3 = Hand("33322", 0)
        hand4 = Hand("22334", 0)

        self.assertEqual(hand3 > hand4, True)
        self.assertEqual(hand3 < hand4, False)
        self.assertEqual(hand3 == hand4, False)

        hand5 = Hand("KK677", 0)
        hand6 = Hand("KTJJT", 0)

        self.assertEqual(hand5 > hand6, True)
        self.assertEqual(hand5 < hand6, False)
        self.assertEqual(hand5 == hand6, False)


if __name__ == "__main__":
    unittest.main()
