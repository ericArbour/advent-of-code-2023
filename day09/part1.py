def parse_line(line):
    return [int(num) for num in line.split(" ")]


def get_diffs(history):
    zipped = zip(history, history[1:])
    return [next - num for num, next in zipped]


def extrapolate(history):
    rows = [history]

    while any(rows[-1]):
        diffs = get_diffs(rows[-1])
        rows.append(diffs)

    reverse_rows = rows[::-1]
    for index, row in enumerate(reverse_rows):
        if index == 0:
            continue
        row.append(row[-1] + reverse_rows[index - 1][-1])

    return rows[0][-1]


def main():
    with open("./input.txt") as f:
        puzzle_input = f.read()

    answer = sum(extrapolate(parse_line(line)) for line in puzzle_input.splitlines())
    print("answer:", answer)


if __name__ == "__main__":
    main()
