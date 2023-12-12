def safe_row_index(matrix, i, j):
    try:
        return matrix[i][j]
    except IndexError:
        return None


def get_neighbors(matrix, pos):
    i, j = pos
    symbol = matrix[i][j]
    left = (i, j - 1)
    up = (i - 1, j)
    right = (i, j + 1)
    down = (i + 1, j)

    pipe_rule_map = {
        "|": (up, down),
        "-": (left, right),
        "L": (up, right),
        "J": (up, left),
        "7": (down, left),
        "F": (down, right),
        "S": (left, up, right, down),
        ".": tuple(),
    }

    return pipe_rule_map[symbol]


def get_connection(matrix, current_pos, last_pos):
    print("current_pos:", current_pos, " - last_pos:", last_pos)

    neighbors = get_neighbors(matrix, current_pos)
    for neighbor in neighbors:
        if neighbor == last_pos:
            continue
        neighbor_neighbors = get_neighbors(matrix, neighbor)
        if current_pos in neighbor_neighbors:
            return neighbor


def get_starting_pos(matrix):
    for i, row in enumerate(matrix):
        for y, char in enumerate(row):
            if char == "S":
                return i, y


def main():
    with open("input.txt") as f:
        puzzle_input = f.read()

    matrix = [[char for char in line] for line in puzzle_input.splitlines()]
    step_count = 0
    last_pos = None
    current_pos = get_starting_pos(matrix)
    current_symbol = None
    while current_symbol != "S":
        print(current_symbol)
        next_pos = get_connection(matrix, current_pos, last_pos)
        last_pos = current_pos
        current_pos = next_pos
        current_symbol = matrix[current_pos[0]][current_pos[1]]
        step_count += 1

    print(step_count // 2)


if __name__ == "__main__":
    main()
