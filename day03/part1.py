import re

num_regex = re.compile(r"\d+")
symbol_regex = re.compile(r"[^.|^\d]")


def is_symbol(string):
    return bool(symbol_regex.match(string))


def get_adj_coords(i, j):
    return (
        (i, j - 1),
        (i - 1, j - 1),
        (i - 1, j),
        (i - 1, j + 1),
        (i, j + 1),
        (i + 1, j + 1),
        (i + 1, j),
        (i + 1, j - 1),
    )


def safe_row_index(rows, x, y):
    try:
        return rows[x][y]
    except IndexError:
        return None


def main():
    with open("input.txt", "r") as f:
        puzzle_input = f.read()
        rows = puzzle_input.splitlines()

        total = 0

        for i, row in enumerate(rows):
            for m in num_regex.finditer(row):
                has_adj_symbol = False
                for j in range(m.start(), m.end()):
                    for x, y in get_adj_coords(i, j):
                        cell = safe_row_index(rows, x, y)
                        if cell and is_symbol(cell):
                            has_adj_symbol = True
                            break

                    if has_adj_symbol:
                        total += int(m.group())
                        break

        print("answer:", total)


if __name__ == "__main__":
    main()
