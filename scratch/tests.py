import unittest
from scratch import solve_part_1
from scratch import solve_part_2


class TestPart1(unittest.TestCase):
    def test_part_1_example_1(self):
        puzzle_input = "1122"
        expected = 3
        result = solve_part_1(puzzle_input)
        self.assertEqual(result, expected, "The result is wrong.")

    def test_part_1_example_2(self):
        puzzle_input = "1111"
        expected = 4
        result = solve_part_1(puzzle_input)
        self.assertEqual(result, expected, "The result is wrong.")

    def test_part_1_example_3(self):
        puzzle_input = "1234"
        expected = 0
        result = solve_part_1(puzzle_input)
        self.assertEqual(result, expected, "The result is wrong.")

    def test_part_1_example_4(self):
        puzzle_input = "91212129"
        expected = 9
        result = solve_part_1(puzzle_input)
        self.assertEqual(result, expected, "The result is wrong.")


class TestPart2(unittest.TestCase):
    def test_part_2_example_1(self):
        puzzle_input = "1212"
        expected = 6
        result = solve_part_2(puzzle_input)
        self.assertEqual(result, expected, "The result is wrong.")

    def test_part_2_example_2(self):
        puzzle_input = "1221"
        expected = 0
        result = solve_part_2(puzzle_input)
        self.assertEqual(result, expected, "The result is wrong.")

    def test_part_2_example_3(self):
        puzzle_input = "123425"
        expected = 4
        result = solve_part_2(puzzle_input)
        self.assertEqual(result, expected, "The result is wrong.")

    def test_part_2_example_4(self):
        puzzle_input = "123123"
        expected = 12
        result = solve_part_2(puzzle_input)
        self.assertEqual(result, expected, "The result is wrong.")

    def test_part_2_example_5(self):
        puzzle_input = "12131415"
        expected = 4
        result = solve_part_2(puzzle_input)
        self.assertEqual(result, expected, "The result is wrong.")


if __name__ == "__main__":
    unittest.main()
