import unittest
from part2 import get_value


class Part2Test(unittest.TestCase):
    def test_example1(self):
        puzzle_input = "two1nine"
        expected = 29
        result = get_value(puzzle_input)
        self.assertEqual(result, expected, "The result is wrong.")

    def test_example2(self):
        puzzle_input = "eightwothree"
        expected = 83
        result = get_value(puzzle_input)
        self.assertEqual(result, expected, "The result is wrong.")

    def test_example3(self):
        puzzle_input = "abcone2threexyz"
        expected = 13
        result = get_value(puzzle_input)
        self.assertEqual(result, expected, "The result is wrong.")

    def test_example4(self):
        puzzle_input = "xtwone3four"
        expected = 24
        result = get_value(puzzle_input)
        self.assertEqual(result, expected, "The result is wrong.")

    def test_example5(self):
        puzzle_input = "4nineeightseven2"
        expected = 42
        result = get_value(puzzle_input)
        self.assertEqual(result, expected, "The result is wrong.")

    def test_example6(self):
        puzzle_input = "zoneight234"
        expected = 14
        result = get_value(puzzle_input)
        self.assertEqual(result, expected, "The result is wrong.")

    def test_example7(self):
        puzzle_input = "7pqrstsixteen"
        expected = 76
        result = get_value(puzzle_input)
        self.assertEqual(result, expected, "The result is wrong.")

    def test_example8(self):
        puzzle_input = "1five72cxh3fivefive"
        expected = 15
        result = get_value(puzzle_input)
        self.assertEqual(result, expected, "The result is wrong.")

    def test_example9(self):
        puzzle_input = "9jdpnzgqrf"
        expected = 99
        result = get_value(puzzle_input)
        self.assertEqual(result, expected, "The result is wrong.")


if __name__ == "__main__":
    unittest.main()
