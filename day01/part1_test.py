import unittest
from part1 import get_value


class Part1Test(unittest.TestCase):
    def test_example1(self):
        puzzle_input = "1abc2"
        expected = 12
        result = get_value(puzzle_input)
        self.assertEqual(result, expected, "The result is wrong.")

    def test_example2(self):
        puzzle_input = "pqr3stu8vwx"
        expected = 38
        result = get_value(puzzle_input)
        self.assertEqual(result, expected, "The result is wrong.")

    def test_example3(self):
        puzzle_input = "a1b2c3d4e5f"
        expected = 15
        result = get_value(puzzle_input)
        self.assertEqual(result, expected, "The result is wrong.")

    def test_example4(self):
        puzzle_input = "treb7uchet"
        expected = 77
        result = get_value(puzzle_input)
        self.assertEqual(result, expected, "The result is wrong.")


if __name__ == "__main__":
    unittest.main()
