import re
from part1 import get_adj_coords
from part1 import safe_row_index
from part1 import num_regex

star_regex = re.compile("\*")


def is_number(string):
    return bool(num_regex.match(string))


def main():
    with open("input.txt", "r") as f:
        puzzle_input = f.read()
        rows = puzzle_input.splitlines()

        total = 0

        for i, row in enumerate(rows):
            for m in star_regex.finditer(row):
                num_start_index = m.start()
                adj_num_cells = []

                for x, y in get_adj_coords(i, num_start_index):
                    cell = safe_row_index(rows, x, y)
                    if cell and is_number(cell):
                        adj_num_cells.append((x, y))

                adj_num_row_indexes = set(x for x, _ in adj_num_cells)
                adj_nums = []

                for adj_num_row_index in adj_num_row_indexes:
                    adj_row = rows[adj_num_row_index]
                    adj_row_adj_num_indexes = [
                        cell[1]
                        for cell in adj_num_cells
                        if cell[0] == adj_num_row_index
                    ]
                    row_adj_nums = [
                        int(m.group())
                        for m in num_regex.finditer(adj_row)
                        if len(
                            [
                                num_index
                                for num_index in adj_row_adj_num_indexes
                                if num_index >= m.start() and num_index < m.end()
                            ]
                        )
                    ]
                    adj_nums.extend(row_adj_nums)

                if len(adj_nums) == 2:
                    total += adj_nums[0] * adj_nums[1]

        print("answer:", total)


if __name__ == "__main__":
    main()
